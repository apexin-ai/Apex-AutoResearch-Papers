# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T201854 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-2/5686fd8c-ab8d-4a40-ad31-d7215e789135.jsonl`
- **Structured JSON:** [`cdabc310c27b2dea4f09.json`](../../sessions/cd/cdabc310c27b2dea4f09.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T20:53:36.116Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T20:53:36.116Z",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T201854 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Reframe as field-level empirical survey: \"Does probe-based calibration work beyond English? A systematic investigation across 2 architectures and 20 languages.\" Three surviving novel contributions: (1) mean-shift rank-invariance theorem with proof — explains why mean-shift fails (ΔAUROC ≡ 0 under StandardScaler + logistic regression), distinguishing from Xiao et al.; (2) resource-tier taxonomy of cross-lingual probe transferability — first quantification across 20 languages showing high-resource transfers, mid is marginal, low fails; (3) practical recommendation — few-shot (25–100 labels) is the only viable path, closing the zero-label dream for low-resource languages. CaCLR is relegated to one paragraph as attempted-and-failed (consistency loss inert, SB-ECE alone insufficient). Decomposition is reported as inconclusive (difficulty removal neither helps nor hurts transfer systematically). Pareto frontier is real on Qwen3 but flat/non-monotonic on Llama 4 Scout — architecture-dependent, not universal. CKA provides suggestive but not convincing mechanistic explanation (r < 0.45). Orthogonality persists broadly but with outliers (cosine up to 0.17 for low-resource), weakening the universality claim. Control tasks reveal capacity artifacts in low-resource settings (selectivity < 8pp). Paper becomes a \"sobering empirical reality check\" for the probe-based calibration line. Target: borderline at EACL, requires very clean writing and strong related-work positioning.\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T20:53:36.119Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T20:53:36.119Z",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135"
}
```

---

## Round 1

41 recorded events

### User

_source line 3 · 2026-05-20T20:53:36.158Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T201854 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Reframe as field-level empirical survey: "Does probe-based calibration work beyond English? A systematic investigation across 2 architectures and 20 languages." Three surviving novel contributions: (1) mean-shift rank-invariance theorem with proof — explains why mean-shift fails (ΔAUROC ≡ 0 under StandardScaler + logistic regression), distinguishing from Xiao et al.; (2) resource-tier taxonomy of cross-lingual probe transferability — first quantification across 20 languages showing high-resource transfers, mid is marginal, low fails; (3) practical recommendation — few-shot (25–100 labels) is the only viable path, closing the zero-label dream for low-resource languages. CaCLR is relegated to one paragraph as attempted-and-failed (consistency loss inert, SB-ECE alone insufficient). Decomposition is reported as inconclusive (difficulty removal neither helps nor hurts transfer systematically). Pareto frontier is real on Qwen3 but flat/non-monotonic on Llama 4 Scout — architecture-dependent, not universal. CKA provides suggestive but not convincing mechanistic explanation (r < 0.45). Orthogonality persists broadly but with outliers (cosine up to 0.17 for low-resource), weakening the universality claim. Control tasks reveal capacity artifacts in low-resource settings (selectivity < 8pp). Paper becomes a "sobering empirical reality check" for the probe-based calibration line. Target: borderline at EACL, requires very clean writing and strong related-work positioning.

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "ce9c66bf-f5bc-46b5-95a4-aabc6b39fe73",
  "type": "user",
  "uuid": "b6ca3ef8-eb55-41ec-8567-5d2dd0e0b30c",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T20:53:36.157Z_

```json
{
  "parentUuid": "b6ca3ef8-eb55-41ec-8567-5d2dd0e0b30c",
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
  "uuid": "dedc60ac-ef9d-46bf-9723-4f75c15b7167",
  "timestamp": "2026-05-20T20:53:36.157Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T20:53:36.157Z_

```json
{
  "parentUuid": "dedc60ac-ef9d-46bf-9723-4f75c15b7167",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "657b7687-7d14-4598-8c28-a86a9b729527",
  "timestamp": "2026-05-20T20:53:36.157Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135",
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
  "aiTitle": "Generate simulated ML research paper with experiments",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135"
}
```

---

### Assistant

_source line 7 · 2026-05-20T20:53:39.345Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "657b7687-7d14-4598-8c28-a86a9b729527",
  "isSidechain": false,
  "requestId": "req_011CbEV5waKHbq9sDtoffvLD",
  "type": "assistant",
  "uuid": "56bb3248-0569-4632-a6ac-9add724e39fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BrLLgXZiiBTaaKDFXmPV4J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11677,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11677,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11677,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11677
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

_source line 8 · 2026-05-20T20:53:40.305Z_

<details open><summary>🔧 Tool call — Read · `toolu_011DFnBbhMtViVExaDVuCJ7X`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56bb3248-0569-4632-a6ac-9add724e39fd",
  "isSidechain": false,
  "requestId": "req_011CbEV5waKHbq9sDtoffvLD",
  "type": "assistant",
  "uuid": "aac4c323-aec4-4c4a-ba9e-5b14a96da12e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BrLLgXZiiBTaaKDFXmPV4J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11677,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11677,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11677,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11677
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

_source line 9 · 2026-05-20T20:53:40.596Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FhjBYr5JHJh3XfVfojGWKi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aac4c323-aec4-4c4a-ba9e-5b14a96da12e",
  "isSidechain": false,
  "requestId": "req_011CbEV5waKHbq9sDtoffvLD",
  "type": "assistant",
  "uuid": "ce91d5c1-6a9f-42a8-a7d5-2738501e9def",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BrLLgXZiiBTaaKDFXmPV4J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11677,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11677,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11677,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11677
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

_source line 10 · 2026-05-20T20:53:40.615Z_

<details><summary>↩ Tool result · `toolu_011DFnBbhMtViVExaDVuCJ7X`</summary>

```text
1	[
2	  {
3	    "name": "Full Pareto Frontier — Qwen3-235B-A22B (94 layers, MoE, INT8)",
4	    "description": "Extract activations at 24 probed layers (every 4th of 94), 20 languages on GlobalMMLU. Train English logistic regression + 2-layer MLP correctness probes. Evaluate 5 transfer conditions: zero-shot, mean-shift, linear projection, few-shot (25/100), CaCLR. Report per-language Spearman ρ (depth vs transfer AUROC) alongside global ρ. Bootstrap CIs (1000 resamples) on all AUROC/ECE; paired permutation tests for method comparisons; Cohen's d for effect sizes.\n",
5	    "results": {
6	      "en_auroc_best_layer": 0.776,
7	      "en_best_layer_idx": 72,
8	      "en_auroc_range": [
9	        0.612,
10	        0.776
11	      ],
12	      "en_ece_raw_best": 0.174,
13	      "en_ece_tempcal_best": 0.069,
14	      "temp_scaling_T": 5.91,
15	      "zs_transfer_auroc_mean_19lang": 0.618,
16	      "zs_transfer_auroc_median_19lang": 0.618,
17	      "zs_transfer_auroc_std_19lang": 0.046,
18	      "zs_transfer_drop_mean_pp": 15.8,
19	      "zs_langs_above_0p65": 7,
20	      "zs_pass_langs": [
21	        "zh",
22	        "fr",
23	        "de",
24	        "es",
25	        "ja",
26	        "ko",
27	        "ru"
28	      ],
29	      "zs_fail_langs": [
30	        "ar",
31	        "hi",
32	        "vi",
33	        "id",
34	        "th",
35	        "pl",
36	        "uk",
37	        "bn",
38	        "te",
39	        "ta",
40	        "sw",
41	        "yo"
42	      ],
43	      "mean_shift_delta_auroc_all_langs": 0.0,
44	      "mean_shift_delta_ece_unreliable": true,
45	      "mean_shift_delta_ece_range_pp": [
46	        -1.2,
47	        6.8
48	      ],
49	      "linproj_auroc_mean_19lang": 0.636,
50	      "linproj_improves_over_zs_count": 11,
51	      "linproj_delta_auroc_vs_zs_mean_pp": 1.8,
52	      "fewshot25_auroc_mean_19lang": 0.644,
53	      "fewshot25_improves_over_zs_count": 14,
54	      "fewshot100_auroc_mean_19lang": 0.662,
55	      "fewshot100_improves_over_zs_count": 16,
56	      "pareto_global_spearman_rho": -0.38,
57	      "pareto_per_lang_rho_median": -0.25,
58	      "pareto_per_lang_rho_range": [
59	        -0.55,
60	        0.31
61	      ],
62	      "pareto_rho_sign_consistency": 0.63,
63	      "pareto_frontier_n_nondominated": 5,
64	      "pareto_frontier_monotonic": false,
65	      "bootstrap_ci_width_auroc_median_pp": 2.8,
66	      "per_lang_zs_auroc": {
67	        "zh": 0.668,
68	        "fr": 0.672,
69	        "de": 0.671,
70	        "es": 0.661,
71	        "ja": 0.658,
72	        "ko": 0.656,
73	        "ru": 0.652,
74	        "ar": 0.625,
75	        "hi": 0.618,
76	        "vi": 0.607,
77	        "id": 0.621,
78	        "th": 0.594,
79	        "pl": 0.628,
80	        "uk": 0.614,
81	        "bn": 0.553,
82	        "te": 0.571,
83	        "ta": 0.568,
84	        "sw": 0.537,
85	        "yo": 0.512
86	      },
87	      "per_lang_best_zs_layer": {
88	        "zh": 52,
89	        "fr": 52,
90	        "de": 52,
91	        "es": 48,
92	        "ja": 48,
93	        "ko": 48,
94	        "ru": 44,
95	        "ar": 40,
96	        "hi": 40,
97	        "vi": 40,
98	        "id": 40,
99	        "th": 36,
100	        "pl": 44,
101	        "uk": 40,
102	        "bn": 28,
103	        "te": 28,
104	        "ta": 28,
105	        "sw": 28,
106	        "yo": 24
107	      },
108	      "per_lang_spearman_rho": {
109	        "zh": -0.55,
110	        "fr": -0.51,
111	        "de": -0.48,
112	        "es": -0.42,
113	        "ja": -0.37,
114	        "ko": -0.33,
115	        "ru": -0.25,
116	        "ar": -0.18,
117	        "hi": -0.11,
118	        "pl": -0.14,
119	        "uk": -0.06,
120	        "id": -0.02,
121	        "vi": 0.04,
122	        "th": 0.09,
123	        "bn": 0.14,
124	        "te": 0.18,
125	        "ta": 0.22,
126	        "sw": 0.27,
127	        "yo": 0.31
128	      },
129	      "transfer_by_resource_tier": {
130	        "high_mean": 0.663,
131	        "high_langs": [
132	          "zh",
133	          "fr",
134	          "de",
135	          "es",
136	          "ja",
137	          "ko",
138	          "ru"
139	        ],
140	        "mid_mean": 0.615,
141	        "mid_langs": [
142	          "ar",
143	          "hi",
144	          "vi",
145	          "id",
146	          "th",
147	          "pl",
148	          "uk"
149	        ],
150	        "low_mean": 0.548,
151	        "low_langs": [
152	          "bn",
153	          "te",
154	          "ta",
155	          "sw",
156	          "yo"
157	        ]
158	      }
159	    },
160	    "tables": [
161	      {
162	        "name": "Table 1: Qwen3-235B English Probe Performance by Layer (Selected Layers)",
163	        "columns": [
164	          "layer",
165	          "depth_pct",
166	          "logreg_auroc",
167	          "mlp_auroc",
168	          "ece_raw",
169	          "ece_tempcal"
170	        ],
171	        "rows": [
172	          [
173	            4,
174	            4,
175	            0.612,
176	            0.618,
177	            0.298,
178	            0.192
179	          ],
180	          [
181	            16,
182	            17,
183	            0.653,
184	            0.661,
185	            0.251,
186	            0.148
187	          ],
188	          [
189	            28,
190	            30,
191	            0.694,
192	            0.708,
193	            0.224,
194	            0.121
195	          ],
196	          [
197	            40,
198	            43,
199	            0.721,
200	            0.737,
201	            0.203,
202	            0.098
203	          ],
204	          [
205	            52,
206	            55,
207	            0.742,
208	            0.755,
209	            0.191,
210	            0.082
211	          ],
212	          [
213	            60,
214	            64,
215	            0.758,
216	            0.769,
217	            0.183,
218	            0.075
219	          ],
220	          [
221	            72,
222	            77,
223	            0.776,
224	            0.783,
225	            0.174,
226	            0.069
227	          ],
228	          [
229	            80,
230	            85,
231	            0.771,
232	            0.779,
233	            0.177,
234	            0.072
235	          ],
236	          [
237	            88,
238	            94,
239	            0.753,
240	            0.762,
241	            0.186,
242	            0.079
243	          ],
244	          [
245	            92,
246	            98,
247	            0.728,
248	            0.739,
249	            0.198,
250	            0.091
251	          ]
252	        ]
253	      },
254	      {
255	        "name": "Table 2: Qwen3-235B Zero-Shot Transfer AUROC by Language (Best Transfer Layer)",
256	        "columns": [
257	          "language",
258	          "family",
259	          "resource_tier",
260	          "best_zs_layer",
261	          "best_zs_auroc",
262	          "en_auroc_same_layer",
263	          "drop_pp",
264	          "spearman_rho",
265	          "rho_p_value"
266	        ],
267	        "rows": [
268	          [
269	            "zh",
270	            "sino_tibetan",
271	            "high",
272	            52,
273	            0.668,
274	            0.742,
275	            7.4,
276	            -0.55,
277	            0.006
278	          ],
279	          [
280	            "fr",
281	            "romance",
282	            "high",
283	            52,
284	            0.672,
285	            0.742,
286	            7.0,
287	            -0.51,
288	            0.011
289	          ],
290	          [
291	            "de",
292	            "germanic",
293	            "high",
294	            52,
295	            0.671,
296	            0.742,
297	            7.1,
298	            -0.48,
299	            0.017
300	          ],
301	          [
302	            "es",
303	            "romance",
304	            "high",
305	            48,
306	            0.661,
307	            0.735,
308	            7.4,
309	            -0.42,
310	            0.041
311	          ],
312	          [
313	            "ja",
314	            "japonic",
315	            "high",
316	            48,
317	            0.658,
318	            0.735,
319	            7.7,
320	            -0.37,
321	            0.075
322	          ],
323	          [
324	            "ko",
325	            "koreanic",
326	            "high",
327	            48,
328	            0.656,
329	            0.735,
330	            7.9,
331	            -0.33,
332	            0.115
333	          ],
334	          [
335	            "ru",
336	            "slavic",
337	            "high",
338	            44,
339	            0.652,
340	            0.728,
341	            7.6,
342	            -0.25,
343	            0.239
344	          ],
345	          [
346	            "pl",
347	            "slavic",
348	            "mid",
349	            44,
350	            0.628,
351	            0.728,
352	            10.0,
353	            -0.14,
354	            0.513
355	          ],
356	          [
357	            "ar",
358	            "afroasiatic",
359	            "mid",
360	            40,
361	            0.625,
362	            0.721,
363	            9.6,
364	            -0.18,
365	            0.399
366	          ],
367	          [
368	            "id",
369	            "austronesian",
370	            "mid",
371	            40,
372	            0.621,
373	            0.721,
374	            10.0,
375	            -0.02,
376	            0.926
377	          ],
378	          [
379	            "hi",
380	            "indic",
381	            "mid",
382	            40,
383	            0.618,
384	            0.721,
385	            10.3,
386	            -0.11,
387	            0.609
388	          ],
389	          [
390	            "uk",
391	            "slavic",
392	            "mid",
393	            40,
394	            0.614,
395	            0.721,
396	            10.7,
397	            -0.06,
398	            0.782
399	          ],
400	          [
401	            "vi",
402	            "austroasiatic",
403	            "mid",
404	            40,
405	            0.607,
406	            0.721,
407	            11.4,
408	            0.04,
409	            0.854
410	          ],
411	          [
412	            "th",
413	            "tai_kadai",
414	            "mid",
415	            36,
416	            0.594,
417	            0.712,
418	            11.8,
419	            0.09,
420	            0.674
421	          ],
422	          [
423	            "bn",
424	            "indic",
425	            "low",
426	            28,
427	            0.553,
428	            0.694,
429	            14.1,
430	            0.14,
431	            0.514
432	          ],
433	          [
434	            "te",
435	            "dravidian",
436	            "low",
437	            28,
438	            0.571,
439	            0.694,
440	            12.3,
441	            0.18,
442	            0.4
443	          ],
444	          [
445	            "ta",
446	            "dravidian",
447	            "low",
448	            28,
449	            0.568,
450	            0.694,
451	            12.6,
452	            0.22,
453	            0.303
454	          ],
455	          [
456	            "sw",
457	            "niger_congo",
458	            "low",
459	            28,
460	            0.537,
461	            0.694,
462	            15.7,
463	            0.27,
464	            0.202
465	          ],
466	          [
467	            "yo",
468	            "niger_congo",
469	            "low",
470	            24,
471	            0.512,
472	            0.711,
473	            19.9,
474	            0.31,
475	            0.141
476	          ]
477	        ]
478	      },
479	      {
480	        "name": "Table 3: Qwen3-235B Transfer Method Comparison (19-Language Mean at Oracle Layer)",
481	        "columns": [
482	          "method",
483	          "auroc_mean",
484	          "auroc_median",
485	          "auroc_std",
486	          "ece_mean",
487	          "delta_vs_zs_pp",
488	          "cohens_d_vs_zs",
489	          "labels_needed"
490	        ],
491	        "rows": [
492	          [
493	            "zero_shot",
494	            0.618,
495	            0.618,
496	            0.046,
497	            0.191,
498	            0.0,
499	            "—",
500	            0
501	          ],
502	          [
503	            "mean_shift",
504	            0.618,
505	            0.618,
506	            0.046,
507	            0.207,
508	            0.0,
509	            0.0,
510	            0
511	          ],
512	          [
513	            "linear_projection",
514	            0.636,
515	            0.633,
516	            0.042,
517	            0.176,
518	            1.8,
519	            0.24,
520	            "~50 parallel"
521	          ],
522	          [
523	            "few_shot_25",
524	            0.644,
525	            0.641,
526	            0.04,
527	            0.169,
528	            2.6,
529	            0.35,
530	            "25 target"
531	          ],
532	          [
533	            "few_shot_100",
534	            0.662,
535	            0.659,
536	            0.037,
537	            0.154,
538	            4.4,
539	            0.58,
540	            "100 target"
541	          ]
542	        ]
543	      }
544	    ],
545	    "figures": [],
546	    "analysis": "Pareto frontier on Qwen3-235B is real but weak: ρ = −0.38 globally, median per-language ρ = −0.25 (explains ~6% of per-language variance). The resource-tier gradient is the cleanest finding: high-resource langs (mean 0.663) transfer at 7–8pp below EN, mid-resource (0.615) at 10–11pp, low-resource (0.548) at 13–20pp. Mean-shift is confirmed mathematically dead (ΔAUROC ≡ 0, validated across all 24 layers × 19 langs). Linear projection and few-shot are the only viable transfer methods. For 12/19 languages, zero-shot transfer AUROC stays below 0.65 — the field should not assume English probes generalize.\n\n\nQwen3-235B improves only modestly over the MVP's Qwen2.5-7B (EN AUROC 0.776 vs 0.754) because gains from scale are sublinear for linear probing — the larger model has more complex, distributed representations where correctness is encoded across many dimensions rather than in a single cleanly accessible direction. The Pareto frontier exists but is noisy: global Spearman ρ = -0.38 means depth explains ~15% of transfer variance. Per-language rho varies dramatically — high-resource languages that share subspace structure with English (zh, fr, de) show clear negative correlation (deeper = worse transfer), while low-resource languages (sw, yo, ta) show positive or near-zero rho because their best transfer happens at shallow layers where representations are still language-agnostic, and the signal is too weak at any depth for a clear depth gradient to emerge. MoE expert routing introduces non-monotonic noise at mid-depth layers (36-56) where routing patterns shift. Mean-shift ΔAUROC is exactly 0.000 across all languages and layers, confirming the rank-invariance proof: under StandardScaler + logistic regression, mean subtraction adds a constant to all logits, preserving ranks. ECE changes from mean-shift are unreliable because they depend on threshold-sensitive binning of shifted probabilities. Linear projection helps 11/19 languages by learning the affine transformation between language subspaces, but fails for low-resource languages where insufficient parallel data quality prevents reliable transformation estimation. Few-shot-100 is the best method but requires per-language labels, partially negating the zero-label promise.\n"
547	  },
548	  {
549	    "name": "Full Pareto Frontier — Llama 4 Scout (48 layers, MoE, INT8)",
550	    "description": "Extract activations at 12 probed layers (every 4th of 48), 20 languages on GlobalMMLU. Train English correctness probes, evaluate 5 transfer conditions. INT8 weight quantization. Report per-language Spearman ρ. Bootstrap CIs + paired tests + Cohen's d.\n",
551	    "results": {
552	      "en_auroc_best_layer": 0.749,
553	      "en_best_layer_idx": 36,
554	      "en_auroc_range": [
555	        0.598,
556	        0.749
557	      ],
558	      "en_ece_raw_best": 0.188,
559	      "en_ece_tempcal_best": 0.074,
560	      "temp_scaling_T": 5.47,
561	      "zs_transfer_auroc_mean_19lang": 0.588,
562	      "zs_transfer_auroc_median_19lang": 0.593,
563	      "zs_transfer_auroc_std_19lang": 0.054,
564	      "zs_transfer_drop_mean_pp": 18.4,
565	      "zs_langs_above_0p65": 5,
566	      "zs_pass_langs": [
567	        "fr",
568	        "zh",
569	        "de",
570	        "ko",
571	        "es"
572	      ],
573	      "zs_fail_langs": [
574	        "ja",
575	        "ru",
576	        "ar",
577	        "hi",
578	        "vi",
579	        "id",
580	        "th",
581	        "pl",
582	        "uk",
583	        "bn",
584	        "te",
585	        "ta",
586	        "sw",
587	        "yo"
588	      ],
589	      "mean_shift_delta_auroc_all_langs": 0.0,
590	      "linproj_auroc_mean_19lang": 0.608,
591	      "linproj_improves_over_zs_count": 10,
592	      "fewshot25_auroc_mean_19lang": 0.617,
593	      "fewshot100_auroc_mean_19lang": 0.641,
594	      "pareto_global_spearman_rho": -0.18,
595	      "pareto_per_lang_rho_median": -0.12,
596	      "pareto_per_lang_rho_range": [
597	        -0.41,
598	        0.48
599	      ],
600	      "pareto_rho_sign_consistency": 0.53,
601	      "pareto_frontier_n_nondominated": 3,
602	      "pareto_frontier_monotonic": false,
603	      "pareto_frontier_agreement_with_qwen3_tau": 0.33,
604	      "nonmonotonic_layers": [
605	        20,
606	        24,
607	        28
608	      ],
609	      "per_lang_zs_auroc": {
610	        "fr": 0.662,
611	        "zh": 0.658,
612	        "de": 0.655,
613	        "ko": 0.652,
614	        "es": 0.651,
615	        "ja": 0.634,
616	        "ru": 0.622,
617	        "pl": 0.608,
618	        "ar": 0.589,
619	        "hi": 0.586,
620	        "id": 0.582,
621	        "uk": 0.578,
622	        "vi": 0.571,
623	        "th": 0.558,
624	        "bn": 0.532,
625	        "te": 0.541,
626	        "ta": 0.528,
627	        "sw": 0.518,
628	        "yo": 0.492
629	      },
630	      "per_lang_spearman_rho": {
631	        "fr": -0.41,
632	        "zh": -0.37,
633	        "de": -0.32,
634	        "ko": -0.21,
635	        "es": -0.18,
636	        "ja": -0.08,
637	        "ru": -0.04,
638	        "pl": 0.03,
639	        "ar": 0.07,
640	        "hi": 0.11,
641	        "id": 0.15,
642	        "uk": 0.18,
643	        "vi": 0.22,
644	        "th": 0.28,
645	        "bn": 0.31,
646	        "te": 0.35,
647	        "ta": 0.38,
648	        "sw": 0.43,
649	        "yo": 0.48
650	      }
651	    },
652	    "tables": [
653	      {
654	        "name": "Table 4: Llama 4 Scout English Probe Performance by Layer",
655	        "columns": [
656	          "layer",
657	          "depth_pct",
658	          "logreg_auroc",
659	          "mlp_auroc",
660	          "ece_raw",
661	          "ece_tempcal"
662	        ],
663	        "rows": [
664	          [
665	            4,
666	            8,
667	            0.598,
668	            0.604,
669	            0.312,
670	            0.201
671	          ],
672	          [
673	            8,
674	            17,
675	            0.631,
676	            0.641,
677	            0.274,
678	            0.168
679	          ],
680	          [
681	            12,
682	            25,
683	            0.668,
684	            0.679,
685	            0.241,
686	            0.137
687	          ],
688	          [
689	            16,
690	            33,
691	            0.694,
692	            0.706,
693	            0.218,
694	            0.112
695	          ],
696	          [
697	            20,
698	            42,
699	            0.712,
700	            0.722,
701	            0.205,
702	            0.098
703	          ],
704	          [
705	            24,
706	            50,
707	            0.726,
708	            0.735,
709	            0.196,
710	            0.088
711	          ],
712	          [
713	            28,
714	            58,
715	            0.734,
716	            0.743,
717	            0.192,
718	            0.083
719	          ],
720	          [
721	            32,
722	            67,
723	            0.741,
724	            0.749,
725	            0.189,
726	            0.078
727	          ],
728	          [
729	            36,
730	            75,
731	            0.749,
732	            0.755,
733	            0.188,
734	            0.074
735	          ],
736	          [
737	            40,
738	            83,
739	            0.744,
740	            0.751,
741	            0.19,
742	            0.077
743	          ],
744	          [
745	            44,
746	            92,
747	            0.731,
748	            0.738,
749	            0.195,
750	            0.084
751	          ],
752	          [
753	            48,
754	            100,
755	            0.708,
756	            0.718,
757	            0.209,
758	            0.097
759	          ]
760	        ]
761	      },
762	      {
763	        "name": "Table 5: Llama 4 Scout Zero-Shot Transfer AUROC by Language",
764	        "columns": [
765	          "language",
766	          "resource_tier",
767	          "best_zs_layer",
768	          "best_zs_auroc",
769	          "drop_vs_en_pp",
770	          "spearman_rho"
771	        ],
772	        "rows": [
773	          [
774	            "fr",
775	            "high",
776	            24,
777	            0.662,
778	            6.4,
779	            -0.41
780	          ],
781	          [
782	            "zh",
783	            "high",
784	            24,
785	            0.658,
786	            6.8,
787	            -0.37
788	          ],
789	          [
790	            "de",
791	            "high",
792	            24,
793	            0.655,
794	            7.1,
795	            -0.32
796	          ],
797	          [
798	            "ko",
799	            "high",
800	            20,
801	            0.652,
802	            6.0,
803	            -0.21
804	          ],
805	          [
806	            "es",
807	            "high",
808	            24,
809	            0.651,
810	            7.5,
811	            -0.18
812	          ],
813	          [
814	            "ja",
815	            "high",
816	            20,
817	            0.634,
818	            7.8,
819	            -0.08
820	          ],
821	          [
822	            "ru",
823	            "high",
824	            20,
825	            0.622,
826	            9.0,
827	            -0.04
828	          ],
829	          [
830	            "pl",
831	            "mid",
832	            20,
833	            0.608,
834	            10.4,
835	            0.03
836	          ],
837	          [
838	            "ar",
839	            "mid",
840	            16,
841	            0.589,
842	            10.5,
843	            0.07
844	          ],
845	          [
846	            "hi",
847	            "mid",
848	            16,
849	            0.586,
850	            10.8,
851	            0.11
852	          ],
853	          [
854	            "id",
855	            "mid",
856	            16,
857	            0.582,
858	            11.2,
859	            0.15
860	          ],
861	          [
862	            "uk",
863	            "mid",
864	            16,
865	            0.578,
866	            11.6,
867	            0.18
868	          ],
869	          [
870	            "vi",
871	            "mid",
872	            16,
873	            0.571,
874	            12.3,
875	            0.22
876	          ],
877	          [
878	            "th",
879	            "mid",
880	            16,
881	            0.558,
882	            13.6,
883	            0.28
884	          ],
885	          [
886	            "te",
887	            "low",
888	            12,
889	            0.541,
890	            12.7,
891	            0.35
892	          ],
893	          [
894	            "bn",
895	            "low",
896	            12,
897	            0.532,
898	            13.6,
899	            0.31
900	          ],
901	          [
902	            "ta",
903	            "low",
904	            12,
905	            0.528,
906	            14.0,
907	            0.38
908	          ],
909	          [
910	            "sw",
911	            "low",
912	            12,
913	            0.518,
914	            15.0,
915	            0.43
916	          ],
917	          [
918	            "yo",
919	            "low",
920	            8,
921	            0.492,
922	            13.9,
923	            0.48
924	          ]
925	        ]
926	      },
927	      {
928	        "name": "Table 6: Cross-Architecture Pareto Agreement",
929	        "columns": [
930	          "metric",
931	          "qwen3_235b",
932	          "llama4_scout",
933	          "agreement"
934	        ],
935	        "rows": [
936	          [
937	            "global_spearman_rho",
938	            -0.38,
939	            -0.18,
940	            "—"
941	          ],
942	          [
943	            "per_lang_rho_median",
944	            -0.25,
945	            -0.12,
946	            "—"
947	          ],
948	          [
949	            "sign_consistency",
950	            0.63,
951	            0.53,
952	            "—"
953	          ],
954	          [
955	            "n_nondominated",
956	            "5/24",
957	            "3/12",
958	            "—"
959	          ],
960	          [
961	            "zs_auroc_mean",
962	            0.618,
963	            0.588,
964	            "—"
965	          ],
966	          [
967	            "optimal_layer_rank_tau",
968	            "—",
969	            "—",
970	            0.33
971	          ],
972	          [
973	            "pass_lang_jaccard",
974	            "—",
975	            "—",
976	            0.47
977	          ]
978	        ]
979	      }
980	    ],
981	    "figures": [],
982	    "analysis": "Llama 4 Scout demolishes the universal Pareto claim. ρ = −0.18 globally, median per-lang ρ = −0.12, sign consistency 0.53. Cross-architecture agreement τ = 0.33. This transforms the paper: the depth-transfer tradeoff is architecture-dependent, not a universal transformer property. Practitioners cannot use layer selection findings from one model on another. For the diagnostic paper, this is reframed as a key finding: \"the field cannot assume probe-based calibration will behave consistently across architectures.\"\n\n\nLlama 4 Scout is the worst-tier's key failure for the Pareto claim. Its 48 layers give only 12 probed points (vs 24 for Qwen3), reducing statistical power for Spearman ρ. More critically, Llama 4 Scout uses a different MoE routing strategy where experts are more language-specialized at intermediate layers (20–28), creating non-monotonic jumps in transfer AUROC that break the depth gradient. Per-language rho median = −0.12 means the depth-transfer tradeoff essentially vanishes on this architecture. Only 5/19 languages pass 0.65 (vs 7 for Qwen3), and the cross-architecture Pareto agreement is τ = 0.33 — optimal layer for a language on Qwen3 does not predict optimal layer on Llama 4. English AUROC peaks lower (0.749 vs 0.776) because the 48-layer structure compresses the representational hierarchy. Transfer is worse overall (0.588 vs 0.618) reflecting more English-centric training data and sparser expert allocation for non-English. The 0.53 sign consistency means the depth-transfer direction is nearly coin-flip across languages — the \"Pareto frontier\" is architecture-specific, not a universal property.\n"
983	  },
984	  {
985	    "name": "CaCLR Implementation and Comparative Evaluation",
986	    "description": "Implement CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency with MMD). Train using English labels + unlabeled parallel activations from GlobalMMLU train split. Compare vs zero-shot, mean-shift, linear projection, few-shot across full Pareto frontier for both models × 19 target languages. α sweep (0.01–10.0), β sweep across 3 OOM (0.001–1.0). Fixed-layer results (50% depth + EN-optimal) alongside per-language oracle.\n",
987	    "results": {
988	      "best_alpha": 0.3,
989	      "best_beta": 0.05,
990	      "beta_sensitivity": "flat — β from 0.001 to 1.0 changes AUROC by <0.4pp; consistency loss is inert",
991	      "alpha_sensitivity": "moderate — α = 0.1–1.0 gives similar results; inverted-U peaking at 0.3",
992	      "caclr_auroc_mean_qwen3": 0.623,
993	      "caclr_auroc_mean_llama4": 0.594,
994	      "caclr_vs_zs_delta_auroc_mean_pp_qwen3": 0.5,
995	      "caclr_vs_zs_delta_auroc_mean_pp_llama4": 0.6,
996	      "caclr_vs_zs_delta_auroc_median_pp": 0.003,
997	      "caclr_vs_linproj_delta_auroc_mean_pp_qwen3": -1.3,
998	      "caclr_vs_linproj_delta_auroc_mean_pp_llama4": -1.4,
999	      "caclr_vs_fewshot100_delta_pp_qwen3": -3.9,
1000	      "caclr_vs_fewshot100_delta_pp_llama4": -4.7,
1001	      "caclr_ece_mean_qwen3": 0.186,
1002	      "caclr_ece_mean_llama4": 0.201,
1003	      "caclr_ece_reduction_vs_tempcal_pp": -0.002,
1004	      "ablation_bce_only_auroc_mean": 0.618,
1005	      "ablation_bce_sbece_auroc_mean": 0.627,
1006	      "ablation_bce_consistency_auroc_mean": 0.611,
1007	      "ablation_full_caclr_auroc_mean": 0.621,
1008	      "beta_delta_over_alpha_only_pp": -0.006,
1009	      "cohens_d_caclr_vs_zs": 0.04,
1010	      "cohens_d_caclr_vs_linproj": -0.18,
1011	      "permutation_test_caclr_vs_zs_p": 0.71,
1012	      "caclr_per_lang_qwen3": {
1013	        "zh": {
1014	          "auroc": 0.671,
1015	          "delta_vs_zs_pp": 0.3
1016	        },
1017	        "fr": {
1018	          "auroc": 0.667,
1019	          "delta_vs_zs_pp": -0.5
1020	        },
1021	        "de": {
1022	          "auroc": 0.664,
1023	          "delta_vs_zs_pp": -0.7
1024	        },
1025	        "es": {
1026	          "auroc": 0.657,
1027	          "delta_vs_zs_pp": -0.4
1028	        },
1029	        "ja": {
1030	          "auroc": 0.653,
1031	          "delta_vs_zs_pp": -0.5
1032	        },
1033	        "ko": {
1034	          "auroc": 0.652,
1035	          "delta_vs_zs_pp": -0.4
1036	        },
1037	        "ru": {
1038	          "auroc": 0.649,
1039	          "delta_vs_zs_pp": -0.3
1040	        },
1041	        "pl": {
1042	          "auroc": 0.631,
1043	          "delta_vs_zs_pp": 0.3
1044	        },
1045	        "ar": {
1046	          "auroc": 0.631,
1047	          "delta_vs_zs_pp": 0.6
1048	        },
1049	        "id": {
1050	          "auroc": 0.627,
1051	          "delta_vs_zs_pp": 0.6
1052	        },
1053	        "hi": {
1054	          "auroc": 0.625,
1055	          "delta_vs_zs_pp": 0.7
1056	        },
1057	        "uk": {
1058	          "auroc": 0.621,
1059	          "delta_vs_zs_pp": 0.7
1060	        },
1061	        "vi": {
1062	          "auroc": 0.615,
1063	          "delta_vs_zs_pp": 0.8
1064	        },
1065	        "th": {
1066	          "auroc": 0.603,
1067	          "delta_vs_zs_pp": 0.9
1068	        },
1069	        "bn": {
1070	          "auroc": 0.564,
1071	          "delta_vs_zs_pp": 1.1
1072	        },
1073	        "te": {
1074	          "auroc": 0.581,
1075	          "delta_vs_zs_pp": 1.0
1076	        },
1077	        "ta": {
1078	          "auroc": 0.578,
1079	          "delta_vs_zs_pp": 1.0
1080	        },
1081	        "sw": {
1082	          "auroc": 0.549,
1083	          "delta_vs_zs_pp": 1.2
1084	        },
1085	        "yo": {
1086	          "auroc": 0.526,
1087	          "delta_vs_zs_pp": 1.4
1088	        }
1089	      }
1090	    },
1091	    "tables": [
1092	      {
1093	        "name": "Table 7: Transfer Method Comparison — Both Models (19-Language Mean)",
1094	        "columns": [
1095	          "method",
1096	          "qwen3_auroc",
1097	          "qwen3_ece",
1098	          "llama4_auroc",
1099	          "llama4_ece",
1100	          "cohens_d_vs_zs",
1101	          "labels_needed"
1102	        ],
1103	        "rows": [
1104	          [
1105	            "zero_shot",
1106	            0.618,
1107	            0.191,
1108	            0.588,
1109	            0.208,
1110	            "—",
1111	            "0 target"
1112	          ],
1113	          [
1114	            "mean_shift",
1115	            0.618,
1116	            0.207,
1117	            0.588,
1118	            0.224,
1119	            0.0,
1120	            "0 target (ΔAUROC≡0)"
1121	          ],
1122	          [
1123	            "CaCLR",
1124	            0.623,
1125	            0.186,
1126	            0.594,
1127	            0.201,
1128	            0.04,
1129	            "0 target + parallel"
1130	          ],
1131	          [
1132	            "linear_projection",
1133	            0.636,
1134	            0.176,
1135	            0.608,
1136	            0.189,
1137	            0.24,
1138	            "~50 parallel"
1139	          ],
1140	          [
1141	            "few_shot_25",
1142	            0.644,
1143	            0.169,
1144	            0.617,
1145	            0.182,
1146	            0.35,
1147	            "25 target"
1148	          ],
1149	          [
1150	            "few_shot_100",
1151	            0.662,
1152	            0.154,
1153	            0.641,
1154	            0.168,
1155	            0.58,
1156	            "100 target"
1157	          ]
1158	        ]
1159	      },
1160	      {
1161	        "name": "Table 8: CaCLR Ablation (Qwen3-235B, 19-Language Mean)",
1162	        "columns": [
1163	          "variant",
1164	          "auroc_mean",
1165	          "ece_mean",
1166	          "delta_vs_full_pp"
1167	        ],
1168	        "rows": [
1169	          [
1170	            "Full CaCLR (BCE+SB-ECE+Consistency)",
1171	            0.621,
1172	            0.186,
1173	            0.0
1174	          ],
1175	          [
1176	            "BCE+SB-ECE (no consistency)",
1177	            0.627,
1178	            0.179,
1179	            0.6
1180	          ],
1181	          [
1182	            "BCE+Consistency (no SB-ECE)",
1183	            0.611,
1184	            0.198,
1185	            -1.0
1186	          ],
1187	          [
1188	            "BCE only (= zero-shot probe)",
1189	            0.618,
1190	            0.191,
1191	            -0.3
1192	          ],
1193	          [
1194	            "Linear Projection (reference)",
1195	            0.636,
1196	            0.176,
1197	            1.5
1198	          ]
1199	        ]
1200	      },
1201	      {
1202	        "name": "Table 9: CaCLR β Sensitivity (Qwen3, α fixed at 0.3, 19-lang mean AUROC)",
1203	        "columns": [
1204	          "beta",
1205	          "auroc_mean",
1206	          "delta_vs_beta0_pp"
1207	        ],
1208	        "rows": [
1209	          [
1210	            0.0,
1211	            0.627,
1212	            0.0
1213	          ],
1214	          [
1215	            0.001,
1216	            0.626,
1217	            -0.1
1218	          ],
1219	          [
1220	            0.005,
1221	            0.625,
1222	            -0.2
1223	          ],
1224	          [
1225	            0.01,
1226	            0.625,
1227	            -0.2
1228	          ],
1229	          [
1230	            0.05,
1231	            0.623,
1232	            -0.4
1233	          ],
1234	          [
1235	            0.1,
1236	            0.621,
1237	            -0.6
1238	          ],
1239	          [
1240	            0.5,
1241	            0.618,
1242	            -0.9
1243	          ],
1244	          [
1245	            1.0,
1246	            0.614,
1247	            -1.3
1248	          ]
1249	        ]
1250	      }
1251	    ],
1252	    "figures": [],
1253	    "analysis": "CaCLR is a rigorous negative result. The ablation cleanly isolates the failure: consistency loss is harmful (adding it to BCE+SB-ECE reduces AUROC by 0.6pp). The β sweep over 3 OOM confirms this is not a tuning failure — the entire β landscape is flat or declining. CKA analysis (plan_011) provides the mechanistic explanation: cross-lingual misalignment at deeper layers is geometric (correctness direction rotates), not distributional (mean/cov shift). MMD-based alignment cannot correct rotation, which is why linear projection (learns rotation) succeeds where CaCLR (matches distributions) fails. For the paper, CaCLR is reported as attempted-and-failed, saving the community from pursuing distributional-matching approaches for this problem class.\n\n\nCaCLR fully fails as a method contribution. The consistency loss (β·L_consistency) is inert: sweeping β over 3 orders of magnitude produces a flat AUROC landscape (<0.4pp variation). Adding consistency to BCE+SB-ECE actually hurts by −0.6pp because MMD-based alignment collapses both signal and noise — the unlabeled parallel activations contain massive language-specific variance (script, morphology, tokenization artifacts) that dominates the correctness signal. Minimizing distributional distance between languages forces the probe to ignore language-specific activation patterns that sometimes carry cross-lingual correctness information. The ablation reveals that the only beneficial component is SB-ECE regularization (+0.9pp), which acts as a calibration regularizer on the English training side but has nothing to do with cross-lingual transfer. Full CaCLR ends up as \"zero-shot + SB-ECE regularization\" — a trivially achievable benefit that does not justify the method's complexity. Linear projection beats CaCLR because it directly estimates the geometric transformation between language subspaces, which is more data-efficient than trying to learn an invariant representation from noisy distributional signals. The paired permutation test CaCLR vs zero-shot gives p = 0.71 — no significant difference. Cohen's d = 0.04 confirms negligible effect size. CaCLR slightly helps low-resource languages (+1pp) and slightly hurts high-resource (−0.5pp), but both effects are within noise. For the paper, CaCLR is relegated to one paragraph: \"the natural distributional- matching approach fails — consistency-based objectives do not help when cross-lingual correctness SNR is low.\"\n"
1254	  },
1255	  {
1256	    "name": "Difficulty-Controlled Ablation (Decomposition)",
1257	    "description": "Train IRT difficulty probes (Ridge regression on human difficulty scores per Civelli et al.), project out difficulty direction from activations, retrain correctness probes on residuals, evaluate transfer. 10 languages × 8 layers per model. Include random-direction control.\n",
1258	    "results": {
1259	      "difficulty_probe_r2_en_qwen3": 0.52,
1260	      "difficulty_probe_r2_en_llama4": 0.47,
1261	      "difficulty_probe_transfer_r2_mean_9lang": 0.38,
1262	      "decomp_difficulty_var_explained_pct_qwen3": 14.3,
1263	      "decomp_difficulty_var_explained_pct_llama4": 11.8,
1264	      "correctness_on_residual_auroc_en_qwen3": 0.741,
1265	      "correctness_on_residual_auroc_en_llama4": 0.714,
1266	      "residual_transfer_auroc_mean_qwen3": 0.613,
1267	      "residual_transfer_auroc_mean_llama4": 0.583,
1268	      "transfer_delta_after_projection_pp_qwen3": -0.5,
1269	      "transfer_delta_after_projection_pp_llama4": -0.5,
1270	      "transfer_delta_range_across_langs_pp": [
1271	        -2.1,
1272	        1.3
1273	      ],
1274	      "random_direction_control_delta_pp": -0.3,
1275	      "difficulty_correctness_cosine_mean": 0.36,
1276	      "difficulty_correctness_cosine_std": 0.11,
1277	      "decomp_prescriptive": false,
1278	      "pct_langs_helped_by_projection": 0.3,
1279	      "pct_langs_hurt_by_projection": 0.5,
1280	      "pct_langs_unchanged": 0.2
1281	    },
1282	    "tables": [
1283	      {
1284	        "name": "Table 10: Difficulty Probe Quality (Ridge, R² on Held-Out)",
1285	        "columns": [
1286	          "language",
1287	          "resource_tier",
1288	          "qwen3_r2",
1289	          "llama4_r2"
1290	        ],
1291	        "rows": [
1292	          [
1293	            "en",
1294	            "—",
1295	            0.52,
1296	            0.47
1297	          ],
1298	          [
1299	            "zh",
1300	            "high",
1301	            0.48,
1302	            0.43
1303	          ],
1304	          [
1305	            "fr",
1306	            "high",
1307	            0.47,
1308	            0.42
1309	          ],
1310	          [
1311	            "de",
1312	            "high",
1313	            0.46,
1314	            0.41
1315	          ],
1316	          [
1317	            "hi",
1318	            "mid",
1319	            0.41,
1320	            0.36
1321	          ],
1322	          [
1323	            "ru",
1324	            "mid",
1325	            0.43,
1326	            0.38
1327	          ],
1328	          [
1329	            "ko",
1330	            "mid",
1331	            0.42,
1332	            0.37
1333	          ],
1334	          [
1335	            "tr",
1336	            "mid",
1337	            0.39,
1338	            0.34
1339	          ],
1340	          [
1341	            "sw",
1342	            "low",
1343	            0.3,
1344	            0.25
1345	          ],
1346	          [
1347	            "bn",
1348	            "low",
1349	            0.28,
1350	            0.23
1351	          ]
1352	        ]
1353	      },
1354	      {
1355	        "name": "Table 11: Decomposition Transfer Ablation (9-Language Mean)",
1356	        "columns": [
1357	          "condition",
1358	          "qwen3_auroc",
1359	          "qwen3_delta_pp",
1360	          "llama4_auroc",
1361	          "llama4_delta_pp"
1362	        ],
1363	        "rows": [
1364	          [
1365	            "Full activations (baseline)",
1366	            0.618,
1367	            0.0,
1368	            0.588,
1369	            0.0
1370	          ],
1371	          [
1372	            "Residual (difficulty out)",
1373	            0.613,
1374	            -0.5,
1375	            0.583,
1376	            -0.5
1377	          ],
1378	          [
1379	            "Difficulty component only",
1380	            0.569,
1381	            -4.9,
1382	            0.548,
1383	            -4.0
1384	          ],
1385	          [
1386	            "Random direction out (ctrl)",
1387	            0.615,
1388	            -0.3,
1389	            0.585,
1390	            -0.3
1391	          ]
1392	        ]
1393	      },
1394	      {
1395	        "name": "Table 12: Per-Language Transfer Delta After Difficulty Projection (Qwen3)",
1396	        "columns": [
1397	          "language",
1398	          "resource_tier",
1399	          "delta_auroc_pp",
1400	          "direction"
1401	        ],
1402	        "rows": [
1403	          [
1404	            "zh",
1405	            "high",
1406	            -0.8,
1407	            "hurt"
1408	          ],
1409	          [
1410	            "fr",
1411	            "high",
1412	            -1.2,
1413	            "hurt"
1414	          ],
1415	          [
1416	            "de",
1417	            "high",
1418	            -0.6,
1419	            "hurt"
1420	          ],
1421	          [
1422	            "hi",
1423	            "mid",
1424	            0.4,
1425	            "helped"
1426	          ],
1427	          [
1428	            "ru",
1429	            "mid",
1430	            -0.3,
1431	            "unchanged"
1432	          ],
1433	          [
1434	            "ko",
1435	            "mid",
1436	            1.0,
1437	            "helped"
1438	          ],
1439	          [
1440	            "tr",
1441	            "mid",
1442	            -2.1,
1443	            "hurt"
1444	          ],
1445	          [
1446	            "sw",
1447	            "low",
1448	            1.3,
1449	            "helped"
1450	          ],
1451	          [
1452	            "bn",
1453	            "low",
1454	            -0.8,
1455	            "hurt"
1456	          ]
1457	        ]
1458	      }
1459	    ],
1460	    "figures": [],
1461	    "analysis": "Decomposition fails as a prescriptive tool. The difficulty-shared component is load-bearing for cross-lingual transfer — removing it hurts more often than it helps (5/10 vs 3/10), and the average delta (−0.5pp) is barely above the random-direction control (−0.3pp). The original Claim 2 hypothesis is abandoned. For the diagnostic paper, this becomes: \"difficulty and capability are entangled in multilingual representations — the clean separation reported in English-only work does not generalize cross-lingually.\"\n\n\nDecomposition is inconclusive. Projecting out difficulty direction changes transfer AUROC by −0.5pp on average — within noise (random-direction control shows −0.3pp from dimensionality reduction alone). The per-language pattern shows no systematic structure: 3/10 languages improve slightly (1–1.3pp), 5/10 worsen (0.5–2.1pp), 2/10 unchanged. The difficulty direction explains only 14% of correctness variance (Qwen3), meaning the decomposition captures a real but minor factor. Critically, the difficulty-shared component turns out to carry useful cross-lingual signal: questions that are hard in English tend to be hard everywhere, and this shared difficulty is one of few reliable cross-lingual bridges. Removing it strips away a genuine invariance. The residual \"capability-specific\" component is more language-dependent, not less — containing idiosyncratic encoding patterns. The cosine between difficulty and correctness directions (0.36 ± 0.11) confirms they are neither orthogonal nor aligned — the moderate overlap prevents clean separation. This contradicts Claim 2's hypothesis that decomposition would be prescriptive. For the paper, decomposition is reported as \"difficulty and capability are entangled in multilingual representations, unlike the clean separation assumed by English-only work.\"\n"
1462	  },
1463	  {
1464	    "name": "Cross-Lingual Orthogonality Analysis",
1465	    "description": "Extract verbalized confidence direction (prompt model for confidence score, fit probe), compute cosine similarity with correctness direction across 20 languages × 2 architectures. Analyze by resource tier and language family.\n",
1466	    "results": {
1467	      "orthogonality_cosine_mean_overall": 0.074,
1468	      "orthogonality_cosine_std_overall": 0.036,
1469	      "orthogonality_cosine_mean_qwen3": 0.069,
1470	      "orthogonality_cosine_mean_llama4": 0.079,
1471	      "orthogonality_cosine_max_across_all": 0.172,
1472	      "orthogonality_cosine_high_resource": 0.052,
1473	      "orthogonality_cosine_mid_resource": 0.073,
1474	      "orthogonality_cosine_low_resource": 0.108,
1475	      "pct_langs_cosine_below_0p10": 0.73,
1476	      "pct_langs_cosine_below_0p05": 0.3,
1477	      "outlier_langs_above_0p15": [
1478	        "yo_llama4"
1479	      ],
1480	      "confidence_probe_r2_en": 0.71,
1481	      "confidence_probe_transfer_r2_mean": 0.58,
1482	      "cosine_resource_tier_spearman": -0.61,
1483	      "per_lang_cosine": {
1484	        "en": {
1485	          "qwen3": 0.036,
1486	          "llama4": 0.041,
1487	          "mean": 0.039
1488	        },
1489	        "zh": {
1490	          "qwen3": 0.041,
1491	          "llama4": 0.048,
1492	          "mean": 0.045
1493	        },
1494	        "fr": {
1495	          "qwen3": 0.044,
1496	          "llama4": 0.052,
1497	          "mean": 0.048
1498	        },
1499	        "de": {
1500	          "qwen3": 0.046,
1501	          "llama4": 0.054,
1502	          "mean": 0.05
1503	        },
1504	        "es": {
1505	          "qwen3": 0.048,
1506	          "llama4": 0.057,
1507	          "mean": 0.053
1508	        },
1509	        "ja": {
1510	          "qwen3": 0.053,
1511	          "llama4": 0.061,
1512	          "mean": 0.057
1513	        },
1514	        "ru": {
1515	          "qwen3": 0.056,
1516	          "llama4": 0.064,
1517	          "mean": 0.06
1518	        },
1519	        "ko": {
1520	          "qwen3": 0.058,
1521	          "llama4": 0.067,
1522	          "mean": 0.063
1523	        },
1524	        "ar": {
1525	          "qwen3": 0.064,
1526	          "llama4": 0.073,
1527	          "mean": 0.069
1528	        },
1529	        "hi": {
1530	          "qwen3": 0.067,
1531	          "llama4": 0.076,
1532	          "mean": 0.072
1533	        },
1534	        "vi": {
1535	          "qwen3": 0.069,
1536	          "llama4": 0.078,
1537	          "mean": 0.074
1538	        },
1539	        "id": {
1540	          "qwen3": 0.065,
1541	          "llama4": 0.074,
1542	          "mean": 0.07
1543	        },
1544	        "th": {
1545	          "qwen3": 0.074,
1546	          "llama4": 0.084,
1547	          "mean": 0.079
1548	        },
1549	        "pl": {
1550	          "qwen3": 0.06,
1551	          "llama4": 0.068,
1552	          "mean": 0.064
1553	        },
1554	        "uk": {
1555	          "qwen3": 0.063,
1556	          "llama4": 0.072,
1557	          "mean": 0.068
1558	        },
1559	        "bn": {
1560	          "qwen3": 0.085,
1561	          "llama4": 0.098,
1562	          "mean": 0.092
1563	        },
1564	        "te": {
1565	          "qwen3": 0.092,
1566	          "llama4": 0.106,
1567	          "mean": 0.099
1568	        },
1569	        "ta": {
1570	          "qwen3": 0.096,
1571	          "llama4": 0.112,
1572	          "mean": 0.104
1573	        },
1574	        "sw": {
1575	          "qwen3": 0.104,
1576	          "llama4": 0.124,
1577	          "mean": 0.114
1578	        },
1579	        "yo": {
1580	          "qwen3": 0.121,
1581	          "llama4": 0.172,
1582	          "mean": 0.147
1583	        }
1584	      }
1585	    },
1586	    "tables": [
1587	      {
1588	        "name": "Table 13: Correctness-Confidence Cosine Similarity by Resource Tier",
1589	        "columns": [
1590	          "resource_tier",
1591	          "n_langs",
1592	          "qwen3_mean",
1593	          "llama4_mean",
1594	          "overall_mean",
1595	          "std"
1596	        ],
1597	        "rows": [
1598	          [
1599	            "high",
1600	            8,
1601	            0.048,
1602	            0.056,
1603	            0.052,
1604	            0.008
1605	          ],
1606	          [
1607	            "mid",
1608	            7,
1609	            0.066,
1610	            0.075,
1611	            0.073,
1612	            0.005
1613	          ],
1614	          [
1615	            "low",
1616	            5,
1617	            0.1,
1618	            0.122,
1619	            0.108,
1620	            0.02
1621	          ],
1622	          [
1623	            "all",
1624	            20,
1625	            0.069,
1626	            0.079,
1627	            0.074,
1628	            0.036
1629	          ]
1630	        ]
1631	      }
1632	    ],
1633	    "figures": [],
1634	    "analysis": "Orthogonality survives as the one mechanistic takeaway: output-based calibration is structurally limited everywhere, not just in English. But the contribution is incremental — same qualitative finding as Miao & Ungar, extended to 20 languages. The resource-tier modulation is novel (effect size 0.052 vs 0.108) but the Yoruba outlier at 0.172 weakens the universality claim. For the paper: \"correctness-confidence dissociation is multilingual, confirming output-based calibration faces a structural ceiling regardless of language, but this ceiling is noisier for low-resource languages.\"\n\n\nOrthogonality persists cross-lingually (mean cosine 0.074) because it reflects a structural property of how LLMs separate verbalized confidence from actual correctness at the representation level. However, the worst-tier variance is higher than Miao & Ungar's English-only finding (std 0.036 vs ~0.01): low-resource languages show weaker orthogonality (cosine ~0.108) because the model has less capacity to maintain the confidence-correctness dissociation for languages with limited training data. Yoruba on Llama4 reaches 0.172 — an outlier above the 0.15 threshold that weakens the universality claim. This happens because Llama4 has minimal Yoruba training data, so both correctness and confidence signals degrade in correlated ways, partially breaking orthogonality. The resource-tier gradient (high: 0.052, mid: 0.073, low: 0.108, Spearman ρ = −0.61 with resource level) is the novel angle, but effect size is modest. Reviewers may see the extension from English-only (Miao & Ungar) to 20 languages as incremental rather than novel, since the qualitative finding is the same.\n"
1635	  },
1636	  {
1637	    "name": "Probe Complexity Comparison",
1638	    "description": "Logistic regression vs 2-layer MLP at each probed layer for both models. Compare English accuracy, cross-lingual transfer, calibration. Test hypothesis: linear probes transfer better.\n",
1639	    "results": {
1640	      "mlp_vs_logreg_en_auroc_delta_mean_pp": 1.0,
1641	      "mlp_vs_logreg_transfer_auroc_delta_mean_pp": -0.3,
1642	      "hypothesis_linear_transfers_better": "weak support",
1643	      "cohens_d_transfer_difference": 0.15,
1644	      "permutation_test_p": 0.34,
1645	      "mlp_en_advantage_deep_layers_pp": 1.4,
1646	      "logreg_transfer_advantage_deep_layers_pp": 0.6,
1647	      "interaction_depth_probe_significant": false
1648	    },
1649	    "tables": [
1650	      {
1651	        "name": "Table 14: Probe Complexity Comparison (Mean Across All Layers)",
1652	        "columns": [
1653	          "model",
1654	          "probe",
1655	          "en_auroc_mean",
1656	          "transfer_auroc_mean",
1657	          "en_ece_mean",
1658	          "transfer_ece_mean"
1659	        ],
1660	        "rows": [
1661	          [
1662	            "qwen3",
1663	            "logreg",
1664	            0.714,
1665	            0.618,
1666	            0.206,
1667	            0.191
1668	          ],
1669	          [
1670	            "qwen3",
1671	            "mlp",
1672	            0.725,
1673	            0.615,
1674	            0.198,
1675	            0.194
1676	          ],
1677	          [
1678	            "llama4",
1679	            "logreg",
1680	            0.697,
1681	            0.588,
1682	            0.219,
1683	            0.208
1684	          ],
1685	          [
1686	            "llama4",
1687	            "mlp",
1688	            0.706,
1689	            0.586,
1690	            0.212,
1691	            0.211
1692	          ]
1693	        ]
1694	      }
1695	    ],
1696	    "figures": [],
1697	    "analysis": "Non-finding. Effect is real but negligible (d = 0.15). Logistic regression confirmed as default choice: simpler, nearly identical performance, better interpretability. Goes in supplementary as methods validation.\n\n\nLinear probes transfer marginally better (−0.3pp MLP penalty in transfer vs +1.0pp MLP advantage in English), but Cohen's d = 0.15 and the permutation test is non-significant (p = 0.34). The effect is too small to be practically meaningful. MLP captures mild nonlinearities in the correctness signal but these are English-specific features that don't generalize. The depth interaction exists weakly (MLP overfits more at deep layers) but isn't statistically significant as an interaction term. This validates logistic regression as the right default but generates no standalone finding.\n"
1698	  },
1699	  {
1700	    "name": "Additional Benchmark Evaluation (Belebele + MMLU-ProX)",
1701	    "description": "Evaluate best probes + CaCLR on Belebele (reading comprehension, 20 languages) and MMLU-ProX (translated MMLU, 20 languages). Tests cross-benchmark generalization.\n",
1702	    "results": {
1703	      "belebele_en_auroc_qwen3": 0.741,
1704	      "belebele_en_auroc_llama4": 0.718,
1705	      "belebele_zs_transfer_mean_qwen3": 0.594,
1706	      "belebele_zs_transfer_mean_llama4": 0.567,
1707	      "belebele_drop_vs_globalmmlu_pp": 2.4,
1708	      "belebele_caclr_delta_vs_linproj_pp": -0.8,
1709	      "mmlupx_en_auroc_qwen3": 0.762,
1710	      "mmlupx_en_auroc_llama4": 0.738,
1711	      "mmlupx_zs_transfer_mean_qwen3": 0.579,
1712	      "mmlupx_zs_transfer_mean_llama4": 0.551,
1713	      "mmlupx_drop_vs_globalmmlu_pp": 3.9,
1714	      "mmlupx_caclr_delta_vs_linproj_pp": -1.1,
1715	      "lang_rank_corr_globalmmlu_belebele": 0.83,
1716	      "lang_rank_corr_globalmmlu_mmlupx": 0.69
1717	    },
1718	    "tables": [
1719	      {
1720	        "name": "Table 15: Cross-Benchmark Generalization (19-Language Mean)",
1721	        "columns": [
1722	          "benchmark",
1723	          "zs_auroc_qwen3",
1724	          "zs_auroc_llama4",
1725	          "caclr_vs_linproj_pp",
1726	          "lang_rank_corr"
1727	        ],
1728	        "rows": [
1729	          [
1730	            "GlobalMMLU",
1731	            0.618,
1732	            0.588,
1733	            -1.3,
1734	            "—"
1735	          ],
1736	          [
1737	            "Belebele",
1738	            0.594,
1739	            0.567,
1740	            -0.8,
1741	            0.83
1742	          ],
1743	          [
1744	            "MMLU-ProX",
1745	            0.579,
1746	            0.551,
1747	            -1.1,
1748	            0.69
1749	          ]
1750	        ]
1751	      }
1752	    ],
1753	    "figures": [],
1754	    "analysis": "Findings partially generalize: Belebele confirms, MMLU-ProX is noisier. Language ranking stable but absolute performance degrades with domain shift. CaCLR's negative result is robust across all three benchmarks. Include Belebele in main results, MMLU-ProX in supplementary with translation-artifact caveat.\n\n\nBelebele partially replicates because it is high-quality and natively multilingual. The 2.4pp transfer drop reflects domain shift (reading comprehension vs knowledge). MMLU-ProX shows worse transfer (3.9pp drop) because machine-translated MMLU introduces systematic distributional shifts (ambiguous domain terms, cultural references, low-resource translation errors). CaCLR remains worse than linear projection on both benchmarks, confirming the negative result generalizes. Language ranking is stable for Belebele (ρ = 0.83) but degrades for MMLU-ProX (ρ = 0.69) due to translation quality variation.\n"
1755	  },
1756	  {
1757	    "name": "INT8 Validation Ablation",
1758	    "description": "Compare INT8 vs FP16 probing results at 5 representative layers for Llama 4 Scout on 5% random subset. Validates quantization doesn't distort correctness signals.\n",
1759	    "results": {
1760	      "int8_vs_fp16_auroc_delta_mean_pp": -0.3,
1761	      "int8_vs_fp16_auroc_delta_max_pp": -0.7,
1762	      "int8_vs_fp16_ece_delta_mean_pp": 0.2,
1763	      "int8_vs_fp16_activation_cosine_sim_mean": 0.994,
1764	      "int8_vs_fp16_rank_correlation_layers": 0.98,
1765	      "validation_passes": true
1766	    },
1767	    "tables": [
1768	      {
1769	        "name": "Table S1: INT8 vs FP16 Comparison (Llama 4 Scout, 5% subset)",
1770	        "columns": [
1771	          "layer",
1772	          "fp16_auroc",
1773	          "int8_auroc",
1774	          "delta_pp",
1775	          "activation_cosine"
1776	        ],
1777	        "rows": [
1778	          [
1779	            8,
1780	            0.637,
1781	            0.633,
1782	            -0.4,
1783	            0.993
1784	          ],
1785	          [
1786	            16,
1787	            0.7,
1788	            0.697,
1789	            -0.3,
1790	            0.994
1791	          ],
1792	          [
1793	            24,
1794	            0.731,
1795	            0.729,
1796	            -0.2,
1797	            0.995
1798	          ],
1799	          [
1800	            32,
1801	            0.746,
1802	            0.743,
1803	            -0.3,
1804	            0.994
1805	          ],
1806	          [
1807	            40,
1808	            0.748,
1809	            0.741,
1810	            -0.7,
1811	            0.992
1812	          ]
1813	        ]
1814	      }
1815	    ],
1816	    "figures": [],
1817	    "analysis": "INT8 validation passes. Quantization is not a confound. One paragraph + Table S1 in supplementary.\n\n\nINT8 quantization introduces minimal distortion. The 0.3pp mean AUROC difference is within noise — INT8 preserves directional structure of activations that linear probes rely on. Cosine similarity 0.994 between INT8 and FP16 activations confirms near-perfect directional alignment. Layer ranking is preserved (rank corr 0.98). This passes cleanly even in the worst tier — quantization is not a source of failure.\n"
1818	  },
1819	  {
1820	    "name": "CKA Cross-Lingual Representation Similarity Analysis",
1821	    "description": "Compute CKA (linear kernel) between English and each target language at every probed layer for both models. Correlate CKA with transfer AUROC to provide mechanistic explanation for the Pareto frontier. Full-scale validation of pilot finding (revised hypothesis: threshold model — transfer collapses only below critical CKA threshold ~0.35). Report CKA × layer × language heatmaps, CKA vs transfer degradation correlation per language, and threshold analysis.\n",
1822	    "results": {
1823	      "cka_en_vs_target_mean_all": 0.72,
1824	      "cka_decline_with_depth": true,
1825	      "cka_shallow_mean": 0.89,
1826	      "cka_deep_mean": 0.54,
1827	      "cka_vs_transfer_auroc_pearson_r_overall": 0.32,
1828	      "cka_vs_transfer_auroc_pearson_r_range_per_lang": [
1829	        -0.08,
1830	        0.71
1831	      ],
1832	      "cka_vs_transfer_pearson_significant_langs": 7,
1833	      "cka_vs_transfer_pearson_nonsig_langs": 12,
1834	      "cka_threshold_0p35_replicates": "partial",
1835	      "n_lang_layer_pairs_below_threshold": 18,
1836	      "transfer_collapse_below_threshold_pct": 0.61,
1837	      "transfer_collapse_above_threshold_pct": 0.22,
1838	      "cka_architecture_consistency": "weak",
1839	      "cka_pearson_qwen3": 0.38,
1840	      "cka_pearson_llama4": 0.24,
1841	      "cka_by_tier": {
1842	        "high_resource_mean": 0.76,
1843	        "mid_resource_mean": 0.71,
1844	        "low_resource_mean": 0.64
1845	      },
1846	      "cka_per_lang_deep_layer": {
1847	        "zh": 0.68,
1848	        "fr": 0.71,
1849	        "de": 0.69,
1850	        "es": 0.67,
1851	        "ja": 0.62,
1852	        "ko": 0.6,
1853	        "ru": 0.58,
1854	        "ar": 0.53,
1855	        "hi": 0.51,
1856	        "vi": 0.48,
1857	        "id": 0.52,
1858	        "th": 0.45,
1859	        "pl": 0.55,
1860	        "uk": 0.54,
1861	        "bn": 0.41,
1862	        "te": 0.39,
1863	        "ta": 0.37,
1864	        "sw": 0.33,
1865	        "yo": 0.28
1866	      },
1867	      "pilot_revision_validated": "partially — threshold exists but is noisy"
1868	    },
1869	    "tables": [
1870	      {
1871	        "name": "Table 16: CKA vs Transfer AUROC Correlation by Architecture",
1872	        "columns": [
1873	          "model",
1874	          "pearson_r",
1875	          "p_value",
1876	          "n_sig_langs",
1877	          "n_total_langs",
1878	          "spearman_rho"
1879	        ],
1880	        "rows": [
1881	          [
1882	            "Qwen3-235B",
1883	            0.38,
1884	            0.002,
1885	            5,
1886	            19,
1887	            0.35
1888	          ],
1889	          [
1890	            "Llama4-Scout",
1891	            0.24,
1892	            0.041,
1893	            2,
1894	            19,
1895	            0.21
1896	          ],
1897	          [
1898	            "Combined",
1899	            0.32,
1900	            0.001,
1901	            7,
1902	            38,
1903	            0.29
1904	          ]
1905	        ]
1906	      },
1907	      {
1908	        "name": "Table 17: CKA Threshold Analysis (threshold = 0.35)",
1909	        "columns": [
1910	          "condition",
1911	          "n_pairs",
1912	          "mean_transfer_auroc",
1913	          "pct_below_0p55",
1914	          "pct_above_0p65"
1915	        ],
1916	        "rows": [
1917	          [
1918	            "CKA < 0.35",
1919	            18,
1920	            0.538,
1921	            0.61,
1922	            0.11
1923	          ],
1924	          [
1925	            "CKA ≥ 0.35",
1926	            438,
1927	            0.612,
1928	            0.22,
1929	            0.39
1930	          ]
1931	        ]
1932	      },
1933	      {
1934	        "name": "Table 18: CKA at Deep Layers (75% depth) by Language",
1935	        "columns": [
1936	          "language",
1937	          "resource_tier",
1938	          "cka_qwen3",
1939	          "cka_llama4",
1940	          "transfer_auroc_qwen3",
1941	          "transfer_auroc_llama4"
1942	        ],
1943	        "rows": [
1944	          [
1945	            "zh",
1946	            "high",
1947	            0.71,
1948	            0.65,
1949	            0.668,
1950	            0.658
1951	          ],
1952	          [
1953	            "fr",
1954	            "high",
1955	            0.74,
1956	            0.68,
1957	            0.672,
1958	            0.662
1959	          ],
1960	          [
1961	            "de",
1962	            "high",
1963	            0.72,
1964	            0.66,
1965	            0.671,
1966	            0.655
1967	          ],
1968	          [
1969	            "ja",
1970	            "high",
1971	            0.65,
1972	            0.59,
1973	            0.658,
1974	            0.634
1975	          ],
1976	          [
1977	            "ru",
1978	            "high",
1979	            0.61,
1980	            0.55,
1981	            0.652,
1982	            0.622
1983	          ],
1984	          [
1985	            "ar",
1986	            "mid",
1987	            0.56,
1988	            0.5,
1989	            0.625,
1990	            0.589
1991	          ],
1992	          [
1993	            "hi",
1994	            "mid",
1995	            0.54,
1996	            0.48,
1997	            0.618,
1998	            0.586
1999	          ],
2000	          [
2001	            "th",
2002	            "mid",
2003	            0.48,
2004	            0.42,
2005	            0.594,
2006	            0.558
2007	          ],
2008	          [
2009	            "sw",
2010	            "low",
2011	            0.36,
2012	            0.3,
2013	            0.537,
2014	            0.518
2015	          ],
2016	          [
2017	            "yo",
2018	            "low",
2019	            0.31,
2020	            0.25,
2021	            0.512,
2022	            0.492
2023	          ]
2024	        ]
2025	      }
2026	    ],
2027	    "figures": [],
2028	    "analysis": "CKA provides suggestive but not convincing mechanistic explanation. The decline with depth is clear, and the threshold model partially replicates (61% transfer collapse below CKA 0.35). But the correlation is too weak (r = 0.32) and architecture-dependent (0.38 vs 0.24) to serve as a reliable predictor. The key insight survives at a qualitative level: cross-lingual misalignment is geometric, which explains why MMD-based CaCLR fails (it matches distributions but can't correct rotation) while linear projection succeeds (it learns the rotation). But the quantitative story is messy. For the paper: report CKA as supporting evidence for the geometric-misalignment interpretation, not as a standalone finding. Two paragraphs in the analysis section.\n\n\nCKA declines with depth on both models (shallow 0.89 → deep 0.54), confirming that deeper layers are less cross-lingually aligned. However, the correlation between CKA and transfer AUROC is weak overall (Pearson r = 0.32, explaining ~10% of variance). This happens because the pilot's revised hypothesis — that transfer collapses only below a critical CKA threshold (~0.35) rather than declining linearly — partially replicates but with too much noise at full scale. Below the 0.35 threshold, 61% of language-layer pairs show transfer collapse (AUROC < 0.55), but 39% do not — meaning the threshold is suggestive, not deterministic. Above the threshold, 22% of pairs still show poor transfer, indicating CKA captures necessary but not sufficient conditions for transfer. Per-language correlations vary wildly: hi (r = 0.71, sig) and sw (r = 0.67, sig) show strong CKA-transfer coupling, but zh (r = 0.12, ns) and fr (r = 0.08, ns) show near-zero correlation because these high-resource languages transfer well regardless of CKA level. Architecture inconsistency is notable: Qwen3 r = 0.38, Llama4 r = 0.24 — the mechanistic explanation is model-dependent. For the paper, CKA provides a \"suggestive but not convincing\" mechanistic account: geometric misalignment (lower CKA) correlates with transfer failure, but the relationship is too noisy and architecture-dependent to serve as a reliable predictor or principled layer selection criterion.\n"
2029	  },
2030	  {
2031	    "name": "Linear Projection Sensitivity Analysis",
2032	    "description": "Vary number of parallel pairs (10, 20, 50, 100, 200) for linear projection transfer. Determines minimum data requirement for this baseline. Both models × 5 representative layers × 19 target languages.\n",
2033	    "results": {
2034	      "linproj_by_n_pairs": {
2035	        "10": {
2036	          "auroc_mean": 0.608,
2037	          "delta_vs_zs_pp": -1.0,
2038	          "pct_langs_improved": 0.26
2039	        },
2040	        "20": {
2041	          "auroc_mean": 0.621,
2042	          "delta_vs_zs_pp": 0.3,
2043	          "pct_langs_improved": 0.42
2044	        },
2045	        "50": {
2046	          "auroc_mean": 0.636,
2047	          "delta_vs_zs_pp": 1.8,
2048	          "pct_langs_improved": 0.55
2049	        },
2050	        "100": {
2051	          "auroc_mean": 0.643,
2052	          "delta_vs_zs_pp": 2.5,
2053	          "pct_langs_improved": 0.63
2054	        },
2055	        "200": {
2056	          "auroc_mean": 0.647,
2057	          "delta_vs_zs_pp": 2.9,
2058	          "pct_langs_improved": 0.68
2059	        }
2060	      },
2061	      "minimum_viable_pairs_high_resource": 20,
2062	      "minimum_viable_pairs_mid_resource": 50,
2063	      "minimum_viable_pairs_low_resource": ">200 (insufficient quality)",
2064	      "saturation_point": "~100 pairs — diminishing returns beyond",
2065	      "linproj_fails_low_resource": true,
2066	      "low_resource_at_200_pairs": {
2067	        "bn": {
2068	          "auroc": 0.561,
2069	          "delta_vs_zs_pp": 0.8
2070	        },
2071	        "te": {
2072	          "auroc": 0.576,
2073	          "delta_vs_zs_pp": 0.5
2074	        },
2075	        "ta": {
2076	          "auroc": 0.571,
2077	          "delta_vs_zs_pp": 0.3
2078	        },
2079	        "sw": {
2080	          "auroc": 0.543,
2081	          "delta_vs_zs_pp": 0.6
2082	        },
2083	        "yo": {
2084	          "auroc": 0.518,
2085	          "delta_vs_zs_pp": 0.6
2086	        }
2087	      },
2088	      "high_resource_at_50_pairs": {
2089	        "zh": {
2090	          "auroc": 0.681,
2091	          "delta_vs_zs_pp": 1.3
2092	        },
2093	        "fr": {
2094	          "auroc": 0.686,
2095	          "delta_vs_zs_pp": 1.4
2096	        },
2097	        "de": {
2098	          "auroc": 0.684,
2099	          "delta_vs_zs_pp": 1.3
2100	        }
2101	      },
2102	      "variance_across_random_subsets_std_pp": 1.8
2103	    },
2104	    "tables": [
2105	      {
2106	        "name": "Table 19: Linear Projection AUROC by Number of Parallel Pairs (19-Lang Mean)",
2107	        "columns": [
2108	          "n_pairs",
2109	          "auroc_mean",
2110	          "auroc_std",
2111	          "delta_vs_zs_pp",
2112	          "pct_langs_improved",
2113	          "pct_langs_hurt"
2114	        ],
2115	        "rows": [
2116	          [
2117	            10,
2118	            0.608,
2119	            0.052,
2120	            -1.0,
2121	            0.26,
2122	            0.53
2123	          ],
2124	          [
2125	            20,
2126	            0.621,
2127	            0.047,
2128	            0.3,
2129	            0.42,
2130	            0.32
2131	          ],
2132	          [
2133	            50,
2134	            0.636,
2135	            0.042,
2136	            1.8,
2137	            0.55,
2138	            0.21
2139	          ],
2140	          [
2141	            100,
2142	            0.643,
2143	            0.04,
2144	            2.5,
2145	            0.63,
2146	            0.16
2147	          ],
2148	          [
2149	            200,
2150	            0.647,
2151	            0.039,
2152	            2.9,
2153	            0.68,
2154	            0.11
2155	          ]
2156	        ]
2157	      },
2158	      {
2159	        "name": "Table 20: Linear Projection at 50 Pairs by Resource Tier",
2160	        "columns": [
2161	          "resource_tier",
2162	          "n_langs",
2163	          "auroc_mean",
2164	          "delta_vs_zs_pp",
2165	          "pct_improved"
2166	        ],
2167	        "rows": [
2168	          [
2169	            "high",
2170	            7,
2171	            0.677,
2172	            3.1,
2173	            0.86
2174	          ],
2175	          [
2176	            "mid",
2177	            7,
2178	            0.631,
2179	            1.6,
2180	            0.57
2181	          ],
2182	          [
2183	            "low",
2184	            5,
2185	            0.553,
2186	            0.1,
2187	            0.2
2188	          ]
2189	        ]
2190	      }
2191	    ],
2192	    "figures": [],
2193	    "analysis": "Linear projection is the strongest zero-label method but has a clear resource-tier limitation. High-resource languages benefit reliably from ~20 pairs; mid-resource need ~50; low-resource fail even at 200 because parallel quality and activation structure are insufficient. For the paper, this strengthens the practical recommendation: \"few-shot (25–100 labels) is the viable path for mid/low-resource; linear projection works only for high-resource languages with quality parallel data.\" The minimum-pairs analysis is a practical contribution that helps practitioners decide between linproj and few-shot.\n\n\nLinear projection's effectiveness depends heavily on the number and quality of parallel pairs. At 10 pairs, the affine transformation is underestimated (high-dimensional activation space needs more samples to estimate rotation matrix reliably), actually hurting transfer (−1.0pp) by introducing noise. At 20 pairs, high-resource languages start benefiting because their parallel pairs have high translation quality and the activation subspaces are already partially aligned. At 50 pairs, the projection stabilizes for high and mid-resource languages (the \"default\" setting in the main experiments). But low-resource languages fail even at 200 pairs for two reasons: (1) GlobalMMLU parallel translations for sw/yo/bn are lower quality (more literal, less natural), so the parallel activations don't capture the true language-specific encoding; (2) the activation subspace for these languages is itself noisier (less structured due to limited pretraining), making the rotation hard to estimate even with many pairs. The variance across random subsets (std 1.8pp) is high, indicating the projection is sensitive to which specific pairs are used — this is a practical reliability concern. Saturation at ~100 pairs means the projection captures most learnable alignment, and remaining transfer gap is due to fundamental representational differences, not data limitation.\n"
2194	  },
2195	  {
2196	    "name": "Probing Control Tasks (Hewitt & Liang 2019)",
2197	    "description": "Train probes on randomly permuted labels at each layer. Compare selectivity (probe AUROC − control AUROC) across layers and languages. Validates that high AUROC reflects genuine correctness direction, not memorized dataset artifacts or probe capacity.\n",
2198	    "results": {
2199	      "control_auroc_mean_en_qwen3": 0.548,
2200	      "control_auroc_mean_en_llama4": 0.544,
2201	      "control_auroc_range_en": [
2202	        0.512,
2203	        0.571
2204	      ],
2205	      "selectivity_en_best_layer_qwen3": 0.228,
2206	      "selectivity_en_best_layer_llama4": 0.205,
2207	      "selectivity_en_mean_all_layers": 0.168,
2208	      "selectivity_min_across_all": 0.048,
2209	      "selectivity_min_language": "yo",
2210	      "selectivity_min_layer": "shallow (L4/L8)",
2211	      "selectivity_by_resource_tier": {
2212	        "high_resource_mean": 0.172,
2213	        "mid_resource_mean": 0.138,
2214	        "low_resource_mean": 0.084
2215	      },
2216	      "low_resource_selectivity_below_8pp": {
2217	        "sw_L4": 0.052,
2218	        "yo_L4": 0.048,
2219	        "yo_L8": 0.056,
2220	        "bn_L4": 0.061,
2221	        "ta_L4": 0.058,
2222	        "sw_L8": 0.063
2223	      },
2224	      "pct_lang_layer_pairs_selectivity_below_8pp": 0.08,
2225	      "pct_low_resource_pairs_selectivity_below_8pp": 0.28,
2226	      "selectivity_depth_gradient": "positive — deeper layers have higher selectivity",
2227	      "selectivity_vs_auroc_correlation": 0.74
2228	    },
2229	    "tables": [
2230	      {
2231	        "name": "Table 21: Control Task Selectivity by Resource Tier",
2232	        "columns": [
2233	          "resource_tier",
2234	          "n_langs",
2235	          "probe_auroc_mean",
2236	          "control_auroc_mean",
2237	          "selectivity_mean_pp",
2238	          "selectivity_min_pp"
2239	        ],
2240	        "rows": [
2241	          [
2242	            "high",
2243	            7,
2244	            0.66,
2245	            0.548,
2246	            17.2,
2247	            10.4
2248	          ],
2249	          [
2250	            "mid",
2251	            7,
2252	            0.614,
2253	            0.546,
2254	            13.8,
2255	            8.2
2256	          ],
2257	          [
2258	            "low",
2259	            5,
2260	            0.548,
2261	            0.544,
2262	            8.4,
2263	            4.8
2264	          ],
2265	          [
2266	            "all",
2267	            19,
2268	            0.618,
2269	            0.546,
2270	            13.8,
2271	            4.8
2272	          ]
2273	        ]
2274	      },
2275	      {
2276	        "name": "Table 22: Selectivity at Best English Layer (L72 Qwen3 / L36 Llama4)",
2277	        "columns": [
2278	          "language",
2279	          "probe_auroc",
2280	          "control_auroc",
2281	          "selectivity_pp",
2282	          "flag"
2283	        ],
2284	        "rows": [
2285	          [
2286	            "en",
2287	            0.776,
2288	            0.548,
2289	            22.8,
2290	            ""
2291	          ],
2292	          [
2293	            "zh",
2294	            0.641,
2295	            0.549,
2296	            9.2,
2297	            ""
2298	          ],
2299	          [
2300	            "fr",
2301	            0.645,
2302	            0.548,
2303	            9.7,
2304	            ""
2305	          ],
2306	          [
2307	            "de",
2308	            0.644,
2309	            0.549,
2310	            9.5,
2311	            ""
2312	          ],
2313	          [
2314	            "ar",
2315	            0.598,
2316	            0.547,
2317	            5.1,
2318	            "⚠ low"
2319	          ],
2320	          [
2321	            "hi",
2322	            0.591,
2323	            0.546,
2324	            4.5,
2325	            "⚠ low"
2326	          ],
2327	          [
2328	            "sw",
2329	            0.508,
2330	            0.552,
2331	            -4.4,
2332	            "✗ below control"
2333	          ],
2334	          [
2335	            "yo",
2336	            0.487,
2337	            0.551,
2338	            -6.4,
2339	            "✗ below control"
2340	          ]
2341	        ]
2342	      },
2343	      {
2344	        "name": "Table 23: Selectivity by Depth Band (19-Language Mean)",
2345	        "columns": [
2346	          "depth_band",
2347	          "probe_auroc_mean",
2348	          "control_auroc_mean",
2349	          "selectivity_pp"
2350	        ],
2351	        "rows": [
2352	          [
2353	            "0–25%",
2354	            0.582,
2355	            0.549,
2356	            3.3
2357	          ],
2358	          [
2359	            "25–50%",
2360	            0.618,
2361	            0.547,
2362	            7.1
2363	          ],
2364	          [
2365	            "50–75%",
2366	            0.641,
2367	            0.546,
2368	            9.5
2369	          ],
2370	          [
2371	            "75–100%",
2372	            0.634,
2373	            0.548,
2374	            8.6
2375	          ]
2376	        ]
2377	      }
2378	    ],
2379	    "figures": [],
2380	    "analysis": "Control tasks are the most damaging experiment for the worst tier. They reveal that 28% of low-resource language-layer pairs have selectivity < 8pp — some \"transfer success\" in these settings is probe capacity artifact. At the English-optimal layer, Swahili and Yoruba actually score BELOW the control, meaning the probe is memorizing random structure rather than detecting correctness. This doesn't invalidate the main results (high-resource selectivity is robust at 17pp+), but it qualifies them: the resource-tier taxonomy should be presented with selectivity as a reliability measure. For the paper: \"Control tasks confirm that probe AUROC for high/mid-resource languages reflects genuine correctness signals (selectivity > 10pp), but low-resource results at shallow/moderate layers should be interpreted cautiously (selectivity 3–8pp). The practical implication reinforces the few-shot recommendation: for low-resource languages, even the probe AUROC metric itself is unreliable without labeled data to establish a non-trivial baseline.\"\n\n\nControl tasks reveal that probe capacity explains a non-trivial portion of AUROC, especially for low-resource languages at shallow layers. The control AUROC (probes on random labels) averages 0.548 for English — above the theoretical 0.50 baseline because logistic regression on high-dimensional activation spaces (d > 4096) can memorize patterns in random labels when sample sizes are small (GlobalMMLU has ~300–600 items per language). This means an AUROC of 0.60 at a shallow layer for a low-resource language has selectivity of only ~5pp — dangerously close to the control. Specifically, 28% of low-resource language-layer pairs have selectivity below 8pp, meaning a non-negligible fraction of \"successful\" transfer AUROC in low-resource settings is probe capacity artifact rather than genuine correctness signal. The selectivity minimum of 4.8pp (Yoruba at L4) means some reported AUROCs are nearly indistinguishable from memorization. Deeper layers show higher selectivity because the correctness signal strengthens with depth while control AUROC stays constant (~0.55). The resource-tier gradient in selectivity (high: 17.2pp, mid: 13.8pp, low: 8.4pp) mirrors the transfer gradient — low-resource languages have both lower AUROC and lower selectivity, compounding the interpretive challenge. For the paper, this means low-resource AUROC numbers should be presented with selectivity-adjusted confidence intervals. Any language-layer pair with selectivity < 8pp should be flagged as unreliable.\n"
2381	  },
2382	  {
2383	    "name": "Gemma 4 31B Dense — Third Architecture (Camera-Ready)",
2384	    "description": "Full Pareto frontier on Gemma 4 31B Dense (60 layers, dense, FP16). 20+ languages. Dense vs MoE architectural contrast.\n",
2385	    "results": {
2386	      "en_auroc_best_layer": 0.761,
2387	      "en_best_layer_idx": 45,
2388	      "en_auroc_range": [
2389	        0.601,
2390	        0.761
2391	      ],
2392	      "zs_transfer_auroc_mean_19lang": 0.605,
2393	      "zs_transfer_drop_mean_pp": 17.1,
2394	      "zs_langs_above_0p65": 6,
2395	      "pareto_global_spearman_rho": -0.44,
2396	      "pareto_per_lang_rho_median": -0.31,
2397	      "pareto_rho_sign_consistency": 0.68,
2398	      "pareto_frontier_n_nondominated": 6,
2399	      "pareto_frontier_agreement_with_qwen3_tau": 0.42,
2400	      "pareto_frontier_agreement_with_llama4_tau": 0.29,
2401	      "caclr_auroc_mean": 0.609,
2402	      "caclr_vs_linproj_pp": -0.9,
2403	      "dense_vs_moe_finding": "Dense architecture shows cleaner Pareto frontier (ρ = −0.44 vs −0.38/−0.18 for MoE) with higher sign consistency (0.68 vs 0.63/0.53). MoE routing is a source of non-monotonic noise, but the frontier is still moderate even for dense models.\n"
2404	    },
2405	    "tables": [
2406	      {
2407	        "name": "Table 24: Three-Architecture Comparison Summary",
2408	        "columns": [
2409	          "model",
2410	          "type",
2411	          "layers",
2412	          "en_auroc",
2413	          "zs_auroc_mean",
2414	          "pareto_rho",
2415	          "sign_consistency",
2416	          "pareto_agreement_mean_tau"
2417	        ],
2418	        "rows": [
2419	          [
2420	            "Qwen3-235B",
2421	            "MoE",
2422	            94,
2423	            0.776,
2424	            0.618,
2425	            -0.38,
2426	            0.63,
2427	            0.38
2428	          ],
2429	          [
2430	            "Llama4-Scout",
2431	            "MoE",
2432	            48,
2433	            0.749,
2434	            0.588,
2435	            -0.18,
2436	            0.53,
2437	            0.31
2438	          ],
2439	          [
2440	            "Gemma4-31B",
2441	            "Dense",
2442	            60,
2443	            0.761,
2444	            0.605,
2445	            -0.44,
2446	            0.68,
2447	            0.36
2448	          ]
2449	        ]
2450	      }
2451	    ],
2452	    "figures": [],
2453	    "analysis": "Gemma4 confirms the diagnostic paper's thesis from a new angle: MoE routing adds non-monotonic noise to the Pareto frontier, but even the dense architecture's frontier is moderate (ρ = −0.44). The depth-transfer tradeoff is real but explains limited variance regardless of architecture. Cross-architecture agreement remains low, confirming architecture-dependence.\n\n\nGemma 4 31B Dense shows a cleaner but still moderate Pareto frontier because dense architectures have more homogeneous layer transitions (no expert routing to create non-monotonic jumps). The Spearman ρ of −0.44 is the highest among three architectures but still means depth explains only ~19% of transfer variance. English AUROC 0.761 is between Qwen3 (0.776) and Llama4 (0.749), consistent with 31B active parameters being intermediate. Transfer is intermediate too (0.605). Cross-architecture agreement remains low (τ = 0.42 with Qwen3, 0.29 with Llama4), confirming architecture-dependence even between dense and MoE models. CaCLR still fails on this architecture, ruling out the hypothesis that MoE routing specifically caused CaCLR's failure.\n"
2454	  },
2455	  {
2456	    "name": "Extended Language Coverage (50+ Languages, Camera-Ready)",
2457	    "description": "Expand from 20 to 50+ languages using full GlobalMMLU/Belebele language sets.\n",
2458	    "results": {
2459	      "total_languages": 52,
2460	      "zs_transfer_auroc_mean_51lang": 0.581,
2461	      "zs_transfer_auroc_median_51lang": 0.574,
2462	      "zs_pass_rate_51lang": 0.24,
2463	      "low_resource_auroc_mean_new_langs": 0.541,
2464	      "worst_language_auroc": 0.488,
2465	      "worst_language": "Amharic (am)",
2466	      "resource_tier_gradient_steeper": true,
2467	      "new_language_families_added": 5,
2468	      "transfer_by_tier_expanded": {
2469	        "high": {
2470	          "n": 10,
2471	          "auroc_mean": 0.651,
2472	          "pass_rate": 0.7
2473	        },
2474	        "mid": {
2475	          "n": 18,
2476	          "auroc_mean": 0.598,
2477	          "pass_rate": 0.28
2478	        },
2479	        "low": {
2480	          "n": 14,
2481	          "auroc_mean": 0.553,
2482	          "pass_rate": 0.07
2483	        },
2484	        "very_low": {
2485	          "n": 10,
2486	          "auroc_mean": 0.518,
2487	          "pass_rate": 0.0
2488	        }
2489	      }
2490	    },
2491	    "tables": [
2492	      {
2493	        "name": "Table 25: Transfer Success by Resource Tier (52-Language Set, Qwen3)",
2494	        "columns": [
2495	          "resource_tier",
2496	          "n_langs",
2497	          "zs_auroc_mean",
2498	          "zs_auroc_std",
2499	          "pass_rate"
2500	        ],
2501	        "rows": [
2502	          [
2503	            "high",
2504	            10,
2505	            0.651,
2506	            0.017,
2507	            0.7
2508	          ],
2509	          [
2510	            "mid",
2511	            18,
2512	            0.598,
2513	            0.023,
2514	            0.28
2515	          ],
2516	          [
2517	            "low",
2518	            14,
2519	            0.553,
2520	            0.028,
2521	            0.07
2522	          ],
2523	          [
2524	            "very_low",
2525	            10,
2526	            0.518,
2527	            0.021,
2528	            0.0
2529	          ]
2530	        ]
2531	      }
2532	    ],
2533	    "figures": [],
2534	    "analysis": "Extended coverage is the strongest evidence for the diagnostic conclusion. With 52 languages, the majority fail to transfer. Very-low-resource languages (10 langs, AUROC 0.518) are indistinguishable from chance when accounting for control task selectivity. The paper's conclusion: \"probe-based calibration does not generalize beyond a small set of high-resource languages without fundamental methodological advances.\"\n\nExpanding to 52 languages worsens the aggregate picture because additional languages are predominantly low and very-low-resource. Many (Amharic, Lao, Mongolian, Georgian) have minimal representation in pretraining data, so their activations share even less structure with English. Pass rate drops from ~37% (7/19) to ~24% (12/51). Some languages approach chance (AUROC ~0.49). The resource-tier gradient steepens: very-low-resource languages (n=10) average 0.518 with 0% pass rate. This strengthens the diagnostic message: probe-based calibration has a severe language barrier.\n"
2535	  }
2536	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aac4c323-aec4-4c4a-ba9e-5b14a96da12e",
  "isSidechain": false,
  "promptId": "ce9c66bf-f5bc-46b5-95a4-aabc6b39fe73",
  "type": "user",
  "uuid": "ab3728bf-a1ca-46b4-80e6-41f2c1c980e6",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Full Pareto Frontier — Qwen3-235B-A22B (94 layers, MoE, INT8)\",\n    \"description\": \"Extract activations at 24 probed layers (every 4th of 94), 20 languages on GlobalMMLU. Train English logistic regression + 2-layer MLP correctness probes. Evaluate 5 transfer conditions: zero-shot, mean-shift, linear projection, few-shot (25/100), CaCLR. Report per-language Spearman ρ (depth vs transfer AUROC) alongside global ρ. Bootstrap CIs (1000 resamples) on all AUROC/ECE; paired permutation tests for method comparisons; Cohen's d for effect sizes.\\n\",\n    \"results\": {\n      \"en_auroc_best_layer\": 0.776,\n      \"en_best_layer_idx\": 72,\n      \"en_auroc_range\": [\n        0.612,\n        0.776\n      ],\n      \"en_ece_raw_best\": 0.174,\n      \"en_ece_tempcal_best\": 0.069,\n      \"temp_scaling_T\": 5.91,\n      \"zs_transfer_auroc_mean_19lang\": 0.618,\n      \"zs_transfer_auroc_median_19lang\": 0.618,\n      \"zs_transfer_auroc_std_19lang\": 0.046,\n      \"zs_transfer_drop_mean_pp\": 15.8,\n      \"zs_langs_above_0p65\": 7,\n      \"zs_pass_langs\": [\n        \"zh\",\n        \"fr\",\n        \"de\",\n        \"es\",\n        \"ja\",\n        \"ko\",\n        \"ru\"\n      ],\n      \"zs_fail_langs\": [\n        \"ar\",\n        \"hi\",\n        \"vi\",\n        \"id\",\n        \"th\",\n        \"pl\",\n        \"uk\",\n        \"bn\",\n        \"te\",\n        \"ta\",\n        \"sw\",\n        \"yo\"\n      ],\n      \"mean_shift_delta_auroc_all_langs\": 0.0,\n      \"mean_shift_delta_ece_unreliable\": true,\n      \"mean_shift_delta_ece_range_pp\": [\n        -1.2,\n        6.8\n      ],\n      \"linproj_auroc_mean_19lang\": 0.636,\n      \"linproj_improves_over_zs_count\": 11,\n      \"linproj_delta_auroc_vs_zs_mean_pp\": 1.8,\n      \"fewshot25_auroc_mean_19lang\": 0.644,\n      \"fewshot25_improves_over_zs_count\": 14,\n      \"fewshot100_auroc_mean_19lang\": 0.662,\n      \"fewshot100_improves_over_zs_count\": 16,\n      \"pareto_global_spearman_rho\": -0.38,\n      \"pareto_per_lang_rho_median\": -0.25,\n      \"pareto_per_lang_rho_range\": [\n        -0.55,\n        0.31\n      ],\n      \"pareto_rho_sign_consistency\": 0.63,\n      \"pareto_frontier_n_nondominated\": 5,\n      \"pareto_frontier_monotonic\": false,\n      \"bootstrap_ci_width_auroc_median_pp\": 2.8,\n      \"per_lang_zs_auroc\": {\n        \"zh\": 0.668,\n        \"fr\": 0.672,\n        \"de\": 0.671,\n        \"es\": 0.661,\n        \"ja\": 0.658,\n        \"ko\": 0.656,\n        \"ru\": 0.652,\n        \"ar\": 0.625,\n        \"hi\": 0.618,\n        \"vi\": 0.607,\n        \"id\": 0.621,\n        \"th\": 0.594,\n        \"pl\": 0.628,\n        \"uk\": 0.614,\n        \"bn\": 0.553,\n        \"te\": 0.571,\n        \"ta\": 0.568,\n        \"sw\": 0.537,\n        \"yo\": 0.512\n      },\n      \"per_lang_best_zs_layer\": {\n        \"zh\": 52,\n        \"fr\": 52,\n        \"de\": 52,\n        \"es\": 48,\n        \"ja\": 48,\n        \"ko\": 48,\n        \"ru\": 44,\n        \"ar\": 40,\n        \"hi\": 40,\n        \"vi\": 40,\n        \"id\": 40,\n        \"th\": 36,\n        \"pl\": 44,\n        \"uk\": 40,\n        \"bn\": 28,\n        \"te\": 28,\n        \"ta\": 28,\n        \"sw\": 28,\n        \"yo\": 24\n      },\n      \"per_lang_spearman_rho\": {\n        \"zh\": -0.55,\n        \"fr\": -0.51,\n        \"de\": -0.48,\n        \"es\": -0.42,\n        \"ja\": -0.37,\n        \"ko\": -0.33,\n        \"ru\": -0.25,\n        \"ar\": -0.18,\n        \"hi\": -0.11,\n        \"pl\": -0.14,\n        \"uk\": -0.06,\n        \"id\": -0.02,\n        \"vi\": 0.04,\n        \"th\": 0.09,\n        \"bn\": 0.14,\n        \"te\": 0.18,\n        \"ta\": 0.22,\n        \"sw\": 0.27,\n        \"yo\": 0.31\n      },\n      \"transfer_by_resource_tier\": {\n        \"high_mean\": 0.663,\n        \"high_langs\": [\n          \"zh\",\n          \"fr\",\n          \"de\",\n          \"es\",\n          \"ja\",\n          \"ko\",\n          \"ru\"\n        ],\n        \"mid_mean\": 0.615,\n        \"mid_langs\": [\n          \"ar\",\n          \"hi\",\n          \"vi\",\n          \"id\",\n          \"th\",\n          \"pl\",\n          \"uk\"\n        ],\n        \"low_mean\": 0.548,\n        \"low_langs\": [\n          \"bn\",\n          \"te\",\n          \"ta\",\n          \"sw\",\n          \"yo\"\n        ]\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: Qwen3-235B English Probe Performance by Layer (Selected Layers)\",\n        \"columns\": [\n          \"layer\",\n          \"depth_pct\",\n          \"logreg_auroc\",\n          \"mlp_auroc\",\n          \"ece_raw\",\n          \"ece_tempcal\"\n        ],\n        \"rows\": [\n          [\n            4,\n            4,\n            0.612,\n            0.618,\n            0.298,\n            0.192\n          ],\n          [\n            16,\n            17,\n            0.653,\n            0.661,\n            0.251,\n            0.148\n          ],\n          [\n            28,\n            30,\n            0.694,\n            0.708,\n            0.224,\n            0.121\n          ],\n          [\n            40,\n            43,\n            0.721,\n            0.737,\n            0.203,\n            0.098\n          ],\n          [\n            52,\n            55,\n            0.742,\n            0.755,\n            0.191,\n            0.082\n          ],\n          [\n            60,\n            64,\n            0.758,\n            0.769,\n            0.183,\n            0.075\n          ],\n          [\n            72,\n            77,\n            0.776,\n            0.783,\n            0.174,\n            0.069\n          ],\n          [\n            80,\n            85,\n            0.771,\n            0.779,\n            0.177,\n            0.072\n          ],\n          [\n            88,\n            94,\n            0.753,\n            0.762,\n            0.186,\n            0.079\n          ],\n          [\n            92,\n            98,\n            0.728,\n            0.739,\n            0.198,\n            0.091\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 2: Qwen3-235B Zero-Shot Transfer AUROC by Language (Best Transfer Layer)\",\n        \"columns\": [\n          \"language\",\n          \"family\",\n          \"resource_tier\",\n          \"best_zs_layer\",\n          \"best_zs_auroc\",\n          \"en_auroc_same_layer\",\n          \"drop_pp\",\n          \"spearman_rho\",\n          \"rho_p_value\"\n        ],\n        \"rows\": [\n          [\n            \"zh\",\n            \"sino_tibetan\",\n            \"high\",\n            52,\n            0.668,\n            0.742,\n            7.4,\n            -0.55,\n            0.006\n          ],\n          [\n            \"fr\",\n            \"romance\",\n            \"high\",\n            52,\n            0.672,\n            0.742,\n            7.0,\n            -0.51,\n            0.011\n          ],\n          [\n            \"de\",\n            \"germanic\",\n            \"high\",\n            52,\n            0.671,\n            0.742,\n            7.1,\n            -0.48,\n            0.017\n          ],\n          [\n            \"es\",\n            \"romance\",\n            \"high\",\n            48,\n            0.661,\n            0.735,\n            7.4,\n            -0.42,\n            0.041\n          ],\n          [\n            \"ja\",\n            \"japonic\",\n            \"high\",\n            48,\n            0.658,\n            0.735,\n            7.7,\n            -0.37,\n            0.075\n          ],\n          [\n            \"ko\",\n            \"koreanic\",\n            \"high\",\n            48,\n            0.656,\n            0.735,\n            7.9,\n            -0.33,\n            0.115\n          ],\n          [\n            \"ru\",\n            \"slavic\",\n            \"high\",\n            44,\n            0.652,\n            0.728,\n            7.6,\n            -0.25,\n            0.239\n          ],\n          [\n            \"pl\",\n            \"slavic\",\n            \"mid\",\n            44,\n            0.628,\n            0.728,\n            10.0,\n            -0.14,\n            0.513\n          ],\n          [\n            \"ar\",\n            \"afroasiatic\",\n            \"mid\",\n            40,\n            0.625,\n            0.721,\n            9.6,\n            -0.18,\n            0.399\n          ],\n          [\n            \"id\",\n            \"austronesian\",\n            \"mid\",\n            40,\n            0.621,\n            0.721,\n            10.0,\n            -0.02,\n            0.926\n          ],\n          [\n            \"hi\",\n            \"indic\",\n            \"mid\",\n            40,\n            0.618,\n            0.721,\n            10.3,\n            -0.11,\n            0.609\n          ],\n          [\n            \"uk\",\n            \"slavic\",\n            \"mid\",\n            40,\n            0.614,\n            0.721,\n            10.7,\n            -0.06,\n            0.782\n          ],\n          [\n            \"vi\",\n            \"austroasiatic\",\n            \"mid\",\n            40,\n            0.607,\n            0.721,\n            11.4,\n            0.04,\n            0.854\n          ],\n          [\n            \"th\",\n            \"tai_kadai\",\n            \"mid\",\n            36,\n            0.594,\n            0.712,\n            11.8,\n            0.09,\n            0.674\n          ],\n          [\n            \"bn\",\n            \"indic\",\n            \"low\",\n            28,\n            0.553,\n            0.694,\n            14.1,\n            0.14,\n            0.514\n          ],\n          [\n            \"te\",\n            \"dravidian\",\n            \"low\",\n            28,\n            0.571,\n            0.694,\n            12.3,\n            0.18,\n            0.4\n          ],\n          [\n            \"ta\",\n            \"dravidian\",\n            \"low\",\n            28,\n            0.568,\n            0.694,\n            12.6,\n            0.22,\n            0.303\n          ],\n          [\n            \"sw\",\n            \"niger_congo\",\n            \"low\",\n            28,\n            0.537,\n            0.694,\n            15.7,\n            0.27,\n            0.202\n          ],\n          [\n            \"yo\",\n            \"niger_congo\",\n            \"low\",\n            24,\n            0.512,\n            0.711,\n            19.9,\n            0.31,\n            0.141\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 3: Qwen3-235B Transfer Method Comparison (19-Language Mean at Oracle Layer)\",\n        \"columns\": [\n          \"method\",\n          \"auroc_mean\",\n          \"auroc_median\",\n          \"auroc_std\",\n          \"ece_mean\",\n          \"delta_vs_zs_pp\",\n          \"cohens_d_vs_zs\",\n          \"labels_needed\"\n        ],\n        \"rows\": [\n          [\n            \"zero_shot\",\n            0.618,\n            0.618,\n            0.046,\n            0.191,\n            0.0,\n            \"—\",\n            0\n          ],\n          [\n            \"mean_shift\",\n            0.618,\n            0.618,\n            0.046,\n            0.207,\n            0.0,\n            0.0,\n            0\n          ],\n          [\n            \"linear_projection\",\n            0.636,\n            0.633,\n            0.042,\n            0.176,\n            1.8,\n            0.24,\n            \"~50 parallel\"\n          ],\n          [\n            \"few_shot_25\",\n            0.644,\n            0.641,\n            0.04,\n            0.169,\n            2.6,\n            0.35,\n            \"25 target\"\n          ],\n          [\n            \"few_shot_100\",\n            0.662,\n            0.659,\n            0.037,\n            0.154,\n            4.4,\n            0.58,\n            \"100 target\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Pareto frontier on Qwen3-235B is real but weak: ρ = −0.38 globally, median per-language ρ = −0.25 (explains ~6% of per-language variance). The resource-tier gradient is the cleanest finding: high-resource langs (mean 0.663) transfer at 7–8pp below EN, mid-resource (0.615) at 10–11pp, low-resource (0.548) at 13–20pp. Mean-shift is confirmed mathematically dead (ΔAUROC ≡ 0, validated across all 24 layers × 19 langs). Linear projection and few-shot are the only viable transfer methods. For 12/19 languages, zero-shot transfer AUROC stays below 0.65 — the field should not assume English probes generalize.\\n\\n\\nQwen3-235B improves only modestly over the MVP's Qwen2.5-7B (EN AUROC 0.776 vs 0.754) because gains from scale are sublinear for linear probing — the larger model has more complex, distributed representations where correctness is encoded across many dimensions rather than in a single cleanly accessible direction. The Pareto frontier exists but is noisy: global Spearman ρ = -0.38 means depth explains ~15% of transfer variance. Per-language rho varies dramatically — high-resource languages that share subspace structure with English (zh, fr, de) show clear negative correlation (deeper = worse transfer), while low-resource languages (sw, yo, ta) show positive or near-zero rho because their best transfer happens at shallow layers where representations are still language-agnostic, and the signal is too weak at any depth for a clear depth gradient to emerge. MoE expert routing introduces non-monotonic noise at mid-depth layers (36-56) where routing patterns shift. Mean-shift ΔAUROC is exactly 0.000 across all languages and layers, confirming the rank-invariance proof: under StandardScaler + logistic regression, mean subtraction adds a constant to all logits, preserving ranks. ECE changes from mean-shift are unreliable because they depend on threshold-sensitive binning of shifted probabilities. Linear projection helps 11/19 languages by learning the affine transformation between language subspaces, but fails for low-resource languages where insufficient parallel data quality prevents reliable transformation estimation. Few-shot-100 is the best method but requires per-language labels, partially negating the zero-label promise.\\n\"\n  },\n  {\n    \"name\": \"Full Pareto Frontier — Llama 4 Scout (48 layers, MoE, INT8)\",\n    \"description\": \"Extract activations at 12 probed layers (every 4th of 48), 20 languages on GlobalMMLU. Train English correctness probes, evaluate 5 transfer conditions. INT8 weight quantization. Report per-language Spearman ρ. Bootstrap CIs + paired tests + Cohen's d.\\n\",\n    \"results\": {\n      \"en_auroc_best_layer\": 0.749,\n      \"en_best_layer_idx\": 36,\n      \"en_auroc_range\": [\n        0.598,\n        0.749\n      ],\n      \"en_ece_raw_best\": 0.188,\n      \"en_ece_tempcal_best\": 0.074,\n      \"temp_scaling_T\": 5.47,\n      \"zs_transfer_auroc_mean_19lang\": 0.588,\n      \"zs_transfer_auroc_median_19lang\": 0.593,\n      \"zs_transfer_auroc_std_19lang\": 0.054,\n      \"zs_transfer_drop_mean_pp\": 18.4,\n      \"zs_langs_above_0p65\": 5,\n      \"zs_pass_langs\": [\n        \"fr\",\n        \"zh\",\n        \"de\",\n        \"ko\",\n        \"es\"\n      ],\n      \"zs_fail_langs\": [\n        \"ja\",\n        \"ru\",\n        \"ar\",\n        \"hi\",\n        \"vi\",\n        \"id\",\n        \"th\",\n        \"pl\",\n        \"uk\",\n        \"bn\",\n        \"te\",\n        \"ta\",\n        \"sw\",\n        \"yo\"\n      ],\n      \"mean_shift_delta_auroc_all_langs\": 0.0,\n      \"linproj_auroc_mean_19lang\": 0.608,\n      \"linproj_improves_over_zs_count\": 10,\n      \"fewshot25_auroc_mean_19lang\": 0.617,\n      \"fewshot100_auroc_mean_19lang\": 0.641,\n      \"pareto_global_spearman_rho\": -0.18,\n      \"pareto_per_lang_rho_median\": -0.12,\n      \"pareto_per_lang_rho_range\": [\n        -0.41,\n        0.48\n      ],\n      \"pareto_rho_sign_consistency\": 0.53,\n      \"pareto_frontier_n_nondominated\": 3,\n      \"pareto_frontier_monotonic\": false,\n      \"pareto_frontier_agreement_with_qwen3_tau\": 0.33,\n      \"nonmonotonic_layers\": [\n        20,\n        24,\n        28\n      ],\n      \"per_lang_zs_auroc\": {\n        \"fr\": 0.662,\n        \"zh\": 0.658,\n        \"de\": 0.655,\n        \"ko\": 0.652,\n        \"es\": 0.651,\n        \"ja\": 0.634,\n        \"ru\": 0.622,\n        \"pl\": 0.608,\n        \"ar\": 0.589,\n        \"hi\": 0.586,\n        \"id\": 0.582,\n        \"uk\": 0.578,\n        \"vi\": 0.571,\n        \"th\": 0.558,\n        \"bn\": 0.532,\n        \"te\": 0.541,\n        \"ta\": 0.528,\n        \"sw\": 0.518,\n        \"yo\": 0.492\n      },\n      \"per_lang_spearman_rho\": {\n        \"fr\": -0.41,\n        \"zh\": -0.37,\n        \"de\": -0.32,\n        \"ko\": -0.21,\n        \"es\": -0.18,\n        \"ja\": -0.08,\n        \"ru\": -0.04,\n        \"pl\": 0.03,\n        \"ar\": 0.07,\n        \"hi\": 0.11,\n        \"id\": 0.15,\n        \"uk\": 0.18,\n        \"vi\": 0.22,\n        \"th\": 0.28,\n        \"bn\": 0.31,\n        \"te\": 0.35,\n        \"ta\": 0.38,\n        \"sw\": 0.43,\n        \"yo\": 0.48\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 4: Llama 4 Scout English Probe Performance by Layer\",\n        \"columns\": [\n          \"layer\",\n          \"depth_pct\",\n          \"logreg_auroc\",\n          \"mlp_auroc\",\n          \"ece_raw\",\n          \"ece_tempcal\"\n        ],\n        \"rows\": [\n          [\n            4,\n            8,\n            0.598,\n            0.604,\n            0.312,\n            0.201\n          ],\n          [\n            8,\n            17,\n            0.631,\n            0.641,\n            0.274,\n            0.168\n          ],\n          [\n            12,\n            25,\n            0.668,\n            0.679,\n            0.241,\n            0.137\n          ],\n          [\n            16,\n            33,\n            0.694,\n            0.706,\n            0.218,\n            0.112\n          ],\n          [\n            20,\n            42,\n            0.712,\n            0.722,\n            0.205,\n            0.098\n          ],\n          [\n            24,\n            50,\n            0.726,\n            0.735,\n            0.196,\n            0.088\n          ],\n          [\n            28,\n            58,\n            0.734,\n            0.743,\n            0.192,\n            0.083\n          ],\n          [\n            32,\n            67,\n            0.741,\n            0.749,\n            0.189,\n            0.078\n          ],\n          [\n            36,\n            75,\n            0.749,\n            0.755,\n            0.188,\n            0.074\n          ],\n          [\n            40,\n            83,\n            0.744,\n            0.751,\n            0.19,\n            0.077\n          ],\n          [\n            44,\n            92,\n            0.731,\n            0.738,\n            0.195,\n            0.084\n          ],\n          [\n            48,\n            100,\n            0.708,\n            0.718,\n            0.209,\n            0.097\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 5: Llama 4 Scout Zero-Shot Transfer AUROC by Language\",\n        \"columns\": [\n          \"language\",\n          \"resource_tier\",\n          \"best_zs_layer\",\n          \"best_zs_auroc\",\n          \"drop_vs_en_pp\",\n          \"spearman_rho\"\n        ],\n        \"rows\": [\n          [\n            \"fr\",\n            \"high\",\n            24,\n            0.662,\n            6.4,\n            -0.41\n          ],\n          [\n            \"zh\",\n            \"high\",\n            24,\n            0.658,\n            6.8,\n            -0.37\n          ],\n          [\n            \"de\",\n            \"high\",\n            24,\n            0.655,\n            7.1,\n            -0.32\n          ],\n          [\n            \"ko\",\n            \"high\",\n            20,\n            0.652,\n            6.0,\n            -0.21\n          ],\n          [\n            \"es\",\n            \"high\",\n            24,\n            0.651,\n            7.5,\n            -0.18\n          ],\n          [\n            \"ja\",\n            \"high\",\n            20,\n            0.634,\n            7.8,\n            -0.08\n          ],\n          [\n            \"ru\",\n            \"high\",\n            20,\n            0.622,\n            9.0,\n            -0.04\n          ],\n          [\n            \"pl\",\n            \"mid\",\n            20,\n            0.608,\n            10.4,\n            0.03\n          ],\n          [\n            \"ar\",\n            \"mid\",\n            16,\n            0.589,\n            10.5,\n            0.07\n          ],\n          [\n            \"hi\",\n            \"mid\",\n            16,\n            0.586,\n            10.8,\n            0.11\n          ],\n          [\n            \"id\",\n            \"mid\",\n            16,\n            0.582,\n            11.2,\n            0.15\n          ],\n          [\n            \"uk\",\n            \"mid\",\n            16,\n            0.578,\n            11.6,\n            0.18\n          ],\n          [\n            \"vi\",\n            \"mid\",\n            16,\n            0.571,\n            12.3,\n            0.22\n          ],\n          [\n            \"th\",\n            \"mid\",\n            16,\n            0.558,\n            13.6,\n            0.28\n          ],\n          [\n            \"te\",\n            \"low\",\n            12,\n            0.541,\n            12.7,\n            0.35\n          ],\n          [\n            \"bn\",\n            \"low\",\n            12,\n            0.532,\n            13.6,\n            0.31\n          ],\n          [\n            \"ta\",\n            \"low\",\n            12,\n            0.528,\n            14.0,\n            0.38\n          ],\n          [\n            \"sw\",\n            \"low\",\n            12,\n            0.518,\n            15.0,\n            0.43\n          ],\n          [\n            \"yo\",\n            \"low\",\n            8,\n            0.492,\n            13.9,\n            0.48\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 6: Cross-Architecture Pareto Agreement\",\n        \"columns\": [\n          \"metric\",\n          \"qwen3_235b\",\n          \"llama4_scout\",\n          \"agreement\"\n        ],\n        \"rows\": [\n          [\n            \"global_spearman_rho\",\n            -0.38,\n            -0.18,\n            \"—\"\n          ],\n          [\n            \"per_lang_rho_median\",\n            -0.25,\n            -0.12,\n            \"—\"\n          ],\n          [\n            \"sign_consistency\",\n            0.63,\n            0.53,\n            \"—\"\n          ],\n          [\n            \"n_nondominated\",\n            \"5/24\",\n            \"3/12\",\n            \"—\"\n          ],\n          [\n            \"zs_auroc_mean\",\n            0.618,\n            0.588,\n            \"—\"\n          ],\n          [\n            \"optimal_layer_rank_tau\",\n            \"—\",\n            \"—\",\n            0.33\n          ],\n          [\n            \"pass_lang_jaccard\",\n            \"—\",\n            \"—\",\n            0.47\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Llama 4 Scout demolishes the universal Pareto claim. ρ = −0.18 globally, median per-lang ρ = −0.12, sign consistency 0.53. Cross-architecture agreement τ = 0.33. This transforms the paper: the depth-transfer tradeoff is architecture-dependent, not a universal transformer property. Practitioners cannot use layer selection findings from one model on another. For the diagnostic paper, this is reframed as a key finding: \\\"the field cannot assume probe-based calibration will behave consistently across architectures.\\\"\\n\\n\\nLlama 4 Scout is the worst-tier's key failure for the Pareto claim. Its 48 layers give only 12 probed points (vs 24 for Qwen3), reducing statistical power for Spearman ρ. More critically, Llama 4 Scout uses a different MoE routing strategy where experts are more language-specialized at intermediate layers (20–28), creating non-monotonic jumps in transfer AUROC that break the depth gradient. Per-language rho median = −0.12 means the depth-transfer tradeoff essentially vanishes on this architecture. Only 5/19 languages pass 0.65 (vs 7 for Qwen3), and the cross-architecture Pareto agreement is τ = 0.33 — optimal layer for a language on Qwen3 does not predict optimal layer on Llama 4. English AUROC peaks lower (0.749 vs 0.776) because the 48-layer structure compresses the representational hierarchy. Transfer is worse overall (0.588 vs 0.618) reflecting more English-centric training data and sparser expert allocation for non-English. The 0.53 sign consistency means the depth-transfer direction is nearly coin-flip across languages — the \\\"Pareto frontier\\\" is architecture-specific, not a universal property.\\n\"\n  },\n  {\n    \"name\": \"CaCLR Implementation and Comparative Evaluation\",\n    \"description\": \"Implement CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency with MMD). Train using English labels + unlabeled parallel activations from GlobalMMLU train split. Compare vs zero-shot, mean-shift, linear projection, few-shot across full Pareto frontier for both models × 19 target languages. α sweep (0.01–10.0), β sweep across 3 OOM (0.001–1.0). Fixed-layer results (50% depth + EN-optimal) alongside per-language oracle.\\n\",\n    \"results\": {\n      \"best_alpha\": 0.3,\n      \"best_beta\": 0.05,\n      \"beta_sensitivity\": \"flat — β from 0.001 to 1.0 changes AUROC by <0.4pp; consistency loss is inert\",\n      \"alpha_sensitivity\": \"moderate — α = 0.1–1.0 gives similar results; inverted-U peaking at 0.3\",\n      \"caclr_auroc_mean_qwen3\": 0.623,\n      \"caclr_auroc_mean_llama4\": 0.594,\n      \"caclr_vs_zs_delta_auroc_mean_pp_qwen3\": 0.5,\n      \"caclr_vs_zs_delta_auroc_mean_pp_llama4\": 0.6,\n      \"caclr_vs_zs_delta_auroc_median_pp\": 0.003,\n      \"caclr_vs_linproj_delta_auroc_mean_pp_qwen3\": -1.3,\n      \"caclr_vs_linproj_delta_auroc_mean_pp_llama4\": -1.4,\n      \"caclr_vs_fewshot100_delta_pp_qwen3\": -3.9,\n      \"caclr_vs_fewshot100_delta_pp_llama4\": -4.7,\n      \"caclr_ece_mean_qwen3\": 0.186,\n      \"caclr_ece_mean_llama4\": 0.201,\n      \"caclr_ece_reduction_vs_tempcal_pp\": -0.002,\n      \"ablation_bce_only_auroc_mean\": 0.618,\n      \"ablation_bce_sbece_auroc_mean\": 0.627,\n      \"ablation_bce_consistency_auroc_mean\": 0.611,\n      \"ablation_full_caclr_auroc_mean\": 0.621,\n      \"beta_delta_over_alpha_only_pp\": -0.006,\n      \"cohens_d_caclr_vs_zs\": 0.04,\n      \"cohens_d_caclr_vs_linproj\": -0.18,\n      \"permutation_test_caclr_vs_zs_p\": 0.71,\n      \"caclr_per_lang_qwen3\": {\n        \"zh\": {\n          \"auroc\": 0.671,\n          \"delta_vs_zs_pp\": 0.3\n        },\n        \"fr\": {\n          \"auroc\": 0.667,\n          \"delta_vs_zs_pp\": -0.5\n        },\n        \"de\": {\n          \"auroc\": 0.664,\n          \"delta_vs_zs_pp\": -0.7\n        },\n        \"es\": {\n          \"auroc\": 0.657,\n          \"delta_vs_zs_pp\": -0.4\n        },\n        \"ja\": {\n          \"auroc\": 0.653,\n          \"delta_vs_zs_pp\": -0.5\n        },\n        \"ko\": {\n          \"auroc\": 0.652,\n          \"delta_vs_zs_pp\": -0.4\n        },\n        \"ru\": {\n          \"auroc\": 0.649,\n          \"delta_vs_zs_pp\": -0.3\n        },\n        \"pl\": {\n          \"auroc\": 0.631,\n          \"delta_vs_zs_pp\": 0.3\n        },\n        \"ar\": {\n          \"auroc\": 0.631,\n          \"delta_vs_zs_pp\": 0.6\n        },\n        \"id\": {\n          \"auroc\": 0.627,\n          \"delta_vs_zs_pp\": 0.6\n        },\n        \"hi\": {\n          \"auroc\": 0.625,\n          \"delta_vs_zs_pp\": 0.7\n        },\n        \"uk\": {\n          \"auroc\": 0.621,\n          \"delta_vs_zs_pp\": 0.7\n        },\n        \"vi\": {\n          \"auroc\": 0.615,\n          \"delta_vs_zs_pp\": 0.8\n        },\n        \"th\": {\n          \"auroc\": 0.603,\n          \"delta_vs_zs_pp\": 0.9\n        },\n        \"bn\": {\n          \"auroc\": 0.564,\n          \"delta_vs_zs_pp\": 1.1\n        },\n        \"te\": {\n          \"auroc\": 0.581,\n          \"delta_vs_zs_pp\": 1.0\n        },\n        \"ta\": {\n          \"auroc\": 0.578,\n          \"delta_vs_zs_pp\": 1.0\n        },\n        \"sw\": {\n          \"auroc\": 0.549,\n          \"delta_vs_zs_pp\": 1.2\n        },\n        \"yo\": {\n          \"auroc\": 0.526,\n          \"delta_vs_zs_pp\": 1.4\n        }\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 7: Transfer Method Comparison — Both Models (19-Language Mean)\",\n        \"columns\": [\n          \"method\",\n          \"qwen3_auroc\",\n          \"qwen3_ece\",\n          \"llama4_auroc\",\n          \"llama4_ece\",\n          \"cohens_d_vs_zs\",\n          \"labels_needed\"\n        ],\n        \"rows\": [\n          [\n            \"zero_shot\",\n            0.618,\n            0.191,\n            0.588,\n            0.208,\n            \"—\",\n            \"0 target\"\n          ],\n          [\n            \"mean_shift\",\n            0.618,\n            0.207,\n            0.588,\n            0.224,\n            0.0,\n            \"0 target (ΔAUROC≡0)\"\n          ],\n          [\n            \"CaCLR\",\n            0.623,\n            0.186,\n            0.594,\n            0.201,\n            0.04,\n            \"0 target + parallel\"\n          ],\n          [\n            \"linear_projection\",\n            0.636,\n            0.176,\n            0.608,\n            0.189,\n            0.24,\n            \"~50 parallel\"\n          ],\n          [\n            \"few_shot_25\",\n            0.644,\n            0.169,\n            0.617,\n            0.182,\n            0.35,\n            \"25 target\"\n          ],\n          [\n            \"few_shot_100\",\n            0.662,\n            0.154,\n            0.641,\n            0.168,\n            0.58,\n            \"100 target\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 8: CaCLR Ablation (Qwen3-235B, 19-Language Mean)\",\n        \"columns\": [\n          \"variant\",\n          \"auroc_mean\",\n          \"ece_mean\",\n          \"delta_vs_full_pp\"\n        ],\n        \"rows\": [\n          [\n            \"Full CaCLR (BCE+SB-ECE+Consistency)\",\n            0.621,\n            0.186,\n            0.0\n          ],\n          [\n            \"BCE+SB-ECE (no consistency)\",\n            0.627,\n            0.179,\n            0.6\n          ],\n          [\n            \"BCE+Consistency (no SB-ECE)\",\n            0.611,\n            0.198,\n            -1.0\n          ],\n          [\n            \"BCE only (= zero-shot probe)\",\n            0.618,\n            0.191,\n            -0.3\n          ],\n          [\n            \"Linear Projection (reference)\",\n            0.636,\n            0.176,\n            1.5\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 9: CaCLR β Sensitivity (Qwen3, α fixed at 0.3, 19-lang mean AUROC)\",\n        \"columns\": [\n          \"beta\",\n          \"auroc_mean\",\n          \"delta_vs_beta0_pp\"\n        ],\n        \"rows\": [\n          [\n            0.0,\n            0.627,\n            0.0\n          ],\n          [\n            0.001,\n            0.626,\n            -0.1\n          ],\n          [\n            0.005,\n            0.625,\n            -0.2\n          ],\n          [\n            0.01,\n            0.625,\n            -0.2\n          ],\n          [\n            0.05,\n            0.623,\n            -0.4\n          ],\n          [\n            0.1,\n            0.621,\n            -0.6\n          ],\n          [\n            0.5,\n            0.618,\n            -0.9\n          ],\n          [\n            1.0,\n            0.614,\n            -1.3\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CaCLR is a rigorous negative result. The ablation cleanly isolates the failure: consistency loss is harmful (adding it to BCE+SB-ECE reduces AUROC by 0.6pp). The β sweep over 3 OOM confirms this is not a tuning failure — the entire β landscape is flat or declining. CKA analysis (plan_011) provides the mechanistic explanation: cross-lingual misalignment at deeper layers is geometric (correctness direction rotates), not distributional (mean/cov shift). MMD-based alignment cannot correct rotation, which is why linear projection (learns rotation) succeeds where CaCLR (matches distributions) fails. For the paper, CaCLR is reported as attempted-and-failed, saving the community from pursuing distributional-matching approaches for this problem class.\\n\\n\\nCaCLR fully fails as a method contribution. The consistency loss (β·L_consistency) is inert: sweeping β over 3 orders of magnitude produces a flat AUROC landscape (<0.4pp variation). Adding consistency to BCE+SB-ECE actually hurts by −0.6pp because MMD-based alignment collapses both signal and noise — the unlabeled parallel activations contain massive language-specific variance (script, morphology, tokenization artifacts) that dominates the correctness signal. Minimizing distributional distance between languages forces the probe to ignore language-specific activation patterns that sometimes carry cross-lingual correctness information. The ablation reveals that the only beneficial component is SB-ECE regularization (+0.9pp), which acts as a calibration regularizer on the English training side but has nothing to do with cross-lingual transfer. Full CaCLR ends up as \\\"zero-shot + SB-ECE regularization\\\" — a trivially achievable benefit that does not justify the method's complexity. Linear projection beats CaCLR because it directly estimates the geometric transformation between language subspaces, which is more data-efficient than trying to learn an invariant representation from noisy distributional signals. The paired permutation test CaCLR vs zero-shot gives p = 0.71 — no significant difference. Cohen's d = 0.04 confirms negligible effect size. CaCLR slightly helps low-resource languages (+1pp) and slightly hurts high-resource (−0.5pp), but both effects are within noise. For the paper, CaCLR is relegated to one paragraph: \\\"the natural distributional- matching approach fails — consistency-based objectives do not help when cross-lingual correctness SNR is low.\\\"\\n\"\n  },\n  {\n    \"name\": \"Difficulty-Controlled Ablation (Decomposition)\",\n    \"description\": \"Train IRT difficulty probes (Ridge regression on human difficulty scores per Civelli et al.), project out difficulty direction from activations, retrain correctness probes on residuals, evaluate transfer. 10 languages × 8 layers per model. Include random-direction control.\\n\",\n    \"results\": {\n      \"difficulty_probe_r2_en_qwen3\": 0.52,\n      \"difficulty_probe_r2_en_llama4\": 0.47,\n      \"difficulty_probe_transfer_r2_mean_9lang\": 0.38,\n      \"decomp_difficulty_var_explained_pct_qwen3\": 14.3,\n      \"decomp_difficulty_var_explained_pct_llama4\": 11.8,\n      \"correctness_on_residual_auroc_en_qwen3\": 0.741,\n      \"correctness_on_residual_auroc_en_llama4\": 0.714,\n      \"residual_transfer_auroc_mean_qwen3\": 0.613,\n      \"residual_transfer_auroc_mean_llama4\": 0.583,\n      \"transfer_delta_after_projection_pp_qwen3\": -0.5,\n      \"transfer_delta_after_projection_pp_llama4\": -0.5,\n      \"transfer_delta_range_across_langs_pp\": [\n        -2.1,\n        1.3\n      ],\n      \"random_direction_control_delta_pp\": -0.3,\n      \"difficulty_correctness_cosine_mean\": 0.36,\n      \"difficulty_correctness_cosine_std\": 0.11,\n      \"decomp_prescriptive\": false,\n      \"pct_langs_helped_by_projection\": 0.3,\n      \"pct_langs_hurt_by_projection\": 0.5,\n      \"pct_langs_unchanged\": 0.2\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 10: Difficulty Probe Quality (Ridge, R² on Held-Out)\",\n        \"columns\": [\n          \"language\",\n          \"resource_tier\",\n          \"qwen3_r2\",\n          \"llama4_r2\"\n        ],\n        \"rows\": [\n          [\n            \"en\",\n            \"—\",\n            0.52,\n            0.47\n          ],\n          [\n            \"zh\",\n            \"high\",\n            0.48,\n            0.43\n          ],\n          [\n            \"fr\",\n            \"high\",\n            0.47,\n            0.42\n          ],\n          [\n            \"de\",\n            \"high\",\n            0.46,\n            0.41\n          ],\n          [\n            \"hi\",\n            \"mid\",\n            0.41,\n            0.36\n          ],\n          [\n            \"ru\",\n            \"mid\",\n            0.43,\n            0.38\n          ],\n          [\n            \"ko\",\n            \"mid\",\n            0.42,\n            0.37\n          ],\n          [\n            \"tr\",\n            \"mid\",\n            0.39,\n            0.34\n          ],\n          [\n            \"sw\",\n            \"low\",\n            0.3,\n            0.25\n          ],\n          [\n            \"bn\",\n            \"low\",\n            0.28,\n            0.23\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 11: Decomposition Transfer Ablation (9-Language Mean)\",\n        \"columns\": [\n          \"condition\",\n          \"qwen3_auroc\",\n          \"qwen3_delta_pp\",\n          \"llama4_auroc\",\n          \"llama4_delta_pp\"\n        ],\n        \"rows\": [\n          [\n            \"Full activations (baseline)\",\n            0.618,\n            0.0,\n            0.588,\n            0.0\n          ],\n          [\n            \"Residual (difficulty out)\",\n            0.613,\n            -0.5,\n            0.583,\n            -0.5\n          ],\n          [\n            \"Difficulty component only\",\n            0.569,\n            -4.9,\n            0.548,\n            -4.0\n          ],\n          [\n            \"Random direction out (ctrl)\",\n            0.615,\n            -0.3,\n            0.585,\n            -0.3\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 12: Per-Language Transfer Delta After Difficulty Projection (Qwen3)\",\n        \"columns\": [\n          \"language\",\n          \"resource_tier\",\n          \"delta_auroc_pp\",\n          \"direction\"\n        ],\n        \"rows\": [\n          [\n            \"zh\",\n            \"high\",\n            -0.8,\n            \"hurt\"\n          ],\n          [\n            \"fr\",\n            \"high\",\n            -1.2,\n            \"hurt\"\n          ],\n          [\n            \"de\",\n            \"high\",\n            -0.6,\n            \"hurt\"\n          ],\n          [\n            \"hi\",\n            \"mid\",\n            0.4,\n            \"helped\"\n          ],\n          [\n            \"ru\",\n            \"mid\",\n            -0.3,\n            \"unchanged\"\n          ],\n          [\n            \"ko\",\n            \"mid\",\n            1.0,\n            \"helped\"\n          ],\n          [\n            \"tr\",\n            \"mid\",\n            -2.1,\n            \"hurt\"\n          ],\n          [\n            \"sw\",\n            \"low\",\n            1.3,\n            \"helped\"\n          ],\n          [\n            \"bn\",\n            \"low\",\n            -0.8,\n            \"hurt\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Decomposition fails as a prescriptive tool. The difficulty-shared component is load-bearing for cross-lingual transfer — removing it hurts more often than it helps (5/10 vs 3/10), and the average delta (−0.5pp) is barely above the random-direction control (−0.3pp). The original Claim 2 hypothesis is abandoned. For the diagnostic paper, this becomes: \\\"difficulty and capability are entangled in multilingual representations — the clean separation reported in English-only work does not generalize cross-lingually.\\\"\\n\\n\\nDecomposition is inconclusive. Projecting out difficulty direction changes transfer AUROC by −0.5pp on average — within noise (random-direction control shows −0.3pp from dimensionality reduction alone). The per-language pattern shows no systematic structure: 3/10 languages improve slightly (1–1.3pp), 5/10 worsen (0.5–2.1pp), 2/10 unchanged. The difficulty direction explains only 14% of correctness variance (Qwen3), meaning the decomposition captures a real but minor factor. Critically, the difficulty-shared component turns out to carry useful cross-lingual signal: questions that are hard in English tend to be hard everywhere, and this shared difficulty is one of few reliable cross-lingual bridges. Removing it strips away a genuine invariance. The residual \\\"capability-specific\\\" component is more language-dependent, not less — containing idiosyncratic encoding patterns. The cosine between difficulty and correctness directions (0.36 ± 0.11) confirms they are neither orthogonal nor aligned — the moderate overlap prevents clean separation. This contradicts Claim 2's hypothesis that decomposition would be prescriptive. For the paper, decomposition is reported as \\\"difficulty and capability are entangled in multilingual representations, unlike the clean separation assumed by English-only work.\\\"\\n\"\n  },\n  {\n    \"name\": \"Cross-Lingual Orthogonality Analysis\",\n    \"description\": \"Extract verbalized confidence direction (prompt model for confidence score, fit probe), compute cosine similarity with correctness direction across 20 languages × 2 architectures. Analyze by resource tier and language family.\\n\",\n    \"results\": {\n      \"orthogonality_cosine_mean_overall\": 0.074,\n      \"orthogonality_cosine_std_overall\": 0.036,\n      \"orthogonality_cosine_mean_qwen3\": 0.069,\n      \"orthogonality_cosine_mean_llama4\": 0.079,\n      \"orthogonality_cosine_max_across_all\": 0.172,\n      \"orthogonality_cosine_high_resource\": 0.052,\n      \"orthogonality_cosine_mid_resource\": 0.073,\n      \"orthogonality_cosine_low_resource\": 0.108,\n      \"pct_langs_cosine_below_0p10\": 0.73,\n      \"pct_langs_cosine_below_0p05\": 0.3,\n      \"outlier_langs_above_0p15\": [\n        \"yo_llama4\"\n      ],\n      \"confidence_probe_r2_en\": 0.71,\n      \"confidence_probe_transfer_r2_mean\": 0.58,\n      \"cosine_resource_tier_spearman\": -0.61,\n      \"per_lang_cosine\": {\n        \"en\": {\n          \"qwen3\": 0.036,\n          \"llama4\": 0.041,\n          \"mean\": 0.039\n        },\n        \"zh\": {\n          \"qwen3\": 0.041,\n          \"llama4\": 0.048,\n          \"mean\": 0.045\n        },\n        \"fr\": {\n          \"qwen3\": 0.044,\n          \"llama4\": 0.052,\n          \"mean\": 0.048\n        },\n        \"de\": {\n          \"qwen3\": 0.046,\n          \"llama4\": 0.054,\n          \"mean\": 0.05\n        },\n        \"es\": {\n          \"qwen3\": 0.048,\n          \"llama4\": 0.057,\n          \"mean\": 0.053\n        },\n        \"ja\": {\n          \"qwen3\": 0.053,\n          \"llama4\": 0.061,\n          \"mean\": 0.057\n        },\n        \"ru\": {\n          \"qwen3\": 0.056,\n          \"llama4\": 0.064,\n          \"mean\": 0.06\n        },\n        \"ko\": {\n          \"qwen3\": 0.058,\n          \"llama4\": 0.067,\n          \"mean\": 0.063\n        },\n        \"ar\": {\n          \"qwen3\": 0.064,\n          \"llama4\": 0.073,\n          \"mean\": 0.069\n        },\n        \"hi\": {\n          \"qwen3\": 0.067,\n          \"llama4\": 0.076,\n          \"mean\": 0.072\n        },\n        \"vi\": {\n          \"qwen3\": 0.069,\n          \"llama4\": 0.078,\n          \"mean\": 0.074\n        },\n        \"id\": {\n          \"qwen3\": 0.065,\n          \"llama4\": 0.074,\n          \"mean\": 0.07\n        },\n        \"th\": {\n          \"qwen3\": 0.074,\n          \"llama4\": 0.084,\n          \"mean\": 0.079\n        },\n        \"pl\": {\n          \"qwen3\": 0.06,\n          \"llama4\": 0.068,\n          \"mean\": 0.064\n        },\n        \"uk\": {\n          \"qwen3\": 0.063,\n          \"llama4\": 0.072,\n          \"mean\": 0.068\n        },\n        \"bn\": {\n          \"qwen3\": 0.085,\n          \"llama4\": 0.098,\n          \"mean\": 0.092\n        },\n        \"te\": {\n          \"qwen3\": 0.092,\n          \"llama4\": 0.106,\n          \"mean\": 0.099\n        },\n        \"ta\": {\n          \"qwen3\": 0.096,\n          \"llama4\": 0.112,\n          \"mean\": 0.104\n        },\n        \"sw\": {\n          \"qwen3\": 0.104,\n          \"llama4\": 0.124,\n          \"mean\": 0.114\n        },\n        \"yo\": {\n          \"qwen3\": 0.121,\n          \"llama4\": 0.172,\n          \"mean\": 0.147\n        }\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 13: Correctness-Confidence Cosine Similarity by Resource Tier\",\n        \"columns\": [\n          \"resource_tier\",\n          \"n_langs\",\n          \"qwen3_mean\",\n          \"llama4_mean\",\n          \"overall_mean\",\n          \"std\"\n        ],\n        \"rows\": [\n          [\n            \"high\",\n            8,\n            0.048,\n            0.056,\n            0.052,\n            0.008\n          ],\n          [\n            \"mid\",\n            7,\n            0.066,\n            0.075,\n            0.073,\n            0.005\n          ],\n          [\n            \"low\",\n            5,\n            0.1,\n            0.122,\n            0.108,\n            0.02\n          ],\n          [\n            \"all\",\n            20,\n            0.069,\n            0.079,\n            0.074,\n            0.036\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Orthogonality survives as the one mechanistic takeaway: output-based calibration is structurally limited everywhere, not just in English. But the contribution is incremental — same qualitative finding as Miao & Ungar, extended to 20 languages. The resource-tier modulation is novel (effect size 0.052 vs 0.108) but the Yoruba outlier at 0.172 weakens the universality claim. For the paper: \\\"correctness-confidence dissociation is multilingual, confirming output-based calibration faces a structural ceiling regardless of language, but this ceiling is noisier for low-resource languages.\\\"\\n\\n\\nOrthogonality persists cross-lingually (mean cosine 0.074) because it reflects a structural property of how LLMs separate verbalized confidence from actual correctness at the representation level. However, the worst-tier variance is higher than Miao & Ungar's English-only finding (std 0.036 vs ~0.01): low-resource languages show weaker orthogonality (cosine ~0.108) because the model has less capacity to maintain the confidence-correctness dissociation for languages with limited training data. Yoruba on Llama4 reaches 0.172 — an outlier above the 0.15 threshold that weakens the universality claim. This happens because Llama4 has minimal Yoruba training data, so both correctness and confidence signals degrade in correlated ways, partially breaking orthogonality. The resource-tier gradient (high: 0.052, mid: 0.073, low: 0.108, Spearman ρ = −0.61 with resource level) is the novel angle, but effect size is modest. Reviewers may see the extension from English-only (Miao & Ungar) to 20 languages as incremental rather than novel, since the qualitative finding is the same.\\n\"\n  },\n  {\n    \"name\": \"Probe Complexity Comparison\",\n    \"description\": \"Logistic regression vs 2-layer MLP at each probed layer for both models. Compare English accuracy, cross-lingual transfer, calibration. Test hypothesis: linear probes transfer better.\\n\",\n    \"results\": {\n      \"mlp_vs_logreg_en_auroc_delta_mean_pp\": 1.0,\n      \"mlp_vs_logreg_transfer_auroc_delta_mean_pp\": -0.3,\n      \"hypothesis_linear_transfers_better\": \"weak support\",\n      \"cohens_d_transfer_difference\": 0.15,\n      \"permutation_test_p\": 0.34,\n      \"mlp_en_advantage_deep_layers_pp\": 1.4,\n      \"logreg_transfer_advantage_deep_layers_pp\": 0.6,\n      \"interaction_depth_probe_significant\": false\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 14: Probe Complexity Comparison (Mean Across All Layers)\",\n        \"columns\": [\n          \"model\",\n          \"probe\",\n          \"en_auroc_mean\",\n          \"transfer_auroc_mean\",\n          \"en_ece_mean\",\n          \"transfer_ece_mean\"\n        ],\n        \"rows\": [\n          [\n            \"qwen3\",\n            \"logreg\",\n            0.714,\n            0.618,\n            0.206,\n            0.191\n          ],\n          [\n            \"qwen3\",\n            \"mlp\",\n            0.725,\n            0.615,\n            0.198,\n            0.194\n          ],\n          [\n            \"llama4\",\n            \"logreg\",\n            0.697,\n            0.588,\n            0.219,\n            0.208\n          ],\n          [\n            \"llama4\",\n            \"mlp\",\n            0.706,\n            0.586,\n            0.212,\n            0.211\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Non-finding. Effect is real but negligible (d = 0.15). Logistic regression confirmed as default choice: simpler, nearly identical performance, better interpretability. Goes in supplementary as methods validation.\\n\\n\\nLinear probes transfer marginally better (−0.3pp MLP penalty in transfer vs +1.0pp MLP advantage in English), but Cohen's d = 0.15 and the permutation test is non-significant (p = 0.34). The effect is too small to be practically meaningful. MLP captures mild nonlinearities in the correctness signal but these are English-specific features that don't generalize. The depth interaction exists weakly (MLP overfits more at deep layers) but isn't statistically significant as an interaction term. This validates logistic regression as the right default but generates no standalone finding.\\n\"\n  },\n  {\n    \"name\": \"Additional Benchmark Evaluation (Belebele + MMLU-ProX)\",\n    \"description\": \"Evaluate best probes + CaCLR on Belebele (reading comprehension, 20 languages) and MMLU-ProX (translated MMLU, 20 languages). Tests cross-benchmark generalization.\\n\",\n    \"results\": {\n      \"belebele_en_auroc_qwen3\": 0.741,\n      \"belebele_en_auroc_llama4\": 0.718,\n      \"belebele_zs_transfer_mean_qwen3\": 0.594,\n      \"belebele_zs_transfer_mean_llama4\": 0.567,\n      \"belebele_drop_vs_globalmmlu_pp\": 2.4,\n      \"belebele_caclr_delta_vs_linproj_pp\": -0.8,\n      \"mmlupx_en_auroc_qwen3\": 0.762,\n      \"mmlupx_en_auroc_llama4\": 0.738,\n      \"mmlupx_zs_transfer_mean_qwen3\": 0.579,\n      \"mmlupx_zs_transfer_mean_llama4\": 0.551,\n      \"mmlupx_drop_vs_globalmmlu_pp\": 3.9,\n      \"mmlupx_caclr_delta_vs_linproj_pp\": -1.1,\n      \"lang_rank_corr_globalmmlu_belebele\": 0.83,\n      \"lang_rank_corr_globalmmlu_mmlupx\": 0.69\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 15: Cross-Benchmark Generalization (19-Language Mean)\",\n        \"columns\": [\n          \"benchmark\",\n          \"zs_auroc_qwen3\",\n          \"zs_auroc_llama4\",\n          \"caclr_vs_linproj_pp\",\n          \"lang_rank_corr\"\n        ],\n        \"rows\": [\n          [\n            \"GlobalMMLU\",\n            0.618,\n            0.588,\n            -1.3,\n            \"—\"\n          ],\n          [\n            \"Belebele\",\n            0.594,\n            0.567,\n            -0.8,\n            0.83\n          ],\n          [\n            \"MMLU-ProX\",\n            0.579,\n            0.551,\n            -1.1,\n            0.69\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Findings partially generalize: Belebele confirms, MMLU-ProX is noisier. Language ranking stable but absolute performance degrades with domain shift. CaCLR's negative result is robust across all three benchmarks. Include Belebele in main results, MMLU-ProX in supplementary with translation-artifact caveat.\\n\\n\\nBelebele partially replicates because it is high-quality and natively multilingual. The 2.4pp transfer drop reflects domain shift (reading comprehension vs knowledge). MMLU-ProX shows worse transfer (3.9pp drop) because machine-translated MMLU introduces systematic distributional shifts (ambiguous domain terms, cultural references, low-resource translation errors). CaCLR remains worse than linear projection on both benchmarks, confirming the negative result generalizes. Language ranking is stable for Belebele (ρ = 0.83) but degrades for MMLU-ProX (ρ = 0.69) due to translation quality variation.\\n\"\n  },\n  {\n    \"name\": \"INT8 Validation Ablation\",\n    \"description\": \"Compare INT8 vs FP16 probing results at 5 representative layers for Llama 4 Scout on 5% random subset. Validates quantization doesn't distort correctness signals.\\n\",\n    \"results\": {\n      \"int8_vs_fp16_auroc_delta_mean_pp\": -0.3,\n      \"int8_vs_fp16_auroc_delta_max_pp\": -0.7,\n      \"int8_vs_fp16_ece_delta_mean_pp\": 0.2,\n      \"int8_vs_fp16_activation_cosine_sim_mean\": 0.994,\n      \"int8_vs_fp16_rank_correlation_layers\": 0.98,\n      \"validation_passes\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S1: INT8 vs FP16 Comparison (Llama 4 Scout, 5% subset)\",\n        \"columns\": [\n          \"layer\",\n          \"fp16_auroc\",\n          \"int8_auroc\",\n          \"delta_pp\",\n          \"activation_cosine\"\n        ],\n        \"rows\": [\n          [\n            8,\n            0.637,\n            0.633,\n            -0.4,\n            0.993\n          ],\n          [\n            16,\n            0.7,\n            0.697,\n            -0.3,\n            0.994\n          ],\n          [\n            24,\n            0.731,\n            0.729,\n            -0.2,\n            0.995\n          ],\n          [\n            32,\n            0.746,\n            0.743,\n            -0.3,\n            0.994\n          ],\n          [\n            40,\n            0.748,\n            0.741,\n            -0.7,\n            0.992\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"INT8 validation passes. Quantization is not a confound. One paragraph + Table S1 in supplementary.\\n\\n\\nINT8 quantization introduces minimal distortion. The 0.3pp mean AUROC difference is within noise — INT8 preserves directional structure of activations that linear probes rely on. Cosine similarity 0.994 between INT8 and FP16 activations confirms near-perfect directional alignment. Layer ranking is preserved (rank corr 0.98). This passes cleanly even in the worst tier — quantization is not a source of failure.\\n\"\n  },\n  {\n    \"name\": \"CKA Cross-Lingual Representation Similarity Analysis\",\n    \"description\": \"Compute CKA (linear kernel) between English and each target language at every probed layer for both models. Correlate CKA with transfer AUROC to provide mechanistic explanation for the Pareto frontier. Full-scale validation of pilot finding (revised hypothesis: threshold model — transfer collapses only below critical CKA threshold ~0.35). Report CKA × layer × language heatmaps, CKA vs transfer degradation correlation per language, and threshold analysis.\\n\",\n    \"results\": {\n      \"cka_en_vs_target_mean_all\": 0.72,\n      \"cka_decline_with_depth\": true,\n      \"cka_shallow_mean\": 0.89,\n      \"cka_deep_mean\": 0.54,\n      \"cka_vs_transfer_auroc_pearson_r_overall\": 0.32,\n      \"cka_vs_transfer_auroc_pearson_r_range_per_lang\": [\n        -0.08,\n        0.71\n      ],\n      \"cka_vs_transfer_pearson_significant_langs\": 7,\n      \"cka_vs_transfer_pearson_nonsig_langs\": 12,\n      \"cka_threshold_0p35_replicates\": \"partial\",\n      \"n_lang_layer_pairs_below_threshold\": 18,\n      \"transfer_collapse_below_threshold_pct\": 0.61,\n      \"transfer_collapse_above_threshold_pct\": 0.22,\n      \"cka_architecture_consistency\": \"weak\",\n      \"cka_pearson_qwen3\": 0.38,\n      \"cka_pearson_llama4\": 0.24,\n      \"cka_by_tier\": {\n        \"high_resource_mean\": 0.76,\n        \"mid_resource_mean\": 0.71,\n        \"low_resource_mean\": 0.64\n      },\n      \"cka_per_lang_deep_layer\": {\n        \"zh\": 0.68,\n        \"fr\": 0.71,\n        \"de\": 0.69,\n        \"es\": 0.67,\n        \"ja\": 0.62,\n        \"ko\": 0.6,\n        \"ru\": 0.58,\n        \"ar\": 0.53,\n        \"hi\": 0.51,\n        \"vi\": 0.48,\n        \"id\": 0.52,\n        \"th\": 0.45,\n        \"pl\": 0.55,\n        \"uk\": 0.54,\n        \"bn\": 0.41,\n        \"te\": 0.39,\n        \"ta\": 0.37,\n        \"sw\": 0.33,\n        \"yo\": 0.28\n      },\n      \"pilot_revision_validated\": \"partially — threshold exists but is noisy\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 16: CKA vs Transfer AUROC Correlation by Architecture\",\n        \"columns\": [\n          \"model\",\n          \"pearson_r\",\n          \"p_value\",\n          \"n_sig_langs\",\n          \"n_total_langs\",\n          \"spearman_rho\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-235B\",\n            0.38,\n            0.002,\n            5,\n            19,\n            0.35\n          ],\n          [\n            \"Llama4-Scout\",\n            0.24,\n            0.041,\n            2,\n            19,\n            0.21\n          ],\n          [\n            \"Combined\",\n            0.32,\n            0.001,\n            7,\n            38,\n            0.29\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 17: CKA Threshold Analysis (threshold = 0.35)\",\n        \"columns\": [\n          \"condition\",\n          \"n_pairs\",\n          \"mean_transfer_auroc\",\n          \"pct_below_0p55\",\n          \"pct_above_0p65\"\n        ],\n        \"rows\": [\n          [\n            \"CKA < 0.35\",\n            18,\n            0.538,\n            0.61,\n            0.11\n          ],\n          [\n            \"CKA ≥ 0.35\",\n            438,\n            0.612,\n            0.22,\n            0.39\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 18: CKA at Deep Layers (75% depth) by Language\",\n        \"columns\": [\n          \"language\",\n          \"resource_tier\",\n          \"cka_qwen3\",\n          \"cka_llama4\",\n          \"transfer_auroc_qwen3\",\n          \"transfer_auroc_llama4\"\n        ],\n        \"rows\": [\n          [\n            \"zh\",\n            \"high\",\n            0.71,\n            0.65,\n            0.668,\n            0.658\n          ],\n          [\n            \"fr\",\n            \"high\",\n            0.74,\n            0.68,\n            0.672,\n            0.662\n          ],\n          [\n            \"de\",\n            \"high\",\n            0.72,\n            0.66,\n            0.671,\n            0.655\n          ],\n          [\n            \"ja\",\n            \"high\",\n            0.65,\n            0.59,\n            0.658,\n            0.634\n          ],\n          [\n            \"ru\",\n            \"high\",\n            0.61,\n            0.55,\n            0.652,\n            0.622\n          ],\n          [\n            \"ar\",\n            \"mid\",\n            0.56,\n            0.5,\n            0.625,\n            0.589\n          ],\n          [\n            \"hi\",\n            \"mid\",\n            0.54,\n            0.48,\n            0.618,\n            0.586\n          ],\n          [\n            \"th\",\n            \"mid\",\n            0.48,\n            0.42,\n            0.594,\n            0.558\n          ],\n          [\n            \"sw\",\n            \"low\",\n            0.36,\n            0.3,\n            0.537,\n            0.518\n          ],\n          [\n            \"yo\",\n            \"low\",\n            0.31,\n            0.25,\n            0.512,\n            0.492\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CKA provides suggestive but not convincing mechanistic explanation. The decline with depth is clear, and the threshold model partially replicates (61% transfer collapse below CKA 0.35). But the correlation is too weak (r = 0.32) and architecture-dependent (0.38 vs 0.24) to serve as a reliable predictor. The key insight survives at a qualitative level: cross-lingual misalignment is geometric, which explains why MMD-based CaCLR fails (it matches distributions but can't correct rotation) while linear projection succeeds (it learns the rotation). But the quantitative story is messy. For the paper: report CKA as supporting evidence for the geometric-misalignment interpretation, not as a standalone finding. Two paragraphs in the analysis section.\\n\\n\\nCKA declines with depth on both models (shallow 0.89 → deep 0.54), confirming that deeper layers are less cross-lingually aligned. However, the correlation between CKA and transfer AUROC is weak overall (Pearson r = 0.32, explaining ~10% of variance). This happens because the pilot's revised hypothesis — that transfer collapses only below a critical CKA threshold (~0.35) rather than declining linearly — partially replicates but with too much noise at full scale. Below the 0.35 threshold, 61% of language-layer pairs show transfer collapse (AUROC < 0.55), but 39% do not — meaning the threshold is suggestive, not deterministic. Above the threshold, 22% of pairs still show poor transfer, indicating CKA captures necessary but not sufficient conditions for transfer. Per-language correlations vary wildly: hi (r = 0.71, sig) and sw (r = 0.67, sig) show strong CKA-transfer coupling, but zh (r = 0.12, ns) and fr (r = 0.08, ns) show near-zero correlation because these high-resource languages transfer well regardless of CKA level. Architecture inconsistency is notable: Qwen3 r = 0.38, Llama4 r = 0.24 — the mechanistic explanation is model-dependent. For the paper, CKA provides a \\\"suggestive but not convincing\\\" mechanistic account: geometric misalignment (lower CKA) correlates with transfer failure, but the relationship is too noisy and architecture-dependent to serve as a reliable predictor or principled layer selection criterion.\\n\"\n  },\n  {\n    \"name\": \"Linear Projection Sensitivity Analysis\",\n    \"description\": \"Vary number of parallel pairs (10, 20, 50, 100, 200) for linear projection transfer. Determines minimum data requirement for this baseline. Both models × 5 representative layers × 19 target languages.\\n\",\n    \"results\": {\n      \"linproj_by_n_pairs\": {\n        \"10\": {\n          \"auroc_mean\": 0.608,\n          \"delta_vs_zs_pp\": -1.0,\n          \"pct_langs_improved\": 0.26\n        },\n        \"20\": {\n          \"auroc_mean\": 0.621,\n          \"delta_vs_zs_pp\": 0.3,\n          \"pct_langs_improved\": 0.42\n        },\n        \"50\": {\n          \"auroc_mean\": 0.636,\n          \"delta_vs_zs_pp\": 1.8,\n          \"pct_langs_improved\": 0.55\n        },\n        \"100\": {\n          \"auroc_mean\": 0.643,\n          \"delta_vs_zs_pp\": 2.5,\n          \"pct_langs_improved\": 0.63\n        },\n        \"200\": {\n          \"auroc_mean\": 0.647,\n          \"delta_vs_zs_pp\": 2.9,\n          \"pct_langs_improved\": 0.68\n        }\n      },\n      \"minimum_viable_pairs_high_resource\": 20,\n      \"minimum_viable_pairs_mid_resource\": 50,\n      \"minimum_viable_pairs_low_resource\": \">200 (insufficient quality)\",\n      \"saturation_point\": \"~100 pairs — diminishing returns beyond\",\n      \"linproj_fails_low_resource\": true,\n      \"low_resource_at_200_pairs\": {\n        \"bn\": {\n          \"auroc\": 0.561,\n          \"delta_vs_zs_pp\": 0.8\n        },\n        \"te\": {\n          \"auroc\": 0.576,\n          \"delta_vs_zs_pp\": 0.5\n        },\n        \"ta\": {\n          \"auroc\": 0.571,\n          \"delta_vs_zs_pp\": 0.3\n        },\n        \"sw\": {\n          \"auroc\": 0.543,\n          \"delta_vs_zs_pp\": 0.6\n        },\n        \"yo\": {\n          \"auroc\": 0.518,\n          \"delta_vs_zs_pp\": 0.6\n        }\n      },\n      \"high_resource_at_50_pairs\": {\n        \"zh\": {\n          \"auroc\": 0.681,\n          \"delta_vs_zs_pp\": 1.3\n        },\n        \"fr\": {\n          \"auroc\": 0.686,\n          \"delta_vs_zs_pp\": 1.4\n        },\n        \"de\": {\n          \"auroc\": 0.684,\n          \"delta_vs_zs_pp\": 1.3\n        }\n      },\n      \"variance_across_random_subsets_std_pp\": 1.8\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 19: Linear Projection AUROC by Number of Parallel Pairs (19-Lang Mean)\",\n        \"columns\": [\n          \"n_pairs\",\n          \"auroc_mean\",\n          \"auroc_std\",\n          \"delta_vs_zs_pp\",\n          \"pct_langs_improved\",\n          \"pct_langs_hurt\"\n        ],\n        \"rows\": [\n          [\n            10,\n            0.608,\n            0.052,\n            -1.0,\n            0.26,\n            0.53\n          ],\n          [\n            20,\n            0.621,\n            0.047,\n            0.3,\n            0.42,\n            0.32\n          ],\n          [\n            50,\n            0.636,\n            0.042,\n            1.8,\n            0.55,\n            0.21\n          ],\n          [\n            100,\n            0.643,\n            0.04,\n            2.5,\n            0.63,\n            0.16\n          ],\n          [\n            200,\n            0.647,\n            0.039,\n            2.9,\n            0.68,\n            0.11\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 20: Linear Projection at 50 Pairs by Resource Tier\",\n        \"columns\": [\n          \"resource_tier\",\n          \"n_langs\",\n          \"auroc_mean\",\n          \"delta_vs_zs_pp\",\n          \"pct_improved\"\n        ],\n        \"rows\": [\n          [\n            \"high\",\n            7,\n            0.677,\n            3.1,\n            0.86\n          ],\n          [\n            \"mid\",\n            7,\n            0.631,\n            1.6,\n            0.57\n          ],\n          [\n            \"low\",\n            5,\n            0.553,\n            0.1,\n            0.2\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Linear projection is the strongest zero-label method but has a clear resource-tier limitation. High-resource languages benefit reliably from ~20 pairs; mid-resource need ~50; low-resource fail even at 200 because parallel quality and activation structure are insufficient. For the paper, this strengthens the practical recommendation: \\\"few-shot (25–100 labels) is the viable path for mid/low-resource; linear projection works only for high-resource languages with quality parallel data.\\\" The minimum-pairs analysis is a practical contribution that helps practitioners decide between linproj and few-shot.\\n\\n\\nLinear projection's effectiveness depends heavily on the number and quality of parallel pairs. At 10 pairs, the affine transformation is underestimated (high-dimensional activation space needs more samples to estimate rotation matrix reliably), actually hurting transfer (−1.0pp) by introducing noise. At 20 pairs, high-resource languages start benefiting because their parallel pairs have high translation quality and the activation subspaces are already partially aligned. At 50 pairs, the projection stabilizes for high and mid-resource languages (the \\\"default\\\" setting in the main experiments). But low-resource languages fail even at 200 pairs for two reasons: (1) GlobalMMLU parallel translations for sw/yo/bn are lower quality (more literal, less natural), so the parallel activations don't capture the true language-specific encoding; (2) the activation subspace for these languages is itself noisier (less structured due to limited pretraining), making the rotation hard to estimate even with many pairs. The variance across random subsets (std 1.8pp) is high, indicating the projection is sensitive to which specific pairs are used — this is a practical reliability concern. Saturation at ~100 pairs means the projection captures most learnable alignment, and remaining transfer gap is due to fundamental representational differences, not data limitation.\\n\"\n  },\n  {\n    \"name\": \"Probing Control Tasks (Hewitt & Liang 2019)\",\n    \"description\": \"Train probes on randomly permuted labels at each layer. Compare selectivity (probe AUROC − control AUROC) across layers and languages. Validates that high AUROC reflects genuine correctness direction, not memorized dataset artifacts or probe capacity.\\n\",\n    \"results\": {\n      \"control_auroc_mean_en_qwen3\": 0.548,\n      \"control_auroc_mean_en_llama4\": 0.544,\n      \"control_auroc_range_en\": [\n        0.512,\n        0.571\n      ],\n      \"selectivity_en_best_layer_qwen3\": 0.228,\n      \"selectivity_en_best_layer_llama4\": 0.205,\n      \"selectivity_en_mean_all_layers\": 0.168,\n      \"selectivity_min_across_all\": 0.048,\n      \"selectivity_min_language\": \"yo\",\n      \"selectivity_min_layer\": \"shallow (L4/L8)\",\n      \"selectivity_by_resource_tier\": {\n        \"high_resource_mean\": 0.172,\n        \"mid_resource_mean\": 0.138,\n        \"low_resource_mean\": 0.084\n      },\n      \"low_resource_selectivity_below_8pp\": {\n        \"sw_L4\": 0.052,\n        \"yo_L4\": 0.048,\n        \"yo_L8\": 0.056,\n        \"bn_L4\": 0.061,\n        \"ta_L4\": 0.058,\n        \"sw_L8\": 0.063\n      },\n      \"pct_lang_layer_pairs_selectivity_below_8pp\": 0.08,\n      \"pct_low_resource_pairs_selectivity_below_8pp\": 0.28,\n      \"selectivity_depth_gradient\": \"positive — deeper layers have higher selectivity\",\n      \"selectivity_vs_auroc_correlation\": 0.74\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 21: Control Task Selectivity by Resource Tier\",\n        \"columns\": [\n          \"resource_tier\",\n          \"n_langs\",\n          \"probe_auroc_mean\",\n          \"control_auroc_mean\",\n          \"selectivity_mean_pp\",\n          \"selectivity_min_pp\"\n        ],\n        \"rows\": [\n          [\n            \"high\",\n            7,\n            0.66,\n            0.548,\n            17.2,\n            10.4\n          ],\n          [\n            \"mid\",\n            7,\n            0.614,\n            0.546,\n            13.8,\n            8.2\n          ],\n          [\n            \"low\",\n            5,\n            0.548,\n            0.544,\n            8.4,\n            4.8\n          ],\n          [\n            \"all\",\n            19,\n            0.618,\n            0.546,\n            13.8,\n            4.8\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 22: Selectivity at Best English Layer (L72 Qwen3 / L36 Llama4)\",\n        \"columns\": [\n          \"language\",\n          \"probe_auroc\",\n          \"control_auroc\",\n          \"selectivity_pp\",\n          \"flag\"\n        ],\n        \"rows\": [\n          [\n            \"en\",\n            0.776,\n            0.548,\n            22.8,\n            \"\"\n          ],\n          [\n            \"zh\",\n            0.641,\n            0.549,\n            9.2,\n            \"\"\n          ],\n          [\n            \"fr\",\n            0.645,\n            0.548,\n            9.7,\n            \"\"\n          ],\n          [\n            \"de\",\n            0.644,\n            0.549,\n            9.5,\n            \"\"\n          ],\n          [\n            \"ar\",\n            0.598,\n            0.547,\n            5.1,\n            \"⚠ low\"\n          ],\n          [\n            \"hi\",\n            0.591,\n            0.546,\n            4.5,\n            \"⚠ low\"\n          ],\n          [\n            \"sw\",\n            0.508,\n            0.552,\n            -4.4,\n            \"✗ below control\"\n          ],\n          [\n            \"yo\",\n            0.487,\n            0.551,\n            -6.4,\n            \"✗ below control\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 23: Selectivity by Depth Band (19-Language Mean)\",\n        \"columns\": [\n          \"depth_band\",\n          \"probe_auroc_mean\",\n          \"control_auroc_mean\",\n          \"selectivity_pp\"\n        ],\n        \"rows\": [\n          [\n            \"0–25%\",\n            0.582,\n            0.549,\n            3.3\n          ],\n          [\n            \"25–50%\",\n            0.618,\n            0.547,\n            7.1\n          ],\n          [\n            \"50–75%\",\n            0.641,\n            0.546,\n            9.5\n          ],\n          [\n            \"75–100%\",\n            0.634,\n            0.548,\n            8.6\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Control tasks are the most damaging experiment for the worst tier. They reveal that 28% of low-resource language-layer pairs have selectivity < 8pp — some \\\"transfer success\\\" in these settings is probe capacity artifact. At the English-optimal layer, Swahili and Yoruba actually score BELOW the control, meaning the probe is memorizing random structure rather than detecting correctness. This doesn't invalidate the main results (high-resource selectivity is robust at 17pp+), but it qualifies them: the resource-tier taxonomy should be presented with selectivity as a reliability measure. For the paper: \\\"Control tasks confirm that probe AUROC for high/mid-resource languages reflects genuine correctness signals (selectivity > 10pp), but low-resource results at shallow/moderate layers should be interpreted cautiously (selectivity 3–8pp). The practical implication reinforces the few-shot recommendation: for low-resource languages, even the probe AUROC metric itself is unreliable without labeled data to establish a non-trivial baseline.\\\"\\n\\n\\nControl tasks reveal that probe capacity explains a non-trivial portion of AUROC, especially for low-resource languages at shallow layers. The control AUROC (probes on random labels) averages 0.548 for English — above the theoretical 0.50 baseline because logistic regression on high-dimensional activation spaces (d > 4096) can memorize patterns in random labels when sample sizes are small (GlobalMMLU has ~300–600 items per language). This means an AUROC of 0.60 at a shallow layer for a low-resource language has selectivity of only ~5pp — dangerously close to the control. Specifically, 28% of low-resource language-layer pairs have selectivity below 8pp, meaning a non-negligible fraction of \\\"successful\\\" transfer AUROC in low-resource settings is probe capacity artifact rather than genuine correctness signal. The selectivity minimum of 4.8pp (Yoruba at L4) means some reported AUROCs are nearly indistinguishable from memorization. Deeper layers show higher selectivity because the correctness signal strengthens with depth while control AUROC stays constant (~0.55). The resource-tier gradient in selectivity (high: 17.2pp, mid: 13.8pp, low: 8.4pp) mirrors the transfer gradient — low-resource languages have both lower AUROC and lower selectivity, compounding the interpretive challenge. For the paper, this means low-resource AUROC numbers should be presented with selectivity-adjusted confidence intervals. Any language-layer pair with selectivity < 8pp should be flagged as unreliable.\\n\"\n  },\n  {\n    \"name\": \"Gemma 4 31B Dense — Third Architecture (Camera-Ready)\",\n    \"description\": \"Full Pareto frontier on Gemma 4 31B Dense (60 layers, dense, FP16). 20+ languages. Dense vs MoE architectural contrast.\\n\",\n    \"results\": {\n      \"en_auroc_best_layer\": 0.761,\n      \"en_best_layer_idx\": 45,\n      \"en_auroc_range\": [\n        0.601,\n        0.761\n      ],\n      \"zs_transfer_auroc_mean_19lang\": 0.605,\n      \"zs_transfer_drop_mean_pp\": 17.1,\n      \"zs_langs_above_0p65\": 6,\n      \"pareto_global_spearman_rho\": -0.44,\n      \"pareto_per_lang_rho_median\": -0.31,\n      \"pareto_rho_sign_consistency\": 0.68,\n      \"pareto_frontier_n_nondominated\": 6,\n      \"pareto_frontier_agreement_with_qwen3_tau\": 0.42,\n      \"pareto_frontier_agreement_with_llama4_tau\": 0.29,\n      \"caclr_auroc_mean\": 0.609,\n      \"caclr_vs_linproj_pp\": -0.9,\n      \"dense_vs_moe_finding\": \"Dense architecture shows cleaner Pareto frontier (ρ = −0.44 vs −0.38/−0.18 for MoE) with higher sign consistency (0.68 vs 0.63/0.53). MoE routing is a source of non-monotonic noise, but the frontier is still moderate even for dense models.\\n\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 24: Three-Architecture Comparison Summary\",\n        \"columns\": [\n          \"model\",\n          \"type\",\n          \"layers\",\n          \"en_auroc\",\n          \"zs_auroc_mean\",\n          \"pareto_rho\",\n          \"sign_consistency\",\n          \"pareto_agreement_mean_tau\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-235B\",\n            \"MoE\",\n            94,\n            0.776,\n            0.618,\n            -0.38,\n            0.63,\n            0.38\n          ],\n          [\n            \"Llama4-Scout\",\n            \"MoE\",\n            48,\n            0.749,\n            0.588,\n            -0.18,\n            0.53,\n            0.31\n          ],\n          [\n            \"Gemma4-31B\",\n            \"Dense\",\n            60,\n            0.761,\n            0.605,\n            -0.44,\n            0.68,\n            0.36\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Gemma4 confirms the diagnostic paper's thesis from a new angle: MoE routing adds non-monotonic noise to the Pareto frontier, but even the dense architecture's frontier is moderate (ρ = −0.44). The depth-transfer tradeoff is real but explains limited variance regardless of architecture. Cross-architecture agreement remains low, confirming architecture-dependence.\\n\\n\\nGemma 4 31B Dense shows a cleaner but still moderate Pareto frontier because dense architectures have more homogeneous layer transitions (no expert routing to create non-monotonic jumps). The Spearman ρ of −0.44 is the highest among three architectures but still means depth explains only ~19% of transfer variance. English AUROC 0.761 is between Qwen3 (0.776) and Llama4 (0.749), consistent with 31B active parameters being intermediate. Transfer is intermediate too (0.605). Cross-architecture agreement remains low (τ = 0.42 with Qwen3, 0.29 with Llama4), confirming architecture-dependence even between dense and MoE models. CaCLR still fails on this architecture, ruling out the hypothesis that MoE routing specifically caused CaCLR's failure.\\n\"\n  },\n  {\n    \"name\": \"Extended Language Coverage (50+ Languages, Camera-Ready)\",\n    \"description\": \"Expand from 20 to 50+ languages using full GlobalMMLU/Belebele language sets.\\n\",\n    \"results\": {\n      \"total_languages\": 52,\n      \"zs_transfer_auroc_mean_51lang\": 0.581,\n      \"zs_transfer_auroc_median_51lang\": 0.574,\n      \"zs_pass_rate_51lang\": 0.24,\n      \"low_resource_auroc_mean_new_langs\": 0.541,\n      \"worst_language_auroc\": 0.488,\n      \"worst_language\": \"Amharic (am)\",\n      \"resource_tier_gradient_steeper\": true,\n      \"new_language_families_added\": 5,\n      \"transfer_by_tier_expanded\": {\n        \"high\": {\n          \"n\": 10,\n          \"auroc_mean\": 0.651,\n          \"pass_rate\": 0.7\n        },\n        \"mid\": {\n          \"n\": 18,\n          \"auroc_mean\": 0.598,\n          \"pass_rate\": 0.28\n        },\n        \"low\": {\n          \"n\": 14,\n          \"auroc_mean\": 0.553,\n          \"pass_rate\": 0.07\n        },\n        \"very_low\": {\n          \"n\": 10,\n          \"auroc_mean\": 0.518,\n          \"pass_rate\": 0.0\n        }\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 25: Transfer Success by Resource Tier (52-Language Set, Qwen3)\",\n        \"columns\": [\n          \"resource_tier\",\n          \"n_langs\",\n          \"zs_auroc_mean\",\n          \"zs_auroc_std\",\n          \"pass_rate\"\n        ],\n        \"rows\": [\n          [\n            \"high\",\n            10,\n            0.651,\n            0.017,\n            0.7\n          ],\n          [\n            \"mid\",\n            18,\n            0.598,\n            0.023,\n            0.28\n          ],\n          [\n            \"low\",\n            14,\n            0.553,\n            0.028,\n            0.07\n          ],\n          [\n            \"very_low\",\n            10,\n            0.518,\n            0.021,\n            0.0\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Extended coverage is the strongest evidence for the diagnostic conclusion. With 52 languages, the majority fail to transfer. Very-low-resource languages (10 langs, AUROC 0.518) are indistinguishable from chance when accounting for control task selectivity. The paper's conclusion: \\\"probe-based calibration does not generalize beyond a small set of high-resource languages without fundamental methodological advances.\\\"\\n\\nExpanding to 52 languages worsens the aggregate picture because additional languages are predominantly low and very-low-resource. Many (Amharic, Lao, Mongolian, Georgian) have minimal representation in pretraining data, so their activations share even less structure with English. Pass rate drops from ~37% (7/19) to ~24% (12/51). Some languages approach chance (AUROC ~0.49). The resource-tier gradient steepens: very-low-resource languages (n=10) average 0.518 with 0% pass rate. This strengthens the diagnostic message: probe-based calibration has a severe language barrier.\\n\"\n  }\n]",
      "numLines": 2536,
      "startLine": 1,
      "totalLines": 2536
    }
  },
  "sourceToolAssistantUUID": "aac4c323-aec4-4c4a-ba9e-5b14a96da12e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-20T20:53:40.603Z_

<details><summary>↩ Tool result · `toolu_01FhjBYr5JHJh3XfVfojGWKi`</summary>

```text
1	# Paper Framing — xling_calib_direction
2	
3	## Target Venue
4	- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)
5	- Core submission: 2 models × 20 languages × all contributions
6	- Camera-ready extension: Gemma 4 31B Dense + 30+ languages
7	
8	## Core Insight
9	The model's internal correctness direction — linearly accessible but orthogonal to verbalized confidence — transfers cross-lingually through intermediate layers, but with a depth-transferability Pareto tradeoff: deeper layers yield better English calibration while shallower layers transfer better. This tradeoff is architecture-dependent and can be shifted by CaCLR, a probe training objective that jointly optimizes correctness prediction and cross-lingual calibration invariance without requiring target-language correctness labels.
10	
11	## Core Claims (4, causal chain)
12	
13	### Claim 1 — Pareto Frontier (Discovery)
14	Cross-lingual correctness probes reveal a depth-transferability Pareto frontier: deeper layers produce better-calibrated English probes but degrade in cross-lingual zero-shot transfer. The optimal transfer depth is architecture-dependent.
15	- MVP evidence: L27 AUROC=0.754 (EN best) but transfer drops 2-4pp vs L24 on Qwen2.5-7B.
16	- Full evidence: 2 architectures × 20 languages × all layers × 5 transfer conditions.
17	
18	### Claim 2 — Decomposition (Analysis)
19	Cross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.
20	- Evidence: IRT difficulty probes → project out → retrain → compare transfer.
21	
22	### Claim 3 — CaCLR (Method / Diagnostic)
23	CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on parallel activations from GlobalMMLU translated items, train split only) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels.
24	- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.
25	- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that distributional matching fails for correctness probe transfer. CKA analysis provides the theoretical explanation: cross-lingual misalignment at deeper layers is *geometric* (correctness direction rotates/scales across language subspaces), not merely *distributional* (mean/covariance shift). MMD-based alignment cannot correct geometric transformations, which is why linear projection (which learns the rotation) succeeds where distributional matching fails. This closes the distributional-matching path with both empirical evidence and mechanistic explanation.
26	- Parallel activations source: GlobalMMLU train-split translations (not test items). This requires parallel *inputs* but zero target-language *labels* — a weaker requirement than per-language annotation.
27	- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.
28	- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.
29	
30	### Claim 4 — Cross-Lingual Orthogonality (Mechanistic)
31	The correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture, establishing output-based calibration as structurally limited regardless of language.
32	- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.
33	
34	## Story Spine
35	- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).
36	- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.
37	- **Our framing**: First systematic test of probe-based calibration in multilingual settings. We discover the Pareto frontier, decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching approach, and provide mechanistic analysis (CKA) explaining why transfer succeeds or fails at each depth. This is both a field-level viability test and (depending on CaCLR results) a practical method contribution or a principled negative result.
38	- **Headline template (method success)**: "On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels."
39	- **Headline template (negative result)**: "Cross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs matches supervised baselines."
40	- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.
41	
42	## Field-Level Significance
43	This paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.
44	
45	## Anticipated Reviewer Concerns & Responses
46	1. **"Xiao et al. already did this"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.
47	2. **"Temperature scaling baseline"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.
48	3. **"Mean-shift too weak / why does it fail?"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.
49	4. **"Difficulty confound"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.
50	5. **"INT8 artifacts"** → Validation ablation comparing INT8 vs FP16 at representative layers.
51	6. **"Only MCQA"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.
52	7. **"Predictable from domain adaptation theory"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.
53	8. **"No statistical tests"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.
54	9. **"Probing methodology concerns"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.
55	10. **"No mechanistic explanation"** → CKA analysis across layers × languages explains WHY transfer fails at deeper layers (cross-lingual representation similarity decreases with depth) and correlates with transfer success.
56	11. **"Why not conformal prediction?"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.
57	12. **"CaCLR parallel activations = test leakage?"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.
58	
59	## Additional Related Work Coverage (Dream-identified gaps)
60	- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. We derive predictions and test them.
61	- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature; CaCLR's failure despite distributional matching is the novel finding.
62	- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — we use CKA to provide mechanistic explanation for the Pareto frontier.
63	- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity.
64	- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.
65	
66	## Differentiation from Closest Prior Work
67	| Paper | Their Focus | Our Difference |
68	|-------|-------------|----------------|
69	| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |
70	| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |
71	| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |
72	| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |
73	| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |
74	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce91d5c1-6a9f-42a8-a7d5-2738501e9def",
  "isSidechain": false,
  "promptId": "ce9c66bf-f5bc-46b5-95a4-aabc6b39fe73",
  "type": "user",
  "uuid": "b58dcf32-2c61-4212-9dd1-b9f45a6ddd6d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/paper_framing.md",
      "content": "# Paper Framing — xling_calib_direction\n\n## Target Venue\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\n- Core submission: 2 models × 20 languages × all contributions\n- Camera-ready extension: Gemma 4 31B Dense + 30+ languages\n\n## Core Insight\nThe model's internal correctness direction — linearly accessible but orthogonal to verbalized confidence — transfers cross-lingually through intermediate layers, but with a depth-transferability Pareto tradeoff: deeper layers yield better English calibration while shallower layers transfer better. This tradeoff is architecture-dependent and can be shifted by CaCLR, a probe training objective that jointly optimizes correctness prediction and cross-lingual calibration invariance without requiring target-language correctness labels.\n\n## Core Claims (4, causal chain)\n\n### Claim 1 — Pareto Frontier (Discovery)\nCross-lingual correctness probes reveal a depth-transferability Pareto frontier: deeper layers produce better-calibrated English probes but degrade in cross-lingual zero-shot transfer. The optimal transfer depth is architecture-dependent.\n- MVP evidence: L27 AUROC=0.754 (EN best) but transfer drops 2-4pp vs L24 on Qwen2.5-7B.\n- Full evidence: 2 architectures × 20 languages × all layers × 5 transfer conditions.\n\n### Claim 2 — Decomposition (Analysis)\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\n\n### Claim 3 — CaCLR (Method / Diagnostic)\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on parallel activations from GlobalMMLU translated items, train split only) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels.\n- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.\n- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that distributional matching fails for correctness probe transfer. CKA analysis provides the theoretical explanation: cross-lingual misalignment at deeper layers is *geometric* (correctness direction rotates/scales across language subspaces), not merely *distributional* (mean/covariance shift). MMD-based alignment cannot correct geometric transformations, which is why linear projection (which learns the rotation) succeeds where distributional matching fails. This closes the distributional-matching path with both empirical evidence and mechanistic explanation.\n- Parallel activations source: GlobalMMLU train-split translations (not test items). This requires parallel *inputs* but zero target-language *labels* — a weaker requirement than per-language annotation.\n- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.\n\n### Claim 4 — Cross-Lingual Orthogonality (Mechanistic)\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture, establishing output-based calibration as structurally limited regardless of language.\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\n\n## Story Spine\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\n- **Our framing**: First systematic test of probe-based calibration in multilingual settings. We discover the Pareto frontier, decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching approach, and provide mechanistic analysis (CKA) explaining why transfer succeeds or fails at each depth. This is both a field-level viability test and (depending on CaCLR results) a practical method contribution or a principled negative result.\n- **Headline template (method success)**: \"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\"\n- **Headline template (negative result)**: \"Cross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs matches supervised baselines.\"\n- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.\n\n## Field-Level Significance\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\n\n## Anticipated Reviewer Concerns & Responses\n1. **\"Xiao et al. already did this\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.\n2. **\"Temperature scaling baseline\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\n3. **\"Mean-shift too weak / why does it fail?\"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.\n4. **\"Difficulty confound\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\n5. **\"INT8 artifacts\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\n6. **\"Only MCQA\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\n7. **\"Predictable from domain adaptation theory\"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.\n8. **\"No statistical tests\"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.\n9. **\"Probing methodology concerns\"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.\n10. **\"No mechanistic explanation\"** → CKA analysis across layers × languages explains WHY transfer fails at deeper layers (cross-lingual representation similarity decreases with depth) and correlates with transfer success.\n11. **\"Why not conformal prediction?\"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.\n12. **\"CaCLR parallel activations = test leakage?\"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.\n\n## Additional Related Work Coverage (Dream-identified gaps)\n- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. We derive predictions and test them.\n- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature; CaCLR's failure despite distributional matching is the novel finding.\n- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — we use CKA to provide mechanistic explanation for the Pareto frontier.\n- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity.\n- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.\n\n## Differentiation from Closest Prior Work\n| Paper | Their Focus | Our Difference |\n|-------|-------------|----------------|\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\n",
      "numLines": 74,
      "startLine": 1,
      "totalLines": 74
    }
  },
  "sourceToolAssistantUUID": "ce91d5c1-6a9f-42a8-a7d5-2738501e9def",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T201854 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direc…",
  "leafUuid": "ab3728bf-a1ca-46b4-80e6-41f2c1c980e6",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated ML research paper with experiments",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135"
}
```

---

### Assistant

_source line 14 · 2026-05-20T20:53:59.574Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data. Let me also read the research and writing skill files to get patterns for the paper.

Actually, I have enough context. Let me now write the full LaTeX paper based on the experiment data and paper framing. This is a "worst" tier dream paper — framed as a "sobering empirical reality check" for probe-based calibration.

Key elements from the data:
1. Pareto frontier exists on Qwen3 but is weak (ρ=-0.38), and nearly vanishes on Llama4 (ρ=-0.18). Gemma4 Dense shows ρ=-0.44. Architecture-dependent.


2. Mean-shift is mathematically dead (ΔAUROC ≡ 0) — rank-invariance theorem
3. Resource-tier taxonomy: high transfers (~0.663), mid marginal (~0.615), low fails (~0.548)
4. CaCLR fails — consistency loss inert, β sweep flat
5. Decomposition inconclusive — difficulty removal neither helps nor hurts systematically
6. Orthogonality persists cross-lingually but with outliers (yo at 0.172)
7. CKA suggestive but weak (r<0.45)
8. Control tasks reveal capacity artifacts in low-resource settings (selectivity <8pp)
9. Few-shot (25-100) is the only viable path
10. Extended to 52 languages — pass rate drops to 24%

Now I'm planning the paper structure: abstract, introduction, related work, then methods covering the probe setup, transfer approaches, CaCLR, decomposition analysis, and orthogonality testing. The experiments section will walk through English performance, cross-lingual transfer with the resource taxonomy, the rank-invariance proof for mean-shift, comparisons across transfer methods, the CaCLR failure, difficulty decomposition results, cross-lingual orthogonality patterns, and additional analyses.

I need to add sections on knowledge-aware analysis, control tasks, extended language coverage across 52 languages, and cross-architecture comparisons before wrapping up with discussion and conclusion. Every number has to be grounded in the JSON data, so I'll start writing and verify against the actual results.

Setting up the output directory...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b58dcf32-2c61-4212-9dd1-b9f45a6ddd6d",
  "isSidechain": false,
  "requestId": "req_011CbEV6GpCedKgRPE6mS2Fj",
  "type": "assistant",
  "uuid": "6fbe4d0a-2b2b-4e67-aecf-771af4147b45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ey7BKMhuvF1JELQiydwWm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34277,
      "cache_read_input_tokens": 23518,
      "output_tokens": 764,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34277,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 764,
          "cache_read_input_tokens": 23518,
          "cache_creation_input_tokens": 34277,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34277
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

_source line 15 · 2026-05-20T20:53:59.576Z_

Now I'll write the full LaTeX paper. Let me first check the output directory exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6fbe4d0a-2b2b-4e67-aecf-771af4147b45",
  "isSidechain": false,
  "requestId": "req_011CbEV6GpCedKgRPE6mS2Fj",
  "type": "assistant",
  "uuid": "1ed5b22a-0fee-47d8-b836-328069d8065a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ey7BKMhuvF1JELQiydwWm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34277,
      "cache_read_input_tokens": 23518,
      "output_tokens": 764,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34277,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 764,
          "cache_read_input_tokens": 23518,
          "cache_creation_input_tokens": 34277,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34277
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

_source line 16 · 2026-05-20T20:54:00.539Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01BBjtzpfUetfnJKVzM2piky`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/",
  "description": "List target directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ed5b22a-0fee-47d8-b836-328069d8065a",
  "isSidechain": false,
  "requestId": "req_011CbEV6GpCedKgRPE6mS2Fj",
  "type": "assistant",
  "uuid": "df61681b-b0b0-4f98-8262-9ee6038da58c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ey7BKMhuvF1JELQiydwWm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34277,
      "cache_read_input_tokens": 23518,
      "output_tokens": 764,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34277,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 764,
          "cache_read_input_tokens": 23518,
          "cache_creation_input_tokens": 34277,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34277
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

_source line 17 · 2026-05-20T20:54:00.699Z_

<details><summary>↩ Tool result · `toolu_01BBjtzpfUetfnJKVzM2piky`</summary>

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
  "parentUuid": "df61681b-b0b0-4f98-8262-9ee6038da58c",
  "isSidechain": false,
  "promptId": "ce9c66bf-f5bc-46b5-95a4-aabc6b39fe73",
  "type": "user",
  "uuid": "2a84e288-6832-45a0-be28-e267061ad84a",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "df61681b-b0b0-4f98-8262-9ee6038da58c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T20:57:31.072Z_

<details open><summary>🔧 Tool call — Write · `toolu_012uZE1gLP9f3p9QARLfAVnR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{microtype}\n\\usepackage{url}\n\n\\newcommand{\\auroc}{\\textsc{auroc}}\n\\newcommand{\\ece}{\\textsc{ece}}\n\n\\title{Does Probe-Based Calibration Work Beyond English?\\\\A Systematic Investigation Across 3 Architectures and 52 Languages}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nProbe-based calibration---training linear classifiers on internal representations to predict answer correctness---has emerged as a promising alternative to output-based calibration in LLMs, but existing work is English-only. We present the first systematic cross-lingual evaluation of correctness probe transfer across 3 architectures (Qwen3-235B, Llama~4 Scout, Gemma~4 31B), up to 52 languages, and 5 transfer conditions. Our findings are sobering. First, we prove that mean-shift adaptation produces exactly zero \\auroc{} change under standard probing pipelines (rank-invariance theorem), distinguishing our setup from prior work. Second, we establish a resource-tier taxonomy of probe transferability: high-resource languages transfer with 7--8pp \\auroc{} drop, mid-resource at 10--12pp, and low-resource at 13--20pp, with control tasks revealing that 28\\% of low-resource results are capacity artifacts (selectivity $<$8pp). Third, the natural distributional-matching approach (CaCLR) fails---its consistency loss is inert across three orders of magnitude of hyperparameter sweep ($p = 0.71$ vs.\\ zero-shot, Cohen's $d = 0.04$). The depth--transferability Pareto frontier is architecture-dependent ($\\rho = -0.44$ dense, $-0.38$ MoE-large, $-0.18$ MoE-small; cross-architecture $\\tau = 0.33$), precluding universal layer selection. Few-shot adaptation with 25--100 target-language labels is the only viable path, closing the zero-label dream for low-resource languages.\n\\end{abstract}\n\n%% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n\nNon-English languages suffer substantially worse calibration in multilingual LLMs, with expected calibration error (\\ece{}) up to 5$\\times$ higher than English \\cite{kadeethum2024calibration}. Output-based calibration methods face a structural ceiling: the correctness direction in internal representations is approximately orthogonal to verbalized confidence \\cite{miao2026orthogonality}, meaning no amount of prompt engineering or temperature scaling can fully close the gap.\n\nA promising alternative is \\emph{probe-based calibration}, which trains lightweight classifiers on internal activations to predict whether the model's answer is correct \\cite{miao2024coral,burns2023discovering}. This approach has shown strong results in English, with recent work demonstrating cross-task transfer \\cite{miao2024coral}, confidence manifold structure \\cite{luo2024confidence}, and the potential for representation-level steering \\cite{miao2026orthogonality}. However, all of this work is English-only.\n\nThe natural question---\\emph{do English correctness probes transfer to other languages?}---has not been systematically investigated. Xiao et al.\\ \\shortcite{xiao2025knowledge} transferred \\emph{knowledge-boundary} probes (input-level answerability) across 8 languages, but knowledge boundaries are fundamentally different from correctness signals: the former encodes whether the model has seen relevant training data, while the latter depends on the model's output for a specific question. Their partial success does not predict ours.\n\nWe present a systematic investigation across 3 architectures (Qwen3-235B-A22B, Llama~4 Scout, Gemma~4 31B Dense), up to 52 languages spanning 15 language families, and 5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot, CaCLR). Our study yields three surviving contributions:\n\n\\paragraph{(1) Mean-shift rank-invariance.} We prove that under StandardScaler normalization and logistic regression---the standard probing pipeline---mean-shift adaptation produces \\emph{exactly} $\\Delta\\auroc{} = 0$ because mean subtraction adds a constant to all logits, preserving ranks. This distinguishes our setup from Xiao et al., where mean-shift succeeds under different metrics.\n\n\\paragraph{(2) Resource-tier taxonomy.} We provide the first quantification of cross-lingual probe transferability across 52 languages, establishing that high-resource languages transfer (7--8pp drop), mid-resource is marginal (10--12pp), and low-resource fails (13--20pp). Control tasks reveal capacity artifacts that further weaken low-resource results.\n\n\\paragraph{(3) Practical recommendation.} Zero-label transfer fails for the majority of the world's languages. Few-shot adaptation with 25--100 target-language labels is the only viable path, closing the zero-label dream for low-resource languages.\n\nAlong the way, we report that the depth--transferability Pareto frontier is architecture-dependent, that the natural distributional-matching method (CaCLR) produces negligible improvement, that difficulty--capability decomposition is inconclusive, and that CKA-based mechanistic analysis is suggestive but not convincing. The paper serves as a sobering empirical reality check for the probe-based calibration research line.\n\n%% ============================================================\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Probe-based calibration.}\nCORAL \\cite{miao2024coral} demonstrated cross-task correctness probe transfer in English; CCPS \\cite{liu2024confidence} and the Confidence Manifold \\cite{luo2024confidence} explored structural properties of correctness representations. Miao \\& Ungar \\shortcite{miao2026orthogonality} discovered that correctness and verbalized confidence directions are orthogonal in English, motivating representation-level intervention. All are English-only.\n\n\\paragraph{Cross-lingual probing.}\nXiao et al.\\ \\shortcite{xiao2025knowledge} transferred knowledge-boundary probes across 8 languages using mean-shift adaptation, reporting partial success. Their target---input-level answerability---differs fundamentally from output-dependent correctness. We analyze this difference and explain why their mean-shift succeeds under accuracy metrics but produces $\\Delta\\auroc{} \\equiv 0$ in our pipeline (\\S\\ref{sec:mean_shift}). Civelli et al.\\ transferred difficulty probes cross-lingually; we use their methodology as a control in our decomposition analysis.\n\n\\paragraph{Cross-lingual alignment.}\nMUSE \\cite{conneau2018muse} and VecMap \\cite{artetxe2018vecmap} demonstrated that cross-lingual word embedding spaces are approximately related by linear transformations. Our linear projection baseline is motivated by this literature; CaCLR's failure despite distributional matching is the novel finding.\n\n\\paragraph{Domain adaptation theory.}\nBen-David et al.\\ \\shortcite{bendavid2010theory} provide the $\\mathcal{H}$-divergence framework predicting that transfer degrades with distributional distance. Our resource-tier gradient is consistent with this theory; the novel findings are that the Pareto frontier shape is architecture-dependent (not predicted by theory) and that distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.\n\n\\paragraph{Representation similarity.}\nCKA \\cite{kornblith2019similarity} measures representational similarity between neural network layers. We use CKA to provide mechanistic context for cross-lingual transfer patterns, though the correlation with transfer success is weaker than anticipated.\n\n\\paragraph{Probing methodology.}\nHewitt \\& Liang \\shortcite{hewitt2019control} proposed control tasks to measure probe selectivity---the gap between real and random-label probe performance. We adopt their methodology and find that low-resource selectivity is dangerously low, qualifying our results.\n\n%% ============================================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Correctness Probing}\n\nGiven a multilingual LLM $f$ and a multiple-choice question $q$ in language $\\ell$, we extract the hidden state $\\mathbf{h}_l \\in \\mathbb{R}^d$ at layer $l$ after the final token. A correctness probe $g_l: \\mathbb{R}^d \\to [0,1]$ is trained on English data to predict $y \\in \\{0,1\\}$ (whether the model's greedy answer is correct).\n\nWe use two probe architectures: logistic regression (default) and 2-layer MLP (512 hidden units, ReLU). All activations are StandardScaler-normalized per layer using English training statistics.\n\n\\subsection{Transfer Conditions}\n\nWe evaluate five transfer strategies for applying an English-trained probe to language $\\ell$:\n\n\\paragraph{Zero-shot.} Apply the English probe directly to $\\ell$-language activations after English-fitted StandardScaler normalization.\n\n\\paragraph{Mean-shift.} Subtract the mean activation difference: $\\tilde{\\mathbf{h}}^{(\\ell)} = \\mathbf{h}^{(\\ell)} - (\\boldsymbol{\\mu}_\\ell - \\boldsymbol{\\mu}_{\\text{en}})$. We prove this is equivalent to zero-shot for \\auroc{} (\\S\\ref{sec:mean_shift}).\n\n\\paragraph{Linear projection.} Learn an affine map $\\mathbf{W}\\mathbf{h}^{(\\ell)} + \\mathbf{b}$ from $n$ parallel activation pairs. We study $n \\in \\{10, 20, 50, 100, 200\\}$.\n\n\\paragraph{Few-shot.} Retrain the probe on $k$ target-language labeled examples ($k \\in \\{25, 100\\}$), initializing from the English probe.\n\n\\paragraph{CaCLR.} Train with a composite objective $\\mathcal{L} = \\mathcal{L}_{\\text{BCE}} + \\alpha \\cdot \\mathcal{L}_{\\text{SB-ECE}} + \\beta \\cdot \\mathcal{L}_{\\text{consistency}}$, where $\\mathcal{L}_{\\text{consistency}}$ minimizes MMD between English and target-language activation distributions using parallel inputs from the GlobalMMLU train split. This requires parallel inputs but zero target-language labels.\n\n\\subsection{Mean-Shift Rank-Invariance}\n\\label{sec:mean_shift}\n\n\\begin{theorem}[Mean-Shift Rank-Invariance]\nLet $g(\\mathbf{h}) = \\sigma(\\mathbf{w}^\\top \\mathbf{h} + b)$ be a logistic regression probe trained on StandardScaler-normalized English activations. For any target language $\\ell$ with mean activation $\\boldsymbol{\\mu}_\\ell$ vs.\\ English mean $\\boldsymbol{\\mu}_{\\text{en}}$, the mean-shifted logit is:\n\\begin{align}\n\\mathbf{w}^\\top \\tilde{\\mathbf{h}}^{(\\ell)} + b &= \\mathbf{w}^\\top \\mathbf{h}^{(\\ell)} + b - \\underbrace{\\mathbf{w}^\\top(\\boldsymbol{\\mu}_\\ell - \\boldsymbol{\\mu}_{\\text{en}})}_{\\text{constant } c_\\ell}\n\\end{align}\nSince $c_\\ell$ is constant across all samples in language $\\ell$, the ranking of logits is preserved. \\auroc{} depends only on rankings, so $\\Delta\\auroc{} \\equiv 0$.\n\\end{theorem}\n\nWe validate this empirically: across 2 models $\\times$ all probed layers $\\times$ 19 languages, the observed $\\Delta\\auroc{}$ is exactly 0.000. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities (range: $[-1.2, +6.8]$pp).\n\nThis distinguishes our setup from Xiao et al., where mean-shift improves \\emph{accuracy} (a threshold-dependent metric). Under our rank-based evaluation, mean-shift is provably inert.\n\n\\subsection{Difficulty Decomposition}\n\nFollowing Civelli et al., we train IRT difficulty probes (Ridge regression on human difficulty scores) and project out the difficulty direction from activations:\n\\begin{equation}\n\\mathbf{h}_{\\text{residual}} = \\mathbf{h} - \\frac{\\mathbf{h}^\\top \\mathbf{d}}{\\|\\mathbf{d}\\|^2} \\mathbf{d}\n\\end{equation}\nwhere $\\mathbf{d}$ is the difficulty probe weight vector. We retrain correctness probes on $\\mathbf{h}_{\\text{residual}}$ and compare transfer. A random-direction control replaces $\\mathbf{d}$ with a random unit vector.\n\n\\subsection{Orthogonality Measurement}\n\nWe prompt each model for verbalized confidence scores, fit a confidence probe on the resulting activations, and measure the cosine similarity between confidence and correctness probe weight vectors across all languages and architectures.\n\n%% ============================================================\n\\section{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.} Qwen3-235B-A22B (94 layers, MoE, INT8), Llama~4 Scout (48 layers, MoE, INT8), Gemma~4 31B (60 layers, Dense, FP16). INT8 quantization is validated against FP16 (\\S\\ref{sec:int8}).\n\n\\paragraph{Benchmarks.} GlobalMMLU (primary), Belebele (reading comprehension), MMLU-ProX (translated MMLU). Train/test split following GlobalMMLU protocol.\n\n\\paragraph{Languages.} Core set: 20 languages spanning 12 families and 3 resource tiers. Extended set: 52 languages, 15 families, 4 resource tiers.\n\n\\paragraph{Layers probed.} Every 4th layer for Qwen3 (24 points over 94 layers), every 4th for Llama~4 (12 points over 48), every 4th for Gemma~4 (15 points over 60).\n\n\\paragraph{Statistical rigor.} Bootstrap CIs (1000 resamples) on all \\auroc{}/\\ece{}; paired permutation tests for method comparisons; Cohen's $d$ for effect sizes.\n\n%% ============================================================\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{English Probe Performance}\n\nTable~\\ref{tab:en_probe} shows English correctness probe \\auroc{} across layers for all three architectures. Probe quality increases with depth up to approximately 75--80\\% of total layers, then declines in the final layers. The best English \\auroc{} is 0.776 (Qwen3, layer 72), 0.749 (Llama~4, layer 36), and 0.761 (Gemma~4, layer 45). MLP probes provide a modest advantage ($+1.0$pp mean) over logistic regression in English but transfer marginally worse ($-0.3$pp; Cohen's $d = 0.15$, $p = 0.34$), confirming logistic regression as the default choice.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Layer} & \\textbf{Depth} & \\textbf{LogReg} & \\textbf{MLP} & \\textbf{ECE\\textsubscript{TC}} \\\\\n\\midrule\n\\multicolumn{5}{c}{\\emph{Qwen3-235B-A22B (94 layers)}} \\\\\n\\midrule\n4 & 4\\% & .612 & .618 & .192 \\\\\n28 & 30\\% & .694 & .708 & .121 \\\\\n52 & 55\\% & .742 & .755 & .082 \\\\\n72 & 77\\% & \\textbf{.776} & \\textbf{.783} & \\textbf{.069} \\\\\n88 & 94\\% & .753 & .762 & .079 \\\\\n\\midrule\n\\multicolumn{5}{c}{\\emph{Llama 4 Scout (48 layers)}} \\\\\n\\midrule\n8 & 17\\% & .631 & .641 & .168 \\\\\n20 & 42\\% & .712 & .722 & .098 \\\\\n36 & 75\\% & \\textbf{.749} & \\textbf{.755} & \\textbf{.074} \\\\\n44 & 92\\% & .731 & .738 & .084 \\\\\n\\midrule\n\\multicolumn{5}{c}{\\emph{Gemma 4 31B Dense (60 layers)}} \\\\\n\\midrule\n45 & 75\\% & \\multicolumn{2}{c}{\\textbf{.761}} & — \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{English correctness probe \\auroc{} (LogReg and MLP) and temperature-calibrated \\ece{} at selected layers. Best layer per model in bold.}\n\\label{tab:en_probe}\n\\end{table}\n\n\\subsection{Cross-Lingual Transfer and the Resource-Tier Taxonomy}\n\\label{sec:transfer}\n\nTable~\\ref{tab:transfer_tier} presents the central finding: zero-shot probe transfer follows a clear resource-tier gradient. On Qwen3, high-resource languages (zh, fr, de, es, ja, ko, ru) transfer at a mean \\auroc{} of 0.663 (7--8pp below English). Mid-resource languages (ar, hi, vi, id, th, pl, uk) average 0.615 (10--12pp drop). Low-resource languages (bn, te, ta, sw, yo) average 0.548 (13--20pp drop), with Yoruba reaching 19.9pp below English.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Tier} & \\textbf{$n$} & \\textbf{Qwen3} & \\textbf{Llama4} & \\textbf{Gemma4} \\\\\n\\midrule\nHigh & 7 & .663 & .648 & — \\\\\nMid & 7 & .615 & .582 & — \\\\\nLow & 5 & .548 & .522 & — \\\\\n\\midrule\nAll 19 & 19 & .618 & .588 & .605 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Zero-shot transfer \\auroc{} (mean) by resource tier. Qwen3 and Llama~4 broken down by tier on the 19-language core set.}\n\\label{tab:transfer_tier}\n\\end{table}\n\nExtended to 52 languages (Table~\\ref{tab:extended}), the picture worsens. The overall mean drops to 0.581, with a 24\\% pass rate (languages exceeding 0.65 \\auroc{}). Very-low-resource languages ($n=10$, including Amharic, Lao, Mongolian) average 0.518 with 0\\% pass rate. Amharic is the worst at 0.488---below chance when accounting for control task selectivity.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Tier} & \\textbf{$n$} & \\textbf{\\auroc{}} & \\textbf{Std} & \\textbf{Pass} \\\\\n\\midrule\nHigh & 10 & .651 & .017 & 70\\% \\\\\nMid & 18 & .598 & .023 & 28\\% \\\\\nLow & 14 & .553 & .028 & 7\\% \\\\\nVery low & 10 & .518 & .021 & 0\\% \\\\\n\\midrule\nAll & 52 & .581 & — & 24\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Zero-shot transfer \\auroc{} across 52 languages (Qwen3). Pass rate = fraction exceeding 0.65 \\auroc{}.}\n\\label{tab:extended}\n\\end{table}\n\nTable~\\ref{tab:per_lang} provides per-language zero-shot transfer \\auroc{} on Qwen3 for the 19-language core set. The best transfer layer shifts shallower with decreasing resource level: layer 52 for zh/fr/de, layer 48 for es/ja/ko, down to layer 24 for Yoruba. This depth gradient motivates the Pareto frontier analysis.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}llccccc@{}}\n\\toprule\n\\textbf{Lang} & \\textbf{Tier} & \\textbf{Layer} & \\textbf{\\auroc{}} & \\textbf{Drop} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nzh & high & 52 & .668 & 7.4 & $-$.55 & .006 \\\\\nfr & high & 52 & .672 & 7.0 & $-$.51 & .011 \\\\\nde & high & 52 & .671 & 7.1 & $-$.48 & .017 \\\\\nes & high & 48 & .661 & 7.4 & $-$.42 & .041 \\\\\nja & high & 48 & .658 & 7.7 & $-$.37 & .075 \\\\\nko & high & 48 & .656 & 7.9 & $-$.33 & .115 \\\\\nru & high & 44 & .652 & 7.6 & $-$.25 & .239 \\\\\n\\midrule\npl & mid & 44 & .628 & 10.0 & $-$.14 & .513 \\\\\nar & mid & 40 & .625 & 9.6 & $-$.18 & .399 \\\\\nid & mid & 40 & .621 & 10.0 & $-$.02 & .926 \\\\\nhi & mid & 40 & .618 & 10.3 & $-$.11 & .609 \\\\\nuk & mid & 40 & .614 & 10.7 & $-$.06 & .782 \\\\\nvi & mid & 40 & .607 & 11.4 & .04 & .854 \\\\\nth & mid & 36 & .594 & 11.8 & .09 & .674 \\\\\n\\midrule\nbn & low & 28 & .553 & 14.1 & .14 & .514 \\\\\nte & low & 28 & .571 & 12.3 & .18 & .400 \\\\\nta & low & 28 & .568 & 12.6 & .22 & .303 \\\\\nsw & low & 28 & .537 & 15.7 & .27 & .202 \\\\\nyo & low & 24 & .512 & 19.9 & .31 & .141 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-language zero-shot transfer on Qwen3. Layer = best transfer layer; Drop = pp below English at same layer; $\\rho$ = Spearman correlation between depth and transfer \\auroc{}; $p$ = associated $p$-value.}\n\\label{tab:per_lang}\n\\end{table}\n\n\\subsection{Architecture-Dependent Pareto Frontier}\n\\label{sec:pareto}\n\nThe depth--transferability tradeoff is real but architecture-dependent. Table~\\ref{tab:arch_compare} summarizes across three architectures. The dense model (Gemma~4) shows the strongest frontier ($\\rho = -0.44$, sign consistency 0.68), followed by the large MoE (Qwen3: $\\rho = -0.38$, 0.63) and the smaller MoE (Llama~4: $\\rho = -0.18$, 0.53).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Type} & \\textbf{EN} & \\textbf{ZS} & \\textbf{$\\rho$} & \\textbf{Sign} \\\\\n\\midrule\nQwen3 & MoE & .776 & .618 & $-$.38 & .63 \\\\\nLlama4 & MoE & .749 & .588 & $-$.18 & .53 \\\\\nGemma4 & Dense & .761 & .605 & $-$.44 & .68 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Three-architecture comparison. EN = best English \\auroc{}; ZS = 19-lang mean zero-shot transfer; $\\rho$ = global Spearman; Sign = sign consistency of per-language $\\rho$.}\n\\label{tab:arch_compare}\n\\end{table}\n\nCross-architecture agreement is low: Kendall's $\\tau = 0.33$ between Qwen3 and Llama~4 for optimal layer rankings, and 0.42 between Qwen3 and Gemma~4. Practitioners cannot transfer layer selection findings from one model to another.\n\nOn Llama~4 Scout, the per-language Spearman $\\rho$ median is only $-0.12$ (range: $[-0.41, +0.48]$), with sign consistency at 0.53---essentially a coin flip. Non-monotonic jumps at layers 20--28 reflect MoE expert routing shifts. The Pareto frontier that exists on Qwen3 and Gemma~4 largely vanishes on Llama~4.\n\n\\subsection{Transfer Method Comparison}\n\\label{sec:methods}\n\nTable~\\ref{tab:methods} compares all transfer conditions across both primary models. Mean-shift produces exactly $\\Delta\\auroc{} = 0$ (as proven in \\S\\ref{sec:mean_shift}). CaCLR provides negligible improvement ($+0.5$pp on Qwen3, $+0.6$pp on Llama~4; Cohen's $d = 0.04$; permutation test $p = 0.71$). Linear projection offers modest gains ($+1.8$pp on Qwen3 with 50 parallel pairs). Few-shot with 100 labels is the strongest method ($+4.4$pp on Qwen3; $d = 0.58$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}lccccl@{}}\n\\toprule\n\\textbf{Method} & \\textbf{Q3} & \\textbf{L4} & \\textbf{$d$} & \\textbf{Labels} \\\\\n\\midrule\nZero-shot & .618 & .588 & — & 0 \\\\\nMean-shift & .618 & .588 & 0.00 & 0 \\\\\nCaCLR & .623 & .594 & 0.04 & 0 + parallel \\\\\nLinProj (50) & .636 & .608 & 0.24 & $\\sim$50 parallel \\\\\nFew-shot 25 & .644 & .617 & 0.35 & 25 target \\\\\nFew-shot 100 & .662 & .641 & 0.58 & 100 target \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Transfer method comparison (19-language mean \\auroc{}). Q3 = Qwen3; L4 = Llama~4; $d$ = Cohen's $d$ vs.\\ zero-shot.}\n\\label{tab:methods}\n\\end{table}\n\n\\subsection{CaCLR: A Principled Negative Result}\n\\label{sec:caclr}\n\nCaCLR's consistency loss ($\\beta \\cdot \\mathcal{L}_{\\text{consistency}}$) is inert. Table~\\ref{tab:caclr_ablation} shows the ablation: adding consistency to BCE+SB-ECE \\emph{reduces} \\auroc{} by 0.6pp. The $\\beta$ sweep over three orders of magnitude (0.001--1.0) produces $<$0.4pp variation (Table~\\ref{tab:beta_sweep}), ruling out a tuning failure.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Variant} & \\textbf{\\auroc{}} & \\textbf{$\\Delta$pp} \\\\\n\\midrule\nFull CaCLR & .621 & 0.0 \\\\\nBCE + SB-ECE & .627 & $+$0.6 \\\\\nBCE + Consistency & .611 & $-$1.0 \\\\\nBCE only ($\\approx$ zero-shot) & .618 & $-$0.3 \\\\\nLinear projection (ref.) & .636 & $+$1.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CaCLR ablation (Qwen3, 19-language mean). Removing consistency \\emph{improves} performance.}\n\\label{tab:caclr_ablation}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcclcc@{}}\n\\toprule\n$\\beta$ & \\textbf{\\auroc{}} & $\\Delta$pp & $\\beta$ & \\textbf{\\auroc{}} & $\\Delta$pp \\\\\n\\midrule\n0.0 & .627 & 0.0 & 0.05 & .623 & $-$0.4 \\\\\n0.001 & .626 & $-$0.1 & 0.1 & .621 & $-$0.6 \\\\\n0.01 & .625 & $-$0.2 & 0.5 & .618 & $-$0.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CaCLR $\\beta$ sensitivity (Qwen3, $\\alpha = 0.3$ fixed, 19-lang mean). Increasing $\\beta$ monotonically hurts.}\n\\label{tab:beta_sweep}\n\\end{table}\n\nThe mechanistic explanation: CKA analysis (\\S\\ref{sec:cka}) shows that cross-lingual misalignment at deeper layers is \\emph{geometric} (the correctness direction rotates across language subspaces), not merely distributional. MMD-based alignment cannot correct rotation, which is why linear projection (which learns the rotation) succeeds where CaCLR (which matches distributions) fails.\n\nCaCLR also fails on Gemma~4 Dense (mean \\auroc{} 0.609, $-0.9$pp vs.\\ linear projection), ruling out the hypothesis that MoE routing specifically caused the failure. On Belebele and MMLU-ProX, CaCLR underperforms linear projection by $-0.8$pp and $-1.1$pp respectively, confirming the negative result generalizes across benchmarks.\n\n\\subsection{Difficulty Decomposition: Inconclusive}\n\\label{sec:decomposition}\n\nThe IRT difficulty probe achieves $R^2 = 0.52$ in English (Qwen3) but transfers with degraded quality (9-language mean $R^2 = 0.38$). Projecting out the difficulty direction changes transfer \\auroc{} by $-0.5$pp on average---barely above the random-direction control ($-0.3$pp).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Q3} & \\textbf{$\\Delta$} & \\textbf{L4} & \\textbf{$\\Delta$} \\\\\n\\midrule\nFull activations & .618 & 0.0 & .588 & 0.0 \\\\\nResidual (diff.\\ out) & .613 & $-$0.5 & .583 & $-$0.5 \\\\\nDifficulty only & .569 & $-$4.9 & .548 & $-$4.0 \\\\\nRandom dir.\\ control & .615 & $-$0.3 & .585 & $-$0.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Decomposition ablation (9-language mean \\auroc{}). Difficulty removal marginally hurts, barely above random control.}\n\\label{tab:decomp}\n\\end{table}\n\nPer-language analysis shows no systematic pattern: 3/10 languages improve slightly ($+0.4$ to $+1.3$pp), 5/10 worsen ($-0.3$ to $-2.1$pp), 2/10 unchanged. The difficulty-shared component carries useful cross-lingual signal (questions hard in English tend to be hard everywhere); removing it strips away a genuine invariance. The cosine between difficulty and correctness directions ($0.36 \\pm 0.11$) confirms moderate entanglement, preventing clean separation.\n\n\\subsection{Cross-Lingual Orthogonality}\n\\label{sec:orthogonality}\n\nThe correctness--confidence orthogonality reported by Miao \\& Ungar \\shortcite{miao2026orthogonality} for English persists cross-lingually (overall mean cosine $= 0.074 \\pm 0.036$; 73\\% of languages below 0.10). However, a resource-tier gradient emerges: high-resource mean 0.052, mid-resource 0.073, low-resource 0.108 (Spearman $\\rho = -0.61$ with resource level). Yoruba on Llama~4 reaches 0.172, an outlier weakening the universality claim.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Tier} & \\textbf{$n$} & \\textbf{Qwen3} & \\textbf{Llama4} & \\textbf{Mean} \\\\\n\\midrule\nHigh & 8 & .048 & .056 & .052 \\\\\nMid & 7 & .066 & .075 & .073 \\\\\nLow & 5 & .100 & .122 & .108 \\\\\nAll & 20 & .069 & .079 & .074 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Correctness--confidence cosine similarity by resource tier. Lower = more orthogonal. Orthogonality persists but weakens for low-resource languages.}\n\\label{tab:orthogonality}\n\\end{table}\n\nThis confirms that output-based calibration faces a structural ceiling regardless of language, but this ceiling is noisier for low-resource languages where the model has less capacity to maintain the confidence--correctness dissociation.\n\n\\subsection{CKA Mechanistic Analysis}\n\\label{sec:cka}\n\nCKA between English and target-language activations declines with depth (shallow mean 0.89, deep mean 0.54), confirming that deeper layers are less cross-lingually aligned. However, the correlation between CKA and transfer \\auroc{} is weak: Pearson $r = 0.38$ on Qwen3, $r = 0.24$ on Llama~4, $r = 0.32$ combined.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Model} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{Sig.} & \\textbf{Total} \\\\\n\\midrule\nQwen3 & .38 & .002 & 5/19 & 19 \\\\\nLlama4 & .24 & .041 & 2/19 & 19 \\\\\nCombined & .32 & .001 & 7/38 & 38 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CKA vs.\\ transfer \\auroc{} correlation. Sig.\\ = languages with individually significant correlation.}\n\\label{tab:cka}\n\\end{table}\n\nA threshold analysis at CKA $= 0.35$ partially replicates: below this threshold, 61\\% of language-layer pairs show transfer collapse (\\auroc{} $< 0.55$), vs.\\ 22\\% above. But 39\\% of below-threshold pairs do not collapse, and the threshold is architecture-dependent. CKA provides a suggestive but not convincing mechanistic account.\n\nThe key qualitative insight survives: cross-lingual misalignment is geometric (correctness direction rotates), explaining why MMD-based CaCLR fails while linear projection succeeds. But the quantitative relationship is too noisy for reliable prediction.\n\n\\subsection{Linear Projection Data Requirements}\n\\label{sec:linproj}\n\nLinear projection improves with more parallel pairs but saturates around 100 (Table~\\ref{tab:linproj_pairs}). Critically, it fails for low-resource languages even at 200 pairs: Bengali +0.8pp, Swahili +0.6pp, Yoruba +0.6pp---within noise.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}rccc@{}}\n\\toprule\n\\textbf{$n$} & \\textbf{\\auroc{}} & \\textbf{$\\Delta$pp} & \\textbf{\\%~Improved} \\\\\n\\midrule\n10 & .608 & $-$1.0 & 26\\% \\\\\n20 & .621 & $+$0.3 & 42\\% \\\\\n50 & .636 & $+$1.8 & 55\\% \\\\\n100 & .643 & $+$2.5 & 63\\% \\\\\n200 & .647 & $+$2.9 & 68\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Linear projection \\auroc{} by number of parallel pairs (19-language mean). Saturates at $\\sim$100 pairs.}\n\\label{tab:linproj_pairs}\n\\end{table}\n\nHigh-resource languages benefit from as few as 20 pairs ($+3.1$pp at 50 pairs), while low-resource languages show minimal improvement regardless of parallel data quantity. The fundamental bottleneck is not the number of parallel pairs but the quality of cross-lingual activation alignment.\n\n\\subsection{Control Tasks: Capacity Artifacts}\n\\label{sec:control}\n\nControl tasks (probes trained on randomly permuted labels) reveal that probe \\auroc{} partially reflects capacity rather than genuine correctness signal. Table~\\ref{tab:control} shows selectivity by resource tier.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\n\\textbf{Tier} & \\textbf{$n$} & \\textbf{Probe} & \\textbf{Ctrl} & \\textbf{Sel.} & \\textbf{Min} \\\\\n\\midrule\nHigh & 7 & .660 & .548 & 17.2 & 10.4 \\\\\nMid & 7 & .614 & .546 & 13.8 & 8.2 \\\\\nLow & 5 & .548 & .544 & 8.4 & 4.8 \\\\\nAll & 19 & .618 & .546 & 13.8 & 4.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Control task selectivity (pp) by resource tier. Probe = real-label \\auroc{}; Ctrl = random-label \\auroc{}; Sel.\\ = selectivity (Probe $-$ Ctrl); Min = minimum selectivity in tier.}\n\\label{tab:control}\n\\end{table}\n\nFor low-resource languages, 28\\% of language-layer pairs have selectivity below 8pp. At the English-optimal layer, Swahili scores 0.508 (selectivity $-4.4$pp, \\emph{below} the random-label control) and Yoruba scores 0.487 ($-6.4$pp below control). These results are indistinguishable from probe memorization of random structure in high-dimensional activation spaces.\n\nThe selectivity depth gradient is positive (deeper layers have higher selectivity: 3.3pp at 0--25\\% depth, 9.5pp at 50--75\\%), reflecting that the correctness signal strengthens with depth while control \\auroc{} remains constant ($\\sim$0.55). This means shallow-layer transfer results for low-resource languages should be interpreted with particular caution.\n\n\\subsection{INT8 Quantization Validation}\n\\label{sec:int8}\n\nINT8 quantization introduces minimal distortion: mean $\\Delta\\auroc{} = -0.3$pp (max $-0.7$pp at layer 40), activation cosine similarity $= 0.994$, layer ranking correlation $= 0.98$. Quantization is not a confound.\n\n\\subsection{Cross-Benchmark Generalization}\n\nFindings partially generalize across benchmarks. On Belebele (natively multilingual reading comprehension), zero-shot transfer drops an additional 2.4pp vs.\\ GlobalMMLU, with language rankings largely preserved ($\\rho = 0.83$). On MMLU-ProX (machine-translated MMLU), the drop is 3.9pp with lower ranking stability ($\\rho = 0.69$), reflecting translation quality variation. CaCLR underperforms linear projection on both benchmarks ($-0.8$pp and $-1.1$pp respectively).\n\n%% ============================================================\n\\section{Analysis}\n\\label{sec:analysis}\n\n\\paragraph{Why does transfer fail for low-resource languages?}\nThree factors compound: (1) the model's internal representations for these languages are less structured, reducing the quality of the correctness signal at any depth; (2) the cross-lingual activation alignment (measured by CKA) degrades more steeply with depth for low-resource languages (CKA at 75\\% depth: sw $= 0.33$, yo $= 0.28$ vs.\\ fr $= 0.71$, zh $= 0.68$); (3) control tasks show that even the \\auroc{} metric itself is unreliable in these settings (selectivity $< 8$pp).\n\n\\paragraph{Why does CaCLR fail?}\nCaCLR's MMD-based consistency loss attempts to align activation \\emph{distributions} across languages. But the cross-lingual misalignment that matters for correctness probes is \\emph{geometric}: the correctness direction rotates across language subspaces at deeper layers. Distribution matching cannot correct rotation---it collapses both signal and noise. Linear projection directly estimates the rotation and therefore succeeds where CaCLR fails.\n\n\\paragraph{Practical guidance.}\nFor high-resource languages (en, zh, fr, de, es, ja, ko, ru): zero-shot transfer is viable with 7--8pp performance loss. Linear projection with $\\sim$50 parallel pairs recovers an additional 1--3pp. For mid-resource languages: few-shot with 25 target-language labels provides the best cost-performance tradeoff. For low-resource languages: the zero-label dream is closed. Few-shot with 100 labels is the minimum viable approach, and even then, results should be validated against control tasks to ensure genuine correctness signal.\n\n%% ============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe present the first systematic evaluation of cross-lingual correctness probe transfer, finding that the probe-based calibration research line does not generalize beyond a small set of high-resource languages without fundamental methodological advances. Mean-shift is provably inert under standard pipelines. The depth--transferability Pareto frontier is architecture-dependent, precluding universal layer selection. CaCLR---the natural distributional-matching approach---fails because cross-lingual misalignment is geometric, not distributional. Few-shot adaptation with 25--100 labels is the only viable path for the majority of the world's languages.\n\n\\paragraph{Limitations.}\nOur study is restricted to MCQA benchmarks. Open-ended generation may exhibit different calibration patterns. INT8 quantization, while validated, may interact differently with other probe architectures. The resource-tier taxonomy is coarse---individual language pairs may deviate based on typological proximity rather than resource level alone.\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a84e288-6832-45a0-be28-e267061ad84a",
  "isSidechain": false,
  "requestId": "req_011CbEV7kNB2CCrQDU2KwM6R",
  "type": "assistant",
  "uuid": "43d550c2-dcd5-40dd-acf5-9f19bb59758c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S8xZ9qmCc77nF4j5HsJQwg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 793,
      "cache_read_input_tokens": 57795,
      "output_tokens": 11596,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 793,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11596,
          "cache_read_input_tokens": 57795,
          "cache_creation_input_tokens": 793,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 793
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

_source line 19 · 2026-05-20T20:57:31.097Z_

<details><summary>↩ Tool result · `toolu_012uZE1gLP9f3p9QARLfAVnR`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "43d550c2-dcd5-40dd-acf5-9f19bb59758c",
  "isSidechain": false,
  "promptId": "ce9c66bf-f5bc-46b5-95a4-aabc6b39fe73",
  "type": "user",
  "uuid": "cf1d9824-c79d-4ff4-9afd-e23dca2fc906",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{microtype}\n\\usepackage{url}\n\n\\newcommand{\\auroc}{\\textsc{auroc}}\n\\newcommand{\\ece}{\\textsc{ece}}\n\n\\title{Does Probe-Based Calibration Work Beyond English?\\\\A Systematic Investigation Across 3 Architectures and 52 Languages}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nProbe-based calibration---training linear classifiers on internal representations to predict answer correctness---has emerged as a promising alternative to output-based calibration in LLMs, but existing work is English-only. We present the first systematic cross-lingual evaluation of correctness probe transfer across 3 architectures (Qwen3-235B, Llama~4 Scout, Gemma~4 31B), up to 52 languages, and 5 transfer conditions. Our findings are sobering. First, we prove that mean-shift adaptation produces exactly zero \\auroc{} change under standard probing pipelines (rank-invariance theorem), distinguishing our setup from prior work. Second, we establish a resource-tier taxonomy of probe transferability: high-resource languages transfer with 7--8pp \\auroc{} drop, mid-resource at 10--12pp, and low-resource at 13--20pp, with control tasks revealing that 28\\% of low-resource results are capacity artifacts (selectivity $<$8pp). Third, the natural distributional-matching approach (CaCLR) fails---its consistency loss is inert across three orders of magnitude of hyperparameter sweep ($p = 0.71$ vs.\\ zero-shot, Cohen's $d = 0.04$). The depth--transferability Pareto frontier is architecture-dependent ($\\rho = -0.44$ dense, $-0.38$ MoE-large, $-0.18$ MoE-small; cross-architecture $\\tau = 0.33$), precluding universal layer selection. Few-shot adaptation with 25--100 target-language labels is the only viable path, closing the zero-label dream for low-resource languages.\n\\end{abstract}\n\n%% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n\nNon-English languages suffer substantially worse calibration in multilingual LLMs, with expected calibration error (\\ece{}) up to 5$\\times$ higher than English \\cite{kadeethum2024calibration}. Output-based calibration methods face a structural ceiling: the correctness direction in internal representations is approximately orthogonal to verbalized confidence \\cite{miao2026orthogonality}, meaning no amount of prompt engineering or temperature scaling can fully close the gap.\n\nA promising alternative is \\emph{probe-based calibration}, which trains lightweight classifiers on internal activations to predict whether the model's answer is correct \\cite{miao2024coral,burns2023discovering}. This approach has shown strong results in English, with recent work demonstrating cross-task transfer \\cite{miao2024coral}, confidence manifold structure \\cite{luo2024confidence}, and the potential for representation-level steering \\cite{miao2026orthogonality}. However, all of this work is English-only.\n\nThe natural question---\\emph{do English correctness probes transfer to other languages?}---has not been systematically investigated. Xiao et al.\\ \\shortcite{xiao2025knowledge} transferred \\emph{knowledge-boundary} probes (input-level answerability) across 8 languages, but knowledge boundaries are fundamentally different from correctness signals: the former encodes whether the model has seen relevant training data, while the latter depends on the model's output for a specific question. Their partial success does not predict ours.\n\nWe present a systematic investigation across 3 architectures (Qwen3-235B-A22B, Llama~4 Scout, Gemma~4 31B Dense), up to 52 languages spanning 15 language families, and 5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot, CaCLR). Our study yields three surviving contributions:\n\n\\paragraph{(1) Mean-shift rank-invariance.} We prove that under StandardScaler normalization and logistic regression---the standard probing pipeline---mean-shift adaptation produces \\emph{exactly} $\\Delta\\auroc{} = 0$ because mean subtraction adds a constant to all logits, preserving ranks. This distinguishes our setup from Xiao et al., where mean-shift succeeds under different metrics.\n\n\\paragraph{(2) Resource-tier taxonomy.} We provide the first quantification of cross-lingual probe transferability across 52 languages, establishing that high-resource languages transfer (7--8pp drop), mid-resource is marginal (10--12pp), and low-resource fails (13--20pp). Control tasks reveal capacity artifacts that further weaken low-resource results.\n\n\\paragraph{(3) Practical recommendation.} Zero-label transfer fails for the majority of the world's languages. Few-shot adaptation with 25--100 target-language labels is the only viable path, closing the zero-label dream for low-resource languages.\n\nAlong the way, we report that the depth--transferability Pareto frontier is architecture-dependent, that the natural distributional-matching method (CaCLR) produces negligible improvement, that difficulty--capability decomposition is inconclusive, and that CKA-based mechanistic analysis is suggestive but not convincing. The paper serves as a sobering empirical reality check for the probe-based calibration research line.\n\n%% ============================================================\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Probe-based calibration.}\nCORAL \\cite{miao2024coral} demonstrated cross-task correctness probe transfer in English; CCPS \\cite{liu2024confidence} and the Confidence Manifold \\cite{luo2024confidence} explored structural properties of correctness representations. Miao \\& Ungar \\shortcite{miao2026orthogonality} discovered that correctness and verbalized confidence directions are orthogonal in English, motivating representation-level intervention. All are English-only.\n\n\\paragraph{Cross-lingual probing.}\nXiao et al.\\ \\shortcite{xiao2025knowledge} transferred knowledge-boundary probes across 8 languages using mean-shift adaptation, reporting partial success. Their target---input-level answerability---differs fundamentally from output-dependent correctness. We analyze this difference and explain why their mean-shift succeeds under accuracy metrics but produces $\\Delta\\auroc{} \\equiv 0$ in our pipeline (\\S\\ref{sec:mean_shift}). Civelli et al.\\ transferred difficulty probes cross-lingually; we use their methodology as a control in our decomposition analysis.\n\n\\paragraph{Cross-lingual alignment.}\nMUSE \\cite{conneau2018muse} and VecMap \\cite{artetxe2018vecmap} demonstrated that cross-lingual word embedding spaces are approximately related by linear transformations. Our linear projection baseline is motivated by this literature; CaCLR's failure despite distributional matching is the novel finding.\n\n\\paragraph{Domain adaptation theory.}\nBen-David et al.\\ \\shortcite{bendavid2010theory} provide the $\\mathcal{H}$-divergence framework predicting that transfer degrades with distributional distance. Our resource-tier gradient is consistent with this theory; the novel findings are that the Pareto frontier shape is architecture-dependent (not predicted by theory) and that distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.\n\n\\paragraph{Representation similarity.}\nCKA \\cite{kornblith2019similarity} measures representational similarity between neural network layers. We use CKA to provide mechanistic context for cross-lingual transfer patterns, though the correlation with transfer success is weaker than anticipated.\n\n\\paragraph{Probing methodology.}\nHewitt \\& Liang \\shortcite{hewitt2019control} proposed control tasks to measure probe selectivity---the gap between real and random-label probe performance. We adopt their methodology and find that low-resource selectivity is dangerously low, qualifying our results.\n\n%% ============================================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Correctness Probing}\n\nGiven a multilingual LLM $f$ and a multiple-choice question $q$ in language $\\ell$, we extract the hidden state $\\mathbf{h}_l \\in \\mathbb{R}^d$ at layer $l$ after the final token. A correctness probe $g_l: \\mathbb{R}^d \\to [0,1]$ is trained on English data to predict $y \\in \\{0,1\\}$ (whether the model's greedy answer is correct).\n\nWe use two probe architectures: logistic regression (default) and 2-layer MLP (512 hidden units, ReLU). All activations are StandardScaler-normalized per layer using English training statistics.\n\n\\subsection{Transfer Conditions}\n\nWe evaluate five transfer strategies for applying an English-trained probe to language $\\ell$:\n\n\\paragraph{Zero-shot.} Apply the English probe directly to $\\ell$-language activations after English-fitted StandardScaler normalization.\n\n\\paragraph{Mean-shift.} Subtract the mean activation difference: $\\tilde{\\mathbf{h}}^{(\\ell)} = \\mathbf{h}^{(\\ell)} - (\\boldsymbol{\\mu}_\\ell - \\boldsymbol{\\mu}_{\\text{en}})$. We prove this is equivalent to zero-shot for \\auroc{} (\\S\\ref{sec:mean_shift}).\n\n\\paragraph{Linear projection.} Learn an affine map $\\mathbf{W}\\mathbf{h}^{(\\ell)} + \\mathbf{b}$ from $n$ parallel activation pairs. We study $n \\in \\{10, 20, 50, 100, 200\\}$.\n\n\\paragraph{Few-shot.} Retrain the probe on $k$ target-language labeled examples ($k \\in \\{25, 100\\}$), initializing from the English probe.\n\n\\paragraph{CaCLR.} Train with a composite objective $\\mathcal{L} = \\mathcal{L}_{\\text{BCE}} + \\alpha \\cdot \\mathcal{L}_{\\text{SB-ECE}} + \\beta \\cdot \\mathcal{L}_{\\text{consistency}}$, where $\\mathcal{L}_{\\text{consistency}}$ minimizes MMD between English and target-language activation distributions using parallel inputs from the GlobalMMLU train split. This requires parallel inputs but zero target-language labels.\n\n\\subsection{Mean-Shift Rank-Invariance}\n\\label{sec:mean_shift}\n\n\\begin{theorem}[Mean-Shift Rank-Invariance]\nLet $g(\\mathbf{h}) = \\sigma(\\mathbf{w}^\\top \\mathbf{h} + b)$ be a logistic regression probe trained on StandardScaler-normalized English activations. For any target language $\\ell$ with mean activation $\\boldsymbol{\\mu}_\\ell$ vs.\\ English mean $\\boldsymbol{\\mu}_{\\text{en}}$, the mean-shifted logit is:\n\\begin{align}\n\\mathbf{w}^\\top \\tilde{\\mathbf{h}}^{(\\ell)} + b &= \\mathbf{w}^\\top \\mathbf{h}^{(\\ell)} + b - \\underbrace{\\mathbf{w}^\\top(\\boldsymbol{\\mu}_\\ell - \\boldsymbol{\\mu}_{\\text{en}})}_{\\text{constant } c_\\ell}\n\\end{align}\nSince $c_\\ell$ is constant across all samples in language $\\ell$, the ranking of logits is preserved. \\auroc{} depends only on rankings, so $\\Delta\\auroc{} \\equiv 0$.\n\\end{theorem}\n\nWe validate this empirically: across 2 models $\\times$ all probed layers $\\times$ 19 languages, the observed $\\Delta\\auroc{}$ is exactly 0.000. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities (range: $[-1.2, +6.8]$pp).\n\nThis distinguishes our setup from Xiao et al., where mean-shift improves \\emph{accuracy} (a threshold-dependent metric). Under our rank-based evaluation, mean-shift is provably inert.\n\n\\subsection{Difficulty Decomposition}\n\nFollowing Civelli et al., we train IRT difficulty probes (Ridge regression on human difficulty scores) and project out the difficulty direction from activations:\n\\begin{equation}\n\\mathbf{h}_{\\text{residual}} = \\mathbf{h} - \\frac{\\mathbf{h}^\\top \\mathbf{d}}{\\|\\mathbf{d}\\|^2} \\mathbf{d}\n\\end{equation}\nwhere $\\mathbf{d}$ is the difficulty probe weight vector. We retrain correctness probes on $\\mathbf{h}_{\\text{residual}}$ and compare transfer. A random-direction control replaces $\\mathbf{d}$ with a random unit vector.\n\n\\subsection{Orthogonality Measurement}\n\nWe prompt each model for verbalized confidence scores, fit a confidence probe on the resulting activations, and measure the cosine similarity between confidence and correctness probe weight vectors across all languages and architectures.\n\n%% ============================================================\n\\section{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.} Qwen3-235B-A22B (94 layers, MoE, INT8), Llama~4 Scout (48 layers, MoE, INT8), Gemma~4 31B (60 layers, Dense, FP16). INT8 quantization is validated against FP16 (\\S\\ref{sec:int8}).\n\n\\paragraph{Benchmarks.} GlobalMMLU (primary), Belebele (reading comprehension), MMLU-ProX (translated MMLU). Train/test split following GlobalMMLU protocol.\n\n\\paragraph{Languages.} Core set: 20 languages spanning 12 families and 3 resource tiers. Extended set: 52 languages, 15 families, 4 resource tiers.\n\n\\paragraph{Layers probed.} Every 4th layer for Qwen3 (24 points over 94 layers), every 4th for Llama~4 (12 points over 48), every 4th for Gemma~4 (15 points over 60).\n\n\\paragraph{Statistical rigor.} Bootstrap CIs (1000 resamples) on all \\auroc{}/\\ece{}; paired permutation tests for method comparisons; Cohen's $d$ for effect sizes.\n\n%% ============================================================\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{English Probe Performance}\n\nTable~\\ref{tab:en_probe} shows English correctness probe \\auroc{} across layers for all three architectures. Probe quality increases with depth up to approximately 75--80\\% of total layers, then declines in the final layers. The best English \\auroc{} is 0.776 (Qwen3, layer 72), 0.749 (Llama~4, layer 36), and 0.761 (Gemma~4, layer 45). MLP probes provide a modest advantage ($+1.0$pp mean) over logistic regression in English but transfer marginally worse ($-0.3$pp; Cohen's $d = 0.15$, $p = 0.34$), confirming logistic regression as the default choice.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Layer} & \\textbf{Depth} & \\textbf{LogReg} & \\textbf{MLP} & \\textbf{ECE\\textsubscript{TC}} \\\\\n\\midrule\n\\multicolumn{5}{c}{\\emph{Qwen3-235B-A22B (94 layers)}} \\\\\n\\midrule\n4 & 4\\% & .612 & .618 & .192 \\\\\n28 & 30\\% & .694 & .708 & .121 \\\\\n52 & 55\\% & .742 & .755 & .082 \\\\\n72 & 77\\% & \\textbf{.776} & \\textbf{.783} & \\textbf{.069} \\\\\n88 & 94\\% & .753 & .762 & .079 \\\\\n\\midrule\n\\multicolumn{5}{c}{\\emph{Llama 4 Scout (48 layers)}} \\\\\n\\midrule\n8 & 17\\% & .631 & .641 & .168 \\\\\n20 & 42\\% & .712 & .722 & .098 \\\\\n36 & 75\\% & \\textbf{.749} & \\textbf{.755} & \\textbf{.074} \\\\\n44 & 92\\% & .731 & .738 & .084 \\\\\n\\midrule\n\\multicolumn{5}{c}{\\emph{Gemma 4 31B Dense (60 layers)}} \\\\\n\\midrule\n45 & 75\\% & \\multicolumn{2}{c}{\\textbf{.761}} & — \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{English correctness probe \\auroc{} (LogReg and MLP) and temperature-calibrated \\ece{} at selected layers. Best layer per model in bold.}\n\\label{tab:en_probe}\n\\end{table}\n\n\\subsection{Cross-Lingual Transfer and the Resource-Tier Taxonomy}\n\\label{sec:transfer}\n\nTable~\\ref{tab:transfer_tier} presents the central finding: zero-shot probe transfer follows a clear resource-tier gradient. On Qwen3, high-resource languages (zh, fr, de, es, ja, ko, ru) transfer at a mean \\auroc{} of 0.663 (7--8pp below English). Mid-resource languages (ar, hi, vi, id, th, pl, uk) average 0.615 (10--12pp drop). Low-resource languages (bn, te, ta, sw, yo) average 0.548 (13--20pp drop), with Yoruba reaching 19.9pp below English.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Tier} & \\textbf{$n$} & \\textbf{Qwen3} & \\textbf{Llama4} & \\textbf{Gemma4} \\\\\n\\midrule\nHigh & 7 & .663 & .648 & — \\\\\nMid & 7 & .615 & .582 & — \\\\\nLow & 5 & .548 & .522 & — \\\\\n\\midrule\nAll 19 & 19 & .618 & .588 & .605 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Zero-shot transfer \\auroc{} (mean) by resource tier. Qwen3 and Llama~4 broken down by tier on the 19-language core set.}\n\\label{tab:transfer_tier}\n\\end{table}\n\nExtended to 52 languages (Table~\\ref{tab:extended}), the picture worsens. The overall mean drops to 0.581, with a 24\\% pass rate (languages exceeding 0.65 \\auroc{}). Very-low-resource languages ($n=10$, including Amharic, Lao, Mongolian) average 0.518 with 0\\% pass rate. Amharic is the worst at 0.488---below chance when accounting for control task selectivity.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Tier} & \\textbf{$n$} & \\textbf{\\auroc{}} & \\textbf{Std} & \\textbf{Pass} \\\\\n\\midrule\nHigh & 10 & .651 & .017 & 70\\% \\\\\nMid & 18 & .598 & .023 & 28\\% \\\\\nLow & 14 & .553 & .028 & 7\\% \\\\\nVery low & 10 & .518 & .021 & 0\\% \\\\\n\\midrule\nAll & 52 & .581 & — & 24\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Zero-shot transfer \\auroc{} across 52 languages (Qwen3). Pass rate = fraction exceeding 0.65 \\auroc{}.}\n\\label{tab:extended}\n\\end{table}\n\nTable~\\ref{tab:per_lang} provides per-language zero-shot transfer \\auroc{} on Qwen3 for the 19-language core set. The best transfer layer shifts shallower with decreasing resource level: layer 52 for zh/fr/de, layer 48 for es/ja/ko, down to layer 24 for Yoruba. This depth gradient motivates the Pareto frontier analysis.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}llccccc@{}}\n\\toprule\n\\textbf{Lang} & \\textbf{Tier} & \\textbf{Layer} & \\textbf{\\auroc{}} & \\textbf{Drop} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nzh & high & 52 & .668 & 7.4 & $-$.55 & .006 \\\\\nfr & high & 52 & .672 & 7.0 & $-$.51 & .011 \\\\\nde & high & 52 & .671 & 7.1 & $-$.48 & .017 \\\\\nes & high & 48 & .661 & 7.4 & $-$.42 & .041 \\\\\nja & high & 48 & .658 & 7.7 & $-$.37 & .075 \\\\\nko & high & 48 & .656 & 7.9 & $-$.33 & .115 \\\\\nru & high & 44 & .652 & 7.6 & $-$.25 & .239 \\\\\n\\midrule\npl & mid & 44 & .628 & 10.0 & $-$.14 & .513 \\\\\nar & mid & 40 & .625 & 9.6 & $-$.18 & .399 \\\\\nid & mid & 40 & .621 & 10.0 & $-$.02 & .926 \\\\\nhi & mid & 40 & .618 & 10.3 & $-$.11 & .609 \\\\\nuk & mid & 40 & .614 & 10.7 & $-$.06 & .782 \\\\\nvi & mid & 40 & .607 & 11.4 & .04 & .854 \\\\\nth & mid & 36 & .594 & 11.8 & .09 & .674 \\\\\n\\midrule\nbn & low & 28 & .553 & 14.1 & .14 & .514 \\\\\nte & low & 28 & .571 & 12.3 & .18 & .400 \\\\\nta & low & 28 & .568 & 12.6 & .22 & .303 \\\\\nsw & low & 28 & .537 & 15.7 & .27 & .202 \\\\\nyo & low & 24 & .512 & 19.9 & .31 & .141 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-language zero-shot transfer on Qwen3. Layer = best transfer layer; Drop = pp below English at same layer; $\\rho$ = Spearman correlation between depth and transfer \\auroc{}; $p$ = associated $p$-value.}\n\\label{tab:per_lang}\n\\end{table}\n\n\\subsection{Architecture-Dependent Pareto Frontier}\n\\label{sec:pareto}\n\nThe depth--transferability tradeoff is real but architecture-dependent. Table~\\ref{tab:arch_compare} summarizes across three architectures. The dense model (Gemma~4) shows the strongest frontier ($\\rho = -0.44$, sign consistency 0.68), followed by the large MoE (Qwen3: $\\rho = -0.38$, 0.63) and the smaller MoE (Llama~4: $\\rho = -0.18$, 0.53).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Type} & \\textbf{EN} & \\textbf{ZS} & \\textbf{$\\rho$} & \\textbf{Sign} \\\\\n\\midrule\nQwen3 & MoE & .776 & .618 & $-$.38 & .63 \\\\\nLlama4 & MoE & .749 & .588 & $-$.18 & .53 \\\\\nGemma4 & Dense & .761 & .605 & $-$.44 & .68 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Three-architecture comparison. EN = best English \\auroc{}; ZS = 19-lang mean zero-shot transfer; $\\rho$ = global Spearman; Sign = sign consistency of per-language $\\rho$.}\n\\label{tab:arch_compare}\n\\end{table}\n\nCross-architecture agreement is low: Kendall's $\\tau = 0.33$ between Qwen3 and Llama~4 for optimal layer rankings, and 0.42 between Qwen3 and Gemma~4. Practitioners cannot transfer layer selection findings from one model to another.\n\nOn Llama~4 Scout, the per-language Spearman $\\rho$ median is only $-0.12$ (range: $[-0.41, +0.48]$), with sign consistency at 0.53---essentially a coin flip. Non-monotonic jumps at layers 20--28 reflect MoE expert routing shifts. The Pareto frontier that exists on Qwen3 and Gemma~4 largely vanishes on Llama~4.\n\n\\subsection{Transfer Method Comparison}\n\\label{sec:methods}\n\nTable~\\ref{tab:methods} compares all transfer conditions across both primary models. Mean-shift produces exactly $\\Delta\\auroc{} = 0$ (as proven in \\S\\ref{sec:mean_shift}). CaCLR provides negligible improvement ($+0.5$pp on Qwen3, $+0.6$pp on Llama~4; Cohen's $d = 0.04$; permutation test $p = 0.71$). Linear projection offers modest gains ($+1.8$pp on Qwen3 with 50 parallel pairs). Few-shot with 100 labels is the strongest method ($+4.4$pp on Qwen3; $d = 0.58$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}lccccl@{}}\n\\toprule\n\\textbf{Method} & \\textbf{Q3} & \\textbf{L4} & \\textbf{$d$} & \\textbf{Labels} \\\\\n\\midrule\nZero-shot & .618 & .588 & — & 0 \\\\\nMean-shift & .618 & .588 & 0.00 & 0 \\\\\nCaCLR & .623 & .594 & 0.04 & 0 + parallel \\\\\nLinProj (50) & .636 & .608 & 0.24 & $\\sim$50 parallel \\\\\nFew-shot 25 & .644 & .617 & 0.35 & 25 target \\\\\nFew-shot 100 & .662 & .641 & 0.58 & 100 target \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Transfer method comparison (19-language mean \\auroc{}). Q3 = Qwen3; L4 = Llama~4; $d$ = Cohen's $d$ vs.\\ zero-shot.}\n\\label{tab:methods}\n\\end{table}\n\n\\subsection{CaCLR: A Principled Negative Result}\n\\label{sec:caclr}\n\nCaCLR's consistency loss ($\\beta \\cdot \\mathcal{L}_{\\text{consistency}}$) is inert. Table~\\ref{tab:caclr_ablation} shows the ablation: adding consistency to BCE+SB-ECE \\emph{reduces} \\auroc{} by 0.6pp. The $\\beta$ sweep over three orders of magnitude (0.001--1.0) produces $<$0.4pp variation (Table~\\ref{tab:beta_sweep}), ruling out a tuning failure.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Variant} & \\textbf{\\auroc{}} & \\textbf{$\\Delta$pp} \\\\\n\\midrule\nFull CaCLR & .621 & 0.0 \\\\\nBCE + SB-ECE & .627 & $+$0.6 \\\\\nBCE + Consistency & .611 & $-$1.0 \\\\\nBCE only ($\\approx$ zero-shot) & .618 & $-$0.3 \\\\\nLinear projection (ref.) & .636 & $+$1.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CaCLR ablation (Qwen3, 19-language mean). Removing consistency \\emph{improves} performance.}\n\\label{tab:caclr_ablation}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcclcc@{}}\n\\toprule\n$\\beta$ & \\textbf{\\auroc{}} & $\\Delta$pp & $\\beta$ & \\textbf{\\auroc{}} & $\\Delta$pp \\\\\n\\midrule\n0.0 & .627 & 0.0 & 0.05 & .623 & $-$0.4 \\\\\n0.001 & .626 & $-$0.1 & 0.1 & .621 & $-$0.6 \\\\\n0.01 & .625 & $-$0.2 & 0.5 & .618 & $-$0.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CaCLR $\\beta$ sensitivity (Qwen3, $\\alpha = 0.3$ fixed, 19-lang mean). Increasing $\\beta$ monotonically hurts.}\n\\label{tab:beta_sweep}\n\\end{table}\n\nThe mechanistic explanation: CKA analysis (\\S\\ref{sec:cka}) shows that cross-lingual misalignment at deeper layers is \\emph{geometric} (the correctness direction rotates across language subspaces), not merely distributional. MMD-based alignment cannot correct rotation, which is why linear projection (which learns the rotation) succeeds where CaCLR (which matches distributions) fails.\n\nCaCLR also fails on Gemma~4 Dense (mean \\auroc{} 0.609, $-0.9$pp vs.\\ linear projection), ruling out the hypothesis that MoE routing specifically caused the failure. On Belebele and MMLU-ProX, CaCLR underperforms linear projection by $-0.8$pp and $-1.1$pp respectively, confirming the negative result generalizes across benchmarks.\n\n\\subsection{Difficulty Decomposition: Inconclusive}\n\\label{sec:decomposition}\n\nThe IRT difficulty probe achieves $R^2 = 0.52$ in English (Qwen3) but transfers with degraded quality (9-language mean $R^2 = 0.38$). Projecting out the difficulty direction changes transfer \\auroc{} by $-0.5$pp on average---barely above the random-direction control ($-0.3$pp).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Q3} & \\textbf{$\\Delta$} & \\textbf{L4} & \\textbf{$\\Delta$} \\\\\n\\midrule\nFull activations & .618 & 0.0 & .588 & 0.0 \\\\\nResidual (diff.\\ out) & .613 & $-$0.5 & .583 & $-$0.5 \\\\\nDifficulty only & .569 & $-$4.9 & .548 & $-$4.0 \\\\\nRandom dir.\\ control & .615 & $-$0.3 & .585 & $-$0.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Decomposition ablation (9-language mean \\auroc{}). Difficulty removal marginally hurts, barely above random control.}\n\\label{tab:decomp}\n\\end{table}\n\nPer-language analysis shows no systematic pattern: 3/10 languages improve slightly ($+0.4$ to $+1.3$pp), 5/10 worsen ($-0.3$ to $-2.1$pp), 2/10 unchanged. The difficulty-shared component carries useful cross-lingual signal (questions hard in English tend to be hard everywhere); removing it strips away a genuine invariance. The cosine between difficulty and correctness directions ($0.36 \\pm 0.11$) confirms moderate entanglement, preventing clean separation.\n\n\\subsection{Cross-Lingual Orthogonality}\n\\label{sec:orthogonality}\n\nThe correctness--confidence orthogonality reported by Miao \\& Ungar \\shortcite{miao2026orthogonality} for English persists cross-lingually (overall mean cosine $= 0.074 \\pm 0.036$; 73\\% of languages below 0.10). However, a resource-tier gradient emerges: high-resource mean 0.052, mid-resource 0.073, low-resource 0.108 (Spearman $\\rho = -0.61$ with resource level). Yoruba on Llama~4 reaches 0.172, an outlier weakening the universality claim.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Tier} & \\textbf{$n$} & \\textbf{Qwen3} & \\textbf{Llama4} & \\textbf{Mean} \\\\\n\\midrule\nHigh & 8 & .048 & .056 & .052 \\\\\nMid & 7 & .066 & .075 & .073 \\\\\nLow & 5 & .100 & .122 & .108 \\\\\nAll & 20 & .069 & .079 & .074 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Correctness--confidence cosine similarity by resource tier. Lower = more orthogonal. Orthogonality persists but weakens for low-resource languages.}\n\\label{tab:orthogonality}\n\\end{table}\n\nThis confirms that output-based calibration faces a structural ceiling regardless of language, but this ceiling is noisier for low-resource languages where the model has less capacity to maintain the confidence--correctness dissociation.\n\n\\subsection{CKA Mechanistic Analysis}\n\\label{sec:cka}\n\nCKA between English and target-language activations declines with depth (shallow mean 0.89, deep mean 0.54), confirming that deeper layers are less cross-lingually aligned. However, the correlation between CKA and transfer \\auroc{} is weak: Pearson $r = 0.38$ on Qwen3, $r = 0.24$ on Llama~4, $r = 0.32$ combined.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Model} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{Sig.} & \\textbf{Total} \\\\\n\\midrule\nQwen3 & .38 & .002 & 5/19 & 19 \\\\\nLlama4 & .24 & .041 & 2/19 & 19 \\\\\nCombined & .32 & .001 & 7/38 & 38 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CKA vs.\\ transfer \\auroc{} correlation. Sig.\\ = languages with individually significant correlation.}\n\\label{tab:cka}\n\\end{table}\n\nA threshold analysis at CKA $= 0.35$ partially replicates: below this threshold, 61\\% of language-layer pairs show transfer collapse (\\auroc{} $< 0.55$), vs.\\ 22\\% above. But 39\\% of below-threshold pairs do not collapse, and the threshold is architecture-dependent. CKA provides a suggestive but not convincing mechanistic account.\n\nThe key qualitative insight survives: cross-lingual misalignment is geometric (correctness direction rotates), explaining why MMD-based CaCLR fails while linear projection succeeds. But the quantitative relationship is too noisy for reliable prediction.\n\n\\subsection{Linear Projection Data Requirements}\n\\label{sec:linproj}\n\nLinear projection improves with more parallel pairs but saturates around 100 (Table~\\ref{tab:linproj_pairs}). Critically, it fails for low-resource languages even at 200 pairs: Bengali +0.8pp, Swahili +0.6pp, Yoruba +0.6pp---within noise.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}rccc@{}}\n\\toprule\n\\textbf{$n$} & \\textbf{\\auroc{}} & \\textbf{$\\Delta$pp} & \\textbf{\\%~Improved} \\\\\n\\midrule\n10 & .608 & $-$1.0 & 26\\% \\\\\n20 & .621 & $+$0.3 & 42\\% \\\\\n50 & .636 & $+$1.8 & 55\\% \\\\\n100 & .643 & $+$2.5 & 63\\% \\\\\n200 & .647 & $+$2.9 & 68\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Linear projection \\auroc{} by number of parallel pairs (19-language mean). Saturates at $\\sim$100 pairs.}\n\\label{tab:linproj_pairs}\n\\end{table}\n\nHigh-resource languages benefit from as few as 20 pairs ($+3.1$pp at 50 pairs), while low-resource languages show minimal improvement regardless of parallel data quantity. The fundamental bottleneck is not the number of parallel pairs but the quality of cross-lingual activation alignment.\n\n\\subsection{Control Tasks: Capacity Artifacts}\n\\label{sec:control}\n\nControl tasks (probes trained on randomly permuted labels) reveal that probe \\auroc{} partially reflects capacity rather than genuine correctness signal. Table~\\ref{tab:control} shows selectivity by resource tier.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\n\\textbf{Tier} & \\textbf{$n$} & \\textbf{Probe} & \\textbf{Ctrl} & \\textbf{Sel.} & \\textbf{Min} \\\\\n\\midrule\nHigh & 7 & .660 & .548 & 17.2 & 10.4 \\\\\nMid & 7 & .614 & .546 & 13.8 & 8.2 \\\\\nLow & 5 & .548 & .544 & 8.4 & 4.8 \\\\\nAll & 19 & .618 & .546 & 13.8 & 4.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Control task selectivity (pp) by resource tier. Probe = real-label \\auroc{}; Ctrl = random-label \\auroc{}; Sel.\\ = selectivity (Probe $-$ Ctrl); Min = minimum selectivity in tier.}\n\\label{tab:control}\n\\end{table}\n\nFor low-resource languages, 28\\% of language-layer pairs have selectivity below 8pp. At the English-optimal layer, Swahili scores 0.508 (selectivity $-4.4$pp, \\emph{below} the random-label control) and Yoruba scores 0.487 ($-6.4$pp below control). These results are indistinguishable from probe memorization of random structure in high-dimensional activation spaces.\n\nThe selectivity depth gradient is positive (deeper layers have higher selectivity: 3.3pp at 0--25\\% depth, 9.5pp at 50--75\\%), reflecting that the correctness signal strengthens with depth while control \\auroc{} remains constant ($\\sim$0.55). This means shallow-layer transfer results for low-resource languages should be interpreted with particular caution.\n\n\\subsection{INT8 Quantization Validation}\n\\label{sec:int8}\n\nINT8 quantization introduces minimal distortion: mean $\\Delta\\auroc{} = -0.3$pp (max $-0.7$pp at layer 40), activation cosine similarity $= 0.994$, layer ranking correlation $= 0.98$. Quantization is not a confound.\n\n\\subsection{Cross-Benchmark Generalization}\n\nFindings partially generalize across benchmarks. On Belebele (natively multilingual reading comprehension), zero-shot transfer drops an additional 2.4pp vs.\\ GlobalMMLU, with language rankings largely preserved ($\\rho = 0.83$). On MMLU-ProX (machine-translated MMLU), the drop is 3.9pp with lower ranking stability ($\\rho = 0.69$), reflecting translation quality variation. CaCLR underperforms linear projection on both benchmarks ($-0.8$pp and $-1.1$pp respectively).\n\n%% ============================================================\n\\section{Analysis}\n\\label{sec:analysis}\n\n\\paragraph{Why does transfer fail for low-resource languages?}\nThree factors compound: (1) the model's internal representations for these languages are less structured, reducing the quality of the correctness signal at any depth; (2) the cross-lingual activation alignment (measured by CKA) degrades more steeply with depth for low-resource languages (CKA at 75\\% depth: sw $= 0.33$, yo $= 0.28$ vs.\\ fr $= 0.71$, zh $= 0.68$); (3) control tasks show that even the \\auroc{} metric itself is unreliable in these settings (selectivity $< 8$pp).\n\n\\paragraph{Why does CaCLR fail?}\nCaCLR's MMD-based consistency loss attempts to align activation \\emph{distributions} across languages. But the cross-lingual misalignment that matters for correctness probes is \\emph{geometric}: the correctness direction rotates across language subspaces at deeper layers. Distribution matching cannot correct rotation---it collapses both signal and noise. Linear projection directly estimates the rotation and therefore succeeds where CaCLR fails.\n\n\\paragraph{Practical guidance.}\nFor high-resource languages (en, zh, fr, de, es, ja, ko, ru): zero-shot transfer is viable with 7--8pp performance loss. Linear projection with $\\sim$50 parallel pairs recovers an additional 1--3pp. For mid-resource languages: few-shot with 25 target-language labels provides the best cost-performance tradeoff. For low-resource languages: the zero-label dream is closed. Few-shot with 100 labels is the minimum viable approach, and even then, results should be validated against control tasks to ensure genuine correctness signal.\n\n%% ============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe present the first systematic evaluation of cross-lingual correctness probe transfer, finding that the probe-based calibration research line does not generalize beyond a small set of high-resource languages without fundamental methodological advances. Mean-shift is provably inert under standard pipelines. The depth--transferability Pareto frontier is architecture-dependent, precluding universal layer selection. CaCLR---the natural distributional-matching approach---fails because cross-lingual misalignment is geometric, not distributional. Few-shot adaptation with 25--100 labels is the only viable path for the majority of the world's languages.\n\n\\paragraph{Limitations.}\nOur study is restricted to MCQA benchmarks. Open-ended generation may exhibit different calibration patterns. INT8 quantization, while validated, may interact differently with other probe architectures. The resource-tier taxonomy is coarse---individual language pairs may deviate based on typological proximity rather than resource level alone.\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "43d550c2-dcd5-40dd-acf5-9f19bb59758c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T201854 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direc…",
  "leafUuid": "cf1d9824-c79d-4ff4-9afd-e23dca2fc906",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated ML research paper with experiments",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135"
}
```

---

### Assistant

_source line 22 · 2026-05-20T20:57:34.694Z_

Now let me compile it. First I need to create a minimal bib file so LaTeX doesn't error out.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf1d9824-c79d-4ff4-9afd-e23dca2fc906",
  "isSidechain": false,
  "requestId": "req_011CbEVPFwLTvvyjy61Fzq97",
  "type": "assistant",
  "uuid": "53bc3e31-f1f4-4269-af2c-c5c9bec4d55a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DDuqAGwTZqCLfwjbET9pRY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11663,
      "cache_read_input_tokens": 58588,
      "output_tokens": 1064,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11663,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1064,
          "cache_read_input_tokens": 58588,
          "cache_creation_input_tokens": 11663,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11663
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

_source line 23 · 2026-05-20T20:57:49.365Z_

<details open><summary>🔧 Tool call — Write · `toolu_01CiFJ7DaUEyA7ALYmMeF1fe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/references.bib",
  "content": "@inproceedings{kadeethum2024calibration,\n  title={Calibration of Multilingual Large Language Models},\n  author={Kadeethum, Teeratorn and others},\n  booktitle={Findings of EMNLP},\n  year={2024}\n}\n\n@article{miao2026orthogonality,\n  title={Correctness and Confidence Are Orthogonal in {LLM} Representations},\n  author={Miao, Ning and Ungar, Lyle},\n  journal={arXiv preprint},\n  year={2026}\n}\n\n@inproceedings{miao2024coral,\n  title={{CORAL}: Benchmarking Multi-Model Correctness Assessment for Retrieval-Augmented Language Models},\n  author={Miao, Ning and others},\n  booktitle={NeurIPS},\n  year={2024}\n}\n\n@inproceedings{burns2023discovering,\n  title={Discovering Latent Knowledge in Language Models Without Supervision},\n  author={Burns, Collin and others},\n  booktitle={ICLR},\n  year={2023}\n}\n\n@inproceedings{xiao2025knowledge,\n  title={Cross-lingual Knowledge Boundary Probing},\n  author={Xiao, Yijun and others},\n  booktitle={ACL},\n  year={2025}\n}\n\n@inproceedings{liu2024confidence,\n  title={Confidence-Conditioned Prediction Sets for Neural Networks},\n  author={Liu, Xin and others},\n  booktitle={ICML},\n  year={2024}\n}\n\n@inproceedings{luo2024confidence,\n  title={The Confidence Manifold: Geometric Structure of Calibration Representations},\n  author={Luo, Haotian and others},\n  booktitle={NeurIPS},\n  year={2024}\n}\n\n@inproceedings{conneau2018muse,\n  title={Word Translation Without Parallel Data},\n  author={Conneau, Alexis and Lample, Guillaume and Ranzato, Marc'Aurelio and Denoyer, Ludovic and J{\\'e}gou, Herv{\\'e}},\n  booktitle={ICLR},\n  year={2018}\n}\n\n@inproceedings{artetxe2018vecmap,\n  title={A Robust Self-Learning Method for Fully Unsupervised Cross-Lingual Mappings of Word Embeddings},\n  author={Artetxe, Mikel and Labaka, Gorka and Agirre, Eneko},\n  booktitle={ACL},\n  year={2018}\n}\n\n@article{bendavid2010theory,\n  title={A Theory of Learning from Different Domains},\n  author={Ben-David, Shai and Blitzer, John and Crammer, Koby and Kulesza, Alex and Pereira, Fernando and Vaughan, Jennifer Wortman},\n  journal={Machine Learning},\n  volume={79},\n  pages={151--175},\n  year={2010}\n}\n\n@inproceedings{kornblith2019similarity,\n  title={Similarity of Neural Network Representations Revisited},\n  author={Kornblith, Simon and Norouzi, Mohammad and Lee, Honglak and Hinton, Geoffrey},\n  booktitle={ICML},\n  year={2019}\n}\n\n@inproceedings{hewitt2019control,\n  title={Designing and Interpreting Probes with Control Tasks},\n  author={Hewitt, John and Liang, Percy},\n  booktitle={EMNLP},\n  year={2019}\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53bc3e31-f1f4-4269-af2c-c5c9bec4d55a",
  "isSidechain": false,
  "requestId": "req_011CbEVPFwLTvvyjy61Fzq97",
  "type": "assistant",
  "uuid": "7fe76b19-2fcd-4ebf-8ee9-9f06dc574c5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DDuqAGwTZqCLfwjbET9pRY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11663,
      "cache_read_input_tokens": 58588,
      "output_tokens": 1064,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11663,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1064,
          "cache_read_input_tokens": 58588,
          "cache_creation_input_tokens": 11663,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11663
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

_source line 24 · 2026-05-20T20:57:49.374Z_

<details><summary>↩ Tool result · `toolu_01CiFJ7DaUEyA7ALYmMeF1fe`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7fe76b19-2fcd-4ebf-8ee9-9f06dc574c5d",
  "isSidechain": false,
  "promptId": "ce9c66bf-f5bc-46b5-95a4-aabc6b39fe73",
  "type": "user",
  "uuid": "d5d1a667-b727-4446-a6b9-3ced8e9eb1b7",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/references.bib",
    "content": "@inproceedings{kadeethum2024calibration,\n  title={Calibration of Multilingual Large Language Models},\n  author={Kadeethum, Teeratorn and others},\n  booktitle={Findings of EMNLP},\n  year={2024}\n}\n\n@article{miao2026orthogonality,\n  title={Correctness and Confidence Are Orthogonal in {LLM} Representations},\n  author={Miao, Ning and Ungar, Lyle},\n  journal={arXiv preprint},\n  year={2026}\n}\n\n@inproceedings{miao2024coral,\n  title={{CORAL}: Benchmarking Multi-Model Correctness Assessment for Retrieval-Augmented Language Models},\n  author={Miao, Ning and others},\n  booktitle={NeurIPS},\n  year={2024}\n}\n\n@inproceedings{burns2023discovering,\n  title={Discovering Latent Knowledge in Language Models Without Supervision},\n  author={Burns, Collin and others},\n  booktitle={ICLR},\n  year={2023}\n}\n\n@inproceedings{xiao2025knowledge,\n  title={Cross-lingual Knowledge Boundary Probing},\n  author={Xiao, Yijun and others},\n  booktitle={ACL},\n  year={2025}\n}\n\n@inproceedings{liu2024confidence,\n  title={Confidence-Conditioned Prediction Sets for Neural Networks},\n  author={Liu, Xin and others},\n  booktitle={ICML},\n  year={2024}\n}\n\n@inproceedings{luo2024confidence,\n  title={The Confidence Manifold: Geometric Structure of Calibration Representations},\n  author={Luo, Haotian and others},\n  booktitle={NeurIPS},\n  year={2024}\n}\n\n@inproceedings{conneau2018muse,\n  title={Word Translation Without Parallel Data},\n  author={Conneau, Alexis and Lample, Guillaume and Ranzato, Marc'Aurelio and Denoyer, Ludovic and J{\\'e}gou, Herv{\\'e}},\n  booktitle={ICLR},\n  year={2018}\n}\n\n@inproceedings{artetxe2018vecmap,\n  title={A Robust Self-Learning Method for Fully Unsupervised Cross-Lingual Mappings of Word Embeddings},\n  author={Artetxe, Mikel and Labaka, Gorka and Agirre, Eneko},\n  booktitle={ACL},\n  year={2018}\n}\n\n@article{bendavid2010theory,\n  title={A Theory of Learning from Different Domains},\n  author={Ben-David, Shai and Blitzer, John and Crammer, Koby and Kulesza, Alex and Pereira, Fernando and Vaughan, Jennifer Wortman},\n  journal={Machine Learning},\n  volume={79},\n  pages={151--175},\n  year={2010}\n}\n\n@inproceedings{kornblith2019similarity,\n  title={Similarity of Neural Network Representations Revisited},\n  author={Kornblith, Simon and Norouzi, Mohammad and Lee, Honglak and Hinton, Geoffrey},\n  booktitle={ICML},\n  year={2019}\n}\n\n@inproceedings{hewitt2019control,\n  title={Designing and Interpreting Probes with Control Tasks},\n  author={Hewitt, John and Liang, Percy},\n  booktitle={EMNLP},\n  year={2019}\n}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "7fe76b19-2fcd-4ebf-8ee9-9f06dc574c5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T20:57:52.941Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014N2cVfcqpq7WCdbz1SqdNd`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "First pdflatex pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5d1a667-b727-4446-a6b9-3ced8e9eb1b7",
  "isSidechain": false,
  "requestId": "req_011CbEVQc4qG5btg6QfY7tcJ",
  "type": "assistant",
  "uuid": "817736be-3111-4a24-b09a-bcfb0b4a10e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0196wUM9R4KnqdF6LejsZj1u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 70251,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1132,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 144,
          "cache_read_input_tokens": 70251,
          "cache_creation_input_tokens": 1132,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1132
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

_source line 26 · 2026-05-20T20:57:53.089Z_

<details><summary>↩ Tool result · `toolu_014N2cVfcqpq7WCdbz1SqdNd`</summary>

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
  "parentUuid": "817736be-3111-4a24-b09a-bcfb0b4a10e9",
  "isSidechain": false,
  "promptId": "ce9c66bf-f5bc-46b5-95a4-aabc6b39fe73",
  "type": "user",
  "uuid": "c8fb4a48-2f73-44d8-a669-ad7f7ce95829",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `acl.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "817736be-3111-4a24-b09a-bcfb0b4a10e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-20T20:57:57.024Z_

<details><summary>Logged reasoning block</summary>

```text
The acl.sty file is not available. Let me switch to a simpler document class that's available, or find the ACL style file. Let me just use a standard article class with appropriate formatting.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8fb4a48-2f73-44d8-a669-ad7f7ce95829",
  "isSidechain": false,
  "requestId": "req_011CbEVQswZYqUE2P7vJdFwV",
  "type": "assistant",
  "uuid": "005d0e90-414a-4e1b-a88b-5a8145af1d50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017yK7xdSdimhnHJjLyef68B",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 425,
      "cache_read_input_tokens": 71383,
      "output_tokens": 494,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 425,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 494,
          "cache_read_input_tokens": 71383,
          "cache_creation_input_tokens": 425,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 425
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

_source line 28 · 2026-05-20T20:57:57.540Z_

ACL style not installed. Let me switch to a standard article class.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "005d0e90-414a-4e1b-a88b-5a8145af1d50",
  "isSidechain": false,
  "requestId": "req_011CbEVQswZYqUE2P7vJdFwV",
  "type": "assistant",
  "uuid": "ada4d7ca-9f82-40c4-8a1b-793402464e43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017yK7xdSdimhnHJjLyef68B",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 425,
      "cache_read_input_tokens": 71383,
      "output_tokens": 494,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 425,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 494,
          "cache_read_input_tokens": 71383,
          "cache_creation_input_tokens": 425,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 425
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

_source line 29 · 2026-05-20T20:58:01.170Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01NTAGRoBc4Sssd13WkbtSBF`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/paper.tex",
  "old_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{microtype}\n\\usepackage{url}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{amsthm}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{microtype}\n\\usepackage{hyperref}\n\\usepackage{url}\n\\usepackage{natbib}\n\\newtheorem{theorem}{Theorem}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ada4d7ca-9f82-40c4-8a1b-793402464e43",
  "isSidechain": false,
  "requestId": "req_011CbEVQswZYqUE2P7vJdFwV",
  "type": "assistant",
  "uuid": "7b207676-8ede-46f2-adc9-8e7f7ab58b6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017yK7xdSdimhnHJjLyef68B",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 425,
      "cache_read_input_tokens": 71383,
      "output_tokens": 494,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 425,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 494,
          "cache_read_input_tokens": 71383,
          "cache_creation_input_tokens": 425,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 425
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

_source line 30 · 2026-05-20T20:58:01.198Z_

<details><summary>↩ Tool result · `toolu_01NTAGRoBc4Sssd13WkbtSBF`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b207676-8ede-46f2-adc9-8e7f7ab58b6d",
  "isSidechain": false,
  "promptId": "ce9c66bf-f5bc-46b5-95a4-aabc6b39fe73",
  "type": "user",
  "uuid": "6c4c4ecb-5e1c-40ec-b723-58d8eedcb435",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/paper.tex",
    "oldString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{microtype}\n\\usepackage{url}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{amsthm}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{microtype}\n\\usepackage{hyperref}\n\\usepackage{url}\n\\usepackage{natbib}\n\\newtheorem{theorem}{Theorem}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 15,
        "newStart": 1,
        "newLines": 19,
        "lines": [
          " \\documentclass[11pt,a4paper]{article}",
          "-\\usepackage[hyperref]{acl}",
          "+\\usepackage[margin=2.5cm]{geometry}",
          " \\usepackage{times}",
          " \\usepackage{latexsym}",
          " \\usepackage{graphicx}",
          " \\usepackage{amsmath}",
          " \\usepackage{amssymb}",
          "+\\usepackage{amsthm}",
          " \\usepackage{booktabs}",
          " \\usepackage{multirow}",
          " \\usepackage{xcolor}",
          " \\usepackage{microtype}",
          "+\\usepackage{hyperref}",
          " \\usepackage{url}",
          "+\\usepackage{natbib}",
          "+\\newtheorem{theorem}{Theorem}",
          " ",
          " \\newcommand{\\auroc}{\\textsc{auroc}}",
          " \\newcommand{\\ece}{\\textsc{ece}}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "7b207676-8ede-46f2-adc9-8e7f7ab58b6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-20T20:58:01.205Z_

```json
{
  "parentUuid": "6c4c4ecb-5e1c-40ec-b723-58d8eedcb435",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "9ff38f80-03e0-4921-8106-7cdbdf654591",
  "timestamp": "2026-05-20T20:58:01.205Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 32 · 2026-05-20T20:58:04.535Z_

Also need to remove the `\shortcite` commands since we're not using ACL natbib, and fix the bibliography command.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ff38f80-03e0-4921-8106-7cdbdf654591",
  "isSidechain": false,
  "requestId": "req_011CbEVRUnos2x93uW1MNcfe",
  "type": "assistant",
  "uuid": "edbca963-6f86-47d0-ac91-5f2fda5a95a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SZXxJM6bRy7jVf6GxzmwG4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 685,
      "cache_read_input_tokens": 71808,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 685,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 71808,
          "cache_creation_input_tokens": 685,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 685
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

_source line 33 · 2026-05-20T20:58:05.722Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01XARcW99dZgDMSKk6s1jwZe`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/paper.tex",
  "old_string": "\\shortcite",
  "new_string": "\\cite"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "edbca963-6f86-47d0-ac91-5f2fda5a95a4",
  "isSidechain": false,
  "requestId": "req_011CbEVRUnos2x93uW1MNcfe",
  "type": "assistant",
  "uuid": "3487ca6d-e33c-4d39-acf9-cbff6caf128f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SZXxJM6bRy7jVf6GxzmwG4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 685,
      "cache_read_input_tokens": 71808,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 685,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 71808,
          "cache_creation_input_tokens": 685,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 685
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

_source line 34 · 2026-05-20T20:58:05.734Z_

<details><summary>↩ Tool result · `toolu_01XARcW99dZgDMSKk6s1jwZe`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/paper.tex has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3487ca6d-e33c-4d39-acf9-cbff6caf128f",
  "isSidechain": false,
  "promptId": "ce9c66bf-f5bc-46b5-95a4-aabc6b39fe73",
  "type": "user",
  "uuid": "fff7a86d-e740-4290-8f54-349c53e3ac75",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/paper.tex",
    "oldString": "\\shortcite",
    "newString": "\\cite",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 37,
        "oldLines": 7,
        "newStart": 37,
        "newLines": 7,
        "lines": [
          " ",
          " A promising alternative is \\emph{probe-based calibration}, which trains lightweight classifiers on internal activations to predict whether the model's answer is correct \\cite{miao2024coral,burns2023discovering}. This approach has shown strong results in English, with recent work demonstrating cross-task transfer \\cite{miao2024coral}, confidence manifold structure \\cite{luo2024confidence}, and the potential for representation-level steering \\cite{miao2026orthogonality}. However, all of this work is English-only.",
          " ",
          "-The natural question---\\emph{do English correctness probes transfer to other languages?}---has not been systematically investigated. Xiao et al.\\ \\shortcite{xiao2025knowledge} transferred \\emph{knowledge-boundary} probes (input-level answerability) across 8 languages, but knowledge boundaries are fundamentally different from correctness signals: the former encodes whether the model has seen relevant training data, while the latter depends on the model's output for a specific question. Their partial success does not predict ours.",
          "+The natural question---\\emph{do English correctness probes transfer to other languages?}---has not been systematically investigated. Xiao et al.\\ \\cite{xiao2025knowledge} transferred \\emph{knowledge-boundary} probes (input-level answerability) across 8 languages, but knowledge boundaries are fundamentally different from correctness signals: the former encodes whether the model has seen relevant training data, while the latter depends on the model's output for a specific question. Their partial success does not predict ours.",
          " ",
          " We present a systematic investigation across 3 architectures (Qwen3-235B-A22B, Llama~4 Scout, Gemma~4 31B Dense), up to 52 languages spanning 15 language families, and 5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot, CaCLR). Our study yields three surviving contributions:",
          " "
        ]
      },
      {
        "oldStart": 54,
        "oldLines": 22,
        "newStart": 54,
        "newLines": 22,
        "lines": [
          " \\label{sec:related}",
          " ",
          " \\paragraph{Probe-based calibration.}",
          "-CORAL \\cite{miao2024coral} demonstrated cross-task correctness probe transfer in English; CCPS \\cite{liu2024confidence} and the Confidence Manifold \\cite{luo2024confidence} explored structural properties of correctness representations. Miao \\& Ungar \\shortcite{miao2026orthogonality} discovered that correctness and verbalized confidence directions are orthogonal in English, motivating representation-level intervention. All are English-only.",
          "+CORAL \\cite{miao2024coral} demonstrated cross-task correctness probe transfer in English; CCPS \\cite{liu2024confidence} and the Confidence Manifold \\cite{luo2024confidence} explored structural properties of correctness representations. Miao \\& Ungar \\cite{miao2026orthogonality} discovered that correctness and verbalized confidence directions are orthogonal in English, motivating representation-level intervention. All are English-only.",
          " ",
          " \\paragraph{Cross-lingual probing.}",
          "-Xiao et al.\\ \\shortcite{xiao2025knowledge} transferred knowledge-boundary probes across 8 languages using mean-shift adaptation, reporting partial success. Their target---input-level answerability---differs fundamentally from output-dependent correctness. We analyze this difference and explain why their mean-shift succeeds under accuracy metrics but produces $\\Delta\\auroc{} \\equiv 0$ in our pipeline (\\S\\ref{sec:mean_shift}). Civelli et al.\\ transferred difficulty probes cross-lingually; we use their methodology as a control in our decomposition analysis.",
          "+Xiao et al.\\ \\cite{xiao2025knowledge} transferred knowledge-boundary probes across 8 languages using mean-shift adaptation, reporting partial success. Their target---input-level answerability---differs fundamentally from output-dependent correctness. We analyze this difference and explain why their mean-shift succeeds under accuracy metrics but produces $\\Delta\\auroc{} \\equiv 0$ in our pipeline (\\S\\ref{sec:mean_shift}). Civelli et al.\\ transferred difficulty probes cross-lingually; we use their methodology as a control in our decomposition analysis.",
          " ",
          " \\paragraph{Cross-lingual alignment.}",
          " MUSE \\cite{conneau2018muse} and VecMap \\cite{artetxe2018vecmap} demonstrated that cross-lingual word embedding spaces are approximately related by linear transformations. Our linear projection baseline is motivated by this literature; CaCLR's failure despite distributional matching is the novel finding.",
          " ",
          " \\paragraph{Domain adaptation theory.}",
          "-Ben-David et al.\\ \\shortcite{bendavid2010theory} provide the $\\mathcal{H}$-divergence framework predicting that transfer degrades with distributional distance. Our resource-tier gradient is consistent with this theory; the novel findings are that the Pareto frontier shape is architecture-dependent (not predicted by theory) and that distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.",
          "+Ben-David et al.\\ \\cite{bendavid2010theory} provide the $\\mathcal{H}$-divergence framework predicting that transfer degrades with distributional distance. Our resource-tier gradient is consistent with this theory; the novel findings are that the Pareto frontier shape is architecture-dependent (not predicted by theory) and that distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.",
          " ",
          " \\paragraph{Representation similarity.}",
          " CKA \\cite{kornblith2019similarity} measures representational similarity between neural network layers. We use CKA to provide mechanistic context for cross-lingual transfer patterns, though the correlation with transfer success is weaker than anticipated.",
          " ",
          " \\paragraph{Probing methodology.}",
          "-Hewitt \\& Liang \\shortcite{hewitt2019control} proposed control tasks to measure probe selectivity---the gap between real and random-label probe performance. We adopt their methodology and find that low-resource selectivity is dangerously low, qualifying our results.",
          "+Hewitt \\& Liang \\cite{hewitt2019control} proposed control tasks to measure probe selectivity---the gap between real and random-label probe performance. We adopt their methodology and find that low-resource selectivity is dangerously low, qualifying our results.",
          " ",
          " %% ============================================================",
          " \\section{Method}"
        ]
      },
      {
        "oldStart": 376,
        "oldLines": 7,
        "newStart": 376,
        "newLines": 7,
        "lines": [
          " \\subsection{Cross-Lingual Orthogonality}",
          " \\label{sec:orthogonality}",
          " ",
          "-The correctness--confidence orthogonality reported by Miao \\& Ungar \\shortcite{miao2026orthogonality} for English persists cross-lingually (overall mean cosine $= 0.074 \\pm 0.036$; 73\\% of languages below 0.10). However, a resource-tier gradient emerges: high-resource mean 0.052, mid-resource 0.073, low-resource 0.108 (Spearman $\\rho = -0.61$ with resource level). Yoruba on Llama~4 reaches 0.172, an outlier weakening the universality claim.",
          "+The correctness--confidence orthogonality reported by Miao \\& Ungar \\cite{miao2026orthogonality} for English persists cross-lingually (overall mean cosine $= 0.074 \\pm 0.036$; 73\\% of languages below 0.10). However, a resource-tier gradient emerges: high-resource mean 0.052, mid-resource 0.073, low-resource 0.108 (Spearman $\\rho = -0.61$ with resource level). Yoruba on Llama~4 reaches 0.172, an outlier weakening the universality claim.",
          " ",
          " \\begin{table}[t]",
          " \\centering"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  },
  "sourceToolAssistantUUID": "3487ca6d-e33c-4d39-acf9-cbff6caf128f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T201854 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direc…",
  "leafUuid": "fff7a86d-e740-4290-8f54-349c53e3ac75",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated ML research paper with experiments",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135"
}
```

---

### Tool call

_source line 37 · 2026-05-20T20:58:09.790Z_

<details open><summary>🔧 Tool call — Edit · `toolu_018vSBdjaZeZU39MAUW2249c`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/paper.tex",
  "old_string": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}",
  "new_string": "\\bibliographystyle{plainnat}\n\\bibliography{references}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fff7a86d-e740-4290-8f54-349c53e3ac75",
  "isSidechain": false,
  "requestId": "req_011CbEVRpB81bL3ckRWMshwo",
  "type": "assistant",
  "uuid": "a41b05f3-faf7-453f-bcda-933f9a9e4c7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ACSyr3Ny3GKifEvUh21F9e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 268,
      "cache_read_input_tokens": 72493,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 268,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 170,
          "cache_read_input_tokens": 72493,
          "cache_creation_input_tokens": 268,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 268
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

_source line 38 · 2026-05-20T20:58:09.808Z_

<details><summary>↩ Tool result · `toolu_018vSBdjaZeZU39MAUW2249c`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a41b05f3-faf7-453f-bcda-933f9a9e4c7d",
  "isSidechain": false,
  "promptId": "ce9c66bf-f5bc-46b5-95a4-aabc6b39fe73",
  "type": "user",
  "uuid": "9b9adc44-18f3-42f3-967f-5d26f7de0622",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst/paper.tex",
    "oldString": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}",
    "newString": "\\bibliographystyle{plainnat}\n\\bibliography{references}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 504,
        "oldLines": 7,
        "newStart": 504,
        "newLines": 7,
        "lines": [
          " \\paragraph{Limitations.}",
          " Our study is restricted to MCQA benchmarks. Open-ended generation may exhibit different calibration patterns. INT8 quantization, while validated, may interact differently with other probe architectures. The resource-tier taxonomy is coarse---individual language pairs may deviate based on typological proximity rather than resource level alone.",
          " ",
          "+\\bibliographystyle{plainnat}",
          " \\bibliography{references}",
          "-\\bibliographystyle{acl_natbib}",
          " ",
          " \\end{document}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "a41b05f3-faf7-453f-bcda-933f9a9e4c7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T20:58:17.644Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Ei256YzhEk6vjm3FHvGKtY`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20 && bibtex paper 2>&1 | tail -10 && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5 && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5",
  "description": "Compile LaTeX with bibtex (3 passes)",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b9adc44-18f3-42f3-967f-5d26f7de0622",
  "isSidechain": false,
  "requestId": "req_011CbEVS83QpYEqo3shzSGE2",
  "type": "assistant",
  "uuid": "29104568-ca2d-4b4f-a661-4552b2654f4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019aSQ2nVUMcaxK1Yunms5gN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 257,
      "cache_read_input_tokens": 72761,
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
          "cache_read_input_tokens": 72761,
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

_source line 40 · 2026-05-20T20:58:19.467Z_

<details><summary>↩ Tool result · `toolu_01Ei256YzhEk6vjm3FHvGKtY`</summary>

```text
Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/us
r/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist
/fonts/type1/public/amsfonts/cm/cmmib10.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symb
ols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>
&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (11 pages, 187242 bytes).
Transcript written on paper.log.
This is BibTeX, Version 0.99d (TeX Live 2025/Debian)
The top-level auxiliary file: paper.aux
The style file: plainnat.bst
Database file #1: references.bib
bols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb
>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (11 pages, 193135 bytes).
Transcript written on paper.log.
>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (11 pages, 194780 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29104568-ca2d-4b4f-a661-4552b2654f4c",
  "isSidechain": false,
  "promptId": "ce9c66bf-f5bc-46b5-95a4-aabc6b39fe73",
  "type": "user",
  "uuid": "55a14b69-ea7b-40b3-a368-6951831e0d16",
  "toolUseResult": {
    "stdout": "Package rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/us\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist\n/fonts/type1/public/amsfonts/cm/cmmib10.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symb\nols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (11 pages, 187242 bytes).\nTranscript written on paper.log.\nThis is BibTeX, Version 0.99d (TeX Live 2025/Debian)\nThe top-level auxiliary file: paper.aux\nThe style file: plainnat.bst\nDatabase file #1: references.bib\nbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb\n>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/te\nxlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (11 pages, 193135 bytes).\nTranscript written on paper.log.\n>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/te\nxlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (11 pages, 194780 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "29104568-ca2d-4b4f-a661-4552b2654f4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-20T20:58:32.684Z_

编译成功，生成 11 页 PDF。

`paper.tex` 已写入 `worst/` 目录并编译为 `paper.pdf`（11 页）。论文覆盖了 `experiment_data.json` 中全部 11 个实验：

- **Table 1**: 英文探针各层性能（3 架构）
- **Table 2**: 资源层级分类（19 语言 + 52 语言扩展）
- **Table 3**: 逐语言零样本迁移（含 Spearman ρ 和 p 值）
- **Table 4**: 三架构 Pareto 前沿对比
- **Table 5**: 迁移方法全面对比（含 Cohen's d）
- **Table 6–7**: CaCLR 消融 + β 敏感性
- **Table 8**: 难度分解消融
- **Table 9**: 正交性（资源层级）
- **Table 10**: CKA 相关性
- **Table 11**: 线性投影数据需求
- **Table 12**: 控制任务选择性

三个核心贡献：(1) mean-shift 秩不变性定理；(2) 资源层级迁移分类法；(3) few-shot 25–100 是唯一可行路径。CaCLR 作为失败负面结果报告，分解不确定，Pareto 前沿依赖架构。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55a14b69-ea7b-40b3-a368-6951831e0d16",
  "isSidechain": false,
  "requestId": "req_011CbEVSppMHr4QE8V1ypHdp",
  "type": "assistant",
  "uuid": "e814018f-ad03-43df-b74d-890c22c4e19d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/worst",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KapmNSaK1mcGE5LXvj9EUD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1106,
      "cache_read_input_tokens": 73018,
      "output_tokens": 403,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1106,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 403,
          "cache_read_input_tokens": 73018,
          "cache_creation_input_tokens": 1106,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1106
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

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T201854 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direc…",
  "leafUuid": "e814018f-ad03-43df-b74d-890c22c4e19d",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated ML research paper with experiments",
  "sessionId": "5686fd8c-ab8d-4a40-ad31-d7215e789135"
}
```

---
