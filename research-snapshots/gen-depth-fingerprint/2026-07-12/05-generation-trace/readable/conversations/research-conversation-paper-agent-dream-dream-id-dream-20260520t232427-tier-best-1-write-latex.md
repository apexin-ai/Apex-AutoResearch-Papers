# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T232427 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/7a6e7dae-2371-44f2-a86f-776f12713121.jsonl`
- **Structured JSON:** [`6bf79f0563defe2a7929.json`](../../sessions/6b/6bf79f0563defe2a7929.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T23:58:33.571Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T23:58:33.571Z",
  "sessionId": "7a6e7dae-2371-44f2-a86f-776f12713121",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T232427 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T232427/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T232427/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T232427/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T232427/best/experiment_data.json`（先 Read 此文件）\n- Venue：emnlp-2026\n- Narrative guidance：原始 framing 完全成立。DDR 二分法 (drifting: hapax, TTR, entropy_mean |ρ|≥0.55; stationary: tail_decay, entropy_max |ρ|<0.10) 在 8+ generators / 5 families 上鲁棒， entropy_std 归为 weakly drifting (|ρ|≈0.20)，不破坏主叙事。 三条 claim 均有充分实验支撑：(1) LOGO binary F1=0.694 为 headline，LOFO 0.686 和 cross-model 0.830 验证泛化性；(2) DDR 跨 3 个 reference model 和 5 个 generator family 稳健， TOST 确认 shape feature stationarity；(3) negative downstream finding 以 TOST ±2% margin 确认。 Scope limitations (base-only, t≤0.7, ≤14B) 诚实报告但不动摇核心 contribution。 论文按原 framing 直接提交 ARR。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T232427/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T23:58:33.574Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T23:58:33.574Z",
  "sessionId": "7a6e7dae-2371-44f2-a86f-776f12713121"
}
```

---

## Round 1

27 recorded events

### User

_source line 3 · 2026-05-20T23:58:33.591Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T232427 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T232427/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T232427/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T232427/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T232427/best/experiment_data.json`（先 Read 此文件）
- Venue：emnlp-2026
- Narrative guidance：原始 framing 完全成立。DDR 二分法 (drifting: hapax, TTR, entropy_mean |ρ|≥0.55; stationary: tail_decay, entropy_max |ρ|<0.10) 在 8+ generators / 5 families 上鲁棒， entropy_std 归为 weakly drifting (|ρ|≈0.20)，不破坏主叙事。 三条 claim 均有充分实验支撑：(1) LOGO binary F1=0.694 为 headline，LOFO 0.686 和 cross-model 0.830 验证泛化性；(2) DDR 跨 3 个 reference model 和 5 个 generator family 稳健， TOST 确认 shape feature stationarity；(3) negative downstream finding 以 TOST ±2% margin 确认。 Scope limitations (base-only, t≤0.7, ≤14B) 诚实报告但不动摇核心 contribution。 论文按原 framing 直接提交 ARR。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T232427/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "1ca86b45-b190-47c7-9689-3b48717c505c",
  "type": "user",
  "uuid": "e1563521-59ea-4bd7-8603-745075a7cf08",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "7a6e7dae-2371-44f2-a86f-776f12713121",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T23:58:33.590Z_

```json
{
  "parentUuid": "e1563521-59ea-4bd7-8603-745075a7cf08",
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
  "uuid": "5c7d5042-5704-47b6-821f-1bbc14a393e2",
  "timestamp": "2026-05-20T23:58:33.590Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "7a6e7dae-2371-44f2-a86f-776f12713121",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T23:58:33.590Z_

```json
{
  "parentUuid": "5c7d5042-5704-47b6-821f-1bbc14a393e2",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ad93bfa6-5cde-43c4-806e-41261c9d0461",
  "timestamp": "2026-05-20T23:58:33.590Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "7a6e7dae-2371-44f2-a86f-776f12713121",
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
  "aiTitle": "Generate complete research paper from experimental data",
  "sessionId": "7a6e7dae-2371-44f2-a86f-776f12713121"
}
```

---

### Assistant

_source line 7 · 2026-05-20T23:58:36.747Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad93bfa6-5cde-43c4-806e-41261c9d0461",
  "isSidechain": false,
  "requestId": "req_011CbEjByr2vv47iYhe1xwtQ",
  "type": "assistant",
  "uuid": "35395ac7-ae69-4635-a661-e722ac3ced86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "7a6e7dae-2371-44f2-a86f-776f12713121",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016vuYEEJ29u9fPEnY582MGR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13357,
      "cache_read_input_tokens": 11841,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13357,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 206,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13357,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13357
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

_source line 8 · 2026-05-20T23:58:37.268Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Tw9FkW2QGVkD9pCJ8a34tW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T232427/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35395ac7-ae69-4635-a661-e722ac3ced86",
  "isSidechain": false,
  "requestId": "req_011CbEjByr2vv47iYhe1xwtQ",
  "type": "assistant",
  "uuid": "86cf0778-39e4-4efb-9b98-ff18e33fc48e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "7a6e7dae-2371-44f2-a86f-776f12713121",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016vuYEEJ29u9fPEnY582MGR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13357,
      "cache_read_input_tokens": 11841,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13357,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 206,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13357,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13357
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

_source line 9 · 2026-05-20T23:58:37.515Z_

<details><summary>↩ Tool result · `toolu_01Tw9FkW2QGVkD9pCJ8a34tW`</summary>

```text
1	[
2	  {
3	    "name": "feature_ablation_and_trend",
4	    "description": "MVP 数据上的三部分分析：(A) feature ablation (full/surface/reference), (B) H1/H2 trend analysis, (C) perplexity pre-validation",
5	    "results": {
6	      "ablation_full_macro_f1": 0.82,
7	      "ablation_surface_only_f1": 0.763,
8	      "ablation_reference_only_f1": 0.719,
9	      "ref_vs_surf_bootstrap_ci": "[0.706,0.733] vs [0.747,0.774]",
10	      "mcnemar_full_vs_surface_p": 0.0,
11	      "mcnemar_full_vs_ref_p": 0.0,
12	      "h2_drifting_features": [
13	        "entropy_mean",
14	        "ttr",
15	        "hapax_ratio"
16	      ],
17	      "h2_slope_entropy_mean": -0.29,
18	      "h2_slope_ttr": -0.034,
19	      "h2_slope_hapax_ratio": -0.043,
20	      "h2_R2_entropy_mean": 0.93,
21	      "h2_R2_ttr": 0.89,
22	      "h2_R2_hapax_ratio": 0.92,
23	      "h1_stationary_features": [
24	        "tail_decay",
25	        "entropy_std",
26	        "entropy_max",
27	        "entropy_min"
28	      ],
29	      "h1_slope_tail_decay": 0.002,
30	      "h1_R2_tail_decay": 0.03,
31	      "entropy_std_slope": -0.12,
32	      "entropy_std_R2": 0.41,
33	      "median_ppl_by_depth": [
34	        13.5,
35	        4.96,
36	        3.0,
37	        2.07,
38	        1.72
39	      ],
40	      "ppl_depth_trend": "monotonic_decrease"
41	    },
42	    "tables": [
43	      "Table A1: Feature Ablation 5-fold CV — Full 0.820, Surface 0.763, Ref 0.719",
44	      "Table A2: Per-feature linear trend (slope, R², p-value) across depths 0–4"
45	    ],
46	    "figures": [],
47	    "analysis": "Surface 和 reference 信号互补性经 McNemar 确认 (p=0)，是论文 complementarity claim 的基础。 entropy_std 的 intermediate status (|slope|=0.12, R²=0.41) 需在正文中诚实讨论， 但不破坏 3-drifting / 2-stationary 的核心二分法， 因为 entropy_std 的 drift magnitude 仅为 drifting 组的 1/3。 Perplexity pre-validation 确认 NLL 分布中存在 depth-dependent signal，为 Claim 3 建立 baseline。\n\n\nFull set 显著优于任一子集 (5.7-10.1pp)。Surface features 捕捉词汇多样性衰减 (TTR/hapax 随 depth 单调递减)，reference features 捕捉 NLL 分布位移 (entropy_mean drift)，两组信号互补。McNemar p=0 确认非冗余。 H2 drifting features 呈清晰单调趋势 (R²>0.89)：递归生成导致词汇空间收缩 和 NLL 均值下降 (recursive compression)。H1 stationary features 保持平坦 (tail_decay R²=0.03)：NLL 分布的 shape 参数在 location shift 下近似不变。 entropy_std 弱趋势 (R²=0.41) 远低于 drifting 组，归为 intermediate 不影响主叙事。 Perplexity 单调递减：deeper text 对 reference model 更 predictable， 因为 model 自身输出的 recursive compression 使 NLL 分布左移。\n"
48	  },
49	  {
50	    "name": "cross_generator_evaluation",
51	    "description": "5-generator LOGO 跨 generator 泛化评估 (Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B)",
52	    "results": {
53	      "total_records": 23032,
54	      "generators": [
55	        "pythia-2.8b",
56	        "pythia-1b",
57	        "olmo-2-1b",
58	        "qwen3-1.7b",
59	        "qwen3-0.6b"
60	      ],
61	      "families": [
62	        "Pythia",
63	        "OLMo",
64	        "Qwen"
65	      ],
66	      "logo_macro_f1": 0.804,
67	      "logo_binary_f1": 0.72,
68	      "logo_binary_ci": [
69	        0.708,
70	        0.732
71	      ],
72	      "per_gen_macro_f1": {
73	        "pythia-1b": 0.851,
74	        "pythia-2.8b": 0.804,
75	        "qwen3-0.6b": 0.818,
76	        "qwen3-1.7b": 0.805,
77	        "olmo-2-1b": 0.752
78	      },
79	      "per_gen_binary_f1": {
80	        "pythia-1b": 0.724,
81	        "pythia-2.8b": 0.72,
82	        "qwen3-0.6b": 0.715,
83	        "qwen3-1.7b": 0.71,
84	        "olmo-2-1b": 0.67
85	      },
86	      "per_gen_binary_variance_pp": 5.4,
87	      "lofo_binary_f1": 0.705,
88	      "lofo_per_family": {
89	        "pythia_held_out": 0.69,
90	        "olmo_held_out": 0.72,
91	        "qwen_held_out": 0.706
92	      },
93	      "ablation_full_f1": 0.804,
94	      "ablation_reference_only_f1": 0.754,
95	      "ablation_surface_only_f1": 0.747,
96	      "mcnemar_p": 0.0,
97	      "entropy_std_importance_drop": 0.0049,
98	      "entropy_std_drift": 0.12,
99	      "top_features": [
100	        "hapax_ratio_0.289",
101	        "ttr_0.168",
102	        "entropy_mean_0.160"
103	      ]
104	    },
105	    "tables": [
106	      "Table 2: Per-generator LOGO macro/binary F1 with 95% CI",
107	      "Table 3: LOFO per-family binary F1",
108	      "Table S1: Feature importance rankings (5-gen aggregate)"
109	    ],
110	    "figures": [],
111	    "analysis": "跨 generator 泛化成功。Per-gen 方差 <10pp 满足 best 档阈值。 LOFO binary F1=0.705 确认跨 family 泛化：仅比 LOGO 低 1.5pp， 证明 Pythia family overlap 未显著 inflate 结果。 Feature ablation 确认 complementarity (McNemar p=0)， 且 pattern 与 plan_001 一致 (full > surface ≈ reference)。\n\n\n5-gen LOGO binary F1=0.720 高于后续 8-gen headline (0.694)， 因为 5-gen set 不包含较难的 Mistral-7B (per-gen F1=0.633) 和 Gemma-2-2B (anomaly)。 Per-gen binary 方差 5.4pp (<10pp 阈值) 证明跨 generator 泛化稳健。 OLMo-2-1B 最低 (0.670) 因为 OLMo 架构 (非 GPT-NeoX/Llama 系) 产生的 distributional pattern 与 Pythia family 差异最大。 Pythia-1B 最高 (0.724) 部分受益于 Pythia-2.8B 在 training fold 中的 family overlap， 但 LOFO 分析控制了此效应 (Pythia held-out 0.690 仅降 3pp)。 Hapax_ratio 仍是最重要特征 (0.289 importance)， 因为词汇多样性衰减是跨 generator 最一致的 depth signal。\n"
112	  },
113	  {
114	    "name": "cross_family_reference_model",
115	    "description": "Non-Pythia reference models (OLMo-2-1B, Qwen3-0.6B) feature extraction，DDR 跨 reference model falsification test",
116	    "results": {
117	      "logo_f1_pythia_ref": 0.803,
118	      "logo_f1_olmo_ref": 0.807,
119	      "logo_f1_qwen_ref": 0.816,
120	      "cross_ref_f1_spread_pp": 1.3,
121	      "entropy_drift_all_refs_negative": true,
122	      "pythia_ref_drift_range": [
123	        -1.19,
124	        -1.4
125	      ],
126	      "olmo_ref_drift_range": [
127	        -0.61,
128	        -0.91
129	      ],
130	      "qwen_ref_drift_range": [
131	        -0.96,
132	        -1.35
133	      ],
134	      "spearman_by_ref": {
135	        "pythia_ref": {
136	          "hapax_ratio": -0.647,
137	          "ttr": -0.63,
138	          "entropy_mean": -0.61,
139	          "tail_decay": -0.04,
140	          "entropy_max": 0.05
141	        },
142	        "olmo_ref": {
143	          "hapax_ratio": -0.647,
144	          "ttr": -0.63,
145	          "entropy_mean": -0.585,
146	          "tail_decay": -0.038,
147	          "entropy_max": 0.055
148	        },
149	        "qwen_ref": {
150	          "hapax_ratio": -0.647,
151	          "ttr": -0.63,
152	          "entropy_mean": -0.62,
153	          "tail_decay": -0.042,
154	          "entropy_max": 0.048
155	        }
156	      },
157	      "stationary_rho_max_across_refs": 0.055,
158	      "ddr_is_pythia_artifact": false
159	    },
160	    "tables": [
161	      "Table 4: LOGO macro F1 by reference model (3 refs × 5 generators)",
162	      "Table S2: Per-feature Spearman ρ by reference model (7×3 matrix)"
163	    ],
164	    "figures": [],
165	    "analysis": "DDR 非 Pythia artifact。这是 Claim 2 最重要的 robustness result。 Entropy_mean drift 方向跨 3 个不同架构 family 的 ref model 一致为负， 证明 drift 来自 generation 过程本身 (recursive compression) 而非特定 ref model 的 bias。 Shape feature stationarity 同样跨 ref 稳健。论文可自信表述 DDR 为 generation-intrinsic property。\n\n\nDDR 模式跨 3 个 reference model (Pythia-410M, OLMo-2-1B, Qwen3-0.6B) 完全稳健。 Surface features (hapax, TTR) 完全不依赖 reference model，rho 跨 ref 完全一致。 Reference features (entropy_mean) 方向一致 (均为负)，magnitude 因 ref model 自身 perplexity calibration 不同而略有差异 (OLMo 偏低)，但不影响 drifting/stationary 分组。 Shape features (tail_decay, entropy_max) 跨 ref 均 |ρ|<0.06。 Qwen ref 分类 F1 略优 (0.816 vs 0.803) 因为 Qwen family 在 generator set 中有 2 个 model，ref-generator family match 提升了 entropy feature 的 discriminability， 但差异仅 1.3pp 证明 reference model 选择不是 critical design decision。 这是 Claim 2 的关键 falsification test：如果 DDR 仅在 Pythia ref 下出现， 叙事崩溃。Best 档下三个 ref 均重现相同分组。\n"
166	  },
167	  {
168	    "name": "downstream_utility",
169	    "description": "OLMo-1B fine-tuning on depth-stratified data, negative downstream finding (Claim 3)",
170	    "results": {
171	      "model": "OLMo-2-0425-1B (1485M)",
172	      "total_runs": 15,
173	      "seeds": [
174	        42,
175	        123,
176	        456
177	      ],
178	      "variants": {
179	        "all": {
180	          "ppl_mean": 2.335,
181	          "ppl_std": 0.0003,
182	          "n_train": 12299
183	        },
184	        "size_matched": {
185	          "ppl_mean": 2.367,
186	          "ppl_std": 0.0002,
187	          "n_train": 3951
188	        },
189	        "depth01": {
190	          "ppl_mean": 2.387,
191	          "ppl_std": 0.001,
192	          "n_train": 3951
193	        },
194	        "binary_filtered": {
195	          "ppl_mean": 2.389,
196	          "ppl_std": 0.001,
197	          "n_train": 3951
198	        },
199	        "depth0_only": {
200	          "ppl_mean": 2.681,
201	          "ppl_std": 0.001,
202	          "n_train": 797
203	        }
204	      },
205	      "ranking": "all(2.335) < size_matched(2.367) < depth01(2.387) ≈ binary_filtered(2.389) << depth0_only(2.681)",
206	      "tost_size_matched_vs_depth01": {
207	        "margin_pct": 2,
208	        "p_value": 0.00011,
209	        "equivalence_confirmed": true
210	      },
211	      "tost_size_matched_vs_binary": {
212	        "margin_pct": 2,
213	        "p_value": 9e-05,
214	        "equivalence_confirmed": true
215	      },
216	      "tost_margin_sensitivity": {
217	        "margin_1pct_p": 0.08,
218	        "margin_2pct_p": 0.00011,
219	        "margin_3pct_p": 2e-06,
220	        "margin_5pct_p": 0.0
221	      },
222	      "cohens_d_matched_vs_depth01": 0.85,
223	      "seed_variance_max_ppl": 0.002
224	    },
225	    "tables": [
226	      "Table 5: Perplexity by training variant (5 variants × 3 seeds, mean ± std)",
227	      "Table S3: TOST margin sensitivity (±1%, ±2%, ±3%, ±5%)"
228	    ],
229	    "figures": [],
230	    "analysis": "Negative finding 是 Claim 3 的核心。Best 档下 TOST 明确确认等价， 且 ranking (random > depth-aware) 是 informative negative： 即使 depth signal 存在，filtering 不改善 downstream quality。 诚实报告 limitation：仅测试了单一 downstream task (CLM) 和单一 metric (perplexity)。 但 TOST + 3 seeds + 5 variants 的设计远超 typical negative finding 的 evidence bar。\n\n\nNegative finding 清晰且符合预期。Depth-aware curation 不优于 random subsampling： size_matched (random) ppl=2.367 优于 depth01 ppl=2.387 和 binary_filtered ppl=2.389。 原因：depth filtering 在移除 deeper text 的同时也移除了 diverse training signal， random subsampling 保留了更完整的 distributional coverage。 TOST at ±2% margin 确认等价 (p=1.1×10⁻⁴)：depth-aware 和 random 在实际意义上无差异。 ±1% margin 未 reject (p=0.08)，这是 honest boundary — 极小 margin 下无法确认等价， 但 ±2% 足以满足实际应用场景的 equivalence threshold。 depth0_only (ppl=2.681) 明显最差因为仅 797 samples (严重不足 + 缺乏 diversity)。 Seed variance 极小 (<0.002) 因为 OLMo-1B fine-tuning 在此 data scale 下非常稳定， Cohen's d inflated 但 TOST 是 appropriate test。 这确立了 depth fingerprinting 作为 diagnostic tool 的定位。\n"
231	  },
232	  {
233	    "name": "prompt_type_comparison",
234	    "description": "Continuation vs elaboration vs inspired_rewriting chains 比较 (Pythia-2.8B, 1000 seeds)",
235	    "results": {
236	      "cv_f1": {
237	        "continuation": 0.781,
238	        "inspired_rewriting": 0.737,
239	        "elaboration": 0.73
240	      },
241	      "lopto_f1": {
242	        "held_out_continuation": 0.762,
243	        "held_out_elaboration": 0.762,
244	        "held_out_rewriting": 0.733,
245	        "avg": 0.753
246	      },
247	      "depth_retention_d4_d0": {
248	        "continuation": 0.831,
249	        "elaboration": 0.986,
250	        "rewriting": 0.939
251	      },
252	      "spearman_rho": {
253	        "continuation": {
254	          "hapax": -0.651,
255	          "ttr": -0.629,
256	          "entropy_mean": -0.665
257	        },
258	        "elaboration": {
259	          "hapax": -0.674,
260	          "ttr": -0.666,
261	          "entropy_mean": -0.583
262	        },
263	        "rewriting": {
264	          "hapax": -0.67,
265	          "ttr": -0.659,
266	          "entropy_mean": -0.564
267	        }
268	      },
269	      "feature_drift_magnitude": {
270	        "continuation": {
271	          "hapax": -0.74,
272	          "ttr": -0.607,
273	          "entropy_mean": -0.557
274	        },
275	        "elaboration": {
276	          "hapax": -0.828,
277	          "ttr": -0.641,
278	          "entropy_mean": -0.471
279	        },
280	        "rewriting": {
281	          "hapax": -0.8,
282	          "ttr": -0.618,
283	          "entropy_mean": -0.477
284	        }
285	      },
286	      "max_gap_cv_pp": 5.1
287	    },
288	    "tables": [
289	      "Table S4: Per-prompt-type CV F1 (within) and LOPTO F1 (cross)",
290	      "Table S5: Spearman ρ by feature × prompt type"
291	    ],
292	    "figures": [],
293	    "analysis": "Prompt-type dependence (continuation 0.781 vs elaboration 0.730 = 5.1pp gap) 诚实报告但 DDR 模式在所有 type 下定性一致。这支持 ecological validity (RC6)： real-world contamination 涉及多种 generation prompt，depth signal 在所有类型下均可提取。 LOPTO avg 0.753 证明不需要知道 prompt type 即可部署。 Continuation-elaboration gap 归因于 continuation 更自由的 distributional drift space， 不是方法论缺陷。\n\n\n三种 prompt type 均保留 depth signal (所有 drifting |ρ|>0.55)，但 continuation 最强 (CV F1=0.781)。Continuation 纯续写最大化 recursive compression — 每步输出成为下一步 的 full context，无语义约束。Elaboration 最弱 (0.730) 因为保持与 seed 的语义关联， 限制了 distributional drift 幅度。Rewriting 居中 (0.737) 因为 semantic preservation 弱于 elaboration 但强于 continuation。 Depth retention 差异大 (elaboration 98.6% vs continuation 83.1%)：continuation 的 deeper text 更短更容易被 min-length filter 截断。 LOPTO 证明跨 prompt type 泛化可行 (avg 0.753)： 在一种 prompt type 上训练仍能在其他类型上保持合理性能。 Feature drift magnitude: elaboration 的 hapax drift 反而更大 (-0.828 vs -0.740) 因为 elaboration 的 higher retention rate 保留了更多 deep samples，使 regression 更稳定。\n"
294	  },
295	  {
296	    "name": "paraphrastic_comparison",
297	    "description": "Paraphrastic chains vs continuation chains, 测试 attractor convergence theory",
298	    "results": {
299	      "paraphrastic_cv_binary_f1": 0.618,
300	      "paraphrastic_cv_3class_f1": 0.68,
301	      "continuation_cv_binary_f1": 0.781,
302	      "continuation_cv_3class_f1": 0.834,
303	      "delta_binary_pp": -16.3,
304	      "paraphrastic_spearman": {
305	        "hapax_ratio": -0.3,
306	        "ttr": -0.26,
307	        "entropy_mean": -0.33,
308	        "tail_decay": -0.02,
309	        "entropy_max": 0.03
310	      },
311	      "paraphrastic_convergence_depth": 3,
312	      "paraphrastic_depth3_vs_depth2_binary_f1": 0.525,
313	      "continuation_depth3_vs_depth2_binary_f1": 0.64,
314	      "depth_retention_paraphrastic_d4_d0": 0.97,
315	      "semantic_sim_d0_d4_paraphrastic": 0.88,
316	      "semantic_sim_d0_d4_continuation": 0.52
317	    },
318	    "tables": [
319	      "Table S6: Paraphrastic vs continuation — CV F1, Spearman ρ, convergence depth"
320	    ],
321	    "figures": [],
322	    "analysis": "Paraphrastic 对比清晰界定了本文 contribution scope。DDR 是 non-paraphrastic chains 的特有现象，因为只有 unconstrained generation 允许 distributional drift 无约束累积。 这与 LLM as Broken Telephone (ACL 2025) 互补：他们研究 paraphrastic attractor cycles， 我们研究 non-paraphrastic depth drift — 两者共同覆盖了 iterative generation 的全景。 Paper 在 related work 中 explicitly connect 两条线。\n\n\nParaphrastic chains 的 depth signal 显著弱于 non-paraphrastic (binary gap 16.3pp)， 符合 attractor convergence theory (ACL 2025)。Paraphrasing 对 input 施加 semantic preservation constraint，限制 distributional drift：vocabulary diversity 在 paraphrase 中近似保持 (|ρ|<0.33 for all features)，因为 paraphrase 倾向复用相同 content words。 ~3 步后 features plateau (depth3 vs depth2 binary F1≈0.525, near chance)， 因为 paraphrastic chain 收敛到 model-specific attractor cycle。 Continuation 无此 constraint，drift 持续累积 (depth3 vs depth2 F1=0.640 仍有信号)。 Depth retention 极高 (97%)：paraphrasing 保持 text length 稳定。 Semantic similarity d0→d4 高 (0.88)：paraphrase 保留了 meaning， 而 continuation (0.52) 已显著 topic-drift。\n"
323	  },
324	  {
325	    "name": "cross_model_chains",
326	    "description": "Cross-model chains (每步不同 generator) vs single-model chains (RC4, ecological validity)",
327	    "results": {
328	      "cross_model_binary_f1": 0.83,
329	      "cross_model_3class_f1": 0.789,
330	      "cross_model_binary_ci": [
331	        0.812,
332	        0.848
333	      ],
334	      "single_model_logo_binary_f1": 0.694,
335	      "delta_cross_vs_single_pp": 13.6,
336	      "cross_model_logo_per_gen": {
337	        "pythia-2.8b": 0.852,
338	        "pythia-1b": 0.838,
339	        "olmo-2-1b": 0.812,
340	        "qwen3-1.7b": 0.843,
341	        "qwen3-0.6b": 0.828
342	      },
343	      "cross_model_per_gen_variance_pp": 4.0,
344	      "heterogeneity_amplification_factor": 1.2,
345	      "ddr_cross_model": {
346	        "hapax_ratio_rho": -0.72,
347	        "ttr_rho": -0.69,
348	        "entropy_mean_rho": -0.68,
349	        "tail_decay_rho": -0.05
350	      },
351	      "cross_model_binary_f1_full_set": 0.764
352	    },
353	    "tables": [
354	      "Table 6: Cross-model vs single-model — binary/3-class F1 with bootstrap CI",
355	      "Table S7: Per-generator LOGO F1 on cross-model chains"
356	    ],
357	    "figures": [],
358	    "analysis": "Cross-model F1=0.830 是论文最强泛化 result。Heterogeneity amplification 是 key insight： 真实 web contamination 涉及 diverse generators → depth signal 更强而非更弱。 这直接 addresses RC4 且 strengthens narrative： controlled single-model evaluation (F1=0.694) 是 conservative lower bound， realistic multi-model scenario 反而更容易检测。 Per-gen variance 4.0pp (cross-model) < 5.4pp (single-model)， 进一步证明 heterogeneity 产生更稳定的信号。\n\n\nCross-model binary F1=0.830 (5-gen subset, generator-level LOGO)，满足核心假设 (≥0.76)。Heterogeneous generators 在每步引入不同 distributional bias， 产生 heterogeneity amplification (factor=1.20)：每步 generator change 叠加产生的 feature divergence 大于单一 generator 的 recursive drift。 单模型 chain 中 model-specific patterns 在 deeper depths 可能趋于 model-specific attractor state，而 cross-model chain 每步注入 fresh distributional perturbation， 阻止 convergence。这导致 drifting features |ρ| 更高 (hapax -0.72 vs single-model -0.647)。 Cross-model 场景更接近真实 web contamination (多模型参与)， 因此 higher F1 是 positive ecological validity result。 Full 8-gen set 的 cross-model binary F1=0.764 (略低于 5-gen 的 0.830)， 因为 8-gen set 包含了更 diverse 的 generator combinations。\n"
359	  },
360	  {
361	    "name": "multi_domain_seeds",
362	    "description": "4-domain seeds 扩展 (Wikipedia, news, scientific, creative/code)",
363	    "results": {
364	      "per_domain_binary_f1": {
365	        "wikipedia": 0.694,
366	        "news": 0.712,
367	        "academic": 0.628,
368	        "code": 0.687
369	      },
370	      "per_domain_binary_ci": {
371	        "news": [
372	          0.69,
373	          0.733
374	        ],
375	        "academic": [
376	          0.603,
377	          0.652
378	        ],
379	        "code": [
380	          0.664,
381	          0.71
382	        ]
383	      },
384	      "per_domain_3class_f1": {
385	        "wikipedia": 0.77,
386	        "news": 0.715,
387	        "academic": 0.656,
388	        "code": 0.673
389	      },
390	      "overall_cross_domain_binary_f1": 0.676,
391	      "domain_gap_max_pp": 8.4,
392	      "worst_domain": "academic",
393	      "best_new_domain": "news",
394	      "ddr_by_domain": {
395	        "wikipedia": {
396	          "hapax_rho": -0.647,
397	          "entropy_mean_rho": -0.61
398	        },
399	        "news": {
400	          "hapax_rho": -0.621,
401	          "entropy_mean_rho": -0.595
402	        },
403	        "academic": {
404	          "hapax_rho": -0.543,
405	          "entropy_mean_rho": -0.52
406	        },
407	        "code": {
408	          "hapax_rho": -0.63,
409	          "entropy_mean_rho": -0.581
410	        }
411	      },
412	      "ddr_pattern_consistent_across_domains": true
413	    },
414	    "tables": [
415	      "Table S8: Per-domain binary F1 with 95% CI (t=0.7 and t=1.0)",
416	      "Table S9: Spearman ρ by feature × domain"
417	    ],
418	    "figures": [],
419	    "analysis": "Multi-domain evaluation supports ecological validity (RC6)。 Domain gap (8.4pp) 诚实报告为 limitation 但不动摇核心 claim： 所有 domain 均显著优于 random baseline (0.50)，且 DDR 模式定性一致。 Academic domain weakness 归因于 genre-specific ceiling effect， 可在 future work 中通过 domain-specific feature engineering 改善。\n\n\nDepth signal 跨 domain 稳健但有 domain-specific variation (max gap 8.4pp)。 Academic 最弱 (0.628) 因为学术写作高度 formulaic — 严格的 genre conventions (句式结构、术语使用) 限制了 generation 的 distributional drift 空间， 且 academic text 的 baseline vocabulary diversity 已较低 (TTR ceiling effect)。 News 最优 (0.712) 因为 news text 词汇丰富度高、topic diversity 大， generation drift 有更大的 feature margin 可供利用。 Code (0.687) 接近 average：代码的 structural patterns (语法约束、缩进) 提供额外区分信号，但 entropy features 被 code syntax 的 deterministic tokens 压缩。 Wikipedia baseline (0.694) 与 8-gen LOGO headline 一致。 DDR 模式跨 domain 定性一致 (所有 domain drifting |ρ|>0.52)， 但 academic domain 的 |ρ| 最低，与 lowest F1 一致。\n"
420	  },
421	  {
422	    "name": "finer_grained_ordinal",
423	    "description": "5-class ordinal classification (gen-0 to gen-4), ordinal methods (CORAL, Frank-Hall) 比较",
424	    "results": {
425	      "xgboost_5class_f1": 0.503,
426	      "coral_5class_f1": 0.497,
427	      "frank_hall_5class_f1": 0.501,
428	      "xgboost_3class_f1": 0.773,
429	      "ordinal_mae": 0.72,
430	      "per_class_5class_f1": {
431	        "gen0": 0.952,
432	        "gen1": 0.518,
433	        "gen2": 0.348,
434	        "gen3": 0.325,
435	        "gen4": 0.372
436	      },
437	      "confusion_matrix_bottleneck": "gen-1/gen-2 boundary concentrates 86% of binary errors as FNs",
438	      "gen2_gen3_mutual_misclass_rate": 0.42
439	    },
440	    "tables": [
441	      "Table S10: 5×5 confusion matrix (XGBoost)",
442	      "Table S11: Ordinal methods comparison (XGBoost, CORAL, Frank-Hall) + 3-class reference"
443	    ],
444	    "figures": [],
445	    "analysis": "3-class (gen-0/gen-1/gen-2+) 是 practical resolution ceiling。 5-class 不可行的根本原因是 distributional drift 的 diminishing marginal return： depth 每增加一步，feature shift magnitude 递减 (concave curve)。 这是 generation process 的 intrinsic property (类似 entropy rate convergence)， 不可通过更好的 classifier 或更多 features 解决。 诚实报告为 scope boundary，不削弱论文核心 contribution (3-class 已是 novel formulation)。\n\n\n5-class F1≈0.50, ordinal methods (CORAL, Frank-Hall) 无改善 (<1pp)。 Gen-0 仍高 F1 (0.952) 因为 seed sharing 提供强信号 (human text vs LLM text 的 distributional gap)。 Gen-1 moderate (0.518)：与 gen-0 的 gap (first generation step) 最大，但与 gen-2 的 margin 已很小。Gen-2/gen-3/gen-4 严重混淆 (mutual misclass 42%)： recursive drift 在前 2 步最陡峭 (feature curve 呈 concave shape, 非线性)， deeper depths 的 marginal drift 已趋近 noise floor。 Ordinal methods 不优于 standard XGBoost 因为 feature space 中的 ordinal structure 在 deeper depths 退化 — 非线性 plateau 而非 monotonic 递增。 CORAL 和 Frank-Hall 假设 ordinal margin 在所有相邻 class pairs 间近似均匀， 但实际 gen-0→gen-1 margin >> gen-2→gen-3 margin，violating this assumption。\n"
446	  },
447	  {
448	    "name": "human_edit_robustness",
449	    "description": "模拟人类编辑的 robustness test — (A) random word replacement (5%/10%/20%) + (B) LLM rephrase",
450	    "results": {
451	      "baseline_binary_f1": 0.695,
452	      "random_replacement": {
453	        "pct5_binary_f1": 0.65,
454	        "pct10_binary_f1": 0.614,
455	        "pct20_binary_f1": 0.591,
456	        "pct5_drop_pp": -4.6,
457	        "pct10_drop_pp": -8.1,
458	        "pct20_drop_pp": -10.4
459	      },
460	      "llm_rephrase": {
461	        "binary_f1": 0.647,
462	        "binary_ci": [
463	          0.631,
464	          0.662
465	        ],
466	        "multiclass_f1": 0.667,
467	        "multiclass_ci": [
468	          0.655,
469	          0.68
470	        ],
471	        "binary_drop_pp": -4.5,
472	        "multiclass_drop_pp": -7.1
473	      },
474	      "edit_distance_ratio": 0.507,
475	      "avg_sentences_replaced": 1.69,
476	      "degradation_profile": "graceful"
477	    },
478	    "tables": [
479	      "Table S12: Binary F1 under edit conditions (baseline, 5%, 10%, 20%, LLM rephrase) with CI"
480	    ],
481	    "figures": [],
482	    "analysis": "Graceful degradation profile 支持论文 practical utility argument (RC5)。 LLM rephrase 4.5pp drop 在可接受范围 — 即使文本被 lightly edited， depth signal 仍有信息量。Heavy editing (20%) 的 10.4pp drop 诚实报告为 limitation，但 realistic human editing 更接近 5-10% level。 Multiclass drop (-7.1pp) > binary drop (-4.5pp)：editing 主要 blur gen-1/gen-2+ boundary， gen-0 detection (human vs LLM) 更 robust to editing。\n\n\nLLM rephrase drop 4.5pp (在 [3.0, 5.0] 范围内)，为 graceful degradation 而非 catastrophic failure。5% random replacement 仅降 4.6pp 因为 distributional features (TTR, entropy, hapax) 是 global statistics — sparse point noise 不改变 aggregate patterns。 10% drop 8.1pp 因为开始影响 type/token ratio 的分子 (unique word count)。 20% drop 10.4pp 因为大规模替换直接扰乱 lexical diversity，但仍远优于 chance (0.50)。 LLM rephrase (edit_distance ~50%, avg 1.69 sentences replaced) drop 4.5pp， 介于 5-10% random 之间：LLM rephrasing 保持 coherence 和 topic 但改变局部 word choice → surface features (hapax, TTR) 被部分扰乱， reference features (entropy) 更 robust 因为 rephrased text 的 NLL 仍保留 depth-dependent pattern。\n"
483	  },
484	  {
485	    "name": "ld_score_feature",
486	    "description": "将 LD-Score (character-level distribution signature) 作为第 8 个特征加入 ensemble",
487	    "results": {
488	      "ld_score_standalone_logo_f1": 0.721,
489	      "ld_score_spearman_with_depth": 0.794,
490	      "seven_feature_logo_f1": 0.798,
491	      "eight_feature_logo_f1": 0.801,
492	      "delta_adding_ld_score_pp": 0.3,
493	      "ld_score_feature_importance_rank": 5,
494	      "ld_score_correlations": {
495	        "with_hapax_ratio": 0.72,
496	        "with_ttr": 0.68,
497	        "with_entropy_mean": 0.51
498	      },
499	      "ld_score_corrected_cv_f1": 0.793
500	    },
501	    "tables": [
502	      "Table S13: 8-feature vs 7-feature LOGO comparison",
503	      "Table S14: Feature correlation matrix (8×8)"
504	    ],
505	    "figures": [],
506	    "analysis": "LD-Score 不纳入 paper 主线 feature set，在 appendix 作为 supplementary evidence 报告。 Character-level 信号已被 word-level features 充分捕捉。 7-feature set 保持为推荐方案 (simplicity, interpretability, efficiency)。 LD-Score 作为 baseline detector (plan_015) 的价值高于作为 ensemble feature 的价值。\n\n\nLD-Score 单独有 moderate ordinal signal (F1=0.721, Spearman ρ=0.794)， 但加入 7-feature ensemble 后仅提升 0.3pp。原因：LD-Score 测量 character bigram distribution 的 divergence from reference，与 word-level surface features (hapax r=0.72, TTR r=0.68) 高度相关 — character-level 词汇多样性衰减与 word-level 衰减高度 co-linear。 LD-Score 的独立贡献仅在于 character bigram patterns 对特定 generator family (尤其是 BPE tokenization 差异大的 model) 有额外 sensitivity， 但这在 LOGO 跨 generator evaluation 中被 averaging 稀释。 Feature importance 排名第 5 (在 entropy_std 和 entropy_max 之间)， 不足以 justify 增加 feature 的复杂度。\n"
507	  },
508	  {
509	    "name": "end_to_end_classifier",
510	    "description": "QLoRA fine-tuned end-to-end depth classifier vs 7-feature handcrafted ensemble",
511	    "results": {
512	      "qlora_base_3class_f1": 0.881,
513	      "qlora_base_binary_f1": 0.826,
514	      "qlora_base_5class_f1": 0.551,
515	      "qlora_instruct_3class_f1": 0.897,
516	      "qlora_instruct_binary_f1": 0.852,
517	      "seven_feature_3class_f1": 0.773,
518	      "seven_feature_binary_f1": 0.694,
519	      "qlora_advantage_3class_pp": 12.4,
520	      "qlora_advantage_binary_pp": 15.8,
521	      "qlora_logo_cross_gen_binary_f1": 0.72,
522	      "qlora_logo_cross_gen_3class_f1": 0.78,
523	      "cost_comparison": {
524	        "seven_feature_gpu_memory_gb": 2.4,
525	        "qlora_gpu_memory_gb": 8.2,
526	        "inference_time_ratio": 6.5
527	      }
528	    },
529	    "tables": [
530	      "Table S15: QLoRA vs 7-feature — F1 (within-CV, LOGO), cost, memory",
531	      "Table S16: QLoRA per-model results (OLMo-base, OLMo-instruct, Qwen-base, Qwen-instruct)"
532	    ],
533	    "figures": [],
534	    "analysis": "QLoRA 定位为 upper bound reference 而非 paper 推荐方案。 7-feature ensemble positioned on efficiency + interpretability + cross-generator robustness。 这 addresses 潜在 \"为什么不用 end-to-end\" 质疑： answer 是 cost-performance tradeoff (2.4× memory, 6.5× speed) 和 cross-generator generalization。 End-to-end 的 LOGO gap (~10pp) 暗示 generator-specific overfitting， 而 7-feature 的 handcrafted nature 保证了 feature 的 generator-agnostic 语义。\n\n\nQLoRA within-distribution 显著优于 7-feature (+12-16pp on binary)， 因为 end-to-end fine-tuning 学习了 handcrafted features 之外的 contextual/positional patterns： 句法结构退化、discourse coherence 下降、repetition 模式等 token-sequence level 信号。 但 QLoRA 的 cross-generator generalization (LOGO binary ~0.72) 远低于 within-distribution (0.826-0.852)，gap ~10pp：end-to-end model 部分 overfit 到 generator-specific token patterns 而非 depth-universal distributional shift。 5-class QLoRA (0.551) 仅比 handcrafted (0.503) 高 ~5pp， 确认 finer classification 的 bottleneck 是 task-inherent difficulty 而非 feature limitation。 7-feature ensemble 的优势在于：(a) 2.4× less GPU memory, (b) 6.5× faster inference, (c) interpretable (每个 feature 有 clear DDR 语义), (d) cross-generator 泛化更稳定 (within-LOGO variance 更小)。\n"
535	  },
536	  {
537	    "name": "text_length_control",
538	    "description": "Text length confound 控制分析 (RC10)",
539	    "results": {
540	      "spearman_length_depth_range": "[-0.066, +0.134]",
541	      "length_depth_correlation": "weak (|ρ|<0.14)",
542	      "length_matched_binary_f1": 0.724,
543	      "unmatched_binary_f1": 0.77,
544	      "length_matched_delta_pp": -4.6,
545	      "random_subsample_control_f1": 0.741,
546	      "random_subsample_delta_pp": -2.9,
547	      "deconfounding_attributable_pp": -1.7,
548	      "normalized_ttr_trend_preserved": true,
549	      "normalized_hapax_trend_preserved": true,
550	      "normalized_rho_stronger": true,
551	      "length_is_confound": false,
552	      "dropout_short_text_bias": true
553	    },
554	    "tables": [
555	      "Table S17: Length-matched vs unmatched vs random-subsample F1",
556	      "Table S18: Length distribution statistics by depth (mean, median, IQR)"
557	    ],
558	    "figures": [],
559	    "analysis": "Length confound 被排除 (RC10 fully addressed)。 Paper 中报告 length-matched F1=0.724 作为 conservative estimate， 同时说明 4.6pp drop 主要来自 sample size reduction (2.9pp) 而非 deconfounding (1.7pp)。 Normalized features 的 stronger trend 是 positive evidence： 控制 length 后 depth signal 更纯净。\n\n\nLength 非 primary confound。Length-depth Spearman ρ 在 [-0.066, +0.134] 范围， text length 不随 depth 系统性变化。Length-matched binary F1=0.724 (vs 0.770)， 下降 4.6pp，但 random subsample control (同等 sample size reduction) F1=0.741， 降 2.9pp。因此 4.6pp drop 中仅 ~1.7pp 可归因于 length deconfounding， 其余 2.9pp 来自 sample size reduction。 Length-normalized surface features (fixed-length windows 上的 TTR, hapax) 保留且加强了 trend (|ρ| 更高)，证明 drift 信号来自 vocabulary diversity 的 intrinsic decrease 而非 text 变长/变短。 Dropout short text bias: deeper text 因 generation quality degradation 而更短， 但这是 generation property (depth 的 consequence) 而非 external confound。\n"
560	  },
561	  {
562	    "name": "large_scale_generator",
563	    "description": "添加 7B+ generator (Qwen3-8B-Base) 测试 scale effect",
564	    "results": {
565	      "total_records": 4497,
566	      "unique_seeds": 995,
567	      "depth_distribution": {
568	        "gen0": 995,
569	        "gen1": 979,
570	        "gen2": 937,
571	        "gen3": 831,
572	        "gen4": 755
573	      },
574	      "qwen3_8b_logo_binary_f1": 0.683,
575	      "qwen3_8b_logo_3class_f1": 0.695,
576	      "qwen3_8b_ci": [
577	        0.66,
578	        0.706
579	      ],
580	      "logo_6gen_avg_f1": 0.789,
581	      "logo_6gen_avg_binary_f1": 0.7,
582	      "delta_8b_vs_smaller_avg_pp": -1.7,
583	      "spearman_8b": {
584	        "hapax_ratio": -0.558,
585	        "ttr": -0.542,
586	        "entropy_mean": -0.475,
587	        "entropy_min": -0.303,
588	        "entropy_max": 0.095,
589	        "tail_decay": -0.089,
590	        "entropy_std": -0.076
591	      },
592	      "ddr_pattern_preserved": true,
593	      "scale_attenuation_drifting_rho": "~85% of <3B average",
594	      "feature_importance_8b": {
595	        "hapax_ratio": 0.269,
596	        "entropy_mean": 0.164,
597	        "ttr": 0.159
598	      }
599	    },
600	    "tables": [
601	      "Table 7: Per-generator LOGO F1 (6 generators, 包含 Qwen3-8B)",
602	      "Table S19: Spearman ρ — 8B vs <3B average by feature"
603	    ],
604	    "figures": [],
605	    "analysis": "Scale effect 诚实报告为 limitation 但 DDR 定性 robust。 0.683 仍远优于 chance (0.50)，depth signal 在 8B scale 仍有实用价值。 14B DDR analysis (exp_060) 进一步确认：drifting/stationary 分组在 14B 仍一致， |ρ| 进一步衰减 (hapax -0.507, ttr -0.492) 但分组不变。 核心假设 \"14B scale DDR 模式定性不变\" 成立。\n\n\nQwen3-8B binary F1=0.683，在 scale_8b_logo_binary_f1 [0.65, 0.70] 范围内。 Scale effect 存在但 moderate：8B vs <3B average 降 ~1.7pp LOGO F1。 原因：larger models 的 generation distribution 更 concentrated (lower entropy, tighter vocabulary, less sampling randomness at same temperature)， 压缩了 depth-wise feature margin。Hapax ratio |ρ| 从 <3B 的 0.647 降至 8B 的 0.558 (attenuation ~86%)：8B model 的 baseline vocabulary diversity 较低， depth-wise 衰减的 absolute magnitude 更小。 DDR 模式定性不变：drifting 三特征仍为 |ρ| 最高 (hapax -0.558, ttr -0.542, entropy_mean -0.475)， stationary 特征仍 |ρ|<0.10 (tail_decay -0.089, entropy_max 0.095)。 Depth distribution 显示 deeper text 更多 dropout (d4 仅 755/995)， 比 smaller models 更显著：8B model 的 longer-context generation 更容易 degenerate at deeper depths。\n"
606	  },
607	  {
608	    "name": "ordinal_baseline_comparison",
609	    "description": "现有 detector 连续分数的 ordinal depth signal — 7-feature 相对优势验证",
610	    "results": {
611	      "seven_feature_logo_f1": 0.798,
612	      "seven_feature_ci": [
613	        0.786,
614	        0.799
615	      ],
616	      "avg_logprob_logo_f1": 0.765,
617	      "avg_logprob_ci": [
618	        0.616,
619	        0.82
620	      ],
621	      "avg_logprob_spearman": 0.788,
622	      "ld_score_logo_f1": 0.721,
623	      "ld_score_ci": [
624	        0.588,
625	        0.77
626	      ],
627	      "ld_score_spearman": 0.794,
628	      "fastdetectgpt_logo_f1": 0.627,
629	      "fastdetectgpt_ci": [
630	        0.511,
631	        0.762
632	      ],
633	      "fastdetectgpt_spearman": 0.433,
634	      "binoculars_logo_f1": 0.579,
635	      "binoculars_ci": [
636	        0.405,
637	        0.664
638	      ],
639	      "binoculars_spearman": 0.199,
640	      "bootstrap_7feat_vs_avglogprob": {
641	        "delta_pp": 3.3,
642	        "p": 0.0,
643	        "significant": true
644	      },
645	      "bootstrap_7feat_vs_fdgpt": {
646	        "delta_pp": 6.7,
647	        "p": 0.0,
648	        "significant": true
649	      },
650	      "best_single_detector": "avg_logprob (0.765)",
651	      "seven_feat_minus_best_single_pp": 3.3
652	    },
653	    "tables": [
654	      "Table 3: LOGO F1 — 7-feature vs 4 baseline detectors, with bootstrap CI and Spearman ρ",
655	      "Table S20: Pairwise bootstrap significance tests (7-feature vs each detector)"
656	    ],
657	    "figures": [],
658	    "analysis": "3.3pp 优势虽不巨大但 statistically significant (bootstrap p<0.01)， 符合 Findings paper 的 empirical contribution 标准。 关键 finding 不仅是 performance gap，而是 existing detectors 确实有 moderate ordinal signal (avg_logprob 0.765)，但 7-feature 通过 feature complementarity 显著提升。 这 reframes contribution：不是 \"novel features\" 而是 \"systematic characterization of DDR + principled feature combination\"， 符合 Findings 定位。 Binoculars 的 bug fix (denominator correction) 确保了 fair comparison。 Wide bootstrap CIs for single detectors (e.g. avg_logprob [0.616, 0.820]) 反映 high per-generator variance — 这本身是 7-feature 的优势 (其 CI [0.786, 0.799] 远窄)。\n\n7-feature 优势 3.3pp over best single detector (avg_logprob)， 在 [3.0, 5.0] 范围内，bootstrap p=0.0 确认显著性 (n=1000)。 Avg_logprob 是最强 single detector (F1=0.765) 因为它直接测量 NLL 均值， 正是 drifting features 捕捉的 primary signal — avg_logprob 本质上是 entropy_mean 的 unnormalized version。但 avg_logprob 缺少 shape features 和 surface features 的互补信号。 LD-Score (0.721) 第二强：character-level distribution shift 与 depth 有 moderate 相关 (ρ=0.794)，但 character-level 信息 partially redundant with word-level surface features。 FastDetectGPT (0.627) 较弱：perturbation-based approach 设计用于 binary real/synthetic detection， 其 log probability curvature metric 对 ordinal depth variation 不 sensitive。 Binoculars (0.579) 最弱：two-model probability ratio 中 depth signal 被 ratio 操作 部分 cancel (两个 model 的 NLL 均随 depth 下降，ratio 变化小)。 7-feature 优势的来源是 complementarity：drifting features 捕捉 location shift， stationary features 提供 noise-resistant baseline，surface features 捕捉 generator-agnostic vocabulary impoverishment。三组信号的 combination 优于任何 single metric。\n"
659	  }
660	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86cf0778-39e4-4efb-9b98-ff18e33fc48e",
  "isSidechain": false,
  "promptId": "1ca86b45-b190-47c7-9689-3b48717c505c",
  "type": "user",
  "uuid": "c332b662-622b-4d10-8874-1ad4368d4515",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T232427/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"feature_ablation_and_trend\",\n    \"description\": \"MVP 数据上的三部分分析：(A) feature ablation (full/surface/reference), (B) H1/H2 trend analysis, (C) perplexity pre-validation\",\n    \"results\": {\n      \"ablation_full_macro_f1\": 0.82,\n      \"ablation_surface_only_f1\": 0.763,\n      \"ablation_reference_only_f1\": 0.719,\n      \"ref_vs_surf_bootstrap_ci\": \"[0.706,0.733] vs [0.747,0.774]\",\n      \"mcnemar_full_vs_surface_p\": 0.0,\n      \"mcnemar_full_vs_ref_p\": 0.0,\n      \"h2_drifting_features\": [\n        \"entropy_mean\",\n        \"ttr\",\n        \"hapax_ratio\"\n      ],\n      \"h2_slope_entropy_mean\": -0.29,\n      \"h2_slope_ttr\": -0.034,\n      \"h2_slope_hapax_ratio\": -0.043,\n      \"h2_R2_entropy_mean\": 0.93,\n      \"h2_R2_ttr\": 0.89,\n      \"h2_R2_hapax_ratio\": 0.92,\n      \"h1_stationary_features\": [\n        \"tail_decay\",\n        \"entropy_std\",\n        \"entropy_max\",\n        \"entropy_min\"\n      ],\n      \"h1_slope_tail_decay\": 0.002,\n      \"h1_R2_tail_decay\": 0.03,\n      \"entropy_std_slope\": -0.12,\n      \"entropy_std_R2\": 0.41,\n      \"median_ppl_by_depth\": [\n        13.5,\n        4.96,\n        3.0,\n        2.07,\n        1.72\n      ],\n      \"ppl_depth_trend\": \"monotonic_decrease\"\n    },\n    \"tables\": [\n      \"Table A1: Feature Ablation 5-fold CV — Full 0.820, Surface 0.763, Ref 0.719\",\n      \"Table A2: Per-feature linear trend (slope, R², p-value) across depths 0–4\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Surface 和 reference 信号互补性经 McNemar 确认 (p=0)，是论文 complementarity claim 的基础。 entropy_std 的 intermediate status (|slope|=0.12, R²=0.41) 需在正文中诚实讨论， 但不破坏 3-drifting / 2-stationary 的核心二分法， 因为 entropy_std 的 drift magnitude 仅为 drifting 组的 1/3。 Perplexity pre-validation 确认 NLL 分布中存在 depth-dependent signal，为 Claim 3 建立 baseline。\\n\\n\\nFull set 显著优于任一子集 (5.7-10.1pp)。Surface features 捕捉词汇多样性衰减 (TTR/hapax 随 depth 单调递减)，reference features 捕捉 NLL 分布位移 (entropy_mean drift)，两组信号互补。McNemar p=0 确认非冗余。 H2 drifting features 呈清晰单调趋势 (R²>0.89)：递归生成导致词汇空间收缩 和 NLL 均值下降 (recursive compression)。H1 stationary features 保持平坦 (tail_decay R²=0.03)：NLL 分布的 shape 参数在 location shift 下近似不变。 entropy_std 弱趋势 (R²=0.41) 远低于 drifting 组，归为 intermediate 不影响主叙事。 Perplexity 单调递减：deeper text 对 reference model 更 predictable， 因为 model 自身输出的 recursive compression 使 NLL 分布左移。\\n\"\n  },\n  {\n    \"name\": \"cross_generator_evaluation\",\n    \"description\": \"5-generator LOGO 跨 generator 泛化评估 (Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B)\",\n    \"results\": {\n      \"total_records\": 23032,\n      \"generators\": [\n        \"pythia-2.8b\",\n        \"pythia-1b\",\n        \"olmo-2-1b\",\n        \"qwen3-1.7b\",\n        \"qwen3-0.6b\"\n      ],\n      \"families\": [\n        \"Pythia\",\n        \"OLMo\",\n        \"Qwen\"\n      ],\n      \"logo_macro_f1\": 0.804,\n      \"logo_binary_f1\": 0.72,\n      \"logo_binary_ci\": [\n        0.708,\n        0.732\n      ],\n      \"per_gen_macro_f1\": {\n        \"pythia-1b\": 0.851,\n        \"pythia-2.8b\": 0.804,\n        \"qwen3-0.6b\": 0.818,\n        \"qwen3-1.7b\": 0.805,\n        \"olmo-2-1b\": 0.752\n      },\n      \"per_gen_binary_f1\": {\n        \"pythia-1b\": 0.724,\n        \"pythia-2.8b\": 0.72,\n        \"qwen3-0.6b\": 0.715,\n        \"qwen3-1.7b\": 0.71,\n        \"olmo-2-1b\": 0.67\n      },\n      \"per_gen_binary_variance_pp\": 5.4,\n      \"lofo_binary_f1\": 0.705,\n      \"lofo_per_family\": {\n        \"pythia_held_out\": 0.69,\n        \"olmo_held_out\": 0.72,\n        \"qwen_held_out\": 0.706\n      },\n      \"ablation_full_f1\": 0.804,\n      \"ablation_reference_only_f1\": 0.754,\n      \"ablation_surface_only_f1\": 0.747,\n      \"mcnemar_p\": 0.0,\n      \"entropy_std_importance_drop\": 0.0049,\n      \"entropy_std_drift\": 0.12,\n      \"top_features\": [\n        \"hapax_ratio_0.289\",\n        \"ttr_0.168\",\n        \"entropy_mean_0.160\"\n      ]\n    },\n    \"tables\": [\n      \"Table 2: Per-generator LOGO macro/binary F1 with 95% CI\",\n      \"Table 3: LOFO per-family binary F1\",\n      \"Table S1: Feature importance rankings (5-gen aggregate)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"跨 generator 泛化成功。Per-gen 方差 <10pp 满足 best 档阈值。 LOFO binary F1=0.705 确认跨 family 泛化：仅比 LOGO 低 1.5pp， 证明 Pythia family overlap 未显著 inflate 结果。 Feature ablation 确认 complementarity (McNemar p=0)， 且 pattern 与 plan_001 一致 (full > surface ≈ reference)。\\n\\n\\n5-gen LOGO binary F1=0.720 高于后续 8-gen headline (0.694)， 因为 5-gen set 不包含较难的 Mistral-7B (per-gen F1=0.633) 和 Gemma-2-2B (anomaly)。 Per-gen binary 方差 5.4pp (<10pp 阈值) 证明跨 generator 泛化稳健。 OLMo-2-1B 最低 (0.670) 因为 OLMo 架构 (非 GPT-NeoX/Llama 系) 产生的 distributional pattern 与 Pythia family 差异最大。 Pythia-1B 最高 (0.724) 部分受益于 Pythia-2.8B 在 training fold 中的 family overlap， 但 LOFO 分析控制了此效应 (Pythia held-out 0.690 仅降 3pp)。 Hapax_ratio 仍是最重要特征 (0.289 importance)， 因为词汇多样性衰减是跨 generator 最一致的 depth signal。\\n\"\n  },\n  {\n    \"name\": \"cross_family_reference_model\",\n    \"description\": \"Non-Pythia reference models (OLMo-2-1B, Qwen3-0.6B) feature extraction，DDR 跨 reference model falsification test\",\n    \"results\": {\n      \"logo_f1_pythia_ref\": 0.803,\n      \"logo_f1_olmo_ref\": 0.807,\n      \"logo_f1_qwen_ref\": 0.816,\n      \"cross_ref_f1_spread_pp\": 1.3,\n      \"entropy_drift_all_refs_negative\": true,\n      \"pythia_ref_drift_range\": [\n        -1.19,\n        -1.4\n      ],\n      \"olmo_ref_drift_range\": [\n        -0.61,\n        -0.91\n      ],\n      \"qwen_ref_drift_range\": [\n        -0.96,\n        -1.35\n      ],\n      \"spearman_by_ref\": {\n        \"pythia_ref\": {\n          \"hapax_ratio\": -0.647,\n          \"ttr\": -0.63,\n          \"entropy_mean\": -0.61,\n          \"tail_decay\": -0.04,\n          \"entropy_max\": 0.05\n        },\n        \"olmo_ref\": {\n          \"hapax_ratio\": -0.647,\n          \"ttr\": -0.63,\n          \"entropy_mean\": -0.585,\n          \"tail_decay\": -0.038,\n          \"entropy_max\": 0.055\n        },\n        \"qwen_ref\": {\n          \"hapax_ratio\": -0.647,\n          \"ttr\": -0.63,\n          \"entropy_mean\": -0.62,\n          \"tail_decay\": -0.042,\n          \"entropy_max\": 0.048\n        }\n      },\n      \"stationary_rho_max_across_refs\": 0.055,\n      \"ddr_is_pythia_artifact\": false\n    },\n    \"tables\": [\n      \"Table 4: LOGO macro F1 by reference model (3 refs × 5 generators)\",\n      \"Table S2: Per-feature Spearman ρ by reference model (7×3 matrix)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"DDR 非 Pythia artifact。这是 Claim 2 最重要的 robustness result。 Entropy_mean drift 方向跨 3 个不同架构 family 的 ref model 一致为负， 证明 drift 来自 generation 过程本身 (recursive compression) 而非特定 ref model 的 bias。 Shape feature stationarity 同样跨 ref 稳健。论文可自信表述 DDR 为 generation-intrinsic property。\\n\\n\\nDDR 模式跨 3 个 reference model (Pythia-410M, OLMo-2-1B, Qwen3-0.6B) 完全稳健。 Surface features (hapax, TTR) 完全不依赖 reference model，rho 跨 ref 完全一致。 Reference features (entropy_mean) 方向一致 (均为负)，magnitude 因 ref model 自身 perplexity calibration 不同而略有差异 (OLMo 偏低)，但不影响 drifting/stationary 分组。 Shape features (tail_decay, entropy_max) 跨 ref 均 |ρ|<0.06。 Qwen ref 分类 F1 略优 (0.816 vs 0.803) 因为 Qwen family 在 generator set 中有 2 个 model，ref-generator family match 提升了 entropy feature 的 discriminability， 但差异仅 1.3pp 证明 reference model 选择不是 critical design decision。 这是 Claim 2 的关键 falsification test：如果 DDR 仅在 Pythia ref 下出现， 叙事崩溃。Best 档下三个 ref 均重现相同分组。\\n\"\n  },\n  {\n    \"name\": \"downstream_utility\",\n    \"description\": \"OLMo-1B fine-tuning on depth-stratified data, negative downstream finding (Claim 3)\",\n    \"results\": {\n      \"model\": \"OLMo-2-0425-1B (1485M)\",\n      \"total_runs\": 15,\n      \"seeds\": [\n        42,\n        123,\n        456\n      ],\n      \"variants\": {\n        \"all\": {\n          \"ppl_mean\": 2.335,\n          \"ppl_std\": 0.0003,\n          \"n_train\": 12299\n        },\n        \"size_matched\": {\n          \"ppl_mean\": 2.367,\n          \"ppl_std\": 0.0002,\n          \"n_train\": 3951\n        },\n        \"depth01\": {\n          \"ppl_mean\": 2.387,\n          \"ppl_std\": 0.001,\n          \"n_train\": 3951\n        },\n        \"binary_filtered\": {\n          \"ppl_mean\": 2.389,\n          \"ppl_std\": 0.001,\n          \"n_train\": 3951\n        },\n        \"depth0_only\": {\n          \"ppl_mean\": 2.681,\n          \"ppl_std\": 0.001,\n          \"n_train\": 797\n        }\n      },\n      \"ranking\": \"all(2.335) < size_matched(2.367) < depth01(2.387) ≈ binary_filtered(2.389) << depth0_only(2.681)\",\n      \"tost_size_matched_vs_depth01\": {\n        \"margin_pct\": 2,\n        \"p_value\": 0.00011,\n        \"equivalence_confirmed\": true\n      },\n      \"tost_size_matched_vs_binary\": {\n        \"margin_pct\": 2,\n        \"p_value\": 9e-05,\n        \"equivalence_confirmed\": true\n      },\n      \"tost_margin_sensitivity\": {\n        \"margin_1pct_p\": 0.08,\n        \"margin_2pct_p\": 0.00011,\n        \"margin_3pct_p\": 2e-06,\n        \"margin_5pct_p\": 0.0\n      },\n      \"cohens_d_matched_vs_depth01\": 0.85,\n      \"seed_variance_max_ppl\": 0.002\n    },\n    \"tables\": [\n      \"Table 5: Perplexity by training variant (5 variants × 3 seeds, mean ± std)\",\n      \"Table S3: TOST margin sensitivity (±1%, ±2%, ±3%, ±5%)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Negative finding 是 Claim 3 的核心。Best 档下 TOST 明确确认等价， 且 ranking (random > depth-aware) 是 informative negative： 即使 depth signal 存在，filtering 不改善 downstream quality。 诚实报告 limitation：仅测试了单一 downstream task (CLM) 和单一 metric (perplexity)。 但 TOST + 3 seeds + 5 variants 的设计远超 typical negative finding 的 evidence bar。\\n\\n\\nNegative finding 清晰且符合预期。Depth-aware curation 不优于 random subsampling： size_matched (random) ppl=2.367 优于 depth01 ppl=2.387 和 binary_filtered ppl=2.389。 原因：depth filtering 在移除 deeper text 的同时也移除了 diverse training signal， random subsampling 保留了更完整的 distributional coverage。 TOST at ±2% margin 确认等价 (p=1.1×10⁻⁴)：depth-aware 和 random 在实际意义上无差异。 ±1% margin 未 reject (p=0.08)，这是 honest boundary — 极小 margin 下无法确认等价， 但 ±2% 足以满足实际应用场景的 equivalence threshold。 depth0_only (ppl=2.681) 明显最差因为仅 797 samples (严重不足 + 缺乏 diversity)。 Seed variance 极小 (<0.002) 因为 OLMo-1B fine-tuning 在此 data scale 下非常稳定， Cohen's d inflated 但 TOST 是 appropriate test。 这确立了 depth fingerprinting 作为 diagnostic tool 的定位。\\n\"\n  },\n  {\n    \"name\": \"prompt_type_comparison\",\n    \"description\": \"Continuation vs elaboration vs inspired_rewriting chains 比较 (Pythia-2.8B, 1000 seeds)\",\n    \"results\": {\n      \"cv_f1\": {\n        \"continuation\": 0.781,\n        \"inspired_rewriting\": 0.737,\n        \"elaboration\": 0.73\n      },\n      \"lopto_f1\": {\n        \"held_out_continuation\": 0.762,\n        \"held_out_elaboration\": 0.762,\n        \"held_out_rewriting\": 0.733,\n        \"avg\": 0.753\n      },\n      \"depth_retention_d4_d0\": {\n        \"continuation\": 0.831,\n        \"elaboration\": 0.986,\n        \"rewriting\": 0.939\n      },\n      \"spearman_rho\": {\n        \"continuation\": {\n          \"hapax\": -0.651,\n          \"ttr\": -0.629,\n          \"entropy_mean\": -0.665\n        },\n        \"elaboration\": {\n          \"hapax\": -0.674,\n          \"ttr\": -0.666,\n          \"entropy_mean\": -0.583\n        },\n        \"rewriting\": {\n          \"hapax\": -0.67,\n          \"ttr\": -0.659,\n          \"entropy_mean\": -0.564\n        }\n      },\n      \"feature_drift_magnitude\": {\n        \"continuation\": {\n          \"hapax\": -0.74,\n          \"ttr\": -0.607,\n          \"entropy_mean\": -0.557\n        },\n        \"elaboration\": {\n          \"hapax\": -0.828,\n          \"ttr\": -0.641,\n          \"entropy_mean\": -0.471\n        },\n        \"rewriting\": {\n          \"hapax\": -0.8,\n          \"ttr\": -0.618,\n          \"entropy_mean\": -0.477\n        }\n      },\n      \"max_gap_cv_pp\": 5.1\n    },\n    \"tables\": [\n      \"Table S4: Per-prompt-type CV F1 (within) and LOPTO F1 (cross)\",\n      \"Table S5: Spearman ρ by feature × prompt type\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Prompt-type dependence (continuation 0.781 vs elaboration 0.730 = 5.1pp gap) 诚实报告但 DDR 模式在所有 type 下定性一致。这支持 ecological validity (RC6)： real-world contamination 涉及多种 generation prompt，depth signal 在所有类型下均可提取。 LOPTO avg 0.753 证明不需要知道 prompt type 即可部署。 Continuation-elaboration gap 归因于 continuation 更自由的 distributional drift space， 不是方法论缺陷。\\n\\n\\n三种 prompt type 均保留 depth signal (所有 drifting |ρ|>0.55)，但 continuation 最强 (CV F1=0.781)。Continuation 纯续写最大化 recursive compression — 每步输出成为下一步 的 full context，无语义约束。Elaboration 最弱 (0.730) 因为保持与 seed 的语义关联， 限制了 distributional drift 幅度。Rewriting 居中 (0.737) 因为 semantic preservation 弱于 elaboration 但强于 continuation。 Depth retention 差异大 (elaboration 98.6% vs continuation 83.1%)：continuation 的 deeper text 更短更容易被 min-length filter 截断。 LOPTO 证明跨 prompt type 泛化可行 (avg 0.753)： 在一种 prompt type 上训练仍能在其他类型上保持合理性能。 Feature drift magnitude: elaboration 的 hapax drift 反而更大 (-0.828 vs -0.740) 因为 elaboration 的 higher retention rate 保留了更多 deep samples，使 regression 更稳定。\\n\"\n  },\n  {\n    \"name\": \"paraphrastic_comparison\",\n    \"description\": \"Paraphrastic chains vs continuation chains, 测试 attractor convergence theory\",\n    \"results\": {\n      \"paraphrastic_cv_binary_f1\": 0.618,\n      \"paraphrastic_cv_3class_f1\": 0.68,\n      \"continuation_cv_binary_f1\": 0.781,\n      \"continuation_cv_3class_f1\": 0.834,\n      \"delta_binary_pp\": -16.3,\n      \"paraphrastic_spearman\": {\n        \"hapax_ratio\": -0.3,\n        \"ttr\": -0.26,\n        \"entropy_mean\": -0.33,\n        \"tail_decay\": -0.02,\n        \"entropy_max\": 0.03\n      },\n      \"paraphrastic_convergence_depth\": 3,\n      \"paraphrastic_depth3_vs_depth2_binary_f1\": 0.525,\n      \"continuation_depth3_vs_depth2_binary_f1\": 0.64,\n      \"depth_retention_paraphrastic_d4_d0\": 0.97,\n      \"semantic_sim_d0_d4_paraphrastic\": 0.88,\n      \"semantic_sim_d0_d4_continuation\": 0.52\n    },\n    \"tables\": [\n      \"Table S6: Paraphrastic vs continuation — CV F1, Spearman ρ, convergence depth\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Paraphrastic 对比清晰界定了本文 contribution scope。DDR 是 non-paraphrastic chains 的特有现象，因为只有 unconstrained generation 允许 distributional drift 无约束累积。 这与 LLM as Broken Telephone (ACL 2025) 互补：他们研究 paraphrastic attractor cycles， 我们研究 non-paraphrastic depth drift — 两者共同覆盖了 iterative generation 的全景。 Paper 在 related work 中 explicitly connect 两条线。\\n\\n\\nParaphrastic chains 的 depth signal 显著弱于 non-paraphrastic (binary gap 16.3pp)， 符合 attractor convergence theory (ACL 2025)。Paraphrasing 对 input 施加 semantic preservation constraint，限制 distributional drift：vocabulary diversity 在 paraphrase 中近似保持 (|ρ|<0.33 for all features)，因为 paraphrase 倾向复用相同 content words。 ~3 步后 features plateau (depth3 vs depth2 binary F1≈0.525, near chance)， 因为 paraphrastic chain 收敛到 model-specific attractor cycle。 Continuation 无此 constraint，drift 持续累积 (depth3 vs depth2 F1=0.640 仍有信号)。 Depth retention 极高 (97%)：paraphrasing 保持 text length 稳定。 Semantic similarity d0→d4 高 (0.88)：paraphrase 保留了 meaning， 而 continuation (0.52) 已显著 topic-drift。\\n\"\n  },\n  {\n    \"name\": \"cross_model_chains\",\n    \"description\": \"Cross-model chains (每步不同 generator) vs single-model chains (RC4, ecological validity)\",\n    \"results\": {\n      \"cross_model_binary_f1\": 0.83,\n      \"cross_model_3class_f1\": 0.789,\n      \"cross_model_binary_ci\": [\n        0.812,\n        0.848\n      ],\n      \"single_model_logo_binary_f1\": 0.694,\n      \"delta_cross_vs_single_pp\": 13.6,\n      \"cross_model_logo_per_gen\": {\n        \"pythia-2.8b\": 0.852,\n        \"pythia-1b\": 0.838,\n        \"olmo-2-1b\": 0.812,\n        \"qwen3-1.7b\": 0.843,\n        \"qwen3-0.6b\": 0.828\n      },\n      \"cross_model_per_gen_variance_pp\": 4.0,\n      \"heterogeneity_amplification_factor\": 1.2,\n      \"ddr_cross_model\": {\n        \"hapax_ratio_rho\": -0.72,\n        \"ttr_rho\": -0.69,\n        \"entropy_mean_rho\": -0.68,\n        \"tail_decay_rho\": -0.05\n      },\n      \"cross_model_binary_f1_full_set\": 0.764\n    },\n    \"tables\": [\n      \"Table 6: Cross-model vs single-model — binary/3-class F1 with bootstrap CI\",\n      \"Table S7: Per-generator LOGO F1 on cross-model chains\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cross-model F1=0.830 是论文最强泛化 result。Heterogeneity amplification 是 key insight： 真实 web contamination 涉及 diverse generators → depth signal 更强而非更弱。 这直接 addresses RC4 且 strengthens narrative： controlled single-model evaluation (F1=0.694) 是 conservative lower bound， realistic multi-model scenario 反而更容易检测。 Per-gen variance 4.0pp (cross-model) < 5.4pp (single-model)， 进一步证明 heterogeneity 产生更稳定的信号。\\n\\n\\nCross-model binary F1=0.830 (5-gen subset, generator-level LOGO)，满足核心假设 (≥0.76)。Heterogeneous generators 在每步引入不同 distributional bias， 产生 heterogeneity amplification (factor=1.20)：每步 generator change 叠加产生的 feature divergence 大于单一 generator 的 recursive drift。 单模型 chain 中 model-specific patterns 在 deeper depths 可能趋于 model-specific attractor state，而 cross-model chain 每步注入 fresh distributional perturbation， 阻止 convergence。这导致 drifting features |ρ| 更高 (hapax -0.72 vs single-model -0.647)。 Cross-model 场景更接近真实 web contamination (多模型参与)， 因此 higher F1 是 positive ecological validity result。 Full 8-gen set 的 cross-model binary F1=0.764 (略低于 5-gen 的 0.830)， 因为 8-gen set 包含了更 diverse 的 generator combinations。\\n\"\n  },\n  {\n    \"name\": \"multi_domain_seeds\",\n    \"description\": \"4-domain seeds 扩展 (Wikipedia, news, scientific, creative/code)\",\n    \"results\": {\n      \"per_domain_binary_f1\": {\n        \"wikipedia\": 0.694,\n        \"news\": 0.712,\n        \"academic\": 0.628,\n        \"code\": 0.687\n      },\n      \"per_domain_binary_ci\": {\n        \"news\": [\n          0.69,\n          0.733\n        ],\n        \"academic\": [\n          0.603,\n          0.652\n        ],\n        \"code\": [\n          0.664,\n          0.71\n        ]\n      },\n      \"per_domain_3class_f1\": {\n        \"wikipedia\": 0.77,\n        \"news\": 0.715,\n        \"academic\": 0.656,\n        \"code\": 0.673\n      },\n      \"overall_cross_domain_binary_f1\": 0.676,\n      \"domain_gap_max_pp\": 8.4,\n      \"worst_domain\": \"academic\",\n      \"best_new_domain\": \"news\",\n      \"ddr_by_domain\": {\n        \"wikipedia\": {\n          \"hapax_rho\": -0.647,\n          \"entropy_mean_rho\": -0.61\n        },\n        \"news\": {\n          \"hapax_rho\": -0.621,\n          \"entropy_mean_rho\": -0.595\n        },\n        \"academic\": {\n          \"hapax_rho\": -0.543,\n          \"entropy_mean_rho\": -0.52\n        },\n        \"code\": {\n          \"hapax_rho\": -0.63,\n          \"entropy_mean_rho\": -0.581\n        }\n      },\n      \"ddr_pattern_consistent_across_domains\": true\n    },\n    \"tables\": [\n      \"Table S8: Per-domain binary F1 with 95% CI (t=0.7 and t=1.0)\",\n      \"Table S9: Spearman ρ by feature × domain\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Multi-domain evaluation supports ecological validity (RC6)。 Domain gap (8.4pp) 诚实报告为 limitation 但不动摇核心 claim： 所有 domain 均显著优于 random baseline (0.50)，且 DDR 模式定性一致。 Academic domain weakness 归因于 genre-specific ceiling effect， 可在 future work 中通过 domain-specific feature engineering 改善。\\n\\n\\nDepth signal 跨 domain 稳健但有 domain-specific variation (max gap 8.4pp)。 Academic 最弱 (0.628) 因为学术写作高度 formulaic — 严格的 genre conventions (句式结构、术语使用) 限制了 generation 的 distributional drift 空间， 且 academic text 的 baseline vocabulary diversity 已较低 (TTR ceiling effect)。 News 最优 (0.712) 因为 news text 词汇丰富度高、topic diversity 大， generation drift 有更大的 feature margin 可供利用。 Code (0.687) 接近 average：代码的 structural patterns (语法约束、缩进) 提供额外区分信号，但 entropy features 被 code syntax 的 deterministic tokens 压缩。 Wikipedia baseline (0.694) 与 8-gen LOGO headline 一致。 DDR 模式跨 domain 定性一致 (所有 domain drifting |ρ|>0.52)， 但 academic domain 的 |ρ| 最低，与 lowest F1 一致。\\n\"\n  },\n  {\n    \"name\": \"finer_grained_ordinal\",\n    \"description\": \"5-class ordinal classification (gen-0 to gen-4), ordinal methods (CORAL, Frank-Hall) 比较\",\n    \"results\": {\n      \"xgboost_5class_f1\": 0.503,\n      \"coral_5class_f1\": 0.497,\n      \"frank_hall_5class_f1\": 0.501,\n      \"xgboost_3class_f1\": 0.773,\n      \"ordinal_mae\": 0.72,\n      \"per_class_5class_f1\": {\n        \"gen0\": 0.952,\n        \"gen1\": 0.518,\n        \"gen2\": 0.348,\n        \"gen3\": 0.325,\n        \"gen4\": 0.372\n      },\n      \"confusion_matrix_bottleneck\": \"gen-1/gen-2 boundary concentrates 86% of binary errors as FNs\",\n      \"gen2_gen3_mutual_misclass_rate\": 0.42\n    },\n    \"tables\": [\n      \"Table S10: 5×5 confusion matrix (XGBoost)\",\n      \"Table S11: Ordinal methods comparison (XGBoost, CORAL, Frank-Hall) + 3-class reference\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"3-class (gen-0/gen-1/gen-2+) 是 practical resolution ceiling。 5-class 不可行的根本原因是 distributional drift 的 diminishing marginal return： depth 每增加一步，feature shift magnitude 递减 (concave curve)。 这是 generation process 的 intrinsic property (类似 entropy rate convergence)， 不可通过更好的 classifier 或更多 features 解决。 诚实报告为 scope boundary，不削弱论文核心 contribution (3-class 已是 novel formulation)。\\n\\n\\n5-class F1≈0.50, ordinal methods (CORAL, Frank-Hall) 无改善 (<1pp)。 Gen-0 仍高 F1 (0.952) 因为 seed sharing 提供强信号 (human text vs LLM text 的 distributional gap)。 Gen-1 moderate (0.518)：与 gen-0 的 gap (first generation step) 最大，但与 gen-2 的 margin 已很小。Gen-2/gen-3/gen-4 严重混淆 (mutual misclass 42%)： recursive drift 在前 2 步最陡峭 (feature curve 呈 concave shape, 非线性)， deeper depths 的 marginal drift 已趋近 noise floor。 Ordinal methods 不优于 standard XGBoost 因为 feature space 中的 ordinal structure 在 deeper depths 退化 — 非线性 plateau 而非 monotonic 递增。 CORAL 和 Frank-Hall 假设 ordinal margin 在所有相邻 class pairs 间近似均匀， 但实际 gen-0→gen-1 margin >> gen-2→gen-3 margin，violating this assumption。\\n\"\n  },\n  {\n    \"name\": \"human_edit_robustness\",\n    \"description\": \"模拟人类编辑的 robustness test — (A) random word replacement (5%/10%/20%) + (B) LLM rephrase\",\n    \"results\": {\n      \"baseline_binary_f1\": 0.695,\n      \"random_replacement\": {\n        \"pct5_binary_f1\": 0.65,\n        \"pct10_binary_f1\": 0.614,\n        \"pct20_binary_f1\": 0.591,\n        \"pct5_drop_pp\": -4.6,\n        \"pct10_drop_pp\": -8.1,\n        \"pct20_drop_pp\": -10.4\n      },\n      \"llm_rephrase\": {\n        \"binary_f1\": 0.647,\n        \"binary_ci\": [\n          0.631,\n          0.662\n        ],\n        \"multiclass_f1\": 0.667,\n        \"multiclass_ci\": [\n          0.655,\n          0.68\n        ],\n        \"binary_drop_pp\": -4.5,\n        \"multiclass_drop_pp\": -7.1\n      },\n      \"edit_distance_ratio\": 0.507,\n      \"avg_sentences_replaced\": 1.69,\n      \"degradation_profile\": \"graceful\"\n    },\n    \"tables\": [\n      \"Table S12: Binary F1 under edit conditions (baseline, 5%, 10%, 20%, LLM rephrase) with CI\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Graceful degradation profile 支持论文 practical utility argument (RC5)。 LLM rephrase 4.5pp drop 在可接受范围 — 即使文本被 lightly edited， depth signal 仍有信息量。Heavy editing (20%) 的 10.4pp drop 诚实报告为 limitation，但 realistic human editing 更接近 5-10% level。 Multiclass drop (-7.1pp) > binary drop (-4.5pp)：editing 主要 blur gen-1/gen-2+ boundary， gen-0 detection (human vs LLM) 更 robust to editing。\\n\\n\\nLLM rephrase drop 4.5pp (在 [3.0, 5.0] 范围内)，为 graceful degradation 而非 catastrophic failure。5% random replacement 仅降 4.6pp 因为 distributional features (TTR, entropy, hapax) 是 global statistics — sparse point noise 不改变 aggregate patterns。 10% drop 8.1pp 因为开始影响 type/token ratio 的分子 (unique word count)。 20% drop 10.4pp 因为大规模替换直接扰乱 lexical diversity，但仍远优于 chance (0.50)。 LLM rephrase (edit_distance ~50%, avg 1.69 sentences replaced) drop 4.5pp， 介于 5-10% random 之间：LLM rephrasing 保持 coherence 和 topic 但改变局部 word choice → surface features (hapax, TTR) 被部分扰乱， reference features (entropy) 更 robust 因为 rephrased text 的 NLL 仍保留 depth-dependent pattern。\\n\"\n  },\n  {\n    \"name\": \"ld_score_feature\",\n    \"description\": \"将 LD-Score (character-level distribution signature) 作为第 8 个特征加入 ensemble\",\n    \"results\": {\n      \"ld_score_standalone_logo_f1\": 0.721,\n      \"ld_score_spearman_with_depth\": 0.794,\n      \"seven_feature_logo_f1\": 0.798,\n      \"eight_feature_logo_f1\": 0.801,\n      \"delta_adding_ld_score_pp\": 0.3,\n      \"ld_score_feature_importance_rank\": 5,\n      \"ld_score_correlations\": {\n        \"with_hapax_ratio\": 0.72,\n        \"with_ttr\": 0.68,\n        \"with_entropy_mean\": 0.51\n      },\n      \"ld_score_corrected_cv_f1\": 0.793\n    },\n    \"tables\": [\n      \"Table S13: 8-feature vs 7-feature LOGO comparison\",\n      \"Table S14: Feature correlation matrix (8×8)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"LD-Score 不纳入 paper 主线 feature set，在 appendix 作为 supplementary evidence 报告。 Character-level 信号已被 word-level features 充分捕捉。 7-feature set 保持为推荐方案 (simplicity, interpretability, efficiency)。 LD-Score 作为 baseline detector (plan_015) 的价值高于作为 ensemble feature 的价值。\\n\\n\\nLD-Score 单独有 moderate ordinal signal (F1=0.721, Spearman ρ=0.794)， 但加入 7-feature ensemble 后仅提升 0.3pp。原因：LD-Score 测量 character bigram distribution 的 divergence from reference，与 word-level surface features (hapax r=0.72, TTR r=0.68) 高度相关 — character-level 词汇多样性衰减与 word-level 衰减高度 co-linear。 LD-Score 的独立贡献仅在于 character bigram patterns 对特定 generator family (尤其是 BPE tokenization 差异大的 model) 有额外 sensitivity， 但这在 LOGO 跨 generator evaluation 中被 averaging 稀释。 Feature importance 排名第 5 (在 entropy_std 和 entropy_max 之间)， 不足以 justify 增加 feature 的复杂度。\\n\"\n  },\n  {\n    \"name\": \"end_to_end_classifier\",\n    \"description\": \"QLoRA fine-tuned end-to-end depth classifier vs 7-feature handcrafted ensemble\",\n    \"results\": {\n      \"qlora_base_3class_f1\": 0.881,\n      \"qlora_base_binary_f1\": 0.826,\n      \"qlora_base_5class_f1\": 0.551,\n      \"qlora_instruct_3class_f1\": 0.897,\n      \"qlora_instruct_binary_f1\": 0.852,\n      \"seven_feature_3class_f1\": 0.773,\n      \"seven_feature_binary_f1\": 0.694,\n      \"qlora_advantage_3class_pp\": 12.4,\n      \"qlora_advantage_binary_pp\": 15.8,\n      \"qlora_logo_cross_gen_binary_f1\": 0.72,\n      \"qlora_logo_cross_gen_3class_f1\": 0.78,\n      \"cost_comparison\": {\n        \"seven_feature_gpu_memory_gb\": 2.4,\n        \"qlora_gpu_memory_gb\": 8.2,\n        \"inference_time_ratio\": 6.5\n      }\n    },\n    \"tables\": [\n      \"Table S15: QLoRA vs 7-feature — F1 (within-CV, LOGO), cost, memory\",\n      \"Table S16: QLoRA per-model results (OLMo-base, OLMo-instruct, Qwen-base, Qwen-instruct)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"QLoRA 定位为 upper bound reference 而非 paper 推荐方案。 7-feature ensemble positioned on efficiency + interpretability + cross-generator robustness。 这 addresses 潜在 \\\"为什么不用 end-to-end\\\" 质疑： answer 是 cost-performance tradeoff (2.4× memory, 6.5× speed) 和 cross-generator generalization。 End-to-end 的 LOGO gap (~10pp) 暗示 generator-specific overfitting， 而 7-feature 的 handcrafted nature 保证了 feature 的 generator-agnostic 语义。\\n\\n\\nQLoRA within-distribution 显著优于 7-feature (+12-16pp on binary)， 因为 end-to-end fine-tuning 学习了 handcrafted features 之外的 contextual/positional patterns： 句法结构退化、discourse coherence 下降、repetition 模式等 token-sequence level 信号。 但 QLoRA 的 cross-generator generalization (LOGO binary ~0.72) 远低于 within-distribution (0.826-0.852)，gap ~10pp：end-to-end model 部分 overfit 到 generator-specific token patterns 而非 depth-universal distributional shift。 5-class QLoRA (0.551) 仅比 handcrafted (0.503) 高 ~5pp， 确认 finer classification 的 bottleneck 是 task-inherent difficulty 而非 feature limitation。 7-feature ensemble 的优势在于：(a) 2.4× less GPU memory, (b) 6.5× faster inference, (c) interpretable (每个 feature 有 clear DDR 语义), (d) cross-generator 泛化更稳定 (within-LOGO variance 更小)。\\n\"\n  },\n  {\n    \"name\": \"text_length_control\",\n    \"description\": \"Text length confound 控制分析 (RC10)\",\n    \"results\": {\n      \"spearman_length_depth_range\": \"[-0.066, +0.134]\",\n      \"length_depth_correlation\": \"weak (|ρ|<0.14)\",\n      \"length_matched_binary_f1\": 0.724,\n      \"unmatched_binary_f1\": 0.77,\n      \"length_matched_delta_pp\": -4.6,\n      \"random_subsample_control_f1\": 0.741,\n      \"random_subsample_delta_pp\": -2.9,\n      \"deconfounding_attributable_pp\": -1.7,\n      \"normalized_ttr_trend_preserved\": true,\n      \"normalized_hapax_trend_preserved\": true,\n      \"normalized_rho_stronger\": true,\n      \"length_is_confound\": false,\n      \"dropout_short_text_bias\": true\n    },\n    \"tables\": [\n      \"Table S17: Length-matched vs unmatched vs random-subsample F1\",\n      \"Table S18: Length distribution statistics by depth (mean, median, IQR)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Length confound 被排除 (RC10 fully addressed)。 Paper 中报告 length-matched F1=0.724 作为 conservative estimate， 同时说明 4.6pp drop 主要来自 sample size reduction (2.9pp) 而非 deconfounding (1.7pp)。 Normalized features 的 stronger trend 是 positive evidence： 控制 length 后 depth signal 更纯净。\\n\\n\\nLength 非 primary confound。Length-depth Spearman ρ 在 [-0.066, +0.134] 范围， text length 不随 depth 系统性变化。Length-matched binary F1=0.724 (vs 0.770)， 下降 4.6pp，但 random subsample control (同等 sample size reduction) F1=0.741， 降 2.9pp。因此 4.6pp drop 中仅 ~1.7pp 可归因于 length deconfounding， 其余 2.9pp 来自 sample size reduction。 Length-normalized surface features (fixed-length windows 上的 TTR, hapax) 保留且加强了 trend (|ρ| 更高)，证明 drift 信号来自 vocabulary diversity 的 intrinsic decrease 而非 text 变长/变短。 Dropout short text bias: deeper text 因 generation quality degradation 而更短， 但这是 generation property (depth 的 consequence) 而非 external confound。\\n\"\n  },\n  {\n    \"name\": \"large_scale_generator\",\n    \"description\": \"添加 7B+ generator (Qwen3-8B-Base) 测试 scale effect\",\n    \"results\": {\n      \"total_records\": 4497,\n      \"unique_seeds\": 995,\n      \"depth_distribution\": {\n        \"gen0\": 995,\n        \"gen1\": 979,\n        \"gen2\": 937,\n        \"gen3\": 831,\n        \"gen4\": 755\n      },\n      \"qwen3_8b_logo_binary_f1\": 0.683,\n      \"qwen3_8b_logo_3class_f1\": 0.695,\n      \"qwen3_8b_ci\": [\n        0.66,\n        0.706\n      ],\n      \"logo_6gen_avg_f1\": 0.789,\n      \"logo_6gen_avg_binary_f1\": 0.7,\n      \"delta_8b_vs_smaller_avg_pp\": -1.7,\n      \"spearman_8b\": {\n        \"hapax_ratio\": -0.558,\n        \"ttr\": -0.542,\n        \"entropy_mean\": -0.475,\n        \"entropy_min\": -0.303,\n        \"entropy_max\": 0.095,\n        \"tail_decay\": -0.089,\n        \"entropy_std\": -0.076\n      },\n      \"ddr_pattern_preserved\": true,\n      \"scale_attenuation_drifting_rho\": \"~85% of <3B average\",\n      \"feature_importance_8b\": {\n        \"hapax_ratio\": 0.269,\n        \"entropy_mean\": 0.164,\n        \"ttr\": 0.159\n      }\n    },\n    \"tables\": [\n      \"Table 7: Per-generator LOGO F1 (6 generators, 包含 Qwen3-8B)\",\n      \"Table S19: Spearman ρ — 8B vs <3B average by feature\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Scale effect 诚实报告为 limitation 但 DDR 定性 robust。 0.683 仍远优于 chance (0.50)，depth signal 在 8B scale 仍有实用价值。 14B DDR analysis (exp_060) 进一步确认：drifting/stationary 分组在 14B 仍一致， |ρ| 进一步衰减 (hapax -0.507, ttr -0.492) 但分组不变。 核心假设 \\\"14B scale DDR 模式定性不变\\\" 成立。\\n\\n\\nQwen3-8B binary F1=0.683，在 scale_8b_logo_binary_f1 [0.65, 0.70] 范围内。 Scale effect 存在但 moderate：8B vs <3B average 降 ~1.7pp LOGO F1。 原因：larger models 的 generation distribution 更 concentrated (lower entropy, tighter vocabulary, less sampling randomness at same temperature)， 压缩了 depth-wise feature margin。Hapax ratio |ρ| 从 <3B 的 0.647 降至 8B 的 0.558 (attenuation ~86%)：8B model 的 baseline vocabulary diversity 较低， depth-wise 衰减的 absolute magnitude 更小。 DDR 模式定性不变：drifting 三特征仍为 |ρ| 最高 (hapax -0.558, ttr -0.542, entropy_mean -0.475)， stationary 特征仍 |ρ|<0.10 (tail_decay -0.089, entropy_max 0.095)。 Depth distribution 显示 deeper text 更多 dropout (d4 仅 755/995)， 比 smaller models 更显著：8B model 的 longer-context generation 更容易 degenerate at deeper depths。\\n\"\n  },\n  {\n    \"name\": \"ordinal_baseline_comparison\",\n    \"description\": \"现有 detector 连续分数的 ordinal depth signal — 7-feature 相对优势验证\",\n    \"results\": {\n      \"seven_feature_logo_f1\": 0.798,\n      \"seven_feature_ci\": [\n        0.786,\n        0.799\n      ],\n      \"avg_logprob_logo_f1\": 0.765,\n      \"avg_logprob_ci\": [\n        0.616,\n        0.82\n      ],\n      \"avg_logprob_spearman\": 0.788,\n      \"ld_score_logo_f1\": 0.721,\n      \"ld_score_ci\": [\n        0.588,\n        0.77\n      ],\n      \"ld_score_spearman\": 0.794,\n      \"fastdetectgpt_logo_f1\": 0.627,\n      \"fastdetectgpt_ci\": [\n        0.511,\n        0.762\n      ],\n      \"fastdetectgpt_spearman\": 0.433,\n      \"binoculars_logo_f1\": 0.579,\n      \"binoculars_ci\": [\n        0.405,\n        0.664\n      ],\n      \"binoculars_spearman\": 0.199,\n      \"bootstrap_7feat_vs_avglogprob\": {\n        \"delta_pp\": 3.3,\n        \"p\": 0.0,\n        \"significant\": true\n      },\n      \"bootstrap_7feat_vs_fdgpt\": {\n        \"delta_pp\": 6.7,\n        \"p\": 0.0,\n        \"significant\": true\n      },\n      \"best_single_detector\": \"avg_logprob (0.765)\",\n      \"seven_feat_minus_best_single_pp\": 3.3\n    },\n    \"tables\": [\n      \"Table 3: LOGO F1 — 7-feature vs 4 baseline detectors, with bootstrap CI and Spearman ρ\",\n      \"Table S20: Pairwise bootstrap significance tests (7-feature vs each detector)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"3.3pp 优势虽不巨大但 statistically significant (bootstrap p<0.01)， 符合 Findings paper 的 empirical contribution 标准。 关键 finding 不仅是 performance gap，而是 existing detectors 确实有 moderate ordinal signal (avg_logprob 0.765)，但 7-feature 通过 feature complementarity 显著提升。 这 reframes contribution：不是 \\\"novel features\\\" 而是 \\\"systematic characterization of DDR + principled feature combination\\\"， 符合 Findings 定位。 Binoculars 的 bug fix (denominator correction) 确保了 fair comparison。 Wide bootstrap CIs for single detectors (e.g. avg_logprob [0.616, 0.820]) 反映 high per-generator variance — 这本身是 7-feature 的优势 (其 CI [0.786, 0.799] 远窄)。\\n\\n7-feature 优势 3.3pp over best single detector (avg_logprob)， 在 [3.0, 5.0] 范围内，bootstrap p=0.0 确认显著性 (n=1000)。 Avg_logprob 是最强 single detector (F1=0.765) 因为它直接测量 NLL 均值， 正是 drifting features 捕捉的 primary signal — avg_logprob 本质上是 entropy_mean 的 unnormalized version。但 avg_logprob 缺少 shape features 和 surface features 的互补信号。 LD-Score (0.721) 第二强：character-level distribution shift 与 depth 有 moderate 相关 (ρ=0.794)，但 character-level 信息 partially redundant with word-level surface features。 FastDetectGPT (0.627) 较弱：perturbation-based approach 设计用于 binary real/synthetic detection， 其 log probability curvature metric 对 ordinal depth variation 不 sensitive。 Binoculars (0.579) 最弱：two-model probability ratio 中 depth signal 被 ratio 操作 部分 cancel (两个 model 的 NLL 均随 depth 下降，ratio 变化小)。 7-feature 优势的来源是 complementarity：drifting features 捕捉 location shift， stationary features 提供 noise-resistant baseline，surface features 捕捉 generator-agnostic vocabulary impoverishment。三组信号的 combination 优于任何 single metric。\\n\"\n  }\n]",
      "numLines": 660,
      "startLine": 1,
      "totalLines": 660
    }
  },
  "sourceToolAssistantUUID": "86cf0778-39e4-4efb-9b98-ff18e33fc48e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "7a6e7dae-2371-44f2-a86f-776f12713121",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T23:58:37.587Z_

<details><summary>↩ Tool result · `toolu_01NZSWTx6c8FWdzjhSEGcVHq`</summary>

```text
1	# Paper Framing — gen-depth-fingerprint
2	
3	## Target Venue
4	- **Primary: EMNLP 2026 Findings (ARR deadline: May 25, 2026)** — D012: 恢复为主投稿目标
5	- Positioning: **Findings paper**（非 main conference long paper）
6	- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)
7	
8	## Core Insight
9	Non-paraphrastic LLM generation chains exhibit **differential depth response** (DDR): **central-tendency/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth, while **shape features** (entropy_max, tail_decay) remain near-stationary. This is consistent with recursive generation inducing a **location shift** in the NLL distribution while approximately preserving distributional shape. The contribution is: (a) the **task formulation** (generation depth classification beyond binary detection), (b) **empirical validation** across 8 generators / 5 model families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B–8B) showing DDR is robust, (c) a lightweight 7-feature ensemble achieving leak-free binary F1 = 0.694 under 8-gen LOGO. Depth signal degrades substantially under instruction tuning, restricting current scope to base models.
10	
11	## Core Claims (3 条，均可证伪)
12	
13	**Claim 1 — Depth Discriminability**: A 7-feature distributional ensemble can classify generation depth (gen-0 / gen-1 / gen-2+) with leak-free binary F1 = 0.694 (95% CI [0.688, 0.700]) under 8-generator LOGO evaluation, generalizing across unseen generators and model families (LOFO binary F1 = 0.686). Cross-model chains yield binary F1 = 0.830 under generator-level LOGO (5-gen subset). Primary metric is leak-free binary F1 (gen-1 vs gen-2+), excluding gen-0 to avoid seed-sharing leakage.
14	
15	**Claim 2 — Differential Depth Response & Feature Complementarity**: Features exhibit DDR: drifting features show |ρ| > 0.60 (hapax −0.63, TTR −0.61, entropy_mean −0.60), while shape features show |ρ| < 0.10 (tail_decay 0.04). KS statistics confirm: drifting 0.516–0.537 vs shape 0.043–0.052 (~10× gap). Full 7-feature set (10-fold CV F1 = 0.773) outperforms surface-only (0.688) and reference-only (0.713; McNemar p ≈ 0). Reference-only yields higher binary F1 (0.833 vs 0.695) but surface features are essential for 3-class gen-0 discrimination.
16	
17	**Claim 3 — Downstream Utility (Negative Finding)**: Depth-aware data curation does NOT improve downstream CLM quality. At equal sample count (n=3,951): random subsampling (ppl=2.367) outperforms depth 0–1 (2.387) and binary-filtered (2.389). TOST confirms equivalence at ±2% margin (p = 1.1×10⁻⁴). Full dataset (n=12,299, ppl=2.335) vs depth-filtered requires ±3% margin for equivalence. Depth fingerprinting is a **diagnostic** tool for provenance characterization, not a **curative** tool for data selection.
18	
19	## Headline Metrics Summary
20	
21	| Metric | Value | Context |
22	|--------|-------|---------|
23	| **Primary: LOGO binary F1** | **0.694** [0.688, 0.700] | 8-gen LOGO, gen-1 vs gen-2+, leak-free |
24	| LOGO 3-class F1 | 0.762 [0.758, 0.766] | Inflated by gen-0 seed sharing |
25	| Cross-model binary F1 | 0.830 | 5-gen subset, generator-level LOGO |
26	| Cross-model 3-class F1 | 0.789 | 5-gen subset, generator-level LOGO |
27	| LOFO binary F1 | 0.686 | Leave-one-family-out |
28	| Per-gen binary F1 range | 0.633–0.724 | Mistral-7B lowest, Pythia-2.8B highest |
29	| 9-gen LOGO 3-class F1 | 0.751 | +Gemma-2-2B; Gemma gen-1 F1=0.036 anomaly |
30	| DDR causality | 6/7 Granger sig, 5.5× perm imp gap | Drifting dominance confirmed |
31	| Feature ablation (10-fold CV) | Full 0.773, Surface 0.688, Ref 0.713 | McNemar p ≈ 0 |
32	| Length-matched binary F1 | 0.724 vs 0.770 unmatched | Deconfounding, not sample-size effect |
33	
34	## Scope & Limitations (必须在论文中突出)
35	
36	1. **Base models only**: Instruct-tuned models show substantially degraded signal (OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base). Alignment-imposed length regulation and format constraints compress the distributional variation DDR exploits. This is the **primary scope limitation**.
37	2. **Temperature sensitivity**: Reliable within t ∈ [0.5, 0.9] (≤1 pp degradation from default t=0.7). At t = 1.0: −6 pp degradation; entropy_mean ρ drops from −0.60 to −0.002. Cross-temperature transfer degrades severely (t=0.7 → t=1.0: Qwen3-1.7B F1 drops 0.789 → 0.418).
38	3. **7-feature ensemble is not optimal**: Multi-detector ensembles (4-det + surface) achieve 3-class 0.795 vs 0.774 (+2.1 pp) and binary 0.708 vs 0.705 (+0.3 pp), but at 2.4× inference cost and 3.2× GPU memory. 7-feature positioned on **efficiency advantage**, not absolute performance.
39	4. **3-class resolution ceiling**: 5-class F1 drops to ~0.50; ordinal methods (CORAL, Frank-Hall) yield no improvement over standard XGBoost. Gen-1/gen-2+ boundary is the bottleneck (concentrates 86% of binary errors as FNs).
40	5. **Scale effect**: Larger generators show moderate degradation (Mistral-7B: 0.633, Qwen3-8B: 0.692 vs average 0.694). Higher-capacity models compress feature margins.
41	6. **Prompt-type dependence**: Continuation chains show stronger drift (F1 = 0.781) than elaboration (0.730).
42	
43	## Story Spine
44	
45	**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth (7–17% of recent scientific papers). Current detection methods offer only binary real-vs-synthetic classification, conflating qualitatively different material: gen-1 retains much of the source distribution's lexical properties, while deeper text exhibits measurably reduced vocabulary diversity and compressed perplexity.
46	
47	**Existing approaches & gaps**: Binary detectors (FastDetectGPT, Binoculars, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) bounds paraphrasing chains to ~3 classes but depends on semantic-preservation constraints. No existing method addresses generation depth estimation in non-paraphrastic continuation chains. When repurposed as ordinal depth predictors, single detector scores show moderate signal but high cross-generator variance.
48	
49	**Our framing**: We formulate generation depth classification (gen-0/gen-1/gen-2+) and characterize DDR across 8 base-model generators from 5 families (0.6B–8B). Central-tendency features drift monotonically while shape features remain near-stationary, consistent with recursive generation inducing a location shift in the NLL distribution. A 7-feature ensemble achieves leak-free binary F1 = 0.694 under 8-gen LOGO with a single 410M reference model. Multi-detector ensembles achieve marginally higher F1 at 2.4× cost. The signal degrades under instruction tuning and high temperature, restricting current scope to base models at moderate temperatures.
50	
51	**Headline result template**: "On 8 base-model generators from 5 families (0.6B–8B), our 7-feature ensemble achieves leak-free binary F1 = 0.694 under LOGO evaluation and 0.830 on cross-model chains, using a single 410M reference model. Depth-aware curation is statistically equivalent to random subsampling for downstream CLM quality (TOST p = 1.1×10⁻⁴ at ±2% margin), establishing depth fingerprinting as a diagnostic tool for provenance characterization."
52	
53	## Anticipated Reviewer Concerns
54	
55	**RC1 — "Is this just vocabulary impoverishment?"**: Surface features alone achieve 0.688, but full features achieve 0.773 (McNemar p ≈ 0). Reference features capture different, complementary signal. Reference-only yields higher binary F1 (0.833) but misses gen-0 discrimination. The complementarity itself is a finding.
56	
57	**RC2 — "Does this generalize beyond Pythia?"**: 8 generators from 5 families (Pythia, OLMo, Qwen, Llama, Mistral). LOFO binary F1 = 0.686 confirms cross-family transfer. Cross-model chains (heterogeneous generators per depth step) yield binary F1 = 0.764.
58	
59	**RC3 — "Is 3-class sufficient?"**: 5-class F1 drops to ~0.50. Ordinal methods (CORAL, Frank-Hall) yield no improvement. Gen-1/gen-2+ boundary is the resolution bottleneck. 3 classes represent practical ceiling.
60	
61	**RC4 — "How realistic are single-model chains?"**: Cross-model chains (different generator per step) are evaluated and yield higher F1 (0.764 binary), suggesting generator heterogeneity amplifies distributional shifts.
62	
63	**RC5 — "What about human editing?"**: Robustness test with simulated human edits (random word replacement + LLM-simulated editing). Reported in appendix.
64	
65	**RC6 — "Ecological validity?"**: Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, rewriting). Prompt-type dependence reported transparently (continuation 0.781 vs elaboration 0.730).
66	
67	**RC8 — "Aren't these just OOD detection features?"**: Contribution is NOT the features but: (a) ordinal depth estimation formulation, (b) empirical DDR discovery (drifting vs stationary), (c) Findings-level empirical characterization. Paper explicitly connects to OOD/perplexity-based detection literature.
68	
69	**RC9 — "Only base models — what about instruct?"**: Acknowledged as primary limitation. OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base. Instruction tuning compresses the distributional variation DDR exploits. Reported transparently; defines scope boundary.
70	
71	**RC10 — "Text length confound"**: Length-matched subsampling: binary F1 = 0.724 (vs 0.770 unmatched). Random-subsample control confirms drop reflects deconfounding, not sample-size reduction.
72	
73	**RC11 — "Downstream — limited evidence"**: Three seeds, single perplexity metric. TOST equivalence confirmed at ±2% margin for equal-count comparison. Margin sensitivity analysis across ±1%–5% reported. Cohen's d inflated by low seed-level variance; TOST is the appropriate test.
74	
75	## Contribution Positioning (Findings Level)
76	The contribution is **empirical and conceptual**, appropriate for Findings:
77	1. **Problem formulation**: Generation depth classification as a new task beyond binary detection (no prior work addresses this in non-paraphrastic chains)
78	2. **Empirical characterization**: DDR across 8 generators / 5 families (0.6B–8B), with cross-generator generalization (LOGO binary F1 = 0.694, LOFO 0.686, cross-model 0.764). Honest reporting of scope boundaries (instruct degradation, temperature sensitivity, scale effect).
79	3. **Negative finding**: Depth-aware curation ≡ random subsampling for downstream quality (TOST confirmed). Depth fingerprinting is diagnostic, not curative.
80	
81	**Framing discipline:**
82	- Do NOT call the drift/stationarity split a "discovery" — it follows from location-shift properties of the NLL distribution. Acknowledge explicitly.
83	- Do NOT use H1/H2 terminology. Use "drifting" vs "stationary" or "differential response."
84	- Do NOT overclaim "dual dynamics." Use "differential depth response" (DDR).
85	- Report **realistic performance range** (binary F1 0.633–0.724 per-generator, 0.694 LOGO average) in abstract/conclusion, not best-case.
86	- Primary metric is leak-free binary F1 (not 3-class, which is inflated by gen-0 seed sharing).
87	- 7-feature ensemble is positioned on efficiency, not absolute superiority over multi-detector ensembles.
88	
89	Related work must cover: perplexity-based detection (DetectGPT, GLTR, DNA-GPT, Binoculars), model collapse theory, OOD detection, data quality scoring, watermarking, vocabulary diversity, stylometry/authorship attribution, iterative generation (LLM as Broken Telephone ACL 2025), membership inference.
90	
91	## Venue Fit
92	- EMNLP 2026 Findings: Excellent fit — directly addresses data contamination, synthetic data feedback loops, data governance. Empirical/conceptual contribution with honest scope boundaries. Findings-appropriate ambition level: novel task formulation + solid characterization, not a state-of-the-art methodology claim.
93	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9220ce9-0c84-4382-9998-65927dc86b01",
  "isSidechain": false,
  "promptId": "1ca86b45-b190-47c7-9689-3b48717c505c",
  "type": "user",
  "uuid": "35340d44-9df9-40fa-a5fa-576845313c8c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T232427/best/paper_framing.md",
      "content": "# Paper Framing — gen-depth-fingerprint\n\n## Target Venue\n- **Primary: EMNLP 2026 Findings (ARR deadline: May 25, 2026)** — D012: 恢复为主投稿目标\n- Positioning: **Findings paper**（非 main conference long paper）\n- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)\n\n## Core Insight\nNon-paraphrastic LLM generation chains exhibit **differential depth response** (DDR): **central-tendency/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth, while **shape features** (entropy_max, tail_decay) remain near-stationary. This is consistent with recursive generation inducing a **location shift** in the NLL distribution while approximately preserving distributional shape. The contribution is: (a) the **task formulation** (generation depth classification beyond binary detection), (b) **empirical validation** across 8 generators / 5 model families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B–8B) showing DDR is robust, (c) a lightweight 7-feature ensemble achieving leak-free binary F1 = 0.694 under 8-gen LOGO. Depth signal degrades substantially under instruction tuning, restricting current scope to base models.\n\n## Core Claims (3 条，均可证伪)\n\n**Claim 1 — Depth Discriminability**: A 7-feature distributional ensemble can classify generation depth (gen-0 / gen-1 / gen-2+) with leak-free binary F1 = 0.694 (95% CI [0.688, 0.700]) under 8-generator LOGO evaluation, generalizing across unseen generators and model families (LOFO binary F1 = 0.686). Cross-model chains yield binary F1 = 0.830 under generator-level LOGO (5-gen subset). Primary metric is leak-free binary F1 (gen-1 vs gen-2+), excluding gen-0 to avoid seed-sharing leakage.\n\n**Claim 2 — Differential Depth Response & Feature Complementarity**: Features exhibit DDR: drifting features show |ρ| > 0.60 (hapax −0.63, TTR −0.61, entropy_mean −0.60), while shape features show |ρ| < 0.10 (tail_decay 0.04). KS statistics confirm: drifting 0.516–0.537 vs shape 0.043–0.052 (~10× gap). Full 7-feature set (10-fold CV F1 = 0.773) outperforms surface-only (0.688) and reference-only (0.713; McNemar p ≈ 0). Reference-only yields higher binary F1 (0.833 vs 0.695) but surface features are essential for 3-class gen-0 discrimination.\n\n**Claim 3 — Downstream Utility (Negative Finding)**: Depth-aware data curation does NOT improve downstream CLM quality. At equal sample count (n=3,951): random subsampling (ppl=2.367) outperforms depth 0–1 (2.387) and binary-filtered (2.389). TOST confirms equivalence at ±2% margin (p = 1.1×10⁻⁴). Full dataset (n=12,299, ppl=2.335) vs depth-filtered requires ±3% margin for equivalence. Depth fingerprinting is a **diagnostic** tool for provenance characterization, not a **curative** tool for data selection.\n\n## Headline Metrics Summary\n\n| Metric | Value | Context |\n|--------|-------|---------|\n| **Primary: LOGO binary F1** | **0.694** [0.688, 0.700] | 8-gen LOGO, gen-1 vs gen-2+, leak-free |\n| LOGO 3-class F1 | 0.762 [0.758, 0.766] | Inflated by gen-0 seed sharing |\n| Cross-model binary F1 | 0.830 | 5-gen subset, generator-level LOGO |\n| Cross-model 3-class F1 | 0.789 | 5-gen subset, generator-level LOGO |\n| LOFO binary F1 | 0.686 | Leave-one-family-out |\n| Per-gen binary F1 range | 0.633–0.724 | Mistral-7B lowest, Pythia-2.8B highest |\n| 9-gen LOGO 3-class F1 | 0.751 | +Gemma-2-2B; Gemma gen-1 F1=0.036 anomaly |\n| DDR causality | 6/7 Granger sig, 5.5× perm imp gap | Drifting dominance confirmed |\n| Feature ablation (10-fold CV) | Full 0.773, Surface 0.688, Ref 0.713 | McNemar p ≈ 0 |\n| Length-matched binary F1 | 0.724 vs 0.770 unmatched | Deconfounding, not sample-size effect |\n\n## Scope & Limitations (必须在论文中突出)\n\n1. **Base models only**: Instruct-tuned models show substantially degraded signal (OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base). Alignment-imposed length regulation and format constraints compress the distributional variation DDR exploits. This is the **primary scope limitation**.\n2. **Temperature sensitivity**: Reliable within t ∈ [0.5, 0.9] (≤1 pp degradation from default t=0.7). At t = 1.0: −6 pp degradation; entropy_mean ρ drops from −0.60 to −0.002. Cross-temperature transfer degrades severely (t=0.7 → t=1.0: Qwen3-1.7B F1 drops 0.789 → 0.418).\n3. **7-feature ensemble is not optimal**: Multi-detector ensembles (4-det + surface) achieve 3-class 0.795 vs 0.774 (+2.1 pp) and binary 0.708 vs 0.705 (+0.3 pp), but at 2.4× inference cost and 3.2× GPU memory. 7-feature positioned on **efficiency advantage**, not absolute performance.\n4. **3-class resolution ceiling**: 5-class F1 drops to ~0.50; ordinal methods (CORAL, Frank-Hall) yield no improvement over standard XGBoost. Gen-1/gen-2+ boundary is the bottleneck (concentrates 86% of binary errors as FNs).\n5. **Scale effect**: Larger generators show moderate degradation (Mistral-7B: 0.633, Qwen3-8B: 0.692 vs average 0.694). Higher-capacity models compress feature margins.\n6. **Prompt-type dependence**: Continuation chains show stronger drift (F1 = 0.781) than elaboration (0.730).\n\n## Story Spine\n\n**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth (7–17% of recent scientific papers). Current detection methods offer only binary real-vs-synthetic classification, conflating qualitatively different material: gen-1 retains much of the source distribution's lexical properties, while deeper text exhibits measurably reduced vocabulary diversity and compressed perplexity.\n\n**Existing approaches & gaps**: Binary detectors (FastDetectGPT, Binoculars, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) bounds paraphrasing chains to ~3 classes but depends on semantic-preservation constraints. No existing method addresses generation depth estimation in non-paraphrastic continuation chains. When repurposed as ordinal depth predictors, single detector scores show moderate signal but high cross-generator variance.\n\n**Our framing**: We formulate generation depth classification (gen-0/gen-1/gen-2+) and characterize DDR across 8 base-model generators from 5 families (0.6B–8B). Central-tendency features drift monotonically while shape features remain near-stationary, consistent with recursive generation inducing a location shift in the NLL distribution. A 7-feature ensemble achieves leak-free binary F1 = 0.694 under 8-gen LOGO with a single 410M reference model. Multi-detector ensembles achieve marginally higher F1 at 2.4× cost. The signal degrades under instruction tuning and high temperature, restricting current scope to base models at moderate temperatures.\n\n**Headline result template**: \"On 8 base-model generators from 5 families (0.6B–8B), our 7-feature ensemble achieves leak-free binary F1 = 0.694 under LOGO evaluation and 0.830 on cross-model chains, using a single 410M reference model. Depth-aware curation is statistically equivalent to random subsampling for downstream CLM quality (TOST p = 1.1×10⁻⁴ at ±2% margin), establishing depth fingerprinting as a diagnostic tool for provenance characterization.\"\n\n## Anticipated Reviewer Concerns\n\n**RC1 — \"Is this just vocabulary impoverishment?\"**: Surface features alone achieve 0.688, but full features achieve 0.773 (McNemar p ≈ 0). Reference features capture different, complementary signal. Reference-only yields higher binary F1 (0.833) but misses gen-0 discrimination. The complementarity itself is a finding.\n\n**RC2 — \"Does this generalize beyond Pythia?\"**: 8 generators from 5 families (Pythia, OLMo, Qwen, Llama, Mistral). LOFO binary F1 = 0.686 confirms cross-family transfer. Cross-model chains (heterogeneous generators per depth step) yield binary F1 = 0.764.\n\n**RC3 — \"Is 3-class sufficient?\"**: 5-class F1 drops to ~0.50. Ordinal methods (CORAL, Frank-Hall) yield no improvement. Gen-1/gen-2+ boundary is the resolution bottleneck. 3 classes represent practical ceiling.\n\n**RC4 — \"How realistic are single-model chains?\"**: Cross-model chains (different generator per step) are evaluated and yield higher F1 (0.764 binary), suggesting generator heterogeneity amplifies distributional shifts.\n\n**RC5 — \"What about human editing?\"**: Robustness test with simulated human edits (random word replacement + LLM-simulated editing). Reported in appendix.\n\n**RC6 — \"Ecological validity?\"**: Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, rewriting). Prompt-type dependence reported transparently (continuation 0.781 vs elaboration 0.730).\n\n**RC8 — \"Aren't these just OOD detection features?\"**: Contribution is NOT the features but: (a) ordinal depth estimation formulation, (b) empirical DDR discovery (drifting vs stationary), (c) Findings-level empirical characterization. Paper explicitly connects to OOD/perplexity-based detection literature.\n\n**RC9 — \"Only base models — what about instruct?\"**: Acknowledged as primary limitation. OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base. Instruction tuning compresses the distributional variation DDR exploits. Reported transparently; defines scope boundary.\n\n**RC10 — \"Text length confound\"**: Length-matched subsampling: binary F1 = 0.724 (vs 0.770 unmatched). Random-subsample control confirms drop reflects deconfounding, not sample-size reduction.\n\n**RC11 — \"Downstream — limited evidence\"**: Three seeds, single perplexity metric. TOST equivalence confirmed at ±2% margin for equal-count comparison. Margin sensitivity analysis across ±1%–5% reported. Cohen's d inflated by low seed-level variance; TOST is the appropriate test.\n\n## Contribution Positioning (Findings Level)\nThe contribution is **empirical and conceptual**, appropriate for Findings:\n1. **Problem formulation**: Generation depth classification as a new task beyond binary detection (no prior work addresses this in non-paraphrastic chains)\n2. **Empirical characterization**: DDR across 8 generators / 5 families (0.6B–8B), with cross-generator generalization (LOGO binary F1 = 0.694, LOFO 0.686, cross-model 0.764). Honest reporting of scope boundaries (instruct degradation, temperature sensitivity, scale effect).\n3. **Negative finding**: Depth-aware curation ≡ random subsampling for downstream quality (TOST confirmed). Depth fingerprinting is diagnostic, not curative.\n\n**Framing discipline:**\n- Do NOT call the drift/stationarity split a \"discovery\" — it follows from location-shift properties of the NLL distribution. Acknowledge explicitly.\n- Do NOT use H1/H2 terminology. Use \"drifting\" vs \"stationary\" or \"differential response.\"\n- Do NOT overclaim \"dual dynamics.\" Use \"differential depth response\" (DDR).\n- Report **realistic performance range** (binary F1 0.633–0.724 per-generator, 0.694 LOGO average) in abstract/conclusion, not best-case.\n- Primary metric is leak-free binary F1 (not 3-class, which is inflated by gen-0 seed sharing).\n- 7-feature ensemble is positioned on efficiency, not absolute superiority over multi-detector ensembles.\n\nRelated work must cover: perplexity-based detection (DetectGPT, GLTR, DNA-GPT, Binoculars), model collapse theory, OOD detection, data quality scoring, watermarking, vocabulary diversity, stylometry/authorship attribution, iterative generation (LLM as Broken Telephone ACL 2025), membership inference.\n\n## Venue Fit\n- EMNLP 2026 Findings: Excellent fit — directly addresses data contamination, synthetic data feedback loops, data governance. Empirical/conceptual contribution with honest scope boundaries. Findings-appropriate ambition level: novel task formulation + solid characterization, not a state-of-the-art methodology claim.\n",
      "numLines": 93,
      "startLine": 1,
      "totalLines": 93
    }
  },
  "sourceToolAssistantUUID": "d9220ce9-0c84-4382-9998-65927dc86b01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "7a6e7dae-2371-44f2-a86f-776f12713121",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T23:58:37.583Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NZSWTx6c8FWdzjhSEGcVHq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T232427/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c332b662-622b-4d10-8874-1ad4368d4515",
  "isSidechain": false,
  "requestId": "req_011CbEjByr2vv47iYhe1xwtQ",
  "type": "assistant",
  "uuid": "d9220ce9-0c84-4382-9998-65927dc86b01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "7a6e7dae-2371-44f2-a86f-776f12713121",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016vuYEEJ29u9fPEnY582MGR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13357,
      "cache_read_input_tokens": 11841,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13357,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 206,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13357,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13357
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T232427 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerpr…",
  "leafUuid": "35340d44-9df9-40fa-a5fa-576845313c8c",
  "sessionId": "7a6e7dae-2371-44f2-a86f-776f12713121"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete research paper from experimental data",
  "sessionId": "7a6e7dae-2371-44f2-a86f-776f12713121"
}
```

---

### Assistant

_source line 14 · 2026-05-20T23:59:08.924Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have both the experiment data and the paper framing. Let me also check if the output directory exists.

Let me now write the full LaTeX paper. I need to cover all 12 experiments from the JSON data:

1. feature_ablation_and_trend - Feature ablation + trend analysis
2. cross_generator_evaluation - 5-gen LOGO evaluation
3. cross_family_reference_model - Cross-reference-model DDR test
4. downstream_utility - Negative downstream finding
5. prompt_type_comparison - Continuation vs elaboration vs rewriting
6. paraphrastic_comparison - Paraphrastic vs non-paraphrastic


7. cross_model_chains - Cross-model chains
8. multi_domain_seeds - Multi-domain evaluation
9. finer_grained_ordinal - 5-class ordinal classification
10. human_edit_robustness - Human edit robustness
11. ld_score_feature - LD-Score feature analysis
12. end_to_end_classifier - QLoRA end-to-end classifier

I see there are actually 15 experiments listed in the data, including text_length_control, large_scale_generator, and ordinal_baseline_comparison. Let me organize these into the paper structure.

I'm planning the main body to cover the core contributions: the DDR framework and its evaluation across multiple generators, the analysis of drifting versus stationary features, baseline comparisons with existing detectors, and the downstream utility findings. The appendix will hold the more specialized experiments like feature ablations, prompt-type variations, and the robustness tests.

Now I'm setting up the LaTeX template and compiling the key results—the LOGO and LOFO F1 scores across different evaluation settings, the cross-model performance at 0.830, and the feature ablation breakdown showing how much the reference-based features contribute compared to surface-level ones. I'm noticing some discrepancies between the paper framing and the experiment data—the JSON shows 5-generator results while the framing references 8-generator numbers, so I'll rely on the JSON for specific experiments and use the framing's headline figures where they align. Now I need to structure the paper carefully, making sure I only use numbers that actually exist in the data, cover all 15 experiments, and organize the results so the most important findings are in the main body with supporting details in appendices. I'll keep the writing compilable with pdflatex and follow the framing's guidance on emphasis. Finishing out the appendix sections with the remaining experiments, then I'm ready to write the full paper using a two-column ACL-style format.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35340d44-9df9-40fa-a5fa-576845313c8c",
  "isSidechain": false,
  "requestId": "req_011CbEjCH7rTPsF8CaPkPZhp",
  "type": "assistant",
  "uuid": "395c135b-ff75-447c-a73e-72734403acad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "7a6e7dae-2371-44f2-a86f-776f12713121",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CX332JLDdScoBZQQ4qChx1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19925,
      "cache_read_input_tokens": 25198,
      "output_tokens": 1728,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19925,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1728,
          "cache_read_input_tokens": 25198,
          "cache_creation_input_tokens": 19925,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19925
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

_source line 15 · 2026-05-20T23:59:08.930Z_

Now let me ensure the output directory exists, then write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "395c135b-ff75-447c-a73e-72734403acad",
  "isSidechain": false,
  "requestId": "req_011CbEjCH7rTPsF8CaPkPZhp",
  "type": "assistant",
  "uuid": "5ccb4213-e635-4a00-81ff-0d65849a9441",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "7a6e7dae-2371-44f2-a86f-776f12713121",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CX332JLDdScoBZQQ4qChx1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19925,
      "cache_read_input_tokens": 25198,
      "output_tokens": 1728,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19925,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1728,
          "cache_read_input_tokens": 25198,
          "cache_creation_input_tokens": 19925,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19925
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

_source line 16 · 2026-05-20T23:59:10.638Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01655t13sxHkA6KjdhzShoHN`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T232427/best/",
  "description": "List target directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ccb4213-e635-4a00-81ff-0d65849a9441",
  "isSidechain": false,
  "requestId": "req_011CbEjCH7rTPsF8CaPkPZhp",
  "type": "assistant",
  "uuid": "c2812036-ebf5-4431-b822-88db62cc8c7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "7a6e7dae-2371-44f2-a86f-776f12713121",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CX332JLDdScoBZQQ4qChx1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19925,
      "cache_read_input_tokens": 25198,
      "output_tokens": 1728,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19925,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1728,
          "cache_read_input_tokens": 25198,
          "cache_creation_input_tokens": 19925,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19925
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

_source line 17 · 2026-05-20T23:59:10.764Z_

<details><summary>↩ Tool result · `toolu_01655t13sxHkA6KjdhzShoHN`</summary>

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
  "parentUuid": "c2812036-ebf5-4431-b822-88db62cc8c7e",
  "isSidechain": false,
  "promptId": "1ca86b45-b190-47c7-9689-3b48717c505c",
  "type": "user",
  "uuid": "b8df179e-d4a1-48d2-be8e-98406176ce5a",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "c2812036-ebf5-4431-b822-88db62cc8c7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "7a6e7dae-2371-44f2-a86f-776f12713121",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T00:03:04.470Z_

<details open><summary>🔧 Tool call — Write · `toolu_01LWzHzh28BPPiQq49Cos8Mj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T232427/best/paper.tex",
  "content": "\\documentclass[11pt,twocolumn]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{geometry}\n\\geometry{a4paper, margin=2.5cm}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\\usepackage{array}\n\\usepackage{enumitem}\n\n\\setlength{\\columnsep}{0.6cm}\n\n\\title{Differential Depth Response in Iterative LLM Generation:\\\\\nA Distributional Fingerprint for Provenance Characterization}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%=============================================================================\n% ABSTRACT\n%=============================================================================\n\\begin{abstract}\nWeb-scraped training corpora increasingly contain LLM-generated text of unknown provenance depth.\nCurrent detectors offer only binary real-vs-synthetic classification, conflating qualitatively different material:\nfirst-generation text retains much of the source lexical distribution, while deeper recursive outputs exhibit measurably reduced vocabulary diversity and compressed perplexity.\nWe formulate \\textbf{generation depth classification} (gen-0/gen-1/gen-2+) and characterize \\textbf{differential depth response} (DDR) across 8 base-model generators from 5 families (0.6B--8B):\ncentral-tendency features (entropy mean, TTR, hapax ratio) drift monotonically with depth ($|\\rho| \\geq 0.55$), while shape features (tail decay, entropy max) remain near-stationary ($|\\rho| < 0.10$).\nA lightweight 7-feature ensemble achieves leak-free binary F1 = 0.694 under 8-generator leave-one-generator-out (LOGO) evaluation (95\\% CI [0.688, 0.700]), and 0.830 on cross-model chains.\nCross-family generalization is confirmed via leave-one-family-out evaluation (binary F1 = 0.686).\nDDR is robust across 3 reference models from different families; shape-feature stationarity holds with $|\\rho| < 0.06$.\nDepth-aware data curation is statistically equivalent to random subsampling for downstream causal language modeling quality (TOST $p = 1.1 \\times 10^{-4}$ at $\\pm 2\\%$ margin), establishing depth fingerprinting as a \\textbf{diagnostic} tool for provenance characterization rather than a curative tool for data selection.\nCurrent scope is restricted to base models at moderate temperatures ($t \\leq 0.9$).\n\\end{abstract}\n\n%=============================================================================\n% 1. INTRODUCTION\n%=============================================================================\n\\section{Introduction}\n\nLarge language models (LLMs) are generating an increasing fraction of web content.\nRecent estimates suggest 7--17\\% of scientific papers and significant portions of web-scraped corpora contain LLM-generated text \\citep{liang2024monitoring}.\nThis poses challenges for training data curation: recursive consumption of synthetic data can degrade model quality through distributional collapse \\citep{shumailov2024model}.\n\nCurrent AI text detection methods operate as binary classifiers --- real vs.\\ synthetic --- and cannot distinguish \\emph{how many generations removed} a text is from its human-authored seed.\nThis distinction matters: first-generation (gen-1) text retains much of the source distribution's lexical properties, while deeper recursive outputs exhibit measurably reduced vocabulary diversity and compressed perplexity distributions.\nConflating these qualitatively different materials limits our ability to understand and mitigate model collapse risks.\n\nWe address this gap by formulating \\textbf{generation depth classification}: given a text, predict whether it is human-authored (gen-0), first-generation LLM output (gen-1), or deeper recursive output (gen-2+).\nOur investigation reveals \\textbf{differential depth response} (DDR): features derived from the next-token log-likelihood (NLL) distribution exhibit a systematic split.\n\\emph{Central-tendency features} (entropy mean, type-token ratio, hapax ratio) drift monotonically with generation depth, consistent with recursive compression of the token distribution.\n\\emph{Shape features} (tail decay rate, entropy max) remain near-stationary, indicating that recursive generation induces a \\emph{location shift} in the NLL distribution while approximately preserving distributional shape.\n\nWe validate DDR across 8 base-model generators from 5 architectural families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B--8B parameters) and 3 reference models.\nA 7-feature ensemble achieves leak-free binary F1 = 0.694 under LOGO evaluation, outperforming repurposed binary detectors (avg-logprob 0.765, FastDetectGPT 0.627, Binoculars 0.579 on macro F1).\nCross-model chains --- where each generation step uses a different generator --- yield binary F1 = 0.830, suggesting generator heterogeneity \\emph{amplifies} rather than obscures depth signal.\n\nOur third contribution is a calibrated negative finding: depth-aware data curation does not improve downstream language modeling quality compared to random subsampling (TOST equivalence confirmed at $\\pm 2\\%$ margin).\nThis positions depth fingerprinting as a \\textbf{diagnostic tool} for data provenance characterization, not a curative tool for data selection.\n\nWe report scope limitations transparently: the signal degrades substantially under instruction tuning (LOGO F1 = 0.338 vs.\\ 0.763 for base models), restricting current applicability to base models at moderate sampling temperatures.\n\n%=============================================================================\n% 2. RELATED WORK\n%=============================================================================\n\\section{Related Work}\n\n\\paragraph{AI text detection.}\nPerplexity-based methods leverage distributional differences between human and machine text.\nGLTR \\citep{gehrmann2019gltr} visualizes token-level log probabilities;\nDetectGPT \\citep{mitchell2023detectgpt} and its faster variant Fast-DetectGPT \\citep{bao2024fast} use perturbation-based log probability curvature;\nBinoculars \\citep{hans2024spotting} computes cross-entropy ratios between two models;\nDNA-GPT \\citep{yang2024dna} uses divergent n-gram analysis.\nAll operate as binary classifiers and cannot estimate generation depth.\n\n\\paragraph{Model collapse \\& iterative generation.}\n\\citet{shumailov2024model} formalize model collapse under iterative training on synthetic data, showing distributional tails vanish over generations.\n\\citet{dohmatob2024tale} provide theoretical bounds on variance collapse.\nLLM as Broken Telephone \\citep{briakou2025llm} studies paraphrastic attractor cycles, showing convergence within $\\sim$3 iterations.\nOur work addresses the complementary non-paraphrastic setting where unconstrained generation permits unbounded distributional drift.\n\n\\paragraph{Data quality \\& provenance.}\nVocabulary diversity metrics (TTR, hapax ratio) are established in corpus linguistics \\citep{mccarthy2010mtld}.\nLD-Score \\citep{tulchinskii2024intrinsic} uses character-level distribution divergence as a detection signal.\nPerplexity-based data filtering \\citep{wenzek2020ccnet} is standard in corpus construction.\nOur work extends these to ordinal depth estimation.\n\n\\paragraph{Stylometry \\& authorship.}\nAuthorship attribution methods \\citep{neal2017surveying} use distributional features for author identification.\nOur feature set draws on this tradition but targets generation depth rather than individual authorship.\n\n%=============================================================================\n% 3. METHOD\n%=============================================================================\n\\section{Method}\n\n\\subsection{Task Formulation}\n\nGiven a text passage $x$, we predict its \\emph{generation depth} $d \\in \\{0, 1, 2+\\}$:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{gen-0}: Human-authored seed text.\n    \\item \\textbf{gen-1}: First-generation LLM output from a human seed.\n    \\item \\textbf{gen-2+}: Output of $\\geq$2 recursive generation steps.\n\\end{itemize}\n\nThe \\textbf{primary metric} is leak-free binary F1 (gen-1 vs.\\ gen-2+), excluding gen-0 to avoid seed-sharing leakage.\nThree-class macro F1 is reported but noted as inflated by gen-0's strong discriminability.\n\n\\subsection{Generation Chain Construction}\n\nFor each human-authored seed $s$, we construct a chain $\\{x_0 = s, x_1, x_2, x_3, x_4\\}$ where $x_{d+1} = \\text{LLM}(x_d)$ using continuation prompting at temperature $t = 0.7$.\nChains are constructed independently per generator.\nCross-model chains use a different generator at each depth step.\n\n\\subsection{Feature Extraction}\n\\label{sec:features}\n\nWe extract 7 features per passage using a reference model $M_{\\text{ref}}$ (Pythia-410M by default):\n\n\\paragraph{Surface features} (computed from raw text):\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{TTR}: Type-token ratio (unique tokens / total tokens).\n    \\item \\textbf{Hapax ratio}: Fraction of tokens appearing exactly once.\n\\end{itemize}\n\n\\paragraph{Reference features} (computed from $M_{\\text{ref}}$'s NLL distribution over $x$):\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{Entropy mean}: Mean per-token NLL.\n    \\item \\textbf{Entropy std}: Standard deviation of per-token NLL.\n    \\item \\textbf{Entropy min/max}: Extremal NLL values.\n    \\item \\textbf{Tail decay}: Decay rate of the upper tail of the NLL distribution, estimated via exponential fit.\n\\end{itemize}\n\n\\subsection{Differential Depth Response (DDR)}\n\nDDR characterizes feature behavior as a function of generation depth via Spearman rank correlation $\\rho$ between feature value and depth $d$:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{Drifting features} ($|\\rho| \\geq 0.55$): hapax ratio, TTR, entropy mean. These exhibit monotonic trends with depth, consistent with recursive compression.\n    \\item \\textbf{Stationary features} ($|\\rho| < 0.10$): tail decay, entropy max. These remain near-constant, indicating the NLL distribution's shape is preserved under location shift.\n    \\item \\textbf{Weakly drifting}: entropy std ($|\\rho| \\approx 0.20$), intermediate between the two groups.\n\\end{itemize}\n\n\\subsection{Evaluation Protocol}\n\nWe use two leave-out evaluation protocols to prevent information leakage:\n\n\\paragraph{LOGO} (Leave-One-Generator-Out): Train on $K{-}1$ generators, test on the held-out generator. Measures cross-generator generalization.\n\n\\paragraph{LOFO} (Leave-One-Family-Out): Train on all generators except those from one architectural family (e.g., hold out all Pythia models). Measures cross-family transfer.\n\nThe classifier is XGBoost with default hyperparameters, evaluated via 5-fold cross-validation within each training split.\n\n%=============================================================================\n% 4. EXPERIMENTS\n%=============================================================================\n\\section{Experiments}\n\n\\subsection{Setup}\n\n\\paragraph{Generators.} We evaluate 8 base-model generators spanning 5 families: Pythia-1B, Pythia-2.8B (EleutherAI); OLMo-2-1B (AI2); Qwen3-0.6B, Qwen3-1.7B, Qwen3-8B (Alibaba); Llama-3.2-3B (Meta); Mistral-7B (Mistral AI).\nAll generation uses continuation prompting at $t = 0.7$.\n\n\\paragraph{Seeds.} Wikipedia passages serve as the primary seed domain ($\\sim$1000 seeds per generator), with additional evaluation on news, academic, and code domains (\\S\\ref{sec:multidomain}).\n\n\\paragraph{Reference model.} Pythia-410M (default). Cross-reference robustness evaluated with OLMo-2-1B and Qwen3-0.6B (\\S\\ref{sec:crossref}).\n\n\\subsection{Feature Ablation \\& Trend Analysis}\n\\label{sec:ablation}\n\nTable~\\ref{tab:ablation} reports 5-fold CV results on the full dataset, ablating feature groups.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Feature Set} & \\textbf{Macro F1} \\\\\n\\midrule\nFull (7 features) & 0.820 \\\\\nSurface only (TTR, hapax) & 0.763 \\\\\nReference only (5 features) & 0.719 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Feature ablation (5-fold CV). Full set significantly outperforms both subsets (McNemar $p < 0.001$), confirming surface--reference complementarity.}\n\\label{tab:ablation}\n\\end{table}\n\nSurface and reference features are complementary: the full set outperforms surface-only by 5.7 pp and reference-only by 10.1 pp (McNemar $p < 0.001$ for both).\nThis establishes that depth signal arises from two distinct sources: vocabulary diversity reduction (surface) and NLL distribution shift (reference).\n\n\\paragraph{DDR trend analysis.}\nLinear regression of features against depth confirms the drifting/stationary split (Table~\\ref{tab:trends}).\nDrifting features show high $R^2$: entropy mean (0.93), hapax ratio (0.92), TTR (0.89).\nStationary features show near-zero $R^2$: tail decay (0.03).\nEntropy std occupies an intermediate position ($R^2 = 0.41$, slope $= -0.12$), with drift magnitude $\\sim$1/3 of the drifting group.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Feature} & \\textbf{Slope} & $R^2$ & \\textbf{Category} \\\\\n\\midrule\nEntropy mean & $-0.29$ & 0.93 & Drifting \\\\\nHapax ratio & $-0.043$ & 0.92 & Drifting \\\\\nTTR & $-0.034$ & 0.89 & Drifting \\\\\nEntropy std & $-0.12$ & 0.41 & Weak \\\\\nTail decay & $+0.002$ & 0.03 & Stationary \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-feature linear trend across depths 0--4. Drifting features exhibit strong monotonic decrease ($R^2 > 0.89$); tail decay is effectively flat.}\n\\label{tab:trends}\n\\end{table}\n\nPerplexity under the reference model decreases monotonically with depth (median: 13.5, 4.96, 3.00, 2.07, 1.72 for depths 0--4), confirming that recursive generation compresses the NLL distribution leftward.\n\n\\subsection{Cross-Generator Generalization}\n\\label{sec:crossgen}\n\nTable~\\ref{tab:crossgen} reports per-generator LOGO results on the 5-generator subset (Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B; $N = 23{,}032$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Generator} & \\textbf{Macro F1} & \\textbf{Binary F1} \\\\\n\\midrule\nPythia-1B & 0.851 & 0.724 \\\\\nPythia-2.8B & 0.804 & 0.720 \\\\\nQwen3-0.6B & 0.818 & 0.715 \\\\\nQwen3-1.7B & 0.805 & 0.710 \\\\\nOLMo-2-1B & 0.752 & 0.670 \\\\\n\\midrule\n\\textbf{Average} & \\textbf{0.804} & \\textbf{0.720} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-generator LOGO evaluation (5-gen subset). Binary F1 variance across generators is 5.4 pp, confirming cross-generator robustness.}\n\\label{tab:crossgen}\n\\end{table}\n\nThe LOGO binary F1 of 0.720 (95\\% CI [0.708, 0.732]) demonstrates cross-generator generalization.\nPer-generator variance is 5.4 pp, with OLMo-2-1B lowest (0.670) due to its non-GPT-NeoX architecture producing more divergent distributional patterns.\nHapax ratio is the most important feature (importance = 0.289), followed by TTR (0.168) and entropy mean (0.160).\n\n\\paragraph{Cross-family transfer.}\nLOFO evaluation confirms generalization beyond same-family models: Pythia held-out F1 = 0.690, OLMo held-out = 0.720, Qwen held-out = 0.706 (average LOFO binary F1 = 0.705).\nThe 1.5 pp drop from LOGO to LOFO indicates minimal family-specific inflation.\n\n\\subsection{Cross-Reference-Model Robustness}\n\\label{sec:crossref}\n\nTo verify that DDR is not an artifact of the Pythia-410M reference model, we extract features using two additional reference models: OLMo-2-1B and Qwen3-0.6B (Table~\\ref{tab:crossref}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Reference} & \\textbf{Macro F1} & \\multicolumn{2}{c}{\\textbf{Spearman $\\rho$}} \\\\\n\\cmidrule(lr){3-4}\n & & hapax & tail decay \\\\\n\\midrule\nPythia-410M & 0.803 & $-0.647$ & $-0.040$ \\\\\nOLMo-2-1B & 0.807 & $-0.647$ & $-0.038$ \\\\\nQwen3-0.6B & 0.816 & $-0.647$ & $-0.042$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{LOGO macro F1 and representative Spearman $\\rho$ by reference model. DDR pattern (drifting vs.\\ stationary split) is consistent across all three reference families. Surface features are identical by construction.}\n\\label{tab:crossref}\n\\end{table}\n\nClassification F1 varies by only 1.3 pp across reference models.\nEntropy mean drift direction is consistently negative across all three reference families (Pythia: $[-1.19, -1.40]$; OLMo: $[-0.61, -0.91]$; Qwen: $[-0.96, -1.35]$).\nShape-feature stationarity holds robustly: maximum $|\\rho|$ across all reference models is 0.055.\nDDR is a property of the generation process, not an artifact of reference model choice.\n\n\\subsection{Baseline Comparison}\n\\label{sec:baseline}\n\nWe compare our 7-feature ensemble against four existing detectors repurposed as ordinal depth predictors (Table~\\ref{tab:baseline}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & \\textbf{LOGO F1} & \\textbf{Spearman $\\rho$} \\\\\n\\midrule\n7-feature ensemble & \\textbf{0.798} & --- \\\\\nAvg log-prob & 0.765 & 0.788 \\\\\nLD-Score & 0.721 & 0.794 \\\\\nFast-DetectGPT & 0.627 & 0.433 \\\\\nBinoculars & 0.579 & 0.199 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{LOGO macro F1 for ordinal depth classification. 7-feature ensemble significantly outperforms all baselines (bootstrap $p < 0.01$). CI for avg-logprob is wide: [0.616, 0.820], reflecting high cross-generator variance.}\n\\label{tab:baseline}\n\\end{table}\n\nThe 7-feature ensemble achieves 0.798, significantly outperforming the best single detector (avg-logprob 0.765; bootstrap $\\Delta = 3.3$ pp, $p < 0.01$).\nAvg-logprob is strongest among single detectors because it directly measures NLL mean --- essentially an unnormalized entropy mean.\nHowever, its narrow 95\\% CI [0.616, 0.820] reveals high per-generator variance, whereas the 7-feature ensemble achieves a much tighter CI [0.786, 0.799].\n\nBinoculars performs worst (0.579): its two-model probability ratio partially cancels depth signal, as both models' NLL decreases with depth.\nFast-DetectGPT (0.627) was designed for binary detection; its perturbation-based curvature metric is insensitive to ordinal depth variation.\n\n\\subsection{Cross-Model Chains}\n\\label{sec:crossmodel}\n\nReal-world contamination involves diverse generators. We evaluate on cross-model chains where each depth step uses a different generator (Table~\\ref{tab:crossmodel}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Setting} & \\textbf{Binary F1} & \\textbf{3-class F1} \\\\\n\\midrule\nSingle-model (LOGO) & 0.694 & --- \\\\\nCross-model (LOGO) & \\textbf{0.830} & 0.789 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model chains (5-gen, generator-level LOGO) vs.\\ single-model LOGO. Generator heterogeneity \\emph{amplifies} depth signal ($+$13.6 pp binary F1).}\n\\label{tab:crossmodel}\n\\end{table}\n\nCross-model binary F1 = 0.830 (95\\% CI [0.812, 0.848]) exceeds single-model LOGO by 13.6 pp.\nPer-generator variance drops to 4.0 pp (vs.\\ 5.4 pp for single-model), indicating more stable signal under heterogeneity.\nDDR drifting-feature correlations strengthen in cross-model chains (hapax $\\rho = -0.72$ vs.\\ $-0.647$ single-model): each generator change injects fresh distributional perturbation, preventing convergence to a model-specific attractor state.\nThis is a positive ecological validity result: realistic multi-generator contamination is \\emph{easier}, not harder, to detect.\n\n\\subsection{Downstream Utility (Negative Finding)}\n\\label{sec:downstream}\n\nWe test whether depth-aware data curation improves downstream language model quality by fine-tuning OLMo-2-1B (1.485B parameters) on depth-stratified subsets (Table~\\ref{tab:downstream}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrcc}\n\\toprule\n\\textbf{Variant} & $n$ & \\textbf{PPL} & \\textbf{$\\pm$ std} \\\\\n\\midrule\nAll data & 12,299 & 2.335 & 0.0003 \\\\\nSize-matched (random) & 3,951 & 2.367 & 0.0002 \\\\\nDepth 0--1 only & 3,951 & 2.387 & 0.001 \\\\\nBinary-filtered & 3,951 & 2.389 & 0.001 \\\\\nDepth-0 only & 797 & 2.681 & 0.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Downstream CLM perplexity (3 seeds). Depth-aware curation (depth 0--1, binary-filtered) does not outperform random subsampling at equal sample count.}\n\\label{tab:downstream}\n\\end{table}\n\nThe ranking is: all data (2.335) $<$ size-matched random (2.367) $<$ depth 0--1 (2.387) $\\approx$ binary-filtered (2.389) $\\ll$ depth-0 only (2.681).\nTOST equivalence tests at $\\pm 2\\%$ margin confirm that depth-aware curation and random subsampling produce equivalent downstream quality ($p = 1.1 \\times 10^{-4}$ for size-matched vs.\\ depth 0--1; $p = 9 \\times 10^{-5}$ for size-matched vs.\\ binary-filtered).\nAt the stricter $\\pm 1\\%$ margin, equivalence is not confirmed ($p = 0.08$).\n\nDepth filtering removes deeper text but also removes diverse training signal; random subsampling preserves more complete distributional coverage.\nSeed variance is minimal ($< 0.002$ across seeds), confirming the stability of this negative finding.\nThis establishes depth fingerprinting as a \\textbf{diagnostic} tool --- useful for characterizing data provenance --- rather than a curative tool for improving training data quality.\n\n%=============================================================================\n% 5. DISCUSSION\n%=============================================================================\n\\section{Discussion}\n\n\\paragraph{DDR as location shift.}\nThe drifting/stationary split is consistent with recursive generation inducing a location shift in the NLL distribution: central-tendency features (mean, diversity) drift while shape features (tail decay, entropy max) are preserved.\nThis is not a ``discovery'' in the strong sense --- it follows from properties of the NLL distribution under recursive compression --- but its empirical robustness across 8 generators, 5 families, and 3 reference models is the contribution.\n\n\\paragraph{Entropy std as intermediate case.}\nEntropy std shows weak drift ($|\\rho| \\approx 0.20$, $R^2 = 0.41$), with magnitude $\\sim$1/3 of the drifting group.\nWe classify it as ``weakly drifting'' without disrupting the core binary distinction.\nIts feature importance is low (rank 5/7 in the 5-gen evaluation).\n\n\\paragraph{Limitations.}\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{Base models only.} Instruction tuning compresses the distributional variation DDR exploits (LOGO F1 = 0.338 for OLMo-Instruct vs.\\ 0.763 base). This is the primary scope limitation.\n\\item \\textbf{Temperature sensitivity.} Reliable within $t \\in [0.5, 0.9]$. At $t = 1.0$, entropy mean $\\rho$ drops to $-0.002$.\n\\item \\textbf{Scale effect.} Larger generators show moderate degradation (Qwen3-8B binary F1 = 0.683; $\\sim$85\\% of drifting $|\\rho|$ vs.\\ $<$3B average). DDR pattern is qualitatively preserved (\\S\\ref{sec:scale}).\n\\item \\textbf{3-class resolution ceiling.} 5-class F1 drops to $\\sim$0.50; ordinal methods offer no improvement (\\S\\ref{sec:ordinal}).\n\\item \\textbf{Prompt-type dependence.} Continuation chains (F1 = 0.781) outperform elaboration (0.730) by 5.1 pp (\\S\\ref{sec:prompttype}).\n\\item \\textbf{Downstream evidence.} Limited to single-task (CLM) and single-metric (perplexity) evaluation with 3 seeds.\n\\end{enumerate}\n\n%=============================================================================\n% 6. CONCLUSION\n%=============================================================================\n\\section{Conclusion}\n\nWe formulate generation depth classification and characterize differential depth response (DDR) across 8 base-model generators from 5 families.\nA 7-feature distributional ensemble achieves leak-free binary F1 = 0.694 (per-generator range: 0.633--0.724) under LOGO evaluation, with cross-model chains reaching 0.830.\nDDR is robust across reference models and generator families but degrades under instruction tuning, defining a clear scope boundary.\nDepth-aware curation is statistically equivalent to random subsampling for downstream quality, positioning depth fingerprinting as a diagnostic rather than curative tool.\nFuture work should address instruction-tuned models, larger scales ($>$14B), and downstream tasks beyond causal language modeling.\n\n%=============================================================================\n% REFERENCES\n%=============================================================================\n{\\small\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{20}\n\n\\bibitem[Bao et~al.(2024)]{bao2024fast}\nBao, G., Zhao, Y., Teng, Z., Yang, L., and Zhang, Y.\n\\newblock Fast-DetectGPT: Efficient zero-shot detection of machine-generated text via conditional probability curvature.\n\\newblock In \\emph{Proc.\\ ICLR}, 2024.\n\n\\bibitem[Briakou et~al.(2025)]{briakou2025llm}\nBriakou, E., et~al.\n\\newblock LLM as a broken telephone: Iterative paraphrasing converges to attractor cycles.\n\\newblock In \\emph{Proc.\\ ACL}, 2025.\n\n\\bibitem[Dohmatob et~al.(2024)]{dohmatob2024tale}\nDohmatob, E., Feng, Y., and Gu, Q.\n\\newblock A tale of tails: Model collapse as a change of scaling laws.\n\\newblock In \\emph{Proc.\\ ICML}, 2024.\n\n\\bibitem[Gehrmann et~al.(2019)]{gehrmann2019gltr}\nGehrmann, S., Strobelt, H., and Rush, A.~M.\n\\newblock GLTR: Statistical detection and visualization of generated text.\n\\newblock In \\emph{Proc.\\ ACL Demo}, 2019.\n\n\\bibitem[Hans et~al.(2024)]{hans2024spotting}\nHans, A., Schwarzschild, A., Cheber, V., Alon, U., Lyu, Z., and Goldstein, T.\n\\newblock Spotting LLMs with Binoculars: Zero-shot detection of machine-generated text.\n\\newblock In \\emph{Proc.\\ ICML}, 2024.\n\n\\bibitem[Liang et~al.(2024)]{liang2024monitoring}\nLiang, W., et~al.\n\\newblock Monitoring AI-modified content at scale: A case study on the impact of ChatGPT on AI conference peer reviews.\n\\newblock \\emph{arXiv:2403.07183}, 2024.\n\n\\bibitem[McCarthy and Jarvis(2010)]{mccarthy2010mtld}\nMcCarthy, P.~M. and Jarvis, S.\n\\newblock MTLD, vocd-D, and HD-D: A validation study of sophisticated approaches to lexical diversity assessment.\n\\newblock \\emph{Behavior Research Methods}, 42(2):381--392, 2010.\n\n\\bibitem[Mitchell et~al.(2023)]{mitchell2023detectgpt}\nMitchell, E., Lee, Y., Khazatsky, A., Manning, C.~D., and Finn, C.\n\\newblock DetectGPT: Zero-shot machine-generated text detection using probability curvature.\n\\newblock In \\emph{Proc.\\ ICML}, 2023.\n\n\\bibitem[Neal and Woodard(2017)]{neal2017surveying}\nNeal, T. and Woodard, D.\n\\newblock Surveying stylometry techniques and applications.\n\\newblock \\emph{ACM Computing Surveys}, 50(6):1--36, 2017.\n\n\\bibitem[Shumailov et~al.(2024)]{shumailov2024model}\nShumailov, I., Shumaylov, Z., Zhao, Y., Gal, Y., Papernot, N., and Anderson, R.\n\\newblock AI models collapse when trained on recursively generated data.\n\\newblock \\emph{Nature}, 631:755--759, 2024.\n\n\\bibitem[Tulchinskii et~al.(2024)]{tulchinskii2024intrinsic}\nTulchinskii, E., et~al.\n\\newblock Intrinsic dimension estimation for robust detection of AI-generated texts.\n\\newblock In \\emph{Proc.\\ NeurIPS}, 2024.\n\n\\bibitem[Wenzek et~al.(2020)]{wenzek2020ccnet}\nWenzek, G., Lachaux, M.-A., Conneau, A., Chaudhary, V., Guzm{\\'a}n, F., Joulin, A., and Grave, E.\n\\newblock CCNet: Extracting high quality monolingual datasets from web crawl data.\n\\newblock In \\emph{Proc.\\ LREC}, 2020.\n\n\\bibitem[Yang et~al.(2024)]{yang2024dna}\nYang, X., Cheng, W., Petzold, L., Wang, W.~Y., and Chen, H.\n\\newblock DNA-GPT: Divergent n-gram analysis for training-free detection of GPT-generated text.\n\\newblock In \\emph{Proc.\\ ICLR}, 2024.\n\n\\end{thebibliography}\n}\n\n%=============================================================================\n% APPENDIX\n%=============================================================================\n\\appendix\n\\onecolumn\n\n\\section{Prompt-Type Comparison}\n\\label{sec:prompttype}\n\nWe evaluate three prompt types --- continuation, elaboration, and inspired rewriting --- on Pythia-2.8B with 1,000 seeds (Table~\\ref{tab:prompttype}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Prompt Type} & \\textbf{CV F1} & \\textbf{LOPTO F1} & \\textbf{Retention (d4/d0)} \\\\\n\\midrule\nContinuation & 0.781 & 0.762 & 0.831 \\\\\nInspired rewriting & 0.737 & 0.733 & 0.939 \\\\\nElaboration & 0.730 & 0.762 & 0.986 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-prompt-type classification (CV = within-type, LOPTO = leave-one-prompt-type-out). Continuation is strongest (5.1 pp gap) because unconstrained generation maximizes distributional drift. LOPTO average 0.753 confirms cross-prompt-type deployment is viable.}\n\\label{tab:prompttype}\n\\end{table}\n\nDDR is qualitatively consistent across all prompt types: all drifting features show $|\\rho| > 0.55$.\nContinuation produces the strongest signal because it maximizes recursive compression without semantic constraints.\nElaboration is weakest because semantic-preservation constraints limit distributional drift amplitude.\nThe depth retention difference (elaboration 98.6\\% vs.\\ continuation 83.1\\%) reflects that continuation's deeper outputs are more likely to be truncated by minimum-length filters.\n\nFeature drift magnitudes by prompt type:\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Feature} & \\textbf{Cont.\\ $\\rho$} & \\textbf{Elab.\\ $\\rho$} & \\textbf{Rewrite $\\rho$} \\\\\n\\midrule\nHapax ratio & $-0.651$ & $-0.674$ & $-0.670$ \\\\\nTTR & $-0.629$ & $-0.666$ & $-0.659$ \\\\\nEntropy mean & $-0.665$ & $-0.583$ & $-0.564$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Spearman $\\rho$ by feature and prompt type. DDR pattern is preserved across all types.}\n\\end{table}\n\n\n\\section{Paraphrastic vs.\\ Non-Paraphrastic Chains}\n\\label{sec:paraphrastic}\n\nParaphrastic chains (each step paraphrases the previous output) exhibit substantially weaker depth signal than continuation chains (Table~\\ref{tab:para}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Chain Type} & \\textbf{Binary F1} & \\textbf{3-class F1} \\\\\n\\midrule\nContinuation & 0.781 & 0.834 \\\\\nParaphrastic & 0.618 & 0.680 \\\\\n\\midrule\n$\\Delta$ & $-16.3$ pp & $-15.4$ pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Paraphrastic vs.\\ continuation chains. The 16.3 pp binary gap reflects attractor convergence in paraphrastic chains.}\n\\label{tab:para}\n\\end{table}\n\nParaphrastic chains converge by depth $\\sim$3 (depth-3 vs.\\ depth-2 binary F1 = 0.525, near chance), consistent with attractor cycle theory \\citep{briakou2025llm}.\nContinuation chains retain discriminability at deeper depths (depth-3 vs.\\ depth-2 F1 = 0.640).\nSemantic similarity from depth 0 to depth 4 is 0.88 for paraphrastic chains (meaning preserved) vs.\\ 0.52 for continuation (significant topic drift).\nDDR correlations in paraphrastic chains are uniformly weak ($|\\rho| < 0.33$), confirming that DDR is specific to non-paraphrastic generation.\n\n\n\\section{Multi-Domain Evaluation}\n\\label{sec:multidomain}\n\nWe evaluate on four seed domains to test ecological validity (Table~\\ref{tab:domain}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Domain} & \\textbf{Binary F1} & \\textbf{3-class F1} & \\textbf{Hapax $\\rho$} & \\textbf{Ent.\\ mean $\\rho$} \\\\\n\\midrule\nWikipedia & 0.694 & 0.770 & $-0.647$ & $-0.610$ \\\\\nNews & 0.712 & 0.715 & $-0.621$ & $-0.595$ \\\\\nCode & 0.687 & 0.673 & $-0.630$ & $-0.581$ \\\\\nAcademic & 0.628 & 0.656 & $-0.543$ & $-0.520$ \\\\\n\\midrule\nCross-domain & 0.676 & --- & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-domain evaluation. DDR pattern is qualitatively consistent (all drifting $|\\rho| > 0.52$). Academic domain is weakest due to formulaic genre conventions limiting distributional drift.}\n\\label{tab:domain}\n\\end{table}\n\nMaximum domain gap is 8.4 pp (news 0.712 vs.\\ academic 0.628).\nAcademic text is weakest because its highly formulaic genre conventions (strict sentence structures, specialized terminology) limit the distributional drift space, and its low baseline TTR creates a ceiling effect.\nNews text is strongest due to high vocabulary diversity providing larger feature margins.\nAll domains show drifting $|\\rho| > 0.52$, confirming DDR pattern consistency.\n\n\n\\section{Finer-Grained Ordinal Classification}\n\\label{sec:ordinal}\n\nFive-class ordinal classification (gen-0 through gen-4) reveals a practical 3-class resolution ceiling (Table~\\ref{tab:ordinal}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & \\textbf{5-class F1} & \\textbf{3-class F1} \\\\\n\\midrule\nXGBoost & 0.503 & 0.773 \\\\\nCORAL & 0.497 & --- \\\\\nFrank-Hall & 0.501 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{5-class ordinal classification. All methods perform comparably ($<$1 pp spread). 3-class reference included for comparison.}\n\\label{tab:ordinal}\n\\end{table}\n\nPer-class 5-class F1: gen-0 = 0.952, gen-1 = 0.518, gen-2 = 0.348, gen-3 = 0.325, gen-4 = 0.372.\nGen-0 remains highly discriminable (human text); gen-2/3/4 are severely confused (mutual misclassification rate 42\\%).\nThe bottleneck is the gen-1/gen-2 boundary, which concentrates 86\\% of binary errors as false negatives.\nOrdinal methods (CORAL, Frank-Hall) do not improve over standard XGBoost because the ordinal margin between adjacent deeper classes is not uniform --- the gen-0$\\to$gen-1 margin far exceeds gen-2$\\to$gen-3, violating the equal-spacing assumption these methods require.\nThe MAE of 0.72 depth levels indicates predictions are off by less than one class on average.\n\n\n\\section{Human Edit Robustness}\n\\label{sec:edit}\n\nWe test robustness to simulated human editing via random word replacement and LLM-based rephrasing (Table~\\ref{tab:edit}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{Binary F1} & \\textbf{$\\Delta$ (pp)} \\\\\n\\midrule\nBaseline (no edit) & 0.695 & --- \\\\\n5\\% random replacement & 0.650 & $-4.6$ \\\\\n10\\% random replacement & 0.614 & $-8.1$ \\\\\n20\\% random replacement & 0.591 & $-10.4$ \\\\\nLLM rephrase & 0.647 & $-4.5$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Binary F1 under simulated editing. Degradation is graceful: LLM rephrase ($\\sim$50\\% edit distance, $\\sim$1.7 sentences replaced) causes only 4.5 pp drop.}\n\\label{tab:edit}\n\\end{table}\n\nDegradation is graceful rather than catastrophic.\nAt 5\\% random replacement, distributional features (TTR, entropy, hapax) are barely affected because they are global statistics --- sparse point noise does not alter aggregate patterns.\nLLM rephrasing ($\\sim$50\\% edit distance) causes a comparable 4.5 pp drop: rephrasing preserves coherence and topic but alters local word choice, partially disrupting surface features while reference features (NLL-based) remain more robust because rephrased text's NLL retains depth-dependent patterns.\nEven under 20\\% replacement, binary F1 (0.591) substantially exceeds chance (0.50).\nMulticlass degradation is larger ($-7.1$ pp under LLM rephrase) because editing primarily blurs the gen-1/gen-2+ boundary.\n\n\n\\section{LD-Score as Additional Feature}\n\\label{sec:ldscore}\n\nWe evaluate LD-Score (character-level distribution signature) as a potential 8th feature (Table~\\ref{tab:ldscore}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Configuration} & \\textbf{LOGO F1} \\\\\n\\midrule\n7-feature ensemble & 0.798 \\\\\n8-feature (+ LD-Score) & 0.801 \\\\\nLD-Score standalone & 0.721 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Adding LD-Score to the 7-feature ensemble yields only 0.3 pp improvement. LD-Score correlates heavily with surface features (hapax $r = 0.72$, TTR $r = 0.68$).}\n\\label{tab:ldscore}\n\\end{table}\n\nLD-Score alone achieves moderate signal (F1 = 0.721, Spearman $\\rho = 0.794$ with depth), but adding it to the ensemble improves F1 by only 0.3 pp.\nCharacter-level vocabulary diversity is highly co-linear with word-level surface features (hapax $r = 0.72$, TTR $r = 0.68$), providing negligible complementary information.\nWe retain the 7-feature set as the recommended configuration for simplicity, interpretability, and efficiency.\n\n\n\\section{End-to-End Neural Classifier}\n\\label{sec:qlora}\n\nWe compare the 7-feature ensemble against QLoRA-finetuned end-to-end classifiers as an upper-bound reference (Table~\\ref{tab:qlora}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{3-class F1} & \\textbf{Binary F1} & \\textbf{GPU (GB)} \\\\\n\\midrule\nQLoRA (instruct) & 0.897 & 0.852 & 8.2 \\\\\nQLoRA (base) & 0.881 & 0.826 & 8.2 \\\\\n7-feature ensemble & 0.773 & 0.694 & 2.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{QLoRA vs.\\ 7-feature ensemble. QLoRA achieves substantially higher within-distribution F1 but at 3.4$\\times$ GPU memory and 6.5$\\times$ inference time.}\n\\label{tab:qlora}\n\\end{table}\n\nQLoRA achieves 12--16 pp higher within-distribution F1 by learning contextual, positional, and discourse-level patterns beyond our handcrafted features.\nHowever, QLoRA's cross-generator generalization (LOGO binary 0.720) is substantially below its within-distribution performance (0.826--0.852), indicating partial overfitting to generator-specific token patterns.\nThe 7-feature ensemble's advantages are: (a) 3.4$\\times$ less GPU memory, (b) 6.5$\\times$ faster inference, (c) interpretable features with clear DDR semantics, (d) more stable cross-generator generalization.\nNotably, QLoRA's 5-class F1 (0.551) only exceeds the handcrafted baseline (0.503) by $\\sim$5 pp, confirming that finer classification is bottlenecked by task-inherent difficulty.\n\n\n\\section{Text Length Confound Control}\n\\label{sec:length}\n\nWe verify that depth signal is not an artifact of text length variation (Table~\\ref{tab:length}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{Binary F1} & \\textbf{$\\Delta$ (pp)} \\\\\n\\midrule\nUnmatched & 0.770 & --- \\\\\nRandom subsample (equal $n$) & 0.741 & $-2.9$ \\\\\nLength-matched & 0.724 & $-4.6$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Length confound analysis. Of the 4.6 pp drop from length matching, 2.9 pp is attributable to sample-size reduction and only 1.7 pp to deconfounding.}\n\\label{tab:length}\n\\end{table}\n\nLength--depth Spearman $\\rho$ is weak ($[-0.066, +0.134]$): text length does not systematically vary with depth.\nOf the 4.6 pp drop from length matching, 2.9 pp is attributable to sample-size reduction (random subsample control) and only 1.7 pp to actual deconfounding.\nLength-normalized surface features (computed over fixed-length windows) \\emph{strengthen} the depth trend ($|\\rho|$ increases), confirming that DDR arises from intrinsic vocabulary diversity decrease rather than length variation.\n\n\n\\section{Large-Scale Generator}\n\\label{sec:scale}\n\nWe add Qwen3-8B-Base to test scale effects (Table~\\ref{tab:scale}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Generator} & \\textbf{Binary F1} & \\textbf{Hapax $\\rho$} & \\textbf{Tail decay $\\rho$} \\\\\n\\midrule\n$<$3B average & 0.700 & $-0.647$ & $-0.040$ \\\\\nQwen3-8B & 0.683 & $-0.558$ & $-0.089$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Scale effect: 8B generator shows moderate degradation ($-1.7$ pp binary F1) with attenuated drifting $|\\rho|$ ($\\sim$85\\% of $<$3B average). DDR pattern (drifting vs.\\ stationary split) is qualitatively preserved.}\n\\label{tab:scale}\n\\end{table}\n\nQwen3-8B binary F1 = 0.683 (95\\% CI [0.660, 0.706]), a moderate 1.7 pp drop from the $<$3B average.\nDrifting features retain $\\sim$85\\% of their correlation magnitude (hapax $\\rho = -0.558$ vs.\\ $-0.647$).\nThe DDR pattern is qualitatively preserved: the three drifting features remain highest-$|\\rho|$ (hapax $-0.558$, TTR $-0.542$, entropy mean $-0.475$), while stationary features remain low ($|\\rho| < 0.10$).\nHigher-capacity models produce more concentrated generation distributions with lower baseline vocabulary diversity, compressing depth-wise feature margins.\n$N = 4{,}497$ total records with depth-dependent dropout (d4: 755/995 seeds) more pronounced than for smaller models.\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8df179e-d4a1-48d2-be8e-98406176ce5a",
  "isSidechain": false,
  "requestId": "req_011CbEjEiep7ax8gcZrPGB53",
  "type": "assistant",
  "uuid": "317a2ae9-9d3c-4cfe-aba4-12af57fe47b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "7a6e7dae-2371-44f2-a86f-776f12713121",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PFQKqduer9bw2khv8Cb7hZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1756,
      "cache_read_input_tokens": 45123,
      "output_tokens": 13197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1756,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13197,
          "cache_read_input_tokens": 45123,
          "cache_creation_input_tokens": 1756,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1756
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

_source line 19 · 2026-05-21T00:03:04.512Z_

<details><summary>↩ Tool result · `toolu_01LWzHzh28BPPiQq49Cos8Mj`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T232427/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "317a2ae9-9d3c-4cfe-aba4-12af57fe47b1",
  "isSidechain": false,
  "promptId": "1ca86b45-b190-47c7-9689-3b48717c505c",
  "type": "user",
  "uuid": "fed85f04-429e-4f52-bb4c-004d23838629",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T232427/best/paper.tex",
    "content": "\\documentclass[11pt,twocolumn]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{geometry}\n\\geometry{a4paper, margin=2.5cm}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\\usepackage{array}\n\\usepackage{enumitem}\n\n\\setlength{\\columnsep}{0.6cm}\n\n\\title{Differential Depth Response in Iterative LLM Generation:\\\\\nA Distributional Fingerprint for Provenance Characterization}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%=============================================================================\n% ABSTRACT\n%=============================================================================\n\\begin{abstract}\nWeb-scraped training corpora increasingly contain LLM-generated text of unknown provenance depth.\nCurrent detectors offer only binary real-vs-synthetic classification, conflating qualitatively different material:\nfirst-generation text retains much of the source lexical distribution, while deeper recursive outputs exhibit measurably reduced vocabulary diversity and compressed perplexity.\nWe formulate \\textbf{generation depth classification} (gen-0/gen-1/gen-2+) and characterize \\textbf{differential depth response} (DDR) across 8 base-model generators from 5 families (0.6B--8B):\ncentral-tendency features (entropy mean, TTR, hapax ratio) drift monotonically with depth ($|\\rho| \\geq 0.55$), while shape features (tail decay, entropy max) remain near-stationary ($|\\rho| < 0.10$).\nA lightweight 7-feature ensemble achieves leak-free binary F1 = 0.694 under 8-generator leave-one-generator-out (LOGO) evaluation (95\\% CI [0.688, 0.700]), and 0.830 on cross-model chains.\nCross-family generalization is confirmed via leave-one-family-out evaluation (binary F1 = 0.686).\nDDR is robust across 3 reference models from different families; shape-feature stationarity holds with $|\\rho| < 0.06$.\nDepth-aware data curation is statistically equivalent to random subsampling for downstream causal language modeling quality (TOST $p = 1.1 \\times 10^{-4}$ at $\\pm 2\\%$ margin), establishing depth fingerprinting as a \\textbf{diagnostic} tool for provenance characterization rather than a curative tool for data selection.\nCurrent scope is restricted to base models at moderate temperatures ($t \\leq 0.9$).\n\\end{abstract}\n\n%=============================================================================\n% 1. INTRODUCTION\n%=============================================================================\n\\section{Introduction}\n\nLarge language models (LLMs) are generating an increasing fraction of web content.\nRecent estimates suggest 7--17\\% of scientific papers and significant portions of web-scraped corpora contain LLM-generated text \\citep{liang2024monitoring}.\nThis poses challenges for training data curation: recursive consumption of synthetic data can degrade model quality through distributional collapse \\citep{shumailov2024model}.\n\nCurrent AI text detection methods operate as binary classifiers --- real vs.\\ synthetic --- and cannot distinguish \\emph{how many generations removed} a text is from its human-authored seed.\nThis distinction matters: first-generation (gen-1) text retains much of the source distribution's lexical properties, while deeper recursive outputs exhibit measurably reduced vocabulary diversity and compressed perplexity distributions.\nConflating these qualitatively different materials limits our ability to understand and mitigate model collapse risks.\n\nWe address this gap by formulating \\textbf{generation depth classification}: given a text, predict whether it is human-authored (gen-0), first-generation LLM output (gen-1), or deeper recursive output (gen-2+).\nOur investigation reveals \\textbf{differential depth response} (DDR): features derived from the next-token log-likelihood (NLL) distribution exhibit a systematic split.\n\\emph{Central-tendency features} (entropy mean, type-token ratio, hapax ratio) drift monotonically with generation depth, consistent with recursive compression of the token distribution.\n\\emph{Shape features} (tail decay rate, entropy max) remain near-stationary, indicating that recursive generation induces a \\emph{location shift} in the NLL distribution while approximately preserving distributional shape.\n\nWe validate DDR across 8 base-model generators from 5 architectural families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B--8B parameters) and 3 reference models.\nA 7-feature ensemble achieves leak-free binary F1 = 0.694 under LOGO evaluation, outperforming repurposed binary detectors (avg-logprob 0.765, FastDetectGPT 0.627, Binoculars 0.579 on macro F1).\nCross-model chains --- where each generation step uses a different generator --- yield binary F1 = 0.830, suggesting generator heterogeneity \\emph{amplifies} rather than obscures depth signal.\n\nOur third contribution is a calibrated negative finding: depth-aware data curation does not improve downstream language modeling quality compared to random subsampling (TOST equivalence confirmed at $\\pm 2\\%$ margin).\nThis positions depth fingerprinting as a \\textbf{diagnostic tool} for data provenance characterization, not a curative tool for data selection.\n\nWe report scope limitations transparently: the signal degrades substantially under instruction tuning (LOGO F1 = 0.338 vs.\\ 0.763 for base models), restricting current applicability to base models at moderate sampling temperatures.\n\n%=============================================================================\n% 2. RELATED WORK\n%=============================================================================\n\\section{Related Work}\n\n\\paragraph{AI text detection.}\nPerplexity-based methods leverage distributional differences between human and machine text.\nGLTR \\citep{gehrmann2019gltr} visualizes token-level log probabilities;\nDetectGPT \\citep{mitchell2023detectgpt} and its faster variant Fast-DetectGPT \\citep{bao2024fast} use perturbation-based log probability curvature;\nBinoculars \\citep{hans2024spotting} computes cross-entropy ratios between two models;\nDNA-GPT \\citep{yang2024dna} uses divergent n-gram analysis.\nAll operate as binary classifiers and cannot estimate generation depth.\n\n\\paragraph{Model collapse \\& iterative generation.}\n\\citet{shumailov2024model} formalize model collapse under iterative training on synthetic data, showing distributional tails vanish over generations.\n\\citet{dohmatob2024tale} provide theoretical bounds on variance collapse.\nLLM as Broken Telephone \\citep{briakou2025llm} studies paraphrastic attractor cycles, showing convergence within $\\sim$3 iterations.\nOur work addresses the complementary non-paraphrastic setting where unconstrained generation permits unbounded distributional drift.\n\n\\paragraph{Data quality \\& provenance.}\nVocabulary diversity metrics (TTR, hapax ratio) are established in corpus linguistics \\citep{mccarthy2010mtld}.\nLD-Score \\citep{tulchinskii2024intrinsic} uses character-level distribution divergence as a detection signal.\nPerplexity-based data filtering \\citep{wenzek2020ccnet} is standard in corpus construction.\nOur work extends these to ordinal depth estimation.\n\n\\paragraph{Stylometry \\& authorship.}\nAuthorship attribution methods \\citep{neal2017surveying} use distributional features for author identification.\nOur feature set draws on this tradition but targets generation depth rather than individual authorship.\n\n%=============================================================================\n% 3. METHOD\n%=============================================================================\n\\section{Method}\n\n\\subsection{Task Formulation}\n\nGiven a text passage $x$, we predict its \\emph{generation depth} $d \\in \\{0, 1, 2+\\}$:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{gen-0}: Human-authored seed text.\n    \\item \\textbf{gen-1}: First-generation LLM output from a human seed.\n    \\item \\textbf{gen-2+}: Output of $\\geq$2 recursive generation steps.\n\\end{itemize}\n\nThe \\textbf{primary metric} is leak-free binary F1 (gen-1 vs.\\ gen-2+), excluding gen-0 to avoid seed-sharing leakage.\nThree-class macro F1 is reported but noted as inflated by gen-0's strong discriminability.\n\n\\subsection{Generation Chain Construction}\n\nFor each human-authored seed $s$, we construct a chain $\\{x_0 = s, x_1, x_2, x_3, x_4\\}$ where $x_{d+1} = \\text{LLM}(x_d)$ using continuation prompting at temperature $t = 0.7$.\nChains are constructed independently per generator.\nCross-model chains use a different generator at each depth step.\n\n\\subsection{Feature Extraction}\n\\label{sec:features}\n\nWe extract 7 features per passage using a reference model $M_{\\text{ref}}$ (Pythia-410M by default):\n\n\\paragraph{Surface features} (computed from raw text):\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{TTR}: Type-token ratio (unique tokens / total tokens).\n    \\item \\textbf{Hapax ratio}: Fraction of tokens appearing exactly once.\n\\end{itemize}\n\n\\paragraph{Reference features} (computed from $M_{\\text{ref}}$'s NLL distribution over $x$):\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{Entropy mean}: Mean per-token NLL.\n    \\item \\textbf{Entropy std}: Standard deviation of per-token NLL.\n    \\item \\textbf{Entropy min/max}: Extremal NLL values.\n    \\item \\textbf{Tail decay}: Decay rate of the upper tail of the NLL distribution, estimated via exponential fit.\n\\end{itemize}\n\n\\subsection{Differential Depth Response (DDR)}\n\nDDR characterizes feature behavior as a function of generation depth via Spearman rank correlation $\\rho$ between feature value and depth $d$:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{Drifting features} ($|\\rho| \\geq 0.55$): hapax ratio, TTR, entropy mean. These exhibit monotonic trends with depth, consistent with recursive compression.\n    \\item \\textbf{Stationary features} ($|\\rho| < 0.10$): tail decay, entropy max. These remain near-constant, indicating the NLL distribution's shape is preserved under location shift.\n    \\item \\textbf{Weakly drifting}: entropy std ($|\\rho| \\approx 0.20$), intermediate between the two groups.\n\\end{itemize}\n\n\\subsection{Evaluation Protocol}\n\nWe use two leave-out evaluation protocols to prevent information leakage:\n\n\\paragraph{LOGO} (Leave-One-Generator-Out): Train on $K{-}1$ generators, test on the held-out generator. Measures cross-generator generalization.\n\n\\paragraph{LOFO} (Leave-One-Family-Out): Train on all generators except those from one architectural family (e.g., hold out all Pythia models). Measures cross-family transfer.\n\nThe classifier is XGBoost with default hyperparameters, evaluated via 5-fold cross-validation within each training split.\n\n%=============================================================================\n% 4. EXPERIMENTS\n%=============================================================================\n\\section{Experiments}\n\n\\subsection{Setup}\n\n\\paragraph{Generators.} We evaluate 8 base-model generators spanning 5 families: Pythia-1B, Pythia-2.8B (EleutherAI); OLMo-2-1B (AI2); Qwen3-0.6B, Qwen3-1.7B, Qwen3-8B (Alibaba); Llama-3.2-3B (Meta); Mistral-7B (Mistral AI).\nAll generation uses continuation prompting at $t = 0.7$.\n\n\\paragraph{Seeds.} Wikipedia passages serve as the primary seed domain ($\\sim$1000 seeds per generator), with additional evaluation on news, academic, and code domains (\\S\\ref{sec:multidomain}).\n\n\\paragraph{Reference model.} Pythia-410M (default). Cross-reference robustness evaluated with OLMo-2-1B and Qwen3-0.6B (\\S\\ref{sec:crossref}).\n\n\\subsection{Feature Ablation \\& Trend Analysis}\n\\label{sec:ablation}\n\nTable~\\ref{tab:ablation} reports 5-fold CV results on the full dataset, ablating feature groups.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Feature Set} & \\textbf{Macro F1} \\\\\n\\midrule\nFull (7 features) & 0.820 \\\\\nSurface only (TTR, hapax) & 0.763 \\\\\nReference only (5 features) & 0.719 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Feature ablation (5-fold CV). Full set significantly outperforms both subsets (McNemar $p < 0.001$), confirming surface--reference complementarity.}\n\\label{tab:ablation}\n\\end{table}\n\nSurface and reference features are complementary: the full set outperforms surface-only by 5.7 pp and reference-only by 10.1 pp (McNemar $p < 0.001$ for both).\nThis establishes that depth signal arises from two distinct sources: vocabulary diversity reduction (surface) and NLL distribution shift (reference).\n\n\\paragraph{DDR trend analysis.}\nLinear regression of features against depth confirms the drifting/stationary split (Table~\\ref{tab:trends}).\nDrifting features show high $R^2$: entropy mean (0.93), hapax ratio (0.92), TTR (0.89).\nStationary features show near-zero $R^2$: tail decay (0.03).\nEntropy std occupies an intermediate position ($R^2 = 0.41$, slope $= -0.12$), with drift magnitude $\\sim$1/3 of the drifting group.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Feature} & \\textbf{Slope} & $R^2$ & \\textbf{Category} \\\\\n\\midrule\nEntropy mean & $-0.29$ & 0.93 & Drifting \\\\\nHapax ratio & $-0.043$ & 0.92 & Drifting \\\\\nTTR & $-0.034$ & 0.89 & Drifting \\\\\nEntropy std & $-0.12$ & 0.41 & Weak \\\\\nTail decay & $+0.002$ & 0.03 & Stationary \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-feature linear trend across depths 0--4. Drifting features exhibit strong monotonic decrease ($R^2 > 0.89$); tail decay is effectively flat.}\n\\label{tab:trends}\n\\end{table}\n\nPerplexity under the reference model decreases monotonically with depth (median: 13.5, 4.96, 3.00, 2.07, 1.72 for depths 0--4), confirming that recursive generation compresses the NLL distribution leftward.\n\n\\subsection{Cross-Generator Generalization}\n\\label{sec:crossgen}\n\nTable~\\ref{tab:crossgen} reports per-generator LOGO results on the 5-generator subset (Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B; $N = 23{,}032$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Generator} & \\textbf{Macro F1} & \\textbf{Binary F1} \\\\\n\\midrule\nPythia-1B & 0.851 & 0.724 \\\\\nPythia-2.8B & 0.804 & 0.720 \\\\\nQwen3-0.6B & 0.818 & 0.715 \\\\\nQwen3-1.7B & 0.805 & 0.710 \\\\\nOLMo-2-1B & 0.752 & 0.670 \\\\\n\\midrule\n\\textbf{Average} & \\textbf{0.804} & \\textbf{0.720} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-generator LOGO evaluation (5-gen subset). Binary F1 variance across generators is 5.4 pp, confirming cross-generator robustness.}\n\\label{tab:crossgen}\n\\end{table}\n\nThe LOGO binary F1 of 0.720 (95\\% CI [0.708, 0.732]) demonstrates cross-generator generalization.\nPer-generator variance is 5.4 pp, with OLMo-2-1B lowest (0.670) due to its non-GPT-NeoX architecture producing more divergent distributional patterns.\nHapax ratio is the most important feature (importance = 0.289), followed by TTR (0.168) and entropy mean (0.160).\n\n\\paragraph{Cross-family transfer.}\nLOFO evaluation confirms generalization beyond same-family models: Pythia held-out F1 = 0.690, OLMo held-out = 0.720, Qwen held-out = 0.706 (average LOFO binary F1 = 0.705).\nThe 1.5 pp drop from LOGO to LOFO indicates minimal family-specific inflation.\n\n\\subsection{Cross-Reference-Model Robustness}\n\\label{sec:crossref}\n\nTo verify that DDR is not an artifact of the Pythia-410M reference model, we extract features using two additional reference models: OLMo-2-1B and Qwen3-0.6B (Table~\\ref{tab:crossref}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Reference} & \\textbf{Macro F1} & \\multicolumn{2}{c}{\\textbf{Spearman $\\rho$}} \\\\\n\\cmidrule(lr){3-4}\n & & hapax & tail decay \\\\\n\\midrule\nPythia-410M & 0.803 & $-0.647$ & $-0.040$ \\\\\nOLMo-2-1B & 0.807 & $-0.647$ & $-0.038$ \\\\\nQwen3-0.6B & 0.816 & $-0.647$ & $-0.042$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{LOGO macro F1 and representative Spearman $\\rho$ by reference model. DDR pattern (drifting vs.\\ stationary split) is consistent across all three reference families. Surface features are identical by construction.}\n\\label{tab:crossref}\n\\end{table}\n\nClassification F1 varies by only 1.3 pp across reference models.\nEntropy mean drift direction is consistently negative across all three reference families (Pythia: $[-1.19, -1.40]$; OLMo: $[-0.61, -0.91]$; Qwen: $[-0.96, -1.35]$).\nShape-feature stationarity holds robustly: maximum $|\\rho|$ across all reference models is 0.055.\nDDR is a property of the generation process, not an artifact of reference model choice.\n\n\\subsection{Baseline Comparison}\n\\label{sec:baseline}\n\nWe compare our 7-feature ensemble against four existing detectors repurposed as ordinal depth predictors (Table~\\ref{tab:baseline}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & \\textbf{LOGO F1} & \\textbf{Spearman $\\rho$} \\\\\n\\midrule\n7-feature ensemble & \\textbf{0.798} & --- \\\\\nAvg log-prob & 0.765 & 0.788 \\\\\nLD-Score & 0.721 & 0.794 \\\\\nFast-DetectGPT & 0.627 & 0.433 \\\\\nBinoculars & 0.579 & 0.199 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{LOGO macro F1 for ordinal depth classification. 7-feature ensemble significantly outperforms all baselines (bootstrap $p < 0.01$). CI for avg-logprob is wide: [0.616, 0.820], reflecting high cross-generator variance.}\n\\label{tab:baseline}\n\\end{table}\n\nThe 7-feature ensemble achieves 0.798, significantly outperforming the best single detector (avg-logprob 0.765; bootstrap $\\Delta = 3.3$ pp, $p < 0.01$).\nAvg-logprob is strongest among single detectors because it directly measures NLL mean --- essentially an unnormalized entropy mean.\nHowever, its narrow 95\\% CI [0.616, 0.820] reveals high per-generator variance, whereas the 7-feature ensemble achieves a much tighter CI [0.786, 0.799].\n\nBinoculars performs worst (0.579): its two-model probability ratio partially cancels depth signal, as both models' NLL decreases with depth.\nFast-DetectGPT (0.627) was designed for binary detection; its perturbation-based curvature metric is insensitive to ordinal depth variation.\n\n\\subsection{Cross-Model Chains}\n\\label{sec:crossmodel}\n\nReal-world contamination involves diverse generators. We evaluate on cross-model chains where each depth step uses a different generator (Table~\\ref{tab:crossmodel}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Setting} & \\textbf{Binary F1} & \\textbf{3-class F1} \\\\\n\\midrule\nSingle-model (LOGO) & 0.694 & --- \\\\\nCross-model (LOGO) & \\textbf{0.830} & 0.789 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model chains (5-gen, generator-level LOGO) vs.\\ single-model LOGO. Generator heterogeneity \\emph{amplifies} depth signal ($+$13.6 pp binary F1).}\n\\label{tab:crossmodel}\n\\end{table}\n\nCross-model binary F1 = 0.830 (95\\% CI [0.812, 0.848]) exceeds single-model LOGO by 13.6 pp.\nPer-generator variance drops to 4.0 pp (vs.\\ 5.4 pp for single-model), indicating more stable signal under heterogeneity.\nDDR drifting-feature correlations strengthen in cross-model chains (hapax $\\rho = -0.72$ vs.\\ $-0.647$ single-model): each generator change injects fresh distributional perturbation, preventing convergence to a model-specific attractor state.\nThis is a positive ecological validity result: realistic multi-generator contamination is \\emph{easier}, not harder, to detect.\n\n\\subsection{Downstream Utility (Negative Finding)}\n\\label{sec:downstream}\n\nWe test whether depth-aware data curation improves downstream language model quality by fine-tuning OLMo-2-1B (1.485B parameters) on depth-stratified subsets (Table~\\ref{tab:downstream}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrcc}\n\\toprule\n\\textbf{Variant} & $n$ & \\textbf{PPL} & \\textbf{$\\pm$ std} \\\\\n\\midrule\nAll data & 12,299 & 2.335 & 0.0003 \\\\\nSize-matched (random) & 3,951 & 2.367 & 0.0002 \\\\\nDepth 0--1 only & 3,951 & 2.387 & 0.001 \\\\\nBinary-filtered & 3,951 & 2.389 & 0.001 \\\\\nDepth-0 only & 797 & 2.681 & 0.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Downstream CLM perplexity (3 seeds). Depth-aware curation (depth 0--1, binary-filtered) does not outperform random subsampling at equal sample count.}\n\\label{tab:downstream}\n\\end{table}\n\nThe ranking is: all data (2.335) $<$ size-matched random (2.367) $<$ depth 0--1 (2.387) $\\approx$ binary-filtered (2.389) $\\ll$ depth-0 only (2.681).\nTOST equivalence tests at $\\pm 2\\%$ margin confirm that depth-aware curation and random subsampling produce equivalent downstream quality ($p = 1.1 \\times 10^{-4}$ for size-matched vs.\\ depth 0--1; $p = 9 \\times 10^{-5}$ for size-matched vs.\\ binary-filtered).\nAt the stricter $\\pm 1\\%$ margin, equivalence is not confirmed ($p = 0.08$).\n\nDepth filtering removes deeper text but also removes diverse training signal; random subsampling preserves more complete distributional coverage.\nSeed variance is minimal ($< 0.002$ across seeds), confirming the stability of this negative finding.\nThis establishes depth fingerprinting as a \\textbf{diagnostic} tool --- useful for characterizing data provenance --- rather than a curative tool for improving training data quality.\n\n%=============================================================================\n% 5. DISCUSSION\n%=============================================================================\n\\section{Discussion}\n\n\\paragraph{DDR as location shift.}\nThe drifting/stationary split is consistent with recursive generation inducing a location shift in the NLL distribution: central-tendency features (mean, diversity) drift while shape features (tail decay, entropy max) are preserved.\nThis is not a ``discovery'' in the strong sense --- it follows from properties of the NLL distribution under recursive compression --- but its empirical robustness across 8 generators, 5 families, and 3 reference models is the contribution.\n\n\\paragraph{Entropy std as intermediate case.}\nEntropy std shows weak drift ($|\\rho| \\approx 0.20$, $R^2 = 0.41$), with magnitude $\\sim$1/3 of the drifting group.\nWe classify it as ``weakly drifting'' without disrupting the core binary distinction.\nIts feature importance is low (rank 5/7 in the 5-gen evaluation).\n\n\\paragraph{Limitations.}\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{Base models only.} Instruction tuning compresses the distributional variation DDR exploits (LOGO F1 = 0.338 for OLMo-Instruct vs.\\ 0.763 base). This is the primary scope limitation.\n\\item \\textbf{Temperature sensitivity.} Reliable within $t \\in [0.5, 0.9]$. At $t = 1.0$, entropy mean $\\rho$ drops to $-0.002$.\n\\item \\textbf{Scale effect.} Larger generators show moderate degradation (Qwen3-8B binary F1 = 0.683; $\\sim$85\\% of drifting $|\\rho|$ vs.\\ $<$3B average). DDR pattern is qualitatively preserved (\\S\\ref{sec:scale}).\n\\item \\textbf{3-class resolution ceiling.} 5-class F1 drops to $\\sim$0.50; ordinal methods offer no improvement (\\S\\ref{sec:ordinal}).\n\\item \\textbf{Prompt-type dependence.} Continuation chains (F1 = 0.781) outperform elaboration (0.730) by 5.1 pp (\\S\\ref{sec:prompttype}).\n\\item \\textbf{Downstream evidence.} Limited to single-task (CLM) and single-metric (perplexity) evaluation with 3 seeds.\n\\end{enumerate}\n\n%=============================================================================\n% 6. CONCLUSION\n%=============================================================================\n\\section{Conclusion}\n\nWe formulate generation depth classification and characterize differential depth response (DDR) across 8 base-model generators from 5 families.\nA 7-feature distributional ensemble achieves leak-free binary F1 = 0.694 (per-generator range: 0.633--0.724) under LOGO evaluation, with cross-model chains reaching 0.830.\nDDR is robust across reference models and generator families but degrades under instruction tuning, defining a clear scope boundary.\nDepth-aware curation is statistically equivalent to random subsampling for downstream quality, positioning depth fingerprinting as a diagnostic rather than curative tool.\nFuture work should address instruction-tuned models, larger scales ($>$14B), and downstream tasks beyond causal language modeling.\n\n%=============================================================================\n% REFERENCES\n%=============================================================================\n{\\small\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{20}\n\n\\bibitem[Bao et~al.(2024)]{bao2024fast}\nBao, G., Zhao, Y., Teng, Z., Yang, L., and Zhang, Y.\n\\newblock Fast-DetectGPT: Efficient zero-shot detection of machine-generated text via conditional probability curvature.\n\\newblock In \\emph{Proc.\\ ICLR}, 2024.\n\n\\bibitem[Briakou et~al.(2025)]{briakou2025llm}\nBriakou, E., et~al.\n\\newblock LLM as a broken telephone: Iterative paraphrasing converges to attractor cycles.\n\\newblock In \\emph{Proc.\\ ACL}, 2025.\n\n\\bibitem[Dohmatob et~al.(2024)]{dohmatob2024tale}\nDohmatob, E., Feng, Y., and Gu, Q.\n\\newblock A tale of tails: Model collapse as a change of scaling laws.\n\\newblock In \\emph{Proc.\\ ICML}, 2024.\n\n\\bibitem[Gehrmann et~al.(2019)]{gehrmann2019gltr}\nGehrmann, S., Strobelt, H., and Rush, A.~M.\n\\newblock GLTR: Statistical detection and visualization of generated text.\n\\newblock In \\emph{Proc.\\ ACL Demo}, 2019.\n\n\\bibitem[Hans et~al.(2024)]{hans2024spotting}\nHans, A., Schwarzschild, A., Cheber, V., Alon, U., Lyu, Z., and Goldstein, T.\n\\newblock Spotting LLMs with Binoculars: Zero-shot detection of machine-generated text.\n\\newblock In \\emph{Proc.\\ ICML}, 2024.\n\n\\bibitem[Liang et~al.(2024)]{liang2024monitoring}\nLiang, W., et~al.\n\\newblock Monitoring AI-modified content at scale: A case study on the impact of ChatGPT on AI conference peer reviews.\n\\newblock \\emph{arXiv:2403.07183}, 2024.\n\n\\bibitem[McCarthy and Jarvis(2010)]{mccarthy2010mtld}\nMcCarthy, P.~M. and Jarvis, S.\n\\newblock MTLD, vocd-D, and HD-D: A validation study of sophisticated approaches to lexical diversity assessment.\n\\newblock \\emph{Behavior Research Methods}, 42(2):381--392, 2010.\n\n\\bibitem[Mitchell et~al.(2023)]{mitchell2023detectgpt}\nMitchell, E., Lee, Y., Khazatsky, A., Manning, C.~D., and Finn, C.\n\\newblock DetectGPT: Zero-shot machine-generated text detection using probability curvature.\n\\newblock In \\emph{Proc.\\ ICML}, 2023.\n\n\\bibitem[Neal and Woodard(2017)]{neal2017surveying}\nNeal, T. and Woodard, D.\n\\newblock Surveying stylometry techniques and applications.\n\\newblock \\emph{ACM Computing Surveys}, 50(6):1--36, 2017.\n\n\\bibitem[Shumailov et~al.(2024)]{shumailov2024model}\nShumailov, I., Shumaylov, Z., Zhao, Y., Gal, Y., Papernot, N., and Anderson, R.\n\\newblock AI models collapse when trained on recursively generated data.\n\\newblock \\emph{Nature}, 631:755--759, 2024.\n\n\\bibitem[Tulchinskii et~al.(2024)]{tulchinskii2024intrinsic}\nTulchinskii, E., et~al.\n\\newblock Intrinsic dimension estimation for robust detection of AI-generated texts.\n\\newblock In \\emph{Proc.\\ NeurIPS}, 2024.\n\n\\bibitem[Wenzek et~al.(2020)]{wenzek2020ccnet}\nWenzek, G., Lachaux, M.-A., Conneau, A., Chaudhary, V., Guzm{\\'a}n, F., Joulin, A., and Grave, E.\n\\newblock CCNet: Extracting high quality monolingual datasets from web crawl data.\n\\newblock In \\emph{Proc.\\ LREC}, 2020.\n\n\\bibitem[Yang et~al.(2024)]{yang2024dna}\nYang, X., Cheng, W., Petzold, L., Wang, W.~Y., and Chen, H.\n\\newblock DNA-GPT: Divergent n-gram analysis for training-free detection of GPT-generated text.\n\\newblock In \\emph{Proc.\\ ICLR}, 2024.\n\n\\end{thebibliography}\n}\n\n%=============================================================================\n% APPENDIX\n%=============================================================================\n\\appendix\n\\onecolumn\n\n\\section{Prompt-Type Comparison}\n\\label{sec:prompttype}\n\nWe evaluate three prompt types --- continuation, elaboration, and inspired rewriting --- on Pythia-2.8B with 1,000 seeds (Table~\\ref{tab:prompttype}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Prompt Type} & \\textbf{CV F1} & \\textbf{LOPTO F1} & \\textbf{Retention (d4/d0)} \\\\\n\\midrule\nContinuation & 0.781 & 0.762 & 0.831 \\\\\nInspired rewriting & 0.737 & 0.733 & 0.939 \\\\\nElaboration & 0.730 & 0.762 & 0.986 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-prompt-type classification (CV = within-type, LOPTO = leave-one-prompt-type-out). Continuation is strongest (5.1 pp gap) because unconstrained generation maximizes distributional drift. LOPTO average 0.753 confirms cross-prompt-type deployment is viable.}\n\\label{tab:prompttype}\n\\end{table}\n\nDDR is qualitatively consistent across all prompt types: all drifting features show $|\\rho| > 0.55$.\nContinuation produces the strongest signal because it maximizes recursive compression without semantic constraints.\nElaboration is weakest because semantic-preservation constraints limit distributional drift amplitude.\nThe depth retention difference (elaboration 98.6\\% vs.\\ continuation 83.1\\%) reflects that continuation's deeper outputs are more likely to be truncated by minimum-length filters.\n\nFeature drift magnitudes by prompt type:\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Feature} & \\textbf{Cont.\\ $\\rho$} & \\textbf{Elab.\\ $\\rho$} & \\textbf{Rewrite $\\rho$} \\\\\n\\midrule\nHapax ratio & $-0.651$ & $-0.674$ & $-0.670$ \\\\\nTTR & $-0.629$ & $-0.666$ & $-0.659$ \\\\\nEntropy mean & $-0.665$ & $-0.583$ & $-0.564$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Spearman $\\rho$ by feature and prompt type. DDR pattern is preserved across all types.}\n\\end{table}\n\n\n\\section{Paraphrastic vs.\\ Non-Paraphrastic Chains}\n\\label{sec:paraphrastic}\n\nParaphrastic chains (each step paraphrases the previous output) exhibit substantially weaker depth signal than continuation chains (Table~\\ref{tab:para}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Chain Type} & \\textbf{Binary F1} & \\textbf{3-class F1} \\\\\n\\midrule\nContinuation & 0.781 & 0.834 \\\\\nParaphrastic & 0.618 & 0.680 \\\\\n\\midrule\n$\\Delta$ & $-16.3$ pp & $-15.4$ pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Paraphrastic vs.\\ continuation chains. The 16.3 pp binary gap reflects attractor convergence in paraphrastic chains.}\n\\label{tab:para}\n\\end{table}\n\nParaphrastic chains converge by depth $\\sim$3 (depth-3 vs.\\ depth-2 binary F1 = 0.525, near chance), consistent with attractor cycle theory \\citep{briakou2025llm}.\nContinuation chains retain discriminability at deeper depths (depth-3 vs.\\ depth-2 F1 = 0.640).\nSemantic similarity from depth 0 to depth 4 is 0.88 for paraphrastic chains (meaning preserved) vs.\\ 0.52 for continuation (significant topic drift).\nDDR correlations in paraphrastic chains are uniformly weak ($|\\rho| < 0.33$), confirming that DDR is specific to non-paraphrastic generation.\n\n\n\\section{Multi-Domain Evaluation}\n\\label{sec:multidomain}\n\nWe evaluate on four seed domains to test ecological validity (Table~\\ref{tab:domain}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Domain} & \\textbf{Binary F1} & \\textbf{3-class F1} & \\textbf{Hapax $\\rho$} & \\textbf{Ent.\\ mean $\\rho$} \\\\\n\\midrule\nWikipedia & 0.694 & 0.770 & $-0.647$ & $-0.610$ \\\\\nNews & 0.712 & 0.715 & $-0.621$ & $-0.595$ \\\\\nCode & 0.687 & 0.673 & $-0.630$ & $-0.581$ \\\\\nAcademic & 0.628 & 0.656 & $-0.543$ & $-0.520$ \\\\\n\\midrule\nCross-domain & 0.676 & --- & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-domain evaluation. DDR pattern is qualitatively consistent (all drifting $|\\rho| > 0.52$). Academic domain is weakest due to formulaic genre conventions limiting distributional drift.}\n\\label{tab:domain}\n\\end{table}\n\nMaximum domain gap is 8.4 pp (news 0.712 vs.\\ academic 0.628).\nAcademic text is weakest because its highly formulaic genre conventions (strict sentence structures, specialized terminology) limit the distributional drift space, and its low baseline TTR creates a ceiling effect.\nNews text is strongest due to high vocabulary diversity providing larger feature margins.\nAll domains show drifting $|\\rho| > 0.52$, confirming DDR pattern consistency.\n\n\n\\section{Finer-Grained Ordinal Classification}\n\\label{sec:ordinal}\n\nFive-class ordinal classification (gen-0 through gen-4) reveals a practical 3-class resolution ceiling (Table~\\ref{tab:ordinal}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & \\textbf{5-class F1} & \\textbf{3-class F1} \\\\\n\\midrule\nXGBoost & 0.503 & 0.773 \\\\\nCORAL & 0.497 & --- \\\\\nFrank-Hall & 0.501 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{5-class ordinal classification. All methods perform comparably ($<$1 pp spread). 3-class reference included for comparison.}\n\\label{tab:ordinal}\n\\end{table}\n\nPer-class 5-class F1: gen-0 = 0.952, gen-1 = 0.518, gen-2 = 0.348, gen-3 = 0.325, gen-4 = 0.372.\nGen-0 remains highly discriminable (human text); gen-2/3/4 are severely confused (mutual misclassification rate 42\\%).\nThe bottleneck is the gen-1/gen-2 boundary, which concentrates 86\\% of binary errors as false negatives.\nOrdinal methods (CORAL, Frank-Hall) do not improve over standard XGBoost because the ordinal margin between adjacent deeper classes is not uniform --- the gen-0$\\to$gen-1 margin far exceeds gen-2$\\to$gen-3, violating the equal-spacing assumption these methods require.\nThe MAE of 0.72 depth levels indicates predictions are off by less than one class on average.\n\n\n\\section{Human Edit Robustness}\n\\label{sec:edit}\n\nWe test robustness to simulated human editing via random word replacement and LLM-based rephrasing (Table~\\ref{tab:edit}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{Binary F1} & \\textbf{$\\Delta$ (pp)} \\\\\n\\midrule\nBaseline (no edit) & 0.695 & --- \\\\\n5\\% random replacement & 0.650 & $-4.6$ \\\\\n10\\% random replacement & 0.614 & $-8.1$ \\\\\n20\\% random replacement & 0.591 & $-10.4$ \\\\\nLLM rephrase & 0.647 & $-4.5$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Binary F1 under simulated editing. Degradation is graceful: LLM rephrase ($\\sim$50\\% edit distance, $\\sim$1.7 sentences replaced) causes only 4.5 pp drop.}\n\\label{tab:edit}\n\\end{table}\n\nDegradation is graceful rather than catastrophic.\nAt 5\\% random replacement, distributional features (TTR, entropy, hapax) are barely affected because they are global statistics --- sparse point noise does not alter aggregate patterns.\nLLM rephrasing ($\\sim$50\\% edit distance) causes a comparable 4.5 pp drop: rephrasing preserves coherence and topic but alters local word choice, partially disrupting surface features while reference features (NLL-based) remain more robust because rephrased text's NLL retains depth-dependent patterns.\nEven under 20\\% replacement, binary F1 (0.591) substantially exceeds chance (0.50).\nMulticlass degradation is larger ($-7.1$ pp under LLM rephrase) because editing primarily blurs the gen-1/gen-2+ boundary.\n\n\n\\section{LD-Score as Additional Feature}\n\\label{sec:ldscore}\n\nWe evaluate LD-Score (character-level distribution signature) as a potential 8th feature (Table~\\ref{tab:ldscore}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Configuration} & \\textbf{LOGO F1} \\\\\n\\midrule\n7-feature ensemble & 0.798 \\\\\n8-feature (+ LD-Score) & 0.801 \\\\\nLD-Score standalone & 0.721 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Adding LD-Score to the 7-feature ensemble yields only 0.3 pp improvement. LD-Score correlates heavily with surface features (hapax $r = 0.72$, TTR $r = 0.68$).}\n\\label{tab:ldscore}\n\\end{table}\n\nLD-Score alone achieves moderate signal (F1 = 0.721, Spearman $\\rho = 0.794$ with depth), but adding it to the ensemble improves F1 by only 0.3 pp.\nCharacter-level vocabulary diversity is highly co-linear with word-level surface features (hapax $r = 0.72$, TTR $r = 0.68$), providing negligible complementary information.\nWe retain the 7-feature set as the recommended configuration for simplicity, interpretability, and efficiency.\n\n\n\\section{End-to-End Neural Classifier}\n\\label{sec:qlora}\n\nWe compare the 7-feature ensemble against QLoRA-finetuned end-to-end classifiers as an upper-bound reference (Table~\\ref{tab:qlora}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{3-class F1} & \\textbf{Binary F1} & \\textbf{GPU (GB)} \\\\\n\\midrule\nQLoRA (instruct) & 0.897 & 0.852 & 8.2 \\\\\nQLoRA (base) & 0.881 & 0.826 & 8.2 \\\\\n7-feature ensemble & 0.773 & 0.694 & 2.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{QLoRA vs.\\ 7-feature ensemble. QLoRA achieves substantially higher within-distribution F1 but at 3.4$\\times$ GPU memory and 6.5$\\times$ inference time.}\n\\label{tab:qlora}\n\\end{table}\n\nQLoRA achieves 12--16 pp higher within-distribution F1 by learning contextual, positional, and discourse-level patterns beyond our handcrafted features.\nHowever, QLoRA's cross-generator generalization (LOGO binary 0.720) is substantially below its within-distribution performance (0.826--0.852), indicating partial overfitting to generator-specific token patterns.\nThe 7-feature ensemble's advantages are: (a) 3.4$\\times$ less GPU memory, (b) 6.5$\\times$ faster inference, (c) interpretable features with clear DDR semantics, (d) more stable cross-generator generalization.\nNotably, QLoRA's 5-class F1 (0.551) only exceeds the handcrafted baseline (0.503) by $\\sim$5 pp, confirming that finer classification is bottlenecked by task-inherent difficulty.\n\n\n\\section{Text Length Confound Control}\n\\label{sec:length}\n\nWe verify that depth signal is not an artifact of text length variation (Table~\\ref{tab:length}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{Binary F1} & \\textbf{$\\Delta$ (pp)} \\\\\n\\midrule\nUnmatched & 0.770 & --- \\\\\nRandom subsample (equal $n$) & 0.741 & $-2.9$ \\\\\nLength-matched & 0.724 & $-4.6$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Length confound analysis. Of the 4.6 pp drop from length matching, 2.9 pp is attributable to sample-size reduction and only 1.7 pp to deconfounding.}\n\\label{tab:length}\n\\end{table}\n\nLength--depth Spearman $\\rho$ is weak ($[-0.066, +0.134]$): text length does not systematically vary with depth.\nOf the 4.6 pp drop from length matching, 2.9 pp is attributable to sample-size reduction (random subsample control) and only 1.7 pp to actual deconfounding.\nLength-normalized surface features (computed over fixed-length windows) \\emph{strengthen} the depth trend ($|\\rho|$ increases), confirming that DDR arises from intrinsic vocabulary diversity decrease rather than length variation.\n\n\n\\section{Large-Scale Generator}\n\\label{sec:scale}\n\nWe add Qwen3-8B-Base to test scale effects (Table~\\ref{tab:scale}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Generator} & \\textbf{Binary F1} & \\textbf{Hapax $\\rho$} & \\textbf{Tail decay $\\rho$} \\\\\n\\midrule\n$<$3B average & 0.700 & $-0.647$ & $-0.040$ \\\\\nQwen3-8B & 0.683 & $-0.558$ & $-0.089$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Scale effect: 8B generator shows moderate degradation ($-1.7$ pp binary F1) with attenuated drifting $|\\rho|$ ($\\sim$85\\% of $<$3B average). DDR pattern (drifting vs.\\ stationary split) is qualitatively preserved.}\n\\label{tab:scale}\n\\end{table}\n\nQwen3-8B binary F1 = 0.683 (95\\% CI [0.660, 0.706]), a moderate 1.7 pp drop from the $<$3B average.\nDrifting features retain $\\sim$85\\% of their correlation magnitude (hapax $\\rho = -0.558$ vs.\\ $-0.647$).\nThe DDR pattern is qualitatively preserved: the three drifting features remain highest-$|\\rho|$ (hapax $-0.558$, TTR $-0.542$, entropy mean $-0.475$), while stationary features remain low ($|\\rho| < 0.10$).\nHigher-capacity models produce more concentrated generation distributions with lower baseline vocabulary diversity, compressing depth-wise feature margins.\n$N = 4{,}497$ total records with depth-dependent dropout (d4: 755/995 seeds) more pronounced than for smaller models.\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "317a2ae9-9d3c-4cfe-aba4-12af57fe47b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "7a6e7dae-2371-44f2-a86f-776f12713121",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 20 · 2026-05-21T00:03:04.525Z_

```json
{
  "parentUuid": "fed85f04-429e-4f52-bb4c-004d23838629",
  "isSidechain": false,
  "attachment": {
    "type": "date_change",
    "newDate": "2026-05-21"
  },
  "type": "attachment",
  "uuid": "7bd290c7-6bcb-4f6a-bffc-a5825bf1b88b",
  "timestamp": "2026-05-21T00:03:04.525Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "7a6e7dae-2371-44f2-a86f-776f12713121",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T232427 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerpr…",
  "leafUuid": "7bd290c7-6bcb-4f6a-bffc-a5825bf1b88b",
  "sessionId": "7a6e7dae-2371-44f2-a86f-776f12713121"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete research paper from experimental data",
  "sessionId": "7a6e7dae-2371-44f2-a86f-776f12713121"
}
```

---

### Tool call

_source line 23 · 2026-05-21T00:03:08.153Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01FqxwjrV1PHHW6dwNzaiYbf`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T232427/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bd290c7-6bcb-4f6a-bffc-a5825bf1b88b",
  "isSidechain": false,
  "requestId": "req_011CbEjXx5RzgEUugrrs91ym",
  "type": "assistant",
  "uuid": "99c125c8-8a82-44fc-969d-b43e6be6a4e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "7a6e7dae-2371-44f2-a86f-776f12713121",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019QPuc3KNovdrjU91TGC7hr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13307,
      "cache_read_input_tokens": 46879,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13307,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 46879,
          "cache_creation_input_tokens": 13307,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13307
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

_source line 24 · 2026-05-21T00:03:09.125Z_

<details><summary>↩ Tool result · `toolu_01FqxwjrV1PHHW6dwNzaiYbf`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
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
Underfull \hbox (badness 1189) in paragraph at lines 33--44
\T1/ptm/m/n/10.95 dif-fer-ent ma-te-rial: first-generation text re-tains

Underfull \hbox (badness 1648) in paragraph at lines 33--44
\T1/ptm/m/n/10.95 model gen-er-a-tors from 5 fam-i-lies (0.6B--8B):

Package natbib Warning: Citation `liang2024monitoring' on page 1 undefined on i
nput line 51.


Package natbib Warning: Citation `shumailov2024model' on page 1 undefined on in
put line 52.


Underfull \hbox (badness 2173) in paragraph at lines 63--66
\T1/ptm/m/n/10.95 Qwen, Llama, Mis-tral; 0.6B--8B pa-ram-e-ters)
[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]
Underfull \hbox (badness 1466) in paragraph at lines 70--71
\T1/ptm/m/n/10.95 sig-nal de-grades sub-stan-tially un-der in-struc-tion

Package natbib Warning: Citation `gehrmann2019gltr' on page 2 undefined on inpu
t line 79.


Package natbib Warning: Citation `mitchell2023detectgpt' on page 2 undefined on
 input line 80.


Package natbib Warning: Citation `bao2024fast' on page 2 undefined on input lin
e 80.


Package natbib Warning: Citation `hans2024spotting' on page 2 undefined on inpu
t line 81.


Package natbib Warning: Citation `yang2024dna' on page 2 undefined on input lin
e 82.


Underfull \hbox (badness 2426) in paragraph at lines 78--84
 []\T1/ptm/b/n/10.95 AI text de-tec-tion.[] \T1/ptm/m/n/10.95 Perplexity-based 
meth-ods

Underfull \hbox (badness 1082) in paragraph at lines 78--84
\T1/ptm/m/n/10.95 vari-ant Fast-DetectGPT (\T1/ptm/b/n/10.95 ?\T1/ptm/m/n/10.95
 ) use perturbation-

Package natbib Warning: Citation `shumailov2024model' on page 2 undefined on in
put line 86.


Package natbib Warning: Citation `dohmatob2024tale' on page 2 undefined on inpu
t line 87.


Package natbib Warning: Citation `briakou2025llm' on page 2 undefined on input 
line 88.


Package natbib Warning: Citation `mccarthy2010mtld' on page 2 undefined on inpu
t line 92.


Package natbib Warning: Citation `tulchinskii2024intrinsic' on page 2 undefined
 on input line 93.


Package natbib Warning: Citation `wenzek2020ccnet' on page 2 undefined on input
 line 94.


Package natbib Warning: Citation `neal2017surveying' on page 2 undefined on inp
ut line 98.

(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)
Underfull \hbox (badness 7064) in paragraph at lines 135--136
 []\T1/ptm/b/n/10.95 Reference fea-tures[] \T1/ptm/m/n/10.95 (com-puted from $\
OML/cmm/m/it/10.95 M[]$\T1/ptm/m/n/10.95 's
[2]

LaTeX Warning: Reference `sec:multidomain' on page 3 undefined on input line 17
2.


LaTeX Warning: Reference `sec:crossref' on page 3 undefined on input line 174.


Underfull \hbox (badness 10000) in paragraph at lines 174--175
 []\T1/ptm/b/n/10.95 Reference model.[] \T1/ptm/m/n/10.95 Pythia-410M (de-fault
).

Underfull \hbox (badness 10000) in paragraph at lines 174--175
\T1/ptm/m/n/10.95 Cross-reference ro-bust-ness eval-u-ated with

LaTeX Warning: Reference `tab:ablation' on page 3 undefined on input line 179.


LaTeX Warning: Reference `tab:trends' on page 3 undefined on input line 201.


LaTeX Warning: Reference `tab:crossgen' on page 3 undefined on input line 229.

[3]
Underfull \hbox (badness 1303) in paragraph at lines 251--254
\T1/ptm/m/n/10.95 tion. Per-generator vari-ance is 5.4 pp, with

LaTeX Warning: Reference `tab:crossref' on page 4 undefined on input line 262.


Underfull \hbox (badness 1205) in paragraph at lines 282--286
\T1/ptm/m/n/10.95 ref-er-ence mod-els. En-tropy mean drift di-rec-

LaTeX Warning: Reference `tab:baseline' on page 4 undefined on input line 290.


LaTeX Warning: Reference `tab:crossmodel' on page 4 undefined on input line 320
.

[4]

LaTeX Warning: Reference `tab:downstream' on page 5 undefined on input line 345
.


Overfull \hbox (0.5529pt too wide) in paragraph at lines 350--361
 [][] 

LaTeX Warning: Reference `sec:scale' on page 5 undefined on input line 391.


LaTeX Warning: Reference `sec:ordinal' on page 5 undefined on input line 392.


LaTeX Warning: Reference `sec:prompttype' on page 5 undefined on input line 393
.


Underfull \hbox (badness 5622) in paragraph at lines 393--394
[]\T1/ptm/b/n/10.95 Prompt-type de-pen-dence. \T1/ptm/m/n/10.95 Con-tin-u-a-tio
n

Underfull \hbox (badness 1331) in paragraph at lines 402--407
\T1/ptm/m/n/10.95 across 8 base-model gen-er-a-tors from 5 fam-i-

Underfull \vbox (badness 3668) has occurred while \output is active [5]
Underfull \hbox (badness 1377) in paragraph at lines 451--454
\T1/ptm/m/n/10 and Finn, C.  De-tect-GPT: Zero-shot machine-
[6]

LaTeX Warning: Reference `tab:prompttype' on page 7 undefined on input line 492
.


LaTeX Warning: Reference `tab:para' on page 7 undefined on input line 536.


Package natbib Warning: Citation `briakou2025llm' on page 7 undefined on input 
line 555.


LaTeX Warning: Reference `tab:domain' on page 7 undefined on input line 564.


LaTeX Warning: `h' float specifier changed to `ht'.

[7]

LaTeX Warning: Reference `tab:ordinal' on page 8 undefined on input line 594.


LaTeX Warning: Reference `tab:edit' on page 8 undefined on input line 622.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:ldscore' on page 8 undefined on input line 652.

[8]

LaTeX Warning: Reference `tab:qlora' on page 9 undefined on input line 678.


LaTeX Warning: Reference `tab:length' on page 9 undefined on input line 705.

[9]

LaTeX Warning: Reference `tab:scale' on page 10 undefined on input line 731.


Package natbib Warning: There were undefined citations.

[10] (./paper.aux

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
msy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/
texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (10 pages, 156305 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
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
Underfull \hbox (badness 1189) in paragraph at lines 33--44
\T1/ptm/m/n/10.95 dif-fer-ent ma-te-rial: first-generation text re-tains

Underfull \hbox (badness 1648) in paragraph at lines 33--44
\T1/ptm/m/n/10.95 model gen-er-a-tors from 5 fam-i-lies (0.6B--8B):

Underfull \hbox (badness 2173) in paragraph at lines 63--66
\T1/ptm/m/n/10.95 Qwen, Llama, Mis-tral; 0.6B--8B pa-ram-e-ters)
[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]
Underfull \hbox (badness 1466) in paragraph at lines 70--71
\T1/ptm/m/n/10.95 sig-nal de-grades sub-stan-tially un-der in-struc-tion

Underfull \hbox (badness 2426) in paragraph at lines 78--84
 []\T1/ptm/b/n/10.95 AI text de-tec-tion.[] \T1/ptm/m/n/10.95 Perplexity-based 
meth-ods

Underfull \hbox (badness 3199) in paragraph at lines 78--84
\T1/ptm/m/n/10.95 man and ma-chine text. GLTR [[]Gehrmann
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)
Underfull \hbox (badness 7064) in paragraph at lines 135--136
 []\T1/ptm/b/n/10.95 Reference fea-tures[] \T1/ptm/m/n/10.95 (com-puted from $\
OML/cmm/m/it/10.95 M[]$\T1/ptm/m/n/10.95 's
[2]
Underfull \hbox (badness 10000) in paragraph at lines 174--175
 []\T1/ptm/b/n/10.95 Reference model.[] \T1/ptm/m/n/10.95 Pythia-410M (de-fault
).

Underfull \hbox (badness 10000) in paragraph at lines 174--175
\T1/ptm/m/n/10.95 Cross-reference ro-bust-ness eval-u-ated with
[3]
Underfull \hbox (badness 1303) in paragraph at lines 251--254
\T1/ptm/m/n/10.95 tion. Per-generator vari-ance is 5.4 pp, with

Underfull \hbox (badness 1205) in paragraph at lines 282--286
\T1/ptm/m/n/10.95 ref-er-ence mod-els. En-tropy mean drift di-rec-
[4]
Overfull \hbox (0.5529pt too wide) in paragraph at lines 350--361
 [][] 

Underfull \hbox (badness 5622) in paragraph at lines 393--394
[]\T1/ptm/b/n/10.95 Prompt-type de-pen-dence. \T1/ptm/m/n/10.95 Con-tin-u-a-tio
n

Underfull \hbox (badness 1331) in paragraph at lines 402--407
\T1/ptm/m/n/10.95 across 8 base-model gen-er-a-tors from 5 fam-i-

Underfull \vbox (badness 3668) has occurred while \output is active [5]
Underfull \hbox (badness 1377) in paragraph at lines 451--454
\T1/ptm/m/n/10 and Finn, C.  De-tect-GPT: Zero-shot machine-
[6]

LaTeX Warning: `h' float specifier changed to `ht'.

[7]

LaTeX Warning: `h' float specifier changed to `ht'.

[8] [9] [10] (./paper.aux) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ
ic/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
msy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/
texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (10 pages, 160584 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99c125c8-8a82-44fc-969d-b43e6be6a4e0",
  "isSidechain": false,
  "promptId": "1ca86b45-b190-47c7-9689-3b48717c505c",
  "type": "user",
  "uuid": "e983f566-09b6-45d9-9c01-a4a8cf5c68b5",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\nUnderfull \\hbox (badness 1189) in paragraph at lines 33--44\n\\T1/ptm/m/n/10.95 dif-fer-ent ma-te-rial: first-generation text re-tains\n\nUnderfull \\hbox (badness 1648) in paragraph at lines 33--44\n\\T1/ptm/m/n/10.95 model gen-er-a-tors from 5 fam-i-lies (0.6B--8B):\n\nPackage natbib Warning: Citation `liang2024monitoring' on page 1 undefined on i\nnput line 51.\n\n\nPackage natbib Warning: Citation `shumailov2024model' on page 1 undefined on in\nput line 52.\n\n\nUnderfull \\hbox (badness 2173) in paragraph at lines 63--66\n\\T1/ptm/m/n/10.95 Qwen, Llama, Mis-tral; 0.6B--8B pa-ram-e-ters)\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\nUnderfull \\hbox (badness 1466) in paragraph at lines 70--71\n\\T1/ptm/m/n/10.95 sig-nal de-grades sub-stan-tially un-der in-struc-tion\n\nPackage natbib Warning: Citation `gehrmann2019gltr' on page 2 undefined on inpu\nt line 79.\n\n\nPackage natbib Warning: Citation `mitchell2023detectgpt' on page 2 undefined on\n input line 80.\n\n\nPackage natbib Warning: Citation `bao2024fast' on page 2 undefined on input lin\ne 80.\n\n\nPackage natbib Warning: Citation `hans2024spotting' on page 2 undefined on inpu\nt line 81.\n\n\nPackage natbib Warning: Citation `yang2024dna' on page 2 undefined on input lin\ne 82.\n\n\nUnderfull \\hbox (badness 2426) in paragraph at lines 78--84\n []\\T1/ptm/b/n/10.95 AI text de-tec-tion.[] \\T1/ptm/m/n/10.95 Perplexity-based \nmeth-ods\n\nUnderfull \\hbox (badness 1082) in paragraph at lines 78--84\n\\T1/ptm/m/n/10.95 vari-ant Fast-DetectGPT (\\T1/ptm/b/n/10.95 ?\\T1/ptm/m/n/10.95\n ) use perturbation-\n\nPackage natbib Warning: Citation `shumailov2024model' on page 2 undefined on in\nput line 86.\n\n\nPackage natbib Warning: Citation `dohmatob2024tale' on page 2 undefined on inpu\nt line 87.\n\n\nPackage natbib Warning: Citation `briakou2025llm' on page 2 undefined on input \nline 88.\n\n\nPackage natbib Warning: Citation `mccarthy2010mtld' on page 2 undefined on inpu\nt line 92.\n\n\nPackage natbib Warning: Citation `tulchinskii2024intrinsic' on page 2 undefined\n on input line 93.\n\n\nPackage natbib Warning: Citation `wenzek2020ccnet' on page 2 undefined on input\n line 94.\n\n\nPackage natbib Warning: Citation `neal2017surveying' on page 2 undefined on inp\nut line 98.\n\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)\nUnderfull \\hbox (badness 7064) in paragraph at lines 135--136\n []\\T1/ptm/b/n/10.95 Reference fea-tures[] \\T1/ptm/m/n/10.95 (com-puted from $\\\nOML/cmm/m/it/10.95 M[]$\\T1/ptm/m/n/10.95 's\n[2]\n\nLaTeX Warning: Reference `sec:multidomain' on page 3 undefined on input line 17\n2.\n\n\nLaTeX Warning: Reference `sec:crossref' on page 3 undefined on input line 174.\n\n\nUnderfull \\hbox (badness 10000) in paragraph at lines 174--175\n []\\T1/ptm/b/n/10.95 Reference model.[] \\T1/ptm/m/n/10.95 Pythia-410M (de-fault\n).\n\nUnderfull \\hbox (badness 10000) in paragraph at lines 174--175\n\\T1/ptm/m/n/10.95 Cross-reference ro-bust-ness eval-u-ated with\n\nLaTeX Warning: Reference `tab:ablation' on page 3 undefined on input line 179.\n\n\nLaTeX Warning: Reference `tab:trends' on page 3 undefined on input line 201.\n\n\nLaTeX Warning: Reference `tab:crossgen' on page 3 undefined on input line 229.\n\n[3]\nUnderfull \\hbox (badness 1303) in paragraph at lines 251--254\n\\T1/ptm/m/n/10.95 tion. Per-generator vari-ance is 5.4 pp, with\n\nLaTeX Warning: Reference `tab:crossref' on page 4 undefined on input line 262.\n\n\nUnderfull \\hbox (badness 1205) in paragraph at lines 282--286\n\\T1/ptm/m/n/10.95 ref-er-ence mod-els. En-tropy mean drift di-rec-\n\nLaTeX Warning: Reference `tab:baseline' on page 4 undefined on input line 290.\n\n\nLaTeX Warning: Reference `tab:crossmodel' on page 4 undefined on input line 320\n.\n\n[4]\n\nLaTeX Warning: Reference `tab:downstream' on page 5 undefined on input line 345\n.\n\n\nOverfull \\hbox (0.5529pt too wide) in paragraph at lines 350--361\n [][] \n\nLaTeX Warning: Reference `sec:scale' on page 5 undefined on input line 391.\n\n\nLaTeX Warning: Reference `sec:ordinal' on page 5 undefined on input line 392.\n\n\nLaTeX Warning: Reference `sec:prompttype' on page 5 undefined on input line 393\n.\n\n\nUnderfull \\hbox (badness 5622) in paragraph at lines 393--394\n[]\\T1/ptm/b/n/10.95 Prompt-type de-pen-dence. \\T1/ptm/m/n/10.95 Con-tin-u-a-tio\nn\n\nUnderfull \\hbox (badness 1331) in paragraph at lines 402--407\n\\T1/ptm/m/n/10.95 across 8 base-model gen-er-a-tors from 5 fam-i-\n\nUnderfull \\vbox (badness 3668) has occurred while \\output is active [5]\nUnderfull \\hbox (badness 1377) in paragraph at lines 451--454\n\\T1/ptm/m/n/10 and Finn, C.  De-tect-GPT: Zero-shot machine-\n[6]\n\nLaTeX Warning: Reference `tab:prompttype' on page 7 undefined on input line 492\n.\n\n\nLaTeX Warning: Reference `tab:para' on page 7 undefined on input line 536.\n\n\nPackage natbib Warning: Citation `briakou2025llm' on page 7 undefined on input \nline 555.\n\n\nLaTeX Warning: Reference `tab:domain' on page 7 undefined on input line 564.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[7]\n\nLaTeX Warning: Reference `tab:ordinal' on page 8 undefined on input line 594.\n\n\nLaTeX Warning: Reference `tab:edit' on page 8 undefined on input line 622.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:ldscore' on page 8 undefined on input line 652.\n\n[8]\n\nLaTeX Warning: Reference `tab:qlora' on page 9 undefined on input line 678.\n\n\nLaTeX Warning: Reference `tab:length' on page 9 undefined on input line 705.\n\n[9]\n\nLaTeX Warning: Reference `tab:scale' on page 10 undefined on input line 731.\n\n\nPackage natbib Warning: There were undefined citations.\n\n[10] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\nic/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/\ntexlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (10 pages, 156305 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\nUnderfull \\hbox (badness 1189) in paragraph at lines 33--44\n\\T1/ptm/m/n/10.95 dif-fer-ent ma-te-rial: first-generation text re-tains\n\nUnderfull \\hbox (badness 1648) in paragraph at lines 33--44\n\\T1/ptm/m/n/10.95 model gen-er-a-tors from 5 fam-i-lies (0.6B--8B):\n\nUnderfull \\hbox (badness 2173) in paragraph at lines 63--66\n\\T1/ptm/m/n/10.95 Qwen, Llama, Mis-tral; 0.6B--8B pa-ram-e-ters)\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\nUnderfull \\hbox (badness 1466) in paragraph at lines 70--71\n\\T1/ptm/m/n/10.95 sig-nal de-grades sub-stan-tially un-der in-struc-tion\n\nUnderfull \\hbox (badness 2426) in paragraph at lines 78--84\n []\\T1/ptm/b/n/10.95 AI text de-tec-tion.[] \\T1/ptm/m/n/10.95 Perplexity-based \nmeth-ods\n\nUnderfull \\hbox (badness 3199) in paragraph at lines 78--84\n\\T1/ptm/m/n/10.95 man and ma-chine text. GLTR [[]Gehrmann\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)\nUnderfull \\hbox (badness 7064) in paragraph at lines 135--136\n []\\T1/ptm/b/n/10.95 Reference fea-tures[] \\T1/ptm/m/n/10.95 (com-puted from $\\\nOML/cmm/m/it/10.95 M[]$\\T1/ptm/m/n/10.95 's\n[2]\nUnderfull \\hbox (badness 10000) in paragraph at lines 174--175\n []\\T1/ptm/b/n/10.95 Reference model.[] \\T1/ptm/m/n/10.95 Pythia-410M (de-fault\n).\n\nUnderfull \\hbox (badness 10000) in paragraph at lines 174--175\n\\T1/ptm/m/n/10.95 Cross-reference ro-bust-ness eval-u-ated with\n[3]\nUnderfull \\hbox (badness 1303) in paragraph at lines 251--254\n\\T1/ptm/m/n/10.95 tion. Per-generator vari-ance is 5.4 pp, with\n\nUnderfull \\hbox (badness 1205) in paragraph at lines 282--286\n\\T1/ptm/m/n/10.95 ref-er-ence mod-els. En-tropy mean drift di-rec-\n[4]\nOverfull \\hbox (0.5529pt too wide) in paragraph at lines 350--361\n [][] \n\nUnderfull \\hbox (badness 5622) in paragraph at lines 393--394\n[]\\T1/ptm/b/n/10.95 Prompt-type de-pen-dence. \\T1/ptm/m/n/10.95 Con-tin-u-a-tio\nn\n\nUnderfull \\hbox (badness 1331) in paragraph at lines 402--407\n\\T1/ptm/m/n/10.95 across 8 base-model gen-er-a-tors from 5 fam-i-\n\nUnderfull \\vbox (badness 3668) has occurred while \\output is active [5]\nUnderfull \\hbox (badness 1377) in paragraph at lines 451--454\n\\T1/ptm/m/n/10 and Finn, C.  De-tect-GPT: Zero-shot machine-\n[6]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[7]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[8] [9] [10] (./paper.aux) )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\nic/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/\ntexlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (10 pages, 160584 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "99c125c8-8a82-44fc-969d-b43e6be6a4e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T232427/best",
  "sessionId": "7a6e7dae-2371-44f2-a86f-776f12713121",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T232427 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerpr…",
  "leafUuid": "e983f566-09b6-45d9-9c01-a4a8cf5c68b5",
  "sessionId": "7a6e7dae-2371-44f2-a86f-776f12713121"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete research paper from experimental data",
  "sessionId": "7a6e7dae-2371-44f2-a86f-776f12713121"
}
```

---

### Assistant

_source line 27 · 2026-05-21T00:03:18.595Z_

编译成功，10 页 PDF（主体 6 页 + 附录 4 页），无 error。

论文覆盖了 `experiment_data.json` 中全部 15 个实验：
- **主体** (§4): feature ablation/trend, cross-generator (5-gen LOGO), cross-reference-model, baseline comparison, cross-model chains, downstream utility
- **附录** (§A--I): prompt-type comparison, paraphrastic chains, multi-domain seeds, 5-class ordinal, human edit robustness, LD-Score, QLoRA end-to-end, text length confound, large-scale generator (8B)

所有定量 claim 均取自实验数据，未编造数字。PDF 位于 `artifacts/dream_reports/dream_20260520T232427/best/paper.pdf`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e983f566-09b6-45d9-9c01-a4a8cf5c68b5",
  "isSidechain": false,
  "requestId": "req_011CbEjYHkMterCPU4HPqtdh",
  "type": "assistant",
  "uuid": "1058ef9c-2ce8-4ae4-bf69-6bcc734cfd2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T232427/best",
  "sessionId": "7a6e7dae-2371-44f2-a86f-776f12713121",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nh1gNQ8EkKbii9V6623SqV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8415,
      "cache_read_input_tokens": 60186,
      "output_tokens": 221,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8415,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 221,
          "cache_read_input_tokens": 60186,
          "cache_creation_input_tokens": 8415,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8415
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T232427 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerpr…",
  "leafUuid": "1058ef9c-2ce8-4ae4-bf69-6bcc734cfd2a",
  "sessionId": "7a6e7dae-2371-44f2-a86f-776f12713121"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete research paper from experimental data",
  "sessionId": "7a6e7dae-2371-44f2-a86f-776f12713121"
}
```

---
