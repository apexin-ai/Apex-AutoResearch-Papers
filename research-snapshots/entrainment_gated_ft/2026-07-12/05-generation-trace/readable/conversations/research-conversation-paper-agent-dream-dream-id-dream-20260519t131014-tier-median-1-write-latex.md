# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260519T131014 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-3/c013dfff-9ae5-416a-b5ae-03fba6a5fd1c.jsonl`
- **Structured JSON:** [`c897919a6cc84c732780.json`](../../sessions/c8/c897919a6cc84c732780.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T13:33:21.244Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T13:33:21.244Z",
  "sessionId": "c013dfff-9ae5-416a-b5ae-03fba6a5fd1c",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260519T131014 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/dream_reports/dream_20260519T131014/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/dream_reports/dream_20260519T131014/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/dream_reports/dream_20260519T131014/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/dream_reports/dream_20260519T131014/median/experiment_data.json`（先 Read 此文件）\n- Venue：emnlp-2026\n- Narrative guidance：Claim 1 从 \"task-specificity as continuous spectrum\" 降级为 \"retrieval-intensive tasks show convergence; generality remains open\"。 Claim 2 保持 binary contrast framing 但明确标注 scale-vs-tokens confound。 Claim 3 equalizer paradox 成立但 mechanistic depth 从 \"causal mechanism\" 降为 \"suggestive mechanistic evidence\"。 标题: \"Aggregate Convergence, Per-Example Divergence: How Attention Reshapes Hybrid Recurrent Architectures on Retrieval Tasks\"。 主投 Findings，reviewer 积极可争取 Main。需补充 limitations 段落诚实讨论 n=3 和单任务问题。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/dream_reports/dream_20260519T131014/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-19T13:33:21.247Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T13:33:21.247Z",
  "sessionId": "c013dfff-9ae5-416a-b5ae-03fba6a5fd1c"
}
```

---

## Round 1

27 recorded events

### User

_source line 3 · 2026-05-19T13:33:21.268Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260519T131014 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/dream_reports/dream_20260519T131014/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/dream_reports/dream_20260519T131014/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/dream_reports/dream_20260519T131014/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/dream_reports/dream_20260519T131014/median/experiment_data.json`（先 Read 此文件）
- Venue：emnlp-2026
- Narrative guidance：Claim 1 从 "task-specificity as continuous spectrum" 降级为 "retrieval-intensive tasks show convergence; generality remains open"。 Claim 2 保持 binary contrast framing 但明确标注 scale-vs-tokens confound。 Claim 3 equalizer paradox 成立但 mechanistic depth 从 "causal mechanism" 降为 "suggestive mechanistic evidence"。 标题: "Aggregate Convergence, Per-Example Divergence: How Attention Reshapes Hybrid Recurrent Architectures on Retrieval Tasks"。 主投 Findings，reviewer 积极可争取 Main。需补充 limitations 段落诚实讨论 n=3 和单任务问题。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/dream_reports/dream_20260519T131014/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "1470b571-8e3c-450f-9a8f-7768e6cda7c5",
  "type": "user",
  "uuid": "ec83f530-e2ba-44d9-b446-5ae539484d74",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "c013dfff-9ae5-416a-b5ae-03fba6a5fd1c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T13:33:21.267Z_

```json
{
  "parentUuid": "ec83f530-e2ba-44d9-b446-5ae539484d74",
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
  "uuid": "86178e44-b10e-491e-846f-36f091692f46",
  "timestamp": "2026-05-19T13:33:21.267Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "c013dfff-9ae5-416a-b5ae-03fba6a5fd1c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T13:33:21.267Z_

```json
{
  "parentUuid": "86178e44-b10e-491e-846f-36f091692f46",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e4c8232d-d8d1-4e36-ac50-e70432a5bb11",
  "timestamp": "2026-05-19T13:33:21.267Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "c013dfff-9ae5-416a-b5ae-03fba6a5fd1c",
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
  "aiTitle": "Generate simulated paper with experiment data",
  "sessionId": "c013dfff-9ae5-416a-b5ae-03fba6a5fd1c"
}
```

---

### Assistant

_source line 7 · 2026-05-19T13:33:23.955Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4c8232d-d8d1-4e36-ac50-e70432a5bb11",
  "isSidechain": false,
  "requestId": "req_011CbC1hsWy2JCmHXbTgpTPS",
  "type": "assistant",
  "uuid": "4d33a64e-9ef9-4e12-8d54-ee6af7358f2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "c013dfff-9ae5-416a-b5ae-03fba6a5fd1c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01165E9FWEmERFEti91zg8vA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11722,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11722,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11722,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11722
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

_source line 8 · 2026-05-19T13:33:24.494Z_

<details open><summary>🔧 Tool call — Read · `toolu_013KZhePepNyviduWmewACdR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/dream_reports/dream_20260519T131014/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d33a64e-9ef9-4e12-8d54-ee6af7358f2a",
  "isSidechain": false,
  "requestId": "req_011CbC1hsWy2JCmHXbTgpTPS",
  "type": "assistant",
  "uuid": "5515cd5b-f6ed-414b-96ff-f1869c7d1c8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "c013dfff-9ae5-416a-b5ae-03fba6a5fd1c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01165E9FWEmERFEti91zg8vA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11722,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11722,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11722,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11722
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

_source line 9 · 2026-05-19T13:33:24.795Z_

<details><summary>↩ Tool result · `toolu_013KZhePepNyviduWmewACdR`</summary>

```text
1	[
2	  {
3	    "name": "Task-specificity characterization of equalizer effect",
4	    "description": "对 6 个 benchmark 在 1.3B 规模下计算 cross-architecture std trajectory (attention ratio 0→24)， 拟合 Spearman ρ(std vs attention_ratio)，建立 convergence strength 与 retrieval demand 的连续关系。\n",
5	    "results": {
6	      "lambada_rho": -1.0,
7	      "lambada_perm_p": 0.0083,
8	      "lambada_std_baseline": 0.024,
9	      "lambada_std_best": 0.005,
10	      "lambada_std_reduction_pct": 79,
11	      "arc_easy_rho": -0.6,
12	      "arc_easy_perm_p": 0.142,
13	      "arc_challenge_rho": -0.3,
14	      "arc_challenge_perm_p": 0.383,
15	      "hellaswag_rho": 0.1,
16	      "hellaswag_perm_p": 0.872,
17	      "winogrande_rho": -0.2,
18	      "winogrande_perm_p": 0.544,
19	      "mmlu_rho": 0.0,
20	      "mmlu_perm_p": 0.983,
21	      "benchmarks_with_rho_below_neg05": 1,
22	      "benchmarks_with_suggestive_rho": 1
23	    },
24	    "tables": [
25	      {
26	        "table_id": "T1",
27	        "caption": "Cross-architecture convergence strength by benchmark (1.3B scale)",
28	        "columns": [
29	          "Benchmark",
30	          "Retrieval Demand (qualitative)",
31	          "Baseline Std (attn=0)",
32	          "Best Std",
33	          "Spearman ρ",
34	          "Exact Perm. p"
35	        ],
36	        "rows": [
37	          [
38	            "LAMBADA",
39	            "High (last-word retrieval)",
40	            "0.024",
41	            "0.005",
42	            "-1.00",
43	            "0.008**"
44	          ],
45	          [
46	            "ARC-Easy",
47	            "Medium (knowledge retrieval)",
48	            "0.018",
49	            "0.011",
50	            "-0.60",
51	            "0.142"
52	          ],
53	          [
54	            "ARC-Challenge",
55	            "Medium-Low",
56	            "0.022",
57	            "0.017",
58	            "-0.30",
59	            "0.383"
60	          ],
61	          [
62	            "WinoGrande",
63	            "Low-Medium (coref)",
64	            "0.015",
65	            "0.013",
66	            "-0.20",
67	            "0.544"
68	          ],
69	          [
70	            "HellaSwag",
71	            "Low (commonsense reasoning)",
72	            "0.012",
73	            "0.013",
74	            "0.10",
75	            "0.872"
76	          ],
77	          [
78	            "MMLU",
79	            "Low (knowledge + reasoning)",
80	            "0.031",
81	            "0.030",
82	            "0.00",
83	            "0.983"
84	          ]
85	        ]
86	      }
87	    ],
88	    "figures": [],
89	    "analysis": "Median 档下 continuous spectrum 论证不成立——只有 LAMBADA 显著、ARC-Easy suggestive， 其余 4 个 benchmark ρ 值在 [-0.3, 0.1] 噪声区间。 Paper 必须将 Claim 1 scope 限缩为 retrieval-intensive task convergence， 而非 general task-type modulation。 Post-hoc taxonomy 风险依然存在：只有一个 \"high retrieval\" benchmark 显著， reviewer 可质疑分类本身是为 fit data 设计的。 Mitigation: 引用 BIG-bench 已有 taxonomy 而非自建，并在 limitations 中诚实标注。\n\n\nMedian 档的核心特征是 LAMBADA 显著但其余 benchmark 未跨越 significance threshold。 LAMBADA 作为纯 last-word retrieval 任务，其 ρ=-1.0 完美单调关系在此档位保持不变——这是整篇论文的锚点。 ARC-Easy ρ=-0.6 处于指标范围 [-0.7, -0.4] 中段，p=0.142 不显著（n=5 attention ratios 统计功效太低）， 但方向一致，可作为 suggestive evidence。ARC-Challenge 更弱因其推理成分更重。 HellaSwag/WinoGrande/MMLU 因 reasoning-dominant 性质，convergence 接近零或为噪声。 这意味着 continuous spectrum 叙事只有两个正方向数据点（LAMBADA 显著 + ARC-E suggestive）， 不足以声称 dose-response，只能说 \"retrieval-intensive tasks show convergence, generality remains open\"。\n"
90	  },
91	  {
92	    "name": "Multi-benchmark per-example analysis",
93	    "description": "对 1.3B 和 340M 模型使用 --log_samples 重新运行 lm-eval， 收集 HellaSwag、ARC-Easy、ARC-Challenge 的 per-example logprob 数据。 计算 per-example delta (hybrid - pure) 并分析是否存在 per-example convergence pattern。\n",
94	    "results": {
95	      "hellaswag_per_example_convergence_detected": false,
96	      "hellaswag_per_example_pattern": "no systematic pattern — deltas approximately i.i.d. across architectures",
97	      "hellaswag_cross_arch_delta_correlation_mean": 0.03,
98	      "arc_easy_per_example_rho_with_attention": -0.5,
99	      "arc_easy_per_example_signal": "ambiguous",
100	      "arc_easy_jaccard_pairwise_helped": 0.12,
101	      "arc_challenge_per_example_convergence_detected": false,
102	      "arc_challenge_cross_arch_delta_correlation_mean": -0.05,
103	      "models_requiring_rerun_340m": 10,
104	      "models_requiring_rerun_1_3b": 3,
105	      "total_gpu_hours_used": 18
106	    },
107	    "tables": [
108	      {
109	        "table_id": "T2",
110	        "caption": "Per-example convergence indicators across benchmarks (1.3B, h24-1 vs h0)",
111	        "columns": [
112	          "Benchmark",
113	          "Mean |Δ logprob|",
114	          "Cross-arch Δ corr.",
115	          "Jaccard (helped)",
116	          "Per-ex convergence?"
117	        ],
118	        "rows": [
119	          [
120	            "LAMBADA",
121	            "0.34",
122	            "0.08",
123	            "0.07",
124	            "Yes (strong)"
125	          ],
126	          [
127	            "ARC-Easy",
128	            "0.12",
129	            "0.18",
130	            "0.12",
131	            "Ambiguous"
132	          ],
133	          [
134	            "ARC-Challenge",
135	            "0.09",
136	            "-0.05",
137	            "0.15",
138	            "No"
139	          ],
140	          [
141	            "HellaSwag",
142	            "0.06",
143	            "0.03",
144	            "0.22",
145	            "No"
146	          ]
147	        ]
148	      }
149	    ],
150	    "figures": [],
151	    "analysis": "HellaSwag per-example 确认非收敛是关键正面结果——从 \"aggregate ρ 不显著\" 升级为 \"per-example 分析确认 attention 对 reasoning task 无系统性影响\"， 堵住了 reviewer \"也许 aggregate 不显著只是 power 不足\" 的攻击路线。 ARC-Easy 的模糊信号是 median 档的标志——它既不能用来扩展 Claim 1 到第二个 task， 也不能被忽略（ρ=-0.5 毕竟有方向性）。 Paper 中应呈现为 \"suggestive but inconclusive at current sample size\"。\n\n\nMedian 档的定义要求 HellaSwag per-example 确认非收敛（好，升级 Claim 1 的 \"non-converging\" 证据）， 但 ARC-Easy per-example 信号模糊。HellaSwag 上 per-example delta 与 architecture identity 无相关， 说明 attention 对 reasoning task 的影响是随机散射的——这正面支持了 \"convergence is retrieval-specific\" 叙事。 ARC-Easy 的 ρ=-0.5 处于中间地带：有方向性但 Jaccard=0.12 说明 helped/hurt 子集有少量重叠， 不像 LAMBADA 那样有清晰的 architecture-specific 分化。 这使得 ARC-Easy 成为一个 ambiguous data point——不能用来支持也不能用来否定 convergence。\n"
152	  },
153	  {
154	    "name": "Helped/hurt sample characterization",
155	    "description": "对 LAMBADA 上每个 architecture 的 helped/hurt sample 子集， 计算 target token frequency、context length、last-sentence perplexity、domain 分布， 测试这些 feature 是否显著区分 helped vs hurt 以及是否跨架构不同。\n",
156	    "results": {
157	      "significant_features_count": 1,
158	      "target_token_frequency_p_gdn": 0.003,
159	      "target_token_frequency_p_retnet": 0.008,
160	      "target_token_frequency_p_hgrn2": 0.022,
161	      "target_token_frequency_effect_direction": "attention helps rare tokens more",
162	      "context_length_p_gdn": 0.087,
163	      "context_length_p_retnet": 0.134,
164	      "context_length_p_hgrn2": 0.062,
165	      "last_sentence_perplexity_p_gdn": 0.214,
166	      "domain_distribution_chi2_p": 0.341,
167	      "cross_arch_feature_profile_differs": "partially",
168	      "jaccard_pairwise_mean": 0.08,
169	      "sample_feature_best_p": 0.003
170	    },
171	    "tables": [
172	      {
173	        "table_id": "T3",
174	        "caption": "Feature comparison between helped and hurt samples per architecture (LAMBADA, 1.3B h24-1 vs h0)",
175	        "columns": [
176	          "Feature",
177	          "GDN (p)",
178	          "GDN (d)",
179	          "RetNet (p)",
180	          "RetNet (d)",
181	          "HGRN2 (p)",
182	          "HGRN2 (d)"
183	        ],
184	        "rows": [
185	          [
186	            "Target token freq (log rank)",
187	            "0.003**",
188	            "-0.41",
189	            "0.008**",
190	            "-0.33",
191	            "0.022*",
192	            "-0.24"
193	          ],
194	          [
195	            "Context length",
196	            "0.087",
197	            "0.19",
198	            "0.134",
199	            "0.15",
200	            "0.062",
201	            "0.22"
202	          ],
203	          [
204	            "Last-sent. perplexity",
205	            "0.214",
206	            "0.12",
207	            "0.378",
208	            "0.08",
209	            "0.156",
210	            "0.14"
211	          ],
212	          [
213	            "Domain entropy (H)",
214	            "0.341",
215	            "—",
216	            "0.287",
217	            "—",
218	            "0.512",
219	            "—"
220	          ]
221	        ]
222	      }
223	    ],
224	    "figures": [],
225	    "analysis": "只有 target token frequency 一个 feature 在 p<0.01 水平显著且三架构一致， 但 effect size 从 GDN d=0.41 到 HGRN2 d=0.24 递减。 这足以写一段有说服力的 mechanistic story (\"attention enables rare token retrieval that recurrence alone cannot achieve\")，但不足以完整解释 architecture-specific 差异。 为什么 GDN 被 hurt 的 sample 和 RetNet 被 hurt 的 sample 几乎不重叠 (Jaccard=0.06) 仍然缺乏 feature-level 解释。 Paper 应当诚实地说 \"token frequency partially explains the mechanism; the architecture-specificity of affected subsets remains only partially characterized\"。\n\n\nMedian 档要求 \"1 个 feature 显著区分 (p<0.01) 但跨架构差异不够鲜明\"。 Target token frequency 是最有物理意义的 feature——attention 层的全局 context access 天然有利于 rare token retrieval，三个架构都显示这一方向，但 effect size 不同 (GDN 最强，HGRN2 最弱，因为 HGRN2 的 hierarchical gating 本身就部分覆盖了 rare token)。 Context length 在三个架构上都接近 but 不跨越 p<0.05，说明 attention 对长 context 有帮助 但不是主要分化因素。Perplexity 和 domain 不显著——这些是 confound 而非 mechanism。 跨架构差异 \"partially\" 因为 token frequency 方向一致但 magnitude 不同， 不像 LAMBADA Jaccard<0.10 那样的鲜明分化，削弱了 \"completely different mechanisms\" 叙事。\n"
226	  },
227	  {
228	    "name": "Attention weight extraction and visualization",
229	    "description": "从三个架构的 h3-1 配置中提取 attention weight matrix， 分析 attention pattern 与 helped/hurt sample identity 的相关性， 以及跨架构 attention pattern 相似度。\n",
230	    "results": {
231	      "attention_pattern_correlation_with_helped_hurt_gdn": 0.31,
232	      "attention_pattern_correlation_with_helped_hurt_retnet": 0.24,
233	      "attention_pattern_correlation_with_helped_hurt_hgrn2": 0.37,
234	      "attention_per_example_correlation_mean": 0.31,
235	      "cross_arch_attention_similarity_cosine_mean": 0.42,
236	      "attention_focus_pattern_gdn": "dispersed across mid-context positions",
237	      "attention_focus_pattern_retnet": "concentrated on recent + first positions (primacy-recency)",
238	      "attention_focus_pattern_hgrn2": "focused on semantically related positions",
239	      "qualitative_finding": "attention layers develop architecture-conditioned patterns",
240	      "gpu_hours_used": 3.5
241	    },
242	    "tables": [
243	      {
244	        "table_id": "T4",
245	        "caption": "Attention pattern analysis for h3-1 models on LAMBADA (1.3B)",
246	        "columns": [
247	          "Architecture",
248	          "Attn-Helped/Hurt Corr.",
249	          "Dominant Pattern",
250	          "Cross-arch Cosine Sim."
251	        ],
252	        "rows": [
253	          [
254	            "GDN",
255	            "0.31",
256	            "Dispersed mid-context",
257	            "— / 0.38 / 0.44"
258	          ],
259	          [
260	            "RetNet",
261	            "0.24",
262	            "Primacy-recency",
263	            "0.38 / — / 0.45"
264	          ],
265	          [
266	            "HGRN2",
267	            "0.37",
268	            "Semantic focus",
269	            "0.44 / 0.45 / —"
270	          ]
271	        ]
272	      }
273	    ],
274	    "figures": [],
275	    "analysis": "Correlation 0.2-0.4 足以说明 \"attention patterns are related to per-example effects\" 但不足以说明 \"attention patterns explain per-example effects\"。 这是 median 档标志性的 gap——方向正确，magnitude 不够支撑 causal claim。 Paper 必须用 \"suggestive mechanistic evidence\" 而非 \"causal mechanism\"， 并在 discussion 中承认 recurrence 状态变化可能是 complementary mechanism 但无法观测。 Qualitative attention pattern 差异（dispersed vs primacy-recency vs semantic） 可以作为有吸引力的 figure 但不能作为定量论证的主体。\n\n\nMedian 档要求 attention-per-example correlation 在 0.2-0.4 范围内，方向正确但不足以独立支撑机制论证。 均值 0.31 说明 attention pattern 与 helped/hurt 有可检测但中等的关联—— 比随机强（排除 null hypothesis）但远不够作为 causal mechanism 的证据。 跨架构 attention cosine similarity 0.42 说明 attention 层在不同 recurrence backbone 上 发展出部分不同的 pattern，与 Jaccard<0.10 的 per-example 分化方向一致， 但相似度高于预期（可能因为 LAMBADA 任务本身的 inductive bias 限制了 attention 的自由度）。 三个架构的 attention 定性 pattern 不同，支持 \"architecture-conditioned attention\" 叙事， 但定量相关性只有 0.2-0.4 意味着 attention pattern 不是唯一的 mechanism—— recurrence 状态本身的改变也参与其中，但我们无法直接观测。\n"
276	  },
277	  {
278	    "name": "Architecture expansion check",
279	    "description": "搜索 Wang et al. model zoo 和公开来源，寻找额外的 hybrid linear recurrent architectures (Mamba/Mamba2 hybrid, RWKV hybrid 等)。如果找到则在 LAMBADA 上评估 convergence。\n",
280	    "results": {
281	      "additional_architectures_found": 0,
282	      "wang_et_al_zoo_exhausted": true,
283	      "mamba_hybrid_public": false,
284	      "rwkv_hybrid_public": false,
285	      "other_hybrid_candidates_checked": [
286	        "Mamba-2 hybrid (not in zoo)",
287	        "RWKV-6 hybrid (no public checkpoint)",
288	        "Griffin (Google, not released)"
289	      ],
290	      "architectures_tested_final": 3
291	    },
292	    "tables": [],
293	    "figures": [],
294	    "analysis": "n=3 是不可改变的硬约束。Paper 的 mitigation 策略： (1) 强调这三种架构代表三种不同的 recurrence mechanism (gated delta rule, linear attention + exp decay, hierarchical gating)， 不是三个随机选择； (2) per-example analysis 提供了每个 architecture × 5 ratios × ~5000 samples 的数据点， 统计上远超 n=3 的印象； (3) 在 limitations 中明确声明 generalization to other recurrence families is an open question。 Reviewer 攻击面: \"n=3 insufficient for general claims\" 是预期中的最常见 weakness comment， Findings 档可以生存，Main 档可能被此点 reject。\n\n\nMedian 档明确指出 \"无额外架构可用（Wang et al. zoo 已穷尽）\"，architectures_tested 固定为 3。 Wang et al. 的 72 个模型覆盖了 GDN、RetNet、HGRN2 三种架构在 2 个 scale × 多个 attention ratio 的组合， 已经是公开可用的最完整 hybrid recurrent model zoo。 Mamba-2 hybrid 和 RWKV hybrid 虽然在文献中被讨论但没有公开 checkpoint。 Griffin (Google) 有公开论文但模型权重未发布。 这意味着 n=3 limitation 无法在本论文中解决，必须在 limitations 中明确讨论 并将其定位为 future work。\n"
295	  },
296	  {
297	    "name": "340M rebound mechanism analysis",
298	    "description": "深入分析 340M 在 attn=8 处的 non-monotonic rebound。 与 1.3B 同 attention ratio 的 per-example 数据对比， 识别哪些 sample 在 340M 发生 diverge，并分析 training token count confound。\n",
299	    "results": {
300	      "rebound_magnitude_340m_attn8_std_increase_pct": 35,
301	      "rebound_samples_overlap_with_1_3b_helped": 0.28,
302	      "rebound_explanation_partial": true,
303	      "capacity_hypothesis_supported": true,
304	      "training_tokens_confound_separable": false,
305	      "training_tokens_340m": "20B",
306	      "training_tokens_1_3b": "100B",
307	      "rebound_sample_characteristics": "predominantly long-context (>80 tokens) with rare target tokens",
308	      "scale_vs_tokens_confound_severity": "moderate — cannot fully decouple"
309	    },
310	    "tables": [
311	      {
312	        "table_id": "T5",
313	        "caption": "340M rebound analysis: per-example comparison at attn=8",
314	        "columns": [
315	          "Metric",
316	          "340M",
317	          "1.3B",
318	          "Interpretation"
319	        ],
320	        "rows": [
321	          [
322	            "Cross-arch std at attn=8",
323	            "0.019 (↑35% from attn=6)",
324	            "0.008 (↓ monotonic)",
325	            "Rebound only at 340M"
326	          ],
327	          [
328	            "Rebound samples: mean context length",
329	            "94.2 tokens",
330	            "N/A (no rebound)",
331	            "Long-context samples most affected"
332	          ],
333	          [
334	            "Rebound samples: mean target freq rank",
335	            "8,420",
336	            "N/A",
337	            "Rare tokens disproportionately affected"
338	          ],
339	          [
340	            "Overlap: rebound↔1.3B helped",
341	            "Jaccard=0.28",
342	            "—",
343	            "Moderate overlap: same hard samples"
344	          ],
345	          [
346	            "Training tokens",
347	            "20B",
348	            "100B",
349	            "5× difference, confounded with scale"
350	          ]
351	        ]
352	      }
353	    ],
354	    "figures": [],
355	    "analysis": "Rebound 机制的 partial explanation 足以支撑 Claim 2 的 \"scale matters\" binary contrast， 但 training-token confound 削弱了 mechanistic clarity。 Reviewer 可以合理地问 \"如果 340M 也训练 100B tokens 会怎样？\"——我们无法回答因为没有这个 ablation。 Paper 策略：(1) 承认 confound，(2) 用 capacity argument (attention 层在小模型中与 recurrence 层 compete for capacity) 作为 primary explanation 因为它有 per-example evidence 支持（long-context rare-token samples 受影响最大）， (3) 明确标注 training-token 量的差异为 limitation。 这在 Findings 档是可接受的诚实度——reviewer 不会因为你承认了 confound 而 reject， 但会因为你假装 confound 不存在而 reject。\n\n\nMedian 档要求 \"340M rebound 有 partial 解释，但 scale vs training-tokens confound 无法完全解耦\"。 Rebound 在 attn=8 发生是因为 340M 模型容量不足以同时维持 recurrence quality 和 attention quality—— 当 attention 层数过多时，recurrence 层被过度压缩导致 baseline capability 下降。 这在长 context + rare token 的 sample 上最明显（这些 sample 需要 recurrence 和 attention 协同工作）。 但 1.3B 模型不仅 scale 更大，training token 也是 5x (100B vs 20B)， 无法区分是 \"更大的模型容量允许 attention 和 recurrence 共存\" 还是 \"更多 training 让模型学会了更好的分工\"。 Paper 必须将此标注为 acknowledged confound，用 \"scale and/or training duration\" 的措辞， 而非单纯归因于 scale。\n"
356	  },
357	  {
358	    "name": "Statistical robustness framework",
359	    "description": "对 convergence metrics 实施 bootstrap CI、Bonferroni/FDR 多重比较校正、 GDN 排除敏感性分析、effect size 报告。\n",
360	    "results": {
361	      "lambada_std_reduction_bootstrap_ci_95_pct": [
362	        58,
363	        72
364	      ],
365	      "lambada_rho_bootstrap_ci_95": [
366	        -1.0,
367	        -0.8
368	      ],
369	      "lambada_rho_bootstrap_ci_width": 0.2,
370	      "arc_easy_rho_bootstrap_ci_95": [
371	        -0.9,
372	        -0.2
373	      ],
374	      "bonferroni_corrected_significant_benchmarks": 1,
375	      "fdr_corrected_significant_benchmarks": 1,
376	      "gdn_excluded_claim1_survives": true,
377	      "gdn_excluded_claim3_survives": true,
378	      "gdn_excluded_claims_surviving": 2,
379	      "gdn_excluded_effect_size_reduction_pct": 35,
380	      "gdn_excluded_lambada_std_reduction_pct": 52,
381	      "gdn_excluded_rho": -0.9,
382	      "cohens_d_lambada_convergence": 1.12,
383	      "cohens_d_lambada_convergence_no_gdn": 0.73,
384	      "eta_squared_attention_effect": 0.34,
385	      "bootstrap_ci_crosses_zero": false
386	    },
387	    "tables": [
388	      {
389	        "table_id": "T6",
390	        "caption": "Bootstrap confidence intervals and sensitivity analysis",
391	        "columns": [
392	          "Metric",
393	          "Full (3 arch)",
394	          "95% CI",
395	          "Excl. GDN (2 arch)",
396	          "95% CI",
397	          "Δ%"
398	        ],
399	        "rows": [
400	          [
401	            "LAMBADA std reduction (%)",
402	            "79",
403	            "[58, 72]",
404	            "52",
405	            "[38, 61]",
406	            "-34"
407	          ],
408	          [
409	            "LAMBADA Spearman ρ",
410	            "-1.00",
411	            "[-1.0, -0.80]",
412	            "-0.90",
413	            "[-1.0, -0.60]",
414	            "—"
415	          ],
416	          [
417	            "Cohen's d (convergence)",
418	            "1.12",
419	            "[0.74, 1.48]",
420	            "0.73",
421	            "[0.41, 1.05]",
422	            "-35"
423	          ],
424	          [
425	            "Pairwise Jaccard (mean)",
426	            "0.08",
427	            "[0.05, 0.12]",
428	            "0.06",
429	            "[0.03, 0.10]",
430	            "-25"
431	          ],
432	          [
433	            "Claims surviving (of 3)",
434	            "3",
435	            "—",
436	            "2",
437	            "—",
438	            "—"
439	          ]
440	        ]
441	      }
442	    ],
443	    "figures": [],
444	    "analysis": "Statistical robustness 结果是 median 档的定义性特征：核心发现 survive 但 weakened。 Effect size 缩小 30-40% 意味着 GDN 贡献了不成比例的 signal—— 这本身是一个 interpretable finding (GDN 的 gated delta rule 可能对 attention 最 responsive)， 但也是一个 vulnerability (如果 reviewer 质疑 GDN 的 D004 data quality)。 Bootstrap CI 不跨零是底线——保证了 \"convergence exists\" 不是 statistical artifact。 Paper 应在 main text 报告 full 结果，在 appendix 报告 GDN-excluded sensitivity analysis， 并在 limitations 中讨论 GDN 依赖性。\n\n\nMedian 档要求 bootstrap CI 较宽但不跨零，排除 GDN 后 Claim 1/3 成立但 effect size 缩小 30-40%。 LAMBADA std reduction 的 bootstrap CI [58%, 72%] 反映了 n=5 attention ratios × n=3 architectures 带来的采样不确定性——79% 的点估计在 CI 上界附近，中位估计约 65%。 排除 GDN 后 reduction 从 79% 降至 52% (缩小 34%) 因为 GDN 的 D004 配置贡献了最大的 convergence signal。 但 52% 仍然 substantial (Cohen's d 从 1.12 降至 0.73，中等到大效应)。 ρ 从 -1.0 降至 -0.90 说明两架构也有很强的 monotonic convergence 但不再完美。 Bonferroni 校正后只有 LAMBADA 显著是必然结果——6 个 benchmark 中只有 1 个 p<0.05， 校正后 threshold 变为 0.0083，只有 LAMBADA 原始 p 勉强通过。 Claims 2/3 排除 GDN 后: Claim 2 中 340M vs 1.3B contrast 在两架构上仍成立; Claim 3 中 Jaccard 在 RetNet-HGRN2 对上仍 <0.10，但只有一个 pair 不如三个 pair 的说服力强。 第三个 claim (claims_surviving = 2 而非 3) 反映 Claim 2 或 Claim 3 在排除 GDN 后 某一个变得 marginal——此处是 Claim 2 因为 340M rebound 的 mechanistic analysis 重度依赖 GDN 数据。\n"
445	  },
446	  {
447	    "name": "Wang et al. explicit differentiation",
448	    "description": "系统性地对比 Wang et al. (arXiv 2507.06457) 的分析与本文的分析， 提取他们关于 convergence 的确切表述，量化本文的增量贡献。\n",
449	    "results": {
450	      "wang_convergence_statements_found": 3,
451	      "wang_convergence_quantitative": false,
452	      "wang_per_example_analysis": false,
453	      "wang_scale_dependent_convergence": false,
454	      "wang_mechanistic_analysis": false,
455	      "differentiation_points": 4,
456	      "wang_relevant_quotes": [
457	        "performance differences between architectures decrease as the attention ratio increases",
458	        "models with higher attention ratios tend to perform more similarly",
459	        "the choice of recurrence mechanism becomes less important at higher attention ratios"
460	      ],
461	      "our_additions": [
462	        "Quantitative convergence framework (Spearman ρ, cross-arch std trajectory, bootstrap CI)",
463	        "Per-example mechanism analysis revealing architecture-specific sample subsets (Jaccard < 0.10)",
464	        "Scale-dependent convergence characterization (340M partial vs 1.3B complete)",
465	        "Sample feature characterization linking convergence to token frequency"
466	      ]
467	    },
468	    "tables": [
469	      {
470	        "table_id": "T7",
471	        "caption": "Explicit differentiation from Wang et al. (2025)",
472	        "columns": [
473	          "Analysis Dimension",
474	          "Wang et al.",
475	          "This Work"
476	        ],
477	        "rows": [
478	          [
479	            "Convergence observation",
480	            "Qualitative ('tend to perform similarly')",
481	            "Quantitative (ρ, std trajectory, CI)"
482	          ],
483	          [
484	            "Per-example analysis",
485	            "Not performed",
486	            "Full per-example logprob analysis, Jaccard, helped/hurt"
487	          ],
488	          [
489	            "Scale dependency",
490	            "Not characterized",
491	            "Binary contrast: 340M partial vs 1.3B complete"
492	          ],
493	          [
494	            "Mechanistic analysis",
495	            "Not performed",
496	            "Sample feature characterization, attention pattern analysis"
497	          ]
498	        ]
499	      }
500	    ],
501	    "figures": [],
502	    "analysis": "4-point differentiation 在 Findings 档足够有说服力—— \"quantitative framework atop qualitative observation\" 是经典的 analysis paper contribution pattern。 Paper introduction 应在致谢 Wang et al. model zoo 的同时明确标注 \"they report X qualitatively; we provide the first quantitative characterization revealing Y\"。 避免任何暗示 Wang et al. 遗漏了什么 \"obvious\" 分析——他们的 paper 目标不同， convergence 对他们是 side observation 而非 research question。\n\n\nWang et al. 在 72-model zoo 的 aggregate 结果讨论中定性地提到了 convergence， 但他们的目标是 benchmark hybrid architectures 而非 analyze convergence as phenomenon。 他们没有计算 cross-arch std trajectory、没有做 per-example analysis、没有 scale-dependent framing。 这是 median 档可以安全声称的 4-point differentiation。 不需要 exaggerate——Wang et al. 提供了 data infrastructure (model zoo)， 我们提供了 analytical framework (equalizer effect characterization)。 关键风险：reviewer 可能认为 \"分析别人的 model zoo\" 的贡献不够 substantial， 尤其在 Main track。Findings track 对此更宽容。\n"
503	  },
504	  {
505	    "name": "Convergence-divergence bridge analysis",
506	    "description": "在 LAMBADA 上绘制 aggregate convergence curve 与 per-example divergence metrics (Jaccard, net effect asymmetry) 随 attention ratio 的共变关系， 展示 equalizer paradox 的 co-evolution。\n",
507	    "results": {
508	      "convergence_divergence_correlation_rho": -0.83,
509	      "convergence_divergence_correlation_p": 0.042,
510	      "aggregate_std_at_ratios": {
511	        "0": 0.024,
512	        "1": 0.019,
513	        "3": 0.014,
514	        "6": 0.009,
515	        "8": 0.007,
516	        "24": 0.005
517	      },
518	      "jaccard_at_ratios": {
519	        "1": 0.14,
520	        "3": 0.11,
521	        "6": 0.09,
522	        "8": 0.08,
523	        "24": 0.07
524	      },
525	      "net_effect_asymmetry_at_ratios": {
526	        "1": 0.12,
527	        "3": 0.18,
528	        "6": 0.24,
529	        "8": 0.27,
530	        "24": 0.31
531	      },
532	      "paradox_strength": "moderate — trends clear but not dramatic"
533	    },
534	    "tables": [
535	      {
536	        "table_id": "T8",
537	        "caption": "Co-evolution of aggregate convergence and per-example divergence (LAMBADA, 1.3B)",
538	        "columns": [
539	          "Attention Ratio",
540	          "Cross-arch Std",
541	          "Pairwise Jaccard (mean)",
542	          "Net Effect Asymmetry"
543	        ],
544	        "rows": [
545	          [
546	            "0 (pure)",
547	            "0.024",
548	            "—",
549	            "—"
550	          ],
551	          [
552	            "1 (h1-1)",
553	            "0.019",
554	            "0.14",
555	            "0.12"
556	          ],
557	          [
558	            "3 (h3-1)",
559	            "0.014",
560	            "0.11",
561	            "0.18"
562	          ],
563	          [
564	            "6 (h6-1)",
565	            "0.009",
566	            "0.09",
567	            "0.24"
568	          ],
569	          [
570	            "8 (h8-1)",
571	            "0.007",
572	            "0.08",
573	            "0.27"
574	          ],
575	          [
576	            "24 (h24-1)",
577	            "0.005",
578	            "0.07",
579	            "0.31"
580	          ]
581	        ]
582	      }
583	    ],
584	    "figures": [],
585	    "analysis": "这是 paper 的 signature visualization——equalizer paradox 的 visual proof。 Median 档下 X 型交叉 clear but not dramatic: 两条曲线的斜率都是 moderate， 不像 best-case 那样有陡峭的 scissor pattern。 ρ=-0.83 (p=0.042) 足以在 paper 中声称 \"significant co-evolution\" 但 reviewer 可能要求 robustness check (e.g., leave-one-out)。 在 Findings 档 + 诚实的 limitation discussion 下，这个 figure 应该能 survive review。 关键 framing: \"As attention layers increasingly equalize aggregate performance, the per-example mechanisms through which this equalization occurs become increasingly architecture-specific—a paradox with direct implications for architecture selection in deployment.\"\n\nMedian 档下 convergence-divergence co-evolution 应该 detectable (ρ=-0.83, p=0.042 刚好显著) 但不 dramatic。Aggregate std 从 0.024 稳步降至 0.005 是已知的 convergence pattern。 Jaccard 从 0.14 降至 0.07 说明随着 attention 增加，helped/hurt 子集变得更 architecture-specific (更少重叠)，但降幅温和。Net effect asymmetry 从 0.12 升至 0.31 说明 每个 architecture 被 attention \"推向\" 的方向越来越不同 (GDN/RetNet hurt 更多, HGRN2 help 更多)。 ρ=-0.83 说明两个 trend 确实 co-evolve——more attention = more aggregate convergence AND more per-example divergence。 但 p=0.042 在 n=5 (或 n=6 含 ratio 0) 下刚好显著，不robust—— drop 一个 attention ratio 就可能不再显著。 这是 median 档的典型 borderline significance。\n"
586	  }
587	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5515cd5b-f6ed-414b-96ff-f1869c7d1c8b",
  "isSidechain": false,
  "promptId": "1470b571-8e3c-450f-9a8f-7768e6cda7c5",
  "type": "user",
  "uuid": "4dc9a5b6-a58f-4b4f-a22c-adabef414b49",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/dream_reports/dream_20260519T131014/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Task-specificity characterization of equalizer effect\",\n    \"description\": \"对 6 个 benchmark 在 1.3B 规模下计算 cross-architecture std trajectory (attention ratio 0→24)， 拟合 Spearman ρ(std vs attention_ratio)，建立 convergence strength 与 retrieval demand 的连续关系。\\n\",\n    \"results\": {\n      \"lambada_rho\": -1.0,\n      \"lambada_perm_p\": 0.0083,\n      \"lambada_std_baseline\": 0.024,\n      \"lambada_std_best\": 0.005,\n      \"lambada_std_reduction_pct\": 79,\n      \"arc_easy_rho\": -0.6,\n      \"arc_easy_perm_p\": 0.142,\n      \"arc_challenge_rho\": -0.3,\n      \"arc_challenge_perm_p\": 0.383,\n      \"hellaswag_rho\": 0.1,\n      \"hellaswag_perm_p\": 0.872,\n      \"winogrande_rho\": -0.2,\n      \"winogrande_perm_p\": 0.544,\n      \"mmlu_rho\": 0.0,\n      \"mmlu_perm_p\": 0.983,\n      \"benchmarks_with_rho_below_neg05\": 1,\n      \"benchmarks_with_suggestive_rho\": 1\n    },\n    \"tables\": [\n      {\n        \"table_id\": \"T1\",\n        \"caption\": \"Cross-architecture convergence strength by benchmark (1.3B scale)\",\n        \"columns\": [\n          \"Benchmark\",\n          \"Retrieval Demand (qualitative)\",\n          \"Baseline Std (attn=0)\",\n          \"Best Std\",\n          \"Spearman ρ\",\n          \"Exact Perm. p\"\n        ],\n        \"rows\": [\n          [\n            \"LAMBADA\",\n            \"High (last-word retrieval)\",\n            \"0.024\",\n            \"0.005\",\n            \"-1.00\",\n            \"0.008**\"\n          ],\n          [\n            \"ARC-Easy\",\n            \"Medium (knowledge retrieval)\",\n            \"0.018\",\n            \"0.011\",\n            \"-0.60\",\n            \"0.142\"\n          ],\n          [\n            \"ARC-Challenge\",\n            \"Medium-Low\",\n            \"0.022\",\n            \"0.017\",\n            \"-0.30\",\n            \"0.383\"\n          ],\n          [\n            \"WinoGrande\",\n            \"Low-Medium (coref)\",\n            \"0.015\",\n            \"0.013\",\n            \"-0.20\",\n            \"0.544\"\n          ],\n          [\n            \"HellaSwag\",\n            \"Low (commonsense reasoning)\",\n            \"0.012\",\n            \"0.013\",\n            \"0.10\",\n            \"0.872\"\n          ],\n          [\n            \"MMLU\",\n            \"Low (knowledge + reasoning)\",\n            \"0.031\",\n            \"0.030\",\n            \"0.00\",\n            \"0.983\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Median 档下 continuous spectrum 论证不成立——只有 LAMBADA 显著、ARC-Easy suggestive， 其余 4 个 benchmark ρ 值在 [-0.3, 0.1] 噪声区间。 Paper 必须将 Claim 1 scope 限缩为 retrieval-intensive task convergence， 而非 general task-type modulation。 Post-hoc taxonomy 风险依然存在：只有一个 \\\"high retrieval\\\" benchmark 显著， reviewer 可质疑分类本身是为 fit data 设计的。 Mitigation: 引用 BIG-bench 已有 taxonomy 而非自建，并在 limitations 中诚实标注。\\n\\n\\nMedian 档的核心特征是 LAMBADA 显著但其余 benchmark 未跨越 significance threshold。 LAMBADA 作为纯 last-word retrieval 任务，其 ρ=-1.0 完美单调关系在此档位保持不变——这是整篇论文的锚点。 ARC-Easy ρ=-0.6 处于指标范围 [-0.7, -0.4] 中段，p=0.142 不显著（n=5 attention ratios 统计功效太低）， 但方向一致，可作为 suggestive evidence。ARC-Challenge 更弱因其推理成分更重。 HellaSwag/WinoGrande/MMLU 因 reasoning-dominant 性质，convergence 接近零或为噪声。 这意味着 continuous spectrum 叙事只有两个正方向数据点（LAMBADA 显著 + ARC-E suggestive）， 不足以声称 dose-response，只能说 \\\"retrieval-intensive tasks show convergence, generality remains open\\\"。\\n\"\n  },\n  {\n    \"name\": \"Multi-benchmark per-example analysis\",\n    \"description\": \"对 1.3B 和 340M 模型使用 --log_samples 重新运行 lm-eval， 收集 HellaSwag、ARC-Easy、ARC-Challenge 的 per-example logprob 数据。 计算 per-example delta (hybrid - pure) 并分析是否存在 per-example convergence pattern。\\n\",\n    \"results\": {\n      \"hellaswag_per_example_convergence_detected\": false,\n      \"hellaswag_per_example_pattern\": \"no systematic pattern — deltas approximately i.i.d. across architectures\",\n      \"hellaswag_cross_arch_delta_correlation_mean\": 0.03,\n      \"arc_easy_per_example_rho_with_attention\": -0.5,\n      \"arc_easy_per_example_signal\": \"ambiguous\",\n      \"arc_easy_jaccard_pairwise_helped\": 0.12,\n      \"arc_challenge_per_example_convergence_detected\": false,\n      \"arc_challenge_cross_arch_delta_correlation_mean\": -0.05,\n      \"models_requiring_rerun_340m\": 10,\n      \"models_requiring_rerun_1_3b\": 3,\n      \"total_gpu_hours_used\": 18\n    },\n    \"tables\": [\n      {\n        \"table_id\": \"T2\",\n        \"caption\": \"Per-example convergence indicators across benchmarks (1.3B, h24-1 vs h0)\",\n        \"columns\": [\n          \"Benchmark\",\n          \"Mean |Δ logprob|\",\n          \"Cross-arch Δ corr.\",\n          \"Jaccard (helped)\",\n          \"Per-ex convergence?\"\n        ],\n        \"rows\": [\n          [\n            \"LAMBADA\",\n            \"0.34\",\n            \"0.08\",\n            \"0.07\",\n            \"Yes (strong)\"\n          ],\n          [\n            \"ARC-Easy\",\n            \"0.12\",\n            \"0.18\",\n            \"0.12\",\n            \"Ambiguous\"\n          ],\n          [\n            \"ARC-Challenge\",\n            \"0.09\",\n            \"-0.05\",\n            \"0.15\",\n            \"No\"\n          ],\n          [\n            \"HellaSwag\",\n            \"0.06\",\n            \"0.03\",\n            \"0.22\",\n            \"No\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"HellaSwag per-example 确认非收敛是关键正面结果——从 \\\"aggregate ρ 不显著\\\" 升级为 \\\"per-example 分析确认 attention 对 reasoning task 无系统性影响\\\"， 堵住了 reviewer \\\"也许 aggregate 不显著只是 power 不足\\\" 的攻击路线。 ARC-Easy 的模糊信号是 median 档的标志——它既不能用来扩展 Claim 1 到第二个 task， 也不能被忽略（ρ=-0.5 毕竟有方向性）。 Paper 中应呈现为 \\\"suggestive but inconclusive at current sample size\\\"。\\n\\n\\nMedian 档的定义要求 HellaSwag per-example 确认非收敛（好，升级 Claim 1 的 \\\"non-converging\\\" 证据）， 但 ARC-Easy per-example 信号模糊。HellaSwag 上 per-example delta 与 architecture identity 无相关， 说明 attention 对 reasoning task 的影响是随机散射的——这正面支持了 \\\"convergence is retrieval-specific\\\" 叙事。 ARC-Easy 的 ρ=-0.5 处于中间地带：有方向性但 Jaccard=0.12 说明 helped/hurt 子集有少量重叠， 不像 LAMBADA 那样有清晰的 architecture-specific 分化。 这使得 ARC-Easy 成为一个 ambiguous data point——不能用来支持也不能用来否定 convergence。\\n\"\n  },\n  {\n    \"name\": \"Helped/hurt sample characterization\",\n    \"description\": \"对 LAMBADA 上每个 architecture 的 helped/hurt sample 子集， 计算 target token frequency、context length、last-sentence perplexity、domain 分布， 测试这些 feature 是否显著区分 helped vs hurt 以及是否跨架构不同。\\n\",\n    \"results\": {\n      \"significant_features_count\": 1,\n      \"target_token_frequency_p_gdn\": 0.003,\n      \"target_token_frequency_p_retnet\": 0.008,\n      \"target_token_frequency_p_hgrn2\": 0.022,\n      \"target_token_frequency_effect_direction\": \"attention helps rare tokens more\",\n      \"context_length_p_gdn\": 0.087,\n      \"context_length_p_retnet\": 0.134,\n      \"context_length_p_hgrn2\": 0.062,\n      \"last_sentence_perplexity_p_gdn\": 0.214,\n      \"domain_distribution_chi2_p\": 0.341,\n      \"cross_arch_feature_profile_differs\": \"partially\",\n      \"jaccard_pairwise_mean\": 0.08,\n      \"sample_feature_best_p\": 0.003\n    },\n    \"tables\": [\n      {\n        \"table_id\": \"T3\",\n        \"caption\": \"Feature comparison between helped and hurt samples per architecture (LAMBADA, 1.3B h24-1 vs h0)\",\n        \"columns\": [\n          \"Feature\",\n          \"GDN (p)\",\n          \"GDN (d)\",\n          \"RetNet (p)\",\n          \"RetNet (d)\",\n          \"HGRN2 (p)\",\n          \"HGRN2 (d)\"\n        ],\n        \"rows\": [\n          [\n            \"Target token freq (log rank)\",\n            \"0.003**\",\n            \"-0.41\",\n            \"0.008**\",\n            \"-0.33\",\n            \"0.022*\",\n            \"-0.24\"\n          ],\n          [\n            \"Context length\",\n            \"0.087\",\n            \"0.19\",\n            \"0.134\",\n            \"0.15\",\n            \"0.062\",\n            \"0.22\"\n          ],\n          [\n            \"Last-sent. perplexity\",\n            \"0.214\",\n            \"0.12\",\n            \"0.378\",\n            \"0.08\",\n            \"0.156\",\n            \"0.14\"\n          ],\n          [\n            \"Domain entropy (H)\",\n            \"0.341\",\n            \"—\",\n            \"0.287\",\n            \"—\",\n            \"0.512\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"只有 target token frequency 一个 feature 在 p<0.01 水平显著且三架构一致， 但 effect size 从 GDN d=0.41 到 HGRN2 d=0.24 递减。 这足以写一段有说服力的 mechanistic story (\\\"attention enables rare token retrieval that recurrence alone cannot achieve\\\")，但不足以完整解释 architecture-specific 差异。 为什么 GDN 被 hurt 的 sample 和 RetNet 被 hurt 的 sample 几乎不重叠 (Jaccard=0.06) 仍然缺乏 feature-level 解释。 Paper 应当诚实地说 \\\"token frequency partially explains the mechanism; the architecture-specificity of affected subsets remains only partially characterized\\\"。\\n\\n\\nMedian 档要求 \\\"1 个 feature 显著区分 (p<0.01) 但跨架构差异不够鲜明\\\"。 Target token frequency 是最有物理意义的 feature——attention 层的全局 context access 天然有利于 rare token retrieval，三个架构都显示这一方向，但 effect size 不同 (GDN 最强，HGRN2 最弱，因为 HGRN2 的 hierarchical gating 本身就部分覆盖了 rare token)。 Context length 在三个架构上都接近 but 不跨越 p<0.05，说明 attention 对长 context 有帮助 但不是主要分化因素。Perplexity 和 domain 不显著——这些是 confound 而非 mechanism。 跨架构差异 \\\"partially\\\" 因为 token frequency 方向一致但 magnitude 不同， 不像 LAMBADA Jaccard<0.10 那样的鲜明分化，削弱了 \\\"completely different mechanisms\\\" 叙事。\\n\"\n  },\n  {\n    \"name\": \"Attention weight extraction and visualization\",\n    \"description\": \"从三个架构的 h3-1 配置中提取 attention weight matrix， 分析 attention pattern 与 helped/hurt sample identity 的相关性， 以及跨架构 attention pattern 相似度。\\n\",\n    \"results\": {\n      \"attention_pattern_correlation_with_helped_hurt_gdn\": 0.31,\n      \"attention_pattern_correlation_with_helped_hurt_retnet\": 0.24,\n      \"attention_pattern_correlation_with_helped_hurt_hgrn2\": 0.37,\n      \"attention_per_example_correlation_mean\": 0.31,\n      \"cross_arch_attention_similarity_cosine_mean\": 0.42,\n      \"attention_focus_pattern_gdn\": \"dispersed across mid-context positions\",\n      \"attention_focus_pattern_retnet\": \"concentrated on recent + first positions (primacy-recency)\",\n      \"attention_focus_pattern_hgrn2\": \"focused on semantically related positions\",\n      \"qualitative_finding\": \"attention layers develop architecture-conditioned patterns\",\n      \"gpu_hours_used\": 3.5\n    },\n    \"tables\": [\n      {\n        \"table_id\": \"T4\",\n        \"caption\": \"Attention pattern analysis for h3-1 models on LAMBADA (1.3B)\",\n        \"columns\": [\n          \"Architecture\",\n          \"Attn-Helped/Hurt Corr.\",\n          \"Dominant Pattern\",\n          \"Cross-arch Cosine Sim.\"\n        ],\n        \"rows\": [\n          [\n            \"GDN\",\n            \"0.31\",\n            \"Dispersed mid-context\",\n            \"— / 0.38 / 0.44\"\n          ],\n          [\n            \"RetNet\",\n            \"0.24\",\n            \"Primacy-recency\",\n            \"0.38 / — / 0.45\"\n          ],\n          [\n            \"HGRN2\",\n            \"0.37\",\n            \"Semantic focus\",\n            \"0.44 / 0.45 / —\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Correlation 0.2-0.4 足以说明 \\\"attention patterns are related to per-example effects\\\" 但不足以说明 \\\"attention patterns explain per-example effects\\\"。 这是 median 档标志性的 gap——方向正确，magnitude 不够支撑 causal claim。 Paper 必须用 \\\"suggestive mechanistic evidence\\\" 而非 \\\"causal mechanism\\\"， 并在 discussion 中承认 recurrence 状态变化可能是 complementary mechanism 但无法观测。 Qualitative attention pattern 差异（dispersed vs primacy-recency vs semantic） 可以作为有吸引力的 figure 但不能作为定量论证的主体。\\n\\n\\nMedian 档要求 attention-per-example correlation 在 0.2-0.4 范围内，方向正确但不足以独立支撑机制论证。 均值 0.31 说明 attention pattern 与 helped/hurt 有可检测但中等的关联—— 比随机强（排除 null hypothesis）但远不够作为 causal mechanism 的证据。 跨架构 attention cosine similarity 0.42 说明 attention 层在不同 recurrence backbone 上 发展出部分不同的 pattern，与 Jaccard<0.10 的 per-example 分化方向一致， 但相似度高于预期（可能因为 LAMBADA 任务本身的 inductive bias 限制了 attention 的自由度）。 三个架构的 attention 定性 pattern 不同，支持 \\\"architecture-conditioned attention\\\" 叙事， 但定量相关性只有 0.2-0.4 意味着 attention pattern 不是唯一的 mechanism—— recurrence 状态本身的改变也参与其中，但我们无法直接观测。\\n\"\n  },\n  {\n    \"name\": \"Architecture expansion check\",\n    \"description\": \"搜索 Wang et al. model zoo 和公开来源，寻找额外的 hybrid linear recurrent architectures (Mamba/Mamba2 hybrid, RWKV hybrid 等)。如果找到则在 LAMBADA 上评估 convergence。\\n\",\n    \"results\": {\n      \"additional_architectures_found\": 0,\n      \"wang_et_al_zoo_exhausted\": true,\n      \"mamba_hybrid_public\": false,\n      \"rwkv_hybrid_public\": false,\n      \"other_hybrid_candidates_checked\": [\n        \"Mamba-2 hybrid (not in zoo)\",\n        \"RWKV-6 hybrid (no public checkpoint)\",\n        \"Griffin (Google, not released)\"\n      ],\n      \"architectures_tested_final\": 3\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"n=3 是不可改变的硬约束。Paper 的 mitigation 策略： (1) 强调这三种架构代表三种不同的 recurrence mechanism (gated delta rule, linear attention + exp decay, hierarchical gating)， 不是三个随机选择； (2) per-example analysis 提供了每个 architecture × 5 ratios × ~5000 samples 的数据点， 统计上远超 n=3 的印象； (3) 在 limitations 中明确声明 generalization to other recurrence families is an open question。 Reviewer 攻击面: \\\"n=3 insufficient for general claims\\\" 是预期中的最常见 weakness comment， Findings 档可以生存，Main 档可能被此点 reject。\\n\\n\\nMedian 档明确指出 \\\"无额外架构可用（Wang et al. zoo 已穷尽）\\\"，architectures_tested 固定为 3。 Wang et al. 的 72 个模型覆盖了 GDN、RetNet、HGRN2 三种架构在 2 个 scale × 多个 attention ratio 的组合， 已经是公开可用的最完整 hybrid recurrent model zoo。 Mamba-2 hybrid 和 RWKV hybrid 虽然在文献中被讨论但没有公开 checkpoint。 Griffin (Google) 有公开论文但模型权重未发布。 这意味着 n=3 limitation 无法在本论文中解决，必须在 limitations 中明确讨论 并将其定位为 future work。\\n\"\n  },\n  {\n    \"name\": \"340M rebound mechanism analysis\",\n    \"description\": \"深入分析 340M 在 attn=8 处的 non-monotonic rebound。 与 1.3B 同 attention ratio 的 per-example 数据对比， 识别哪些 sample 在 340M 发生 diverge，并分析 training token count confound。\\n\",\n    \"results\": {\n      \"rebound_magnitude_340m_attn8_std_increase_pct\": 35,\n      \"rebound_samples_overlap_with_1_3b_helped\": 0.28,\n      \"rebound_explanation_partial\": true,\n      \"capacity_hypothesis_supported\": true,\n      \"training_tokens_confound_separable\": false,\n      \"training_tokens_340m\": \"20B\",\n      \"training_tokens_1_3b\": \"100B\",\n      \"rebound_sample_characteristics\": \"predominantly long-context (>80 tokens) with rare target tokens\",\n      \"scale_vs_tokens_confound_severity\": \"moderate — cannot fully decouple\"\n    },\n    \"tables\": [\n      {\n        \"table_id\": \"T5\",\n        \"caption\": \"340M rebound analysis: per-example comparison at attn=8\",\n        \"columns\": [\n          \"Metric\",\n          \"340M\",\n          \"1.3B\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"Cross-arch std at attn=8\",\n            \"0.019 (↑35% from attn=6)\",\n            \"0.008 (↓ monotonic)\",\n            \"Rebound only at 340M\"\n          ],\n          [\n            \"Rebound samples: mean context length\",\n            \"94.2 tokens\",\n            \"N/A (no rebound)\",\n            \"Long-context samples most affected\"\n          ],\n          [\n            \"Rebound samples: mean target freq rank\",\n            \"8,420\",\n            \"N/A\",\n            \"Rare tokens disproportionately affected\"\n          ],\n          [\n            \"Overlap: rebound↔1.3B helped\",\n            \"Jaccard=0.28\",\n            \"—\",\n            \"Moderate overlap: same hard samples\"\n          ],\n          [\n            \"Training tokens\",\n            \"20B\",\n            \"100B\",\n            \"5× difference, confounded with scale\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Rebound 机制的 partial explanation 足以支撑 Claim 2 的 \\\"scale matters\\\" binary contrast， 但 training-token confound 削弱了 mechanistic clarity。 Reviewer 可以合理地问 \\\"如果 340M 也训练 100B tokens 会怎样？\\\"——我们无法回答因为没有这个 ablation。 Paper 策略：(1) 承认 confound，(2) 用 capacity argument (attention 层在小模型中与 recurrence 层 compete for capacity) 作为 primary explanation 因为它有 per-example evidence 支持（long-context rare-token samples 受影响最大）， (3) 明确标注 training-token 量的差异为 limitation。 这在 Findings 档是可接受的诚实度——reviewer 不会因为你承认了 confound 而 reject， 但会因为你假装 confound 不存在而 reject。\\n\\n\\nMedian 档要求 \\\"340M rebound 有 partial 解释，但 scale vs training-tokens confound 无法完全解耦\\\"。 Rebound 在 attn=8 发生是因为 340M 模型容量不足以同时维持 recurrence quality 和 attention quality—— 当 attention 层数过多时，recurrence 层被过度压缩导致 baseline capability 下降。 这在长 context + rare token 的 sample 上最明显（这些 sample 需要 recurrence 和 attention 协同工作）。 但 1.3B 模型不仅 scale 更大，training token 也是 5x (100B vs 20B)， 无法区分是 \\\"更大的模型容量允许 attention 和 recurrence 共存\\\" 还是 \\\"更多 training 让模型学会了更好的分工\\\"。 Paper 必须将此标注为 acknowledged confound，用 \\\"scale and/or training duration\\\" 的措辞， 而非单纯归因于 scale。\\n\"\n  },\n  {\n    \"name\": \"Statistical robustness framework\",\n    \"description\": \"对 convergence metrics 实施 bootstrap CI、Bonferroni/FDR 多重比较校正、 GDN 排除敏感性分析、effect size 报告。\\n\",\n    \"results\": {\n      \"lambada_std_reduction_bootstrap_ci_95_pct\": [\n        58,\n        72\n      ],\n      \"lambada_rho_bootstrap_ci_95\": [\n        -1.0,\n        -0.8\n      ],\n      \"lambada_rho_bootstrap_ci_width\": 0.2,\n      \"arc_easy_rho_bootstrap_ci_95\": [\n        -0.9,\n        -0.2\n      ],\n      \"bonferroni_corrected_significant_benchmarks\": 1,\n      \"fdr_corrected_significant_benchmarks\": 1,\n      \"gdn_excluded_claim1_survives\": true,\n      \"gdn_excluded_claim3_survives\": true,\n      \"gdn_excluded_claims_surviving\": 2,\n      \"gdn_excluded_effect_size_reduction_pct\": 35,\n      \"gdn_excluded_lambada_std_reduction_pct\": 52,\n      \"gdn_excluded_rho\": -0.9,\n      \"cohens_d_lambada_convergence\": 1.12,\n      \"cohens_d_lambada_convergence_no_gdn\": 0.73,\n      \"eta_squared_attention_effect\": 0.34,\n      \"bootstrap_ci_crosses_zero\": false\n    },\n    \"tables\": [\n      {\n        \"table_id\": \"T6\",\n        \"caption\": \"Bootstrap confidence intervals and sensitivity analysis\",\n        \"columns\": [\n          \"Metric\",\n          \"Full (3 arch)\",\n          \"95% CI\",\n          \"Excl. GDN (2 arch)\",\n          \"95% CI\",\n          \"Δ%\"\n        ],\n        \"rows\": [\n          [\n            \"LAMBADA std reduction (%)\",\n            \"79\",\n            \"[58, 72]\",\n            \"52\",\n            \"[38, 61]\",\n            \"-34\"\n          ],\n          [\n            \"LAMBADA Spearman ρ\",\n            \"-1.00\",\n            \"[-1.0, -0.80]\",\n            \"-0.90\",\n            \"[-1.0, -0.60]\",\n            \"—\"\n          ],\n          [\n            \"Cohen's d (convergence)\",\n            \"1.12\",\n            \"[0.74, 1.48]\",\n            \"0.73\",\n            \"[0.41, 1.05]\",\n            \"-35\"\n          ],\n          [\n            \"Pairwise Jaccard (mean)\",\n            \"0.08\",\n            \"[0.05, 0.12]\",\n            \"0.06\",\n            \"[0.03, 0.10]\",\n            \"-25\"\n          ],\n          [\n            \"Claims surviving (of 3)\",\n            \"3\",\n            \"—\",\n            \"2\",\n            \"—\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Statistical robustness 结果是 median 档的定义性特征：核心发现 survive 但 weakened。 Effect size 缩小 30-40% 意味着 GDN 贡献了不成比例的 signal—— 这本身是一个 interpretable finding (GDN 的 gated delta rule 可能对 attention 最 responsive)， 但也是一个 vulnerability (如果 reviewer 质疑 GDN 的 D004 data quality)。 Bootstrap CI 不跨零是底线——保证了 \\\"convergence exists\\\" 不是 statistical artifact。 Paper 应在 main text 报告 full 结果，在 appendix 报告 GDN-excluded sensitivity analysis， 并在 limitations 中讨论 GDN 依赖性。\\n\\n\\nMedian 档要求 bootstrap CI 较宽但不跨零，排除 GDN 后 Claim 1/3 成立但 effect size 缩小 30-40%。 LAMBADA std reduction 的 bootstrap CI [58%, 72%] 反映了 n=5 attention ratios × n=3 architectures 带来的采样不确定性——79% 的点估计在 CI 上界附近，中位估计约 65%。 排除 GDN 后 reduction 从 79% 降至 52% (缩小 34%) 因为 GDN 的 D004 配置贡献了最大的 convergence signal。 但 52% 仍然 substantial (Cohen's d 从 1.12 降至 0.73，中等到大效应)。 ρ 从 -1.0 降至 -0.90 说明两架构也有很强的 monotonic convergence 但不再完美。 Bonferroni 校正后只有 LAMBADA 显著是必然结果——6 个 benchmark 中只有 1 个 p<0.05， 校正后 threshold 变为 0.0083，只有 LAMBADA 原始 p 勉强通过。 Claims 2/3 排除 GDN 后: Claim 2 中 340M vs 1.3B contrast 在两架构上仍成立; Claim 3 中 Jaccard 在 RetNet-HGRN2 对上仍 <0.10，但只有一个 pair 不如三个 pair 的说服力强。 第三个 claim (claims_surviving = 2 而非 3) 反映 Claim 2 或 Claim 3 在排除 GDN 后 某一个变得 marginal——此处是 Claim 2 因为 340M rebound 的 mechanistic analysis 重度依赖 GDN 数据。\\n\"\n  },\n  {\n    \"name\": \"Wang et al. explicit differentiation\",\n    \"description\": \"系统性地对比 Wang et al. (arXiv 2507.06457) 的分析与本文的分析， 提取他们关于 convergence 的确切表述，量化本文的增量贡献。\\n\",\n    \"results\": {\n      \"wang_convergence_statements_found\": 3,\n      \"wang_convergence_quantitative\": false,\n      \"wang_per_example_analysis\": false,\n      \"wang_scale_dependent_convergence\": false,\n      \"wang_mechanistic_analysis\": false,\n      \"differentiation_points\": 4,\n      \"wang_relevant_quotes\": [\n        \"performance differences between architectures decrease as the attention ratio increases\",\n        \"models with higher attention ratios tend to perform more similarly\",\n        \"the choice of recurrence mechanism becomes less important at higher attention ratios\"\n      ],\n      \"our_additions\": [\n        \"Quantitative convergence framework (Spearman ρ, cross-arch std trajectory, bootstrap CI)\",\n        \"Per-example mechanism analysis revealing architecture-specific sample subsets (Jaccard < 0.10)\",\n        \"Scale-dependent convergence characterization (340M partial vs 1.3B complete)\",\n        \"Sample feature characterization linking convergence to token frequency\"\n      ]\n    },\n    \"tables\": [\n      {\n        \"table_id\": \"T7\",\n        \"caption\": \"Explicit differentiation from Wang et al. (2025)\",\n        \"columns\": [\n          \"Analysis Dimension\",\n          \"Wang et al.\",\n          \"This Work\"\n        ],\n        \"rows\": [\n          [\n            \"Convergence observation\",\n            \"Qualitative ('tend to perform similarly')\",\n            \"Quantitative (ρ, std trajectory, CI)\"\n          ],\n          [\n            \"Per-example analysis\",\n            \"Not performed\",\n            \"Full per-example logprob analysis, Jaccard, helped/hurt\"\n          ],\n          [\n            \"Scale dependency\",\n            \"Not characterized\",\n            \"Binary contrast: 340M partial vs 1.3B complete\"\n          ],\n          [\n            \"Mechanistic analysis\",\n            \"Not performed\",\n            \"Sample feature characterization, attention pattern analysis\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"4-point differentiation 在 Findings 档足够有说服力—— \\\"quantitative framework atop qualitative observation\\\" 是经典的 analysis paper contribution pattern。 Paper introduction 应在致谢 Wang et al. model zoo 的同时明确标注 \\\"they report X qualitatively; we provide the first quantitative characterization revealing Y\\\"。 避免任何暗示 Wang et al. 遗漏了什么 \\\"obvious\\\" 分析——他们的 paper 目标不同， convergence 对他们是 side observation 而非 research question。\\n\\n\\nWang et al. 在 72-model zoo 的 aggregate 结果讨论中定性地提到了 convergence， 但他们的目标是 benchmark hybrid architectures 而非 analyze convergence as phenomenon。 他们没有计算 cross-arch std trajectory、没有做 per-example analysis、没有 scale-dependent framing。 这是 median 档可以安全声称的 4-point differentiation。 不需要 exaggerate——Wang et al. 提供了 data infrastructure (model zoo)， 我们提供了 analytical framework (equalizer effect characterization)。 关键风险：reviewer 可能认为 \\\"分析别人的 model zoo\\\" 的贡献不够 substantial， 尤其在 Main track。Findings track 对此更宽容。\\n\"\n  },\n  {\n    \"name\": \"Convergence-divergence bridge analysis\",\n    \"description\": \"在 LAMBADA 上绘制 aggregate convergence curve 与 per-example divergence metrics (Jaccard, net effect asymmetry) 随 attention ratio 的共变关系， 展示 equalizer paradox 的 co-evolution。\\n\",\n    \"results\": {\n      \"convergence_divergence_correlation_rho\": -0.83,\n      \"convergence_divergence_correlation_p\": 0.042,\n      \"aggregate_std_at_ratios\": {\n        \"0\": 0.024,\n        \"1\": 0.019,\n        \"3\": 0.014,\n        \"6\": 0.009,\n        \"8\": 0.007,\n        \"24\": 0.005\n      },\n      \"jaccard_at_ratios\": {\n        \"1\": 0.14,\n        \"3\": 0.11,\n        \"6\": 0.09,\n        \"8\": 0.08,\n        \"24\": 0.07\n      },\n      \"net_effect_asymmetry_at_ratios\": {\n        \"1\": 0.12,\n        \"3\": 0.18,\n        \"6\": 0.24,\n        \"8\": 0.27,\n        \"24\": 0.31\n      },\n      \"paradox_strength\": \"moderate — trends clear but not dramatic\"\n    },\n    \"tables\": [\n      {\n        \"table_id\": \"T8\",\n        \"caption\": \"Co-evolution of aggregate convergence and per-example divergence (LAMBADA, 1.3B)\",\n        \"columns\": [\n          \"Attention Ratio\",\n          \"Cross-arch Std\",\n          \"Pairwise Jaccard (mean)\",\n          \"Net Effect Asymmetry\"\n        ],\n        \"rows\": [\n          [\n            \"0 (pure)\",\n            \"0.024\",\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"1 (h1-1)\",\n            \"0.019\",\n            \"0.14\",\n            \"0.12\"\n          ],\n          [\n            \"3 (h3-1)\",\n            \"0.014\",\n            \"0.11\",\n            \"0.18\"\n          ],\n          [\n            \"6 (h6-1)\",\n            \"0.009\",\n            \"0.09\",\n            \"0.24\"\n          ],\n          [\n            \"8 (h8-1)\",\n            \"0.007\",\n            \"0.08\",\n            \"0.27\"\n          ],\n          [\n            \"24 (h24-1)\",\n            \"0.005\",\n            \"0.07\",\n            \"0.31\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"这是 paper 的 signature visualization——equalizer paradox 的 visual proof。 Median 档下 X 型交叉 clear but not dramatic: 两条曲线的斜率都是 moderate， 不像 best-case 那样有陡峭的 scissor pattern。 ρ=-0.83 (p=0.042) 足以在 paper 中声称 \\\"significant co-evolution\\\" 但 reviewer 可能要求 robustness check (e.g., leave-one-out)。 在 Findings 档 + 诚实的 limitation discussion 下，这个 figure 应该能 survive review。 关键 framing: \\\"As attention layers increasingly equalize aggregate performance, the per-example mechanisms through which this equalization occurs become increasingly architecture-specific—a paradox with direct implications for architecture selection in deployment.\\\"\\n\\nMedian 档下 convergence-divergence co-evolution 应该 detectable (ρ=-0.83, p=0.042 刚好显著) 但不 dramatic。Aggregate std 从 0.024 稳步降至 0.005 是已知的 convergence pattern。 Jaccard 从 0.14 降至 0.07 说明随着 attention 增加，helped/hurt 子集变得更 architecture-specific (更少重叠)，但降幅温和。Net effect asymmetry 从 0.12 升至 0.31 说明 每个 architecture 被 attention \\\"推向\\\" 的方向越来越不同 (GDN/RetNet hurt 更多, HGRN2 help 更多)。 ρ=-0.83 说明两个 trend 确实 co-evolve——more attention = more aggregate convergence AND more per-example divergence。 但 p=0.042 在 n=5 (或 n=6 含 ratio 0) 下刚好显著，不robust—— drop 一个 attention ratio 就可能不再显著。 这是 median 档的典型 borderline significance。\\n\"\n  }\n]",
      "numLines": 587,
      "startLine": 1,
      "totalLines": 587
    }
  },
  "sourceToolAssistantUUID": "5515cd5b-f6ed-414b-96ff-f1869c7d1c8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "c013dfff-9ae5-416a-b5ae-03fba6a5fd1c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T13:33:25.071Z_

<details><summary>↩ Tool result · `toolu_01M1cDDCQ52eUT7eir4H8bQE`</summary>

```text
1	# Paper Framing — entrainment_gated_ft
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (via ARR)
5	- Backup: EMNLP 2026 Findings
6	- Deadline: ARR June 2026 cycle (submission ~June 15)
7	
8	## Paper Type
9	Empirical analysis paper (not method paper)
10	
11	## Core Claims (3 条)
12	
13	### Claim 1: Task-Specific Equalizer Effect
14	Adding attention layers to different linear recurrent architectures (GatedDeltaNet, RetNet, HGRN2) induces aggregate performance convergence whose strength scales with task retrieval demand—strongest on LAMBADA (ρ=-1.0, cross-arch std drops 79%), suggestive on ARC-Easy (ρ=-0.7, underpowered), absent on reasoning-heavy tasks (HellaSwag, WinoGrande). This continuous relationship between retrieval demand and convergence strength is a key finding, not a limitation of single-task significance.
15	
16	### Claim 2: Scale-Dependent Convergence
17	The convergence effect is scale-dependent: monotonically complete at 1.3B parameters (Spearman ρ=-1.0 for cross-arch std vs attention ratio, exact permutation p=0.0083) but only partial at 340M with a non-monotonic rebound at high attention ratios. Note: only two scale points available (Wang et al. do not provide 7B models); this is a binary contrast, not a multi-point trend. Paper must frame honestly as "scale matters" without implying extrapolation.
18	
19	### Claim 3: Architecture-Specific Mechanism (Equalizer Paradox)
20	Despite aggregate convergence, attention acts on almost entirely different sample subsets per architecture (pairwise Jaccard < 0.10). GDN and RetNet are hurt (net negative on LAMBADA), HGRN2 is helped (net positive), with symmetric effect magnitudes—convergence emerges from complementary, not redundant, mechanisms.
21	
22	## Story Spine
23	
24	### Problem
25	Hybrid architectures mixing linear recurrence with full attention are becoming the dominant paradigm for efficient language models. A critical open question: does adding attention homogenize model behavior across different recurrence mechanisms, or do architecture-specific effects persist?
26	
27	### Existing Approaches & Gaps
28	Wang et al. (2025, arXiv 2507.06457) provide the most comprehensive model zoo (72 models, 3 architectures, multiple scales and attention ratios) but report only aggregate metrics. They qualitatively note convergence trends but do not analyze: (a) the per-example mechanism, (b) scale dependency of convergence, (c) task-specificity, or (d) why architectures converge to similar *aggregate* performance through *different* individual-sample effects.
29	
30	### Our Framing
31	We provide the first quantitative characterization of the "equalizer effect"—a systematic per-example analysis revealing that attention creates aggregate performance convergence through architecture-specific, largely non-overlapping mechanisms. This "equalizer paradox" (aggregate convergence + per-example divergence) has direct implications for architecture selection: even when aggregate metrics converge, the types of inputs each architecture handles well remain architecture-specific.
32	
33	### Headline Result Template
34	"At 1.3B scale, adding attention layers reduces cross-architecture performance variance by 79% on LAMBADA (std 0.024→0.005), yet per-example analysis reveals the affected sample subsets are almost entirely non-overlapping across architectures (Jaccard < 0.10), with symmetric but opposite effect directions."
35	
36	## Venue Fit Risks
37	
38	### Risk 1: Architecture Analysis vs NLP
39	EMNLP is NLP-focused; this paper is closer to architecture analysis. **Mitigation**: Frame in terms of understanding language model behavior on specific linguistic tasks. Anchor analysis to token-level and context-level linguistic features (frequency, context length, retrieval demand). Include practical recommendations for practitioners choosing hybrid architectures for specific NLP tasks.
40	
41	### Risk 2: Limited Task Coverage
42	Currently only LAMBADA shows clear convergence. **Mitigation**: (a) Extend per-example analysis to HellaSwag and other benchmarks, (b) provide principled explanation of LAMBADA's retrieval-dependent nature vs reasoning tasks, (c) if convergence appears on other retrieval tasks, strengthens Claim 1; if not, reframe as "convergence is task-type-specific" which is still interesting.
43	
44	### Risk 3: Small Architecture Sample
45	Only 3 architectures (GDN, RetNet, HGRN2). **Mitigation**: These represent three distinct recurrence mechanisms (gated delta rule, linear attention with exponential decay, hierarchical gated recurrence). Check if Wang et al. have additional architectures or scales. n=3 is sufficient for the per-example analysis which is our main contribution.
46	
47	### Risk 4: Wang et al. Overlap
48	They have the model zoo AND qualitative convergence observation. **Mitigation**: Our contribution is explicitly about what they did NOT do: quantitative convergence framework, scale-dependent analysis, per-example mechanism analysis. Frame as "using their excellent model zoo, we discover a deeper phenomenon they missed."
49	
50	## Anticipated Reviewer Concerns
51	
52	### Concern A: "This is just a negative result from a failed hypothesis"
53	Response: Frame as discovery paper. The equalizer effect is a positive finding—it was not the hypothesis we started with, but it's a genuine empirical phenomenon with theoretical implications. Many impactful papers come from unexpected findings.
54	Required evidence: Strong standalone story; no mention of original entrainment hypothesis in the paper.
55	
56	### Concern B: "Only one task shows the effect" + Post-hoc taxonomy risk
57	Response: Do NOT use binary retrieval/reasoning split — vulnerable to post-hoc cherry-picking (only 1 benchmark in "retrieval" category, exactly the one that's significant). Instead:
58	1. **Continuous spectrum**: Plot convergence strength (Spearman ρ) against a continuous measure of "retrieval demand" per benchmark. LAMBADA ρ=-1.0, ARC-E ρ=-0.7 (suggestive), ARC-C ρ=-0.3, HellaSwag/WinoGrande/MMLU near zero. Frame as dose-response: more retrieval demand → stronger convergence.
59	2. **Cite existing task taxonomies**: Use BIG-bench taxonomy or other published meta-analyses for task property classification — don't invent our own post-hoc.
60	3. **Honest reporting**: ARC-E ρ=-0.7 (p=0.117) is "suggestive but underpowered" — n=5 ratios means low statistical power. Continuous spectrum framing turns "only LAMBADA significant" into "graded effect consistent with retrieval demand."
61	4. **Winogrande ambiguity**: Coreference resolution has a retrieval component (finding antecedent). Acknowledge this honestly rather than forcing it into "reasoning."
62	5. **exp-002 validation**: If HellaSwag per-example analysis confirms no convergence at sample level, upgrades from "aggregate not significant" to "per-example confirmed non-converging."
63	Required experiments: exp-001 (done, PASS on dichotomy), exp-002 (per-example validation), exp-003 (sample characterization).
64	
65	### Concern C: "No causal mechanism"
66	Response: Per-example analysis provides mechanistic evidence (different subsets). Strengthen with attention weight visualization and sample feature characterization.
67	Required experiments: Sample characterization (exp-003), attention weight analysis (exp-004).
68	
69	### Concern D: "n=3 architectures is too few"
70	Response: Three architectures with 5 attention ratios × 2 scales = 30 models. The per-example analysis provides thousands of data points. Check if additional architectures available.
71	Required experiments: Architecture expansion check (exp-005).
72	
73	### Concern E: "Two scales don't establish a trend"
74	Response: 7B unavailable (Wang et al. capped at 1.3B). Frame as "binary contrast showing scale is a necessary condition" — convergence requires sufficient model capacity (1.3B), not just attention. Strengthen via exp-007 (340M rebound mechanism analysis) to provide mechanistic explanation for the scale gap. Acknowledge as limitation; do not imply extrapolation.
75	Required experiments: exp-007 (340M rebound mechanism).
76	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81c3aae5-43b3-4800-b08a-d7e9e2786033",
  "isSidechain": false,
  "promptId": "1470b571-8e3c-450f-9a8f-7768e6cda7c5",
  "type": "user",
  "uuid": "ed5eb573-f0f8-4d44-9b2e-e9b480df6553",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/dream_reports/dream_20260519T131014/median/paper_framing.md",
      "content": "# Paper Framing — entrainment_gated_ft\n\n## Target Venue\n- Primary: EMNLP 2026 Main (via ARR)\n- Backup: EMNLP 2026 Findings\n- Deadline: ARR June 2026 cycle (submission ~June 15)\n\n## Paper Type\nEmpirical analysis paper (not method paper)\n\n## Core Claims (3 条)\n\n### Claim 1: Task-Specific Equalizer Effect\nAdding attention layers to different linear recurrent architectures (GatedDeltaNet, RetNet, HGRN2) induces aggregate performance convergence whose strength scales with task retrieval demand—strongest on LAMBADA (ρ=-1.0, cross-arch std drops 79%), suggestive on ARC-Easy (ρ=-0.7, underpowered), absent on reasoning-heavy tasks (HellaSwag, WinoGrande). This continuous relationship between retrieval demand and convergence strength is a key finding, not a limitation of single-task significance.\n\n### Claim 2: Scale-Dependent Convergence\nThe convergence effect is scale-dependent: monotonically complete at 1.3B parameters (Spearman ρ=-1.0 for cross-arch std vs attention ratio, exact permutation p=0.0083) but only partial at 340M with a non-monotonic rebound at high attention ratios. Note: only two scale points available (Wang et al. do not provide 7B models); this is a binary contrast, not a multi-point trend. Paper must frame honestly as \"scale matters\" without implying extrapolation.\n\n### Claim 3: Architecture-Specific Mechanism (Equalizer Paradox)\nDespite aggregate convergence, attention acts on almost entirely different sample subsets per architecture (pairwise Jaccard < 0.10). GDN and RetNet are hurt (net negative on LAMBADA), HGRN2 is helped (net positive), with symmetric effect magnitudes—convergence emerges from complementary, not redundant, mechanisms.\n\n## Story Spine\n\n### Problem\nHybrid architectures mixing linear recurrence with full attention are becoming the dominant paradigm for efficient language models. A critical open question: does adding attention homogenize model behavior across different recurrence mechanisms, or do architecture-specific effects persist?\n\n### Existing Approaches & Gaps\nWang et al. (2025, arXiv 2507.06457) provide the most comprehensive model zoo (72 models, 3 architectures, multiple scales and attention ratios) but report only aggregate metrics. They qualitatively note convergence trends but do not analyze: (a) the per-example mechanism, (b) scale dependency of convergence, (c) task-specificity, or (d) why architectures converge to similar *aggregate* performance through *different* individual-sample effects.\n\n### Our Framing\nWe provide the first quantitative characterization of the \"equalizer effect\"—a systematic per-example analysis revealing that attention creates aggregate performance convergence through architecture-specific, largely non-overlapping mechanisms. This \"equalizer paradox\" (aggregate convergence + per-example divergence) has direct implications for architecture selection: even when aggregate metrics converge, the types of inputs each architecture handles well remain architecture-specific.\n\n### Headline Result Template\n\"At 1.3B scale, adding attention layers reduces cross-architecture performance variance by 79% on LAMBADA (std 0.024→0.005), yet per-example analysis reveals the affected sample subsets are almost entirely non-overlapping across architectures (Jaccard < 0.10), with symmetric but opposite effect directions.\"\n\n## Venue Fit Risks\n\n### Risk 1: Architecture Analysis vs NLP\nEMNLP is NLP-focused; this paper is closer to architecture analysis. **Mitigation**: Frame in terms of understanding language model behavior on specific linguistic tasks. Anchor analysis to token-level and context-level linguistic features (frequency, context length, retrieval demand). Include practical recommendations for practitioners choosing hybrid architectures for specific NLP tasks.\n\n### Risk 2: Limited Task Coverage\nCurrently only LAMBADA shows clear convergence. **Mitigation**: (a) Extend per-example analysis to HellaSwag and other benchmarks, (b) provide principled explanation of LAMBADA's retrieval-dependent nature vs reasoning tasks, (c) if convergence appears on other retrieval tasks, strengthens Claim 1; if not, reframe as \"convergence is task-type-specific\" which is still interesting.\n\n### Risk 3: Small Architecture Sample\nOnly 3 architectures (GDN, RetNet, HGRN2). **Mitigation**: These represent three distinct recurrence mechanisms (gated delta rule, linear attention with exponential decay, hierarchical gated recurrence). Check if Wang et al. have additional architectures or scales. n=3 is sufficient for the per-example analysis which is our main contribution.\n\n### Risk 4: Wang et al. Overlap\nThey have the model zoo AND qualitative convergence observation. **Mitigation**: Our contribution is explicitly about what they did NOT do: quantitative convergence framework, scale-dependent analysis, per-example mechanism analysis. Frame as \"using their excellent model zoo, we discover a deeper phenomenon they missed.\"\n\n## Anticipated Reviewer Concerns\n\n### Concern A: \"This is just a negative result from a failed hypothesis\"\nResponse: Frame as discovery paper. The equalizer effect is a positive finding—it was not the hypothesis we started with, but it's a genuine empirical phenomenon with theoretical implications. Many impactful papers come from unexpected findings.\nRequired evidence: Strong standalone story; no mention of original entrainment hypothesis in the paper.\n\n### Concern B: \"Only one task shows the effect\" + Post-hoc taxonomy risk\nResponse: Do NOT use binary retrieval/reasoning split — vulnerable to post-hoc cherry-picking (only 1 benchmark in \"retrieval\" category, exactly the one that's significant). Instead:\n1. **Continuous spectrum**: Plot convergence strength (Spearman ρ) against a continuous measure of \"retrieval demand\" per benchmark. LAMBADA ρ=-1.0, ARC-E ρ=-0.7 (suggestive), ARC-C ρ=-0.3, HellaSwag/WinoGrande/MMLU near zero. Frame as dose-response: more retrieval demand → stronger convergence.\n2. **Cite existing task taxonomies**: Use BIG-bench taxonomy or other published meta-analyses for task property classification — don't invent our own post-hoc.\n3. **Honest reporting**: ARC-E ρ=-0.7 (p=0.117) is \"suggestive but underpowered\" — n=5 ratios means low statistical power. Continuous spectrum framing turns \"only LAMBADA significant\" into \"graded effect consistent with retrieval demand.\"\n4. **Winogrande ambiguity**: Coreference resolution has a retrieval component (finding antecedent). Acknowledge this honestly rather than forcing it into \"reasoning.\"\n5. **exp-002 validation**: If HellaSwag per-example analysis confirms no convergence at sample level, upgrades from \"aggregate not significant\" to \"per-example confirmed non-converging.\"\nRequired experiments: exp-001 (done, PASS on dichotomy), exp-002 (per-example validation), exp-003 (sample characterization).\n\n### Concern C: \"No causal mechanism\"\nResponse: Per-example analysis provides mechanistic evidence (different subsets). Strengthen with attention weight visualization and sample feature characterization.\nRequired experiments: Sample characterization (exp-003), attention weight analysis (exp-004).\n\n### Concern D: \"n=3 architectures is too few\"\nResponse: Three architectures with 5 attention ratios × 2 scales = 30 models. The per-example analysis provides thousands of data points. Check if additional architectures available.\nRequired experiments: Architecture expansion check (exp-005).\n\n### Concern E: \"Two scales don't establish a trend\"\nResponse: 7B unavailable (Wang et al. capped at 1.3B). Frame as \"binary contrast showing scale is a necessary condition\" — convergence requires sufficient model capacity (1.3B), not just attention. Strengthen via exp-007 (340M rebound mechanism analysis) to provide mechanistic explanation for the scale gap. Acknowledge as limitation; do not imply extrapolation.\nRequired experiments: exp-007 (340M rebound mechanism).\n",
      "numLines": 76,
      "startLine": 1,
      "totalLines": 76
    }
  },
  "sourceToolAssistantUUID": "81c3aae5-43b3-4800-b08a-d7e9e2786033",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "c013dfff-9ae5-416a-b5ae-03fba6a5fd1c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T13:33:25.067Z_

<details open><summary>🔧 Tool call — Read · `toolu_01M1cDDCQ52eUT7eir4H8bQE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/dream_reports/dream_20260519T131014/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4dc9a5b6-a58f-4b4f-a22c-adabef414b49",
  "isSidechain": false,
  "requestId": "req_011CbC1hsWy2JCmHXbTgpTPS",
  "type": "assistant",
  "uuid": "81c3aae5-43b3-4800-b08a-d7e9e2786033",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "c013dfff-9ae5-416a-b5ae-03fba6a5fd1c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01165E9FWEmERFEti91zg8vA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11722,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11722,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11722,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11722
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260519T131014 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gate…",
  "leafUuid": "ed5eb573-f0f8-4d44-9b2e-e9b480df6553",
  "sessionId": "c013dfff-9ae5-416a-b5ae-03fba6a5fd1c"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper with experiment data",
  "sessionId": "c013dfff-9ae5-416a-b5ae-03fba6a5fd1c"
}
```

---

### Assistant

_source line 14 · 2026-05-19T13:33:44.320Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data. Let me also read the paper-writing-norms skill and check if there's a LaTeX template available.

Let me plan the paper structure:

Title: "Aggregate Convergence, Per-Example Divergence: How Attention Reshapes Hybrid Recurrent Architectures on Retrieval Tasks"

The paper needs:
1. Abstract
2. Introduction
3. Background/Related Work
4. Method (Experimental Setup)
5. Results (with tables for each experiment)
6. Discussion
7. Limitations
8. Conclusion

I need to create tables T1-T8 from the experiment data.


I'm now writing the full LaTeX paper in ACL/EMNLP format, keeping in mind the key narrative constraints: downgrading the task-specificity claim to focus on retrieval-intensive tasks, marking the scale-versus-tokens confound in the binary contrast, framing the mechanistic evidence as suggestive rather than causal, and making sure to include a limitations section addressing the n=3 sample size and single-task scope. I'm mapping out the eight tables that will present the experimental results—starting with cross-architecture convergence metrics, then per-example indicators, feature comparisons between helped and hurt samples, attention patterns, the 340M model rebound analysis, bootstrap confidence intervals, differentiation from prior work, and finally the co-evolution dynamics. Now I'll write the complete paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed5eb573-f0f8-4d44-9b2e-e9b480df6553",
  "isSidechain": false,
  "requestId": "req_011CbC1i9qjtini1rXnQQxRV",
  "type": "assistant",
  "uuid": "58e5259f-921a-4584-a5a1-a2a2499373d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "c013dfff-9ae5-416a-b5ae-03fba6a5fd1c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016PghmKRBHtJGu1fqbpLTvr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25598,
      "cache_read_input_tokens": 11841,
      "output_tokens": 778,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25598,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 778,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 25598,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25598
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-19T13:33:44.340Z_

Now I have all the data. Let me check what directory exists and write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58e5259f-921a-4584-a5a1-a2a2499373d5",
  "isSidechain": false,
  "requestId": "req_011CbC1i9qjtini1rXnQQxRV",
  "type": "assistant",
  "uuid": "3feded93-d518-4306-b04f-35c4ccda149f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "c013dfff-9ae5-416a-b5ae-03fba6a5fd1c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016PghmKRBHtJGu1fqbpLTvr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25598,
      "cache_read_input_tokens": 11841,
      "output_tokens": 778,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25598,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 778,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 25598,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25598
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-19T13:33:45.615Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01TNMK4hqLzUVgPEnQzWtUTf`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/dream_reports/dream_20260519T131014/median/",
  "description": "List existing files in target directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3feded93-d518-4306-b04f-35c4ccda149f",
  "isSidechain": false,
  "requestId": "req_011CbC1i9qjtini1rXnQQxRV",
  "type": "assistant",
  "uuid": "baac1ecf-b024-46c1-8a9a-c2400c37d4da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "c013dfff-9ae5-416a-b5ae-03fba6a5fd1c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016PghmKRBHtJGu1fqbpLTvr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25598,
      "cache_read_input_tokens": 11841,
      "output_tokens": 778,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25598,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 778,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 25598,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25598
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-19T13:33:45.804Z_

<details><summary>↩ Tool result · `toolu_01TNMK4hqLzUVgPEnQzWtUTf`</summary>

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
  "parentUuid": "baac1ecf-b024-46c1-8a9a-c2400c37d4da",
  "isSidechain": false,
  "promptId": "1470b571-8e3c-450f-9a8f-7768e6cda7c5",
  "type": "user",
  "uuid": "f5215a5d-0353-474f-830e-87ee00e70205",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "baac1ecf-b024-46c1-8a9a-c2400c37d4da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "c013dfff-9ae5-416a-b5ae-03fba6a5fd1c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-19T13:33:48.055Z_

Writing the full LaTeX paper now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5215a5d-0353-474f-830e-87ee00e70205",
  "isSidechain": false,
  "requestId": "req_011CbC1jgHqdWJNHUuwj1RMf",
  "type": "assistant",
  "uuid": "0c29ee51-7cfc-4393-8c59-e91c141c9eec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "c013dfff-9ae5-416a-b5ae-03fba6a5fd1c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011CmNhKy11FQY6tQs3ozsma",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 807,
      "cache_read_input_tokens": 37439,
      "output_tokens": 10064,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 807,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10064,
          "cache_read_input_tokens": 37439,
          "cache_creation_input_tokens": 807,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 807
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

_source line 19 · 2026-05-19T13:36:53.154Z_

<details open><summary>🔧 Tool call — Write · `toolu_01NjcwEhT5Gnur36G9CTG1P9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/dream_reports/dream_20260519T131014/median/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{geometry}\n\\geometry{a4paper, margin=1in}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\\usepackage{array}\n\n\\hypersetup{colorlinks=true, linkcolor=blue, citecolor=blue, urlcolor=blue}\n\n\\newcommand{\\spearman}{\\rho_s}\n\\newcommand{\\ie}{i.e.}\n\\newcommand{\\eg}{e.g.}\n\n\\title{Aggregate Convergence, Per-Example Divergence:\\\\ How Attention Reshapes Hybrid Recurrent Architectures\\\\ on Retrieval Tasks}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%% ============================================================\n%% ABSTRACT\n%% ============================================================\n\\begin{abstract}\nHybrid architectures that interleave linear recurrence with full attention are increasingly dominant in efficient language modeling, yet whether attention homogenizes behavior across different recurrence mechanisms remains poorly understood. Using a publicly available model zoo of 72 hybrid models spanning three architectures (GatedDeltaNet, RetNet, HGRN2), two scales (340M, 1.3B), and six attention ratios, we provide the first quantitative characterization of what we term the \\emph{equalizer effect}: on retrieval-intensive tasks, adding attention layers monotonically reduces cross-architecture performance variance (Spearman $\\rho{=}{-}1.0$, $p{=}0.008$ on LAMBADA; cross-architecture std drops 79\\%). Per-example analysis, however, reveals that this aggregate convergence masks architecture-specific mechanisms---the sample subsets helped or hurt by attention are nearly non-overlapping across architectures (pairwise Jaccard $< 0.10$). This \\emph{equalizer paradox} is scale-dependent: convergence is monotonically complete at 1.3B but partial at 340M, with a non-monotonic rebound at high attention ratios. We identify target token frequency as a shared mechanistic driver (attention disproportionately aids rare-token retrieval across all three architectures, $p < 0.025$) while attention weight analysis reveals architecture-conditioned attention patterns that offer suggestive but not causal mechanistic evidence. These findings hold under bootstrap confidence intervals and survive leave-one-architecture-out sensitivity analysis, though with 30--40\\% effect size reduction. Our results demonstrate that aggregate benchmark convergence can conceal fundamental differences in how architectures process individual examples, with practical implications for architecture selection in deployment.\n\\end{abstract}\n\n%% ============================================================\n%% 1. INTRODUCTION\n%% ============================================================\n\\section{Introduction}\n\nThe design space for efficient language models has rapidly expanded with hybrid architectures that combine linear recurrent layers with full attention layers \\citep{wang2025mzoobenchmarkinghybridllms}. By varying the ratio of attention to recurrence layers, practitioners can trade off between the computational efficiency of recurrence and the expressivity of attention. A natural question arises: as attention layers are added, do different recurrence mechanisms converge to similar behavior, or do architecture-specific effects persist?\n\nWang et al.\\ qualitatively observe that ``performance differences between architectures decrease as the attention ratio increases'' in their 72-model zoo spanning GatedDeltaNet (GDN), RetNet, and HGRN2. However, their work---aimed at benchmarking hybrid architectures rather than analyzing convergence---provides no quantitative characterization of this phenomenon, no per-example analysis of its mechanism, and no investigation of its scale or task dependency.\n\nWe provide the first systematic, quantitative study of this \\emph{equalizer effect}. Our analysis reveals three findings:\n\n\\begin{enumerate}\n    \\item \\textbf{Retrieval-specific convergence.} On LAMBADA, a retrieval-intensive task, adding attention reduces cross-architecture standard deviation by 79\\% with perfect monotonic Spearman correlation ($\\rho{=}{-}1.0$, permutation $p{=}0.008$). This convergence is absent on reasoning-heavy tasks (HellaSwag, WinoGrande, MMLU), with only suggestive evidence on ARC-Easy ($\\rho{=}{-}0.6$, $p{=}0.142$). Whether this pattern generalizes beyond retrieval-intensive tasks remains an open question.\n    \\item \\textbf{Scale-dependent convergence.} Convergence is monotonically complete at 1.3B parameters but partial at 340M, where a non-monotonic rebound occurs at high attention ratios. The 340M rebound disproportionately affects long-context samples with rare target tokens, consistent with a capacity hypothesis. We note that scale and training token count are confounded (20B vs.\\ 100B tokens) and cannot be fully disentangled.\n    \\item \\textbf{The equalizer paradox.} Despite aggregate convergence, per-example analysis reveals that attention acts on nearly non-overlapping sample subsets across architectures (pairwise Jaccard $< 0.10$). GDN and RetNet show net negative effects on LAMBADA while HGRN2 shows net positive effects, yet aggregate scores converge. Attention weight analysis reveals architecture-conditioned patterns (dispersed, primacy-recency, semantic focus) that provide suggestive mechanistic evidence for this paradox.\n\\end{enumerate}\n\nOur contributions are analytical rather than methodological: we introduce a quantitative framework for measuring cross-architecture convergence, demonstrate that aggregate metrics can mask fundamental mechanistic differences, and provide the first per-example characterization of how attention interacts with different recurrence mechanisms.\n\n%% ============================================================\n%% 2. RELATED WORK\n%% ============================================================\n\\section{Related Work}\n\n\\paragraph{Linear recurrent architectures.}\nLinear recurrent models offer subquadratic complexity alternatives to Transformers. GatedDeltaNet \\citep{yang2024gateddeltanetworks} uses gated delta rules for state updates, RetNet \\citep{sun2023retentive} combines linear attention with exponential decay, and HGRN2 \\citep{qin2024hgrn2} employs hierarchical gated recurrence. Each implements a fundamentally different recurrence mechanism, making their comparison under attention injection informative about the role of architecture-specific inductive biases.\n\n\\paragraph{Hybrid architectures.}\nInterleaving attention with recurrence has become a practical paradigm. Jamba \\citep{lieber2024jamba} mixes Mamba with attention; Griffin \\citep{de2024griffin} combines gated linear recurrence with local attention. Wang et al.\\ provide the most systematic study, training 72 models with controlled attention ratios across three architectures and two scales. Their qualitative observation of performance convergence is our starting point.\n\n\\paragraph{Per-example analysis in NLP.}\nInstance-level analysis has a rich history: dataset cartography \\citep{swayamdipta2020dataset}, influence functions \\citep{koh2017understanding}, and pointwise V-information \\citep{ethayarajh2022understanding} all examine model behavior at the individual example level. We adopt a simpler approach---comparing per-example logprob deltas across architectures---that is sufficient to reveal the convergence--divergence paradox.\n\n%% ============================================================\n%% 3. EXPERIMENTAL SETUP\n%% ============================================================\n\\section{Experimental Setup}\n\n\\subsection{Model Zoo}\n\nWe use the publicly available model zoo from Wang et al., comprising 72 hybrid linear recurrent models. The zoo covers three architectures (GatedDeltaNet, RetNet, HGRN2), two parameter scales (340M, 1.3B), and multiple attention ratios. In our notation, \\texttt{h$k$-1} denotes a model with $k$ attention layers out of 24 total layers. The attention ratios tested are 0 (pure recurrent), 1, 3, 6, 8, and 24. Training data volumes differ across scales: 340M models are trained on 20B tokens while 1.3B models are trained on 100B tokens.\n\n\\subsection{Evaluation Protocol}\n\nWe evaluate on six benchmarks using \\texttt{lm-evaluation-harness}: LAMBADA (last-word prediction), ARC-Easy, ARC-Challenge \\citep{clark2018arc}, HellaSwag \\citep{zellers2019hellaswag}, WinoGrande \\citep{sakaguchi2021winogrande}, and MMLU \\citep{hendrycks2021mmlu}. For per-example analysis, we use \\texttt{--log\\_samples} to collect per-example logprobabilities.\n\n\\subsection{Convergence Metrics}\n\nWe measure convergence via cross-architecture standard deviation at each attention ratio: $\\sigma_{\\text{cross}}(k) = \\text{std}(\\{\\text{score}_a(k)\\}_{a \\in \\mathcal{A}})$ where $\\mathcal{A} = \\{\\text{GDN}, \\text{RetNet}, \\text{HGRN2}\\}$. Convergence strength is quantified by Spearman $\\rho$ between attention ratio and $\\sigma_{\\text{cross}}$. Statistical significance is assessed via exact permutation tests ($n{=}5$ ratios excluding pure recurrent baseline).\n\n\\subsection{Per-Example Analysis}\n\nFor each example $x_i$, we compute the delta $\\Delta_i^{a}(k) = \\log p_{a,k}(x_i) - \\log p_{a,0}(x_i)$, measuring the effect of adding $k$ attention layers on architecture $a$'s prediction for $x_i$. We classify examples as ``helped'' ($\\Delta > 0$) or ``hurt'' ($\\Delta < 0$) and compute pairwise Jaccard similarity of helped sets across architectures:\n\\[\nJ(a_1, a_2) = \\frac{|H_{a_1} \\cap H_{a_2}|}{|H_{a_1} \\cup H_{a_2}|}\n\\]\nwhere $H_a = \\{x_i : \\Delta_i^a > 0\\}$.\n\n%% ============================================================\n%% 4. RESULTS\n%% ============================================================\n\\section{Results}\n\n\\subsection{Task-Specific Convergence (Claim 1)}\n\\label{sec:task-specific}\n\nTable~\\ref{tab:convergence} presents the convergence analysis across six benchmarks at 1.3B scale. LAMBADA exhibits the strongest convergence: cross-architecture std drops from 0.024 (pure recurrent) to 0.005 (highest attention ratio), a 79\\% reduction, with a perfect monotonic Spearman $\\rho{=}{-}1.00$ ($p{=}0.008$). ARC-Easy shows a suggestive trend ($\\rho{=}{-}0.60$) but does not reach significance ($p{=}0.142$), consistent with its moderate retrieval demand. The remaining benchmarks---ARC-Challenge ($\\rho{=}{-}0.30$), WinoGrande ($\\rho{=}{-}0.20$), HellaSwag ($\\rho{=}0.10$), and MMLU ($\\rho{=}0.00$)---show no meaningful convergence pattern.\n\nAfter Bonferroni correction for six comparisons (adjusted $\\alpha = 0.0083$), only LAMBADA remains significant. This pattern is consistent with the interpretation that convergence is strongest on tasks with high retrieval demand, but we emphasize that with only one benchmark reaching significance (and one suggestive), we cannot claim a general dose-response relationship. Whether convergence extends to other retrieval-intensive tasks beyond LAMBADA remains an open question.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-architecture convergence strength by benchmark (1.3B scale). $\\rho$: Spearman correlation between attention ratio and cross-architecture std. Significance: **$p<0.01$, *$p<0.05$.}\n\\label{tab:convergence}\n\\begin{tabular}{@{}lllrrl@{}}\n\\toprule\nBenchmark & Retrieval Demand & Baseline Std & Best Std & $\\rho$ & Perm.\\ $p$ \\\\\n\\midrule\nLAMBADA & High (last-word) & 0.024 & 0.005 & $-$1.00 & 0.008** \\\\\nARC-Easy & Medium (knowledge) & 0.018 & 0.011 & $-$0.60 & 0.142 \\\\\nARC-Challenge & Medium-Low & 0.022 & 0.017 & $-$0.30 & 0.383 \\\\\nWinoGrande & Low-Med (coref) & 0.015 & 0.013 & $-$0.20 & 0.544 \\\\\nHellaSwag & Low (commonsense) & 0.012 & 0.013 & 0.10 & 0.872 \\\\\nMMLU & Low (knowledge+reas.) & 0.031 & 0.030 & 0.00 & 0.983 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Per-Example Convergence Analysis}\n\\label{sec:per-example}\n\nTo distinguish genuine non-convergence from statistical underpowering, we conduct per-example analysis on four benchmarks (Table~\\ref{tab:perexample}). On LAMBADA, strong per-example convergence is confirmed: the mean absolute logprob delta is large (0.34) and cross-architecture delta correlation, while low (0.08), reflects systematic but architecture-specific effects. On HellaSwag, per-example analysis confirms the absence of convergence at the individual sample level (cross-architecture delta correlation 0.03, no systematic pattern), ruling out the hypothesis that aggregate non-significance merely reflects insufficient statistical power. ARC-Easy shows an ambiguous signal ($\\rho{=}{-}0.5$ with attention, Jaccard of helped sets $= 0.12$), neither clearly supporting nor refuting per-example convergence. ARC-Challenge shows no per-example convergence (delta correlation $-0.05$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Per-example convergence indicators across benchmarks (1.3B, h24-1 vs.\\ h0).}\n\\label{tab:perexample}\n\\begin{tabular}{@{}lcccl@{}}\n\\toprule\nBenchmark & $|\\Delta|$ (mean) & Cross-arch $\\Delta$ corr. & Jaccard (helped) & Convergence? \\\\\n\\midrule\nLAMBADA & 0.34 & 0.08 & 0.07 & Yes (strong) \\\\\nARC-Easy & 0.12 & 0.18 & 0.12 & Ambiguous \\\\\nARC-Challenge & 0.09 & $-$0.05 & 0.15 & No \\\\\nHellaSwag & 0.06 & 0.03 & 0.22 & No \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Sample Feature Characterization}\n\\label{sec:features}\n\nWe characterize the features distinguishing helped from hurt examples on LAMBADA (Table~\\ref{tab:features}). Target token frequency is the only feature reaching significance across all three architectures: attention disproportionately helps examples with rare target tokens (GDN $p{=}0.003$, $d{=}{-}0.41$; RetNet $p{=}0.008$, $d{=}{-}0.33$; HGRN2 $p{=}0.022$, $d{=}{-}0.24$). This is mechanistically interpretable: attention's global context window enables retrieval of rare tokens that recurrence alone---with its compressed state representation---cannot reliably access.\n\nContext length shows a consistent but non-significant trend ($p$ values 0.062--0.134), suggesting attention may additionally benefit longer-context examples. Last-sentence perplexity and domain distribution do not significantly predict helped/hurt status.\n\nCrucially, the effect size for target token frequency varies across architectures (GDN $d{=}0.41$ vs.\\ HGRN2 $d{=}0.24$), consistent with HGRN2's hierarchical gating partially compensating for the rare-token retrieval limitation. Despite this shared feature-level signal, the actual helped/hurt sample subsets remain architecture-specific (pairwise Jaccard $= 0.08$), indicating that token frequency is a partial but not complete mechanistic explanation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Feature comparison between helped and hurt samples per architecture (LAMBADA, 1.3B, h24-1 vs.\\ h0). $d$: Cohen's $d$; negative $d$ for token frequency indicates attention helps rare tokens.}\n\\label{tab:features}\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\n\\multirow{2}{*}{Feature} & \\multicolumn{2}{c}{GDN} & \\multicolumn{2}{c}{RetNet} & \\multicolumn{2}{c}{HGRN2} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5} \\cmidrule(lr){6-7}\n & $p$ & $d$ & $p$ & $d$ & $p$ & $d$ \\\\\n\\midrule\nTarget token freq & 0.003** & $-$0.41 & 0.008** & $-$0.33 & 0.022* & $-$0.24 \\\\\nContext length & 0.087 & 0.19 & 0.134 & 0.15 & 0.062 & 0.22 \\\\\nLast-sent.\\ perplexity & 0.214 & 0.12 & 0.378 & 0.08 & 0.156 & 0.14 \\\\\nDomain entropy & 0.341 & --- & 0.287 & --- & 0.512 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Attention Pattern Analysis}\n\\label{sec:attention}\n\nTable~\\ref{tab:attention} presents the attention weight analysis for h3-1 models (3 attention layers out of 24). Attention patterns show moderate correlation with per-example helped/hurt status (mean $r{=}0.31$ across architectures), indicating a detectable but incomplete relationship between attention allocation and individual-example effects.\n\nThe three architectures develop qualitatively different attention patterns despite sharing the same attention mechanism: GDN's attention disperses across mid-context positions, RetNet's concentrates on primacy and recency positions, and HGRN2's focuses on semantically related positions. Cross-architecture cosine similarity is moderate (mean 0.42), reflecting partial overlap that may be driven by task-level inductive biases from LAMBADA.\n\nThese results provide suggestive mechanistic evidence that attention adapts its behavior to complement the specific recurrence mechanism it is paired with. However, the moderate correlation strength (0.24--0.37) means attention patterns alone do not fully explain the per-example effects; changes in recurrence state likely contribute as a complementary mechanism that we cannot directly observe.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Attention pattern analysis for h3-1 models on LAMBADA (1.3B). Cross-arch cosine similarities are between architectures (GDN/RetNet/HGRN2).}\n\\label{tab:attention}\n\\begin{tabular}{@{}lcll@{}}\n\\toprule\nArchitecture & Attn--Helped/Hurt Corr. & Dominant Pattern & Cross-arch Cosine \\\\\n\\midrule\nGDN & 0.31 & Dispersed mid-context & ---~/~0.38~/~0.44 \\\\\nRetNet & 0.24 & Primacy-recency & 0.38~/~---~/~0.45 \\\\\nHGRN2 & 0.37 & Semantic focus & 0.44~/~0.45~/~--- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Scale-Dependent Convergence}\n\\label{sec:scale}\n\nTable~\\ref{tab:rebound} summarizes the 340M rebound analysis. At 1.3B, cross-architecture std decreases monotonically with attention ratio. At 340M, convergence proceeds similarly until attention ratio 6, but at ratio 8 the cross-architecture std increases by 35\\% (from 0.014 at ratio 6 to 0.019 at ratio 8). Per-example analysis reveals that the rebound disproportionately affects long-context examples (mean 94.2 tokens) with rare target tokens (mean frequency rank 8,420), consistent with a \\emph{capacity hypothesis}: at 340M, attention layers and recurrence layers compete for limited model capacity, and high attention ratios compromise recurrence quality for the most demanding examples.\n\nThe rebound samples moderately overlap with those helped by attention at 1.3B (Jaccard $= 0.28$), suggesting these are inherently difficult examples that require both strong recurrence and attention---a combination achievable at 1.3B but not at 340M.\n\nWe note an important confound: 340M models are trained on 20B tokens while 1.3B models are trained on 100B tokens. We cannot fully disentangle whether the scale-dependent convergence reflects model capacity, training duration, or their interaction.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{340M rebound analysis: per-example comparison at attention ratio 8.}\n\\label{tab:rebound}\n\\begin{tabular}{@{}llll@{}}\n\\toprule\nMetric & 340M & 1.3B & Interpretation \\\\\n\\midrule\nCross-arch std (attn=8) & 0.019 ($\\uparrow$35\\%) & 0.008 ($\\downarrow$ mono.) & Rebound at 340M only \\\\\nRebound: mean ctx length & 94.2 tokens & N/A & Long-context affected \\\\\nRebound: mean tgt freq rank & 8,420 & N/A & Rare tokens affected \\\\\nOverlap w/ 1.3B helped & \\multicolumn{2}{c}{Jaccard = 0.28} & Moderate overlap \\\\\nTraining tokens & 20B & 100B & Confounded with scale \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{The Equalizer Paradox: Convergence--Divergence Co-evolution}\n\\label{sec:paradox}\n\nTable~\\ref{tab:coevolution} and the convergence--divergence co-evolution analysis reveal the central paradox of this paper. As attention ratio increases, aggregate cross-architecture std monotonically decreases (0.024 $\\to$ 0.005) while per-example net effect asymmetry monotonically increases (0.12 $\\to$ 0.31). These two trends are significantly anti-correlated ($\\rho{=}{-}0.83$, $p{=}0.042$).\n\nThis means that the more attention homogenizes aggregate performance, the more divergent the per-example mechanisms become. At the highest attention ratio (h24-1), architectures achieve nearly identical aggregate scores on LAMBADA, but each architecture arrives at this score by helping and hurting almost entirely different subsets of examples. The pairwise Jaccard similarity of helped sets decreases from 0.14 (one attention layer) to 0.07 (24 attention layers), reflecting increasing architecture-specificity of the attention-mediated effects.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Co-evolution of aggregate convergence and per-example divergence (LAMBADA, 1.3B). Net effect asymmetry measures the divergence in per-architecture improvement directions.}\n\\label{tab:coevolution}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nAttention Ratio & Cross-arch Std & Jaccard (mean) & Net Effect Asymmetry \\\\\n\\midrule\n0 (pure) & 0.024 & --- & --- \\\\\n1 (h1-1) & 0.019 & 0.14 & 0.12 \\\\\n3 (h3-1) & 0.014 & 0.11 & 0.18 \\\\\n6 (h6-1) & 0.009 & 0.09 & 0.24 \\\\\n8 (h8-1) & 0.007 & 0.08 & 0.27 \\\\\n24 (h24-1) & 0.005 & 0.07 & 0.31 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Statistical Robustness}\n\\label{sec:robustness}\n\nTable~\\ref{tab:robustness} presents bootstrap confidence intervals and leave-one-architecture-out sensitivity analysis. Key results survive robustness checks but with reduced effect sizes:\n\n\\begin{itemize}\n    \\item LAMBADA std reduction: 79\\% point estimate, bootstrap 95\\% CI [58\\%, 72\\%]. Excluding GDN: 52\\%, CI [38\\%, 61\\%].\n    \\item LAMBADA Spearman $\\rho$: $-$1.00, CI [$-$1.0, $-$0.80]. Excluding GDN: $-$0.90, CI [$-$1.0, $-$0.60].\n    \\item Cohen's $d$ for convergence effect: 1.12, CI [0.74, 1.48]. Excluding GDN: 0.73, CI [0.41, 1.05].\n\\end{itemize}\n\nBootstrap CIs do not cross zero for any core metric, establishing that the convergence effect is not a statistical artifact. However, GDN contributes disproportionately to the effect---excluding it reduces effect sizes by 25--35\\%. This is interpretable: GDN's gated delta rule mechanism may be most responsive to attention injection, making it the strongest ``equalizer'' responder. Nevertheless, convergence remains substantial with only RetNet and HGRN2 (52\\% std reduction, Cohen's $d = 0.73$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Bootstrap confidence intervals and sensitivity analysis. ``Full'' uses all three architectures; ``Excl.\\ GDN'' removes GatedDeltaNet.}\n\\label{tab:robustness}\n\\begin{tabular}{@{}lccccr@{}}\n\\toprule\nMetric & Full & 95\\% CI & Excl.\\ GDN & 95\\% CI & $\\Delta$\\% \\\\\n\\midrule\nLAMBADA std red.\\ (\\%) & 79 & [58, 72] & 52 & [38, 61] & $-$34 \\\\\nLAMBADA $\\rho$ & $-$1.00 & [$-$1.0, $-$0.80] & $-$0.90 & [$-$1.0, $-$0.60] & --- \\\\\nCohen's $d$ & 1.12 & [0.74, 1.48] & 0.73 & [0.41, 1.05] & $-$35 \\\\\nJaccard (mean) & 0.08 & [0.05, 0.12] & 0.06 & [0.03, 0.10] & $-$25 \\\\\nClaims surviving & 3/3 & --- & 2/3 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ============================================================\n%% 5. COMPARISON WITH WANG ET AL.\n%% ============================================================\n\\section{Relationship to Wang et al.\\ (2025)}\n\nOur work builds directly on the model zoo of Wang et al.\\ and is complementary to their benchmarking study. Table~\\ref{tab:differentiation} summarizes the analytical dimensions we add. Wang et al.\\ qualitatively observe that ``models with higher attention ratios tend to perform more similarly'' and ``the choice of recurrence mechanism becomes less important at higher attention ratios.'' We formalize this observation through a quantitative convergence framework with statistical testing, extend it to per-example granularity, and uncover the convergence--divergence paradox that is invisible in aggregate metrics.\n\nWe emphasize that this is not a critique of Wang et al.---their contribution is the model zoo itself, and convergence analysis was not their research question. Our work demonstrates the analytical value that systematic per-example investigation can extract from shared experimental infrastructure.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Analytical contributions beyond Wang et al.\\ (2025).}\n\\label{tab:differentiation}\n\\begin{tabular}{@{}p{3cm}p{4.2cm}p{4.8cm}@{}}\n\\toprule\nDimension & Wang et al. & This Work \\\\\n\\midrule\nConvergence & Qualitative (``tend to perform similarly'') & Quantitative ($\\rho$, std trajectory, bootstrap CI) \\\\\nPer-example & Not performed & Full logprob analysis, Jaccard, helped/hurt \\\\\nScale dependency & Not characterized & Binary contrast: 340M partial vs.\\ 1.3B complete \\\\\nMechanistic & Not performed & Sample feature characterization, attention patterns \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ============================================================\n%% 6. DISCUSSION\n%% ============================================================\n\\section{Discussion}\n\n\\paragraph{Practical implications.}\nThe equalizer paradox has direct consequences for architecture selection. When aggregate benchmarks show convergence across hybrid architectures, practitioners might conclude that the choice of recurrence mechanism is unimportant. Our per-example analysis shows this conclusion is misleading: architectures that appear equivalent in aggregate may fail on different subsets of inputs. For applications where per-example reliability matters---machine translation, question answering, retrieval-augmented generation---the specific recurrence mechanism remains consequential even at high attention ratios.\n\n\\paragraph{Mechanistic interpretation.}\nTarget token frequency emerges as a shared mechanistic driver: attention universally aids rare-token retrieval across architectures. However, the varying effect sizes (Cohen's $d$ from 0.24 to 0.41) and low cross-architecture Jaccard suggest that each recurrence mechanism has different ``blind spots'' that attention compensates for. The qualitative differences in attention patterns (dispersed vs.\\ primacy-recency vs.\\ semantic focus) are consistent with attention adapting to complement the specific information bottleneck of each recurrence mechanism. We emphasize that this is suggestive mechanistic evidence, not a causal demonstration---the recurrence state changes induced by attention layer presence likely contribute as an unobservable complementary mechanism.\n\n\\paragraph{Why retrieval tasks?}\nLAMBADA requires predicting a final word based on distant context---a retrieval operation that exercises exactly the capacity that attention provides (global context access) and that recurrence compresses away. Reasoning-heavy tasks like HellaSwag require integrating local coherence cues where recurrence may already be sufficient, explaining the absence of convergence. ARC-Easy's intermediate position ($\\rho{=}{-}0.6$) is consistent with its partial reliance on knowledge retrieval, but we acknowledge this explanation is post-hoc and the statistical evidence is insufficient.\n\n%% ============================================================\n%% 7. LIMITATIONS\n%% ============================================================\n\\section{Limitations}\n\n\\paragraph{Architecture coverage (n=3).}\nOur analysis covers three architectures: GatedDeltaNet, RetNet, and HGRN2. These represent three distinct recurrence mechanisms (gated delta rule, linear attention with exponential decay, hierarchical gated recurrence) and are all publicly available hybrid architectures from Wang et al.'s zoo. However, important architectures such as Mamba/Mamba-2 hybrids, RWKV hybrids, and Griffin lack public checkpoints with controlled attention ratios. Generalization of the equalizer effect to other recurrence families is an open question.\n\n\\paragraph{Task coverage.}\nOnly LAMBADA shows statistically significant convergence after multiple comparison correction. While we provide a retrieval-demand interpretation, this relies on a single significant benchmark, making the task-specificity claim inherently underpowered. Future work with additional retrieval-intensive benchmarks (e.g., natural questions, passage retrieval) is needed.\n\n\\paragraph{Scale confound.}\nThe 340M and 1.3B models differ in both parameter count and training data volume (20B vs.\\ 100B tokens). We cannot determine whether scale-dependent convergence reflects model capacity, training duration, or their interaction. No 7B-scale models are available in the model zoo.\n\n\\paragraph{Statistical power.}\nWith only 5 attention ratios per architecture, Spearman correlation has limited statistical power ($n{=}5$). ARC-Easy's $\\rho{=}{-}0.6$ ($p{=}0.142$) might reach significance with more attention ratio data points. Bootstrap CIs are correspondingly wide (e.g., LAMBADA $\\rho$ CI width $= 0.2$). The convergence--divergence co-evolution correlation ($\\rho{=}{-}0.83$, $p{=}0.042$) is borderline significant and sensitive to individual data points.\n\n\\paragraph{GDN dependency.}\nGatedDeltaNet contributes disproportionately to the convergence signal; excluding it reduces effect sizes by 30--40\\%. While claims survive this sensitivity analysis, the reduced effect sizes mean our strongest results are partially GDN-dependent.\n\n%% ============================================================\n%% 8. CONCLUSION\n%% ============================================================\n\\section{Conclusion}\n\nWe have provided the first quantitative characterization of the equalizer effect in hybrid linear recurrent architectures. On retrieval-intensive tasks, adding attention layers monotonically reduces cross-architecture performance variance at sufficient scale, yet per-example analysis reveals this convergence is achieved through architecture-specific, largely non-overlapping mechanisms. This equalizer paradox---aggregate convergence masking per-example divergence---challenges the assumption that converging benchmark scores imply converging model behavior. Whether this phenomenon extends beyond retrieval-intensive tasks and beyond the three architectures studied here remains an important direction for future work.\n\n%% ============================================================\n%% REFERENCES\n%% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{10}\n\n\\bibitem[Clark et al.(2018)]{clark2018arc}\nClark, P., Cowhey, I., Etzioni, O., Khot, T., Sabharwal, A., Schoenick, C., and Tafjord, O. (2018).\n\\newblock Think you have solved question answering? {T}ry {ARC}, the {AI2} reasoning challenge.\n\\newblock \\emph{arXiv preprint arXiv:1803.05457}.\n\n\\bibitem[De~Mesmay et al.(2024)]{de2024griffin}\nDe~Mesmay, A., Botev, A., Sherburn, D., et al. (2024).\n\\newblock Griffin: Mixing gated linear recurrences with local attention for efficient language models.\n\\newblock \\emph{arXiv preprint arXiv:2402.19427}.\n\n\\bibitem[Ethayarajh et al.(2022)]{ethayarajh2022understanding}\nEthayarajh, K., Choi, Y., and Swayamdipta, S. (2022).\n\\newblock Understanding dataset difficulty with $\\mathcal{V}$-usable information.\n\\newblock In \\emph{Proceedings of ICML}.\n\n\\bibitem[Hendrycks et al.(2021)]{hendrycks2021mmlu}\nHendrycks, D., Burns, C., Basart, S., Zou, A., Mazeika, M., Song, D., and Steinhardt, J. (2021).\n\\newblock Measuring massive multitask language understanding.\n\\newblock In \\emph{Proceedings of ICLR}.\n\n\\bibitem[Koh and Liang(2017)]{koh2017understanding}\nKoh, P.~W. and Liang, P. (2017).\n\\newblock Understanding black-box predictions via influence functions.\n\\newblock In \\emph{Proceedings of ICML}.\n\n\\bibitem[Lieber et al.(2024)]{lieber2024jamba}\nLieber, O., Lenz, B., Bata, H., et al. (2024).\n\\newblock Jamba: A hybrid {T}ransformer-{M}amba language model.\n\\newblock \\emph{arXiv preprint arXiv:2403.19887}.\n\n\\bibitem[Qin et al.(2024)]{qin2024hgrn2}\nQin, Z., Li, D., Sun, W., Sun, W., Shen, X., Han, X., and Wei, Y. (2024).\n\\newblock {HGRN2}: Gated linear {RNN}s with state expansion.\n\\newblock \\emph{arXiv preprint arXiv:2404.07904}.\n\n\\bibitem[Sakaguchi et al.(2021)]{sakaguchi2021winogrande}\nSakaguchi, K., Le~Bras, R., Bhagavatula, C., and Choi, Y. (2021).\n\\newblock {WinoGrande}: An adversarial {W}inograd schema challenge at scale.\n\\newblock \\emph{Communications of the ACM}, 64(9):99--106.\n\n\\bibitem[Sun et al.(2023)]{sun2023retentive}\nSun, Y., Dong, L., Huang, S., Ma, S., Xia, Y., Xue, J., Wang, J., and Wei, F. (2023).\n\\newblock Retentive network: A successor to {T}ransformer for large language models.\n\\newblock \\emph{arXiv preprint arXiv:2307.08621}.\n\n\\bibitem[Swayamdipta et al.(2020)]{swayamdipta2020dataset}\nSwayamdipta, S., Schwartz, R., Lourie, N., Wang, Y., Hajishirzi, H., Smith, N.~A., and Choi, Y. (2020).\n\\newblock Dataset cartography: Mapping and diagnosing datasets with training dynamics.\n\\newblock In \\emph{Proceedings of EMNLP}.\n\n\\bibitem[Wang et al.(2025)]{wang2025mzoobenchmarkinghybridllms}\nWang, J., Ren, L., et al. (2025).\n\\newblock MZoo: Benchmarking hybrid {LLM}s with a model zoo of linear recurrent architectures.\n\\newblock \\emph{arXiv preprint arXiv:2507.06457}.\n\n\\bibitem[Yang et al.(2024)]{yang2024gateddeltanetworks}\nYang, S., Wang, B., Shen, Y., Panda, R., and Kim, Y. (2024).\n\\newblock Gated delta networks: Improving mamba2 with delta rule.\n\\newblock \\emph{arXiv preprint arXiv:2412.06464}.\n\n\\bibitem[Zellers et al.(2019)]{zellers2019hellaswag}\nZellers, R., Holtzman, A., Bisk, Y., Farhadi, A., and Choi, Y. (2019).\n\\newblock {HellaSwag}: Can a machine really finish your sentence?\n\\newblock In \\emph{Proceedings of ACL}.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c29ee51-7cfc-4393-8c59-e91c141c9eec",
  "isSidechain": false,
  "requestId": "req_011CbC1jgHqdWJNHUuwj1RMf",
  "type": "assistant",
  "uuid": "ada232c0-eb29-43e9-a28d-0de61eb16c45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "c013dfff-9ae5-416a-b5ae-03fba6a5fd1c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011CmNhKy11FQY6tQs3ozsma",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 807,
      "cache_read_input_tokens": 37439,
      "output_tokens": 10064,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 807,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10064,
          "cache_read_input_tokens": 37439,
          "cache_creation_input_tokens": 807,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 807
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

_source line 20 · 2026-05-19T13:36:53.181Z_

<details><summary>↩ Tool result · `toolu_01NjcwEhT5Gnur36G9CTG1P9`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/dream_reports/dream_20260519T131014/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ada232c0-eb29-43e9-a28d-0de61eb16c45",
  "isSidechain": false,
  "promptId": "1470b571-8e3c-450f-9a8f-7768e6cda7c5",
  "type": "user",
  "uuid": "747f2534-8424-4b4f-94cd-d1f9e2e8b877",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/dream_reports/dream_20260519T131014/median/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{geometry}\n\\geometry{a4paper, margin=1in}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\\usepackage{array}\n\n\\hypersetup{colorlinks=true, linkcolor=blue, citecolor=blue, urlcolor=blue}\n\n\\newcommand{\\spearman}{\\rho_s}\n\\newcommand{\\ie}{i.e.}\n\\newcommand{\\eg}{e.g.}\n\n\\title{Aggregate Convergence, Per-Example Divergence:\\\\ How Attention Reshapes Hybrid Recurrent Architectures\\\\ on Retrieval Tasks}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%% ============================================================\n%% ABSTRACT\n%% ============================================================\n\\begin{abstract}\nHybrid architectures that interleave linear recurrence with full attention are increasingly dominant in efficient language modeling, yet whether attention homogenizes behavior across different recurrence mechanisms remains poorly understood. Using a publicly available model zoo of 72 hybrid models spanning three architectures (GatedDeltaNet, RetNet, HGRN2), two scales (340M, 1.3B), and six attention ratios, we provide the first quantitative characterization of what we term the \\emph{equalizer effect}: on retrieval-intensive tasks, adding attention layers monotonically reduces cross-architecture performance variance (Spearman $\\rho{=}{-}1.0$, $p{=}0.008$ on LAMBADA; cross-architecture std drops 79\\%). Per-example analysis, however, reveals that this aggregate convergence masks architecture-specific mechanisms---the sample subsets helped or hurt by attention are nearly non-overlapping across architectures (pairwise Jaccard $< 0.10$). This \\emph{equalizer paradox} is scale-dependent: convergence is monotonically complete at 1.3B but partial at 340M, with a non-monotonic rebound at high attention ratios. We identify target token frequency as a shared mechanistic driver (attention disproportionately aids rare-token retrieval across all three architectures, $p < 0.025$) while attention weight analysis reveals architecture-conditioned attention patterns that offer suggestive but not causal mechanistic evidence. These findings hold under bootstrap confidence intervals and survive leave-one-architecture-out sensitivity analysis, though with 30--40\\% effect size reduction. Our results demonstrate that aggregate benchmark convergence can conceal fundamental differences in how architectures process individual examples, with practical implications for architecture selection in deployment.\n\\end{abstract}\n\n%% ============================================================\n%% 1. INTRODUCTION\n%% ============================================================\n\\section{Introduction}\n\nThe design space for efficient language models has rapidly expanded with hybrid architectures that combine linear recurrent layers with full attention layers \\citep{wang2025mzoobenchmarkinghybridllms}. By varying the ratio of attention to recurrence layers, practitioners can trade off between the computational efficiency of recurrence and the expressivity of attention. A natural question arises: as attention layers are added, do different recurrence mechanisms converge to similar behavior, or do architecture-specific effects persist?\n\nWang et al.\\ qualitatively observe that ``performance differences between architectures decrease as the attention ratio increases'' in their 72-model zoo spanning GatedDeltaNet (GDN), RetNet, and HGRN2. However, their work---aimed at benchmarking hybrid architectures rather than analyzing convergence---provides no quantitative characterization of this phenomenon, no per-example analysis of its mechanism, and no investigation of its scale or task dependency.\n\nWe provide the first systematic, quantitative study of this \\emph{equalizer effect}. Our analysis reveals three findings:\n\n\\begin{enumerate}\n    \\item \\textbf{Retrieval-specific convergence.} On LAMBADA, a retrieval-intensive task, adding attention reduces cross-architecture standard deviation by 79\\% with perfect monotonic Spearman correlation ($\\rho{=}{-}1.0$, permutation $p{=}0.008$). This convergence is absent on reasoning-heavy tasks (HellaSwag, WinoGrande, MMLU), with only suggestive evidence on ARC-Easy ($\\rho{=}{-}0.6$, $p{=}0.142$). Whether this pattern generalizes beyond retrieval-intensive tasks remains an open question.\n    \\item \\textbf{Scale-dependent convergence.} Convergence is monotonically complete at 1.3B parameters but partial at 340M, where a non-monotonic rebound occurs at high attention ratios. The 340M rebound disproportionately affects long-context samples with rare target tokens, consistent with a capacity hypothesis. We note that scale and training token count are confounded (20B vs.\\ 100B tokens) and cannot be fully disentangled.\n    \\item \\textbf{The equalizer paradox.} Despite aggregate convergence, per-example analysis reveals that attention acts on nearly non-overlapping sample subsets across architectures (pairwise Jaccard $< 0.10$). GDN and RetNet show net negative effects on LAMBADA while HGRN2 shows net positive effects, yet aggregate scores converge. Attention weight analysis reveals architecture-conditioned patterns (dispersed, primacy-recency, semantic focus) that provide suggestive mechanistic evidence for this paradox.\n\\end{enumerate}\n\nOur contributions are analytical rather than methodological: we introduce a quantitative framework for measuring cross-architecture convergence, demonstrate that aggregate metrics can mask fundamental mechanistic differences, and provide the first per-example characterization of how attention interacts with different recurrence mechanisms.\n\n%% ============================================================\n%% 2. RELATED WORK\n%% ============================================================\n\\section{Related Work}\n\n\\paragraph{Linear recurrent architectures.}\nLinear recurrent models offer subquadratic complexity alternatives to Transformers. GatedDeltaNet \\citep{yang2024gateddeltanetworks} uses gated delta rules for state updates, RetNet \\citep{sun2023retentive} combines linear attention with exponential decay, and HGRN2 \\citep{qin2024hgrn2} employs hierarchical gated recurrence. Each implements a fundamentally different recurrence mechanism, making their comparison under attention injection informative about the role of architecture-specific inductive biases.\n\n\\paragraph{Hybrid architectures.}\nInterleaving attention with recurrence has become a practical paradigm. Jamba \\citep{lieber2024jamba} mixes Mamba with attention; Griffin \\citep{de2024griffin} combines gated linear recurrence with local attention. Wang et al.\\ provide the most systematic study, training 72 models with controlled attention ratios across three architectures and two scales. Their qualitative observation of performance convergence is our starting point.\n\n\\paragraph{Per-example analysis in NLP.}\nInstance-level analysis has a rich history: dataset cartography \\citep{swayamdipta2020dataset}, influence functions \\citep{koh2017understanding}, and pointwise V-information \\citep{ethayarajh2022understanding} all examine model behavior at the individual example level. We adopt a simpler approach---comparing per-example logprob deltas across architectures---that is sufficient to reveal the convergence--divergence paradox.\n\n%% ============================================================\n%% 3. EXPERIMENTAL SETUP\n%% ============================================================\n\\section{Experimental Setup}\n\n\\subsection{Model Zoo}\n\nWe use the publicly available model zoo from Wang et al., comprising 72 hybrid linear recurrent models. The zoo covers three architectures (GatedDeltaNet, RetNet, HGRN2), two parameter scales (340M, 1.3B), and multiple attention ratios. In our notation, \\texttt{h$k$-1} denotes a model with $k$ attention layers out of 24 total layers. The attention ratios tested are 0 (pure recurrent), 1, 3, 6, 8, and 24. Training data volumes differ across scales: 340M models are trained on 20B tokens while 1.3B models are trained on 100B tokens.\n\n\\subsection{Evaluation Protocol}\n\nWe evaluate on six benchmarks using \\texttt{lm-evaluation-harness}: LAMBADA (last-word prediction), ARC-Easy, ARC-Challenge \\citep{clark2018arc}, HellaSwag \\citep{zellers2019hellaswag}, WinoGrande \\citep{sakaguchi2021winogrande}, and MMLU \\citep{hendrycks2021mmlu}. For per-example analysis, we use \\texttt{--log\\_samples} to collect per-example logprobabilities.\n\n\\subsection{Convergence Metrics}\n\nWe measure convergence via cross-architecture standard deviation at each attention ratio: $\\sigma_{\\text{cross}}(k) = \\text{std}(\\{\\text{score}_a(k)\\}_{a \\in \\mathcal{A}})$ where $\\mathcal{A} = \\{\\text{GDN}, \\text{RetNet}, \\text{HGRN2}\\}$. Convergence strength is quantified by Spearman $\\rho$ between attention ratio and $\\sigma_{\\text{cross}}$. Statistical significance is assessed via exact permutation tests ($n{=}5$ ratios excluding pure recurrent baseline).\n\n\\subsection{Per-Example Analysis}\n\nFor each example $x_i$, we compute the delta $\\Delta_i^{a}(k) = \\log p_{a,k}(x_i) - \\log p_{a,0}(x_i)$, measuring the effect of adding $k$ attention layers on architecture $a$'s prediction for $x_i$. We classify examples as ``helped'' ($\\Delta > 0$) or ``hurt'' ($\\Delta < 0$) and compute pairwise Jaccard similarity of helped sets across architectures:\n\\[\nJ(a_1, a_2) = \\frac{|H_{a_1} \\cap H_{a_2}|}{|H_{a_1} \\cup H_{a_2}|}\n\\]\nwhere $H_a = \\{x_i : \\Delta_i^a > 0\\}$.\n\n%% ============================================================\n%% 4. RESULTS\n%% ============================================================\n\\section{Results}\n\n\\subsection{Task-Specific Convergence (Claim 1)}\n\\label{sec:task-specific}\n\nTable~\\ref{tab:convergence} presents the convergence analysis across six benchmarks at 1.3B scale. LAMBADA exhibits the strongest convergence: cross-architecture std drops from 0.024 (pure recurrent) to 0.005 (highest attention ratio), a 79\\% reduction, with a perfect monotonic Spearman $\\rho{=}{-}1.00$ ($p{=}0.008$). ARC-Easy shows a suggestive trend ($\\rho{=}{-}0.60$) but does not reach significance ($p{=}0.142$), consistent with its moderate retrieval demand. The remaining benchmarks---ARC-Challenge ($\\rho{=}{-}0.30$), WinoGrande ($\\rho{=}{-}0.20$), HellaSwag ($\\rho{=}0.10$), and MMLU ($\\rho{=}0.00$)---show no meaningful convergence pattern.\n\nAfter Bonferroni correction for six comparisons (adjusted $\\alpha = 0.0083$), only LAMBADA remains significant. This pattern is consistent with the interpretation that convergence is strongest on tasks with high retrieval demand, but we emphasize that with only one benchmark reaching significance (and one suggestive), we cannot claim a general dose-response relationship. Whether convergence extends to other retrieval-intensive tasks beyond LAMBADA remains an open question.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-architecture convergence strength by benchmark (1.3B scale). $\\rho$: Spearman correlation between attention ratio and cross-architecture std. Significance: **$p<0.01$, *$p<0.05$.}\n\\label{tab:convergence}\n\\begin{tabular}{@{}lllrrl@{}}\n\\toprule\nBenchmark & Retrieval Demand & Baseline Std & Best Std & $\\rho$ & Perm.\\ $p$ \\\\\n\\midrule\nLAMBADA & High (last-word) & 0.024 & 0.005 & $-$1.00 & 0.008** \\\\\nARC-Easy & Medium (knowledge) & 0.018 & 0.011 & $-$0.60 & 0.142 \\\\\nARC-Challenge & Medium-Low & 0.022 & 0.017 & $-$0.30 & 0.383 \\\\\nWinoGrande & Low-Med (coref) & 0.015 & 0.013 & $-$0.20 & 0.544 \\\\\nHellaSwag & Low (commonsense) & 0.012 & 0.013 & 0.10 & 0.872 \\\\\nMMLU & Low (knowledge+reas.) & 0.031 & 0.030 & 0.00 & 0.983 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Per-Example Convergence Analysis}\n\\label{sec:per-example}\n\nTo distinguish genuine non-convergence from statistical underpowering, we conduct per-example analysis on four benchmarks (Table~\\ref{tab:perexample}). On LAMBADA, strong per-example convergence is confirmed: the mean absolute logprob delta is large (0.34) and cross-architecture delta correlation, while low (0.08), reflects systematic but architecture-specific effects. On HellaSwag, per-example analysis confirms the absence of convergence at the individual sample level (cross-architecture delta correlation 0.03, no systematic pattern), ruling out the hypothesis that aggregate non-significance merely reflects insufficient statistical power. ARC-Easy shows an ambiguous signal ($\\rho{=}{-}0.5$ with attention, Jaccard of helped sets $= 0.12$), neither clearly supporting nor refuting per-example convergence. ARC-Challenge shows no per-example convergence (delta correlation $-0.05$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Per-example convergence indicators across benchmarks (1.3B, h24-1 vs.\\ h0).}\n\\label{tab:perexample}\n\\begin{tabular}{@{}lcccl@{}}\n\\toprule\nBenchmark & $|\\Delta|$ (mean) & Cross-arch $\\Delta$ corr. & Jaccard (helped) & Convergence? \\\\\n\\midrule\nLAMBADA & 0.34 & 0.08 & 0.07 & Yes (strong) \\\\\nARC-Easy & 0.12 & 0.18 & 0.12 & Ambiguous \\\\\nARC-Challenge & 0.09 & $-$0.05 & 0.15 & No \\\\\nHellaSwag & 0.06 & 0.03 & 0.22 & No \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Sample Feature Characterization}\n\\label{sec:features}\n\nWe characterize the features distinguishing helped from hurt examples on LAMBADA (Table~\\ref{tab:features}). Target token frequency is the only feature reaching significance across all three architectures: attention disproportionately helps examples with rare target tokens (GDN $p{=}0.003$, $d{=}{-}0.41$; RetNet $p{=}0.008$, $d{=}{-}0.33$; HGRN2 $p{=}0.022$, $d{=}{-}0.24$). This is mechanistically interpretable: attention's global context window enables retrieval of rare tokens that recurrence alone---with its compressed state representation---cannot reliably access.\n\nContext length shows a consistent but non-significant trend ($p$ values 0.062--0.134), suggesting attention may additionally benefit longer-context examples. Last-sentence perplexity and domain distribution do not significantly predict helped/hurt status.\n\nCrucially, the effect size for target token frequency varies across architectures (GDN $d{=}0.41$ vs.\\ HGRN2 $d{=}0.24$), consistent with HGRN2's hierarchical gating partially compensating for the rare-token retrieval limitation. Despite this shared feature-level signal, the actual helped/hurt sample subsets remain architecture-specific (pairwise Jaccard $= 0.08$), indicating that token frequency is a partial but not complete mechanistic explanation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Feature comparison between helped and hurt samples per architecture (LAMBADA, 1.3B, h24-1 vs.\\ h0). $d$: Cohen's $d$; negative $d$ for token frequency indicates attention helps rare tokens.}\n\\label{tab:features}\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\n\\multirow{2}{*}{Feature} & \\multicolumn{2}{c}{GDN} & \\multicolumn{2}{c}{RetNet} & \\multicolumn{2}{c}{HGRN2} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5} \\cmidrule(lr){6-7}\n & $p$ & $d$ & $p$ & $d$ & $p$ & $d$ \\\\\n\\midrule\nTarget token freq & 0.003** & $-$0.41 & 0.008** & $-$0.33 & 0.022* & $-$0.24 \\\\\nContext length & 0.087 & 0.19 & 0.134 & 0.15 & 0.062 & 0.22 \\\\\nLast-sent.\\ perplexity & 0.214 & 0.12 & 0.378 & 0.08 & 0.156 & 0.14 \\\\\nDomain entropy & 0.341 & --- & 0.287 & --- & 0.512 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Attention Pattern Analysis}\n\\label{sec:attention}\n\nTable~\\ref{tab:attention} presents the attention weight analysis for h3-1 models (3 attention layers out of 24). Attention patterns show moderate correlation with per-example helped/hurt status (mean $r{=}0.31$ across architectures), indicating a detectable but incomplete relationship between attention allocation and individual-example effects.\n\nThe three architectures develop qualitatively different attention patterns despite sharing the same attention mechanism: GDN's attention disperses across mid-context positions, RetNet's concentrates on primacy and recency positions, and HGRN2's focuses on semantically related positions. Cross-architecture cosine similarity is moderate (mean 0.42), reflecting partial overlap that may be driven by task-level inductive biases from LAMBADA.\n\nThese results provide suggestive mechanistic evidence that attention adapts its behavior to complement the specific recurrence mechanism it is paired with. However, the moderate correlation strength (0.24--0.37) means attention patterns alone do not fully explain the per-example effects; changes in recurrence state likely contribute as a complementary mechanism that we cannot directly observe.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Attention pattern analysis for h3-1 models on LAMBADA (1.3B). Cross-arch cosine similarities are between architectures (GDN/RetNet/HGRN2).}\n\\label{tab:attention}\n\\begin{tabular}{@{}lcll@{}}\n\\toprule\nArchitecture & Attn--Helped/Hurt Corr. & Dominant Pattern & Cross-arch Cosine \\\\\n\\midrule\nGDN & 0.31 & Dispersed mid-context & ---~/~0.38~/~0.44 \\\\\nRetNet & 0.24 & Primacy-recency & 0.38~/~---~/~0.45 \\\\\nHGRN2 & 0.37 & Semantic focus & 0.44~/~0.45~/~--- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Scale-Dependent Convergence}\n\\label{sec:scale}\n\nTable~\\ref{tab:rebound} summarizes the 340M rebound analysis. At 1.3B, cross-architecture std decreases monotonically with attention ratio. At 340M, convergence proceeds similarly until attention ratio 6, but at ratio 8 the cross-architecture std increases by 35\\% (from 0.014 at ratio 6 to 0.019 at ratio 8). Per-example analysis reveals that the rebound disproportionately affects long-context examples (mean 94.2 tokens) with rare target tokens (mean frequency rank 8,420), consistent with a \\emph{capacity hypothesis}: at 340M, attention layers and recurrence layers compete for limited model capacity, and high attention ratios compromise recurrence quality for the most demanding examples.\n\nThe rebound samples moderately overlap with those helped by attention at 1.3B (Jaccard $= 0.28$), suggesting these are inherently difficult examples that require both strong recurrence and attention---a combination achievable at 1.3B but not at 340M.\n\nWe note an important confound: 340M models are trained on 20B tokens while 1.3B models are trained on 100B tokens. We cannot fully disentangle whether the scale-dependent convergence reflects model capacity, training duration, or their interaction.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{340M rebound analysis: per-example comparison at attention ratio 8.}\n\\label{tab:rebound}\n\\begin{tabular}{@{}llll@{}}\n\\toprule\nMetric & 340M & 1.3B & Interpretation \\\\\n\\midrule\nCross-arch std (attn=8) & 0.019 ($\\uparrow$35\\%) & 0.008 ($\\downarrow$ mono.) & Rebound at 340M only \\\\\nRebound: mean ctx length & 94.2 tokens & N/A & Long-context affected \\\\\nRebound: mean tgt freq rank & 8,420 & N/A & Rare tokens affected \\\\\nOverlap w/ 1.3B helped & \\multicolumn{2}{c}{Jaccard = 0.28} & Moderate overlap \\\\\nTraining tokens & 20B & 100B & Confounded with scale \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{The Equalizer Paradox: Convergence--Divergence Co-evolution}\n\\label{sec:paradox}\n\nTable~\\ref{tab:coevolution} and the convergence--divergence co-evolution analysis reveal the central paradox of this paper. As attention ratio increases, aggregate cross-architecture std monotonically decreases (0.024 $\\to$ 0.005) while per-example net effect asymmetry monotonically increases (0.12 $\\to$ 0.31). These two trends are significantly anti-correlated ($\\rho{=}{-}0.83$, $p{=}0.042$).\n\nThis means that the more attention homogenizes aggregate performance, the more divergent the per-example mechanisms become. At the highest attention ratio (h24-1), architectures achieve nearly identical aggregate scores on LAMBADA, but each architecture arrives at this score by helping and hurting almost entirely different subsets of examples. The pairwise Jaccard similarity of helped sets decreases from 0.14 (one attention layer) to 0.07 (24 attention layers), reflecting increasing architecture-specificity of the attention-mediated effects.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Co-evolution of aggregate convergence and per-example divergence (LAMBADA, 1.3B). Net effect asymmetry measures the divergence in per-architecture improvement directions.}\n\\label{tab:coevolution}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nAttention Ratio & Cross-arch Std & Jaccard (mean) & Net Effect Asymmetry \\\\\n\\midrule\n0 (pure) & 0.024 & --- & --- \\\\\n1 (h1-1) & 0.019 & 0.14 & 0.12 \\\\\n3 (h3-1) & 0.014 & 0.11 & 0.18 \\\\\n6 (h6-1) & 0.009 & 0.09 & 0.24 \\\\\n8 (h8-1) & 0.007 & 0.08 & 0.27 \\\\\n24 (h24-1) & 0.005 & 0.07 & 0.31 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Statistical Robustness}\n\\label{sec:robustness}\n\nTable~\\ref{tab:robustness} presents bootstrap confidence intervals and leave-one-architecture-out sensitivity analysis. Key results survive robustness checks but with reduced effect sizes:\n\n\\begin{itemize}\n    \\item LAMBADA std reduction: 79\\% point estimate, bootstrap 95\\% CI [58\\%, 72\\%]. Excluding GDN: 52\\%, CI [38\\%, 61\\%].\n    \\item LAMBADA Spearman $\\rho$: $-$1.00, CI [$-$1.0, $-$0.80]. Excluding GDN: $-$0.90, CI [$-$1.0, $-$0.60].\n    \\item Cohen's $d$ for convergence effect: 1.12, CI [0.74, 1.48]. Excluding GDN: 0.73, CI [0.41, 1.05].\n\\end{itemize}\n\nBootstrap CIs do not cross zero for any core metric, establishing that the convergence effect is not a statistical artifact. However, GDN contributes disproportionately to the effect---excluding it reduces effect sizes by 25--35\\%. This is interpretable: GDN's gated delta rule mechanism may be most responsive to attention injection, making it the strongest ``equalizer'' responder. Nevertheless, convergence remains substantial with only RetNet and HGRN2 (52\\% std reduction, Cohen's $d = 0.73$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Bootstrap confidence intervals and sensitivity analysis. ``Full'' uses all three architectures; ``Excl.\\ GDN'' removes GatedDeltaNet.}\n\\label{tab:robustness}\n\\begin{tabular}{@{}lccccr@{}}\n\\toprule\nMetric & Full & 95\\% CI & Excl.\\ GDN & 95\\% CI & $\\Delta$\\% \\\\\n\\midrule\nLAMBADA std red.\\ (\\%) & 79 & [58, 72] & 52 & [38, 61] & $-$34 \\\\\nLAMBADA $\\rho$ & $-$1.00 & [$-$1.0, $-$0.80] & $-$0.90 & [$-$1.0, $-$0.60] & --- \\\\\nCohen's $d$ & 1.12 & [0.74, 1.48] & 0.73 & [0.41, 1.05] & $-$35 \\\\\nJaccard (mean) & 0.08 & [0.05, 0.12] & 0.06 & [0.03, 0.10] & $-$25 \\\\\nClaims surviving & 3/3 & --- & 2/3 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ============================================================\n%% 5. COMPARISON WITH WANG ET AL.\n%% ============================================================\n\\section{Relationship to Wang et al.\\ (2025)}\n\nOur work builds directly on the model zoo of Wang et al.\\ and is complementary to their benchmarking study. Table~\\ref{tab:differentiation} summarizes the analytical dimensions we add. Wang et al.\\ qualitatively observe that ``models with higher attention ratios tend to perform more similarly'' and ``the choice of recurrence mechanism becomes less important at higher attention ratios.'' We formalize this observation through a quantitative convergence framework with statistical testing, extend it to per-example granularity, and uncover the convergence--divergence paradox that is invisible in aggregate metrics.\n\nWe emphasize that this is not a critique of Wang et al.---their contribution is the model zoo itself, and convergence analysis was not their research question. Our work demonstrates the analytical value that systematic per-example investigation can extract from shared experimental infrastructure.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Analytical contributions beyond Wang et al.\\ (2025).}\n\\label{tab:differentiation}\n\\begin{tabular}{@{}p{3cm}p{4.2cm}p{4.8cm}@{}}\n\\toprule\nDimension & Wang et al. & This Work \\\\\n\\midrule\nConvergence & Qualitative (``tend to perform similarly'') & Quantitative ($\\rho$, std trajectory, bootstrap CI) \\\\\nPer-example & Not performed & Full logprob analysis, Jaccard, helped/hurt \\\\\nScale dependency & Not characterized & Binary contrast: 340M partial vs.\\ 1.3B complete \\\\\nMechanistic & Not performed & Sample feature characterization, attention patterns \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ============================================================\n%% 6. DISCUSSION\n%% ============================================================\n\\section{Discussion}\n\n\\paragraph{Practical implications.}\nThe equalizer paradox has direct consequences for architecture selection. When aggregate benchmarks show convergence across hybrid architectures, practitioners might conclude that the choice of recurrence mechanism is unimportant. Our per-example analysis shows this conclusion is misleading: architectures that appear equivalent in aggregate may fail on different subsets of inputs. For applications where per-example reliability matters---machine translation, question answering, retrieval-augmented generation---the specific recurrence mechanism remains consequential even at high attention ratios.\n\n\\paragraph{Mechanistic interpretation.}\nTarget token frequency emerges as a shared mechanistic driver: attention universally aids rare-token retrieval across architectures. However, the varying effect sizes (Cohen's $d$ from 0.24 to 0.41) and low cross-architecture Jaccard suggest that each recurrence mechanism has different ``blind spots'' that attention compensates for. The qualitative differences in attention patterns (dispersed vs.\\ primacy-recency vs.\\ semantic focus) are consistent with attention adapting to complement the specific information bottleneck of each recurrence mechanism. We emphasize that this is suggestive mechanistic evidence, not a causal demonstration---the recurrence state changes induced by attention layer presence likely contribute as an unobservable complementary mechanism.\n\n\\paragraph{Why retrieval tasks?}\nLAMBADA requires predicting a final word based on distant context---a retrieval operation that exercises exactly the capacity that attention provides (global context access) and that recurrence compresses away. Reasoning-heavy tasks like HellaSwag require integrating local coherence cues where recurrence may already be sufficient, explaining the absence of convergence. ARC-Easy's intermediate position ($\\rho{=}{-}0.6$) is consistent with its partial reliance on knowledge retrieval, but we acknowledge this explanation is post-hoc and the statistical evidence is insufficient.\n\n%% ============================================================\n%% 7. LIMITATIONS\n%% ============================================================\n\\section{Limitations}\n\n\\paragraph{Architecture coverage (n=3).}\nOur analysis covers three architectures: GatedDeltaNet, RetNet, and HGRN2. These represent three distinct recurrence mechanisms (gated delta rule, linear attention with exponential decay, hierarchical gated recurrence) and are all publicly available hybrid architectures from Wang et al.'s zoo. However, important architectures such as Mamba/Mamba-2 hybrids, RWKV hybrids, and Griffin lack public checkpoints with controlled attention ratios. Generalization of the equalizer effect to other recurrence families is an open question.\n\n\\paragraph{Task coverage.}\nOnly LAMBADA shows statistically significant convergence after multiple comparison correction. While we provide a retrieval-demand interpretation, this relies on a single significant benchmark, making the task-specificity claim inherently underpowered. Future work with additional retrieval-intensive benchmarks (e.g., natural questions, passage retrieval) is needed.\n\n\\paragraph{Scale confound.}\nThe 340M and 1.3B models differ in both parameter count and training data volume (20B vs.\\ 100B tokens). We cannot determine whether scale-dependent convergence reflects model capacity, training duration, or their interaction. No 7B-scale models are available in the model zoo.\n\n\\paragraph{Statistical power.}\nWith only 5 attention ratios per architecture, Spearman correlation has limited statistical power ($n{=}5$). ARC-Easy's $\\rho{=}{-}0.6$ ($p{=}0.142$) might reach significance with more attention ratio data points. Bootstrap CIs are correspondingly wide (e.g., LAMBADA $\\rho$ CI width $= 0.2$). The convergence--divergence co-evolution correlation ($\\rho{=}{-}0.83$, $p{=}0.042$) is borderline significant and sensitive to individual data points.\n\n\\paragraph{GDN dependency.}\nGatedDeltaNet contributes disproportionately to the convergence signal; excluding it reduces effect sizes by 30--40\\%. While claims survive this sensitivity analysis, the reduced effect sizes mean our strongest results are partially GDN-dependent.\n\n%% ============================================================\n%% 8. CONCLUSION\n%% ============================================================\n\\section{Conclusion}\n\nWe have provided the first quantitative characterization of the equalizer effect in hybrid linear recurrent architectures. On retrieval-intensive tasks, adding attention layers monotonically reduces cross-architecture performance variance at sufficient scale, yet per-example analysis reveals this convergence is achieved through architecture-specific, largely non-overlapping mechanisms. This equalizer paradox---aggregate convergence masking per-example divergence---challenges the assumption that converging benchmark scores imply converging model behavior. Whether this phenomenon extends beyond retrieval-intensive tasks and beyond the three architectures studied here remains an important direction for future work.\n\n%% ============================================================\n%% REFERENCES\n%% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{10}\n\n\\bibitem[Clark et al.(2018)]{clark2018arc}\nClark, P., Cowhey, I., Etzioni, O., Khot, T., Sabharwal, A., Schoenick, C., and Tafjord, O. (2018).\n\\newblock Think you have solved question answering? {T}ry {ARC}, the {AI2} reasoning challenge.\n\\newblock \\emph{arXiv preprint arXiv:1803.05457}.\n\n\\bibitem[De~Mesmay et al.(2024)]{de2024griffin}\nDe~Mesmay, A., Botev, A., Sherburn, D., et al. (2024).\n\\newblock Griffin: Mixing gated linear recurrences with local attention for efficient language models.\n\\newblock \\emph{arXiv preprint arXiv:2402.19427}.\n\n\\bibitem[Ethayarajh et al.(2022)]{ethayarajh2022understanding}\nEthayarajh, K., Choi, Y., and Swayamdipta, S. (2022).\n\\newblock Understanding dataset difficulty with $\\mathcal{V}$-usable information.\n\\newblock In \\emph{Proceedings of ICML}.\n\n\\bibitem[Hendrycks et al.(2021)]{hendrycks2021mmlu}\nHendrycks, D., Burns, C., Basart, S., Zou, A., Mazeika, M., Song, D., and Steinhardt, J. (2021).\n\\newblock Measuring massive multitask language understanding.\n\\newblock In \\emph{Proceedings of ICLR}.\n\n\\bibitem[Koh and Liang(2017)]{koh2017understanding}\nKoh, P.~W. and Liang, P. (2017).\n\\newblock Understanding black-box predictions via influence functions.\n\\newblock In \\emph{Proceedings of ICML}.\n\n\\bibitem[Lieber et al.(2024)]{lieber2024jamba}\nLieber, O., Lenz, B., Bata, H., et al. (2024).\n\\newblock Jamba: A hybrid {T}ransformer-{M}amba language model.\n\\newblock \\emph{arXiv preprint arXiv:2403.19887}.\n\n\\bibitem[Qin et al.(2024)]{qin2024hgrn2}\nQin, Z., Li, D., Sun, W., Sun, W., Shen, X., Han, X., and Wei, Y. (2024).\n\\newblock {HGRN2}: Gated linear {RNN}s with state expansion.\n\\newblock \\emph{arXiv preprint arXiv:2404.07904}.\n\n\\bibitem[Sakaguchi et al.(2021)]{sakaguchi2021winogrande}\nSakaguchi, K., Le~Bras, R., Bhagavatula, C., and Choi, Y. (2021).\n\\newblock {WinoGrande}: An adversarial {W}inograd schema challenge at scale.\n\\newblock \\emph{Communications of the ACM}, 64(9):99--106.\n\n\\bibitem[Sun et al.(2023)]{sun2023retentive}\nSun, Y., Dong, L., Huang, S., Ma, S., Xia, Y., Xue, J., Wang, J., and Wei, F. (2023).\n\\newblock Retentive network: A successor to {T}ransformer for large language models.\n\\newblock \\emph{arXiv preprint arXiv:2307.08621}.\n\n\\bibitem[Swayamdipta et al.(2020)]{swayamdipta2020dataset}\nSwayamdipta, S., Schwartz, R., Lourie, N., Wang, Y., Hajishirzi, H., Smith, N.~A., and Choi, Y. (2020).\n\\newblock Dataset cartography: Mapping and diagnosing datasets with training dynamics.\n\\newblock In \\emph{Proceedings of EMNLP}.\n\n\\bibitem[Wang et al.(2025)]{wang2025mzoobenchmarkinghybridllms}\nWang, J., Ren, L., et al. (2025).\n\\newblock MZoo: Benchmarking hybrid {LLM}s with a model zoo of linear recurrent architectures.\n\\newblock \\emph{arXiv preprint arXiv:2507.06457}.\n\n\\bibitem[Yang et al.(2024)]{yang2024gateddeltanetworks}\nYang, S., Wang, B., Shen, Y., Panda, R., and Kim, Y. (2024).\n\\newblock Gated delta networks: Improving mamba2 with delta rule.\n\\newblock \\emph{arXiv preprint arXiv:2412.06464}.\n\n\\bibitem[Zellers et al.(2019)]{zellers2019hellaswag}\nZellers, R., Holtzman, A., Bisk, Y., Farhadi, A., and Choi, Y. (2019).\n\\newblock {HellaSwag}: Can a machine really finish your sentence?\n\\newblock In \\emph{Proceedings of ACL}.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "ada232c0-eb29-43e9-a28d-0de61eb16c45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "c013dfff-9ae5-416a-b5ae-03fba6a5fd1c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260519T131014 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gate…",
  "leafUuid": "747f2534-8424-4b4f-94cd-d1f9e2e8b877",
  "sessionId": "c013dfff-9ae5-416a-b5ae-03fba6a5fd1c"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper with experiment data",
  "sessionId": "c013dfff-9ae5-416a-b5ae-03fba6a5fd1c"
}
```

---

### Tool call

_source line 23 · 2026-05-19T13:36:57.393Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014nF5JjqD37RL68jXtpvv7S`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/dream_reports/dream_20260519T131014/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "747f2534-8424-4b4f-94cd-d1f9e2e8b877",
  "isSidechain": false,
  "requestId": "req_011CbC1yVT7mpQAsSjoVwppo",
  "type": "assistant",
  "uuid": "8575df89-0a6f-4bda-9b83-c8ab5f93deb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "c013dfff-9ae5-416a-b5ae-03fba6a5fd1c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X1sN9j3Sx7D7qG4g3amVfH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10132,
      "cache_read_input_tokens": 38246,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10132,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 38246,
          "cache_creation_input_tokens": 10132,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10132
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

_source line 24 · 2026-05-19T13:36:58.300Z_

<details><summary>↩ Tool result · `toolu_014nF5JjqD37RL68jXtpvv7S`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
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
Overfull \hbox (8.76143pt too wide) in paragraph at lines 36--37
\T1/ptm/m/n/10 overlapping across ar-chi-tec-tures (pair-wise Jac-card $\OML/cm
m/m/it/10 < \OT1/cmr/m/n/10 0\OML/cmm/m/it/10 :\OT1/cmr/m/n/10 10$\T1/ptm/m/n/1
0 ). This \T1/ptm/m/it/10 equal-izer para-dox \T1/ptm/m/n/10 is scale-dependent
:

Package natbib Warning: Citation `wang2025mzoobenchmarkinghybridllms' on page 1
 undefined on input line 44.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]

Package natbib Warning: Citation `yang2024gateddeltanetworks' on page 2 undefin
ed on input line 64.


Package natbib Warning: Citation `sun2023retentive' on page 2 undefined on inpu
t line 64.


Package natbib Warning: Citation `qin2024hgrn2' on page 2 undefined on input li
ne 64.


Package natbib Warning: Citation `lieber2024jamba' on page 2 undefined on input
 line 67.


Package natbib Warning: Citation `de2024griffin' on page 2 undefined on input l
ine 67.


Package natbib Warning: Citation `swayamdipta2020dataset' on page 2 undefined o
n input line 70.


Package natbib Warning: Citation `koh2017understanding' on page 2 undefined on 
input line 70.


Package natbib Warning: Citation `ethayarajh2022understanding' on page 2 undefi
ned on input line 70.


Overfull \hbox (3.85017pt too wide) in paragraph at lines 70--71
\T1/ptm/m/n/10.95 am-ple level. We adopt a sim-pler approach---comparing per-ex
ample log-prob deltas across architectures---
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1pcr.fd)

Package natbib Warning: Citation `clark2018arc' on page 2 undefined on input li
ne 83.


Package natbib Warning: Citation `zellers2019hellaswag' on page 2 undefined on 
input line 83.


Package natbib Warning: Citation `sakaguchi2021winogrande' on page 2 undefined 
on input line 83.


Package natbib Warning: Citation `hendrycks2021mmlu' on page 2 undefined on inp
ut line 83.

[2]

LaTeX Warning: Reference `tab:convergence' on page 3 undefined on input line 10
5.


LaTeX Warning: Reference `tab:perexample' on page 3 undefined on input line 131
.

[3]

LaTeX Warning: Reference `tab:features' on page 4 undefined on input line 153.


Overfull \hbox (20.5918pt too wide) in paragraph at lines 153--154
\T1/ptm/m/n/10.95 text win-dow en-ables re-trieval of rare to-kens that re-cur-
rence alone---with its com-pressed state representation---

LaTeX Warning: Reference `tab:attention' on page 4 undefined on input line 181.


[4]

LaTeX Warning: Reference `tab:rebound' on page 5 undefined on input line 206.


LaTeX Warning: Reference `tab:coevolution' on page 5 undefined on input line 23
3.

[5]

LaTeX Warning: Reference `tab:robustness' on page 6 undefined on input line 259
.

(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)

LaTeX Warning: Reference `tab:differentiation' on page 6 undefined on input lin
e 292.

[6]
Underfull \hbox (badness 4378) in paragraph at lines 305--306
[]|\T1/ptm/m/n/10 Quantitative ($\OML/cmm/m/it/10 ^^Z$\T1/ptm/m/n/10 , std tra-
jec-tory,

Underfull \hbox (badness 2707) in paragraph at lines 306--307
[]|\T1/ptm/m/n/10 Full log-prob anal-y-sis, Jac-card,

Underfull \hbox (badness 1533) in paragraph at lines 308--309
[]|\T1/ptm/m/n/10 Sample fea-ture char-ac-ter-i-za-tion,
[7]
Overfull \hbox (3.30283pt too wide) in paragraph at lines 352--353
\T1/ptm/m/n/10.95 is achieved through architecture-specific, largely non-overla
pping mech-a-nisms. This equal-izer paradox---

Overfull \hbox (3.68692pt too wide) in paragraph at lines 352--353
\T1/ptm/m/n/10.95 bench-mark scores im-ply con-verg-ing model be-hav-ior. Wheth
er this phe-nomenon ex-tends be-yond retrieval-
[8]

Package natbib Warning: There were undefined citations.

[9] (./paper.aux

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
ic/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
msy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/urw/times/utmri8a.pfb>
Output written on paper.pdf (9 pages, 157765 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
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
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)
Overfull \hbox (8.76143pt too wide) in paragraph at lines 36--37
\T1/ptm/m/n/10 overlapping across ar-chi-tec-tures (pair-wise Jac-card $\OML/cm
m/m/it/10 < \OT1/cmr/m/n/10 0\OML/cmm/m/it/10 :\OT1/cmr/m/n/10 10$\T1/ptm/m/n/1
0 ). This \T1/ptm/m/it/10 equal-izer para-dox \T1/ptm/m/n/10 is scale-dependent
:
[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]
Overfull \hbox (21.90599pt too wide) in paragraph at lines 70--71
 []\T1/ptm/b/n/10.95 Per-example anal-y-sis in NLP.[] \T1/ptm/m/n/10.95 Instanc
e-level anal-y-sis has a rich his-tory: dataset car-tog-ra-phy [[][]Swayamdipta

(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1pcr.fd) [2] [3]
Overfull \hbox (20.5918pt too wide) in paragraph at lines 153--154
\T1/ptm/m/n/10.95 text win-dow en-ables re-trieval of rare to-kens that re-cur-
rence alone---with its com-pressed state representation---
[4] [5] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [6]
Underfull \hbox (badness 4378) in paragraph at lines 305--306
[]|\T1/ptm/m/n/10 Quantitative ($\OML/cmm/m/it/10 ^^Z$\T1/ptm/m/n/10 , std tra-
jec-tory,

Underfull \hbox (badness 2707) in paragraph at lines 306--307
[]|\T1/ptm/m/n/10 Full log-prob anal-y-sis, Jac-card,

Underfull \hbox (badness 1533) in paragraph at lines 308--309
[]|\T1/ptm/m/n/10 Sample fea-ture char-ac-ter-i-za-tion,
[7]
Overfull \hbox (3.30283pt too wide) in paragraph at lines 352--353
\T1/ptm/m/n/10.95 is achieved through architecture-specific, largely non-overla
pping mech-a-nisms. This equal-izer paradox---

Overfull \hbox (3.68692pt too wide) in paragraph at lines 352--353
\T1/ptm/m/n/10.95 bench-mark scores im-ply con-verg-ing model be-hav-ior. Wheth
er this phe-nomenon ex-tends be-yond retrieval-
[8] [9] (./paper.aux) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ
ic/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
msy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/urw/times/utmri8a.pfb>
Output written on paper.pdf (9 pages, 160779 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8575df89-0a6f-4bda-9b83-c8ab5f93deb9",
  "isSidechain": false,
  "promptId": "1470b571-8e3c-450f-9a8f-7768e6cda7c5",
  "type": "user",
  "uuid": "a798ea7d-01b8-4aac-bc7a-95fb6c3e6c27",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\nOverfull \\hbox (8.76143pt too wide) in paragraph at lines 36--37\n\\T1/ptm/m/n/10 overlapping across ar-chi-tec-tures (pair-wise Jac-card $\\OML/cm\nm/m/it/10 < \\OT1/cmr/m/n/10 0\\OML/cmm/m/it/10 :\\OT1/cmr/m/n/10 10$\\T1/ptm/m/n/1\n0 ). This \\T1/ptm/m/it/10 equal-izer para-dox \\T1/ptm/m/n/10 is scale-dependent\n:\n\nPackage natbib Warning: Citation `wang2025mzoobenchmarkinghybridllms' on page 1\n undefined on input line 44.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\n\nPackage natbib Warning: Citation `yang2024gateddeltanetworks' on page 2 undefin\ned on input line 64.\n\n\nPackage natbib Warning: Citation `sun2023retentive' on page 2 undefined on inpu\nt line 64.\n\n\nPackage natbib Warning: Citation `qin2024hgrn2' on page 2 undefined on input li\nne 64.\n\n\nPackage natbib Warning: Citation `lieber2024jamba' on page 2 undefined on input\n line 67.\n\n\nPackage natbib Warning: Citation `de2024griffin' on page 2 undefined on input l\nine 67.\n\n\nPackage natbib Warning: Citation `swayamdipta2020dataset' on page 2 undefined o\nn input line 70.\n\n\nPackage natbib Warning: Citation `koh2017understanding' on page 2 undefined on \ninput line 70.\n\n\nPackage natbib Warning: Citation `ethayarajh2022understanding' on page 2 undefi\nned on input line 70.\n\n\nOverfull \\hbox (3.85017pt too wide) in paragraph at lines 70--71\n\\T1/ptm/m/n/10.95 am-ple level. We adopt a sim-pler approach---comparing per-ex\nample log-prob deltas across architectures---\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1pcr.fd)\n\nPackage natbib Warning: Citation `clark2018arc' on page 2 undefined on input li\nne 83.\n\n\nPackage natbib Warning: Citation `zellers2019hellaswag' on page 2 undefined on \ninput line 83.\n\n\nPackage natbib Warning: Citation `sakaguchi2021winogrande' on page 2 undefined \non input line 83.\n\n\nPackage natbib Warning: Citation `hendrycks2021mmlu' on page 2 undefined on inp\nut line 83.\n\n[2]\n\nLaTeX Warning: Reference `tab:convergence' on page 3 undefined on input line 10\n5.\n\n\nLaTeX Warning: Reference `tab:perexample' on page 3 undefined on input line 131\n.\n\n[3]\n\nLaTeX Warning: Reference `tab:features' on page 4 undefined on input line 153.\n\n\nOverfull \\hbox (20.5918pt too wide) in paragraph at lines 153--154\n\\T1/ptm/m/n/10.95 text win-dow en-ables re-trieval of rare to-kens that re-cur-\nrence alone---with its com-pressed state representation---\n\nLaTeX Warning: Reference `tab:attention' on page 4 undefined on input line 181.\n\n\n[4]\n\nLaTeX Warning: Reference `tab:rebound' on page 5 undefined on input line 206.\n\n\nLaTeX Warning: Reference `tab:coevolution' on page 5 undefined on input line 23\n3.\n\n[5]\n\nLaTeX Warning: Reference `tab:robustness' on page 6 undefined on input line 259\n.\n\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)\n\nLaTeX Warning: Reference `tab:differentiation' on page 6 undefined on input lin\ne 292.\n\n[6]\nUnderfull \\hbox (badness 4378) in paragraph at lines 305--306\n[]|\\T1/ptm/m/n/10 Quantitative ($\\OML/cmm/m/it/10 ^^Z$\\T1/ptm/m/n/10 , std tra-\njec-tory,\n\nUnderfull \\hbox (badness 2707) in paragraph at lines 306--307\n[]|\\T1/ptm/m/n/10 Full log-prob anal-y-sis, Jac-card,\n\nUnderfull \\hbox (badness 1533) in paragraph at lines 308--309\n[]|\\T1/ptm/m/n/10 Sample fea-ture char-ac-ter-i-za-tion,\n[7]\nOverfull \\hbox (3.30283pt too wide) in paragraph at lines 352--353\n\\T1/ptm/m/n/10.95 is achieved through architecture-specific, largely non-overla\npping mech-a-nisms. This equal-izer paradox---\n\nOverfull \\hbox (3.68692pt too wide) in paragraph at lines 352--353\n\\T1/ptm/m/n/10.95 bench-mark scores im-ply con-verg-ing model be-hav-ior. Wheth\ner this phe-nomenon ex-tends be-yond retrieval-\n[8]\n\nPackage natbib Warning: There were undefined citations.\n\n[9] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\nic/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (9 pages, 157765 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\nOverfull \\hbox (8.76143pt too wide) in paragraph at lines 36--37\n\\T1/ptm/m/n/10 overlapping across ar-chi-tec-tures (pair-wise Jac-card $\\OML/cm\nm/m/it/10 < \\OT1/cmr/m/n/10 0\\OML/cmm/m/it/10 :\\OT1/cmr/m/n/10 10$\\T1/ptm/m/n/1\n0 ). This \\T1/ptm/m/it/10 equal-izer para-dox \\T1/ptm/m/n/10 is scale-dependent\n:\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\nOverfull \\hbox (21.90599pt too wide) in paragraph at lines 70--71\n []\\T1/ptm/b/n/10.95 Per-example anal-y-sis in NLP.[] \\T1/ptm/m/n/10.95 Instanc\ne-level anal-y-sis has a rich his-tory: dataset car-tog-ra-phy [[][]Swayamdipta\n\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1pcr.fd) [2] [3]\nOverfull \\hbox (20.5918pt too wide) in paragraph at lines 153--154\n\\T1/ptm/m/n/10.95 text win-dow en-ables re-trieval of rare to-kens that re-cur-\nrence alone---with its com-pressed state representation---\n[4] [5] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [6]\nUnderfull \\hbox (badness 4378) in paragraph at lines 305--306\n[]|\\T1/ptm/m/n/10 Quantitative ($\\OML/cmm/m/it/10 ^^Z$\\T1/ptm/m/n/10 , std tra-\njec-tory,\n\nUnderfull \\hbox (badness 2707) in paragraph at lines 306--307\n[]|\\T1/ptm/m/n/10 Full log-prob anal-y-sis, Jac-card,\n\nUnderfull \\hbox (badness 1533) in paragraph at lines 308--309\n[]|\\T1/ptm/m/n/10 Sample fea-ture char-ac-ter-i-za-tion,\n[7]\nOverfull \\hbox (3.30283pt too wide) in paragraph at lines 352--353\n\\T1/ptm/m/n/10.95 is achieved through architecture-specific, largely non-overla\npping mech-a-nisms. This equal-izer paradox---\n\nOverfull \\hbox (3.68692pt too wide) in paragraph at lines 352--353\n\\T1/ptm/m/n/10.95 bench-mark scores im-ply con-verg-ing model be-hav-ior. Wheth\ner this phe-nomenon ex-tends be-yond retrieval-\n[8] [9] (./paper.aux) )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\nic/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (9 pages, 160779 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "8575df89-0a6f-4bda-9b83-c8ab5f93deb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/dream_reports/dream_20260519T131014/median",
  "sessionId": "c013dfff-9ae5-416a-b5ae-03fba6a5fd1c",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260519T131014 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gate…",
  "leafUuid": "a798ea7d-01b8-4aac-bc7a-95fb6c3e6c27",
  "sessionId": "c013dfff-9ae5-416a-b5ae-03fba6a5fd1c"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper with experiment data",
  "sessionId": "c013dfff-9ae5-416a-b5ae-03fba6a5fd1c"
}
```

---

### Assistant

_source line 27 · 2026-05-19T13:37:06.043Z_

编译成功，生成 9 页 PDF。

产出：
- `paper.tex` — 完整 LaTeX 源码
- `paper.pdf` — 9 页，包含 Abstract、Introduction、Related Work、Experimental Setup、Results（8 张表覆盖全部 7 个实验 + Wang et al. 对比）、Discussion、Limitations、Conclusion、References
- 所有定量数据直接取自 `experiment_data.json`，三条 claim 按 narrative guidance 降级处理（Claim 1 限缩为 retrieval-specific、Claim 2 标注 scale-vs-tokens confound、Claim 3 降为 suggestive mechanistic evidence），Limitations 段落诚实讨论 n=3 和单任务问题

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a798ea7d-01b8-4aac-bc7a-95fb6c3e6c27",
  "isSidechain": false,
  "requestId": "req_011CbC1ysHms9fKa4BBSbinx",
  "type": "assistant",
  "uuid": "b38fd9ec-2089-47a8-ac2d-1a54a9a89436",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/dream_reports/dream_20260519T131014/median",
  "sessionId": "c013dfff-9ae5-416a-b5ae-03fba6a5fd1c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DHQD2QmxWNYFXdt8AFyP3E",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7440,
      "cache_read_input_tokens": 48378,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7440,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 208,
          "cache_read_input_tokens": 48378,
          "cache_creation_input_tokens": 7440,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7440
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260519T131014 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gate…",
  "leafUuid": "b38fd9ec-2089-47a8-ac2d-1a54a9a89436",
  "sessionId": "c013dfff-9ae5-416a-b5ae-03fba6a5fd1c"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper with experiment data",
  "sessionId": "c013dfff-9ae5-416a-b5ae-03fba6a5fd1c"
}
```

---
