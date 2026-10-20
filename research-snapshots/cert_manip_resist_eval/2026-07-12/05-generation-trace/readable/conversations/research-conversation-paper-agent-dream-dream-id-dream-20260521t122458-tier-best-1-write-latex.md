# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122458 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-2/63663d37-a323-4180-9c6d-c85faa2f45aa.jsonl`
- **Structured JSON:** [`9ddbefd129e5493640ef.json`](../../sessions/9d/9ddbefd129e5493640ef.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T13:27:09.945Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T13:27:09.945Z",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122458 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Method contribution paper — 因果链完整：Pareto discovery（architecture-dependent depth-transferability tradeoff with overall positive depth-transfer trend）→ Decomposition explains it（difficulty transfers, capability does not）→ CaCLR solves it（consistency loss shifts Pareto frontier, +3.3pp mean, 14/20 languages improved）→ CKA geometric explanation reveals why（Simpson's Paradox confirmed across 3 architectures, partial rho +0.44 mean, p<0.01）。四条 claim 全力度支撑。Headline: \"CaCLR-trained correctness probes reduce non-English ECE by 38% requiring zero target-language labels.\" Control task warning（10% cross-lingual artifact rate） 和 linear projection sample efficiency（~40 pairs to 95%）作为 elevated empirical contributions 进入 main body。Procrustes effect reversal（threshold ~0.52）为 practitioner 提供直接指导。 三个架构（Qwen3 MoE + Llama4 MoE + Gemma4 Dense）消除架构混淆因子——phenomenon 是 transformer depth 的 universal property。Mean EN AUROC 0.818（range 0.805–0.835），ZS 20-lang mean 0.767， gap 5.2pp。所有 key metrics 落在 best 区间内。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T13:27:09.949Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T13:27:09.949Z",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa"
}
```

---

## Round 1

45 recorded events

### User

_source line 3 · 2026-05-21T13:27:09.966Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122458 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Method contribution paper — 因果链完整：Pareto discovery（architecture-dependent depth-transferability tradeoff with overall positive depth-transfer trend）→ Decomposition explains it（difficulty transfers, capability does not）→ CaCLR solves it（consistency loss shifts Pareto frontier, +3.3pp mean, 14/20 languages improved）→ CKA geometric explanation reveals why（Simpson's Paradox confirmed across 3 architectures, partial rho +0.44 mean, p<0.01）。四条 claim 全力度支撑。Headline: "CaCLR-trained correctness probes reduce non-English ECE by 38% requiring zero target-language labels." Control task warning（10% cross-lingual artifact rate） 和 linear projection sample efficiency（~40 pairs to 95%）作为 elevated empirical contributions 进入 main body。Procrustes effect reversal（threshold ~0.52）为 practitioner 提供直接指导。 三个架构（Qwen3 MoE + Llama4 MoE + Gemma4 Dense）消除架构混淆因子——phenomenon 是 transformer depth 的 universal property。Mean EN AUROC 0.818（range 0.805–0.835），ZS 20-lang mean 0.767， gap 5.2pp。所有 key metrics 落在 best 区间内。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "abfe29c1-5ae0-4522-8fc6-1901a8a7bf7b",
  "type": "user",
  "uuid": "48330345-df77-499f-9d61-4fdc046928b7",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T13:27:09.966Z_

```json
{
  "parentUuid": "48330345-df77-499f-9d61-4fdc046928b7",
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
  "uuid": "249ba0c7-bea4-48a2-83c1-fe4956bc4ffa",
  "timestamp": "2026-05-21T13:27:09.966Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T13:27:09.966Z_

```json
{
  "parentUuid": "249ba0c7-bea4-48a2-83c1-fe4956bc4ffa",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "1f5b18db-3a44-495c-a226-df3b9fa3e361",
  "timestamp": "2026-05-21T13:27:09.966Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa",
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
  "aiTitle": "Generate calibration paper with CaCLR method",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa"
}
```

---

### Assistant

_source line 7 · 2026-05-21T13:27:12.820Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f5b18db-3a44-495c-a226-df3b9fa3e361",
  "isSidechain": false,
  "requestId": "req_011CbFnrLDo9sqZojCHPi2CZ",
  "type": "assistant",
  "uuid": "d0fd64ee-3902-4902-bd60-d932e9a7c018",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WV25Gccu51zqxQFZNMJ9DQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11655,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11655,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11655,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11655
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

_source line 8 · 2026-05-21T13:27:13.814Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Y3DQSKRQQHSGUyr7ms1adc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0fd64ee-3902-4902-bd60-d932e9a7c018",
  "isSidechain": false,
  "requestId": "req_011CbFnrLDo9sqZojCHPi2CZ",
  "type": "assistant",
  "uuid": "95ec5bda-2a74-47fe-8744-c8ce88939808",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WV25Gccu51zqxQFZNMJ9DQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11655,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11655,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11655,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11655
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

_source line 9 · 2026-05-21T13:27:14.177Z_

<details open><summary>🔧 Tool call — Read · `toolu_016dgpL8F8pcKu3Kq1vHT6rE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95ec5bda-2a74-47fe-8744-c8ce88939808",
  "isSidechain": false,
  "requestId": "req_011CbFnrLDo9sqZojCHPi2CZ",
  "type": "assistant",
  "uuid": "ac739ca1-6ab5-456b-8e47-4cba0f9458cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WV25Gccu51zqxQFZNMJ9DQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11655,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11655,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11655,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11655
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

_source line 10 · 2026-05-21T13:27:14.191Z_

<details><summary>↩ Tool result · `toolu_01Y3DQSKRQQHSGUyr7ms1adc`</summary>

```text
1	[
2	  {
3	    "name": "Full Pareto Frontier — Qwen3-235B-A22B (MoE)",
4	    "description": "94-layer MoE (INT4, ~22B active), 24 probed layers (every 4th: L0,L4,...,L92), 20 typologically diverse languages, English logistic regression probes, 5 transfer conditions: zero-shot, mean-shift, linear projection (200 pairs), few-shot 25/100, CaCLR (optimal α=0.1, β=0.05 from plan_003)。验证 MVP 发现的 positive depth-transfer trend 和 local deep-layer Pareto tradeoff 在大 MoE 模型上放大。\n",
5	    "results": {
6	      "en_best_auroc": 0.835,
7	      "en_best_layer_idx": 68,
8	      "en_best_depth_pct": 72,
9	      "en_auroc_range": [
10	        0.59,
11	        0.835
12	      ],
13	      "en_ece_raw_best": 0.172,
14	      "zs_mean_auroc_20lang_at_zs_optimal": 0.775,
15	      "zs_best_transfer_layer_idx": 48,
16	      "zs_best_transfer_depth_pct": 51,
17	      "zs_pass_rate_auroc_gt_058": 19,
18	      "zs_fail_langs": [
19	        "yo"
20	      ],
21	      "zs_auroc_by_tier": {
22	        "HIGH_mean": 0.817,
23	        "MID_mean": 0.788,
24	        "LOW_mean": 0.693
25	      },
26	      "zs_auroc_selected": {
27	        "zh": 0.83,
28	        "es": 0.82,
29	        "fr": 0.82,
30	        "de": 0.82,
31	        "ja": 0.81,
32	        "nl": 0.81,
33	        "pt": 0.81,
34	        "ar": 0.8,
35	        "hi": 0.79,
36	        "ko": 0.79,
37	        "ru": 0.8,
38	        "tr": 0.78,
39	        "vi": 0.77,
40	        "id": 0.79,
41	        "pl": 0.79,
42	        "uk": 0.78,
43	        "sw": 0.72,
44	        "bn": 0.73,
45	        "te": 0.67,
46	        "yo": 0.575
47	      },
48	      "overall_spearman_depth_vs_zs": {
49	        "global_rho": 0.68,
50	        "global_p": 0.0003
51	      },
52	      "per_lang_spearman_rho_median": 0.62,
53	      "per_lang_positive_rho_count": 17,
54	      "per_lang_significant_positive_count": 14,
55	      "per_lang_negative_rho_langs": [
56	        "yo",
57	        "te",
58	        "sw"
59	      ],
60	      "pareto_tradeoff_langs_count": 15,
61	      "pareto_en_optimal_layer": 68,
62	      "pareto_zs_optimal_layer": 48,
63	      "pareto_depth_gap_layers": 20,
64	      "pareto_zs_drop_at_en_optimal_pp": 3.8,
65	      "mean_shift_delta_auroc": 0.0,
66	      "linproj_200pairs_mean_auroc": 0.793,
67	      "linproj_200pairs_delta_pp": 1.8,
68	      "fewshot_25_mean_auroc": 0.762,
69	      "fewshot_100_mean_auroc": 0.788,
70	      "caclr_mean_auroc": 0.812,
71	      "caclr_delta_vs_zs_pp": 3.7
72	    },
73	    "tables": [
74	      {
75	        "name": "Table 1: Qwen3-235B Pareto Frontier (selected layers)",
76	        "columns": [
77	          "layer_idx",
78	          "depth_pct",
79	          "en_auroc",
80	          "zs_mean_20",
81	          "zs_drop_vs_en_pp",
82	          "on_pareto"
83	        ],
84	        "rows": [
85	          [
86	            4,
87	            4,
88	            0.59,
89	            0.582,
90	            0.8,
91	            false
92	          ],
93	          [
94	            12,
95	            13,
96	            0.645,
97	            0.636,
98	            0.9,
99	            false
100	          ],
101	          [
102	            20,
103	            21,
104	            0.71,
105	            0.7,
106	            1.0,
107	            false
108	          ],
109	          [
110	            28,
111	            30,
112	            0.752,
113	            0.74,
114	            1.2,
115	            false
116	          ],
117	          [
118	            36,
119	            38,
120	            0.785,
121	            0.77,
122	            1.5,
123	            false
124	          ],
125	          [
126	            40,
127	            43,
128	            0.798,
129	            0.779,
130	            1.9,
131	            false
132	          ],
133	          [
134	            44,
135	            47,
136	            0.808,
137	            0.782,
138	            2.6,
139	            false
140	          ],
141	          [
142	            48,
143	            51,
144	            0.815,
145	            0.775,
146	            4.0,
147	            true
148	          ],
149	          [
150	            52,
151	            55,
152	            0.822,
153	            0.768,
154	            5.4,
155	            true
156	          ],
157	          [
158	            56,
159	            60,
160	            0.828,
161	            0.757,
162	            7.1,
163	            true
164	          ],
165	          [
166	            60,
167	            64,
168	            0.832,
169	            0.745,
170	            8.7,
171	            true
172	          ],
173	          [
174	            64,
175	            68,
176	            0.834,
177	            0.738,
178	            9.6,
179	            true
180	          ],
181	          [
182	            68,
183	            72,
184	            0.835,
185	            0.737,
186	            9.8,
187	            true
188	          ],
189	          [
190	            72,
191	            77,
192	            0.834,
193	            0.725,
194	            10.9,
195	            false
196	          ],
197	          [
198	            76,
199	            81,
200	            0.83,
201	            0.71,
202	            12.0,
203	            false
204	          ],
205	          [
206	            80,
207	            85,
208	            0.822,
209	            0.695,
210	            12.7,
211	            false
212	          ],
213	          [
214	            84,
215	            89,
216	            0.815,
217	            0.678,
218	            13.7,
219	            false
220	          ],
221	          [
222	            88,
223	            94,
224	            0.805,
225	            0.66,
226	            14.5,
227	            false
228	          ],
229	          [
230	            92,
231	            98,
232	            0.79,
233	            0.642,
234	            14.8,
235	            false
236	          ]
237	        ]
238	      },
239	      {
240	        "name": "Table 2: Per-Language Spearman ρ (depth vs ZS AUROC), Qwen3",
241	        "columns": [
242	          "language",
243	          "tier",
244	          "spearman_rho",
245	          "p_value",
246	          "significant_at_005"
247	        ],
248	        "rows": [
249	          [
250	            "zh",
251	            "HIGH",
252	            0.75,
253	            0.0001,
254	            true
255	          ],
256	          [
257	            "es",
258	            "HIGH",
259	            0.72,
260	            0.0002,
261	            true
262	          ],
263	          [
264	            "fr",
265	            "HIGH",
266	            0.7,
267	            0.0003,
268	            true
269	          ],
270	          [
271	            "de",
272	            "HIGH",
273	            0.73,
274	            0.0002,
275	            true
276	          ],
277	          [
278	            "ja",
279	            "HIGH",
280	            0.68,
281	            0.0005,
282	            true
283	          ],
284	          [
285	            "nl",
286	            "HIGH",
287	            0.71,
288	            0.0003,
289	            true
290	          ],
291	          [
292	            "pt",
293	            "HIGH",
294	            0.69,
295	            0.0004,
296	            true
297	          ],
298	          [
299	            "ar",
300	            "MID",
301	            0.67,
302	            0.0006,
303	            true
304	          ],
305	          [
306	            "hi",
307	            "MID",
308	            0.62,
309	            0.002,
310	            true
311	          ],
312	          [
313	            "ko",
314	            "MID",
315	            0.65,
316	            0.001,
317	            true
318	          ],
319	          [
320	            "ru",
321	            "MID",
322	            0.68,
323	            0.0005,
324	            true
325	          ],
326	          [
327	            "tr",
328	            "MID",
329	            0.6,
330	            0.003,
331	            true
332	          ],
333	          [
334	            "vi",
335	            "MID",
336	            0.55,
337	            0.007,
338	            true
339	          ],
340	          [
341	            "id",
342	            "MID",
343	            0.63,
344	            0.002,
345	            true
346	          ],
347	          [
348	            "pl",
349	            "MID",
350	            0.62,
351	            0.002,
352	            true
353	          ],
354	          [
355	            "uk",
356	            "MID",
357	            0.58,
358	            0.005,
359	            true
360	          ],
361	          [
362	            "sw",
363	            "LOW",
364	            -0.12,
365	            0.58,
366	            false
367	          ],
368	          [
369	            "bn",
370	            "LOW",
371	            0.35,
372	            0.1,
373	            false
374	          ],
375	          [
376	            "te",
377	            "LOW",
378	            -0.08,
379	            0.72,
380	            false
381	          ],
382	          [
383	            "yo",
384	            "LOW",
385	            -0.18,
386	            0.42,
387	            false
388	          ]
389	        ]
390	      },
391	      {
392	        "name": "Table 3: Transfer Conditions at ZS-Optimal Layer (L48), Qwen3",
393	        "columns": [
394	          "condition",
395	          "mean_auroc_20",
396	          "delta_vs_zs_pp",
397	          "requires"
398	        ],
399	        "rows": [
400	          [
401	            "zero-shot",
402	            0.775,
403	            0.0,
404	            "—"
405	          ],
406	          [
407	            "mean-shift",
408	            0.775,
409	            0.0,
410	            "—"
411	          ],
412	          [
413	            "linear_proj_200",
414	            0.793,
415	            1.8,
416	            "200 parallel pairs"
417	          ],
418	          [
419	            "few-shot-25",
420	            0.762,
421	            -1.3,
422	            "25 labeled per lang"
423	          ],
424	          [
425	            "few-shot-100",
426	            0.788,
427	            1.3,
428	            "100 labeled per lang"
429	          ],
430	          [
431	            "CaCLR",
432	            0.812,
433	            3.7,
434	            "parallel activations"
435	          ]
436	        ]
437	      }
438	    ],
439	    "figures": [],
440	    "analysis": "Qwen3-235B 展现 strong, consistent positive depth-transfer trend（global ρ=+0.68, p=0.0003）和 pronounced local Pareto tradeoff（15/20 langs）。EN-optimal (L68) 与 ZS-optimal (L48) 相距 20 层，远大于 MVP 的 3 层，确认 tradeoff 在大模型上放大。 14/20 languages 的 per-language ρ 显著为正，表明 \"deeper is generally better for transfer\" 是跨语言一致的。3 个 LOW-resource languages (yo/te/sw) 显示 negative/near-zero ρ， 因为这些语言的 correctness signal quality 在深层退化快于 probe discrimination 的提升。 CaCLR 在 ZS-optimal layer 提供 +3.7pp，是所有 label-free methods 中最优。\n\n\nQwen3-235B 的 22B active params 比 MVP Qwen2.5-7B 多 ~3×。Probing scaling 预期 EN AUROC 从 0.754 提升至 0.835：更大模型在 intermediate layers 编码更清晰的 correctness signal， 因为 pretraining loss 更低 → 内部 representations 对 factual accuracy 更 informative。\nOverall positive depth-transfer trend（median per-lang Spearman ρ=+0.62）因为更深层 encode 更多 semantic content → 更好的 correctness discrimination，且 correctness direction 的 cross-lingual alignment 在 shallow-to-mid layers 持续改善（CKA 在 0-50% depth 下降缓慢）。 17/20 languages 有 positive ρ，3 个 negative 的（yo/te/sw）是 LOW-resource：这些语言在 Qwen3 pretraining corpus 中占比极低（<0.1%），ZS AUROC 的 depth profile 呈倒 U 形 （peak 在 ~40% depth 而非 >50%），因为深层的 language-specific specialization 对这些语言 反而有害。\nLocal Pareto tradeoff：从 ZS-optimal (L48, 51% depth) 到 EN-optimal (L68, 72% depth)， EN 增加 2pp（0.815→0.835）但 ZS 平均下降 3.8pp（0.775→0.737）。这一 tradeoff 在 15/20 languages 上可观测（ZS-optimal ≠ EN-optimal，gap >1.5pp）。94 层深网络比 28 层 MVP 有 更大的 specialization 空间，使 EN-optimal 与 ZS-optimal 之间的 depth gap 从 MVP 的 3 层 扩大至 20 层（22pp depth）。\nMoE routing 在深层产生 language-specific expert activation patterns，加速 CKA cliff 下降，导致 Qwen3 的 Pareto tradeoff 比 Llama4/Gemma4 更 pronounced（15/20 vs 10-12/20）。\nMean-shift ΔAUROC ≡ 0：StandardScaler + LR 下 mean-shift 对 AUROC 无影响（rank-invariant, MVP 中已数学证明并实验验证）。\nLinear projection (+1.8pp) 通过 Procrustes 捕获 correctness subspace 旋转。 CaCLR (+3.7pp) 通过 end-to-end 优化超越 linear projection。 Few-shot-100 (+1.3pp) 在 full-scale 上弱于 ZS 因为 100 个 labeled samples 对 14K train set 的 probe 参数贡献边际很小。\n"
441	  },
442	  {
443	    "name": "Full Pareto Frontier — Llama 4 Scout (MoE)",
444	    "description": "48-layer MoE (W4A16, 17B×16E, top-2 routing), 12 probed layers (every 4th: L0,L4,...,L44,L47), 20 languages, 5 transfer conditions。验证 MVP Llama-3.1-8B 的 weaker/mixed tradeoff pattern 是否是 Llama 架构家族特征。\n",
445	    "results": {
446	      "en_best_auroc": 0.815,
447	      "en_best_layer_idx": 36,
448	      "en_best_depth_pct": 75,
449	      "en_auroc_range": [
450	        0.57,
451	        0.815
452	      ],
453	      "en_ece_raw_best": 0.178,
454	      "zs_mean_auroc_20lang_at_zs_optimal": 0.765,
455	      "zs_best_transfer_layer_idx": 28,
456	      "zs_best_transfer_depth_pct": 58,
457	      "zs_pass_rate_auroc_gt_058": 17,
458	      "zs_fail_langs": [
459	        "yo",
460	        "te",
461	        "sw"
462	      ],
463	      "zs_auroc_by_tier": {
464	        "HIGH_mean": 0.808,
465	        "MID_mean": 0.778,
466	        "LOW_mean": 0.672
467	      },
468	      "per_lang_spearman_rho_median": 0.72,
469	      "per_lang_positive_rho_count": 19,
470	      "per_lang_significant_positive_count": 16,
471	      "per_lang_negative_rho_langs": [
472	        "yo"
473	      ],
474	      "pareto_tradeoff_langs_count": 10,
475	      "pareto_zs_drop_at_en_optimal_pp": 2.5,
476	      "mean_shift_delta_auroc": 0.0,
477	      "linproj_200pairs_mean_auroc": 0.781,
478	      "fewshot_100_mean_auroc": 0.778,
479	      "caclr_mean_auroc": 0.798,
480	      "caclr_delta_vs_zs_pp": 3.3
481	    },
482	    "tables": [
483	      {
484	        "name": "Table 4: Llama 4 Scout Pareto Frontier",
485	        "columns": [
486	          "layer_idx",
487	          "depth_pct",
488	          "en_auroc",
489	          "zs_mean_20",
490	          "on_pareto"
491	        ],
492	        "rows": [
493	          [
494	            4,
495	            8,
496	            0.57,
497	            0.562,
498	            false
499	          ],
500	          [
501	            8,
502	            17,
503	            0.64,
504	            0.63,
505	            false
506	          ],
507	          [
508	            12,
509	            25,
510	            0.7,
511	            0.69,
512	            false
513	          ],
514	          [
515	            16,
516	            33,
517	            0.74,
518	            0.728,
519	            false
520	          ],
521	          [
522	            20,
523	            42,
524	            0.768,
525	            0.755,
526	            false
527	          ],
528	          [
529	            24,
530	            50,
531	            0.785,
532	            0.764,
533	            false
534	          ],
535	          [
536	            28,
537	            58,
538	            0.798,
539	            0.765,
540	            true
541	          ],
542	          [
543	            32,
544	            67,
545	            0.808,
546	            0.755,
547	            true
548	          ],
549	          [
550	            36,
551	            75,
552	            0.815,
553	            0.742,
554	            true
555	          ],
556	          [
557	            40,
558	            83,
559	            0.81,
560	            0.722,
561	            false
562	          ],
563	          [
564	            44,
565	            92,
566	            0.795,
567	            0.695,
568	            false
569	          ],
570	          [
571	            47,
572	            98,
573	            0.778,
574	            0.668,
575	            false
576	          ]
577	        ]
578	      },
579	      {
580	        "name": "Table 5: Architecture-Dependent Pareto Summary",
581	        "columns": [
582	          "metric",
583	          "Qwen3_235B",
584	          "Llama4_Scout",
585	          "interpretation"
586	        ],
587	        "rows": [
588	          [
589	            "en_best_auroc",
590	            0.835,
591	            0.815,
592	            "both strong, Qwen slightly higher (22B>17B active)"
593	          ],
594	          [
595	            "zs_mean_at_zs_opt",
596	            0.775,
597	            0.765,
598	            "comparable transfer quality"
599	          ],
600	          [
601	            "per_lang_rho_median",
602	            "+0.62",
603	            "+0.72",
604	            "both positive; Llama higher (fewer deep layers)"
605	          ],
606	          [
607	            "positive_rho_langs",
608	            "17/20",
609	            "19/20",
610	            "Llama more consistent"
611	          ],
612	          [
613	            "pareto_tradeoff_langs",
614	            "15/20",
615	            "10/20",
616	            "Qwen stronger tradeoff"
617	          ],
618	          [
619	            "pareto_zs_drop_pp",
620	            3.8,
621	            2.5,
622	            "Qwen steeper"
623	          ],
624	          [
625	            "best_transfer_depth_pct",
626	            51,
627	            58,
628	            "comparable mid-depth zone"
629	          ]
630	        ]
631	      }
632	    ],
633	    "figures": [],
634	    "analysis": "Llama4 与 Qwen3 的对比确认 architecture-dependent tradeoff strength。两者都有 positive depth-transfer trend 和 local Pareto tradeoff，但 effect sizes 不同： Qwen3 在 15/20 languages 上有 measurable tradeoff（mean drop 3.8pp），Llama4 仅 10/20（mean drop 2.5pp）。差异无法从 domain adaptation theory 预测—— 这是 architecture/training-recipe 的 empirical finding。Best-transfer depth converges to 51-58%，暗示 universal \"mid-depth transfer zone\"。\n\n\nLlama 4 Scout 延续 MVP Llama-3.1-8B 的 weaker tradeoff 模式但在关键方面加强。 Per-language Spearman median ρ=+0.72 高于 Qwen3 (0.62)，因为 Llama4 仅 48 层—— 更少的深层 specialization 空间意味着 ZS AUROC 的下降区间更短（最后 ~20% 层）， 而上升区间（前 58% 层）主导了 overall correlation。19/20 languages 有 positive ρ （仅 yo negative）。\nPareto tradeoff 仅 10/20 languages（vs Qwen3 15/20），且 ZS drop 仅 2.5pp （vs Qwen3 3.8pp）。这与 MVP 一致（Llama-3.1-8B: 2/5 langs showed tradeoff, ar/ko 在深层反而改善）。归因于 Meta 的 multilingual training recipe：Llama4 在 pretraining 中对中高资源语言的 cross-lingual alignment 更均匀，深层 language-specific routing 效应弱于 Qwen3。\nEN best AUROC 0.815 低于 Qwen3 的 0.835，部分因为 17B active params < 22B (Qwen3)，部分因为 W4A16 量化引入 ~0.3pp noise（plan_010 验证）。\nArchitecture-dependent tradeoff strength 是 Claim 1 核心： Qwen3 strong (15/20, -3.8pp) vs Llama4 weak (10/20, -2.5pp)， median per-lang ρ 差异虽然在同一方向（都正），但 Qwen3 的 Pareto zone 更宽。\n"
635	  },
636	  {
637	    "name": "Full Pareto Frontier — Gemma 4 31B Dense",
638	    "description": "60 text layers, dense architecture, BF16 (~62.5GB, single 96GB GPU), 16 probed layers (every 4th + final: L0,L4,...,L56,L59), 20 languages, 5 transfer conditions。 P0 priority — provides dense vs MoE architectural contrast, eliminates confound between architecture type and tradeoff strength。无量化 → 消除量化 confound。\n",
639	    "results": {
640	      "en_best_auroc": 0.805,
641	      "en_best_layer_idx": 44,
642	      "en_best_depth_pct": 73,
643	      "en_auroc_range": [
644	        0.57,
645	        0.805
646	      ],
647	      "en_ece_raw_best": 0.185,
648	      "zs_mean_auroc_20lang_at_zs_optimal": 0.76,
649	      "zs_best_transfer_layer_idx": 36,
650	      "zs_best_transfer_depth_pct": 60,
651	      "zs_pass_rate_auroc_gt_058": 18,
652	      "zs_fail_langs": [
653	        "yo",
654	        "te"
655	      ],
656	      "zs_auroc_by_tier": {
657	        "HIGH_mean": 0.802,
658	        "MID_mean": 0.772,
659	        "LOW_mean": 0.67
660	      },
661	      "per_lang_spearman_rho_median": 0.65,
662	      "per_lang_positive_rho_count": 18,
663	      "per_lang_significant_positive_count": 14,
664	      "pareto_tradeoff_langs_count": 12,
665	      "pareto_zs_drop_at_en_optimal_pp": 3.0,
666	      "linproj_200pairs_mean_auroc": 0.776,
667	      "caclr_mean_auroc": 0.79,
668	      "caclr_delta_vs_zs_pp": 3.0,
669	      "simpson_partial_rho": 0.44,
670	      "simpson_partial_p": 0.004
671	    },
672	    "tables": [
673	      {
674	        "name": "Table 6: Three-Architecture Comprehensive Summary",
675	        "columns": [
676	          "model",
677	          "type",
678	          "layers",
679	          "en_best",
680	          "zs_mean_20",
681	          "en_zs_gap_pp",
682	          "pareto_rho_median",
683	          "pareto_langs",
684	          "simpson_partial_rho",
685	          "caclr_delta_pp"
686	        ],
687	        "rows": [
688	          [
689	            "Qwen3-235B",
690	            "MoE",
691	            94,
692	            0.835,
693	            0.775,
694	            6.0,
695	            "+0.62",
696	            "15/20",
697	            "+0.48",
698	            3.7
699	          ],
700	          [
701	            "Llama4 Scout",
702	            "MoE",
703	            48,
704	            0.815,
705	            0.765,
706	            5.0,
707	            "+0.72",
708	            "10/20",
709	            "+0.41",
710	            3.3
711	          ],
712	          [
713	            "Gemma4 31B",
714	            "Dense",
715	            60,
716	            0.805,
717	            0.76,
718	            4.5,
719	            "+0.65",
720	            "12/20",
721	            "+0.44",
722	            3.0
723	          ],
724	          [
725	            "Mean (3 arch)",
726	            "—",
727	            "—",
728	            0.818,
729	            0.767,
730	            5.2,
731	            "+0.66",
732	            "37/60=62%",
733	            "+0.44",
734	            3.3
735	          ]
736	        ]
737	      }
738	    ],
739	    "figures": [],
740	    "analysis": "Three-architecture replication 是 universality claim 最强证据。Simpson's Paradox 在 3/3 architectures 上 confirmed (partial ρ range 0.41-0.48, all p<0.01)。 Dense vs MoE contrast minimal — phenomenon 是 transformer depth 的 property。 Mean EN AUROC 0.818 在 [0.80, 0.86] 内。Mean gap 5.2pp 在 [4, 8] 内。 Pareto prevalence 62% 在 [0.5, 0.75] 内。CaCLR 一致 +3.0-3.7pp。\n\n\nGemma4 31B Dense 是三架构中唯一的 dense model，消除了 \"MoE routing 导致 Pareto tradeoff\" 的替代解释。EN best AUROC 0.805 低于两个 MoE 模型（0.835/0.815）， 因为 31B dense < 22B/17B MoE active（MoE 的 expert routing 提供 effective capacity boost，使相同 active param 下 probe 信号更强）。\nPareto tradeoff 在 12/20 languages 上可观测（介于 Qwen3 15/20 和 Llama4 10/20 之间），ZS drop 3.0pp。Dense architecture 没有 routing-specific specialization， 但深层仍然发生 language-specific feature specialization（attention heads 在 deep layers 对不同语言的 subword patterns 有不同 activation）。这证实 Pareto tradeoff 是 transformer depth 的 universal property，不是 MoE routing 的 artifact。\nSimpson's Paradox 在 dense 架构上同样成立（partial ρ=+0.44, p=0.004）， 确认 geometric insight 是 architecture-universal。BF16 无量化 → 消除量化 distortion confound，使 CKA 和 subspace angle 分析更 reliable。\nPer-lang Spearman median ρ=+0.65（介于 Qwen 0.62 和 Llama 0.72 之间）， 60 层提供的深层 specialization 空间在两者之间。\n"
741	  },
742	  {
743	    "name": "CKA Cross-Lingual Similarity & Simpson's Paradox",
744	    "description": "Linear CKA (EN vs each target) at every probed layer, 20 languages × 3 models。 核心分析：(a) same-layer cross-language correlation (n=20 per layer), (b) partial Spearman controlling for normalized depth — THE single most important analysis, (c) subspace angle quantitative analysis, (d) CKA cliff threshold identification。 验证 pilot Simpson's Paradox 在 full-scale 上 3 架构复现。\n",
745	    "results": {
746	      "qwen3_raw_rho": -0.38,
747	      "qwen3_raw_p": 0.0001,
748	      "llama4_raw_rho": -0.42,
749	      "llama4_raw_p": 0.0001,
750	      "gemma4_raw_rho": -0.4,
751	      "gemma4_raw_p": 0.0001,
752	      "qwen3_partial_rho": 0.48,
753	      "qwen3_partial_p": 0.0018,
754	      "qwen3_partial_bootstrap_ci_95": [
755	        0.3,
756	        0.63
757	      ],
758	      "llama4_partial_rho": 0.41,
759	      "llama4_partial_p": 0.0065,
760	      "llama4_partial_bootstrap_ci_95": [
761	        0.21,
762	        0.58
763	      ],
764	      "gemma4_partial_rho": 0.44,
765	      "gemma4_partial_p": 0.0038,
766	      "gemma4_partial_bootstrap_ci_95": [
767	        0.26,
768	        0.6
769	      ],
770	      "simpson_paradox_confirmed_all_3_arch": true,
771	      "qwen3_per_layer_positive_count_of_24": 19,
772	      "qwen3_per_layer_significant_count_of_24": 8,
773	      "llama4_per_layer_positive_count_of_12": 10,
774	      "llama4_per_layer_significant_count_of_12": 4,
775	      "gemma4_per_layer_positive_count_of_16": 13,
776	      "gemma4_per_layer_significant_count_of_16": 6,
777	      "cka_peak_depth_pct_range": [
778	        15,
779	        25
780	      ],
781	      "cka_peak_value_range": [
782	        0.82,
783	        0.86
784	      ],
785	      "transfer_collapse_cka_threshold": 0.35,
786	      "below_threshold_mean_zs_auroc": 0.6,
787	      "above_threshold_mean_zs_auroc": 0.74,
788	      "correctness_subspace_angle_within_layer_mean_deg": 12.8,
789	      "correctness_subspace_angle_within_layer_std_deg": 5.4,
790	      "correctness_subspace_angle_across_layer_mean_deg": 37.5,
791	      "correctness_subspace_angle_across_layer_std_deg": 10.8,
792	      "random_baseline_angle_deg": 87.1
793	    },
794	    "tables": [
795	      {
796	        "name": "Table 7: Simpson's Paradox — Raw vs Partial Correlation (3 Architectures)",
797	        "columns": [
798	          "model",
799	          "analysis",
800	          "spearman_rho",
801	          "p_value",
802	          "bootstrap_95CI",
803	          "interpretation"
804	        ],
805	        "rows": [
806	          [
807	            "Qwen3-235B",
808	            "raw pooled",
809	            -0.38,
810	            "<0.001",
811	            "[-0.46, -0.29]",
812	            "negative — depth confound"
813	          ],
814	          [
815	            "Qwen3-235B",
816	            "partial (controlling depth)",
817	            0.48,
818	            0.0018,
819	            "[+0.30, +0.63]",
820	            "positive — genuine geometric signal"
821	          ],
822	          [
823	            "Llama4 Scout",
824	            "raw pooled",
825	            -0.42,
826	            "<0.001",
827	            "[-0.51, -0.32]",
828	            "negative — depth confound"
829	          ],
830	          [
831	            "Llama4 Scout",
832	            "partial (controlling depth)",
833	            0.41,
834	            0.0065,
835	            "[+0.21, +0.58]",
836	            "positive — genuine geometric signal"
837	          ],
838	          [
839	            "Gemma4 31B",
840	            "raw pooled",
841	            -0.4,
842	            "<0.001",
843	            "[-0.49, -0.30]",
844	            "negative — depth confound"
845	          ],
846	          [
847	            "Gemma4 31B",
848	            "partial (controlling depth)",
849	            0.44,
850	            0.0038,
851	            "[+0.26, +0.60]",
852	            "positive — genuine geometric signal"
853	          ]
854	        ]
855	      },
856	      {
857	        "name": "Table 8: Subspace Angle Analysis (correctness direction, pooled across archs)",
858	        "columns": [
859	          "comparison_type",
860	          "mean_angle_deg",
861	          "std_deg",
862	          "interpretation"
863	        ],
864	        "rows": [
865	          [
866	            "within-layer cross-language",
867	            12.8,
868	            5.4,
869	            "highly aligned — correctness direction is near-universal"
870	          ],
871	          [
872	            "cross-layer same-language",
873	            37.5,
874	            10.8,
875	            "significant drift — direction rotates with depth"
876	          ],
877	          [
878	            "random baseline (shuffled)",
879	            87.1,
880	            2.0,
881	            "near-orthogonal — confirms non-trivial signal"
882	          ]
883	        ]
884	      },
885	      {
886	        "name": "Table 9: CKA Heatmap Summary (Qwen3, mean across 20 langs by tier)",
887	        "columns": [
888	          "depth_pct",
889	          "HIGH_CKA",
890	          "MID_CKA",
891	          "LOW_CKA",
892	          "overall_CKA"
893	        ],
894	        "rows": [
895	          [
896	            13,
897	            0.87,
898	            0.8,
899	            0.64,
900	            0.79
901	          ],
902	          [
903	            30,
904	            0.85,
905	            0.78,
906	            0.6,
907	            0.77
908	          ],
909	          [
910	            47,
911	            0.7,
912	            0.58,
913	            0.38,
914	            0.58
915	          ],
916	          [
917	            64,
918	            0.5,
919	            0.38,
920	            0.24,
921	            0.39
922	          ],
923	          [
924	            77,
925	            0.4,
926	            0.28,
927	            0.16,
928	            0.3
929	          ],
930	          [
931	            94,
932	            0.27,
933	            0.19,
934	            0.1,
935	            0.2
936	          ]
937	        ]
938	      }
939	    ],
940	    "figures": [],
941	    "analysis": "Simpson's Paradox 在 3/3 architectures 上显著复现（partial ρ: 0.41-0.48, all p<0.01, all bootstrap CIs exclude zero）。这是本文核心几何洞见——不是 trivially expected from measurement overlap：sign reversal 从负到正是 non-trivial 的。Subspace angle analysis 提供 mechanistic grounding。CKA cliff threshold ~0.35 connects Claim 1 (Pareto) with Claim 4 (geometry)。所有 partial correlations 的 bootstrap CIs 在 [0.3, 0.55] key metric range 内。\n\n\nSimpson's Paradox 的 causal mechanism：depth 同时作用于 CKA（deeper → representations diverge → CKA drops）和 ZS AUROC（deeper → EN probe更强 → higher absolute AUROC up to mid-depth），创造了 depth confound。Raw pooled correlation 为负：shallow layers 有 high CKA 但 low AUROC（probe 本身弱），deep layers 有 low CKA 但 moderate/declining AUROC。控制 depth 后，within 每个 layer，higher CKA 的语言确实有 better transfer， partial ρ 为正。\nMVP pilot（Llama, 5 langs × 9 layers）已展现 ρ=+0.41, p=0.006。Full-scale（20 langs × 12-24 layers per arch）增强统计 power：per-layer test 从 n=5 增至 n=20。 MVP Qwen pilot 仅 ρ=+0.18 (p=0.274)，full-scale 上升至 +0.48 因为：(1) n 从 5 增至 20 语言，power 大幅提升；(2) 20 语言覆盖更宽的 CKA 范围（增加了极低 CKA 的 yo/te 和高 CKA 的 nl/pt），扩大了 within-layer variance。\nSubspace angle analysis 提供 structural grounding：correctness direction 在同一 layer 内跨语言仅旋转 ~13°（near-universal），但跨 layer 旋转 ~38°（significant drift）， vs random baseline ~87°。这解释了为何 within-layer CKA 预测 transfer（correctness direction 对齐良好）但 raw pooled 不预测（depth confound 混淆了 correctness 与 non- correctness dimensions 的 divergence）。\nCKA cliff threshold ~0.35 直接解释了 architecture-dependent tradeoff 差异：Qwen3 的 CKA cliff 更陡（deep-layer CKA 下降更快因为 MoE routing），导致更多语言在 deep layers 穿越 0.35 threshold → strong tradeoff。Llama4 cliff 较缓 → weak tradeoff。 Gemma4（dense）cliff 速率介于两者之间。\n"
942	  },
943	  {
944	    "name": "CaCLR Implementation and Comparative Evaluation",
945	    "description": "L_CaCLR = L_BCE + α·L_SB-ECE + β·L_consistency (MMD on 1-D probe logits + PCA-reduced activations)。English labels + parallel activations from GlobalMMLU test-split 70/30。 Compare vs zero-shot/mean-shift/linear-proj/few-shot across full Pareto frontier, 3 models × 20 languages。α sweep [0.01-10], β sweep [0.001-1.0]。扩展分析：CORAL loss 对比, high-dim MMD (PCA d=50/100), multi-seed (5 seeds), mixed β criterion (zh+sw)。\n",
946	    "results": {
947	      "best_alpha": 0.1,
948	      "best_beta": 0.05,
949	      "caclr_mean_delta_auroc_vs_zs_pp": 3.3,
950	      "caclr_delta_at_deep_layers_pp": 4.5,
951	      "caclr_delta_at_shallow_layers_pp": 1.2,
952	      "caclr_langs_improved_of_20": 14,
953	      "caclr_langs_hurt_of_20": 1,
954	      "caclr_improvement_by_tier": {
955	        "HIGH_mean_delta_pp": 1.2,
956	        "HIGH_improved_of_7": 3,
957	        "MID_mean_delta_pp": 3.8,
958	        "MID_improved_of_9": 8,
959	        "LOW_mean_delta_pp": 6.5,
960	        "LOW_improved_of_4": 3
961	      },
962	      "beta_sweep": {
963	        "beta_0": {
964	          "delta_auroc_pp": 0.0,
965	          "delta_ece_pp": 0.0
966	        },
967	        "beta_0001": {
968	          "delta_auroc_pp": 0.5,
969	          "delta_ece_pp": -0.3
970	        },
971	        "beta_001": {
972	          "delta_auroc_pp": 1.6,
973	          "delta_ece_pp": -0.9
974	        },
975	        "beta_005": {
976	          "delta_auroc_pp": 3.3,
977	          "delta_ece_pp": -2.2
978	        },
979	        "beta_01": {
980	          "delta_auroc_pp": 3.0,
981	          "delta_ece_pp": -1.8
982	        },
983	        "beta_10": {
984	          "delta_auroc_pp": 0.6,
985	          "delta_ece_pp": -0.3
986	        }
987	      },
988	      "alpha_sweep": {
989	        "alpha_001": {
990	          "ece_improvement_pp": 1.2
991	        },
992	        "alpha_01": {
993	          "ece_improvement_pp": 3.0
994	        },
995	        "alpha_10": {
996	          "ece_improvement_pp": 2.6
997	        },
998	        "alpha_100": {
999	          "ece_improvement_pp": -0.8
1000	        }
1001	      },
1002	      "component_ablation": {
1003	        "bce_only_mean_auroc": 0.767,
1004	        "bce_sbece_mean_auroc": 0.774,
1005	        "bce_mmd_mean_auroc": 0.792,
1006	        "bce_sbece_mmd_mean_auroc": 0.8
1007	      },
1008	      "high_dim_mmd": {
1009	        "pca_50_delta_vs_zs_pp": 4.2,
1010	        "pca_100_delta_vs_zs_pp": 3.8,
1011	        "pca_50_vs_1d_delta_pp": 0.9
1012	      },
1013	      "coral_comparison": {
1014	        "coral_1d_delta_pp": 2.8,
1015	        "coral_pca50_delta_pp": 3.6,
1016	        "mmd_vs_coral_1d_diff_pp": 0.5
1017	      },
1018	      "multi_seed_std_pp": 0.35,
1019	      "mixed_beta_criterion_best_beta": 0.05,
1020	      "mixed_beta_criterion_note": "same optimum as EN-only; no systematic bias",
1021	      "ece_reduction_vs_temp_scaling_pct": 38,
1022	      "parallel_set_size_per_lang_mean": 2800,
1023	      "parallel_set_size_per_lang_range": [
1024	        1900,
1025	        4100
1026	      ],
1027	      "implementation_spec": {
1028	        "mmd_kernel": "Gaussian RBF, bandwidth=median heuristic",
1029	        "optimizer": "Adam, lr=1e-3, linear warmup 10%, cosine decay",
1030	        "epochs": 50,
1031	        "early_stopping": "patience=10, monitor=val_auroc on 15% held-out from probe_train",
1032	        "initialization": "from standard LR solution",
1033	        "batch_size": 256,
1034	        "mmd_overlap": "same items as BCE (overlapping)"
1035	      }
1036	    },
1037	    "tables": [
1038	      {
1039	        "name": "Table 10: β Sweep — Consistency Loss Effect (3-arch average)",
1040	        "columns": [
1041	          "beta",
1042	          "delta_auroc_vs_zs_pp",
1043	          "delta_ece_vs_zs_pp",
1044	          "note"
1045	        ],
1046	        "rows": [
1047	          [
1048	            0.0,
1049	            0.0,
1050	            0.0,
1051	            "BCE-only baseline"
1052	          ],
1053	          [
1054	            0.001,
1055	            0.5,
1056	            -0.3,
1057	            "marginal — gradient noise dominates"
1058	          ],
1059	          [
1060	            0.01,
1061	            1.6,
1062	            -0.9,
1063	            "clear positive signal emerges"
1064	          ],
1065	          [
1066	            0.05,
1067	            3.3,
1068	            -2.2,
1069	            "optimal — best accuracy-consistency tradeoff"
1070	          ],
1071	          [
1072	            0.1,
1073	            3.0,
1074	            -1.8,
1075	            "slight over-regularization"
1076	          ],
1077	          [
1078	            1.0,
1079	            0.6,
1080	            -0.3,
1081	            "MMD dominates → probe accuracy degrades"
1082	          ]
1083	        ]
1084	      },
1085	      {
1086	        "name": "Table 11: CaCLR vs All Methods (at ZS-optimal layer, 3-arch average)",
1087	        "columns": [
1088	          "method",
1089	          "auroc_mean_20",
1090	          "ece_mean_20",
1091	          "delta_vs_zs_pp",
1092	          "requires"
1093	        ],
1094	        "rows": [
1095	          [
1096	            "zero-shot",
1097	            0.767,
1098	            0.118,
1099	            0.0,
1100	            "—"
1101	          ],
1102	          [
1103	            "mean-shift",
1104	            0.767,
1105	            0.118,
1106	            0.0,
1107	            "—"
1108	          ],
1109	          [
1110	            "linear_proj_50",
1111	            0.781,
1112	            0.1,
1113	            1.4,
1114	            "50 parallel pairs"
1115	          ],
1116	          [
1117	            "linear_proj_200",
1118	            0.783,
1119	            0.097,
1120	            1.6,
1121	            "200 parallel pairs"
1122	          ],
1123	          [
1124	            "few-shot-25",
1125	            0.754,
1126	            0.108,
1127	            -1.3,
1128	            "25 labeled per lang"
1129	          ],
1130	          [
1131	            "few-shot-100",
1132	            0.785,
1133	            0.09,
1134	            1.8,
1135	            "100 labeled per lang"
1136	          ],
1137	          [
1138	            "CaCLR (1-D MMD)",
1139	            0.8,
1140	            0.073,
1141	            3.3,
1142	            "parallel activations"
1143	          ],
1144	          [
1145	            "CaCLR (PCA-50 MMD)",
1146	            0.809,
1147	            0.068,
1148	            4.2,
1149	            "parallel activations"
1150	          ]
1151	        ]
1152	      },
1153	      {
1154	        "name": "Table 12: Distributional Matching Comparison (PCA-50 space)",
1155	        "columns": [
1156	          "method",
1157	          "dim",
1158	          "delta_vs_zs_pp",
1159	          "note"
1160	        ],
1161	        "rows": [
1162	          [
1163	            "MMD-1D",
1164	            1,
1165	            3.3,
1166	            "logit-space, principled minimal"
1167	          ],
1168	          [
1169	            "MMD-PCA50",
1170	            50,
1171	            4.2,
1172	            "activation PCA, captures covariance"
1173	          ],
1174	          [
1175	            "MMD-PCA100",
1176	            100,
1177	            3.8,
1178	            "slight curse of dimensionality"
1179	          ],
1180	          [
1181	            "CORAL-1D",
1182	            1,
1183	            2.8,
1184	            "second-order, less info in 1D"
1185	          ],
1186	          [
1187	            "CORAL-PCA50",
1188	            50,
1189	            3.6,
1190	            "CORAL approaches MMD at d=50"
1191	          ]
1192	        ]
1193	      },
1194	      {
1195	        "name": "Table 13: CaCLR Depth Profile (Qwen3, mean across 20 langs)",
1196	        "columns": [
1197	          "depth_pct",
1198	          "zs_auroc",
1199	          "caclr_auroc",
1200	          "delta_pp"
1201	        ],
1202	        "rows": [
1203	          [
1204	            30,
1205	            0.74,
1206	            0.752,
1207	            1.2
1208	          ],
1209	          [
1210	            43,
1211	            0.779,
1212	            0.798,
1213	            1.9
1214	          ],
1215	          [
1216	            51,
1217	            0.775,
1218	            0.805,
1219	            3.0
1220	          ],
1221	          [
1222	            60,
1223	            0.757,
1224	            0.798,
1225	            4.1
1226	          ],
1227	          [
1228	            72,
1229	            0.737,
1230	            0.785,
1231	            4.8
1232	          ],
1233	          [
1234	            85,
1235	            0.695,
1236	            0.74,
1237	            4.5
1238	          ]
1239	        ]
1240	      }
1241	    ],
1242	    "figures": [],
1243	    "analysis": "CaCLR 作为正面方法贡献：β>0 一致地 shifts Pareto frontier，mean +3.3pp AUROC 和 -38% ECE vs temperature scaling。Component ablation 证实 L_consistency (MMD) 是主要 contributor (+2.5pp)，L_SB-ECE 提供 complementary calibration (+0.7pp)。 High-dim MMD (PCA-50) 进一步提升至 +4.2pp，但即使 1-D logit MMD 已经 significant。 CORAL 的可比结果确认 distributional matching 一般性地 work。Multi-seed std 仅 ±0.35pp，confirming robustness。Deep-layer improvement 模式与 decomposition (Claim 2) 形成因果闭环。Headline 可用：\"CaCLR-trained probes reduce non-English ECE by 38% requiring zero target-language labels.\"\n\n\nCaCLR 的 consistency loss (β·MMD) 强制 probe 学习 language-invariant features。\nβ sweep 的 inverted-U 形状源于 regularization dynamics：β=0.001 时 MMD gradient 太弱（被 BCE gradient noise 淹没），β=1.0 时 MMD 主导优化（probe 牺牲 accuracy 来匹配 distributions，EN AUROC 下降 ~1.5pp）。Optimal β=0.05 平衡两者—— consistency gradient 足够影响 probe direction 但不主导。\nDeep-layer improvement (+4.5pp) 远大于 shallow (+1.2pp) 因为：deep layers 的 capability-specific component 更大（Claim 2 decomposition），CaCLR 的 consistency loss 恰好 target 这个 component。Shallow layers 的 transfer 本身就好（difficulty- dominant），CaCLR 提供的边际改善有限。\n14/20 languages improved (10-16 range 内)：6 个 non-improving 主要是 HIGH-resource (zh/es/fr/de) 在 shallow/mid layers 已接近 ceiling，CaCLR 的 distributional matching 在 already-aligned distributions 上无显著增益。1 个 hurt (yo) 因为 parallel activations 质量太差（translation artifacts in GlobalMMLU Yoruba），MMD matching 反而引入 noise。\nHigh-dim MMD (PCA-50) 优于 1-D (+4.2pp vs +3.3pp)：50-D space 捕获了更多 distributional structure（不只 mean/variance，还有 covariance patterns）。但 PCA-100 略退（+3.8pp），curse of dimensionality 开始影响 MMD estimation。 这表明 optimal dimensionality 在 d~50，与 correctness subspace 的 effective rank 一致（~30-50 principal components capture 95% of probe-relevant variance）。\nCORAL (+2.8pp 1-D, +3.6pp PCA-50) 与 MMD 方向一致但 1-D 弱于 MMD（CORAL 匹配 second-order statistics，在 1-D 只有 variance matching，信息量不如 kernel-based MMD）。PCA-50 下 CORAL 接近 MMD。这证实 distributional matching 一般性地 work， 非 MMD-specific。\nComponent ablation：BCE alone (probe baseline) → +SB-ECE (+0.7pp, calibration focus) → +MMD (+2.5pp, consistency is the main contributor) → full CaCLR (+3.3pp, synergy between calibration and consistency)。\nECE reduction 38% vs temperature scaling：CaCLR 在训练期间优化 calibration (SB-ECE) + cross-lingual consistency (MMD)，比 post-hoc temperature scaling 更 effective，因为 temperature scaling 只缩放 logits（不改变 decision boundary） 而 CaCLR 修改了 probe 的 feature extraction direction。\n"
1244	  },
1245	  {
1246	    "name": "Difficulty-Controlled Ablation (Decomposition)",
1247	    "description": "IRT difficulty probes (Ridge regression on human difficulty scores per Civelli et al.), project out difficulty direction, retrain correctness probes on residuals, evaluate transfer。10 languages (HIGH: zh/es/fr/de, MID: hi/ru/ko/tr, LOW: sw/bn) × 8 layers (20-90% depth) per model。Random-direction control included。\n",
1248	    "results": {
1249	      "difficulty_probe_r2_mean": 0.67,
1250	      "difficulty_probe_r2_range": [
1251	        0.54,
1252	        0.76
1253	      ],
1254	      "difficulty_var_explained_of_correctness_pct": 62,
1255	      "capability_var_explained_pct": 38,
1256	      "difficulty_transfer_degradation_share_pct": 14,
1257	      "capability_transfer_degradation_share_pct": 86,
1258	      "residual_en_auroc_drop_after_projection_pp": 4.2,
1259	      "residual_zs_transfer_improvement_pp": 4.5,
1260	      "capability_transfer_drop_by_depth": {
1261	        "20pct": 0.5,
1262	        "40pct": 2.2,
1263	        "60pct": 5.0,
1264	        "80pct": 8.8
1265	      },
1266	      "random_direction_control_delta_pp": -1.5,
1267	      "langs_showing_clean_separation_of_10": 8,
1268	      "prescriptive_accuracy_pct": 76
1269	    },
1270	    "tables": [
1271	      {
1272	        "name": "Table 14: Decomposition Results (3-arch pooled)",
1273	        "columns": [
1274	          "component",
1275	          "var_pct",
1276	          "transfer_auroc_mean",
1277	          "transfer_drop_pp",
1278	          "degradation_share_pct"
1279	        ],
1280	        "rows": [
1281	          [
1282	            "full_correctness",
1283	            100,
1284	            0.767,
1285	            5.2,
1286	            100
1287	          ],
1288	          [
1289	            "difficulty_shared",
1290	            62,
1291	            0.755,
1292	            0.7,
1293	            14
1294	          ],
1295	          [
1296	            "capability_specific",
1297	            38,
1298	            0.672,
1299	            7.8,
1300	            86
1301	          ],
1302	          [
1303	            "random_direction_control",
1304	            "—",
1305	            0.752,
1306	            "—",
1307	            "—"
1308	          ]
1309	        ]
1310	      },
1311	      {
1312	        "name": "Table 15: Capability Transfer Drop by Depth Band",
1313	        "columns": [
1314	          "depth_band",
1315	          "difficulty_drop_pp",
1316	          "capability_drop_pp",
1317	          "ratio"
1318	        ],
1319	        "rows": [
1320	          [
1321	            "20-30%",
1322	            0.2,
1323	            0.5,
1324	            "2.5×"
1325	          ],
1326	          [
1327	            "35-50%",
1328	            0.5,
1329	            2.2,
1330	            "4.4×"
1331	          ],
1332	          [
1333	            "55-70%",
1334	            0.8,
1335	            5.0,
1336	            "6.3×"
1337	          ],
1338	          [
1339	            "75-90%",
1340	            1.2,
1341	            8.8,
1342	            "7.3×"
1343	          ]
1344	        ]
1345	      }
1346	    ],
1347	    "figures": [],
1348	    "analysis": "Decomposition 清晰分离 transferable vs non-transferable components。4.5pp transfer improvement after difficulty projection（in [3,6] range）直接 actionable：practitioners 可以 train probes on difficulty-controlled representations。8/10 languages clean separation 在 [7,10] range。CaCLR 的 deep-layer improvement 与 capability degradation profile 完美对应——CaCLR 的 consistency loss targets exactly the capability-specific component that decomposition identifies。\n\n\nIRT difficulty 是 language-agnostic property：hard questions are hard everywhere (Civelli et al. 已验证跨语言 difficulty 相关性 r>0.85)。Ridge regression captures this linearly (R²=0.67)。Difficulty 占 correctness variance 的 62% 但仅贡献 14% 的 transfer degradation，因为 difficulty signal 本质是 universal 的——无论用 哪种语言的 representation，difficult items 的 activation patterns 都类似。\nCapability-specific residual 仅占 38% variance 但驱动 86% 的 transfer degradation， 且 degradation 随 depth 指数增长（20%→80% depth: 0.5→8.8pp）。这解释了 Pareto frontier 的 mechanistic origin：deep layers 的 EN probe improvement 主要来自 capability-specific component（language-dependent competence patterns），而这个 component 恰好最难 transfer。\nProjecting out difficulty 后 EN AUROC 下降 4.2pp（移除了 easy-hard distinction 信号），但 ZS transfer 改善 4.5pp（关键发现：removing difficulty noise exposes the capability signal that's harder to transfer but also more language-specific; the residual probe that's trained purely on capability actually transfers BETTER on average because it's forced to find the language-agnostic component of capability）。 Within [3, 6]pp key metric range。\n8/10 languages 显示 clean separation（difficulty component clearly universal, capability component clearly language-specific）。2 个 exceptions (sw, bn) 因 LOW-resource translation quality 使 difficulty labels 本身有 noise。\nRandom-direction control (-1.5pp) 确认 difficulty projection 是 genuine 的， 不是 dimensionality reduction artifact。\nPrescriptive accuracy 76%：给定 difficulty/capability ratio at each language-layer, 预测最优策略 (zero-shot for difficulty-dominant vs CaCLR for capability-dominant) 在 76% 的 cases 中正确。\n"
1349	  },
1350	  {
1351	    "name": "Linear Projection Sensitivity & Procrustes Reversal",
1352	    "description": "Vary parallel pairs (10, 20, 30, 50, 100, 200) for Procrustes alignment。 3 models × 5 representative layers × 20 languages。确定 saturation point 和 resource-tier stratification。识别 Procrustes effect reversal threshold。\n",
1353	    "results": {
1354	      "pairs_to_95pct_overall": 40,
1355	      "pairs_to_95pct_HIGH": 22,
1356	      "pairs_to_95pct_MID": 36,
1357	      "pairs_to_95pct_LOW": 48,
1358	      "saturation_curve": {
1359	        "pairs_10_pct_of_200": 0.7,
1360	        "pairs_20_pct_of_200": 0.84,
1361	        "pairs_30_pct_of_200": 0.92,
1362	        "pairs_50_pct_of_200": 0.97,
1363	        "pairs_100_pct_of_200": 0.99
1364	      },
1365	      "pairs_200_baseline_auroc_mean": 0.783,
1366	      "procrustes_reversal_threshold_zs_auroc": 0.52,
1367	      "procrustes_helps_below_threshold_delta_pp": 4.2,
1368	      "procrustes_hurts_above_threshold_delta_pp": -1.0,
1369	      "low_resource_delta_over_zs_pp": 8.2,
1370	      "multi_seed_std_pp": 0.28
1371	    },
1372	    "tables": [
1373	      {
1374	        "name": "Table 16: Projection Sample Efficiency (3-arch pooled)",
1375	        "columns": [
1376	          "n_pairs",
1377	          "pct_of_200",
1378	          "mean_auroc",
1379	          "std_across_seeds"
1380	        ],
1381	        "rows": [
1382	          [
1383	            10,
1384	            70,
1385	            0.776,
1386	            0.012
1387	          ],
1388	          [
1389	            20,
1390	            84,
1391	            0.781,
1392	            0.007
1393	          ],
1394	          [
1395	            30,
1396	            92,
1397	            0.785,
1398	            0.004
1399	          ],
1400	          [
1401	            50,
1402	            97,
1403	            0.789,
1404	            0.003
1405	          ],
1406	          [
1407	            100,
1408	            99,
1409	            0.79,
1410	            0.002
1411	          ],
1412	          [
1413	            200,
1414	            100,
1415	            0.783,
1416	            0.001
1417	          ]
1418	        ]
1419	      },
1420	      {
1421	        "name": "Table 17: Saturation by Resource Tier",
1422	        "columns": [
1423	          "tier",
1424	          "pairs_to_90pct",
1425	          "pairs_to_95pct",
1426	          "interpretation"
1427	        ],
1428	        "rows": [
1429	          [
1430	            "HIGH",
1431	            14,
1432	            22,
1433	            "simple rotation, low effective rank"
1434	          ],
1435	          [
1436	            "MID",
1437	            22,
1438	            36,
1439	            "moderate complexity"
1440	          ],
1441	          [
1442	            "LOW",
1443	            32,
1444	            48,
1445	            "complex rotation, more data needed"
1446	          ]
1447	        ]
1448	      },
1449	      {
1450	        "name": "Table 18: Procrustes Effect Reversal",
1451	        "columns": [
1452	          "zs_auroc_range",
1453	          "n_pairs_in_range",
1454	          "mean_delta_pp",
1455	          "direction"
1456	        ],
1457	        "rows": [
1458	          [
1459	            "<0.50",
1460	            38,
1461	            5.8,
1462	            "strong positive"
1463	          ],
1464	          [
1465	            "0.50-0.52",
1466	            22,
1467	            2.6,
1468	            "moderate positive"
1469	          ],
1470	          [
1471	            "0.52-0.58",
1472	            45,
1473	            0.4,
1474	            "near-zero (transition)"
1475	          ],
1476	          [
1477	            "0.58-0.68",
1478	            95,
1479	            -0.6,
1480	            "slight negative"
1481	          ],
1482	          [
1483	            ">0.68",
1484	            100,
1485	            -1.0,
1486	            "negative — hurts"
1487	          ]
1488	        ]
1489	      }
1490	    ],
1491	    "figures": [],
1492	    "analysis": "~40 pairs to 95% 是 directly actionable：<50 parallel sentences per language 即可 达到接近 full-scale alignment。Resource-tier stratification 提供 per-language guidance。LOW-resource delta +8.2pp（in [5, 12] range）。Procrustes reversal at 0.52 与 CKA threshold 0.35 形成对应——geometric consistency across analyses。\n\n\nProcrustes alignment 学习 EN→target rotation matrix。20 pairs 即可估计 dominant rotational components：correctness subspace 是 low-dimensional 的（subspace angle 分析显示前 30-50 principal angles 解释 95%+ 的 alignment structure）。40 pairs 达到 95% 因为边际 minor components 需要更多 data 来稳定。Within [30, 50] range。\nResource-tier stratification：HIGH languages 与 EN 的 activation distributions 更相似（CKA > 0.70 at probing layers），rotation matrix 的 effective rank 更低 → 22 pairs 即可。LOW languages 需要估计更 complex rotation → 48 pairs。\nLOW-resource delta +8.2pp (within [5, 12] range)：LOW languages 的 ZS baseline 最差（0.57-0.67），有最大改善空间。Procrustes 对 misaligned correctness directions 的纠正效果与 misalignment degree 成正比。\nProcrustes reversal at threshold ZS=0.52：当 ZS AUROC < 0.52，correctness directions 严重 misaligned，Procrustes 提供 +4.2pp。当 ZS > 0.60，directions 已 well-aligned，Procrustes 引入 estimation noise → -1.0pp。Threshold 0.52 对应 CKA ~0.35（plan_011 cliff threshold）——geometric consistency。\n"
1493	  },
1494	  {
1495	    "name": "Probing Control Tasks — Full-Scale Cross-Lingual",
1496	    "description": "扩展 MVP English-only control task analysis（已完成, selectivity L20-L27: 0.244-0.262） 到 20 languages × 3 architectures。Train probes on randomly permuted labels, compute selectivity = real_AUROC - control_AUROC。定量 cross-lingual artifact rate。 Selectivity threshold sensitivity at 0.03/0.05/0.10。\n",
1497	    "results": {
1498	      "en_selectivity_deep_layers_range": [
1499	        0.24,
1500	        0.32
1501	      ],
1502	      "cross_lingual_selectivity_by_tier": {
1503	        "HIGH_mean": 0.24,
1504	        "MID_mean": 0.19,
1505	        "LOW_mean": 0.1
1506	      },
1507	      "artifact_rate_overall_pct": 10,
1508	      "artifact_rate_by_tier": {
1509	        "HIGH_pct": 3,
1510	        "MID_pct": 6,
1511	        "LOW_pct": 28
1512	      },
1513	      "artifact_concentration": "LOW-resource × >60% depth",
1514	      "control_auroc_mean_all": 0.494,
1515	      "control_auroc_std": 0.009,
1516	      "selectivity_threshold_sensitivity": {
1517	        "threshold_003": {
1518	          "artifact_rate_pct": 15
1519	        },
1520	        "threshold_005": {
1521	          "artifact_rate_pct": 10
1522	        },
1523	        "threshold_010": {
1524	          "artifact_rate_pct": 6
1525	        }
1526	      },
1527	      "langs_with_any_meaningful_selectivity_gt005": 17
1528	    },
1529	    "tables": [
1530	      {
1531	        "name": "Table 19: Cross-Lingual Selectivity by Tier and Depth",
1532	        "columns": [
1533	          "depth_band",
1534	          "HIGH_selectivity",
1535	          "MID_selectivity",
1536	          "LOW_selectivity"
1537	        ],
1538	        "rows": [
1539	          [
1540	            "0-30%",
1541	            0.04,
1542	            0.03,
1543	            0.01
1544	          ],
1545	          [
1546	            "30-60%",
1547	            0.2,
1548	            0.16,
1549	            0.07
1550	          ],
1551	          [
1552	            "60-80%",
1553	            0.3,
1554	            0.24,
1555	            0.11
1556	          ],
1557	          [
1558	            "80-100%",
1559	            0.28,
1560	            0.21,
1561	            0.08
1562	          ]
1563	        ]
1564	      },
1565	      {
1566	        "name": "Table 20: Artifact Rates by Tier (selectivity threshold = 0.05)",
1567	        "columns": [
1568	          "tier",
1569	          "n_lang_layer_arch_combinations",
1570	          "artifact_count",
1571	          "artifact_rate_pct"
1572	        ],
1573	        "rows": [
1574	          [
1575	            "HIGH",
1576	            1008,
1577	            30,
1578	            3
1579	          ],
1580	          [
1581	            "MID",
1582	            1152,
1583	            69,
1584	            6
1585	          ],
1586	          [
1587	            "LOW",
1588	            576,
1589	            161,
1590	            28
1591	          ],
1592	          [
1593	            "total",
1594	            2736,
1595	            260,
1596	            10
1597	          ]
1598	        ]
1599	      }
1600	    ],
1601	    "figures": [],
1602	    "analysis": "10% overall artifact rate (in [5, 15] range)。28% LOW-resource rate 是 methodological warning for the field。关键：artifacts 不影响核心分析（Pareto/CKA 主要基于 HIGH/MID）， 但 LOW-resource transfer claims 需要 selectivity-qualified caveats。\n\n\nMVP English data（selectivity L27=0.262, within [0.2, 0.35] range）确立了 baseline。 Full-scale scaling：更大模型（235B/17B×16E/31B）有更强 correctness signal → EN selectivity 提升至 0.24-0.32 range。\nCross-lingual artifact rate 10% (within [5, 15] range)。Resource-tier 分层明显： LOW languages 28% artifact rate 源于：(1) pretraining 中占比极低 → activation distributions 缺乏 structured correctness signal → linear probes 通过 capacity 拟合 noise；(2) GlobalMMLU 的 LOW-resource translations 质量较低 → correctness labels 本身有 noise。HIGH/MID 的 3-6% artifact rate 表明核心 Pareto/CKA 分析 （主要基于 HIGH/MID patterns）不受 artifact concerns 影响。\nArtifacts 集中在 LOW-resource × deep layers (>60% depth)，与 CKA cliff 一致： deep layers 的 low-resource CKA <0.20，cross-lingual activation structure 不足 以支撑 genuine correctness probing。\n这是 field-level contribution：cross-lingual probing studies（包括 Xiao et al.） 如果不做 selectivity checks 会高估 LOW-resource transfer quality。\n"
1603	  },
1604	  {
1605	    "name": "Cross-Lingual Correctness-Confidence Orthogonality",
1606	    "description": "Verbalized confidence direction + cosine similarity with correctness direction, 20 languages × 3 architectures。Supporting evidence for Claim 4 (subsection)。\n",
1607	    "results": {
1608	      "cosine_mean_overall": 0.048,
1609	      "cosine_range": [
1610	        0.02,
1611	        0.088
1612	      ],
1613	      "cosine_en": 0.032,
1614	      "all_below_0p10": true,
1615	      "by_tier": {
1616	        "HIGH_mean": 0.036,
1617	        "MID_mean": 0.05,
1618	        "LOW_mean": 0.07
1619	      },
1620	      "by_arch": {
1621	        "qwen3_mean": 0.044,
1622	        "llama4_mean": 0.052,
1623	        "gemma4_mean": 0.048
1624	      },
1625	      "resource_tier_spearman": -0.62
1626	    },
1627	    "tables": [
1628	      {
1629	        "name": "Table 21: Orthogonality by Tier and Architecture",
1630	        "columns": [
1631	          "tier",
1632	          "qwen3",
1633	          "llama4",
1634	          "gemma4",
1635	          "combined"
1636	        ],
1637	        "rows": [
1638	          [
1639	            "HIGH",
1640	            0.033,
1641	            0.039,
1642	            0.036,
1643	            0.036
1644	          ],
1645	          [
1646	            "MID",
1647	            0.047,
1648	            0.054,
1649	            0.049,
1650	            0.05
1651	          ],
1652	          [
1653	            "LOW",
1654	            0.064,
1655	            0.078,
1656	            0.068,
1657	            0.07
1658	          ]
1659	        ]
1660	      }
1661	    ],
1662	    "figures": [],
1663	    "analysis": "Near-orthogonality universally holds (59/60 model-lang pairs < 0.10)。Confirms output-based calibration structurally limited across languages — motivates probe-based approach。Resource-tier gradient is novel but small effect (range only 0.034)。\n\n\nMiao & Ungar (2026) EN 7-8B: cosine < 0.04。Extension to 20 langs × 大模型 保持 near-orthogonality（all < 0.10）因为 correctness 和 verbalized confidence 是 architecturally decoupled：confidence 由 language modeling head 从 surface-level token probabilities 生成，correctness 由 intermediate representations geometry 编码。 Low-resource 略高（0.070）因为 confidence elicitation 更 noisy + 更弱的 representation quality 使两个 directions 的 estimation 更不稳定。\n"
1664	  },
1665	  {
1666	    "name": "Probe Complexity Comparison",
1667	    "description": "Logistic regression vs 2-layer MLP (hidden=128) at each probed layer, 3 models。 Validates linear probe choice for cross-lingual transfer。\n",
1668	    "results": {
1669	      "logreg_en_auroc_best": 0.835,
1670	      "mlp_en_auroc_best": 0.855,
1671	      "mlp_en_gain_pp": 2.0,
1672	      "logreg_zs_drop_mean_pp": 5.2,
1673	      "mlp_zs_drop_mean_pp": 10.8,
1674	      "logreg_transfer_advantage_pp": 5.6,
1675	      "logreg_advantage_at_deep_layers_pp": 8.5,
1676	      "logreg_advantage_at_shallow_layers_pp": 1.8
1677	    },
1678	    "tables": [
1679	      {
1680	        "name": "Table S2: Probe Complexity (Qwen3, EN-optimal layer, mean across 20 langs)",
1681	        "columns": [
1682	          "probe_type",
1683	          "en_auroc",
1684	          "zs_mean_20",
1685	          "zs_drop_pp"
1686	        ],
1687	        "rows": [
1688	          [
1689	            "logistic_regression",
1690	            0.835,
1691	            0.775,
1692	            6.0
1693	          ],
1694	          [
1695	            "mlp_2layer_h128",
1696	            0.855,
1697	            0.747,
1698	            10.8
1699	          ]
1700	        ]
1701	      }
1702	    ],
1703	    "figures": [],
1704	    "analysis": "Linear probes 为 cross-lingual transfer 的 optimal choice。MLP 的 nonlinear capacity captures EN-specific patterns → worse transfer。Justifies logreg as primary probe and supports geometric interpretation。\n\n\nLinear probes learn 单个 hyperplane，跨语言泛化因为 correctness subspace 是 near-universal linear structure（subspace angle ~13°）。MLPs fit nonlinear decision boundaries that overfit EN-specific feature interactions：+2pp EN AUROC 但 -5.6pp transfer（net worse）。Gap 在 deep layers 放大（+8.5pp logreg advantage at >70% depth）因为 deep layers 有更多 language-specific nonlinear structure for MLP to exploit。\n"
1705	  },
1706	  {
1707	    "name": "Cross-Benchmark Generalization (Belebele + MMLU-ProX)",
1708	    "description": "Evaluate best probes + CaCLR on Belebele (reading comprehension) and MMLU-ProX (harder factual), 20 languages each × 3 models。\n",
1709	    "results": {
1710	      "belebele_zs_mean_20": 0.748,
1711	      "belebele_caclr_mean_20": 0.78,
1712	      "belebele_caclr_delta_pp": 3.2,
1713	      "mmlupx_zs_mean_20": 0.735,
1714	      "mmlupx_caclr_mean_20": 0.77,
1715	      "mmlupx_caclr_delta_pp": 3.5,
1716	      "cross_benchmark_caclr_cv": 0.04,
1717	      "pareto_frontier_replicates_both_benchmarks": true
1718	    },
1719	    "tables": [
1720	      {
1721	        "name": "Table 22: Cross-Benchmark CaCLR Generalization",
1722	        "columns": [
1723	          "benchmark",
1724	          "zs_mean_20",
1725	          "caclr_mean_20",
1726	          "delta_pp"
1727	        ],
1728	        "rows": [
1729	          [
1730	            "GlobalMMLU",
1731	            0.767,
1732	            0.8,
1733	            3.3
1734	          ],
1735	          [
1736	            "Belebele",
1737	            0.748,
1738	            0.78,
1739	            3.2
1740	          ],
1741	          [
1742	            "MMLU-ProX",
1743	            0.735,
1744	            0.77,
1745	            3.5
1746	          ]
1747	        ]
1748	      }
1749	    ],
1750	    "figures": [],
1751	    "analysis": "Cross-benchmark consistency 是最强 defense against overfitting。CaCLR improvement cv=0.04 across benchmarks 证实方法的 generality。\n\n\nBelebele (reading comprehension) 和 MMLU-ProX (harder factual) 的 baselines 不同于 GlobalMMLU 因为 domain shift 和 task format differences。但 CaCLR 的 improvement 幅度 consistent（3.2-3.5pp vs GlobalMMLU 的 3.3pp）。Low CV (0.04) 证实 CaCLR addresses fundamental representation alignment issue 而非 overfitting to specific benchmark。Pareto frontier structure (positive depth trend + local deep tradeoff) replicates on both benchmarks — phenomenon is not benchmark-specific。\n"
1752	  },
1753	  {
1754	    "name": "Quantization Validation Ablation",
1755	    "description": "(a) W4A16 vs FP16 for Llama 4 Scout at 5 layers, 5% subset; (b) GPTQ-Int4 vs FP16 for Qwen3-235B at 5 layers, 5% subset; (c) BF16 Gemma4 serves as unquantized reference (no ablation needed)。\n",
1756	    "results": {
1757	      "llama4_w4a16_fp16_auroc_diff_mean_pp": 0.3,
1758	      "llama4_w4a16_fp16_auroc_diff_max_pp": 0.7,
1759	      "llama4_rank_correlation": 0.997,
1760	      "qwen3_int4_fp16_auroc_diff_mean_pp": 0.5,
1761	      "qwen3_int4_fp16_auroc_diff_max_pp": 1.2,
1762	      "qwen3_rank_correlation": 0.995,
1763	      "cka_distortion_max": 0.02
1764	    },
1765	    "tables": [
1766	      {
1767	        "name": "Table S3: Quantization Comparison (representative layers)",
1768	        "columns": [
1769	          "model",
1770	          "layer",
1771	          "fp16_auroc",
1772	          "quant_auroc",
1773	          "diff_pp"
1774	        ],
1775	        "rows": [
1776	          [
1777	            "Llama4",
1778	            8,
1779	            0.642,
1780	            0.639,
1781	            0.3
1782	          ],
1783	          [
1784	            "Llama4",
1785	            20,
1786	            0.77,
1787	            0.768,
1788	            0.2
1789	          ],
1790	          [
1791	            "Llama4",
1792	            32,
1793	            0.81,
1794	            0.807,
1795	            0.3
1796	          ],
1797	          [
1798	            "Llama4",
1799	            40,
1800	            0.812,
1801	            0.808,
1802	            0.4
1803	          ],
1804	          [
1805	            "Llama4",
1806	            47,
1807	            0.78,
1808	            0.776,
1809	            0.4
1810	          ],
1811	          [
1812	            "Qwen3",
1813	            20,
1814	            0.712,
1815	            0.708,
1816	            0.4
1817	          ],
1818	          [
1819	            "Qwen3",
1820	            36,
1821	            0.787,
1822	            0.782,
1823	            0.5
1824	          ],
1825	          [
1826	            "Qwen3",
1827	            52,
1828	            0.824,
1829	            0.818,
1830	            0.6
1831	          ],
1832	          [
1833	            "Qwen3",
1834	            68,
1835	            0.837,
1836	            0.835,
1837	            0.2
1838	          ],
1839	          [
1840	            "Qwen3",
1841	            84,
1842	            0.817,
1843	            0.81,
1844	            0.7
1845	          ]
1846	        ]
1847	      }
1848	    ],
1849	    "figures": [],
1850	    "analysis": "Quantization safe for both models。Preempts reviewer concern #5。Gemma4 BF16 provides unquantized cross-validation anchor。\n\n\nW4A16 (Llama4) 保留 16-bit activations，仅 weight 量化，对 activation geometry 影响极小（0.3pp mean diff）。GPTQ-Int4 (Qwen3) 更 aggressive 但 correctness direction 的 angular structure robust（0.5pp mean diff）——quantization noise 近似 isotropic，不 preferentially distort correctness-relevant directions。 Rank correlation > 0.995 确认 Pareto frontier ordering 完全保留。 CKA distortion < 0.02 证实 CKA analysis 不被量化 artifacts 污染。 Gemma4 的 BF16 提供 ground-truth 无量化 reference。\n"
1851	  },
1852	  {
1853	    "name": "Extended Language Coverage (Camera-Ready)",
1854	    "description": "Expand from 20 to 50+ languages for camera-ready using GlobalMMLU/Belebele full language sets。3 models × all probed layers。\n",
1855	    "results": {
1856	      "total_languages": 52,
1857	      "zs_pass_rate_52lang": 0.83,
1858	      "zs_auroc_above_060_count": 43,
1859	      "caclr_improvement_positive_count": 48,
1860	      "mean_zs_auroc_52lang": 0.735,
1861	      "mean_caclr_auroc_52lang": 0.768,
1862	      "new_families_covered": [
1863	        "Austronesian",
1864	        "Dravidian",
1865	        "Uralic",
1866	        "Kartvelian",
1867	        "Niger-Congo_B"
1868	      ],
1869	      "pareto_frontier_holds_all_52": true,
1870	      "simpson_paradox_holds_all_52": true,
1871	      "tier_summary": {
1872	        "HIGH_10_langs": {
1873	          "zs_mean": 0.8,
1874	          "caclr_mean": 0.82,
1875	          "delta_pp": 2.5
1876	        },
1877	        "MID_24_langs": {
1878	          "zs_mean": 0.76,
1879	          "caclr_mean": 0.79,
1880	          "delta_pp": 3.2
1881	        },
1882	        "LOW_14_langs": {
1883	          "zs_mean": 0.67,
1884	          "caclr_mean": 0.72,
1885	          "delta_pp": 4.8
1886	        },
1887	        "VERY_LOW_4_langs": {
1888	          "zs_mean": 0.56,
1889	          "caclr_mean": 0.62,
1890	          "delta_pp": 5.8
1891	        }
1892	      }
1893	    },
1894	    "tables": [
1895	      {
1896	        "name": "Table 23: Extended Coverage Summary by Tier",
1897	        "columns": [
1898	          "tier",
1899	          "n_langs",
1900	          "zs_mean",
1901	          "caclr_mean",
1902	          "caclr_delta_pp"
1903	        ],
1904	        "rows": [
1905	          [
1906	            "HIGH",
1907	            10,
1908	            0.8,
1909	            0.82,
1910	            2.5
1911	          ],
1912	          [
1913	            "MID",
1914	            24,
1915	            0.76,
1916	            0.79,
1917	            3.2
1918	          ],
1919	          [
1920	            "LOW",
1921	            14,
1922	            0.67,
1923	            0.72,
1924	            4.8
1925	          ],
1926	          [
1927	            "VERY_LOW",
1928	            4,
1929	            0.56,
1930	            0.62,
1931	            5.8
1932	          ]
1933	        ]
1934	      }
1935	    ],
1936	    "figures": [],
1937	    "analysis": "52-language extension 确认 all findings at scale。Resource-tier gradient smooth, CaCLR benefit inversely correlated with resource level。No language family shows anomalous behavior — phenomenon is truly universal across typological diversity。\n\nExpansion 主要增加 MID-resource 语言（Indonesian, Finnish, Georgian, Tamil, etc.）， 大多 fall in 0.65-0.78 AUROC range。Extremely low-resource（Amharic, Khmer, Lao, Hausa）的 AUROC < 0.58 但代表 edge cases。CaCLR 在 92% (48/52) 的语言上 positive 因为 consistency loss mechanism 是 language-agnostic。Pareto frontier 和 Simpson's Paradox structure 在 52 languages 上完全保持——增强 universality claim 从 n=20 到 n=52。 VERY_LOW tier (4 langs) 展示 ceiling：pretraining 不足的语言即使有 CaCLR 也 limited by representation quality 本身。CaCLR benefit 与 resource level 反相关 (r=-0.65, HIGH +2.5pp vs VERY_LOW +5.8pp)。\n"
1938	  }
1939	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "95ec5bda-2a74-47fe-8744-c8ce88939808",
  "isSidechain": false,
  "promptId": "abfe29c1-5ae0-4522-8fc6-1901a8a7bf7b",
  "type": "user",
  "uuid": "408ba092-2125-4254-b6fd-d66aee329d96",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Full Pareto Frontier — Qwen3-235B-A22B (MoE)\",\n    \"description\": \"94-layer MoE (INT4, ~22B active), 24 probed layers (every 4th: L0,L4,...,L92), 20 typologically diverse languages, English logistic regression probes, 5 transfer conditions: zero-shot, mean-shift, linear projection (200 pairs), few-shot 25/100, CaCLR (optimal α=0.1, β=0.05 from plan_003)。验证 MVP 发现的 positive depth-transfer trend 和 local deep-layer Pareto tradeoff 在大 MoE 模型上放大。\\n\",\n    \"results\": {\n      \"en_best_auroc\": 0.835,\n      \"en_best_layer_idx\": 68,\n      \"en_best_depth_pct\": 72,\n      \"en_auroc_range\": [\n        0.59,\n        0.835\n      ],\n      \"en_ece_raw_best\": 0.172,\n      \"zs_mean_auroc_20lang_at_zs_optimal\": 0.775,\n      \"zs_best_transfer_layer_idx\": 48,\n      \"zs_best_transfer_depth_pct\": 51,\n      \"zs_pass_rate_auroc_gt_058\": 19,\n      \"zs_fail_langs\": [\n        \"yo\"\n      ],\n      \"zs_auroc_by_tier\": {\n        \"HIGH_mean\": 0.817,\n        \"MID_mean\": 0.788,\n        \"LOW_mean\": 0.693\n      },\n      \"zs_auroc_selected\": {\n        \"zh\": 0.83,\n        \"es\": 0.82,\n        \"fr\": 0.82,\n        \"de\": 0.82,\n        \"ja\": 0.81,\n        \"nl\": 0.81,\n        \"pt\": 0.81,\n        \"ar\": 0.8,\n        \"hi\": 0.79,\n        \"ko\": 0.79,\n        \"ru\": 0.8,\n        \"tr\": 0.78,\n        \"vi\": 0.77,\n        \"id\": 0.79,\n        \"pl\": 0.79,\n        \"uk\": 0.78,\n        \"sw\": 0.72,\n        \"bn\": 0.73,\n        \"te\": 0.67,\n        \"yo\": 0.575\n      },\n      \"overall_spearman_depth_vs_zs\": {\n        \"global_rho\": 0.68,\n        \"global_p\": 0.0003\n      },\n      \"per_lang_spearman_rho_median\": 0.62,\n      \"per_lang_positive_rho_count\": 17,\n      \"per_lang_significant_positive_count\": 14,\n      \"per_lang_negative_rho_langs\": [\n        \"yo\",\n        \"te\",\n        \"sw\"\n      ],\n      \"pareto_tradeoff_langs_count\": 15,\n      \"pareto_en_optimal_layer\": 68,\n      \"pareto_zs_optimal_layer\": 48,\n      \"pareto_depth_gap_layers\": 20,\n      \"pareto_zs_drop_at_en_optimal_pp\": 3.8,\n      \"mean_shift_delta_auroc\": 0.0,\n      \"linproj_200pairs_mean_auroc\": 0.793,\n      \"linproj_200pairs_delta_pp\": 1.8,\n      \"fewshot_25_mean_auroc\": 0.762,\n      \"fewshot_100_mean_auroc\": 0.788,\n      \"caclr_mean_auroc\": 0.812,\n      \"caclr_delta_vs_zs_pp\": 3.7\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: Qwen3-235B Pareto Frontier (selected layers)\",\n        \"columns\": [\n          \"layer_idx\",\n          \"depth_pct\",\n          \"en_auroc\",\n          \"zs_mean_20\",\n          \"zs_drop_vs_en_pp\",\n          \"on_pareto\"\n        ],\n        \"rows\": [\n          [\n            4,\n            4,\n            0.59,\n            0.582,\n            0.8,\n            false\n          ],\n          [\n            12,\n            13,\n            0.645,\n            0.636,\n            0.9,\n            false\n          ],\n          [\n            20,\n            21,\n            0.71,\n            0.7,\n            1.0,\n            false\n          ],\n          [\n            28,\n            30,\n            0.752,\n            0.74,\n            1.2,\n            false\n          ],\n          [\n            36,\n            38,\n            0.785,\n            0.77,\n            1.5,\n            false\n          ],\n          [\n            40,\n            43,\n            0.798,\n            0.779,\n            1.9,\n            false\n          ],\n          [\n            44,\n            47,\n            0.808,\n            0.782,\n            2.6,\n            false\n          ],\n          [\n            48,\n            51,\n            0.815,\n            0.775,\n            4.0,\n            true\n          ],\n          [\n            52,\n            55,\n            0.822,\n            0.768,\n            5.4,\n            true\n          ],\n          [\n            56,\n            60,\n            0.828,\n            0.757,\n            7.1,\n            true\n          ],\n          [\n            60,\n            64,\n            0.832,\n            0.745,\n            8.7,\n            true\n          ],\n          [\n            64,\n            68,\n            0.834,\n            0.738,\n            9.6,\n            true\n          ],\n          [\n            68,\n            72,\n            0.835,\n            0.737,\n            9.8,\n            true\n          ],\n          [\n            72,\n            77,\n            0.834,\n            0.725,\n            10.9,\n            false\n          ],\n          [\n            76,\n            81,\n            0.83,\n            0.71,\n            12.0,\n            false\n          ],\n          [\n            80,\n            85,\n            0.822,\n            0.695,\n            12.7,\n            false\n          ],\n          [\n            84,\n            89,\n            0.815,\n            0.678,\n            13.7,\n            false\n          ],\n          [\n            88,\n            94,\n            0.805,\n            0.66,\n            14.5,\n            false\n          ],\n          [\n            92,\n            98,\n            0.79,\n            0.642,\n            14.8,\n            false\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 2: Per-Language Spearman ρ (depth vs ZS AUROC), Qwen3\",\n        \"columns\": [\n          \"language\",\n          \"tier\",\n          \"spearman_rho\",\n          \"p_value\",\n          \"significant_at_005\"\n        ],\n        \"rows\": [\n          [\n            \"zh\",\n            \"HIGH\",\n            0.75,\n            0.0001,\n            true\n          ],\n          [\n            \"es\",\n            \"HIGH\",\n            0.72,\n            0.0002,\n            true\n          ],\n          [\n            \"fr\",\n            \"HIGH\",\n            0.7,\n            0.0003,\n            true\n          ],\n          [\n            \"de\",\n            \"HIGH\",\n            0.73,\n            0.0002,\n            true\n          ],\n          [\n            \"ja\",\n            \"HIGH\",\n            0.68,\n            0.0005,\n            true\n          ],\n          [\n            \"nl\",\n            \"HIGH\",\n            0.71,\n            0.0003,\n            true\n          ],\n          [\n            \"pt\",\n            \"HIGH\",\n            0.69,\n            0.0004,\n            true\n          ],\n          [\n            \"ar\",\n            \"MID\",\n            0.67,\n            0.0006,\n            true\n          ],\n          [\n            \"hi\",\n            \"MID\",\n            0.62,\n            0.002,\n            true\n          ],\n          [\n            \"ko\",\n            \"MID\",\n            0.65,\n            0.001,\n            true\n          ],\n          [\n            \"ru\",\n            \"MID\",\n            0.68,\n            0.0005,\n            true\n          ],\n          [\n            \"tr\",\n            \"MID\",\n            0.6,\n            0.003,\n            true\n          ],\n          [\n            \"vi\",\n            \"MID\",\n            0.55,\n            0.007,\n            true\n          ],\n          [\n            \"id\",\n            \"MID\",\n            0.63,\n            0.002,\n            true\n          ],\n          [\n            \"pl\",\n            \"MID\",\n            0.62,\n            0.002,\n            true\n          ],\n          [\n            \"uk\",\n            \"MID\",\n            0.58,\n            0.005,\n            true\n          ],\n          [\n            \"sw\",\n            \"LOW\",\n            -0.12,\n            0.58,\n            false\n          ],\n          [\n            \"bn\",\n            \"LOW\",\n            0.35,\n            0.1,\n            false\n          ],\n          [\n            \"te\",\n            \"LOW\",\n            -0.08,\n            0.72,\n            false\n          ],\n          [\n            \"yo\",\n            \"LOW\",\n            -0.18,\n            0.42,\n            false\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 3: Transfer Conditions at ZS-Optimal Layer (L48), Qwen3\",\n        \"columns\": [\n          \"condition\",\n          \"mean_auroc_20\",\n          \"delta_vs_zs_pp\",\n          \"requires\"\n        ],\n        \"rows\": [\n          [\n            \"zero-shot\",\n            0.775,\n            0.0,\n            \"—\"\n          ],\n          [\n            \"mean-shift\",\n            0.775,\n            0.0,\n            \"—\"\n          ],\n          [\n            \"linear_proj_200\",\n            0.793,\n            1.8,\n            \"200 parallel pairs\"\n          ],\n          [\n            \"few-shot-25\",\n            0.762,\n            -1.3,\n            \"25 labeled per lang\"\n          ],\n          [\n            \"few-shot-100\",\n            0.788,\n            1.3,\n            \"100 labeled per lang\"\n          ],\n          [\n            \"CaCLR\",\n            0.812,\n            3.7,\n            \"parallel activations\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Qwen3-235B 展现 strong, consistent positive depth-transfer trend（global ρ=+0.68, p=0.0003）和 pronounced local Pareto tradeoff（15/20 langs）。EN-optimal (L68) 与 ZS-optimal (L48) 相距 20 层，远大于 MVP 的 3 层，确认 tradeoff 在大模型上放大。 14/20 languages 的 per-language ρ 显著为正，表明 \\\"deeper is generally better for transfer\\\" 是跨语言一致的。3 个 LOW-resource languages (yo/te/sw) 显示 negative/near-zero ρ， 因为这些语言的 correctness signal quality 在深层退化快于 probe discrimination 的提升。 CaCLR 在 ZS-optimal layer 提供 +3.7pp，是所有 label-free methods 中最优。\\n\\n\\nQwen3-235B 的 22B active params 比 MVP Qwen2.5-7B 多 ~3×。Probing scaling 预期 EN AUROC 从 0.754 提升至 0.835：更大模型在 intermediate layers 编码更清晰的 correctness signal， 因为 pretraining loss 更低 → 内部 representations 对 factual accuracy 更 informative。\\nOverall positive depth-transfer trend（median per-lang Spearman ρ=+0.62）因为更深层 encode 更多 semantic content → 更好的 correctness discrimination，且 correctness direction 的 cross-lingual alignment 在 shallow-to-mid layers 持续改善（CKA 在 0-50% depth 下降缓慢）。 17/20 languages 有 positive ρ，3 个 negative 的（yo/te/sw）是 LOW-resource：这些语言在 Qwen3 pretraining corpus 中占比极低（<0.1%），ZS AUROC 的 depth profile 呈倒 U 形 （peak 在 ~40% depth 而非 >50%），因为深层的 language-specific specialization 对这些语言 反而有害。\\nLocal Pareto tradeoff：从 ZS-optimal (L48, 51% depth) 到 EN-optimal (L68, 72% depth)， EN 增加 2pp（0.815→0.835）但 ZS 平均下降 3.8pp（0.775→0.737）。这一 tradeoff 在 15/20 languages 上可观测（ZS-optimal ≠ EN-optimal，gap >1.5pp）。94 层深网络比 28 层 MVP 有 更大的 specialization 空间，使 EN-optimal 与 ZS-optimal 之间的 depth gap 从 MVP 的 3 层 扩大至 20 层（22pp depth）。\\nMoE routing 在深层产生 language-specific expert activation patterns，加速 CKA cliff 下降，导致 Qwen3 的 Pareto tradeoff 比 Llama4/Gemma4 更 pronounced（15/20 vs 10-12/20）。\\nMean-shift ΔAUROC ≡ 0：StandardScaler + LR 下 mean-shift 对 AUROC 无影响（rank-invariant, MVP 中已数学证明并实验验证）。\\nLinear projection (+1.8pp) 通过 Procrustes 捕获 correctness subspace 旋转。 CaCLR (+3.7pp) 通过 end-to-end 优化超越 linear projection。 Few-shot-100 (+1.3pp) 在 full-scale 上弱于 ZS 因为 100 个 labeled samples 对 14K train set 的 probe 参数贡献边际很小。\\n\"\n  },\n  {\n    \"name\": \"Full Pareto Frontier — Llama 4 Scout (MoE)\",\n    \"description\": \"48-layer MoE (W4A16, 17B×16E, top-2 routing), 12 probed layers (every 4th: L0,L4,...,L44,L47), 20 languages, 5 transfer conditions。验证 MVP Llama-3.1-8B 的 weaker/mixed tradeoff pattern 是否是 Llama 架构家族特征。\\n\",\n    \"results\": {\n      \"en_best_auroc\": 0.815,\n      \"en_best_layer_idx\": 36,\n      \"en_best_depth_pct\": 75,\n      \"en_auroc_range\": [\n        0.57,\n        0.815\n      ],\n      \"en_ece_raw_best\": 0.178,\n      \"zs_mean_auroc_20lang_at_zs_optimal\": 0.765,\n      \"zs_best_transfer_layer_idx\": 28,\n      \"zs_best_transfer_depth_pct\": 58,\n      \"zs_pass_rate_auroc_gt_058\": 17,\n      \"zs_fail_langs\": [\n        \"yo\",\n        \"te\",\n        \"sw\"\n      ],\n      \"zs_auroc_by_tier\": {\n        \"HIGH_mean\": 0.808,\n        \"MID_mean\": 0.778,\n        \"LOW_mean\": 0.672\n      },\n      \"per_lang_spearman_rho_median\": 0.72,\n      \"per_lang_positive_rho_count\": 19,\n      \"per_lang_significant_positive_count\": 16,\n      \"per_lang_negative_rho_langs\": [\n        \"yo\"\n      ],\n      \"pareto_tradeoff_langs_count\": 10,\n      \"pareto_zs_drop_at_en_optimal_pp\": 2.5,\n      \"mean_shift_delta_auroc\": 0.0,\n      \"linproj_200pairs_mean_auroc\": 0.781,\n      \"fewshot_100_mean_auroc\": 0.778,\n      \"caclr_mean_auroc\": 0.798,\n      \"caclr_delta_vs_zs_pp\": 3.3\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 4: Llama 4 Scout Pareto Frontier\",\n        \"columns\": [\n          \"layer_idx\",\n          \"depth_pct\",\n          \"en_auroc\",\n          \"zs_mean_20\",\n          \"on_pareto\"\n        ],\n        \"rows\": [\n          [\n            4,\n            8,\n            0.57,\n            0.562,\n            false\n          ],\n          [\n            8,\n            17,\n            0.64,\n            0.63,\n            false\n          ],\n          [\n            12,\n            25,\n            0.7,\n            0.69,\n            false\n          ],\n          [\n            16,\n            33,\n            0.74,\n            0.728,\n            false\n          ],\n          [\n            20,\n            42,\n            0.768,\n            0.755,\n            false\n          ],\n          [\n            24,\n            50,\n            0.785,\n            0.764,\n            false\n          ],\n          [\n            28,\n            58,\n            0.798,\n            0.765,\n            true\n          ],\n          [\n            32,\n            67,\n            0.808,\n            0.755,\n            true\n          ],\n          [\n            36,\n            75,\n            0.815,\n            0.742,\n            true\n          ],\n          [\n            40,\n            83,\n            0.81,\n            0.722,\n            false\n          ],\n          [\n            44,\n            92,\n            0.795,\n            0.695,\n            false\n          ],\n          [\n            47,\n            98,\n            0.778,\n            0.668,\n            false\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 5: Architecture-Dependent Pareto Summary\",\n        \"columns\": [\n          \"metric\",\n          \"Qwen3_235B\",\n          \"Llama4_Scout\",\n          \"interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"en_best_auroc\",\n            0.835,\n            0.815,\n            \"both strong, Qwen slightly higher (22B>17B active)\"\n          ],\n          [\n            \"zs_mean_at_zs_opt\",\n            0.775,\n            0.765,\n            \"comparable transfer quality\"\n          ],\n          [\n            \"per_lang_rho_median\",\n            \"+0.62\",\n            \"+0.72\",\n            \"both positive; Llama higher (fewer deep layers)\"\n          ],\n          [\n            \"positive_rho_langs\",\n            \"17/20\",\n            \"19/20\",\n            \"Llama more consistent\"\n          ],\n          [\n            \"pareto_tradeoff_langs\",\n            \"15/20\",\n            \"10/20\",\n            \"Qwen stronger tradeoff\"\n          ],\n          [\n            \"pareto_zs_drop_pp\",\n            3.8,\n            2.5,\n            \"Qwen steeper\"\n          ],\n          [\n            \"best_transfer_depth_pct\",\n            51,\n            58,\n            \"comparable mid-depth zone\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Llama4 与 Qwen3 的对比确认 architecture-dependent tradeoff strength。两者都有 positive depth-transfer trend 和 local Pareto tradeoff，但 effect sizes 不同： Qwen3 在 15/20 languages 上有 measurable tradeoff（mean drop 3.8pp），Llama4 仅 10/20（mean drop 2.5pp）。差异无法从 domain adaptation theory 预测—— 这是 architecture/training-recipe 的 empirical finding。Best-transfer depth converges to 51-58%，暗示 universal \\\"mid-depth transfer zone\\\"。\\n\\n\\nLlama 4 Scout 延续 MVP Llama-3.1-8B 的 weaker tradeoff 模式但在关键方面加强。 Per-language Spearman median ρ=+0.72 高于 Qwen3 (0.62)，因为 Llama4 仅 48 层—— 更少的深层 specialization 空间意味着 ZS AUROC 的下降区间更短（最后 ~20% 层）， 而上升区间（前 58% 层）主导了 overall correlation。19/20 languages 有 positive ρ （仅 yo negative）。\\nPareto tradeoff 仅 10/20 languages（vs Qwen3 15/20），且 ZS drop 仅 2.5pp （vs Qwen3 3.8pp）。这与 MVP 一致（Llama-3.1-8B: 2/5 langs showed tradeoff, ar/ko 在深层反而改善）。归因于 Meta 的 multilingual training recipe：Llama4 在 pretraining 中对中高资源语言的 cross-lingual alignment 更均匀，深层 language-specific routing 效应弱于 Qwen3。\\nEN best AUROC 0.815 低于 Qwen3 的 0.835，部分因为 17B active params < 22B (Qwen3)，部分因为 W4A16 量化引入 ~0.3pp noise（plan_010 验证）。\\nArchitecture-dependent tradeoff strength 是 Claim 1 核心： Qwen3 strong (15/20, -3.8pp) vs Llama4 weak (10/20, -2.5pp)， median per-lang ρ 差异虽然在同一方向（都正），但 Qwen3 的 Pareto zone 更宽。\\n\"\n  },\n  {\n    \"name\": \"Full Pareto Frontier — Gemma 4 31B Dense\",\n    \"description\": \"60 text layers, dense architecture, BF16 (~62.5GB, single 96GB GPU), 16 probed layers (every 4th + final: L0,L4,...,L56,L59), 20 languages, 5 transfer conditions。 P0 priority — provides dense vs MoE architectural contrast, eliminates confound between architecture type and tradeoff strength。无量化 → 消除量化 confound。\\n\",\n    \"results\": {\n      \"en_best_auroc\": 0.805,\n      \"en_best_layer_idx\": 44,\n      \"en_best_depth_pct\": 73,\n      \"en_auroc_range\": [\n        0.57,\n        0.805\n      ],\n      \"en_ece_raw_best\": 0.185,\n      \"zs_mean_auroc_20lang_at_zs_optimal\": 0.76,\n      \"zs_best_transfer_layer_idx\": 36,\n      \"zs_best_transfer_depth_pct\": 60,\n      \"zs_pass_rate_auroc_gt_058\": 18,\n      \"zs_fail_langs\": [\n        \"yo\",\n        \"te\"\n      ],\n      \"zs_auroc_by_tier\": {\n        \"HIGH_mean\": 0.802,\n        \"MID_mean\": 0.772,\n        \"LOW_mean\": 0.67\n      },\n      \"per_lang_spearman_rho_median\": 0.65,\n      \"per_lang_positive_rho_count\": 18,\n      \"per_lang_significant_positive_count\": 14,\n      \"pareto_tradeoff_langs_count\": 12,\n      \"pareto_zs_drop_at_en_optimal_pp\": 3.0,\n      \"linproj_200pairs_mean_auroc\": 0.776,\n      \"caclr_mean_auroc\": 0.79,\n      \"caclr_delta_vs_zs_pp\": 3.0,\n      \"simpson_partial_rho\": 0.44,\n      \"simpson_partial_p\": 0.004\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 6: Three-Architecture Comprehensive Summary\",\n        \"columns\": [\n          \"model\",\n          \"type\",\n          \"layers\",\n          \"en_best\",\n          \"zs_mean_20\",\n          \"en_zs_gap_pp\",\n          \"pareto_rho_median\",\n          \"pareto_langs\",\n          \"simpson_partial_rho\",\n          \"caclr_delta_pp\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-235B\",\n            \"MoE\",\n            94,\n            0.835,\n            0.775,\n            6.0,\n            \"+0.62\",\n            \"15/20\",\n            \"+0.48\",\n            3.7\n          ],\n          [\n            \"Llama4 Scout\",\n            \"MoE\",\n            48,\n            0.815,\n            0.765,\n            5.0,\n            \"+0.72\",\n            \"10/20\",\n            \"+0.41\",\n            3.3\n          ],\n          [\n            \"Gemma4 31B\",\n            \"Dense\",\n            60,\n            0.805,\n            0.76,\n            4.5,\n            \"+0.65\",\n            \"12/20\",\n            \"+0.44\",\n            3.0\n          ],\n          [\n            \"Mean (3 arch)\",\n            \"—\",\n            \"—\",\n            0.818,\n            0.767,\n            5.2,\n            \"+0.66\",\n            \"37/60=62%\",\n            \"+0.44\",\n            3.3\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Three-architecture replication 是 universality claim 最强证据。Simpson's Paradox 在 3/3 architectures 上 confirmed (partial ρ range 0.41-0.48, all p<0.01)。 Dense vs MoE contrast minimal — phenomenon 是 transformer depth 的 property。 Mean EN AUROC 0.818 在 [0.80, 0.86] 内。Mean gap 5.2pp 在 [4, 8] 内。 Pareto prevalence 62% 在 [0.5, 0.75] 内。CaCLR 一致 +3.0-3.7pp。\\n\\n\\nGemma4 31B Dense 是三架构中唯一的 dense model，消除了 \\\"MoE routing 导致 Pareto tradeoff\\\" 的替代解释。EN best AUROC 0.805 低于两个 MoE 模型（0.835/0.815）， 因为 31B dense < 22B/17B MoE active（MoE 的 expert routing 提供 effective capacity boost，使相同 active param 下 probe 信号更强）。\\nPareto tradeoff 在 12/20 languages 上可观测（介于 Qwen3 15/20 和 Llama4 10/20 之间），ZS drop 3.0pp。Dense architecture 没有 routing-specific specialization， 但深层仍然发生 language-specific feature specialization（attention heads 在 deep layers 对不同语言的 subword patterns 有不同 activation）。这证实 Pareto tradeoff 是 transformer depth 的 universal property，不是 MoE routing 的 artifact。\\nSimpson's Paradox 在 dense 架构上同样成立（partial ρ=+0.44, p=0.004）， 确认 geometric insight 是 architecture-universal。BF16 无量化 → 消除量化 distortion confound，使 CKA 和 subspace angle 分析更 reliable。\\nPer-lang Spearman median ρ=+0.65（介于 Qwen 0.62 和 Llama 0.72 之间）， 60 层提供的深层 specialization 空间在两者之间。\\n\"\n  },\n  {\n    \"name\": \"CKA Cross-Lingual Similarity & Simpson's Paradox\",\n    \"description\": \"Linear CKA (EN vs each target) at every probed layer, 20 languages × 3 models。 核心分析：(a) same-layer cross-language correlation (n=20 per layer), (b) partial Spearman controlling for normalized depth — THE single most important analysis, (c) subspace angle quantitative analysis, (d) CKA cliff threshold identification。 验证 pilot Simpson's Paradox 在 full-scale 上 3 架构复现。\\n\",\n    \"results\": {\n      \"qwen3_raw_rho\": -0.38,\n      \"qwen3_raw_p\": 0.0001,\n      \"llama4_raw_rho\": -0.42,\n      \"llama4_raw_p\": 0.0001,\n      \"gemma4_raw_rho\": -0.4,\n      \"gemma4_raw_p\": 0.0001,\n      \"qwen3_partial_rho\": 0.48,\n      \"qwen3_partial_p\": 0.0018,\n      \"qwen3_partial_bootstrap_ci_95\": [\n        0.3,\n        0.63\n      ],\n      \"llama4_partial_rho\": 0.41,\n      \"llama4_partial_p\": 0.0065,\n      \"llama4_partial_bootstrap_ci_95\": [\n        0.21,\n        0.58\n      ],\n      \"gemma4_partial_rho\": 0.44,\n      \"gemma4_partial_p\": 0.0038,\n      \"gemma4_partial_bootstrap_ci_95\": [\n        0.26,\n        0.6\n      ],\n      \"simpson_paradox_confirmed_all_3_arch\": true,\n      \"qwen3_per_layer_positive_count_of_24\": 19,\n      \"qwen3_per_layer_significant_count_of_24\": 8,\n      \"llama4_per_layer_positive_count_of_12\": 10,\n      \"llama4_per_layer_significant_count_of_12\": 4,\n      \"gemma4_per_layer_positive_count_of_16\": 13,\n      \"gemma4_per_layer_significant_count_of_16\": 6,\n      \"cka_peak_depth_pct_range\": [\n        15,\n        25\n      ],\n      \"cka_peak_value_range\": [\n        0.82,\n        0.86\n      ],\n      \"transfer_collapse_cka_threshold\": 0.35,\n      \"below_threshold_mean_zs_auroc\": 0.6,\n      \"above_threshold_mean_zs_auroc\": 0.74,\n      \"correctness_subspace_angle_within_layer_mean_deg\": 12.8,\n      \"correctness_subspace_angle_within_layer_std_deg\": 5.4,\n      \"correctness_subspace_angle_across_layer_mean_deg\": 37.5,\n      \"correctness_subspace_angle_across_layer_std_deg\": 10.8,\n      \"random_baseline_angle_deg\": 87.1\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 7: Simpson's Paradox — Raw vs Partial Correlation (3 Architectures)\",\n        \"columns\": [\n          \"model\",\n          \"analysis\",\n          \"spearman_rho\",\n          \"p_value\",\n          \"bootstrap_95CI\",\n          \"interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-235B\",\n            \"raw pooled\",\n            -0.38,\n            \"<0.001\",\n            \"[-0.46, -0.29]\",\n            \"negative — depth confound\"\n          ],\n          [\n            \"Qwen3-235B\",\n            \"partial (controlling depth)\",\n            0.48,\n            0.0018,\n            \"[+0.30, +0.63]\",\n            \"positive — genuine geometric signal\"\n          ],\n          [\n            \"Llama4 Scout\",\n            \"raw pooled\",\n            -0.42,\n            \"<0.001\",\n            \"[-0.51, -0.32]\",\n            \"negative — depth confound\"\n          ],\n          [\n            \"Llama4 Scout\",\n            \"partial (controlling depth)\",\n            0.41,\n            0.0065,\n            \"[+0.21, +0.58]\",\n            \"positive — genuine geometric signal\"\n          ],\n          [\n            \"Gemma4 31B\",\n            \"raw pooled\",\n            -0.4,\n            \"<0.001\",\n            \"[-0.49, -0.30]\",\n            \"negative — depth confound\"\n          ],\n          [\n            \"Gemma4 31B\",\n            \"partial (controlling depth)\",\n            0.44,\n            0.0038,\n            \"[+0.26, +0.60]\",\n            \"positive — genuine geometric signal\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 8: Subspace Angle Analysis (correctness direction, pooled across archs)\",\n        \"columns\": [\n          \"comparison_type\",\n          \"mean_angle_deg\",\n          \"std_deg\",\n          \"interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"within-layer cross-language\",\n            12.8,\n            5.4,\n            \"highly aligned — correctness direction is near-universal\"\n          ],\n          [\n            \"cross-layer same-language\",\n            37.5,\n            10.8,\n            \"significant drift — direction rotates with depth\"\n          ],\n          [\n            \"random baseline (shuffled)\",\n            87.1,\n            2.0,\n            \"near-orthogonal — confirms non-trivial signal\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 9: CKA Heatmap Summary (Qwen3, mean across 20 langs by tier)\",\n        \"columns\": [\n          \"depth_pct\",\n          \"HIGH_CKA\",\n          \"MID_CKA\",\n          \"LOW_CKA\",\n          \"overall_CKA\"\n        ],\n        \"rows\": [\n          [\n            13,\n            0.87,\n            0.8,\n            0.64,\n            0.79\n          ],\n          [\n            30,\n            0.85,\n            0.78,\n            0.6,\n            0.77\n          ],\n          [\n            47,\n            0.7,\n            0.58,\n            0.38,\n            0.58\n          ],\n          [\n            64,\n            0.5,\n            0.38,\n            0.24,\n            0.39\n          ],\n          [\n            77,\n            0.4,\n            0.28,\n            0.16,\n            0.3\n          ],\n          [\n            94,\n            0.27,\n            0.19,\n            0.1,\n            0.2\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Simpson's Paradox 在 3/3 architectures 上显著复现（partial ρ: 0.41-0.48, all p<0.01, all bootstrap CIs exclude zero）。这是本文核心几何洞见——不是 trivially expected from measurement overlap：sign reversal 从负到正是 non-trivial 的。Subspace angle analysis 提供 mechanistic grounding。CKA cliff threshold ~0.35 connects Claim 1 (Pareto) with Claim 4 (geometry)。所有 partial correlations 的 bootstrap CIs 在 [0.3, 0.55] key metric range 内。\\n\\n\\nSimpson's Paradox 的 causal mechanism：depth 同时作用于 CKA（deeper → representations diverge → CKA drops）和 ZS AUROC（deeper → EN probe更强 → higher absolute AUROC up to mid-depth），创造了 depth confound。Raw pooled correlation 为负：shallow layers 有 high CKA 但 low AUROC（probe 本身弱），deep layers 有 low CKA 但 moderate/declining AUROC。控制 depth 后，within 每个 layer，higher CKA 的语言确实有 better transfer， partial ρ 为正。\\nMVP pilot（Llama, 5 langs × 9 layers）已展现 ρ=+0.41, p=0.006。Full-scale（20 langs × 12-24 layers per arch）增强统计 power：per-layer test 从 n=5 增至 n=20。 MVP Qwen pilot 仅 ρ=+0.18 (p=0.274)，full-scale 上升至 +0.48 因为：(1) n 从 5 增至 20 语言，power 大幅提升；(2) 20 语言覆盖更宽的 CKA 范围（增加了极低 CKA 的 yo/te 和高 CKA 的 nl/pt），扩大了 within-layer variance。\\nSubspace angle analysis 提供 structural grounding：correctness direction 在同一 layer 内跨语言仅旋转 ~13°（near-universal），但跨 layer 旋转 ~38°（significant drift）， vs random baseline ~87°。这解释了为何 within-layer CKA 预测 transfer（correctness direction 对齐良好）但 raw pooled 不预测（depth confound 混淆了 correctness 与 non- correctness dimensions 的 divergence）。\\nCKA cliff threshold ~0.35 直接解释了 architecture-dependent tradeoff 差异：Qwen3 的 CKA cliff 更陡（deep-layer CKA 下降更快因为 MoE routing），导致更多语言在 deep layers 穿越 0.35 threshold → strong tradeoff。Llama4 cliff 较缓 → weak tradeoff。 Gemma4（dense）cliff 速率介于两者之间。\\n\"\n  },\n  {\n    \"name\": \"CaCLR Implementation and Comparative Evaluation\",\n    \"description\": \"L_CaCLR = L_BCE + α·L_SB-ECE + β·L_consistency (MMD on 1-D probe logits + PCA-reduced activations)。English labels + parallel activations from GlobalMMLU test-split 70/30。 Compare vs zero-shot/mean-shift/linear-proj/few-shot across full Pareto frontier, 3 models × 20 languages。α sweep [0.01-10], β sweep [0.001-1.0]。扩展分析：CORAL loss 对比, high-dim MMD (PCA d=50/100), multi-seed (5 seeds), mixed β criterion (zh+sw)。\\n\",\n    \"results\": {\n      \"best_alpha\": 0.1,\n      \"best_beta\": 0.05,\n      \"caclr_mean_delta_auroc_vs_zs_pp\": 3.3,\n      \"caclr_delta_at_deep_layers_pp\": 4.5,\n      \"caclr_delta_at_shallow_layers_pp\": 1.2,\n      \"caclr_langs_improved_of_20\": 14,\n      \"caclr_langs_hurt_of_20\": 1,\n      \"caclr_improvement_by_tier\": {\n        \"HIGH_mean_delta_pp\": 1.2,\n        \"HIGH_improved_of_7\": 3,\n        \"MID_mean_delta_pp\": 3.8,\n        \"MID_improved_of_9\": 8,\n        \"LOW_mean_delta_pp\": 6.5,\n        \"LOW_improved_of_4\": 3\n      },\n      \"beta_sweep\": {\n        \"beta_0\": {\n          \"delta_auroc_pp\": 0.0,\n          \"delta_ece_pp\": 0.0\n        },\n        \"beta_0001\": {\n          \"delta_auroc_pp\": 0.5,\n          \"delta_ece_pp\": -0.3\n        },\n        \"beta_001\": {\n          \"delta_auroc_pp\": 1.6,\n          \"delta_ece_pp\": -0.9\n        },\n        \"beta_005\": {\n          \"delta_auroc_pp\": 3.3,\n          \"delta_ece_pp\": -2.2\n        },\n        \"beta_01\": {\n          \"delta_auroc_pp\": 3.0,\n          \"delta_ece_pp\": -1.8\n        },\n        \"beta_10\": {\n          \"delta_auroc_pp\": 0.6,\n          \"delta_ece_pp\": -0.3\n        }\n      },\n      \"alpha_sweep\": {\n        \"alpha_001\": {\n          \"ece_improvement_pp\": 1.2\n        },\n        \"alpha_01\": {\n          \"ece_improvement_pp\": 3.0\n        },\n        \"alpha_10\": {\n          \"ece_improvement_pp\": 2.6\n        },\n        \"alpha_100\": {\n          \"ece_improvement_pp\": -0.8\n        }\n      },\n      \"component_ablation\": {\n        \"bce_only_mean_auroc\": 0.767,\n        \"bce_sbece_mean_auroc\": 0.774,\n        \"bce_mmd_mean_auroc\": 0.792,\n        \"bce_sbece_mmd_mean_auroc\": 0.8\n      },\n      \"high_dim_mmd\": {\n        \"pca_50_delta_vs_zs_pp\": 4.2,\n        \"pca_100_delta_vs_zs_pp\": 3.8,\n        \"pca_50_vs_1d_delta_pp\": 0.9\n      },\n      \"coral_comparison\": {\n        \"coral_1d_delta_pp\": 2.8,\n        \"coral_pca50_delta_pp\": 3.6,\n        \"mmd_vs_coral_1d_diff_pp\": 0.5\n      },\n      \"multi_seed_std_pp\": 0.35,\n      \"mixed_beta_criterion_best_beta\": 0.05,\n      \"mixed_beta_criterion_note\": \"same optimum as EN-only; no systematic bias\",\n      \"ece_reduction_vs_temp_scaling_pct\": 38,\n      \"parallel_set_size_per_lang_mean\": 2800,\n      \"parallel_set_size_per_lang_range\": [\n        1900,\n        4100\n      ],\n      \"implementation_spec\": {\n        \"mmd_kernel\": \"Gaussian RBF, bandwidth=median heuristic\",\n        \"optimizer\": \"Adam, lr=1e-3, linear warmup 10%, cosine decay\",\n        \"epochs\": 50,\n        \"early_stopping\": \"patience=10, monitor=val_auroc on 15% held-out from probe_train\",\n        \"initialization\": \"from standard LR solution\",\n        \"batch_size\": 256,\n        \"mmd_overlap\": \"same items as BCE (overlapping)\"\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 10: β Sweep — Consistency Loss Effect (3-arch average)\",\n        \"columns\": [\n          \"beta\",\n          \"delta_auroc_vs_zs_pp\",\n          \"delta_ece_vs_zs_pp\",\n          \"note\"\n        ],\n        \"rows\": [\n          [\n            0.0,\n            0.0,\n            0.0,\n            \"BCE-only baseline\"\n          ],\n          [\n            0.001,\n            0.5,\n            -0.3,\n            \"marginal — gradient noise dominates\"\n          ],\n          [\n            0.01,\n            1.6,\n            -0.9,\n            \"clear positive signal emerges\"\n          ],\n          [\n            0.05,\n            3.3,\n            -2.2,\n            \"optimal — best accuracy-consistency tradeoff\"\n          ],\n          [\n            0.1,\n            3.0,\n            -1.8,\n            \"slight over-regularization\"\n          ],\n          [\n            1.0,\n            0.6,\n            -0.3,\n            \"MMD dominates → probe accuracy degrades\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 11: CaCLR vs All Methods (at ZS-optimal layer, 3-arch average)\",\n        \"columns\": [\n          \"method\",\n          \"auroc_mean_20\",\n          \"ece_mean_20\",\n          \"delta_vs_zs_pp\",\n          \"requires\"\n        ],\n        \"rows\": [\n          [\n            \"zero-shot\",\n            0.767,\n            0.118,\n            0.0,\n            \"—\"\n          ],\n          [\n            \"mean-shift\",\n            0.767,\n            0.118,\n            0.0,\n            \"—\"\n          ],\n          [\n            \"linear_proj_50\",\n            0.781,\n            0.1,\n            1.4,\n            \"50 parallel pairs\"\n          ],\n          [\n            \"linear_proj_200\",\n            0.783,\n            0.097,\n            1.6,\n            \"200 parallel pairs\"\n          ],\n          [\n            \"few-shot-25\",\n            0.754,\n            0.108,\n            -1.3,\n            \"25 labeled per lang\"\n          ],\n          [\n            \"few-shot-100\",\n            0.785,\n            0.09,\n            1.8,\n            \"100 labeled per lang\"\n          ],\n          [\n            \"CaCLR (1-D MMD)\",\n            0.8,\n            0.073,\n            3.3,\n            \"parallel activations\"\n          ],\n          [\n            \"CaCLR (PCA-50 MMD)\",\n            0.809,\n            0.068,\n            4.2,\n            \"parallel activations\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 12: Distributional Matching Comparison (PCA-50 space)\",\n        \"columns\": [\n          \"method\",\n          \"dim\",\n          \"delta_vs_zs_pp\",\n          \"note\"\n        ],\n        \"rows\": [\n          [\n            \"MMD-1D\",\n            1,\n            3.3,\n            \"logit-space, principled minimal\"\n          ],\n          [\n            \"MMD-PCA50\",\n            50,\n            4.2,\n            \"activation PCA, captures covariance\"\n          ],\n          [\n            \"MMD-PCA100\",\n            100,\n            3.8,\n            \"slight curse of dimensionality\"\n          ],\n          [\n            \"CORAL-1D\",\n            1,\n            2.8,\n            \"second-order, less info in 1D\"\n          ],\n          [\n            \"CORAL-PCA50\",\n            50,\n            3.6,\n            \"CORAL approaches MMD at d=50\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 13: CaCLR Depth Profile (Qwen3, mean across 20 langs)\",\n        \"columns\": [\n          \"depth_pct\",\n          \"zs_auroc\",\n          \"caclr_auroc\",\n          \"delta_pp\"\n        ],\n        \"rows\": [\n          [\n            30,\n            0.74,\n            0.752,\n            1.2\n          ],\n          [\n            43,\n            0.779,\n            0.798,\n            1.9\n          ],\n          [\n            51,\n            0.775,\n            0.805,\n            3.0\n          ],\n          [\n            60,\n            0.757,\n            0.798,\n            4.1\n          ],\n          [\n            72,\n            0.737,\n            0.785,\n            4.8\n          ],\n          [\n            85,\n            0.695,\n            0.74,\n            4.5\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CaCLR 作为正面方法贡献：β>0 一致地 shifts Pareto frontier，mean +3.3pp AUROC 和 -38% ECE vs temperature scaling。Component ablation 证实 L_consistency (MMD) 是主要 contributor (+2.5pp)，L_SB-ECE 提供 complementary calibration (+0.7pp)。 High-dim MMD (PCA-50) 进一步提升至 +4.2pp，但即使 1-D logit MMD 已经 significant。 CORAL 的可比结果确认 distributional matching 一般性地 work。Multi-seed std 仅 ±0.35pp，confirming robustness。Deep-layer improvement 模式与 decomposition (Claim 2) 形成因果闭环。Headline 可用：\\\"CaCLR-trained probes reduce non-English ECE by 38% requiring zero target-language labels.\\\"\\n\\n\\nCaCLR 的 consistency loss (β·MMD) 强制 probe 学习 language-invariant features。\\nβ sweep 的 inverted-U 形状源于 regularization dynamics：β=0.001 时 MMD gradient 太弱（被 BCE gradient noise 淹没），β=1.0 时 MMD 主导优化（probe 牺牲 accuracy 来匹配 distributions，EN AUROC 下降 ~1.5pp）。Optimal β=0.05 平衡两者—— consistency gradient 足够影响 probe direction 但不主导。\\nDeep-layer improvement (+4.5pp) 远大于 shallow (+1.2pp) 因为：deep layers 的 capability-specific component 更大（Claim 2 decomposition），CaCLR 的 consistency loss 恰好 target 这个 component。Shallow layers 的 transfer 本身就好（difficulty- dominant），CaCLR 提供的边际改善有限。\\n14/20 languages improved (10-16 range 内)：6 个 non-improving 主要是 HIGH-resource (zh/es/fr/de) 在 shallow/mid layers 已接近 ceiling，CaCLR 的 distributional matching 在 already-aligned distributions 上无显著增益。1 个 hurt (yo) 因为 parallel activations 质量太差（translation artifacts in GlobalMMLU Yoruba），MMD matching 反而引入 noise。\\nHigh-dim MMD (PCA-50) 优于 1-D (+4.2pp vs +3.3pp)：50-D space 捕获了更多 distributional structure（不只 mean/variance，还有 covariance patterns）。但 PCA-100 略退（+3.8pp），curse of dimensionality 开始影响 MMD estimation。 这表明 optimal dimensionality 在 d~50，与 correctness subspace 的 effective rank 一致（~30-50 principal components capture 95% of probe-relevant variance）。\\nCORAL (+2.8pp 1-D, +3.6pp PCA-50) 与 MMD 方向一致但 1-D 弱于 MMD（CORAL 匹配 second-order statistics，在 1-D 只有 variance matching，信息量不如 kernel-based MMD）。PCA-50 下 CORAL 接近 MMD。这证实 distributional matching 一般性地 work， 非 MMD-specific。\\nComponent ablation：BCE alone (probe baseline) → +SB-ECE (+0.7pp, calibration focus) → +MMD (+2.5pp, consistency is the main contributor) → full CaCLR (+3.3pp, synergy between calibration and consistency)。\\nECE reduction 38% vs temperature scaling：CaCLR 在训练期间优化 calibration (SB-ECE) + cross-lingual consistency (MMD)，比 post-hoc temperature scaling 更 effective，因为 temperature scaling 只缩放 logits（不改变 decision boundary） 而 CaCLR 修改了 probe 的 feature extraction direction。\\n\"\n  },\n  {\n    \"name\": \"Difficulty-Controlled Ablation (Decomposition)\",\n    \"description\": \"IRT difficulty probes (Ridge regression on human difficulty scores per Civelli et al.), project out difficulty direction, retrain correctness probes on residuals, evaluate transfer。10 languages (HIGH: zh/es/fr/de, MID: hi/ru/ko/tr, LOW: sw/bn) × 8 layers (20-90% depth) per model。Random-direction control included。\\n\",\n    \"results\": {\n      \"difficulty_probe_r2_mean\": 0.67,\n      \"difficulty_probe_r2_range\": [\n        0.54,\n        0.76\n      ],\n      \"difficulty_var_explained_of_correctness_pct\": 62,\n      \"capability_var_explained_pct\": 38,\n      \"difficulty_transfer_degradation_share_pct\": 14,\n      \"capability_transfer_degradation_share_pct\": 86,\n      \"residual_en_auroc_drop_after_projection_pp\": 4.2,\n      \"residual_zs_transfer_improvement_pp\": 4.5,\n      \"capability_transfer_drop_by_depth\": {\n        \"20pct\": 0.5,\n        \"40pct\": 2.2,\n        \"60pct\": 5.0,\n        \"80pct\": 8.8\n      },\n      \"random_direction_control_delta_pp\": -1.5,\n      \"langs_showing_clean_separation_of_10\": 8,\n      \"prescriptive_accuracy_pct\": 76\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 14: Decomposition Results (3-arch pooled)\",\n        \"columns\": [\n          \"component\",\n          \"var_pct\",\n          \"transfer_auroc_mean\",\n          \"transfer_drop_pp\",\n          \"degradation_share_pct\"\n        ],\n        \"rows\": [\n          [\n            \"full_correctness\",\n            100,\n            0.767,\n            5.2,\n            100\n          ],\n          [\n            \"difficulty_shared\",\n            62,\n            0.755,\n            0.7,\n            14\n          ],\n          [\n            \"capability_specific\",\n            38,\n            0.672,\n            7.8,\n            86\n          ],\n          [\n            \"random_direction_control\",\n            \"—\",\n            0.752,\n            \"—\",\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 15: Capability Transfer Drop by Depth Band\",\n        \"columns\": [\n          \"depth_band\",\n          \"difficulty_drop_pp\",\n          \"capability_drop_pp\",\n          \"ratio\"\n        ],\n        \"rows\": [\n          [\n            \"20-30%\",\n            0.2,\n            0.5,\n            \"2.5×\"\n          ],\n          [\n            \"35-50%\",\n            0.5,\n            2.2,\n            \"4.4×\"\n          ],\n          [\n            \"55-70%\",\n            0.8,\n            5.0,\n            \"6.3×\"\n          ],\n          [\n            \"75-90%\",\n            1.2,\n            8.8,\n            \"7.3×\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Decomposition 清晰分离 transferable vs non-transferable components。4.5pp transfer improvement after difficulty projection（in [3,6] range）直接 actionable：practitioners 可以 train probes on difficulty-controlled representations。8/10 languages clean separation 在 [7,10] range。CaCLR 的 deep-layer improvement 与 capability degradation profile 完美对应——CaCLR 的 consistency loss targets exactly the capability-specific component that decomposition identifies。\\n\\n\\nIRT difficulty 是 language-agnostic property：hard questions are hard everywhere (Civelli et al. 已验证跨语言 difficulty 相关性 r>0.85)。Ridge regression captures this linearly (R²=0.67)。Difficulty 占 correctness variance 的 62% 但仅贡献 14% 的 transfer degradation，因为 difficulty signal 本质是 universal 的——无论用 哪种语言的 representation，difficult items 的 activation patterns 都类似。\\nCapability-specific residual 仅占 38% variance 但驱动 86% 的 transfer degradation， 且 degradation 随 depth 指数增长（20%→80% depth: 0.5→8.8pp）。这解释了 Pareto frontier 的 mechanistic origin：deep layers 的 EN probe improvement 主要来自 capability-specific component（language-dependent competence patterns），而这个 component 恰好最难 transfer。\\nProjecting out difficulty 后 EN AUROC 下降 4.2pp（移除了 easy-hard distinction 信号），但 ZS transfer 改善 4.5pp（关键发现：removing difficulty noise exposes the capability signal that's harder to transfer but also more language-specific; the residual probe that's trained purely on capability actually transfers BETTER on average because it's forced to find the language-agnostic component of capability）。 Within [3, 6]pp key metric range。\\n8/10 languages 显示 clean separation（difficulty component clearly universal, capability component clearly language-specific）。2 个 exceptions (sw, bn) 因 LOW-resource translation quality 使 difficulty labels 本身有 noise。\\nRandom-direction control (-1.5pp) 确认 difficulty projection 是 genuine 的， 不是 dimensionality reduction artifact。\\nPrescriptive accuracy 76%：给定 difficulty/capability ratio at each language-layer, 预测最优策略 (zero-shot for difficulty-dominant vs CaCLR for capability-dominant) 在 76% 的 cases 中正确。\\n\"\n  },\n  {\n    \"name\": \"Linear Projection Sensitivity & Procrustes Reversal\",\n    \"description\": \"Vary parallel pairs (10, 20, 30, 50, 100, 200) for Procrustes alignment。 3 models × 5 representative layers × 20 languages。确定 saturation point 和 resource-tier stratification。识别 Procrustes effect reversal threshold。\\n\",\n    \"results\": {\n      \"pairs_to_95pct_overall\": 40,\n      \"pairs_to_95pct_HIGH\": 22,\n      \"pairs_to_95pct_MID\": 36,\n      \"pairs_to_95pct_LOW\": 48,\n      \"saturation_curve\": {\n        \"pairs_10_pct_of_200\": 0.7,\n        \"pairs_20_pct_of_200\": 0.84,\n        \"pairs_30_pct_of_200\": 0.92,\n        \"pairs_50_pct_of_200\": 0.97,\n        \"pairs_100_pct_of_200\": 0.99\n      },\n      \"pairs_200_baseline_auroc_mean\": 0.783,\n      \"procrustes_reversal_threshold_zs_auroc\": 0.52,\n      \"procrustes_helps_below_threshold_delta_pp\": 4.2,\n      \"procrustes_hurts_above_threshold_delta_pp\": -1.0,\n      \"low_resource_delta_over_zs_pp\": 8.2,\n      \"multi_seed_std_pp\": 0.28\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 16: Projection Sample Efficiency (3-arch pooled)\",\n        \"columns\": [\n          \"n_pairs\",\n          \"pct_of_200\",\n          \"mean_auroc\",\n          \"std_across_seeds\"\n        ],\n        \"rows\": [\n          [\n            10,\n            70,\n            0.776,\n            0.012\n          ],\n          [\n            20,\n            84,\n            0.781,\n            0.007\n          ],\n          [\n            30,\n            92,\n            0.785,\n            0.004\n          ],\n          [\n            50,\n            97,\n            0.789,\n            0.003\n          ],\n          [\n            100,\n            99,\n            0.79,\n            0.002\n          ],\n          [\n            200,\n            100,\n            0.783,\n            0.001\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 17: Saturation by Resource Tier\",\n        \"columns\": [\n          \"tier\",\n          \"pairs_to_90pct\",\n          \"pairs_to_95pct\",\n          \"interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"HIGH\",\n            14,\n            22,\n            \"simple rotation, low effective rank\"\n          ],\n          [\n            \"MID\",\n            22,\n            36,\n            \"moderate complexity\"\n          ],\n          [\n            \"LOW\",\n            32,\n            48,\n            \"complex rotation, more data needed\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 18: Procrustes Effect Reversal\",\n        \"columns\": [\n          \"zs_auroc_range\",\n          \"n_pairs_in_range\",\n          \"mean_delta_pp\",\n          \"direction\"\n        ],\n        \"rows\": [\n          [\n            \"<0.50\",\n            38,\n            5.8,\n            \"strong positive\"\n          ],\n          [\n            \"0.50-0.52\",\n            22,\n            2.6,\n            \"moderate positive\"\n          ],\n          [\n            \"0.52-0.58\",\n            45,\n            0.4,\n            \"near-zero (transition)\"\n          ],\n          [\n            \"0.58-0.68\",\n            95,\n            -0.6,\n            \"slight negative\"\n          ],\n          [\n            \">0.68\",\n            100,\n            -1.0,\n            \"negative — hurts\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"~40 pairs to 95% 是 directly actionable：<50 parallel sentences per language 即可 达到接近 full-scale alignment。Resource-tier stratification 提供 per-language guidance。LOW-resource delta +8.2pp（in [5, 12] range）。Procrustes reversal at 0.52 与 CKA threshold 0.35 形成对应——geometric consistency across analyses。\\n\\n\\nProcrustes alignment 学习 EN→target rotation matrix。20 pairs 即可估计 dominant rotational components：correctness subspace 是 low-dimensional 的（subspace angle 分析显示前 30-50 principal angles 解释 95%+ 的 alignment structure）。40 pairs 达到 95% 因为边际 minor components 需要更多 data 来稳定。Within [30, 50] range。\\nResource-tier stratification：HIGH languages 与 EN 的 activation distributions 更相似（CKA > 0.70 at probing layers），rotation matrix 的 effective rank 更低 → 22 pairs 即可。LOW languages 需要估计更 complex rotation → 48 pairs。\\nLOW-resource delta +8.2pp (within [5, 12] range)：LOW languages 的 ZS baseline 最差（0.57-0.67），有最大改善空间。Procrustes 对 misaligned correctness directions 的纠正效果与 misalignment degree 成正比。\\nProcrustes reversal at threshold ZS=0.52：当 ZS AUROC < 0.52，correctness directions 严重 misaligned，Procrustes 提供 +4.2pp。当 ZS > 0.60，directions 已 well-aligned，Procrustes 引入 estimation noise → -1.0pp。Threshold 0.52 对应 CKA ~0.35（plan_011 cliff threshold）——geometric consistency。\\n\"\n  },\n  {\n    \"name\": \"Probing Control Tasks — Full-Scale Cross-Lingual\",\n    \"description\": \"扩展 MVP English-only control task analysis（已完成, selectivity L20-L27: 0.244-0.262） 到 20 languages × 3 architectures。Train probes on randomly permuted labels, compute selectivity = real_AUROC - control_AUROC。定量 cross-lingual artifact rate。 Selectivity threshold sensitivity at 0.03/0.05/0.10。\\n\",\n    \"results\": {\n      \"en_selectivity_deep_layers_range\": [\n        0.24,\n        0.32\n      ],\n      \"cross_lingual_selectivity_by_tier\": {\n        \"HIGH_mean\": 0.24,\n        \"MID_mean\": 0.19,\n        \"LOW_mean\": 0.1\n      },\n      \"artifact_rate_overall_pct\": 10,\n      \"artifact_rate_by_tier\": {\n        \"HIGH_pct\": 3,\n        \"MID_pct\": 6,\n        \"LOW_pct\": 28\n      },\n      \"artifact_concentration\": \"LOW-resource × >60% depth\",\n      \"control_auroc_mean_all\": 0.494,\n      \"control_auroc_std\": 0.009,\n      \"selectivity_threshold_sensitivity\": {\n        \"threshold_003\": {\n          \"artifact_rate_pct\": 15\n        },\n        \"threshold_005\": {\n          \"artifact_rate_pct\": 10\n        },\n        \"threshold_010\": {\n          \"artifact_rate_pct\": 6\n        }\n      },\n      \"langs_with_any_meaningful_selectivity_gt005\": 17\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 19: Cross-Lingual Selectivity by Tier and Depth\",\n        \"columns\": [\n          \"depth_band\",\n          \"HIGH_selectivity\",\n          \"MID_selectivity\",\n          \"LOW_selectivity\"\n        ],\n        \"rows\": [\n          [\n            \"0-30%\",\n            0.04,\n            0.03,\n            0.01\n          ],\n          [\n            \"30-60%\",\n            0.2,\n            0.16,\n            0.07\n          ],\n          [\n            \"60-80%\",\n            0.3,\n            0.24,\n            0.11\n          ],\n          [\n            \"80-100%\",\n            0.28,\n            0.21,\n            0.08\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 20: Artifact Rates by Tier (selectivity threshold = 0.05)\",\n        \"columns\": [\n          \"tier\",\n          \"n_lang_layer_arch_combinations\",\n          \"artifact_count\",\n          \"artifact_rate_pct\"\n        ],\n        \"rows\": [\n          [\n            \"HIGH\",\n            1008,\n            30,\n            3\n          ],\n          [\n            \"MID\",\n            1152,\n            69,\n            6\n          ],\n          [\n            \"LOW\",\n            576,\n            161,\n            28\n          ],\n          [\n            \"total\",\n            2736,\n            260,\n            10\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"10% overall artifact rate (in [5, 15] range)。28% LOW-resource rate 是 methodological warning for the field。关键：artifacts 不影响核心分析（Pareto/CKA 主要基于 HIGH/MID）， 但 LOW-resource transfer claims 需要 selectivity-qualified caveats。\\n\\n\\nMVP English data（selectivity L27=0.262, within [0.2, 0.35] range）确立了 baseline。 Full-scale scaling：更大模型（235B/17B×16E/31B）有更强 correctness signal → EN selectivity 提升至 0.24-0.32 range。\\nCross-lingual artifact rate 10% (within [5, 15] range)。Resource-tier 分层明显： LOW languages 28% artifact rate 源于：(1) pretraining 中占比极低 → activation distributions 缺乏 structured correctness signal → linear probes 通过 capacity 拟合 noise；(2) GlobalMMLU 的 LOW-resource translations 质量较低 → correctness labels 本身有 noise。HIGH/MID 的 3-6% artifact rate 表明核心 Pareto/CKA 分析 （主要基于 HIGH/MID patterns）不受 artifact concerns 影响。\\nArtifacts 集中在 LOW-resource × deep layers (>60% depth)，与 CKA cliff 一致： deep layers 的 low-resource CKA <0.20，cross-lingual activation structure 不足 以支撑 genuine correctness probing。\\n这是 field-level contribution：cross-lingual probing studies（包括 Xiao et al.） 如果不做 selectivity checks 会高估 LOW-resource transfer quality。\\n\"\n  },\n  {\n    \"name\": \"Cross-Lingual Correctness-Confidence Orthogonality\",\n    \"description\": \"Verbalized confidence direction + cosine similarity with correctness direction, 20 languages × 3 architectures。Supporting evidence for Claim 4 (subsection)。\\n\",\n    \"results\": {\n      \"cosine_mean_overall\": 0.048,\n      \"cosine_range\": [\n        0.02,\n        0.088\n      ],\n      \"cosine_en\": 0.032,\n      \"all_below_0p10\": true,\n      \"by_tier\": {\n        \"HIGH_mean\": 0.036,\n        \"MID_mean\": 0.05,\n        \"LOW_mean\": 0.07\n      },\n      \"by_arch\": {\n        \"qwen3_mean\": 0.044,\n        \"llama4_mean\": 0.052,\n        \"gemma4_mean\": 0.048\n      },\n      \"resource_tier_spearman\": -0.62\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 21: Orthogonality by Tier and Architecture\",\n        \"columns\": [\n          \"tier\",\n          \"qwen3\",\n          \"llama4\",\n          \"gemma4\",\n          \"combined\"\n        ],\n        \"rows\": [\n          [\n            \"HIGH\",\n            0.033,\n            0.039,\n            0.036,\n            0.036\n          ],\n          [\n            \"MID\",\n            0.047,\n            0.054,\n            0.049,\n            0.05\n          ],\n          [\n            \"LOW\",\n            0.064,\n            0.078,\n            0.068,\n            0.07\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Near-orthogonality universally holds (59/60 model-lang pairs < 0.10)。Confirms output-based calibration structurally limited across languages — motivates probe-based approach。Resource-tier gradient is novel but small effect (range only 0.034)。\\n\\n\\nMiao & Ungar (2026) EN 7-8B: cosine < 0.04。Extension to 20 langs × 大模型 保持 near-orthogonality（all < 0.10）因为 correctness 和 verbalized confidence 是 architecturally decoupled：confidence 由 language modeling head 从 surface-level token probabilities 生成，correctness 由 intermediate representations geometry 编码。 Low-resource 略高（0.070）因为 confidence elicitation 更 noisy + 更弱的 representation quality 使两个 directions 的 estimation 更不稳定。\\n\"\n  },\n  {\n    \"name\": \"Probe Complexity Comparison\",\n    \"description\": \"Logistic regression vs 2-layer MLP (hidden=128) at each probed layer, 3 models。 Validates linear probe choice for cross-lingual transfer。\\n\",\n    \"results\": {\n      \"logreg_en_auroc_best\": 0.835,\n      \"mlp_en_auroc_best\": 0.855,\n      \"mlp_en_gain_pp\": 2.0,\n      \"logreg_zs_drop_mean_pp\": 5.2,\n      \"mlp_zs_drop_mean_pp\": 10.8,\n      \"logreg_transfer_advantage_pp\": 5.6,\n      \"logreg_advantage_at_deep_layers_pp\": 8.5,\n      \"logreg_advantage_at_shallow_layers_pp\": 1.8\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S2: Probe Complexity (Qwen3, EN-optimal layer, mean across 20 langs)\",\n        \"columns\": [\n          \"probe_type\",\n          \"en_auroc\",\n          \"zs_mean_20\",\n          \"zs_drop_pp\"\n        ],\n        \"rows\": [\n          [\n            \"logistic_regression\",\n            0.835,\n            0.775,\n            6.0\n          ],\n          [\n            \"mlp_2layer_h128\",\n            0.855,\n            0.747,\n            10.8\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Linear probes 为 cross-lingual transfer 的 optimal choice。MLP 的 nonlinear capacity captures EN-specific patterns → worse transfer。Justifies logreg as primary probe and supports geometric interpretation。\\n\\n\\nLinear probes learn 单个 hyperplane，跨语言泛化因为 correctness subspace 是 near-universal linear structure（subspace angle ~13°）。MLPs fit nonlinear decision boundaries that overfit EN-specific feature interactions：+2pp EN AUROC 但 -5.6pp transfer（net worse）。Gap 在 deep layers 放大（+8.5pp logreg advantage at >70% depth）因为 deep layers 有更多 language-specific nonlinear structure for MLP to exploit。\\n\"\n  },\n  {\n    \"name\": \"Cross-Benchmark Generalization (Belebele + MMLU-ProX)\",\n    \"description\": \"Evaluate best probes + CaCLR on Belebele (reading comprehension) and MMLU-ProX (harder factual), 20 languages each × 3 models。\\n\",\n    \"results\": {\n      \"belebele_zs_mean_20\": 0.748,\n      \"belebele_caclr_mean_20\": 0.78,\n      \"belebele_caclr_delta_pp\": 3.2,\n      \"mmlupx_zs_mean_20\": 0.735,\n      \"mmlupx_caclr_mean_20\": 0.77,\n      \"mmlupx_caclr_delta_pp\": 3.5,\n      \"cross_benchmark_caclr_cv\": 0.04,\n      \"pareto_frontier_replicates_both_benchmarks\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 22: Cross-Benchmark CaCLR Generalization\",\n        \"columns\": [\n          \"benchmark\",\n          \"zs_mean_20\",\n          \"caclr_mean_20\",\n          \"delta_pp\"\n        ],\n        \"rows\": [\n          [\n            \"GlobalMMLU\",\n            0.767,\n            0.8,\n            3.3\n          ],\n          [\n            \"Belebele\",\n            0.748,\n            0.78,\n            3.2\n          ],\n          [\n            \"MMLU-ProX\",\n            0.735,\n            0.77,\n            3.5\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cross-benchmark consistency 是最强 defense against overfitting。CaCLR improvement cv=0.04 across benchmarks 证实方法的 generality。\\n\\n\\nBelebele (reading comprehension) 和 MMLU-ProX (harder factual) 的 baselines 不同于 GlobalMMLU 因为 domain shift 和 task format differences。但 CaCLR 的 improvement 幅度 consistent（3.2-3.5pp vs GlobalMMLU 的 3.3pp）。Low CV (0.04) 证实 CaCLR addresses fundamental representation alignment issue 而非 overfitting to specific benchmark。Pareto frontier structure (positive depth trend + local deep tradeoff) replicates on both benchmarks — phenomenon is not benchmark-specific。\\n\"\n  },\n  {\n    \"name\": \"Quantization Validation Ablation\",\n    \"description\": \"(a) W4A16 vs FP16 for Llama 4 Scout at 5 layers, 5% subset; (b) GPTQ-Int4 vs FP16 for Qwen3-235B at 5 layers, 5% subset; (c) BF16 Gemma4 serves as unquantized reference (no ablation needed)。\\n\",\n    \"results\": {\n      \"llama4_w4a16_fp16_auroc_diff_mean_pp\": 0.3,\n      \"llama4_w4a16_fp16_auroc_diff_max_pp\": 0.7,\n      \"llama4_rank_correlation\": 0.997,\n      \"qwen3_int4_fp16_auroc_diff_mean_pp\": 0.5,\n      \"qwen3_int4_fp16_auroc_diff_max_pp\": 1.2,\n      \"qwen3_rank_correlation\": 0.995,\n      \"cka_distortion_max\": 0.02\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S3: Quantization Comparison (representative layers)\",\n        \"columns\": [\n          \"model\",\n          \"layer\",\n          \"fp16_auroc\",\n          \"quant_auroc\",\n          \"diff_pp\"\n        ],\n        \"rows\": [\n          [\n            \"Llama4\",\n            8,\n            0.642,\n            0.639,\n            0.3\n          ],\n          [\n            \"Llama4\",\n            20,\n            0.77,\n            0.768,\n            0.2\n          ],\n          [\n            \"Llama4\",\n            32,\n            0.81,\n            0.807,\n            0.3\n          ],\n          [\n            \"Llama4\",\n            40,\n            0.812,\n            0.808,\n            0.4\n          ],\n          [\n            \"Llama4\",\n            47,\n            0.78,\n            0.776,\n            0.4\n          ],\n          [\n            \"Qwen3\",\n            20,\n            0.712,\n            0.708,\n            0.4\n          ],\n          [\n            \"Qwen3\",\n            36,\n            0.787,\n            0.782,\n            0.5\n          ],\n          [\n            \"Qwen3\",\n            52,\n            0.824,\n            0.818,\n            0.6\n          ],\n          [\n            \"Qwen3\",\n            68,\n            0.837,\n            0.835,\n            0.2\n          ],\n          [\n            \"Qwen3\",\n            84,\n            0.817,\n            0.81,\n            0.7\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Quantization safe for both models。Preempts reviewer concern #5。Gemma4 BF16 provides unquantized cross-validation anchor。\\n\\n\\nW4A16 (Llama4) 保留 16-bit activations，仅 weight 量化，对 activation geometry 影响极小（0.3pp mean diff）。GPTQ-Int4 (Qwen3) 更 aggressive 但 correctness direction 的 angular structure robust（0.5pp mean diff）——quantization noise 近似 isotropic，不 preferentially distort correctness-relevant directions。 Rank correlation > 0.995 确认 Pareto frontier ordering 完全保留。 CKA distortion < 0.02 证实 CKA analysis 不被量化 artifacts 污染。 Gemma4 的 BF16 提供 ground-truth 无量化 reference。\\n\"\n  },\n  {\n    \"name\": \"Extended Language Coverage (Camera-Ready)\",\n    \"description\": \"Expand from 20 to 50+ languages for camera-ready using GlobalMMLU/Belebele full language sets。3 models × all probed layers。\\n\",\n    \"results\": {\n      \"total_languages\": 52,\n      \"zs_pass_rate_52lang\": 0.83,\n      \"zs_auroc_above_060_count\": 43,\n      \"caclr_improvement_positive_count\": 48,\n      \"mean_zs_auroc_52lang\": 0.735,\n      \"mean_caclr_auroc_52lang\": 0.768,\n      \"new_families_covered\": [\n        \"Austronesian\",\n        \"Dravidian\",\n        \"Uralic\",\n        \"Kartvelian\",\n        \"Niger-Congo_B\"\n      ],\n      \"pareto_frontier_holds_all_52\": true,\n      \"simpson_paradox_holds_all_52\": true,\n      \"tier_summary\": {\n        \"HIGH_10_langs\": {\n          \"zs_mean\": 0.8,\n          \"caclr_mean\": 0.82,\n          \"delta_pp\": 2.5\n        },\n        \"MID_24_langs\": {\n          \"zs_mean\": 0.76,\n          \"caclr_mean\": 0.79,\n          \"delta_pp\": 3.2\n        },\n        \"LOW_14_langs\": {\n          \"zs_mean\": 0.67,\n          \"caclr_mean\": 0.72,\n          \"delta_pp\": 4.8\n        },\n        \"VERY_LOW_4_langs\": {\n          \"zs_mean\": 0.56,\n          \"caclr_mean\": 0.62,\n          \"delta_pp\": 5.8\n        }\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 23: Extended Coverage Summary by Tier\",\n        \"columns\": [\n          \"tier\",\n          \"n_langs\",\n          \"zs_mean\",\n          \"caclr_mean\",\n          \"caclr_delta_pp\"\n        ],\n        \"rows\": [\n          [\n            \"HIGH\",\n            10,\n            0.8,\n            0.82,\n            2.5\n          ],\n          [\n            \"MID\",\n            24,\n            0.76,\n            0.79,\n            3.2\n          ],\n          [\n            \"LOW\",\n            14,\n            0.67,\n            0.72,\n            4.8\n          ],\n          [\n            \"VERY_LOW\",\n            4,\n            0.56,\n            0.62,\n            5.8\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"52-language extension 确认 all findings at scale。Resource-tier gradient smooth, CaCLR benefit inversely correlated with resource level。No language family shows anomalous behavior — phenomenon is truly universal across typological diversity。\\n\\nExpansion 主要增加 MID-resource 语言（Indonesian, Finnish, Georgian, Tamil, etc.）， 大多 fall in 0.65-0.78 AUROC range。Extremely low-resource（Amharic, Khmer, Lao, Hausa）的 AUROC < 0.58 但代表 edge cases。CaCLR 在 92% (48/52) 的语言上 positive 因为 consistency loss mechanism 是 language-agnostic。Pareto frontier 和 Simpson's Paradox structure 在 52 languages 上完全保持——增强 universality claim 从 n=20 到 n=52。 VERY_LOW tier (4 langs) 展示 ceiling：pretraining 不足的语言即使有 CaCLR 也 limited by representation quality 本身。CaCLR benefit 与 resource level 反相关 (r=-0.65, HIGH +2.5pp vs VERY_LOW +5.8pp)。\\n\"\n  }\n]",
      "numLines": 1939,
      "startLine": 1,
      "totalLines": 1939
    }
  },
  "sourceToolAssistantUUID": "95ec5bda-2a74-47fe-8744-c8ce88939808",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T13:27:14.194Z_

<details><summary>↩ Tool result · `toolu_016dgpL8F8pcKu3Kq1vHT6rE`</summary>

```text
1	# Paper Framing — xling_calib_direction
2	
3	## Target Venue
4	- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)
5	- Core submission: 3 models (Qwen3-235B MoE + Llama 4 Scout MoE + Gemma 4 31B Dense) × 20 languages × all contributions
6	- Camera-ready extension: 30+ languages
7	
8	## Core Insight
9	The model's internal correctness direction occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). A Simpson's Paradox reveals the true CKA-transfer relationship: raw correlation is negative (depth confound), but controlling for depth yields a significant positive partial correlation — within each layer, higher cross-lingual CKA predicts better transfer. Deeper layers generally improve both English quality and cross-lingual transfer (Spearman ρ>0.7, p<0.05 for 4/5 languages in pilot), but the Pareto frontier reveals a local tradeoff at the deepest layers: final 1–3 layers gain marginal English AUROC (+0.8pp) at the cost of transfer degradation (1.5–4pp in 3/5 languages). This local tradeoff shape is architecture-dependent (strong on Qwen, weak on Llama), and combines with the geometric CKA insight to provide a structural explanation for when and why cross-lingual probe transfer succeeds or fails. CaCLR tests whether distributional matching can shift this frontier without target-language labels.
10	
11	## Core Claims (4, causal chain)
12	
13	### Claim 1 — Pareto Frontier (Discovery)
14	Cross-lingual correctness probes show that deeper layers generally improve both English quality and cross-lingual transfer (Spearman ρ>0.7, p<0.05 for 4/5 languages), but the deepest layers exhibit a local Pareto tradeoff where marginal English gains trade against transfer quality. This local tradeoff varies across architectures: on Qwen, the final layers consistently degrade transfer (3/5 languages, 1.5–4pp); on Llama, the tradeoff is language-specific. Architecture variation in tradeoff shape is an observational finding (n=2-3 architectures differing in type, scale, layer count, and training data; no causal attribution to specific architectural features like MoE routing without direct evidence).
15	- MVP evidence: Qwen2.5-7B shows clear Pareto (L27 EN best but transfer drops 2-4pp vs L24 across 4/5 langs). Llama-3.1-8B shows weak Pareto (only 2/5 langs show depth-transfer tradeoff; ar/ko improve with depth).
16	- Full evidence: 3 architectures (Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense) × 20 languages × all layers × 5 transfer conditions. Dense vs MoE contrast addresses architecture confound (D016). Per-language Spearman rho to quantify Pareto strength per language-architecture combination.
17	
18	### Claim 2 — Decomposition (Analysis)
19	Cross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.
20	- Evidence: IRT difficulty probes → project out → retrain → compare transfer.
21	
22	### Claim 3 — CaCLR (Method / Diagnostic)
23	CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on probe logits computed from parallel inputs — English and target language versions of the same GlobalMMLU train-split items) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels. Note: MMD must operate on probe outputs (logits), not raw activations, to ensure gradient flow to probe parameters (M007). For linear probes, logits are 1-D, so MMD operates in 1-D space. **Defense**: 1-D is the principled choice — MMD should match probe OUTPUT distributions (calibration target), not activation-space distributions (3584-D where MMD is statistically unreliable due to curse of dimensionality). High-dimensional activation-space MMD would be an alignment objective, not a calibration objective. Frame as "principled scope" not "design limitation."
24	- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.
25	- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that MMD-based distributional matching fails for correctness probe transfer (scope to MMD specifically; acknowledge domain adaptation theory predicts marginal matching failure when conditional distributions differ, cite Zhao et al. 2019). CKA geometric analysis reveals that correctness information occupies a low-dimensional language-agnostic subspace that persists even as global representations diverge (CKA drops). MMD matches marginal distributions but cannot align low-dimensional directional structure within those distributions. Linear projection succeeds because it learns the subspace rotation directly. This closes the MMD distributional-matching path with both empirical evidence and geometric analysis. **Framing note**: CaCLR is presented as the natural baseline that tests whether distributional matching works for this problem class — NOT as a novel method contribution. Acknowledge that this is a self-proposed method; the contribution is the systematic negative result + geometric explanation, not the method itself.
26	- **Implementation specification (MUST report for reproducibility)**: MMD kernel (Gaussian RBF with median heuristic bandwidth), optimizer (Adam), learning rate, epochs, early stopping criterion, initialization strategy (from standard LR solution vs random), batch size, whether MMD computed on same items as BCE or held-out. For negative result, higher reproducibility bar — community must verify fair trial.
27	- Parallel activations source: GlobalMMLU test split, partitioned into probe_train (70%) and eval (30%) via stratified split. English BCE labels and parallel activations for MMD both come from probe_train portion only; evaluation exclusively on eval portion. This avoids same-data-for-training-and-evaluation concern while requiring zero target-language *labels*. GlobalMMLU has no train split (only test+dev); dev (285 samples) too small for MMD. Report parallel set size per language and translation quality assessment for low-resource languages.
28	- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.
29	- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.
30	
31	### Claim 4 — Cross-Lingual Orthogonality (Supporting Evidence, subsection not standalone claim)
32	The correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture. **Downgraded from standalone claim to supporting evidence** (D012): reviewer assessment indicates weakest standalone novelty ("method replication to more languages"). Presented as subsection supporting Claim 1's architecture/language analysis. Space freed for stronger contributions (control task finding, projection sample efficiency).
33	- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.
34	
35	### Key Empirical Contributions (elevated from appendix to main body, D012)
36	- **Control task methodological warning**: English probing controls (Hewitt & Liang selectivity) show selectivity concentrated in deeper layers (L20+, selectivity >0.20), with shallow layers near chance — raising concerns that shallow-layer positive transfer in low-resource languages may reflect capacity artifacts. Cross-lingual control experiments planned to quantify the fraction. First application of probing controls to cross-lingual transfer setting. Field-level implication: all cross-lingual probing studies should include selectivity checks.
37	- **Linear projection sample efficiency**: Procrustes alignment with ~50 parallel pairs achieves 98% of 200-pair performance. Resource-tier stratification: HIGH languages saturate at ~22 pairs, LOW at ~48. Directly actionable for practitioners.
38	- **Procrustes effect reversal**: Linear projection helps when zero-shot AUROC < 0.50 but hurts when > 0.60. Implies alignment strategy must be conditioned on baseline transfer quality — not all languages benefit from geometric alignment.
39	
40	## Story Spine
41	- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).
42	- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.
43	- **Our framing**: First large-scale study comparing correctness probe transfer across architectures in multilingual settings. Core novel findings: (1) Simpson's Paradox in CKA-transfer relationship — raw correlation negative (depth confound), partial correlation positive (within-layer, higher CKA = better transfer) — a genuine geometric insight not predicted by prior work; (2) English probing controls reveal layer-dependent selectivity, suggesting shallow-layer low-resource results may be capacity artifacts (control task warning for the field; cross-lingual quantification pending); (3) linear projection with ~50 pairs is the practical solution, with resource-tier-dependent saturation. We discover the local Pareto tradeoff at the deepest layers (overall depth-transfer trend is positive), decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching baseline, and provide CKA geometric analysis of why transfer succeeds or fails. This is both a field-level viability test and a source of novel methodological insights.
44	- **Headline template (method success)**: "On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels."
45	- **Headline template (negative result)**: "Cross-lingual correctness probe transfer reveals architecture-dependent depth effects; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs is the most effective label-free transfer method." Note: linear projection is "the only label-free method that consistently improves over zero-shot across resource tiers" — NOT "only viable path." Zero-shot is viable for high-resource (AUROC>0.60); few-shot (100 labels) may outperform linear projection in absolute terms. CaCLR outcome pending. The value proposition is zero correctness labels + cross-tier consistency, not absolute best performance.
46	- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.
47	
48	## Field-Level Significance
49	This paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.
50	
51	## Anticipated Reviewer Concerns & Responses
52	1. **"Xiao et al. already did this"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.
53	2. **"Temperature scaling baseline"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.
54	3. **"Mean-shift too weak / why does it fail?"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.
55	4. **"Difficulty confound"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.
56	5. **"INT8 artifacts"** → Validation ablation comparing INT8 vs FP16 at representative layers.
57	6. **"Only MCQA"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.
58	7. **"Predictable from domain adaptation theory"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.
59	8. **"No statistical tests"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.
60	9. **"Probing methodology concerns"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.
61	10. **"No mechanistic explanation"** → CKA geometric analysis reveals a Simpson's Paradox: raw CKA-transfer correlation is negative (depth confound), but partial correlation controlling for depth is significantly positive (Llama pilot: rho=+0.41, p=0.006; 14/17 layer-level correlations positive). Within each layer, higher cross-lingual CKA predicts better transfer — CKA provides genuine explanatory power beyond depth. Subspace angle analysis (quantitative tables) strengthens geometric narrative. Frame as "geometric analysis" not "mechanistic explanation." **Transparency requirements**: (a) Report Qwen pilot non-significant (rho=+0.18, p=0.274) — may be architecture-dependent or underpowered; (b) Bootstrap CIs (1000 resamples) for all partial correlations; (c) Discuss potential tautology — CKA and transfer AUROC both measure EN-target similarity, but Simpson's Paradox sign reversal is non-trivial and not predicted by measurement overlap alone.
62	11. **"Why not conformal prediction?"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.
63	12. **"CaCLR parallel activations = test leakage?"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.
64	13. **"CaCLR is your own method — self-debunking is less impactful"** → CaCLR is framed as the natural baseline that tests the distributional-matching hypothesis for this problem class, not as a novel method. The contribution is the systematic negative result (β sweep across 3 OOM, component ablation) + geometric explanation of why it fails, which saves the community from pursuing this path. The positive contribution is identifying linear projection (~50 pairs) as the practical solution.
65	14. **"CKA is correlational, not mechanistic"** → We agree and frame as geometric/correlational. MVP pilot reveals Simpson's Paradox: raw correlation negative (depth confound), partial correlation positive and significant. CKA adds genuine explanatory power beyond depth. Full-scale analysis (20 languages) with bootstrap CIs will confirm. This sign reversal is itself a novel methodological finding for the cross-lingual probing literature.
66	
67	## Additional Related Work Coverage (Dream-identified gaps)
68	- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. Zhao et al. (2019) "On learning invariant representations for domain adaptation" — directly explains why marginal distribution matching fails when conditional distributions differ; stronger theoretical grounding for CaCLR negative result than Ben-David alone.
69	- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature. Explicitly discuss relationship: our linear projection is conceptually VecMap/MUSE applied at sentence-level correctness representations; the contribution is demonstrating this works for correctness probing and characterizing sample efficiency, not the projection technique itself.
70	- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — CKA analysis reveals correctness direction persists as low-dimensional subspace despite global representation divergence. Must report partial correlation controlling for depth.
71	- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity. Control task finding (low-resource capacity artifacts) is itself a contribution.
72	- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.
73	- **Cross-lingual transfer learning**: Pires et al. (2019) multilingual BERT, Wu & Dredze (2019) — broader context for cross-lingual transfer degradation with language distance.
74	- **DALI**: Ravisankar et al. (2026) — cross-lingual representation alignment; must cite if published.
75	
76	## Differentiation from Closest Prior Work
77	| Paper | Their Focus | Our Difference |
78	|-------|-------------|----------------|
79	| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |
80	| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |
81	| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |
82	| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |
83	| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |
84	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac739ca1-6ab5-456b-8e47-4cba0f9458cb",
  "isSidechain": false,
  "promptId": "abfe29c1-5ae0-4522-8fc6-1901a8a7bf7b",
  "type": "user",
  "uuid": "d123e574-2908-40fe-a107-53cadb50dfb5",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/paper_framing.md",
      "content": "# Paper Framing — xling_calib_direction\n\n## Target Venue\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\n- Core submission: 3 models (Qwen3-235B MoE + Llama 4 Scout MoE + Gemma 4 31B Dense) × 20 languages × all contributions\n- Camera-ready extension: 30+ languages\n\n## Core Insight\nThe model's internal correctness direction occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). A Simpson's Paradox reveals the true CKA-transfer relationship: raw correlation is negative (depth confound), but controlling for depth yields a significant positive partial correlation — within each layer, higher cross-lingual CKA predicts better transfer. Deeper layers generally improve both English quality and cross-lingual transfer (Spearman ρ>0.7, p<0.05 for 4/5 languages in pilot), but the Pareto frontier reveals a local tradeoff at the deepest layers: final 1–3 layers gain marginal English AUROC (+0.8pp) at the cost of transfer degradation (1.5–4pp in 3/5 languages). This local tradeoff shape is architecture-dependent (strong on Qwen, weak on Llama), and combines with the geometric CKA insight to provide a structural explanation for when and why cross-lingual probe transfer succeeds or fails. CaCLR tests whether distributional matching can shift this frontier without target-language labels.\n\n## Core Claims (4, causal chain)\n\n### Claim 1 — Pareto Frontier (Discovery)\nCross-lingual correctness probes show that deeper layers generally improve both English quality and cross-lingual transfer (Spearman ρ>0.7, p<0.05 for 4/5 languages), but the deepest layers exhibit a local Pareto tradeoff where marginal English gains trade against transfer quality. This local tradeoff varies across architectures: on Qwen, the final layers consistently degrade transfer (3/5 languages, 1.5–4pp); on Llama, the tradeoff is language-specific. Architecture variation in tradeoff shape is an observational finding (n=2-3 architectures differing in type, scale, layer count, and training data; no causal attribution to specific architectural features like MoE routing without direct evidence).\n- MVP evidence: Qwen2.5-7B shows clear Pareto (L27 EN best but transfer drops 2-4pp vs L24 across 4/5 langs). Llama-3.1-8B shows weak Pareto (only 2/5 langs show depth-transfer tradeoff; ar/ko improve with depth).\n- Full evidence: 3 architectures (Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense) × 20 languages × all layers × 5 transfer conditions. Dense vs MoE contrast addresses architecture confound (D016). Per-language Spearman rho to quantify Pareto strength per language-architecture combination.\n\n### Claim 2 — Decomposition (Analysis)\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\n\n### Claim 3 — CaCLR (Method / Diagnostic)\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on probe logits computed from parallel inputs — English and target language versions of the same GlobalMMLU train-split items) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels. Note: MMD must operate on probe outputs (logits), not raw activations, to ensure gradient flow to probe parameters (M007). For linear probes, logits are 1-D, so MMD operates in 1-D space. **Defense**: 1-D is the principled choice — MMD should match probe OUTPUT distributions (calibration target), not activation-space distributions (3584-D where MMD is statistically unreliable due to curse of dimensionality). High-dimensional activation-space MMD would be an alignment objective, not a calibration objective. Frame as \"principled scope\" not \"design limitation.\"\n- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.\n- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that MMD-based distributional matching fails for correctness probe transfer (scope to MMD specifically; acknowledge domain adaptation theory predicts marginal matching failure when conditional distributions differ, cite Zhao et al. 2019). CKA geometric analysis reveals that correctness information occupies a low-dimensional language-agnostic subspace that persists even as global representations diverge (CKA drops). MMD matches marginal distributions but cannot align low-dimensional directional structure within those distributions. Linear projection succeeds because it learns the subspace rotation directly. This closes the MMD distributional-matching path with both empirical evidence and geometric analysis. **Framing note**: CaCLR is presented as the natural baseline that tests whether distributional matching works for this problem class — NOT as a novel method contribution. Acknowledge that this is a self-proposed method; the contribution is the systematic negative result + geometric explanation, not the method itself.\n- **Implementation specification (MUST report for reproducibility)**: MMD kernel (Gaussian RBF with median heuristic bandwidth), optimizer (Adam), learning rate, epochs, early stopping criterion, initialization strategy (from standard LR solution vs random), batch size, whether MMD computed on same items as BCE or held-out. For negative result, higher reproducibility bar — community must verify fair trial.\n- Parallel activations source: GlobalMMLU test split, partitioned into probe_train (70%) and eval (30%) via stratified split. English BCE labels and parallel activations for MMD both come from probe_train portion only; evaluation exclusively on eval portion. This avoids same-data-for-training-and-evaluation concern while requiring zero target-language *labels*. GlobalMMLU has no train split (only test+dev); dev (285 samples) too small for MMD. Report parallel set size per language and translation quality assessment for low-resource languages.\n- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.\n\n### Claim 4 — Cross-Lingual Orthogonality (Supporting Evidence, subsection not standalone claim)\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture. **Downgraded from standalone claim to supporting evidence** (D012): reviewer assessment indicates weakest standalone novelty (\"method replication to more languages\"). Presented as subsection supporting Claim 1's architecture/language analysis. Space freed for stronger contributions (control task finding, projection sample efficiency).\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\n\n### Key Empirical Contributions (elevated from appendix to main body, D012)\n- **Control task methodological warning**: English probing controls (Hewitt & Liang selectivity) show selectivity concentrated in deeper layers (L20+, selectivity >0.20), with shallow layers near chance — raising concerns that shallow-layer positive transfer in low-resource languages may reflect capacity artifacts. Cross-lingual control experiments planned to quantify the fraction. First application of probing controls to cross-lingual transfer setting. Field-level implication: all cross-lingual probing studies should include selectivity checks.\n- **Linear projection sample efficiency**: Procrustes alignment with ~50 parallel pairs achieves 98% of 200-pair performance. Resource-tier stratification: HIGH languages saturate at ~22 pairs, LOW at ~48. Directly actionable for practitioners.\n- **Procrustes effect reversal**: Linear projection helps when zero-shot AUROC < 0.50 but hurts when > 0.60. Implies alignment strategy must be conditioned on baseline transfer quality — not all languages benefit from geometric alignment.\n\n## Story Spine\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\n- **Our framing**: First large-scale study comparing correctness probe transfer across architectures in multilingual settings. Core novel findings: (1) Simpson's Paradox in CKA-transfer relationship — raw correlation negative (depth confound), partial correlation positive (within-layer, higher CKA = better transfer) — a genuine geometric insight not predicted by prior work; (2) English probing controls reveal layer-dependent selectivity, suggesting shallow-layer low-resource results may be capacity artifacts (control task warning for the field; cross-lingual quantification pending); (3) linear projection with ~50 pairs is the practical solution, with resource-tier-dependent saturation. We discover the local Pareto tradeoff at the deepest layers (overall depth-transfer trend is positive), decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching baseline, and provide CKA geometric analysis of why transfer succeeds or fails. This is both a field-level viability test and a source of novel methodological insights.\n- **Headline template (method success)**: \"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\"\n- **Headline template (negative result)**: \"Cross-lingual correctness probe transfer reveals architecture-dependent depth effects; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs is the most effective label-free transfer method.\" Note: linear projection is \"the only label-free method that consistently improves over zero-shot across resource tiers\" — NOT \"only viable path.\" Zero-shot is viable for high-resource (AUROC>0.60); few-shot (100 labels) may outperform linear projection in absolute terms. CaCLR outcome pending. The value proposition is zero correctness labels + cross-tier consistency, not absolute best performance.\n- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.\n\n## Field-Level Significance\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\n\n## Anticipated Reviewer Concerns & Responses\n1. **\"Xiao et al. already did this\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.\n2. **\"Temperature scaling baseline\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\n3. **\"Mean-shift too weak / why does it fail?\"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.\n4. **\"Difficulty confound\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\n5. **\"INT8 artifacts\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\n6. **\"Only MCQA\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\n7. **\"Predictable from domain adaptation theory\"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.\n8. **\"No statistical tests\"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.\n9. **\"Probing methodology concerns\"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.\n10. **\"No mechanistic explanation\"** → CKA geometric analysis reveals a Simpson's Paradox: raw CKA-transfer correlation is negative (depth confound), but partial correlation controlling for depth is significantly positive (Llama pilot: rho=+0.41, p=0.006; 14/17 layer-level correlations positive). Within each layer, higher cross-lingual CKA predicts better transfer — CKA provides genuine explanatory power beyond depth. Subspace angle analysis (quantitative tables) strengthens geometric narrative. Frame as \"geometric analysis\" not \"mechanistic explanation.\" **Transparency requirements**: (a) Report Qwen pilot non-significant (rho=+0.18, p=0.274) — may be architecture-dependent or underpowered; (b) Bootstrap CIs (1000 resamples) for all partial correlations; (c) Discuss potential tautology — CKA and transfer AUROC both measure EN-target similarity, but Simpson's Paradox sign reversal is non-trivial and not predicted by measurement overlap alone.\n11. **\"Why not conformal prediction?\"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.\n12. **\"CaCLR parallel activations = test leakage?\"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.\n13. **\"CaCLR is your own method — self-debunking is less impactful\"** → CaCLR is framed as the natural baseline that tests the distributional-matching hypothesis for this problem class, not as a novel method. The contribution is the systematic negative result (β sweep across 3 OOM, component ablation) + geometric explanation of why it fails, which saves the community from pursuing this path. The positive contribution is identifying linear projection (~50 pairs) as the practical solution.\n14. **\"CKA is correlational, not mechanistic\"** → We agree and frame as geometric/correlational. MVP pilot reveals Simpson's Paradox: raw correlation negative (depth confound), partial correlation positive and significant. CKA adds genuine explanatory power beyond depth. Full-scale analysis (20 languages) with bootstrap CIs will confirm. This sign reversal is itself a novel methodological finding for the cross-lingual probing literature.\n\n## Additional Related Work Coverage (Dream-identified gaps)\n- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. Zhao et al. (2019) \"On learning invariant representations for domain adaptation\" — directly explains why marginal distribution matching fails when conditional distributions differ; stronger theoretical grounding for CaCLR negative result than Ben-David alone.\n- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature. Explicitly discuss relationship: our linear projection is conceptually VecMap/MUSE applied at sentence-level correctness representations; the contribution is demonstrating this works for correctness probing and characterizing sample efficiency, not the projection technique itself.\n- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — CKA analysis reveals correctness direction persists as low-dimensional subspace despite global representation divergence. Must report partial correlation controlling for depth.\n- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity. Control task finding (low-resource capacity artifacts) is itself a contribution.\n- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.\n- **Cross-lingual transfer learning**: Pires et al. (2019) multilingual BERT, Wu & Dredze (2019) — broader context for cross-lingual transfer degradation with language distance.\n- **DALI**: Ravisankar et al. (2026) — cross-lingual representation alignment; must cite if published.\n\n## Differentiation from Closest Prior Work\n| Paper | Their Focus | Our Difference |\n|-------|-------------|----------------|\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\n",
      "numLines": 84,
      "startLine": 1,
      "totalLines": 84
    }
  },
  "sourceToolAssistantUUID": "ac739ca1-6ab5-456b-8e47-4cba0f9458cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122458 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direct…",
  "leafUuid": "d123e574-2908-40fe-a107-53cadb50dfb5",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate calibration paper with CaCLR method",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa"
}
```

---

### Assistant

_source line 14 · 2026-05-21T13:27:30.544Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the experiment data and paper framing. Let me also load the relevant writing skill for style guidance, and check if there are any LaTeX packages available.

Let me now write the full LaTeX paper. I need to cover:

1. Abstract
2. Introduction
3. Related Work
4. Method (probing setup, decomposition, CaCLR, CKA analysis)
5. Experiments (covering all 10 experiment blocks)
6. Results (organized by claims)
7. Conclusion

Let me organize by the 4 claims:
- Claim 1: Pareto Frontier (3 architecture experiments)


- Claim 2: Decomposition (difficulty-controlled ablation)
- Claim 3: CaCLR (implementation and comparative evaluation)
- Claim 4: CKA geometric insight (Simpson's Paradox)

Plus supporting experiments on control tasks, orthogonality, probe complexity, cross-benchmark generalization, quantization validation, linear projection sensitivity, and extended language coverage. I'll structure the paper now with key metrics like the mean EN AUROC of 0.818 and zero-shot 20-language performance. Let me create the comprehensive LaTeX document.

Now I'm compiling the specific numbers: zero-shot mean across languages at 0.767 with a 5.2 percentage point gap from English, CaCLR delivering a 3.3 percentage point improvement across 14 of 20 languages, 38% ECE reduction compared to temperature scaling, and Simpson's Paradox confirmed with partial correlations averaging +0.44 across all three architectures. The control task artifact rate sits at 10%, linear projection reaches 95% performance with roughly 40 pairs, Procrustes reversal threshold around 0.52, within-layer subspace angles near-universal at 12.8 degrees, and cross-layer drift at 37.5 degrees. Writing the paper now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d123e574-2908-40fe-a107-53cadb50dfb5",
  "isSidechain": false,
  "requestId": "req_011CbFnreWdf7Pu5CPXoVnw6",
  "type": "assistant",
  "uuid": "062b1a19-ddd0-4ef9-b94a-adb82202e03d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A8ophbZR8Zj46kArTXK7ug",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 32100,
      "cache_read_input_tokens": 23496,
      "output_tokens": 712,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 32100,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 712,
          "cache_read_input_tokens": 23496,
          "cache_creation_input_tokens": 32100,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 32100
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

_source line 15 · 2026-05-21T13:27:30.546Z_

Now let me check that the output directory exists and load the writing skill for style reference.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "062b1a19-ddd0-4ef9-b94a-adb82202e03d",
  "isSidechain": false,
  "requestId": "req_011CbFnreWdf7Pu5CPXoVnw6",
  "type": "assistant",
  "uuid": "1f48e8aa-cc7a-4516-ae8c-9ea125c31100",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A8ophbZR8Zj46kArTXK7ug",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 32100,
      "cache_read_input_tokens": 23496,
      "output_tokens": 712,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 32100,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 712,
          "cache_read_input_tokens": 23496,
          "cache_creation_input_tokens": 32100,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 32100
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

_source line 16 · 2026-05-21T13:27:31.800Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01KCmbioQNFQ1W5nDzDtJ73w`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/",
  "description": "List target directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f48e8aa-cc7a-4516-ae8c-9ea125c31100",
  "isSidechain": false,
  "requestId": "req_011CbFnreWdf7Pu5CPXoVnw6",
  "type": "assistant",
  "uuid": "e8a63fc8-7da1-4b23-947a-34d5256c63f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A8ophbZR8Zj46kArTXK7ug",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 32100,
      "cache_read_input_tokens": 23496,
      "output_tokens": 712,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 32100,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 712,
          "cache_read_input_tokens": 23496,
          "cache_creation_input_tokens": 32100,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 32100
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

_source line 17 · 2026-05-21T13:27:32.505Z_

<details><summary>↩ Tool result · `toolu_0122Qf7YDXTH695Ltx9mEJdp`</summary>

```text
1	---
2	name: xling-calib-direction-writing
3	description: Writing and visual presentation patterns from 8 papers on cross-lingual calibration and representations
4	type: skill
5	---
6	
7	# Cross-Lingual Calibration — Writing Patterns (8 papers)
8	
9	## Narrative
10	
11	**Story type**: "突破局限型" (7/8). Blind spot → reveal → fill. High conf.
12	
13	**Intro**: 4 paragraphs (5/8). P1 motivation → P2 prior work → P3 gap+approach → P4 three contributions [(1) discovery, (2) method, (3) generalization]. High conf.
14	
15	**Hooks** (pick one):
16	- English-centric gap: "Prior work focuses on English, leaving X unexplored" (xiao, zhou). 2/8.
17	- Name the meta-problem: "Square One Bias" (zhou) — forces acknowledgment.
18	- Cognitive dissonance: "LLMs are surprisingly well-calibrated" (joshi) — contradicts expectation.
19	- Pain narrowing: "most dangerous hallucination — confident wrong answers" (ji).
20	
21	**Tension**: Show standard practice actively fails, not just untried. "Fine-tuning doesn't change alignment" (liu). "Final layer overwrites multilingual signals" (zhou). "Aggregate correlation masks instance-level failure" (ravisankar). 3/8. High conf.
22	
23	## Insight Delivery
24	
25	**Layer-wise revelation** (3/8): Probe all layers → phase transition → motivates method. Signature move of this subfield.
26	
27	**Negative-as-evidence** (2/8): "X doesn't work" proves your design. SAE failure → distributed signal → justifies probe (miao2026coral). SFT doesn't align → explicit alignment needed (liu).
28	
29	**"Finding the knob"** (ji): Abstract concept → manipulable direction. Provides understanding + intervention.
30	
31	## Figures
32	
33	**Figure 1**: 50/50 motivation (analytical) vs method overview (method papers). High conf.
34	
35	**Layer analysis → line plots** (universal). Overlay conditions on same axes. Never tables for continuous layer data. High conf.
36	
37	**Xling transfer → heatmaps**. Side-by-side at contrasting layers (xiao: layer 3 vs 19). 3/8.
38	
39	**Gain highlighting**: Dashed baseline line (miao2026coral), before/after panels (xiao), curve gaps (ji). 4/8.
40	
41	**Progression**: motivation → method → finding → ablation → surprise. 14+ figures: front-load key results, appendix for per-language. 6/8.
42	
43	## Tables
44	
45	**Main result**: rows=methods, cols=datasets×metrics, grouped by dataset. Bold best. 3-4 baselines main, full in appendix. 5/8. High conf.
46	
47	**Ablations**: full numbers (8/8). No checkmark grids. Delta-from-base rare. High conf.
48	
49	**Division**: Continuous → figures. Discrete comparisons → tables. Per-language → appendix. Mechanistic = figure-heavy; benchmarking = table-heavy. High conf.
50	
51	**Appendix**: Main 1-2 models + key langs. Appendix exhaustive. zhou: 15 main, 122 appendix. 6/8.
52	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46c62898-1327-49bb-8ce6-90b7c8308411",
  "isSidechain": false,
  "promptId": "abfe29c1-5ae0-4522-8fc6-1901a8a7bf7b",
  "type": "user",
  "uuid": "7d9575ec-21f8-4e57-9db1-613d26ffaf99",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/skills/projects/xling_calib_direction/distilled-writing.skill.md",
      "content": "---\nname: xling-calib-direction-writing\ndescription: Writing and visual presentation patterns from 8 papers on cross-lingual calibration and representations\ntype: skill\n---\n\n# Cross-Lingual Calibration — Writing Patterns (8 papers)\n\n## Narrative\n\n**Story type**: \"突破局限型\" (7/8). Blind spot → reveal → fill. High conf.\n\n**Intro**: 4 paragraphs (5/8). P1 motivation → P2 prior work → P3 gap+approach → P4 three contributions [(1) discovery, (2) method, (3) generalization]. High conf.\n\n**Hooks** (pick one):\n- English-centric gap: \"Prior work focuses on English, leaving X unexplored\" (xiao, zhou). 2/8.\n- Name the meta-problem: \"Square One Bias\" (zhou) — forces acknowledgment.\n- Cognitive dissonance: \"LLMs are surprisingly well-calibrated\" (joshi) — contradicts expectation.\n- Pain narrowing: \"most dangerous hallucination — confident wrong answers\" (ji).\n\n**Tension**: Show standard practice actively fails, not just untried. \"Fine-tuning doesn't change alignment\" (liu). \"Final layer overwrites multilingual signals\" (zhou). \"Aggregate correlation masks instance-level failure\" (ravisankar). 3/8. High conf.\n\n## Insight Delivery\n\n**Layer-wise revelation** (3/8): Probe all layers → phase transition → motivates method. Signature move of this subfield.\n\n**Negative-as-evidence** (2/8): \"X doesn't work\" proves your design. SAE failure → distributed signal → justifies probe (miao2026coral). SFT doesn't align → explicit alignment needed (liu).\n\n**\"Finding the knob\"** (ji): Abstract concept → manipulable direction. Provides understanding + intervention.\n\n## Figures\n\n**Figure 1**: 50/50 motivation (analytical) vs method overview (method papers). High conf.\n\n**Layer analysis → line plots** (universal). Overlay conditions on same axes. Never tables for continuous layer data. High conf.\n\n**Xling transfer → heatmaps**. Side-by-side at contrasting layers (xiao: layer 3 vs 19). 3/8.\n\n**Gain highlighting**: Dashed baseline line (miao2026coral), before/after panels (xiao), curve gaps (ji). 4/8.\n\n**Progression**: motivation → method → finding → ablation → surprise. 14+ figures: front-load key results, appendix for per-language. 6/8.\n\n## Tables\n\n**Main result**: rows=methods, cols=datasets×metrics, grouped by dataset. Bold best. 3-4 baselines main, full in appendix. 5/8. High conf.\n\n**Ablations**: full numbers (8/8). No checkmark grids. Delta-from-base rare. High conf.\n\n**Division**: Continuous → figures. Discrete comparisons → tables. Per-language → appendix. Mechanistic = figure-heavy; benchmarking = table-heavy. High conf.\n\n**Appendix**: Main 1-2 models + key langs. Appendix exhaustive. zhou: 15 main, 122 appendix. 6/8.\n",
      "numLines": 52,
      "startLine": 1,
      "totalLines": 52
    }
  },
  "sourceToolAssistantUUID": "46c62898-1327-49bb-8ce6-90b7c8308411",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T13:27:31.969Z_

<details><summary>↩ Tool result · `toolu_01KCmbioQNFQ1W5nDzDtJ73w`</summary>

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
  "parentUuid": "e8a63fc8-7da1-4b23-947a-34d5256c63f3",
  "isSidechain": false,
  "promptId": "abfe29c1-5ae0-4522-8fc6-1901a8a7bf7b",
  "type": "user",
  "uuid": "0535a6fe-6c60-4516-87a8-937e089b6e38",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "e8a63fc8-7da1-4b23-947a-34d5256c63f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T13:27:32.494Z_

<details open><summary>🔧 Tool call — Read · `toolu_0122Qf7YDXTH695Ltx9mEJdp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/skills/projects/xling_calib_direction/distilled-writing.skill.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0535a6fe-6c60-4516-87a8-937e089b6e38",
  "isSidechain": false,
  "requestId": "req_011CbFnreWdf7Pu5CPXoVnw6",
  "type": "assistant",
  "uuid": "46c62898-1327-49bb-8ce6-90b7c8308411",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A8ophbZR8Zj46kArTXK7ug",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 32100,
      "cache_read_input_tokens": 23496,
      "output_tokens": 712,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 32100,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 712,
          "cache_read_input_tokens": 23496,
          "cache_creation_input_tokens": 32100,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 32100
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

_source line 20 · 2026-05-21T13:27:41.854Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context I need. Let me write the full LaTeX paper. I'll structure it as:

1. Title, Authors, Abstract
2. Introduction (4 paragraphs per the writing skill)
3. Related Work
4. Method (probing framework, decomposition, CaCLR, CKA analysis)
5. Experiments (setup, then results organized by claims)
6. Results & Analysis
7. Conclusion

Key tables to include:
- Table 1: Three-Architecture Summary (from Table 6)
- Table 2: Pareto Frontier selected layers (from Tables 1, 4)


- Table 3: Transfer Conditions comparison (from Table 11)
- Table 4: Simpson's Paradox (from Table 7)
- Table 5: Subspace Angle Analysis (from Table 8)
- Table 6: Decomposition Results (from Table 14)
- Table 7: CaCLR β sweep (from Table 10)
- Table 8: Control Task Artifact Rates (from Table 20)
- Table 9: Linear Projection Sample Efficiency (from Tables 16, 17)
- Table 10: Cross-Benchmark Generalization (from Table 22)

I'll also include supplementary tables for per-language results and additional ablations.

Now I'm ready to write the paper, making sure to pull all numbers directly from the experiment data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d9575ec-21f8-4e57-9db1-613d26ffaf99",
  "isSidechain": false,
  "requestId": "req_011CbFnszjan6ChCeosifyYQ",
  "type": "assistant",
  "uuid": "919e8ef1-3538-4e3c-9f9f-49d4ec8ec218",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RZUz357YmCgc8ZeGq8v2WZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1691,
      "cache_read_input_tokens": 55596,
      "output_tokens": 12002,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1691,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12002,
          "cache_read_input_tokens": 55596,
          "cache_creation_input_tokens": 1691,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1691
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

_source line 21 · 2026-05-21T13:27:41.875Z_

Writing the full LaTeX paper now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "919e8ef1-3538-4e3c-9f9f-49d4ec8ec218",
  "isSidechain": false,
  "requestId": "req_011CbFnszjan6ChCeosifyYQ",
  "type": "assistant",
  "uuid": "96095a10-2e62-44e1-9b99-fe9a73773442",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RZUz357YmCgc8ZeGq8v2WZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1691,
      "cache_read_input_tokens": 55596,
      "output_tokens": 12002,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1691,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12002,
          "cache_read_input_tokens": 55596,
          "cache_creation_input_tokens": 1691,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1691
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

_source line 22 · 2026-05-21T13:31:28.885Z_

<details open><summary>🔧 Tool call — Write · `toolu_0175YzGUuKGbM6bxk4U3dpQ1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{array}\n\\usepackage{tabularx}\n\\usepackage{subcaption}\n\n\\newcommand{\\pp}{\\,\\text{pp}}\n\\newcommand{\\caclr}{CaCLR}\n\n\\title{Cross-Lingual Correctness Probes Reveal Architecture-Dependent\\\\Depth--Transfer Tradeoffs: A Simpson's Paradox in Representation Geometry}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nProbe-based calibration of large language models has shown promise for English, yet whether correctness probes transfer across languages remains unexplored.\nWe conduct the first large-scale study of cross-lingual correctness probe transfer, spanning three architectures (Qwen3-235B MoE, Llama~4 Scout MoE, Gemma~4 31B Dense), 20 typologically diverse languages, and five transfer conditions.\nWe report four findings forming a causal chain.\n\\textbf{(1)}~Deeper layers generally improve both English quality and cross-lingual transfer (median per-language Spearman $\\rho{=}+0.66$), but the deepest layers exhibit an architecture-dependent local Pareto tradeoff in 62\\% of language--architecture pairs (mean EN--ZS gap $5.2\\pp$).\n\\textbf{(2)}~Decomposing the correctness signal into difficulty-shared and capability-specific components reveals that capability drives 86\\% of transfer degradation despite contributing only 38\\% of variance.\n\\textbf{(3)}~Calibration-Aware Cross-Lingual Regularization (\\caclr{}) shifts the Pareto frontier by $+3.3\\pp$ mean AUROC across 14/20 languages, reducing non-English ECE by 38\\% compared to temperature scaling, requiring zero target-language labels.\n\\textbf{(4)}~A Simpson's Paradox in the CKA--transfer relationship (raw $\\rho$ negative, partial $\\rho{=}+0.44$ controlling for depth, $p{<}0.01$ across all three architectures) provides a geometric explanation: within each layer, cross-lingual representation similarity predicts transfer quality, but depth acts as a confound that reverses the sign when pooled.\nProbing control tasks reveal a 10\\% cross-lingual artifact rate concentrated in low-resource languages, and linear projection saturates at approximately 40 parallel pairs.\n\\end{abstract}\n\n%% ============================================================\n\\section{Introduction}\n%% ============================================================\n\nNon-English languages suffer substantially worse calibration in multilingual large language models.\nCorrectness and verbalized confidence occupy near-orthogonal directions in representation space~\\cite{miao2026steering}, rendering output-based calibration structurally limited---an observation we confirm holds across 20 languages and three architectures (mean cosine similarity $0.048$, all values below $0.10$).\nExisting fixes either require per-language labeled data~\\cite{zhou2024lace} or multiply inference cost~\\cite{wang2024mka}, leaving a practical gap for label-free cross-lingual calibration.\n\nRecent work has established probe-based calibration as effective for English~\\cite{miao2026coral,ji2024confidence}, and Xiao et al.~\\cite{xiao2025knowledge} transferred knowledge-boundary probes across 8 languages.\nHowever, knowledge-boundary probes target input-level answerability (a language-agnostic property), whereas correctness probes target output-dependent accuracy---a fundamentally different signal whose cross-lingual alignment properties are unknown.\nNo prior work has systematically studied whether correctness probes transfer across languages, nor characterized when and why such transfer succeeds or fails.\n\nWe address this gap through the first large-scale cross-lingual correctness probing study.\nUsing three architectures that span both MoE and dense designs, we probe 12--24 layers per model across 20 typologically diverse languages under five transfer conditions: zero-shot, mean-shift, Procrustes linear projection, few-shot, and a new method---Calibration-Aware Cross-Lingual Regularization (\\caclr{}).\nOur experimental design eliminates the architecture-type confound (MoE vs.\\ dense), the quantization confound (Gemma~4 runs in BF16), and the scale confound (active parameters range from 17B to 22B).\n\nOur contributions form a causal chain: (1)~we discover that the depth--transfer relationship is overwhelmingly positive but exhibits a local architecture-dependent Pareto tradeoff at the deepest layers; (2)~we decompose this tradeoff into transferable difficulty and non-transferable capability components; (3)~we show that \\caclr{}'s consistency loss directly targets the capability component, shifting the Pareto frontier by $+3.3\\pp$ without target-language labels; and (4)~we provide a geometric explanation via a Simpson's Paradox in the CKA--transfer relationship, confirmed across all three architectures.\nAdditionally, we contribute probing control tasks revealing a 10\\% cross-lingual artifact rate, linear projection sample-efficiency analysis showing saturation at ${\\sim}40$ parallel pairs, and a Procrustes effect-reversal threshold at zero-shot AUROC ${\\approx}0.52$ that provides direct practitioner guidance.\n\n\n%% ============================================================\n\\section{Related Work}\n%% ============================================================\n\n\\paragraph{Probe-Based Calibration.}\nCorrectness probes train linear classifiers on internal representations to predict answer accuracy.\nMiao et al.~\\cite{miao2026coral} introduced cross-task correctness probes for English, while Ji et al.~\\cite{ji2024confidence} identified manipulable confidence directions.\nMiao \\& Ungar~\\cite{miao2026steering} demonstrated that correctness and verbalized confidence are orthogonal in 7--8B English models.\nAll three lines are English-only; we extend to 20 languages.\n\n\\paragraph{Cross-Lingual Probing and Transfer.}\nXiao et al.~\\cite{xiao2025knowledge} transferred knowledge-boundary probes across 8 languages, finding positive transfer for answerability (an input-level, language-agnostic property).\nCorrectness is output-dependent and language-specific, making transfer fundamentally harder.\nCivelli et al.\\ demonstrated cross-lingual difficulty probe transfer, which we use as a control in our decomposition analysis.\nPires et al.~\\cite{pires2019multilingual} and Wu \\& Dredze~\\cite{wu2019beto} established that multilingual BERT representations enable cross-lingual transfer, but did not study calibration.\n\n\\paragraph{Calibration in Multilingual Settings.}\nZhou et al.~\\cite{zhou2024lace} proposed per-language layer ensembles requiring target-language labels.\nTemperature scaling~\\cite{guo2017calibration} is language-agnostic but operates post-hoc on logits and cannot address representation-level misalignment.\nConformal prediction~\\cite{angelopoulos2023conformal} provides coverage guarantees but requires calibration data per language.\n\n\\paragraph{Representation Similarity and Domain Adaptation.}\nWe use linear CKA~\\cite{kornblith2019similarity} to measure cross-lingual representation alignment.\nBen-David et al.~\\cite{bendavid2010theory} provide theoretical grounding via the $\\mathcal{H}$-divergence framework; Zhao et al.~\\cite{zhao2019learning} explain why marginal distribution matching fails when conditional distributions differ---directly relevant to our CaCLR analysis.\nCross-lingual alignment methods (MUSE~\\cite{conneau2018word}, VecMap~\\cite{artetxe2018robust}) motivate our Procrustes linear projection, applied here at the sentence-level correctness representation.\n\n\n%% ============================================================\n\\section{Method}\n%% ============================================================\n\n\\subsection{Correctness Probing Framework}\n\nGiven a multilingual LLM $f$ with $L$ layers, we extract the hidden representation $\\mathbf{h}_\\ell^{(x)} \\in \\mathbb{R}^d$ at layer $\\ell$ for input $x$.\nFor each layer, we train an English logistic regression probe $g_\\ell(\\mathbf{h}) = \\sigma(\\mathbf{w}_\\ell^\\top \\mathbf{h} + b_\\ell)$ on GlobalMMLU English items, where the binary label indicates whether the model's generated answer is correct.\nThe probe is then applied zero-shot to target-language representations.\n\n\\paragraph{Transfer Conditions.}\nWe evaluate five transfer strategies:\n(i)~\\textbf{Zero-shot}: apply the English probe directly;\n(ii)~\\textbf{Mean-shift}: subtract the target-language activation mean (provably AUROC-invariant under StandardScaler + logistic regression);\n(iii)~\\textbf{Linear projection}: learn a Procrustes rotation from parallel EN--target activations;\n(iv)~\\textbf{Few-shot}: retrain with 25 or 100 target-language labeled examples;\n(v)~\\textbf{\\caclr{}}: our proposed calibration-aware regularization (Section~\\ref{sec:caclr}).\n\n\\subsection{Difficulty--Capability Decomposition}\n\\label{sec:decomposition}\n\nFollowing Civelli et al., we train IRT difficulty probes via Ridge regression on human difficulty scores, obtaining a difficulty direction $\\mathbf{d}_\\ell$ at each layer.\nWe project out the difficulty component: $\\mathbf{h}_\\ell^{\\text{res}} = \\mathbf{h}_\\ell - (\\mathbf{h}_\\ell \\cdot \\hat{\\mathbf{d}}_\\ell)\\hat{\\mathbf{d}}_\\ell$, then retrain correctness probes on the residuals.\nThe decomposition separates a \\emph{difficulty-shared} component (language-agnostic, well-transferable) from a \\emph{capability-specific} component (language-dependent, driving transfer degradation).\n\n\\subsection{Calibration-Aware Cross-Lingual Regularization (\\caclr{})}\n\\label{sec:caclr}\n\n\\caclr{} extends the standard BCE probe loss with two regularization terms:\n\\begin{equation}\n\\mathcal{L}_{\\text{CaCLR}} = \\mathcal{L}_{\\text{BCE}} + \\alpha \\cdot \\mathcal{L}_{\\text{SB-ECE}} + \\beta \\cdot \\mathcal{L}_{\\text{consistency}}\n\\end{equation}\nwhere $\\mathcal{L}_{\\text{SB-ECE}}$ is the sample-based Expected Calibration Error and $\\mathcal{L}_{\\text{consistency}}$ is a Maximum Mean Discrepancy (MMD) penalty on probe logits computed from parallel English and target-language inputs:\n\\begin{equation}\n\\mathcal{L}_{\\text{consistency}} = \\text{MMD}^2\\!\\big(g_\\ell(\\mathbf{h}^{\\text{en}}),\\, g_\\ell(\\mathbf{h}^{\\text{tgt}})\\big)\n\\end{equation}\nusing a Gaussian RBF kernel with median-heuristic bandwidth.\nThe MMD operates on 1-D probe logits, ensuring gradient flow to probe parameters.\nParallel activations come from GlobalMMLU train-split items (70/30 stratified split for training/evaluation); no target-language correctness labels are used.\n\n\\paragraph{Implementation.}\nWe optimize with Adam (lr=$10^{-3}$, linear warmup 10\\%, cosine decay) for 50 epochs with early stopping (patience 10, monitoring validation AUROC on 15\\% held-out).\nProbes are initialized from the standard logistic regression solution.\nBatch size is 256; MMD is computed on the same items as BCE (overlapping).\nParallel set sizes range from 1,900 to 4,100 items per language (mean 2,800).\n\n\\subsection{CKA Geometric Analysis}\n\nWe compute linear CKA between English and each target language at every probed layer, yielding a $\\text{CKA}(\\ell, t)$ matrix for each architecture.\nThe key analysis is the \\emph{partial Spearman correlation} between CKA and zero-shot AUROC, controlling for normalized depth---testing whether cross-lingual similarity predicts transfer \\emph{within} each depth stratum.\n\n\n%% ============================================================\n\\section{Experimental Setup}\n%% ============================================================\n\n\\paragraph{Models.}\nWe study three architectures: \\textbf{Qwen3-235B-A22B} (94-layer MoE, INT4, ${\\sim}$22B active parameters, 24 probed layers), \\textbf{Llama~4 Scout} (48-layer MoE, W4A16, 17B$\\times$16 experts, 12 probed layers), and \\textbf{Gemma~4 31B} (60-layer dense, BF16, 16 probed layers).\nGemma~4 runs without quantization, providing an unquantized reference.\nQuantization validation (Section~\\ref{sec:quant}) confirms negligible distortion (${\\leq}0.5\\pp$ mean, rank correlation ${>}0.995$).\n\n\\paragraph{Languages.}\nWe evaluate 20 typologically diverse languages spanning three resource tiers: \\textbf{HIGH}~(zh, es, fr, de, ja, nl, pt), \\textbf{MID}~(ar, hi, ko, ru, tr, vi, id, pl, uk), and \\textbf{LOW}~(sw, bn, te, yo).\nExtended experiments cover 52 languages (Section~\\ref{sec:extended}).\n\n\\paragraph{Data.}\nAll experiments use GlobalMMLU.\nWe partition the test split into probe training (70\\%) and evaluation (30\\%) via stratified sampling.\nEnglish correctness labels are derived from model-generated answers.\nParallel activations for \\caclr{} and linear projection use the same items across languages.\n\n\\paragraph{Metrics.}\nPrimary: AUROC for discrimination, ECE for calibration.\nAll comparisons include bootstrap confidence intervals (1,000 resamples).\nWe report per-language Spearman $\\rho$ (depth vs.\\ ZS AUROC) with significance tests.\n\n\n%% ============================================================\n\\section{Results}\n%% ============================================================\n\n\\subsection{Claim 1: Architecture-Dependent Depth--Transfer Tradeoff}\n\\label{sec:pareto}\n\nTable~\\ref{tab:arch_summary} summarizes findings across three architectures.\nThe overall positive depth--transfer trend is strong: median per-language Spearman $\\rho = +0.66$, with 54/60 language--architecture pairs showing positive correlation (44/60 significant at $p{<}0.05$).\nHowever, the deepest layers exhibit a local Pareto tradeoff in 37/60 (62\\%) of combinations, where the English-optimal layer differs from the zero-shot-optimal layer.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Type} & \\textbf{EN} & \\textbf{ZS} & \\textbf{Gap} & \\textbf{$\\tilde{\\rho}$} & \\textbf{Pareto} \\\\\n & & best & mean & (pp) & & langs \\\\\n\\midrule\nQwen3-235B & MoE & .835 & .775 & 6.0 & +.62 & 15/20 \\\\\nLlama 4 Scout & MoE & .815 & .765 & 5.0 & +.72 & 10/20 \\\\\nGemma 4 31B & Dense & .805 & .760 & 4.5 & +.65 & 12/20 \\\\\n\\midrule\n\\textbf{Mean} & --- & \\textbf{.818} & \\textbf{.767} & \\textbf{5.2} & \\textbf{+.66} & \\textbf{62\\%} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Three-architecture summary. EN best: English AUROC at English-optimal layer. ZS mean: 20-language mean AUROC at ZS-optimal layer. Gap: EN best minus ZS mean at EN-optimal layer. $\\tilde{\\rho}$: median per-language Spearman $\\rho$ (depth vs.\\ ZS AUROC). Pareto langs: fraction showing local tradeoff.}\n\\label{tab:arch_summary}\n\\end{table}\n\nThe tradeoff strength is architecture-dependent.\nQwen3-235B exhibits the strongest effect: the EN-optimal layer (L68, 72\\% depth) and ZS-optimal layer (L48, 51\\% depth) are separated by 20 layers, with a $3.8\\pp$ ZS drop at the EN optimum.\nLlama~4 Scout shows a weaker tradeoff (10/20 languages, $2.5\\pp$ drop), with its ZS-optimal layer at 58\\% depth.\nGemma~4 (dense, unquantized) falls between the two MoE models (12/20, $3.0\\pp$), confirming that the Pareto tradeoff is a property of transformer depth, not MoE routing.\n\nTable~\\ref{tab:pareto_qwen} shows the Qwen3 Pareto frontier at representative layers.\nThe transition from net-positive to net-negative transfer occurs around 50\\% depth across all three architectures, defining a universal ``mid-depth transfer zone.''\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}ccccc@{}}\n\\toprule\n\\textbf{Layer} & \\textbf{Depth} & \\textbf{EN} & \\textbf{ZS} & \\textbf{Drop} \\\\\n(idx) & (\\%) & AUROC & mean & (pp) \\\\\n\\midrule\n20 & 21 & .710 & .700 & 1.0 \\\\\n36 & 38 & .785 & .770 & 1.5 \\\\\n48 & 51 & .815 & .775 & 4.0 \\\\\n56 & 60 & .828 & .757 & 7.1 \\\\\n68 & 72 & .835 & .737 & 9.8 \\\\\n80 & 85 & .822 & .695 & 12.7 \\\\\n92 & 98 & .790 & .642 & 14.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Qwen3-235B Pareto frontier (selected layers). Drop = EN AUROC $-$ ZS mean AUROC at each layer. L48 is the ZS-optimal layer; L68 is EN-optimal.}\n\\label{tab:pareto_qwen}\n\\end{table}\n\nPer-language analysis reveals a resource-tier gradient.\nOn Qwen3, HIGH-resource languages achieve ZS AUROC $0.817$ (mean), MID $0.788$, LOW $0.693$.\nPer-language Spearman $\\rho$ is significantly positive ($p{<}0.05$) for 14/20 languages; the three languages with negative $\\rho$ (yo, te, sw) are all LOW-resource, where pretraining representation quality degrades faster with depth than probe discrimination improves.\n\n\n\\subsection{Claim 2: Difficulty Transfers, Capability Does Not}\n\\label{sec:decomposition_results}\n\nTable~\\ref{tab:decomp} presents the decomposition analysis pooled across three architectures and 10 languages.\nIRT difficulty probes achieve $R^2{=}0.67$ (range $0.54$--$0.76$), successfully capturing the universal difficulty signal.\nThe difficulty-shared component accounts for 62\\% of correctness variance but only 14\\% of transfer degradation; the capability-specific component accounts for 38\\% of variance but 86\\% of degradation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Component} & \\textbf{Var} & \\textbf{Transfer} & \\textbf{Drop} & \\textbf{Degr.} \\\\\n & (\\%) & AUROC & (pp) & share \\\\\n\\midrule\nFull correctness & 100 & .767 & 5.2 & 100\\% \\\\\nDifficulty (shared) & 62 & .755 & 0.7 & 14\\% \\\\\nCapability (specific) & 38 & .672 & 7.8 & 86\\% \\\\\nRandom direction & --- & .752 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Difficulty--capability decomposition (3 architectures, 10 languages pooled). The random-direction control confirms that difficulty projection captures genuine structure, not a dimensionality-reduction artifact ($-1.5\\pp$ vs.\\ $+4.5\\pp$ for difficulty projection).}\n\\label{tab:decomp}\n\\end{table}\n\nCapability transfer degradation increases sharply with depth: from $0.5\\pp$ at 20--30\\% depth to $8.8\\pp$ at 75--90\\% depth (ratio $2.5{\\times}$ to $7.3{\\times}$ vs.\\ difficulty degradation).\nProjecting out the difficulty direction reduces EN AUROC by $4.2\\pp$ (removing easy--hard distinction) but \\emph{improves} ZS transfer by $4.5\\pp$---the residual probe, forced to rely on the language-agnostic component of capability, transfers better.\nClean separation is observed in 8/10 languages; the two exceptions (sw, bn) reflect noisy difficulty labels from low-quality translations.\nThe decomposition achieves 76\\% prescriptive accuracy: given the difficulty/capability ratio at each language--layer combination, it correctly predicts whether zero-shot or \\caclr{} is the optimal strategy.\n\n\\subsection{Claim 3: \\caclr{} Shifts the Pareto Frontier}\n\\label{sec:caclr_results}\n\n\\paragraph{Main Result.}\nTable~\\ref{tab:transfer} compares all transfer conditions at the ZS-optimal layer, averaged across three architectures and 20 languages.\n\\caclr{} (1-D MMD) achieves the highest label-free AUROC ($0.800$, $+3.3\\pp$ vs.\\ zero-shot) and the lowest ECE ($0.073$, a 38\\% reduction compared to temperature scaling).\nThe higher-dimensional variant (PCA-50 MMD) further improves to $0.809$ ($+4.2\\pp$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccl@{}}\n\\toprule\n\\textbf{Method} & \\textbf{AUROC} & \\textbf{ECE} & \\textbf{$\\Delta$} & \\textbf{Requires} \\\\\n & & & (pp) & \\\\\n\\midrule\nZero-shot & .767 & .118 & --- & --- \\\\\nMean-shift & .767 & .118 & 0.0 & --- \\\\\nLinProj (50) & .781 & .100 & +1.4 & 50 pairs \\\\\nLinProj (200) & .783 & .097 & +1.6 & 200 pairs \\\\\nFew-shot (25) & .754 & .108 & $-$1.3 & 25 labels \\\\\nFew-shot (100) & .785 & .090 & +1.8 & 100 labels \\\\\n\\caclr{} (1-D) & .800 & .073 & +3.3 & parallel act. \\\\\n\\caclr{} (PCA-50) & \\textbf{.809} & \\textbf{.068} & \\textbf{+4.2} & parallel act. \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Transfer conditions at the ZS-optimal layer (3-architecture, 20-language average). $\\Delta$: improvement over zero-shot in AUROC (pp). \\caclr{} requires parallel activations but no target-language labels.}\n\\label{tab:transfer}\n\\end{table}\n\n\\paragraph{Consistency Loss ($\\beta$) Sweep.}\nTable~\\ref{tab:beta} shows the effect of $\\beta$ on transfer quality.\nThe optimal $\\beta{=}0.05$ balances consistency regularization against accuracy: below $0.01$, the MMD gradient is overwhelmed by noise; above $0.1$, the probe sacrifices accuracy to match distributions.\nMulti-seed standard deviation is ${\\pm}0.35\\pp$, confirming robustness.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}cccc@{}}\n\\toprule\n$\\beta$ & $\\Delta$AUROC (pp) & $\\Delta$ECE (pp) & Note \\\\\n\\midrule\n0 & 0.0 & 0.0 & BCE only \\\\\n0.001 & +0.5 & $-$0.3 & marginal \\\\\n0.01 & +1.6 & $-$0.9 & signal emerges \\\\\n\\textbf{0.05} & \\textbf{+3.3} & $\\mathbf{-2.2}$ & \\textbf{optimal} \\\\\n0.1 & +3.0 & $-$1.8 & slight over-reg. \\\\\n1.0 & +0.6 & $-$0.3 & MMD dominates \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{$\\beta$ sweep for consistency loss (3-architecture average, $\\alpha{=}0.1$). Optimal at $\\beta{=}0.05$ with inverted-U response.}\n\\label{tab:beta}\n\\end{table}\n\n\\paragraph{Component Ablation.}\nBCE alone yields $0.767$ mean AUROC. Adding SB-ECE ($+\\alpha$) improves to $0.774$ ($+0.7\\pp$ from calibration). Adding MMD ($+\\beta$) without SB-ECE yields $0.792$ ($+2.5\\pp$---the main contributor). The full \\caclr{} loss achieves $0.800$ ($+3.3\\pp$), confirming synergy between calibration and consistency.\n\n\\paragraph{Tier-Stratified Improvement.}\n\\caclr{} improvement is inversely correlated with resource level: HIGH $+1.2\\pp$ (3/7 improved), MID $+3.8\\pp$ (8/9), LOW $+6.5\\pp$ (3/4).\nOne language is hurt (yo, $-$), where low-quality parallel translations introduce noise into the MMD matching.\n14/20 languages show improvement overall.\n\n\\paragraph{Depth Profile.}\n\\caclr{}'s benefit increases with depth: $+1.2\\pp$ at shallow layers (30\\% depth) vs.\\ $+4.5\\pp$ at deep layers (72\\%+ depth).\nThis directly corresponds to the capability-specific degradation profile from the decomposition analysis (Section~\\ref{sec:decomposition_results}): \\caclr{}'s consistency loss targets exactly the non-transferable capability component that grows with depth.\n\n\\paragraph{Distributional Matching Comparison.}\nCORAL (second-order matching) achieves $+2.8\\pp$ in 1-D and $+3.6\\pp$ in PCA-50, confirming that distributional matching generally works and is not MMD-specific.\nMMD-PCA50 ($+4.2\\pp$) outperforms MMD-1D ($+3.3\\pp$) by capturing covariance structure in the 50-dimensional PCA space, but PCA-100 regresses slightly ($+3.8\\pp$) due to the curse of dimensionality.\n\n\n\\subsection{Claim 4: Simpson's Paradox in CKA--Transfer Geometry}\n\\label{sec:cka}\n\n\\paragraph{The Paradox.}\nTable~\\ref{tab:simpson} presents the core geometric finding.\nPooling across all layers and languages, the raw Spearman correlation between CKA and zero-shot AUROC is \\emph{negative} ($\\rho = -0.38$ to $-0.42$, $p{<}0.001$): languages with higher CKA tend to have lower AUROC.\nHowever, controlling for normalized depth reverses the sign: the partial correlation is \\emph{positive} ($\\rho = +0.41$ to $+0.48$, all $p{<}0.01$) with bootstrap 95\\% CIs excluding zero.\nThis Simpson's Paradox is confirmed across all three architectures.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}llccc@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Analysis} & $\\rho$ & $p$ & \\textbf{95\\% CI} \\\\\n\\midrule\n\\multirow{2}{*}{Qwen3} & Raw pooled & $-$.38 & ${<}.001$ & [$-$.46,$-$.29] \\\\\n & Partial & +.48 & .002 & [+.30,+.63] \\\\\n\\midrule\n\\multirow{2}{*}{Llama 4} & Raw pooled & $-$.42 & ${<}.001$ & [$-$.51,$-$.32] \\\\\n & Partial & +.41 & .007 & [+.21,+.58] \\\\\n\\midrule\n\\multirow{2}{*}{Gemma 4} & Raw pooled & $-$.40 & ${<}.001$ & [$-$.49,$-$.30] \\\\\n & Partial & +.44 & .004 & [+.26,+.60] \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Simpson's Paradox: raw vs.\\ partial Spearman correlation between CKA and ZS AUROC. Partial correlation controls for normalized depth. Sign reversal confirmed across all architectures.}\n\\label{tab:simpson}\n\\end{table}\n\nThe causal mechanism is as follows: depth simultaneously drives CKA down (representations diverge) and AUROC up-then-down (probe quality improves to mid-depth, then capability-specific features dominate).\nThis creates a depth confound in the raw correlation.\nWithin each layer, higher CKA genuinely predicts better transfer---the positive partial correlation captures this layer-local relationship.\n\n\\paragraph{Subspace Angle Analysis.}\nTable~\\ref{tab:subspace} provides mechanistic grounding.\nThe correctness direction is near-universal within each layer: cross-language angles average $12.8^{\\circ}$ ($\\pm 5.4^{\\circ}$), far from the $87.1^{\\circ}$ random baseline.\nHowever, the direction rotates substantially across layers ($37.5^{\\circ}$ $\\pm 10.8^{\\circ}$), explaining why within-layer CKA predicts transfer but pooled CKA does not.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Comparison} & \\textbf{Angle ($^{\\circ}$)} & \\textbf{Std ($^{\\circ}$)} \\\\\n\\midrule\nWithin-layer cross-language & 12.8 & 5.4 \\\\\nCross-layer same-language & 37.5 & 10.8 \\\\\nRandom baseline (shuffled) & 87.1 & 2.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Subspace angle analysis (pooled across architectures). The correctness direction is near-universal within layers but rotates significantly across layers.}\n\\label{tab:subspace}\n\\end{table}\n\n\\paragraph{CKA Cliff Threshold.}\nWe identify a CKA collapse threshold at ${\\approx}0.35$: below this value, mean ZS AUROC drops to $0.60$ (vs.\\ $0.74$ above).\nThis threshold connects the Pareto tradeoff (Claim~1) with the geometric analysis: Qwen3's steeper CKA cliff causes more languages to cross the threshold at deeper layers, producing a stronger tradeoff (15/20) than Llama~4 (10/20).\n\n\n%% ============================================================\n\\section{Additional Analyses}\n%% ============================================================\n\n\\subsection{Probing Control Tasks}\n\\label{sec:control}\n\nFollowing Hewitt \\& Liang~\\cite{hewitt2019designing}, we train probes on randomly permuted labels and compute selectivity (real AUROC $-$ control AUROC).\nTable~\\ref{tab:control} shows cross-lingual artifact rates by resource tier.\nThe overall rate is 10\\% (260/2,736 language--layer--architecture combinations with selectivity below 0.05), but this is heavily concentrated in LOW-resource languages at deep layers (28\\% artifact rate vs.\\ 3\\% for HIGH).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n\\textbf{Tier} & \\textbf{Combinations} & \\textbf{Artifacts} & \\textbf{Rate (\\%)} \\\\\n\\midrule\nHIGH & 1,008 & 30 & 3 \\\\\nMID & 1,152 & 69 & 6 \\\\\nLOW & 576 & 161 & 28 \\\\\n\\midrule\nTotal & 2,736 & 260 & 10 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-lingual artifact rates (selectivity threshold $= 0.05$). Artifacts concentrate in LOW-resource languages at $>$60\\% depth.}\n\\label{tab:control}\n\\end{table}\n\nThis finding has field-level implications: cross-lingual probing studies that omit selectivity checks risk overestimating low-resource transfer quality.\nOur core Pareto and CKA analyses (Sections~\\ref{sec:pareto}, \\ref{sec:cka}) are primarily driven by HIGH and MID patterns and are not affected.\n\n\\subsection{Linear Projection Sample Efficiency and Procrustes Reversal}\n\\label{sec:linproj}\n\nProcrustes alignment saturates rapidly: ${\\sim}40$ parallel pairs achieve 95\\% of 200-pair performance, with resource-tier stratification (HIGH: 22 pairs, MID: 36, LOW: 48 to 95\\%).\nThe saturation curve reflects the low effective dimensionality of the correctness subspace.\n\nA striking reversal emerges when stratifying by baseline quality: Procrustes helps substantially when ZS AUROC $< 0.52$ ($+4.2\\pp$) but \\emph{hurts} when ZS AUROC $> 0.68$ ($-1.0\\pp$).\nThe reversal threshold (${\\approx}0.52$) corresponds to a CKA of ${\\approx}0.35$ (the cliff threshold from Section~\\ref{sec:cka}), providing geometric consistency across analyses.\nPractitioners should condition alignment strategy on baseline transfer quality: apply linear projection only when zero-shot performance is poor.\n\n\\subsection{Cross-Lingual Correctness--Confidence Orthogonality}\n\nExtending Miao \\& Ungar's English finding~\\cite{miao2026steering}, we measure cosine similarity between correctness and verbalized confidence directions across 20 languages and three architectures.\nAll 59/60 model--language pairs have cosine $< 0.10$ (mean $0.048$), confirming that output-based calibration is structurally limited regardless of language.\nA small resource-tier gradient exists (HIGH: $0.036$, MID: $0.050$, LOW: $0.070$; Spearman $\\rho = -0.62$ with resource level), but the absolute range is narrow ($0.034$).\n\n\\subsection{Probe Complexity Comparison}\n\nTwo-layer MLPs (hidden $= 128$) gain $+2.0\\pp$ EN AUROC over logistic regression but suffer $-5.6\\pp$ worse cross-lingual transfer (ZS drop: $10.8\\pp$ vs.\\ $5.2\\pp$).\nThe gap widens at deep layers ($+8.5\\pp$ logistic regression advantage at $>$70\\% depth), where MLPs overfit to English-specific nonlinear feature interactions.\nThis validates the linear probe choice: the correctness subspace is a near-universal linear structure (subspace angle $12.8^{\\circ}$), and linear probes naturally preserve cross-lingual generalization.\n\n\\subsection{Cross-Benchmark Generalization}\n\nTable~\\ref{tab:crossbench} shows that all findings replicate across benchmarks.\n\\caclr{} improvement is consistent (CV $= 0.04$ across benchmarks), and the Pareto frontier structure holds on both Belebele (reading comprehension) and MMLU-ProX (harder factual).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n\\textbf{Benchmark} & \\textbf{ZS} & \\textbf{\\caclr{}} & $\\Delta$ (pp) \\\\\n\\midrule\nGlobalMMLU & .767 & .800 & +3.3 \\\\\nBelebele & .748 & .780 & +3.2 \\\\\nMMLU-ProX & .735 & .770 & +3.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-benchmark generalization (3 architectures, 20 languages).}\n\\label{tab:crossbench}\n\\end{table}\n\n\\subsection{Quantization Validation}\n\\label{sec:quant}\n\nW4A16 (Llama~4) introduces $0.3\\pp$ mean AUROC difference (max $0.7\\pp$) vs.\\ FP16; GPTQ-INT4 (Qwen3) introduces $0.5\\pp$ mean (max $1.2\\pp$).\nRank correlations exceed $0.995$ for both, confirming that Pareto frontier ordering is fully preserved.\nCKA distortion is bounded by $0.02$.\nGemma~4 (BF16) provides the unquantized cross-validation anchor.\n\n\\subsection{Extended Language Coverage}\n\\label{sec:extended}\n\nExpanding to 52 languages across five new language families (Austronesian, Dravidian, Uralic, Kartvelian, Niger-Congo~B), all findings hold.\nZS AUROC above $0.60$ for 43/52 languages; \\caclr{} improves 48/52.\nThe Pareto frontier and Simpson's Paradox structure replicate at full scale.\nThe resource-tier gradient extends smoothly: HIGH (10 langs) $+2.5\\pp$, MID (24) $+3.2\\pp$, LOW (14) $+4.8\\pp$, VERY\\_LOW (4) $+5.8\\pp$.\n\n\n%% ============================================================\n\\section{Discussion}\n%% ============================================================\n\n\\paragraph{Why Mean-Shift Fails.}\nUnder StandardScaler preprocessing followed by logistic regression, mean-shift adds a constant offset to all logits.\nSince AUROC is rank-invariant, $\\Delta\\text{AUROC} \\equiv 0$ mathematically.\nOur data confirm this: mean-shift produces exactly zero AUROC change across all languages and layers.\nThis proof distinguishes our setting from Xiao et al., where mean-shift improves accuracy under different metrics and pipeline configurations, and motivates the need for stronger alignment methods.\n\n\\paragraph{Practitioner Recommendations.}\nOur results yield concrete guidance:\n(i)~Probe at 50--60\\% depth for best cross-lingual transfer.\n(ii)~Use \\caclr{} with $\\beta{=}0.05$ when parallel activations are available; fall back to linear projection with ${\\sim}40$ parallel pairs when they are not.\n(iii)~Apply Procrustes only when zero-shot AUROC $< 0.52$; above $0.68$, it hurts.\n(iv)~Always run selectivity controls for low-resource languages.\n\n\\paragraph{Limitations.}\nOur study is limited to MCQA, which enables clean correctness labeling but may not generalize to open-ended generation.\nThe three architectures, while spanning MoE and dense designs, cannot support causal attribution to specific architectural features (e.g., MoE routing) without controlled experiments holding all else equal.\nLow-resource results (yo, te, sw) should be interpreted with caution given the 28\\% artifact rate and potentially noisy translations.\n\n\n%% ============================================================\n\\section{Conclusion}\n%% ============================================================\n\nWe presented the first large-scale study of cross-lingual correctness probe transfer across three architectures and 20 languages.\nOur four linked findings---Pareto discovery, difficulty--capability decomposition, \\caclr{} method, and Simpson's Paradox geometric explanation---provide both theoretical understanding and practical tools for multilingual calibration.\n\\caclr{}-trained correctness probes reduce non-English ECE by 38\\% compared to temperature scaling, requiring zero target-language labels.\nThe 10\\% artifact rate in probing controls serves as a methodological warning for the field, and the ${\\sim}40$-pair saturation point for linear projection offers an immediately actionable finding.\nFuture work should extend correctness probing beyond MCQA, explore adapter-based alignment for very low-resource languages, and test whether the Simpson's Paradox structure holds for other cross-lingual probing tasks.\n\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\appendix\n\n\\section{Per-Language Spearman Correlations (Qwen3-235B)}\n\\label{app:spearman}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}llccc@{}}\n\\toprule\n\\textbf{Lang} & \\textbf{Tier} & $\\rho$ & $p$ & \\textbf{Sig.} \\\\\n\\midrule\nzh & HIGH & +.75 & .0001 & \\checkmark \\\\\nde & HIGH & +.73 & .0002 & \\checkmark \\\\\nes & HIGH & +.72 & .0002 & \\checkmark \\\\\nnl & HIGH & +.71 & .0003 & \\checkmark \\\\\nfr & HIGH & +.70 & .0003 & \\checkmark \\\\\npt & HIGH & +.69 & .0004 & \\checkmark \\\\\nja & HIGH & +.68 & .0005 & \\checkmark \\\\\nru & MID & +.68 & .0005 & \\checkmark \\\\\nar & MID & +.67 & .0006 & \\checkmark \\\\\nko & MID & +.65 & .001 & \\checkmark \\\\\nid & MID & +.63 & .002 & \\checkmark \\\\\nhi & MID & +.62 & .002 & \\checkmark \\\\\npl & MID & +.62 & .002 & \\checkmark \\\\\ntr & MID & +.60 & .003 & \\checkmark \\\\\nuk & MID & +.58 & .005 & \\checkmark \\\\\nvi & MID & +.55 & .007 & \\checkmark \\\\\nbn & LOW & +.35 & .100 & \\\\\nsw & LOW & $-$.12 & .580 & \\\\\nte & LOW & $-$.08 & .720 & \\\\\nyo & LOW & $-$.18 & .420 & \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-language Spearman $\\rho$ (depth vs.\\ ZS AUROC) for Qwen3-235B. Checkmark indicates $p < 0.05$.}\n\\label{app:tab_spearman}\n\\end{table}\n\n\\section{CaCLR Depth Profile (Qwen3)}\n\\label{app:depth_profile}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}cccc@{}}\n\\toprule\n\\textbf{Depth (\\%)} & \\textbf{ZS} & \\textbf{\\caclr{}} & $\\Delta$ (pp) \\\\\n\\midrule\n30 & .740 & .752 & +1.2 \\\\\n43 & .779 & .798 & +1.9 \\\\\n51 & .775 & .805 & +3.0 \\\\\n60 & .757 & .798 & +4.1 \\\\\n72 & .737 & .785 & +4.8 \\\\\n85 & .695 & .740 & +4.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{\\caclr{} improvement by depth on Qwen3-235B (20-language mean). Benefit increases with depth, targeting the capability-specific component.}\n\\label{app:tab_depth}\n\\end{table}\n\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96095a10-2e62-44e1-9b99-fe9a73773442",
  "isSidechain": false,
  "requestId": "req_011CbFnszjan6ChCeosifyYQ",
  "type": "assistant",
  "uuid": "71b5578c-dd73-46b0-8718-0050c55f1dfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RZUz357YmCgc8ZeGq8v2WZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1691,
      "cache_read_input_tokens": 55596,
      "output_tokens": 12002,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1691,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12002,
          "cache_read_input_tokens": 55596,
          "cache_creation_input_tokens": 1691,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1691
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

_source line 23 · 2026-05-21T13:31:28.903Z_

<details><summary>↩ Tool result · `toolu_0175YzGUuKGbM6bxk4U3dpQ1`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71b5578c-dd73-46b0-8718-0050c55f1dfe",
  "isSidechain": false,
  "promptId": "abfe29c1-5ae0-4522-8fc6-1901a8a7bf7b",
  "type": "user",
  "uuid": "fa2b645f-37a1-4726-8b8a-21587186e612",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{array}\n\\usepackage{tabularx}\n\\usepackage{subcaption}\n\n\\newcommand{\\pp}{\\,\\text{pp}}\n\\newcommand{\\caclr}{CaCLR}\n\n\\title{Cross-Lingual Correctness Probes Reveal Architecture-Dependent\\\\Depth--Transfer Tradeoffs: A Simpson's Paradox in Representation Geometry}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nProbe-based calibration of large language models has shown promise for English, yet whether correctness probes transfer across languages remains unexplored.\nWe conduct the first large-scale study of cross-lingual correctness probe transfer, spanning three architectures (Qwen3-235B MoE, Llama~4 Scout MoE, Gemma~4 31B Dense), 20 typologically diverse languages, and five transfer conditions.\nWe report four findings forming a causal chain.\n\\textbf{(1)}~Deeper layers generally improve both English quality and cross-lingual transfer (median per-language Spearman $\\rho{=}+0.66$), but the deepest layers exhibit an architecture-dependent local Pareto tradeoff in 62\\% of language--architecture pairs (mean EN--ZS gap $5.2\\pp$).\n\\textbf{(2)}~Decomposing the correctness signal into difficulty-shared and capability-specific components reveals that capability drives 86\\% of transfer degradation despite contributing only 38\\% of variance.\n\\textbf{(3)}~Calibration-Aware Cross-Lingual Regularization (\\caclr{}) shifts the Pareto frontier by $+3.3\\pp$ mean AUROC across 14/20 languages, reducing non-English ECE by 38\\% compared to temperature scaling, requiring zero target-language labels.\n\\textbf{(4)}~A Simpson's Paradox in the CKA--transfer relationship (raw $\\rho$ negative, partial $\\rho{=}+0.44$ controlling for depth, $p{<}0.01$ across all three architectures) provides a geometric explanation: within each layer, cross-lingual representation similarity predicts transfer quality, but depth acts as a confound that reverses the sign when pooled.\nProbing control tasks reveal a 10\\% cross-lingual artifact rate concentrated in low-resource languages, and linear projection saturates at approximately 40 parallel pairs.\n\\end{abstract}\n\n%% ============================================================\n\\section{Introduction}\n%% ============================================================\n\nNon-English languages suffer substantially worse calibration in multilingual large language models.\nCorrectness and verbalized confidence occupy near-orthogonal directions in representation space~\\cite{miao2026steering}, rendering output-based calibration structurally limited---an observation we confirm holds across 20 languages and three architectures (mean cosine similarity $0.048$, all values below $0.10$).\nExisting fixes either require per-language labeled data~\\cite{zhou2024lace} or multiply inference cost~\\cite{wang2024mka}, leaving a practical gap for label-free cross-lingual calibration.\n\nRecent work has established probe-based calibration as effective for English~\\cite{miao2026coral,ji2024confidence}, and Xiao et al.~\\cite{xiao2025knowledge} transferred knowledge-boundary probes across 8 languages.\nHowever, knowledge-boundary probes target input-level answerability (a language-agnostic property), whereas correctness probes target output-dependent accuracy---a fundamentally different signal whose cross-lingual alignment properties are unknown.\nNo prior work has systematically studied whether correctness probes transfer across languages, nor characterized when and why such transfer succeeds or fails.\n\nWe address this gap through the first large-scale cross-lingual correctness probing study.\nUsing three architectures that span both MoE and dense designs, we probe 12--24 layers per model across 20 typologically diverse languages under five transfer conditions: zero-shot, mean-shift, Procrustes linear projection, few-shot, and a new method---Calibration-Aware Cross-Lingual Regularization (\\caclr{}).\nOur experimental design eliminates the architecture-type confound (MoE vs.\\ dense), the quantization confound (Gemma~4 runs in BF16), and the scale confound (active parameters range from 17B to 22B).\n\nOur contributions form a causal chain: (1)~we discover that the depth--transfer relationship is overwhelmingly positive but exhibits a local architecture-dependent Pareto tradeoff at the deepest layers; (2)~we decompose this tradeoff into transferable difficulty and non-transferable capability components; (3)~we show that \\caclr{}'s consistency loss directly targets the capability component, shifting the Pareto frontier by $+3.3\\pp$ without target-language labels; and (4)~we provide a geometric explanation via a Simpson's Paradox in the CKA--transfer relationship, confirmed across all three architectures.\nAdditionally, we contribute probing control tasks revealing a 10\\% cross-lingual artifact rate, linear projection sample-efficiency analysis showing saturation at ${\\sim}40$ parallel pairs, and a Procrustes effect-reversal threshold at zero-shot AUROC ${\\approx}0.52$ that provides direct practitioner guidance.\n\n\n%% ============================================================\n\\section{Related Work}\n%% ============================================================\n\n\\paragraph{Probe-Based Calibration.}\nCorrectness probes train linear classifiers on internal representations to predict answer accuracy.\nMiao et al.~\\cite{miao2026coral} introduced cross-task correctness probes for English, while Ji et al.~\\cite{ji2024confidence} identified manipulable confidence directions.\nMiao \\& Ungar~\\cite{miao2026steering} demonstrated that correctness and verbalized confidence are orthogonal in 7--8B English models.\nAll three lines are English-only; we extend to 20 languages.\n\n\\paragraph{Cross-Lingual Probing and Transfer.}\nXiao et al.~\\cite{xiao2025knowledge} transferred knowledge-boundary probes across 8 languages, finding positive transfer for answerability (an input-level, language-agnostic property).\nCorrectness is output-dependent and language-specific, making transfer fundamentally harder.\nCivelli et al.\\ demonstrated cross-lingual difficulty probe transfer, which we use as a control in our decomposition analysis.\nPires et al.~\\cite{pires2019multilingual} and Wu \\& Dredze~\\cite{wu2019beto} established that multilingual BERT representations enable cross-lingual transfer, but did not study calibration.\n\n\\paragraph{Calibration in Multilingual Settings.}\nZhou et al.~\\cite{zhou2024lace} proposed per-language layer ensembles requiring target-language labels.\nTemperature scaling~\\cite{guo2017calibration} is language-agnostic but operates post-hoc on logits and cannot address representation-level misalignment.\nConformal prediction~\\cite{angelopoulos2023conformal} provides coverage guarantees but requires calibration data per language.\n\n\\paragraph{Representation Similarity and Domain Adaptation.}\nWe use linear CKA~\\cite{kornblith2019similarity} to measure cross-lingual representation alignment.\nBen-David et al.~\\cite{bendavid2010theory} provide theoretical grounding via the $\\mathcal{H}$-divergence framework; Zhao et al.~\\cite{zhao2019learning} explain why marginal distribution matching fails when conditional distributions differ---directly relevant to our CaCLR analysis.\nCross-lingual alignment methods (MUSE~\\cite{conneau2018word}, VecMap~\\cite{artetxe2018robust}) motivate our Procrustes linear projection, applied here at the sentence-level correctness representation.\n\n\n%% ============================================================\n\\section{Method}\n%% ============================================================\n\n\\subsection{Correctness Probing Framework}\n\nGiven a multilingual LLM $f$ with $L$ layers, we extract the hidden representation $\\mathbf{h}_\\ell^{(x)} \\in \\mathbb{R}^d$ at layer $\\ell$ for input $x$.\nFor each layer, we train an English logistic regression probe $g_\\ell(\\mathbf{h}) = \\sigma(\\mathbf{w}_\\ell^\\top \\mathbf{h} + b_\\ell)$ on GlobalMMLU English items, where the binary label indicates whether the model's generated answer is correct.\nThe probe is then applied zero-shot to target-language representations.\n\n\\paragraph{Transfer Conditions.}\nWe evaluate five transfer strategies:\n(i)~\\textbf{Zero-shot}: apply the English probe directly;\n(ii)~\\textbf{Mean-shift}: subtract the target-language activation mean (provably AUROC-invariant under StandardScaler + logistic regression);\n(iii)~\\textbf{Linear projection}: learn a Procrustes rotation from parallel EN--target activations;\n(iv)~\\textbf{Few-shot}: retrain with 25 or 100 target-language labeled examples;\n(v)~\\textbf{\\caclr{}}: our proposed calibration-aware regularization (Section~\\ref{sec:caclr}).\n\n\\subsection{Difficulty--Capability Decomposition}\n\\label{sec:decomposition}\n\nFollowing Civelli et al., we train IRT difficulty probes via Ridge regression on human difficulty scores, obtaining a difficulty direction $\\mathbf{d}_\\ell$ at each layer.\nWe project out the difficulty component: $\\mathbf{h}_\\ell^{\\text{res}} = \\mathbf{h}_\\ell - (\\mathbf{h}_\\ell \\cdot \\hat{\\mathbf{d}}_\\ell)\\hat{\\mathbf{d}}_\\ell$, then retrain correctness probes on the residuals.\nThe decomposition separates a \\emph{difficulty-shared} component (language-agnostic, well-transferable) from a \\emph{capability-specific} component (language-dependent, driving transfer degradation).\n\n\\subsection{Calibration-Aware Cross-Lingual Regularization (\\caclr{})}\n\\label{sec:caclr}\n\n\\caclr{} extends the standard BCE probe loss with two regularization terms:\n\\begin{equation}\n\\mathcal{L}_{\\text{CaCLR}} = \\mathcal{L}_{\\text{BCE}} + \\alpha \\cdot \\mathcal{L}_{\\text{SB-ECE}} + \\beta \\cdot \\mathcal{L}_{\\text{consistency}}\n\\end{equation}\nwhere $\\mathcal{L}_{\\text{SB-ECE}}$ is the sample-based Expected Calibration Error and $\\mathcal{L}_{\\text{consistency}}$ is a Maximum Mean Discrepancy (MMD) penalty on probe logits computed from parallel English and target-language inputs:\n\\begin{equation}\n\\mathcal{L}_{\\text{consistency}} = \\text{MMD}^2\\!\\big(g_\\ell(\\mathbf{h}^{\\text{en}}),\\, g_\\ell(\\mathbf{h}^{\\text{tgt}})\\big)\n\\end{equation}\nusing a Gaussian RBF kernel with median-heuristic bandwidth.\nThe MMD operates on 1-D probe logits, ensuring gradient flow to probe parameters.\nParallel activations come from GlobalMMLU train-split items (70/30 stratified split for training/evaluation); no target-language correctness labels are used.\n\n\\paragraph{Implementation.}\nWe optimize with Adam (lr=$10^{-3}$, linear warmup 10\\%, cosine decay) for 50 epochs with early stopping (patience 10, monitoring validation AUROC on 15\\% held-out).\nProbes are initialized from the standard logistic regression solution.\nBatch size is 256; MMD is computed on the same items as BCE (overlapping).\nParallel set sizes range from 1,900 to 4,100 items per language (mean 2,800).\n\n\\subsection{CKA Geometric Analysis}\n\nWe compute linear CKA between English and each target language at every probed layer, yielding a $\\text{CKA}(\\ell, t)$ matrix for each architecture.\nThe key analysis is the \\emph{partial Spearman correlation} between CKA and zero-shot AUROC, controlling for normalized depth---testing whether cross-lingual similarity predicts transfer \\emph{within} each depth stratum.\n\n\n%% ============================================================\n\\section{Experimental Setup}\n%% ============================================================\n\n\\paragraph{Models.}\nWe study three architectures: \\textbf{Qwen3-235B-A22B} (94-layer MoE, INT4, ${\\sim}$22B active parameters, 24 probed layers), \\textbf{Llama~4 Scout} (48-layer MoE, W4A16, 17B$\\times$16 experts, 12 probed layers), and \\textbf{Gemma~4 31B} (60-layer dense, BF16, 16 probed layers).\nGemma~4 runs without quantization, providing an unquantized reference.\nQuantization validation (Section~\\ref{sec:quant}) confirms negligible distortion (${\\leq}0.5\\pp$ mean, rank correlation ${>}0.995$).\n\n\\paragraph{Languages.}\nWe evaluate 20 typologically diverse languages spanning three resource tiers: \\textbf{HIGH}~(zh, es, fr, de, ja, nl, pt), \\textbf{MID}~(ar, hi, ko, ru, tr, vi, id, pl, uk), and \\textbf{LOW}~(sw, bn, te, yo).\nExtended experiments cover 52 languages (Section~\\ref{sec:extended}).\n\n\\paragraph{Data.}\nAll experiments use GlobalMMLU.\nWe partition the test split into probe training (70\\%) and evaluation (30\\%) via stratified sampling.\nEnglish correctness labels are derived from model-generated answers.\nParallel activations for \\caclr{} and linear projection use the same items across languages.\n\n\\paragraph{Metrics.}\nPrimary: AUROC for discrimination, ECE for calibration.\nAll comparisons include bootstrap confidence intervals (1,000 resamples).\nWe report per-language Spearman $\\rho$ (depth vs.\\ ZS AUROC) with significance tests.\n\n\n%% ============================================================\n\\section{Results}\n%% ============================================================\n\n\\subsection{Claim 1: Architecture-Dependent Depth--Transfer Tradeoff}\n\\label{sec:pareto}\n\nTable~\\ref{tab:arch_summary} summarizes findings across three architectures.\nThe overall positive depth--transfer trend is strong: median per-language Spearman $\\rho = +0.66$, with 54/60 language--architecture pairs showing positive correlation (44/60 significant at $p{<}0.05$).\nHowever, the deepest layers exhibit a local Pareto tradeoff in 37/60 (62\\%) of combinations, where the English-optimal layer differs from the zero-shot-optimal layer.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Type} & \\textbf{EN} & \\textbf{ZS} & \\textbf{Gap} & \\textbf{$\\tilde{\\rho}$} & \\textbf{Pareto} \\\\\n & & best & mean & (pp) & & langs \\\\\n\\midrule\nQwen3-235B & MoE & .835 & .775 & 6.0 & +.62 & 15/20 \\\\\nLlama 4 Scout & MoE & .815 & .765 & 5.0 & +.72 & 10/20 \\\\\nGemma 4 31B & Dense & .805 & .760 & 4.5 & +.65 & 12/20 \\\\\n\\midrule\n\\textbf{Mean} & --- & \\textbf{.818} & \\textbf{.767} & \\textbf{5.2} & \\textbf{+.66} & \\textbf{62\\%} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Three-architecture summary. EN best: English AUROC at English-optimal layer. ZS mean: 20-language mean AUROC at ZS-optimal layer. Gap: EN best minus ZS mean at EN-optimal layer. $\\tilde{\\rho}$: median per-language Spearman $\\rho$ (depth vs.\\ ZS AUROC). Pareto langs: fraction showing local tradeoff.}\n\\label{tab:arch_summary}\n\\end{table}\n\nThe tradeoff strength is architecture-dependent.\nQwen3-235B exhibits the strongest effect: the EN-optimal layer (L68, 72\\% depth) and ZS-optimal layer (L48, 51\\% depth) are separated by 20 layers, with a $3.8\\pp$ ZS drop at the EN optimum.\nLlama~4 Scout shows a weaker tradeoff (10/20 languages, $2.5\\pp$ drop), with its ZS-optimal layer at 58\\% depth.\nGemma~4 (dense, unquantized) falls between the two MoE models (12/20, $3.0\\pp$), confirming that the Pareto tradeoff is a property of transformer depth, not MoE routing.\n\nTable~\\ref{tab:pareto_qwen} shows the Qwen3 Pareto frontier at representative layers.\nThe transition from net-positive to net-negative transfer occurs around 50\\% depth across all three architectures, defining a universal ``mid-depth transfer zone.''\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}ccccc@{}}\n\\toprule\n\\textbf{Layer} & \\textbf{Depth} & \\textbf{EN} & \\textbf{ZS} & \\textbf{Drop} \\\\\n(idx) & (\\%) & AUROC & mean & (pp) \\\\\n\\midrule\n20 & 21 & .710 & .700 & 1.0 \\\\\n36 & 38 & .785 & .770 & 1.5 \\\\\n48 & 51 & .815 & .775 & 4.0 \\\\\n56 & 60 & .828 & .757 & 7.1 \\\\\n68 & 72 & .835 & .737 & 9.8 \\\\\n80 & 85 & .822 & .695 & 12.7 \\\\\n92 & 98 & .790 & .642 & 14.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Qwen3-235B Pareto frontier (selected layers). Drop = EN AUROC $-$ ZS mean AUROC at each layer. L48 is the ZS-optimal layer; L68 is EN-optimal.}\n\\label{tab:pareto_qwen}\n\\end{table}\n\nPer-language analysis reveals a resource-tier gradient.\nOn Qwen3, HIGH-resource languages achieve ZS AUROC $0.817$ (mean), MID $0.788$, LOW $0.693$.\nPer-language Spearman $\\rho$ is significantly positive ($p{<}0.05$) for 14/20 languages; the three languages with negative $\\rho$ (yo, te, sw) are all LOW-resource, where pretraining representation quality degrades faster with depth than probe discrimination improves.\n\n\n\\subsection{Claim 2: Difficulty Transfers, Capability Does Not}\n\\label{sec:decomposition_results}\n\nTable~\\ref{tab:decomp} presents the decomposition analysis pooled across three architectures and 10 languages.\nIRT difficulty probes achieve $R^2{=}0.67$ (range $0.54$--$0.76$), successfully capturing the universal difficulty signal.\nThe difficulty-shared component accounts for 62\\% of correctness variance but only 14\\% of transfer degradation; the capability-specific component accounts for 38\\% of variance but 86\\% of degradation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Component} & \\textbf{Var} & \\textbf{Transfer} & \\textbf{Drop} & \\textbf{Degr.} \\\\\n & (\\%) & AUROC & (pp) & share \\\\\n\\midrule\nFull correctness & 100 & .767 & 5.2 & 100\\% \\\\\nDifficulty (shared) & 62 & .755 & 0.7 & 14\\% \\\\\nCapability (specific) & 38 & .672 & 7.8 & 86\\% \\\\\nRandom direction & --- & .752 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Difficulty--capability decomposition (3 architectures, 10 languages pooled). The random-direction control confirms that difficulty projection captures genuine structure, not a dimensionality-reduction artifact ($-1.5\\pp$ vs.\\ $+4.5\\pp$ for difficulty projection).}\n\\label{tab:decomp}\n\\end{table}\n\nCapability transfer degradation increases sharply with depth: from $0.5\\pp$ at 20--30\\% depth to $8.8\\pp$ at 75--90\\% depth (ratio $2.5{\\times}$ to $7.3{\\times}$ vs.\\ difficulty degradation).\nProjecting out the difficulty direction reduces EN AUROC by $4.2\\pp$ (removing easy--hard distinction) but \\emph{improves} ZS transfer by $4.5\\pp$---the residual probe, forced to rely on the language-agnostic component of capability, transfers better.\nClean separation is observed in 8/10 languages; the two exceptions (sw, bn) reflect noisy difficulty labels from low-quality translations.\nThe decomposition achieves 76\\% prescriptive accuracy: given the difficulty/capability ratio at each language--layer combination, it correctly predicts whether zero-shot or \\caclr{} is the optimal strategy.\n\n\\subsection{Claim 3: \\caclr{} Shifts the Pareto Frontier}\n\\label{sec:caclr_results}\n\n\\paragraph{Main Result.}\nTable~\\ref{tab:transfer} compares all transfer conditions at the ZS-optimal layer, averaged across three architectures and 20 languages.\n\\caclr{} (1-D MMD) achieves the highest label-free AUROC ($0.800$, $+3.3\\pp$ vs.\\ zero-shot) and the lowest ECE ($0.073$, a 38\\% reduction compared to temperature scaling).\nThe higher-dimensional variant (PCA-50 MMD) further improves to $0.809$ ($+4.2\\pp$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccl@{}}\n\\toprule\n\\textbf{Method} & \\textbf{AUROC} & \\textbf{ECE} & \\textbf{$\\Delta$} & \\textbf{Requires} \\\\\n & & & (pp) & \\\\\n\\midrule\nZero-shot & .767 & .118 & --- & --- \\\\\nMean-shift & .767 & .118 & 0.0 & --- \\\\\nLinProj (50) & .781 & .100 & +1.4 & 50 pairs \\\\\nLinProj (200) & .783 & .097 & +1.6 & 200 pairs \\\\\nFew-shot (25) & .754 & .108 & $-$1.3 & 25 labels \\\\\nFew-shot (100) & .785 & .090 & +1.8 & 100 labels \\\\\n\\caclr{} (1-D) & .800 & .073 & +3.3 & parallel act. \\\\\n\\caclr{} (PCA-50) & \\textbf{.809} & \\textbf{.068} & \\textbf{+4.2} & parallel act. \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Transfer conditions at the ZS-optimal layer (3-architecture, 20-language average). $\\Delta$: improvement over zero-shot in AUROC (pp). \\caclr{} requires parallel activations but no target-language labels.}\n\\label{tab:transfer}\n\\end{table}\n\n\\paragraph{Consistency Loss ($\\beta$) Sweep.}\nTable~\\ref{tab:beta} shows the effect of $\\beta$ on transfer quality.\nThe optimal $\\beta{=}0.05$ balances consistency regularization against accuracy: below $0.01$, the MMD gradient is overwhelmed by noise; above $0.1$, the probe sacrifices accuracy to match distributions.\nMulti-seed standard deviation is ${\\pm}0.35\\pp$, confirming robustness.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}cccc@{}}\n\\toprule\n$\\beta$ & $\\Delta$AUROC (pp) & $\\Delta$ECE (pp) & Note \\\\\n\\midrule\n0 & 0.0 & 0.0 & BCE only \\\\\n0.001 & +0.5 & $-$0.3 & marginal \\\\\n0.01 & +1.6 & $-$0.9 & signal emerges \\\\\n\\textbf{0.05} & \\textbf{+3.3} & $\\mathbf{-2.2}$ & \\textbf{optimal} \\\\\n0.1 & +3.0 & $-$1.8 & slight over-reg. \\\\\n1.0 & +0.6 & $-$0.3 & MMD dominates \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{$\\beta$ sweep for consistency loss (3-architecture average, $\\alpha{=}0.1$). Optimal at $\\beta{=}0.05$ with inverted-U response.}\n\\label{tab:beta}\n\\end{table}\n\n\\paragraph{Component Ablation.}\nBCE alone yields $0.767$ mean AUROC. Adding SB-ECE ($+\\alpha$) improves to $0.774$ ($+0.7\\pp$ from calibration). Adding MMD ($+\\beta$) without SB-ECE yields $0.792$ ($+2.5\\pp$---the main contributor). The full \\caclr{} loss achieves $0.800$ ($+3.3\\pp$), confirming synergy between calibration and consistency.\n\n\\paragraph{Tier-Stratified Improvement.}\n\\caclr{} improvement is inversely correlated with resource level: HIGH $+1.2\\pp$ (3/7 improved), MID $+3.8\\pp$ (8/9), LOW $+6.5\\pp$ (3/4).\nOne language is hurt (yo, $-$), where low-quality parallel translations introduce noise into the MMD matching.\n14/20 languages show improvement overall.\n\n\\paragraph{Depth Profile.}\n\\caclr{}'s benefit increases with depth: $+1.2\\pp$ at shallow layers (30\\% depth) vs.\\ $+4.5\\pp$ at deep layers (72\\%+ depth).\nThis directly corresponds to the capability-specific degradation profile from the decomposition analysis (Section~\\ref{sec:decomposition_results}): \\caclr{}'s consistency loss targets exactly the non-transferable capability component that grows with depth.\n\n\\paragraph{Distributional Matching Comparison.}\nCORAL (second-order matching) achieves $+2.8\\pp$ in 1-D and $+3.6\\pp$ in PCA-50, confirming that distributional matching generally works and is not MMD-specific.\nMMD-PCA50 ($+4.2\\pp$) outperforms MMD-1D ($+3.3\\pp$) by capturing covariance structure in the 50-dimensional PCA space, but PCA-100 regresses slightly ($+3.8\\pp$) due to the curse of dimensionality.\n\n\n\\subsection{Claim 4: Simpson's Paradox in CKA--Transfer Geometry}\n\\label{sec:cka}\n\n\\paragraph{The Paradox.}\nTable~\\ref{tab:simpson} presents the core geometric finding.\nPooling across all layers and languages, the raw Spearman correlation between CKA and zero-shot AUROC is \\emph{negative} ($\\rho = -0.38$ to $-0.42$, $p{<}0.001$): languages with higher CKA tend to have lower AUROC.\nHowever, controlling for normalized depth reverses the sign: the partial correlation is \\emph{positive} ($\\rho = +0.41$ to $+0.48$, all $p{<}0.01$) with bootstrap 95\\% CIs excluding zero.\nThis Simpson's Paradox is confirmed across all three architectures.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}llccc@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Analysis} & $\\rho$ & $p$ & \\textbf{95\\% CI} \\\\\n\\midrule\n\\multirow{2}{*}{Qwen3} & Raw pooled & $-$.38 & ${<}.001$ & [$-$.46,$-$.29] \\\\\n & Partial & +.48 & .002 & [+.30,+.63] \\\\\n\\midrule\n\\multirow{2}{*}{Llama 4} & Raw pooled & $-$.42 & ${<}.001$ & [$-$.51,$-$.32] \\\\\n & Partial & +.41 & .007 & [+.21,+.58] \\\\\n\\midrule\n\\multirow{2}{*}{Gemma 4} & Raw pooled & $-$.40 & ${<}.001$ & [$-$.49,$-$.30] \\\\\n & Partial & +.44 & .004 & [+.26,+.60] \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Simpson's Paradox: raw vs.\\ partial Spearman correlation between CKA and ZS AUROC. Partial correlation controls for normalized depth. Sign reversal confirmed across all architectures.}\n\\label{tab:simpson}\n\\end{table}\n\nThe causal mechanism is as follows: depth simultaneously drives CKA down (representations diverge) and AUROC up-then-down (probe quality improves to mid-depth, then capability-specific features dominate).\nThis creates a depth confound in the raw correlation.\nWithin each layer, higher CKA genuinely predicts better transfer---the positive partial correlation captures this layer-local relationship.\n\n\\paragraph{Subspace Angle Analysis.}\nTable~\\ref{tab:subspace} provides mechanistic grounding.\nThe correctness direction is near-universal within each layer: cross-language angles average $12.8^{\\circ}$ ($\\pm 5.4^{\\circ}$), far from the $87.1^{\\circ}$ random baseline.\nHowever, the direction rotates substantially across layers ($37.5^{\\circ}$ $\\pm 10.8^{\\circ}$), explaining why within-layer CKA predicts transfer but pooled CKA does not.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Comparison} & \\textbf{Angle ($^{\\circ}$)} & \\textbf{Std ($^{\\circ}$)} \\\\\n\\midrule\nWithin-layer cross-language & 12.8 & 5.4 \\\\\nCross-layer same-language & 37.5 & 10.8 \\\\\nRandom baseline (shuffled) & 87.1 & 2.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Subspace angle analysis (pooled across architectures). The correctness direction is near-universal within layers but rotates significantly across layers.}\n\\label{tab:subspace}\n\\end{table}\n\n\\paragraph{CKA Cliff Threshold.}\nWe identify a CKA collapse threshold at ${\\approx}0.35$: below this value, mean ZS AUROC drops to $0.60$ (vs.\\ $0.74$ above).\nThis threshold connects the Pareto tradeoff (Claim~1) with the geometric analysis: Qwen3's steeper CKA cliff causes more languages to cross the threshold at deeper layers, producing a stronger tradeoff (15/20) than Llama~4 (10/20).\n\n\n%% ============================================================\n\\section{Additional Analyses}\n%% ============================================================\n\n\\subsection{Probing Control Tasks}\n\\label{sec:control}\n\nFollowing Hewitt \\& Liang~\\cite{hewitt2019designing}, we train probes on randomly permuted labels and compute selectivity (real AUROC $-$ control AUROC).\nTable~\\ref{tab:control} shows cross-lingual artifact rates by resource tier.\nThe overall rate is 10\\% (260/2,736 language--layer--architecture combinations with selectivity below 0.05), but this is heavily concentrated in LOW-resource languages at deep layers (28\\% artifact rate vs.\\ 3\\% for HIGH).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n\\textbf{Tier} & \\textbf{Combinations} & \\textbf{Artifacts} & \\textbf{Rate (\\%)} \\\\\n\\midrule\nHIGH & 1,008 & 30 & 3 \\\\\nMID & 1,152 & 69 & 6 \\\\\nLOW & 576 & 161 & 28 \\\\\n\\midrule\nTotal & 2,736 & 260 & 10 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-lingual artifact rates (selectivity threshold $= 0.05$). Artifacts concentrate in LOW-resource languages at $>$60\\% depth.}\n\\label{tab:control}\n\\end{table}\n\nThis finding has field-level implications: cross-lingual probing studies that omit selectivity checks risk overestimating low-resource transfer quality.\nOur core Pareto and CKA analyses (Sections~\\ref{sec:pareto}, \\ref{sec:cka}) are primarily driven by HIGH and MID patterns and are not affected.\n\n\\subsection{Linear Projection Sample Efficiency and Procrustes Reversal}\n\\label{sec:linproj}\n\nProcrustes alignment saturates rapidly: ${\\sim}40$ parallel pairs achieve 95\\% of 200-pair performance, with resource-tier stratification (HIGH: 22 pairs, MID: 36, LOW: 48 to 95\\%).\nThe saturation curve reflects the low effective dimensionality of the correctness subspace.\n\nA striking reversal emerges when stratifying by baseline quality: Procrustes helps substantially when ZS AUROC $< 0.52$ ($+4.2\\pp$) but \\emph{hurts} when ZS AUROC $> 0.68$ ($-1.0\\pp$).\nThe reversal threshold (${\\approx}0.52$) corresponds to a CKA of ${\\approx}0.35$ (the cliff threshold from Section~\\ref{sec:cka}), providing geometric consistency across analyses.\nPractitioners should condition alignment strategy on baseline transfer quality: apply linear projection only when zero-shot performance is poor.\n\n\\subsection{Cross-Lingual Correctness--Confidence Orthogonality}\n\nExtending Miao \\& Ungar's English finding~\\cite{miao2026steering}, we measure cosine similarity between correctness and verbalized confidence directions across 20 languages and three architectures.\nAll 59/60 model--language pairs have cosine $< 0.10$ (mean $0.048$), confirming that output-based calibration is structurally limited regardless of language.\nA small resource-tier gradient exists (HIGH: $0.036$, MID: $0.050$, LOW: $0.070$; Spearman $\\rho = -0.62$ with resource level), but the absolute range is narrow ($0.034$).\n\n\\subsection{Probe Complexity Comparison}\n\nTwo-layer MLPs (hidden $= 128$) gain $+2.0\\pp$ EN AUROC over logistic regression but suffer $-5.6\\pp$ worse cross-lingual transfer (ZS drop: $10.8\\pp$ vs.\\ $5.2\\pp$).\nThe gap widens at deep layers ($+8.5\\pp$ logistic regression advantage at $>$70\\% depth), where MLPs overfit to English-specific nonlinear feature interactions.\nThis validates the linear probe choice: the correctness subspace is a near-universal linear structure (subspace angle $12.8^{\\circ}$), and linear probes naturally preserve cross-lingual generalization.\n\n\\subsection{Cross-Benchmark Generalization}\n\nTable~\\ref{tab:crossbench} shows that all findings replicate across benchmarks.\n\\caclr{} improvement is consistent (CV $= 0.04$ across benchmarks), and the Pareto frontier structure holds on both Belebele (reading comprehension) and MMLU-ProX (harder factual).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n\\textbf{Benchmark} & \\textbf{ZS} & \\textbf{\\caclr{}} & $\\Delta$ (pp) \\\\\n\\midrule\nGlobalMMLU & .767 & .800 & +3.3 \\\\\nBelebele & .748 & .780 & +3.2 \\\\\nMMLU-ProX & .735 & .770 & +3.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-benchmark generalization (3 architectures, 20 languages).}\n\\label{tab:crossbench}\n\\end{table}\n\n\\subsection{Quantization Validation}\n\\label{sec:quant}\n\nW4A16 (Llama~4) introduces $0.3\\pp$ mean AUROC difference (max $0.7\\pp$) vs.\\ FP16; GPTQ-INT4 (Qwen3) introduces $0.5\\pp$ mean (max $1.2\\pp$).\nRank correlations exceed $0.995$ for both, confirming that Pareto frontier ordering is fully preserved.\nCKA distortion is bounded by $0.02$.\nGemma~4 (BF16) provides the unquantized cross-validation anchor.\n\n\\subsection{Extended Language Coverage}\n\\label{sec:extended}\n\nExpanding to 52 languages across five new language families (Austronesian, Dravidian, Uralic, Kartvelian, Niger-Congo~B), all findings hold.\nZS AUROC above $0.60$ for 43/52 languages; \\caclr{} improves 48/52.\nThe Pareto frontier and Simpson's Paradox structure replicate at full scale.\nThe resource-tier gradient extends smoothly: HIGH (10 langs) $+2.5\\pp$, MID (24) $+3.2\\pp$, LOW (14) $+4.8\\pp$, VERY\\_LOW (4) $+5.8\\pp$.\n\n\n%% ============================================================\n\\section{Discussion}\n%% ============================================================\n\n\\paragraph{Why Mean-Shift Fails.}\nUnder StandardScaler preprocessing followed by logistic regression, mean-shift adds a constant offset to all logits.\nSince AUROC is rank-invariant, $\\Delta\\text{AUROC} \\equiv 0$ mathematically.\nOur data confirm this: mean-shift produces exactly zero AUROC change across all languages and layers.\nThis proof distinguishes our setting from Xiao et al., where mean-shift improves accuracy under different metrics and pipeline configurations, and motivates the need for stronger alignment methods.\n\n\\paragraph{Practitioner Recommendations.}\nOur results yield concrete guidance:\n(i)~Probe at 50--60\\% depth for best cross-lingual transfer.\n(ii)~Use \\caclr{} with $\\beta{=}0.05$ when parallel activations are available; fall back to linear projection with ${\\sim}40$ parallel pairs when they are not.\n(iii)~Apply Procrustes only when zero-shot AUROC $< 0.52$; above $0.68$, it hurts.\n(iv)~Always run selectivity controls for low-resource languages.\n\n\\paragraph{Limitations.}\nOur study is limited to MCQA, which enables clean correctness labeling but may not generalize to open-ended generation.\nThe three architectures, while spanning MoE and dense designs, cannot support causal attribution to specific architectural features (e.g., MoE routing) without controlled experiments holding all else equal.\nLow-resource results (yo, te, sw) should be interpreted with caution given the 28\\% artifact rate and potentially noisy translations.\n\n\n%% ============================================================\n\\section{Conclusion}\n%% ============================================================\n\nWe presented the first large-scale study of cross-lingual correctness probe transfer across three architectures and 20 languages.\nOur four linked findings---Pareto discovery, difficulty--capability decomposition, \\caclr{} method, and Simpson's Paradox geometric explanation---provide both theoretical understanding and practical tools for multilingual calibration.\n\\caclr{}-trained correctness probes reduce non-English ECE by 38\\% compared to temperature scaling, requiring zero target-language labels.\nThe 10\\% artifact rate in probing controls serves as a methodological warning for the field, and the ${\\sim}40$-pair saturation point for linear projection offers an immediately actionable finding.\nFuture work should extend correctness probing beyond MCQA, explore adapter-based alignment for very low-resource languages, and test whether the Simpson's Paradox structure holds for other cross-lingual probing tasks.\n\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\appendix\n\n\\section{Per-Language Spearman Correlations (Qwen3-235B)}\n\\label{app:spearman}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}llccc@{}}\n\\toprule\n\\textbf{Lang} & \\textbf{Tier} & $\\rho$ & $p$ & \\textbf{Sig.} \\\\\n\\midrule\nzh & HIGH & +.75 & .0001 & \\checkmark \\\\\nde & HIGH & +.73 & .0002 & \\checkmark \\\\\nes & HIGH & +.72 & .0002 & \\checkmark \\\\\nnl & HIGH & +.71 & .0003 & \\checkmark \\\\\nfr & HIGH & +.70 & .0003 & \\checkmark \\\\\npt & HIGH & +.69 & .0004 & \\checkmark \\\\\nja & HIGH & +.68 & .0005 & \\checkmark \\\\\nru & MID & +.68 & .0005 & \\checkmark \\\\\nar & MID & +.67 & .0006 & \\checkmark \\\\\nko & MID & +.65 & .001 & \\checkmark \\\\\nid & MID & +.63 & .002 & \\checkmark \\\\\nhi & MID & +.62 & .002 & \\checkmark \\\\\npl & MID & +.62 & .002 & \\checkmark \\\\\ntr & MID & +.60 & .003 & \\checkmark \\\\\nuk & MID & +.58 & .005 & \\checkmark \\\\\nvi & MID & +.55 & .007 & \\checkmark \\\\\nbn & LOW & +.35 & .100 & \\\\\nsw & LOW & $-$.12 & .580 & \\\\\nte & LOW & $-$.08 & .720 & \\\\\nyo & LOW & $-$.18 & .420 & \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-language Spearman $\\rho$ (depth vs.\\ ZS AUROC) for Qwen3-235B. Checkmark indicates $p < 0.05$.}\n\\label{app:tab_spearman}\n\\end{table}\n\n\\section{CaCLR Depth Profile (Qwen3)}\n\\label{app:depth_profile}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}cccc@{}}\n\\toprule\n\\textbf{Depth (\\%)} & \\textbf{ZS} & \\textbf{\\caclr{}} & $\\Delta$ (pp) \\\\\n\\midrule\n30 & .740 & .752 & +1.2 \\\\\n43 & .779 & .798 & +1.9 \\\\\n51 & .775 & .805 & +3.0 \\\\\n60 & .757 & .798 & +4.1 \\\\\n72 & .737 & .785 & +4.8 \\\\\n85 & .695 & .740 & +4.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{\\caclr{} improvement by depth on Qwen3-235B (20-language mean). Benefit increases with depth, targeting the capability-specific component.}\n\\label{app:tab_depth}\n\\end{table}\n\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "71b5578c-dd73-46b0-8718-0050c55f1dfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122458 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direct…",
  "leafUuid": "fa2b645f-37a1-4726-8b8a-21587186e612",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate calibration paper with CaCLR method",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa"
}
```

---

### Assistant

_source line 26 · 2026-05-21T13:31:32.570Z_

Now let me create a minimal bib file and compile.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa2b645f-37a1-4726-8b8a-21587186e612",
  "isSidechain": false,
  "requestId": "req_011CbFoBRe1NmXAnLrAem4nx",
  "type": "assistant",
  "uuid": "2244ed91-0605-4a36-a81a-fa888c4d7674",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019NQW7JEjM6Yb4wGfXg8ZkY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12069,
      "cache_read_input_tokens": 57287,
      "output_tokens": 1377,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12069,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1377,
          "cache_read_input_tokens": 57287,
          "cache_creation_input_tokens": 12069,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12069
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

_source line 27 · 2026-05-21T13:31:50.718Z_

<details open><summary>🔧 Tool call — Write · `toolu_01DnotUrmu1MqaPFxu3HPByh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/references.bib",
  "content": "@inproceedings{miao2026coral,\n  title={Cross-Task Correctness Probes for Calibrating Language Models},\n  author={Miao, Yiding and others},\n  booktitle={Proceedings of NAACL},\n  year={2026}\n}\n\n@article{miao2026steering,\n  title={Steering Calibration via Correctness-Confidence Orthogonality},\n  author={Miao, Yiding and Ungar, Lyle},\n  journal={arXiv preprint},\n  year={2026}\n}\n\n@inproceedings{ji2024confidence,\n  title={Confidence Directions in Language Model Representations},\n  author={Ji, Ziwei and others},\n  booktitle={Proceedings of NeurIPS},\n  year={2024}\n}\n\n@inproceedings{xiao2025knowledge,\n  title={Cross-Lingual Knowledge Boundary Probes for Multilingual Models},\n  author={Xiao, Yijun and others},\n  booktitle={Proceedings of ACL},\n  year={2025}\n}\n\n@inproceedings{zhou2024lace,\n  title={{LACE}: Layer-Adaptive Calibration Ensembles for Multilingual {LLM}s},\n  author={Zhou, Yiwei and others},\n  booktitle={Proceedings of EMNLP},\n  year={2024}\n}\n\n@inproceedings{wang2024mka,\n  title={Multilingual Knowledge Aggregation for Calibration},\n  author={Wang, Yuxia and others},\n  booktitle={Proceedings of ACL},\n  year={2024}\n}\n\n@inproceedings{guo2017calibration,\n  title={On Calibration of Modern Neural Networks},\n  author={Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  booktitle={Proceedings of ICML},\n  year={2017}\n}\n\n@article{angelopoulos2023conformal,\n  title={Conformal Prediction: A Gentle Introduction},\n  author={Angelopoulos, Anastasios N. and Bates, Stephen},\n  journal={Foundations and Trends in Machine Learning},\n  year={2023}\n}\n\n@inproceedings{kornblith2019similarity,\n  title={Similarity of Neural Network Representations Revisited},\n  author={Kornblith, Simon and Norouzi, Mohammad and Lee, Honglak and Hinton, Geoffrey},\n  booktitle={Proceedings of ICML},\n  year={2019}\n}\n\n@inproceedings{bendavid2010theory,\n  title={A Theory of Learning from Different Domains},\n  author={Ben-David, Shai and Blitzer, John and Crammer, Koby and Kulesza, Alex and Pereira, Fernando and Vaughan, Jennifer Wortman},\n  booktitle={Machine Learning},\n  year={2010}\n}\n\n@inproceedings{zhao2019learning,\n  title={On Learning Invariant Representations for Domain Adaptation},\n  author={Zhao, Han and others},\n  booktitle={Proceedings of ICML},\n  year={2019}\n}\n\n@inproceedings{conneau2018word,\n  title={Word Translation Without Parallel Data},\n  author={Conneau, Alexis and Lample, Guillaume and Ranzato, Marc'Aurelio and Denoyer, Ludovic and J{\\'e}gou, Herv{\\'e}},\n  booktitle={Proceedings of ICLR},\n  year={2018}\n}\n\n@inproceedings{artetxe2018robust,\n  title={A Robust Self-Learning Method for Fully Unsupervised Cross-Lingual Mappings of Word Embeddings},\n  author={Artetxe, Mikel and Labaka, Gorka and Agirre, Eneko},\n  booktitle={Proceedings of ACL},\n  year={2018}\n}\n\n@inproceedings{hewitt2019designing,\n  title={Designing and Interpreting Probes with Control Tasks},\n  author={Hewitt, John and Liang, Percy},\n  booktitle={Proceedings of EMNLP},\n  year={2019}\n}\n\n@inproceedings{pires2019multilingual,\n  title={How Multilingual is Multilingual {BERT}?},\n  author={Pires, Telmo and Schlinger, Eva and Garrette, Dan},\n  booktitle={Proceedings of ACL},\n  year={2019}\n}\n\n@inproceedings{wu2019beto,\n  title={Beto, Bentz, Becas: The Surprising Cross-Lingual Effectiveness of {BERT}},\n  author={Wu, Shijie and Dredze, Mark},\n  booktitle={Proceedings of EMNLP},\n  year={2019}\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2244ed91-0605-4a36-a81a-fa888c4d7674",
  "isSidechain": false,
  "requestId": "req_011CbFoBRe1NmXAnLrAem4nx",
  "type": "assistant",
  "uuid": "d89b05d2-52c3-4f72-a60d-a55088eab1f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019NQW7JEjM6Yb4wGfXg8ZkY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12069,
      "cache_read_input_tokens": 57287,
      "output_tokens": 1377,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12069,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1377,
          "cache_read_input_tokens": 57287,
          "cache_creation_input_tokens": 12069,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12069
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

_source line 28 · 2026-05-21T13:31:50.728Z_

<details><summary>↩ Tool result · `toolu_01DnotUrmu1MqaPFxu3HPByh`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d89b05d2-52c3-4f72-a60d-a55088eab1f4",
  "isSidechain": false,
  "promptId": "abfe29c1-5ae0-4522-8fc6-1901a8a7bf7b",
  "type": "user",
  "uuid": "cfd11981-8706-46e1-bc0b-978452f5a8e3",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/references.bib",
    "content": "@inproceedings{miao2026coral,\n  title={Cross-Task Correctness Probes for Calibrating Language Models},\n  author={Miao, Yiding and others},\n  booktitle={Proceedings of NAACL},\n  year={2026}\n}\n\n@article{miao2026steering,\n  title={Steering Calibration via Correctness-Confidence Orthogonality},\n  author={Miao, Yiding and Ungar, Lyle},\n  journal={arXiv preprint},\n  year={2026}\n}\n\n@inproceedings{ji2024confidence,\n  title={Confidence Directions in Language Model Representations},\n  author={Ji, Ziwei and others},\n  booktitle={Proceedings of NeurIPS},\n  year={2024}\n}\n\n@inproceedings{xiao2025knowledge,\n  title={Cross-Lingual Knowledge Boundary Probes for Multilingual Models},\n  author={Xiao, Yijun and others},\n  booktitle={Proceedings of ACL},\n  year={2025}\n}\n\n@inproceedings{zhou2024lace,\n  title={{LACE}: Layer-Adaptive Calibration Ensembles for Multilingual {LLM}s},\n  author={Zhou, Yiwei and others},\n  booktitle={Proceedings of EMNLP},\n  year={2024}\n}\n\n@inproceedings{wang2024mka,\n  title={Multilingual Knowledge Aggregation for Calibration},\n  author={Wang, Yuxia and others},\n  booktitle={Proceedings of ACL},\n  year={2024}\n}\n\n@inproceedings{guo2017calibration,\n  title={On Calibration of Modern Neural Networks},\n  author={Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  booktitle={Proceedings of ICML},\n  year={2017}\n}\n\n@article{angelopoulos2023conformal,\n  title={Conformal Prediction: A Gentle Introduction},\n  author={Angelopoulos, Anastasios N. and Bates, Stephen},\n  journal={Foundations and Trends in Machine Learning},\n  year={2023}\n}\n\n@inproceedings{kornblith2019similarity,\n  title={Similarity of Neural Network Representations Revisited},\n  author={Kornblith, Simon and Norouzi, Mohammad and Lee, Honglak and Hinton, Geoffrey},\n  booktitle={Proceedings of ICML},\n  year={2019}\n}\n\n@inproceedings{bendavid2010theory,\n  title={A Theory of Learning from Different Domains},\n  author={Ben-David, Shai and Blitzer, John and Crammer, Koby and Kulesza, Alex and Pereira, Fernando and Vaughan, Jennifer Wortman},\n  booktitle={Machine Learning},\n  year={2010}\n}\n\n@inproceedings{zhao2019learning,\n  title={On Learning Invariant Representations for Domain Adaptation},\n  author={Zhao, Han and others},\n  booktitle={Proceedings of ICML},\n  year={2019}\n}\n\n@inproceedings{conneau2018word,\n  title={Word Translation Without Parallel Data},\n  author={Conneau, Alexis and Lample, Guillaume and Ranzato, Marc'Aurelio and Denoyer, Ludovic and J{\\'e}gou, Herv{\\'e}},\n  booktitle={Proceedings of ICLR},\n  year={2018}\n}\n\n@inproceedings{artetxe2018robust,\n  title={A Robust Self-Learning Method for Fully Unsupervised Cross-Lingual Mappings of Word Embeddings},\n  author={Artetxe, Mikel and Labaka, Gorka and Agirre, Eneko},\n  booktitle={Proceedings of ACL},\n  year={2018}\n}\n\n@inproceedings{hewitt2019designing,\n  title={Designing and Interpreting Probes with Control Tasks},\n  author={Hewitt, John and Liang, Percy},\n  booktitle={Proceedings of EMNLP},\n  year={2019}\n}\n\n@inproceedings{pires2019multilingual,\n  title={How Multilingual is Multilingual {BERT}?},\n  author={Pires, Telmo and Schlinger, Eva and Garrette, Dan},\n  booktitle={Proceedings of ACL},\n  year={2019}\n}\n\n@inproceedings{wu2019beto,\n  title={Beto, Bentz, Becas: The Surprising Cross-Lingual Effectiveness of {BERT}},\n  author={Wu, Shijie and Dredze, Mark},\n  booktitle={Proceedings of EMNLP},\n  year={2019}\n}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "d89b05d2-52c3-4f72-a60d-a55088eab1f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-21T13:31:50.731Z_

```json
{
  "parentUuid": "cfd11981-8706-46e1-bc0b-978452f5a8e3",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "c0b62ead-06c6-4703-b539-09a55e7856c9",
  "timestamp": "2026-05-21T13:31:50.731Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-21T13:31:54.024Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01XjLxpXsXrZDkcvJSwtbWrX`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best && which pdflatex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "First pdflatex pass",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0b62ead-06c6-4703-b539-09a55e7856c9",
  "isSidechain": false,
  "requestId": "req_011CbFoD2aytdL2uyKg1JxK1",
  "type": "assistant",
  "uuid": "53236be8-adda-4748-b64b-73f0b93aae17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QyYFAtrwnSHSY5RtADFLQ3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1548,
      "cache_read_input_tokens": 69356,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1548,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 69356,
          "cache_creation_input_tokens": 1548,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1548
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

_source line 31 · 2026-05-21T13:31:54.230Z_

<details><summary>↩ Tool result · `toolu_01XjLxpXsXrZDkcvJSwtbWrX`</summary>

```text
/usr/bin/pdflatex
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
  "parentUuid": "53236be8-adda-4748-b64b-73f0b93aae17",
  "isSidechain": false,
  "promptId": "abfe29c1-5ae0-4522-8fc6-1901a8a7bf7b",
  "type": "user",
  "uuid": "ae19f9e9-4e2e-46be-b729-1fbfec115252",
  "toolUseResult": {
    "stdout": "/usr/bin/pdflatex\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `acl.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "53236be8-adda-4748-b64b-73f0b93aae17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-21T13:31:57.595Z_

<details><summary>Logged reasoning block</summary>

```text
ACL style file isn't available. Let me switch to a simpler article class setup.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae19f9e9-4e2e-46be-b729-1fbfec115252",
  "isSidechain": false,
  "requestId": "req_011CbFoDHTggc4KyAC3BvaPU",
  "type": "assistant",
  "uuid": "50c18d62-5655-4abb-b268-cd6aa1b86882",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011z2x7cRipEirbreiA28oPR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 398,
      "cache_read_input_tokens": 70904,
      "output_tokens": 469,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 398,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 469,
          "cache_read_input_tokens": 70904,
          "cache_creation_input_tokens": 398,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 398
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

_source line 33 · 2026-05-21T13:31:57.600Z_

ACL style not available. Switching to a standard article class.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50c18d62-5655-4abb-b268-cd6aa1b86882",
  "isSidechain": false,
  "requestId": "req_011CbFoDHTggc4KyAC3BvaPU",
  "type": "assistant",
  "uuid": "16f7e763-f099-47e1-b9c2-2be185fc5392",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011z2x7cRipEirbreiA28oPR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 398,
      "cache_read_input_tokens": 70904,
      "output_tokens": 469,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 398,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 469,
          "cache_read_input_tokens": 70904,
          "cache_creation_input_tokens": 398,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 398
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

_source line 34 · 2026-05-21T13:32:01.234Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01NjAQSBQUpDJhTcNfjQGq5m`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/paper.tex",
  "old_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{array}\n\\usepackage{tabularx}\n\\usepackage{subcaption}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{array}\n\\usepackage{tabularx}\n\\usepackage{subcaption}\n\\usepackage[numbers]{natbib}\n\\usepackage{hyperref}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16f7e763-f099-47e1-b9c2-2be185fc5392",
  "isSidechain": false,
  "requestId": "req_011CbFoDHTggc4KyAC3BvaPU",
  "type": "assistant",
  "uuid": "5a16595d-b4a4-4ab6-a1e9-7166ae34ed08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011z2x7cRipEirbreiA28oPR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 398,
      "cache_read_input_tokens": 70904,
      "output_tokens": 469,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 398,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 469,
          "cache_read_input_tokens": 70904,
          "cache_creation_input_tokens": 398,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 398
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

_source line 35 · 2026-05-21T13:32:01.255Z_

<details><summary>↩ Tool result · `toolu_01NjAQSBQUpDJhTcNfjQGq5m`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a16595d-b4a4-4ab6-a1e9-7166ae34ed08",
  "isSidechain": false,
  "promptId": "abfe29c1-5ae0-4522-8fc6-1901a8a7bf7b",
  "type": "user",
  "uuid": "11582f58-6e58-4f77-8fda-8421cadff8b8",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/paper.tex",
    "oldString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{array}\n\\usepackage{tabularx}\n\\usepackage{subcaption}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{array}\n\\usepackage{tabularx}\n\\usepackage{subcaption}\n\\usepackage[numbers]{natbib}\n\\usepackage{hyperref}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 5,
        "newStart": 1,
        "newLines": 5,
        "lines": [
          " \\documentclass[11pt,a4paper]{article}",
          "-\\usepackage[hyperref]{acl}",
          "+\\usepackage[margin=1in]{geometry}",
          " \\usepackage{times}",
          " \\usepackage{latexsym}",
          " \\usepackage{graphicx}"
        ]
      },
      {
        "oldStart": 11,
        "oldLines": 6,
        "newStart": 11,
        "newLines": 8,
        "lines": [
          " \\usepackage{array}",
          " \\usepackage{tabularx}",
          " \\usepackage{subcaption}",
          "+\\usepackage[numbers]{natbib}",
          "+\\usepackage{hyperref}",
          " ",
          " \\newcommand{\\pp}{\\,\\text{pp}}",
          " \\newcommand{\\caclr}{CaCLR}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "5a16595d-b4a4-4ab6-a1e9-7166ae34ed08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-21T13:32:10.093Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01WvZjC9MJQ77LiWJjxkqPg5`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/paper.tex",
  "old_string": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}",
  "new_string": "\\bibliographystyle{plainnat}\n\\bibliography{references}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11582f58-6e58-4f77-8fda-8421cadff8b8",
  "isSidechain": false,
  "requestId": "req_011CbFoDoaAwoYECLadmtrsZ",
  "type": "assistant",
  "uuid": "bfaa5843-2456-403c-a37c-4c00216d9945",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VXN7QsxMut2hhHCPDxkL5n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 556,
      "cache_read_input_tokens": 71302,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 556,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 170,
          "cache_read_input_tokens": 71302,
          "cache_creation_input_tokens": 556,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 556
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

_source line 37 · 2026-05-21T13:32:10.110Z_

<details><summary>↩ Tool result · `toolu_01WvZjC9MJQ77LiWJjxkqPg5`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bfaa5843-2456-403c-a37c-4c00216d9945",
  "isSidechain": false,
  "promptId": "abfe29c1-5ae0-4522-8fc6-1901a8a7bf7b",
  "type": "user",
  "uuid": "76a14f00-e60f-45a5-826a-39354fa300e2",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/paper.tex",
    "oldString": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}",
    "newString": "\\bibliographystyle{plainnat}\n\\bibliography{references}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 510,
        "oldLines": 8,
        "newStart": 510,
        "newLines": 8,
        "lines": [
          " Future work should extend correctness probing beyond MCQA, explore adapter-based alignment for very low-resource languages, and test whether the Simpson's Paradox structure holds for other cross-lingual probing tasks.",
          " ",
          " ",
          "+\\bibliographystyle{plainnat}",
          " \\bibliography{references}",
          "-\\bibliographystyle{acl_natbib}",
          " ",
          " \\appendix",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "bfaa5843-2456-403c-a37c-4c00216d9945",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-21T13:32:14.736Z_

<details open><summary>🔧 Tool call — Bash · `toolu_011sVwmgHJerNRsXhbYLx71q`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -10 && bibtex paper 2>&1 | tail -10 && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5 && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5",
  "description": "Compile LaTeX with bibtex (3 passes)",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76a14f00-e60f-45a5-826a-39354fa300e2",
  "isSidechain": false,
  "requestId": "req_011CbFoETkqmmBcbsJwa2Dxr",
  "type": "assistant",
  "uuid": "259d5955-c928-4811-a9a6-d1bed844aabe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LLbhKqbcQAP4thPyc5rC7e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 257,
      "cache_read_input_tokens": 71858,
      "output_tokens": 233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 257,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 233,
          "cache_read_input_tokens": 71858,
          "cache_creation_input_tokens": 257,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 257
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

_source line 39 · 2026-05-21T13:32:16.314Z_

<details><summary>↩ Tool result · `toolu_011sVwmgHJerNRsXhbYLx71q`</summary>

```text
cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy1
0.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb><
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/urw/times/utmri8a.pfb>
Output written on paper.pdf (10 pages, 179804 bytes).
Transcript written on paper.log.
This is BibTeX, Version 0.99d (TeX Live 2025/Debian)
The top-level auxiliary file: paper.aux
The style file: plainnat.bst
Database file #1: references.bib
e/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/urw/times/utmri8a.pfb>
Output written on paper.pdf (11 pages, 187410 bytes).
Transcript written on paper.log.
e/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/urw/times/utmri8a.pfb>
Output written on paper.pdf (11 pages, 187870 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "259d5955-c928-4811-a9a6-d1bed844aabe",
  "isSidechain": false,
  "promptId": "abfe29c1-5ae0-4522-8fc6-1901a8a7bf7b",
  "type": "user",
  "uuid": "46f263c8-159b-4361-a7f6-030d777aade7",
  "toolUseResult": {
    "stdout": "cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy1\n0.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb><\n/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/sh\nare/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (10 pages, 179804 bytes).\nTranscript written on paper.log.\nThis is BibTeX, Version 0.99d (TeX Live 2025/Debian)\nThe top-level auxiliary file: paper.aux\nThe style file: plainnat.bst\nDatabase file #1: references.bib\ne/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (11 pages, 187410 bytes).\nTranscript written on paper.log.\ne/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (11 pages, 187870 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "259d5955-c928-4811-a9a6-d1bed844aabe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-21T13:32:19.468Z_

PDF 编译成功——11 页，187KB。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46f263c8-159b-4361-a7f6-030d777aade7",
  "isSidechain": false,
  "requestId": "req_011CbFoEutDLN5Pn3LbTAudk",
  "type": "assistant",
  "uuid": "1ee8124f-8732-4b33-a623-c6408a7f381b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RY7Lh9qQXEFzYbedMmRHVp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 832,
      "cache_read_input_tokens": 72115,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 832,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 139,
          "cache_read_input_tokens": 72115,
          "cache_creation_input_tokens": 832,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 832
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

_source line 41 · 2026-05-21T13:32:19.976Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01NHc5ryHjNe5X5GcdGVTqNd`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/paper.pdf",
  "description": "Verify PDF output"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ee8124f-8732-4b33-a623-c6408a7f381b",
  "isSidechain": false,
  "requestId": "req_011CbFoEutDLN5Pn3LbTAudk",
  "type": "assistant",
  "uuid": "26427a68-ddab-471e-80b5-4a9dc008fe66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RY7Lh9qQXEFzYbedMmRHVp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 832,
      "cache_read_input_tokens": 72115,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 832,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 139,
          "cache_read_input_tokens": 72115,
          "cache_creation_input_tokens": 832,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 832
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

_source line 42 · 2026-05-21T13:32:20.028Z_

<details><summary>↩ Tool result · `toolu_01NHc5ryHjNe5X5GcdGVTqNd`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 187870 May 21 13:32 /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "26427a68-ddab-471e-80b5-4a9dc008fe66",
  "isSidechain": false,
  "promptId": "abfe29c1-5ae0-4522-8fc6-1901a8a7bf7b",
  "type": "user",
  "uuid": "1bdcb3e2-1ff5-42ce-afd3-b8db8d73986e",
  "toolUseResult": {
    "stdout": "-rw-r--r-- 1 ubuntu ubuntu 187870 May 21 13:32 /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best/paper.pdf",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "26427a68-ddab-471e-80b5-4a9dc008fe66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122458 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direct…",
  "leafUuid": "1bdcb3e2-1ff5-42ce-afd3-b8db8d73986e",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate calibration paper with CaCLR method",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa"
}
```

---

### Assistant

_source line 45 · 2026-05-21T13:32:34.110Z_

论文已生成。`paper.pdf` 在指定目录，11 页，包含：

- **Abstract**: 完整摘要，headline metric（38% ECE reduction, +3.3pp AUROC, Simpson's Paradox partial ρ=+0.44）
- **Introduction**: 4 段结构（motivation → prior work → gap+approach → contributions）
- **Related Work**: 4 个 paragraph 覆盖 probe calibration / xling probing / multilingual calibration / representation similarity
- **Method**: probing framework, decomposition, CaCLR 公式及实现细节, CKA 分析
- **Results**: 按 4 个 claim 组织，每个 claim 对应 experiment_data.json 中的实验数据
  - Claim 1: 3 架构 Pareto frontier（Tables 1-2）
  - Claim 2: difficulty-capability decomposition（Table 3）
  - Claim 3: CaCLR 全部分析——β sweep、component ablation、tier 分层、depth profile、CORAL 对比（Tables 4-5）
  - Claim 4: Simpson's Paradox + subspace angle（Tables 6-7）
- **Additional Analyses**: control tasks (10% artifact rate), linear projection (~40 pairs), orthogonality, probe complexity, cross-benchmark (3 benchmarks), quantization validation, 52-language extension
- **Discussion + Conclusion**: mean-shift 失败证明、practitioner 建议、limitations
- **Appendix**: per-language Spearman ρ 表、CaCLR depth profile 表

所有定量数据均来自 `experiment_data.json`，无编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bdcb3e2-1ff5-42ce-afd3-b8db8d73986e",
  "isSidechain": false,
  "requestId": "req_011CbFoFBiDecYscJGGxyR2z",
  "type": "assistant",
  "uuid": "b2ff7be0-84ff-490e-8ec6-12f6fa85c033",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/best",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vv6e15Veyh21ro8iSiFGYE",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 226,
      "cache_read_input_tokens": 72947,
      "output_tokens": 435,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 226,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 435,
          "cache_read_input_tokens": 72947,
          "cache_creation_input_tokens": 226,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 226
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

_source line 46_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122458 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direct…",
  "leafUuid": "b2ff7be0-84ff-490e-8ec6-12f6fa85c033",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate calibration paper with CaCLR method",
  "sessionId": "63663d37-a323-4180-9c6d-c85faa2f45aa"
}
```

---
