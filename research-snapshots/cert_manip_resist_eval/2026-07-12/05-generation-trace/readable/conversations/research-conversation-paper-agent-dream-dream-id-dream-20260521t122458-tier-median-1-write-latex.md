# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122458 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 67
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-3/7a93ce26-60b3-4962-9826-30997b183b7b.jsonl`
- **Structured JSON:** [`1ba579f2bc044f1faa71.json`](../../sessions/1b/1ba579f2bc044f1faa71.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T13:32:36.649Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T13:32:36.649Z",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122458 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Observational findings (Pareto, CKA, decomposition) replicate at scale but with smaller effect sizes and more noise. CaCLR consistency loss is inert across the full β sweep; paper pivots to planned negative-result narrative with geometric explanation (MMD matches marginals but not low-dimensional directional subspace). Simpson's Paradox confirmed in 1-2 of 3 architectures (Llama 4 Scout significant, Qwen3-235B trending, Gemma 4 borderline). Claim 2 (decomposition) downgraded from quantitative prescriptive to qualitative descriptive. Headline pivots to: \"Cross-lingual probe transfer reveals architecture-dependent depth effects; distributional matching fails but linear projection with ~80 parallel pairs is the practical label-free solution.\" Paper holds for EACL: field-level viability test + negative result + practical solution + geometric insights. Compress Claim 2 to subsection to make space for stronger negative-result analysis and CKA geometric section.\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T13:32:36.652Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T13:32:36.652Z",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b"
}
```

---

## Round 1

65 recorded events

### User

_source line 3 · 2026-05-21T13:32:36.671Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122458 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Observational findings (Pareto, CKA, decomposition) replicate at scale but with smaller effect sizes and more noise. CaCLR consistency loss is inert across the full β sweep; paper pivots to planned negative-result narrative with geometric explanation (MMD matches marginals but not low-dimensional directional subspace). Simpson's Paradox confirmed in 1-2 of 3 architectures (Llama 4 Scout significant, Qwen3-235B trending, Gemma 4 borderline). Claim 2 (decomposition) downgraded from quantitative prescriptive to qualitative descriptive. Headline pivots to: "Cross-lingual probe transfer reveals architecture-dependent depth effects; distributional matching fails but linear projection with ~80 parallel pairs is the practical label-free solution." Paper holds for EACL: field-level viability test + negative result + practical solution + geometric insights. Compress Claim 2 to subsection to make space for stronger negative-result analysis and CKA geometric section.

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "e8f1a248-e970-4548-96f9-5cd439647eab",
  "type": "user",
  "uuid": "7d1a2179-57cd-4bda-ae7d-f39b2e5338bb",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T13:32:36.671Z_

```json
{
  "parentUuid": "7d1a2179-57cd-4bda-ae7d-f39b2e5338bb",
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
  "uuid": "3e0e1e05-73a2-4033-9a92-805cb7042923",
  "timestamp": "2026-05-21T13:32:36.671Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T13:32:36.671Z_

```json
{
  "parentUuid": "3e0e1e05-73a2-4033-9a92-805cb7042923",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "110874af-7506-458d-a8fe-4f94303287d4",
  "timestamp": "2026-05-21T13:32:36.671Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
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
  "aiTitle": "Generate simulated research paper with experimental data",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b"
}
```

---

### Assistant

_source line 7 · 2026-05-21T13:32:39.316Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "110874af-7506-458d-a8fe-4f94303287d4",
  "isSidechain": false,
  "requestId": "req_011CbFoGQyxeDb37RoUK24W1",
  "type": "assistant",
  "uuid": "b8c82e78-41aa-4d9f-93ae-4f2bbdeb9621",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018yPwnvwGzrb9z5aRixHxAF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11544,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11544,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11544,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11544
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

_source line 8 · 2026-05-21T13:32:40.270Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PxaqKL8TwRmNMSYGFqP1uu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8c82e78-41aa-4d9f-93ae-4f2bbdeb9621",
  "isSidechain": false,
  "requestId": "req_011CbFoGQyxeDb37RoUK24W1",
  "type": "assistant",
  "uuid": "0263ea16-1d24-4985-96f2-85fc8219b40c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018yPwnvwGzrb9z5aRixHxAF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11544,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11544,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11544,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11544
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

_source line 9 · 2026-05-21T13:32:40.569Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VJVSQY3DZLoYnpJ3iy9Ytb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0263ea16-1d24-4985-96f2-85fc8219b40c",
  "isSidechain": false,
  "requestId": "req_011CbFoGQyxeDb37RoUK24W1",
  "type": "assistant",
  "uuid": "b97e3c4e-a753-4366-9d7a-e65159746e87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018yPwnvwGzrb9z5aRixHxAF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11544,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11544,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11544,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11544
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

_source line 10 · 2026-05-21T13:32:40.595Z_

<details><summary>↩ Tool result · `toolu_01PxaqKL8TwRmNMSYGFqP1uu`</summary>

```text
1	[
2	  {
3	    "name": "Full Pareto Frontier — Qwen3-235B-A22B (94 layers, MoE, INT4)",
4	    "description": "94-layer MoE 模型，24 probed layers (每4层取1), 20 languages × 5 transfer conditions。 MoE routing 在深层创建更强的语言特异化，产生比 7B pilot 更清晰但仍非普遍的 Pareto tradeoff。\n",
5	    "results": {
6	      "en_best_auroc": 0.81,
7	      "en_best_layer": "L80",
8	      "en_best_layer_depth_pct": 0.851,
9	      "en_auroc_range": [
10	        0.59,
11	        0.81
12	      ],
13	      "en_best_ece_raw": 0.178,
14	      "layer_depth_delta_pp": 22.0,
15	      "transfer_optimal_layer_mean": "L68",
16	      "transfer_optimal_depth_pct": 0.723,
17	      "en_transfer_layer_gap_auroc_pp": 2.5,
18	      "zs_pass_count_of_20": 15,
19	      "zs_pass_rate": 0.75,
20	      "zs_mean_auroc_at_en_optimal_layer": 0.668,
21	      "zs_mean_auroc_at_transfer_optimal_layer": 0.688,
22	      "mean_zs_auroc_drop_vs_en_pp": 12.2,
23	      "pareto_langs_with_negative_depth_transfer_rho": 14,
24	      "pareto_langs_significant_negative_rho": 9,
25	      "pareto_spearman_rho_median": -0.38,
26	      "pareto_spearman_rho_range": [
27	        -0.65,
28	        0.2
29	      ],
30	      "pareto_depth_transfer_drop_final_layers_pp": 2.3,
31	      "best_zs_auroc_by_tier": {
32	        "HIGH_mean": 0.728,
33	        "MID_mean": 0.678,
34	        "LOW_mean": 0.582
35	      },
36	      "best_zs_auroc_per_lang": {
37	        "zh": 0.738,
38	        "es": 0.745,
39	        "fr": 0.74,
40	        "de": 0.725,
41	        "pt": 0.732,
42	        "ja": 0.71,
43	        "ar": 0.695,
44	        "ru": 0.705,
45	        "ko": 0.688,
46	        "hi": 0.67,
47	        "vi": 0.68,
48	        "tr": 0.66,
49	        "sw": 0.598,
50	        "bn": 0.612,
51	        "te": 0.572,
52	        "id": 0.69,
53	        "pl": 0.698,
54	        "nl": 0.72,
55	        "uk": 0.695,
56	        "yo": 0.535
57	      },
58	      "mean_shift_delta_auroc": 0.0,
59	      "linear_proj_200_mean_auroc": 0.698,
60	      "few_shot_25_mean_auroc": 0.685,
61	      "few_shot_100_mean_auroc": 0.718,
62	      "spearman_depth_vs_transfer_positive_langs": 14
63	    },
64	    "tables": [
65	      {
66	        "name": "Table 1: Per-Language ZS AUROC and Pareto Statistics (Qwen3-235B, EN-optimal L80)",
67	        "data": "| Tier | Language | ZS AUROC | Best ZS Layer | Spearman ρ | p-value | Pattern          |\n|------|----------|----------|---------------|------------|---------|------------------|\n| HIGH | zh       | 0.738    | L68           | -0.48      | 0.018   | Clear tradeoff   |\n| HIGH | es       | 0.745    | L72           | -0.44      | 0.031   | Clear tradeoff   |\n| HIGH | fr       | 0.740    | L72           | -0.42      | 0.041   | Clear tradeoff   |\n| HIGH | de       | 0.725    | L64           | -0.51      | 0.011   | Clear tradeoff   |\n| HIGH | pt       | 0.732    | L68           | -0.39      | 0.059   | Trending         |\n| HIGH | ja       | 0.710    | L64           | -0.55      | 0.005   | Clear tradeoff   |\n| MID  | ar       | 0.695    | L72           | -0.22      | 0.301   | Weak/absent      |\n| MID  | ru       | 0.705    | L68           | -0.46      | 0.024   | Clear tradeoff   |\n| MID  | ko       | 0.688    | L68           | +0.08      | 0.711   | No tradeoff      |\n| MID  | hi       | 0.670    | L60           | -0.40      | 0.052   | Trending         |\n| MID  | vi       | 0.680    | L64           | -0.38      | 0.068   | Trending         |\n| MID  | tr       | 0.660    | L56           | -0.35      | 0.093   | Trending         |\n| MID  | id       | 0.690    | L68           | -0.43      | 0.036   | Clear tradeoff   |\n| LOW  | sw       | 0.598    | L52           | -0.28      | 0.184   | Weak             |\n| LOW  | bn       | 0.612    | L56           | -0.33      | 0.115   | Weak             |\n| LOW  | te       | 0.572    | L48           | -0.19      | 0.374   | Weak             |\n| LOW  | pl       | 0.698    | L68           | -0.45      | 0.027   | Clear tradeoff   |\n| LOW  | nl       | 0.720    | L68           | -0.47      | 0.021   | Clear tradeoff   |\n| LOW  | uk       | 0.695    | L64           | -0.41      | 0.046   | Clear tradeoff   |\n| LOW  | yo       | 0.535    | L44           | +0.12      | 0.578   | No tradeoff      |\n"
68	      },
69	      {
70	        "name": "Table 2: Transfer Method Comparison (mean across 20 languages, EN-optimal layer)",
71	        "data": "| Method              | Mean AUROC | Δ vs ZS (pp) | Paired perm p | Req. labels | Req. parallel |\n|---------------------|------------|--------------|---------------|-------------|---------------|\n| Zero-shot           | 0.668      | —            | —             | 0           | 0             |\n| Mean-shift          | 0.668      | 0.0          | n/a           | 0           | N (mean only) |\n| CaCLR (best β=0.01) | 0.671      | +0.3         | p=0.38        | 0           | ~10K parallel |\n| Linear proj (50)    | 0.684      | +1.6         | p=0.012       | 0           | 50 pairs      |\n| Linear proj (200)   | 0.698      | +3.0         | p<0.001       | 0           | 200 pairs     |\n| Few-shot 25         | 0.685      | +1.7         | p=0.008       | 25          | 0             |\n| Few-shot 100        | 0.718      | +5.0         | p<0.001       | 100         | 0             |\n"
72	      }
73	    ],
74	    "figures": [],
75	    "analysis": "Qwen3-235B 的 MoE 架构产生了 pilot 预期的清晰 Pareto，但非所有语言均参与： 9/20 语言 Spearman ρ 显著为负 (p<0.05)，另 5 个 trending (p<0.10)，6 个不显著或方向相反。 Pareto 强度与 resource tier 正相关但非完美（pl/nl/uk 虽在 LOW tier 但因与 EN 词汇重叠高，表现接近 HIGH）。 MoE routing 加速了 L64+ 的语言特异化，但效果分布在 4-8 层的范围内，不是单点 cliff。 ar/ko 不 show tradeoff 的原因需在 CKA 分析 (plan_011) 中进一步解释—— 可能是这两种语言在 Qwen3 训练数据中占比足够高，expert sharing 保持了 EN-target alignment。\n\n\nQwen3-235B 的 22B active MoE 参数从 7B pilot (EN AUROC 0.754) 提升到 ~0.81， 符合 correctness signal 随模型规模 sublinear scaling 的预期——22B/7B ≈ 3x 参数但 AUROC 提升仅 ~6pp，因为 correctness direction 的 linear accessibility 在 7B 时已接近 ceiling。 MoE routing 在深层（L64+）为不同语言激活不同 expert subset，加速 representation 语言特异化。 CKA 在 L64-L80 急剧下降（slope ~-0.022/layer），创造比 7B pilot 更清晰的 Pareto cliff。 但 \"更清晰\" 不等于 \"普遍\"：仍有 6/20 语言（主要 ar/ko + 部分低资源）不显示负 rho 或方向相反， 因为 (1) ar/ko 在 Qwen 训练数据中比例足够高，MoE routing 未完全将其与 EN 分离； (2) 极低资源语言（yo/am）全深度 AUROC 都低，depth variation 太小无法检测 tradeoff。 15/20 languages ZS AUROC > 0.58 — 新增 10 语言中 5 个通过（es/fr/de 等 HIGH 语言全通过）， 但 yo 可能低于阈值。Mean-shift 仍然恒等于 0（数学不变性不随模型规模变化）。 Transfer-optimal layer 在 L68（72% depth）而非 EN-optimal L80，gap ~2.5pp， 比 7B pilot 的 L24 vs L27 (~1.5pp) 更大但非剧烈——MoE 架构放大了 gap 但非无限放大。\n"
76	  },
77	  {
78	    "name": "Full Pareto Frontier — Llama 4 Scout (48 layers, MoE, W4A16)",
79	    "description": "48-layer 17B-16E MoE，12 probed layers (每4层取1+final), 20 languages × 5 transfer conditions。 Llama 架构族在 pilot (3.1-8B) 中显示弱 Pareto，full-scale MoE 预期延续但 Pareto 稍增。\n",
80	    "results": {
81	      "en_best_auroc": 0.77,
82	      "en_best_layer": "L44",
83	      "en_best_layer_depth_pct": 0.917,
84	      "en_auroc_range": [
85	        0.61,
86	        0.77
87	      ],
88	      "en_best_ece_raw": 0.192,
89	      "layer_depth_delta_pp": 16.0,
90	      "transfer_optimal_layer_mean": "L36",
91	      "transfer_optimal_depth_pct": 0.75,
92	      "en_transfer_layer_gap_auroc_pp": 1.5,
93	      "zs_pass_count_of_20": 14,
94	      "zs_pass_rate": 0.7,
95	      "zs_mean_auroc_at_en_optimal_layer": 0.648,
96	      "zs_mean_auroc_at_transfer_optimal_layer": 0.66,
97	      "mean_zs_auroc_drop_vs_en_pp": 11.0,
98	      "pareto_langs_with_negative_depth_transfer_rho": 11,
99	      "pareto_langs_significant_negative_rho": 5,
100	      "pareto_spearman_rho_median": -0.25,
101	      "pareto_spearman_rho_range": [
102	        -0.52,
103	        0.38
104	      ],
105	      "pareto_depth_transfer_drop_final_layers_pp": 1.2,
106	      "best_zs_auroc_by_tier": {
107	        "HIGH_mean": 0.708,
108	        "MID_mean": 0.658,
109	        "LOW_mean": 0.562
110	      },
111	      "best_zs_auroc_per_lang": {
112	        "zh": 0.718,
113	        "es": 0.725,
114	        "fr": 0.72,
115	        "de": 0.705,
116	        "pt": 0.712,
117	        "ja": 0.69,
118	        "ar": 0.672,
119	        "ru": 0.685,
120	        "ko": 0.68,
121	        "hi": 0.645,
122	        "vi": 0.658,
123	        "tr": 0.635,
124	        "sw": 0.578,
125	        "bn": 0.59,
126	        "te": 0.555,
127	        "id": 0.672,
128	        "pl": 0.678,
129	        "nl": 0.7,
130	        "uk": 0.67,
131	        "yo": 0.52
132	      },
133	      "mean_shift_delta_auroc": 0.0,
134	      "linear_proj_200_mean_auroc": 0.678,
135	      "few_shot_100_mean_auroc": 0.7,
136	      "spearman_depth_vs_transfer_positive_langs": 13
137	    },
138	    "tables": [
139	      {
140	        "name": "Table 3: Architecture Comparison — Pareto Strength",
141	        "data": "| Metric                         | Qwen3-235B (MoE) | Llama4 Scout (MoE) |\n|--------------------------------|-------------------|--------------------|\n| EN best AUROC                  | 0.81              | 0.77               |\n| Mean ZS AUROC (EN-opt layer)   | 0.668             | 0.648              |\n| Pareto significant langs (/20) | 9                 | 5                  |\n| Median per-lang Pareto ρ       | -0.38             | -0.25              |\n| CKA cliff onset (% depth)      | ~68%              | ~50%               |\n| CKA depth gradient (cliff)     | -0.022/layer      | -0.013/layer       |\n| EN-opt vs Transfer-opt gap (pp)| 2.5               | 1.5                |\n"
142	      },
143	      {
144	        "name": "Table 4: Divergent Languages Between Architectures",
145	        "data": "| Language | Qwen3 ρ | Qwen3 p | Llama4 ρ | Llama4 p | Pattern     |\n|----------|---------|---------|----------|----------|-------------|\n| ar       | -0.22   | 0.301   | +0.18    | 0.575    | Divergent   |\n| ko       | +0.08   | 0.711   | +0.32    | 0.311    | Both pos    |\n| vi       | -0.38   | 0.068   | +0.15    | 0.641    | Divergent   |\n| ja       | -0.55   | 0.005   | -0.42    | 0.175    | Both neg    |\n| hi       | -0.40   | 0.052   | -0.48    | 0.115    | Both neg    |\n"
146	      }
147	    ],
148	    "figures": [],
149	    "analysis": "两个 MoE 架构的 Pareto 差异证实架构依赖性——但差异根源是 CKA gradient shape， 不是 MoE vs dense (需 Gemma 4 dense 对照验证)。Llama4 的渐进 CKA decline 意味着 cross-lingual alignment 是渐变退化而非突变，实践意义是：layer selection 对 Llama4 不那么关键， 任何 50-90% depth 的层都是 reasonable choice，而 Qwen3 有明确的 optimal window (60-75% depth)。 ar/ko/vi 在 Llama4 上的正向深度效应扩大了 pilot 发现——这些语言在 Llama 训练数据中 representation 可能与 EN 共享更多 expert（tokenizer 和 training distribution 的差异是 observational confound，n=2 architectures 不做因果归因）。\n\n\nLlama 4 Scout (17B active) 从 pilot Llama-3.1-8B (EN 0.728) 提升到 ~0.77， 提升幅度低于 Qwen3 的 scaling，因为 Llama 4 的 16-expert MoE 在中层已开始 expert specialization， correctness signal 在 L20-L36 plateau 而非持续爬升到最深层。 Pilot 中 Llama 的弱 Pareto 模式延续：仅 5/20 语言显著负 rho (p<0.05)， 另 6 个 trending，9 个不显著或方向相反。ar/ko 延续 pilot 中的正向深度效应 （ZS AUROC 随深度单调增加，无 tradeoff），扩展到 vi 也呈此模式。 关键架构差异在 CKA depth gradient：Llama CKA decline 从 ~50% depth 开始渐进下降 (slope ~-0.013/layer)，而非 Qwen3 的 ~68% depth 后骤降 (slope ~-0.022/layer)。 渐进 CKA decline → tradeoff 分散在更宽的层范围 → per-language Spearman ρ magnitude 更小。 EN-optimal (L44) vs transfer-optimal (L36) gap 仅 ~1.5pp vs Qwen3 的 ~2.5pp。 12 probed layers 的较少层采样（vs Qwen3 的 24 层）也降低了 Spearman 检验功效 (n=12 vs n=24)。\n"
150	  },
151	  {
152	    "name": "CaCLR Implementation and Systematic Negative Result",
153	    "description": "CaCLR (BCE + α·SB-ECE + β·MMD) 完整实现。β sweep 3 OOM (0.001-1.0)， component ablation, CORAL comparison, high-dim MMD (PCA d=50/100), multi-seed, mixed β criterion。 Median tier: consistency loss inert → negative result + geometric explanation。\n",
154	    "results": {
155	      "caclr_mean_delta_auroc_vs_zs_pp": 0.3,
156	      "caclr_delta_auroc_range_pp": [
157	        -0.8,
158	        1.2
159	      ],
160	      "caclr_langs_improved_of_20": 8,
161	      "caclr_langs_degraded_of_20": 5,
162	      "caclr_langs_unchanged_of_20": 7,
163	      "caclr_best_beta": 0.01,
164	      "caclr_best_alpha": 0.3,
165	      "beta_sweep": {
166	        "beta_0.001": {
167	          "mean_delta_auroc_pp": 0.1,
168	          "paired_perm_p": 0.72,
169	          "cohen_d": 0.02
170	        },
171	        "beta_0.01": {
172	          "mean_delta_auroc_pp": 0.3,
173	          "paired_perm_p": 0.38,
174	          "cohen_d": 0.06
175	        },
176	        "beta_0.1": {
177	          "mean_delta_auroc_pp": -0.1,
178	          "paired_perm_p": 0.65,
179	          "cohen_d": 0.03
180	        },
181	        "beta_1.0": {
182	          "mean_delta_auroc_pp": -0.7,
183	          "paired_perm_p": 0.15,
184	          "cohen_d": 0.15
185	        }
186	      },
187	      "alpha_sweep": {
188	        "alpha_0.01": {
189	          "mean_delta_ece_pp": -0.2,
190	          "mean_delta_auroc_pp": 0.0
191	        },
192	        "alpha_0.1": {
193	          "mean_delta_ece_pp": -0.6,
194	          "mean_delta_auroc_pp": -0.1
195	        },
196	        "alpha_1.0": {
197	          "mean_delta_ece_pp": -1.8,
198	          "mean_delta_auroc_pp": -0.5
199	        },
200	        "alpha_10.0": {
201	          "mean_delta_ece_pp": -2.3,
202	          "mean_delta_auroc_pp": -1.4
203	        }
204	      },
205	      "component_ablation": {
206	        "bce_only": {
207	          "auroc": 0.668,
208	          "ece": 0.19
209	        },
210	        "bce_sbece": {
211	          "auroc": 0.665,
212	          "ece": 0.175
213	        },
214	        "bce_mmd": {
215	          "auroc": 0.67,
216	          "ece": 0.188
217	        },
218	        "bce_sbece_mmd": {
219	          "auroc": 0.669,
220	          "ece": 0.174
221	        }
222	      },
223	      "coral_comparison": {
224	        "coral_mean_delta_auroc_pp": 0.4,
225	        "coral_p_vs_zs": 0.32,
226	        "coral_conclusion": "also inert — distributional matching failure is general, not MMD-specific"
227	      },
228	      "high_dim_mmd": {
229	        "pca_d50_mean_delta_auroc_pp": 0.5,
230	        "pca_d50_p_vs_zs": 0.28,
231	        "pca_d100_mean_delta_auroc_pp": 0.2,
232	        "pca_d100_p_vs_zs": 0.51,
233	        "conclusion": "high-dim MMD also inert — broadens distributional matching failure claim"
234	      },
235	      "multi_seed_std": {
236	        "caclr_auroc_std": 0.003,
237	        "few_shot_25_auroc_std": 0.005,
238	        "few_shot_100_auroc_std": 0.004,
239	        "procrustes_auroc_std": 0.002
240	      },
241	      "mixed_beta_criterion": {
242	        "en_only_best_beta": 0.01,
243	        "en_zh_sw_best_beta": 0.01,
244	        "conclusion": "mixed criterion selects same β — no systematic bias"
245	      },
246	      "method_comparison_mean_20lang": {
247	        "zero_shot": 0.668,
248	        "mean_shift": 0.668,
249	        "caclr_best": 0.671,
250	        "coral_best": 0.672,
251	        "high_dim_mmd_best": 0.673,
252	        "linear_proj_50": 0.684,
253	        "linear_proj_200": 0.698,
254	        "few_shot_25": 0.685,
255	        "few_shot_100": 0.718
256	      },
257	      "implementation_spec": {
258	        "mmd_kernel": "Gaussian RBF, bandwidth via median heuristic (recomputed per batch)",
259	        "optimizer": "Adam, lr=5e-4, cosine decay to 1e-5",
260	        "epochs": 50,
261	        "early_stopping": "patience=10 on validation BCE loss",
262	        "initialization": "from standard LR solution (warm-start)",
263	        "batch_size": 256,
264	        "mmd_items": "same as BCE (probe_train split, 70% of GlobalMMLU test)",
265	        "parallel_set_size_range": [
266	          8500,
267	          12200
268	        ],
269	        "seeds": [
270	          42,
271	          137,
272	          256
273	        ]
274	      }
275	    },
276	    "tables": [
277	      {
278	        "name": "Table 5: β Sweep Results (Qwen3-235B, L68, mean 20 languages, 3 seeds)",
279	        "data": "| β     | Mean AUROC | Δ vs ZS (pp) | 95% Boot CI (pp)  | Cohen's d | Interpretation      |\n|-------|------------|--------------|-------------------|-----------|---------------------|\n| 0     | 0.668      | —            | —                 | —         | ZS baseline         |\n| 0.001 | 0.669      | +0.1         | [-0.5, +0.7]      | 0.02      | Negligible          |\n| 0.01  | 0.671      | +0.3         | [-0.4, +1.0]      | 0.06      | Negligible          |\n| 0.1   | 0.667      | -0.1         | [-0.8, +0.6]      | 0.03      | Negligible          |\n| 1.0   | 0.661      | -0.7         | [-1.4, +0.0]      | 0.15      | Slight degradation  |\n"
280	      },
281	      {
282	        "name": "Table 6: Distributional Matching Ablation (all methods, mean 20 langs)",
283	        "data": "| Method               | Operates on | Mean AUROC | Δ vs ZS | p-value | Conclusion |\n|----------------------|-------------|------------|---------|---------|------------|\n| MMD (1-D logit)      | probe logit | 0.671      | +0.3pp  | 0.38    | Inert      |\n| MMD (PCA d=50)       | activations | 0.673      | +0.5pp  | 0.28    | Inert      |\n| MMD (PCA d=100)      | activations | 0.670      | +0.2pp  | 0.51    | Inert      |\n| CORAL (1-D logit)    | probe logit | 0.672      | +0.4pp  | 0.32    | Inert      |\n| CORAL (PCA d=50)     | activations | 0.671      | +0.3pp  | 0.40    | Inert      |\n| Linear projection    | activations | 0.698      | +3.0pp  | <0.001  | Effective  |\n| Few-shot 100         | labels      | 0.718      | +5.0pp  | <0.001  | Effective  |\n"
284	      },
285	      {
286	        "name": "Table 7: CKA Subspace Angle — Why Distributional Matching Fails",
287	        "data": "| Language Tier | Mean subspace angle (EN→target) | MMD dist before | MMD dist after CaCLR | Angle after CaCLR | Interpretation                |\n|--------------|----------------------------------|-----------------|----------------------|--------------------|-------------------------------|\n| HIGH         | 11°                              | 0.018           | 0.008                | 10.5°              | MMD reduces, angle unchanged  |\n| MID          | 23°                              | 0.042           | 0.018                | 22°                | MMD reduces, angle unchanged  |\n| LOW          | 44°                              | 0.105           | 0.048                | 42°                | MMD reduces, angle unchanged  |\n"
288	      }
289	    ],
290	    "figures": [],
291	    "analysis": "CaCLR negative result 贡献在三个层面：(1) Systematic β sweep (3 OOM × 2 architectures × 20 langs) 关闭了 MMD-based consistency loss 路径；(2) CORAL + high-dim MMD ablation 扩展结论到 \"distributional matching in general fails for correctness probe transfer\"——不是 MMD 的问题， 是 marginal-conditional mismatch 的本质问题；(3) CKA subspace angle analysis 提供几何解释： CaCLR 成功减小了 marginal distance 但 correctness subspace angle 几乎不变。 Constructive framing: CaCLR 是 \"the natural baseline that tests the distributional matching hypothesis\"——其失败不是方法论错误，而是对 Zhao et al. (2019) 理论的实证验证， 同时指向 linear projection (~80 pairs) 作为 practical recommendation。\n\n\nCaCLR 的 MMD consistency loss 在 1-D probe logit 空间操作，这是根本的 architectural mismatch。 Correctness information 占据高维 activation 空间的 1-3 维子空间；MMD 只能匹配 logit 的 marginal distribution (均值/方差)，无法检测或纠正 correctness direction 的旋转。 β=0.001-0.01 时 consistency loss 太弱，等效于 pure BCE；β=0.1-1.0 时 loss 开始干扰 BCE 训练——强制匹配 marginal 反而扰动了 EN probe 已学到的 correctness direction，AUROC 下降。 8/20 语言 show 微小正 delta (0.1-1.2pp) 但无一统计显著——这是 noise 而非 signal。 CORAL (second-order alignment) 和 high-dim MMD (PCA d=50/100) 也无效—— distributional matching 的失败不限于 MMD kernel 或操作维度，而是因为 Zhao et al. (2019) 的理论预测成立：P(correct|activation) 的 conditional structure 在不同语言间不同（language-specific capability component），marginal matching 无法修复 conditional mismatch。CKA subspace analysis 将提供几何证据：CaCLR 成功减小了 marginal distance 但 subspace angle 几乎不变（见 plan_011 交叉分析）。 与此对照，linear projection 直接学习旋转矩阵，绕过 distributional matching 的局限。 Multi-seed 结果稳定 (std ~0.002-0.005)，排除 single-seed artifact 的可能。\n"
292	  },
293	  {
294	    "name": "Difficulty-Controlled Decomposition Ablation",
295	    "description": "IRT difficulty probes → project out difficulty direction → retrain correctness probes → evaluate transfer。 10 languages × 8 layers × 3 models。含 random-direction control。 Median tier: 定性分离成立但 prescriptive 能力弱，弱化为 descriptive。\n",
296	    "results": {
297	      "mean_delta_auroc_difficulty_projected_pp": 1.8,
298	      "delta_auroc_range_pp": [
299	        -1.2,
300	        3.5
301	      ],
302	      "langs_with_positive_delta_of_10": 6,
303	      "langs_with_negative_delta_of_10": 2,
304	      "langs_with_negligible_delta_of_10": 2,
305	      "random_direction_mean_delta_pp": 0.7,
306	      "difficulty_vs_random_effect_ratio": 2.6,
307	      "difficulty_probe_r2": 0.32,
308	      "per_lang_results": {
309	        "zh": {
310	          "delta_pp": 0.8,
311	          "sig": false
312	        },
313	        "es": {
314	          "delta_pp": 1.2,
315	          "sig": false
316	        },
317	        "fr": {
318	          "delta_pp": 1.5,
319	          "sig": true
320	        },
321	        "de": {
322	          "delta_pp": 1.8,
323	          "sig": true
324	        },
325	        "hi": {
326	          "delta_pp": 2.8,
327	          "sig": true
328	        },
329	        "ru": {
330	          "delta_pp": 2.2,
331	          "sig": true
332	        },
333	        "ko": {
334	          "delta_pp": -0.6,
335	          "sig": false
336	        },
337	        "tr": {
338	          "delta_pp": 2.5,
339	          "sig": true
340	        },
341	        "sw": {
342	          "delta_pp": -1.2,
343	          "sig": false
344	        },
345	        "bn": {
346	          "delta_pp": 3.5,
347	          "sig": true
348	        }
349	      },
350	      "decomposition_clean_separation_count_of_10": 5,
351	      "prescriptive_accuracy": 0.56
352	    },
353	    "tables": [
354	      {
355	        "name": "Table 8: Decomposition Results by Language (Qwen3-235B, 8-layer mean)",
356	        "data": "| Language | Tier | Full AUROC | Diff-proj AUROC | Δ (pp) | Random-proj AUROC | Rand Δ (pp) | Diff-specific (pp) |\n|----------|------|------------|-----------------|--------|-------------------|-------------|--------------------|\n| zh       | HIGH | 0.738      | 0.746           | +0.8   | 0.742             | +0.4        | +0.4               |\n| es       | HIGH | 0.745      | 0.757           | +1.2   | 0.751             | +0.6        | +0.6               |\n| fr       | HIGH | 0.740      | 0.755           | +1.5   | 0.747             | +0.7        | +0.8               |\n| de       | HIGH | 0.725      | 0.743           | +1.8   | 0.733             | +0.8        | +1.0               |\n| hi       | MID  | 0.670      | 0.698           | +2.8   | 0.678             | +0.8        | +2.0               |\n| ru       | MID  | 0.705      | 0.727           | +2.2   | 0.713             | +0.8        | +1.4               |\n| ko       | MID  | 0.688      | 0.682           | -0.6   | 0.691             | +0.3        | -0.9               |\n| tr       | MID  | 0.660      | 0.685           | +2.5   | 0.668             | +0.8        | +1.7               |\n| sw       | LOW  | 0.598      | 0.586           | -1.2   | 0.601             | +0.3        | -1.5               |\n| bn       | LOW  | 0.612      | 0.647           | +3.5   | 0.620             | +0.8        | +2.7               |\n"
357	      }
358	    ],
359	    "figures": [],
360	    "analysis": "Decomposition 支持 \"correctness transfer contains difficulty-shared and capability-specific components\" 的定性结论。6/10 语言 show improvement，其中 5 具有统计显著性，且 difficulty-specific effect consistently exceeds random-direction control。但 prescriptive accuracy (56%) 与 chance (50%) 差距极小——decomposition 不是 reliable strategy selector。 Paper 中弱化 Claim 2 为 subsection-level descriptive finding，压缩到 ~1 page： \"We observe that projecting out the shared difficulty component generally improves transfer for mid-resource languages (+2-3pp) but can harm low-resource languages where difficulty and capability are more entangled. This separation is descriptive rather than prescriptive — it explains what transfer contains but does not predict optimal strategy.\"\n\n\nDifficulty 成分确实跨语言共享（IRT difficulty 与语言无关），projection 后 residual 更 capability-specific。 平均 +1.8pp 改善高于 random-direction control 的 +0.7pp，比值 2.6 表明约 60% 的效果是 difficulty-specific，40% 来自纯维度缩减降噪。但效果 modest (<3pp for most languages)， 原因：(1) difficulty probe R²=0.32 意味着 projection 不完全——只移除了 32% 的 difficulty 方差； (2) difficulty 和 capability 在 activation 空间中不正交——projection 在 ko/sw 中损害了 AUROC， 因为这些语言的 difficulty-capability 纠缠更深（ko 的 MMLU difficulty ordering 与 EN 差异大， sw 的 correctness signal 本身就弱，projection 后更弱）； (3) HIGH 资源语言（zh/es）改善小是因为 capability 成分已经 well-aligned（不需要 decomposition）， MID/LOW 资源语言改善更大是因为 removing difficulty confound 确实帮助—— 但仅在 correctness signal 足够强的 MID 语言上 (hi/ru/tr/bn)。 Prescriptive accuracy 56% (vs chance 50%) 表明 decomposition 无法可靠预测最优对齐策略。 弱化 Claim 2 为 \"descriptive separation observed; difficulty-capability entanglement varies across languages but decomposition does not reliably predict optimal transfer strategy\"。\n"
361	  },
362	  {
363	    "name": "Cross-Lingual Orthogonality Analysis",
364	    "description": "提取 verbalized confidence direction，计算与 correctness direction 的 cosine similarity， 20 languages × 2+ architectures。Supporting evidence for Claim 4 (subsection)。\n",
365	    "results": {
366	      "mean_cosine_all_langs": 0.04,
367	      "cosine_range": [
368	        0.01,
369	        0.148
370	      ],
371	      "langs_below_0.05": 13,
372	      "langs_below_0.10": 17,
373	      "langs_above_0.10": 3,
374	      "per_tier_mean_cosine": {
375	        "HIGH": 0.026,
376	        "MID": 0.044,
377	        "LOW": 0.075
378	      },
379	      "architecture_comparison": {
380	        "qwen3_mean": 0.037,
381	        "llama4_mean": 0.043,
382	        "difference_sig": false
383	      },
384	      "outlier_langs": [
385	        "am",
386	        "yo",
387	        "te"
388	      ],
389	      "outlier_cosine": [
390	        0.148,
391	        0.122,
392	        0.105
393	      ]
394	    },
395	    "tables": [
396	      {
397	        "name": "Table 9: Correctness-Confidence Cosine Similarity by Resource Tier",
398	        "data": "| Tier | n  | Mean cos | Std   | Min   | Max   | n < 0.05 | n < 0.10 |\n|------|----|----------|-------|-------|-------|----------|----------|\n| HIGH | 6  | 0.026    | 0.010 | 0.010 | 0.042 | 5        | 6        |\n| MID  | 8  | 0.044    | 0.016 | 0.022 | 0.072 | 4        | 8        |\n| LOW  | 6  | 0.075    | 0.038 | 0.030 | 0.148 | 2        | 3        |\n"
399	      }
400	    ],
401	    "figures": [],
402	    "analysis": "Orthogonality 作为 subsection supporting evidence 充分：17/20 languages cosine < 0.10, 13/20 < 0.05。结论 compact：correctness-confidence orthogonality is cross-lingually robust, reinforcing the necessity of probe-based calibration methods over output-based approaches. am/yo/te 高 cosine 与 plan_013 selectivity analysis 交叉验证——若 selectivity < 0.05, 则标注为 unreliable measurement。\n\n\nMiao & Ungar (2026) 在 English 7-8B 上发现 cosine < 0.04。跨语言扩展时： HIGH 资源语言复现此结果（模型对这些语言的 correctness 和 confidence direction 都稳定， 分化清晰）。MID 语言 cosine 略高（0.03-0.06），因为 verbalized confidence 在中资源语言上 更不稳定（模型在这些语言上的 confidence verbalization 训练数据更少）。 LOW 资源语言中 am/yo/te 出现较高 cosine (>0.10)——这不是真正的 correctness-confidence alignment，而是两个 direction 都很弱时 cosine 被噪声主导的 artifact。 plan_013 full-scale control task 将确认这些语言的 deep-layer selectivity < 0.05。 两个架构间差异不显著 (0.037 vs 0.043, p=0.42)——orthogonality 是 representation 的 structural property，不随架构变化。\n"
403	  },
404	  {
405	    "name": "Probe Complexity Comparison (LR vs 2-Layer MLP)",
406	    "description": "每层每模型对比 logistic regression 和 2-layer MLP 的 EN accuracy、 cross-lingual transfer degradation 和 calibration quality。CPU-bound。\n",
407	    "results": {
408	      "qwen3": {
409	        "lr_en_best_auroc": 0.81,
410	        "mlp_en_best_auroc": 0.832,
411	        "lr_mean_zs_auroc": 0.668,
412	        "mlp_mean_zs_auroc": 0.638,
413	        "lr_transfer_gap_pp": 14.2,
414	        "mlp_transfer_gap_pp": 19.4
415	      },
416	      "llama4": {
417	        "lr_en_best_auroc": 0.77,
418	        "mlp_en_best_auroc": 0.792,
419	        "lr_mean_zs_auroc": 0.648,
420	        "mlp_mean_zs_auroc": 0.622,
421	        "lr_transfer_gap_pp": 12.2,
422	        "mlp_transfer_gap_pp": 17.0
423	      },
424	      "mlp_en_advantage_mean_pp": 2.1,
425	      "lr_transfer_advantage_mean_pp": 3.0,
426	      "lr_preferred_for_transfer": true,
427	      "mlp_preferred_for_en_only": true
428	    },
429	    "tables": [
430	      {
431	        "name": "Table 10: LR vs MLP Transfer Comparison",
432	        "data": "| Metric                    | Qwen3 LR | Qwen3 MLP | Llama4 LR | Llama4 MLP |\n|---------------------------|----------|-----------|-----------|------------|\n| EN best AUROC             | 0.810    | 0.832     | 0.770     | 0.792      |\n| Mean ZS AUROC             | 0.668    | 0.638     | 0.648     | 0.622      |\n| Transfer gap (pp)         | 14.2     | 19.4      | 12.2      | 17.0       |\n| EN ECE (best layer)       | 0.178    | 0.165     | 0.192     | 0.178      |\n| Mean ZS ECE               | 0.218    | 0.248     | 0.228     | 0.258      |\n| ZS pass rate (>0.58)      | 75%      | 55%       | 70%       | 50%        |\n"
433	      }
434	    ],
435	    "figures": [],
436	    "analysis": "LR vs MLP 验证了 linear probe 是 cross-lingual transfer 的正确方法论选择。 Paper 中报告为 methodology validation (1-2 paragraphs)，不展开为独立贡献。\n\n\nMLP (2-layer, 256 hidden units) 多出的参数让它学到 EN-specific activation patterns （如英语特有的 token position bias、named entity patterns 等），EN AUROC +2.1pp。 但这些 EN-specific patterns 不跨语言迁移——MLP 过拟合了 EN distributional structure。 LR 被迫学习单一 hyperplane（1 个 correctness direction），更可能对应 language-agnostic subspace。 Transfer gap: LR ~13pp vs MLP ~18pp——MLP 多出的 ~5pp gap 分解为 EN advantage (~2pp) + EN-specific overfitting (~3pp)。 ECE 模式相同：MLP 在 EN 上 ECE 更好（更多参数→更好的概率估计）， 但在 ZS transfer 时 ECE 更差（overfitted probabilities 在新 distribution 上更 miscalibrated）。\n"
437	  },
438	  {
439	    "name": "Additional Benchmark Evaluation (Belebele + MMLU-ProX)",
440	    "description": "在 Belebele (RC) 和 MMLU-ProX (翻译 MMLU) 上评估 best probes + all transfer methods。 验证 generalization beyond GlobalMMLU。20 languages × 2 models。\n",
441	    "results": {
442	      "belebele": {
443	        "en_best_auroc": 0.75,
444	        "mean_zs_auroc": 0.632,
445	        "zs_pass_rate": 0.6,
446	        "pareto_preserved": true,
447	        "pareto_strength": "weaker than GlobalMMLU (fewer sig langs)",
448	        "pareto_sig_langs_of_20": 6,
449	        "rank_corr_with_globalmmlu": 0.84,
450	        "linear_proj_delta_pp": 2.5,
451	        "caclr_delta_pp": 0.2
452	      },
453	      "mmlu_prox": {
454	        "en_best_auroc": 0.79,
455	        "mean_zs_auroc": 0.658,
456	        "zs_pass_rate": 0.72,
457	        "pareto_preserved": true,
458	        "pareto_strength": "comparable to GlobalMMLU",
459	        "pareto_sig_langs_of_20": 8,
460	        "rank_corr_with_globalmmlu": 0.92,
461	        "linear_proj_delta_pp": 2.8,
462	        "caclr_delta_pp": 0.3
463	      },
464	      "cross_benchmark_lang_ranking_rho": 0.89,
465	      "linear_proj_generalizes": true,
466	      "caclr_still_inert": true
467	    },
468	    "tables": [
469	      {
470	        "name": "Table 11: Cross-Benchmark Consistency (Qwen3-235B)",
471	        "data": "| Metric             | GlobalMMLU | Belebele | MMLU-ProX |\n|--------------------|------------|----------|-----------|\n| EN best AUROC      | 0.81       | 0.75     | 0.79      |\n| Mean ZS AUROC      | 0.668      | 0.632    | 0.658     |\n| ZS pass rate       | 75%        | 60%      | 72%       |\n| Pareto sig langs   | 9          | 6        | 8         |\n| Linear proj Δ (pp) | +3.0       | +2.5     | +2.8      |\n| CaCLR Δ (pp)       | +0.3       | +0.2     | +0.3      |\n"
472	      }
473	    ],
474	    "figures": [],
475	    "analysis": "Cross-benchmark 验证确认主要发现的 robustness。Belebele 上 Pareto 更弱是预期的。 Key message: \"all qualitative findings (architecture dependence, resource-tier gradient, CaCLR failure, linear projection effectiveness) generalize across benchmarks.\"\n\n\nBelebele 是阅读理解（passage-dependent correctness），与 GlobalMMLU 的 parametric knowledge 不同——correctness signal 的性质部分不同。EN AUROC 略低 (0.75 vs 0.81)，因为 RC correctness 更依赖 passage comprehension 而非 parametric knowledge，probe 的 linear accessibility 稍低。Transfer 更差因为 RC 的 cross-lingual alignment 更依赖 word-level translation quality。 但 Pareto 结构保留——depth-transferability tradeoff 是 representation geometry 的性质。 MMLU-ProX 与 GlobalMMLU 高度相关（同源翻译数据），模式几乎一致 (rho=0.92)。 Cross-benchmark language ranking rho=0.89——结果不是 benchmark-specific。 CaCLR 在两个 benchmark 上仍 inert，linear projection 仍有效——泛化确认。\n"
476	  },
477	  {
478	    "name": "Gemma 4 32.7B Dense — Third Architecture",
479	    "description": "Dense 架构对照 (vs 两个 MoE)，60 text decoder layers, BF16, 20 languages。 提供 dense vs MoE architectural contrast。P0 for core submission。\n",
480	    "results": {
481	      "en_best_auroc": 0.79,
482	      "en_best_layer": "L52",
483	      "en_best_layer_depth_pct": 0.867,
484	      "en_auroc_range": [
485	        0.6,
486	        0.79
487	      ],
488	      "en_best_ece_raw": 0.182,
489	      "layer_depth_delta_pp": 19.0,
490	      "transfer_optimal_layer_mean": "L44",
491	      "transfer_optimal_depth_pct": 0.733,
492	      "en_transfer_layer_gap_auroc_pp": 1.8,
493	      "zs_pass_count_of_20": 14,
494	      "zs_pass_rate": 0.7,
495	      "zs_mean_auroc_at_en_optimal_layer": 0.66,
496	      "mean_zs_auroc_drop_vs_en_pp": 11.0,
497	      "pareto_langs_significant_negative_rho": 7,
498	      "pareto_spearman_rho_median": -0.32,
499	      "pareto_depth_transfer_drop_final_layers_pp": 1.6,
500	      "cka_cliff_slope": -0.014,
501	      "cka_cliff_onset_depth_pct": 0.58,
502	      "partial_rho_cka": 0.24,
503	      "partial_p": 0.038,
504	      "simpson_significant": true
505	    },
506	    "tables": [
507	      {
508	        "name": "Table 12: Three-Architecture Comparison",
509	        "data": "| Metric                      | Qwen3-235B (MoE) | Llama4 Scout (MoE) | Gemma4 31B (Dense) |\n|-----------------------------|-------------------|--------------------|---------------------|\n| Type                        | MoE (22B active)  | MoE (17B active)   | Dense (31B)         |\n| Total / Active params       | 235B / 22B        | 109B / 17B         | 31B / 31B           |\n| Layers                      | 94                | 48                 | 60                  |\n| EN best AUROC               | 0.81              | 0.77               | 0.79                |\n| Mean ZS AUROC               | 0.668             | 0.648              | 0.660               |\n| Pareto sig langs (/20)      | 9                 | 5                  | 7                   |\n| Median Pareto ρ             | -0.38             | -0.25              | -0.32               |\n| CKA cliff slope             | -0.022            | -0.013             | -0.014              |\n| Partial ρ (CKA~AUROC|depth) | 0.16 (p=.072)     | 0.29 (p=.018)      | 0.24 (p=.038)       |\n| Simpson's sig?              | Trending          | Yes                | Yes                 |\n"
510	      }
511	    ],
512	    "figures": [],
513	    "analysis": "Gemma 4 作为 dense 对照确认 Pareto 不是 MoE artifact。三架构的 CKA cliff slope 与 Pareto 强度呈清晰的 monotonic relationship (steeper → more languages with tradeoff)， 但 n=3 仅为 suggestive。Simpson's Paradox 变为 2/3 显著——strengthens geometric narrative。 Paper 中强调 architecture dependence 是 descriptive finding (各架构 scale/depth/training data all differ, 无法 isolate 单一因素)。\n\n\nDense 架构的 CKA decline 比 MoE 更线性渐进——无 expert routing 加速特异化机制， 所有参数共享导致语言 representation 的分化更缓慢。 CKA slope ~-0.014/layer，介于 Qwen3 (-0.022) 和 Llama4 (-0.013) 之间。 EN AUROC ~0.79 (31B full params) 接近 Qwen3 的 0.81 (22B active MoE)， 因为 correctness direction 的 linear accessibility 在 ~20B+ 后已接近 saturation。 Pareto 强度 intermediate: 7/20 语言显著负 rho (between Qwen3's 9 and Llama4's 5)。 Simpson's Paradox 在 Gemma 4 上显著 (partial rho=0.24, p=0.038)—— 其 linear-ish CKA decline 使得 linear partial correlation 比 Qwen3 的 step-function decline 更有效（Qwen3 partial rho=0.16, p=0.072 不显著，部分因为非线性 depth-CKA 关系）。 三架构 Simpson's confirmation: Llama4 (显著), Gemma4 (显著), Qwen3 (trending) → 2/3。 Dense vs MoE 对比核心发现：Pareto 不是 MoE-specific，dense 架构也有但更弱。 这排除了 \"Pareto tradeoff 是 MoE expert routing 的 artifact\" 的替代假说。\n"
514	  },
515	  {
516	    "name": "Extended Language Coverage (50+ Languages)",
517	    "description": "从 20 扩展至 50+ 语言，利用 GlobalMMLU/Belebele 全语言集。Camera-ready extension。\n",
518	    "results": {
519	      "total_languages": 52,
520	      "zs_pass_rate_52": 0.6,
521	      "zs_pass_count_52": 31,
522	      "artifact_rate_very_low_resource": 0.45,
523	      "new_low_resource_langs_with_artifacts": 16,
524	      "resource_tier_gradient_confirmed": true,
525	      "rank_correlation_20_vs_52": 0.95,
526	      "min_zs_auroc": 0.5,
527	      "min_zs_lang": "Haitian Creole (ht)",
528	      "new_findings": "Diminishing returns; very-low-resource languages (< 1M training tokens) uniformly near chance. Writing system clusters emerge (Cyrillic, Devanagari, Arabic script) as moderate predictor of transfer quality within resource tier.\n"
529	    },
530	    "tables": [
531	      {
532	        "name": "Table S1: Language Coverage Expansion Summary",
533	        "data": "| Tier      | 20-lang n | 52-lang n | Mean ZS AUROC | Artifact rate | Pass rate |\n|-----------|-----------|-----------|---------------|---------------|-----------|\n| HIGH      | 6         | 10        | 0.72          | 5%            | 100%      |\n| MID       | 8         | 15        | 0.66          | 20%           | 87%       |\n| LOW       | 6         | 16        | 0.58          | 32%           | 56%       |\n| VERY-LOW  | 0         | 11        | 0.53          | 45%           | 27%       |\n"
534	      }
535	    ],
536	    "figures": [],
537	    "analysis": "Camera-ready extension。Core story 不变。VERY-LOW resource languages 的高 artifact rate reinforces probing control 的必要性。Paper 中 core analysis 仍基于 20 languages (cleaner statistics)， 52-language results in extended table + map visualization。\n\n\n新增 32 语言大多为 LOW/VERY-LOW resource。Pass rate 从 20 语言的 ~72% 降至 52 语言的 ~60%， 因为新增语言偏向低资源。Very-low-resource 语言 (ht, rm, fy, gd 等) 的 artifact rate ~45%， 几乎一半的 layer-language 结果不可靠。但 20 语言的核心发现在 52 语言上完全保持 (rank corr 0.95)。 主要增量贡献：(1) 统计 power 增加 (n=52 vs n=20 for cross-language analyses)， (2) writing system 作为 transfer predictor 的新发现（同脚本语言 pair 的 CKA 更高）， (3) 覆盖面更全面的 field-level claim。边际收益递减——每新增一种语言，对核心 claim 的增量证据极小。\n"
538	  },
539	  {
540	    "name": "Quantization Validation Ablation",
541	    "description": "(a) W4A16 vs FP16 at 5 layers for Llama 4 Scout on 5% subset; (b) GPTQ-Int4 vs FP16 at 5 layers for Qwen3-235B on 5% subset.\n",
542	    "results": {
543	      "llama4_w4a16_vs_fp16": {
544	        "mean_abs_delta_auroc": 0.004,
545	        "max_abs_delta_auroc": 0.008,
546	        "per_layer_deltas": {
547	          "L8": -0.002,
548	          "L16": 0.004,
549	          "L24": -0.005,
550	          "L36": 0.003,
551	          "L44": -0.008
552	        },
553	        "cka_fp16_vs_quant_mean": 0.988
554	      },
555	      "qwen3_int4_vs_fp16": {
556	        "mean_abs_delta_auroc": 0.006,
557	        "max_abs_delta_auroc": 0.012,
558	        "per_layer_deltas": {
559	          "L16": -0.005,
560	          "L36": 0.004,
561	          "L52": -0.003,
562	          "L68": 0.006,
563	          "L80": -0.012
564	        },
565	        "cka_fp16_vs_quant_mean": 0.98
566	      },
567	      "quantization_safe": true,
568	      "conclusion": "All |ΔAUROC| < 0.015, all CKA > 0.97 — quantization artifacts negligible"
569	    },
570	    "tables": [
571	      {
572	        "name": "Table S2: Quantization Validation Per-Layer",
573	        "data": "| Model  | Layer (depth%) | FP16 AUROC | Quant AUROC | ΔAUROC  | CKA     |\n|--------|----------------|------------|-------------|---------|---------|\n| Llama4 | L8 (17%)       | 0.635      | 0.633       | -0.002  | 0.992   |\n| Llama4 | L16 (33%)      | 0.688      | 0.692       | +0.004  | 0.990   |\n| Llama4 | L24 (50%)      | 0.722      | 0.717       | -0.005  | 0.988   |\n| Llama4 | L36 (75%)      | 0.750      | 0.753       | +0.003  | 0.986   |\n| Llama4 | L44 (92%)      | 0.770      | 0.762       | -0.008  | 0.984   |\n| Qwen3  | L16 (17%)      | 0.632      | 0.627       | -0.005  | 0.988   |\n| Qwen3  | L36 (38%)      | 0.708      | 0.712       | +0.004  | 0.984   |\n| Qwen3  | L52 (55%)      | 0.742      | 0.739       | -0.003  | 0.982   |\n| Qwen3  | L68 (72%)      | 0.775      | 0.781       | +0.006  | 0.978   |\n| Qwen3  | L80 (85%)      | 0.810      | 0.798       | -0.012  | 0.972   |\n"
574	      }
575	    ],
576	    "figures": [],
577	    "analysis": "Quantization safe. 报告为一段话 + appendix table: \"Quantization artifacts are negligible (max |ΔAUROC| = 0.012, CKA > 0.97 across all layers), supporting the validity of our INT4/W4A16 experimental setup.\"\n\n\n4-bit weight quantization 保留 activation 空间的大部分结构。Correctness direction 是 低维子空间特征——quantization noise 主要分布在与 correctness direction 正交的高维 null space 中 (random projection preservation 原理)。Qwen3 的 MoE + INT4 在最深层 (L80) 有稍大 delta (-0.012pp) 因为 expert routing 决策在 INT4 下可能微变，但仍在 bootstrap CI 内。 CKA(FP16, quant) > 0.97 确认 global representation structure 保留。\n"
578	  },
579	  {
580	    "name": "Full CKA Cross-Lingual Similarity & Simpson's Paradox Analysis",
581	    "description": "Linear CKA (EN vs 20 target languages) at every probed layer, 3 models。 Core analysis: partial correlation controlling for depth (Simpson's Paradox)。 Median tier: 1-2/3 architectures significant。\n",
582	    "results": {
583	      "qwen3": {
584	        "raw_spearman_rho": -0.24,
585	        "raw_p": "<0.001",
586	        "partial_rho_ctrl_depth": 0.16,
587	        "partial_p": 0.072,
588	        "significant": false,
589	        "bootstrap_ci_95": [
590	          -0.03,
591	          0.35
592	        ],
593	        "per_layer_positive_rho_count_of_24": 17,
594	        "per_layer_significant_count": 5,
595	        "cka_cliff_onset_layer": "L64",
596	        "cka_cliff_onset_depth_pct": 0.68,
597	        "cka_final_layer_mean": 0.09,
598	        "cka_peak_layer": "L36",
599	        "cka_peak_mean": 0.82
600	      },
601	      "llama4": {
602	        "raw_spearman_rho": -0.3,
603	        "raw_p": "<0.001",
604	        "partial_rho_ctrl_depth": 0.31,
605	        "partial_p": 0.012,
606	        "significant": true,
607	        "bootstrap_ci_95": [
608	          0.08,
609	          0.52
610	        ],
611	        "per_layer_positive_rho_count_of_12": 10,
612	        "per_layer_significant_count": 4,
613	        "cka_cliff_onset_layer": "L24",
614	        "cka_cliff_onset_depth_pct": 0.5,
615	        "cka_final_layer_mean": 0.2,
616	        "cka_peak_layer": "L12",
617	        "cka_peak_mean": 0.83
618	      },
619	      "gemma4": {
620	        "raw_spearman_rho": -0.26,
621	        "raw_p": "<0.001",
622	        "partial_rho_ctrl_depth": 0.24,
623	        "partial_p": 0.038,
624	        "significant": true,
625	        "bootstrap_ci_95": [
626	          0.02,
627	          0.45
628	        ],
629	        "per_layer_positive_rho_count_of_16": 12,
630	        "per_layer_significant_count": 4,
631	        "cka_cliff_onset_layer": "L36",
632	        "cka_cliff_onset_depth_pct": 0.6,
633	        "cka_final_layer_mean": 0.15,
634	        "cka_peak_layer": "L20",
635	        "cka_peak_mean": 0.8
636	      },
637	      "simpson_paradox_confirmed_of_3": 2,
638	      "cka_transfer_collapse_threshold": 0.3,
639	      "subspace_angle_analysis": {
640	        "qwen3": {
641	          "HIGH_angle": 10,
642	          "MID_angle": 22,
643	          "LOW_angle": 46
644	        },
645	        "llama4": {
646	          "HIGH_angle": 13,
647	          "MID_angle": 26,
648	          "LOW_angle": 41
649	        },
650	        "gemma4": {
651	          "HIGH_angle": 11,
652	          "MID_angle": 24,
653	          "LOW_angle": 43
654	        }
655	      }
656	    },
657	    "tables": [
658	      {
659	        "name": "Table 13: Simpson's Paradox — Raw vs Partial Correlation (3 architectures)",
660	        "data": "| Architecture   | n obs | Raw ρ  | Raw p   | Partial ρ | Partial p | Boot 95% CI    | Sig? |\n|----------------|-------|--------|---------|-----------|-----------|----------------|------|\n| Qwen3-235B     | 480   | -0.24  | <0.001  | +0.16     | 0.072     | [-0.03, +0.35] | No   |\n| Llama4 Scout   | 240   | -0.30  | <0.001  | +0.31     | 0.012     | [+0.08, +0.52] | Yes  |\n| Gemma4 31B     | 320   | -0.26  | <0.001  | +0.24     | 0.038     | [+0.02, +0.45] | Yes  |\n| Pilot Llama8B  | 45    | -0.16  | 0.294   | +0.41     | 0.006     | [+0.12, +0.65] | Yes  |\n| Pilot Qwen7B   | 40    | -0.16  | 0.310   | +0.18     | 0.274     | [-0.15, +0.48] | No   |\n"
661	      },
662	      {
663	        "name": "Table 14: CKA Depth Profile Summary",
664	        "data": "| Depth %  | Qwen3 CKA | Llama4 CKA | Gemma4 CKA |\n|----------|-----------|------------|------------|\n| 0%       | 0.70      | 0.58       | 0.62       |\n| 17%      | 0.76      | 0.81       | 0.78       |\n| 34%      | 0.82      | 0.75       | 0.75       |\n| 50%      | 0.80      | 0.56       | 0.65       |\n| 68%      | 0.60      | 0.40       | 0.48       |\n| 77%      | 0.38      | 0.32       | 0.38       |\n| 85%      | 0.22      | 0.28       | 0.28       |\n| 100%     | 0.09      | 0.20       | 0.15       |\n"
665	      },
666	      {
667	        "name": "Table 15: Subspace Angle Analysis (Correctness Direction)",
668	        "data": "| Tier | Qwen3 angle | Llama4 angle | Gemma4 angle | Mean ZS AUROC | Interpretation          |\n|------|-------------|--------------|--------------|---------------|-------------------------|\n| HIGH | 10°         | 13°          | 11°          | 0.72          | Near-aligned            |\n| MID  | 22°         | 26°          | 24°          | 0.66          | Moderate rotation       |\n| LOW  | 46°         | 41°          | 43°          | 0.57          | Substantial misalignment|\n"
669	      }
670	    ],
671	    "figures": [],
672	    "analysis": "Simpson's Paradox 在 2/3 architectures 统计显著 (Llama4, Gemma4)，Qwen3 trending (p=0.072)。 Paper 中用 hedged language: \"In architectures with near-linear CKA depth gradients (Llama 4, Gemma 4), partial correlation controlling for depth reveals a significant positive CKA-transfer relationship (ρ=0.24-0.31, p<0.05), confirming that CKA provides genuine explanatory power beyond depth. In Qwen3-235B, the step-function-like CKA profile limits linear partial correlation effectiveness (ρ=0.16, p=0.072); within-layer analysis confirms the positive direction (17/24 layers positive ρ).\" CKA cliff slope 与 Pareto strength 的 monotonic relationship across 3 architectures is suggestive but n=3 is insufficient for formal correlation. Frame as observation. Subspace angle analysis provides the most directly interpretable geometric result: correctness direction rotates gradually from EN as language distance increases, with resource tier as a strong proxy for rotation magnitude.\n\n\nSimpson's Paradox 的架构依赖性源于 CKA-depth gradient 的函数形状。 Llama4 CKA 从 peak 0.83 (L12) 线性下降到 0.20 (L48)——steep linear slope 使得 linear partial correlation 高效地分离 depth confound (partial rho=0.31, p=0.012)。 Gemma4 CKA 也近似线性下降 (partial rho=0.24, p=0.038)——intermediate slope 产生 intermediate partial correlation，也刚好显著。 Qwen3 的 CKA profile 是 \"plateau then cliff\"：L0-L64 CKA 几乎不变 (0.75-0.82)， L64-L92 急剧下降到 0.09。这种 step-function-like profile 导致 linear partial correlation 效果差——depth 作为线性控制变量无法有效 capture 非线性 CKA-depth 关系。 Partial rho=0.16 (p=0.072) trending 但不显著。加入 depth² 作为二次控制项后可能显著， 但 paper 中应诚实报告 standard method 的结果。 Per-layer analysis (n=20 languages per layer): 大多数层的 within-layer rho 为正 (70-83% of layers across models)，但因 n=20 individual significance 有限。 最有 power 的层在 50-75% depth（CKA variance 最大的区域）。 Subspace angle 提供互补定量证据：HIGH 语言 ~10-13°（几乎对齐，zero-shot 可行）， LOW 语言 ~41-46°（严重 misaligned，需要 linear projection）。 这与 Procrustes reversal (plan_012) 的发现互洽——reversal 阈值对应 ~20-25° angle。\n"
673	  },
674	  {
675	    "name": "Linear Projection Sensitivity & Procrustes Effect Reversal",
676	    "description": "Vary parallel pairs (10, 20, 50, 100, 200) for linear projection. 2 models × 5 representative layers × 20 languages。Resource-tier stratified saturation curves。 Procrustes effect reversal analysis。\n",
677	    "results": {
678	      "overall_pairs_to_95pct": 80,
679	      "per_tier_pairs_to_95pct": {
680	        "HIGH": 38,
681	        "MID": 62,
682	        "LOW": 95
683	      },
684	      "saturation_curve": {
685	        "pairs_10": {
686	          "pct_of_max": 0.38,
687	          "mean_delta_auroc_pp": 1.1
688	        },
689	        "pairs_20": {
690	          "pct_of_max": 0.58,
691	          "mean_delta_auroc_pp": 1.7
692	        },
693	        "pairs_50": {
694	          "pct_of_max": 0.82,
695	          "mean_delta_auroc_pp": 2.5
696	        },
697	        "pairs_100": {
698	          "pct_of_max": 0.95,
699	          "mean_delta_auroc_pp": 2.9
700	        },
701	        "pairs_200": {
702	          "pct_of_max": 1.0,
703	          "mean_delta_auroc_pp": 3.0
704	        }
705	      },
706	      "procrustes_reversal": {
707	        "threshold_estimate": 0.57,
708	        "threshold_ci_95": [
709	          0.48,
710	          0.64
711	        ],
712	        "benefit_below_0.50": {
713	          "mean_delta_pp": 5.5,
714	          "n_langs": 3
715	        },
716	        "ambiguous_0.50_0.60": {
717	          "mean_delta_pp": 1.8,
718	          "n_langs": 5
719	        },
720	        "mild_benefit_0.60_0.65": {
721	          "mean_delta_pp": 0.3,
722	          "n_langs": 4
723	        },
724	        "harm_above_0.65": {
725	          "mean_delta_pp": -1.5,
726	          "n_langs": 8
727	        }
728	      },
729	      "saturation_r2_by_tier": {
730	        "HIGH": 0.97,
731	        "MID": 0.92,
732	        "LOW": 0.8
733	      },
734	      "linear_proj_delta_low_resource_pp": 5.0
735	    },
736	    "tables": [
737	      {
738	        "name": "Table 16: Saturation Curves by Resource Tier (Qwen3-235B, L68)",
739	        "data": "| Pairs | HIGH Δ (pp) | MID Δ (pp) | LOW Δ (pp) | Overall Δ (pp) |\n|-------|-------------|------------|------------|----------------|\n| 10    | +0.1        | +0.8       | +2.5       | +1.1           |\n| 20    | +0.3        | +1.5       | +3.8       | +1.7           |\n| 50    | +0.4        | +2.3       | +5.2       | +2.5           |\n| 100   | +0.5        | +2.6       | +5.8       | +2.9           |\n| 200   | +0.5        | +2.7       | +6.2       | +3.0           |\n"
740	      },
741	      {
742	        "name": "Table 17: Procrustes Effect Reversal by ZS AUROC Band",
743	        "data": "| ZS AUROC band | n langs | Mean Δ (pp) | Std  | % positive | Example langs     |\n|---------------|---------|-------------|------|------------|-------------------|\n| < 0.50        | 3       | +5.5        | 1.8  | 100%       | am, yo, te        |\n| 0.50 - 0.58   | 3       | +3.2        | 1.5  | 100%       | sw, bn, tr        |\n| 0.58 - 0.62   | 2       | +1.2        | 0.9  | 100%       | hi, vi            |\n| 0.62 - 0.67   | 4       | +0.2        | 0.8  | 50%        | ar, ko, id, uk    |\n| 0.67 - 0.72   | 4       | -0.8        | 0.6  | 25%        | ru, ja, de, pt    |\n| > 0.72        | 4       | -1.8        | 0.5  | 0%         | zh, es, fr, nl    |\n"
744	      }
745	    ],
746	    "figures": [],
747	    "analysis": "Linear projection 是最直接的 practical contribution：80 parallel pairs (约 3-4 小时标注) 达到 95% of max improvement。LOW-resource languages benefit most (+5-6pp)，正是最需要帮助的类别。 Procrustes reversal 是重要的 practitioner caveat——不加区分地做 alignment 会损害已经 well-aligned 的语言。Deployment recommendation: 先测 zero-shot AUROC，低于 0.57 时 use projection， 高于 0.65 时直接 zero-shot，0.57-0.65 区间按 language-specific validation 决定。 Architecture-dependent threshold variation: Qwen3 threshold ~0.55, Llama4 ~0.60 (Llama4 的 better baseline alignment 意味着 reversal 出现更早)—— 但 n=2 architectures 不足以 parametrize threshold，建议 practitioner 用 ~0.57 ± 0.05。\n\n\nSaturation at ~80 pairs (而非 pilot 预估的 ~50)，因为：(1) 20 语言引入更多方差， (2) 部分低资源语言的 parallel pair translation quality 低（机翻 artifacts 增加 noise）， (3) 低资源语言的 subspace angle 更大 (~40-46°)，需要更多样本来估计更复杂的旋转。 Resource-tier stratification 清晰：HIGH 语言 ~38 pairs (subspace angle ~10-13°, 简单旋转)， LOW 语言 ~95 pairs (angle ~41-46°, 更复杂旋转 + translation noise)。 Procrustes reversal mechanism: 当 ZS AUROC > 0.65 时，EN-target correctness direction 已 near-aligned (angle <15°)，Procrustes 旋转估计引入的 noise > alignment gain → 净负效果。 当 ZS AUROC < 0.50 时，严重 misalignment (angle >35°) 使得 alignment gain >> noise。 Threshold ~0.57 对应 ~20° angle 的平衡点。 LOW tier 的 curve 不够 clean (R²=0.80)——个别语言 saturation 非单调 (e.g., sw 在 20 pairs 时偶然好于 50 pairs，因为特定 pair 的 quality variance)。 Practical recommendation: ~80 parallel pairs for general use; skip projection for HIGH-resource languages (ZS AUROC > 0.65)。\n"
748	  },
749	  {
750	    "name": "Probing Control Tasks — Full Scale (20 languages × 3 models)",
751	    "description": "Hewitt & Liang (2019) control tasks 扩展到 20 languages × 3 architectures × 所有 probed layers。 验证 AUROC 反映 genuine correctness direction。Selectivity threshold sensitivity analysis。 Note: English-only pilot DONE (plan_013 registry), 此处为 full cross-lingual extension。\n",
752	    "results": {
753	      "overall_artifact_rate_pct": 22,
754	      "artifact_rate_by_tier": {
755	        "HIGH": 5,
756	        "MID": 22,
757	        "LOW": 35
758	      },
759	      "selectivity_deep_layers_mean": 0.2,
760	      "selectivity_by_tier_deep_layers": {
761	        "HIGH": 0.23,
762	        "MID": 0.16,
763	        "LOW": 0.08
764	      },
765	      "control_auroc_range": [
766	        0.48,
767	        0.52
768	      ],
769	      "threshold_sensitivity": {
770	        "threshold_0.03": {
771	          "artifact_rate_pct": 32
772	        },
773	        "threshold_0.05": {
774	          "artifact_rate_pct": 22
775	        },
776	        "threshold_0.10": {
777	          "artifact_rate_pct": 12
778	        }
779	      },
780	      "affected_zone": "primarily 0-40% depth for MID/LOW, 0-20% depth for HIGH",
781	      "cross_lingual_control_finding": "~22% of language-layer combinations have selectivity < 0.05. Concentrated in LOW-resource shallow layers (83% of L0-25% depth × LOW tier). At EN-optimal depth, only am/yo/te have selectivity < 0.05 (probe capacity artifacts).\n"
782	    },
783	    "tables": [
784	      {
785	        "name": "Table 18: Artifact Rate by Resource Tier and Depth (3-model mean)",
786	        "data": "| Depth zone     | HIGH artifact % | MID artifact % | LOW artifact % | Overall |\n|----------------|-----------------|----------------|----------------|---------|\n| 0-25% depth    | 15%             | 55%            | 80%            | 50%     |\n| 25-50% depth   | 3%              | 28%            | 55%            | 29%     |\n| 50-75% depth   | 0%              | 10%            | 18%            | 9%      |\n| 75-100% depth  | 0%              | 2%             | 5%             | 2%      |\n| Overall        | 5%              | 22%            | 35%            | 22%     |\n"
787	      },
788	      {
789	        "name": "Table 19: Selectivity at EN-Optimal Layer (representative languages)",
790	        "data": "| Tier | Language | Real AUROC | Control AUROC | Selectivity | Artifact? |\n|------|----------|------------|---------------|-------------|-----------|\n| HIGH | zh       | 0.738      | 0.502         | 0.236       | No        |\n| HIGH | es       | 0.745      | 0.498         | 0.247       | No        |\n| MID  | hi       | 0.670      | 0.506         | 0.164       | No        |\n| MID  | tr       | 0.660      | 0.510         | 0.150       | No        |\n| LOW  | sw       | 0.598      | 0.508         | 0.090       | No        |\n| LOW  | bn       | 0.612      | 0.504         | 0.108       | No        |\n| LOW  | yo       | 0.535      | 0.512         | 0.023       | YES       |\n| LOW  | am       | 0.530      | 0.515         | 0.015       | YES       |\n| LOW  | te       | 0.572      | 0.518         | 0.054       | Borderline|\n"
791	      }
792	    ],
793	    "figures": [],
794	    "analysis": "Control task 发现是独立的 methodological contribution。在 paper main body 中： (1) 用 selectivity threshold 过滤不可靠结果后重新报告 main results (confirm conclusions unchanged); (2) 报告 ~22% artifact rate 作为 methodological warning for the field; (3) 讨论 implications: \"all cross-lingual probing studies should include selectivity checks, especially for low-resource languages where probe capacity can mimic genuine signal.\" am/yo 在 EN-optimal depth 的 selectivity < 0.03 确认 plan_005 中这些语言的 高 cosine similarity 是 noise artifact 而非真实 correctness-confidence alignment。\n\nPilot (Qwen2.5-7B EN-only) 显示 selectivity 在 L20+ 为 0.24-0.26, L0-L12 为 0.02-0.04。 跨语言扩展时：HIGH 资源语言的 deep-layer selectivity 接近 EN (~0.23)—— 模型对这些语言有足够的 correctness signal 使 real probe >> control probe。 MID 资源语言 deep-layer selectivity 降至 ~0.16——仍明显超过 threshold 但 gap 缩小， 因为 (1) correctness signal 更弱, (2) control probe 在更 uniform 的 activation 分布上 偶尔达到略高 AUROC (0.50→0.51)。 LOW 资源语言 deep-layer selectivity 仅 ~0.08——部分 language-layer 组合低于 0.05 threshold， 尤其是 am/yo/te (这些语言在模型训练数据中极少，correctness signal 接近 noise floor)。 ~22% overall artifact rate (at threshold 0.05) 的 breakdown： 5% from HIGH (仅最浅层 L0-L4), 22% from MID (shallow+mid layers), 35% from LOW (broad range)。 Threshold sensitivity: 0.03 更宽松 (32% artifacts)，0.10 更严格 (仅 12%)—— paper 中报告 0.05 (Hewitt & Liang original) as primary，0.03/0.10 in sensitivity analysis。 Field-level contribution: 首次在 cross-lingual probing 中系统应用 selectivity analysis。\n"
795	  }
796	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0263ea16-1d24-4985-96f2-85fc8219b40c",
  "isSidechain": false,
  "promptId": "e8f1a248-e970-4548-96f9-5cd439647eab",
  "type": "user",
  "uuid": "bdde09f5-4f07-4be7-b2a3-d3a33e79b6c1",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Full Pareto Frontier — Qwen3-235B-A22B (94 layers, MoE, INT4)\",\n    \"description\": \"94-layer MoE 模型，24 probed layers (每4层取1), 20 languages × 5 transfer conditions。 MoE routing 在深层创建更强的语言特异化，产生比 7B pilot 更清晰但仍非普遍的 Pareto tradeoff。\\n\",\n    \"results\": {\n      \"en_best_auroc\": 0.81,\n      \"en_best_layer\": \"L80\",\n      \"en_best_layer_depth_pct\": 0.851,\n      \"en_auroc_range\": [\n        0.59,\n        0.81\n      ],\n      \"en_best_ece_raw\": 0.178,\n      \"layer_depth_delta_pp\": 22.0,\n      \"transfer_optimal_layer_mean\": \"L68\",\n      \"transfer_optimal_depth_pct\": 0.723,\n      \"en_transfer_layer_gap_auroc_pp\": 2.5,\n      \"zs_pass_count_of_20\": 15,\n      \"zs_pass_rate\": 0.75,\n      \"zs_mean_auroc_at_en_optimal_layer\": 0.668,\n      \"zs_mean_auroc_at_transfer_optimal_layer\": 0.688,\n      \"mean_zs_auroc_drop_vs_en_pp\": 12.2,\n      \"pareto_langs_with_negative_depth_transfer_rho\": 14,\n      \"pareto_langs_significant_negative_rho\": 9,\n      \"pareto_spearman_rho_median\": -0.38,\n      \"pareto_spearman_rho_range\": [\n        -0.65,\n        0.2\n      ],\n      \"pareto_depth_transfer_drop_final_layers_pp\": 2.3,\n      \"best_zs_auroc_by_tier\": {\n        \"HIGH_mean\": 0.728,\n        \"MID_mean\": 0.678,\n        \"LOW_mean\": 0.582\n      },\n      \"best_zs_auroc_per_lang\": {\n        \"zh\": 0.738,\n        \"es\": 0.745,\n        \"fr\": 0.74,\n        \"de\": 0.725,\n        \"pt\": 0.732,\n        \"ja\": 0.71,\n        \"ar\": 0.695,\n        \"ru\": 0.705,\n        \"ko\": 0.688,\n        \"hi\": 0.67,\n        \"vi\": 0.68,\n        \"tr\": 0.66,\n        \"sw\": 0.598,\n        \"bn\": 0.612,\n        \"te\": 0.572,\n        \"id\": 0.69,\n        \"pl\": 0.698,\n        \"nl\": 0.72,\n        \"uk\": 0.695,\n        \"yo\": 0.535\n      },\n      \"mean_shift_delta_auroc\": 0.0,\n      \"linear_proj_200_mean_auroc\": 0.698,\n      \"few_shot_25_mean_auroc\": 0.685,\n      \"few_shot_100_mean_auroc\": 0.718,\n      \"spearman_depth_vs_transfer_positive_langs\": 14\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: Per-Language ZS AUROC and Pareto Statistics (Qwen3-235B, EN-optimal L80)\",\n        \"data\": \"| Tier | Language | ZS AUROC | Best ZS Layer | Spearman ρ | p-value | Pattern          |\\n|------|----------|----------|---------------|------------|---------|------------------|\\n| HIGH | zh       | 0.738    | L68           | -0.48      | 0.018   | Clear tradeoff   |\\n| HIGH | es       | 0.745    | L72           | -0.44      | 0.031   | Clear tradeoff   |\\n| HIGH | fr       | 0.740    | L72           | -0.42      | 0.041   | Clear tradeoff   |\\n| HIGH | de       | 0.725    | L64           | -0.51      | 0.011   | Clear tradeoff   |\\n| HIGH | pt       | 0.732    | L68           | -0.39      | 0.059   | Trending         |\\n| HIGH | ja       | 0.710    | L64           | -0.55      | 0.005   | Clear tradeoff   |\\n| MID  | ar       | 0.695    | L72           | -0.22      | 0.301   | Weak/absent      |\\n| MID  | ru       | 0.705    | L68           | -0.46      | 0.024   | Clear tradeoff   |\\n| MID  | ko       | 0.688    | L68           | +0.08      | 0.711   | No tradeoff      |\\n| MID  | hi       | 0.670    | L60           | -0.40      | 0.052   | Trending         |\\n| MID  | vi       | 0.680    | L64           | -0.38      | 0.068   | Trending         |\\n| MID  | tr       | 0.660    | L56           | -0.35      | 0.093   | Trending         |\\n| MID  | id       | 0.690    | L68           | -0.43      | 0.036   | Clear tradeoff   |\\n| LOW  | sw       | 0.598    | L52           | -0.28      | 0.184   | Weak             |\\n| LOW  | bn       | 0.612    | L56           | -0.33      | 0.115   | Weak             |\\n| LOW  | te       | 0.572    | L48           | -0.19      | 0.374   | Weak             |\\n| LOW  | pl       | 0.698    | L68           | -0.45      | 0.027   | Clear tradeoff   |\\n| LOW  | nl       | 0.720    | L68           | -0.47      | 0.021   | Clear tradeoff   |\\n| LOW  | uk       | 0.695    | L64           | -0.41      | 0.046   | Clear tradeoff   |\\n| LOW  | yo       | 0.535    | L44           | +0.12      | 0.578   | No tradeoff      |\\n\"\n      },\n      {\n        \"name\": \"Table 2: Transfer Method Comparison (mean across 20 languages, EN-optimal layer)\",\n        \"data\": \"| Method              | Mean AUROC | Δ vs ZS (pp) | Paired perm p | Req. labels | Req. parallel |\\n|---------------------|------------|--------------|---------------|-------------|---------------|\\n| Zero-shot           | 0.668      | —            | —             | 0           | 0             |\\n| Mean-shift          | 0.668      | 0.0          | n/a           | 0           | N (mean only) |\\n| CaCLR (best β=0.01) | 0.671      | +0.3         | p=0.38        | 0           | ~10K parallel |\\n| Linear proj (50)    | 0.684      | +1.6         | p=0.012       | 0           | 50 pairs      |\\n| Linear proj (200)   | 0.698      | +3.0         | p<0.001       | 0           | 200 pairs     |\\n| Few-shot 25         | 0.685      | +1.7         | p=0.008       | 25          | 0             |\\n| Few-shot 100        | 0.718      | +5.0         | p<0.001       | 100         | 0             |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Qwen3-235B 的 MoE 架构产生了 pilot 预期的清晰 Pareto，但非所有语言均参与： 9/20 语言 Spearman ρ 显著为负 (p<0.05)，另 5 个 trending (p<0.10)，6 个不显著或方向相反。 Pareto 强度与 resource tier 正相关但非完美（pl/nl/uk 虽在 LOW tier 但因与 EN 词汇重叠高，表现接近 HIGH）。 MoE routing 加速了 L64+ 的语言特异化，但效果分布在 4-8 层的范围内，不是单点 cliff。 ar/ko 不 show tradeoff 的原因需在 CKA 分析 (plan_011) 中进一步解释—— 可能是这两种语言在 Qwen3 训练数据中占比足够高，expert sharing 保持了 EN-target alignment。\\n\\n\\nQwen3-235B 的 22B active MoE 参数从 7B pilot (EN AUROC 0.754) 提升到 ~0.81， 符合 correctness signal 随模型规模 sublinear scaling 的预期——22B/7B ≈ 3x 参数但 AUROC 提升仅 ~6pp，因为 correctness direction 的 linear accessibility 在 7B 时已接近 ceiling。 MoE routing 在深层（L64+）为不同语言激活不同 expert subset，加速 representation 语言特异化。 CKA 在 L64-L80 急剧下降（slope ~-0.022/layer），创造比 7B pilot 更清晰的 Pareto cliff。 但 \\\"更清晰\\\" 不等于 \\\"普遍\\\"：仍有 6/20 语言（主要 ar/ko + 部分低资源）不显示负 rho 或方向相反， 因为 (1) ar/ko 在 Qwen 训练数据中比例足够高，MoE routing 未完全将其与 EN 分离； (2) 极低资源语言（yo/am）全深度 AUROC 都低，depth variation 太小无法检测 tradeoff。 15/20 languages ZS AUROC > 0.58 — 新增 10 语言中 5 个通过（es/fr/de 等 HIGH 语言全通过）， 但 yo 可能低于阈值。Mean-shift 仍然恒等于 0（数学不变性不随模型规模变化）。 Transfer-optimal layer 在 L68（72% depth）而非 EN-optimal L80，gap ~2.5pp， 比 7B pilot 的 L24 vs L27 (~1.5pp) 更大但非剧烈——MoE 架构放大了 gap 但非无限放大。\\n\"\n  },\n  {\n    \"name\": \"Full Pareto Frontier — Llama 4 Scout (48 layers, MoE, W4A16)\",\n    \"description\": \"48-layer 17B-16E MoE，12 probed layers (每4层取1+final), 20 languages × 5 transfer conditions。 Llama 架构族在 pilot (3.1-8B) 中显示弱 Pareto，full-scale MoE 预期延续但 Pareto 稍增。\\n\",\n    \"results\": {\n      \"en_best_auroc\": 0.77,\n      \"en_best_layer\": \"L44\",\n      \"en_best_layer_depth_pct\": 0.917,\n      \"en_auroc_range\": [\n        0.61,\n        0.77\n      ],\n      \"en_best_ece_raw\": 0.192,\n      \"layer_depth_delta_pp\": 16.0,\n      \"transfer_optimal_layer_mean\": \"L36\",\n      \"transfer_optimal_depth_pct\": 0.75,\n      \"en_transfer_layer_gap_auroc_pp\": 1.5,\n      \"zs_pass_count_of_20\": 14,\n      \"zs_pass_rate\": 0.7,\n      \"zs_mean_auroc_at_en_optimal_layer\": 0.648,\n      \"zs_mean_auroc_at_transfer_optimal_layer\": 0.66,\n      \"mean_zs_auroc_drop_vs_en_pp\": 11.0,\n      \"pareto_langs_with_negative_depth_transfer_rho\": 11,\n      \"pareto_langs_significant_negative_rho\": 5,\n      \"pareto_spearman_rho_median\": -0.25,\n      \"pareto_spearman_rho_range\": [\n        -0.52,\n        0.38\n      ],\n      \"pareto_depth_transfer_drop_final_layers_pp\": 1.2,\n      \"best_zs_auroc_by_tier\": {\n        \"HIGH_mean\": 0.708,\n        \"MID_mean\": 0.658,\n        \"LOW_mean\": 0.562\n      },\n      \"best_zs_auroc_per_lang\": {\n        \"zh\": 0.718,\n        \"es\": 0.725,\n        \"fr\": 0.72,\n        \"de\": 0.705,\n        \"pt\": 0.712,\n        \"ja\": 0.69,\n        \"ar\": 0.672,\n        \"ru\": 0.685,\n        \"ko\": 0.68,\n        \"hi\": 0.645,\n        \"vi\": 0.658,\n        \"tr\": 0.635,\n        \"sw\": 0.578,\n        \"bn\": 0.59,\n        \"te\": 0.555,\n        \"id\": 0.672,\n        \"pl\": 0.678,\n        \"nl\": 0.7,\n        \"uk\": 0.67,\n        \"yo\": 0.52\n      },\n      \"mean_shift_delta_auroc\": 0.0,\n      \"linear_proj_200_mean_auroc\": 0.678,\n      \"few_shot_100_mean_auroc\": 0.7,\n      \"spearman_depth_vs_transfer_positive_langs\": 13\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3: Architecture Comparison — Pareto Strength\",\n        \"data\": \"| Metric                         | Qwen3-235B (MoE) | Llama4 Scout (MoE) |\\n|--------------------------------|-------------------|--------------------|\\n| EN best AUROC                  | 0.81              | 0.77               |\\n| Mean ZS AUROC (EN-opt layer)   | 0.668             | 0.648              |\\n| Pareto significant langs (/20) | 9                 | 5                  |\\n| Median per-lang Pareto ρ       | -0.38             | -0.25              |\\n| CKA cliff onset (% depth)      | ~68%              | ~50%               |\\n| CKA depth gradient (cliff)     | -0.022/layer      | -0.013/layer       |\\n| EN-opt vs Transfer-opt gap (pp)| 2.5               | 1.5                |\\n\"\n      },\n      {\n        \"name\": \"Table 4: Divergent Languages Between Architectures\",\n        \"data\": \"| Language | Qwen3 ρ | Qwen3 p | Llama4 ρ | Llama4 p | Pattern     |\\n|----------|---------|---------|----------|----------|-------------|\\n| ar       | -0.22   | 0.301   | +0.18    | 0.575    | Divergent   |\\n| ko       | +0.08   | 0.711   | +0.32    | 0.311    | Both pos    |\\n| vi       | -0.38   | 0.068   | +0.15    | 0.641    | Divergent   |\\n| ja       | -0.55   | 0.005   | -0.42    | 0.175    | Both neg    |\\n| hi       | -0.40   | 0.052   | -0.48    | 0.115    | Both neg    |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"两个 MoE 架构的 Pareto 差异证实架构依赖性——但差异根源是 CKA gradient shape， 不是 MoE vs dense (需 Gemma 4 dense 对照验证)。Llama4 的渐进 CKA decline 意味着 cross-lingual alignment 是渐变退化而非突变，实践意义是：layer selection 对 Llama4 不那么关键， 任何 50-90% depth 的层都是 reasonable choice，而 Qwen3 有明确的 optimal window (60-75% depth)。 ar/ko/vi 在 Llama4 上的正向深度效应扩大了 pilot 发现——这些语言在 Llama 训练数据中 representation 可能与 EN 共享更多 expert（tokenizer 和 training distribution 的差异是 observational confound，n=2 architectures 不做因果归因）。\\n\\n\\nLlama 4 Scout (17B active) 从 pilot Llama-3.1-8B (EN 0.728) 提升到 ~0.77， 提升幅度低于 Qwen3 的 scaling，因为 Llama 4 的 16-expert MoE 在中层已开始 expert specialization， correctness signal 在 L20-L36 plateau 而非持续爬升到最深层。 Pilot 中 Llama 的弱 Pareto 模式延续：仅 5/20 语言显著负 rho (p<0.05)， 另 6 个 trending，9 个不显著或方向相反。ar/ko 延续 pilot 中的正向深度效应 （ZS AUROC 随深度单调增加，无 tradeoff），扩展到 vi 也呈此模式。 关键架构差异在 CKA depth gradient：Llama CKA decline 从 ~50% depth 开始渐进下降 (slope ~-0.013/layer)，而非 Qwen3 的 ~68% depth 后骤降 (slope ~-0.022/layer)。 渐进 CKA decline → tradeoff 分散在更宽的层范围 → per-language Spearman ρ magnitude 更小。 EN-optimal (L44) vs transfer-optimal (L36) gap 仅 ~1.5pp vs Qwen3 的 ~2.5pp。 12 probed layers 的较少层采样（vs Qwen3 的 24 层）也降低了 Spearman 检验功效 (n=12 vs n=24)。\\n\"\n  },\n  {\n    \"name\": \"CaCLR Implementation and Systematic Negative Result\",\n    \"description\": \"CaCLR (BCE + α·SB-ECE + β·MMD) 完整实现。β sweep 3 OOM (0.001-1.0)， component ablation, CORAL comparison, high-dim MMD (PCA d=50/100), multi-seed, mixed β criterion。 Median tier: consistency loss inert → negative result + geometric explanation。\\n\",\n    \"results\": {\n      \"caclr_mean_delta_auroc_vs_zs_pp\": 0.3,\n      \"caclr_delta_auroc_range_pp\": [\n        -0.8,\n        1.2\n      ],\n      \"caclr_langs_improved_of_20\": 8,\n      \"caclr_langs_degraded_of_20\": 5,\n      \"caclr_langs_unchanged_of_20\": 7,\n      \"caclr_best_beta\": 0.01,\n      \"caclr_best_alpha\": 0.3,\n      \"beta_sweep\": {\n        \"beta_0.001\": {\n          \"mean_delta_auroc_pp\": 0.1,\n          \"paired_perm_p\": 0.72,\n          \"cohen_d\": 0.02\n        },\n        \"beta_0.01\": {\n          \"mean_delta_auroc_pp\": 0.3,\n          \"paired_perm_p\": 0.38,\n          \"cohen_d\": 0.06\n        },\n        \"beta_0.1\": {\n          \"mean_delta_auroc_pp\": -0.1,\n          \"paired_perm_p\": 0.65,\n          \"cohen_d\": 0.03\n        },\n        \"beta_1.0\": {\n          \"mean_delta_auroc_pp\": -0.7,\n          \"paired_perm_p\": 0.15,\n          \"cohen_d\": 0.15\n        }\n      },\n      \"alpha_sweep\": {\n        \"alpha_0.01\": {\n          \"mean_delta_ece_pp\": -0.2,\n          \"mean_delta_auroc_pp\": 0.0\n        },\n        \"alpha_0.1\": {\n          \"mean_delta_ece_pp\": -0.6,\n          \"mean_delta_auroc_pp\": -0.1\n        },\n        \"alpha_1.0\": {\n          \"mean_delta_ece_pp\": -1.8,\n          \"mean_delta_auroc_pp\": -0.5\n        },\n        \"alpha_10.0\": {\n          \"mean_delta_ece_pp\": -2.3,\n          \"mean_delta_auroc_pp\": -1.4\n        }\n      },\n      \"component_ablation\": {\n        \"bce_only\": {\n          \"auroc\": 0.668,\n          \"ece\": 0.19\n        },\n        \"bce_sbece\": {\n          \"auroc\": 0.665,\n          \"ece\": 0.175\n        },\n        \"bce_mmd\": {\n          \"auroc\": 0.67,\n          \"ece\": 0.188\n        },\n        \"bce_sbece_mmd\": {\n          \"auroc\": 0.669,\n          \"ece\": 0.174\n        }\n      },\n      \"coral_comparison\": {\n        \"coral_mean_delta_auroc_pp\": 0.4,\n        \"coral_p_vs_zs\": 0.32,\n        \"coral_conclusion\": \"also inert — distributional matching failure is general, not MMD-specific\"\n      },\n      \"high_dim_mmd\": {\n        \"pca_d50_mean_delta_auroc_pp\": 0.5,\n        \"pca_d50_p_vs_zs\": 0.28,\n        \"pca_d100_mean_delta_auroc_pp\": 0.2,\n        \"pca_d100_p_vs_zs\": 0.51,\n        \"conclusion\": \"high-dim MMD also inert — broadens distributional matching failure claim\"\n      },\n      \"multi_seed_std\": {\n        \"caclr_auroc_std\": 0.003,\n        \"few_shot_25_auroc_std\": 0.005,\n        \"few_shot_100_auroc_std\": 0.004,\n        \"procrustes_auroc_std\": 0.002\n      },\n      \"mixed_beta_criterion\": {\n        \"en_only_best_beta\": 0.01,\n        \"en_zh_sw_best_beta\": 0.01,\n        \"conclusion\": \"mixed criterion selects same β — no systematic bias\"\n      },\n      \"method_comparison_mean_20lang\": {\n        \"zero_shot\": 0.668,\n        \"mean_shift\": 0.668,\n        \"caclr_best\": 0.671,\n        \"coral_best\": 0.672,\n        \"high_dim_mmd_best\": 0.673,\n        \"linear_proj_50\": 0.684,\n        \"linear_proj_200\": 0.698,\n        \"few_shot_25\": 0.685,\n        \"few_shot_100\": 0.718\n      },\n      \"implementation_spec\": {\n        \"mmd_kernel\": \"Gaussian RBF, bandwidth via median heuristic (recomputed per batch)\",\n        \"optimizer\": \"Adam, lr=5e-4, cosine decay to 1e-5\",\n        \"epochs\": 50,\n        \"early_stopping\": \"patience=10 on validation BCE loss\",\n        \"initialization\": \"from standard LR solution (warm-start)\",\n        \"batch_size\": 256,\n        \"mmd_items\": \"same as BCE (probe_train split, 70% of GlobalMMLU test)\",\n        \"parallel_set_size_range\": [\n          8500,\n          12200\n        ],\n        \"seeds\": [\n          42,\n          137,\n          256\n        ]\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 5: β Sweep Results (Qwen3-235B, L68, mean 20 languages, 3 seeds)\",\n        \"data\": \"| β     | Mean AUROC | Δ vs ZS (pp) | 95% Boot CI (pp)  | Cohen's d | Interpretation      |\\n|-------|------------|--------------|-------------------|-----------|---------------------|\\n| 0     | 0.668      | —            | —                 | —         | ZS baseline         |\\n| 0.001 | 0.669      | +0.1         | [-0.5, +0.7]      | 0.02      | Negligible          |\\n| 0.01  | 0.671      | +0.3         | [-0.4, +1.0]      | 0.06      | Negligible          |\\n| 0.1   | 0.667      | -0.1         | [-0.8, +0.6]      | 0.03      | Negligible          |\\n| 1.0   | 0.661      | -0.7         | [-1.4, +0.0]      | 0.15      | Slight degradation  |\\n\"\n      },\n      {\n        \"name\": \"Table 6: Distributional Matching Ablation (all methods, mean 20 langs)\",\n        \"data\": \"| Method               | Operates on | Mean AUROC | Δ vs ZS | p-value | Conclusion |\\n|----------------------|-------------|------------|---------|---------|------------|\\n| MMD (1-D logit)      | probe logit | 0.671      | +0.3pp  | 0.38    | Inert      |\\n| MMD (PCA d=50)       | activations | 0.673      | +0.5pp  | 0.28    | Inert      |\\n| MMD (PCA d=100)      | activations | 0.670      | +0.2pp  | 0.51    | Inert      |\\n| CORAL (1-D logit)    | probe logit | 0.672      | +0.4pp  | 0.32    | Inert      |\\n| CORAL (PCA d=50)     | activations | 0.671      | +0.3pp  | 0.40    | Inert      |\\n| Linear projection    | activations | 0.698      | +3.0pp  | <0.001  | Effective  |\\n| Few-shot 100         | labels      | 0.718      | +5.0pp  | <0.001  | Effective  |\\n\"\n      },\n      {\n        \"name\": \"Table 7: CKA Subspace Angle — Why Distributional Matching Fails\",\n        \"data\": \"| Language Tier | Mean subspace angle (EN→target) | MMD dist before | MMD dist after CaCLR | Angle after CaCLR | Interpretation                |\\n|--------------|----------------------------------|-----------------|----------------------|--------------------|-------------------------------|\\n| HIGH         | 11°                              | 0.018           | 0.008                | 10.5°              | MMD reduces, angle unchanged  |\\n| MID          | 23°                              | 0.042           | 0.018                | 22°                | MMD reduces, angle unchanged  |\\n| LOW          | 44°                              | 0.105           | 0.048                | 42°                | MMD reduces, angle unchanged  |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CaCLR negative result 贡献在三个层面：(1) Systematic β sweep (3 OOM × 2 architectures × 20 langs) 关闭了 MMD-based consistency loss 路径；(2) CORAL + high-dim MMD ablation 扩展结论到 \\\"distributional matching in general fails for correctness probe transfer\\\"——不是 MMD 的问题， 是 marginal-conditional mismatch 的本质问题；(3) CKA subspace angle analysis 提供几何解释： CaCLR 成功减小了 marginal distance 但 correctness subspace angle 几乎不变。 Constructive framing: CaCLR 是 \\\"the natural baseline that tests the distributional matching hypothesis\\\"——其失败不是方法论错误，而是对 Zhao et al. (2019) 理论的实证验证， 同时指向 linear projection (~80 pairs) 作为 practical recommendation。\\n\\n\\nCaCLR 的 MMD consistency loss 在 1-D probe logit 空间操作，这是根本的 architectural mismatch。 Correctness information 占据高维 activation 空间的 1-3 维子空间；MMD 只能匹配 logit 的 marginal distribution (均值/方差)，无法检测或纠正 correctness direction 的旋转。 β=0.001-0.01 时 consistency loss 太弱，等效于 pure BCE；β=0.1-1.0 时 loss 开始干扰 BCE 训练——强制匹配 marginal 反而扰动了 EN probe 已学到的 correctness direction，AUROC 下降。 8/20 语言 show 微小正 delta (0.1-1.2pp) 但无一统计显著——这是 noise 而非 signal。 CORAL (second-order alignment) 和 high-dim MMD (PCA d=50/100) 也无效—— distributional matching 的失败不限于 MMD kernel 或操作维度，而是因为 Zhao et al. (2019) 的理论预测成立：P(correct|activation) 的 conditional structure 在不同语言间不同（language-specific capability component），marginal matching 无法修复 conditional mismatch。CKA subspace analysis 将提供几何证据：CaCLR 成功减小了 marginal distance 但 subspace angle 几乎不变（见 plan_011 交叉分析）。 与此对照，linear projection 直接学习旋转矩阵，绕过 distributional matching 的局限。 Multi-seed 结果稳定 (std ~0.002-0.005)，排除 single-seed artifact 的可能。\\n\"\n  },\n  {\n    \"name\": \"Difficulty-Controlled Decomposition Ablation\",\n    \"description\": \"IRT difficulty probes → project out difficulty direction → retrain correctness probes → evaluate transfer。 10 languages × 8 layers × 3 models。含 random-direction control。 Median tier: 定性分离成立但 prescriptive 能力弱，弱化为 descriptive。\\n\",\n    \"results\": {\n      \"mean_delta_auroc_difficulty_projected_pp\": 1.8,\n      \"delta_auroc_range_pp\": [\n        -1.2,\n        3.5\n      ],\n      \"langs_with_positive_delta_of_10\": 6,\n      \"langs_with_negative_delta_of_10\": 2,\n      \"langs_with_negligible_delta_of_10\": 2,\n      \"random_direction_mean_delta_pp\": 0.7,\n      \"difficulty_vs_random_effect_ratio\": 2.6,\n      \"difficulty_probe_r2\": 0.32,\n      \"per_lang_results\": {\n        \"zh\": {\n          \"delta_pp\": 0.8,\n          \"sig\": false\n        },\n        \"es\": {\n          \"delta_pp\": 1.2,\n          \"sig\": false\n        },\n        \"fr\": {\n          \"delta_pp\": 1.5,\n          \"sig\": true\n        },\n        \"de\": {\n          \"delta_pp\": 1.8,\n          \"sig\": true\n        },\n        \"hi\": {\n          \"delta_pp\": 2.8,\n          \"sig\": true\n        },\n        \"ru\": {\n          \"delta_pp\": 2.2,\n          \"sig\": true\n        },\n        \"ko\": {\n          \"delta_pp\": -0.6,\n          \"sig\": false\n        },\n        \"tr\": {\n          \"delta_pp\": 2.5,\n          \"sig\": true\n        },\n        \"sw\": {\n          \"delta_pp\": -1.2,\n          \"sig\": false\n        },\n        \"bn\": {\n          \"delta_pp\": 3.5,\n          \"sig\": true\n        }\n      },\n      \"decomposition_clean_separation_count_of_10\": 5,\n      \"prescriptive_accuracy\": 0.56\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 8: Decomposition Results by Language (Qwen3-235B, 8-layer mean)\",\n        \"data\": \"| Language | Tier | Full AUROC | Diff-proj AUROC | Δ (pp) | Random-proj AUROC | Rand Δ (pp) | Diff-specific (pp) |\\n|----------|------|------------|-----------------|--------|-------------------|-------------|--------------------|\\n| zh       | HIGH | 0.738      | 0.746           | +0.8   | 0.742             | +0.4        | +0.4               |\\n| es       | HIGH | 0.745      | 0.757           | +1.2   | 0.751             | +0.6        | +0.6               |\\n| fr       | HIGH | 0.740      | 0.755           | +1.5   | 0.747             | +0.7        | +0.8               |\\n| de       | HIGH | 0.725      | 0.743           | +1.8   | 0.733             | +0.8        | +1.0               |\\n| hi       | MID  | 0.670      | 0.698           | +2.8   | 0.678             | +0.8        | +2.0               |\\n| ru       | MID  | 0.705      | 0.727           | +2.2   | 0.713             | +0.8        | +1.4               |\\n| ko       | MID  | 0.688      | 0.682           | -0.6   | 0.691             | +0.3        | -0.9               |\\n| tr       | MID  | 0.660      | 0.685           | +2.5   | 0.668             | +0.8        | +1.7               |\\n| sw       | LOW  | 0.598      | 0.586           | -1.2   | 0.601             | +0.3        | -1.5               |\\n| bn       | LOW  | 0.612      | 0.647           | +3.5   | 0.620             | +0.8        | +2.7               |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Decomposition 支持 \\\"correctness transfer contains difficulty-shared and capability-specific components\\\" 的定性结论。6/10 语言 show improvement，其中 5 具有统计显著性，且 difficulty-specific effect consistently exceeds random-direction control。但 prescriptive accuracy (56%) 与 chance (50%) 差距极小——decomposition 不是 reliable strategy selector。 Paper 中弱化 Claim 2 为 subsection-level descriptive finding，压缩到 ~1 page： \\\"We observe that projecting out the shared difficulty component generally improves transfer for mid-resource languages (+2-3pp) but can harm low-resource languages where difficulty and capability are more entangled. This separation is descriptive rather than prescriptive — it explains what transfer contains but does not predict optimal strategy.\\\"\\n\\n\\nDifficulty 成分确实跨语言共享（IRT difficulty 与语言无关），projection 后 residual 更 capability-specific。 平均 +1.8pp 改善高于 random-direction control 的 +0.7pp，比值 2.6 表明约 60% 的效果是 difficulty-specific，40% 来自纯维度缩减降噪。但效果 modest (<3pp for most languages)， 原因：(1) difficulty probe R²=0.32 意味着 projection 不完全——只移除了 32% 的 difficulty 方差； (2) difficulty 和 capability 在 activation 空间中不正交——projection 在 ko/sw 中损害了 AUROC， 因为这些语言的 difficulty-capability 纠缠更深（ko 的 MMLU difficulty ordering 与 EN 差异大， sw 的 correctness signal 本身就弱，projection 后更弱）； (3) HIGH 资源语言（zh/es）改善小是因为 capability 成分已经 well-aligned（不需要 decomposition）， MID/LOW 资源语言改善更大是因为 removing difficulty confound 确实帮助—— 但仅在 correctness signal 足够强的 MID 语言上 (hi/ru/tr/bn)。 Prescriptive accuracy 56% (vs chance 50%) 表明 decomposition 无法可靠预测最优对齐策略。 弱化 Claim 2 为 \\\"descriptive separation observed; difficulty-capability entanglement varies across languages but decomposition does not reliably predict optimal transfer strategy\\\"。\\n\"\n  },\n  {\n    \"name\": \"Cross-Lingual Orthogonality Analysis\",\n    \"description\": \"提取 verbalized confidence direction，计算与 correctness direction 的 cosine similarity， 20 languages × 2+ architectures。Supporting evidence for Claim 4 (subsection)。\\n\",\n    \"results\": {\n      \"mean_cosine_all_langs\": 0.04,\n      \"cosine_range\": [\n        0.01,\n        0.148\n      ],\n      \"langs_below_0.05\": 13,\n      \"langs_below_0.10\": 17,\n      \"langs_above_0.10\": 3,\n      \"per_tier_mean_cosine\": {\n        \"HIGH\": 0.026,\n        \"MID\": 0.044,\n        \"LOW\": 0.075\n      },\n      \"architecture_comparison\": {\n        \"qwen3_mean\": 0.037,\n        \"llama4_mean\": 0.043,\n        \"difference_sig\": false\n      },\n      \"outlier_langs\": [\n        \"am\",\n        \"yo\",\n        \"te\"\n      ],\n      \"outlier_cosine\": [\n        0.148,\n        0.122,\n        0.105\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 9: Correctness-Confidence Cosine Similarity by Resource Tier\",\n        \"data\": \"| Tier | n  | Mean cos | Std   | Min   | Max   | n < 0.05 | n < 0.10 |\\n|------|----|----------|-------|-------|-------|----------|----------|\\n| HIGH | 6  | 0.026    | 0.010 | 0.010 | 0.042 | 5        | 6        |\\n| MID  | 8  | 0.044    | 0.016 | 0.022 | 0.072 | 4        | 8        |\\n| LOW  | 6  | 0.075    | 0.038 | 0.030 | 0.148 | 2        | 3        |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Orthogonality 作为 subsection supporting evidence 充分：17/20 languages cosine < 0.10, 13/20 < 0.05。结论 compact：correctness-confidence orthogonality is cross-lingually robust, reinforcing the necessity of probe-based calibration methods over output-based approaches. am/yo/te 高 cosine 与 plan_013 selectivity analysis 交叉验证——若 selectivity < 0.05, 则标注为 unreliable measurement。\\n\\n\\nMiao & Ungar (2026) 在 English 7-8B 上发现 cosine < 0.04。跨语言扩展时： HIGH 资源语言复现此结果（模型对这些语言的 correctness 和 confidence direction 都稳定， 分化清晰）。MID 语言 cosine 略高（0.03-0.06），因为 verbalized confidence 在中资源语言上 更不稳定（模型在这些语言上的 confidence verbalization 训练数据更少）。 LOW 资源语言中 am/yo/te 出现较高 cosine (>0.10)——这不是真正的 correctness-confidence alignment，而是两个 direction 都很弱时 cosine 被噪声主导的 artifact。 plan_013 full-scale control task 将确认这些语言的 deep-layer selectivity < 0.05。 两个架构间差异不显著 (0.037 vs 0.043, p=0.42)——orthogonality 是 representation 的 structural property，不随架构变化。\\n\"\n  },\n  {\n    \"name\": \"Probe Complexity Comparison (LR vs 2-Layer MLP)\",\n    \"description\": \"每层每模型对比 logistic regression 和 2-layer MLP 的 EN accuracy、 cross-lingual transfer degradation 和 calibration quality。CPU-bound。\\n\",\n    \"results\": {\n      \"qwen3\": {\n        \"lr_en_best_auroc\": 0.81,\n        \"mlp_en_best_auroc\": 0.832,\n        \"lr_mean_zs_auroc\": 0.668,\n        \"mlp_mean_zs_auroc\": 0.638,\n        \"lr_transfer_gap_pp\": 14.2,\n        \"mlp_transfer_gap_pp\": 19.4\n      },\n      \"llama4\": {\n        \"lr_en_best_auroc\": 0.77,\n        \"mlp_en_best_auroc\": 0.792,\n        \"lr_mean_zs_auroc\": 0.648,\n        \"mlp_mean_zs_auroc\": 0.622,\n        \"lr_transfer_gap_pp\": 12.2,\n        \"mlp_transfer_gap_pp\": 17.0\n      },\n      \"mlp_en_advantage_mean_pp\": 2.1,\n      \"lr_transfer_advantage_mean_pp\": 3.0,\n      \"lr_preferred_for_transfer\": true,\n      \"mlp_preferred_for_en_only\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 10: LR vs MLP Transfer Comparison\",\n        \"data\": \"| Metric                    | Qwen3 LR | Qwen3 MLP | Llama4 LR | Llama4 MLP |\\n|---------------------------|----------|-----------|-----------|------------|\\n| EN best AUROC             | 0.810    | 0.832     | 0.770     | 0.792      |\\n| Mean ZS AUROC             | 0.668    | 0.638     | 0.648     | 0.622      |\\n| Transfer gap (pp)         | 14.2     | 19.4      | 12.2      | 17.0       |\\n| EN ECE (best layer)       | 0.178    | 0.165     | 0.192     | 0.178      |\\n| Mean ZS ECE               | 0.218    | 0.248     | 0.228     | 0.258      |\\n| ZS pass rate (>0.58)      | 75%      | 55%       | 70%       | 50%        |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"LR vs MLP 验证了 linear probe 是 cross-lingual transfer 的正确方法论选择。 Paper 中报告为 methodology validation (1-2 paragraphs)，不展开为独立贡献。\\n\\n\\nMLP (2-layer, 256 hidden units) 多出的参数让它学到 EN-specific activation patterns （如英语特有的 token position bias、named entity patterns 等），EN AUROC +2.1pp。 但这些 EN-specific patterns 不跨语言迁移——MLP 过拟合了 EN distributional structure。 LR 被迫学习单一 hyperplane（1 个 correctness direction），更可能对应 language-agnostic subspace。 Transfer gap: LR ~13pp vs MLP ~18pp——MLP 多出的 ~5pp gap 分解为 EN advantage (~2pp) + EN-specific overfitting (~3pp)。 ECE 模式相同：MLP 在 EN 上 ECE 更好（更多参数→更好的概率估计）， 但在 ZS transfer 时 ECE 更差（overfitted probabilities 在新 distribution 上更 miscalibrated）。\\n\"\n  },\n  {\n    \"name\": \"Additional Benchmark Evaluation (Belebele + MMLU-ProX)\",\n    \"description\": \"在 Belebele (RC) 和 MMLU-ProX (翻译 MMLU) 上评估 best probes + all transfer methods。 验证 generalization beyond GlobalMMLU。20 languages × 2 models。\\n\",\n    \"results\": {\n      \"belebele\": {\n        \"en_best_auroc\": 0.75,\n        \"mean_zs_auroc\": 0.632,\n        \"zs_pass_rate\": 0.6,\n        \"pareto_preserved\": true,\n        \"pareto_strength\": \"weaker than GlobalMMLU (fewer sig langs)\",\n        \"pareto_sig_langs_of_20\": 6,\n        \"rank_corr_with_globalmmlu\": 0.84,\n        \"linear_proj_delta_pp\": 2.5,\n        \"caclr_delta_pp\": 0.2\n      },\n      \"mmlu_prox\": {\n        \"en_best_auroc\": 0.79,\n        \"mean_zs_auroc\": 0.658,\n        \"zs_pass_rate\": 0.72,\n        \"pareto_preserved\": true,\n        \"pareto_strength\": \"comparable to GlobalMMLU\",\n        \"pareto_sig_langs_of_20\": 8,\n        \"rank_corr_with_globalmmlu\": 0.92,\n        \"linear_proj_delta_pp\": 2.8,\n        \"caclr_delta_pp\": 0.3\n      },\n      \"cross_benchmark_lang_ranking_rho\": 0.89,\n      \"linear_proj_generalizes\": true,\n      \"caclr_still_inert\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 11: Cross-Benchmark Consistency (Qwen3-235B)\",\n        \"data\": \"| Metric             | GlobalMMLU | Belebele | MMLU-ProX |\\n|--------------------|------------|----------|-----------|\\n| EN best AUROC      | 0.81       | 0.75     | 0.79      |\\n| Mean ZS AUROC      | 0.668      | 0.632    | 0.658     |\\n| ZS pass rate       | 75%        | 60%      | 72%       |\\n| Pareto sig langs   | 9          | 6        | 8         |\\n| Linear proj Δ (pp) | +3.0       | +2.5     | +2.8      |\\n| CaCLR Δ (pp)       | +0.3       | +0.2     | +0.3      |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cross-benchmark 验证确认主要发现的 robustness。Belebele 上 Pareto 更弱是预期的。 Key message: \\\"all qualitative findings (architecture dependence, resource-tier gradient, CaCLR failure, linear projection effectiveness) generalize across benchmarks.\\\"\\n\\n\\nBelebele 是阅读理解（passage-dependent correctness），与 GlobalMMLU 的 parametric knowledge 不同——correctness signal 的性质部分不同。EN AUROC 略低 (0.75 vs 0.81)，因为 RC correctness 更依赖 passage comprehension 而非 parametric knowledge，probe 的 linear accessibility 稍低。Transfer 更差因为 RC 的 cross-lingual alignment 更依赖 word-level translation quality。 但 Pareto 结构保留——depth-transferability tradeoff 是 representation geometry 的性质。 MMLU-ProX 与 GlobalMMLU 高度相关（同源翻译数据），模式几乎一致 (rho=0.92)。 Cross-benchmark language ranking rho=0.89——结果不是 benchmark-specific。 CaCLR 在两个 benchmark 上仍 inert，linear projection 仍有效——泛化确认。\\n\"\n  },\n  {\n    \"name\": \"Gemma 4 32.7B Dense — Third Architecture\",\n    \"description\": \"Dense 架构对照 (vs 两个 MoE)，60 text decoder layers, BF16, 20 languages。 提供 dense vs MoE architectural contrast。P0 for core submission。\\n\",\n    \"results\": {\n      \"en_best_auroc\": 0.79,\n      \"en_best_layer\": \"L52\",\n      \"en_best_layer_depth_pct\": 0.867,\n      \"en_auroc_range\": [\n        0.6,\n        0.79\n      ],\n      \"en_best_ece_raw\": 0.182,\n      \"layer_depth_delta_pp\": 19.0,\n      \"transfer_optimal_layer_mean\": \"L44\",\n      \"transfer_optimal_depth_pct\": 0.733,\n      \"en_transfer_layer_gap_auroc_pp\": 1.8,\n      \"zs_pass_count_of_20\": 14,\n      \"zs_pass_rate\": 0.7,\n      \"zs_mean_auroc_at_en_optimal_layer\": 0.66,\n      \"mean_zs_auroc_drop_vs_en_pp\": 11.0,\n      \"pareto_langs_significant_negative_rho\": 7,\n      \"pareto_spearman_rho_median\": -0.32,\n      \"pareto_depth_transfer_drop_final_layers_pp\": 1.6,\n      \"cka_cliff_slope\": -0.014,\n      \"cka_cliff_onset_depth_pct\": 0.58,\n      \"partial_rho_cka\": 0.24,\n      \"partial_p\": 0.038,\n      \"simpson_significant\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 12: Three-Architecture Comparison\",\n        \"data\": \"| Metric                      | Qwen3-235B (MoE) | Llama4 Scout (MoE) | Gemma4 31B (Dense) |\\n|-----------------------------|-------------------|--------------------|---------------------|\\n| Type                        | MoE (22B active)  | MoE (17B active)   | Dense (31B)         |\\n| Total / Active params       | 235B / 22B        | 109B / 17B         | 31B / 31B           |\\n| Layers                      | 94                | 48                 | 60                  |\\n| EN best AUROC               | 0.81              | 0.77               | 0.79                |\\n| Mean ZS AUROC               | 0.668             | 0.648              | 0.660               |\\n| Pareto sig langs (/20)      | 9                 | 5                  | 7                   |\\n| Median Pareto ρ             | -0.38             | -0.25              | -0.32               |\\n| CKA cliff slope             | -0.022            | -0.013             | -0.014              |\\n| Partial ρ (CKA~AUROC|depth) | 0.16 (p=.072)     | 0.29 (p=.018)      | 0.24 (p=.038)       |\\n| Simpson's sig?              | Trending          | Yes                | Yes                 |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Gemma 4 作为 dense 对照确认 Pareto 不是 MoE artifact。三架构的 CKA cliff slope 与 Pareto 强度呈清晰的 monotonic relationship (steeper → more languages with tradeoff)， 但 n=3 仅为 suggestive。Simpson's Paradox 变为 2/3 显著——strengthens geometric narrative。 Paper 中强调 architecture dependence 是 descriptive finding (各架构 scale/depth/training data all differ, 无法 isolate 单一因素)。\\n\\n\\nDense 架构的 CKA decline 比 MoE 更线性渐进——无 expert routing 加速特异化机制， 所有参数共享导致语言 representation 的分化更缓慢。 CKA slope ~-0.014/layer，介于 Qwen3 (-0.022) 和 Llama4 (-0.013) 之间。 EN AUROC ~0.79 (31B full params) 接近 Qwen3 的 0.81 (22B active MoE)， 因为 correctness direction 的 linear accessibility 在 ~20B+ 后已接近 saturation。 Pareto 强度 intermediate: 7/20 语言显著负 rho (between Qwen3's 9 and Llama4's 5)。 Simpson's Paradox 在 Gemma 4 上显著 (partial rho=0.24, p=0.038)—— 其 linear-ish CKA decline 使得 linear partial correlation 比 Qwen3 的 step-function decline 更有效（Qwen3 partial rho=0.16, p=0.072 不显著，部分因为非线性 depth-CKA 关系）。 三架构 Simpson's confirmation: Llama4 (显著), Gemma4 (显著), Qwen3 (trending) → 2/3。 Dense vs MoE 对比核心发现：Pareto 不是 MoE-specific，dense 架构也有但更弱。 这排除了 \\\"Pareto tradeoff 是 MoE expert routing 的 artifact\\\" 的替代假说。\\n\"\n  },\n  {\n    \"name\": \"Extended Language Coverage (50+ Languages)\",\n    \"description\": \"从 20 扩展至 50+ 语言，利用 GlobalMMLU/Belebele 全语言集。Camera-ready extension。\\n\",\n    \"results\": {\n      \"total_languages\": 52,\n      \"zs_pass_rate_52\": 0.6,\n      \"zs_pass_count_52\": 31,\n      \"artifact_rate_very_low_resource\": 0.45,\n      \"new_low_resource_langs_with_artifacts\": 16,\n      \"resource_tier_gradient_confirmed\": true,\n      \"rank_correlation_20_vs_52\": 0.95,\n      \"min_zs_auroc\": 0.5,\n      \"min_zs_lang\": \"Haitian Creole (ht)\",\n      \"new_findings\": \"Diminishing returns; very-low-resource languages (< 1M training tokens) uniformly near chance. Writing system clusters emerge (Cyrillic, Devanagari, Arabic script) as moderate predictor of transfer quality within resource tier.\\n\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S1: Language Coverage Expansion Summary\",\n        \"data\": \"| Tier      | 20-lang n | 52-lang n | Mean ZS AUROC | Artifact rate | Pass rate |\\n|-----------|-----------|-----------|---------------|---------------|-----------|\\n| HIGH      | 6         | 10        | 0.72          | 5%            | 100%      |\\n| MID       | 8         | 15        | 0.66          | 20%           | 87%       |\\n| LOW       | 6         | 16        | 0.58          | 32%           | 56%       |\\n| VERY-LOW  | 0         | 11        | 0.53          | 45%           | 27%       |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Camera-ready extension。Core story 不变。VERY-LOW resource languages 的高 artifact rate reinforces probing control 的必要性。Paper 中 core analysis 仍基于 20 languages (cleaner statistics)， 52-language results in extended table + map visualization。\\n\\n\\n新增 32 语言大多为 LOW/VERY-LOW resource。Pass rate 从 20 语言的 ~72% 降至 52 语言的 ~60%， 因为新增语言偏向低资源。Very-low-resource 语言 (ht, rm, fy, gd 等) 的 artifact rate ~45%， 几乎一半的 layer-language 结果不可靠。但 20 语言的核心发现在 52 语言上完全保持 (rank corr 0.95)。 主要增量贡献：(1) 统计 power 增加 (n=52 vs n=20 for cross-language analyses)， (2) writing system 作为 transfer predictor 的新发现（同脚本语言 pair 的 CKA 更高）， (3) 覆盖面更全面的 field-level claim。边际收益递减——每新增一种语言，对核心 claim 的增量证据极小。\\n\"\n  },\n  {\n    \"name\": \"Quantization Validation Ablation\",\n    \"description\": \"(a) W4A16 vs FP16 at 5 layers for Llama 4 Scout on 5% subset; (b) GPTQ-Int4 vs FP16 at 5 layers for Qwen3-235B on 5% subset.\\n\",\n    \"results\": {\n      \"llama4_w4a16_vs_fp16\": {\n        \"mean_abs_delta_auroc\": 0.004,\n        \"max_abs_delta_auroc\": 0.008,\n        \"per_layer_deltas\": {\n          \"L8\": -0.002,\n          \"L16\": 0.004,\n          \"L24\": -0.005,\n          \"L36\": 0.003,\n          \"L44\": -0.008\n        },\n        \"cka_fp16_vs_quant_mean\": 0.988\n      },\n      \"qwen3_int4_vs_fp16\": {\n        \"mean_abs_delta_auroc\": 0.006,\n        \"max_abs_delta_auroc\": 0.012,\n        \"per_layer_deltas\": {\n          \"L16\": -0.005,\n          \"L36\": 0.004,\n          \"L52\": -0.003,\n          \"L68\": 0.006,\n          \"L80\": -0.012\n        },\n        \"cka_fp16_vs_quant_mean\": 0.98\n      },\n      \"quantization_safe\": true,\n      \"conclusion\": \"All |ΔAUROC| < 0.015, all CKA > 0.97 — quantization artifacts negligible\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S2: Quantization Validation Per-Layer\",\n        \"data\": \"| Model  | Layer (depth%) | FP16 AUROC | Quant AUROC | ΔAUROC  | CKA     |\\n|--------|----------------|------------|-------------|---------|---------|\\n| Llama4 | L8 (17%)       | 0.635      | 0.633       | -0.002  | 0.992   |\\n| Llama4 | L16 (33%)      | 0.688      | 0.692       | +0.004  | 0.990   |\\n| Llama4 | L24 (50%)      | 0.722      | 0.717       | -0.005  | 0.988   |\\n| Llama4 | L36 (75%)      | 0.750      | 0.753       | +0.003  | 0.986   |\\n| Llama4 | L44 (92%)      | 0.770      | 0.762       | -0.008  | 0.984   |\\n| Qwen3  | L16 (17%)      | 0.632      | 0.627       | -0.005  | 0.988   |\\n| Qwen3  | L36 (38%)      | 0.708      | 0.712       | +0.004  | 0.984   |\\n| Qwen3  | L52 (55%)      | 0.742      | 0.739       | -0.003  | 0.982   |\\n| Qwen3  | L68 (72%)      | 0.775      | 0.781       | +0.006  | 0.978   |\\n| Qwen3  | L80 (85%)      | 0.810      | 0.798       | -0.012  | 0.972   |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Quantization safe. 报告为一段话 + appendix table: \\\"Quantization artifacts are negligible (max |ΔAUROC| = 0.012, CKA > 0.97 across all layers), supporting the validity of our INT4/W4A16 experimental setup.\\\"\\n\\n\\n4-bit weight quantization 保留 activation 空间的大部分结构。Correctness direction 是 低维子空间特征——quantization noise 主要分布在与 correctness direction 正交的高维 null space 中 (random projection preservation 原理)。Qwen3 的 MoE + INT4 在最深层 (L80) 有稍大 delta (-0.012pp) 因为 expert routing 决策在 INT4 下可能微变，但仍在 bootstrap CI 内。 CKA(FP16, quant) > 0.97 确认 global representation structure 保留。\\n\"\n  },\n  {\n    \"name\": \"Full CKA Cross-Lingual Similarity & Simpson's Paradox Analysis\",\n    \"description\": \"Linear CKA (EN vs 20 target languages) at every probed layer, 3 models。 Core analysis: partial correlation controlling for depth (Simpson's Paradox)。 Median tier: 1-2/3 architectures significant。\\n\",\n    \"results\": {\n      \"qwen3\": {\n        \"raw_spearman_rho\": -0.24,\n        \"raw_p\": \"<0.001\",\n        \"partial_rho_ctrl_depth\": 0.16,\n        \"partial_p\": 0.072,\n        \"significant\": false,\n        \"bootstrap_ci_95\": [\n          -0.03,\n          0.35\n        ],\n        \"per_layer_positive_rho_count_of_24\": 17,\n        \"per_layer_significant_count\": 5,\n        \"cka_cliff_onset_layer\": \"L64\",\n        \"cka_cliff_onset_depth_pct\": 0.68,\n        \"cka_final_layer_mean\": 0.09,\n        \"cka_peak_layer\": \"L36\",\n        \"cka_peak_mean\": 0.82\n      },\n      \"llama4\": {\n        \"raw_spearman_rho\": -0.3,\n        \"raw_p\": \"<0.001\",\n        \"partial_rho_ctrl_depth\": 0.31,\n        \"partial_p\": 0.012,\n        \"significant\": true,\n        \"bootstrap_ci_95\": [\n          0.08,\n          0.52\n        ],\n        \"per_layer_positive_rho_count_of_12\": 10,\n        \"per_layer_significant_count\": 4,\n        \"cka_cliff_onset_layer\": \"L24\",\n        \"cka_cliff_onset_depth_pct\": 0.5,\n        \"cka_final_layer_mean\": 0.2,\n        \"cka_peak_layer\": \"L12\",\n        \"cka_peak_mean\": 0.83\n      },\n      \"gemma4\": {\n        \"raw_spearman_rho\": -0.26,\n        \"raw_p\": \"<0.001\",\n        \"partial_rho_ctrl_depth\": 0.24,\n        \"partial_p\": 0.038,\n        \"significant\": true,\n        \"bootstrap_ci_95\": [\n          0.02,\n          0.45\n        ],\n        \"per_layer_positive_rho_count_of_16\": 12,\n        \"per_layer_significant_count\": 4,\n        \"cka_cliff_onset_layer\": \"L36\",\n        \"cka_cliff_onset_depth_pct\": 0.6,\n        \"cka_final_layer_mean\": 0.15,\n        \"cka_peak_layer\": \"L20\",\n        \"cka_peak_mean\": 0.8\n      },\n      \"simpson_paradox_confirmed_of_3\": 2,\n      \"cka_transfer_collapse_threshold\": 0.3,\n      \"subspace_angle_analysis\": {\n        \"qwen3\": {\n          \"HIGH_angle\": 10,\n          \"MID_angle\": 22,\n          \"LOW_angle\": 46\n        },\n        \"llama4\": {\n          \"HIGH_angle\": 13,\n          \"MID_angle\": 26,\n          \"LOW_angle\": 41\n        },\n        \"gemma4\": {\n          \"HIGH_angle\": 11,\n          \"MID_angle\": 24,\n          \"LOW_angle\": 43\n        }\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 13: Simpson's Paradox — Raw vs Partial Correlation (3 architectures)\",\n        \"data\": \"| Architecture   | n obs | Raw ρ  | Raw p   | Partial ρ | Partial p | Boot 95% CI    | Sig? |\\n|----------------|-------|--------|---------|-----------|-----------|----------------|------|\\n| Qwen3-235B     | 480   | -0.24  | <0.001  | +0.16     | 0.072     | [-0.03, +0.35] | No   |\\n| Llama4 Scout   | 240   | -0.30  | <0.001  | +0.31     | 0.012     | [+0.08, +0.52] | Yes  |\\n| Gemma4 31B     | 320   | -0.26  | <0.001  | +0.24     | 0.038     | [+0.02, +0.45] | Yes  |\\n| Pilot Llama8B  | 45    | -0.16  | 0.294   | +0.41     | 0.006     | [+0.12, +0.65] | Yes  |\\n| Pilot Qwen7B   | 40    | -0.16  | 0.310   | +0.18     | 0.274     | [-0.15, +0.48] | No   |\\n\"\n      },\n      {\n        \"name\": \"Table 14: CKA Depth Profile Summary\",\n        \"data\": \"| Depth %  | Qwen3 CKA | Llama4 CKA | Gemma4 CKA |\\n|----------|-----------|------------|------------|\\n| 0%       | 0.70      | 0.58       | 0.62       |\\n| 17%      | 0.76      | 0.81       | 0.78       |\\n| 34%      | 0.82      | 0.75       | 0.75       |\\n| 50%      | 0.80      | 0.56       | 0.65       |\\n| 68%      | 0.60      | 0.40       | 0.48       |\\n| 77%      | 0.38      | 0.32       | 0.38       |\\n| 85%      | 0.22      | 0.28       | 0.28       |\\n| 100%     | 0.09      | 0.20       | 0.15       |\\n\"\n      },\n      {\n        \"name\": \"Table 15: Subspace Angle Analysis (Correctness Direction)\",\n        \"data\": \"| Tier | Qwen3 angle | Llama4 angle | Gemma4 angle | Mean ZS AUROC | Interpretation          |\\n|------|-------------|--------------|--------------|---------------|-------------------------|\\n| HIGH | 10°         | 13°          | 11°          | 0.72          | Near-aligned            |\\n| MID  | 22°         | 26°          | 24°          | 0.66          | Moderate rotation       |\\n| LOW  | 46°         | 41°          | 43°          | 0.57          | Substantial misalignment|\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Simpson's Paradox 在 2/3 architectures 统计显著 (Llama4, Gemma4)，Qwen3 trending (p=0.072)。 Paper 中用 hedged language: \\\"In architectures with near-linear CKA depth gradients (Llama 4, Gemma 4), partial correlation controlling for depth reveals a significant positive CKA-transfer relationship (ρ=0.24-0.31, p<0.05), confirming that CKA provides genuine explanatory power beyond depth. In Qwen3-235B, the step-function-like CKA profile limits linear partial correlation effectiveness (ρ=0.16, p=0.072); within-layer analysis confirms the positive direction (17/24 layers positive ρ).\\\" CKA cliff slope 与 Pareto strength 的 monotonic relationship across 3 architectures is suggestive but n=3 is insufficient for formal correlation. Frame as observation. Subspace angle analysis provides the most directly interpretable geometric result: correctness direction rotates gradually from EN as language distance increases, with resource tier as a strong proxy for rotation magnitude.\\n\\n\\nSimpson's Paradox 的架构依赖性源于 CKA-depth gradient 的函数形状。 Llama4 CKA 从 peak 0.83 (L12) 线性下降到 0.20 (L48)——steep linear slope 使得 linear partial correlation 高效地分离 depth confound (partial rho=0.31, p=0.012)。 Gemma4 CKA 也近似线性下降 (partial rho=0.24, p=0.038)——intermediate slope 产生 intermediate partial correlation，也刚好显著。 Qwen3 的 CKA profile 是 \\\"plateau then cliff\\\"：L0-L64 CKA 几乎不变 (0.75-0.82)， L64-L92 急剧下降到 0.09。这种 step-function-like profile 导致 linear partial correlation 效果差——depth 作为线性控制变量无法有效 capture 非线性 CKA-depth 关系。 Partial rho=0.16 (p=0.072) trending 但不显著。加入 depth² 作为二次控制项后可能显著， 但 paper 中应诚实报告 standard method 的结果。 Per-layer analysis (n=20 languages per layer): 大多数层的 within-layer rho 为正 (70-83% of layers across models)，但因 n=20 individual significance 有限。 最有 power 的层在 50-75% depth（CKA variance 最大的区域）。 Subspace angle 提供互补定量证据：HIGH 语言 ~10-13°（几乎对齐，zero-shot 可行）， LOW 语言 ~41-46°（严重 misaligned，需要 linear projection）。 这与 Procrustes reversal (plan_012) 的发现互洽——reversal 阈值对应 ~20-25° angle。\\n\"\n  },\n  {\n    \"name\": \"Linear Projection Sensitivity & Procrustes Effect Reversal\",\n    \"description\": \"Vary parallel pairs (10, 20, 50, 100, 200) for linear projection. 2 models × 5 representative layers × 20 languages。Resource-tier stratified saturation curves。 Procrustes effect reversal analysis。\\n\",\n    \"results\": {\n      \"overall_pairs_to_95pct\": 80,\n      \"per_tier_pairs_to_95pct\": {\n        \"HIGH\": 38,\n        \"MID\": 62,\n        \"LOW\": 95\n      },\n      \"saturation_curve\": {\n        \"pairs_10\": {\n          \"pct_of_max\": 0.38,\n          \"mean_delta_auroc_pp\": 1.1\n        },\n        \"pairs_20\": {\n          \"pct_of_max\": 0.58,\n          \"mean_delta_auroc_pp\": 1.7\n        },\n        \"pairs_50\": {\n          \"pct_of_max\": 0.82,\n          \"mean_delta_auroc_pp\": 2.5\n        },\n        \"pairs_100\": {\n          \"pct_of_max\": 0.95,\n          \"mean_delta_auroc_pp\": 2.9\n        },\n        \"pairs_200\": {\n          \"pct_of_max\": 1.0,\n          \"mean_delta_auroc_pp\": 3.0\n        }\n      },\n      \"procrustes_reversal\": {\n        \"threshold_estimate\": 0.57,\n        \"threshold_ci_95\": [\n          0.48,\n          0.64\n        ],\n        \"benefit_below_0.50\": {\n          \"mean_delta_pp\": 5.5,\n          \"n_langs\": 3\n        },\n        \"ambiguous_0.50_0.60\": {\n          \"mean_delta_pp\": 1.8,\n          \"n_langs\": 5\n        },\n        \"mild_benefit_0.60_0.65\": {\n          \"mean_delta_pp\": 0.3,\n          \"n_langs\": 4\n        },\n        \"harm_above_0.65\": {\n          \"mean_delta_pp\": -1.5,\n          \"n_langs\": 8\n        }\n      },\n      \"saturation_r2_by_tier\": {\n        \"HIGH\": 0.97,\n        \"MID\": 0.92,\n        \"LOW\": 0.8\n      },\n      \"linear_proj_delta_low_resource_pp\": 5.0\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 16: Saturation Curves by Resource Tier (Qwen3-235B, L68)\",\n        \"data\": \"| Pairs | HIGH Δ (pp) | MID Δ (pp) | LOW Δ (pp) | Overall Δ (pp) |\\n|-------|-------------|------------|------------|----------------|\\n| 10    | +0.1        | +0.8       | +2.5       | +1.1           |\\n| 20    | +0.3        | +1.5       | +3.8       | +1.7           |\\n| 50    | +0.4        | +2.3       | +5.2       | +2.5           |\\n| 100   | +0.5        | +2.6       | +5.8       | +2.9           |\\n| 200   | +0.5        | +2.7       | +6.2       | +3.0           |\\n\"\n      },\n      {\n        \"name\": \"Table 17: Procrustes Effect Reversal by ZS AUROC Band\",\n        \"data\": \"| ZS AUROC band | n langs | Mean Δ (pp) | Std  | % positive | Example langs     |\\n|---------------|---------|-------------|------|------------|-------------------|\\n| < 0.50        | 3       | +5.5        | 1.8  | 100%       | am, yo, te        |\\n| 0.50 - 0.58   | 3       | +3.2        | 1.5  | 100%       | sw, bn, tr        |\\n| 0.58 - 0.62   | 2       | +1.2        | 0.9  | 100%       | hi, vi            |\\n| 0.62 - 0.67   | 4       | +0.2        | 0.8  | 50%        | ar, ko, id, uk    |\\n| 0.67 - 0.72   | 4       | -0.8        | 0.6  | 25%        | ru, ja, de, pt    |\\n| > 0.72        | 4       | -1.8        | 0.5  | 0%         | zh, es, fr, nl    |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Linear projection 是最直接的 practical contribution：80 parallel pairs (约 3-4 小时标注) 达到 95% of max improvement。LOW-resource languages benefit most (+5-6pp)，正是最需要帮助的类别。 Procrustes reversal 是重要的 practitioner caveat——不加区分地做 alignment 会损害已经 well-aligned 的语言。Deployment recommendation: 先测 zero-shot AUROC，低于 0.57 时 use projection， 高于 0.65 时直接 zero-shot，0.57-0.65 区间按 language-specific validation 决定。 Architecture-dependent threshold variation: Qwen3 threshold ~0.55, Llama4 ~0.60 (Llama4 的 better baseline alignment 意味着 reversal 出现更早)—— 但 n=2 architectures 不足以 parametrize threshold，建议 practitioner 用 ~0.57 ± 0.05。\\n\\n\\nSaturation at ~80 pairs (而非 pilot 预估的 ~50)，因为：(1) 20 语言引入更多方差， (2) 部分低资源语言的 parallel pair translation quality 低（机翻 artifacts 增加 noise）， (3) 低资源语言的 subspace angle 更大 (~40-46°)，需要更多样本来估计更复杂的旋转。 Resource-tier stratification 清晰：HIGH 语言 ~38 pairs (subspace angle ~10-13°, 简单旋转)， LOW 语言 ~95 pairs (angle ~41-46°, 更复杂旋转 + translation noise)。 Procrustes reversal mechanism: 当 ZS AUROC > 0.65 时，EN-target correctness direction 已 near-aligned (angle <15°)，Procrustes 旋转估计引入的 noise > alignment gain → 净负效果。 当 ZS AUROC < 0.50 时，严重 misalignment (angle >35°) 使得 alignment gain >> noise。 Threshold ~0.57 对应 ~20° angle 的平衡点。 LOW tier 的 curve 不够 clean (R²=0.80)——个别语言 saturation 非单调 (e.g., sw 在 20 pairs 时偶然好于 50 pairs，因为特定 pair 的 quality variance)。 Practical recommendation: ~80 parallel pairs for general use; skip projection for HIGH-resource languages (ZS AUROC > 0.65)。\\n\"\n  },\n  {\n    \"name\": \"Probing Control Tasks — Full Scale (20 languages × 3 models)\",\n    \"description\": \"Hewitt & Liang (2019) control tasks 扩展到 20 languages × 3 architectures × 所有 probed layers。 验证 AUROC 反映 genuine correctness direction。Selectivity threshold sensitivity analysis。 Note: English-only pilot DONE (plan_013 registry), 此处为 full cross-lingual extension。\\n\",\n    \"results\": {\n      \"overall_artifact_rate_pct\": 22,\n      \"artifact_rate_by_tier\": {\n        \"HIGH\": 5,\n        \"MID\": 22,\n        \"LOW\": 35\n      },\n      \"selectivity_deep_layers_mean\": 0.2,\n      \"selectivity_by_tier_deep_layers\": {\n        \"HIGH\": 0.23,\n        \"MID\": 0.16,\n        \"LOW\": 0.08\n      },\n      \"control_auroc_range\": [\n        0.48,\n        0.52\n      ],\n      \"threshold_sensitivity\": {\n        \"threshold_0.03\": {\n          \"artifact_rate_pct\": 32\n        },\n        \"threshold_0.05\": {\n          \"artifact_rate_pct\": 22\n        },\n        \"threshold_0.10\": {\n          \"artifact_rate_pct\": 12\n        }\n      },\n      \"affected_zone\": \"primarily 0-40% depth for MID/LOW, 0-20% depth for HIGH\",\n      \"cross_lingual_control_finding\": \"~22% of language-layer combinations have selectivity < 0.05. Concentrated in LOW-resource shallow layers (83% of L0-25% depth × LOW tier). At EN-optimal depth, only am/yo/te have selectivity < 0.05 (probe capacity artifacts).\\n\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 18: Artifact Rate by Resource Tier and Depth (3-model mean)\",\n        \"data\": \"| Depth zone     | HIGH artifact % | MID artifact % | LOW artifact % | Overall |\\n|----------------|-----------------|----------------|----------------|---------|\\n| 0-25% depth    | 15%             | 55%            | 80%            | 50%     |\\n| 25-50% depth   | 3%              | 28%            | 55%            | 29%     |\\n| 50-75% depth   | 0%              | 10%            | 18%            | 9%      |\\n| 75-100% depth  | 0%              | 2%             | 5%             | 2%      |\\n| Overall        | 5%              | 22%            | 35%            | 22%     |\\n\"\n      },\n      {\n        \"name\": \"Table 19: Selectivity at EN-Optimal Layer (representative languages)\",\n        \"data\": \"| Tier | Language | Real AUROC | Control AUROC | Selectivity | Artifact? |\\n|------|----------|------------|---------------|-------------|-----------|\\n| HIGH | zh       | 0.738      | 0.502         | 0.236       | No        |\\n| HIGH | es       | 0.745      | 0.498         | 0.247       | No        |\\n| MID  | hi       | 0.670      | 0.506         | 0.164       | No        |\\n| MID  | tr       | 0.660      | 0.510         | 0.150       | No        |\\n| LOW  | sw       | 0.598      | 0.508         | 0.090       | No        |\\n| LOW  | bn       | 0.612      | 0.504         | 0.108       | No        |\\n| LOW  | yo       | 0.535      | 0.512         | 0.023       | YES       |\\n| LOW  | am       | 0.530      | 0.515         | 0.015       | YES       |\\n| LOW  | te       | 0.572      | 0.518         | 0.054       | Borderline|\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Control task 发现是独立的 methodological contribution。在 paper main body 中： (1) 用 selectivity threshold 过滤不可靠结果后重新报告 main results (confirm conclusions unchanged); (2) 报告 ~22% artifact rate 作为 methodological warning for the field; (3) 讨论 implications: \\\"all cross-lingual probing studies should include selectivity checks, especially for low-resource languages where probe capacity can mimic genuine signal.\\\" am/yo 在 EN-optimal depth 的 selectivity < 0.03 确认 plan_005 中这些语言的 高 cosine similarity 是 noise artifact 而非真实 correctness-confidence alignment。\\n\\nPilot (Qwen2.5-7B EN-only) 显示 selectivity 在 L20+ 为 0.24-0.26, L0-L12 为 0.02-0.04。 跨语言扩展时：HIGH 资源语言的 deep-layer selectivity 接近 EN (~0.23)—— 模型对这些语言有足够的 correctness signal 使 real probe >> control probe。 MID 资源语言 deep-layer selectivity 降至 ~0.16——仍明显超过 threshold 但 gap 缩小， 因为 (1) correctness signal 更弱, (2) control probe 在更 uniform 的 activation 分布上 偶尔达到略高 AUROC (0.50→0.51)。 LOW 资源语言 deep-layer selectivity 仅 ~0.08——部分 language-layer 组合低于 0.05 threshold， 尤其是 am/yo/te (这些语言在模型训练数据中极少，correctness signal 接近 noise floor)。 ~22% overall artifact rate (at threshold 0.05) 的 breakdown： 5% from HIGH (仅最浅层 L0-L4), 22% from MID (shallow+mid layers), 35% from LOW (broad range)。 Threshold sensitivity: 0.03 更宽松 (32% artifacts)，0.10 更严格 (仅 12%)—— paper 中报告 0.05 (Hewitt & Liang original) as primary，0.03/0.10 in sensitivity analysis。 Field-level contribution: 首次在 cross-lingual probing 中系统应用 selectivity analysis。\\n\"\n  }\n]",
      "numLines": 796,
      "startLine": 1,
      "totalLines": 796
    }
  },
  "sourceToolAssistantUUID": "0263ea16-1d24-4985-96f2-85fc8219b40c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T13:32:40.575Z_

<details><summary>↩ Tool result · `toolu_01VJVSQY3DZLoYnpJ3iy9Ytb`</summary>

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
  "parentUuid": "b97e3c4e-a753-4366-9d7a-e65159746e87",
  "isSidechain": false,
  "promptId": "e8f1a248-e970-4548-96f9-5cd439647eab",
  "type": "user",
  "uuid": "221d4324-f00a-4c4f-b8ec-8ea3191a6079",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median/paper_framing.md",
      "content": "# Paper Framing — xling_calib_direction\n\n## Target Venue\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\n- Core submission: 3 models (Qwen3-235B MoE + Llama 4 Scout MoE + Gemma 4 31B Dense) × 20 languages × all contributions\n- Camera-ready extension: 30+ languages\n\n## Core Insight\nThe model's internal correctness direction occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). A Simpson's Paradox reveals the true CKA-transfer relationship: raw correlation is negative (depth confound), but controlling for depth yields a significant positive partial correlation — within each layer, higher cross-lingual CKA predicts better transfer. Deeper layers generally improve both English quality and cross-lingual transfer (Spearman ρ>0.7, p<0.05 for 4/5 languages in pilot), but the Pareto frontier reveals a local tradeoff at the deepest layers: final 1–3 layers gain marginal English AUROC (+0.8pp) at the cost of transfer degradation (1.5–4pp in 3/5 languages). This local tradeoff shape is architecture-dependent (strong on Qwen, weak on Llama), and combines with the geometric CKA insight to provide a structural explanation for when and why cross-lingual probe transfer succeeds or fails. CaCLR tests whether distributional matching can shift this frontier without target-language labels.\n\n## Core Claims (4, causal chain)\n\n### Claim 1 — Pareto Frontier (Discovery)\nCross-lingual correctness probes show that deeper layers generally improve both English quality and cross-lingual transfer (Spearman ρ>0.7, p<0.05 for 4/5 languages), but the deepest layers exhibit a local Pareto tradeoff where marginal English gains trade against transfer quality. This local tradeoff varies across architectures: on Qwen, the final layers consistently degrade transfer (3/5 languages, 1.5–4pp); on Llama, the tradeoff is language-specific. Architecture variation in tradeoff shape is an observational finding (n=2-3 architectures differing in type, scale, layer count, and training data; no causal attribution to specific architectural features like MoE routing without direct evidence).\n- MVP evidence: Qwen2.5-7B shows clear Pareto (L27 EN best but transfer drops 2-4pp vs L24 across 4/5 langs). Llama-3.1-8B shows weak Pareto (only 2/5 langs show depth-transfer tradeoff; ar/ko improve with depth).\n- Full evidence: 3 architectures (Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense) × 20 languages × all layers × 5 transfer conditions. Dense vs MoE contrast addresses architecture confound (D016). Per-language Spearman rho to quantify Pareto strength per language-architecture combination.\n\n### Claim 2 — Decomposition (Analysis)\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\n\n### Claim 3 — CaCLR (Method / Diagnostic)\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on probe logits computed from parallel inputs — English and target language versions of the same GlobalMMLU train-split items) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels. Note: MMD must operate on probe outputs (logits), not raw activations, to ensure gradient flow to probe parameters (M007). For linear probes, logits are 1-D, so MMD operates in 1-D space. **Defense**: 1-D is the principled choice — MMD should match probe OUTPUT distributions (calibration target), not activation-space distributions (3584-D where MMD is statistically unreliable due to curse of dimensionality). High-dimensional activation-space MMD would be an alignment objective, not a calibration objective. Frame as \"principled scope\" not \"design limitation.\"\n- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.\n- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that MMD-based distributional matching fails for correctness probe transfer (scope to MMD specifically; acknowledge domain adaptation theory predicts marginal matching failure when conditional distributions differ, cite Zhao et al. 2019). CKA geometric analysis reveals that correctness information occupies a low-dimensional language-agnostic subspace that persists even as global representations diverge (CKA drops). MMD matches marginal distributions but cannot align low-dimensional directional structure within those distributions. Linear projection succeeds because it learns the subspace rotation directly. This closes the MMD distributional-matching path with both empirical evidence and geometric analysis. **Framing note**: CaCLR is presented as the natural baseline that tests whether distributional matching works for this problem class — NOT as a novel method contribution. Acknowledge that this is a self-proposed method; the contribution is the systematic negative result + geometric explanation, not the method itself.\n- **Implementation specification (MUST report for reproducibility)**: MMD kernel (Gaussian RBF with median heuristic bandwidth), optimizer (Adam), learning rate, epochs, early stopping criterion, initialization strategy (from standard LR solution vs random), batch size, whether MMD computed on same items as BCE or held-out. For negative result, higher reproducibility bar — community must verify fair trial.\n- Parallel activations source: GlobalMMLU test split, partitioned into probe_train (70%) and eval (30%) via stratified split. English BCE labels and parallel activations for MMD both come from probe_train portion only; evaluation exclusively on eval portion. This avoids same-data-for-training-and-evaluation concern while requiring zero target-language *labels*. GlobalMMLU has no train split (only test+dev); dev (285 samples) too small for MMD. Report parallel set size per language and translation quality assessment for low-resource languages.\n- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.\n\n### Claim 4 — Cross-Lingual Orthogonality (Supporting Evidence, subsection not standalone claim)\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture. **Downgraded from standalone claim to supporting evidence** (D012): reviewer assessment indicates weakest standalone novelty (\"method replication to more languages\"). Presented as subsection supporting Claim 1's architecture/language analysis. Space freed for stronger contributions (control task finding, projection sample efficiency).\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\n\n### Key Empirical Contributions (elevated from appendix to main body, D012)\n- **Control task methodological warning**: English probing controls (Hewitt & Liang selectivity) show selectivity concentrated in deeper layers (L20+, selectivity >0.20), with shallow layers near chance — raising concerns that shallow-layer positive transfer in low-resource languages may reflect capacity artifacts. Cross-lingual control experiments planned to quantify the fraction. First application of probing controls to cross-lingual transfer setting. Field-level implication: all cross-lingual probing studies should include selectivity checks.\n- **Linear projection sample efficiency**: Procrustes alignment with ~50 parallel pairs achieves 98% of 200-pair performance. Resource-tier stratification: HIGH languages saturate at ~22 pairs, LOW at ~48. Directly actionable for practitioners.\n- **Procrustes effect reversal**: Linear projection helps when zero-shot AUROC < 0.50 but hurts when > 0.60. Implies alignment strategy must be conditioned on baseline transfer quality — not all languages benefit from geometric alignment.\n\n## Story Spine\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\n- **Our framing**: First large-scale study comparing correctness probe transfer across architectures in multilingual settings. Core novel findings: (1) Simpson's Paradox in CKA-transfer relationship — raw correlation negative (depth confound), partial correlation positive (within-layer, higher CKA = better transfer) — a genuine geometric insight not predicted by prior work; (2) English probing controls reveal layer-dependent selectivity, suggesting shallow-layer low-resource results may be capacity artifacts (control task warning for the field; cross-lingual quantification pending); (3) linear projection with ~50 pairs is the practical solution, with resource-tier-dependent saturation. We discover the local Pareto tradeoff at the deepest layers (overall depth-transfer trend is positive), decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching baseline, and provide CKA geometric analysis of why transfer succeeds or fails. This is both a field-level viability test and a source of novel methodological insights.\n- **Headline template (method success)**: \"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\"\n- **Headline template (negative result)**: \"Cross-lingual correctness probe transfer reveals architecture-dependent depth effects; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs is the most effective label-free transfer method.\" Note: linear projection is \"the only label-free method that consistently improves over zero-shot across resource tiers\" — NOT \"only viable path.\" Zero-shot is viable for high-resource (AUROC>0.60); few-shot (100 labels) may outperform linear projection in absolute terms. CaCLR outcome pending. The value proposition is zero correctness labels + cross-tier consistency, not absolute best performance.\n- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.\n\n## Field-Level Significance\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\n\n## Anticipated Reviewer Concerns & Responses\n1. **\"Xiao et al. already did this\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.\n2. **\"Temperature scaling baseline\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\n3. **\"Mean-shift too weak / why does it fail?\"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.\n4. **\"Difficulty confound\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\n5. **\"INT8 artifacts\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\n6. **\"Only MCQA\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\n7. **\"Predictable from domain adaptation theory\"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.\n8. **\"No statistical tests\"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.\n9. **\"Probing methodology concerns\"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.\n10. **\"No mechanistic explanation\"** → CKA geometric analysis reveals a Simpson's Paradox: raw CKA-transfer correlation is negative (depth confound), but partial correlation controlling for depth is significantly positive (Llama pilot: rho=+0.41, p=0.006; 14/17 layer-level correlations positive). Within each layer, higher cross-lingual CKA predicts better transfer — CKA provides genuine explanatory power beyond depth. Subspace angle analysis (quantitative tables) strengthens geometric narrative. Frame as \"geometric analysis\" not \"mechanistic explanation.\" **Transparency requirements**: (a) Report Qwen pilot non-significant (rho=+0.18, p=0.274) — may be architecture-dependent or underpowered; (b) Bootstrap CIs (1000 resamples) for all partial correlations; (c) Discuss potential tautology — CKA and transfer AUROC both measure EN-target similarity, but Simpson's Paradox sign reversal is non-trivial and not predicted by measurement overlap alone.\n11. **\"Why not conformal prediction?\"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.\n12. **\"CaCLR parallel activations = test leakage?\"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.\n13. **\"CaCLR is your own method — self-debunking is less impactful\"** → CaCLR is framed as the natural baseline that tests the distributional-matching hypothesis for this problem class, not as a novel method. The contribution is the systematic negative result (β sweep across 3 OOM, component ablation) + geometric explanation of why it fails, which saves the community from pursuing this path. The positive contribution is identifying linear projection (~50 pairs) as the practical solution.\n14. **\"CKA is correlational, not mechanistic\"** → We agree and frame as geometric/correlational. MVP pilot reveals Simpson's Paradox: raw correlation negative (depth confound), partial correlation positive and significant. CKA adds genuine explanatory power beyond depth. Full-scale analysis (20 languages) with bootstrap CIs will confirm. This sign reversal is itself a novel methodological finding for the cross-lingual probing literature.\n\n## Additional Related Work Coverage (Dream-identified gaps)\n- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. Zhao et al. (2019) \"On learning invariant representations for domain adaptation\" — directly explains why marginal distribution matching fails when conditional distributions differ; stronger theoretical grounding for CaCLR negative result than Ben-David alone.\n- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature. Explicitly discuss relationship: our linear projection is conceptually VecMap/MUSE applied at sentence-level correctness representations; the contribution is demonstrating this works for correctness probing and characterizing sample efficiency, not the projection technique itself.\n- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — CKA analysis reveals correctness direction persists as low-dimensional subspace despite global representation divergence. Must report partial correlation controlling for depth.\n- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity. Control task finding (low-resource capacity artifacts) is itself a contribution.\n- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.\n- **Cross-lingual transfer learning**: Pires et al. (2019) multilingual BERT, Wu & Dredze (2019) — broader context for cross-lingual transfer degradation with language distance.\n- **DALI**: Ravisankar et al. (2026) — cross-lingual representation alignment; must cite if published.\n\n## Differentiation from Closest Prior Work\n| Paper | Their Focus | Our Difference |\n|-------|-------------|----------------|\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\n",
      "numLines": 84,
      "startLine": 1,
      "totalLines": 84
    }
  },
  "sourceToolAssistantUUID": "b97e3c4e-a753-4366-9d7a-e65159746e87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122458 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_dire…",
  "leafUuid": "bdde09f5-4f07-4be7-b2a3-d3a33e79b6c1",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper with experimental data",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b"
}
```

---

### Assistant

_source line 14 · 2026-05-21T13:32:56.465Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of both the experiment data and the paper framing. Let me also load the research and writing skills to guide the paper structure and style.

Let me now write the complete LaTeX paper. I need to cover all 10 experiments:

1. Full Pareto Frontier — Qwen3-235B
2. Full Pareto Frontier — Llama 4 Scout
3. CaCLR Implementation and Systematic Negative Result
4. Difficulty-Controlled Decomposition Ablation
5. Cross-Lingual Orthogonality Analysis
6. Probe Complexity Comparison (LR vs 2-Layer MLP)


7. Additional Benchmark Evaluation (Belebele + MMLU-ProX)
8. Gemma 4 32.7B Dense — Third Architecture
9. Extended Language Coverage (50+ Languages)
10. Quantization Validation Ablation
11. Full CKA Cross-Lingual Similarity & Simpson's Paradox Analysis
12. Linear Projection Sensitivity & Procrustes Effect Reversal
13. Probing Control Tasks — Full Scale

I need to organize these into a coherent paper structure with an abstract, introduction, related work, method section, comprehensive experiments with appropriate subsections, and conclusion, weaving together the key narrative from the guidance materials.

The Pareto frontier replicates at scale but with diminished effects and increased noise, while the CaCLR consistency loss shows no meaningful impact—a negative result I can frame through geometric reasoning. Simpson's Paradox appears in one or two of the three architectures, which means I'm downgrading the decomposition claim to a qualitative observation rather than a strong finding. The core headline is that cross-lingual probe transfer exhibits architecture-dependent depth effects, distributional matching doesn't work as hoped, but linear projection with roughly eighty parallel language pairs emerges as the practical label-free solution. This framing should hold up for EACL submission.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "221d4324-f00a-4c4f-b8ec-8ea3191a6079",
  "isSidechain": false,
  "requestId": "req_011CbFoGhuCKBQDdSXGKqYwT",
  "type": "assistant",
  "uuid": "1622eb78-0606-4aaf-a08f-a390edcd7d20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QtBaCt971fERUPjc7wPWL7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29557,
      "cache_read_input_tokens": 23385,
      "output_tokens": 672,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 29557,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 672,
          "cache_read_input_tokens": 23385,
          "cache_creation_input_tokens": 29557,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 29557
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

_source line 15 · 2026-05-21T13:32:56.470Z_

Now let me read the research and writing skills for style guidance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1622eb78-0606-4aaf-a08f-a390edcd7d20",
  "isSidechain": false,
  "requestId": "req_011CbFoGhuCKBQDdSXGKqYwT",
  "type": "assistant",
  "uuid": "bba3cd4f-df5c-4fbc-a022-b05613a54cf1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QtBaCt971fERUPjc7wPWL7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29557,
      "cache_read_input_tokens": 23385,
      "output_tokens": 672,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 29557,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 672,
          "cache_read_input_tokens": 23385,
          "cache_creation_input_tokens": 29557,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 29557
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

_source line 16 · 2026-05-21T13:32:57.344Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Q4p34QfoBdQbd9s8yt7ebg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/skills/projects/xling_calib_direction/distilled-research.skill.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bba3cd4f-df5c-4fbc-a022-b05613a54cf1",
  "isSidechain": false,
  "requestId": "req_011CbFoGhuCKBQDdSXGKqYwT",
  "type": "assistant",
  "uuid": "930868c0-1d50-40e9-96d9-d6f7992dad3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QtBaCt971fERUPjc7wPWL7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29557,
      "cache_read_input_tokens": 23385,
      "output_tokens": 672,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 29557,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 672,
          "cache_read_input_tokens": 23385,
          "cache_creation_input_tokens": 29557,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 29557
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

_source line 17 · 2026-05-21T13:32:57.586Z_

<details><summary>↩ Tool result · `toolu_01Qvec8GwwjNKA3RjSt628NT`</summary>

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
  "parentUuid": "4c952648-7e7c-4ef7-8260-546cb60c4c42",
  "isSidechain": false,
  "promptId": "e8f1a248-e970-4548-96f9-5cd439647eab",
  "type": "user",
  "uuid": "ef879eed-99f1-49fc-9fc5-e46822db8f18",
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
  "sourceToolAssistantUUID": "4c952648-7e7c-4ef7-8260-546cb60c4c42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T13:32:57.354Z_

<details><summary>↩ Tool result · `toolu_01Q4p34QfoBdQbd9s8yt7ebg`</summary>

```text
1	---
2	name: xling-calib-direction-research
3	description: Research patterns from 12 papers on cross-lingual calibration and internal representations in LLMs
4	type: skill
5	---
6	
7	# Cross-Lingual Calibration — Research Patterns (12 papers)
8	
9	## Evaluation Protocol
10	
11	**Metrics**: ECE (8/12) + AUROC (5/12) + Brier (4/12). Always pair calibration with discrimination. Point estimates without CIs is field norm (6/8). High conf.
12	
13	**Benchmarks**: MMLU (5/12), Belebele for multilingual (122 langs), TruthfulQA. Transfer: ARC, HellaSwag, CSQA. High conf.
14	
15	**Models**: 3-6 models. Llama-3.1-8B + Qwen2.5-7B near-universal. Include multilingual-first model (Aya). High conf.
16	
17	## Method Trends
18	
19	**Linear probing of hidden states** (7/12): Linear classifiers suffice. AUC 0.80-0.97. Source: confidence_manifold2026. High conf.
20	
21	**Layer-wise analysis standard** (7/12): Middle-to-late layers (15-29/32) richest for xling/calibration. Final layer suboptimal for non-English. Source: zhou2025lace (24-29), civelli2026shared (xling ~15, monolingual ~30). High conf.
22	
23	**Inference-time steering** (4/12): Extract direction, add to activations, no retraining. Source: ji2025calibrating, miao2026coral, miao2026closing. Med conf.
24	
25	**Training-free methods rising** (3/12): LACE, mean shift, projection. Field moving from fine-tuning. Med conf.
26	
27	**Temperature scaling declining**: Only baseline now. High conf.
28	
29	## Cross-Paper Findings
30	
31	**Non-English ECE 5x English** (23% vs 4.6%). Structural, tied to pretraining data. Source: zhou2025lace. 3/12. High conf.
32	
33	**Cross-lingual reps are linear**: Knowledge/confidence linearly encoded across languages in middle layers. Mean shift/projection enables training-free transfer. Source: xiao2025knowledge. 4/12. High conf.
34	
35	**Correctness distributed not sparse**: SAE neuron ablation negligible (delta ECE 1.25e-4). 3-8D subspace. Source: miao2026coral, confidence_manifold2026. 2/12. Med conf.
36	
37	**Layer-depth Pareto**: English calibration improves monotonically; non-English peaks mid-late then degrades. Source: zhou2025lace, joshi2025calibration. 2/12. High conf.
38	
39	## Competitor Landscape
40	
41	**zhou2025lace** (competitor): Per-language layer ensemble, ECE 22→3%, training-free. No directional methods.
42	**joshi2025calibration** (competitor): Calibration direction in residual stream. Transfers across datasets but NOT across models. Monolingual only.
43	
44	**Our niche**: No paper combines xling transfer + calibration directions + layer-depth Pareto. joshi's direction fails cross-model. civelli shows xling/monolingual optimal layers diverge. Intersection is open.
45	
46	## Gaps
47	
48	- Cross-model direction transfer unsolved (joshi shows failure)
49	- No multilingual verbal uncertainty (ji2025calibrating English-only)
50	- MCQA-only (5/12) → generation calibration open
51	- Instance-level causal validation missing (ravisankar correlation only)
52	- Scale beyond 7-8B untested
53	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "930868c0-1d50-40e9-96d9-d6f7992dad3c",
  "isSidechain": false,
  "promptId": "e8f1a248-e970-4548-96f9-5cd439647eab",
  "type": "user",
  "uuid": "f97f1fc2-6bfc-48f2-b5e0-085510589ac5",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/skills/projects/xling_calib_direction/distilled-research.skill.md",
      "content": "---\nname: xling-calib-direction-research\ndescription: Research patterns from 12 papers on cross-lingual calibration and internal representations in LLMs\ntype: skill\n---\n\n# Cross-Lingual Calibration — Research Patterns (12 papers)\n\n## Evaluation Protocol\n\n**Metrics**: ECE (8/12) + AUROC (5/12) + Brier (4/12). Always pair calibration with discrimination. Point estimates without CIs is field norm (6/8). High conf.\n\n**Benchmarks**: MMLU (5/12), Belebele for multilingual (122 langs), TruthfulQA. Transfer: ARC, HellaSwag, CSQA. High conf.\n\n**Models**: 3-6 models. Llama-3.1-8B + Qwen2.5-7B near-universal. Include multilingual-first model (Aya). High conf.\n\n## Method Trends\n\n**Linear probing of hidden states** (7/12): Linear classifiers suffice. AUC 0.80-0.97. Source: confidence_manifold2026. High conf.\n\n**Layer-wise analysis standard** (7/12): Middle-to-late layers (15-29/32) richest for xling/calibration. Final layer suboptimal for non-English. Source: zhou2025lace (24-29), civelli2026shared (xling ~15, monolingual ~30). High conf.\n\n**Inference-time steering** (4/12): Extract direction, add to activations, no retraining. Source: ji2025calibrating, miao2026coral, miao2026closing. Med conf.\n\n**Training-free methods rising** (3/12): LACE, mean shift, projection. Field moving from fine-tuning. Med conf.\n\n**Temperature scaling declining**: Only baseline now. High conf.\n\n## Cross-Paper Findings\n\n**Non-English ECE 5x English** (23% vs 4.6%). Structural, tied to pretraining data. Source: zhou2025lace. 3/12. High conf.\n\n**Cross-lingual reps are linear**: Knowledge/confidence linearly encoded across languages in middle layers. Mean shift/projection enables training-free transfer. Source: xiao2025knowledge. 4/12. High conf.\n\n**Correctness distributed not sparse**: SAE neuron ablation negligible (delta ECE 1.25e-4). 3-8D subspace. Source: miao2026coral, confidence_manifold2026. 2/12. Med conf.\n\n**Layer-depth Pareto**: English calibration improves monotonically; non-English peaks mid-late then degrades. Source: zhou2025lace, joshi2025calibration. 2/12. High conf.\n\n## Competitor Landscape\n\n**zhou2025lace** (competitor): Per-language layer ensemble, ECE 22→3%, training-free. No directional methods.\n**joshi2025calibration** (competitor): Calibration direction in residual stream. Transfers across datasets but NOT across models. Monolingual only.\n\n**Our niche**: No paper combines xling transfer + calibration directions + layer-depth Pareto. joshi's direction fails cross-model. civelli shows xling/monolingual optimal layers diverge. Intersection is open.\n\n## Gaps\n\n- Cross-model direction transfer unsolved (joshi shows failure)\n- No multilingual verbal uncertainty (ji2025calibrating English-only)\n- MCQA-only (5/12) → generation calibration open\n- Instance-level causal validation missing (ravisankar correlation only)\n- Scale beyond 7-8B untested\n",
      "numLines": 53,
      "startLine": 1,
      "totalLines": 53
    }
  },
  "sourceToolAssistantUUID": "930868c0-1d50-40e9-96d9-d6f7992dad3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T13:32:57.577Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Qvec8GwwjNKA3RjSt628NT`</summary>

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
  "parentUuid": "f97f1fc2-6bfc-48f2-b5e0-085510589ac5",
  "isSidechain": false,
  "requestId": "req_011CbFoGhuCKBQDdSXGKqYwT",
  "type": "assistant",
  "uuid": "4c952648-7e7c-4ef7-8260-546cb60c4c42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QtBaCt971fERUPjc7wPWL7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29557,
      "cache_read_input_tokens": 23385,
      "output_tokens": 672,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 29557,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 672,
          "cache_read_input_tokens": 23385,
          "cache_creation_input_tokens": 29557,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 29557
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

_source line 20 · 2026-05-21T13:33:00.524Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me write the complete LaTeX paper. I need to ensure the output directory exists first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef879eed-99f1-49fc-9fc5-e46822db8f18",
  "isSidechain": false,
  "requestId": "req_011CbFoHxfyZnktSmcZmoBgf",
  "type": "assistant",
  "uuid": "7e48d1f5-85f5-4da0-b875-fefbda2d22d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gQkbZMNmSLbirhiiy7g5H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2624,
      "cache_read_input_tokens": 52942,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2624,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 174,
          "cache_read_input_tokens": 52942,
          "cache_creation_input_tokens": 2624,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2624
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

_source line 21 · 2026-05-21T13:33:00.533Z_

Let me check that the output directory exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e48d1f5-85f5-4da0-b875-fefbda2d22d4",
  "isSidechain": false,
  "requestId": "req_011CbFoHxfyZnktSmcZmoBgf",
  "type": "assistant",
  "uuid": "a2e7d05e-1857-4e23-8b82-2f7333032f62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gQkbZMNmSLbirhiiy7g5H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2624,
      "cache_read_input_tokens": 52942,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2624,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 174,
          "cache_read_input_tokens": 52942,
          "cache_creation_input_tokens": 2624,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2624
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

_source line 22 · 2026-05-21T13:33:01.965Z_

<details open><summary>🔧 Tool call — Bash · `toolu_011HdYxEHss9usjEQqgYVaoE`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median/",
  "description": "List target output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2e7d05e-1857-4e23-8b82-2f7333032f62",
  "isSidechain": false,
  "requestId": "req_011CbFoHxfyZnktSmcZmoBgf",
  "type": "assistant",
  "uuid": "fff5482a-4f59-4b59-9e16-fc41f7c2cd80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gQkbZMNmSLbirhiiy7g5H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2624,
      "cache_read_input_tokens": 52942,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2624,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 174,
          "cache_read_input_tokens": 52942,
          "cache_creation_input_tokens": 2624,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2624
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

_source line 23 · 2026-05-21T13:33:02.132Z_

<details><summary>↩ Tool result · `toolu_011HdYxEHss9usjEQqgYVaoE`</summary>

```text
total 156
drwxr-xr-x 2 ubuntu ubuntu  4096 May 21 13:32 .
drwxr-xr-x 5 ubuntu ubuntu  4096 May 21 13:32 ..
-rw-r--r-- 1 ubuntu ubuntu 60322 May 21 13:32 experiment_data.json
-rw-r--r-- 1 ubuntu ubuntu 66107 May 21 13:32 imagined_experiments.yaml
-rw-r--r-- 1 ubuntu ubuntu 19467 May 21 13:32 paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fff5482a-4f59-4b59-9e16-fc41f7c2cd80",
  "isSidechain": false,
  "promptId": "e8f1a248-e970-4548-96f9-5cd439647eab",
  "type": "user",
  "uuid": "0388f30a-20cd-4524-9ec1-fc336bbeda49",
  "toolUseResult": {
    "stdout": "total 156\ndrwxr-xr-x 2 ubuntu ubuntu  4096 May 21 13:32 .\ndrwxr-xr-x 5 ubuntu ubuntu  4096 May 21 13:32 ..\n-rw-r--r-- 1 ubuntu ubuntu 60322 May 21 13:32 experiment_data.json\n-rw-r--r-- 1 ubuntu ubuntu 66107 May 21 13:32 imagined_experiments.yaml\n-rw-r--r-- 1 ubuntu ubuntu 19467 May 21 13:32 paper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "fff5482a-4f59-4b59-9e16-fc41f7c2cd80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-21T13:33:04.782Z_

Now writing the full LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0388f30a-20cd-4524-9ec1-fc336bbeda49",
  "isSidechain": false,
  "requestId": "req_011CbFoJHnvDPFNh2zH32B1R",
  "type": "assistant",
  "uuid": "0ff092ae-8a0f-478f-a371-d7df87347fef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0178REvBLC8RPpxaFNST1rSr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 340,
      "cache_read_input_tokens": 55566,
      "output_tokens": 14638,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 340,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14638,
          "cache_read_input_tokens": 55566,
          "cache_creation_input_tokens": 340,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 340
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

_source line 25 · 2026-05-21T13:37:31.185Z_

<details open><summary>🔧 Tool call — Write · `toolu_015cLLLkynD6iTze8fsjVJC8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{microtype}\n\n\\newcommand{\\aur}{\\textsc{auroc}}\n\\newcommand{\\ece}{\\textsc{ece}}\n\\newcommand{\\zs}{\\textsc{zs}}\n\\newcommand{\\caclr}{\\textsc{CaCLR}}\n\\newcommand{\\cka}{\\textsc{CKA}}\n\n\\title{Cross-Lingual Correctness Probe Transfer Reveals Architecture-Dependent Depth Effects:\\\\ Distributional Matching Fails but Linear Projection Succeeds}\n\n\\author{\n  Anonymous \\\\\n  \\texttt{anonymous@example.com}\n}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nProbe-based calibration methods extract internal correctness directions from LLM hidden states, achieving strong results in English. Whether these directions transfer cross-lingually remains untested at scale. We present the first large-scale study of correctness probe transfer across three architectures (Qwen3-235B MoE, Llama~4 Scout MoE, Gemma~4 31B Dense) and 20~languages spanning four resource tiers. We find: (1)~a depth--transferability Pareto tradeoff that is architecture-dependent---9/20 languages show significant negative depth--transfer correlation on Qwen3 versus 5/20 on Llama~4; (2)~\\cka{} analysis reveals a Simpson's Paradox where raw CKA--transfer correlation is negative but partial correlation controlling for depth is significantly positive in 2/3~architectures; (3)~distributional matching via \\caclr{} (MMD-based consistency loss) is inert across a full $\\beta$ sweep, with CORAL and high-dimensional MMD variants also failing---geometric analysis shows these methods reduce marginal distance but leave the correctness subspace angle unchanged; (4)~linear projection with ${\\sim}80$~parallel pairs achieves 95\\% of maximum improvement and is the most effective label-free transfer method, particularly for low-resource languages (+5--6~pp). We release probing controls showing 22\\% of language--layer combinations contain capacity artifacts, concentrated in low-resource shallow layers---a methodological warning for the field.\n\\end{abstract}\n\n% ============================================================\n% 1. INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nNon-English languages suffer substantially worse calibration in multilingual LLMs, with expected calibration error (\\ece{}) reaching 5$\\times$ that of English \\cite{zhou2025lace}. Recent work demonstrates that internal correctness directions---linear features in hidden-state space that predict answer correctness---enable effective probe-based calibration for English \\cite{miao2026coral,joshi2025calibration,confidence_manifold2026}. These correctness directions are orthogonal to verbalized confidence \\cite{miao2026closing}, occupy a low-dimensional subspace \\cite{confidence_manifold2026}, and can be extracted with simple logistic regression \\cite{joshi2025calibration}. Yet no prior work systematically tests whether this research line extends beyond English.\n\nThe closest prior effort, \\citet{xiao2025knowledge}, transfers \\emph{knowledge-boundary} probes (input-level answerability) across 8~languages, finding partial success with mean-shift alignment. However, knowledge-boundary and correctness probes target fundamentally different signals: answerability is input-dependent and binary, while correctness depends on the model's actual output and varies with question difficulty. \\citet{civelli2026shared} show that cross-lingual and monolingual optimal layers diverge, but do not study correctness probing or calibration. The intersection of cross-lingual transfer, correctness directions, and calibration remains open.\n\nWe present the first large-scale study of cross-lingual correctness probe transfer, spanning three architectures (Qwen3-235B, Llama~4 Scout, Gemma~4 31B), 20~languages across four resource tiers, and multiple transfer methods. Our core finding is that \\textbf{deeper layers generally improve both English discrimination and cross-lingual transfer, but the deepest layers exhibit a local Pareto tradeoff where marginal English gains trade against transfer quality}---and the shape of this tradeoff is architecture-dependent. A Simpson's Paradox in the \\cka{}--transfer relationship provides geometric insight: raw correlation is negative (depth confound), but within each layer, higher cross-lingual \\cka{} predicts better transfer.\n\nOur contributions are: (1)~discovery of the architecture-dependent Pareto frontier across 3~architectures and 20~languages; (2)~a systematic negative result showing that distributional matching (MMD, CORAL, high-dimensional variants) fails for correctness probe transfer, with geometric explanation via \\cka{} subspace analysis; (3)~characterization of linear projection as the practical label-free solution, with resource-tier-stratified saturation at ${\\sim}80$~parallel pairs; (4)~first application of probing controls \\cite{hewitt2019designing} to cross-lingual transfer, revealing that 22\\% of language--layer combinations are capacity artifacts.\n\n% ============================================================\n% 2. RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Probe-based calibration.}\n\\citet{joshi2025calibration} extract calibration directions from residual streams, finding strong within-model transfer across datasets but failure across models. \\citet{miao2026coral} discover distributed correctness representations via SAE analysis and propose cross-task steering. \\citet{miao2026closing} show correctness and verbalized confidence directions are orthogonal ($\\cos < 0.04$), motivating probe-based over output-based calibration. \\citet{confidence_manifold2026} demonstrate that correctness occupies a 3--8D subspace accessible to linear probes. All are English-only.\n\n\\paragraph{Cross-lingual representations.}\nCross-lingual representations in multilingual LLMs exhibit linear structure amenable to projection-based alignment \\cite{conneau2018word,artetxe2018robust}. \\citet{pires2019multilingual} and \\citet{wu2019beto} establish that mBERT transfers cross-lingually via shared subspaces. \\citet{ravisankar2026dali} study cross-lingual representation alignment more broadly. Our linear projection is conceptually analogous to VecMap/MUSE applied at sentence-level correctness representations; the contribution is demonstrating effectiveness for correctness probing and characterizing sample efficiency.\n\n\\paragraph{Multilingual calibration.}\n\\citet{zhou2025lace} propose per-language layer ensembles (LACE), reducing non-English \\ece{} from 22\\% to 3\\%, but require per-language labeled data. \\citet{xiao2025knowledge} transfer knowledge-boundary probes across 8~languages using mean-shift. We target a different signal (correctness), a different metric (calibration), more languages (20+), and analyze the Pareto frontier.\n\n\\paragraph{Domain adaptation theory.}\n\\citet{bendavid2010theory} provide the H-divergence framework predicting that representation alignment aids transfer. \\citet{zhao2019learning} show that marginal distribution matching fails when conditional distributions differ---directly grounding our \\caclr{} negative result.\n\n\\paragraph{Probing methodology.}\nWe follow \\citet{hewitt2019designing}'s control-task framework to validate that probe \\aur{} reflects genuine correctness directions rather than capacity artifacts.\n\n% ============================================================\n% 3. METHOD\n% ============================================================\n\\section{Method}\n\n\\subsection{Correctness Probes}\n\nGiven a multilingual LLM and a multiple-choice question $q$ with model answer $a$, we extract the hidden-state representation $\\mathbf{h}_l \\in \\mathbb{R}^d$ at layer $l$ corresponding to the last token position. A linear probe $f_l(\\mathbf{h}) = \\sigma(\\mathbf{w}_l^\\top \\mathbf{h} + b_l)$ is trained on English data to predict binary correctness ($y = \\mathbb{1}[a = a^*]$). We use logistic regression (LR) trained with binary cross-entropy, validated by comparison with 2-layer MLP probes (Section~\\ref{sec:probe_complexity}).\n\n\\subsection{Transfer Methods}\n\nWe evaluate five transfer strategies for applying English-trained probes to target language $t$:\n\n\\paragraph{Zero-shot (\\zs{}).} Apply the English probe directly: $\\hat{p}_t = f_l(\\mathbf{h}_l^t)$.\n\n\\paragraph{Mean-shift.} Shift target representations by the mean difference: $\\hat{p}_t = f_l(\\mathbf{h}_l^t + \\boldsymbol{\\mu}^{\\text{en}} - \\boldsymbol{\\mu}^t)$. Under StandardScaler + logistic regression, this adds a constant offset to all logits; since \\aur{} is rank-invariant, $\\Delta$\\aur{} $\\equiv 0$ mathematically.\n\n\\paragraph{\\caclr{}.} We train the probe with a composite loss:\n\\begin{equation}\n\\mathcal{L} = \\mathcal{L}_{\\text{BCE}} + \\alpha \\cdot \\mathcal{L}_{\\text{SB-ECE}} + \\beta \\cdot \\mathcal{L}_{\\text{MMD}}\n\\end{equation}\nwhere $\\mathcal{L}_{\\text{MMD}}$ uses a Gaussian RBF kernel with median-heuristic bandwidth, computed on 1-D probe logits from English and target-language parallel inputs (GlobalMMLU items). This tests whether distributional matching can improve transfer. Implementation: Adam optimizer (lr=$5{\\times}10^{-4}$, cosine decay to $10^{-5}$), 50~epochs, early stopping (patience=10 on validation BCE), warm-started from the standard LR solution, batch size 256, 3~seeds.\n\n\\paragraph{Linear projection.} Learn a Procrustes rotation $\\mathbf{W}^* = \\arg\\min_{\\mathbf{W}^\\top\\mathbf{W}=\\mathbf{I}} \\|\\mathbf{W}\\mathbf{H}^t - \\mathbf{H}^{\\text{en}}\\|_F$ from $n$ parallel sentence pairs, then apply: $\\hat{p}_t = f_l(\\mathbf{W}^* \\mathbf{h}_l^t)$.\n\n\\paragraph{Few-shot.} Retrain the probe on $k$ target-language labeled examples ($k \\in \\{25, 100\\}$), requiring target-language correctness labels unlike the above methods.\n\n\\subsection{CKA Analysis}\n\nWe compute linear Centered Kernel Alignment \\cite{kornblith2019similarity} between English and target-language representations at each probed layer: $\\text{CKA}(\\mathbf{H}^{\\text{en}}_l, \\mathbf{H}^t_l)$. To disentangle the depth confound, we compute partial Spearman correlations between \\cka{} and transfer \\aur{} controlling for layer depth.\n\n\\subsection{Probing Controls}\n\nFollowing \\citet{hewitt2019designing}, we train control probes that predict random binary labels, measuring selectivity as $\\text{sel} = \\text{AUROC}_{\\text{real}} - \\text{AUROC}_{\\text{control}}$. Language--layer combinations with $\\text{sel} < 0.05$ are flagged as potential capacity artifacts.\n\n\\subsection{Data and Models}\n\n\\paragraph{Benchmarks.} GlobalMMLU (primary, 20~languages), Belebele (reading comprehension), MMLU-ProX (translated MMLU). GlobalMMLU test split is partitioned into probe\\_train (70\\%) and eval (30\\%) via stratified split.\n\n\\paragraph{Models.} Qwen3-235B-A22B (94~layers, MoE, INT4), Llama~4 Scout (48~layers, MoE, W4A16), Gemma~4 31B (60~layers, Dense, BF16). Quantization validated in Section~\\ref{sec:quantization}.\n\n\\paragraph{Languages.} 20~languages across 4~tiers: HIGH (zh, es, fr, de, pt, ja), MID (ar, ru, ko, hi, vi, tr, id), LOW (sw, bn, te, pl, nl, uk, yo).\n\n% ============================================================\n% 4. EXPERIMENTS\n% ============================================================\n\\section{Experiments}\n\n\\subsection{Pareto Frontier Across Architectures}\n\\label{sec:pareto}\n\nWe probe every 4th layer across all three architectures, computing English \\aur{} and zero-shot transfer \\aur{} for 20~languages.\n\n\\paragraph{Qwen3-235B.} English-optimal layer is L80 (85\\% depth, \\aur{}=0.81). Zero-shot transfer at this layer averages 0.668 across 20~languages, with a clear resource-tier gradient (HIGH: 0.728, MID: 0.678, LOW: 0.582). Per-language Spearman $\\rho$ between depth and transfer \\aur{} reveals architecture-dependent Pareto structure: 9/20~languages show significant negative $\\rho$ ($p<0.05$), 5~trending ($p<0.10$), and 6~non-significant or positive. The transfer-optimal layer is L68 (72\\% depth), 2.5~pp below the English-optimal layer.\n\n\\paragraph{Llama 4 Scout.} English-optimal at L44 (92\\% depth, \\aur{}=0.77). The Pareto tradeoff is weaker: only 5/20~languages show significant negative $\\rho$ (median $\\rho = -0.25$ versus Qwen3's $-0.38$). The transfer-optimal layer is L36 (75\\% depth), with a smaller EN--transfer gap of 1.5~pp.\n\n\\paragraph{Gemma 4 31B (Dense).} English-optimal at L52 (87\\% depth, \\aur{}=0.79). As the dense architecture control, Gemma~4 shows intermediate Pareto strength: 7/20~languages with significant negative $\\rho$ (median $-0.32$). This confirms the Pareto tradeoff is not a MoE artifact.\n\nTable~\\ref{tab:arch_comparison} summarizes the three-architecture comparison.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Qwen3} & \\textbf{Llama4} & \\textbf{Gemma4} \\\\\n & \\textbf{(MoE)} & \\textbf{(MoE)} & \\textbf{(Dense)} \\\\\n\\midrule\nLayers & 94 & 48 & 60 \\\\\nActive params & 22B & 17B & 31B \\\\\nEN best \\aur{} & 0.81 & 0.77 & 0.79 \\\\\nMean ZS \\aur{} & 0.668 & 0.648 & 0.660 \\\\\nPareto sig. (/20) & 9 & 5 & 7 \\\\\nMedian Pareto $\\rho$ & $-0.38$ & $-0.25$ & $-0.32$ \\\\\n\\cka{} cliff slope & $-0.022$ & $-0.013$ & $-0.014$ \\\\\nEN--transfer gap & 2.5 pp & 1.5 pp & 1.8 pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Architecture comparison on Pareto frontier strength. Pareto sig.\\ = number of languages with significant negative depth--transfer Spearman $\\rho$ ($p<0.05$).}\n\\label{tab:arch_comparison}\n\\end{table}\n\n\\paragraph{Per-language patterns.}\nTable~\\ref{tab:per_lang} shows detailed per-language statistics for Qwen3-235B. Languages with high training-data representation (zh, es, fr) show clear Pareto tradeoffs, while ar and ko show no tradeoff or positive depth effects. The pattern is consistent with MoE routing creating language-specific expert subsets at depth.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccl}\n\\toprule\n\\textbf{Tier} & \\textbf{Lang} & \\textbf{ZS} & \\textbf{Best} & \\textbf{$\\rho$} & \\textbf{Pattern} \\\\\n\\midrule\nHIGH & zh & .738 & L68 & $-$0.48* & Tradeoff \\\\\nHIGH & es & .745 & L72 & $-$0.44* & Tradeoff \\\\\nHIGH & fr & .740 & L72 & $-$0.42* & Tradeoff \\\\\nHIGH & de & .725 & L64 & $-$0.51* & Tradeoff \\\\\nHIGH & ja & .710 & L64 & $-$0.55* & Tradeoff \\\\\n\\midrule\nMID & ru & .705 & L68 & $-$0.46* & Tradeoff \\\\\nMID & id & .690 & L68 & $-$0.43* & Tradeoff \\\\\nMID & ar & .695 & L72 & $-$0.22 & Weak \\\\\nMID & ko & .688 & L68 & $+$0.08 & None \\\\\n\\midrule\nLOW & pl & .698 & L68 & $-$0.45* & Tradeoff \\\\\nLOW & nl & .720 & L68 & $-$0.47* & Tradeoff \\\\\nLOW & yo & .535 & L44 & $+$0.12 & None \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Selected per-language results for Qwen3-235B (EN-optimal L80). ZS = zero-shot \\aur{} at EN-optimal layer. * denotes $p<0.05$.}\n\\label{tab:per_lang}\n\\end{table}\n\n\\paragraph{Divergent languages across architectures.}\nSeveral languages exhibit divergent Pareto patterns between Qwen3 and Llama~4: ar shows weak negative $\\rho$ on Qwen3 ($-0.22$, $p=0.30$) but positive on Llama~4 ($+0.18$, $p=0.58$); vi shows trending negative on Qwen3 ($-0.38$, $p=0.07$) but positive on Llama~4 ($+0.15$, $p=0.64$). These divergences likely reflect differences in training data composition and tokenizer coverage, though with $n=2$ architectures, causal attribution is not possible.\n\n\\subsection{CKA Geometry and Simpson's Paradox}\n\\label{sec:cka}\n\nLinear \\cka{} between English and target-language representations declines with depth across all three architectures, but with different profiles: Qwen3 shows a plateau-then-cliff pattern (CKA stable at ${\\sim}0.80$ through 68\\% depth, then dropping to 0.09 at the final layer), while Llama~4 and Gemma~4 show more gradual linear decline.\n\n\\paragraph{Simpson's Paradox.}\nThe raw Spearman correlation between \\cka{} and transfer \\aur{} is significantly \\emph{negative} across all architectures ($\\rho = -0.24$ to $-0.30$, all $p < 0.001$): languages with higher \\cka{} appear to transfer worse. However, this is a depth confound---deeper layers simultaneously decrease \\cka{} and increase English \\aur{}, creating a spurious negative correlation. Controlling for depth via partial correlation reverses the sign (Table~\\ref{tab:simpson}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Arch.} & \\textbf{Raw $\\rho$} & \\textbf{Partial $\\rho$} & \\textbf{$p$} & \\textbf{Sig.?} \\\\\n\\midrule\nQwen3-235B & $-$0.24 & $+$0.16 & .072 & No \\\\\nLlama4 Scout & $-$0.30 & $+$0.31 & .012 & Yes \\\\\nGemma4 31B & $-$0.26 & $+$0.24 & .038 & Yes \\\\\n\\midrule\n\\emph{Pilot Llama8B} & $-$0.16 & $+$0.41 & .006 & Yes \\\\\n\\emph{Pilot Qwen7B} & $-$0.16 & $+$0.18 & .274 & No \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Simpson's Paradox: raw vs.\\ partial Spearman $\\rho$ between \\cka{} and transfer \\aur{}, controlling for layer depth. Partial correlation is positive in all cases, significant in 2/3 full-scale architectures.}\n\\label{tab:simpson}\n\\end{table}\n\nIn architectures with near-linear \\cka{} depth gradients (Llama~4, Gemma~4), the partial correlation is significant ($\\rho=0.24{-}0.31$, $p<0.05$), confirming that \\cka{} provides genuine explanatory power beyond depth. In Qwen3-235B, the step-function-like \\cka{} profile limits linear partial correlation effectiveness ($\\rho=0.16$, $p=0.072$); within-layer analysis confirms the positive direction (17/24 layers with positive $\\rho$).\n\n\\paragraph{Subspace angle analysis.}\nWe measure the angle between English and target-language correctness directions (Table~\\ref{tab:subspace}). HIGH-resource languages show near-alignment ($10{-}13^\\circ$), while LOW-resource languages show substantial misalignment ($41{-}46^\\circ$). This provides the geometric basis for why zero-shot transfer works for high-resource but fails for low-resource languages.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Tier} & \\textbf{Qwen3} & \\textbf{Llama4} & \\textbf{Gemma4} & \\textbf{ZS \\aur{}} \\\\\n\\midrule\nHIGH & $11^\\circ$ & $13^\\circ$ & $11^\\circ$ & 0.72 \\\\\nMID  & $22^\\circ$ & $26^\\circ$ & $24^\\circ$ & 0.66 \\\\\nLOW  & $46^\\circ$ & $41^\\circ$ & $43^\\circ$ & 0.57 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Mean subspace angle between English and target-language correctness directions by resource tier. Larger angles correspond to worse zero-shot transfer.}\n\\label{tab:subspace}\n\\end{table}\n\n\\subsection{CaCLR: A Systematic Negative Result}\n\\label{sec:caclr}\n\n\\caclr{} tests whether distributional matching can improve cross-lingual transfer. We sweep $\\beta \\in \\{0.001, 0.01, 0.1, 1.0\\}$ across 20~languages on Qwen3-235B (L68), with 3~seeds each.\n\n\\paragraph{$\\beta$ sweep.} Table~\\ref{tab:beta_sweep} shows the consistency loss is inert: the best configuration ($\\beta=0.01$) achieves +0.3~pp over zero-shot ($p=0.38$, Cohen's $d=0.06$). At $\\beta=1.0$, the loss begins to degrade performance ($-0.7$~pp). All bootstrap 95\\% CIs cross zero.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n$\\beta$ & \\textbf{Mean \\aur{}} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} & \\textbf{$d$} \\\\\n\\midrule\n0 (ZS) & 0.668 & --- & --- & --- \\\\\n0.001 & 0.669 & +0.1 & [$-$0.5, +0.7] & 0.02 \\\\\n0.01 & 0.671 & +0.3 & [$-$0.4, +1.0] & 0.06 \\\\\n0.1 & 0.667 & $-$0.1 & [$-$0.8, +0.6] & 0.03 \\\\\n1.0 & 0.661 & $-$0.7 & [$-$1.4, +0.0] & 0.15 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{$\\beta$ sweep for \\caclr{} (Qwen3-235B, L68, mean over 20~languages, 3~seeds). All effects are negligible.}\n\\label{tab:beta_sweep}\n\\end{table}\n\n\\paragraph{Distributional matching ablation.} Table~\\ref{tab:dist_matching} extends the failure beyond MMD. CORAL (second-order alignment) and high-dimensional MMD (PCA $d=50, 100$) on activation space are equally inert. The failure is not MMD-specific---it reflects a fundamental limitation of distributional matching for this problem class.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{\\aur{}} & \\textbf{$\\Delta$ (pp)} & \\textbf{$p$} \\\\\n\\midrule\nZero-shot & 0.668 & --- & --- \\\\\nMMD (1-D logit) & 0.671 & +0.3 & .38 \\\\\nMMD (PCA $d{=}50$) & 0.673 & +0.5 & .28 \\\\\nMMD (PCA $d{=}100$) & 0.670 & +0.2 & .51 \\\\\nCORAL (1-D logit) & 0.672 & +0.4 & .32 \\\\\nCORAL (PCA $d{=}50$) & 0.671 & +0.3 & .40 \\\\\n\\midrule\nLinear projection & \\textbf{0.698} & \\textbf{+3.0} & $<$.001 \\\\\nFew-shot 100 & \\textbf{0.718} & \\textbf{+5.0} & $<$.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Distributional matching ablation. All marginal-matching methods are inert; linear projection and few-shot, which directly address subspace rotation, succeed.}\n\\label{tab:dist_matching}\n\\end{table}\n\n\\paragraph{Geometric explanation.}\n\\cka{} subspace analysis (Table~\\ref{tab:why_fails}) reveals the mechanism: \\caclr{} successfully reduces MMD distance (marginal alignment) but leaves the correctness subspace angle essentially unchanged. MMD matches marginal distributions but cannot detect or correct the directional rotation of the correctness subspace between languages. Linear projection succeeds precisely because it directly learns this rotation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Tier} & \\textbf{Angle} & \\textbf{MMD} & \\textbf{MMD} & \\textbf{Angle} \\\\\n & \\textbf{before} & \\textbf{before} & \\textbf{after} & \\textbf{after} \\\\\n\\midrule\nHIGH & $11^\\circ$ & 0.018 & 0.008 & $10.5^\\circ$ \\\\\nMID  & $23^\\circ$ & 0.042 & 0.018 & $22^\\circ$ \\\\\nLOW  & $44^\\circ$ & 0.105 & 0.048 & $42^\\circ$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Why distributional matching fails: \\caclr{} reduces MMD distance but correctness subspace angle is unchanged. The conditional structure differs across languages; marginal matching cannot fix conditional mismatch \\cite{zhao2019learning}.}\n\\label{tab:why_fails}\n\\end{table}\n\n\\paragraph{Component ablation.}\nAblating $\\mathcal{L}_{\\text{SB-ECE}}$ ($\\alpha$ sweep): increasing $\\alpha$ reduces \\ece{} ($-1.8$~pp at $\\alpha=1.0$) but degrades \\aur{} ($-0.5$~pp). BCE alone (\\aur{}=0.668, \\ece{}=0.19) versus full \\caclr{} (\\aur{}=0.669, \\ece{}=0.174)---the calibration component helps marginally, but the consistency component does not.\n\n\\subsection{Transfer Method Comparison}\n\\label{sec:transfer}\n\nTable~\\ref{tab:transfer_comparison} presents the full transfer method comparison on Qwen3-235B at the transfer-optimal layer (L68).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{\\aur{}} & \\textbf{$\\Delta$} & \\textbf{$p$} & \\textbf{Req.} \\\\\n\\midrule\nZero-shot & .668 & --- & --- & 0 \\\\\nMean-shift & .668 & 0.0 & n/a & 0 \\\\\n\\caclr{} ($\\beta{=}0.01$) & .671 & +0.3 & .38 & ${\\sim}$10K par. \\\\\nLinear proj.\\ (50) & .684 & +1.6 & .012 & 50 pairs \\\\\nLinear proj.\\ (200) & .698 & +3.0 & $<$.001 & 200 pairs \\\\\nFew-shot 25 & .685 & +1.7 & .008 & 25 labels \\\\\nFew-shot 100 & .718 & +5.0 & $<$.001 & 100 labels \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Transfer method comparison (Qwen3-235B, L68, mean over 20~languages). Linear projection is the best label-free method; few-shot with 100~labels achieves the highest absolute performance.}\n\\label{tab:transfer_comparison}\n\\end{table}\n\nMean-shift is mathematically inert ($\\Delta$\\aur{} $\\equiv 0$ under StandardScaler + LR, since adding a constant to all logits preserves ranks). \\caclr{} is statistically indistinguishable from zero-shot. Linear projection with 200~pairs achieves +3.0~pp ($p<0.001$), and few-shot with 100~labels achieves +5.0~pp ($p<0.001$).\n\n\\subsection{Linear Projection: Sample Efficiency and Effect Reversal}\n\\label{sec:projection}\n\n\\paragraph{Saturation curves.}\nWe vary the number of parallel pairs from 10 to 200 (Table~\\ref{tab:saturation}). Overall, 80~pairs achieves 95\\% of maximum improvement. Resource-tier stratification is clear: HIGH languages saturate at ${\\sim}38$~pairs (subspace angle ${\\sim}11^\\circ$), while LOW languages require ${\\sim}95$~pairs (angle ${\\sim}43^\\circ$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Pairs} & \\textbf{HIGH} & \\textbf{MID} & \\textbf{LOW} & \\textbf{Overall} \\\\\n\\midrule\n10  & +0.1 & +0.8 & +2.5 & +1.1 \\\\\n20  & +0.3 & +1.5 & +3.8 & +1.7 \\\\\n50  & +0.4 & +2.3 & +5.2 & +2.5 \\\\\n100 & +0.5 & +2.6 & +5.8 & +2.9 \\\\\n200 & +0.5 & +2.7 & +6.2 & +3.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Linear projection $\\Delta$\\aur{} (pp) by resource tier and parallel pair count (Qwen3-235B, L68). LOW-resource languages benefit most.}\n\\label{tab:saturation}\n\\end{table}\n\n\\paragraph{Procrustes effect reversal.}\nLinear projection does not uniformly help. Table~\\ref{tab:reversal} shows that languages with zero-shot \\aur{} $> 0.65$ are \\emph{harmed} by projection ($-1.5$~pp mean), while those with \\aur{} $< 0.50$ benefit substantially (+5.5~pp). The reversal threshold is ${\\sim}0.57$ (95\\% CI: $[0.48, 0.64]$). When the correctness direction is already near-aligned ($< 15^\\circ$), the estimation noise in the Procrustes rotation exceeds the alignment gain.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccl}\n\\toprule\n\\textbf{ZS \\aur{} band} & \\textbf{$n$} & \\textbf{Mean $\\Delta$} & \\textbf{Example} \\\\\n\\midrule\n$< 0.50$ & 3 & +5.5 pp & am, yo, te \\\\\n$0.50{-}0.58$ & 3 & +3.2 pp & sw, bn, tr \\\\\n$0.58{-}0.62$ & 2 & +1.2 pp & hi, vi \\\\\n$0.62{-}0.67$ & 4 & +0.2 pp & ar, ko, id, uk \\\\\n$0.67{-}0.72$ & 4 & $-$0.8 pp & ru, ja, de, pt \\\\\n$> 0.72$ & 4 & $-$1.8 pp & zh, es, fr, nl \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Procrustes effect reversal: linear projection helps low-ZS languages but harms high-ZS ones. Deployment recommendation: use projection when ZS \\aur{} $< 0.57$, skip for $> 0.65$.}\n\\label{tab:reversal}\n\\end{table}\n\n\\subsection{Difficulty Decomposition}\n\\label{sec:decomposition}\n\nWe test whether cross-lingual transfer decomposes into difficulty-shared and capability-specific components. IRT difficulty probes ($R^2 = 0.32$) extract a difficulty direction; projecting it out and retraining correctness probes yields the results in Table~\\ref{tab:decomp}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Tier} & \\textbf{Lang} & \\textbf{Full} & \\textbf{Diff-proj} & \\textbf{$\\Delta$} & \\textbf{Rand $\\Delta$} \\\\\n\\midrule\nHIGH & zh & .738 & .746 & +0.8 & +0.4 \\\\\nHIGH & es & .745 & .757 & +1.2 & +0.6 \\\\\nHIGH & de & .725 & .743 & +1.8* & +0.8 \\\\\nMID  & hi & .670 & .698 & +2.8* & +0.8 \\\\\nMID  & ru & .705 & .727 & +2.2* & +0.8 \\\\\nMID  & tr & .660 & .685 & +2.5* & +0.8 \\\\\nMID  & ko & .688 & .682 & $-$0.6 & +0.3 \\\\\nLOW  & sw & .598 & .586 & $-$1.2 & +0.3 \\\\\nLOW  & bn & .612 & .647 & +3.5* & +0.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Difficulty decomposition results (Qwen3-235B, 8-layer mean). Diff-proj = after projecting out difficulty direction. Rand $\\Delta$ = random-direction control. * = $p<0.05$.}\n\\label{tab:decomp}\n\\end{table}\n\nProjecting out the difficulty direction generally improves transfer for mid-resource languages (+2--3~pp) but harms low-resource languages where difficulty and capability are more entangled. The mean effect (+1.8~pp) exceeds the random-direction control (+0.7~pp) by a factor of 2.6, confirming that ${\\sim}60\\%$ of the effect is difficulty-specific. However, prescriptive accuracy (predicting which strategy benefits a given language) is only 56\\%, barely above chance. We therefore present this as a \\textbf{descriptive} finding: the decomposition explains what transfer contains but does not reliably predict optimal strategy.\n\n\\subsection{Cross-Lingual Orthogonality}\n\\label{sec:orthogonality}\n\nThe correctness--confidence orthogonality discovered by \\citet{miao2026closing} for English ($\\cos < 0.04$) persists across languages. Mean cosine similarity is 0.04 overall, with 17/20~languages below 0.10 and 13/20 below 0.05. HIGH-resource languages closely replicate the English result (mean $\\cos = 0.026$), while LOW-resource languages show higher cosine (mean $0.075$), driven by three outliers (am: 0.148, yo: 0.122, te: 0.105). Probing controls (Section~\\ref{sec:controls}) confirm these outliers have low selectivity, indicating the elevated cosine is a noise artifact from weak directional signals rather than genuine alignment. The two architectures show no significant difference ($0.037$ vs $0.043$, $p=0.42$), indicating orthogonality is a structural property of the representation space.\n\n\\subsection{Probe Complexity Validation}\n\\label{sec:probe_complexity}\n\nWe compare logistic regression (LR) and 2-layer MLP probes to validate our methodological choice (Table~\\ref{tab:lr_mlp}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Q-LR} & \\textbf{Q-MLP} & \\textbf{L-LR} & \\textbf{L-MLP} \\\\\n\\midrule\nEN \\aur{} & .810 & .832 & .770 & .792 \\\\\nMean ZS \\aur{} & .668 & .638 & .648 & .622 \\\\\nTransfer gap & 14.2 & 19.4 & 12.2 & 17.0 \\\\\nZS pass rate & 75\\% & 55\\% & 70\\% & 50\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{LR vs MLP probe comparison (Q=Qwen3, L=Llama4). MLP overfits English-specific patterns, widening the transfer gap by ${\\sim}5$~pp.}\n\\label{tab:lr_mlp}\n\\end{table}\n\nMLP probes achieve +2.1~pp higher English \\aur{} by exploiting English-specific activation patterns, but these do not transfer: the cross-lingual gap widens from ${\\sim}13$~pp (LR) to ${\\sim}18$~pp (MLP). LR's single-hyperplane constraint forces it to learn language-agnostic features, making it the correct choice for cross-lingual transfer.\n\n\\subsection{Cross-Benchmark Generalization}\n\\label{sec:benchmarks}\n\nTable~\\ref{tab:cross_bench} validates our findings on Belebele (reading comprehension) and MMLU-ProX (translated MMLU).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{GlobalMMLU} & \\textbf{Belebele} & \\textbf{MMLU-ProX} \\\\\n\\midrule\nEN \\aur{} & 0.81 & 0.75 & 0.79 \\\\\nMean ZS \\aur{} & 0.668 & 0.632 & 0.658 \\\\\nZS pass rate & 75\\% & 60\\% & 72\\% \\\\\nPareto sig. & 9 & 6 & 8 \\\\\nLin.\\ proj.\\ $\\Delta$ & +3.0 & +2.5 & +2.8 \\\\\n\\caclr{} $\\Delta$ & +0.3 & +0.2 & +0.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-benchmark consistency (Qwen3-235B). All qualitative findings generalize. Cross-benchmark language ranking $\\rho = 0.89$.}\n\\label{tab:cross_bench}\n\\end{table}\n\nBelebele shows weaker Pareto (6~vs 9 significant languages) as expected for passage-dependent correctness, but the Pareto structure is preserved. \\caclr{} remains inert on both benchmarks. Linear projection remains effective. Cross-benchmark language ranking correlation is $\\rho = 0.89$, confirming results are not benchmark-specific.\n\n\\subsection{Probing Controls}\n\\label{sec:controls}\n\nFollowing \\citet{hewitt2019designing}, we train control probes on all 20~languages $\\times$ 3~architectures $\\times$ all probed layers. Table~\\ref{tab:controls} shows the artifact rate by resource tier and depth.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Depth} & \\textbf{HIGH} & \\textbf{MID} & \\textbf{LOW} & \\textbf{All} \\\\\n\\midrule\n0--25\\%  & 15\\% & 55\\% & 80\\% & 50\\% \\\\\n25--50\\% & 3\\% & 28\\% & 55\\% & 29\\% \\\\\n50--75\\% & 0\\% & 10\\% & 18\\% & 9\\% \\\\\n75--100\\% & 0\\% & 2\\% & 5\\% & 2\\% \\\\\n\\midrule\nOverall & 5\\% & 22\\% & 35\\% & 22\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Artifact rate (selectivity $< 0.05$) by resource tier and depth zone, averaged across 3~architectures. Low-resource shallow layers are predominantly artifacts.}\n\\label{tab:controls}\n\\end{table}\n\nOverall, 22\\% of language--layer combinations have selectivity $< 0.05$, concentrated in LOW-resource shallow layers (80\\% artifact rate at 0--25\\% depth). At the English-optimal depth, only am, yo, and te fall below the selectivity threshold (selectivity 0.015--0.054). After filtering, all main results are confirmed unchanged. This finding has field-level implications: \\textbf{all cross-lingual probing studies should include selectivity checks}, especially for low-resource languages where probe capacity can mimic genuine signal.\n\n\\subsection{Quantization Validation}\n\\label{sec:quantization}\n\nWe validate that INT4/W4A16 quantization does not introduce artifacts by comparing against FP16 at 5~layers per model on a 5\\% data subset. All $|\\Delta\\text{AUROC}| < 0.015$ and all CKA(FP16, quant) $> 0.97$ (Table~\\ref{tab:quant}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccr}\n\\toprule\n\\textbf{Model} & \\textbf{Layer} & \\textbf{FP16} & \\textbf{Quant} & \\textbf{$\\Delta$} \\\\\n\\midrule\nLlama4 & L8 (17\\%) & .635 & .633 & $-$.002 \\\\\nLlama4 & L24 (50\\%) & .722 & .717 & $-$.005 \\\\\nLlama4 & L44 (92\\%) & .770 & .762 & $-$.008 \\\\\n\\midrule\nQwen3 & L16 (17\\%) & .632 & .627 & $-$.005 \\\\\nQwen3 & L52 (55\\%) & .742 & .739 & $-$.003 \\\\\nQwen3 & L80 (85\\%) & .810 & .798 & $-$.012 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Quantization validation (selected layers). Max $|\\Delta| = 0.012$; CKA $> 0.97$ throughout. Quantization artifacts are negligible.}\n\\label{tab:quant}\n\\end{table}\n\nThe largest delta ($-0.012$ at Qwen3 L80) occurs at the deepest probed layer of the MoE model, where expert routing decisions may shift slightly under INT4. All deltas remain within bootstrap confidence intervals, supporting the validity of our quantized experimental setup.\n\n\\subsection{Extended Language Coverage}\n\\label{sec:extended}\n\nWe extend from 20 to 52~languages using GlobalMMLU and Belebele's full language sets (Table~\\ref{tab:extended}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Tier} & \\textbf{$n_{20}$} & \\textbf{$n_{52}$} & \\textbf{ZS \\aur{}} & \\textbf{Art.\\%} & \\textbf{Pass} \\\\\n\\midrule\nHIGH & 6 & 10 & 0.72 & 5\\% & 100\\% \\\\\nMID & 8 & 15 & 0.66 & 20\\% & 87\\% \\\\\nLOW & 6 & 16 & 0.58 & 32\\% & 56\\% \\\\\nV-LOW & 0 & 11 & 0.53 & 45\\% & 27\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Language coverage expansion to 52 languages. Art.\\% = artifact rate. Pass = ZS \\aur{} $>$ 0.58. Core findings replicate (rank correlation 20 vs.\\ 52 = 0.95).}\n\\label{tab:extended}\n\\end{table}\n\nThe rank correlation between 20-language and 52-language results is $0.95$, confirming that our core analysis on 20~languages is representative. Very-low-resource languages ($< 1$M training tokens) show 45\\% artifact rates and near-chance performance, reinforcing the necessity of probing controls. Writing-system clusters emerge as a moderate predictor of transfer quality within resource tiers.\n\n% ============================================================\n% 5. DISCUSSION\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{Practical recommendations.}\nFor practitioners deploying multilingual calibration: (1)~select probe layer at 70--75\\% depth rather than the English-optimal layer; (2)~use zero-shot transfer for HIGH-resource languages (ZS \\aur{} $> 0.65$); (3)~apply linear projection with ${\\sim}80$ parallel pairs for languages with ZS \\aur{} $< 0.57$; (4)~for the ambiguous zone ($0.57{-}0.65$), validate on a small held-out set.\n\n\\paragraph{Why distributional matching fails.}\nThe \\caclr{} negative result is grounded in the theoretical analysis of \\citet{zhao2019learning}: when $P(\\text{correct} \\mid \\mathbf{h})$ differs across languages (the capability-specific component), marginal distribution matching cannot recover the conditional structure. Our \\cka{} analysis provides empirical confirmation---MMD successfully reduces marginal distance while leaving the correctness subspace angle unchanged. Linear projection succeeds because it directly learns the subspace rotation without assuming distributional equivalence.\n\n\\paragraph{Limitations.}\nOur study is limited to MCQA benchmarks, which enable clean correctness labeling but may not generalize to open-ended generation. The three architectures differ simultaneously in type (MoE vs dense), scale, layer count, and training data; architectural effects cannot be isolated ($n=3$). Simpson's Paradox significance depends on the \\cka{} depth profile shape, limiting its universality as a diagnostic. Probing controls flag 22\\% of language--layer combinations as artifacts, and we cannot rule out subtler capacity effects below our selectivity threshold.\n\n% ============================================================\n% 6. CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe present the first large-scale study of cross-lingual correctness probe transfer across three architectures and 20~languages. The depth--transferability Pareto tradeoff is architecture-dependent, with \\cka{} geometry providing explanatory power via a Simpson's Paradox that reverses the apparent negative CKA--transfer relationship. Distributional matching (\\caclr{}, CORAL, high-dimensional MMD) uniformly fails---a systematic negative result explained by the inability of marginal matching to correct directional misalignment in the correctness subspace. Linear projection with ${\\sim}80$~parallel pairs is the most effective label-free solution, particularly for low-resource languages, though it should be skipped when zero-shot transfer already works well. Our probing controls reveal that 22\\% of cross-lingual probing results are capacity artifacts, a finding with implications for the broader field. Together, these results validate that probe-based calibration extends to multilingual settings, while identifying when and why it succeeds or fails.\n\n% ============================================================\n% REFERENCES\n% ============================================================\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{30}\n\n\\bibitem[\\protect\\citename{Angelopoulos and Bates}2023]{angelopoulos2023conformal}\nAnastasios~N. Angelopoulos and Stephen Bates. 2023.\n\\newblock Conformal prediction: A gentle introduction.\n\\newblock {\\em Foundations and Trends in Machine Learning}, 16(4):494--591.\n\n\\bibitem[\\protect\\citename{Artetxe et~al.}2018]{artetxe2018robust}\nMikel Artetxe, Gorka Labaka, and Eneko Agirre. 2018.\n\\newblock A robust self-learning method for fully unsupervised cross-lingual mappings of word embeddings.\n\\newblock In {\\em Proceedings of ACL}.\n\n\\bibitem[\\protect\\citename{Ben-David et~al.}2010]{bendavid2010theory}\nShai Ben-David, John Blitzer, Koby Crammer, Alex Kulesza, Fernando Pereira, and Jennifer~Wortman Vaughan. 2010.\n\\newblock A theory of learning from different domains.\n\\newblock {\\em Machine Learning}, 79:151--175.\n\n\\bibitem[\\protect\\citename{Civelli et~al.}2026]{civelli2026shared}\nMatteo Civelli, Tommaso Melis, and others. 2026.\n\\newblock Shared and language-specific difficulty representations across languages.\n\\newblock In {\\em Proceedings of ACL}.\n\n\\bibitem[\\protect\\citename{Confidence Manifold}2026]{confidence_manifold2026}\nAnonymous. 2026.\n\\newblock The confidence manifold: Internal geometry of LLM calibration.\n\\newblock Preprint.\n\n\\bibitem[\\protect\\citename{Conneau et~al.}2018]{conneau2018word}\nAlexis Conneau, Guillaume Lample, Marc'Aurelio Ranzato, Ludovic Denoyer, and Herv\\'{e} J\\'{e}gou. 2018.\n\\newblock Word translation without parallel data.\n\\newblock In {\\em Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Hewitt and Liang}2019]{hewitt2019designing}\nJohn Hewitt and Percy Liang. 2019.\n\\newblock Designing and interpreting probes with control tasks.\n\\newblock In {\\em Proceedings of EMNLP}.\n\n\\bibitem[\\protect\\citename{Ji et~al.}2025]{ji2025calibrating}\nZiwei Ji and others. 2025.\n\\newblock Calibrating language models via internal representations.\n\\newblock In {\\em Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Joshi et~al.}2025]{joshi2025calibration}\nPratik Joshi and others. 2025.\n\\newblock Calibration directions in the residual stream.\n\\newblock In {\\em Proceedings of NeurIPS}.\n\n\\bibitem[\\protect\\citename{Kornblith et~al.}2019]{kornblith2019similarity}\nSimon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton. 2019.\n\\newblock Similarity of neural network representations revisited.\n\\newblock In {\\em Proceedings of ICML}.\n\n\\bibitem[\\protect\\citename{Miao et~al.}2026a]{miao2026coral}\nYifei Miao and others. 2026.\n\\newblock Cross-task correctness probing via SAE analysis.\n\\newblock In {\\em Proceedings of ACL}.\n\n\\bibitem[\\protect\\citename{Miao and Ungar}2026]{miao2026closing}\nYifei Miao and Lyle Ungar. 2026.\n\\newblock Closing the gap between correctness and confidence.\n\\newblock In {\\em Proceedings of NAACL}.\n\n\\bibitem[\\protect\\citename{Pires et~al.}2019]{pires2019multilingual}\nTelmo Pires, Eva Schlinger, and Dan Garrette. 2019.\n\\newblock How multilingual is multilingual {BERT}?\n\\newblock In {\\em Proceedings of ACL}.\n\n\\bibitem[\\protect\\citename{Ravisankar et~al.}2026]{ravisankar2026dali}\nAditya Ravisankar and others. 2026.\n\\newblock {DALI}: Cross-lingual representation alignment.\n\\newblock Preprint.\n\n\\bibitem[\\protect\\citename{Wu and Dredze}2019]{wu2019beto}\nShijie Wu and Mark Dredze. 2019.\n\\newblock Beto, bentz, becas: The surprising cross-lingual effectiveness of {BERT}.\n\\newblock In {\\em Proceedings of EMNLP}.\n\n\\bibitem[\\protect\\citename{Xiao et~al.}2025]{xiao2025knowledge}\nYuxia Xiao and others. 2025.\n\\newblock Cross-lingual knowledge boundary probing.\n\\newblock In {\\em Proceedings of ACL}.\n\n\\bibitem[\\protect\\citename{Zhao et~al.}2019]{zhao2019learning}\nHan Zhao, Remi~Tachet des Combes, Kun Zhang, and Geoffrey Gordon. 2019.\n\\newblock On learning invariant representations for domain adaptation.\n\\newblock In {\\em Proceedings of ICML}.\n\n\\bibitem[\\protect\\citename{Zhou et~al.}2025]{zhou2025lace}\nKaitlyn Zhou, Dan Jurafsky, and Tatsunori Hashimoto. 2025.\n\\newblock {LACE}: Language-agnostic calibration via layer ensemble.\n\\newblock In {\\em Proceedings of ACL}.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ff092ae-8a0f-478f-a371-d7df87347fef",
  "isSidechain": false,
  "requestId": "req_011CbFoJHnvDPFNh2zH32B1R",
  "type": "assistant",
  "uuid": "3960d394-bed1-4602-80b3-757e6e1535c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0178REvBLC8RPpxaFNST1rSr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 340,
      "cache_read_input_tokens": 55566,
      "output_tokens": 14638,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 340,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14638,
          "cache_read_input_tokens": 55566,
          "cache_creation_input_tokens": 340,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 340
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

_source line 26 · 2026-05-21T13:37:31.274Z_

<details><summary>↩ Tool result · `toolu_015cLLLkynD6iTze8fsjVJC8`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3960d394-bed1-4602-80b3-757e6e1535c6",
  "isSidechain": false,
  "promptId": "e8f1a248-e970-4548-96f9-5cd439647eab",
  "type": "user",
  "uuid": "a822bfd0-2ba4-4d55-9ebf-b02a219c7a49",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{microtype}\n\n\\newcommand{\\aur}{\\textsc{auroc}}\n\\newcommand{\\ece}{\\textsc{ece}}\n\\newcommand{\\zs}{\\textsc{zs}}\n\\newcommand{\\caclr}{\\textsc{CaCLR}}\n\\newcommand{\\cka}{\\textsc{CKA}}\n\n\\title{Cross-Lingual Correctness Probe Transfer Reveals Architecture-Dependent Depth Effects:\\\\ Distributional Matching Fails but Linear Projection Succeeds}\n\n\\author{\n  Anonymous \\\\\n  \\texttt{anonymous@example.com}\n}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nProbe-based calibration methods extract internal correctness directions from LLM hidden states, achieving strong results in English. Whether these directions transfer cross-lingually remains untested at scale. We present the first large-scale study of correctness probe transfer across three architectures (Qwen3-235B MoE, Llama~4 Scout MoE, Gemma~4 31B Dense) and 20~languages spanning four resource tiers. We find: (1)~a depth--transferability Pareto tradeoff that is architecture-dependent---9/20 languages show significant negative depth--transfer correlation on Qwen3 versus 5/20 on Llama~4; (2)~\\cka{} analysis reveals a Simpson's Paradox where raw CKA--transfer correlation is negative but partial correlation controlling for depth is significantly positive in 2/3~architectures; (3)~distributional matching via \\caclr{} (MMD-based consistency loss) is inert across a full $\\beta$ sweep, with CORAL and high-dimensional MMD variants also failing---geometric analysis shows these methods reduce marginal distance but leave the correctness subspace angle unchanged; (4)~linear projection with ${\\sim}80$~parallel pairs achieves 95\\% of maximum improvement and is the most effective label-free transfer method, particularly for low-resource languages (+5--6~pp). We release probing controls showing 22\\% of language--layer combinations contain capacity artifacts, concentrated in low-resource shallow layers---a methodological warning for the field.\n\\end{abstract}\n\n% ============================================================\n% 1. INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nNon-English languages suffer substantially worse calibration in multilingual LLMs, with expected calibration error (\\ece{}) reaching 5$\\times$ that of English \\cite{zhou2025lace}. Recent work demonstrates that internal correctness directions---linear features in hidden-state space that predict answer correctness---enable effective probe-based calibration for English \\cite{miao2026coral,joshi2025calibration,confidence_manifold2026}. These correctness directions are orthogonal to verbalized confidence \\cite{miao2026closing}, occupy a low-dimensional subspace \\cite{confidence_manifold2026}, and can be extracted with simple logistic regression \\cite{joshi2025calibration}. Yet no prior work systematically tests whether this research line extends beyond English.\n\nThe closest prior effort, \\citet{xiao2025knowledge}, transfers \\emph{knowledge-boundary} probes (input-level answerability) across 8~languages, finding partial success with mean-shift alignment. However, knowledge-boundary and correctness probes target fundamentally different signals: answerability is input-dependent and binary, while correctness depends on the model's actual output and varies with question difficulty. \\citet{civelli2026shared} show that cross-lingual and monolingual optimal layers diverge, but do not study correctness probing or calibration. The intersection of cross-lingual transfer, correctness directions, and calibration remains open.\n\nWe present the first large-scale study of cross-lingual correctness probe transfer, spanning three architectures (Qwen3-235B, Llama~4 Scout, Gemma~4 31B), 20~languages across four resource tiers, and multiple transfer methods. Our core finding is that \\textbf{deeper layers generally improve both English discrimination and cross-lingual transfer, but the deepest layers exhibit a local Pareto tradeoff where marginal English gains trade against transfer quality}---and the shape of this tradeoff is architecture-dependent. A Simpson's Paradox in the \\cka{}--transfer relationship provides geometric insight: raw correlation is negative (depth confound), but within each layer, higher cross-lingual \\cka{} predicts better transfer.\n\nOur contributions are: (1)~discovery of the architecture-dependent Pareto frontier across 3~architectures and 20~languages; (2)~a systematic negative result showing that distributional matching (MMD, CORAL, high-dimensional variants) fails for correctness probe transfer, with geometric explanation via \\cka{} subspace analysis; (3)~characterization of linear projection as the practical label-free solution, with resource-tier-stratified saturation at ${\\sim}80$~parallel pairs; (4)~first application of probing controls \\cite{hewitt2019designing} to cross-lingual transfer, revealing that 22\\% of language--layer combinations are capacity artifacts.\n\n% ============================================================\n% 2. RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Probe-based calibration.}\n\\citet{joshi2025calibration} extract calibration directions from residual streams, finding strong within-model transfer across datasets but failure across models. \\citet{miao2026coral} discover distributed correctness representations via SAE analysis and propose cross-task steering. \\citet{miao2026closing} show correctness and verbalized confidence directions are orthogonal ($\\cos < 0.04$), motivating probe-based over output-based calibration. \\citet{confidence_manifold2026} demonstrate that correctness occupies a 3--8D subspace accessible to linear probes. All are English-only.\n\n\\paragraph{Cross-lingual representations.}\nCross-lingual representations in multilingual LLMs exhibit linear structure amenable to projection-based alignment \\cite{conneau2018word,artetxe2018robust}. \\citet{pires2019multilingual} and \\citet{wu2019beto} establish that mBERT transfers cross-lingually via shared subspaces. \\citet{ravisankar2026dali} study cross-lingual representation alignment more broadly. Our linear projection is conceptually analogous to VecMap/MUSE applied at sentence-level correctness representations; the contribution is demonstrating effectiveness for correctness probing and characterizing sample efficiency.\n\n\\paragraph{Multilingual calibration.}\n\\citet{zhou2025lace} propose per-language layer ensembles (LACE), reducing non-English \\ece{} from 22\\% to 3\\%, but require per-language labeled data. \\citet{xiao2025knowledge} transfer knowledge-boundary probes across 8~languages using mean-shift. We target a different signal (correctness), a different metric (calibration), more languages (20+), and analyze the Pareto frontier.\n\n\\paragraph{Domain adaptation theory.}\n\\citet{bendavid2010theory} provide the H-divergence framework predicting that representation alignment aids transfer. \\citet{zhao2019learning} show that marginal distribution matching fails when conditional distributions differ---directly grounding our \\caclr{} negative result.\n\n\\paragraph{Probing methodology.}\nWe follow \\citet{hewitt2019designing}'s control-task framework to validate that probe \\aur{} reflects genuine correctness directions rather than capacity artifacts.\n\n% ============================================================\n% 3. METHOD\n% ============================================================\n\\section{Method}\n\n\\subsection{Correctness Probes}\n\nGiven a multilingual LLM and a multiple-choice question $q$ with model answer $a$, we extract the hidden-state representation $\\mathbf{h}_l \\in \\mathbb{R}^d$ at layer $l$ corresponding to the last token position. A linear probe $f_l(\\mathbf{h}) = \\sigma(\\mathbf{w}_l^\\top \\mathbf{h} + b_l)$ is trained on English data to predict binary correctness ($y = \\mathbb{1}[a = a^*]$). We use logistic regression (LR) trained with binary cross-entropy, validated by comparison with 2-layer MLP probes (Section~\\ref{sec:probe_complexity}).\n\n\\subsection{Transfer Methods}\n\nWe evaluate five transfer strategies for applying English-trained probes to target language $t$:\n\n\\paragraph{Zero-shot (\\zs{}).} Apply the English probe directly: $\\hat{p}_t = f_l(\\mathbf{h}_l^t)$.\n\n\\paragraph{Mean-shift.} Shift target representations by the mean difference: $\\hat{p}_t = f_l(\\mathbf{h}_l^t + \\boldsymbol{\\mu}^{\\text{en}} - \\boldsymbol{\\mu}^t)$. Under StandardScaler + logistic regression, this adds a constant offset to all logits; since \\aur{} is rank-invariant, $\\Delta$\\aur{} $\\equiv 0$ mathematically.\n\n\\paragraph{\\caclr{}.} We train the probe with a composite loss:\n\\begin{equation}\n\\mathcal{L} = \\mathcal{L}_{\\text{BCE}} + \\alpha \\cdot \\mathcal{L}_{\\text{SB-ECE}} + \\beta \\cdot \\mathcal{L}_{\\text{MMD}}\n\\end{equation}\nwhere $\\mathcal{L}_{\\text{MMD}}$ uses a Gaussian RBF kernel with median-heuristic bandwidth, computed on 1-D probe logits from English and target-language parallel inputs (GlobalMMLU items). This tests whether distributional matching can improve transfer. Implementation: Adam optimizer (lr=$5{\\times}10^{-4}$, cosine decay to $10^{-5}$), 50~epochs, early stopping (patience=10 on validation BCE), warm-started from the standard LR solution, batch size 256, 3~seeds.\n\n\\paragraph{Linear projection.} Learn a Procrustes rotation $\\mathbf{W}^* = \\arg\\min_{\\mathbf{W}^\\top\\mathbf{W}=\\mathbf{I}} \\|\\mathbf{W}\\mathbf{H}^t - \\mathbf{H}^{\\text{en}}\\|_F$ from $n$ parallel sentence pairs, then apply: $\\hat{p}_t = f_l(\\mathbf{W}^* \\mathbf{h}_l^t)$.\n\n\\paragraph{Few-shot.} Retrain the probe on $k$ target-language labeled examples ($k \\in \\{25, 100\\}$), requiring target-language correctness labels unlike the above methods.\n\n\\subsection{CKA Analysis}\n\nWe compute linear Centered Kernel Alignment \\cite{kornblith2019similarity} between English and target-language representations at each probed layer: $\\text{CKA}(\\mathbf{H}^{\\text{en}}_l, \\mathbf{H}^t_l)$. To disentangle the depth confound, we compute partial Spearman correlations between \\cka{} and transfer \\aur{} controlling for layer depth.\n\n\\subsection{Probing Controls}\n\nFollowing \\citet{hewitt2019designing}, we train control probes that predict random binary labels, measuring selectivity as $\\text{sel} = \\text{AUROC}_{\\text{real}} - \\text{AUROC}_{\\text{control}}$. Language--layer combinations with $\\text{sel} < 0.05$ are flagged as potential capacity artifacts.\n\n\\subsection{Data and Models}\n\n\\paragraph{Benchmarks.} GlobalMMLU (primary, 20~languages), Belebele (reading comprehension), MMLU-ProX (translated MMLU). GlobalMMLU test split is partitioned into probe\\_train (70\\%) and eval (30\\%) via stratified split.\n\n\\paragraph{Models.} Qwen3-235B-A22B (94~layers, MoE, INT4), Llama~4 Scout (48~layers, MoE, W4A16), Gemma~4 31B (60~layers, Dense, BF16). Quantization validated in Section~\\ref{sec:quantization}.\n\n\\paragraph{Languages.} 20~languages across 4~tiers: HIGH (zh, es, fr, de, pt, ja), MID (ar, ru, ko, hi, vi, tr, id), LOW (sw, bn, te, pl, nl, uk, yo).\n\n% ============================================================\n% 4. EXPERIMENTS\n% ============================================================\n\\section{Experiments}\n\n\\subsection{Pareto Frontier Across Architectures}\n\\label{sec:pareto}\n\nWe probe every 4th layer across all three architectures, computing English \\aur{} and zero-shot transfer \\aur{} for 20~languages.\n\n\\paragraph{Qwen3-235B.} English-optimal layer is L80 (85\\% depth, \\aur{}=0.81). Zero-shot transfer at this layer averages 0.668 across 20~languages, with a clear resource-tier gradient (HIGH: 0.728, MID: 0.678, LOW: 0.582). Per-language Spearman $\\rho$ between depth and transfer \\aur{} reveals architecture-dependent Pareto structure: 9/20~languages show significant negative $\\rho$ ($p<0.05$), 5~trending ($p<0.10$), and 6~non-significant or positive. The transfer-optimal layer is L68 (72\\% depth), 2.5~pp below the English-optimal layer.\n\n\\paragraph{Llama 4 Scout.} English-optimal at L44 (92\\% depth, \\aur{}=0.77). The Pareto tradeoff is weaker: only 5/20~languages show significant negative $\\rho$ (median $\\rho = -0.25$ versus Qwen3's $-0.38$). The transfer-optimal layer is L36 (75\\% depth), with a smaller EN--transfer gap of 1.5~pp.\n\n\\paragraph{Gemma 4 31B (Dense).} English-optimal at L52 (87\\% depth, \\aur{}=0.79). As the dense architecture control, Gemma~4 shows intermediate Pareto strength: 7/20~languages with significant negative $\\rho$ (median $-0.32$). This confirms the Pareto tradeoff is not a MoE artifact.\n\nTable~\\ref{tab:arch_comparison} summarizes the three-architecture comparison.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Qwen3} & \\textbf{Llama4} & \\textbf{Gemma4} \\\\\n & \\textbf{(MoE)} & \\textbf{(MoE)} & \\textbf{(Dense)} \\\\\n\\midrule\nLayers & 94 & 48 & 60 \\\\\nActive params & 22B & 17B & 31B \\\\\nEN best \\aur{} & 0.81 & 0.77 & 0.79 \\\\\nMean ZS \\aur{} & 0.668 & 0.648 & 0.660 \\\\\nPareto sig. (/20) & 9 & 5 & 7 \\\\\nMedian Pareto $\\rho$ & $-0.38$ & $-0.25$ & $-0.32$ \\\\\n\\cka{} cliff slope & $-0.022$ & $-0.013$ & $-0.014$ \\\\\nEN--transfer gap & 2.5 pp & 1.5 pp & 1.8 pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Architecture comparison on Pareto frontier strength. Pareto sig.\\ = number of languages with significant negative depth--transfer Spearman $\\rho$ ($p<0.05$).}\n\\label{tab:arch_comparison}\n\\end{table}\n\n\\paragraph{Per-language patterns.}\nTable~\\ref{tab:per_lang} shows detailed per-language statistics for Qwen3-235B. Languages with high training-data representation (zh, es, fr) show clear Pareto tradeoffs, while ar and ko show no tradeoff or positive depth effects. The pattern is consistent with MoE routing creating language-specific expert subsets at depth.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccl}\n\\toprule\n\\textbf{Tier} & \\textbf{Lang} & \\textbf{ZS} & \\textbf{Best} & \\textbf{$\\rho$} & \\textbf{Pattern} \\\\\n\\midrule\nHIGH & zh & .738 & L68 & $-$0.48* & Tradeoff \\\\\nHIGH & es & .745 & L72 & $-$0.44* & Tradeoff \\\\\nHIGH & fr & .740 & L72 & $-$0.42* & Tradeoff \\\\\nHIGH & de & .725 & L64 & $-$0.51* & Tradeoff \\\\\nHIGH & ja & .710 & L64 & $-$0.55* & Tradeoff \\\\\n\\midrule\nMID & ru & .705 & L68 & $-$0.46* & Tradeoff \\\\\nMID & id & .690 & L68 & $-$0.43* & Tradeoff \\\\\nMID & ar & .695 & L72 & $-$0.22 & Weak \\\\\nMID & ko & .688 & L68 & $+$0.08 & None \\\\\n\\midrule\nLOW & pl & .698 & L68 & $-$0.45* & Tradeoff \\\\\nLOW & nl & .720 & L68 & $-$0.47* & Tradeoff \\\\\nLOW & yo & .535 & L44 & $+$0.12 & None \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Selected per-language results for Qwen3-235B (EN-optimal L80). ZS = zero-shot \\aur{} at EN-optimal layer. * denotes $p<0.05$.}\n\\label{tab:per_lang}\n\\end{table}\n\n\\paragraph{Divergent languages across architectures.}\nSeveral languages exhibit divergent Pareto patterns between Qwen3 and Llama~4: ar shows weak negative $\\rho$ on Qwen3 ($-0.22$, $p=0.30$) but positive on Llama~4 ($+0.18$, $p=0.58$); vi shows trending negative on Qwen3 ($-0.38$, $p=0.07$) but positive on Llama~4 ($+0.15$, $p=0.64$). These divergences likely reflect differences in training data composition and tokenizer coverage, though with $n=2$ architectures, causal attribution is not possible.\n\n\\subsection{CKA Geometry and Simpson's Paradox}\n\\label{sec:cka}\n\nLinear \\cka{} between English and target-language representations declines with depth across all three architectures, but with different profiles: Qwen3 shows a plateau-then-cliff pattern (CKA stable at ${\\sim}0.80$ through 68\\% depth, then dropping to 0.09 at the final layer), while Llama~4 and Gemma~4 show more gradual linear decline.\n\n\\paragraph{Simpson's Paradox.}\nThe raw Spearman correlation between \\cka{} and transfer \\aur{} is significantly \\emph{negative} across all architectures ($\\rho = -0.24$ to $-0.30$, all $p < 0.001$): languages with higher \\cka{} appear to transfer worse. However, this is a depth confound---deeper layers simultaneously decrease \\cka{} and increase English \\aur{}, creating a spurious negative correlation. Controlling for depth via partial correlation reverses the sign (Table~\\ref{tab:simpson}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Arch.} & \\textbf{Raw $\\rho$} & \\textbf{Partial $\\rho$} & \\textbf{$p$} & \\textbf{Sig.?} \\\\\n\\midrule\nQwen3-235B & $-$0.24 & $+$0.16 & .072 & No \\\\\nLlama4 Scout & $-$0.30 & $+$0.31 & .012 & Yes \\\\\nGemma4 31B & $-$0.26 & $+$0.24 & .038 & Yes \\\\\n\\midrule\n\\emph{Pilot Llama8B} & $-$0.16 & $+$0.41 & .006 & Yes \\\\\n\\emph{Pilot Qwen7B} & $-$0.16 & $+$0.18 & .274 & No \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Simpson's Paradox: raw vs.\\ partial Spearman $\\rho$ between \\cka{} and transfer \\aur{}, controlling for layer depth. Partial correlation is positive in all cases, significant in 2/3 full-scale architectures.}\n\\label{tab:simpson}\n\\end{table}\n\nIn architectures with near-linear \\cka{} depth gradients (Llama~4, Gemma~4), the partial correlation is significant ($\\rho=0.24{-}0.31$, $p<0.05$), confirming that \\cka{} provides genuine explanatory power beyond depth. In Qwen3-235B, the step-function-like \\cka{} profile limits linear partial correlation effectiveness ($\\rho=0.16$, $p=0.072$); within-layer analysis confirms the positive direction (17/24 layers with positive $\\rho$).\n\n\\paragraph{Subspace angle analysis.}\nWe measure the angle between English and target-language correctness directions (Table~\\ref{tab:subspace}). HIGH-resource languages show near-alignment ($10{-}13^\\circ$), while LOW-resource languages show substantial misalignment ($41{-}46^\\circ$). This provides the geometric basis for why zero-shot transfer works for high-resource but fails for low-resource languages.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Tier} & \\textbf{Qwen3} & \\textbf{Llama4} & \\textbf{Gemma4} & \\textbf{ZS \\aur{}} \\\\\n\\midrule\nHIGH & $11^\\circ$ & $13^\\circ$ & $11^\\circ$ & 0.72 \\\\\nMID  & $22^\\circ$ & $26^\\circ$ & $24^\\circ$ & 0.66 \\\\\nLOW  & $46^\\circ$ & $41^\\circ$ & $43^\\circ$ & 0.57 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Mean subspace angle between English and target-language correctness directions by resource tier. Larger angles correspond to worse zero-shot transfer.}\n\\label{tab:subspace}\n\\end{table}\n\n\\subsection{CaCLR: A Systematic Negative Result}\n\\label{sec:caclr}\n\n\\caclr{} tests whether distributional matching can improve cross-lingual transfer. We sweep $\\beta \\in \\{0.001, 0.01, 0.1, 1.0\\}$ across 20~languages on Qwen3-235B (L68), with 3~seeds each.\n\n\\paragraph{$\\beta$ sweep.} Table~\\ref{tab:beta_sweep} shows the consistency loss is inert: the best configuration ($\\beta=0.01$) achieves +0.3~pp over zero-shot ($p=0.38$, Cohen's $d=0.06$). At $\\beta=1.0$, the loss begins to degrade performance ($-0.7$~pp). All bootstrap 95\\% CIs cross zero.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n$\\beta$ & \\textbf{Mean \\aur{}} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} & \\textbf{$d$} \\\\\n\\midrule\n0 (ZS) & 0.668 & --- & --- & --- \\\\\n0.001 & 0.669 & +0.1 & [$-$0.5, +0.7] & 0.02 \\\\\n0.01 & 0.671 & +0.3 & [$-$0.4, +1.0] & 0.06 \\\\\n0.1 & 0.667 & $-$0.1 & [$-$0.8, +0.6] & 0.03 \\\\\n1.0 & 0.661 & $-$0.7 & [$-$1.4, +0.0] & 0.15 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{$\\beta$ sweep for \\caclr{} (Qwen3-235B, L68, mean over 20~languages, 3~seeds). All effects are negligible.}\n\\label{tab:beta_sweep}\n\\end{table}\n\n\\paragraph{Distributional matching ablation.} Table~\\ref{tab:dist_matching} extends the failure beyond MMD. CORAL (second-order alignment) and high-dimensional MMD (PCA $d=50, 100$) on activation space are equally inert. The failure is not MMD-specific---it reflects a fundamental limitation of distributional matching for this problem class.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{\\aur{}} & \\textbf{$\\Delta$ (pp)} & \\textbf{$p$} \\\\\n\\midrule\nZero-shot & 0.668 & --- & --- \\\\\nMMD (1-D logit) & 0.671 & +0.3 & .38 \\\\\nMMD (PCA $d{=}50$) & 0.673 & +0.5 & .28 \\\\\nMMD (PCA $d{=}100$) & 0.670 & +0.2 & .51 \\\\\nCORAL (1-D logit) & 0.672 & +0.4 & .32 \\\\\nCORAL (PCA $d{=}50$) & 0.671 & +0.3 & .40 \\\\\n\\midrule\nLinear projection & \\textbf{0.698} & \\textbf{+3.0} & $<$.001 \\\\\nFew-shot 100 & \\textbf{0.718} & \\textbf{+5.0} & $<$.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Distributional matching ablation. All marginal-matching methods are inert; linear projection and few-shot, which directly address subspace rotation, succeed.}\n\\label{tab:dist_matching}\n\\end{table}\n\n\\paragraph{Geometric explanation.}\n\\cka{} subspace analysis (Table~\\ref{tab:why_fails}) reveals the mechanism: \\caclr{} successfully reduces MMD distance (marginal alignment) but leaves the correctness subspace angle essentially unchanged. MMD matches marginal distributions but cannot detect or correct the directional rotation of the correctness subspace between languages. Linear projection succeeds precisely because it directly learns this rotation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Tier} & \\textbf{Angle} & \\textbf{MMD} & \\textbf{MMD} & \\textbf{Angle} \\\\\n & \\textbf{before} & \\textbf{before} & \\textbf{after} & \\textbf{after} \\\\\n\\midrule\nHIGH & $11^\\circ$ & 0.018 & 0.008 & $10.5^\\circ$ \\\\\nMID  & $23^\\circ$ & 0.042 & 0.018 & $22^\\circ$ \\\\\nLOW  & $44^\\circ$ & 0.105 & 0.048 & $42^\\circ$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Why distributional matching fails: \\caclr{} reduces MMD distance but correctness subspace angle is unchanged. The conditional structure differs across languages; marginal matching cannot fix conditional mismatch \\cite{zhao2019learning}.}\n\\label{tab:why_fails}\n\\end{table}\n\n\\paragraph{Component ablation.}\nAblating $\\mathcal{L}_{\\text{SB-ECE}}$ ($\\alpha$ sweep): increasing $\\alpha$ reduces \\ece{} ($-1.8$~pp at $\\alpha=1.0$) but degrades \\aur{} ($-0.5$~pp). BCE alone (\\aur{}=0.668, \\ece{}=0.19) versus full \\caclr{} (\\aur{}=0.669, \\ece{}=0.174)---the calibration component helps marginally, but the consistency component does not.\n\n\\subsection{Transfer Method Comparison}\n\\label{sec:transfer}\n\nTable~\\ref{tab:transfer_comparison} presents the full transfer method comparison on Qwen3-235B at the transfer-optimal layer (L68).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{\\aur{}} & \\textbf{$\\Delta$} & \\textbf{$p$} & \\textbf{Req.} \\\\\n\\midrule\nZero-shot & .668 & --- & --- & 0 \\\\\nMean-shift & .668 & 0.0 & n/a & 0 \\\\\n\\caclr{} ($\\beta{=}0.01$) & .671 & +0.3 & .38 & ${\\sim}$10K par. \\\\\nLinear proj.\\ (50) & .684 & +1.6 & .012 & 50 pairs \\\\\nLinear proj.\\ (200) & .698 & +3.0 & $<$.001 & 200 pairs \\\\\nFew-shot 25 & .685 & +1.7 & .008 & 25 labels \\\\\nFew-shot 100 & .718 & +5.0 & $<$.001 & 100 labels \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Transfer method comparison (Qwen3-235B, L68, mean over 20~languages). Linear projection is the best label-free method; few-shot with 100~labels achieves the highest absolute performance.}\n\\label{tab:transfer_comparison}\n\\end{table}\n\nMean-shift is mathematically inert ($\\Delta$\\aur{} $\\equiv 0$ under StandardScaler + LR, since adding a constant to all logits preserves ranks). \\caclr{} is statistically indistinguishable from zero-shot. Linear projection with 200~pairs achieves +3.0~pp ($p<0.001$), and few-shot with 100~labels achieves +5.0~pp ($p<0.001$).\n\n\\subsection{Linear Projection: Sample Efficiency and Effect Reversal}\n\\label{sec:projection}\n\n\\paragraph{Saturation curves.}\nWe vary the number of parallel pairs from 10 to 200 (Table~\\ref{tab:saturation}). Overall, 80~pairs achieves 95\\% of maximum improvement. Resource-tier stratification is clear: HIGH languages saturate at ${\\sim}38$~pairs (subspace angle ${\\sim}11^\\circ$), while LOW languages require ${\\sim}95$~pairs (angle ${\\sim}43^\\circ$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Pairs} & \\textbf{HIGH} & \\textbf{MID} & \\textbf{LOW} & \\textbf{Overall} \\\\\n\\midrule\n10  & +0.1 & +0.8 & +2.5 & +1.1 \\\\\n20  & +0.3 & +1.5 & +3.8 & +1.7 \\\\\n50  & +0.4 & +2.3 & +5.2 & +2.5 \\\\\n100 & +0.5 & +2.6 & +5.8 & +2.9 \\\\\n200 & +0.5 & +2.7 & +6.2 & +3.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Linear projection $\\Delta$\\aur{} (pp) by resource tier and parallel pair count (Qwen3-235B, L68). LOW-resource languages benefit most.}\n\\label{tab:saturation}\n\\end{table}\n\n\\paragraph{Procrustes effect reversal.}\nLinear projection does not uniformly help. Table~\\ref{tab:reversal} shows that languages with zero-shot \\aur{} $> 0.65$ are \\emph{harmed} by projection ($-1.5$~pp mean), while those with \\aur{} $< 0.50$ benefit substantially (+5.5~pp). The reversal threshold is ${\\sim}0.57$ (95\\% CI: $[0.48, 0.64]$). When the correctness direction is already near-aligned ($< 15^\\circ$), the estimation noise in the Procrustes rotation exceeds the alignment gain.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccl}\n\\toprule\n\\textbf{ZS \\aur{} band} & \\textbf{$n$} & \\textbf{Mean $\\Delta$} & \\textbf{Example} \\\\\n\\midrule\n$< 0.50$ & 3 & +5.5 pp & am, yo, te \\\\\n$0.50{-}0.58$ & 3 & +3.2 pp & sw, bn, tr \\\\\n$0.58{-}0.62$ & 2 & +1.2 pp & hi, vi \\\\\n$0.62{-}0.67$ & 4 & +0.2 pp & ar, ko, id, uk \\\\\n$0.67{-}0.72$ & 4 & $-$0.8 pp & ru, ja, de, pt \\\\\n$> 0.72$ & 4 & $-$1.8 pp & zh, es, fr, nl \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Procrustes effect reversal: linear projection helps low-ZS languages but harms high-ZS ones. Deployment recommendation: use projection when ZS \\aur{} $< 0.57$, skip for $> 0.65$.}\n\\label{tab:reversal}\n\\end{table}\n\n\\subsection{Difficulty Decomposition}\n\\label{sec:decomposition}\n\nWe test whether cross-lingual transfer decomposes into difficulty-shared and capability-specific components. IRT difficulty probes ($R^2 = 0.32$) extract a difficulty direction; projecting it out and retraining correctness probes yields the results in Table~\\ref{tab:decomp}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Tier} & \\textbf{Lang} & \\textbf{Full} & \\textbf{Diff-proj} & \\textbf{$\\Delta$} & \\textbf{Rand $\\Delta$} \\\\\n\\midrule\nHIGH & zh & .738 & .746 & +0.8 & +0.4 \\\\\nHIGH & es & .745 & .757 & +1.2 & +0.6 \\\\\nHIGH & de & .725 & .743 & +1.8* & +0.8 \\\\\nMID  & hi & .670 & .698 & +2.8* & +0.8 \\\\\nMID  & ru & .705 & .727 & +2.2* & +0.8 \\\\\nMID  & tr & .660 & .685 & +2.5* & +0.8 \\\\\nMID  & ko & .688 & .682 & $-$0.6 & +0.3 \\\\\nLOW  & sw & .598 & .586 & $-$1.2 & +0.3 \\\\\nLOW  & bn & .612 & .647 & +3.5* & +0.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Difficulty decomposition results (Qwen3-235B, 8-layer mean). Diff-proj = after projecting out difficulty direction. Rand $\\Delta$ = random-direction control. * = $p<0.05$.}\n\\label{tab:decomp}\n\\end{table}\n\nProjecting out the difficulty direction generally improves transfer for mid-resource languages (+2--3~pp) but harms low-resource languages where difficulty and capability are more entangled. The mean effect (+1.8~pp) exceeds the random-direction control (+0.7~pp) by a factor of 2.6, confirming that ${\\sim}60\\%$ of the effect is difficulty-specific. However, prescriptive accuracy (predicting which strategy benefits a given language) is only 56\\%, barely above chance. We therefore present this as a \\textbf{descriptive} finding: the decomposition explains what transfer contains but does not reliably predict optimal strategy.\n\n\\subsection{Cross-Lingual Orthogonality}\n\\label{sec:orthogonality}\n\nThe correctness--confidence orthogonality discovered by \\citet{miao2026closing} for English ($\\cos < 0.04$) persists across languages. Mean cosine similarity is 0.04 overall, with 17/20~languages below 0.10 and 13/20 below 0.05. HIGH-resource languages closely replicate the English result (mean $\\cos = 0.026$), while LOW-resource languages show higher cosine (mean $0.075$), driven by three outliers (am: 0.148, yo: 0.122, te: 0.105). Probing controls (Section~\\ref{sec:controls}) confirm these outliers have low selectivity, indicating the elevated cosine is a noise artifact from weak directional signals rather than genuine alignment. The two architectures show no significant difference ($0.037$ vs $0.043$, $p=0.42$), indicating orthogonality is a structural property of the representation space.\n\n\\subsection{Probe Complexity Validation}\n\\label{sec:probe_complexity}\n\nWe compare logistic regression (LR) and 2-layer MLP probes to validate our methodological choice (Table~\\ref{tab:lr_mlp}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Q-LR} & \\textbf{Q-MLP} & \\textbf{L-LR} & \\textbf{L-MLP} \\\\\n\\midrule\nEN \\aur{} & .810 & .832 & .770 & .792 \\\\\nMean ZS \\aur{} & .668 & .638 & .648 & .622 \\\\\nTransfer gap & 14.2 & 19.4 & 12.2 & 17.0 \\\\\nZS pass rate & 75\\% & 55\\% & 70\\% & 50\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{LR vs MLP probe comparison (Q=Qwen3, L=Llama4). MLP overfits English-specific patterns, widening the transfer gap by ${\\sim}5$~pp.}\n\\label{tab:lr_mlp}\n\\end{table}\n\nMLP probes achieve +2.1~pp higher English \\aur{} by exploiting English-specific activation patterns, but these do not transfer: the cross-lingual gap widens from ${\\sim}13$~pp (LR) to ${\\sim}18$~pp (MLP). LR's single-hyperplane constraint forces it to learn language-agnostic features, making it the correct choice for cross-lingual transfer.\n\n\\subsection{Cross-Benchmark Generalization}\n\\label{sec:benchmarks}\n\nTable~\\ref{tab:cross_bench} validates our findings on Belebele (reading comprehension) and MMLU-ProX (translated MMLU).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{GlobalMMLU} & \\textbf{Belebele} & \\textbf{MMLU-ProX} \\\\\n\\midrule\nEN \\aur{} & 0.81 & 0.75 & 0.79 \\\\\nMean ZS \\aur{} & 0.668 & 0.632 & 0.658 \\\\\nZS pass rate & 75\\% & 60\\% & 72\\% \\\\\nPareto sig. & 9 & 6 & 8 \\\\\nLin.\\ proj.\\ $\\Delta$ & +3.0 & +2.5 & +2.8 \\\\\n\\caclr{} $\\Delta$ & +0.3 & +0.2 & +0.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-benchmark consistency (Qwen3-235B). All qualitative findings generalize. Cross-benchmark language ranking $\\rho = 0.89$.}\n\\label{tab:cross_bench}\n\\end{table}\n\nBelebele shows weaker Pareto (6~vs 9 significant languages) as expected for passage-dependent correctness, but the Pareto structure is preserved. \\caclr{} remains inert on both benchmarks. Linear projection remains effective. Cross-benchmark language ranking correlation is $\\rho = 0.89$, confirming results are not benchmark-specific.\n\n\\subsection{Probing Controls}\n\\label{sec:controls}\n\nFollowing \\citet{hewitt2019designing}, we train control probes on all 20~languages $\\times$ 3~architectures $\\times$ all probed layers. Table~\\ref{tab:controls} shows the artifact rate by resource tier and depth.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Depth} & \\textbf{HIGH} & \\textbf{MID} & \\textbf{LOW} & \\textbf{All} \\\\\n\\midrule\n0--25\\%  & 15\\% & 55\\% & 80\\% & 50\\% \\\\\n25--50\\% & 3\\% & 28\\% & 55\\% & 29\\% \\\\\n50--75\\% & 0\\% & 10\\% & 18\\% & 9\\% \\\\\n75--100\\% & 0\\% & 2\\% & 5\\% & 2\\% \\\\\n\\midrule\nOverall & 5\\% & 22\\% & 35\\% & 22\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Artifact rate (selectivity $< 0.05$) by resource tier and depth zone, averaged across 3~architectures. Low-resource shallow layers are predominantly artifacts.}\n\\label{tab:controls}\n\\end{table}\n\nOverall, 22\\% of language--layer combinations have selectivity $< 0.05$, concentrated in LOW-resource shallow layers (80\\% artifact rate at 0--25\\% depth). At the English-optimal depth, only am, yo, and te fall below the selectivity threshold (selectivity 0.015--0.054). After filtering, all main results are confirmed unchanged. This finding has field-level implications: \\textbf{all cross-lingual probing studies should include selectivity checks}, especially for low-resource languages where probe capacity can mimic genuine signal.\n\n\\subsection{Quantization Validation}\n\\label{sec:quantization}\n\nWe validate that INT4/W4A16 quantization does not introduce artifacts by comparing against FP16 at 5~layers per model on a 5\\% data subset. All $|\\Delta\\text{AUROC}| < 0.015$ and all CKA(FP16, quant) $> 0.97$ (Table~\\ref{tab:quant}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccr}\n\\toprule\n\\textbf{Model} & \\textbf{Layer} & \\textbf{FP16} & \\textbf{Quant} & \\textbf{$\\Delta$} \\\\\n\\midrule\nLlama4 & L8 (17\\%) & .635 & .633 & $-$.002 \\\\\nLlama4 & L24 (50\\%) & .722 & .717 & $-$.005 \\\\\nLlama4 & L44 (92\\%) & .770 & .762 & $-$.008 \\\\\n\\midrule\nQwen3 & L16 (17\\%) & .632 & .627 & $-$.005 \\\\\nQwen3 & L52 (55\\%) & .742 & .739 & $-$.003 \\\\\nQwen3 & L80 (85\\%) & .810 & .798 & $-$.012 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Quantization validation (selected layers). Max $|\\Delta| = 0.012$; CKA $> 0.97$ throughout. Quantization artifacts are negligible.}\n\\label{tab:quant}\n\\end{table}\n\nThe largest delta ($-0.012$ at Qwen3 L80) occurs at the deepest probed layer of the MoE model, where expert routing decisions may shift slightly under INT4. All deltas remain within bootstrap confidence intervals, supporting the validity of our quantized experimental setup.\n\n\\subsection{Extended Language Coverage}\n\\label{sec:extended}\n\nWe extend from 20 to 52~languages using GlobalMMLU and Belebele's full language sets (Table~\\ref{tab:extended}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Tier} & \\textbf{$n_{20}$} & \\textbf{$n_{52}$} & \\textbf{ZS \\aur{}} & \\textbf{Art.\\%} & \\textbf{Pass} \\\\\n\\midrule\nHIGH & 6 & 10 & 0.72 & 5\\% & 100\\% \\\\\nMID & 8 & 15 & 0.66 & 20\\% & 87\\% \\\\\nLOW & 6 & 16 & 0.58 & 32\\% & 56\\% \\\\\nV-LOW & 0 & 11 & 0.53 & 45\\% & 27\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Language coverage expansion to 52 languages. Art.\\% = artifact rate. Pass = ZS \\aur{} $>$ 0.58. Core findings replicate (rank correlation 20 vs.\\ 52 = 0.95).}\n\\label{tab:extended}\n\\end{table}\n\nThe rank correlation between 20-language and 52-language results is $0.95$, confirming that our core analysis on 20~languages is representative. Very-low-resource languages ($< 1$M training tokens) show 45\\% artifact rates and near-chance performance, reinforcing the necessity of probing controls. Writing-system clusters emerge as a moderate predictor of transfer quality within resource tiers.\n\n% ============================================================\n% 5. DISCUSSION\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{Practical recommendations.}\nFor practitioners deploying multilingual calibration: (1)~select probe layer at 70--75\\% depth rather than the English-optimal layer; (2)~use zero-shot transfer for HIGH-resource languages (ZS \\aur{} $> 0.65$); (3)~apply linear projection with ${\\sim}80$ parallel pairs for languages with ZS \\aur{} $< 0.57$; (4)~for the ambiguous zone ($0.57{-}0.65$), validate on a small held-out set.\n\n\\paragraph{Why distributional matching fails.}\nThe \\caclr{} negative result is grounded in the theoretical analysis of \\citet{zhao2019learning}: when $P(\\text{correct} \\mid \\mathbf{h})$ differs across languages (the capability-specific component), marginal distribution matching cannot recover the conditional structure. Our \\cka{} analysis provides empirical confirmation---MMD successfully reduces marginal distance while leaving the correctness subspace angle unchanged. Linear projection succeeds because it directly learns the subspace rotation without assuming distributional equivalence.\n\n\\paragraph{Limitations.}\nOur study is limited to MCQA benchmarks, which enable clean correctness labeling but may not generalize to open-ended generation. The three architectures differ simultaneously in type (MoE vs dense), scale, layer count, and training data; architectural effects cannot be isolated ($n=3$). Simpson's Paradox significance depends on the \\cka{} depth profile shape, limiting its universality as a diagnostic. Probing controls flag 22\\% of language--layer combinations as artifacts, and we cannot rule out subtler capacity effects below our selectivity threshold.\n\n% ============================================================\n% 6. CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe present the first large-scale study of cross-lingual correctness probe transfer across three architectures and 20~languages. The depth--transferability Pareto tradeoff is architecture-dependent, with \\cka{} geometry providing explanatory power via a Simpson's Paradox that reverses the apparent negative CKA--transfer relationship. Distributional matching (\\caclr{}, CORAL, high-dimensional MMD) uniformly fails---a systematic negative result explained by the inability of marginal matching to correct directional misalignment in the correctness subspace. Linear projection with ${\\sim}80$~parallel pairs is the most effective label-free solution, particularly for low-resource languages, though it should be skipped when zero-shot transfer already works well. Our probing controls reveal that 22\\% of cross-lingual probing results are capacity artifacts, a finding with implications for the broader field. Together, these results validate that probe-based calibration extends to multilingual settings, while identifying when and why it succeeds or fails.\n\n% ============================================================\n% REFERENCES\n% ============================================================\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{30}\n\n\\bibitem[\\protect\\citename{Angelopoulos and Bates}2023]{angelopoulos2023conformal}\nAnastasios~N. Angelopoulos and Stephen Bates. 2023.\n\\newblock Conformal prediction: A gentle introduction.\n\\newblock {\\em Foundations and Trends in Machine Learning}, 16(4):494--591.\n\n\\bibitem[\\protect\\citename{Artetxe et~al.}2018]{artetxe2018robust}\nMikel Artetxe, Gorka Labaka, and Eneko Agirre. 2018.\n\\newblock A robust self-learning method for fully unsupervised cross-lingual mappings of word embeddings.\n\\newblock In {\\em Proceedings of ACL}.\n\n\\bibitem[\\protect\\citename{Ben-David et~al.}2010]{bendavid2010theory}\nShai Ben-David, John Blitzer, Koby Crammer, Alex Kulesza, Fernando Pereira, and Jennifer~Wortman Vaughan. 2010.\n\\newblock A theory of learning from different domains.\n\\newblock {\\em Machine Learning}, 79:151--175.\n\n\\bibitem[\\protect\\citename{Civelli et~al.}2026]{civelli2026shared}\nMatteo Civelli, Tommaso Melis, and others. 2026.\n\\newblock Shared and language-specific difficulty representations across languages.\n\\newblock In {\\em Proceedings of ACL}.\n\n\\bibitem[\\protect\\citename{Confidence Manifold}2026]{confidence_manifold2026}\nAnonymous. 2026.\n\\newblock The confidence manifold: Internal geometry of LLM calibration.\n\\newblock Preprint.\n\n\\bibitem[\\protect\\citename{Conneau et~al.}2018]{conneau2018word}\nAlexis Conneau, Guillaume Lample, Marc'Aurelio Ranzato, Ludovic Denoyer, and Herv\\'{e} J\\'{e}gou. 2018.\n\\newblock Word translation without parallel data.\n\\newblock In {\\em Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Hewitt and Liang}2019]{hewitt2019designing}\nJohn Hewitt and Percy Liang. 2019.\n\\newblock Designing and interpreting probes with control tasks.\n\\newblock In {\\em Proceedings of EMNLP}.\n\n\\bibitem[\\protect\\citename{Ji et~al.}2025]{ji2025calibrating}\nZiwei Ji and others. 2025.\n\\newblock Calibrating language models via internal representations.\n\\newblock In {\\em Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Joshi et~al.}2025]{joshi2025calibration}\nPratik Joshi and others. 2025.\n\\newblock Calibration directions in the residual stream.\n\\newblock In {\\em Proceedings of NeurIPS}.\n\n\\bibitem[\\protect\\citename{Kornblith et~al.}2019]{kornblith2019similarity}\nSimon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton. 2019.\n\\newblock Similarity of neural network representations revisited.\n\\newblock In {\\em Proceedings of ICML}.\n\n\\bibitem[\\protect\\citename{Miao et~al.}2026a]{miao2026coral}\nYifei Miao and others. 2026.\n\\newblock Cross-task correctness probing via SAE analysis.\n\\newblock In {\\em Proceedings of ACL}.\n\n\\bibitem[\\protect\\citename{Miao and Ungar}2026]{miao2026closing}\nYifei Miao and Lyle Ungar. 2026.\n\\newblock Closing the gap between correctness and confidence.\n\\newblock In {\\em Proceedings of NAACL}.\n\n\\bibitem[\\protect\\citename{Pires et~al.}2019]{pires2019multilingual}\nTelmo Pires, Eva Schlinger, and Dan Garrette. 2019.\n\\newblock How multilingual is multilingual {BERT}?\n\\newblock In {\\em Proceedings of ACL}.\n\n\\bibitem[\\protect\\citename{Ravisankar et~al.}2026]{ravisankar2026dali}\nAditya Ravisankar and others. 2026.\n\\newblock {DALI}: Cross-lingual representation alignment.\n\\newblock Preprint.\n\n\\bibitem[\\protect\\citename{Wu and Dredze}2019]{wu2019beto}\nShijie Wu and Mark Dredze. 2019.\n\\newblock Beto, bentz, becas: The surprising cross-lingual effectiveness of {BERT}.\n\\newblock In {\\em Proceedings of EMNLP}.\n\n\\bibitem[\\protect\\citename{Xiao et~al.}2025]{xiao2025knowledge}\nYuxia Xiao and others. 2025.\n\\newblock Cross-lingual knowledge boundary probing.\n\\newblock In {\\em Proceedings of ACL}.\n\n\\bibitem[\\protect\\citename{Zhao et~al.}2019]{zhao2019learning}\nHan Zhao, Remi~Tachet des Combes, Kun Zhang, and Geoffrey Gordon. 2019.\n\\newblock On learning invariant representations for domain adaptation.\n\\newblock In {\\em Proceedings of ICML}.\n\n\\bibitem[\\protect\\citename{Zhou et~al.}2025]{zhou2025lace}\nKaitlyn Zhou, Dan Jurafsky, and Tatsunori Hashimoto. 2025.\n\\newblock {LACE}: Language-agnostic calibration via layer ensemble.\n\\newblock In {\\em Proceedings of ACL}.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "3960d394-bed1-4602-80b3-757e6e1535c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 27 · 2026-05-21T13:37:31.280Z_

```json
{
  "parentUuid": "a822bfd0-2ba4-4d55-9ebf-b02a219c7a49",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "2eeacaca-7ecd-4604-a056-69cbfea28ae3",
  "timestamp": "2026-05-21T13:37:31.280Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122458 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_dire…",
  "leafUuid": "2eeacaca-7ecd-4604-a056-69cbfea28ae3",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper with experimental data",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b"
}
```

---

### Assistant

_source line 30 · 2026-05-21T13:37:34.757Z_

Now compiling the LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2eeacaca-7ecd-4604-a056-69cbfea28ae3",
  "isSidechain": false,
  "requestId": "req_011CbFoe8XcoGbW6TLzBYD8N",
  "type": "assistant",
  "uuid": "02457287-6946-45c9-9552-19c886f7352f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KZAJJTfFJ2XLUiJAts5a2K",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14808,
      "cache_read_input_tokens": 55906,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14808,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 181,
          "cache_read_input_tokens": 55906,
          "cache_creation_input_tokens": 14808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14808
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

_source line 31 · 2026-05-21T13:37:36.121Z_

<details open><summary>🔧 Tool call — Bash · `toolu_013WPEUUVi9LoizzZr6zxKSw`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02457287-6946-45c9-9552-19c886f7352f",
  "isSidechain": false,
  "requestId": "req_011CbFoe8XcoGbW6TLzBYD8N",
  "type": "assistant",
  "uuid": "d89933f4-354b-4185-8367-0f3b13f71b47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KZAJJTfFJ2XLUiJAts5a2K",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14808,
      "cache_read_input_tokens": 55906,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14808,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 181,
          "cache_read_input_tokens": 55906,
          "cache_creation_input_tokens": 14808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14808
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

_source line 32 · 2026-05-21T13:37:36.267Z_

<details><summary>↩ Tool result · reported error · `toolu_013WPEUUVi9LoizzZr6zxKSw`</summary>

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
  "parentUuid": "d89933f4-354b-4185-8367-0f3b13f71b47",
  "isSidechain": false,
  "promptId": "e8f1a248-e970-4548-96f9-5cd439647eab",
  "type": "user",
  "uuid": "36bb1e03-632b-406d-9ddb-58339e4a02de",
  "toolUseResult": "Error: Exit code 1\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `acl.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
  "sourceToolAssistantUUID": "d89933f4-354b-4185-8367-0f3b13f71b47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-21T13:37:39.760Z_

<details><summary>Logged reasoning block</summary>

```text
The `acl.sty` file is not found. Let me switch to a simpler document class or check what's available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36bb1e03-632b-406d-9ddb-58339e4a02de",
  "isSidechain": false,
  "requestId": "req_011CbFoeVpHMf9MfraYsdvoP",
  "type": "assistant",
  "uuid": "6ac52744-7d12-4775-974c-d5b1ed32c44e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nb3Cac5MAvNM3B2dEacxSm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 475,
      "cache_read_input_tokens": 70714,
      "output_tokens": 459,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 475,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 459,
          "cache_read_input_tokens": 70714,
          "cache_creation_input_tokens": 475,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 475
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

_source line 34 · 2026-05-21T13:37:40.341Z_

ACL style not available. Let me fix to use a standard class.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ac52744-7d12-4775-974c-d5b1ed32c44e",
  "isSidechain": false,
  "requestId": "req_011CbFoeVpHMf9MfraYsdvoP",
  "type": "assistant",
  "uuid": "ba2f008b-cdb0-4c7b-9c64-32ef91d6896d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nb3Cac5MAvNM3B2dEacxSm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 475,
      "cache_read_input_tokens": 70714,
      "output_tokens": 459,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 475,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 459,
          "cache_read_input_tokens": 70714,
          "cache_creation_input_tokens": 475,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 475
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

_source line 35 · 2026-05-21T13:37:43.439Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01SPmF2th2cvV4XXNuYXFb7C`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median/paper.tex",
  "old_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{microtype}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{microtype}\n\\usepackage{natbib}\n\\usepackage{hyperref}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba2f008b-cdb0-4c7b-9c64-32ef91d6896d",
  "isSidechain": false,
  "requestId": "req_011CbFoeVpHMf9MfraYsdvoP",
  "type": "assistant",
  "uuid": "830c5da6-a396-4a10-a582-94dfb1e60d10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nb3Cac5MAvNM3B2dEacxSm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 475,
      "cache_read_input_tokens": 70714,
      "output_tokens": 459,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 475,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 459,
          "cache_read_input_tokens": 70714,
          "cache_creation_input_tokens": 475,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 475
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

_source line 36 · 2026-05-21T13:37:43.459Z_

<details><summary>↩ Tool result · `toolu_01SPmF2th2cvV4XXNuYXFb7C`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "830c5da6-a396-4a10-a582-94dfb1e60d10",
  "isSidechain": false,
  "promptId": "e8f1a248-e970-4548-96f9-5cd439647eab",
  "type": "user",
  "uuid": "9152d71e-a6de-4d3e-9652-5fe6958099fb",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median/paper.tex",
    "oldString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{microtype}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{microtype}\n\\usepackage{natbib}\n\\usepackage{hyperref}",
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
        "oldStart": 10,
        "oldLines": 6,
        "newStart": 10,
        "newLines": 8,
        "lines": [
          " \\usepackage{xcolor}",
          " \\usepackage{subcaption}",
          " \\usepackage{microtype}",
          "+\\usepackage{natbib}",
          "+\\usepackage{hyperref}",
          " ",
          " \\newcommand{\\aur}{\\textsc{auroc}}",
          " \\newcommand{\\ece}{\\textsc{ece}}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "830c5da6-a396-4a10-a582-94dfb1e60d10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-21T13:37:47.345Z_

Also need to remove the duplicate bibliography section since we're using `\begin{thebibliography}` directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9152d71e-a6de-4d3e-9652-5fe6958099fb",
  "isSidechain": false,
  "requestId": "req_011CbFof2bhnQWHJwayCdjcr",
  "type": "assistant",
  "uuid": "3ff0b93a-6647-47cf-a61b-84a09effc219",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y3eM3k7gyPZFb3uU7uR9bC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 546,
      "cache_read_input_tokens": 71189,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 546,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 204,
          "cache_read_input_tokens": 71189,
          "cache_creation_input_tokens": 546,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 546
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

_source line 38 · 2026-05-21T13:37:48.466Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01Q6nuRcSMiPkjMdus2S8ad7`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median/paper.tex",
  "old_string": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{30}",
  "new_string": "\\begin{thebibliography}{30}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ff0b93a-6647-47cf-a61b-84a09effc219",
  "isSidechain": false,
  "requestId": "req_011CbFof2bhnQWHJwayCdjcr",
  "type": "assistant",
  "uuid": "bc2052b2-b452-4ea6-9d51-8810381498a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y3eM3k7gyPZFb3uU7uR9bC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 546,
      "cache_read_input_tokens": 71189,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 546,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 204,
          "cache_read_input_tokens": 71189,
          "cache_creation_input_tokens": 546,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 546
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

_source line 39 · 2026-05-21T13:37:48.477Z_

<details><summary>↩ Tool result · `toolu_01Q6nuRcSMiPkjMdus2S8ad7`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc2052b2-b452-4ea6-9d51-8810381498a6",
  "isSidechain": false,
  "promptId": "e8f1a248-e970-4548-96f9-5cd439647eab",
  "type": "user",
  "uuid": "335624bc-a6ee-4498-b66e-d9752de1d32d",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median/paper.tex",
    "oldString": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{30}",
    "newString": "\\begin{thebibliography}{30}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 567,
        "oldLines": 9,
        "newStart": 567,
        "newLines": 6,
        "lines": [
          " % ============================================================",
          " % REFERENCES",
          " % ============================================================",
          "-\\bibliography{references}",
          "-\\bibliographystyle{acl_natbib}",
          "-",
          " \\begin{thebibliography}{30}",
          " ",
          " \\bibitem[\\protect\\citename{Angelopoulos and Bates}2023]{angelopoulos2023conformal}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "bc2052b2-b452-4ea6-9d51-8810381498a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-21T13:37:53.601Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Tu5jrZEGDkPtoJeUWfE7qg`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "335624bc-a6ee-4498-b66e-d9752de1d32d",
  "isSidechain": false,
  "requestId": "req_011CbFofQc2iCuR7xze8jjM5",
  "type": "assistant",
  "uuid": "c815028d-1c85-44ff-950c-a001bf1e9b0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ccsinnn3MNk81Y11LbjQHX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 291,
      "cache_read_input_tokens": 71735,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 291,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 71735,
          "cache_creation_input_tokens": 291,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 291
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

_source line 41 · 2026-05-21T13:37:54.286Z_

<details><summary>↩ Tool result · reported error · `toolu_01Tu5jrZEGDkPtoJeUWfE7qg`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.sty
(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)
(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype-pdftex.def)
(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.cfg))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-ptm.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-cmr.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-msa.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)
(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-msb.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1pcr.fd)

Package natbib Warning: Citation `zhou2025lace' on page 1 undefined on input li
ne 46.


Package natbib Warning: Citation `miao

... [4889 characters truncated] ...

y argument?
John Blitzer, Koby Crammer, Alex Kulesza, Fernando Pereira, and Jenni\ETC.
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.586 
      
Runaway argument?
Tommaso Melis, and others. 2026. \newblock Shared and language-specif\ETC.
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.591 
      
Runaway argument?
\@nil {confidence_manifold2026} Anonymous. 2026. \newblock The confid\ETC.
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.596 
      
Runaway argument?
Guillaume Lample, Marc'Aurelio Ranzato, Ludovic Denoyer, and Herv\'{e\ETC.
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.601 
      
Runaway argument?
\@nil {hewitt2019designing} John Hewitt and Percy Liang. 2019. \newblock \ETC.
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.606 
      
Runaway argument?
\@nil {ji2025calibrating} Ziwei Ji and others. 2025. \newblock Calibr\ETC.
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.611 
      
Runaway argument?
\@nil {joshi2025calibration} Pratik Joshi and others. 2025. \newblock \ETC.
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.616 
      
Runaway argument?
Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton. 2019. \newblock S\ETC.
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.621 
      
Runaway argument?
\@nil {miao2026coral} Yifei Miao and others. 2026. \newblock Cross-ta\ETC.
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.626 
      
Runaway argument?
\@nil {miao2026closing} Yifei Miao and Lyle Ungar. 2026. \newblock Cl\ETC.
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.631 
      
Runaway argument?
Eva Schlinger, and Dan Garrette. 2019. \newblock How multilingual is \ETC.
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.636 
      
Runaway argument?
\@nil {ravisankar2026dali} Aditya Ravisankar and others. 2026. \newblock \ETC.
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.641 
      
Runaway argument?
bentz, becas: The surprising cross-lingual effectiveness of {BERT}. \newblock \
ETC.
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.646 
      
Runaway argument?
\@nil {xiao2025knowledge} Yuxia Xiao and others. 2025. \newblock Cros\ETC.
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.651 
      
Runaway argument?
Remi~Tachet des Combes, Kun Zhang, and Geoffrey Gordon. 2019. \newblock \ETC.
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.656 
      
Runaway argument?
Dan Jurafsky, and Tatsunori Hashimoto. 2025. \newblock {LACE}: Langua\ETC.
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.661 
      

Package natbib Warning: There were undefined citations.

[11] (./paper.aux)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmbx8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmmib10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts
/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr
7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist
/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8
a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (11 pages, 215172 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c815028d-1c85-44ff-950c-a001bf1e9b0e",
  "isSidechain": false,
  "promptId": "e8f1a248-e970-4548-96f9-5cd439647eab",
  "type": "user",
  "uuid": "0cf1e2a1-75b8-4d59-a6ca-ce908f1aafa7",
  "toolUseResult": "Error: Exit code 1\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.sty\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype-pdftex.def)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-ptm.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-cmr.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-msa.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-msb.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1pcr.fd)\n\nPackage natbib Warning: Citation `zhou2025lace' on page 1 undefined on input li\nne 46.\n\n\nPackage natbib Warning: Citation `miao\n\n... [4889 characters truncated] ...\n\ny argument?\nJohn Blitzer, Koby Crammer, Alex Kulesza, Fernando Pereira, and Jenni\\ETC.\n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.586 \n      \nRunaway argument?\nTommaso Melis, and others. 2026. \\newblock Shared and language-specif\\ETC.\n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.591 \n      \nRunaway argument?\n\\@nil {confidence_manifold2026} Anonymous. 2026. \\newblock The confid\\ETC.\n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.596 \n      \nRunaway argument?\nGuillaume Lample, Marc'Aurelio Ranzato, Ludovic Denoyer, and Herv\\'{e\\ETC.\n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.601 \n      \nRunaway argument?\n\\@nil {hewitt2019designing} John Hewitt and Percy Liang. 2019. \\newblock \\ETC.\n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.606 \n      \nRunaway argument?\n\\@nil {ji2025calibrating} Ziwei Ji and others. 2025. \\newblock Calibr\\ETC.\n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.611 \n      \nRunaway argument?\n\\@nil {joshi2025calibration} Pratik Joshi and others. 2025. \\newblock \\ETC.\n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.616 \n      \nRunaway argument?\nMohammad Norouzi, Honglak Lee, and Geoffrey Hinton. 2019. \\newblock S\\ETC.\n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.621 \n      \nRunaway argument?\n\\@nil {miao2026coral} Yifei Miao and others. 2026. \\newblock Cross-ta\\ETC.\n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.626 \n      \nRunaway argument?\n\\@nil {miao2026closing} Yifei Miao and Lyle Ungar. 2026. \\newblock Cl\\ETC.\n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.631 \n      \nRunaway argument?\nEva Schlinger, and Dan Garrette. 2019. \\newblock How multilingual is \\ETC.\n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.636 \n      \nRunaway argument?\n\\@nil {ravisankar2026dali} Aditya Ravisankar and others. 2026. \\newblock \\ETC.\n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.641 \n      \nRunaway argument?\nbentz, becas: The surprising cross-lingual effectiveness of {BERT}. \\newblock \\\nETC.\n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.646 \n      \nRunaway argument?\n\\@nil {xiao2025knowledge} Yuxia Xiao and others. 2025. \\newblock Cros\\ETC.\n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.651 \n      \nRunaway argument?\nRemi~Tachet des Combes, Kun Zhang, and Geoffrey Gordon. 2019. \\newblock \\ETC.\n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.656 \n      \nRunaway argument?\nDan Jurafsky, and Tatsunori Hashimoto. 2025. \\newblock {LACE}: Langua\\ETC.\n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.661 \n      \n\nPackage natbib Warning: There were undefined citations.\n\n[11] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmbx8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmmib10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts\n/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr\n7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sh\nare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist\n/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\nurw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8\na.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (11 pages, 215172 bytes).\nTranscript written on paper.log.",
  "sourceToolAssistantUUID": "c815028d-1c85-44ff-950c-a001bf1e9b0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122458 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_dire…",
  "leafUuid": "0cf1e2a1-75b8-4d59-a6ca-ce908f1aafa7",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper with experimental data",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b"
}
```

---

### Assistant

_source line 44 · 2026-05-21T13:38:00.518Z_

<details><summary>Logged reasoning block</summary>

```text
The PDF was generated (11 pages, 215172 bytes), though there are errors in the bibliography section due to natbib compatibility with `\begin{thebibliography}`. The issue is that natbib expects a specific format for `\bibitem`. Let me fix the bibliography to use the proper natbib format.

Actually, the simplest fix is to remove natbib and just use the standard bibliography. Or format the `\bibitem` entries properly for natbib.

The PDF was still generated despite the errors, but the citations won't render properly. 

Now I'm reformatting the bibliography entries...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cf1e2a1-75b8-4d59-a6ca-ce908f1aafa7",
  "isSidechain": false,
  "requestId": "req_011CbFofpziwF4wCETQ5B41e",
  "type": "assistant",
  "uuid": "f6f0ab32-72a4-4c63-a053-c17534fdb45b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018R74KFJVjK9NsmXccuyjzR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4415,
      "cache_read_input_tokens": 72026,
      "output_tokens": 287,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4415,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 287,
          "cache_read_input_tokens": 72026,
          "cache_creation_input_tokens": 4415,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4415
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

_source line 45 · 2026-05-21T13:38:00.522Z_

PDF generated (11 pages) but bibliography has natbib formatting issues. Let me fix it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6f0ab32-72a4-4c63-a053-c17534fdb45b",
  "isSidechain": false,
  "requestId": "req_011CbFofpziwF4wCETQ5B41e",
  "type": "assistant",
  "uuid": "e2a37f2a-fded-4d04-a726-b5aad6e18399",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018R74KFJVjK9NsmXccuyjzR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4415,
      "cache_read_input_tokens": 72026,
      "output_tokens": 287,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4415,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 287,
          "cache_read_input_tokens": 72026,
          "cache_creation_input_tokens": 4415,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4415
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

_source line 46 · 2026-05-21T13:38:02.813Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AtqkUKnXwgsLdCb6UnAieV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median/paper.tex",
  "offset": 565
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2a37f2a-fded-4d04-a726-b5aad6e18399",
  "isSidechain": false,
  "requestId": "req_011CbFofpziwF4wCETQ5B41e",
  "type": "assistant",
  "uuid": "fb83ba90-7a87-4d4b-8943-3ba0481ed437",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018R74KFJVjK9NsmXccuyjzR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4415,
      "cache_read_input_tokens": 72026,
      "output_tokens": 287,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4415,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 287,
          "cache_read_input_tokens": 72026,
          "cache_creation_input_tokens": 4415,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4415
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

_source line 47 · 2026-05-21T13:38:02.823Z_

<details><summary>↩ Tool result · `toolu_01AtqkUKnXwgsLdCb6UnAieV`</summary>

```text
565	We present the first large-scale study of cross-lingual correctness probe transfer across three architectures and 20~languages. The depth--transferability Pareto tradeoff is architecture-dependent, with \cka{} geometry providing explanatory power via a Simpson's Paradox that reverses the apparent negative CKA--transfer relationship. Distributional matching (\caclr{}, CORAL, high-dimensional MMD) uniformly fails---a systematic negative result explained by the inability of marginal matching to correct directional misalignment in the correctness subspace. Linear projection with ${\sim}80$~parallel pairs is the most effective label-free solution, particularly for low-resource languages, though it should be skipped when zero-shot transfer already works well. Our probing controls reveal that 22\% of cross-lingual probing results are capacity artifacts, a finding with implications for the broader field. Together, these results validate that probe-based calibration extends to multilingual settings, while identifying when and why it succeeds or fails.
566	
567	% ============================================================
568	% REFERENCES
569	% ============================================================
570	\begin{thebibliography}{30}
571	
572	\bibitem[\protect\citename{Angelopoulos and Bates}2023]{angelopoulos2023conformal}
573	Anastasios~N. Angelopoulos and Stephen Bates. 2023.
574	\newblock Conformal prediction: A gentle introduction.
575	\newblock {\em Foundations and Trends in Machine Learning}, 16(4):494--591.
576	
577	\bibitem[\protect\citename{Artetxe et~al.}2018]{artetxe2018robust}
578	Mikel Artetxe, Gorka Labaka, and Eneko Agirre. 2018.
579	\newblock A robust self-learning method for fully unsupervised cross-lingual mappings of word embeddings.
580	\newblock In {\em Proceedings of ACL}.
581	
582	\bibitem[\protect\citename{Ben-David et~al.}2010]{bendavid2010theory}
583	Shai Ben-David, John Blitzer, Koby Crammer, Alex Kulesza, Fernando Pereira, and Jennifer~Wortman Vaughan. 2010.
584	\newblock A theory of learning from different domains.
585	\newblock {\em Machine Learning}, 79:151--175.
586	
587	\bibitem[\protect\citename{Civelli et~al.}2026]{civelli2026shared}
588	Matteo Civelli, Tommaso Melis, and others. 2026.
589	\newblock Shared and language-specific difficulty representations across languages.
590	\newblock In {\em Proceedings of ACL}.
591	
592	\bibitem[\protect\citename{Confidence Manifold}2026]{confidence_manifold2026}
593	Anonymous. 2026.
594	\newblock The confidence manifold: Internal geometry of LLM calibration.
595	\newblock Preprint.
596	
597	\bibitem[\protect\citename{Conneau et~al.}2018]{conneau2018word}
598	Alexis Conneau, Guillaume Lample, Marc'Aurelio Ranzato, Ludovic Denoyer, and Herv\'{e} J\'{e}gou. 2018.
599	\newblock Word translation without parallel data.
600	\newblock In {\em Proceedings of ICLR}.
601	
602	\bibitem[\protect\citename{Hewitt and Liang}2019]{hewitt2019designing}
603	John Hewitt and Percy Liang. 2019.
604	\newblock Designing and interpreting probes with control tasks.
605	\newblock In {\em Proceedings of EMNLP}.
606	
607	\bibitem[\protect\citename{Ji et~al.}2025]{ji2025calibrating}
608	Ziwei Ji and others. 2025.
609	\newblock Calibrating language models via internal representations.
610	\newblock In {\em Proceedings of ICLR}.
611	
612	\bibitem[\protect\citename{Joshi et~al.}2025]{joshi2025calibration}
613	Pratik Joshi and others. 2025.
614	\newblock Calibration directions in the residual stream.
615	\newblock In {\em Proceedings of NeurIPS}.
616	
617	\bibitem[\protect\citename{Kornblith et~al.}2019]{kornblith2019similarity}
618	Simon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton. 2019.
619	\newblock Similarity of neural network representations revisited.
620	\newblock In {\em Proceedings of ICML}.
621	
622	\bibitem[\protect\citename{Miao et~al.}2026a]{miao2026coral}
623	Yifei Miao and others. 2026.
624	\newblock Cross-task correctness probing via SAE analysis.
625	\newblock In {\em Proceedings of ACL}.
626	
627	\bibitem[\protect\citename{Miao and Ungar}2026]{miao2026closing}
628	Yifei Miao and Lyle Ungar. 2026.
629	\newblock Closing the gap between correctness and confidence.
630	\newblock In {\em Proceedings of NAACL}.
631	
632	\bibitem[\protect\citename{Pires et~al.}2019]{pires2019multilingual}
633	Telmo Pires, Eva Schlinger, and Dan Garrette. 2019.
634	\newblock How multilingual is multilingual {BERT}?
635	\newblock In {\em Proceedings of ACL}.
636	
637	\bibitem[\protect\citename{Ravisankar et~al.}2026]{ravisankar2026dali}
638	Aditya Ravisankar and others. 2026.
639	\newblock {DALI}: Cross-lingual representation alignment.
640	\newblock Preprint.
641	
642	\bibitem[\protect\citename{Wu and Dredze}2019]{wu2019beto}
643	Shijie Wu and Mark Dredze. 2019.
644	\newblock Beto, bentz, becas: The surprising cross-lingual effectiveness of {BERT}.
645	\newblock In {\em Proceedings of EMNLP}.
646	
647	\bibitem[\protect\citename{Xiao et~al.}2025]{xiao2025knowledge}
648	Yuxia Xiao and others. 2025.
649	\newblock Cross-lingual knowledge boundary probing.
650	\newblock In {\em Proceedings of ACL}.
651	
652	\bibitem[\protect\citename{Zhao et~al.}2019]{zhao2019learning}
653	Han Zhao, Remi~Tachet des Combes, Kun Zhang, and Geoffrey Gordon. 2019.
654	\newblock On learning invariant representations for domain adaptation.
655	\newblock In {\em Proceedings of ICML}.
656	
657	\bibitem[\protect\citename{Zhou et~al.}2025]{zhou2025lace}
658	Kaitlyn Zhou, Dan Jurafsky, and Tatsunori Hashimoto. 2025.
659	\newblock {LACE}: Language-agnostic calibration via layer ensemble.
660	\newblock In {\em Proceedings of ACL}.
661	
662	\end{thebibliography}
663	
664	\end{document}
665	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb83ba90-7a87-4d4b-8943-3ba0481ed437",
  "isSidechain": false,
  "promptId": "e8f1a248-e970-4548-96f9-5cd439647eab",
  "type": "user",
  "uuid": "bc1eadf8-fb75-4b1a-8a34-fd3f8d570d2f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median/paper.tex",
      "content": "We present the first large-scale study of cross-lingual correctness probe transfer across three architectures and 20~languages. The depth--transferability Pareto tradeoff is architecture-dependent, with \\cka{} geometry providing explanatory power via a Simpson's Paradox that reverses the apparent negative CKA--transfer relationship. Distributional matching (\\caclr{}, CORAL, high-dimensional MMD) uniformly fails---a systematic negative result explained by the inability of marginal matching to correct directional misalignment in the correctness subspace. Linear projection with ${\\sim}80$~parallel pairs is the most effective label-free solution, particularly for low-resource languages, though it should be skipped when zero-shot transfer already works well. Our probing controls reveal that 22\\% of cross-lingual probing results are capacity artifacts, a finding with implications for the broader field. Together, these results validate that probe-based calibration extends to multilingual settings, while identifying when and why it succeeds or fails.\n\n% ============================================================\n% REFERENCES\n% ============================================================\n\\begin{thebibliography}{30}\n\n\\bibitem[\\protect\\citename{Angelopoulos and Bates}2023]{angelopoulos2023conformal}\nAnastasios~N. Angelopoulos and Stephen Bates. 2023.\n\\newblock Conformal prediction: A gentle introduction.\n\\newblock {\\em Foundations and Trends in Machine Learning}, 16(4):494--591.\n\n\\bibitem[\\protect\\citename{Artetxe et~al.}2018]{artetxe2018robust}\nMikel Artetxe, Gorka Labaka, and Eneko Agirre. 2018.\n\\newblock A robust self-learning method for fully unsupervised cross-lingual mappings of word embeddings.\n\\newblock In {\\em Proceedings of ACL}.\n\n\\bibitem[\\protect\\citename{Ben-David et~al.}2010]{bendavid2010theory}\nShai Ben-David, John Blitzer, Koby Crammer, Alex Kulesza, Fernando Pereira, and Jennifer~Wortman Vaughan. 2010.\n\\newblock A theory of learning from different domains.\n\\newblock {\\em Machine Learning}, 79:151--175.\n\n\\bibitem[\\protect\\citename{Civelli et~al.}2026]{civelli2026shared}\nMatteo Civelli, Tommaso Melis, and others. 2026.\n\\newblock Shared and language-specific difficulty representations across languages.\n\\newblock In {\\em Proceedings of ACL}.\n\n\\bibitem[\\protect\\citename{Confidence Manifold}2026]{confidence_manifold2026}\nAnonymous. 2026.\n\\newblock The confidence manifold: Internal geometry of LLM calibration.\n\\newblock Preprint.\n\n\\bibitem[\\protect\\citename{Conneau et~al.}2018]{conneau2018word}\nAlexis Conneau, Guillaume Lample, Marc'Aurelio Ranzato, Ludovic Denoyer, and Herv\\'{e} J\\'{e}gou. 2018.\n\\newblock Word translation without parallel data.\n\\newblock In {\\em Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Hewitt and Liang}2019]{hewitt2019designing}\nJohn Hewitt and Percy Liang. 2019.\n\\newblock Designing and interpreting probes with control tasks.\n\\newblock In {\\em Proceedings of EMNLP}.\n\n\\bibitem[\\protect\\citename{Ji et~al.}2025]{ji2025calibrating}\nZiwei Ji and others. 2025.\n\\newblock Calibrating language models via internal representations.\n\\newblock In {\\em Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Joshi et~al.}2025]{joshi2025calibration}\nPratik Joshi and others. 2025.\n\\newblock Calibration directions in the residual stream.\n\\newblock In {\\em Proceedings of NeurIPS}.\n\n\\bibitem[\\protect\\citename{Kornblith et~al.}2019]{kornblith2019similarity}\nSimon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton. 2019.\n\\newblock Similarity of neural network representations revisited.\n\\newblock In {\\em Proceedings of ICML}.\n\n\\bibitem[\\protect\\citename{Miao et~al.}2026a]{miao2026coral}\nYifei Miao and others. 2026.\n\\newblock Cross-task correctness probing via SAE analysis.\n\\newblock In {\\em Proceedings of ACL}.\n\n\\bibitem[\\protect\\citename{Miao and Ungar}2026]{miao2026closing}\nYifei Miao and Lyle Ungar. 2026.\n\\newblock Closing the gap between correctness and confidence.\n\\newblock In {\\em Proceedings of NAACL}.\n\n\\bibitem[\\protect\\citename{Pires et~al.}2019]{pires2019multilingual}\nTelmo Pires, Eva Schlinger, and Dan Garrette. 2019.\n\\newblock How multilingual is multilingual {BERT}?\n\\newblock In {\\em Proceedings of ACL}.\n\n\\bibitem[\\protect\\citename{Ravisankar et~al.}2026]{ravisankar2026dali}\nAditya Ravisankar and others. 2026.\n\\newblock {DALI}: Cross-lingual representation alignment.\n\\newblock Preprint.\n\n\\bibitem[\\protect\\citename{Wu and Dredze}2019]{wu2019beto}\nShijie Wu and Mark Dredze. 2019.\n\\newblock Beto, bentz, becas: The surprising cross-lingual effectiveness of {BERT}.\n\\newblock In {\\em Proceedings of EMNLP}.\n\n\\bibitem[\\protect\\citename{Xiao et~al.}2025]{xiao2025knowledge}\nYuxia Xiao and others. 2025.\n\\newblock Cross-lingual knowledge boundary probing.\n\\newblock In {\\em Proceedings of ACL}.\n\n\\bibitem[\\protect\\citename{Zhao et~al.}2019]{zhao2019learning}\nHan Zhao, Remi~Tachet des Combes, Kun Zhang, and Geoffrey Gordon. 2019.\n\\newblock On learning invariant representations for domain adaptation.\n\\newblock In {\\em Proceedings of ICML}.\n\n\\bibitem[\\protect\\citename{Zhou et~al.}2025]{zhou2025lace}\nKaitlyn Zhou, Dan Jurafsky, and Tatsunori Hashimoto. 2025.\n\\newblock {LACE}: Language-agnostic calibration via layer ensemble.\n\\newblock In {\\em Proceedings of ACL}.\n\n\\end{thebibliography}\n\n\\end{document}\n",
      "numLines": 101,
      "startLine": 565,
      "totalLines": 665
    }
  },
  "sourceToolAssistantUUID": "fb83ba90-7a87-4d4b-8943-3ba0481ed437",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-21T13:38:06.160Z_

The issue is `\protect\citename` format which natbib doesn't understand. Let me replace the bibliography with natbib-compatible format.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc1eadf8-fb75-4b1a-8a34-fd3f8d570d2f",
  "isSidechain": false,
  "requestId": "req_011CbFogTdcusFgmL8JLZpFK",
  "type": "assistant",
  "uuid": "0f3f7339-0b1d-42db-947f-5d9954353a4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019n87J1Ux8ehEktQcibXLW5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2256,
      "cache_read_input_tokens": 76441,
      "output_tokens": 3073,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2256,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3073,
          "cache_read_input_tokens": 76441,
          "cache_creation_input_tokens": 2256,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2256
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

_source line 49 · 2026-05-21T13:38:29.237Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01CsdH7xTYgZ5p8MkQfWqDJF`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median/paper.tex",
  "old_string": "\\begin{thebibliography}{30}\n\n\\bibitem[\\protect\\citename{Angelopoulos and Bates}2023]{angelopoulos2023conformal}\nAnastasios~N. Angelopoulos and Stephen Bates. 2023.\n\\newblock Conformal prediction: A gentle introduction.\n\\newblock {\\em Foundations and Trends in Machine Learning}, 16(4):494--591.\n\n\\bibitem[\\protect\\citename{Artetxe et~al.}2018]{artetxe2018robust}\nMikel Artetxe, Gorka Labaka, and Eneko Agirre. 2018.\n\\newblock A robust self-learning method for fully unsupervised cross-lingual mappings of word embeddings.\n\\newblock In {\\em Proceedings of ACL}.\n\n\\bibitem[\\protect\\citename{Ben-David et~al.}2010]{bendavid2010theory}\nShai Ben-David, John Blitzer, Koby Crammer, Alex Kulesza, Fernando Pereira, and Jennifer~Wortman Vaughan. 2010.\n\\newblock A theory of learning from different domains.\n\\newblock {\\em Machine Learning}, 79:151--175.\n\n\\bibitem[\\protect\\citename{Civelli et~al.}2026]{civelli2026shared}\nMatteo Civelli, Tommaso Melis, and others. 2026.\n\\newblock Shared and language-specific difficulty representations across languages.\n\\newblock In {\\em Proceedings of ACL}.\n\n\\bibitem[\\protect\\citename{Confidence Manifold}2026]{confidence_manifold2026}\nAnonymous. 2026.\n\\newblock The confidence manifold: Internal geometry of LLM calibration.\n\\newblock Preprint.\n\n\\bibitem[\\protect\\citename{Conneau et~al.}2018]{conneau2018word}\nAlexis Conneau, Guillaume Lample, Marc'Aurelio Ranzato, Ludovic Denoyer, and Herv\\'{e} J\\'{e}gou. 2018.\n\\newblock Word translation without parallel data.\n\\newblock In {\\em Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Hewitt and Liang}2019]{hewitt2019designing}\nJohn Hewitt and Percy Liang. 2019.\n\\newblock Designing and interpreting probes with control tasks.\n\\newblock In {\\em Proceedings of EMNLP}.\n\n\\bibitem[\\protect\\citename{Ji et~al.}2025]{ji2025calibrating}\nZiwei Ji and others. 2025.\n\\newblock Calibrating language models via internal representations.\n\\newblock In {\\em Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Joshi et~al.}2025]{joshi2025calibration}\nPratik Joshi and others. 2025.\n\\newblock Calibration directions in the residual stream.\n\\newblock In {\\em Proceedings of NeurIPS}.\n\n\\bibitem[\\protect\\citename{Kornblith et~al.}2019]{kornblith2019similarity}\nSimon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton. 2019.\n\\newblock Similarity of neural network representations revisited.\n\\newblock In {\\em Proceedings of ICML}.\n\n\\bibitem[\\protect\\citename{Miao et~al.}2026a]{miao2026coral}\nYifei Miao and others. 2026.\n\\newblock Cross-task correctness probing via SAE analysis.\n\\newblock In {\\em Proceedings of ACL}.\n\n\\bibitem[\\protect\\citename{Miao and Ungar}2026]{miao2026closing}\nYifei Miao and Lyle Ungar. 2026.\n\\newblock Closing the gap between correctness and confidence.\n\\newblock In {\\em Proceedings of NAACL}.\n\n\\bibitem[\\protect\\citename{Pires et~al.}2019]{pires2019multilingual}\nTelmo Pires, Eva Schlinger, and Dan Garrette. 2019.\n\\newblock How multilingual is multilingual {BERT}?\n\\newblock In {\\em Proceedings of ACL}.\n\n\\bibitem[\\protect\\citename{Ravisankar et~al.}2026]{ravisankar2026dali}\nAditya Ravisankar and others. 2026.\n\\newblock {DALI}: Cross-lingual representation alignment.\n\\newblock Preprint.\n\n\\bibitem[\\protect\\citename{Wu and Dredze}2019]{wu2019beto}\nShijie Wu and Mark Dredze. 2019.\n\\newblock Beto, bentz, becas: The surprising cross-lingual effectiveness of {BERT}.\n\\newblock In {\\em Proceedings of EMNLP}.\n\n\\bibitem[\\protect\\citename{Xiao et~al.}2025]{xiao2025knowledge}\nYuxia Xiao and others. 2025.\n\\newblock Cross-lingual knowledge boundary probing.\n\\newblock In {\\em Proceedings of ACL}.\n\n\\bibitem[\\protect\\citename{Zhao et~al.}2019]{zhao2019learning}\nHan Zhao, Remi~Tachet des Combes, Kun Zhang, and Geoffrey Gordon. 2019.\n\\newblock On learning invariant representations for domain adaptation.\n\\newblock In {\\em Proceedings of ICML}.\n\n\\bibitem[\\protect\\citename{Zhou et~al.}2025]{zhou2025lace}\nKaitlyn Zhou, Dan Jurafsky, and Tatsunori Hashimoto. 2025.\n\\newblock {LACE}: Language-agnostic calibration via layer ensemble.\n\\newblock In {\\em Proceedings of ACL}.\n\n\\end{thebibliography}",
  "new_string": "\\begin{thebibliography}{18}\n\n\\bibitem[Angelopoulos and Bates(2023)]{angelopoulos2023conformal}\nA.~N. Angelopoulos and S.~Bates.\n\\newblock Conformal prediction: A gentle introduction.\n\\newblock {\\em Foundations and Trends in ML}, 16(4):494--591, 2023.\n\n\\bibitem[Artetxe et~al.(2018)]{artetxe2018robust}\nM.~Artetxe, G.~Labaka, and E.~Agirre.\n\\newblock A robust self-learning method for fully unsupervised cross-lingual mappings of word embeddings.\n\\newblock In {\\em Proc. ACL}, 2018.\n\n\\bibitem[Ben-David et~al.(2010)]{bendavid2010theory}\nS.~Ben-David, J.~Blitzer, K.~Crammer, A.~Kulesza, F.~Pereira, and J.~W. Vaughan.\n\\newblock A theory of learning from different domains.\n\\newblock {\\em Machine Learning}, 79:151--175, 2010.\n\n\\bibitem[Civelli et~al.(2026)]{civelli2026shared}\nM.~Civelli, T.~Melis, et~al.\n\\newblock Shared and language-specific difficulty representations across languages.\n\\newblock In {\\em Proc. ACL}, 2026.\n\n\\bibitem[{Anonymous}(2026)]{confidence_manifold2026}\n{Anonymous}.\n\\newblock The confidence manifold: Internal geometry of LLM calibration.\n\\newblock Preprint, 2026.\n\n\\bibitem[Conneau et~al.(2018)]{conneau2018word}\nA.~Conneau, G.~Lample, M.~Ranzato, L.~Denoyer, and H.~J\\'{e}gou.\n\\newblock Word translation without parallel data.\n\\newblock In {\\em Proc. ICLR}, 2018.\n\n\\bibitem[Hewitt and Liang(2019)]{hewitt2019designing}\nJ.~Hewitt and P.~Liang.\n\\newblock Designing and interpreting probes with control tasks.\n\\newblock In {\\em Proc. EMNLP}, 2019.\n\n\\bibitem[Ji et~al.(2025)]{ji2025calibrating}\nZ.~Ji et~al.\n\\newblock Calibrating language models via internal representations.\n\\newblock In {\\em Proc. ICLR}, 2025.\n\n\\bibitem[Joshi et~al.(2025)]{joshi2025calibration}\nP.~Joshi et~al.\n\\newblock Calibration directions in the residual stream.\n\\newblock In {\\em Proc. NeurIPS}, 2025.\n\n\\bibitem[Kornblith et~al.(2019)]{kornblith2019similarity}\nS.~Kornblith, M.~Norouzi, H.~Lee, and G.~Hinton.\n\\newblock Similarity of neural network representations revisited.\n\\newblock In {\\em Proc. ICML}, 2019.\n\n\\bibitem[Miao et~al.(2026)]{miao2026coral}\nY.~Miao et~al.\n\\newblock Cross-task correctness probing via SAE analysis.\n\\newblock In {\\em Proc. ACL}, 2026.\n\n\\bibitem[Miao and Ungar(2026)]{miao2026closing}\nY.~Miao and L.~Ungar.\n\\newblock Closing the gap between correctness and confidence.\n\\newblock In {\\em Proc. NAACL}, 2026.\n\n\\bibitem[Pires et~al.(2019)]{pires2019multilingual}\nT.~Pires, E.~Schlinger, and D.~Garrette.\n\\newblock How multilingual is multilingual {BERT}?\n\\newblock In {\\em Proc. ACL}, 2019.\n\n\\bibitem[Ravisankar et~al.(2026)]{ravisankar2026dali}\nA.~Ravisankar et~al.\n\\newblock {DALI}: Cross-lingual representation alignment.\n\\newblock Preprint, 2026.\n\n\\bibitem[Wu and Dredze(2019)]{wu2019beto}\nS.~Wu and M.~Dredze.\n\\newblock Beto, bentz, becas: The surprising cross-lingual effectiveness of {BERT}.\n\\newblock In {\\em Proc. EMNLP}, 2019.\n\n\\bibitem[Xiao et~al.(2025)]{xiao2025knowledge}\nY.~Xiao et~al.\n\\newblock Cross-lingual knowledge boundary probing.\n\\newblock In {\\em Proc. ACL}, 2025.\n\n\\bibitem[Zhao et~al.(2019)]{zhao2019learning}\nH.~Zhao, R.~Tachet des Combes, K.~Zhang, and G.~Gordon.\n\\newblock On learning invariant representations for domain adaptation.\n\\newblock In {\\em Proc. ICML}, 2019.\n\n\\bibitem[Zhou et~al.(2025)]{zhou2025lace}\nK.~Zhou, D.~Jurafsky, and T.~Hashimoto.\n\\newblock {LACE}: Language-agnostic calibration via layer ensemble.\n\\newblock In {\\em Proc. ACL}, 2025.\n\n\\end{thebibliography}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f3f7339-0b1d-42db-947f-5d9954353a4b",
  "isSidechain": false,
  "requestId": "req_011CbFogTdcusFgmL8JLZpFK",
  "type": "assistant",
  "uuid": "f7d6b3c0-3c9b-4738-a0ee-b8cfb3826292",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019n87J1Ux8ehEktQcibXLW5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2256,
      "cache_read_input_tokens": 76441,
      "output_tokens": 3073,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2256,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3073,
          "cache_read_input_tokens": 76441,
          "cache_creation_input_tokens": 2256,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2256
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

_source line 50 · 2026-05-21T13:38:29.268Z_

<details><summary>↩ Tool result · `toolu_01CsdH7xTYgZ5p8MkQfWqDJF`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7d6b3c0-3c9b-4738-a0ee-b8cfb3826292",
  "isSidechain": false,
  "promptId": "e8f1a248-e970-4548-96f9-5cd439647eab",
  "type": "user",
  "uuid": "7ee25c6d-8693-4fd7-84cd-0a8c56d592bb",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median/paper.tex",
    "oldString": "\\begin{thebibliography}{30}\n\n\\bibitem[\\protect\\citename{Angelopoulos and Bates}2023]{angelopoulos2023conformal}\nAnastasios~N. Angelopoulos and Stephen Bates. 2023.\n\\newblock Conformal prediction: A gentle introduction.\n\\newblock {\\em Foundations and Trends in Machine Learning}, 16(4):494--591.\n\n\\bibitem[\\protect\\citename{Artetxe et~al.}2018]{artetxe2018robust}\nMikel Artetxe, Gorka Labaka, and Eneko Agirre. 2018.\n\\newblock A robust self-learning method for fully unsupervised cross-lingual mappings of word embeddings.\n\\newblock In {\\em Proceedings of ACL}.\n\n\\bibitem[\\protect\\citename{Ben-David et~al.}2010]{bendavid2010theory}\nShai Ben-David, John Blitzer, Koby Crammer, Alex Kulesza, Fernando Pereira, and Jennifer~Wortman Vaughan. 2010.\n\\newblock A theory of learning from different domains.\n\\newblock {\\em Machine Learning}, 79:151--175.\n\n\\bibitem[\\protect\\citename{Civelli et~al.}2026]{civelli2026shared}\nMatteo Civelli, Tommaso Melis, and others. 2026.\n\\newblock Shared and language-specific difficulty representations across languages.\n\\newblock In {\\em Proceedings of ACL}.\n\n\\bibitem[\\protect\\citename{Confidence Manifold}2026]{confidence_manifold2026}\nAnonymous. 2026.\n\\newblock The confidence manifold: Internal geometry of LLM calibration.\n\\newblock Preprint.\n\n\\bibitem[\\protect\\citename{Conneau et~al.}2018]{conneau2018word}\nAlexis Conneau, Guillaume Lample, Marc'Aurelio Ranzato, Ludovic Denoyer, and Herv\\'{e} J\\'{e}gou. 2018.\n\\newblock Word translation without parallel data.\n\\newblock In {\\em Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Hewitt and Liang}2019]{hewitt2019designing}\nJohn Hewitt and Percy Liang. 2019.\n\\newblock Designing and interpreting probes with control tasks.\n\\newblock In {\\em Proceedings of EMNLP}.\n\n\\bibitem[\\protect\\citename{Ji et~al.}2025]{ji2025calibrating}\nZiwei Ji and others. 2025.\n\\newblock Calibrating language models via internal representations.\n\\newblock In {\\em Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Joshi et~al.}2025]{joshi2025calibration}\nPratik Joshi and others. 2025.\n\\newblock Calibration directions in the residual stream.\n\\newblock In {\\em Proceedings of NeurIPS}.\n\n\\bibitem[\\protect\\citename{Kornblith et~al.}2019]{kornblith2019similarity}\nSimon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton. 2019.\n\\newblock Similarity of neural network representations revisited.\n\\newblock In {\\em Proceedings of ICML}.\n\n\\bibitem[\\protect\\citename{Miao et~al.}2026a]{miao2026coral}\nYifei Miao and others. 2026.\n\\newblock Cross-task correctness probing via SAE analysis.\n\\newblock In {\\em Proceedings of ACL}.\n\n\\bibitem[\\protect\\citename{Miao and Ungar}2026]{miao2026closing}\nYifei Miao and Lyle Ungar. 2026.\n\\newblock Closing the gap between correctness and confidence.\n\\newblock In {\\em Proceedings of NAACL}.\n\n\\bibitem[\\protect\\citename{Pires et~al.}2019]{pires2019multilingual}\nTelmo Pires, Eva Schlinger, and Dan Garrette. 2019.\n\\newblock How multilingual is multilingual {BERT}?\n\\newblock In {\\em Proceedings of ACL}.\n\n\\bibitem[\\protect\\citename{Ravisankar et~al.}2026]{ravisankar2026dali}\nAditya Ravisankar and others. 2026.\n\\newblock {DALI}: Cross-lingual representation alignment.\n\\newblock Preprint.\n\n\\bibitem[\\protect\\citename{Wu and Dredze}2019]{wu2019beto}\nShijie Wu and Mark Dredze. 2019.\n\\newblock Beto, bentz, becas: The surprising cross-lingual effectiveness of {BERT}.\n\\newblock In {\\em Proceedings of EMNLP}.\n\n\\bibitem[\\protect\\citename{Xiao et~al.}2025]{xiao2025knowledge}\nYuxia Xiao and others. 2025.\n\\newblock Cross-lingual knowledge boundary probing.\n\\newblock In {\\em Proceedings of ACL}.\n\n\\bibitem[\\protect\\citename{Zhao et~al.}2019]{zhao2019learning}\nHan Zhao, Remi~Tachet des Combes, Kun Zhang, and Geoffrey Gordon. 2019.\n\\newblock On learning invariant representations for domain adaptation.\n\\newblock In {\\em Proceedings of ICML}.\n\n\\bibitem[\\protect\\citename{Zhou et~al.}2025]{zhou2025lace}\nKaitlyn Zhou, Dan Jurafsky, and Tatsunori Hashimoto. 2025.\n\\newblock {LACE}: Language-agnostic calibration via layer ensemble.\n\\newblock In {\\em Proceedings of ACL}.\n\n\\end{thebibliography}",
    "newString": "\\begin{thebibliography}{18}\n\n\\bibitem[Angelopoulos and Bates(2023)]{angelopoulos2023conformal}\nA.~N. Angelopoulos and S.~Bates.\n\\newblock Conformal prediction: A gentle introduction.\n\\newblock {\\em Foundations and Trends in ML}, 16(4):494--591, 2023.\n\n\\bibitem[Artetxe et~al.(2018)]{artetxe2018robust}\nM.~Artetxe, G.~Labaka, and E.~Agirre.\n\\newblock A robust self-learning method for fully unsupervised cross-lingual mappings of word embeddings.\n\\newblock In {\\em Proc. ACL}, 2018.\n\n\\bibitem[Ben-David et~al.(2010)]{bendavid2010theory}\nS.~Ben-David, J.~Blitzer, K.~Crammer, A.~Kulesza, F.~Pereira, and J.~W. Vaughan.\n\\newblock A theory of learning from different domains.\n\\newblock {\\em Machine Learning}, 79:151--175, 2010.\n\n\\bibitem[Civelli et~al.(2026)]{civelli2026shared}\nM.~Civelli, T.~Melis, et~al.\n\\newblock Shared and language-specific difficulty representations across languages.\n\\newblock In {\\em Proc. ACL}, 2026.\n\n\\bibitem[{Anonymous}(2026)]{confidence_manifold2026}\n{Anonymous}.\n\\newblock The confidence manifold: Internal geometry of LLM calibration.\n\\newblock Preprint, 2026.\n\n\\bibitem[Conneau et~al.(2018)]{conneau2018word}\nA.~Conneau, G.~Lample, M.~Ranzato, L.~Denoyer, and H.~J\\'{e}gou.\n\\newblock Word translation without parallel data.\n\\newblock In {\\em Proc. ICLR}, 2018.\n\n\\bibitem[Hewitt and Liang(2019)]{hewitt2019designing}\nJ.~Hewitt and P.~Liang.\n\\newblock Designing and interpreting probes with control tasks.\n\\newblock In {\\em Proc. EMNLP}, 2019.\n\n\\bibitem[Ji et~al.(2025)]{ji2025calibrating}\nZ.~Ji et~al.\n\\newblock Calibrating language models via internal representations.\n\\newblock In {\\em Proc. ICLR}, 2025.\n\n\\bibitem[Joshi et~al.(2025)]{joshi2025calibration}\nP.~Joshi et~al.\n\\newblock Calibration directions in the residual stream.\n\\newblock In {\\em Proc. NeurIPS}, 2025.\n\n\\bibitem[Kornblith et~al.(2019)]{kornblith2019similarity}\nS.~Kornblith, M.~Norouzi, H.~Lee, and G.~Hinton.\n\\newblock Similarity of neural network representations revisited.\n\\newblock In {\\em Proc. ICML}, 2019.\n\n\\bibitem[Miao et~al.(2026)]{miao2026coral}\nY.~Miao et~al.\n\\newblock Cross-task correctness probing via SAE analysis.\n\\newblock In {\\em Proc. ACL}, 2026.\n\n\\bibitem[Miao and Ungar(2026)]{miao2026closing}\nY.~Miao and L.~Ungar.\n\\newblock Closing the gap between correctness and confidence.\n\\newblock In {\\em Proc. NAACL}, 2026.\n\n\\bibitem[Pires et~al.(2019)]{pires2019multilingual}\nT.~Pires, E.~Schlinger, and D.~Garrette.\n\\newblock How multilingual is multilingual {BERT}?\n\\newblock In {\\em Proc. ACL}, 2019.\n\n\\bibitem[Ravisankar et~al.(2026)]{ravisankar2026dali}\nA.~Ravisankar et~al.\n\\newblock {DALI}: Cross-lingual representation alignment.\n\\newblock Preprint, 2026.\n\n\\bibitem[Wu and Dredze(2019)]{wu2019beto}\nS.~Wu and M.~Dredze.\n\\newblock Beto, bentz, becas: The surprising cross-lingual effectiveness of {BERT}.\n\\newblock In {\\em Proc. EMNLP}, 2019.\n\n\\bibitem[Xiao et~al.(2025)]{xiao2025knowledge}\nY.~Xiao et~al.\n\\newblock Cross-lingual knowledge boundary probing.\n\\newblock In {\\em Proc. ACL}, 2025.\n\n\\bibitem[Zhao et~al.(2019)]{zhao2019learning}\nH.~Zhao, R.~Tachet des Combes, K.~Zhang, and G.~Gordon.\n\\newblock On learning invariant representations for domain adaptation.\n\\newblock In {\\em Proc. ICML}, 2019.\n\n\\bibitem[Zhou et~al.(2025)]{zhou2025lace}\nK.~Zhou, D.~Jurafsky, and T.~Hashimoto.\n\\newblock {LACE}: Language-agnostic calibration via layer ensemble.\n\\newblock In {\\em Proc. ACL}, 2025.\n\n\\end{thebibliography}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 567,
        "oldLines": 97,
        "newStart": 567,
        "newLines": 97,
        "lines": [
          " % ============================================================",
          " % REFERENCES",
          " % ============================================================",
          "-\\begin{thebibliography}{30}",
          "+\\begin{thebibliography}{18}",
          " ",
          "-\\bibitem[\\protect\\citename{Angelopoulos and Bates}2023]{angelopoulos2023conformal}",
          "-Anastasios~N. Angelopoulos and Stephen Bates. 2023.",
          "+\\bibitem[Angelopoulos and Bates(2023)]{angelopoulos2023conformal}",
          "+A.~N. Angelopoulos and S.~Bates.",
          " \\newblock Conformal prediction: A gentle introduction.",
          "-\\newblock {\\em Foundations and Trends in Machine Learning}, 16(4):494--591.",
          "+\\newblock {\\em Foundations and Trends in ML}, 16(4):494--591, 2023.",
          " ",
          "-\\bibitem[\\protect\\citename{Artetxe et~al.}2018]{artetxe2018robust}",
          "-Mikel Artetxe, Gorka Labaka, and Eneko Agirre. 2018.",
          "+\\bibitem[Artetxe et~al.(2018)]{artetxe2018robust}",
          "+M.~Artetxe, G.~Labaka, and E.~Agirre.",
          " \\newblock A robust self-learning method for fully unsupervised cross-lingual mappings of word embeddings.",
          "-\\newblock In {\\em Proceedings of ACL}.",
          "+\\newblock In {\\em Proc. ACL}, 2018.",
          " ",
          "-\\bibitem[\\protect\\citename{Ben-David et~al.}2010]{bendavid2010theory}",
          "-Shai Ben-David, John Blitzer, Koby Crammer, Alex Kulesza, Fernando Pereira, and Jennifer~Wortman Vaughan. 2010.",
          "+\\bibitem[Ben-David et~al.(2010)]{bendavid2010theory}",
          "+S.~Ben-David, J.~Blitzer, K.~Crammer, A.~Kulesza, F.~Pereira, and J.~W. Vaughan.",
          " \\newblock A theory of learning from different domains.",
          "-\\newblock {\\em Machine Learning}, 79:151--175.",
          "+\\newblock {\\em Machine Learning}, 79:151--175, 2010.",
          " ",
          "-\\bibitem[\\protect\\citename{Civelli et~al.}2026]{civelli2026shared}",
          "-Matteo Civelli, Tommaso Melis, and others. 2026.",
          "+\\bibitem[Civelli et~al.(2026)]{civelli2026shared}",
          "+M.~Civelli, T.~Melis, et~al.",
          " \\newblock Shared and language-specific difficulty representations across languages.",
          "-\\newblock In {\\em Proceedings of ACL}.",
          "+\\newblock In {\\em Proc. ACL}, 2026.",
          " ",
          "-\\bibitem[\\protect\\citename{Confidence Manifold}2026]{confidence_manifold2026}",
          "-Anonymous. 2026.",
          "+\\bibitem[{Anonymous}(2026)]{confidence_manifold2026}",
          "+{Anonymous}.",
          " \\newblock The confidence manifold: Internal geometry of LLM calibration.",
          "-\\newblock Preprint.",
          "+\\newblock Preprint, 2026.",
          " ",
          "-\\bibitem[\\protect\\citename{Conneau et~al.}2018]{conneau2018word}",
          "-Alexis Conneau, Guillaume Lample, Marc'Aurelio Ranzato, Ludovic Denoyer, and Herv\\'{e} J\\'{e}gou. 2018.",
          "+\\bibitem[Conneau et~al.(2018)]{conneau2018word}",
          "+A.~Conneau, G.~Lample, M.~Ranzato, L.~Denoyer, and H.~J\\'{e}gou.",
          " \\newblock Word translation without parallel data.",
          "-\\newblock In {\\em Proceedings of ICLR}.",
          "+\\newblock In {\\em Proc. ICLR}, 2018.",
          " ",
          "-\\bibitem[\\protect\\citename{Hewitt and Liang}2019]{hewitt2019designing}",
          "-John Hewitt and Percy Liang. 2019.",
          "+\\bibitem[Hewitt and Liang(2019)]{hewitt2019designing}",
          "+J.~Hewitt and P.~Liang.",
          " \\newblock Designing and interpreting probes with control tasks.",
          "-\\newblock In {\\em Proceedings of EMNLP}.",
          "+\\newblock In {\\em Proc. EMNLP}, 2019.",
          " ",
          "-\\bibitem[\\protect\\citename{Ji et~al.}2025]{ji2025calibrating}",
          "-Ziwei Ji and others. 2025.",
          "+\\bibitem[Ji et~al.(2025)]{ji2025calibrating}",
          "+Z.~Ji et~al.",
          " \\newblock Calibrating language models via internal representations.",
          "-\\newblock In {\\em Proceedings of ICLR}.",
          "+\\newblock In {\\em Proc. ICLR}, 2025.",
          " ",
          "-\\bibitem[\\protect\\citename{Joshi et~al.}2025]{joshi2025calibration}",
          "-Pratik Joshi and others. 2025.",
          "+\\bibitem[Joshi et~al.(2025)]{joshi2025calibration}",
          "+P.~Joshi et~al.",
          " \\newblock Calibration directions in the residual stream.",
          "-\\newblock In {\\em Proceedings of NeurIPS}.",
          "+\\newblock In {\\em Proc. NeurIPS}, 2025.",
          " ",
          "-\\bibitem[\\protect\\citename{Kornblith et~al.}2019]{kornblith2019similarity}",
          "-Simon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton. 2019.",
          "+\\bibitem[Kornblith et~al.(2019)]{kornblith2019similarity}",
          "+S.~Kornblith, M.~Norouzi, H.~Lee, and G.~Hinton.",
          " \\newblock Similarity of neural network representations revisited.",
          "-\\newblock In {\\em Proceedings of ICML}.",
          "+\\newblock In {\\em Proc. ICML}, 2019.",
          " ",
          "-\\bibitem[\\protect\\citename{Miao et~al.}2026a]{miao2026coral}",
          "-Yifei Miao and others. 2026.",
          "+\\bibitem[Miao et~al.(2026)]{miao2026coral}",
          "+Y.~Miao et~al.",
          " \\newblock Cross-task correctness probing via SAE analysis.",
          "-\\newblock In {\\em Proceedings of ACL}.",
          "+\\newblock In {\\em Proc. ACL}, 2026.",
          " ",
          "-\\bibitem[\\protect\\citename{Miao and Ungar}2026]{miao2026closing}",
          "-Yifei Miao and Lyle Ungar. 2026.",
          "+\\bibitem[Miao and Ungar(2026)]{miao2026closing}",
          "+Y.~Miao and L.~Ungar.",
          " \\newblock Closing the gap between correctness and confidence.",
          "-\\newblock In {\\em Proceedings of NAACL}.",
          "+\\newblock In {\\em Proc. NAACL}, 2026.",
          " ",
          "-\\bibitem[\\protect\\citename{Pires et~al.}2019]{pires2019multilingual}",
          "-Telmo Pires, Eva Schlinger, and Dan Garrette. 2019.",
          "+\\bibitem[Pires et~al.(2019)]{pires2019multilingual}",
          "+T.~Pires, E.~Schlinger, and D.~Garrette.",
          " \\newblock How multilingual is multilingual {BERT}?",
          "-\\newblock In {\\em Proceedings of ACL}.",
          "+\\newblock In {\\em Proc. ACL}, 2019.",
          " ",
          "-\\bibitem[\\protect\\citename{Ravisankar et~al.}2026]{ravisankar2026dali}",
          "-Aditya Ravisankar and others. 2026.",
          "+\\bibitem[Ravisankar et~al.(2026)]{ravisankar2026dali}",
          "+A.~Ravisankar et~al.",
          " \\newblock {DALI}: Cross-lingual representation alignment.",
          "-\\newblock Preprint.",
          "+\\newblock Preprint, 2026.",
          " ",
          "-\\bibitem[\\protect\\citename{Wu and Dredze}2019]{wu2019beto}",
          "-Shijie Wu and Mark Dredze. 2019.",
          "+\\bibitem[Wu and Dredze(2019)]{wu2019beto}",
          "+S.~Wu and M.~Dredze.",
          " \\newblock Beto, bentz, becas: The surprising cross-lingual effectiveness of {BERT}.",
          "-\\newblock In {\\em Proceedings of EMNLP}.",
          "+\\newblock In {\\em Proc. EMNLP}, 2019.",
          " ",
          "-\\bibitem[\\protect\\citename{Xiao et~al.}2025]{xiao2025knowledge}",
          "-Yuxia Xiao and others. 2025.",
          "+\\bibitem[Xiao et~al.(2025)]{xiao2025knowledge}",
          "+Y.~Xiao et~al.",
          " \\newblock Cross-lingual knowledge boundary probing.",
          "-\\newblock In {\\em Proceedings of ACL}.",
          "+\\newblock In {\\em Proc. ACL}, 2025.",
          " ",
          "-\\bibitem[\\protect\\citename{Zhao et~al.}2019]{zhao2019learning}",
          "-Han Zhao, Remi~Tachet des Combes, Kun Zhang, and Geoffrey Gordon. 2019.",
          "+\\bibitem[Zhao et~al.(2019)]{zhao2019learning}",
          "+H.~Zhao, R.~Tachet des Combes, K.~Zhang, and G.~Gordon.",
          " \\newblock On learning invariant representations for domain adaptation.",
          "-\\newblock In {\\em Proceedings of ICML}.",
          "+\\newblock In {\\em Proc. ICML}, 2019.",
          " ",
          "-\\bibitem[\\protect\\citename{Zhou et~al.}2025]{zhou2025lace}",
          "-Kaitlyn Zhou, Dan Jurafsky, and Tatsunori Hashimoto. 2025.",
          "+\\bibitem[Zhou et~al.(2025)]{zhou2025lace}",
          "+K.~Zhou, D.~Jurafsky, and T.~Hashimoto.",
          " \\newblock {LACE}: Language-agnostic calibration via layer ensemble.",
          "-\\newblock In {\\em Proceedings of ACL}.",
          "+\\newblock In {\\em Proc. ACL}, 2025.",
          " ",
          " \\end{thebibliography}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "f7d6b3c0-3c9b-4738-a0ee-b8cfb3826292",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 51 · 2026-05-21T13:38:29.273Z_

```json
{
  "parentUuid": "7ee25c6d-8693-4fd7-84cd-0a8c56d592bb",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "877038a6-6953-41db-9390-12006dca071b",
  "timestamp": "2026-05-21T13:38:29.273Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 52_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122458 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_dire…",
  "leafUuid": "877038a6-6953-41db-9390-12006dca071b",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b"
}
```

---

### Runtime record

_source line 53_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper with experimental data",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b"
}
```

---

### Tool call

_source line 54 · 2026-05-21T13:38:32.981Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0196KeWMa2Qnn4QdTnH8RXuo`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "Compile LaTeX paper twice",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "877038a6-6953-41db-9390-12006dca071b",
  "isSidechain": false,
  "requestId": "req_011CbFoiQRCVkDDH6RXUXZy8",
  "type": "assistant",
  "uuid": "e978597a-0307-44e1-a6d2-7c8004dce1a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015DijiwpSaV9JGmncGh5P91",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3264,
      "cache_read_input_tokens": 78697,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3264,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 177,
          "cache_read_input_tokens": 78697,
          "cache_creation_input_tokens": 3264,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3264
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

_source line 55 · 2026-05-21T13:38:34.241Z_

<details><summary>↩ Tool result · `toolu_0196KeWMa2Qnn4QdTnH8RXuo`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.sty
(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)
(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype-pdftex.def)
(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.cfg))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
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
(./paper.aux)
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-ptm.cfg) (./paper.out)
(./paper.out) (/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-cmr.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-msa.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)
(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-msb.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1pcr.fd)

Package natbib Warning: Citation `zhou2025lace' on page 1 undefined on input li
ne 46.


Package natbib Warning: Citation `miao2026coral' on page 1 undefined on input l
ine 46.


Package natbib Warning: Citation `joshi2025calibration' on page 1 undefined on 
input line 46.


Package natbib Warning: Citation `confidence_manifold2026' on page 1 undefined 
on input line 46.


Package natbib Warning: Citation `miao2026closing' on page 1 undefined on input
 line 46.


Package natbib Warning: Citation `confidence_manifold2026' on page 1 undefined 
on input line 46.


Package natbib Warning: Citation `joshi2025calibration' on page 1 undefined on 
input line 46.


Package natbib Warning: Citation `xiao2025knowledge' on page 1 undefined on inp
ut line 48.


Package natbib Warning: Citation `civelli2026shared' on page 1 undefined on inp
ut line 48.


Package natbib Warning: Citation `hewitt2019designing' on page 1 undefined on i
nput line 52.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]

Package natbib Warning: Citation `joshi2025calibration' on page 2 undefined on 
input line 60.


Package natbib Warning: Citation `miao2026coral' on page 2 undefined on input l
ine 60.


Package natbib Warning: Citation `miao2026closing' on page 2 undefined on input
 line 60.


Package natbib Warning: Citation `confidence_manifold2026' on page 2 undefined 
on input line 60.


Package natbib Warning: Citation `conneau2018word' on page 2 undefined on input
 line 63.


Package natbib Warning: Citation `artetxe2018robust' on page 2 undefined on inp
ut line 63.


Package natbib Warning: Citation `pires2019multilingual' on page 2 undefined on
 input line 63.


Package natbib Warning: Citation `wu2019beto' on page 2 undefined on input line
 63.


Package natbib Warning: Citation `ravisankar2026dali' on page 2 undefined on in
put line 63.


Package natbib Warning: Citation `zhou2025lace' on page 2 undefined on input li
ne 66.


Package natbib Warning: Citation `xiao2025knowledge' on page 2 undefined on inp
ut line 66.


Package natbib Warning: Citation `bendavid2010theory' on page 2 undefined on in
put line 69.


Package natbib Warning: Citation `zhao2019learning' on page 2 undefined on inpu
t line 69.


Package natbib Warning: Citation `hewitt2019designing' on page 2 undefined on i
nput line 72.

[2]

Package natbib Warning: Citation `kornblith2019similarity' on page 3 undefined 
on input line 103.


Package natbib Warning: Citation `hewitt2019designing' on page 3 undefined on i
nput line 107.

[3] [4] [5]

Package natbib Warning: Citation `zhao2019learning' on page 6 undefined on inpu
t line 304.


Package natbib Warning: Citation `zhao2019learning' on page 6 undefined on inpu
t line 304.

[6]

Package natbib Warning: Citation `miao2026closing' on page 7 undefined on input
 line 417.

[7]

Package natbib Warning: Citation `hewitt2019designing' on page 8 undefined on i
nput line 472.

[8]

Package natbib Warning: Citation `zhao2019learning' on page 9 undefined on inpu
t line 555.

[9] [10] [11]

Package natbib Warning: There were undefined citations.

[12] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

) )&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx8.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/public/amsfonts/cm/cmmib10.pfb>&lt;/usr/share/texlive/texmf-di
st/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont
s/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm
sy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb
>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>
&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-di
st/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
urw/times/utmri8a.pfb>
Output written on paper.pdf (12 pages, 221768 bytes).
Transcript written on paper.log.
nts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips
/base/8r.enc}] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] (./paper.aux) )&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx8.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-di
st/fonts/type1/public/amsfonts/cm/cmmib10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi
c/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/
cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/us
r/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/t
imes/utmri8a.pfb>
Output written on paper.pdf (12 pages, 224569 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e978597a-0307-44e1-a6d2-7c8004dce1a7",
  "isSidechain": false,
  "promptId": "e8f1a248-e970-4548-96f9-5cd439647eab",
  "type": "user",
  "uuid": "c8564c9e-c77b-4a24-9c39-a9b015c92da5",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.sty\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype-pdftex.def)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/microtype.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-ptm.cfg) (./paper.out)\n(./paper.out) (/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-cmr.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-msa.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/microtype/mt-msb.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1pcr.fd)\n\nPackage natbib Warning: Citation `zhou2025lace' on page 1 undefined on input li\nne 46.\n\n\nPackage natbib Warning: Citation `miao2026coral' on page 1 undefined on input l\nine 46.\n\n\nPackage natbib Warning: Citation `joshi2025calibration' on page 1 undefined on \ninput line 46.\n\n\nPackage natbib Warning: Citation `confidence_manifold2026' on page 1 undefined \non input line 46.\n\n\nPackage natbib Warning: Citation `miao2026closing' on page 1 undefined on input\n line 46.\n\n\nPackage natbib Warning: Citation `confidence_manifold2026' on page 1 undefined \non input line 46.\n\n\nPackage natbib Warning: Citation `joshi2025calibration' on page 1 undefined on \ninput line 46.\n\n\nPackage natbib Warning: Citation `xiao2025knowledge' on page 1 undefined on inp\nut line 48.\n\n\nPackage natbib Warning: Citation `civelli2026shared' on page 1 undefined on inp\nut line 48.\n\n\nPackage natbib Warning: Citation `hewitt2019designing' on page 1 undefined on i\nnput line 52.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\n\nPackage natbib Warning: Citation `joshi2025calibration' on page 2 undefined on \ninput line 60.\n\n\nPackage natbib Warning: Citation `miao2026coral' on page 2 undefined on input l\nine 60.\n\n\nPackage natbib Warning: Citation `miao2026closing' on page 2 undefined on input\n line 60.\n\n\nPackage natbib Warning: Citation `confidence_manifold2026' on page 2 undefined \non input line 60.\n\n\nPackage natbib Warning: Citation `conneau2018word' on page 2 undefined on input\n line 63.\n\n\nPackage natbib Warning: Citation `artetxe2018robust' on page 2 undefined on inp\nut line 63.\n\n\nPackage natbib Warning: Citation `pires2019multilingual' on page 2 undefined on\n input line 63.\n\n\nPackage natbib Warning: Citation `wu2019beto' on page 2 undefined on input line\n 63.\n\n\nPackage natbib Warning: Citation `ravisankar2026dali' on page 2 undefined on in\nput line 63.\n\n\nPackage natbib Warning: Citation `zhou2025lace' on page 2 undefined on input li\nne 66.\n\n\nPackage natbib Warning: Citation `xiao2025knowledge' on page 2 undefined on inp\nut line 66.\n\n\nPackage natbib Warning: Citation `bendavid2010theory' on page 2 undefined on in\nput line 69.\n\n\nPackage natbib Warning: Citation `zhao2019learning' on page 2 undefined on inpu\nt line 69.\n\n\nPackage natbib Warning: Citation `hewitt2019designing' on page 2 undefined on i\nnput line 72.\n\n[2]\n\nPackage natbib Warning: Citation `kornblith2019similarity' on page 3 undefined \non input line 103.\n\n\nPackage natbib Warning: Citation `hewitt2019designing' on page 3 undefined on i\nnput line 107.\n\n[3] [4] [5]\n\nPackage natbib Warning: Citation `zhao2019learning' on page 6 undefined on inpu\nt line 304.\n\n\nPackage natbib Warning: Citation `zhao2019learning' on page 6 undefined on inpu\nt line 304.\n\n[6]\n\nPackage natbib Warning: Citation `miao2026closing' on page 7 undefined on input\n line 417.\n\n[7]\n\nPackage natbib Warning: Citation `hewitt2019designing' on page 8 undefined on i\nnput line 472.\n\n[8]\n\nPackage natbib Warning: Citation `zhao2019learning' on page 9 undefined on inpu\nt line 555.\n\n[9] [10] [11]\n\nPackage natbib Warning: There were undefined citations.\n\n[12] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n) )&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx8.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/public/amsfonts/cm/cmmib10.pfb>&lt;/usr/share/texlive/texmf-di\nst/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont\ns/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm\nsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb\n>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-di\nst/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\nurw/times/utmri8a.pfb>\nOutput written on paper.pdf (12 pages, 221768 bytes).\nTranscript written on paper.log.\nnts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips\n/base/8r.enc}] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] (./paper.aux) )&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/sh\nare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx8.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-di\nst/fonts/type1/public/amsfonts/cm/cmmib10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi\nc/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\ncmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/us\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texliv\ne/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/t\nimes/utmri8a.pfb>\nOutput written on paper.pdf (12 pages, 224569 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "e978597a-0307-44e1-a6d2-7c8004dce1a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 56 · 2026-05-21T13:38:40.954Z_

<details><summary>Logged reasoning block</summary>

```text
The PDF compiled successfully but citations are still undefined. The problem is that natbib needs a third pass. Actually the issue is that the citations in the text use `\cite{}` and `\citet{}` but the thebibliography entries need to match. Let me run a third pass.

Actually, the issue is that the warnings say "Citation(s) may have changed. Rerun to get citations correct." This means we need a third compilation pass. Let me run one more.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8564c9e-c77b-4a24-9c39-a9b015c92da5",
  "isSidechain": false,
  "requestId": "req_011CbFoimhcjbonUK89jswy5",
  "type": "assistant",
  "uuid": "95b0184e-9c0b-41f0-a208-7a469c71c6a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019jQ58zZoRnyAHATpMguu4q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4876,
      "cache_read_input_tokens": 81961,
      "output_tokens": 305,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4876,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 305,
          "cache_read_input_tokens": 81961,
          "cache_creation_input_tokens": 4876,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4876
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

_source line 57 · 2026-05-21T13:38:40.989Z_

Need one more pass to resolve citations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95b0184e-9c0b-41f0-a208-7a469c71c6a0",
  "isSidechain": false,
  "requestId": "req_011CbFoimhcjbonUK89jswy5",
  "type": "assistant",
  "uuid": "d586edee-069f-45ed-b774-e297be72dd56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019jQ58zZoRnyAHATpMguu4q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4876,
      "cache_read_input_tokens": 81961,
      "output_tokens": 305,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4876,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 305,
          "cache_read_input_tokens": 81961,
          "cache_creation_input_tokens": 4876,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4876
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

_source line 58 · 2026-05-21T13:38:51.679Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Q8pHPWWGP1seByTs6pgx5Y`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | grep -E \"(Output written|Warning|Error)\" | head -10",
  "description": "Third LaTeX pass to resolve citations",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d586edee-069f-45ed-b774-e297be72dd56",
  "isSidechain": false,
  "requestId": "req_011CbFoimhcjbonUK89jswy5",
  "type": "assistant",
  "uuid": "843bdb85-6136-4cff-b4f4-1e5991a473f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019jQ58zZoRnyAHATpMguu4q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4876,
      "cache_read_input_tokens": 81961,
      "output_tokens": 305,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4876,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 305,
          "cache_read_input_tokens": 81961,
          "cache_creation_input_tokens": 4876,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4876
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

_source line 59 · 2026-05-21T13:38:52.350Z_

<details><summary>↩ Tool result · `toolu_01Q8pHPWWGP1seByTs6pgx5Y`</summary>

```text
Output written on paper.pdf (12 pages, 224569 bytes).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "843bdb85-6136-4cff-b4f4-1e5991a473f4",
  "isSidechain": false,
  "promptId": "e8f1a248-e970-4548-96f9-5cd439647eab",
  "type": "user",
  "uuid": "9924abbd-28c8-477e-8e1c-5cf51fc41b90",
  "toolUseResult": {
    "stdout": "Output written on paper.pdf (12 pages, 224569 bytes).",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "843bdb85-6136-4cff-b4f4-1e5991a473f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 60 · 2026-05-21T13:38:55.311Z_

Compiled cleanly. 12-page PDF with no warnings on the third pass. Let me verify the output.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9924abbd-28c8-477e-8e1c-5cf51fc41b90",
  "isSidechain": false,
  "requestId": "req_011CbFok77wxjpoCMhGLcKkU",
  "type": "assistant",
  "uuid": "5e8c41e2-1b94-477f-a73b-a7cc1b358b02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018LVfp5Ub3Q1VzE4tzXZkt7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 286,
      "cache_read_input_tokens": 86837,
      "output_tokens": 149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 286,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 149,
          "cache_read_input_tokens": 86837,
          "cache_creation_input_tokens": 286,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 286
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

_source line 61 · 2026-05-21T13:38:57.746Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01NMC4NCjXEBTmXuHRQuGhkJ`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median/paper.pdf",
  "description": "Verify PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e8c41e2-1b94-477f-a73b-a7cc1b358b02",
  "isSidechain": false,
  "requestId": "req_011CbFok77wxjpoCMhGLcKkU",
  "type": "assistant",
  "uuid": "33f763ae-74b0-4d2f-931f-5d86cd995144",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018LVfp5Ub3Q1VzE4tzXZkt7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 286,
      "cache_read_input_tokens": 86837,
      "output_tokens": 149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 286,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 149,
          "cache_read_input_tokens": 86837,
          "cache_creation_input_tokens": 286,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 286
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

_source line 62 · 2026-05-21T13:38:57.808Z_

<details><summary>↩ Tool result · `toolu_01NMC4NCjXEBTmXuHRQuGhkJ`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 224569 May 21 13:38 /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33f763ae-74b0-4d2f-931f-5d86cd995144",
  "isSidechain": false,
  "promptId": "e8f1a248-e970-4548-96f9-5cd439647eab",
  "type": "user",
  "uuid": "7b57e95d-3900-4c87-b387-7c4ee8731f2e",
  "toolUseResult": {
    "stdout": "-rw-r--r-- 1 ubuntu ubuntu 224569 May 21 13:38 /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median/paper.pdf",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "33f763ae-74b0-4d2f-931f-5d86cd995144",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 63_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122458 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_dire…",
  "leafUuid": "7b57e95d-3900-4c87-b387-7c4ee8731f2e",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b"
}
```

---

### Runtime record

_source line 64_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper with experimental data",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b"
}
```

---

### Assistant

_source line 65 · 2026-05-21T13:39:10.690Z_

论文已生成：`paper.pdf`（12 页，225KB）。

**覆盖的实验 / 对应章节**：

| 实验 | 章节 |
|------|------|
| Pareto Frontier (Qwen3/Llama4/Gemma4) | §4.1 + Table 1-2 |
| CKA & Simpson's Paradox | §4.2 + Table 3-5 |
| CaCLR 负结果 + β sweep + CORAL + high-dim MMD | §4.3 + Table 6-8 |
| Transfer method 全对比 | §4.4 + Table 9 |
| Linear projection 饱和曲线 + Procrustes reversal | §4.5 + Table 10-11 |
| Difficulty decomposition | §4.6 + Table 12 |
| 正交性 | §4.7 |
| Probe complexity (LR vs MLP) | §4.8 + Table 13 |
| Cross-benchmark (Belebele/MMLU-ProX) | §4.9 + Table 14 |
| Probing controls | §4.10 + Table 15 |
| Quantization validation | §4.11 + Table 16 |
| 52-language extension | §4.12 + Table 17 |

所有定量数据来自 `experiment_data.json`，无编造数字。叙事按 narrative guidance 执行：CaCLR 负结果为核心，Claim 2 压缩为 descriptive subsection，headline 聚焦 architecture-dependent depth effects + linear projection practical solution。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b57e95d-3900-4c87-b387-7c4ee8731f2e",
  "isSidechain": false,
  "requestId": "req_011CbFokWRufsBHKXRG24hUU",
  "type": "assistant",
  "uuid": "d593fefb-fa9a-4198-9545-69f274c1922c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/median",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JYu4PQ3Pn2EKohzivikVrc",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 236,
      "cache_read_input_tokens": 87123,
      "output_tokens": 433,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 236,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 433,
          "cache_read_input_tokens": 87123,
          "cache_creation_input_tokens": 236,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 236
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

_source line 66_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122458 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_dire…",
  "leafUuid": "d593fefb-fa9a-4198-9545-69f274c1922c",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b"
}
```

---

### Runtime record

_source line 67_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper with experimental data",
  "sessionId": "7a93ce26-60b3-4962-9826-30997b183b7b"
}
```

---
