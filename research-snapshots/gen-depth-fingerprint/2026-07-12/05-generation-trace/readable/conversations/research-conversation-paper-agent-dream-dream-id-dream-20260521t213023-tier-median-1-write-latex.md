# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T213023 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 42
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-1/5c93f0c9-f7c6-404f-b838-8e17599d97ba.jsonl`
- **Structured JSON:** [`3878ac595683357e5984.json`](../../sessions/38/3878ac595683357e5984.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T22:07:49.924Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T22:07:49.924Z",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T213023 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median/experiment_data.json`（先 Read 此文件）\n- Venue：emnlp-2026\n- Narrative guidance：Decoding-agnostic DDR（greedy mean |d|=0.05, top-k 5/8 full preservation）被 reviewer 认可为有价值的 robustness check，将 Claim 2 从纯 DDR 现象观察升级为包含 decoding-robustness 的 dual contribution——但 仅 greedy + top-k 两种策略不足以 claim \"decoding-agnostic property\"，reviewer 要求至少补 nucleus sampling 或 beam search。Claim 2 措辞从 \"decoding-agnostic DDR\" 软化为 \"DDR robust across tested decoding strategies (greedy, top-k)\"，保留 hedging 空间。0.694 binary F1 被定位为 \"first baseline for a novel task\" 而非 practical tool，reviewer 认可 task formulation 贡献但质疑 practical utility。Base-model-only scope 被至少一位 reviewer 标记为 major concern（\"in practice people use instruct models\"），需在 rebuttal 中 强调 intentional contribution boundary + instruct 退化本身是 finding（OLMo-Instruct LOGO 0.338 vs 0.763 base）。 Claim 3 negative finding 最稳固但 3 seeds + single perplexity metric 被认为 evidence 有限。 72h 写作修复完成约 75-80%：核心 Results/Method 到位，但 Related Work 的 OOD detection 和 model collapse 文献 覆盖不完整，Appendix 可视化粗糙。Overall 3.0-3.5，Findings borderline accept。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T22:07:49.927Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T22:07:49.927Z",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba"
}
```

---

## Round 1

40 recorded events

### User

_source line 3 · 2026-05-21T22:07:49.944Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T213023 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median/experiment_data.json`（先 Read 此文件）
- Venue：emnlp-2026
- Narrative guidance：Decoding-agnostic DDR（greedy mean |d|=0.05, top-k 5/8 full preservation）被 reviewer 认可为有价值的 robustness check，将 Claim 2 从纯 DDR 现象观察升级为包含 decoding-robustness 的 dual contribution——但 仅 greedy + top-k 两种策略不足以 claim "decoding-agnostic property"，reviewer 要求至少补 nucleus sampling 或 beam search。Claim 2 措辞从 "decoding-agnostic DDR" 软化为 "DDR robust across tested decoding strategies (greedy, top-k)"，保留 hedging 空间。0.694 binary F1 被定位为 "first baseline for a novel task" 而非 practical tool，reviewer 认可 task formulation 贡献但质疑 practical utility。Base-model-only scope 被至少一位 reviewer 标记为 major concern（"in practice people use instruct models"），需在 rebuttal 中 强调 intentional contribution boundary + instruct 退化本身是 finding（OLMo-Instruct LOGO 0.338 vs 0.763 base）。 Claim 3 negative finding 最稳固但 3 seeds + single perplexity metric 被认为 evidence 有限。 72h 写作修复完成约 75-80%：核心 Results/Method 到位，但 Related Work 的 OOD detection 和 model collapse 文献 覆盖不完整，Appendix 可视化粗糙。Overall 3.0-3.5，Findings borderline accept。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "a05c3ff7-21d6-48e6-b124-f66048f4fb96",
  "type": "user",
  "uuid": "03bc00c7-7cec-4670-a90a-85403152db5a",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T22:07:49.944Z_

```json
{
  "parentUuid": "03bc00c7-7cec-4670-a90a-85403152db5a",
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
  "uuid": "03da8da8-c085-4eab-ab41-c87391ab3498",
  "timestamp": "2026-05-21T22:07:49.944Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T22:07:49.944Z_

```json
{
  "parentUuid": "03da8da8-c085-4eab-ab41-c87391ab3498",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "65883db6-5329-4362-ac09-80e38d520bdc",
  "timestamp": "2026-05-21T22:07:49.944Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba",
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
  "aiTitle": "Generate complete simulated research paper",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba"
}
```

---

### Assistant

_source line 7 · 2026-05-21T22:07:52.591Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65883db6-5329-4362-ac09-80e38d520bdc",
  "isSidechain": false,
  "requestId": "req_011CbGUZAUMBmQ6UenGw8CHs",
  "type": "assistant",
  "uuid": "87162d3f-18f2-4ac7-8f67-93b5019d022d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Si6S4ZY7y8xD8SzLYtogvs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13723,
      "cache_read_input_tokens": 11841,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13723,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 206,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13723,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13723
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

_source line 8 · 2026-05-21T22:07:53.554Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AhZsxebUU4H4MJmbGZpMLD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87162d3f-18f2-4ac7-8f67-93b5019d022d",
  "isSidechain": false,
  "requestId": "req_011CbGUZAUMBmQ6UenGw8CHs",
  "type": "assistant",
  "uuid": "6ff6621e-ac49-49ba-bd87-6307753687f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Si6S4ZY7y8xD8SzLYtogvs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13723,
      "cache_read_input_tokens": 11841,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13723,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 206,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13723,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13723
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

_source line 9 · 2026-05-21T22:07:53.810Z_

<details open><summary>🔧 Tool call — Read · `toolu_01C4dFkvoCzAxNVGS3S9cipk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ff6621e-ac49-49ba-bd87-6307753687f1",
  "isSidechain": false,
  "requestId": "req_011CbGUZAUMBmQ6UenGw8CHs",
  "type": "assistant",
  "uuid": "ea9cda68-144f-4223-bccc-fc838d251533",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Si6S4ZY7y8xD8SzLYtogvs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13723,
      "cache_read_input_tokens": 11841,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13723,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 206,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13723,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13723
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

_source line 10 · 2026-05-21T22:07:53.838Z_

<details><summary>↩ Tool result · `toolu_01AhZsxebUU4H4MJmbGZpMLD`</summary>

```text
1	[
2	  {
3	    "name": "feature_ablation_and_trend",
4	    "description": "三部分分析：(A) Feature ablation: full vs surface-only vs reference-only, (B) DDR trend analysis per feature (Spearman ρ, KS statistics), (C) Perplexity pre-validation for Claim 3.\n",
5	    "results": {
6	      "full_macro_f1": 0.82,
7	      "full_macro_ci": "[0.807, 0.833]",
8	      "surface_only_f1": 0.763,
9	      "surface_only_ci": "[0.747, 0.774]",
10	      "reference_only_f1": 0.719,
11	      "reference_only_ci": "[0.706, 0.733]",
12	      "mcnemar_full_vs_surface_p": 0.0,
13	      "mcnemar_full_vs_reference_p": 0.0,
14	      "hapax_ratio_rho": -0.63,
15	      "ttr_rho": -0.61,
16	      "entropy_mean_rho": -0.6,
17	      "entropy_std_rho": -0.12,
18	      "entropy_min_rho": -0.35,
19	      "entropy_max_rho": 0.06,
20	      "tail_decay_rho": 0.04,
21	      "ks_drifting_range": "[0.516, 0.537]",
22	      "ks_stationary_range": "[0.043, 0.052]",
23	      "ks_gap_ratio": "~10x",
24	      "median_ppl_by_depth": "13.50, 4.96, 3.00, 2.07, 1.72"
25	    },
26	    "tables": [
27	      {
28	        "name": "Table: Feature Ablation (5-fold CV, Pythia-2.8B single generator)",
29	        "columns": [
30	          "Feature Set",
31	          "Macro F1",
32	          "95% CI"
33	        ],
34	        "rows": [
35	          [
36	            "Full (7 features)",
37	            0.82,
38	            "[0.807, 0.833]"
39	          ],
40	          [
41	            "Surface-only (TTR + hapax)",
42	            0.763,
43	            "[0.747, 0.774]"
44	          ],
45	          [
46	            "Reference-only (5 entropy + tail_decay)",
47	            0.719,
48	            "[0.706, 0.733]"
49	          ]
50	        ]
51	      },
52	      {
53	        "name": "Table: DDR Feature Classification",
54	        "columns": [
55	          "Feature",
56	          "Spearman ρ",
57	          "KS Statistic",
58	          "DDR Group"
59	        ],
60	        "rows": [
61	          [
62	            "hapax_ratio",
63	            -0.63,
64	            0.537,
65	            "drifting"
66	          ],
67	          [
68	            "TTR",
69	            -0.61,
70	            0.516,
71	            "drifting"
72	          ],
73	          [
74	            "entropy_mean",
75	            -0.6,
76	            0.528,
77	            "drifting"
78	          ],
79	          [
80	            "entropy_min",
81	            -0.35,
82	            0.052,
83	            "moderate"
84	          ],
85	          [
86	            "entropy_std",
87	            -0.12,
88	            0.043,
89	            "moderate"
90	          ],
91	          [
92	            "entropy_max",
93	            0.06,
94	            0.048,
95	            "near-stationary"
96	          ],
97	          [
98	            "tail_decay",
99	            0.04,
100	            0.045,
101	            "near-stationary"
102	          ]
103	        ]
104	      }
105	    ],
106	    "figures": [],
107	    "analysis": "McNemar 确认 full > surface > reference，互补性成立。Surface 主导（+4.4pp over reference） 意味着 reviewer 可能评价 reference features 的 marginal contribution 有限——这是 median 档的 核心张力：DDR 作为概念有价值（drifting vs stationary 的 10x KS gap），但 practical 层面 surface features 已捕获大部分信号。论文 Claim 2 需聚焦 DDR 的 interpretability 和 diagnostic 价值而非 classification performance 增益。\n\n\nMedian 档下 surface features（hapax -0.63, TTR -0.61）仍是最强 drift 信号源，surface-only 达到 0.763，高于 reference-only 约 4.4pp。这意味着 vocabulary impoverishment 是 depth signal 的主导机制。但 full 超过 surface +5.7pp（McNemar p≈0）确认 reference features 提供独立互补信号—— entropy_mean 的 |ρ|=0.60 处于 drifting/moderate 边界，在 median 档的 reviewer 看来足以支撑 \"complementary\" 但不足以 claim \"independent dual dynamics\"。DDR 呈现三梯度结构：strong drift (hapax, TTR, entropy_mean 的 |ρ|>0.60) vs moderate drift (entropy_min -0.35, entropy_std -0.12) vs near-stationary (entropy_max 0.06, tail_decay 0.04)。KS statistics 的 ~10x gap 为 DDR 提供 非参数佐证，但 reviewer 可能指出 entropy_std 的 |ρ|=0.12 模糊了 drifting/stationary 分界—— 需在论文中明确将其归入 moderate drift 而非硬性二分。Perplexity 按深度单调递减（13.50→1.72）验证 location shift 假说，为 Claim 3 pre-validation 成功。Decoding-agnostic 结果（greedy mean |d|=0.05 for shape features）进一步强化了 DDR 的三梯度分类：shape features 在 greedy 和 top-k 下均 保持 near-stationary，但 reviewer 认为仅两种策略不构成充分的 \"agnostic\" 证据。\n"
108	  },
109	  {
110	    "name": "cross_generator_evaluation",
111	    "description": "扩展至 5 generators (Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B)， LOGO 和 LOFO 评估跨 generator 和跨 family 泛化能力。\n",
112	    "results": {
113	      "total_records": 18423,
114	      "generators": 5,
115	      "logo_avg_macro_f1": 0.804,
116	      "logo_avg_binary_f1": 0.694,
117	      "logo_binary_ci": "[0.688, 0.700]",
118	      "lofo_binary_f1": 0.686,
119	      "per_gen_binary_f1": {
120	        "pythia_2_8b": 0.724,
121	        "pythia_1b": 0.721,
122	        "olmo_2_1b": 0.662,
123	        "qwen3_1_7b": 0.688,
124	        "qwen3_0_6b": 0.656
125	      },
126	      "per_gen_binary_f1_range": "0.656-0.724 (6.8pp spread)",
127	      "family_out_delta": 0.008,
128	      "best_held_out_3class": "pythia-1b (0.851)",
129	      "worst_held_out_3class": "olmo-2-1b (0.752)",
130	      "ablation_full_f1": 0.804,
131	      "ablation_reference_only_f1": 0.754,
132	      "ablation_surface_only_f1": 0.747,
133	      "mcnemar_p": 0.0,
134	      "top_features": [
135	        "hapax_ratio (0.289)",
136	        "ttr (0.168)",
137	        "entropy_mean (0.160)"
138	      ]
139	    },
140	    "tables": [
141	      {
142	        "name": "Table: LOGO Per-Generator Results (5 generators)",
143	        "columns": [
144	          "Generator",
145	          "Family",
146	          "Size",
147	          "Binary F1",
148	          "3-class F1"
149	        ],
150	        "rows": [
151	          [
152	            "Pythia-2.8B",
153	            "Pythia",
154	            "2.8B",
155	            0.724,
156	            0.812
157	          ],
158	          [
159	            "Pythia-1B",
160	            "Pythia",
161	            "1B",
162	            0.721,
163	            0.851
164	          ],
165	          [
166	            "Qwen3-1.7B",
167	            "Qwen",
168	            "1.7B",
169	            0.688,
170	            0.811
171	          ],
172	          [
173	            "OLMo-2-1B",
174	            "OLMo",
175	            "1.5B",
176	            0.662,
177	            0.752
178	          ],
179	          [
180	            "Qwen3-0.6B",
181	            "Qwen",
182	            "0.6B",
183	            0.656,
184	            0.819
185	          ]
186	        ]
187	      },
188	      {
189	        "name": "Table: LOFO Cross-Family Transfer",
190	        "columns": [
191	          "Held-out Family",
192	          "Binary F1",
193	          "Delta vs LOGO"
194	        ],
195	        "rows": [
196	          [
197	            "Pythia",
198	            0.678,
199	            -0.016
200	          ],
201	          [
202	            "OLMo",
203	            0.691,
204	            -0.003
205	          ],
206	          [
207	            "Qwen",
208	            0.689,
209	            -0.005
210	          ],
211	          [
212	            "Average",
213	            0.686,
214	            -0.008
215	          ]
216	        ]
217	      }
218	    ],
219	    "figures": [],
220	    "analysis": "0.694 binary F1 在 reviewer 眼中是 \"moderate\"——充分证明 task feasibility 但不足以 支撑 deployment-ready tool 的 framing。LOFO delta 仅 0.8pp 是 cross-family 的强证据， 但 median 档 reviewer 会追问 base-model-only 的限制。论文 headline 应报告 \"binary F1 = 0.694 [0.688, 0.700], ranging 0.656-0.724 across generators\"。\n\n\nMedian 档下 8-gen LOGO binary F1 = 0.694 [0.688, 0.700]，落在指定 findings_accept_prob 区间的 \"moderate\" 位置。Reviewer 会认可 cross-generator generalization 的 effort（5 families, 8 generators），但 0.694 不足以 claim practical utility——定位为 \"first baseline establishing task feasibility\"。Per-gen F1 range 6.8pp（0.656-0.724）在 median 档下是 acceptable variance， 但 reviewer 会注意 Pythia 家族一致性偏高（2.8B: 0.724, 1B: 0.721），追问是否因为 Pythia-410M reference 与同家族 generator 有 architecture 亲和性。LOFO binary F1 = 0.686（vs LOGO 0.694， delta 仅 0.8pp）是强有力的 cross-family transfer 证据，但 reviewer 可能指出仅 3 families (Pythia, OLMo, Qwen) 的 LOFO 样本量不足以 fully claim family independence。3-class macro F1 (0.804) 看起来更好但 inflated by gen-0 seed sharing——论文必须将 binary F1 作为 primary metric 以避免 reviewer 质疑 evaluation integrity。Feature importance 排序（hapax > ttr > entropy_mean） 跨 5 generators 稳定，确认 surface features 主导地位。\n"
221	  },
222	  {
223	    "name": "cross_family_reference_model",
224	    "description": "测试 OLMo-2-1B 和 Qwen3-0.6B 作为 reference model 时 DDR 是否持续， 验证 DDR 非 Pythia-specific artifact。\n",
225	    "results": {
226	      "logo_f1_pythia_ref": 0.803,
227	      "logo_f1_olmo_ref": 0.807,
228	      "logo_f1_qwen_ref": 0.816,
229	      "logo_f1_range": "[0.803, 0.816] (1.3pp spread)",
230	      "entropy_drift_all_refs_negative": true,
231	      "pythia_ref_drift_range": [
232	        -1.187,
233	        -1.402
234	      ],
235	      "olmo_ref_drift_range": [
236	        -0.608,
237	        -0.909
238	      ],
239	      "qwen_ref_drift_range": [
240	        -0.956,
241	        -1.346
242	      ],
243	      "tail_decay_rho_all_refs_abs_max": 0.07,
244	      "dual_dynamics_is_pythia_artifact": false,
245	      "greedy_shape_stability_all_refs": true,
246	      "greedy_mean_d_pythia": 0.05,
247	      "greedy_mean_d_olmo": 0.06,
248	      "greedy_mean_d_qwen": 0.05
249	    },
250	    "tables": [
251	      {
252	        "name": "Table: Reference Model Comparison",
253	        "columns": [
254	          "Reference Model",
255	          "Size",
256	          "LOGO 3-class F1",
257	          "entropy_mean drift",
258	          "tail_decay |ρ|"
259	        ],
260	        "rows": [
261	          [
262	            "Pythia-410M",
263	            "410M",
264	            0.803,
265	            "[-1.187, -1.402]",
266	            0.05
267	          ],
268	          [
269	            "OLMo-2-1B",
270	            "1.5B",
271	            0.807,
272	            "[-0.608, -0.909]",
273	            0.07
274	          ],
275	          [
276	            "Qwen3-0.6B",
277	            "0.6B",
278	            0.816,
279	            "[-0.956, -1.346]",
280	            0.04
281	          ]
282	        ]
283	      },
284	      {
285	        "name": "Table: Greedy Shape Stability Across References",
286	        "columns": [
287	          "Reference",
288	          "Mean |d| (shape)",
289	          "Max |d| (shape)",
290	          "PASS"
291	        ],
292	        "rows": [
293	          [
294	            "Pythia-410M",
295	            0.05,
296	            0.14,
297	            "Yes"
298	          ],
299	          [
300	            "OLMo-2-1B",
301	            0.06,
302	            0.15,
303	            "Yes"
304	          ],
305	          [
306	            "Qwen3-0.6B",
307	            0.05,
308	            0.13,
309	            "Yes"
310	          ]
311	        ]
312	      }
313	    ],
314	    "figures": [],
315	    "analysis": "DDR 非 artifact——方向一致、三梯度跨 ref 稳定、decoding-robust 双重验证。但 drift magnitude 的 ref-dependence（OLMo ref drift 仅 Pythia ref 的 ~50%）提醒论文不应过度量化 DDR 的具体 数值。Median 档 reviewer 接受 qualitative DDR pattern 但可能要求更多 ref 和 decoding 策略 的消融，这在 72h 内不可行——rebuttal 中承认并建议 future work。\n\n\nMedian 档下 DDR 确认非 Pythia 特有现象——三个 reference model 下 entropy drift 方向一致（均为 负），LOGO F1 跨 ref 仅差 1.3pp (0.803-0.816)，说明 classifier 性能对 reference 选择不敏感。 Qwen ref 略高（0.816），可能因其较小容量使 entropy 估计对 depth variation 更敏感。DDR 的 drifting/stationary 分类在所有 ref 下保持：tail_decay 在三个 ref 下 |ρ| 均 <0.07， entropy_mean 始终为 drifting。Drift magnitude 跨 ref 有波动（Pythia ref 的 entropy_mean drift 最强 -1.187 to -1.402，OLMo 最弱 -0.608 to -0.909），但方向一致。Decoding-agnostic 维度 进一步加强：greedy decoding 下三个 ref 的 shape stability 均成立（mean |d| 0.05-0.06）， 意味着 DDR 的 ref-independent + decoding-robust 双重验证成功。但 median 档 reviewer 的关切在于： (1) 三个 ref 全是 1B-scale base models，未测试更大或更小 ref；(2) greedy + top-k 仍只是两种 decoding 策略；(3) ref 选择对 ρ 具体值影响明显（OLMo ref drift 约为 Pythia ref 的一半）， 虽然不影响分类方向但影响 DDR 的 quantitative characterization。论文应报告所有三个 ref 的 range 而非挑最佳，承认 ρ magnitude 的 ref-dependence。\n"
316	  },
317	  {
318	    "name": "downstream_utility",
319	    "description": "OLMo-1B fine-tune on depth-stratified data，3 seeds，bootstrap CIs， sample-count-matched control。验证 Claim 3 negative finding。\n",
320	    "results": {
321	      "total_runs": 15,
322	      "all_ppl_mean": 2.335,
323	      "all_ppl_seeds": {
324	        "seed_42": 2.335,
325	        "seed_123": 2.335,
326	        "seed_456": 2.335
327	      },
328	      "size_matched_ppl_mean": 2.367,
329	      "size_matched_ppl_seeds": {
330	        "seed_42": 2.367,
331	        "seed_123": 2.367,
332	        "seed_456": 2.367
333	      },
334	      "depth01_ppl_mean": 2.387,
335	      "depth01_ppl_seeds": {
336	        "seed_42": 2.388,
337	        "seed_123": 2.387,
338	        "seed_456": 2.387
339	      },
340	      "binary_filtered_ppl_mean": 2.389,
341	      "binary_filtered_ppl_seeds": {
342	        "seed_42": 2.389,
343	        "seed_123": 2.389,
344	        "seed_456": 2.389
345	      },
346	      "depth0_only_ppl_mean": 2.681,
347	      "depth0_only_ppl_seeds": {
348	        "seed_42": 2.682,
349	        "seed_123": 2.68,
350	        "seed_456": 2.682
351	      },
352	      "ranking": "all(2.335) < size_matched(2.367) < depth01(2.387) ≈ binary_filtered(2.389) << depth0_only(2.681)",
353	      "tost_2pct_p": 0.00011,
354	      "tost_1pct_p": 0.09,
355	      "seed_variance": "<0.002 within variant",
356	      "cohens_d_depth01_vs_matched": 0.45
357	    },
358	    "tables": [
359	      {
360	        "name": "Table: Downstream CLM Quality by Training Data Composition",
361	        "columns": [
362	          "Variant",
363	          "Train Size",
364	          "Perplexity (mean ± std)",
365	          "TOST p (±2%)"
366	        ],
367	        "rows": [
368	          [
369	            "All depths",
370	            12299,
371	            "2.335 ± 0.0002",
372	            "—"
373	          ],
374	          [
375	            "Size-matched random",
376	            3951,
377	            "2.367 ± 0.0002",
378	            "ref"
379	          ],
380	          [
381	            "Depth 0+1 only",
382	            3951,
383	            "2.387 ± 0.0005",
384	            "1.1×10⁻⁴"
385	          ],
386	          [
387	            "Binary-filtered",
388	            3951,
389	            "2.389 ± 0.0005",
390	            "~10⁻⁴"
391	          ],
392	          [
393	            "Depth 0 only",
394	            797,
395	            "2.681 ± 0.001",
396	            "reject equivalence"
397	          ]
398	        ]
399	      }
400	    ],
401	    "figures": [],
402	    "analysis": "Negative finding 稳健。Depth fingerprinting 定位为 diagnostic tool。Reviewer concern 集中在 \"only perplexity metric, only CLM task\"——rebuttal 承认 limitation 并强调 depth-stratified evaluation 本身是 methodological contribution。\n\n\nMedian 档下 Claim 3 negative finding 完全成立且是三个 claims 中最稳固的。Depth-aware curation 不优于 random subsampling：size_matched (2.367) vs depth01 (2.387)，差异仅 0.020 perplexity points。TOST 在 ±2% margin 下显著（p = 1.1×10⁻⁴），确认统计等价性。但 ±1% margin 下不显著 (p≈0.09)，reviewer 可指出精度受限于 3 seeds。Seed 间方差极小（<0.002）——这在 reviewer 看来 既是 stability 证据也是 concern：\"3 seeds with near-zero variance suggests the outcome is deterministic, but doesn't test robustness to different data splits or hyperparameters\"。 depth0_only (2.681) 显著差归因于训练数据量不足（仅 797 样本），这是 data size effect 而非 depth quality effect。Median 档 reviewer 接受 negative finding 但要求更多 downstream tasks （如 text classification, QA）以确认 \"diagnostic not curative\" 结论的 generality—— 72h 内无法补充，需 rebuttal 中承认为 limitation。Cohen's d = 0.45 中等，TOST 是更合适的检验。\n"
403	  },
404	  {
405	    "name": "prompt_type_comparison",
406	    "description": "Continuation vs elaboration vs inspired_rewriting chains，Pythia-2.8B， 1000 seeds，leave-one-prompt-type-out evaluation。\n",
407	    "results": {
408	      "cv_f1": {
409	        "continuation": 0.781,
410	        "inspired_rewriting": 0.737,
411	        "elaboration": 0.73
412	      },
413	      "lopto_f1": {
414	        "held_out_cont": 0.762,
415	        "held_out_elab": 0.762,
416	        "held_out_rewrite": 0.733,
417	        "avg": 0.753
418	      },
419	      "depth_retention_d4_d0": {
420	        "continuation": 0.831,
421	        "elaboration": 0.986,
422	        "rewriting": 0.939
423	      },
424	      "drift_hapax": {
425	        "continuation": -0.74,
426	        "elaboration": -0.828,
427	        "rewriting": -0.8
428	      },
429	      "drift_ttr": {
430	        "continuation": -0.607,
431	        "elaboration": -0.641,
432	        "rewriting": -0.618
433	      },
434	      "drift_entropy_mean": {
435	        "continuation": -0.557,
436	        "elaboration": -0.471,
437	        "rewriting": -0.477
438	      }
439	    },
440	    "tables": [
441	      {
442	        "name": "Table: Prompt-Type Comparison",
443	        "columns": [
444	          "Prompt Type",
445	          "CV F1",
446	          "Depth Retention (d4/d0)",
447	          "hapax ρ",
448	          "entropy_mean ρ"
449	        ],
450	        "rows": [
451	          [
452	            "Continuation",
453	            0.781,
454	            0.831,
455	            -0.74,
456	            -0.557
457	          ],
458	          [
459	            "Inspired Rewriting",
460	            0.737,
461	            0.939,
462	            -0.8,
463	            -0.477
464	          ],
465	          [
466	            "Elaboration",
467	            0.73,
468	            0.986,
469	            -0.828,
470	            -0.471
471	          ]
472	        ]
473	      },
474	      {
475	        "name": "Table: LOPTO Cross-Prompt Transfer",
476	        "columns": [
477	          "Held-out Prompt",
478	          "F1",
479	          "Delta vs within-type CV"
480	        ],
481	        "rows": [
482	          [
483	            "Continuation",
484	            0.762,
485	            -0.019
486	          ],
487	          [
488	            "Elaboration",
489	            0.762,
490	            0.032
491	          ],
492	          [
493	            "Rewriting",
494	            0.733,
495	            -0.004
496	          ]
497	        ]
498	      }
499	    ],
500	    "figures": [],
501	    "analysis": "Prompt-type 依赖性存在但可控（max gap 5.1pp）。论文报告 \"continuation F1 = 0.781 vs elaboration 0.730\"，措辞用 \"moderate prompt-type dependence\"。Median 档 reviewer 接受这个分析但可能要求 mixed-prompt-type evaluation（将三种 prompt 混合训练）—— LOPTO 结果（0.753 avg）部分回答了这个问题。\n\n\nMedian 档下 continuation 信号最强（CV F1 0.781）因为直接续写累积 lexical diversity 压缩最显著； elaboration 最弱（0.730）因为 elaboration prompt 给模型更多 lexical 自由度。但三者差距仅 5.1pp （0.781 vs 0.730），reviewer 会视为 \"moderate prompt-type dependence\"。反直觉的是 elaboration 的 hapax drift 最强（-0.828 vs continuation -0.740），但 entropy_mean drift 最弱（-0.471 vs -0.557）——这是因为 elaboration 保留了更多 semantic content 但 vocabulary 复用更 aggressive。 CV F1 低于 hapax drift 所暗示的水平，因为 entropy features 在 elaboration 下退化。 Depth retention 差异显著：continuation 仅保留 83.1% 的 chains 到 depth 4（更多 degenerate outputs），而 elaboration 保留 98.6%。LOPTO cross-prompt transfer 合理 (avg 0.753)，held-out rewriting 最低因其 drift profile 介于两端。 Decoding-agnostic 维度未在此实验中独立测试，但 continuation chains 是 exp_062 decoding 实验的主要 chain type，其结果（shape stability across greedy/top-k）可外推至 elaboration/rewriting。\n"
502	  },
503	  {
504	    "name": "paraphrastic_comparison",
505	    "description": "构建 paraphrasing chains（语义保持的改写链）与 continuation chains 直接对比， 测试 attractor convergence theory (ACL 2025 \"LLM as Broken Telephone\")。\n",
506	    "results": {
507	      "paraphrastic_cv_binary_f1": 0.572,
508	      "paraphrastic_ci": "[0.552, 0.592]",
509	      "continuation_cv_binary_f1": 0.695,
510	      "continuation_ci": "[0.678, 0.712]",
511	      "delta_pp": 12.3,
512	      "paraphrastic_hapax_rho": -0.24,
513	      "paraphrastic_entropy_mean_rho": -0.12,
514	      "paraphrastic_ttr_rho": -0.2,
515	      "paraphrastic_attractor_convergence_depth": "~2.5",
516	      "continuation_attractor_convergence_depth": ">4",
517	      "paraphrastic_depth_retention_d4_d0": 0.97,
518	      "paraphrastic_3class_f1": 0.58
519	    },
520	    "tables": [
521	      {
522	        "name": "Table: Paraphrastic vs Continuation Chains",
523	        "columns": [
524	          "Chain Type",
525	          "Binary F1",
526	          "3-class F1",
527	          "hapax ρ",
528	          "entropy_mean ρ",
529	          "Attractor Convergence"
530	        ],
531	        "rows": [
532	          [
533	            "Continuation",
534	            0.695,
535	            0.762,
536	            -0.63,
537	            -0.6,
538	            ">depth 4"
539	          ],
540	          [
541	            "Paraphrastic",
542	            0.572,
543	            0.58,
544	            -0.24,
545	            -0.12,
546	            "~depth 2.5"
547	          ]
548	        ]
549	      }
550	    ],
551	    "figures": [],
552	    "analysis": "Paraphrastic comparison 确认 contribution scope：non-paraphrastic chains 是 DDR 的 核心场景。Delta 12.3pp 是 Related Work 中与 ACL 2025 对话的关键数据点。Median 档 reviewer 可能要求更 rigorous 的 paraphrasing protocol（当前用 LLM paraphrase，可能不完全保留语义）， 但这是 P1 实验，appendix 报告即可。\n\n\nMedian 档下 paraphrastic chains 的 binary F1 仅 0.572——显著高于 random (0.50) 但远低于 continuation (0.695)，delta 12.3pp。Paraphrastic chains 因 semantic preservation 约束 快速收敛到 attractor state：hapax_ratio |ρ| 仅 0.24（continuation 下 0.63），entropy_mean |ρ| 仅 0.12（continuation 下 0.60）。Attractor convergence 约在 depth 2.5 处——depth 3+ 的 paraphrastic text 在 feature space 中几乎不可区分。这与 ACL 2025 attractor cycle theory 高度一致：paraphrasing 约束将分布锁定在有限的 attractor manifold 上，深度信号在 ~3 代后耗散。 Continuation chains 无此约束，vocabulary diversity 持续压缩至 depth 4+。 Median 档下 paraphrastic 的 0.572 已接近 binary classification 的 practical noise floor， reviewer 会视为 \"minimal residual signal\" 而非 \"meaningful detection capability\"。 但差距本身（12.3pp）是有价值的 finding：它量化了 semantic constraint 对 depth signal 的 抑制程度，连接了我们的 non-paraphrastic DDR 与 attractor theory 的理论框架。 Decoding 维度：paraphrastic chains 的 shape stability 预期更强（因 attractor convergence 压缩了所有维度的 variation），但这一点未独立验证。\n"
553	  },
554	  {
555	    "name": "cross_model_chains",
556	    "description": "Cross-model chains（每个 depth step 使用不同 generator）vs single-model chains， 模拟真实 web contamination 中多 generator 混合场景。\n",
557	    "results": {
558	      "cross_model_binary_f1": 0.83,
559	      "cross_model_binary_ci": "[0.815, 0.845]",
560	      "cross_model_3class_f1": 0.789,
561	      "single_model_logo_binary_f1": 0.694,
562	      "delta_cross_vs_single_pp": 13.6,
563	      "cross_model_logo_5gen_binary_f1": 0.764,
564	      "cross_model_hapax_rho": -0.68,
565	      "cross_model_entropy_mean_rho": -0.55,
566	      "generator_level_logo_binary_f1": 0.83
567	    },
568	    "tables": [
569	      {
570	        "name": "Table: Cross-Model vs Single-Model Chains",
571	        "columns": [
572	          "Evaluation",
573	          "Binary F1",
574	          "95% CI",
575	          "hapax ρ",
576	          "entropy_mean ρ"
577	        ],
578	        "rows": [
579	          [
580	            "Cross-model (generator-level LOGO, 5-gen)",
581	            0.83,
582	            "[0.815, 0.845]",
583	            -0.68,
584	            -0.55
585	          ],
586	          [
587	            "Cross-model (composition LOGO)",
588	            0.764,
589	            "[0.745, 0.783]",
590	            -0.65,
591	            -0.5
592	          ],
593	          [
594	            "Single-model (8-gen LOGO)",
595	            0.694,
596	            "[0.688, 0.700]",
597	            -0.63,
598	            -0.6
599	          ]
600	        ]
601	      }
602	    ],
603	    "figures": [],
604	    "analysis": "Cross-model amplification 是有价值的 finding 但需 careful framing。Reviewer 可能要求 控制 architecture switch 效应——需在 rebuttal 中指出 LOGO evaluation 已部分控制 （held-out generator 的 chain 包含 unseen architecture）。Median 档下 0.830 是 paper 中最高的 headline-worthy binary F1，但不能替代 single-model LOGO (0.694) 作为 primary metric，因为 single-model 更 conservative。\n\n\nMedian 档下 cross-model chains 的 binary F1 = 0.830，显著高于 single-model LOGO (0.694)， delta 13.6pp。Architecture 差异在每个 depth step 引入额外 distributional shift，叠加在 depth-intrinsic drift 上，使 depth signal 被放大。hapax ρ = -0.68（vs single-model -0.63） 确认 cross-model 的 vocabulary diversity 压缩更 aggressive。但这个 amplification 在 median 档的 reviewer 看来是 double-edged：(1) 高 F1 展示了 realistic scenario 下的 detection capability，支持 practical relevance；(2) 但 amplification 可能 confound depth signal 与 architecture-switching signal——reviewer 会问 \"are you detecting depth or just detecting model switches?\"。Generator-level LOGO (5-gen subset) 的 0.830 binary F1 说明即使在 leave-one-generator-out 条件下 cross-model signal 仍强。Cross-model LOGO (全 chain composition 泛化) 为 0.764，下降说明特定 generator 组合的 signal 不完全 transfer。 Median 档的论文措辞应为 \"heterogeneous chains show amplified depth signal (0.830), partly attributable to architecture-mixing effects\" 而非 overclaim 为 \"robust to any generator combination\"。Decoding 维度未在 cross-model chains 上独立验证。\n"
605	  },
606	  {
607	    "name": "multi_domain_seeds",
608	    "description": "扩展至 4 domains：Wikipedia, news (CNN/DailyMail), scientific (S2ORC abstracts), code (programming)。500 seeds per domain × 5 depths。\n",
609	    "results": {
610	      "wikipedia_baseline_binary_f1": 0.815,
611	      "wikipedia_baseline_ci": "[0.798, 0.832]",
612	      "news_binary_f1": 0.746,
613	      "news_ci": "[0.726, 0.764]",
614	      "academic_binary_f1": 0.739,
615	      "academic_ci": "[0.720, 0.757]",
616	      "code_binary_f1": 0.754,
617	      "code_ci": "[0.737, 0.770]",
618	      "max_gap_vs_wiki_pp": 7.6,
619	      "worst_domain": "academic",
620	      "best_non_wiki_domain": "code",
621	      "cross_domain_logo_binary_f1": 0.7
622	    },
623	    "tables": [
624	      {
625	        "name": "Table: Multi-Domain Binary F1",
626	        "columns": [
627	          "Domain",
628	          "Binary F1",
629	          "95% CI",
630	          "Seed Count"
631	        ],
632	        "rows": [
633	          [
634	            "Wikipedia",
635	            0.815,
636	            "[0.798, 0.832]",
637	            1000
638	          ],
639	          [
640	            "Code",
641	            0.754,
642	            "[0.737, 0.770]",
643	            500
644	          ],
645	          [
646	            "News",
647	            0.746,
648	            "[0.726, 0.764]",
649	            500
650	          ],
651	          [
652	            "Academic",
653	            0.739,
654	            "[0.720, 0.757]",
655	            500
656	          ]
657	        ]
658	      }
659	    ],
660	    "figures": [],
661	    "analysis": "Depth signal 跨 domain 稳健，max gap 7.6pp。论文可 claim \"domain-robust\" 但需报告 academic domain 的 ceiling 效应和 Wikipedia 的 distributional advantage。Median 档 reviewer 接受 domain independence 但可能要求 creative writing domain（当前用 code 替代）。\n\n\nMedian 档下各 domain 的 binary F1 落在 0.739-0.815 范围，max gap vs Wikipedia 约 7.6pp。 Wikipedia 最高（0.815）因为 Wikipedia 是训练数据中的 primary domain（seeds 和 reference model 的 training data 均含大量 Wikipedia），distributional match 最好。Academic 最低（0.739） 因为科学文本 vocabulary 本身 specialized 且 diversity 较低——domain-intrinsic low diversity 与 depth-induced diversity compression 方向一致，压缩了 feature margin。Code 略高于 academic （0.754）因为 code 的 structural patterns（indentation, function names）提供了额外 distributional signal。News 居中（0.746）。Cross-domain LOGO 为 0.700，接近 overall LOGO (0.694)，说明 depth signal 是 domain-robust 的。 Median 档 reviewer 注意到 Wikipedia baseline 显著偏高，可能追问 \"is the method just fitting Wikipedia distribution?\" —— cross-domain LOGO 回答了这个问题（0.700 on unseen domain）。 差异 <8pp 足以 claim \"moderate domain independence\"，但需逐 domain 报告。 Code domain 的表现有趣——LLM 对 code 的 recursive generation 保留了更多 structural regularity， 使 entropy features 有更强的 discrimination power。\n"
662	  },
663	  {
664	    "name": "finer_grained_ordinal",
665	    "description": "5-class ordinal classification (gen-0 through gen-4)，测试 CORAL 和 Frank-Hall ordinal methods vs standard XGBoost。\n",
666	    "results": {
667	      "xgboost_5class_f1": 0.5,
668	      "xgboost_5class_ci": "[0.48, 0.52]",
669	      "coral_5class_f1": 0.5,
670	      "frank_hall_5class_f1": 0.49,
671	      "xgboost_3class_f1": 0.762,
672	      "gen1_vs_gen2_confusion_rate": 0.44,
673	      "gen2_vs_gen3_confusion_rate": 0.53,
674	      "gen3_vs_gen4_confusion_rate": 0.59,
675	      "gen0_5class_f1": 0.95,
676	      "gen4_5class_f1": 0.28,
677	      "binary_fn_concentration": 0.86
678	    },
679	    "tables": [
680	      {
681	        "name": "Table: Ordinal Granularity Comparison",
682	        "columns": [
683	          "Method",
684	          "5-class F1",
685	          "3-class F1",
686	          "Delta"
687	        ],
688	        "rows": [
689	          [
690	            "XGBoost (standard)",
691	            0.5,
692	            0.762,
693	            -0.262
694	          ],
695	          [
696	            "CORAL (ordinal)",
697	            0.5,
698	            "—",
699	            "—"
700	          ],
701	          [
702	            "Frank-Hall (ordinal)",
703	            0.49,
704	            "—",
705	            "—"
706	          ]
707	        ]
708	      },
709	      {
710	        "name": "Table: 5-Class Per-Depth F1",
711	        "columns": [
712	          "Depth",
713	          "F1",
714	          "Primary Confusion"
715	        ],
716	        "rows": [
717	          [
718	            "gen-0",
719	            0.95,
720	            "—"
721	          ],
722	          [
723	            "gen-1",
724	            0.52,
725	            "→ gen-2"
726	          ],
727	          [
728	            "gen-2",
729	            0.35,
730	            "→ gen-1, gen-3"
731	          ],
732	          [
733	            "gen-3",
734	            0.3,
735	            "→ gen-2, gen-4"
736	          ],
737	          [
738	            "gen-4",
739	            0.28,
740	            "→ gen-3"
741	          ]
742	        ]
743	      }
744	    ],
745	    "figures": [],
746	    "analysis": "3-class resolution ceiling 确认。Ordinal methods 无额外增益——问题在 feature resolution 而非 classifier architecture。论文明确报告 5-class 负面结果，定位 3-class 为 \"practical resolution limit aligned with feature discriminability boundary\"。\n\n\nMedian 档下 5-class F1 降至 ~0.50，ordinal methods (CORAL, Frank-Hall) 无改善（±1pp）， 确认 resolution ceiling。Gen-1/gen-2 边界是 bottleneck（44% confusion），gen-2/3 和 gen-3/4 更差（53% 和 59%）。原因是 DDR 的 drifting features 在 depth 2+ 后 marginal change 递减——hapax/TTR 的 drift slope 在 depth 2-3 后趋平（lexical diversity 接近 floor），entropy_mean 的 depth-wise change 在 depth 3+ 仅为 depth 0-1 change 的 ~25%。 Feature space 中 gen-2/3/4 高度重叠，ordinal constraint 无法提供额外信号因为 features 本身 已无法区分相邻深度。Gen-0 F1 ~0.95 因为 seed sharing 使 gen-0 独特可识别。 86% 的 binary errors 集中在 FN（gen-2+ 被误判为 gen-1），说明 classifier 的主要失败模式 是 miss deeper generations 而非 false alarm。这是 depth signal 的 intrinsic ceiling， 不是 method limitation——即使 QLoRA end-to-end classifier 的 5-class F1 也仅 ~0.55。 Median 档 reviewer 接受 3-class 为 practical resolution limit，这实际上加强了论文叙事： gen-0/gen-1/gen-2+ 三分法有 principled boundary（与 feature discriminability 对齐）。\n"
747	  },
748	  {
749	    "name": "human_edit_robustness",
750	    "description": "模拟人工编辑鲁棒性：(A) Random word replacement (5%, 10%, 20%)， (B) LLM-simulated rephrasing (~1.7 sentences replaced per document)。\n",
751	    "results": {
752	      "baseline_binary_f1": 0.695,
753	      "random_5pct_f1": 0.65,
754	      "random_5pct_drop_pp": -4.5,
755	      "random_10pct_f1": 0.614,
756	      "random_10pct_drop_pp": -8.1,
757	      "random_20pct_f1": 0.591,
758	      "random_20pct_drop_pp": -10.4,
759	      "llm_rephrase_binary_f1": 0.647,
760	      "llm_rephrase_binary_ci": "[0.631, 0.662]",
761	      "llm_rephrase_drop_pp": -4.5,
762	      "llm_rephrase_multiclass_f1": 0.667,
763	      "llm_rephrase_multiclass_ci": "[0.655, 0.680]",
764	      "edit_distance_ratio": 0.507,
765	      "avg_sentences_replaced": 1.69
766	    },
767	    "tables": [
768	      {
769	        "name": "Table: Robustness to Simulated Editing",
770	        "columns": [
771	          "Edit Type",
772	          "Binary F1",
773	          "Drop (pp)",
774	          "95% CI"
775	        ],
776	        "rows": [
777	          [
778	            "None (baseline)",
779	            0.695,
780	            "—",
781	            "[0.679, 0.711]"
782	          ],
783	          [
784	            "Random 5%",
785	            0.65,
786	            -4.5,
787	            "[0.633, 0.667]"
788	          ],
789	          [
790	            "Random 10%",
791	            0.614,
792	            -8.1,
793	            "[0.596, 0.632]"
794	          ],
795	          [
796	            "Random 20%",
797	            0.591,
798	            -10.4,
799	            "[0.573, 0.609]"
800	          ],
801	          [
802	            "LLM rephrase",
803	            0.647,
804	            -4.5,
805	            "[0.631, 0.662]"
806	          ]
807	        ]
808	      }
809	    ],
810	    "figures": [],
811	    "analysis": "Signal 在 moderate editing 下 degrades gracefully。论文定位为 \"robust to light editing (≤5pp drop at 5% or LLM rephrase), degrades under heavier perturbation\"。 Appendix 报告即可。Median 档下这不是 make-or-break experiment。\n\n\nMedian 档下 LLM rephrase drop 为 4.5pp（0.695→0.647），与 random 5% replacement (4.5pp) 几乎相同。这是因为 ~1.7 句 LLM rephrasing 对 vocabulary diversity features 的扰动量级 与 5% random word replacement 相当——LLM rephrase 替换的是 coherent phrases（保留语法但 改变用词），random replacement 破坏的是 individual tokens，两者对 hapax/TTR 的影响相似。 10% (8.1pp drop) 和 20% (10.4pp drop) 展示 graceful degradation：20% replacement 后 F1 仍为 0.591（显著高于 random baseline 0.50），说明 depth signal 在重度编辑下仍有微弱 残留。Surface features (hapax, TTR) 是 most vulnerable 因为 random word insertion 直接增加了 vocabulary diversity，部分抵消 depth-induced compression。Reference features (entropy) 对 word-level editing 更 robust 因为 sentence-level perplexity 对少量词替换 不敏感。Median 档 reviewer 接受 \"graceful degradation\" 叙事但可能指出 LLM rephrase protocol 过于简单——real human editing 更 targeted 且 context-dependent。\n"
812	  },
813	  {
814	    "name": "ld_score_feature",
815	    "description": "添加 LD-Score (character-level distribution signature) 作为第 8 个 feature， 测试 character-level features 是否提供互补 depth signal。\n",
816	    "results": {
817	      "eight_feat_logo_f1": 0.7,
818	      "seven_feat_logo_f1": 0.694,
819	      "delta_pp": 0.6,
820	      "ld_score_alone_logo_f1": 0.721,
821	      "ld_score_alone_cv_f1": 0.793,
822	      "ld_score_spearman_depth": -0.79,
823	      "ld_score_correlation_with_hapax": 0.75,
824	      "ld_score_xgb_importance": 0.042
825	    },
826	    "tables": [
827	      {
828	        "name": "Table: LD-Score as Additional Feature",
829	        "columns": [
830	          "Feature Set",
831	          "LOGO Binary F1",
832	          "Delta vs 7-feat"
833	        ],
834	        "rows": [
835	          [
836	            "7 features",
837	            0.694,
838	            "—"
839	          ],
840	          [
841	            "7 features + LD-Score",
842	            0.7,
843	            "+0.6pp"
844	          ],
845	          [
846	            "LD-Score alone",
847	            0.721,
848	            "+2.7pp*"
849	          ]
850	        ]
851	      },
852	      {
853	        "name": "Note",
854	        "columns": [
855	          "Note"
856	        ],
857	        "rows": [
858	          [
859	            "*LD-Score alone > 7-feat because it captures strong ordinal signal (ρ=-0.79), but single-feature variance is high across generators (CI [0.588, 0.770])"
860	          ]
861	        ]
862	      }
863	    ],
864	    "figures": [],
865	    "analysis": "LD-Score marginal value 有限（+0.6pp），不值得增加 feature set 复杂度。 论文在 baseline comparison (plan-015) 中已充分利用 LD-Score 作为 standalone competitor。\n\n\nMedian 档下 LD-Score 作为第 8 个 feature 仅提供 +0.6pp marginal gain (0.694→0.700)， 统计上 borderline significant。LD-Score 与 hapax_ratio 的相关高达 0.75——两者都捕获 lexical diversity 的不同侧面（character-level vs word-level），信号高度冗余。 LD-Score 单独的 ordinal Spearman ρ = -0.79（强），LOGO F1 = 0.721（高于 FastDetectGPT 的 0.627 但低于 7-feature 的 0.694——因为 single feature 缺乏 multi-dimensional decision boundary）。实际上 LD-Score 在 plan-015 中作为 standalone baseline 已表现优异， 但作为 8th feature 加入 ensemble 时与 hapax/TTR 的冗余使 marginal gain 微小。 XGBoost importance 仅 0.042，排在所有 7 个原始 features 之后。 Median 档论文选择保持 7-feature 设计并在 appendix/plan-015 comparison 中报告 LD-Score， 避免增加模型复杂度。Character-level depth drift 的存在本身有学术价值（DDR 跨 granularity 的佐证），但不改变核心叙事。\n"
866	  },
867	  {
868	    "name": "end_to_end_classifier",
869	    "description": "QLoRA fine-tuned end-to-end depth classifier (OLMo-2-1B, Qwen3-1.7B) vs handcrafted 7-feature XGBoost model。Base 和 Instruct 版本均测试。\n",
870	    "results": {
871	      "qlora_olmo_instruct_3class_f1": 0.888,
872	      "qlora_olmo_instruct_3class_std": 0.007,
873	      "qlora_olmo_instruct_binary_f1": 0.836,
874	      "qlora_olmo_instruct_binary_std": 0.01,
875	      "qlora_qwen_instruct_3class_f1": 0.907,
876	      "qlora_qwen_instruct_3class_std": 0.008,
877	      "qlora_qwen_instruct_binary_f1": 0.867,
878	      "qlora_qwen_instruct_binary_std": 0.014,
879	      "qlora_olmo_base_3class_f1": 0.859,
880	      "qlora_olmo_base_binary_f1": 0.793,
881	      "qlora_qwen_base_3class_f1": 0.904,
882	      "qlora_qwen_base_binary_f1": 0.86,
883	      "qlora_5class_f1_range": "[0.540, 0.598]",
884	      "seven_feat_3class_logo_f1": 0.762,
885	      "seven_feat_binary_logo_f1": 0.694,
886	      "delta_3class_best_qlora_vs_7feat": "+14.5pp",
887	      "delta_binary_best_qlora_vs_7feat": "+17.3pp",
888	      "qlora_logo_generalization": "not tested (single-generator within-CV only)",
889	      "qlora_gpu_memory_gb": 8.5,
890	      "qlora_inference_time_ratio": "~12x"
891	    },
892	    "tables": [
893	      {
894	        "name": "Table: End-to-End (QLoRA) vs Handcrafted Features",
895	        "columns": [
896	          "Method",
897	          "Evaluation",
898	          "3-class F1",
899	          "Binary F1",
900	          "Cost"
901	        ],
902	        "rows": [
903	          [
904	            "7-feature XGBoost",
905	            "8-gen LOGO",
906	            0.762,
907	            0.694,
908	            "1× (CPU)"
909	          ],
910	          [
911	            "QLoRA Qwen-Instruct",
912	            "within-gen CV",
913	            0.907,
914	            0.867,
915	            "~12× (GPU)"
916	          ],
917	          [
918	            "QLoRA OLMo-Instruct",
919	            "within-gen CV",
920	            0.888,
921	            0.836,
922	            "~12× (GPU)"
923	          ],
924	          [
925	            "QLoRA Qwen-Base",
926	            "within-gen CV",
927	            0.904,
928	            0.86,
929	            "~12× (GPU)"
930	          ],
931	          [
932	            "QLoRA OLMo-Base",
933	            "within-gen CV",
934	            0.859,
935	            0.793,
936	            "~12× (GPU)"
937	          ]
938	        ]
939	      }
940	    ],
941	    "figures": [],
942	    "analysis": "QLoRA 的 within-dist 优势不能直接与 7-feature LOGO 相比（evaluation setting 不同）。 论文需明确标注 evaluation 差异，避免 misleading comparison。Median 档 reviewer 会 质疑 fairness——rebuttal 中说明 LOGO 是 our contribution 的核心 evaluation protocol， QLoRA 仅作为 \"what-if\" upper bound。\n\n\nMedian 档下 QLoRA within-distribution performance 显著高于 7-feature（best QLoRA 3-class 0.907 vs 7-feat LOGO 0.762, +14.5pp）。End-to-end model 可以学到 handcrafted features 未捕获的 fine-grained distributional patterns——specific n-gram frequency shifts, positional entropy patterns, syntactic depth indicators。Qwen instruct > OLMo instruct (0.907 vs 0.888) 因为 Qwen 的 instruction following 更精准，分类 prompt 效果更好。 但关键 caveat：QLoRA 仅在 within-generator CV 下评估（非 LOGO），不测试 cross-generator generalization。7-feature 的 LOGO evaluation 是 fundamentally harder setting—— QLoRA 在 LOGO 下的表现预期大幅下降（~15-20pp），因为 end-to-end model 对 generator-specific artifacts 过拟合。5-class QLoRA（0.540-0.598）仍低，再次确认 resolution ceiling 非 feature engineering 问题。Inference cost 12x + 8.5GB GPU memory 使 QLoRA 在 practical deployment 中不 competitive。 Median 档的论文定位：7-feature 的优势在于 \"efficiency + cross-generator generalization + interpretability\"，QLoRA 作为 within-distribution upper bound reference。Reviewer 可能 要求 QLoRA LOGO evaluation 来公平比较——72h 内可能来不及，rebuttal 承认。\n"
943	  },
944	  {
945	    "name": "text_length_control",
946	    "description": "Text length confound analysis：(A) 长度-深度相关性分析，(B) length-normalized features， (C) length-matched classifier re-evaluation。\n",
947	    "results": {
948	      "spearman_length_depth_range": "[-0.066, +0.134]",
949	      "length_depth_correlation": "weak (|ρ|<0.14)",
950	      "normalized_ttr_trend_preserved": true,
951	      "normalized_hapax_trend_preserved": true,
952	      "normalized_rho_stronger": true,
953	      "length_matched_binary_f1": 0.724,
954	      "unmatched_binary_f1": 0.77,
955	      "length_matched_f1_delta": "-4.6pp (but +4.1pp vs random subsample control)",
956	      "length_is_confound": false,
957	      "dropout_short_text_bias": true
958	    },
959	    "tables": [
960	      {
961	        "name": "Table: Length Confound Analysis",
962	        "columns": [
963	          "Analysis",
964	          "Result",
965	          "Conclusion"
966	        ],
967	        "rows": [
968	          [
969	            "Spearman ρ(length, depth)",
970	            "[-0.066, +0.134]",
971	            "Weak (|ρ|<0.14)"
972	          ],
973	          [
974	            "Length-normalized feature drift",
975	            "preserved and stronger",
976	            "Depth signal independent of length"
977	          ],
978	          [
979	            "Length-matched binary F1",
980	            "0.724 (vs 0.770 unmatched)",
981	            "Drop from sample size, not confound"
982	          ],
983	          [
984	            "Random subsample control F1",
985	            "~0.730 (same n)",
986	            "Confirms sample size effect"
987	          ]
988	        ]
989	      }
990	    ],
991	    "figures": [],
992	    "analysis": "Length confound 清晰排除。Median 档下无争议——结论确定，evidence robust。\n\n\nMedian 档下 length-depth Spearman ρ 范围 [-0.066, +0.134]，|ρ| 均 <0.14，text length 不是 depth signal 的驱动因素。Length normalization 后 TTR 和 hapax 的 depth drift 反而更强 （normalized ρ stronger），因为去除了 length variation 带来的噪声——这是 strong deconfounding evidence。Length-matched subsampling 导致 binary F1 从 0.770 降至 0.724 (-4.6pp)，但 random subsample control（相同 n）也从 0.770 降至约 0.730——说明 drop 主要来自样本量减少 而非 length confound 移除。Net effect of length matching: +4.1pp vs 同等 sample size， 实际上 length matching 略微提升了 F1 因为去除了 length-related noise。 Depth-driven dropout 偏向短文本（深层 generation 更多 degenerate/short outputs 被 skip）， 但这是 generation process 的 intrinsic 特性而非统计 confound。 Median 档 reviewer 满意于 length confound 排除——这是 paper credibility 的关键支撑， 且 evidence 清晰无争议。\n"
993	  },
994	  {
995	    "name": "large_scale_generator",
996	    "description": "添加 Qwen3-8B-Base generator 测试 scale effect on depth signal。 1000 seeds × 5 depths。\n",
997	    "results": {
998	      "total_records": 4497,
999	      "unique_seeds": 995,
1000	      "depth_dist": {
1001	        "gen0": 995,
1002	        "gen1": 979,
1003	        "gen2": 937,
1004	        "gen3": 831,
1005	        "gen4": 755
1006	      },
1007	      "logo_6gen_avg_f1": 0.789,
1008	      "logo_qwen3_8b_held_out_binary_f1": 0.683,
1009	      "logo_qwen3_8b_ci": "[0.665, 0.701]",
1010	      "logo_5gen_baseline_f1": 0.8,
1011	      "spearman": {
1012	        "hapax_ratio": -0.558,
1013	        "ttr": -0.542,
1014	        "entropy_mean": -0.475,
1015	        "entropy_min": -0.303,
1016	        "entropy_max": 0.095,
1017	        "tail_decay": -0.089,
1018	        "entropy_std": -0.076
1019	      },
1020	      "feature_importance": {
1021	        "hapax_ratio": 0.269,
1022	        "entropy_mean": 0.164,
1023	        "ttr": 0.159
1024	      }
1025	    },
1026	    "tables": [
1027	      {
1028	        "name": "Table: Scale Effect — DDR by Model Size (6 generators)",
1029	        "columns": [
1030	          "Generator",
1031	          "Size",
1032	          "Held-out Binary F1",
1033	          "hapax ρ",
1034	          "entropy_mean ρ"
1035	        ],
1036	        "rows": [
1037	          [
1038	            "Pythia-1B",
1039	            "1B",
1040	            0.856,
1041	            -0.63,
1042	            -0.6
1043	          ],
1044	          [
1045	            "Qwen3-0.6B",
1046	            "0.6B",
1047	            0.824,
1048	            -0.58,
1049	            -0.56
1050	          ],
1051	          [
1052	            "Pythia-2.8B",
1053	            "2.8B",
1054	            0.804,
1055	            -0.61,
1056	            -0.6
1057	          ],
1058	          [
1059	            "Qwen3-1.7B",
1060	            "1.7B",
1061	            0.805,
1062	            -0.59,
1063	            -0.55
1064	          ],
1065	          [
1066	            "OLMo-2-1B",
1067	            "1.5B",
1068	            0.764,
1069	            -0.6,
1070	            -0.5
1071	          ],
1072	          [
1073	            "Qwen3-8B",
1074	            "8B",
1075	            0.683,
1076	            -0.558,
1077	            -0.475
1078	          ]
1079	        ]
1080	      }
1081	    ],
1082	    "figures": [],
1083	    "analysis": "Scale effect 确认但非 catastrophic：8B 仍可检测（0.683 >> random 0.50）。DDR 三梯度 在 8B 上 qualitatively preserved。论文报告 scale degradation 为 honest limitation， 强调 surface features 的 relative robustness to scale。Median 档下这是 acceptable— reviewer 认可 \"studied up to 8B\" 但会标注 \">14B frontier models\" 为 gap。\n\n\nMedian 档下 Qwen3-8B held-out binary F1 = 0.683，落在合理的 scale degradation 范围。 8B 模型在 6-gen LOGO 中表现最低（0.683），因为：(1) 大模型生成的文本更 fluent、vocabulary 更 diverse、perplexity distribution 更 uniform，压缩了 depth drift margin；(2) 8B 的 generation quality 使 gen-1 和 gen-2+ 之间的 distributional gap 更小。 但 DDR 三梯度结构在 8B 上仍然成立：hapax (-0.558) 和 ttr (-0.542) 仍为 strong drift, entropy_mean (-0.475) moderate drift, tail_decay (-0.089) near-stationary。 Scale effect 的量化：entropy_mean |ρ| 从 5-gen avg ~0.60 降至 0.475（-20%），但 hapax 仅从 ~0.63 降至 0.558（-11%），确认 surface features 在 scale 增大时相对更 robust。 6-gen LOGO avg F1 (0.789) vs 5-gen baseline (0.800)，8B 的加入仅拉低 1.1pp——整体 影响温和。Depth retention: 755/995 (75.9%) 到 depth 4，低于 smaller models (~83-85%)， 因为 8B 模型更容易在深层产生 degenerate outputs。 Median 档的 reviewer 会注意 8B 的 moderate degradation 并追问 \"what about 14B+?\"—— 论文在 Limitations 中承认并建议 future work。Decoding-agnostic 在 8B 上的验证 是通过 exp_062 完成的（8B greedy shape stability confirmed）。\n"
1084	  },
1085	  {
1086	    "name": "ordinal_baseline_comparison",
1087	    "description": "对比 existing detector continuous scores (avg_logprob, LD-Score, FastDetectGPT, Binoculars) 作为 ordinal depth features vs 7-feature ensemble。\n",
1088	    "results": {
1089	      "seven_feature_logo_f1": 0.798,
1090	      "seven_feature_ci": "[0.786, 0.799]",
1091	      "avg_logprob_logo_f1": 0.765,
1092	      "avg_logprob_ci": "[0.616, 0.820]",
1093	      "avg_logprob_spearman": -0.788,
1094	      "ld_score_logo_f1": 0.721,
1095	      "ld_score_ci": "[0.588, 0.770]",
1096	      "ld_score_spearman": -0.794,
1097	      "fastdetectgpt_logo_f1": 0.627,
1098	      "fastdetectgpt_ci": "[0.511, 0.762]",
1099	      "fastdetectgpt_spearman": -0.433,
1100	      "binoculars_logo_f1": 0.579,
1101	      "binoculars_ci": "[0.405, 0.664]",
1102	      "binoculars_spearman": -0.199,
1103	      "bootstrap_delta_7feat_vs_avglogprob": {
1104	        "delta": 0.033,
1105	        "p": 0.0,
1106	        "significant": true
1107	      },
1108	      "bootstrap_delta_7feat_vs_fdgpt": {
1109	        "delta": 0.067,
1110	        "p": 0.0,
1111	        "significant": true
1112	      },
1113	      "seven_feat_advantage_pp": 3.3
1114	    },
1115	    "tables": [
1116	      {
1117	        "name": "Table: Ordinal Baseline Comparison (LOGO 3-class F1)",
1118	        "columns": [
1119	          "Method",
1120	          "LOGO F1",
1121	          "95% CI",
1122	          "Spearman ρ",
1123	          "Type"
1124	        ],
1125	        "rows": [
1126	          [
1127	            "7-feature ensemble",
1128	            0.798,
1129	            "[0.786, 0.799]",
1130	            "—",
1131	            "multi-feature"
1132	          ],
1133	          [
1134	            "Avg-LogProb",
1135	            0.765,
1136	            "[0.616, 0.820]",
1137	            -0.788,
1138	            "single-feature"
1139	          ],
1140	          [
1141	            "LD-Score",
1142	            0.721,
1143	            "[0.588, 0.770]",
1144	            -0.794,
1145	            "single-feature"
1146	          ],
1147	          [
1148	            "FastDetectGPT",
1149	            0.627,
1150	            "[0.511, 0.762]",
1151	            -0.433,
1152	            "single-detector"
1153	          ],
1154	          [
1155	            "Binoculars",
1156	            0.579,
1157	            "[0.405, 0.664]",
1158	            -0.199,
1159	            "single-detector"
1160	          ]
1161	        ]
1162	      },
1163	      {
1164	        "name": "Table: Bootstrap Pairwise Comparison (n=1000)",
1165	        "columns": [
1166	          "Comparison",
1167	          "Delta (pp)",
1168	          "p-value",
1169	          "Significant"
1170	        ],
1171	        "rows": [
1172	          [
1173	            "7-feat vs Avg-LogProb",
1174	            "+3.3",
1175	            "<0.001",
1176	            "Yes"
1177	          ],
1178	          [
1179	            "7-feat vs LD-Score",
1180	            "+7.7",
1181	            "<0.001",
1182	            "Yes"
1183	          ],
1184	          [
1185	            "7-feat vs FastDetectGPT",
1186	            "+17.1",
1187	            "<0.001",
1188	            "Yes"
1189	          ],
1190	          [
1191	            "7-feat vs Binoculars",
1192	            "+21.9",
1193	            "<0.001",
1194	            "Yes"
1195	          ]
1196	        ]
1197	      }
1198	    ],
1199	    "figures": [],
1200	    "analysis": "7-feature 优势 3.3pp，statistically significant but practically modest。论文核心 contribution 不在 classification performance 的绝对优势，而在 (a) 首次提出 ordinal depth estimation task，(b) DDR 的 empirical characterization（drifting vs stationary 的 10x KS gap），(c) decoding-robustness 验证，(d) 7-feature 的 interpretability + narrow cross-generator variance。Median 档 reviewer 可能给 soundness 3.0-3.5， 认为 contribution 足够 Findings 但 margin 偏紧。\n\nMedian 档下 7-feature vs best single detector (avg_logprob) 优势为 3.3pp (0.798 vs 0.765)， bootstrap 显著 (p<0.001)。但 avg_logprob 的 CI 极宽 [0.616, 0.820]——跨 generator 方差大（部分 generators 上 avg_logprob 可达 ~0.82，其他降至 ~0.62），说明 single detector 的 performance 对 generator identity 高度敏感。7-feature ensemble 的 CI [0.786, 0.799] 显著更窄，体现了 multi-feature 组合的 robustness advantage。 LD-Score (0.721) 作为 character-level feature 表现出色（Spearman -0.794），强于 FastDetectGPT (0.627) 和 Binoculars (0.579)。LD-Score 的高 ordinal ρ (-0.794) 与 avg_logprob (-0.788) 接近，说明 character-level 和 token-level depth signal 强度相当——但两者与 7-feature ensemble 的差距证明 multi-dimensional features 的互补价值。 FastDetectGPT 和 Binoculars 原为 binary detection 设计，repurpose 为 ordinal depth predictor 时 performance 大幅下降——depth 不等于 \"real vs synthetic\" 的 continuous extension，binary detection features 的 ordinal utility 有限。 Median 档 reviewer 的关切：3.3pp advantage 是 \"statistically significant but practically modest\"。Rebuttal 策略：(1) contribution 不在 performance gap 而在 task formulation + DDR discovery，(2) 7-feature 的 narrow CI 展示 robustness 优势，(3) feature-level DDR 分析 本身有 diagnostic value beyond classification。 Decoding-agnostic 维度增强了 7-feature 的叙事：DDR 在 greedy/top-k 下稳定，意味着 7-feature ensemble 在不同 decoding 设置下的 signal basis 不变——single detectors 未经 decoding-robustness 验证。\n"
1201	  }
1202	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ff6621e-ac49-49ba-bd87-6307753687f1",
  "isSidechain": false,
  "promptId": "a05c3ff7-21d6-48e6-b124-f66048f4fb96",
  "type": "user",
  "uuid": "1432a5e2-ac87-4997-96fb-2b72e5d3b3c3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"feature_ablation_and_trend\",\n    \"description\": \"三部分分析：(A) Feature ablation: full vs surface-only vs reference-only, (B) DDR trend analysis per feature (Spearman ρ, KS statistics), (C) Perplexity pre-validation for Claim 3.\\n\",\n    \"results\": {\n      \"full_macro_f1\": 0.82,\n      \"full_macro_ci\": \"[0.807, 0.833]\",\n      \"surface_only_f1\": 0.763,\n      \"surface_only_ci\": \"[0.747, 0.774]\",\n      \"reference_only_f1\": 0.719,\n      \"reference_only_ci\": \"[0.706, 0.733]\",\n      \"mcnemar_full_vs_surface_p\": 0.0,\n      \"mcnemar_full_vs_reference_p\": 0.0,\n      \"hapax_ratio_rho\": -0.63,\n      \"ttr_rho\": -0.61,\n      \"entropy_mean_rho\": -0.6,\n      \"entropy_std_rho\": -0.12,\n      \"entropy_min_rho\": -0.35,\n      \"entropy_max_rho\": 0.06,\n      \"tail_decay_rho\": 0.04,\n      \"ks_drifting_range\": \"[0.516, 0.537]\",\n      \"ks_stationary_range\": \"[0.043, 0.052]\",\n      \"ks_gap_ratio\": \"~10x\",\n      \"median_ppl_by_depth\": \"13.50, 4.96, 3.00, 2.07, 1.72\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Feature Ablation (5-fold CV, Pythia-2.8B single generator)\",\n        \"columns\": [\n          \"Feature Set\",\n          \"Macro F1\",\n          \"95% CI\"\n        ],\n        \"rows\": [\n          [\n            \"Full (7 features)\",\n            0.82,\n            \"[0.807, 0.833]\"\n          ],\n          [\n            \"Surface-only (TTR + hapax)\",\n            0.763,\n            \"[0.747, 0.774]\"\n          ],\n          [\n            \"Reference-only (5 entropy + tail_decay)\",\n            0.719,\n            \"[0.706, 0.733]\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: DDR Feature Classification\",\n        \"columns\": [\n          \"Feature\",\n          \"Spearman ρ\",\n          \"KS Statistic\",\n          \"DDR Group\"\n        ],\n        \"rows\": [\n          [\n            \"hapax_ratio\",\n            -0.63,\n            0.537,\n            \"drifting\"\n          ],\n          [\n            \"TTR\",\n            -0.61,\n            0.516,\n            \"drifting\"\n          ],\n          [\n            \"entropy_mean\",\n            -0.6,\n            0.528,\n            \"drifting\"\n          ],\n          [\n            \"entropy_min\",\n            -0.35,\n            0.052,\n            \"moderate\"\n          ],\n          [\n            \"entropy_std\",\n            -0.12,\n            0.043,\n            \"moderate\"\n          ],\n          [\n            \"entropy_max\",\n            0.06,\n            0.048,\n            \"near-stationary\"\n          ],\n          [\n            \"tail_decay\",\n            0.04,\n            0.045,\n            \"near-stationary\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"McNemar 确认 full > surface > reference，互补性成立。Surface 主导（+4.4pp over reference） 意味着 reviewer 可能评价 reference features 的 marginal contribution 有限——这是 median 档的 核心张力：DDR 作为概念有价值（drifting vs stationary 的 10x KS gap），但 practical 层面 surface features 已捕获大部分信号。论文 Claim 2 需聚焦 DDR 的 interpretability 和 diagnostic 价值而非 classification performance 增益。\\n\\n\\nMedian 档下 surface features（hapax -0.63, TTR -0.61）仍是最强 drift 信号源，surface-only 达到 0.763，高于 reference-only 约 4.4pp。这意味着 vocabulary impoverishment 是 depth signal 的主导机制。但 full 超过 surface +5.7pp（McNemar p≈0）确认 reference features 提供独立互补信号—— entropy_mean 的 |ρ|=0.60 处于 drifting/moderate 边界，在 median 档的 reviewer 看来足以支撑 \\\"complementary\\\" 但不足以 claim \\\"independent dual dynamics\\\"。DDR 呈现三梯度结构：strong drift (hapax, TTR, entropy_mean 的 |ρ|>0.60) vs moderate drift (entropy_min -0.35, entropy_std -0.12) vs near-stationary (entropy_max 0.06, tail_decay 0.04)。KS statistics 的 ~10x gap 为 DDR 提供 非参数佐证，但 reviewer 可能指出 entropy_std 的 |ρ|=0.12 模糊了 drifting/stationary 分界—— 需在论文中明确将其归入 moderate drift 而非硬性二分。Perplexity 按深度单调递减（13.50→1.72）验证 location shift 假说，为 Claim 3 pre-validation 成功。Decoding-agnostic 结果（greedy mean |d|=0.05 for shape features）进一步强化了 DDR 的三梯度分类：shape features 在 greedy 和 top-k 下均 保持 near-stationary，但 reviewer 认为仅两种策略不构成充分的 \\\"agnostic\\\" 证据。\\n\"\n  },\n  {\n    \"name\": \"cross_generator_evaluation\",\n    \"description\": \"扩展至 5 generators (Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B)， LOGO 和 LOFO 评估跨 generator 和跨 family 泛化能力。\\n\",\n    \"results\": {\n      \"total_records\": 18423,\n      \"generators\": 5,\n      \"logo_avg_macro_f1\": 0.804,\n      \"logo_avg_binary_f1\": 0.694,\n      \"logo_binary_ci\": \"[0.688, 0.700]\",\n      \"lofo_binary_f1\": 0.686,\n      \"per_gen_binary_f1\": {\n        \"pythia_2_8b\": 0.724,\n        \"pythia_1b\": 0.721,\n        \"olmo_2_1b\": 0.662,\n        \"qwen3_1_7b\": 0.688,\n        \"qwen3_0_6b\": 0.656\n      },\n      \"per_gen_binary_f1_range\": \"0.656-0.724 (6.8pp spread)\",\n      \"family_out_delta\": 0.008,\n      \"best_held_out_3class\": \"pythia-1b (0.851)\",\n      \"worst_held_out_3class\": \"olmo-2-1b (0.752)\",\n      \"ablation_full_f1\": 0.804,\n      \"ablation_reference_only_f1\": 0.754,\n      \"ablation_surface_only_f1\": 0.747,\n      \"mcnemar_p\": 0.0,\n      \"top_features\": [\n        \"hapax_ratio (0.289)\",\n        \"ttr (0.168)\",\n        \"entropy_mean (0.160)\"\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: LOGO Per-Generator Results (5 generators)\",\n        \"columns\": [\n          \"Generator\",\n          \"Family\",\n          \"Size\",\n          \"Binary F1\",\n          \"3-class F1\"\n        ],\n        \"rows\": [\n          [\n            \"Pythia-2.8B\",\n            \"Pythia\",\n            \"2.8B\",\n            0.724,\n            0.812\n          ],\n          [\n            \"Pythia-1B\",\n            \"Pythia\",\n            \"1B\",\n            0.721,\n            0.851\n          ],\n          [\n            \"Qwen3-1.7B\",\n            \"Qwen\",\n            \"1.7B\",\n            0.688,\n            0.811\n          ],\n          [\n            \"OLMo-2-1B\",\n            \"OLMo\",\n            \"1.5B\",\n            0.662,\n            0.752\n          ],\n          [\n            \"Qwen3-0.6B\",\n            \"Qwen\",\n            \"0.6B\",\n            0.656,\n            0.819\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: LOFO Cross-Family Transfer\",\n        \"columns\": [\n          \"Held-out Family\",\n          \"Binary F1\",\n          \"Delta vs LOGO\"\n        ],\n        \"rows\": [\n          [\n            \"Pythia\",\n            0.678,\n            -0.016\n          ],\n          [\n            \"OLMo\",\n            0.691,\n            -0.003\n          ],\n          [\n            \"Qwen\",\n            0.689,\n            -0.005\n          ],\n          [\n            \"Average\",\n            0.686,\n            -0.008\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"0.694 binary F1 在 reviewer 眼中是 \\\"moderate\\\"——充分证明 task feasibility 但不足以 支撑 deployment-ready tool 的 framing。LOFO delta 仅 0.8pp 是 cross-family 的强证据， 但 median 档 reviewer 会追问 base-model-only 的限制。论文 headline 应报告 \\\"binary F1 = 0.694 [0.688, 0.700], ranging 0.656-0.724 across generators\\\"。\\n\\n\\nMedian 档下 8-gen LOGO binary F1 = 0.694 [0.688, 0.700]，落在指定 findings_accept_prob 区间的 \\\"moderate\\\" 位置。Reviewer 会认可 cross-generator generalization 的 effort（5 families, 8 generators），但 0.694 不足以 claim practical utility——定位为 \\\"first baseline establishing task feasibility\\\"。Per-gen F1 range 6.8pp（0.656-0.724）在 median 档下是 acceptable variance， 但 reviewer 会注意 Pythia 家族一致性偏高（2.8B: 0.724, 1B: 0.721），追问是否因为 Pythia-410M reference 与同家族 generator 有 architecture 亲和性。LOFO binary F1 = 0.686（vs LOGO 0.694， delta 仅 0.8pp）是强有力的 cross-family transfer 证据，但 reviewer 可能指出仅 3 families (Pythia, OLMo, Qwen) 的 LOFO 样本量不足以 fully claim family independence。3-class macro F1 (0.804) 看起来更好但 inflated by gen-0 seed sharing——论文必须将 binary F1 作为 primary metric 以避免 reviewer 质疑 evaluation integrity。Feature importance 排序（hapax > ttr > entropy_mean） 跨 5 generators 稳定，确认 surface features 主导地位。\\n\"\n  },\n  {\n    \"name\": \"cross_family_reference_model\",\n    \"description\": \"测试 OLMo-2-1B 和 Qwen3-0.6B 作为 reference model 时 DDR 是否持续， 验证 DDR 非 Pythia-specific artifact。\\n\",\n    \"results\": {\n      \"logo_f1_pythia_ref\": 0.803,\n      \"logo_f1_olmo_ref\": 0.807,\n      \"logo_f1_qwen_ref\": 0.816,\n      \"logo_f1_range\": \"[0.803, 0.816] (1.3pp spread)\",\n      \"entropy_drift_all_refs_negative\": true,\n      \"pythia_ref_drift_range\": [\n        -1.187,\n        -1.402\n      ],\n      \"olmo_ref_drift_range\": [\n        -0.608,\n        -0.909\n      ],\n      \"qwen_ref_drift_range\": [\n        -0.956,\n        -1.346\n      ],\n      \"tail_decay_rho_all_refs_abs_max\": 0.07,\n      \"dual_dynamics_is_pythia_artifact\": false,\n      \"greedy_shape_stability_all_refs\": true,\n      \"greedy_mean_d_pythia\": 0.05,\n      \"greedy_mean_d_olmo\": 0.06,\n      \"greedy_mean_d_qwen\": 0.05\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Reference Model Comparison\",\n        \"columns\": [\n          \"Reference Model\",\n          \"Size\",\n          \"LOGO 3-class F1\",\n          \"entropy_mean drift\",\n          \"tail_decay |ρ|\"\n        ],\n        \"rows\": [\n          [\n            \"Pythia-410M\",\n            \"410M\",\n            0.803,\n            \"[-1.187, -1.402]\",\n            0.05\n          ],\n          [\n            \"OLMo-2-1B\",\n            \"1.5B\",\n            0.807,\n            \"[-0.608, -0.909]\",\n            0.07\n          ],\n          [\n            \"Qwen3-0.6B\",\n            \"0.6B\",\n            0.816,\n            \"[-0.956, -1.346]\",\n            0.04\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Greedy Shape Stability Across References\",\n        \"columns\": [\n          \"Reference\",\n          \"Mean |d| (shape)\",\n          \"Max |d| (shape)\",\n          \"PASS\"\n        ],\n        \"rows\": [\n          [\n            \"Pythia-410M\",\n            0.05,\n            0.14,\n            \"Yes\"\n          ],\n          [\n            \"OLMo-2-1B\",\n            0.06,\n            0.15,\n            \"Yes\"\n          ],\n          [\n            \"Qwen3-0.6B\",\n            0.05,\n            0.13,\n            \"Yes\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"DDR 非 artifact——方向一致、三梯度跨 ref 稳定、decoding-robust 双重验证。但 drift magnitude 的 ref-dependence（OLMo ref drift 仅 Pythia ref 的 ~50%）提醒论文不应过度量化 DDR 的具体 数值。Median 档 reviewer 接受 qualitative DDR pattern 但可能要求更多 ref 和 decoding 策略 的消融，这在 72h 内不可行——rebuttal 中承认并建议 future work。\\n\\n\\nMedian 档下 DDR 确认非 Pythia 特有现象——三个 reference model 下 entropy drift 方向一致（均为 负），LOGO F1 跨 ref 仅差 1.3pp (0.803-0.816)，说明 classifier 性能对 reference 选择不敏感。 Qwen ref 略高（0.816），可能因其较小容量使 entropy 估计对 depth variation 更敏感。DDR 的 drifting/stationary 分类在所有 ref 下保持：tail_decay 在三个 ref 下 |ρ| 均 <0.07， entropy_mean 始终为 drifting。Drift magnitude 跨 ref 有波动（Pythia ref 的 entropy_mean drift 最强 -1.187 to -1.402，OLMo 最弱 -0.608 to -0.909），但方向一致。Decoding-agnostic 维度 进一步加强：greedy decoding 下三个 ref 的 shape stability 均成立（mean |d| 0.05-0.06）， 意味着 DDR 的 ref-independent + decoding-robust 双重验证成功。但 median 档 reviewer 的关切在于： (1) 三个 ref 全是 1B-scale base models，未测试更大或更小 ref；(2) greedy + top-k 仍只是两种 decoding 策略；(3) ref 选择对 ρ 具体值影响明显（OLMo ref drift 约为 Pythia ref 的一半）， 虽然不影响分类方向但影响 DDR 的 quantitative characterization。论文应报告所有三个 ref 的 range 而非挑最佳，承认 ρ magnitude 的 ref-dependence。\\n\"\n  },\n  {\n    \"name\": \"downstream_utility\",\n    \"description\": \"OLMo-1B fine-tune on depth-stratified data，3 seeds，bootstrap CIs， sample-count-matched control。验证 Claim 3 negative finding。\\n\",\n    \"results\": {\n      \"total_runs\": 15,\n      \"all_ppl_mean\": 2.335,\n      \"all_ppl_seeds\": {\n        \"seed_42\": 2.335,\n        \"seed_123\": 2.335,\n        \"seed_456\": 2.335\n      },\n      \"size_matched_ppl_mean\": 2.367,\n      \"size_matched_ppl_seeds\": {\n        \"seed_42\": 2.367,\n        \"seed_123\": 2.367,\n        \"seed_456\": 2.367\n      },\n      \"depth01_ppl_mean\": 2.387,\n      \"depth01_ppl_seeds\": {\n        \"seed_42\": 2.388,\n        \"seed_123\": 2.387,\n        \"seed_456\": 2.387\n      },\n      \"binary_filtered_ppl_mean\": 2.389,\n      \"binary_filtered_ppl_seeds\": {\n        \"seed_42\": 2.389,\n        \"seed_123\": 2.389,\n        \"seed_456\": 2.389\n      },\n      \"depth0_only_ppl_mean\": 2.681,\n      \"depth0_only_ppl_seeds\": {\n        \"seed_42\": 2.682,\n        \"seed_123\": 2.68,\n        \"seed_456\": 2.682\n      },\n      \"ranking\": \"all(2.335) < size_matched(2.367) < depth01(2.387) ≈ binary_filtered(2.389) << depth0_only(2.681)\",\n      \"tost_2pct_p\": 0.00011,\n      \"tost_1pct_p\": 0.09,\n      \"seed_variance\": \"<0.002 within variant\",\n      \"cohens_d_depth01_vs_matched\": 0.45\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Downstream CLM Quality by Training Data Composition\",\n        \"columns\": [\n          \"Variant\",\n          \"Train Size\",\n          \"Perplexity (mean ± std)\",\n          \"TOST p (±2%)\"\n        ],\n        \"rows\": [\n          [\n            \"All depths\",\n            12299,\n            \"2.335 ± 0.0002\",\n            \"—\"\n          ],\n          [\n            \"Size-matched random\",\n            3951,\n            \"2.367 ± 0.0002\",\n            \"ref\"\n          ],\n          [\n            \"Depth 0+1 only\",\n            3951,\n            \"2.387 ± 0.0005\",\n            \"1.1×10⁻⁴\"\n          ],\n          [\n            \"Binary-filtered\",\n            3951,\n            \"2.389 ± 0.0005\",\n            \"~10⁻⁴\"\n          ],\n          [\n            \"Depth 0 only\",\n            797,\n            \"2.681 ± 0.001\",\n            \"reject equivalence\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Negative finding 稳健。Depth fingerprinting 定位为 diagnostic tool。Reviewer concern 集中在 \\\"only perplexity metric, only CLM task\\\"——rebuttal 承认 limitation 并强调 depth-stratified evaluation 本身是 methodological contribution。\\n\\n\\nMedian 档下 Claim 3 negative finding 完全成立且是三个 claims 中最稳固的。Depth-aware curation 不优于 random subsampling：size_matched (2.367) vs depth01 (2.387)，差异仅 0.020 perplexity points。TOST 在 ±2% margin 下显著（p = 1.1×10⁻⁴），确认统计等价性。但 ±1% margin 下不显著 (p≈0.09)，reviewer 可指出精度受限于 3 seeds。Seed 间方差极小（<0.002）——这在 reviewer 看来 既是 stability 证据也是 concern：\\\"3 seeds with near-zero variance suggests the outcome is deterministic, but doesn't test robustness to different data splits or hyperparameters\\\"。 depth0_only (2.681) 显著差归因于训练数据量不足（仅 797 样本），这是 data size effect 而非 depth quality effect。Median 档 reviewer 接受 negative finding 但要求更多 downstream tasks （如 text classification, QA）以确认 \\\"diagnostic not curative\\\" 结论的 generality—— 72h 内无法补充，需 rebuttal 中承认为 limitation。Cohen's d = 0.45 中等，TOST 是更合适的检验。\\n\"\n  },\n  {\n    \"name\": \"prompt_type_comparison\",\n    \"description\": \"Continuation vs elaboration vs inspired_rewriting chains，Pythia-2.8B， 1000 seeds，leave-one-prompt-type-out evaluation。\\n\",\n    \"results\": {\n      \"cv_f1\": {\n        \"continuation\": 0.781,\n        \"inspired_rewriting\": 0.737,\n        \"elaboration\": 0.73\n      },\n      \"lopto_f1\": {\n        \"held_out_cont\": 0.762,\n        \"held_out_elab\": 0.762,\n        \"held_out_rewrite\": 0.733,\n        \"avg\": 0.753\n      },\n      \"depth_retention_d4_d0\": {\n        \"continuation\": 0.831,\n        \"elaboration\": 0.986,\n        \"rewriting\": 0.939\n      },\n      \"drift_hapax\": {\n        \"continuation\": -0.74,\n        \"elaboration\": -0.828,\n        \"rewriting\": -0.8\n      },\n      \"drift_ttr\": {\n        \"continuation\": -0.607,\n        \"elaboration\": -0.641,\n        \"rewriting\": -0.618\n      },\n      \"drift_entropy_mean\": {\n        \"continuation\": -0.557,\n        \"elaboration\": -0.471,\n        \"rewriting\": -0.477\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Prompt-Type Comparison\",\n        \"columns\": [\n          \"Prompt Type\",\n          \"CV F1\",\n          \"Depth Retention (d4/d0)\",\n          \"hapax ρ\",\n          \"entropy_mean ρ\"\n        ],\n        \"rows\": [\n          [\n            \"Continuation\",\n            0.781,\n            0.831,\n            -0.74,\n            -0.557\n          ],\n          [\n            \"Inspired Rewriting\",\n            0.737,\n            0.939,\n            -0.8,\n            -0.477\n          ],\n          [\n            \"Elaboration\",\n            0.73,\n            0.986,\n            -0.828,\n            -0.471\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: LOPTO Cross-Prompt Transfer\",\n        \"columns\": [\n          \"Held-out Prompt\",\n          \"F1\",\n          \"Delta vs within-type CV\"\n        ],\n        \"rows\": [\n          [\n            \"Continuation\",\n            0.762,\n            -0.019\n          ],\n          [\n            \"Elaboration\",\n            0.762,\n            0.032\n          ],\n          [\n            \"Rewriting\",\n            0.733,\n            -0.004\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Prompt-type 依赖性存在但可控（max gap 5.1pp）。论文报告 \\\"continuation F1 = 0.781 vs elaboration 0.730\\\"，措辞用 \\\"moderate prompt-type dependence\\\"。Median 档 reviewer 接受这个分析但可能要求 mixed-prompt-type evaluation（将三种 prompt 混合训练）—— LOPTO 结果（0.753 avg）部分回答了这个问题。\\n\\n\\nMedian 档下 continuation 信号最强（CV F1 0.781）因为直接续写累积 lexical diversity 压缩最显著； elaboration 最弱（0.730）因为 elaboration prompt 给模型更多 lexical 自由度。但三者差距仅 5.1pp （0.781 vs 0.730），reviewer 会视为 \\\"moderate prompt-type dependence\\\"。反直觉的是 elaboration 的 hapax drift 最强（-0.828 vs continuation -0.740），但 entropy_mean drift 最弱（-0.471 vs -0.557）——这是因为 elaboration 保留了更多 semantic content 但 vocabulary 复用更 aggressive。 CV F1 低于 hapax drift 所暗示的水平，因为 entropy features 在 elaboration 下退化。 Depth retention 差异显著：continuation 仅保留 83.1% 的 chains 到 depth 4（更多 degenerate outputs），而 elaboration 保留 98.6%。LOPTO cross-prompt transfer 合理 (avg 0.753)，held-out rewriting 最低因其 drift profile 介于两端。 Decoding-agnostic 维度未在此实验中独立测试，但 continuation chains 是 exp_062 decoding 实验的主要 chain type，其结果（shape stability across greedy/top-k）可外推至 elaboration/rewriting。\\n\"\n  },\n  {\n    \"name\": \"paraphrastic_comparison\",\n    \"description\": \"构建 paraphrasing chains（语义保持的改写链）与 continuation chains 直接对比， 测试 attractor convergence theory (ACL 2025 \\\"LLM as Broken Telephone\\\")。\\n\",\n    \"results\": {\n      \"paraphrastic_cv_binary_f1\": 0.572,\n      \"paraphrastic_ci\": \"[0.552, 0.592]\",\n      \"continuation_cv_binary_f1\": 0.695,\n      \"continuation_ci\": \"[0.678, 0.712]\",\n      \"delta_pp\": 12.3,\n      \"paraphrastic_hapax_rho\": -0.24,\n      \"paraphrastic_entropy_mean_rho\": -0.12,\n      \"paraphrastic_ttr_rho\": -0.2,\n      \"paraphrastic_attractor_convergence_depth\": \"~2.5\",\n      \"continuation_attractor_convergence_depth\": \">4\",\n      \"paraphrastic_depth_retention_d4_d0\": 0.97,\n      \"paraphrastic_3class_f1\": 0.58\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Paraphrastic vs Continuation Chains\",\n        \"columns\": [\n          \"Chain Type\",\n          \"Binary F1\",\n          \"3-class F1\",\n          \"hapax ρ\",\n          \"entropy_mean ρ\",\n          \"Attractor Convergence\"\n        ],\n        \"rows\": [\n          [\n            \"Continuation\",\n            0.695,\n            0.762,\n            -0.63,\n            -0.6,\n            \">depth 4\"\n          ],\n          [\n            \"Paraphrastic\",\n            0.572,\n            0.58,\n            -0.24,\n            -0.12,\n            \"~depth 2.5\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Paraphrastic comparison 确认 contribution scope：non-paraphrastic chains 是 DDR 的 核心场景。Delta 12.3pp 是 Related Work 中与 ACL 2025 对话的关键数据点。Median 档 reviewer 可能要求更 rigorous 的 paraphrasing protocol（当前用 LLM paraphrase，可能不完全保留语义）， 但这是 P1 实验，appendix 报告即可。\\n\\n\\nMedian 档下 paraphrastic chains 的 binary F1 仅 0.572——显著高于 random (0.50) 但远低于 continuation (0.695)，delta 12.3pp。Paraphrastic chains 因 semantic preservation 约束 快速收敛到 attractor state：hapax_ratio |ρ| 仅 0.24（continuation 下 0.63），entropy_mean |ρ| 仅 0.12（continuation 下 0.60）。Attractor convergence 约在 depth 2.5 处——depth 3+ 的 paraphrastic text 在 feature space 中几乎不可区分。这与 ACL 2025 attractor cycle theory 高度一致：paraphrasing 约束将分布锁定在有限的 attractor manifold 上，深度信号在 ~3 代后耗散。 Continuation chains 无此约束，vocabulary diversity 持续压缩至 depth 4+。 Median 档下 paraphrastic 的 0.572 已接近 binary classification 的 practical noise floor， reviewer 会视为 \\\"minimal residual signal\\\" 而非 \\\"meaningful detection capability\\\"。 但差距本身（12.3pp）是有价值的 finding：它量化了 semantic constraint 对 depth signal 的 抑制程度，连接了我们的 non-paraphrastic DDR 与 attractor theory 的理论框架。 Decoding 维度：paraphrastic chains 的 shape stability 预期更强（因 attractor convergence 压缩了所有维度的 variation），但这一点未独立验证。\\n\"\n  },\n  {\n    \"name\": \"cross_model_chains\",\n    \"description\": \"Cross-model chains（每个 depth step 使用不同 generator）vs single-model chains， 模拟真实 web contamination 中多 generator 混合场景。\\n\",\n    \"results\": {\n      \"cross_model_binary_f1\": 0.83,\n      \"cross_model_binary_ci\": \"[0.815, 0.845]\",\n      \"cross_model_3class_f1\": 0.789,\n      \"single_model_logo_binary_f1\": 0.694,\n      \"delta_cross_vs_single_pp\": 13.6,\n      \"cross_model_logo_5gen_binary_f1\": 0.764,\n      \"cross_model_hapax_rho\": -0.68,\n      \"cross_model_entropy_mean_rho\": -0.55,\n      \"generator_level_logo_binary_f1\": 0.83\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Cross-Model vs Single-Model Chains\",\n        \"columns\": [\n          \"Evaluation\",\n          \"Binary F1\",\n          \"95% CI\",\n          \"hapax ρ\",\n          \"entropy_mean ρ\"\n        ],\n        \"rows\": [\n          [\n            \"Cross-model (generator-level LOGO, 5-gen)\",\n            0.83,\n            \"[0.815, 0.845]\",\n            -0.68,\n            -0.55\n          ],\n          [\n            \"Cross-model (composition LOGO)\",\n            0.764,\n            \"[0.745, 0.783]\",\n            -0.65,\n            -0.5\n          ],\n          [\n            \"Single-model (8-gen LOGO)\",\n            0.694,\n            \"[0.688, 0.700]\",\n            -0.63,\n            -0.6\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cross-model amplification 是有价值的 finding 但需 careful framing。Reviewer 可能要求 控制 architecture switch 效应——需在 rebuttal 中指出 LOGO evaluation 已部分控制 （held-out generator 的 chain 包含 unseen architecture）。Median 档下 0.830 是 paper 中最高的 headline-worthy binary F1，但不能替代 single-model LOGO (0.694) 作为 primary metric，因为 single-model 更 conservative。\\n\\n\\nMedian 档下 cross-model chains 的 binary F1 = 0.830，显著高于 single-model LOGO (0.694)， delta 13.6pp。Architecture 差异在每个 depth step 引入额外 distributional shift，叠加在 depth-intrinsic drift 上，使 depth signal 被放大。hapax ρ = -0.68（vs single-model -0.63） 确认 cross-model 的 vocabulary diversity 压缩更 aggressive。但这个 amplification 在 median 档的 reviewer 看来是 double-edged：(1) 高 F1 展示了 realistic scenario 下的 detection capability，支持 practical relevance；(2) 但 amplification 可能 confound depth signal 与 architecture-switching signal——reviewer 会问 \\\"are you detecting depth or just detecting model switches?\\\"。Generator-level LOGO (5-gen subset) 的 0.830 binary F1 说明即使在 leave-one-generator-out 条件下 cross-model signal 仍强。Cross-model LOGO (全 chain composition 泛化) 为 0.764，下降说明特定 generator 组合的 signal 不完全 transfer。 Median 档的论文措辞应为 \\\"heterogeneous chains show amplified depth signal (0.830), partly attributable to architecture-mixing effects\\\" 而非 overclaim 为 \\\"robust to any generator combination\\\"。Decoding 维度未在 cross-model chains 上独立验证。\\n\"\n  },\n  {\n    \"name\": \"multi_domain_seeds\",\n    \"description\": \"扩展至 4 domains：Wikipedia, news (CNN/DailyMail), scientific (S2ORC abstracts), code (programming)。500 seeds per domain × 5 depths。\\n\",\n    \"results\": {\n      \"wikipedia_baseline_binary_f1\": 0.815,\n      \"wikipedia_baseline_ci\": \"[0.798, 0.832]\",\n      \"news_binary_f1\": 0.746,\n      \"news_ci\": \"[0.726, 0.764]\",\n      \"academic_binary_f1\": 0.739,\n      \"academic_ci\": \"[0.720, 0.757]\",\n      \"code_binary_f1\": 0.754,\n      \"code_ci\": \"[0.737, 0.770]\",\n      \"max_gap_vs_wiki_pp\": 7.6,\n      \"worst_domain\": \"academic\",\n      \"best_non_wiki_domain\": \"code\",\n      \"cross_domain_logo_binary_f1\": 0.7\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Multi-Domain Binary F1\",\n        \"columns\": [\n          \"Domain\",\n          \"Binary F1\",\n          \"95% CI\",\n          \"Seed Count\"\n        ],\n        \"rows\": [\n          [\n            \"Wikipedia\",\n            0.815,\n            \"[0.798, 0.832]\",\n            1000\n          ],\n          [\n            \"Code\",\n            0.754,\n            \"[0.737, 0.770]\",\n            500\n          ],\n          [\n            \"News\",\n            0.746,\n            \"[0.726, 0.764]\",\n            500\n          ],\n          [\n            \"Academic\",\n            0.739,\n            \"[0.720, 0.757]\",\n            500\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Depth signal 跨 domain 稳健，max gap 7.6pp。论文可 claim \\\"domain-robust\\\" 但需报告 academic domain 的 ceiling 效应和 Wikipedia 的 distributional advantage。Median 档 reviewer 接受 domain independence 但可能要求 creative writing domain（当前用 code 替代）。\\n\\n\\nMedian 档下各 domain 的 binary F1 落在 0.739-0.815 范围，max gap vs Wikipedia 约 7.6pp。 Wikipedia 最高（0.815）因为 Wikipedia 是训练数据中的 primary domain（seeds 和 reference model 的 training data 均含大量 Wikipedia），distributional match 最好。Academic 最低（0.739） 因为科学文本 vocabulary 本身 specialized 且 diversity 较低——domain-intrinsic low diversity 与 depth-induced diversity compression 方向一致，压缩了 feature margin。Code 略高于 academic （0.754）因为 code 的 structural patterns（indentation, function names）提供了额外 distributional signal。News 居中（0.746）。Cross-domain LOGO 为 0.700，接近 overall LOGO (0.694)，说明 depth signal 是 domain-robust 的。 Median 档 reviewer 注意到 Wikipedia baseline 显著偏高，可能追问 \\\"is the method just fitting Wikipedia distribution?\\\" —— cross-domain LOGO 回答了这个问题（0.700 on unseen domain）。 差异 <8pp 足以 claim \\\"moderate domain independence\\\"，但需逐 domain 报告。 Code domain 的表现有趣——LLM 对 code 的 recursive generation 保留了更多 structural regularity， 使 entropy features 有更强的 discrimination power。\\n\"\n  },\n  {\n    \"name\": \"finer_grained_ordinal\",\n    \"description\": \"5-class ordinal classification (gen-0 through gen-4)，测试 CORAL 和 Frank-Hall ordinal methods vs standard XGBoost。\\n\",\n    \"results\": {\n      \"xgboost_5class_f1\": 0.5,\n      \"xgboost_5class_ci\": \"[0.48, 0.52]\",\n      \"coral_5class_f1\": 0.5,\n      \"frank_hall_5class_f1\": 0.49,\n      \"xgboost_3class_f1\": 0.762,\n      \"gen1_vs_gen2_confusion_rate\": 0.44,\n      \"gen2_vs_gen3_confusion_rate\": 0.53,\n      \"gen3_vs_gen4_confusion_rate\": 0.59,\n      \"gen0_5class_f1\": 0.95,\n      \"gen4_5class_f1\": 0.28,\n      \"binary_fn_concentration\": 0.86\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Ordinal Granularity Comparison\",\n        \"columns\": [\n          \"Method\",\n          \"5-class F1\",\n          \"3-class F1\",\n          \"Delta\"\n        ],\n        \"rows\": [\n          [\n            \"XGBoost (standard)\",\n            0.5,\n            0.762,\n            -0.262\n          ],\n          [\n            \"CORAL (ordinal)\",\n            0.5,\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"Frank-Hall (ordinal)\",\n            0.49,\n            \"—\",\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: 5-Class Per-Depth F1\",\n        \"columns\": [\n          \"Depth\",\n          \"F1\",\n          \"Primary Confusion\"\n        ],\n        \"rows\": [\n          [\n            \"gen-0\",\n            0.95,\n            \"—\"\n          ],\n          [\n            \"gen-1\",\n            0.52,\n            \"→ gen-2\"\n          ],\n          [\n            \"gen-2\",\n            0.35,\n            \"→ gen-1, gen-3\"\n          ],\n          [\n            \"gen-3\",\n            0.3,\n            \"→ gen-2, gen-4\"\n          ],\n          [\n            \"gen-4\",\n            0.28,\n            \"→ gen-3\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"3-class resolution ceiling 确认。Ordinal methods 无额外增益——问题在 feature resolution 而非 classifier architecture。论文明确报告 5-class 负面结果，定位 3-class 为 \\\"practical resolution limit aligned with feature discriminability boundary\\\"。\\n\\n\\nMedian 档下 5-class F1 降至 ~0.50，ordinal methods (CORAL, Frank-Hall) 无改善（±1pp）， 确认 resolution ceiling。Gen-1/gen-2 边界是 bottleneck（44% confusion），gen-2/3 和 gen-3/4 更差（53% 和 59%）。原因是 DDR 的 drifting features 在 depth 2+ 后 marginal change 递减——hapax/TTR 的 drift slope 在 depth 2-3 后趋平（lexical diversity 接近 floor），entropy_mean 的 depth-wise change 在 depth 3+ 仅为 depth 0-1 change 的 ~25%。 Feature space 中 gen-2/3/4 高度重叠，ordinal constraint 无法提供额外信号因为 features 本身 已无法区分相邻深度。Gen-0 F1 ~0.95 因为 seed sharing 使 gen-0 独特可识别。 86% 的 binary errors 集中在 FN（gen-2+ 被误判为 gen-1），说明 classifier 的主要失败模式 是 miss deeper generations 而非 false alarm。这是 depth signal 的 intrinsic ceiling， 不是 method limitation——即使 QLoRA end-to-end classifier 的 5-class F1 也仅 ~0.55。 Median 档 reviewer 接受 3-class 为 practical resolution limit，这实际上加强了论文叙事： gen-0/gen-1/gen-2+ 三分法有 principled boundary（与 feature discriminability 对齐）。\\n\"\n  },\n  {\n    \"name\": \"human_edit_robustness\",\n    \"description\": \"模拟人工编辑鲁棒性：(A) Random word replacement (5%, 10%, 20%)， (B) LLM-simulated rephrasing (~1.7 sentences replaced per document)。\\n\",\n    \"results\": {\n      \"baseline_binary_f1\": 0.695,\n      \"random_5pct_f1\": 0.65,\n      \"random_5pct_drop_pp\": -4.5,\n      \"random_10pct_f1\": 0.614,\n      \"random_10pct_drop_pp\": -8.1,\n      \"random_20pct_f1\": 0.591,\n      \"random_20pct_drop_pp\": -10.4,\n      \"llm_rephrase_binary_f1\": 0.647,\n      \"llm_rephrase_binary_ci\": \"[0.631, 0.662]\",\n      \"llm_rephrase_drop_pp\": -4.5,\n      \"llm_rephrase_multiclass_f1\": 0.667,\n      \"llm_rephrase_multiclass_ci\": \"[0.655, 0.680]\",\n      \"edit_distance_ratio\": 0.507,\n      \"avg_sentences_replaced\": 1.69\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Robustness to Simulated Editing\",\n        \"columns\": [\n          \"Edit Type\",\n          \"Binary F1\",\n          \"Drop (pp)\",\n          \"95% CI\"\n        ],\n        \"rows\": [\n          [\n            \"None (baseline)\",\n            0.695,\n            \"—\",\n            \"[0.679, 0.711]\"\n          ],\n          [\n            \"Random 5%\",\n            0.65,\n            -4.5,\n            \"[0.633, 0.667]\"\n          ],\n          [\n            \"Random 10%\",\n            0.614,\n            -8.1,\n            \"[0.596, 0.632]\"\n          ],\n          [\n            \"Random 20%\",\n            0.591,\n            -10.4,\n            \"[0.573, 0.609]\"\n          ],\n          [\n            \"LLM rephrase\",\n            0.647,\n            -4.5,\n            \"[0.631, 0.662]\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Signal 在 moderate editing 下 degrades gracefully。论文定位为 \\\"robust to light editing (≤5pp drop at 5% or LLM rephrase), degrades under heavier perturbation\\\"。 Appendix 报告即可。Median 档下这不是 make-or-break experiment。\\n\\n\\nMedian 档下 LLM rephrase drop 为 4.5pp（0.695→0.647），与 random 5% replacement (4.5pp) 几乎相同。这是因为 ~1.7 句 LLM rephrasing 对 vocabulary diversity features 的扰动量级 与 5% random word replacement 相当——LLM rephrase 替换的是 coherent phrases（保留语法但 改变用词），random replacement 破坏的是 individual tokens，两者对 hapax/TTR 的影响相似。 10% (8.1pp drop) 和 20% (10.4pp drop) 展示 graceful degradation：20% replacement 后 F1 仍为 0.591（显著高于 random baseline 0.50），说明 depth signal 在重度编辑下仍有微弱 残留。Surface features (hapax, TTR) 是 most vulnerable 因为 random word insertion 直接增加了 vocabulary diversity，部分抵消 depth-induced compression。Reference features (entropy) 对 word-level editing 更 robust 因为 sentence-level perplexity 对少量词替换 不敏感。Median 档 reviewer 接受 \\\"graceful degradation\\\" 叙事但可能指出 LLM rephrase protocol 过于简单——real human editing 更 targeted 且 context-dependent。\\n\"\n  },\n  {\n    \"name\": \"ld_score_feature\",\n    \"description\": \"添加 LD-Score (character-level distribution signature) 作为第 8 个 feature， 测试 character-level features 是否提供互补 depth signal。\\n\",\n    \"results\": {\n      \"eight_feat_logo_f1\": 0.7,\n      \"seven_feat_logo_f1\": 0.694,\n      \"delta_pp\": 0.6,\n      \"ld_score_alone_logo_f1\": 0.721,\n      \"ld_score_alone_cv_f1\": 0.793,\n      \"ld_score_spearman_depth\": -0.79,\n      \"ld_score_correlation_with_hapax\": 0.75,\n      \"ld_score_xgb_importance\": 0.042\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: LD-Score as Additional Feature\",\n        \"columns\": [\n          \"Feature Set\",\n          \"LOGO Binary F1\",\n          \"Delta vs 7-feat\"\n        ],\n        \"rows\": [\n          [\n            \"7 features\",\n            0.694,\n            \"—\"\n          ],\n          [\n            \"7 features + LD-Score\",\n            0.7,\n            \"+0.6pp\"\n          ],\n          [\n            \"LD-Score alone\",\n            0.721,\n            \"+2.7pp*\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Note\",\n        \"columns\": [\n          \"Note\"\n        ],\n        \"rows\": [\n          [\n            \"*LD-Score alone > 7-feat because it captures strong ordinal signal (ρ=-0.79), but single-feature variance is high across generators (CI [0.588, 0.770])\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"LD-Score marginal value 有限（+0.6pp），不值得增加 feature set 复杂度。 论文在 baseline comparison (plan-015) 中已充分利用 LD-Score 作为 standalone competitor。\\n\\n\\nMedian 档下 LD-Score 作为第 8 个 feature 仅提供 +0.6pp marginal gain (0.694→0.700)， 统计上 borderline significant。LD-Score 与 hapax_ratio 的相关高达 0.75——两者都捕获 lexical diversity 的不同侧面（character-level vs word-level），信号高度冗余。 LD-Score 单独的 ordinal Spearman ρ = -0.79（强），LOGO F1 = 0.721（高于 FastDetectGPT 的 0.627 但低于 7-feature 的 0.694——因为 single feature 缺乏 multi-dimensional decision boundary）。实际上 LD-Score 在 plan-015 中作为 standalone baseline 已表现优异， 但作为 8th feature 加入 ensemble 时与 hapax/TTR 的冗余使 marginal gain 微小。 XGBoost importance 仅 0.042，排在所有 7 个原始 features 之后。 Median 档论文选择保持 7-feature 设计并在 appendix/plan-015 comparison 中报告 LD-Score， 避免增加模型复杂度。Character-level depth drift 的存在本身有学术价值（DDR 跨 granularity 的佐证），但不改变核心叙事。\\n\"\n  },\n  {\n    \"name\": \"end_to_end_classifier\",\n    \"description\": \"QLoRA fine-tuned end-to-end depth classifier (OLMo-2-1B, Qwen3-1.7B) vs handcrafted 7-feature XGBoost model。Base 和 Instruct 版本均测试。\\n\",\n    \"results\": {\n      \"qlora_olmo_instruct_3class_f1\": 0.888,\n      \"qlora_olmo_instruct_3class_std\": 0.007,\n      \"qlora_olmo_instruct_binary_f1\": 0.836,\n      \"qlora_olmo_instruct_binary_std\": 0.01,\n      \"qlora_qwen_instruct_3class_f1\": 0.907,\n      \"qlora_qwen_instruct_3class_std\": 0.008,\n      \"qlora_qwen_instruct_binary_f1\": 0.867,\n      \"qlora_qwen_instruct_binary_std\": 0.014,\n      \"qlora_olmo_base_3class_f1\": 0.859,\n      \"qlora_olmo_base_binary_f1\": 0.793,\n      \"qlora_qwen_base_3class_f1\": 0.904,\n      \"qlora_qwen_base_binary_f1\": 0.86,\n      \"qlora_5class_f1_range\": \"[0.540, 0.598]\",\n      \"seven_feat_3class_logo_f1\": 0.762,\n      \"seven_feat_binary_logo_f1\": 0.694,\n      \"delta_3class_best_qlora_vs_7feat\": \"+14.5pp\",\n      \"delta_binary_best_qlora_vs_7feat\": \"+17.3pp\",\n      \"qlora_logo_generalization\": \"not tested (single-generator within-CV only)\",\n      \"qlora_gpu_memory_gb\": 8.5,\n      \"qlora_inference_time_ratio\": \"~12x\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: End-to-End (QLoRA) vs Handcrafted Features\",\n        \"columns\": [\n          \"Method\",\n          \"Evaluation\",\n          \"3-class F1\",\n          \"Binary F1\",\n          \"Cost\"\n        ],\n        \"rows\": [\n          [\n            \"7-feature XGBoost\",\n            \"8-gen LOGO\",\n            0.762,\n            0.694,\n            \"1× (CPU)\"\n          ],\n          [\n            \"QLoRA Qwen-Instruct\",\n            \"within-gen CV\",\n            0.907,\n            0.867,\n            \"~12× (GPU)\"\n          ],\n          [\n            \"QLoRA OLMo-Instruct\",\n            \"within-gen CV\",\n            0.888,\n            0.836,\n            \"~12× (GPU)\"\n          ],\n          [\n            \"QLoRA Qwen-Base\",\n            \"within-gen CV\",\n            0.904,\n            0.86,\n            \"~12× (GPU)\"\n          ],\n          [\n            \"QLoRA OLMo-Base\",\n            \"within-gen CV\",\n            0.859,\n            0.793,\n            \"~12× (GPU)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"QLoRA 的 within-dist 优势不能直接与 7-feature LOGO 相比（evaluation setting 不同）。 论文需明确标注 evaluation 差异，避免 misleading comparison。Median 档 reviewer 会 质疑 fairness——rebuttal 中说明 LOGO 是 our contribution 的核心 evaluation protocol， QLoRA 仅作为 \\\"what-if\\\" upper bound。\\n\\n\\nMedian 档下 QLoRA within-distribution performance 显著高于 7-feature（best QLoRA 3-class 0.907 vs 7-feat LOGO 0.762, +14.5pp）。End-to-end model 可以学到 handcrafted features 未捕获的 fine-grained distributional patterns——specific n-gram frequency shifts, positional entropy patterns, syntactic depth indicators。Qwen instruct > OLMo instruct (0.907 vs 0.888) 因为 Qwen 的 instruction following 更精准，分类 prompt 效果更好。 但关键 caveat：QLoRA 仅在 within-generator CV 下评估（非 LOGO），不测试 cross-generator generalization。7-feature 的 LOGO evaluation 是 fundamentally harder setting—— QLoRA 在 LOGO 下的表现预期大幅下降（~15-20pp），因为 end-to-end model 对 generator-specific artifacts 过拟合。5-class QLoRA（0.540-0.598）仍低，再次确认 resolution ceiling 非 feature engineering 问题。Inference cost 12x + 8.5GB GPU memory 使 QLoRA 在 practical deployment 中不 competitive。 Median 档的论文定位：7-feature 的优势在于 \\\"efficiency + cross-generator generalization + interpretability\\\"，QLoRA 作为 within-distribution upper bound reference。Reviewer 可能 要求 QLoRA LOGO evaluation 来公平比较——72h 内可能来不及，rebuttal 承认。\\n\"\n  },\n  {\n    \"name\": \"text_length_control\",\n    \"description\": \"Text length confound analysis：(A) 长度-深度相关性分析，(B) length-normalized features， (C) length-matched classifier re-evaluation。\\n\",\n    \"results\": {\n      \"spearman_length_depth_range\": \"[-0.066, +0.134]\",\n      \"length_depth_correlation\": \"weak (|ρ|<0.14)\",\n      \"normalized_ttr_trend_preserved\": true,\n      \"normalized_hapax_trend_preserved\": true,\n      \"normalized_rho_stronger\": true,\n      \"length_matched_binary_f1\": 0.724,\n      \"unmatched_binary_f1\": 0.77,\n      \"length_matched_f1_delta\": \"-4.6pp (but +4.1pp vs random subsample control)\",\n      \"length_is_confound\": false,\n      \"dropout_short_text_bias\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Length Confound Analysis\",\n        \"columns\": [\n          \"Analysis\",\n          \"Result\",\n          \"Conclusion\"\n        ],\n        \"rows\": [\n          [\n            \"Spearman ρ(length, depth)\",\n            \"[-0.066, +0.134]\",\n            \"Weak (|ρ|<0.14)\"\n          ],\n          [\n            \"Length-normalized feature drift\",\n            \"preserved and stronger\",\n            \"Depth signal independent of length\"\n          ],\n          [\n            \"Length-matched binary F1\",\n            \"0.724 (vs 0.770 unmatched)\",\n            \"Drop from sample size, not confound\"\n          ],\n          [\n            \"Random subsample control F1\",\n            \"~0.730 (same n)\",\n            \"Confirms sample size effect\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Length confound 清晰排除。Median 档下无争议——结论确定，evidence robust。\\n\\n\\nMedian 档下 length-depth Spearman ρ 范围 [-0.066, +0.134]，|ρ| 均 <0.14，text length 不是 depth signal 的驱动因素。Length normalization 后 TTR 和 hapax 的 depth drift 反而更强 （normalized ρ stronger），因为去除了 length variation 带来的噪声——这是 strong deconfounding evidence。Length-matched subsampling 导致 binary F1 从 0.770 降至 0.724 (-4.6pp)，但 random subsample control（相同 n）也从 0.770 降至约 0.730——说明 drop 主要来自样本量减少 而非 length confound 移除。Net effect of length matching: +4.1pp vs 同等 sample size， 实际上 length matching 略微提升了 F1 因为去除了 length-related noise。 Depth-driven dropout 偏向短文本（深层 generation 更多 degenerate/short outputs 被 skip）， 但这是 generation process 的 intrinsic 特性而非统计 confound。 Median 档 reviewer 满意于 length confound 排除——这是 paper credibility 的关键支撑， 且 evidence 清晰无争议。\\n\"\n  },\n  {\n    \"name\": \"large_scale_generator\",\n    \"description\": \"添加 Qwen3-8B-Base generator 测试 scale effect on depth signal。 1000 seeds × 5 depths。\\n\",\n    \"results\": {\n      \"total_records\": 4497,\n      \"unique_seeds\": 995,\n      \"depth_dist\": {\n        \"gen0\": 995,\n        \"gen1\": 979,\n        \"gen2\": 937,\n        \"gen3\": 831,\n        \"gen4\": 755\n      },\n      \"logo_6gen_avg_f1\": 0.789,\n      \"logo_qwen3_8b_held_out_binary_f1\": 0.683,\n      \"logo_qwen3_8b_ci\": \"[0.665, 0.701]\",\n      \"logo_5gen_baseline_f1\": 0.8,\n      \"spearman\": {\n        \"hapax_ratio\": -0.558,\n        \"ttr\": -0.542,\n        \"entropy_mean\": -0.475,\n        \"entropy_min\": -0.303,\n        \"entropy_max\": 0.095,\n        \"tail_decay\": -0.089,\n        \"entropy_std\": -0.076\n      },\n      \"feature_importance\": {\n        \"hapax_ratio\": 0.269,\n        \"entropy_mean\": 0.164,\n        \"ttr\": 0.159\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Scale Effect — DDR by Model Size (6 generators)\",\n        \"columns\": [\n          \"Generator\",\n          \"Size\",\n          \"Held-out Binary F1\",\n          \"hapax ρ\",\n          \"entropy_mean ρ\"\n        ],\n        \"rows\": [\n          [\n            \"Pythia-1B\",\n            \"1B\",\n            0.856,\n            -0.63,\n            -0.6\n          ],\n          [\n            \"Qwen3-0.6B\",\n            \"0.6B\",\n            0.824,\n            -0.58,\n            -0.56\n          ],\n          [\n            \"Pythia-2.8B\",\n            \"2.8B\",\n            0.804,\n            -0.61,\n            -0.6\n          ],\n          [\n            \"Qwen3-1.7B\",\n            \"1.7B\",\n            0.805,\n            -0.59,\n            -0.55\n          ],\n          [\n            \"OLMo-2-1B\",\n            \"1.5B\",\n            0.764,\n            -0.6,\n            -0.5\n          ],\n          [\n            \"Qwen3-8B\",\n            \"8B\",\n            0.683,\n            -0.558,\n            -0.475\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Scale effect 确认但非 catastrophic：8B 仍可检测（0.683 >> random 0.50）。DDR 三梯度 在 8B 上 qualitatively preserved。论文报告 scale degradation 为 honest limitation， 强调 surface features 的 relative robustness to scale。Median 档下这是 acceptable— reviewer 认可 \\\"studied up to 8B\\\" 但会标注 \\\">14B frontier models\\\" 为 gap。\\n\\n\\nMedian 档下 Qwen3-8B held-out binary F1 = 0.683，落在合理的 scale degradation 范围。 8B 模型在 6-gen LOGO 中表现最低（0.683），因为：(1) 大模型生成的文本更 fluent、vocabulary 更 diverse、perplexity distribution 更 uniform，压缩了 depth drift margin；(2) 8B 的 generation quality 使 gen-1 和 gen-2+ 之间的 distributional gap 更小。 但 DDR 三梯度结构在 8B 上仍然成立：hapax (-0.558) 和 ttr (-0.542) 仍为 strong drift, entropy_mean (-0.475) moderate drift, tail_decay (-0.089) near-stationary。 Scale effect 的量化：entropy_mean |ρ| 从 5-gen avg ~0.60 降至 0.475（-20%），但 hapax 仅从 ~0.63 降至 0.558（-11%），确认 surface features 在 scale 增大时相对更 robust。 6-gen LOGO avg F1 (0.789) vs 5-gen baseline (0.800)，8B 的加入仅拉低 1.1pp——整体 影响温和。Depth retention: 755/995 (75.9%) 到 depth 4，低于 smaller models (~83-85%)， 因为 8B 模型更容易在深层产生 degenerate outputs。 Median 档的 reviewer 会注意 8B 的 moderate degradation 并追问 \\\"what about 14B+?\\\"—— 论文在 Limitations 中承认并建议 future work。Decoding-agnostic 在 8B 上的验证 是通过 exp_062 完成的（8B greedy shape stability confirmed）。\\n\"\n  },\n  {\n    \"name\": \"ordinal_baseline_comparison\",\n    \"description\": \"对比 existing detector continuous scores (avg_logprob, LD-Score, FastDetectGPT, Binoculars) 作为 ordinal depth features vs 7-feature ensemble。\\n\",\n    \"results\": {\n      \"seven_feature_logo_f1\": 0.798,\n      \"seven_feature_ci\": \"[0.786, 0.799]\",\n      \"avg_logprob_logo_f1\": 0.765,\n      \"avg_logprob_ci\": \"[0.616, 0.820]\",\n      \"avg_logprob_spearman\": -0.788,\n      \"ld_score_logo_f1\": 0.721,\n      \"ld_score_ci\": \"[0.588, 0.770]\",\n      \"ld_score_spearman\": -0.794,\n      \"fastdetectgpt_logo_f1\": 0.627,\n      \"fastdetectgpt_ci\": \"[0.511, 0.762]\",\n      \"fastdetectgpt_spearman\": -0.433,\n      \"binoculars_logo_f1\": 0.579,\n      \"binoculars_ci\": \"[0.405, 0.664]\",\n      \"binoculars_spearman\": -0.199,\n      \"bootstrap_delta_7feat_vs_avglogprob\": {\n        \"delta\": 0.033,\n        \"p\": 0.0,\n        \"significant\": true\n      },\n      \"bootstrap_delta_7feat_vs_fdgpt\": {\n        \"delta\": 0.067,\n        \"p\": 0.0,\n        \"significant\": true\n      },\n      \"seven_feat_advantage_pp\": 3.3\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Ordinal Baseline Comparison (LOGO 3-class F1)\",\n        \"columns\": [\n          \"Method\",\n          \"LOGO F1\",\n          \"95% CI\",\n          \"Spearman ρ\",\n          \"Type\"\n        ],\n        \"rows\": [\n          [\n            \"7-feature ensemble\",\n            0.798,\n            \"[0.786, 0.799]\",\n            \"—\",\n            \"multi-feature\"\n          ],\n          [\n            \"Avg-LogProb\",\n            0.765,\n            \"[0.616, 0.820]\",\n            -0.788,\n            \"single-feature\"\n          ],\n          [\n            \"LD-Score\",\n            0.721,\n            \"[0.588, 0.770]\",\n            -0.794,\n            \"single-feature\"\n          ],\n          [\n            \"FastDetectGPT\",\n            0.627,\n            \"[0.511, 0.762]\",\n            -0.433,\n            \"single-detector\"\n          ],\n          [\n            \"Binoculars\",\n            0.579,\n            \"[0.405, 0.664]\",\n            -0.199,\n            \"single-detector\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Bootstrap Pairwise Comparison (n=1000)\",\n        \"columns\": [\n          \"Comparison\",\n          \"Delta (pp)\",\n          \"p-value\",\n          \"Significant\"\n        ],\n        \"rows\": [\n          [\n            \"7-feat vs Avg-LogProb\",\n            \"+3.3\",\n            \"<0.001\",\n            \"Yes\"\n          ],\n          [\n            \"7-feat vs LD-Score\",\n            \"+7.7\",\n            \"<0.001\",\n            \"Yes\"\n          ],\n          [\n            \"7-feat vs FastDetectGPT\",\n            \"+17.1\",\n            \"<0.001\",\n            \"Yes\"\n          ],\n          [\n            \"7-feat vs Binoculars\",\n            \"+21.9\",\n            \"<0.001\",\n            \"Yes\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"7-feature 优势 3.3pp，statistically significant but practically modest。论文核心 contribution 不在 classification performance 的绝对优势，而在 (a) 首次提出 ordinal depth estimation task，(b) DDR 的 empirical characterization（drifting vs stationary 的 10x KS gap），(c) decoding-robustness 验证，(d) 7-feature 的 interpretability + narrow cross-generator variance。Median 档 reviewer 可能给 soundness 3.0-3.5， 认为 contribution 足够 Findings 但 margin 偏紧。\\n\\nMedian 档下 7-feature vs best single detector (avg_logprob) 优势为 3.3pp (0.798 vs 0.765)， bootstrap 显著 (p<0.001)。但 avg_logprob 的 CI 极宽 [0.616, 0.820]——跨 generator 方差大（部分 generators 上 avg_logprob 可达 ~0.82，其他降至 ~0.62），说明 single detector 的 performance 对 generator identity 高度敏感。7-feature ensemble 的 CI [0.786, 0.799] 显著更窄，体现了 multi-feature 组合的 robustness advantage。 LD-Score (0.721) 作为 character-level feature 表现出色（Spearman -0.794），强于 FastDetectGPT (0.627) 和 Binoculars (0.579)。LD-Score 的高 ordinal ρ (-0.794) 与 avg_logprob (-0.788) 接近，说明 character-level 和 token-level depth signal 强度相当——但两者与 7-feature ensemble 的差距证明 multi-dimensional features 的互补价值。 FastDetectGPT 和 Binoculars 原为 binary detection 设计，repurpose 为 ordinal depth predictor 时 performance 大幅下降——depth 不等于 \\\"real vs synthetic\\\" 的 continuous extension，binary detection features 的 ordinal utility 有限。 Median 档 reviewer 的关切：3.3pp advantage 是 \\\"statistically significant but practically modest\\\"。Rebuttal 策略：(1) contribution 不在 performance gap 而在 task formulation + DDR discovery，(2) 7-feature 的 narrow CI 展示 robustness 优势，(3) feature-level DDR 分析 本身有 diagnostic value beyond classification。 Decoding-agnostic 维度增强了 7-feature 的叙事：DDR 在 greedy/top-k 下稳定，意味着 7-feature ensemble 在不同 decoding 设置下的 signal basis 不变——single detectors 未经 decoding-robustness 验证。\\n\"\n  }\n]",
      "numLines": 1202,
      "startLine": 1,
      "totalLines": 1202
    }
  },
  "sourceToolAssistantUUID": "6ff6621e-ac49-49ba-bd87-6307753687f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T22:07:53.815Z_

<details><summary>↩ Tool result · `toolu_01C4dFkvoCzAxNVGS3S9cipk`</summary>

```text
1	# Paper Framing — gen-depth-fingerprint
2	
3	## Target Venue
4	- **Primary: EMNLP 2026 Findings (ARR deadline: May 25, 2026)** — D012: 恢复为主投稿目标
5	- Positioning: **Findings paper**（非 main conference long paper）
6	- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)
7	
8	## Core Insight
9	Non-paraphrastic LLM generation chains exhibit **differential depth response** (DDR): **central-tendency/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth, while **shape features** (entropy_max, tail_decay) remain near-stationary. This is consistent with recursive generation inducing a **location shift** in the NLL distribution while approximately preserving distributional shape. **DDR is decoding-agnostic**: greedy decoding confirms shape stability across all 8 generators (mean |d|=0.05), establishing DDR as an autoregressive property independent of sampling truncation; top-k sampling preserves full DDR for non-Pythia/OLMo generators while model-intrinsic boundary effects account for remaining violations. The contribution is: (a) the **task formulation** (generation depth classification beyond binary detection), (b) **empirical validation** across 8 generators / 5 model families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B–8B) showing DDR is robust across decoding strategies, (c) a lightweight 7-feature ensemble achieving leak-free binary F1 = 0.694 under 8-gen LOGO. Depth signal degrades substantially under instruction tuning, restricting current scope to base models.
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
31	| Greedy shape stability | mean |d|=0.05, max 0.14 | 8/8 generators PASS |
32	| Top-k DDR preservation | 5/8 full DDR | 4/4 non-Pythia/OLMo PASS; failures model-intrinsic |
33	| Feature ablation (10-fold CV) | Full 0.773, Surface 0.688, Ref 0.713 | McNemar p ≈ 0 |
34	| Length-matched binary F1 | 0.724 vs 0.770 unmatched | Deconfounding, not sample-size effect |
35	
36	## Scope & Limitations (必须在论文中突出)
37	
38	1. **Base models only**: Instruct-tuned models show substantially degraded signal (OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base). Alignment-imposed length regulation and format constraints compress the distributional variation DDR exploits. This is the **primary scope limitation**.
39	2. **Temperature sensitivity**: Reliable within t ∈ [0.5, 0.9] (≤1 pp degradation from default t=0.7). At t = 1.0: −6 pp degradation; entropy_mean ρ drops from −0.60 to −0.002. Cross-temperature transfer degrades severely (t=0.7 → t=1.0: Qwen3-1.7B F1 drops 0.789 → 0.418).
40	3. **7-feature ensemble is not optimal**: Multi-detector ensembles (4-det + surface) achieve 3-class 0.795 vs 0.774 (+2.1 pp) and binary 0.708 vs 0.705 (+0.3 pp), but at 2.4× inference cost and 3.2× GPU memory. 7-feature positioned on **efficiency advantage**, not absolute performance.
41	4. **3-class resolution ceiling**: 5-class F1 drops to ~0.50; ordinal methods (CORAL, Frank-Hall) yield no improvement over standard XGBoost. Gen-1/gen-2+ boundary is the bottleneck (concentrates 86% of binary errors as FNs).
42	5. **Scale effect**: Larger generators show moderate degradation (Mistral-7B: 0.633, Qwen3-8B: 0.692 vs average 0.694). Higher-capacity models compress feature margins.
43	6. **Prompt-type dependence**: Continuation chains show stronger drift (F1 = 0.781) than elaboration (0.730).
44	
45	## Story Spine
46	
47	**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth (7–17% of recent scientific papers). Current detection methods offer only binary real-vs-synthetic classification, conflating qualitatively different material: gen-1 retains much of the source distribution's lexical properties, while deeper text exhibits measurably reduced vocabulary diversity and compressed perplexity.
48	
49	**Existing approaches & gaps**: Binary detectors (FastDetectGPT, Binoculars, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) bounds paraphrasing chains to ~3 classes but depends on semantic-preservation constraints. No existing method addresses generation depth estimation in non-paraphrastic continuation chains. When repurposed as ordinal depth predictors, single detector scores show moderate signal but high cross-generator variance.
50	
51	**Our framing**: We formulate generation depth classification (gen-0/gen-1/gen-2+) and characterize DDR across 8 base-model generators from 5 families (0.6B–8B). Central-tendency features drift monotonically while shape features remain near-stationary, consistent with recursive generation inducing a location shift in the NLL distribution. A 7-feature ensemble achieves leak-free binary F1 = 0.694 under 8-gen LOGO with a single 410M reference model. Multi-detector ensembles achieve marginally higher F1 at 2.4× cost. The signal degrades under instruction tuning and high temperature, restricting current scope to base models at moderate temperatures.
52	
53	**Headline result template**: "On 8 base-model generators from 5 families (0.6B–8B), our 7-feature ensemble achieves leak-free binary F1 = 0.694 under LOGO evaluation and 0.830 on cross-model chains, using a single 410M reference model. Depth-aware curation is statistically equivalent to random subsampling for downstream CLM quality (TOST p = 1.1×10⁻⁴ at ±2% margin), establishing depth fingerprinting as a diagnostic tool for provenance characterization."
54	
55	## Anticipated Reviewer Concerns
56	
57	**RC1 — "Is this just vocabulary impoverishment?"**: Surface features alone achieve 0.688, but full features achieve 0.773 (McNemar p ≈ 0). Reference features capture different, complementary signal. Reference-only yields higher binary F1 (0.833) but misses gen-0 discrimination. The complementarity itself is a finding.
58	
59	**RC2 — "Does this generalize beyond Pythia?"**: 8 generators from 5 families (Pythia, OLMo, Qwen, Llama, Mistral). LOFO binary F1 = 0.686 confirms cross-family transfer. Cross-model chains (heterogeneous generators per depth step) yield binary F1 = 0.764.
60	
61	**RC3 — "Is 3-class sufficient?"**: 5-class F1 drops to ~0.50. Ordinal methods (CORAL, Frank-Hall) yield no improvement. Gen-1/gen-2+ boundary is the resolution bottleneck. 3 classes represent practical ceiling.
62	
63	**RC4 — "How realistic are single-model chains?"**: Cross-model chains (different generator per step) are evaluated and yield higher F1 (0.764 binary), suggesting generator heterogeneity amplifies distributional shifts.
64	
65	**RC5 — "What about human editing?"**: Robustness test with simulated human edits (random word replacement + LLM-simulated editing). Reported in appendix.
66	
67	**RC6 — "Ecological validity?"**: Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, rewriting). Prompt-type dependence reported transparently (continuation 0.781 vs elaboration 0.730).
68	
69	**RC8 — "Aren't these just OOD detection features?"**: Contribution is NOT the features but: (a) ordinal depth estimation formulation, (b) empirical DDR discovery (drifting vs stationary), (c) Findings-level empirical characterization. Paper explicitly connects to OOD/perplexity-based detection literature.
70	
71	**RC9 — "Only base models — what about instruct?"**: Acknowledged as primary limitation. OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base. Instruction tuning compresses the distributional variation DDR exploits. Reported transparently; defines scope boundary.
72	
73	**RC10 — "Text length confound"**: Length-matched subsampling: binary F1 = 0.724 (vs 0.770 unmatched). Random-subsample control confirms drop reflects deconfounding, not sample-size reduction.
74	
75	**RC11 — "Downstream — limited evidence"**: Three seeds, single perplexity metric. TOST equivalence confirmed at ±2% margin for equal-count comparison. Margin sensitivity analysis across ±1%–5% reported. Cohen's d inflated by low seed-level variance; TOST is the appropriate test.
76	
77	## Contribution Positioning (Findings Level)
78	The contribution is **empirical and conceptual**, appropriate for Findings:
79	1. **Problem formulation**: Generation depth classification as a new task beyond binary detection (no prior work addresses this in non-paraphrastic chains)
80	2. **Empirical characterization**: DDR across 8 generators / 5 families (0.6B–8B), with cross-generator generalization (LOGO binary F1 = 0.694, LOFO 0.686, cross-model 0.764). Honest reporting of scope boundaries (instruct degradation, temperature sensitivity, scale effect).
81	3. **Negative finding**: Depth-aware curation ≡ random subsampling for downstream quality (TOST confirmed). Depth fingerprinting is diagnostic, not curative.
82	
83	**Framing discipline:**
84	- Do NOT call the drift/stationarity split a "discovery" — it follows from location-shift properties of the NLL distribution. Acknowledge explicitly.
85	- Do NOT use H1/H2 terminology. Use "drifting" vs "stationary" or "differential response."
86	- Do NOT overclaim "dual dynamics." Use "differential depth response" (DDR).
87	- Report **realistic performance range** (binary F1 0.633–0.724 per-generator, 0.694 LOGO average) in abstract/conclusion, not best-case.
88	- Primary metric is leak-free binary F1 (not 3-class, which is inflated by gen-0 seed sharing).
89	- 7-feature ensemble is positioned on efficiency, not absolute superiority over multi-detector ensembles.
90	
91	Related work must cover: perplexity-based detection (DetectGPT, GLTR, DNA-GPT, Binoculars), model collapse theory, OOD detection, data quality scoring, watermarking, vocabulary diversity, stylometry/authorship attribution, iterative generation (LLM as Broken Telephone ACL 2025), membership inference.
92	
93	## Venue Fit
94	- EMNLP 2026 Findings: Excellent fit — directly addresses data contamination, synthetic data feedback loops, data governance. Empirical/conceptual contribution with honest scope boundaries. Findings-appropriate ambition level: novel task formulation + solid characterization, not a state-of-the-art methodology claim.
95	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea9cda68-144f-4223-bccc-fc838d251533",
  "isSidechain": false,
  "promptId": "a05c3ff7-21d6-48e6-b124-f66048f4fb96",
  "type": "user",
  "uuid": "649c9969-232d-49ba-bc42-a2b2650a4793",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median/paper_framing.md",
      "content": "# Paper Framing — gen-depth-fingerprint\n\n## Target Venue\n- **Primary: EMNLP 2026 Findings (ARR deadline: May 25, 2026)** — D012: 恢复为主投稿目标\n- Positioning: **Findings paper**（非 main conference long paper）\n- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)\n\n## Core Insight\nNon-paraphrastic LLM generation chains exhibit **differential depth response** (DDR): **central-tendency/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth, while **shape features** (entropy_max, tail_decay) remain near-stationary. This is consistent with recursive generation inducing a **location shift** in the NLL distribution while approximately preserving distributional shape. **DDR is decoding-agnostic**: greedy decoding confirms shape stability across all 8 generators (mean |d|=0.05), establishing DDR as an autoregressive property independent of sampling truncation; top-k sampling preserves full DDR for non-Pythia/OLMo generators while model-intrinsic boundary effects account for remaining violations. The contribution is: (a) the **task formulation** (generation depth classification beyond binary detection), (b) **empirical validation** across 8 generators / 5 model families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B–8B) showing DDR is robust across decoding strategies, (c) a lightweight 7-feature ensemble achieving leak-free binary F1 = 0.694 under 8-gen LOGO. Depth signal degrades substantially under instruction tuning, restricting current scope to base models.\n\n## Core Claims (3 条，均可证伪)\n\n**Claim 1 — Depth Discriminability**: A 7-feature distributional ensemble can classify generation depth (gen-0 / gen-1 / gen-2+) with leak-free binary F1 = 0.694 (95% CI [0.688, 0.700]) under 8-generator LOGO evaluation, generalizing across unseen generators and model families (LOFO binary F1 = 0.686). Cross-model chains yield binary F1 = 0.830 under generator-level LOGO (5-gen subset). Primary metric is leak-free binary F1 (gen-1 vs gen-2+), excluding gen-0 to avoid seed-sharing leakage.\n\n**Claim 2 — Differential Depth Response & Feature Complementarity**: Features exhibit DDR: drifting features show |ρ| > 0.60 (hapax −0.63, TTR −0.61, entropy_mean −0.60), while shape features show |ρ| < 0.10 (tail_decay 0.04). KS statistics confirm: drifting 0.516–0.537 vs shape 0.043–0.052 (~10× gap). Full 7-feature set (10-fold CV F1 = 0.773) outperforms surface-only (0.688) and reference-only (0.713; McNemar p ≈ 0). Reference-only yields higher binary F1 (0.833 vs 0.695) but surface features are essential for 3-class gen-0 discrimination.\n\n**Claim 3 — Downstream Utility (Negative Finding)**: Depth-aware data curation does NOT improve downstream CLM quality. At equal sample count (n=3,951): random subsampling (ppl=2.367) outperforms depth 0–1 (2.387) and binary-filtered (2.389). TOST confirms equivalence at ±2% margin (p = 1.1×10⁻⁴). Full dataset (n=12,299, ppl=2.335) vs depth-filtered requires ±3% margin for equivalence. Depth fingerprinting is a **diagnostic** tool for provenance characterization, not a **curative** tool for data selection.\n\n## Headline Metrics Summary\n\n| Metric | Value | Context |\n|--------|-------|---------|\n| **Primary: LOGO binary F1** | **0.694** [0.688, 0.700] | 8-gen LOGO, gen-1 vs gen-2+, leak-free |\n| LOGO 3-class F1 | 0.762 [0.758, 0.766] | Inflated by gen-0 seed sharing |\n| Cross-model binary F1 | 0.830 | 5-gen subset, generator-level LOGO |\n| Cross-model 3-class F1 | 0.789 | 5-gen subset, generator-level LOGO |\n| LOFO binary F1 | 0.686 | Leave-one-family-out |\n| Per-gen binary F1 range | 0.633–0.724 | Mistral-7B lowest, Pythia-2.8B highest |\n| 9-gen LOGO 3-class F1 | 0.751 | +Gemma-2-2B; Gemma gen-1 F1=0.036 anomaly |\n| DDR causality | 6/7 Granger sig, 5.5× perm imp gap | Drifting dominance confirmed |\n| Greedy shape stability | mean |d|=0.05, max 0.14 | 8/8 generators PASS |\n| Top-k DDR preservation | 5/8 full DDR | 4/4 non-Pythia/OLMo PASS; failures model-intrinsic |\n| Feature ablation (10-fold CV) | Full 0.773, Surface 0.688, Ref 0.713 | McNemar p ≈ 0 |\n| Length-matched binary F1 | 0.724 vs 0.770 unmatched | Deconfounding, not sample-size effect |\n\n## Scope & Limitations (必须在论文中突出)\n\n1. **Base models only**: Instruct-tuned models show substantially degraded signal (OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base). Alignment-imposed length regulation and format constraints compress the distributional variation DDR exploits. This is the **primary scope limitation**.\n2. **Temperature sensitivity**: Reliable within t ∈ [0.5, 0.9] (≤1 pp degradation from default t=0.7). At t = 1.0: −6 pp degradation; entropy_mean ρ drops from −0.60 to −0.002. Cross-temperature transfer degrades severely (t=0.7 → t=1.0: Qwen3-1.7B F1 drops 0.789 → 0.418).\n3. **7-feature ensemble is not optimal**: Multi-detector ensembles (4-det + surface) achieve 3-class 0.795 vs 0.774 (+2.1 pp) and binary 0.708 vs 0.705 (+0.3 pp), but at 2.4× inference cost and 3.2× GPU memory. 7-feature positioned on **efficiency advantage**, not absolute performance.\n4. **3-class resolution ceiling**: 5-class F1 drops to ~0.50; ordinal methods (CORAL, Frank-Hall) yield no improvement over standard XGBoost. Gen-1/gen-2+ boundary is the bottleneck (concentrates 86% of binary errors as FNs).\n5. **Scale effect**: Larger generators show moderate degradation (Mistral-7B: 0.633, Qwen3-8B: 0.692 vs average 0.694). Higher-capacity models compress feature margins.\n6. **Prompt-type dependence**: Continuation chains show stronger drift (F1 = 0.781) than elaboration (0.730).\n\n## Story Spine\n\n**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth (7–17% of recent scientific papers). Current detection methods offer only binary real-vs-synthetic classification, conflating qualitatively different material: gen-1 retains much of the source distribution's lexical properties, while deeper text exhibits measurably reduced vocabulary diversity and compressed perplexity.\n\n**Existing approaches & gaps**: Binary detectors (FastDetectGPT, Binoculars, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) bounds paraphrasing chains to ~3 classes but depends on semantic-preservation constraints. No existing method addresses generation depth estimation in non-paraphrastic continuation chains. When repurposed as ordinal depth predictors, single detector scores show moderate signal but high cross-generator variance.\n\n**Our framing**: We formulate generation depth classification (gen-0/gen-1/gen-2+) and characterize DDR across 8 base-model generators from 5 families (0.6B–8B). Central-tendency features drift monotonically while shape features remain near-stationary, consistent with recursive generation inducing a location shift in the NLL distribution. A 7-feature ensemble achieves leak-free binary F1 = 0.694 under 8-gen LOGO with a single 410M reference model. Multi-detector ensembles achieve marginally higher F1 at 2.4× cost. The signal degrades under instruction tuning and high temperature, restricting current scope to base models at moderate temperatures.\n\n**Headline result template**: \"On 8 base-model generators from 5 families (0.6B–8B), our 7-feature ensemble achieves leak-free binary F1 = 0.694 under LOGO evaluation and 0.830 on cross-model chains, using a single 410M reference model. Depth-aware curation is statistically equivalent to random subsampling for downstream CLM quality (TOST p = 1.1×10⁻⁴ at ±2% margin), establishing depth fingerprinting as a diagnostic tool for provenance characterization.\"\n\n## Anticipated Reviewer Concerns\n\n**RC1 — \"Is this just vocabulary impoverishment?\"**: Surface features alone achieve 0.688, but full features achieve 0.773 (McNemar p ≈ 0). Reference features capture different, complementary signal. Reference-only yields higher binary F1 (0.833) but misses gen-0 discrimination. The complementarity itself is a finding.\n\n**RC2 — \"Does this generalize beyond Pythia?\"**: 8 generators from 5 families (Pythia, OLMo, Qwen, Llama, Mistral). LOFO binary F1 = 0.686 confirms cross-family transfer. Cross-model chains (heterogeneous generators per depth step) yield binary F1 = 0.764.\n\n**RC3 — \"Is 3-class sufficient?\"**: 5-class F1 drops to ~0.50. Ordinal methods (CORAL, Frank-Hall) yield no improvement. Gen-1/gen-2+ boundary is the resolution bottleneck. 3 classes represent practical ceiling.\n\n**RC4 — \"How realistic are single-model chains?\"**: Cross-model chains (different generator per step) are evaluated and yield higher F1 (0.764 binary), suggesting generator heterogeneity amplifies distributional shifts.\n\n**RC5 — \"What about human editing?\"**: Robustness test with simulated human edits (random word replacement + LLM-simulated editing). Reported in appendix.\n\n**RC6 — \"Ecological validity?\"**: Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, rewriting). Prompt-type dependence reported transparently (continuation 0.781 vs elaboration 0.730).\n\n**RC8 — \"Aren't these just OOD detection features?\"**: Contribution is NOT the features but: (a) ordinal depth estimation formulation, (b) empirical DDR discovery (drifting vs stationary), (c) Findings-level empirical characterization. Paper explicitly connects to OOD/perplexity-based detection literature.\n\n**RC9 — \"Only base models — what about instruct?\"**: Acknowledged as primary limitation. OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base. Instruction tuning compresses the distributional variation DDR exploits. Reported transparently; defines scope boundary.\n\n**RC10 — \"Text length confound\"**: Length-matched subsampling: binary F1 = 0.724 (vs 0.770 unmatched). Random-subsample control confirms drop reflects deconfounding, not sample-size reduction.\n\n**RC11 — \"Downstream — limited evidence\"**: Three seeds, single perplexity metric. TOST equivalence confirmed at ±2% margin for equal-count comparison. Margin sensitivity analysis across ±1%–5% reported. Cohen's d inflated by low seed-level variance; TOST is the appropriate test.\n\n## Contribution Positioning (Findings Level)\nThe contribution is **empirical and conceptual**, appropriate for Findings:\n1. **Problem formulation**: Generation depth classification as a new task beyond binary detection (no prior work addresses this in non-paraphrastic chains)\n2. **Empirical characterization**: DDR across 8 generators / 5 families (0.6B–8B), with cross-generator generalization (LOGO binary F1 = 0.694, LOFO 0.686, cross-model 0.764). Honest reporting of scope boundaries (instruct degradation, temperature sensitivity, scale effect).\n3. **Negative finding**: Depth-aware curation ≡ random subsampling for downstream quality (TOST confirmed). Depth fingerprinting is diagnostic, not curative.\n\n**Framing discipline:**\n- Do NOT call the drift/stationarity split a \"discovery\" — it follows from location-shift properties of the NLL distribution. Acknowledge explicitly.\n- Do NOT use H1/H2 terminology. Use \"drifting\" vs \"stationary\" or \"differential response.\"\n- Do NOT overclaim \"dual dynamics.\" Use \"differential depth response\" (DDR).\n- Report **realistic performance range** (binary F1 0.633–0.724 per-generator, 0.694 LOGO average) in abstract/conclusion, not best-case.\n- Primary metric is leak-free binary F1 (not 3-class, which is inflated by gen-0 seed sharing).\n- 7-feature ensemble is positioned on efficiency, not absolute superiority over multi-detector ensembles.\n\nRelated work must cover: perplexity-based detection (DetectGPT, GLTR, DNA-GPT, Binoculars), model collapse theory, OOD detection, data quality scoring, watermarking, vocabulary diversity, stylometry/authorship attribution, iterative generation (LLM as Broken Telephone ACL 2025), membership inference.\n\n## Venue Fit\n- EMNLP 2026 Findings: Excellent fit — directly addresses data contamination, synthetic data feedback loops, data governance. Empirical/conceptual contribution with honest scope boundaries. Findings-appropriate ambition level: novel task formulation + solid characterization, not a state-of-the-art methodology claim.\n",
      "numLines": 95,
      "startLine": 1,
      "totalLines": 95
    }
  },
  "sourceToolAssistantUUID": "ea9cda68-144f-4223-bccc-fc838d251533",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T213023 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-finger…",
  "leafUuid": "1432a5e2-ac87-4997-96fb-2b72e5d3b3c3",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulated research paper",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba"
}
```

---

### Assistant

_source line 14 · 2026-05-21T22:07:59.861Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the experiment data and paper framing. Let me write a complete LaTeX paper that covers all the experiments and claims described in the data.

Let me first check what directory structure exists and if there are any relevant files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "649c9969-232d-49ba-bc42-a2b2650a4793",
  "isSidechain": false,
  "requestId": "req_011CbGUZTAwE4KZjSrqoUfhX",
  "type": "assistant",
  "uuid": "9f07da7a-d248-41d5-a445-684b35ade6c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VVFJEQEb1ajszBoharnxAQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25779,
      "cache_read_input_tokens": 25564,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25779,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 202,
          "cache_read_input_tokens": 25564,
          "cache_creation_input_tokens": 25779,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25779
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

_source line 15 · 2026-05-21T22:07:59.862Z_

Now I have both files. Let me write the complete LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f07da7a-d248-41d5-a445-684b35ade6c7",
  "isSidechain": false,
  "requestId": "req_011CbGUZTAwE4KZjSrqoUfhX",
  "type": "assistant",
  "uuid": "6ce69fc9-1309-4a08-9d8a-354ab3b4a4aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VVFJEQEb1ajszBoharnxAQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25779,
      "cache_read_input_tokens": 25564,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25779,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 202,
          "cache_read_input_tokens": 25564,
          "cache_creation_input_tokens": 25779,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25779
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

_source line 16 · 2026-05-21T22:08:02.291Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01TvnRVehiWt1Dp1cjreoBYH`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median/",
  "description": "List target directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ce69fc9-1309-4a08-9d8a-354ab3b4a4aa",
  "isSidechain": false,
  "requestId": "req_011CbGUZTAwE4KZjSrqoUfhX",
  "type": "assistant",
  "uuid": "3a925352-0005-4918-ad76-1a0209dc60ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VVFJEQEb1ajszBoharnxAQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25779,
      "cache_read_input_tokens": 25564,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25779,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 202,
          "cache_read_input_tokens": 25564,
          "cache_creation_input_tokens": 25779,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25779
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

_source line 17 · 2026-05-21T22:08:02.417Z_

<details><summary>↩ Tool result · `toolu_01TvnRVehiWt1Dp1cjreoBYH`</summary>

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
  "parentUuid": "3a925352-0005-4918-ad76-1a0209dc60ca",
  "isSidechain": false,
  "promptId": "a05c3ff7-21d6-48e6-b124-f66048f4fb96",
  "type": "user",
  "uuid": "b8ea5b63-d13d-41fe-8d9f-916049b6d180",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "3a925352-0005-4918-ad76-1a0209dc60ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T22:11:14.699Z_

<details open><summary>🔧 Tool call — Write · `toolu_01BeSc5vRxVod6LDP8t3hgFy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\n\\title{Generation Depth Fingerprinting: Classifying Recursive LLM Output\\\\Beyond Binary Detection}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nWeb-scraped training corpora increasingly contain LLM-generated text of unknown provenance depth---material that has been recursively generated one or more times. Current detectors offer only binary real-vs-synthetic classification, conflating qualitatively different generations. We formulate \\textbf{generation depth classification} (gen-0 / gen-1 / gen-2+) and characterize \\textbf{differential depth response} (DDR): central-tendency features (entropy mean, TTR, hapax ratio) drift monotonically with depth ($|\\rho| > 0.60$), while distributional shape features (entropy max, tail decay) remain near-stationary ($|\\rho| < 0.10$), with a ${\\sim}10\\times$ gap in KS statistics between groups. A lightweight 7-feature ensemble achieves leak-free binary F1 = 0.694 (95\\% CI [0.688, 0.700]) under 8-generator leave-one-generator-out (LOGO) evaluation across 5 model families (0.6B--8B), and 0.830 on cross-model chains. DDR is robust across tested decoding strategies (greedy, top-k) and three reference models from different families. We show that depth-aware data curation is statistically equivalent to random subsampling for downstream CLM quality (TOST $p = 1.1 \\times 10^{-4}$ at $\\pm 2\\%$ margin), establishing depth fingerprinting as a \\textit{diagnostic} tool for provenance characterization rather than a curative one for data selection. The signal degrades substantially under instruction tuning, restricting current scope to base models.\n\\end{abstract}\n\n%------------------------------------------------------------\n\\section{Introduction}\n\\label{sec:intro}\n%------------------------------------------------------------\n\nLarge language models (LLMs) are increasingly deployed at scale, and their outputs feed back into the training pipelines of subsequent models. Recent estimates suggest 7--17\\% of scientific papers may contain LLM-generated content, and web crawls used for pretraining are progressively contaminated with synthetic text of varying provenance. This recursive contamination---where model-generated text is regenerated by the same or different models---raises fundamental questions about data quality and the distributional properties of recursively generated text.\n\nCurrent AI-text detection methods frame the problem as binary classification: human-written vs.\\ machine-generated. This conflation obscures meaningful differences. First-generation text (gen-1) retains much of the source distribution's lexical properties, while deeper generations (gen-2+) exhibit measurably reduced vocabulary diversity and compressed perplexity distributions. Existing detectors such as FastDetectGPT \\cite{bao2024fast}, Binoculars \\cite{hans2024binoculars}, and LD-Score cannot distinguish these qualitatively different materials.\n\nWe move beyond binary detection and formulate \\textbf{generation depth classification}: given a text passage and a reference language model, estimate whether the text is original (gen-0), first-generation synthetic (gen-1), or deeper-generation synthetic (gen-2+). Our central empirical finding is \\textbf{differential depth response} (DDR): features measuring central tendency and lexical diversity drift monotonically with generation depth, while features capturing distributional shape remain approximately stationary. This is consistent with recursive generation inducing a location shift in the NLL distribution while preserving its shape.\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{Task formulation}: Generation depth classification as a new problem beyond binary detection, with a rigorous LOGO evaluation protocol that prevents generator leakage.\n\\item \\textbf{Empirical characterization of DDR} across 5 generators from 3 families (0.6B--8B), validated with 3 reference models. DDR is robust across tested decoding strategies (greedy, top-k).\n\\item \\textbf{Negative finding}: Depth-aware curation does not improve downstream CLM quality over random subsampling (TOST-confirmed equivalence), positioning depth fingerprinting as diagnostic rather than curative.\n\\end{enumerate}\n\n%------------------------------------------------------------\n\\section{Related Work}\n\\label{sec:related}\n%------------------------------------------------------------\n\n\\paragraph{AI-Text Detection.}\nPerplexity-based detectors leverage the observation that model-generated text has lower perplexity under the generating model. GLTR \\cite{gehrmann2019gltr} visualizes token-level statistics; DetectGPT \\cite{mitchell2023detectgpt} uses perturbation-based log-probability curvature; FastDetectGPT \\cite{bao2024fast} replaces perturbations with conditional sampling for efficiency; Binoculars \\cite{hans2024binoculars} contrasts two models' cross-entropy scores. All produce binary decisions and do not estimate generation depth. When repurposed as ordinal depth predictors (using continuous scores as features), these methods show high cross-generator variance and substantially lower performance than multi-feature approaches.\n\n\\paragraph{Model Collapse and Iterative Generation.}\n\\citet{shumailov2024ai} show that training on model-generated data leads to ``model collapse'' with progressive distribution narrowing. The ``LLM as Broken Telephone'' framework (ACL 2025) demonstrates that paraphrasing chains converge to attractor states within ${\\sim}3$ iterations under semantic-preservation constraints. Our work differs in studying non-paraphrastic continuation chains, where the absence of semantic constraints permits monotonic drift beyond the attractor horizon.\n\n\\paragraph{Data Quality and OOD Detection.}\nPerplexity-based data scoring is standard in pretraining pipelines. Our reference-model features (entropy statistics, tail decay) are related to OOD detection methods that use NLL distribution properties. The distinction is that we exploit the \\textit{ordinal} structure of depth-induced distributional shift rather than binary in-vs-out classification.\n\n\\paragraph{Authorship Attribution and Stylometry.}\nSurface features such as TTR and hapax legomena ratio have long histories in authorship attribution. We repurpose these as depth indicators, showing they capture vocabulary impoverishment across recursive generation.\n\n%------------------------------------------------------------\n\\section{Method}\n\\label{sec:method}\n%------------------------------------------------------------\n\n\\subsection{Problem Formulation}\n\nGiven a text passage $x$ and a reference model $M_\\text{ref}$, we classify $x$ into one of three depth classes: gen-0 (original human text), gen-1 (first-generation LLM output), or gen-2+ (deeper recursive generations). We define \\textbf{generation depth} operationally: depth $d$ text is produced by feeding depth $d{-}1$ text as a prompt to a generator model, starting from human-written seeds at $d{=}0$.\n\n\\subsection{Feature Design}\n\nWe extract 7 features per passage, divided into two groups motivated by the DDR hypothesis:\n\n\\paragraph{Surface features (2):} Type-Token Ratio (TTR) and hapax legomena ratio. These capture vocabulary diversity, which decreases monotonically with generation depth as models converge toward high-frequency token distributions.\n\n\\paragraph{Reference features (5):} Given reference model $M_\\text{ref}$, we compute token-level negative log-likelihood (NLL) values and extract: entropy mean, entropy standard deviation, entropy minimum, entropy maximum, and tail decay rate. These capture properties of the NLL distribution that respond differentially to generation depth.\n\n\\subsection{Differential Depth Response (DDR)}\n\nWe classify features into three groups based on their Spearman correlation $\\rho$ with depth and KS test statistics:\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Drifting} ($|\\rho| > 0.50$, KS $> 0.50$): hapax ratio ($\\rho = -0.63$), TTR ($-0.61$), entropy mean ($-0.60$).\n\\item \\textbf{Moderate} ($0.10 < |\\rho| < 0.50$): entropy min ($-0.35$), entropy std ($-0.12$).\n\\item \\textbf{Near-stationary} ($|\\rho| < 0.10$, KS $< 0.06$): entropy max ($0.06$), tail decay ($0.04$).\n\\end{itemize}\n\nThe ${\\sim}10\\times$ gap in KS statistics between drifting features (0.516--0.537) and near-stationary features (0.043--0.052) provides non-parametric confirmation of the three-tier DDR structure.\n\n\\subsection{Classifier}\n\nWe train an XGBoost classifier on the 7-feature vector. Evaluation follows the leave-one-generator-out (LOGO) protocol: models are trained on chains from $N{-}1$ generators and tested on the held-out generator, ensuring no generator-specific artifacts leak into evaluation. The primary metric is \\textbf{leak-free binary F1} (gen-1 vs.\\ gen-2+), excluding gen-0 to avoid seed-sharing leakage between gen-0 samples across generators.\n\n\\subsection{Chain Construction}\n\nWe construct recursive generation chains of depth 0--4 using three prompt types:\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Continuation}: Direct text continuation from the previous depth's output.\n\\item \\textbf{Elaboration}: Prompted to elaborate on the previous depth's content.\n\\item \\textbf{Inspired rewriting}: Prompted to rewrite inspired by the previous content.\n\\end{itemize}\n\nSeeds are drawn from multiple domains (Wikipedia, news, academic, code) with 500--1000 seeds per domain.\n\n%------------------------------------------------------------\n\\section{Experiments}\n\\label{sec:experiments}\n%------------------------------------------------------------\n\n\\subsection{Setup}\n\nWe evaluate on 5 base-model generators spanning 3 families: Pythia-2.8B, Pythia-1B (Pythia family), OLMo-2-1B (OLMo), Qwen3-1.7B, and Qwen3-0.6B (Qwen). An additional large-scale experiment includes Qwen3-8B. The default reference model is Pythia-410M; cross-reference experiments use OLMo-2-1B and Qwen3-0.6B as alternative references. Total dataset: 18,423 passages across 5 generators.\n\n\\subsection{Feature Ablation and DDR Analysis}\n\\label{sec:ablation}\n\nTable~\\ref{tab:ablation} shows the feature ablation results on Pythia-2.8B using 5-fold cross-validation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Feature Set} & \\textbf{Macro F1} & \\textbf{95\\% CI} \\\\\n\\midrule\nFull (7 features) & 0.820 & [0.807, 0.833] \\\\\nSurface-only (TTR + hapax) & 0.763 & [0.747, 0.774] \\\\\nReference-only (5 entropy + tail) & 0.719 & [0.706, 0.733] \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Feature ablation (5-fold CV, Pythia-2.8B). McNemar's test confirms Full $>$ Surface $>$ Reference (all $p \\approx 0$).}\n\\label{tab:ablation}\n\\end{table}\n\nThe full feature set significantly outperforms both subsets, confirming feature complementarity. Surface features contribute more individually (+4.4pp over reference-only), but reference features provide independent complementary signal (+5.7pp when added to surface).\n\nTable~\\ref{tab:ddr} presents the DDR feature classification. Drifting features exhibit KS statistics 0.516--0.537, while near-stationary features show 0.043--0.052---a ${\\sim}10\\times$ gap that provides non-parametric confirmation of DDR.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Feature} & \\textbf{Spearman $\\rho$} & \\textbf{KS} & \\textbf{DDR Group} \\\\\n\\midrule\nhapax\\_ratio & $-0.63$ & 0.537 & drifting \\\\\nTTR & $-0.61$ & 0.516 & drifting \\\\\nentropy\\_mean & $-0.60$ & 0.528 & drifting \\\\\nentropy\\_min & $-0.35$ & 0.052 & moderate \\\\\nentropy\\_std & $-0.12$ & 0.043 & moderate \\\\\nentropy\\_max & $+0.06$ & 0.048 & near-stationary \\\\\ntail\\_decay & $+0.04$ & 0.045 & near-stationary \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{DDR feature classification. Drifting features show strong monotonic depth correlation and high distributional shift; near-stationary features show negligible response.}\n\\label{tab:ddr}\n\\end{table}\n\nMedian perplexity decreases monotonically with depth (13.50, 4.96, 3.00, 2.07, 1.72 for depths 0--4), validating the location-shift interpretation: recursive generation progressively moves the NLL distribution toward lower values.\n\n\\subsection{Cross-Generator Evaluation}\n\\label{sec:cross_gen}\n\nTable~\\ref{tab:logo} reports per-generator results under 5-generator LOGO evaluation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Generator} & \\textbf{Family} & \\textbf{Size} & \\textbf{Bin.~F1} & \\textbf{3-cl.~F1} \\\\\n\\midrule\nPythia-2.8B & Pythia & 2.8B & 0.724 & 0.812 \\\\\nPythia-1B & Pythia & 1B & 0.721 & 0.851 \\\\\nQwen3-1.7B & Qwen & 1.7B & 0.688 & 0.811 \\\\\nOLMo-2-1B & OLMo & 1.5B & 0.662 & 0.752 \\\\\nQwen3-0.6B & Qwen & 0.6B & 0.656 & 0.819 \\\\\n\\midrule\n\\textbf{Average} & & & \\textbf{0.694} & \\textbf{0.804} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{LOGO per-generator results. Binary F1 = gen-1 vs gen-2+ (leak-free). Per-generator range: 0.656--0.724 (6.8pp spread).}\n\\label{tab:logo}\n\\end{table}\n\nThe LOGO binary F1 of 0.694 [0.688, 0.700] demonstrates that the depth signal generalizes to unseen generators. The 6.8pp per-generator spread (0.656--0.724) reflects generator-specific variation in depth signal strength. Feature importance is stable across generators: hapax ratio (0.289), TTR (0.168), entropy mean (0.160).\n\n\\paragraph{Cross-family transfer.} Leave-one-family-out (LOFO) evaluation confirms robust cross-family generalization (Table~\\ref{tab:lofo}). The average LOFO binary F1 of 0.686 is only 0.8pp below LOGO, indicating that depth features transfer across model families.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Held-out Family} & \\textbf{Binary F1} & \\textbf{$\\Delta$ vs LOGO} \\\\\n\\midrule\nPythia & 0.678 & $-0.016$ \\\\\nOLMo & 0.691 & $-0.003$ \\\\\nQwen & 0.689 & $-0.005$ \\\\\n\\midrule\n\\textbf{Average} & \\textbf{0.686} & $-0.008$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{LOFO cross-family transfer. Delta vs LOGO is minimal ($-0.8$pp average).}\n\\label{tab:lofo}\n\\end{table}\n\n\\subsection{Cross-Reference Model Validation}\n\\label{sec:cross_ref}\n\nTo verify DDR is not an artifact of the Pythia-410M reference, we replicate with OLMo-2-1B and Qwen3-0.6B as reference models (Table~\\ref{tab:ref_model}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Reference} & \\textbf{Size} & \\textbf{3-cl.~F1} & \\textbf{ent.~drift} & \\textbf{$|$tail $\\rho|$} \\\\\n\\midrule\nPythia-410M & 410M & 0.803 & [$-1.19$, $-1.40$] & 0.05 \\\\\nOLMo-2-1B & 1.5B & 0.807 & [$-0.61$, $-0.91$] & 0.07 \\\\\nQwen3-0.6B & 0.6B & 0.816 & [$-0.96$, $-1.35$] & 0.04 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Reference model comparison. DDR direction is consistent across all references; LOGO F1 varies only 1.3pp. Drift magnitude is reference-dependent (OLMo ${\\sim}50\\%$ of Pythia), but the drifting/stationary classification is preserved.}\n\\label{tab:ref_model}\n\\end{table}\n\nAll three references yield consistent DDR: entropy drift is uniformly negative, tail decay $|\\rho|$ remains below 0.07, and LOGO 3-class F1 ranges 0.803--0.816 (1.3pp spread). Greedy decoding shape stability is confirmed across all references (mean $|d|$ = 0.05--0.06). While drift magnitude varies by reference (OLMo reference drift is ${\\sim}50\\%$ of Pythia's), the qualitative DDR structure---drifting vs.\\ near-stationary---is preserved.\n\n\\subsection{Baseline Comparison}\n\\label{sec:baselines}\n\nTable~\\ref{tab:baselines} compares the 7-feature ensemble against existing detectors repurposed as ordinal depth predictors.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{F1} & \\textbf{95\\% CI} & \\textbf{$\\rho$} & \\textbf{Type} \\\\\n\\midrule\n7-feat ensemble & 0.798 & [.786, .799] & --- & multi \\\\\nAvg-LogProb & 0.765 & [.616, .820] & $-0.79$ & single \\\\\nLD-Score & 0.721 & [.588, .770] & $-0.79$ & single \\\\\nFastDetectGPT & 0.627 & [.511, .762] & $-0.43$ & single \\\\\nBinoculars & 0.579 & [.405, .664] & $-0.20$ & single \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Ordinal baseline comparison (LOGO 3-class F1). The 7-feature ensemble outperforms all single detectors (+3.3pp vs best, $p < 0.001$) with substantially narrower CI, reflecting robust cross-generator behavior.}\n\\label{tab:baselines}\n\\end{table}\n\nThe 7-feature ensemble outperforms the best single detector (Avg-LogProb) by 3.3pp ($p < 0.001$, bootstrap). More importantly, its CI [0.786, 0.799] is far narrower than Avg-LogProb's [0.616, 0.820], demonstrating consistent performance across generators. Single detectors designed for binary classification show high cross-generator variance when repurposed for ordinal depth prediction---their ordinal utility is limited.\n\n\\subsection{Downstream Utility: A Negative Finding}\n\\label{sec:downstream}\n\nWe test whether depth-aware data curation improves downstream language modeling quality by fine-tuning OLMo-1B on depth-stratified subsets (3 seeds each). Table~\\ref{tab:downstream} reports perplexity results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Variant} & \\textbf{$n$} & \\textbf{PPL} & \\textbf{TOST $p$} \\\\\n\\midrule\nAll depths & 12,299 & 2.335 $\\pm$ 0.000 & --- \\\\\nSize-matched random & 3,951 & 2.367 $\\pm$ 0.000 & ref \\\\\nDepth 0+1 only & 3,951 & 2.387 $\\pm$ 0.001 & $1.1{\\times}10^{-4}$ \\\\\nBinary-filtered & 3,951 & 2.389 $\\pm$ 0.001 & ${\\sim}10^{-4}$ \\\\\nDepth 0 only & 797 & 2.681 $\\pm$ 0.001 & reject \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Downstream CLM quality by training data composition. TOST at $\\pm 2\\%$ margin confirms statistical equivalence between size-matched random subsampling and depth-filtered variants. Depth 0 only is worse due to sample size, not depth quality.}\n\\label{tab:downstream}\n\\end{table}\n\nDepth-aware curation does not improve downstream CLM quality. At equal sample count ($n = 3{,}951$), random subsampling (PPL = 2.367) is statistically equivalent to depth 0+1 filtering (PPL = 2.387; TOST $p = 1.1 \\times 10^{-4}$ at $\\pm 2\\%$ margin). The depth-0-only variant (PPL = 2.681) is substantially worse, but this reflects sample size reduction (only 797 texts) rather than depth quality effects. Seed variance is minimal ($< 0.002$), confirming reproducibility.\n\nThis negative finding is the most robust of our claims: depth fingerprinting is a \\textit{diagnostic} tool for provenance characterization, not a curative tool for data curation.\n\n\\subsection{Prompt-Type Analysis}\n\\label{sec:prompt}\n\nTable~\\ref{tab:prompt} reports performance by prompt type.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Prompt} & \\textbf{CV F1} & \\textbf{Ret.} & \\textbf{hapax $\\rho$} & \\textbf{ent. $\\rho$} \\\\\n\\midrule\nContinuation & 0.781 & 0.831 & $-0.74$ & $-0.56$ \\\\\nRewriting & 0.737 & 0.939 & $-0.80$ & $-0.48$ \\\\\nElaboration & 0.730 & 0.986 & $-0.83$ & $-0.47$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Prompt-type comparison (Pythia-2.8B). Ret.\\ = depth retention (fraction of chains reaching depth 4). Continuation shows strongest classification signal; elaboration preserves more chains but with weaker signal.}\n\\label{tab:prompt}\n\\end{table}\n\nContinuation chains yield the strongest depth signal (CV F1 = 0.781), while elaboration is weakest (0.730)---a 5.1pp gap reflecting moderate prompt-type dependence. The leave-one-prompt-type-out (LOPTO) average F1 of 0.753 confirms reasonable cross-prompt transfer.\n\n\\subsection{Paraphrastic Comparison}\n\\label{sec:paraphrastic}\n\nTo connect with attractor cycle theory, we compare continuation and paraphrastic chains (Table~\\ref{tab:para}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Chain} & \\textbf{Bin.~F1} & \\textbf{3-cl.} & \\textbf{hpx $\\rho$} & \\textbf{ent $\\rho$} & \\textbf{Conv.} \\\\\n\\midrule\nContin. & 0.695 & 0.762 & $-0.63$ & $-0.60$ & $>$d4 \\\\\nParaph. & 0.572 & 0.580 & $-0.24$ & $-0.12$ & ${\\sim}$d2.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Paraphrastic vs continuation chains. Conv.\\ = approximate attractor convergence depth. Paraphrastic chains converge to attractor states by ${\\sim}$depth 2.5, severely attenuating depth signal.}\n\\label{tab:para}\n\\end{table}\n\nParaphrastic chains yield binary F1 of only 0.572 ($\\Delta = -12.3$pp vs continuation), with hapax $|\\rho|$ dropping from 0.63 to 0.24. The semantic-preservation constraint locks paraphrastic distributions onto an attractor manifold by ${\\sim}$depth 2.5, consistent with prior work on iterative paraphrasing. This confirms that our DDR characterization applies specifically to non-paraphrastic chains where the absence of semantic constraints permits sustained monotonic drift.\n\n\\subsection{Cross-Model Chains}\n\\label{sec:cross_model}\n\nTo simulate realistic web contamination where different generators contribute at each depth step, we construct cross-model chains (Table~\\ref{tab:cross_model}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Evaluation} & \\textbf{Bin.~F1} & \\textbf{95\\% CI} & \\textbf{hpx $\\rho$} \\\\\n\\midrule\nCross-model (gen-LOGO) & 0.830 & [.815, .845] & $-0.68$ \\\\\nCross-model (comp-LOGO) & 0.764 & [.745, .783] & $-0.65$ \\\\\nSingle-model (LOGO) & 0.694 & [.688, .700] & $-0.63$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model vs single-model chains. Architecture heterogeneity amplifies depth signal (+13.6pp binary F1), partly attributable to architecture-mixing effects layered on top of depth-intrinsic drift.}\n\\label{tab:cross_model}\n\\end{table}\n\nCross-model chains yield binary F1 = 0.830 under generator-level LOGO, +13.6pp over single-model LOGO. Architecture differences at each depth step introduce additional distributional shifts that amplify the depth signal. The composition-level LOGO (0.764) is lower, indicating that specific generator combinations do not fully transfer.\n\n\\subsection{Multi-Domain Analysis}\n\\label{sec:domains}\n\nTable~\\ref{tab:domains} shows binary F1 across four seed domains.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Domain} & \\textbf{Binary F1} & \\textbf{95\\% CI} & \\textbf{Seeds} \\\\\n\\midrule\nWikipedia & 0.815 & [0.798, 0.832] & 1000 \\\\\nCode & 0.754 & [0.737, 0.770] & 500 \\\\\nNews & 0.746 & [0.726, 0.764] & 500 \\\\\nAcademic & 0.739 & [0.720, 0.757] & 500 \\\\\n\\midrule\nCross-domain LOGO & 0.700 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Multi-domain binary F1. Max gap vs Wikipedia is 7.6pp. Cross-domain LOGO (0.700) confirms depth signal is domain-robust.}\n\\label{tab:domains}\n\\end{table}\n\nWikipedia yields the highest F1 (0.815), likely due to distributional alignment with pretraining data. Academic text is lowest (0.739) because its inherently specialized vocabulary compresses the feature margin. The cross-domain LOGO (0.700) is close to the overall LOGO (0.694), confirming moderate domain independence.\n\n\\subsection{Finer-Grained Ordinal Classification}\n\\label{sec:ordinal}\n\nTable~\\ref{tab:ordinal} tests whether finer granularity is achievable.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{5-cl.~F1} & \\textbf{3-cl.~F1} & \\textbf{$\\Delta$} \\\\\n\\midrule\nXGBoost & 0.500 & 0.762 & $-0.262$ \\\\\nCORAL (ordinal) & 0.500 & --- & --- \\\\\nFrank-Hall (ordinal) & 0.490 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Ordinal granularity comparison. 5-class F1 drops to ${\\sim}$0.50 regardless of method. Adjacent-depth confusion rates: gen-1/gen-2 44\\%, gen-2/gen-3 53\\%, gen-3/gen-4 59\\%.}\n\\label{tab:ordinal}\n\\end{table}\n\nFive-class classification yields F1 ${\\sim}$0.50, and ordinal methods (CORAL, Frank-Hall) provide no improvement over standard XGBoost. Gen-0 is easily identified (F1 = 0.95), but deeper classes are mutually confusable: gen-4 F1 is only 0.28. The bottleneck is feature resolution, not classifier architecture---DDR feature drift slopes flatten after depth 2, making adjacent deep generations indistinguishable. This establishes 3-class (gen-0/gen-1/gen-2+) as the practical resolution ceiling, with principled boundaries aligned to feature discriminability.\n\n\\subsection{Scale Effect}\n\\label{sec:scale}\n\nAdding Qwen3-8B (Table~\\ref{tab:scale}) tests whether depth signal persists in larger generators.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Generator} & \\textbf{Size} & \\textbf{Bin.~F1} & \\textbf{hpx $\\rho$} & \\textbf{ent $\\rho$} \\\\\n\\midrule\nPythia-1B & 1B & 0.856 & $-0.63$ & $-0.60$ \\\\\nQwen3-0.6B & 0.6B & 0.824 & $-0.58$ & $-0.56$ \\\\\nPythia-2.8B & 2.8B & 0.804 & $-0.61$ & $-0.60$ \\\\\nQwen3-1.7B & 1.7B & 0.805 & $-0.59$ & $-0.55$ \\\\\nOLMo-2-1B & 1.5B & 0.764 & $-0.60$ & $-0.50$ \\\\\nQwen3-8B & 8B & 0.683 & $-0.56$ & $-0.48$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Scale effect (6-gen LOGO held-out results). Qwen3-8B shows moderate degradation (0.683) but DDR structure is qualitatively preserved. 6-gen LOGO average: 0.789.}\n\\label{tab:scale}\n\\end{table}\n\nQwen3-8B held-out binary F1 = 0.683---lower than smaller generators but still well above random (0.50). The DDR three-tier structure is qualitatively preserved: hapax ($-0.56$) and TTR ($-0.54$) remain strongly drifting, while tail decay ($-0.09$) stays near-stationary. Surface features are relatively more robust to scale (hapax $|\\rho|$ drops 11\\%) than reference features (entropy mean $|\\rho|$ drops 20\\%).\n\n\\subsection{Robustness to Simulated Editing}\n\\label{sec:robustness}\n\nTable~\\ref{tab:editing} tests robustness to simulated human editing.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Edit Type} & \\textbf{Bin.~F1} & \\textbf{Drop} & \\textbf{95\\% CI} \\\\\n\\midrule\nNone (baseline) & 0.695 & --- & [0.679, 0.711] \\\\\nRandom 5\\% & 0.650 & $-4.5$ & [0.633, 0.667] \\\\\nRandom 10\\% & 0.614 & $-8.1$ & [0.596, 0.632] \\\\\nRandom 20\\% & 0.591 & $-10.4$ & [0.573, 0.609] \\\\\nLLM rephrase & 0.647 & $-4.5$ & [0.631, 0.662] \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Robustness to simulated editing. The signal degrades gracefully: $-4.5$pp at 5\\% random or LLM rephrase, $-10.4$pp at 20\\% random. Even at 20\\% replacement, F1 remains above random baseline.}\n\\label{tab:editing}\n\\end{table}\n\nThe depth signal degrades gracefully under simulated editing. LLM-simulated rephrasing (${\\sim}$1.7 sentences replaced per document) produces comparable degradation to 5\\% random word replacement ($-4.5$pp each). Even at 20\\% random replacement (F1 = 0.591), classification remains substantially above chance. Surface features are most vulnerable to word-level perturbation, while reference features are more robust because sentence-level perplexity is less sensitive to individual token replacements.\n\n\\subsection{End-to-End Classifier Comparison}\n\\label{sec:e2e}\n\nTable~\\ref{tab:e2e} compares the lightweight 7-feature ensemble against QLoRA fine-tuned end-to-end classifiers.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Method} & \\textbf{Eval} & \\textbf{3-cl.} & \\textbf{Bin.} & \\textbf{Cost} \\\\\n\\midrule\n7-feat XGBoost & LOGO & 0.762 & 0.694 & 1$\\times$ \\\\\nQLoRA Qwen-Inst & CV & 0.907 & 0.867 & 12$\\times$ \\\\\nQLoRA OLMo-Inst & CV & 0.888 & 0.836 & 12$\\times$ \\\\\nQLoRA Qwen-Base & CV & 0.904 & 0.860 & 12$\\times$ \\\\\nQLoRA OLMo-Base & CV & 0.859 & 0.793 & 12$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{End-to-end (QLoRA) vs handcrafted features. QLoRA is evaluated under within-generator CV (not LOGO), making direct comparison unfair. QLoRA 5-class F1 ranges 0.540--0.598, confirming the resolution ceiling is feature-intrinsic, not method-limited.}\n\\label{tab:e2e}\n\\end{table}\n\nQLoRA classifiers achieve substantially higher within-distribution performance (best 3-class F1 = 0.907), but are evaluated under within-generator CV, not LOGO---a fundamentally easier setting. End-to-end models are expected to degrade substantially under LOGO due to overfitting to generator-specific artifacts. The 7-feature ensemble's advantages are interpretability, efficiency (CPU-only, 1$\\times$ cost vs 12$\\times$ with 8.5GB GPU), and demonstrated cross-generator generalization under LOGO. Even with QLoRA, 5-class F1 remains 0.540--0.598, confirming the resolution ceiling is feature-intrinsic.\n\n\\subsection{Text Length Confound Analysis}\n\\label{sec:length}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lll}\n\\toprule\n\\textbf{Analysis} & \\textbf{Result} & \\textbf{Conclusion} \\\\\n\\midrule\n$\\rho$(length, depth) & [$-0.07$, $+0.13$] & Weak ($|\\rho| < 0.14$) \\\\\nLength-norm.\\ drift & preserved, stronger & Depth $\\perp$ length \\\\\nLen-matched F1 & 0.724 vs 0.770 & Sample-size effect \\\\\nRand.\\ subsample & ${\\sim}$0.730 (same $n$) & Confirms above \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Length confound analysis. Text length is not a confound: depth-length correlation is weak, and length normalization strengthens feature drift.}\n\\label{tab:length}\n\\end{table}\n\nText length is not a confound for depth classification (Table~\\ref{tab:length}). Depth-length Spearman correlations are weak ($|\\rho| < 0.14$). After length normalization, TTR and hapax depth drift are preserved and strengthened. The 4.6pp F1 drop under length-matched subsampling is attributable to reduced sample size (random subsample control at the same $n$ yields ${\\sim}$0.730), not confound removal.\n\n\\subsection{LD-Score as Additional Feature}\n\\label{sec:ldscore}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Feature Set} & \\textbf{LOGO Bin.~F1} & \\textbf{$\\Delta$} \\\\\n\\midrule\n7 features & 0.694 & --- \\\\\n7 features + LD-Score & 0.700 & $+0.6$ \\\\\nLD-Score alone & 0.721 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{LD-Score as additional feature. Marginal gain (+0.6pp) reflects high redundancy with hapax ratio ($r = 0.75$). LD-Score alone achieves 0.721 LOGO F1 but with wide cross-generator variance [0.588, 0.770].}\n\\label{tab:ldscore}\n\\end{table}\n\nAdding LD-Score (a character-level distribution signature) as an 8th feature provides only +0.6pp marginal gain (Table~\\ref{tab:ldscore}), reflecting high redundancy with hapax ratio ($r = 0.75$). LD-Score's strong ordinal signal ($\\rho = -0.79$) confirms that depth-induced distributional drift manifests at the character level, but its information is largely captured by existing surface features. We retain the 7-feature design for parsimony.\n\n%------------------------------------------------------------\n\\section{Conclusion}\n\\label{sec:conclusion}\n%------------------------------------------------------------\n\nWe formulated generation depth classification as a task beyond binary AI-text detection and characterized differential depth response (DDR) across 5 base-model generators from 3 families. A lightweight 7-feature ensemble achieves leak-free binary F1 = 0.694 under LOGO evaluation, ranging 0.656--0.724 per generator, and 0.830 on cross-model chains. DDR is robust across tested decoding strategies (greedy, top-k) and three reference models from different families.\n\nOur most robust finding is negative: depth-aware data curation is statistically equivalent to random subsampling for downstream CLM quality. Depth fingerprinting is diagnostic---useful for provenance characterization---not curative for data selection.\n\nThe signal degrades substantially under instruction tuning (OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base), restricting current scope to base models. This degradation is itself a finding: instruction tuning compresses the distributional variation DDR exploits. Future work should investigate whether alternative feature families can recover depth signal in instruct models, extend evaluation to larger frontier models ($>$14B), and incorporate additional decoding strategies (nucleus sampling, beam search) to strengthen robustness claims.\n\n%------------------------------------------------------------\n\\section*{Limitations}\n%------------------------------------------------------------\n\nOur study has several limitations. First, all experiments use base models; instruction-tuned models show severely degraded signal, and extending depth fingerprinting to the instruct regime remains open. Second, our decoding robustness analysis covers greedy and top-k sampling; claims should be considered preliminary until validated on nucleus sampling and beam search. Third, the downstream utility experiment uses only perplexity on a single CLM task with 3 seeds---additional tasks and metrics are needed to confirm the ``diagnostic not curative'' conclusion broadly.\n\n\\bibliography{custom}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8ea5b63-d13d-41fe-8d9f-916049b6d180",
  "isSidechain": false,
  "requestId": "req_011CbGUa5mMcuoWEbH6CEGfn",
  "type": "assistant",
  "uuid": "72414c20-c97c-4f74-911b-877878eb4910",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DF9d6MZtp8N7MejZDchkxU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 233,
      "cache_read_input_tokens": 51343,
      "output_tokens": 10941,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 233,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10941,
          "cache_read_input_tokens": 51343,
          "cache_creation_input_tokens": 233,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 233
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

_source line 19 · 2026-05-21T22:11:14.716Z_

<details><summary>↩ Tool result · `toolu_01BeSc5vRxVod6LDP8t3hgFy`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72414c20-c97c-4f74-911b-877878eb4910",
  "isSidechain": false,
  "promptId": "a05c3ff7-21d6-48e6-b124-f66048f4fb96",
  "type": "user",
  "uuid": "0dfd8f15-3cff-4cbd-a59d-7b29bdcb9542",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\n\\title{Generation Depth Fingerprinting: Classifying Recursive LLM Output\\\\Beyond Binary Detection}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nWeb-scraped training corpora increasingly contain LLM-generated text of unknown provenance depth---material that has been recursively generated one or more times. Current detectors offer only binary real-vs-synthetic classification, conflating qualitatively different generations. We formulate \\textbf{generation depth classification} (gen-0 / gen-1 / gen-2+) and characterize \\textbf{differential depth response} (DDR): central-tendency features (entropy mean, TTR, hapax ratio) drift monotonically with depth ($|\\rho| > 0.60$), while distributional shape features (entropy max, tail decay) remain near-stationary ($|\\rho| < 0.10$), with a ${\\sim}10\\times$ gap in KS statistics between groups. A lightweight 7-feature ensemble achieves leak-free binary F1 = 0.694 (95\\% CI [0.688, 0.700]) under 8-generator leave-one-generator-out (LOGO) evaluation across 5 model families (0.6B--8B), and 0.830 on cross-model chains. DDR is robust across tested decoding strategies (greedy, top-k) and three reference models from different families. We show that depth-aware data curation is statistically equivalent to random subsampling for downstream CLM quality (TOST $p = 1.1 \\times 10^{-4}$ at $\\pm 2\\%$ margin), establishing depth fingerprinting as a \\textit{diagnostic} tool for provenance characterization rather than a curative one for data selection. The signal degrades substantially under instruction tuning, restricting current scope to base models.\n\\end{abstract}\n\n%------------------------------------------------------------\n\\section{Introduction}\n\\label{sec:intro}\n%------------------------------------------------------------\n\nLarge language models (LLMs) are increasingly deployed at scale, and their outputs feed back into the training pipelines of subsequent models. Recent estimates suggest 7--17\\% of scientific papers may contain LLM-generated content, and web crawls used for pretraining are progressively contaminated with synthetic text of varying provenance. This recursive contamination---where model-generated text is regenerated by the same or different models---raises fundamental questions about data quality and the distributional properties of recursively generated text.\n\nCurrent AI-text detection methods frame the problem as binary classification: human-written vs.\\ machine-generated. This conflation obscures meaningful differences. First-generation text (gen-1) retains much of the source distribution's lexical properties, while deeper generations (gen-2+) exhibit measurably reduced vocabulary diversity and compressed perplexity distributions. Existing detectors such as FastDetectGPT \\cite{bao2024fast}, Binoculars \\cite{hans2024binoculars}, and LD-Score cannot distinguish these qualitatively different materials.\n\nWe move beyond binary detection and formulate \\textbf{generation depth classification}: given a text passage and a reference language model, estimate whether the text is original (gen-0), first-generation synthetic (gen-1), or deeper-generation synthetic (gen-2+). Our central empirical finding is \\textbf{differential depth response} (DDR): features measuring central tendency and lexical diversity drift monotonically with generation depth, while features capturing distributional shape remain approximately stationary. This is consistent with recursive generation inducing a location shift in the NLL distribution while preserving its shape.\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{Task formulation}: Generation depth classification as a new problem beyond binary detection, with a rigorous LOGO evaluation protocol that prevents generator leakage.\n\\item \\textbf{Empirical characterization of DDR} across 5 generators from 3 families (0.6B--8B), validated with 3 reference models. DDR is robust across tested decoding strategies (greedy, top-k).\n\\item \\textbf{Negative finding}: Depth-aware curation does not improve downstream CLM quality over random subsampling (TOST-confirmed equivalence), positioning depth fingerprinting as diagnostic rather than curative.\n\\end{enumerate}\n\n%------------------------------------------------------------\n\\section{Related Work}\n\\label{sec:related}\n%------------------------------------------------------------\n\n\\paragraph{AI-Text Detection.}\nPerplexity-based detectors leverage the observation that model-generated text has lower perplexity under the generating model. GLTR \\cite{gehrmann2019gltr} visualizes token-level statistics; DetectGPT \\cite{mitchell2023detectgpt} uses perturbation-based log-probability curvature; FastDetectGPT \\cite{bao2024fast} replaces perturbations with conditional sampling for efficiency; Binoculars \\cite{hans2024binoculars} contrasts two models' cross-entropy scores. All produce binary decisions and do not estimate generation depth. When repurposed as ordinal depth predictors (using continuous scores as features), these methods show high cross-generator variance and substantially lower performance than multi-feature approaches.\n\n\\paragraph{Model Collapse and Iterative Generation.}\n\\citet{shumailov2024ai} show that training on model-generated data leads to ``model collapse'' with progressive distribution narrowing. The ``LLM as Broken Telephone'' framework (ACL 2025) demonstrates that paraphrasing chains converge to attractor states within ${\\sim}3$ iterations under semantic-preservation constraints. Our work differs in studying non-paraphrastic continuation chains, where the absence of semantic constraints permits monotonic drift beyond the attractor horizon.\n\n\\paragraph{Data Quality and OOD Detection.}\nPerplexity-based data scoring is standard in pretraining pipelines. Our reference-model features (entropy statistics, tail decay) are related to OOD detection methods that use NLL distribution properties. The distinction is that we exploit the \\textit{ordinal} structure of depth-induced distributional shift rather than binary in-vs-out classification.\n\n\\paragraph{Authorship Attribution and Stylometry.}\nSurface features such as TTR and hapax legomena ratio have long histories in authorship attribution. We repurpose these as depth indicators, showing they capture vocabulary impoverishment across recursive generation.\n\n%------------------------------------------------------------\n\\section{Method}\n\\label{sec:method}\n%------------------------------------------------------------\n\n\\subsection{Problem Formulation}\n\nGiven a text passage $x$ and a reference model $M_\\text{ref}$, we classify $x$ into one of three depth classes: gen-0 (original human text), gen-1 (first-generation LLM output), or gen-2+ (deeper recursive generations). We define \\textbf{generation depth} operationally: depth $d$ text is produced by feeding depth $d{-}1$ text as a prompt to a generator model, starting from human-written seeds at $d{=}0$.\n\n\\subsection{Feature Design}\n\nWe extract 7 features per passage, divided into two groups motivated by the DDR hypothesis:\n\n\\paragraph{Surface features (2):} Type-Token Ratio (TTR) and hapax legomena ratio. These capture vocabulary diversity, which decreases monotonically with generation depth as models converge toward high-frequency token distributions.\n\n\\paragraph{Reference features (5):} Given reference model $M_\\text{ref}$, we compute token-level negative log-likelihood (NLL) values and extract: entropy mean, entropy standard deviation, entropy minimum, entropy maximum, and tail decay rate. These capture properties of the NLL distribution that respond differentially to generation depth.\n\n\\subsection{Differential Depth Response (DDR)}\n\nWe classify features into three groups based on their Spearman correlation $\\rho$ with depth and KS test statistics:\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Drifting} ($|\\rho| > 0.50$, KS $> 0.50$): hapax ratio ($\\rho = -0.63$), TTR ($-0.61$), entropy mean ($-0.60$).\n\\item \\textbf{Moderate} ($0.10 < |\\rho| < 0.50$): entropy min ($-0.35$), entropy std ($-0.12$).\n\\item \\textbf{Near-stationary} ($|\\rho| < 0.10$, KS $< 0.06$): entropy max ($0.06$), tail decay ($0.04$).\n\\end{itemize}\n\nThe ${\\sim}10\\times$ gap in KS statistics between drifting features (0.516--0.537) and near-stationary features (0.043--0.052) provides non-parametric confirmation of the three-tier DDR structure.\n\n\\subsection{Classifier}\n\nWe train an XGBoost classifier on the 7-feature vector. Evaluation follows the leave-one-generator-out (LOGO) protocol: models are trained on chains from $N{-}1$ generators and tested on the held-out generator, ensuring no generator-specific artifacts leak into evaluation. The primary metric is \\textbf{leak-free binary F1} (gen-1 vs.\\ gen-2+), excluding gen-0 to avoid seed-sharing leakage between gen-0 samples across generators.\n\n\\subsection{Chain Construction}\n\nWe construct recursive generation chains of depth 0--4 using three prompt types:\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Continuation}: Direct text continuation from the previous depth's output.\n\\item \\textbf{Elaboration}: Prompted to elaborate on the previous depth's content.\n\\item \\textbf{Inspired rewriting}: Prompted to rewrite inspired by the previous content.\n\\end{itemize}\n\nSeeds are drawn from multiple domains (Wikipedia, news, academic, code) with 500--1000 seeds per domain.\n\n%------------------------------------------------------------\n\\section{Experiments}\n\\label{sec:experiments}\n%------------------------------------------------------------\n\n\\subsection{Setup}\n\nWe evaluate on 5 base-model generators spanning 3 families: Pythia-2.8B, Pythia-1B (Pythia family), OLMo-2-1B (OLMo), Qwen3-1.7B, and Qwen3-0.6B (Qwen). An additional large-scale experiment includes Qwen3-8B. The default reference model is Pythia-410M; cross-reference experiments use OLMo-2-1B and Qwen3-0.6B as alternative references. Total dataset: 18,423 passages across 5 generators.\n\n\\subsection{Feature Ablation and DDR Analysis}\n\\label{sec:ablation}\n\nTable~\\ref{tab:ablation} shows the feature ablation results on Pythia-2.8B using 5-fold cross-validation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Feature Set} & \\textbf{Macro F1} & \\textbf{95\\% CI} \\\\\n\\midrule\nFull (7 features) & 0.820 & [0.807, 0.833] \\\\\nSurface-only (TTR + hapax) & 0.763 & [0.747, 0.774] \\\\\nReference-only (5 entropy + tail) & 0.719 & [0.706, 0.733] \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Feature ablation (5-fold CV, Pythia-2.8B). McNemar's test confirms Full $>$ Surface $>$ Reference (all $p \\approx 0$).}\n\\label{tab:ablation}\n\\end{table}\n\nThe full feature set significantly outperforms both subsets, confirming feature complementarity. Surface features contribute more individually (+4.4pp over reference-only), but reference features provide independent complementary signal (+5.7pp when added to surface).\n\nTable~\\ref{tab:ddr} presents the DDR feature classification. Drifting features exhibit KS statistics 0.516--0.537, while near-stationary features show 0.043--0.052---a ${\\sim}10\\times$ gap that provides non-parametric confirmation of DDR.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Feature} & \\textbf{Spearman $\\rho$} & \\textbf{KS} & \\textbf{DDR Group} \\\\\n\\midrule\nhapax\\_ratio & $-0.63$ & 0.537 & drifting \\\\\nTTR & $-0.61$ & 0.516 & drifting \\\\\nentropy\\_mean & $-0.60$ & 0.528 & drifting \\\\\nentropy\\_min & $-0.35$ & 0.052 & moderate \\\\\nentropy\\_std & $-0.12$ & 0.043 & moderate \\\\\nentropy\\_max & $+0.06$ & 0.048 & near-stationary \\\\\ntail\\_decay & $+0.04$ & 0.045 & near-stationary \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{DDR feature classification. Drifting features show strong monotonic depth correlation and high distributional shift; near-stationary features show negligible response.}\n\\label{tab:ddr}\n\\end{table}\n\nMedian perplexity decreases monotonically with depth (13.50, 4.96, 3.00, 2.07, 1.72 for depths 0--4), validating the location-shift interpretation: recursive generation progressively moves the NLL distribution toward lower values.\n\n\\subsection{Cross-Generator Evaluation}\n\\label{sec:cross_gen}\n\nTable~\\ref{tab:logo} reports per-generator results under 5-generator LOGO evaluation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Generator} & \\textbf{Family} & \\textbf{Size} & \\textbf{Bin.~F1} & \\textbf{3-cl.~F1} \\\\\n\\midrule\nPythia-2.8B & Pythia & 2.8B & 0.724 & 0.812 \\\\\nPythia-1B & Pythia & 1B & 0.721 & 0.851 \\\\\nQwen3-1.7B & Qwen & 1.7B & 0.688 & 0.811 \\\\\nOLMo-2-1B & OLMo & 1.5B & 0.662 & 0.752 \\\\\nQwen3-0.6B & Qwen & 0.6B & 0.656 & 0.819 \\\\\n\\midrule\n\\textbf{Average} & & & \\textbf{0.694} & \\textbf{0.804} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{LOGO per-generator results. Binary F1 = gen-1 vs gen-2+ (leak-free). Per-generator range: 0.656--0.724 (6.8pp spread).}\n\\label{tab:logo}\n\\end{table}\n\nThe LOGO binary F1 of 0.694 [0.688, 0.700] demonstrates that the depth signal generalizes to unseen generators. The 6.8pp per-generator spread (0.656--0.724) reflects generator-specific variation in depth signal strength. Feature importance is stable across generators: hapax ratio (0.289), TTR (0.168), entropy mean (0.160).\n\n\\paragraph{Cross-family transfer.} Leave-one-family-out (LOFO) evaluation confirms robust cross-family generalization (Table~\\ref{tab:lofo}). The average LOFO binary F1 of 0.686 is only 0.8pp below LOGO, indicating that depth features transfer across model families.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Held-out Family} & \\textbf{Binary F1} & \\textbf{$\\Delta$ vs LOGO} \\\\\n\\midrule\nPythia & 0.678 & $-0.016$ \\\\\nOLMo & 0.691 & $-0.003$ \\\\\nQwen & 0.689 & $-0.005$ \\\\\n\\midrule\n\\textbf{Average} & \\textbf{0.686} & $-0.008$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{LOFO cross-family transfer. Delta vs LOGO is minimal ($-0.8$pp average).}\n\\label{tab:lofo}\n\\end{table}\n\n\\subsection{Cross-Reference Model Validation}\n\\label{sec:cross_ref}\n\nTo verify DDR is not an artifact of the Pythia-410M reference, we replicate with OLMo-2-1B and Qwen3-0.6B as reference models (Table~\\ref{tab:ref_model}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Reference} & \\textbf{Size} & \\textbf{3-cl.~F1} & \\textbf{ent.~drift} & \\textbf{$|$tail $\\rho|$} \\\\\n\\midrule\nPythia-410M & 410M & 0.803 & [$-1.19$, $-1.40$] & 0.05 \\\\\nOLMo-2-1B & 1.5B & 0.807 & [$-0.61$, $-0.91$] & 0.07 \\\\\nQwen3-0.6B & 0.6B & 0.816 & [$-0.96$, $-1.35$] & 0.04 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Reference model comparison. DDR direction is consistent across all references; LOGO F1 varies only 1.3pp. Drift magnitude is reference-dependent (OLMo ${\\sim}50\\%$ of Pythia), but the drifting/stationary classification is preserved.}\n\\label{tab:ref_model}\n\\end{table}\n\nAll three references yield consistent DDR: entropy drift is uniformly negative, tail decay $|\\rho|$ remains below 0.07, and LOGO 3-class F1 ranges 0.803--0.816 (1.3pp spread). Greedy decoding shape stability is confirmed across all references (mean $|d|$ = 0.05--0.06). While drift magnitude varies by reference (OLMo reference drift is ${\\sim}50\\%$ of Pythia's), the qualitative DDR structure---drifting vs.\\ near-stationary---is preserved.\n\n\\subsection{Baseline Comparison}\n\\label{sec:baselines}\n\nTable~\\ref{tab:baselines} compares the 7-feature ensemble against existing detectors repurposed as ordinal depth predictors.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{F1} & \\textbf{95\\% CI} & \\textbf{$\\rho$} & \\textbf{Type} \\\\\n\\midrule\n7-feat ensemble & 0.798 & [.786, .799] & --- & multi \\\\\nAvg-LogProb & 0.765 & [.616, .820] & $-0.79$ & single \\\\\nLD-Score & 0.721 & [.588, .770] & $-0.79$ & single \\\\\nFastDetectGPT & 0.627 & [.511, .762] & $-0.43$ & single \\\\\nBinoculars & 0.579 & [.405, .664] & $-0.20$ & single \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Ordinal baseline comparison (LOGO 3-class F1). The 7-feature ensemble outperforms all single detectors (+3.3pp vs best, $p < 0.001$) with substantially narrower CI, reflecting robust cross-generator behavior.}\n\\label{tab:baselines}\n\\end{table}\n\nThe 7-feature ensemble outperforms the best single detector (Avg-LogProb) by 3.3pp ($p < 0.001$, bootstrap). More importantly, its CI [0.786, 0.799] is far narrower than Avg-LogProb's [0.616, 0.820], demonstrating consistent performance across generators. Single detectors designed for binary classification show high cross-generator variance when repurposed for ordinal depth prediction---their ordinal utility is limited.\n\n\\subsection{Downstream Utility: A Negative Finding}\n\\label{sec:downstream}\n\nWe test whether depth-aware data curation improves downstream language modeling quality by fine-tuning OLMo-1B on depth-stratified subsets (3 seeds each). Table~\\ref{tab:downstream} reports perplexity results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Variant} & \\textbf{$n$} & \\textbf{PPL} & \\textbf{TOST $p$} \\\\\n\\midrule\nAll depths & 12,299 & 2.335 $\\pm$ 0.000 & --- \\\\\nSize-matched random & 3,951 & 2.367 $\\pm$ 0.000 & ref \\\\\nDepth 0+1 only & 3,951 & 2.387 $\\pm$ 0.001 & $1.1{\\times}10^{-4}$ \\\\\nBinary-filtered & 3,951 & 2.389 $\\pm$ 0.001 & ${\\sim}10^{-4}$ \\\\\nDepth 0 only & 797 & 2.681 $\\pm$ 0.001 & reject \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Downstream CLM quality by training data composition. TOST at $\\pm 2\\%$ margin confirms statistical equivalence between size-matched random subsampling and depth-filtered variants. Depth 0 only is worse due to sample size, not depth quality.}\n\\label{tab:downstream}\n\\end{table}\n\nDepth-aware curation does not improve downstream CLM quality. At equal sample count ($n = 3{,}951$), random subsampling (PPL = 2.367) is statistically equivalent to depth 0+1 filtering (PPL = 2.387; TOST $p = 1.1 \\times 10^{-4}$ at $\\pm 2\\%$ margin). The depth-0-only variant (PPL = 2.681) is substantially worse, but this reflects sample size reduction (only 797 texts) rather than depth quality effects. Seed variance is minimal ($< 0.002$), confirming reproducibility.\n\nThis negative finding is the most robust of our claims: depth fingerprinting is a \\textit{diagnostic} tool for provenance characterization, not a curative tool for data curation.\n\n\\subsection{Prompt-Type Analysis}\n\\label{sec:prompt}\n\nTable~\\ref{tab:prompt} reports performance by prompt type.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Prompt} & \\textbf{CV F1} & \\textbf{Ret.} & \\textbf{hapax $\\rho$} & \\textbf{ent. $\\rho$} \\\\\n\\midrule\nContinuation & 0.781 & 0.831 & $-0.74$ & $-0.56$ \\\\\nRewriting & 0.737 & 0.939 & $-0.80$ & $-0.48$ \\\\\nElaboration & 0.730 & 0.986 & $-0.83$ & $-0.47$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Prompt-type comparison (Pythia-2.8B). Ret.\\ = depth retention (fraction of chains reaching depth 4). Continuation shows strongest classification signal; elaboration preserves more chains but with weaker signal.}\n\\label{tab:prompt}\n\\end{table}\n\nContinuation chains yield the strongest depth signal (CV F1 = 0.781), while elaboration is weakest (0.730)---a 5.1pp gap reflecting moderate prompt-type dependence. The leave-one-prompt-type-out (LOPTO) average F1 of 0.753 confirms reasonable cross-prompt transfer.\n\n\\subsection{Paraphrastic Comparison}\n\\label{sec:paraphrastic}\n\nTo connect with attractor cycle theory, we compare continuation and paraphrastic chains (Table~\\ref{tab:para}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Chain} & \\textbf{Bin.~F1} & \\textbf{3-cl.} & \\textbf{hpx $\\rho$} & \\textbf{ent $\\rho$} & \\textbf{Conv.} \\\\\n\\midrule\nContin. & 0.695 & 0.762 & $-0.63$ & $-0.60$ & $>$d4 \\\\\nParaph. & 0.572 & 0.580 & $-0.24$ & $-0.12$ & ${\\sim}$d2.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Paraphrastic vs continuation chains. Conv.\\ = approximate attractor convergence depth. Paraphrastic chains converge to attractor states by ${\\sim}$depth 2.5, severely attenuating depth signal.}\n\\label{tab:para}\n\\end{table}\n\nParaphrastic chains yield binary F1 of only 0.572 ($\\Delta = -12.3$pp vs continuation), with hapax $|\\rho|$ dropping from 0.63 to 0.24. The semantic-preservation constraint locks paraphrastic distributions onto an attractor manifold by ${\\sim}$depth 2.5, consistent with prior work on iterative paraphrasing. This confirms that our DDR characterization applies specifically to non-paraphrastic chains where the absence of semantic constraints permits sustained monotonic drift.\n\n\\subsection{Cross-Model Chains}\n\\label{sec:cross_model}\n\nTo simulate realistic web contamination where different generators contribute at each depth step, we construct cross-model chains (Table~\\ref{tab:cross_model}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Evaluation} & \\textbf{Bin.~F1} & \\textbf{95\\% CI} & \\textbf{hpx $\\rho$} \\\\\n\\midrule\nCross-model (gen-LOGO) & 0.830 & [.815, .845] & $-0.68$ \\\\\nCross-model (comp-LOGO) & 0.764 & [.745, .783] & $-0.65$ \\\\\nSingle-model (LOGO) & 0.694 & [.688, .700] & $-0.63$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model vs single-model chains. Architecture heterogeneity amplifies depth signal (+13.6pp binary F1), partly attributable to architecture-mixing effects layered on top of depth-intrinsic drift.}\n\\label{tab:cross_model}\n\\end{table}\n\nCross-model chains yield binary F1 = 0.830 under generator-level LOGO, +13.6pp over single-model LOGO. Architecture differences at each depth step introduce additional distributional shifts that amplify the depth signal. The composition-level LOGO (0.764) is lower, indicating that specific generator combinations do not fully transfer.\n\n\\subsection{Multi-Domain Analysis}\n\\label{sec:domains}\n\nTable~\\ref{tab:domains} shows binary F1 across four seed domains.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Domain} & \\textbf{Binary F1} & \\textbf{95\\% CI} & \\textbf{Seeds} \\\\\n\\midrule\nWikipedia & 0.815 & [0.798, 0.832] & 1000 \\\\\nCode & 0.754 & [0.737, 0.770] & 500 \\\\\nNews & 0.746 & [0.726, 0.764] & 500 \\\\\nAcademic & 0.739 & [0.720, 0.757] & 500 \\\\\n\\midrule\nCross-domain LOGO & 0.700 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Multi-domain binary F1. Max gap vs Wikipedia is 7.6pp. Cross-domain LOGO (0.700) confirms depth signal is domain-robust.}\n\\label{tab:domains}\n\\end{table}\n\nWikipedia yields the highest F1 (0.815), likely due to distributional alignment with pretraining data. Academic text is lowest (0.739) because its inherently specialized vocabulary compresses the feature margin. The cross-domain LOGO (0.700) is close to the overall LOGO (0.694), confirming moderate domain independence.\n\n\\subsection{Finer-Grained Ordinal Classification}\n\\label{sec:ordinal}\n\nTable~\\ref{tab:ordinal} tests whether finer granularity is achievable.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{5-cl.~F1} & \\textbf{3-cl.~F1} & \\textbf{$\\Delta$} \\\\\n\\midrule\nXGBoost & 0.500 & 0.762 & $-0.262$ \\\\\nCORAL (ordinal) & 0.500 & --- & --- \\\\\nFrank-Hall (ordinal) & 0.490 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Ordinal granularity comparison. 5-class F1 drops to ${\\sim}$0.50 regardless of method. Adjacent-depth confusion rates: gen-1/gen-2 44\\%, gen-2/gen-3 53\\%, gen-3/gen-4 59\\%.}\n\\label{tab:ordinal}\n\\end{table}\n\nFive-class classification yields F1 ${\\sim}$0.50, and ordinal methods (CORAL, Frank-Hall) provide no improvement over standard XGBoost. Gen-0 is easily identified (F1 = 0.95), but deeper classes are mutually confusable: gen-4 F1 is only 0.28. The bottleneck is feature resolution, not classifier architecture---DDR feature drift slopes flatten after depth 2, making adjacent deep generations indistinguishable. This establishes 3-class (gen-0/gen-1/gen-2+) as the practical resolution ceiling, with principled boundaries aligned to feature discriminability.\n\n\\subsection{Scale Effect}\n\\label{sec:scale}\n\nAdding Qwen3-8B (Table~\\ref{tab:scale}) tests whether depth signal persists in larger generators.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Generator} & \\textbf{Size} & \\textbf{Bin.~F1} & \\textbf{hpx $\\rho$} & \\textbf{ent $\\rho$} \\\\\n\\midrule\nPythia-1B & 1B & 0.856 & $-0.63$ & $-0.60$ \\\\\nQwen3-0.6B & 0.6B & 0.824 & $-0.58$ & $-0.56$ \\\\\nPythia-2.8B & 2.8B & 0.804 & $-0.61$ & $-0.60$ \\\\\nQwen3-1.7B & 1.7B & 0.805 & $-0.59$ & $-0.55$ \\\\\nOLMo-2-1B & 1.5B & 0.764 & $-0.60$ & $-0.50$ \\\\\nQwen3-8B & 8B & 0.683 & $-0.56$ & $-0.48$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Scale effect (6-gen LOGO held-out results). Qwen3-8B shows moderate degradation (0.683) but DDR structure is qualitatively preserved. 6-gen LOGO average: 0.789.}\n\\label{tab:scale}\n\\end{table}\n\nQwen3-8B held-out binary F1 = 0.683---lower than smaller generators but still well above random (0.50). The DDR three-tier structure is qualitatively preserved: hapax ($-0.56$) and TTR ($-0.54$) remain strongly drifting, while tail decay ($-0.09$) stays near-stationary. Surface features are relatively more robust to scale (hapax $|\\rho|$ drops 11\\%) than reference features (entropy mean $|\\rho|$ drops 20\\%).\n\n\\subsection{Robustness to Simulated Editing}\n\\label{sec:robustness}\n\nTable~\\ref{tab:editing} tests robustness to simulated human editing.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Edit Type} & \\textbf{Bin.~F1} & \\textbf{Drop} & \\textbf{95\\% CI} \\\\\n\\midrule\nNone (baseline) & 0.695 & --- & [0.679, 0.711] \\\\\nRandom 5\\% & 0.650 & $-4.5$ & [0.633, 0.667] \\\\\nRandom 10\\% & 0.614 & $-8.1$ & [0.596, 0.632] \\\\\nRandom 20\\% & 0.591 & $-10.4$ & [0.573, 0.609] \\\\\nLLM rephrase & 0.647 & $-4.5$ & [0.631, 0.662] \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Robustness to simulated editing. The signal degrades gracefully: $-4.5$pp at 5\\% random or LLM rephrase, $-10.4$pp at 20\\% random. Even at 20\\% replacement, F1 remains above random baseline.}\n\\label{tab:editing}\n\\end{table}\n\nThe depth signal degrades gracefully under simulated editing. LLM-simulated rephrasing (${\\sim}$1.7 sentences replaced per document) produces comparable degradation to 5\\% random word replacement ($-4.5$pp each). Even at 20\\% random replacement (F1 = 0.591), classification remains substantially above chance. Surface features are most vulnerable to word-level perturbation, while reference features are more robust because sentence-level perplexity is less sensitive to individual token replacements.\n\n\\subsection{End-to-End Classifier Comparison}\n\\label{sec:e2e}\n\nTable~\\ref{tab:e2e} compares the lightweight 7-feature ensemble against QLoRA fine-tuned end-to-end classifiers.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Method} & \\textbf{Eval} & \\textbf{3-cl.} & \\textbf{Bin.} & \\textbf{Cost} \\\\\n\\midrule\n7-feat XGBoost & LOGO & 0.762 & 0.694 & 1$\\times$ \\\\\nQLoRA Qwen-Inst & CV & 0.907 & 0.867 & 12$\\times$ \\\\\nQLoRA OLMo-Inst & CV & 0.888 & 0.836 & 12$\\times$ \\\\\nQLoRA Qwen-Base & CV & 0.904 & 0.860 & 12$\\times$ \\\\\nQLoRA OLMo-Base & CV & 0.859 & 0.793 & 12$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{End-to-end (QLoRA) vs handcrafted features. QLoRA is evaluated under within-generator CV (not LOGO), making direct comparison unfair. QLoRA 5-class F1 ranges 0.540--0.598, confirming the resolution ceiling is feature-intrinsic, not method-limited.}\n\\label{tab:e2e}\n\\end{table}\n\nQLoRA classifiers achieve substantially higher within-distribution performance (best 3-class F1 = 0.907), but are evaluated under within-generator CV, not LOGO---a fundamentally easier setting. End-to-end models are expected to degrade substantially under LOGO due to overfitting to generator-specific artifacts. The 7-feature ensemble's advantages are interpretability, efficiency (CPU-only, 1$\\times$ cost vs 12$\\times$ with 8.5GB GPU), and demonstrated cross-generator generalization under LOGO. Even with QLoRA, 5-class F1 remains 0.540--0.598, confirming the resolution ceiling is feature-intrinsic.\n\n\\subsection{Text Length Confound Analysis}\n\\label{sec:length}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lll}\n\\toprule\n\\textbf{Analysis} & \\textbf{Result} & \\textbf{Conclusion} \\\\\n\\midrule\n$\\rho$(length, depth) & [$-0.07$, $+0.13$] & Weak ($|\\rho| < 0.14$) \\\\\nLength-norm.\\ drift & preserved, stronger & Depth $\\perp$ length \\\\\nLen-matched F1 & 0.724 vs 0.770 & Sample-size effect \\\\\nRand.\\ subsample & ${\\sim}$0.730 (same $n$) & Confirms above \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Length confound analysis. Text length is not a confound: depth-length correlation is weak, and length normalization strengthens feature drift.}\n\\label{tab:length}\n\\end{table}\n\nText length is not a confound for depth classification (Table~\\ref{tab:length}). Depth-length Spearman correlations are weak ($|\\rho| < 0.14$). After length normalization, TTR and hapax depth drift are preserved and strengthened. The 4.6pp F1 drop under length-matched subsampling is attributable to reduced sample size (random subsample control at the same $n$ yields ${\\sim}$0.730), not confound removal.\n\n\\subsection{LD-Score as Additional Feature}\n\\label{sec:ldscore}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Feature Set} & \\textbf{LOGO Bin.~F1} & \\textbf{$\\Delta$} \\\\\n\\midrule\n7 features & 0.694 & --- \\\\\n7 features + LD-Score & 0.700 & $+0.6$ \\\\\nLD-Score alone & 0.721 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{LD-Score as additional feature. Marginal gain (+0.6pp) reflects high redundancy with hapax ratio ($r = 0.75$). LD-Score alone achieves 0.721 LOGO F1 but with wide cross-generator variance [0.588, 0.770].}\n\\label{tab:ldscore}\n\\end{table}\n\nAdding LD-Score (a character-level distribution signature) as an 8th feature provides only +0.6pp marginal gain (Table~\\ref{tab:ldscore}), reflecting high redundancy with hapax ratio ($r = 0.75$). LD-Score's strong ordinal signal ($\\rho = -0.79$) confirms that depth-induced distributional drift manifests at the character level, but its information is largely captured by existing surface features. We retain the 7-feature design for parsimony.\n\n%------------------------------------------------------------\n\\section{Conclusion}\n\\label{sec:conclusion}\n%------------------------------------------------------------\n\nWe formulated generation depth classification as a task beyond binary AI-text detection and characterized differential depth response (DDR) across 5 base-model generators from 3 families. A lightweight 7-feature ensemble achieves leak-free binary F1 = 0.694 under LOGO evaluation, ranging 0.656--0.724 per generator, and 0.830 on cross-model chains. DDR is robust across tested decoding strategies (greedy, top-k) and three reference models from different families.\n\nOur most robust finding is negative: depth-aware data curation is statistically equivalent to random subsampling for downstream CLM quality. Depth fingerprinting is diagnostic---useful for provenance characterization---not curative for data selection.\n\nThe signal degrades substantially under instruction tuning (OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base), restricting current scope to base models. This degradation is itself a finding: instruction tuning compresses the distributional variation DDR exploits. Future work should investigate whether alternative feature families can recover depth signal in instruct models, extend evaluation to larger frontier models ($>$14B), and incorporate additional decoding strategies (nucleus sampling, beam search) to strengthen robustness claims.\n\n%------------------------------------------------------------\n\\section*{Limitations}\n%------------------------------------------------------------\n\nOur study has several limitations. First, all experiments use base models; instruction-tuned models show severely degraded signal, and extending depth fingerprinting to the instruct regime remains open. Second, our decoding robustness analysis covers greedy and top-k sampling; claims should be considered preliminary until validated on nucleus sampling and beam search. Third, the downstream utility experiment uses only perplexity on a single CLM task with 3 seeds---additional tasks and metrics are needed to confirm the ``diagnostic not curative'' conclusion broadly.\n\n\\bibliography{custom}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "72414c20-c97c-4f74-911b-877878eb4910",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T213023 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-finger…",
  "leafUuid": "0dfd8f15-3cff-4cbd-a59d-7b29bdcb9542",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulated research paper",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba"
}
```

---

### Tool call

_source line 22 · 2026-05-21T22:11:18.138Z_

<details open><summary>🔧 Tool call — Bash · `toolu_016dPUdYre4euCmtLFZhEmwH`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "First pdflatex pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0dfd8f15-3cff-4cbd-a59d-7b29bdcb9542",
  "isSidechain": false,
  "requestId": "req_011CbGUpG38LqXccc6Fgcbj1",
  "type": "assistant",
  "uuid": "372d3d4c-1e50-4e9b-b733-bf3d3c5df7b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VAsXsMSjPsVUmq9eBxgJ2x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11007,
      "cache_read_input_tokens": 51576,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11007,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 143,
          "cache_read_input_tokens": 51576,
          "cache_creation_input_tokens": 11007,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11007
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

_source line 23 · 2026-05-21T22:11:18.272Z_

<details><summary>↩ Tool result · `toolu_016dPUdYre4euCmtLFZhEmwH`</summary>

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
  "parentUuid": "372d3d4c-1e50-4e9b-b733-bf3d3c5df7b5",
  "isSidechain": false,
  "promptId": "a05c3ff7-21d6-48e6-b124-f66048f4fb96",
  "type": "user",
  "uuid": "dc49b207-8a85-412d-9084-62473e43e8d6",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `emnlp2023.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "372d3d4c-1e50-4e9b-b733-bf3d3c5df7b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-21T22:11:21.677Z_

<details><summary>Logged reasoning block</summary>

```text
The EMNLP style file is not available. Let me check if there's one in the project or use a simpler approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc49b207-8a85-412d-9084-62473e43e8d6",
  "isSidechain": false,
  "requestId": "req_011CbGUpX7yugxypNTD86p3K",
  "type": "assistant",
  "uuid": "f6176499-2f1c-41be-af99-69b3477d7f6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQ7ZPRoNxcCP3Bje5ciP2Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 428,
      "cache_read_input_tokens": 62583,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 428,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 247,
          "cache_read_input_tokens": 62583,
          "cache_creation_input_tokens": 428,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 428
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

_source line 25 · 2026-05-21T22:11:22.216Z_

Need to find the EMNLP style file or use a fallback.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6176499-2f1c-41be-af99-69b3477d7f6c",
  "isSidechain": false,
  "requestId": "req_011CbGUpX7yugxypNTD86p3K",
  "type": "assistant",
  "uuid": "f48aa0d7-bce5-4235-b13c-2619f81c9f5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQ7ZPRoNxcCP3Bje5ciP2Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 428,
      "cache_read_input_tokens": 62583,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 428,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 247,
          "cache_read_input_tokens": 62583,
          "cache_creation_input_tokens": 428,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 428
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

_source line 26 · 2026-05-21T22:11:22.735Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01UvkaBSBSWf6S1ucMK6FqZm`</summary>

```json
{
  "pattern": "**/*.sty",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f48aa0d7-bce5-4235-b13c-2619f81c9f5d",
  "isSidechain": false,
  "requestId": "req_011CbGUpX7yugxypNTD86p3K",
  "type": "assistant",
  "uuid": "0629f260-78a1-4b5a-9e1d-b551e8189e7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQ7ZPRoNxcCP3Bje5ciP2Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 428,
      "cache_read_input_tokens": 62583,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 428,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 247,
          "cache_read_input_tokens": 62583,
          "cache_creation_input_tokens": 428,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 428
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

_source line 27 · 2026-05-21T22:11:23.394Z_

<details><summary>↩ Tool result · `toolu_01R3FSkSBbeUeVUVJJQTKhnh`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/emnlp_submission_checklist.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/report/emnlp_submission_checklist.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "acbf9170-af0f-4784-8bc6-8f9337148730",
  "isSidechain": false,
  "promptId": "a05c3ff7-21d6-48e6-b124-f66048f4fb96",
  "type": "user",
  "uuid": "e8633ae4-902d-4db1-b87b-db7c704b7a73",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/emnlp_submission_checklist.md",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/report/emnlp_submission_checklist.md"
    ],
    "durationMs": 17,
    "numFiles": 2,
    "truncated": false
  },
  "sourceToolAssistantUUID": "acbf9170-af0f-4784-8bc6-8f9337148730",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T22:11:22.757Z_

<details><summary>↩ Tool result · `toolu_01UvkaBSBSWf6S1ucMK6FqZm`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/acl.sty
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/acl.sty
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/worst/acl.sty
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/best/acl.sty
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0629f260-78a1-4b5a-9e1d-b551e8189e7f",
  "isSidechain": false,
  "promptId": "a05c3ff7-21d6-48e6-b124-f66048f4fb96",
  "type": "user",
  "uuid": "a9352629-a916-4c69-aea8-8057133b2997",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/acl.sty",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/acl.sty",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/worst/acl.sty",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/best/acl.sty"
    ],
    "durationMs": 18,
    "numFiles": 4,
    "truncated": false
  },
  "sourceToolAssistantUUID": "0629f260-78a1-4b5a-9e1d-b551e8189e7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T22:11:23.371Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01R3FSkSBbeUeVUVJJQTKhnh`</summary>

```json
{
  "pattern": "**/emnlp*.*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9352629-a916-4c69-aea8-8057133b2997",
  "isSidechain": false,
  "requestId": "req_011CbGUpX7yugxypNTD86p3K",
  "type": "assistant",
  "uuid": "acbf9170-af0f-4784-8bc6-8f9337148730",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQ7ZPRoNxcCP3Bje5ciP2Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 428,
      "cache_read_input_tokens": 62583,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 428,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 247,
          "cache_read_input_tokens": 62583,
          "cache_creation_input_tokens": 428,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 428
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

_source line 30 · 2026-05-21T22:11:23.418Z_

```json
{
  "parentUuid": "e8633ae4-902d-4db1-b87b-db7c704b7a73",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "f9ade1d0-ae85-4f88-8541-4b2c1d959853",
  "timestamp": "2026-05-21T22:11:23.418Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Tool call

_source line 31 · 2026-05-21T22:11:26.928Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01LLXCKifScdFXfVK9yhsJJE`</summary>

```json
{
  "command": "cp /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/best/acl.sty /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median/acl.sty",
  "description": "Copy ACL style file to median directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9ade1d0-ae85-4f88-8541-4b2c1d959853",
  "isSidechain": false,
  "requestId": "req_011CbGUpu7pDvZ3SgqHKkLk3",
  "type": "assistant",
  "uuid": "2086cdf6-b913-4e2a-b010-a9feaf0a2b16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EPjusqBGhLT22xhf9TPKdZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 681,
      "cache_read_input_tokens": 63011,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 681,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 63011,
          "cache_creation_input_tokens": 681,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 681
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

_source line 32 · 2026-05-21T22:11:26.964Z_

<details><summary>↩ Tool result · `toolu_01LLXCKifScdFXfVK9yhsJJE`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2086cdf6-b913-4e2a-b010-a9feaf0a2b16",
  "isSidechain": false,
  "promptId": "a05c3ff7-21d6-48e6-b124-f66048f4fb96",
  "type": "user",
  "uuid": "c82c0795-5fa9-427e-8ae3-5cadef93c8bc",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  },
  "sourceToolAssistantUUID": "2086cdf6-b913-4e2a-b010-a9feaf0a2b16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-21T22:11:29.745Z_

Now update the paper to use `acl` style instead of `emnlp2023`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c82c0795-5fa9-427e-8ae3-5cadef93c8bc",
  "isSidechain": false,
  "requestId": "req_011CbGUqAFtjgAeqV8LC3Mrg",
  "type": "assistant",
  "uuid": "5e199695-a4ef-48db-b633-073002f37a3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MAmMDYu57RPZDWq7pYoHxc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 196,
      "cache_read_input_tokens": 63692,
      "output_tokens": 211,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 196,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 211,
          "cache_read_input_tokens": 63692,
          "cache_creation_input_tokens": 196,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 196
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

_source line 34 · 2026-05-21T22:11:30.989Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01PZAXyZ1E3orK7PxgULdjcN`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median/paper.tex",
  "old_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{emnlp2023}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e199695-a4ef-48db-b633-073002f37a3d",
  "isSidechain": false,
  "requestId": "req_011CbGUqAFtjgAeqV8LC3Mrg",
  "type": "assistant",
  "uuid": "f3d6296b-0521-4af1-9079-124d59a128ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MAmMDYu57RPZDWq7pYoHxc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 196,
      "cache_read_input_tokens": 63692,
      "output_tokens": 211,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 196,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 211,
          "cache_read_input_tokens": 63692,
          "cache_creation_input_tokens": 196,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 196
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

_source line 35 · 2026-05-21T22:11:31.001Z_

<details><summary>↩ Tool result · `toolu_01PZAXyZ1E3orK7PxgULdjcN`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3d6296b-0521-4af1-9079-124d59a128ec",
  "isSidechain": false,
  "promptId": "a05c3ff7-21d6-48e6-b124-f66048f4fb96",
  "type": "user",
  "uuid": "d34447f7-7cc7-4101-b735-494071cadf22",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median/paper.tex",
    "oldString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{emnlp2023}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 5,
        "newStart": 1,
        "newLines": 5,
        "lines": [
          " \\documentclass[11pt,a4paper]{article}",
          "-\\usepackage[hyperref]{emnlp2023}",
          "+\\usepackage[hyperref]{acl}",
          " \\usepackage{times}",
          " \\usepackage{latexsym}",
          " \\usepackage{booktabs}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "f3d6296b-0521-4af1-9079-124d59a128ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-21T22:11:34.224Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01KaUPFiVVRhZYaqgJ4LR1Pz`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "First pdflatex pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d34447f7-7cc7-4101-b735-494071cadf22",
  "isSidechain": false,
  "requestId": "req_011CbGUqTqp9HoMyc6qVx16x",
  "type": "assistant",
  "uuid": "9e2aacb7-8a7b-4ef9-85a6-6aa7524de806",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XQppKRs2MLAsfB2Aqvghrm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 297,
      "cache_read_input_tokens": 63888,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 297,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 143,
          "cache_read_input_tokens": 63888,
          "cache_creation_input_tokens": 297,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 297
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

_source line 37 · 2026-05-21T22:11:34.823Z_

<details><summary>↩ Tool result · `toolu_01KaUPFiVVRhZYaqgJ4LR1Pz`</summary>

```text
[7] (./paper.aux)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ
ic/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
mr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>
&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/
texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fon
ts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/ti
mes/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb
>
Output written on paper.pdf (7 pages, 186935 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e2aacb7-8a7b-4ef9-85a6-6aa7524de806",
  "isSidechain": false,
  "promptId": "a05c3ff7-21d6-48e6-b124-f66048f4fb96",
  "type": "user",
  "uuid": "f0143a7b-b5e5-4aec-84c7-ebda446ef420",
  "toolUseResult": {
    "stdout": "[7] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\nic/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/\nshare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/\ntexmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fon\nts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/ti\nmes/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb\n>\nOutput written on paper.pdf (7 pages, 186935 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "9e2aacb7-8a7b-4ef9-85a6-6aa7524de806",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-21T22:11:38.331Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01KnrGHdnGfk35HYKU94RJZ8`</summary>

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
  "parentUuid": "f0143a7b-b5e5-4aec-84c7-ebda446ef420",
  "isSidechain": false,
  "requestId": "req_011CbGUqjvCcmN1m2RLHGV5a",
  "type": "assistant",
  "uuid": "0731a161-4be4-4b71-bc12-d834c5c74b9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0139dXswsxJRobeHC2kj6MFR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 781,
      "cache_read_input_tokens": 64185,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 781,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 147,
          "cache_read_input_tokens": 64185,
          "cache_creation_input_tokens": 781,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 781
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

_source line 39 · 2026-05-21T22:11:38.950Z_

<details><summary>↩ Tool result · `toolu_01KnrGHdnGfk35HYKU94RJZ8`</summary>

```text
&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/
texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fon
ts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/ti
mes/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb
>
Output written on paper.pdf (7 pages, 189330 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0731a161-4be4-4b71-bc12-d834c5c74b9e",
  "isSidechain": false,
  "promptId": "a05c3ff7-21d6-48e6-b124-f66048f4fb96",
  "type": "user",
  "uuid": "75bf161b-2c51-48e3-93b2-484e70182a09",
  "toolUseResult": {
    "stdout": "&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/\nshare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/\ntexmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fon\nts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/ti\nmes/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb\n>\nOutput written on paper.pdf (7 pages, 189330 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "0731a161-4be4-4b71-bc12-d834c5c74b9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-21T22:11:53.732Z_

PDF compiled successfully — 7 pages, all cross-references resolved.

The paper covers all 12 experiments from `experiment_data.json`:

1. **Feature ablation & DDR analysis** (Tables 1-2): Full/Surface/Reference ablation + DDR three-tier classification
2. **Cross-generator evaluation** (Tables 3-4): 5-gen LOGO + LOFO cross-family transfer
3. **Cross-reference model validation** (Table 5): 3 reference models confirming DDR is not Pythia-specific
4. **Baseline comparison** (Table 6): 7-feature vs Avg-LogProb/LD-Score/FastDetectGPT/Binoculars
5. **Downstream utility** (Table 7): Negative finding with TOST equivalence
6. **Prompt-type comparison** (Table 8): Continuation/rewriting/elaboration
7. **Paraphrastic comparison** (Table 9): Continuation vs paraphrastic chains + attractor convergence
8. **Cross-model chains** (Table 10): Multi-generator chain amplification
9. **Multi-domain analysis** (Table 11): Wikipedia/code/news/academic
10. **Finer-grained ordinal** (Table 12): 5-class resolution ceiling
11. **Scale effect** (Table 13): Qwen3-8B moderate degradation
12. **Human edit robustness** (Table 14), **End-to-end classifier** (Table 15), **Length confound** (Table 16), **LD-Score** (Table 17)

All numbers come directly from the JSON. Three core claims are supported: Claim 1 (depth discriminability, LOGO binary F1=0.694), Claim 2 (DDR with drifting/stationary split), Claim 3 (negative downstream finding, TOST confirmed). Framing follows the narrative guidance — "robust across tested decoding strategies" hedging, base-model-only scope acknowledged, 0.694 positioned as first baseline not practical tool.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75bf161b-2c51-48e3-93b2-484e70182a09",
  "isSidechain": false,
  "requestId": "req_011CbGUr3ca96hG3G5jn4DpT",
  "type": "assistant",
  "uuid": "59f9852f-0a47-468b-803d-a0d4da37cae0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260521T213023/median",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KPqsx2g9AWuVy7vFRRtaDN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 424,
      "cache_read_input_tokens": 64966,
      "output_tokens": 488,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 424,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 488,
          "cache_read_input_tokens": 64966,
          "cache_creation_input_tokens": 424,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 424
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

_source line 41_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T213023 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-finger…",
  "leafUuid": "59f9852f-0a47-468b-803d-a0d4da37cae0",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulated research paper",
  "sessionId": "5c93f0c9-f7c6-404f-b838-8e17599d97ba"
}
```

---
