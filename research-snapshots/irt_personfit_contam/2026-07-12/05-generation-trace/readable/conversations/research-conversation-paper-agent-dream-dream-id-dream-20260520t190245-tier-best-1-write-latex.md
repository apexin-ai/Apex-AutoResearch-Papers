# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T190245 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 69
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-3/f4e042fb-0a90-4bbe-8eb1-3013bf130d8d.jsonl`
- **Structured JSON:** [`f35f95e7fd24765e7bb8.json`](../../sessions/f3/f35f95e7fd24765e7bb8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T19:22:24.462Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T19:22:24.462Z",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T190245 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best/experiment_data.json`（先 Read 此文件）\n- Venue：emnlp-2026\n- Narrative guidance：原始 framing 完全成立。IRT-FIT 是 minimal-information operating point 上的有效检测框架： 跨 4 个模型家族一致检测、post-RL robust、在实际关键的低污染率下无需标注数据即胜过 supervised baselines。 三条 claims 无需调整——Claim 1 的 \"principled framework\" 有 ctrl-contam 全面验证， Claim 2 的 power function 有 multi-benchmark 实证确认，Claim 3 的 empirical findings 加入 ctrl-contam 的跨模型 memorization 量化。θ-shift 作为 methodological contribution 而非 limitation。 Headline: \"binary response patterns alone detect SFT contamination across model families, even after RL post-training.\"\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T19:22:24.465Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T19:22:24.465Z",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d"
}
```

---

## Round 1

67 recorded events

### User

_source line 3 · 2026-05-20T19:22:24.484Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T190245 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best/experiment_data.json`（先 Read 此文件）
- Venue：emnlp-2026
- Narrative guidance：原始 framing 完全成立。IRT-FIT 是 minimal-information operating point 上的有效检测框架： 跨 4 个模型家族一致检测、post-RL robust、在实际关键的低污染率下无需标注数据即胜过 supervised baselines。 三条 claims 无需调整——Claim 1 的 "principled framework" 有 ctrl-contam 全面验证， Claim 2 的 power function 有 multi-benchmark 实证确认，Claim 3 的 empirical findings 加入 ctrl-contam 的跨模型 memorization 量化。θ-shift 作为 methodological contribution 而非 limitation。 Headline: "binary response patterns alone detect SFT contamination across model families, even after RL post-training."

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "eb66b833-472c-4a64-b5b3-e6647c252907",
  "type": "user",
  "uuid": "d3a3069c-28e8-4603-837a-e1b0007a5fc1",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T19:22:24.483Z_

```json
{
  "parentUuid": "d3a3069c-28e8-4603-837a-e1b0007a5fc1",
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
  "uuid": "8637e777-51db-4c2a-b957-f15c8c3eda45",
  "timestamp": "2026-05-20T19:22:24.483Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T19:22:24.483Z_

```json
{
  "parentUuid": "8637e777-51db-4c2a-b957-f15c8c3eda45",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "01b0b802-5631-4eff-a241-dc7d5b633e55",
  "timestamp": "2026-05-20T19:22:24.483Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
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
  "aiTitle": "Generate IRT contamination detection paper",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d"
}
```

---

### Assistant

_source line 7 · 2026-05-20T19:22:26.865Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01b0b802-5631-4eff-a241-dc7d5b633e55",
  "isSidechain": false,
  "requestId": "req_011CbEN8bteioiSyixXvt3pg",
  "type": "assistant",
  "uuid": "ee01bfdb-7662-44ae-96ba-72adf6100568",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019mdghCbRbVRYKWQmm1TEcj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11765,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11765,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11765,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11765
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

_source line 8 · 2026-05-20T19:22:27.827Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NKQS32rrpnEDDHuqab2xeT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee01bfdb-7662-44ae-96ba-72adf6100568",
  "isSidechain": false,
  "requestId": "req_011CbEN8bteioiSyixXvt3pg",
  "type": "assistant",
  "uuid": "c22630af-1a38-47d4-8e10-f4019fda80b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019mdghCbRbVRYKWQmm1TEcj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11765,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11765,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11765,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11765
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

_source line 9 · 2026-05-20T19:22:28.198Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JxWdFwFH6hRNN4Rw4nXYFj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c22630af-1a38-47d4-8e10-f4019fda80b9",
  "isSidechain": false,
  "requestId": "req_011CbEN8bteioiSyixXvt3pg",
  "type": "assistant",
  "uuid": "60999672-183f-459d-8674-1c2cdd67dbe1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019mdghCbRbVRYKWQmm1TEcj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11765,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11765,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11765,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11765
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

_source line 10 · 2026-05-20T19:22:28.208Z_

<details><summary>↩ Tool result · `toolu_01NKQS32rrpnEDDHuqab2xeT`</summary>

```text
1	[
2	  {
3	    "name": "Controlled Contamination Pilot (Qwen3.5-9B)",
4	    "description": "Qwen3.5-9B × 4 conditions (0%-seed1/0%-seed2/15%/50%) × MMLU。 验证 Δlz* 显著性、clean-vs-clean noise floor、seen/unseen memorization fraction。\n",
5	    "results": {
6	      "clean_s1_lz_star": 7.2,
7	      "clean_s2_lz_star": 6.8,
8	      "clean_delta_lz": 0.4,
9	      "clean_delta_nonsig": true,
10	      "contam_15_lz_star_free": 2.8,
11	      "contam_15_delta_lz_free": -4.1,
12	      "contam_15_cohens_d": -3.95,
13	      "contam_50_lz_star_free": 4.9,
14	      "contam_50_delta_lz_free": -2.0,
15	      "contam_15_lz_star_fixed": 10.5,
16	      "contam_50_lz_star_fixed": 16.8,
17	      "theta_fixed_delta_15": 3.5,
18	      "theta_fixed_delta_50": 9.8,
19	      "theta_fixed_ratio": 2.8,
20	      "accuracy_clean": 0.71,
21	      "accuracy_contam_15": 0.76,
22	      "accuracy_contam_50": 0.8,
23	      "accuracy_contam_15_seen": 0.86,
24	      "accuracy_contam_15_unseen": 0.73,
25	      "memorization_fraction_15": 0.42,
26	      "memorization_fraction_50": 0.31,
27	      "theta_shift_clean": -0.08,
28	      "theta_shift_contam_15": 0.22,
29	      "theta_shift_contam_50": 0.41
30	    },
31	    "tables": [
32	      {
33	        "name": "Table: Qwen3.5-9B Pilot Results",
34	        "columns": [
35	          "condition",
36	          "accuracy",
37	          "lz_star_free",
38	          "lz_star_fixed",
39	          "theta_MLE",
40	          "delta_lz_free",
41	          "delta_lz_fixed"
42	        ],
43	        "rows": [
44	          [
45	            "clean_s1",
46	            0.71,
47	            7.2,
48	            7.2,
49	            -0.08,
50	            "—",
51	            "—"
52	          ],
53	          [
54	            "clean_s2",
55	            0.71,
56	            6.8,
57	            6.8,
58	            -0.09,
59	            0.4,
60	            0.4
61	          ],
62	          [
63	            "contam_15",
64	            0.76,
65	            2.8,
66	            10.5,
67	            0.22,
68	            -4.1,
69	            3.5
70	          ],
71	          [
72	            "contam_50",
73	            0.8,
74	            4.9,
75	            16.8,
76	            0.41,
77	            -2.0,
78	            9.8
79	          ]
80	        ]
81	      }
82	    ],
83	    "figures": [],
84	    "analysis": "Go/no-go 信号明确通过。|d|=3.95 远超 0.8 的 large effect 阈值。θ-fixed 恢复单调 dose-response (ratio=2.80∈[2.5,4.0])，确认 θ-shift 是唯一导致 free-θ 非单调的机制。 memorization_fraction=0.42 意味着理论 power 的 ~42% 可在实际中实现——MMLU 15% 理论 power 98.5% × 0.42 = adjusted power ≈41%，但 lz* 检测的是 aggregate pattern 而非逐 item 检测， 所以 aggregate Δlz* 仍然产生 |d|≈4 的强效应。\n\n\nQwen3.5-9B 作为较新架构（含 thinking 能力），SFT memorization 效率略高于 Qwen2.5-7B。 15% 污染产生强信号（|d|≈4.0）是因为 QLoRA 在小比例 seen items 上产生明确的 aberrant pattern： 模型在高难度 seen items 上异常正确，而在 unseen items 上保持原有错误模式。memorization_fraction≈0.42 说明 ~42% 的 seen items 被完全记忆（产生 aberrant response），剩余 58% 产生了泛化而非逐字记忆。 θ-shift 机制与 pilot 一致：污染提升整体能力估计，θ_MLE 上升吸收了部分 aberrance signal， θ-fixed 恢复单调性。clean-vs-clean Δ≈0.4 确认 noise floor 远低于检测阈值。\n"
85	  },
86	  {
87	    "name": "Full Multi-Model Controlled Contamination",
88	    "description": "4 模型 (Qwen3.5-9B, Gemma-4-31B, Llama-3.1-8B, Mistral-7B-v0.3) × 6 contamination levels (0/5/10/15/25/50%) × 3 benchmarks (MMLU, GSM8K, HellaSwag)。\n",
89	    "results": {
90	      "cohens_d_15pct_mmlu": {
91	        "qwen3.5-9b": -3.95,
92	        "gemma-4-31b": -4.52,
93	        "llama-3.1-8b": -2.85,
94	        "mistral-7b-v0.3": -2.42
95	      },
96	      "cohens_d_15pct_mean": 3.44,
97	      "cohens_d_15pct_min": 2.42,
98	      "models_significant_at_15pct": 4,
99	      "benchmarks_significant_per_model": {
100	        "qwen3.5-9b": 3,
101	        "gemma-4-31b": 3,
102	        "llama-3.1-8b": 2,
103	        "mistral-7b-v0.3": 2
104	      },
105	      "gsm8k_cohens_d_15pct": {
106	        "qwen3.5-9b": -1.42,
107	        "gemma-4-31b": -1.68,
108	        "llama-3.1-8b": -0.91,
109	        "mistral-7b-v0.3": -0.85
110	      },
111	      "gsm8k_all_above_0.8": true,
112	      "memorization_fraction_15pct": {
113	        "qwen3.5-9b": 0.42,
114	        "gemma-4-31b": 0.48,
115	        "llama-3.1-8b": 0.35,
116	        "mistral-7b-v0.3": 0.33
117	      },
118	      "memorization_fraction_mean": 0.4,
119	      "theta_fixed_dose_response_ratio": {
120	        "qwen3.5-9b": 2.8,
121	        "gemma-4-31b": 3.45,
122	        "llama-3.1-8b": 2.62,
123	        "mistral-7b-v0.3": 2.55
124	      },
125	      "theta_fixed_ratio_mean": 2.86,
126	      "theta_fixed_all_monotonic": true,
127	      "seen_unseen_lz_gap_15pct": {
128	        "qwen3.5-9b": 3.2,
129	        "gemma-4-31b": 4.1,
130	        "llama-3.1-8b": 2.7,
131	        "mistral-7b-v0.3": 2.5
132	      },
133	      "seen_unseen_gap_mean": 3.13,
134	      "dose_response_mmlu_theta_fixed": {
135	        "5pct": {
136	          "qwen": 1.1,
137	          "gemma": 1.4,
138	          "llama": 0.8,
139	          "mistral": 0.7
140	        },
141	        "10pct": {
142	          "qwen": 2.2,
143	          "gemma": 2.7,
144	          "llama": 1.6,
145	          "mistral": 1.4
146	        },
147	        "15pct": {
148	          "qwen": 3.5,
149	          "gemma": 4.2,
150	          "llama": 2.5,
151	          "mistral": 2.2
152	        },
153	        "25pct": {
154	          "qwen": 5.8,
155	          "gemma": 7.0,
156	          "llama": 4.1,
157	          "mistral": 3.7
158	        },
159	        "50pct": {
160	          "qwen": 9.8,
161	          "gemma": 14.5,
162	          "llama": 6.6,
163	          "mistral": 6.3
164	        }
165	      }
166	    },
167	    "tables": [
168	      {
169	        "name": "Table: Cross-Model Detection at 15% Contamination (MMLU)",
170	        "columns": [
171	          "model",
172	          "accuracy_clean",
173	          "accuracy_contam15",
174	          "delta_lz_free",
175	          "delta_lz_fixed",
176	          "cohens_d",
177	          "memorization_frac",
178	          "theta_shift"
179	        ],
180	        "rows": [
181	          [
182	            "Qwen3.5-9B",
183	            0.71,
184	            0.76,
185	            -4.1,
186	            3.5,
187	            -3.95,
188	            0.42,
189	            0.3
190	          ],
191	          [
192	            "Gemma-4-31B",
193	            0.78,
194	            0.84,
195	            -4.8,
196	            4.2,
197	            -4.52,
198	            0.48,
199	            0.35
200	          ],
201	          [
202	            "Llama-3.1-8B",
203	            0.63,
204	            0.69,
205	            -2.9,
206	            2.5,
207	            -2.85,
208	            0.35,
209	            0.24
210	          ],
211	          [
212	            "Mistral-7B-v0.3",
213	            0.61,
214	            0.67,
215	            -2.5,
216	            2.2,
217	            -2.42,
218	            0.33,
219	            0.21
220	          ]
221	        ]
222	      },
223	      {
224	        "name": "Table: GSM8K Small-Benchmark Detection at 15%",
225	        "columns": [
226	          "model",
227	          "n_items",
228	          "delta_lz_fixed",
229	          "cohens_d",
230	          "significant_p005"
231	        ],
232	        "rows": [
233	          [
234	            "Qwen3.5-9B",
235	            1319,
236	            1.8,
237	            -1.42,
238	            true
239	          ],
240	          [
241	            "Gemma-4-31B",
242	            1319,
243	            2.1,
244	            -1.68,
245	            true
246	          ],
247	          [
248	            "Llama-3.1-8B",
249	            1319,
250	            1.2,
251	            -0.91,
252	            true
253	          ],
254	          [
255	            "Mistral-7B-v0.3",
256	            1319,
257	            1.1,
258	            -0.85,
259	            true
260	          ]
261	        ]
262	      },
263	      {
264	        "name": "Table: θ-Fixed Dose-Response (MMLU, all models)",
265	        "columns": [
266	          "contam_level",
267	          "qwen_delta",
268	          "gemma_delta",
269	          "llama_delta",
270	          "mistral_delta",
271	          "monotonic"
272	        ],
273	        "rows": [
274	          [
275	            "5%",
276	            1.1,
277	            1.4,
278	            0.8,
279	            0.7,
280	            "✓"
281	          ],
282	          [
283	            "10%",
284	            2.2,
285	            2.7,
286	            1.6,
287	            1.4,
288	            "✓"
289	          ],
290	          [
291	            "15%",
292	            3.5,
293	            4.2,
294	            2.5,
295	            2.2,
296	            "✓"
297	          ],
298	          [
299	            "25%",
300	            5.8,
301	            7.0,
302	            4.1,
303	            3.7,
304	            "✓"
305	          ],
306	          [
307	            "50%",
308	            9.8,
309	            14.5,
310	            6.6,
311	            6.3,
312	            "✓"
313	          ]
314	        ]
315	      }
316	    ],
317	    "figures": [],
318	    "analysis": "核心假设 1 完全验证：SFT memorization fingerprint 跨 4 个模型家族一致。效应量范围 [2.42, 4.52] 远超统计显著性需求。θ-fixed 策略普适性确认（假设 2），所有模型的 dose-response ratio ∈[2.55, 3.45]。 GSM8K 的小 benchmark 假设（假设 4）通过 |d|>0.8 验证，尽管绝对信号弱于 MMLU（n=14042 vs 1319）， paired comparison 设计弥补了 power 不足。这为 Claim 1 提供了跨架构、跨规模的 ground-truth validation。\n\n\nBest 档要求 4/4 模型在 15% 均显著。Gemma-4-31B 作为 31B 参数模型具有更强的 memorization 能力 （SFT 时容量更大，更容易逐字存储 seen items），因此 |d| 最高（4.52）且 memorization_fraction 最高（0.48）。Llama-3.1-8B 和 Mistral-7B-v0.3 参数较少但仍在 |d|>2.0 范围，因为 QLoRA 即使在小模型上也能有效注入 memorization——关键是 LoRA rank 足够捕获 item-level patterns。 GSM8K 虽然只有 ~1.3K items（理论 power 较低），但 ctrl-contam 测量的是 Δlz*（within-model shift） 而非绝对检测，所以即使 power function 预测 single-model detection 只有 59%， paired comparison 的效应量仍可达 |d|>0.8。θ-fixed 策略在所有模型上普适是因为 θ-shift 机制是 IRT MLE 估计的数学性质（污染→更多正确→θ_MLE↑），与模型架构无关。 Seen/unseen gap∈[2.5,5.0] 反映了 SFT 的部分泛化效应：seen items lz*≈0（memorized items 看起来\"正常\"），unseen items lz* 保持高值（未被 memorize 的 items 仍然产生 aberrant patterns）。\n"
319	  },
320	  {
321	    "name": "Baseline Comparison (≥5 methods)",
322	    "description": "在 ctrl-contam ground-truth 上比较 IRT-FIT vs 5+ baselines 的 AUROC。 Baselines: ConStat (re-test), Min-K%++ (token probs), accuracy z-score, PPL-based detection, random baseline, + ML classifiers (LR/RF)。\n",
323	    "results": {
324	      "auroc_5pct": {
325	        "lz_star_theta_fixed": 0.78,
326	        "lr_binary_oracle": 0.62,
327	        "rf_binary_oracle": 0.59,
328	        "accuracy_zscore": 0.55,
329	        "min_k_pp": 0.71,
330	        "ppl_based": 0.68,
331	        "constat_retest": 0.65,
332	        "random": 0.5
333	      },
334	      "auroc_10pct": {
335	        "lz_star_theta_fixed": 0.87,
336	        "lr_binary_oracle": 0.74,
337	        "rf_binary_oracle": 0.72,
338	        "accuracy_zscore": 0.63,
339	        "min_k_pp": 0.82,
340	        "ppl_based": 0.79,
341	        "constat_retest": 0.76,
342	        "random": 0.5
343	      },
344	      "auroc_15pct": {
345	        "lz_star_theta_fixed": 0.92,
346	        "lr_binary_oracle": 0.84,
347	        "rf_binary_oracle": 0.82,
348	        "accuracy_zscore": 0.71,
349	        "min_k_pp": 0.89,
350	        "ppl_based": 0.86,
351	        "constat_retest": 0.83,
352	        "random": 0.5
353	      },
354	      "auroc_25pct": {
355	        "lz_star_theta_fixed": 0.94,
356	        "lr_binary_oracle": 0.92,
357	        "rf_binary_oracle": 0.91,
358	        "accuracy_zscore": 0.78,
359	        "min_k_pp": 0.95,
360	        "ppl_based": 0.93,
361	        "constat_retest": 0.91,
362	        "random": 0.5
363	      },
364	      "lz_minus_best_baseline_5pct": 0.07,
365	      "lz_minus_best_binary_baseline_5pct": 0.16,
366	      "crossover_point": "~20% (Min-K%++ surpasses lz* above 20%)",
367	      "bootstrap_ci_width_mean": 0.04,
368	      "information_levels": {
369	        "binary_only": [
370	          "lz_star",
371	          "accuracy_zscore",
372	          "lr_binary",
373	          "rf_binary"
374	        ],
375	        "token_probs": [
376	          "min_k_pp",
377	          "ppl_based"
378	        ],
379	        "retest_required": [
380	          "constat_retest"
381	        ]
382	      }
383	    },
384	    "tables": [
385	      {
386	        "name": "Table: AUROC Comparison Across Contamination Levels (MMLU, averaged over 4 models)",
387	        "columns": [
388	          "method",
389	          "info_level",
390	          "auroc_5pct",
391	          "auroc_10pct",
392	          "auroc_15pct",
393	          "auroc_25pct"
394	        ],
395	        "rows": [
396	          [
397	            "lz*_θ-fixed",
398	            "binary",
399	            "0.78±0.03",
400	            "0.87±0.03",
401	            "0.92±0.02",
402	            "0.94±0.02"
403	          ],
404	          [
405	            "Min-K%++",
406	            "token_probs",
407	            "0.71±0.04",
408	            "0.82±0.03",
409	            "0.89±0.02",
410	            "0.95±0.01"
411	          ],
412	          [
413	            "PPL-based",
414	            "log_probs",
415	            "0.68±0.04",
416	            "0.79±0.03",
417	            "0.86±0.03",
418	            "0.93±0.02"
419	          ],
420	          [
421	            "ConStat",
422	            "retest",
423	            "0.65±0.05",
424	            "0.76±0.04",
425	            "0.83±0.03",
426	            "0.91±0.02"
427	          ],
428	          [
429	            "LR (oracle)",
430	            "binary",
431	            "0.62±0.05",
432	            "0.74±0.04",
433	            "0.84±0.03",
434	            "0.92±0.02"
435	          ],
436	          [
437	            "RF (oracle)",
438	            "binary",
439	            "0.59±0.06",
440	            "0.72±0.04",
441	            "0.82±0.03",
442	            "0.91±0.02"
443	          ],
444	          [
445	            "Acc z-score",
446	            "binary",
447	            "0.55±0.05",
448	            "0.63±0.04",
449	            "0.71±0.04",
450	            "0.78±0.03"
451	          ],
452	          [
453	            "Random",
454	            "—",
455	            0.5,
456	            0.5,
457	            0.5,
458	            0.5
459	          ]
460	        ]
461	      },
462	      {
463	        "name": "Table: lz* Advantage Over Best Baseline at Each Level",
464	        "columns": [
465	          "contam_level",
466	          "best_baseline",
467	          "best_baseline_auroc",
468	          "lz_auroc",
469	          "delta",
470	          "significant"
471	        ],
472	        "rows": [
473	          [
474	            "5%",
475	            "Min-K%++",
476	            0.71,
477	            0.78,
478	            0.07,
479	            "p<0.05"
480	          ],
481	          [
482	            "10%",
483	            "Min-K%++",
484	            0.82,
485	            0.87,
486	            0.05,
487	            "p<0.05"
488	          ],
489	          [
490	            "15%",
491	            "Min-K%++",
492	            0.89,
493	            0.92,
494	            0.03,
495	            "p=0.08"
496	          ],
497	          [
498	            "25%",
499	            "Min-K%++",
500	            0.95,
501	            0.94,
502	            -0.01,
503	            "n.s."
504	          ]
505	        ]
506	      }
507	    ],
508	    "figures": [],
509	    "analysis": "Best 档的 headline result：lz* 在实际关键的 5-10% 低污染率下无需任何标注数据或 token access 即胜过 supervised baselines 和 token-level methods。这验证了 IRT structure 作为 inductive bias 在 data-scarce regime 的优势。crossover 发生在 ~20%——高于此水平时 Min-K%++ 的 token-level signal 更强，但 20%+ 的污染在实际场景中已经很容易被 accuracy jump 发现。 关键 framing：lz* 在 \"检测困难\" 的低污染区间胜出，正是 minimal-information 方法最有价值的 regime。\n\n\nlz* 在 5-10% 低污染率胜出所有 baselines（假设 5）的机制：IRT 结构作为 inductive bias。 在低污染率下，signal-to-noise 极低——只有 5-10% 的 items 携带 contamination signal。 ML classifiers（LR/RF）即使有 oracle labels 也面临严重的 class imbalance（5% positive）， 且 binary feature space（0/1 per item）在低 contamination 时几乎不可分。 lz* 的优势来自 IRT model 提供的 structured expectation：它知道每个 item 的 expected P(correct|θ)， 因此即使只有 5% items 被 contaminate，这些 items 上的 \"impossible correctness\"（高难度 item 被答对） 会被精确捕获为 aberrance。而 ML classifier 只看到 raw 0/1 pattern，缺乏 item difficulty 的先验。 Min-K%++ 在 5% 时 AUROC=0.71 弱于 lz*（0.78）是因为 token-level 信号在极低污染时被 noise 淹没， 但在 20%+ 时 token distribution shift 变得明显，超过 binary-level detection。 accuracy z-score 作为 same-level binary baseline 在所有水平都远不如 lz*—— 它只看 total score 而非 pattern，丢失了 item-level aberrance 信息。 这确立了 IRT structure 作为 binary-only 方法的关键 advantage。\n"
510	  },
511	  {
512	    "name": "Post-RL Signal Retention",
513	    "description": "Qwen3.5-9B 上先 SFT 污染（15%）再 GRPO 训练，测试 Δlz* 在 RL 后是否保持。 回应 Wang et al. (2025) 的 MIA 全失效发现。\n",
514	    "results": {
515	      "pre_rl_delta_lz_fixed": 3.5,
516	      "pre_rl_cohens_d": -3.95,
517	      "pre_rl_accuracy_contam": 0.76,
518	      "pre_rl_accuracy_seen": 0.86,
519	      "post_rl_delta_lz_fixed": 2.8,
520	      "post_rl_cohens_d": -3.15,
521	      "post_rl_accuracy_contam": 0.79,
522	      "post_rl_accuracy_seen": 0.82,
523	      "signal_retention": 0.8,
524	      "retention_above_70pct": true,
525	      "min_k_pp_pre_rl_auroc": 0.89,
526	      "min_k_pp_post_rl_auroc": 0.54,
527	      "ppl_pre_rl_auroc": 0.86,
528	      "ppl_post_rl_auroc": 0.52,
529	      "lz_star_pre_rl_auroc": 0.92,
530	      "lz_star_post_rl_auroc": 0.85,
531	      "seen_accuracy_drop_post_rl": 0.04,
532	      "unseen_accuracy_gain_post_rl": 0.03,
533	      "memorization_fraction_post_rl": 0.34,
534	      "theta_shift_post_rl": 0.28
535	    },
536	    "tables": [
537	      {
538	        "name": "Table: Pre-RL vs Post-RL Detection Comparison",
539	        "columns": [
540	          "method",
541	          "info_level",
542	          "auroc_pre_rl",
543	          "auroc_post_rl",
544	          "retention_pct"
545	        ],
546	        "rows": [
547	          [
548	            "lz*_θ-fixed",
549	            "binary",
550	            0.92,
551	            0.85,
552	            "80%"
553	          ],
554	          [
555	            "Min-K%++",
556	            "token_probs",
557	            0.89,
558	            0.54,
559	            "4%"
560	          ],
561	          [
562	            "PPL-based",
563	            "log_probs",
564	            0.86,
565	            0.52,
566	            "2%"
567	          ],
568	          [
569	            "Acc z-score",
570	            "binary",
571	            0.71,
572	            0.65,
573	            "60%"
574	          ],
575	          [
576	            "LR (oracle)",
577	            "binary",
578	            0.84,
579	            0.72,
580	            "56%"
581	          ]
582	        ]
583	      },
584	      {
585	        "name": "Table: Binary Response Patterns Pre/Post RL",
586	        "columns": [
587	          "metric",
588	          "pre_rl",
589	          "post_rl",
590	          "change"
591	        ],
592	        "rows": [
593	          [
594	            "Δlz*_fixed",
595	            3.5,
596	            2.8,
597	            "-20%"
598	          ],
599	          [
600	            "Cohen's d",
601	            -3.95,
602	            -3.15,
603	            "-20%"
604	          ],
605	          [
606	            "Seen accuracy",
607	            0.86,
608	            0.82,
609	            "-4pp"
610	          ],
611	          [
612	            "Unseen accuracy",
613	            0.73,
614	            0.76,
615	            "+3pp"
616	          ],
617	          [
618	            "Memorization fraction",
619	            0.42,
620	            0.34,
621	            "-8pp"
622	          ]
623	        ]
624	      }
625	    ],
626	    "figures": [],
627	    "analysis": "这是论文最强的 selling point 之一。Wang et al. (2025) 证明所有 10 种 log-prob based methods 在 RL 后降至 random，而 lz* 保留 80% 信号。这直接证明了 minimal-information operating point 的 structural advantage：binary patterns 对 RL 是 robust 的，因为 RL 优化的是 generation quality 而非 item-level correctness erasure。paper 可以引用此结果 直接回应 Wang et al. 的 \"all methods fail\" claim——\"all TOKEN-LEVEL methods fail, but BINARY-LEVEL detection survives.\"\n\n\nPost-RL signal retention ≥70%（假设 3）成立的核心原因：GRPO 优化的是 reward signal（正确率/格式）， 而非 item-level response distribution。SFT memorization 写入的是 \"看到 item X → 输出 answer Y\" 的 pattern，这是 parameter-level 的 association。GRPO 的 policy gradient 更新主要影响 reasoning chain 的 token distribution，而 binary correctness 层面的 memorization 痕迹 （hard item 仍然答对）大部分保留。signal 从 3.5 降到 2.8（retention=80%）的 20% 损失来自： (a) RL 训练中少量 seen items 的 memorization 被 \"覆盖\"（RL 发现了不同的 reasoning path）， (b) RL 普遍提升了 unseen items 的正确率（θ进一步上升），轻微压缩了 seen/unseen gap。 但关键是 binary response 层面的 aberrant pattern 仍然存在——模型在 \"不该答对\" 的 hard items 上 仍然答对，这个 pattern-level signal 是 RL 无法消除的，因为 RL 没有动机去 \"故意答错\" 已经答对的题。 相比之下，MIA methods（Min-K%++, PPL）失效是因为 RL 彻底重塑了 token-level distribution—— reasoning tokens 的 perplexity 分布被 GRPO 重新优化，训练数据的 token-level fingerprint 消失。 这是 binary vs token-level detection 的 structural advantage。\n"
628	  },
629	  {
630	    "name": "Multiscale lzm Statistic",
631	    "description": "实现 Hong, Lin & Cheng (2021) 的 multiscale lzm——跨 benchmark 聚合的标准化 lz* 总分。 在 PSN-IRT 12 模型和 ctrl-contam 模型上验证。\n",
632	    "results": {
633	      "gemini15_lzm": 42.8,
634	      "deepseek_v3_lzm": 38.2,
635	      "yi_lightning_lzm": 35.6,
636	      "qwen_plus_lzm": 33.1,
637	      "doubao_pro_lzm": -8.4,
638	      "mistral_7b_lzm": 2.1,
639	      "lzm_vs_mean_lz_correlation": 0.97,
640	      "lzm_flagged_at_alpha005": "11/12",
641	      "ctrl_contam_lzm_clean": 8.5,
642	      "ctrl_contam_lzm_15pct": 14.2,
643	      "ctrl_contam_lzm_50pct": 22.8,
644	      "lzm_cohens_d_15pct": -4.12,
645	      "lzm_incremental_over_single_benchmark": "+0.15 AUROC vs single-best benchmark"
646	    },
647	    "tables": [
648	      {
649	        "name": "Table: lzm Scores for PSN-IRT 12 Models",
650	        "columns": [
651	          "model",
652	          "lz_mmlu",
653	          "lz_hellaswag",
654	          "lz_gsm8k",
655	          "lz_arc_c",
656	          "lz_humaneval",
657	          "lzm_aggregate"
658	        ],
659	        "rows": [
660	          [
661	            "Gemini-1.5",
662	            31.8,
663	            28.4,
664	            12.1,
665	            6.2,
666	            -2.4,
667	            42.8
668	          ],
669	          [
670	            "DeepSeek-V3",
671	            28.6,
672	            25.1,
673	            10.8,
674	            5.8,
675	            -1.2,
676	            38.2
677	          ],
678	          [
679	            "Yi-Lightning",
680	            26.4,
681	            22.3,
682	            9.5,
683	            -0.3,
684	            -1.8,
685	            35.6
686	          ],
687	          [
688	            "Doubao-Pro",
689	            -12.5,
690	            -8.2,
691	            4.3,
692	            -2.1,
693	            -3.8,
694	            -8.4
695	          ]
696	        ]
697	      }
698	    ],
699	    "figures": [],
700	    "analysis": "lzm 提供了一个 principled 的跨 benchmark 聚合方式，比简单 mean(lz*) 有理论优势 （proper variance weighting）。在 ctrl-contam 中，multi-benchmark contamination 的 lzm 检测力比 single-best benchmark 强 0.15 AUROC，证明了 multiscale 方法的实用价值。 但核心贡献仍是 per-benchmark lz*，lzm 作为 extension/robustness check。\n\n\nlzm 聚合跨 benchmark 信号的原理：如果一个模型在多个 benchmarks 上都表现异常， lzm 将这些独立 signals 标准化后求和，产生比任何单一 benchmark 更强的检测统计量。 在 best 档下，ctrl-contam 跨 3 个 benchmarks 都注入了污染，lzm 的 multi-benchmark aggregation 产生额外的 +0.15 AUROC 增益。对 PSN-IRT 12 模型，lzm 与 mean_lz* 高度相关（r=0.97） 因为大多数模型的 anomaly 在所有 benchmarks 上方向一致（positive direction dominant, 93.3% cells）。 Doubao-pro 的负 lzm 反映其独特的 negative lz* 模式（STEM 和 Humanities domains 特异性不足）。 这是一个 methodological addition（不是核心贡献），但增强了 paper 的 completeness。\n"
701	  },
702	  {
703	    "name": "Extra Benchmarks (BBH + MATH)",
704	    "description": "BBH (6,511 items) 和 MATH (5,000 items) 扩展，填充 1K-10K items 的 power gap。 在 ctrl-contam 模型上验证中等规模 benchmark 的检测力。\n",
705	    "results": {
706	      "bbh_theoretical_power_15pct": 0.88,
707	      "math_theoretical_power_15pct": 0.82,
708	      "bbh_actual_power_15pct": 0.85,
709	      "math_actual_power_15pct": 0.78,
710	      "bbh_cohens_d_15pct": -3.21,
711	      "math_cohens_d_15pct": -2.88,
712	      "bbh_memorization_fraction": 0.4,
713	      "math_memorization_fraction": 0.36,
714	      "R2_with_new_benchmarks": 0.968,
715	      "bbh_dose_response_monotonic_theta_fixed": true,
716	      "math_dose_response_monotonic_theta_fixed": true,
717	      "bbh_theta_fixed_ratio": 2.72,
718	      "math_theta_fixed_ratio": 2.58
719	    },
720	    "tables": [
721	      {
722	        "name": "Table: Extended Power Function Validation",
723	        "columns": [
724	          "benchmark",
725	          "n_items",
726	          "theoretical_power_15pct",
727	          "actual_power_ctrl",
728	          "cohens_d_15pct"
729	        ],
730	        "rows": [
731	          [
732	            "MMLU",
733	            14042,
734	            0.985,
735	            0.92,
736	            -3.95
737	          ],
738	          [
739	            "HellaSwag",
740	            10042,
741	            0.753,
742	            0.71,
743	            -2.64
744	          ],
745	          [
746	            "BBH",
747	            6511,
748	            0.88,
749	            0.85,
750	            -3.21
751	          ],
752	          [
753	            "MATH",
754	            5000,
755	            0.82,
756	            0.78,
757	            -2.88
758	          ],
759	          [
760	            "GSM8K",
761	            1319,
762	            0.59,
763	            0.55,
764	            -1.42
765	          ]
766	        ]
767	      }
768	    ],
769	    "figures": [],
770	    "analysis": "BBH 和 MATH 的加入完善了 power function 的中间区段验证。5 个 benchmarks 覆盖了 1.3K 到 14K items 的完整范围，R²=0.968 确认 power 与 √n 的理论关系在实际 ctrl-contam 中成立。 这直接支撑 Claim 2 的核心论断：detection power is a predictable function of benchmark size。\n\n\nBBH（6511 items）和 MATH（5000 items）填充了 GSM8K（1319）和 MMLU（14042）之间的 gap。 在 best 档下，两者都产生显著检测信号：BBH 因为 items 多且区分度高（BIG-Bench Hard 的 items 被设计为 challenging），theoretical power 接近 90%；MATH 的 items 更结构化（数学题）， memorization fraction 稍低（0.36 vs 0.40）因为数学题的 SFT 更容易产生 generalization 而非 verbatim memorization。两者的加入使 power function 的 R² 从 0.957 提升到 0.968， 进一步验证了 Claim 2 的 power ∝ f(n_items) 关系。这些中等规模 benchmarks 是实际应用中最常见的尺寸范围（多数 benchmarks 在 1K-10K 之间），因此验证至关重要。\n"
771	  },
772	  {
773	    "name": "Natural Experiment (base→chat pairs)",
774	    "description": "v1 leaderboard base→chat model pairs 计算 Δlz* = lz*(chat) - lz*(base) 作为 SFT 效应代理。\n",
775	    "results": {
776	      "n_pairs": 21,
777	      "n_complete_pairs": 9,
778	      "hellaswag_systematic_effect": {
779	        "mean_deviation": -3.8,
780	        "t_stat": -4.2,
781	        "p_value": 0.0008,
782	        "direction": "SFT decreases person-fit"
783	      },
784	      "gsm8k_systematic_effect": {
785	        "mean_deviation": 4.5,
786	        "t_stat": 3.8,
787	        "p_value": 0.004,
788	        "direction": "SFT increases person-fit"
789	      },
790	      "mmlu_effect": {
791	        "p_value": 0.12,
792	        "direction": "non-significant"
793	      },
794	      "arc_c_effect": {
795	        "p_value": 0.31,
796	        "direction": "non-significant"
797	      },
798	      "individual_outlier_pairs": 1,
799	      "outlier_model": "codellama-34b-instruct",
800	      "outlier_benchmark": "GSM8K",
801	      "outlier_delta_lz": 8.7
802	    },
803	    "tables": [
804	      {
805	        "name": "Table: Systematic SFT Effects on lz* (base→chat)",
806	        "columns": [
807	          "benchmark",
808	          "n_pairs",
809	          "mean_Δlz",
810	          "t_stat",
811	          "p_value",
812	          "interpretation"
813	        ],
814	        "rows": [
815	          [
816	            "HellaSwag",
817	            9,
818	            -3.8,
819	            -4.2,
820	            0.0008,
821	            "SFT improves commonsense (less aberrant)"
822	          ],
823	          [
824	            "GSM8K",
825	            9,
826	            4.5,
827	            3.8,
828	            0.004,
829	            "Math SFT creates new aberrance patterns"
830	          ],
831	          [
832	            "MMLU",
833	            9,
834	            1.8,
835	            1.7,
836	            0.12,
837	            "n.s."
838	          ],
839	          [
840	            "ARC-C",
841	            9,
842	            0.9,
843	            1.1,
844	            0.31,
845	            "n.s."
846	          ]
847	        ]
848	      }
849	    ],
850	    "figures": [],
851	    "analysis": "P2-optional 实验。提供了 real-world SFT 效应的 converging evidence，但受限于 a_r=0.111 的 discrimination failure。在 paper 中作为 supplementary finding 而非 primary evidence。\n\n\nBest 档下 natural experiment 的结果比 registry 中的实际结果稍强：HellaSwag 和 GSM8K 显示更清晰的 systematic SFT effect（p<0.001 和 p<0.005），且出现一个 individual outlier （codellama-34b-instruct 在 GSM8K 上 Δlz*=8.7，远超 group mean）。这个 outlier 的出现是 best 档独有的——它提供了 \"自然实验中发现疑似污染\" 的 case study evidence。 HellaSwag 的 negative shift 解释：chat SFT 训练中包含了对话/常识推理数据， 这些与 HellaSwag 的 commonsense completion task 有 domain overlap，导致泛化性提升 但 pattern 变得 less aberrant（更符合 IRT 预测）。GSM8K positive shift： chat 模型的 math instruction tuning 不是 benchmark-specific memorization 而是 reasoning capability，但少数模型可能直接接触了 GSM8K items。 由于 a_r=0.111 的 discrimination failure，此实验只能作为 converging evidence，不是 primary claim。\n"
852	  },
853	  {
854	    "name": "V1 IRT Refit Expanded (N=178)",
855	    "description": "扩大 v1 IRT 重拟合样本量至 N≥178，最终验证 Path D（large-scale audit）是否可行。\n",
856	    "results": {
857	      "n_models": 178,
858	      "n_items": 14042,
859	      "3pl_a_pearson_r": 0.13,
860	      "2pl_a_pearson_r": -0.03,
861	      "3pl_b_pearson_r": 0.66,
862	      "a_r_below_threshold": true,
863	      "conclusion": "Path D confirmed dead. Classical MML-EM cannot recover IRT discrimination from LLM response data at available sample sizes."
864	    },
865	    "tables": [
866	      {
867	        "name": "Table: IRT Parameter Recovery (Classical vs PSN-IRT)",
868	        "columns": [
869	          "method",
870	          "N_models",
871	          "a_pearson_r",
872	          "b_pearson_r",
873	          "conclusion"
874	        ],
875	        "rows": [
876	          [
877	            "MML-EM 3PL (N=63)",
878	            63,
879	            0.111,
880	            0.626,
881	            "a failure"
882	          ],
883	          [
884	            "MML-EM 3PL (N=178)",
885	            178,
886	            0.13,
887	            0.66,
888	            "a failure persists"
889	          ],
890	          [
891	            "PSN-IRT (neural)",
892	            12,
893	            "validated",
894	            "validated",
895	            "reference standard"
896	          ]
897	        ]
898	      }
899	    ],
900	    "figures": [],
901	    "analysis": "Path D 的确定性关闭是 paper structure 的关键节点。它确立了 \"why ctrl-contam, not leaderboard audit\" 的 methodological justification，并为 Future Work 中的 \"neural IRT at scale\" 提供了动机。\n\n\n即使在 best 档，Path D（leaderboard-scale audit via classical IRT refit）仍然失败。 这不是 experiment failure 而是 honest negative result：classical IRT estimation 需要 hundreds of examinees with similar ability distributions，而 LLM response data 的特殊性（模型间 ability range 极大，item response 非 locally independent） 使得 MML-EM 无法恢复 discrimination parameters。a_r=0.13 << 0.4 threshold 确认 discriminability failure 不是样本量问题而是 structural incompatibility。 这本身是 Claim 3(c) 的贡献：quantifying the estimation challenge for neural IRT。\n"
902	  },
903	  {
904	    "name": "4PL vs 3PL Ablation",
905	    "description": "4PL vs 3PL(d=1) 消融实验：量化 d 参数对检测灵敏度的影响。\n",
906	    "results": {
907	      "mean_power_gain_4pl_vs_3pl": {
908	        "MMLU": "+28pp",
909	        "HellaSwag": "+27pp",
910	        "GSM8K": "+21pp",
911	        "ARC_C": "+15pp",
912	        "HumanEval": "+14pp"
913	      },
914	      "far_4pl": 0.05,
915	      "far_3pl": "0.05-0.17 (inflated)",
916	      "far_2pl": "0.50-1.00 (catastrophic)",
917	      "items_with_d_lt_095_mmlu": "46%",
918	      "ctrl_contam_4pl_d_15pct": -3.95,
919	      "ctrl_contam_3pl_d_15pct": -1.82,
920	      "power_loss_without_d": "54%"
921	    },
922	    "tables": [
923	      {
924	        "name": "Table: 4PL vs 3PL Detection Performance",
925	        "columns": [
926	          "benchmark",
927	          "n_items",
928	          "power_4pl_25pct",
929	          "power_3pl_25pct",
930	          "gain",
931	          "pct_items_d_lt_095"
932	        ],
933	        "rows": [
934	          [
935	            "MMLU",
936	            14042,
937	            0.776,
938	            0.329,
939	            "+44.7pp",
940	            "46%"
941	          ],
942	          [
943	            "HellaSwag",
944	            10042,
945	            0.534,
946	            0.28,
947	            "+25.4pp",
948	            "38%"
949	          ],
950	          [
951	            "GSM8K",
952	            1319,
953	            0.73,
954	            0.334,
955	            "+39.6pp",
956	            "42%"
957	          ],
958	          [
959	            "ARC-C",
960	            295,
961	            0.132,
962	            0.091,
963	            "+4.1pp",
964	            "29%"
965	          ],
966	          [
967	            "HumanEval",
968	            164,
969	            0.318,
970	            0.165,
971	            "+15.3pp",
972	            "35%"
973	          ]
974	        ]
975	      }
976	    ],
977	    "figures": [],
978	    "analysis": "4PL ablation 是 methodological rigor 的体现。Reviewer 可能质疑 \"为什么不用更简单的 3PL\"， 此实验给出定量答案：+28pp average power gain，54% signal loss without d。 结合 exp-4pl-real-data-degradation（r=0.225 between 4PL/3PL lz*）， establishes 4PL 作为 LLM person-fit 的 minimum viable parameterization。\n\n\n4PL 的 d 参数（upper asymptote）对高能力 LLM 至关重要：当 d<1 时，P(correct) 的上限低于 1.0， 高能力模型在这些 items 上 \"应该\" 答错（按 4PL 预测）。如果忽略 d（设 d=1）， model 预测所有高能力模型都应该答对所有题——这会让 few errors 变成 extreme aberrance（false alarm）。 MMLU 46% items 有 d<0.95 意味着将近一半的题目有上限效应，忽略这些会产生巨大的 FAR 膨胀。 在 best 档下，ctrl-contam 进一步确认：同一污染实验用 3PL 分析时 |d| 从 3.95 降到 1.82， 因为 3PL 的 inflated null variance 稀释了真实信号。这证明 4PL 不是 \"nice-to-have\" 而是 LLM person-fit 分析的 necessary condition。\n"
979	  },
980	  {
981	    "name": "Baseline Comparison — Accuracy Z-Score (completed)",
982	    "description": "Accuracy z-score 作为 same-level binary-only baseline 的扩展对比， 整合入完整 baseline comparison 实验中。\n",
983	    "results": {
984	      "acc_zscore_auroc_5pct": 0.55,
985	      "acc_zscore_auroc_10pct": 0.63,
986	      "acc_zscore_auroc_15pct": 0.71,
987	      "acc_zscore_auroc_25pct": 0.78,
988	      "lz_star_advantage_over_zscore_5pct": "+0.23 AUROC",
989	      "lz_star_advantage_over_zscore_15pct": "+0.21 AUROC",
990	      "lz_star_advantage_over_zscore_25pct": "+0.16 AUROC"
991	    },
992	    "tables": [],
993	    "figures": [],
994	    "analysis": "Accuracy z-score 是 \"straw-man\" 但也是 fair comparison：它是唯一的 same-information-level baseline （binary only, no training data）。lz* 的 consistent +0.16-0.23 AUROC advantage 直接证明 IRT item parameters 提供了有价值的 structural information。\n\n\nAccuracy z-score 只利用 total score（sum of binary responses）而丢失所有 item-level pattern information。lz* 的优势正来自于 item-level aberrance detection： 它区分 \"总分高因为答对了该对的题\" vs \"总分高因为答对了不该对的题\"。 在 5% 低污染时，只有 ~700 items（14042×5%）被 contaminate，total score change 微乎其微 （+2-3 pp accuracy），z-score 几乎无法检测。但 lz* 能捕捉到这 700 items 中的 \"不可能正确\" 模式。 这是 \"IRT structure as inductive bias\" 的最直接证明。\n"
995	  },
996	  {
997	    "name": "Domain-Level Analysis",
998	    "description": "MMLU domain-level 分析：按 subject category 分别计算 person-fit，识别污染的 domain 分布。\n",
999	    "results": {
1000	      "gemini_subjects_flagged": "50/57 (87.7%)",
1001	      "gemini_contamination_uniform": true,
1002	      "gemini_category_lz_range": [
1003	        15.3,
1004	        21.2
1005	      ],
1006	      "ctrl_contam_domain_uniformity": "uniform (as expected, since QLoRA trains on random 15% sample)",
1007	      "ctrl_contam_stem_lz": 3.8,
1008	      "ctrl_contam_humanities_lz": 3.3,
1009	      "ctrl_contam_social_sci_lz": 3.5,
1010	      "ctrl_contam_other_lz": 3.2,
1011	      "doubao_selective_domains": true,
1012	      "doubao_negative_pattern": "STEM and Humanities strongly negative, Other positive"
1013	    },
1014	    "tables": [
1015	      {
1016	        "name": "Table: MMLU Domain-Level lz* (Gemini-1.5 vs Ctrl-Contam)",
1017	        "columns": [
1018	          "domain",
1019	          "gemini_lz",
1020	          "ctrl_contam_15_lz",
1021	          "ctrl_contam_clean_lz"
1022	        ],
1023	        "rows": [
1024	          [
1025	            "STEM",
1026	            21.2,
1027	            3.8,
1028	            0.1
1029	          ],
1030	          [
1031	            "Humanities",
1032	            17.9,
1033	            3.3,
1034	            -0.2
1035	          ],
1036	          [
1037	            "Social Sciences",
1038	            15.9,
1039	            3.5,
1040	            0.0
1041	          ],
1042	          [
1043	            "Other",
1044	            15.3,
1045	            3.2,
1046	            0.1
1047	          ]
1048	        ]
1049	      }
1050	    ],
1051	    "figures": [],
1052	    "analysis": "Domain analysis 提供了 contamination 的 \"spatial resolution\"：从 aggregate model-level detection 到 domain-level localization。在 paper 中服务于两个目的：(a) 验证 ctrl-contam 内部一致性 （random sampling → uniform signal），(b) case study 中展示不同 contamination type 的 domain fingerprint。\n\n\nDomain analysis 在 best 档下产生两个 clear findings：(1) Gemini-1.5 的 contamination 是 uniform across domains（所有 subject 都被 memorize），consistent with \"bulk training data leak\" 而非 \"selective domain tuning\"；(2) ctrl-contam 模型的 domain-level signal 也是 uniform （因为 QLoRA 训练样本是 randomly sampled across all subjects），验证了实验设计的 internal consistency。 Doubao 的 selective negative pattern 则展示了不同类型的 anomaly：可能是 domain-specific training data 导致某些 domains 泛化过强（lz*<0 = over-consistent pattern）。\n"
1053	  },
1054	  {
1055	    "name": "Leaderboard Audit (Abandoned)",
1056	    "description": "Open LLM Leaderboard v1 大规模 13K+ 模型扫描。因 IRT refit failure 放弃。\n",
1057	    "results": {
1058	      "status": "ABANDONED",
1059	      "reason": "a_r=0.111 discrimination failure makes lz* degenerate to accuracy-like metric at scale",
1060	      "paper_treatment": "Data availability noted in Discussion/Future Work; 13K+ per-item data available for future neural IRT estimation"
1061	    },
1062	    "tables": [],
1063	    "figures": [],
1064	    "analysis": "ABANDONED。在 paper 中转化为 methodological contribution：量化了 classical vs neural IRT 在 LLM context 中的 gap，为 future work 提供了 concrete roadmap（13K+ data available, awaiting better estimation methods）。\n\n即使在 best 档，leaderboard audit 仍然 abandoned。这不影响 best 档的叙事， 因为 ctrl-contam 提供了比 leaderboard audit 更强的 ground-truth validation。 Audit 的 abandonment 本身是 honest negative result (Claim 3c)：classical IRT 的 sample size requirement 与 LLM evaluation ecosystem 不兼容。 Paper 中将其定位为 \"future work when neural IRT estimation at scale becomes feasible\"。\n"
1065	  }
1066	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c22630af-1a38-47d4-8e10-f4019fda80b9",
  "isSidechain": false,
  "promptId": "eb66b833-472c-4a64-b5b3-e6647c252907",
  "type": "user",
  "uuid": "550107b1-adb0-470b-ac14-3fc799784a5d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Controlled Contamination Pilot (Qwen3.5-9B)\",\n    \"description\": \"Qwen3.5-9B × 4 conditions (0%-seed1/0%-seed2/15%/50%) × MMLU。 验证 Δlz* 显著性、clean-vs-clean noise floor、seen/unseen memorization fraction。\\n\",\n    \"results\": {\n      \"clean_s1_lz_star\": 7.2,\n      \"clean_s2_lz_star\": 6.8,\n      \"clean_delta_lz\": 0.4,\n      \"clean_delta_nonsig\": true,\n      \"contam_15_lz_star_free\": 2.8,\n      \"contam_15_delta_lz_free\": -4.1,\n      \"contam_15_cohens_d\": -3.95,\n      \"contam_50_lz_star_free\": 4.9,\n      \"contam_50_delta_lz_free\": -2.0,\n      \"contam_15_lz_star_fixed\": 10.5,\n      \"contam_50_lz_star_fixed\": 16.8,\n      \"theta_fixed_delta_15\": 3.5,\n      \"theta_fixed_delta_50\": 9.8,\n      \"theta_fixed_ratio\": 2.8,\n      \"accuracy_clean\": 0.71,\n      \"accuracy_contam_15\": 0.76,\n      \"accuracy_contam_50\": 0.8,\n      \"accuracy_contam_15_seen\": 0.86,\n      \"accuracy_contam_15_unseen\": 0.73,\n      \"memorization_fraction_15\": 0.42,\n      \"memorization_fraction_50\": 0.31,\n      \"theta_shift_clean\": -0.08,\n      \"theta_shift_contam_15\": 0.22,\n      \"theta_shift_contam_50\": 0.41\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Qwen3.5-9B Pilot Results\",\n        \"columns\": [\n          \"condition\",\n          \"accuracy\",\n          \"lz_star_free\",\n          \"lz_star_fixed\",\n          \"theta_MLE\",\n          \"delta_lz_free\",\n          \"delta_lz_fixed\"\n        ],\n        \"rows\": [\n          [\n            \"clean_s1\",\n            0.71,\n            7.2,\n            7.2,\n            -0.08,\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"clean_s2\",\n            0.71,\n            6.8,\n            6.8,\n            -0.09,\n            0.4,\n            0.4\n          ],\n          [\n            \"contam_15\",\n            0.76,\n            2.8,\n            10.5,\n            0.22,\n            -4.1,\n            3.5\n          ],\n          [\n            \"contam_50\",\n            0.8,\n            4.9,\n            16.8,\n            0.41,\n            -2.0,\n            9.8\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Go/no-go 信号明确通过。|d|=3.95 远超 0.8 的 large effect 阈值。θ-fixed 恢复单调 dose-response (ratio=2.80∈[2.5,4.0])，确认 θ-shift 是唯一导致 free-θ 非单调的机制。 memorization_fraction=0.42 意味着理论 power 的 ~42% 可在实际中实现——MMLU 15% 理论 power 98.5% × 0.42 = adjusted power ≈41%，但 lz* 检测的是 aggregate pattern 而非逐 item 检测， 所以 aggregate Δlz* 仍然产生 |d|≈4 的强效应。\\n\\n\\nQwen3.5-9B 作为较新架构（含 thinking 能力），SFT memorization 效率略高于 Qwen2.5-7B。 15% 污染产生强信号（|d|≈4.0）是因为 QLoRA 在小比例 seen items 上产生明确的 aberrant pattern： 模型在高难度 seen items 上异常正确，而在 unseen items 上保持原有错误模式。memorization_fraction≈0.42 说明 ~42% 的 seen items 被完全记忆（产生 aberrant response），剩余 58% 产生了泛化而非逐字记忆。 θ-shift 机制与 pilot 一致：污染提升整体能力估计，θ_MLE 上升吸收了部分 aberrance signal， θ-fixed 恢复单调性。clean-vs-clean Δ≈0.4 确认 noise floor 远低于检测阈值。\\n\"\n  },\n  {\n    \"name\": \"Full Multi-Model Controlled Contamination\",\n    \"description\": \"4 模型 (Qwen3.5-9B, Gemma-4-31B, Llama-3.1-8B, Mistral-7B-v0.3) × 6 contamination levels (0/5/10/15/25/50%) × 3 benchmarks (MMLU, GSM8K, HellaSwag)。\\n\",\n    \"results\": {\n      \"cohens_d_15pct_mmlu\": {\n        \"qwen3.5-9b\": -3.95,\n        \"gemma-4-31b\": -4.52,\n        \"llama-3.1-8b\": -2.85,\n        \"mistral-7b-v0.3\": -2.42\n      },\n      \"cohens_d_15pct_mean\": 3.44,\n      \"cohens_d_15pct_min\": 2.42,\n      \"models_significant_at_15pct\": 4,\n      \"benchmarks_significant_per_model\": {\n        \"qwen3.5-9b\": 3,\n        \"gemma-4-31b\": 3,\n        \"llama-3.1-8b\": 2,\n        \"mistral-7b-v0.3\": 2\n      },\n      \"gsm8k_cohens_d_15pct\": {\n        \"qwen3.5-9b\": -1.42,\n        \"gemma-4-31b\": -1.68,\n        \"llama-3.1-8b\": -0.91,\n        \"mistral-7b-v0.3\": -0.85\n      },\n      \"gsm8k_all_above_0.8\": true,\n      \"memorization_fraction_15pct\": {\n        \"qwen3.5-9b\": 0.42,\n        \"gemma-4-31b\": 0.48,\n        \"llama-3.1-8b\": 0.35,\n        \"mistral-7b-v0.3\": 0.33\n      },\n      \"memorization_fraction_mean\": 0.4,\n      \"theta_fixed_dose_response_ratio\": {\n        \"qwen3.5-9b\": 2.8,\n        \"gemma-4-31b\": 3.45,\n        \"llama-3.1-8b\": 2.62,\n        \"mistral-7b-v0.3\": 2.55\n      },\n      \"theta_fixed_ratio_mean\": 2.86,\n      \"theta_fixed_all_monotonic\": true,\n      \"seen_unseen_lz_gap_15pct\": {\n        \"qwen3.5-9b\": 3.2,\n        \"gemma-4-31b\": 4.1,\n        \"llama-3.1-8b\": 2.7,\n        \"mistral-7b-v0.3\": 2.5\n      },\n      \"seen_unseen_gap_mean\": 3.13,\n      \"dose_response_mmlu_theta_fixed\": {\n        \"5pct\": {\n          \"qwen\": 1.1,\n          \"gemma\": 1.4,\n          \"llama\": 0.8,\n          \"mistral\": 0.7\n        },\n        \"10pct\": {\n          \"qwen\": 2.2,\n          \"gemma\": 2.7,\n          \"llama\": 1.6,\n          \"mistral\": 1.4\n        },\n        \"15pct\": {\n          \"qwen\": 3.5,\n          \"gemma\": 4.2,\n          \"llama\": 2.5,\n          \"mistral\": 2.2\n        },\n        \"25pct\": {\n          \"qwen\": 5.8,\n          \"gemma\": 7.0,\n          \"llama\": 4.1,\n          \"mistral\": 3.7\n        },\n        \"50pct\": {\n          \"qwen\": 9.8,\n          \"gemma\": 14.5,\n          \"llama\": 6.6,\n          \"mistral\": 6.3\n        }\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Cross-Model Detection at 15% Contamination (MMLU)\",\n        \"columns\": [\n          \"model\",\n          \"accuracy_clean\",\n          \"accuracy_contam15\",\n          \"delta_lz_free\",\n          \"delta_lz_fixed\",\n          \"cohens_d\",\n          \"memorization_frac\",\n          \"theta_shift\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3.5-9B\",\n            0.71,\n            0.76,\n            -4.1,\n            3.5,\n            -3.95,\n            0.42,\n            0.3\n          ],\n          [\n            \"Gemma-4-31B\",\n            0.78,\n            0.84,\n            -4.8,\n            4.2,\n            -4.52,\n            0.48,\n            0.35\n          ],\n          [\n            \"Llama-3.1-8B\",\n            0.63,\n            0.69,\n            -2.9,\n            2.5,\n            -2.85,\n            0.35,\n            0.24\n          ],\n          [\n            \"Mistral-7B-v0.3\",\n            0.61,\n            0.67,\n            -2.5,\n            2.2,\n            -2.42,\n            0.33,\n            0.21\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: GSM8K Small-Benchmark Detection at 15%\",\n        \"columns\": [\n          \"model\",\n          \"n_items\",\n          \"delta_lz_fixed\",\n          \"cohens_d\",\n          \"significant_p005\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3.5-9B\",\n            1319,\n            1.8,\n            -1.42,\n            true\n          ],\n          [\n            \"Gemma-4-31B\",\n            1319,\n            2.1,\n            -1.68,\n            true\n          ],\n          [\n            \"Llama-3.1-8B\",\n            1319,\n            1.2,\n            -0.91,\n            true\n          ],\n          [\n            \"Mistral-7B-v0.3\",\n            1319,\n            1.1,\n            -0.85,\n            true\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: θ-Fixed Dose-Response (MMLU, all models)\",\n        \"columns\": [\n          \"contam_level\",\n          \"qwen_delta\",\n          \"gemma_delta\",\n          \"llama_delta\",\n          \"mistral_delta\",\n          \"monotonic\"\n        ],\n        \"rows\": [\n          [\n            \"5%\",\n            1.1,\n            1.4,\n            0.8,\n            0.7,\n            \"✓\"\n          ],\n          [\n            \"10%\",\n            2.2,\n            2.7,\n            1.6,\n            1.4,\n            \"✓\"\n          ],\n          [\n            \"15%\",\n            3.5,\n            4.2,\n            2.5,\n            2.2,\n            \"✓\"\n          ],\n          [\n            \"25%\",\n            5.8,\n            7.0,\n            4.1,\n            3.7,\n            \"✓\"\n          ],\n          [\n            \"50%\",\n            9.8,\n            14.5,\n            6.6,\n            6.3,\n            \"✓\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"核心假设 1 完全验证：SFT memorization fingerprint 跨 4 个模型家族一致。效应量范围 [2.42, 4.52] 远超统计显著性需求。θ-fixed 策略普适性确认（假设 2），所有模型的 dose-response ratio ∈[2.55, 3.45]。 GSM8K 的小 benchmark 假设（假设 4）通过 |d|>0.8 验证，尽管绝对信号弱于 MMLU（n=14042 vs 1319）， paired comparison 设计弥补了 power 不足。这为 Claim 1 提供了跨架构、跨规模的 ground-truth validation。\\n\\n\\nBest 档要求 4/4 模型在 15% 均显著。Gemma-4-31B 作为 31B 参数模型具有更强的 memorization 能力 （SFT 时容量更大，更容易逐字存储 seen items），因此 |d| 最高（4.52）且 memorization_fraction 最高（0.48）。Llama-3.1-8B 和 Mistral-7B-v0.3 参数较少但仍在 |d|>2.0 范围，因为 QLoRA 即使在小模型上也能有效注入 memorization——关键是 LoRA rank 足够捕获 item-level patterns。 GSM8K 虽然只有 ~1.3K items（理论 power 较低），但 ctrl-contam 测量的是 Δlz*（within-model shift） 而非绝对检测，所以即使 power function 预测 single-model detection 只有 59%， paired comparison 的效应量仍可达 |d|>0.8。θ-fixed 策略在所有模型上普适是因为 θ-shift 机制是 IRT MLE 估计的数学性质（污染→更多正确→θ_MLE↑），与模型架构无关。 Seen/unseen gap∈[2.5,5.0] 反映了 SFT 的部分泛化效应：seen items lz*≈0（memorized items 看起来\\\"正常\\\"），unseen items lz* 保持高值（未被 memorize 的 items 仍然产生 aberrant patterns）。\\n\"\n  },\n  {\n    \"name\": \"Baseline Comparison (≥5 methods)\",\n    \"description\": \"在 ctrl-contam ground-truth 上比较 IRT-FIT vs 5+ baselines 的 AUROC。 Baselines: ConStat (re-test), Min-K%++ (token probs), accuracy z-score, PPL-based detection, random baseline, + ML classifiers (LR/RF)。\\n\",\n    \"results\": {\n      \"auroc_5pct\": {\n        \"lz_star_theta_fixed\": 0.78,\n        \"lr_binary_oracle\": 0.62,\n        \"rf_binary_oracle\": 0.59,\n        \"accuracy_zscore\": 0.55,\n        \"min_k_pp\": 0.71,\n        \"ppl_based\": 0.68,\n        \"constat_retest\": 0.65,\n        \"random\": 0.5\n      },\n      \"auroc_10pct\": {\n        \"lz_star_theta_fixed\": 0.87,\n        \"lr_binary_oracle\": 0.74,\n        \"rf_binary_oracle\": 0.72,\n        \"accuracy_zscore\": 0.63,\n        \"min_k_pp\": 0.82,\n        \"ppl_based\": 0.79,\n        \"constat_retest\": 0.76,\n        \"random\": 0.5\n      },\n      \"auroc_15pct\": {\n        \"lz_star_theta_fixed\": 0.92,\n        \"lr_binary_oracle\": 0.84,\n        \"rf_binary_oracle\": 0.82,\n        \"accuracy_zscore\": 0.71,\n        \"min_k_pp\": 0.89,\n        \"ppl_based\": 0.86,\n        \"constat_retest\": 0.83,\n        \"random\": 0.5\n      },\n      \"auroc_25pct\": {\n        \"lz_star_theta_fixed\": 0.94,\n        \"lr_binary_oracle\": 0.92,\n        \"rf_binary_oracle\": 0.91,\n        \"accuracy_zscore\": 0.78,\n        \"min_k_pp\": 0.95,\n        \"ppl_based\": 0.93,\n        \"constat_retest\": 0.91,\n        \"random\": 0.5\n      },\n      \"lz_minus_best_baseline_5pct\": 0.07,\n      \"lz_minus_best_binary_baseline_5pct\": 0.16,\n      \"crossover_point\": \"~20% (Min-K%++ surpasses lz* above 20%)\",\n      \"bootstrap_ci_width_mean\": 0.04,\n      \"information_levels\": {\n        \"binary_only\": [\n          \"lz_star\",\n          \"accuracy_zscore\",\n          \"lr_binary\",\n          \"rf_binary\"\n        ],\n        \"token_probs\": [\n          \"min_k_pp\",\n          \"ppl_based\"\n        ],\n        \"retest_required\": [\n          \"constat_retest\"\n        ]\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: AUROC Comparison Across Contamination Levels (MMLU, averaged over 4 models)\",\n        \"columns\": [\n          \"method\",\n          \"info_level\",\n          \"auroc_5pct\",\n          \"auroc_10pct\",\n          \"auroc_15pct\",\n          \"auroc_25pct\"\n        ],\n        \"rows\": [\n          [\n            \"lz*_θ-fixed\",\n            \"binary\",\n            \"0.78±0.03\",\n            \"0.87±0.03\",\n            \"0.92±0.02\",\n            \"0.94±0.02\"\n          ],\n          [\n            \"Min-K%++\",\n            \"token_probs\",\n            \"0.71±0.04\",\n            \"0.82±0.03\",\n            \"0.89±0.02\",\n            \"0.95±0.01\"\n          ],\n          [\n            \"PPL-based\",\n            \"log_probs\",\n            \"0.68±0.04\",\n            \"0.79±0.03\",\n            \"0.86±0.03\",\n            \"0.93±0.02\"\n          ],\n          [\n            \"ConStat\",\n            \"retest\",\n            \"0.65±0.05\",\n            \"0.76±0.04\",\n            \"0.83±0.03\",\n            \"0.91±0.02\"\n          ],\n          [\n            \"LR (oracle)\",\n            \"binary\",\n            \"0.62±0.05\",\n            \"0.74±0.04\",\n            \"0.84±0.03\",\n            \"0.92±0.02\"\n          ],\n          [\n            \"RF (oracle)\",\n            \"binary\",\n            \"0.59±0.06\",\n            \"0.72±0.04\",\n            \"0.82±0.03\",\n            \"0.91±0.02\"\n          ],\n          [\n            \"Acc z-score\",\n            \"binary\",\n            \"0.55±0.05\",\n            \"0.63±0.04\",\n            \"0.71±0.04\",\n            \"0.78±0.03\"\n          ],\n          [\n            \"Random\",\n            \"—\",\n            0.5,\n            0.5,\n            0.5,\n            0.5\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: lz* Advantage Over Best Baseline at Each Level\",\n        \"columns\": [\n          \"contam_level\",\n          \"best_baseline\",\n          \"best_baseline_auroc\",\n          \"lz_auroc\",\n          \"delta\",\n          \"significant\"\n        ],\n        \"rows\": [\n          [\n            \"5%\",\n            \"Min-K%++\",\n            0.71,\n            0.78,\n            0.07,\n            \"p<0.05\"\n          ],\n          [\n            \"10%\",\n            \"Min-K%++\",\n            0.82,\n            0.87,\n            0.05,\n            \"p<0.05\"\n          ],\n          [\n            \"15%\",\n            \"Min-K%++\",\n            0.89,\n            0.92,\n            0.03,\n            \"p=0.08\"\n          ],\n          [\n            \"25%\",\n            \"Min-K%++\",\n            0.95,\n            0.94,\n            -0.01,\n            \"n.s.\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Best 档的 headline result：lz* 在实际关键的 5-10% 低污染率下无需任何标注数据或 token access 即胜过 supervised baselines 和 token-level methods。这验证了 IRT structure 作为 inductive bias 在 data-scarce regime 的优势。crossover 发生在 ~20%——高于此水平时 Min-K%++ 的 token-level signal 更强，但 20%+ 的污染在实际场景中已经很容易被 accuracy jump 发现。 关键 framing：lz* 在 \\\"检测困难\\\" 的低污染区间胜出，正是 minimal-information 方法最有价值的 regime。\\n\\n\\nlz* 在 5-10% 低污染率胜出所有 baselines（假设 5）的机制：IRT 结构作为 inductive bias。 在低污染率下，signal-to-noise 极低——只有 5-10% 的 items 携带 contamination signal。 ML classifiers（LR/RF）即使有 oracle labels 也面临严重的 class imbalance（5% positive）， 且 binary feature space（0/1 per item）在低 contamination 时几乎不可分。 lz* 的优势来自 IRT model 提供的 structured expectation：它知道每个 item 的 expected P(correct|θ)， 因此即使只有 5% items 被 contaminate，这些 items 上的 \\\"impossible correctness\\\"（高难度 item 被答对） 会被精确捕获为 aberrance。而 ML classifier 只看到 raw 0/1 pattern，缺乏 item difficulty 的先验。 Min-K%++ 在 5% 时 AUROC=0.71 弱于 lz*（0.78）是因为 token-level 信号在极低污染时被 noise 淹没， 但在 20%+ 时 token distribution shift 变得明显，超过 binary-level detection。 accuracy z-score 作为 same-level binary baseline 在所有水平都远不如 lz*—— 它只看 total score 而非 pattern，丢失了 item-level aberrance 信息。 这确立了 IRT structure 作为 binary-only 方法的关键 advantage。\\n\"\n  },\n  {\n    \"name\": \"Post-RL Signal Retention\",\n    \"description\": \"Qwen3.5-9B 上先 SFT 污染（15%）再 GRPO 训练，测试 Δlz* 在 RL 后是否保持。 回应 Wang et al. (2025) 的 MIA 全失效发现。\\n\",\n    \"results\": {\n      \"pre_rl_delta_lz_fixed\": 3.5,\n      \"pre_rl_cohens_d\": -3.95,\n      \"pre_rl_accuracy_contam\": 0.76,\n      \"pre_rl_accuracy_seen\": 0.86,\n      \"post_rl_delta_lz_fixed\": 2.8,\n      \"post_rl_cohens_d\": -3.15,\n      \"post_rl_accuracy_contam\": 0.79,\n      \"post_rl_accuracy_seen\": 0.82,\n      \"signal_retention\": 0.8,\n      \"retention_above_70pct\": true,\n      \"min_k_pp_pre_rl_auroc\": 0.89,\n      \"min_k_pp_post_rl_auroc\": 0.54,\n      \"ppl_pre_rl_auroc\": 0.86,\n      \"ppl_post_rl_auroc\": 0.52,\n      \"lz_star_pre_rl_auroc\": 0.92,\n      \"lz_star_post_rl_auroc\": 0.85,\n      \"seen_accuracy_drop_post_rl\": 0.04,\n      \"unseen_accuracy_gain_post_rl\": 0.03,\n      \"memorization_fraction_post_rl\": 0.34,\n      \"theta_shift_post_rl\": 0.28\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Pre-RL vs Post-RL Detection Comparison\",\n        \"columns\": [\n          \"method\",\n          \"info_level\",\n          \"auroc_pre_rl\",\n          \"auroc_post_rl\",\n          \"retention_pct\"\n        ],\n        \"rows\": [\n          [\n            \"lz*_θ-fixed\",\n            \"binary\",\n            0.92,\n            0.85,\n            \"80%\"\n          ],\n          [\n            \"Min-K%++\",\n            \"token_probs\",\n            0.89,\n            0.54,\n            \"4%\"\n          ],\n          [\n            \"PPL-based\",\n            \"log_probs\",\n            0.86,\n            0.52,\n            \"2%\"\n          ],\n          [\n            \"Acc z-score\",\n            \"binary\",\n            0.71,\n            0.65,\n            \"60%\"\n          ],\n          [\n            \"LR (oracle)\",\n            \"binary\",\n            0.84,\n            0.72,\n            \"56%\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Binary Response Patterns Pre/Post RL\",\n        \"columns\": [\n          \"metric\",\n          \"pre_rl\",\n          \"post_rl\",\n          \"change\"\n        ],\n        \"rows\": [\n          [\n            \"Δlz*_fixed\",\n            3.5,\n            2.8,\n            \"-20%\"\n          ],\n          [\n            \"Cohen's d\",\n            -3.95,\n            -3.15,\n            \"-20%\"\n          ],\n          [\n            \"Seen accuracy\",\n            0.86,\n            0.82,\n            \"-4pp\"\n          ],\n          [\n            \"Unseen accuracy\",\n            0.73,\n            0.76,\n            \"+3pp\"\n          ],\n          [\n            \"Memorization fraction\",\n            0.42,\n            0.34,\n            \"-8pp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"这是论文最强的 selling point 之一。Wang et al. (2025) 证明所有 10 种 log-prob based methods 在 RL 后降至 random，而 lz* 保留 80% 信号。这直接证明了 minimal-information operating point 的 structural advantage：binary patterns 对 RL 是 robust 的，因为 RL 优化的是 generation quality 而非 item-level correctness erasure。paper 可以引用此结果 直接回应 Wang et al. 的 \\\"all methods fail\\\" claim——\\\"all TOKEN-LEVEL methods fail, but BINARY-LEVEL detection survives.\\\"\\n\\n\\nPost-RL signal retention ≥70%（假设 3）成立的核心原因：GRPO 优化的是 reward signal（正确率/格式）， 而非 item-level response distribution。SFT memorization 写入的是 \\\"看到 item X → 输出 answer Y\\\" 的 pattern，这是 parameter-level 的 association。GRPO 的 policy gradient 更新主要影响 reasoning chain 的 token distribution，而 binary correctness 层面的 memorization 痕迹 （hard item 仍然答对）大部分保留。signal 从 3.5 降到 2.8（retention=80%）的 20% 损失来自： (a) RL 训练中少量 seen items 的 memorization 被 \\\"覆盖\\\"（RL 发现了不同的 reasoning path）， (b) RL 普遍提升了 unseen items 的正确率（θ进一步上升），轻微压缩了 seen/unseen gap。 但关键是 binary response 层面的 aberrant pattern 仍然存在——模型在 \\\"不该答对\\\" 的 hard items 上 仍然答对，这个 pattern-level signal 是 RL 无法消除的，因为 RL 没有动机去 \\\"故意答错\\\" 已经答对的题。 相比之下，MIA methods（Min-K%++, PPL）失效是因为 RL 彻底重塑了 token-level distribution—— reasoning tokens 的 perplexity 分布被 GRPO 重新优化，训练数据的 token-level fingerprint 消失。 这是 binary vs token-level detection 的 structural advantage。\\n\"\n  },\n  {\n    \"name\": \"Multiscale lzm Statistic\",\n    \"description\": \"实现 Hong, Lin & Cheng (2021) 的 multiscale lzm——跨 benchmark 聚合的标准化 lz* 总分。 在 PSN-IRT 12 模型和 ctrl-contam 模型上验证。\\n\",\n    \"results\": {\n      \"gemini15_lzm\": 42.8,\n      \"deepseek_v3_lzm\": 38.2,\n      \"yi_lightning_lzm\": 35.6,\n      \"qwen_plus_lzm\": 33.1,\n      \"doubao_pro_lzm\": -8.4,\n      \"mistral_7b_lzm\": 2.1,\n      \"lzm_vs_mean_lz_correlation\": 0.97,\n      \"lzm_flagged_at_alpha005\": \"11/12\",\n      \"ctrl_contam_lzm_clean\": 8.5,\n      \"ctrl_contam_lzm_15pct\": 14.2,\n      \"ctrl_contam_lzm_50pct\": 22.8,\n      \"lzm_cohens_d_15pct\": -4.12,\n      \"lzm_incremental_over_single_benchmark\": \"+0.15 AUROC vs single-best benchmark\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: lzm Scores for PSN-IRT 12 Models\",\n        \"columns\": [\n          \"model\",\n          \"lz_mmlu\",\n          \"lz_hellaswag\",\n          \"lz_gsm8k\",\n          \"lz_arc_c\",\n          \"lz_humaneval\",\n          \"lzm_aggregate\"\n        ],\n        \"rows\": [\n          [\n            \"Gemini-1.5\",\n            31.8,\n            28.4,\n            12.1,\n            6.2,\n            -2.4,\n            42.8\n          ],\n          [\n            \"DeepSeek-V3\",\n            28.6,\n            25.1,\n            10.8,\n            5.8,\n            -1.2,\n            38.2\n          ],\n          [\n            \"Yi-Lightning\",\n            26.4,\n            22.3,\n            9.5,\n            -0.3,\n            -1.8,\n            35.6\n          ],\n          [\n            \"Doubao-Pro\",\n            -12.5,\n            -8.2,\n            4.3,\n            -2.1,\n            -3.8,\n            -8.4\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"lzm 提供了一个 principled 的跨 benchmark 聚合方式，比简单 mean(lz*) 有理论优势 （proper variance weighting）。在 ctrl-contam 中，multi-benchmark contamination 的 lzm 检测力比 single-best benchmark 强 0.15 AUROC，证明了 multiscale 方法的实用价值。 但核心贡献仍是 per-benchmark lz*，lzm 作为 extension/robustness check。\\n\\n\\nlzm 聚合跨 benchmark 信号的原理：如果一个模型在多个 benchmarks 上都表现异常， lzm 将这些独立 signals 标准化后求和，产生比任何单一 benchmark 更强的检测统计量。 在 best 档下，ctrl-contam 跨 3 个 benchmarks 都注入了污染，lzm 的 multi-benchmark aggregation 产生额外的 +0.15 AUROC 增益。对 PSN-IRT 12 模型，lzm 与 mean_lz* 高度相关（r=0.97） 因为大多数模型的 anomaly 在所有 benchmarks 上方向一致（positive direction dominant, 93.3% cells）。 Doubao-pro 的负 lzm 反映其独特的 negative lz* 模式（STEM 和 Humanities domains 特异性不足）。 这是一个 methodological addition（不是核心贡献），但增强了 paper 的 completeness。\\n\"\n  },\n  {\n    \"name\": \"Extra Benchmarks (BBH + MATH)\",\n    \"description\": \"BBH (6,511 items) 和 MATH (5,000 items) 扩展，填充 1K-10K items 的 power gap。 在 ctrl-contam 模型上验证中等规模 benchmark 的检测力。\\n\",\n    \"results\": {\n      \"bbh_theoretical_power_15pct\": 0.88,\n      \"math_theoretical_power_15pct\": 0.82,\n      \"bbh_actual_power_15pct\": 0.85,\n      \"math_actual_power_15pct\": 0.78,\n      \"bbh_cohens_d_15pct\": -3.21,\n      \"math_cohens_d_15pct\": -2.88,\n      \"bbh_memorization_fraction\": 0.4,\n      \"math_memorization_fraction\": 0.36,\n      \"R2_with_new_benchmarks\": 0.968,\n      \"bbh_dose_response_monotonic_theta_fixed\": true,\n      \"math_dose_response_monotonic_theta_fixed\": true,\n      \"bbh_theta_fixed_ratio\": 2.72,\n      \"math_theta_fixed_ratio\": 2.58\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Extended Power Function Validation\",\n        \"columns\": [\n          \"benchmark\",\n          \"n_items\",\n          \"theoretical_power_15pct\",\n          \"actual_power_ctrl\",\n          \"cohens_d_15pct\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            14042,\n            0.985,\n            0.92,\n            -3.95\n          ],\n          [\n            \"HellaSwag\",\n            10042,\n            0.753,\n            0.71,\n            -2.64\n          ],\n          [\n            \"BBH\",\n            6511,\n            0.88,\n            0.85,\n            -3.21\n          ],\n          [\n            \"MATH\",\n            5000,\n            0.82,\n            0.78,\n            -2.88\n          ],\n          [\n            \"GSM8K\",\n            1319,\n            0.59,\n            0.55,\n            -1.42\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"BBH 和 MATH 的加入完善了 power function 的中间区段验证。5 个 benchmarks 覆盖了 1.3K 到 14K items 的完整范围，R²=0.968 确认 power 与 √n 的理论关系在实际 ctrl-contam 中成立。 这直接支撑 Claim 2 的核心论断：detection power is a predictable function of benchmark size。\\n\\n\\nBBH（6511 items）和 MATH（5000 items）填充了 GSM8K（1319）和 MMLU（14042）之间的 gap。 在 best 档下，两者都产生显著检测信号：BBH 因为 items 多且区分度高（BIG-Bench Hard 的 items 被设计为 challenging），theoretical power 接近 90%；MATH 的 items 更结构化（数学题）， memorization fraction 稍低（0.36 vs 0.40）因为数学题的 SFT 更容易产生 generalization 而非 verbatim memorization。两者的加入使 power function 的 R² 从 0.957 提升到 0.968， 进一步验证了 Claim 2 的 power ∝ f(n_items) 关系。这些中等规模 benchmarks 是实际应用中最常见的尺寸范围（多数 benchmarks 在 1K-10K 之间），因此验证至关重要。\\n\"\n  },\n  {\n    \"name\": \"Natural Experiment (base→chat pairs)\",\n    \"description\": \"v1 leaderboard base→chat model pairs 计算 Δlz* = lz*(chat) - lz*(base) 作为 SFT 效应代理。\\n\",\n    \"results\": {\n      \"n_pairs\": 21,\n      \"n_complete_pairs\": 9,\n      \"hellaswag_systematic_effect\": {\n        \"mean_deviation\": -3.8,\n        \"t_stat\": -4.2,\n        \"p_value\": 0.0008,\n        \"direction\": \"SFT decreases person-fit\"\n      },\n      \"gsm8k_systematic_effect\": {\n        \"mean_deviation\": 4.5,\n        \"t_stat\": 3.8,\n        \"p_value\": 0.004,\n        \"direction\": \"SFT increases person-fit\"\n      },\n      \"mmlu_effect\": {\n        \"p_value\": 0.12,\n        \"direction\": \"non-significant\"\n      },\n      \"arc_c_effect\": {\n        \"p_value\": 0.31,\n        \"direction\": \"non-significant\"\n      },\n      \"individual_outlier_pairs\": 1,\n      \"outlier_model\": \"codellama-34b-instruct\",\n      \"outlier_benchmark\": \"GSM8K\",\n      \"outlier_delta_lz\": 8.7\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Systematic SFT Effects on lz* (base→chat)\",\n        \"columns\": [\n          \"benchmark\",\n          \"n_pairs\",\n          \"mean_Δlz\",\n          \"t_stat\",\n          \"p_value\",\n          \"interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"HellaSwag\",\n            9,\n            -3.8,\n            -4.2,\n            0.0008,\n            \"SFT improves commonsense (less aberrant)\"\n          ],\n          [\n            \"GSM8K\",\n            9,\n            4.5,\n            3.8,\n            0.004,\n            \"Math SFT creates new aberrance patterns\"\n          ],\n          [\n            \"MMLU\",\n            9,\n            1.8,\n            1.7,\n            0.12,\n            \"n.s.\"\n          ],\n          [\n            \"ARC-C\",\n            9,\n            0.9,\n            1.1,\n            0.31,\n            \"n.s.\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"P2-optional 实验。提供了 real-world SFT 效应的 converging evidence，但受限于 a_r=0.111 的 discrimination failure。在 paper 中作为 supplementary finding 而非 primary evidence。\\n\\n\\nBest 档下 natural experiment 的结果比 registry 中的实际结果稍强：HellaSwag 和 GSM8K 显示更清晰的 systematic SFT effect（p<0.001 和 p<0.005），且出现一个 individual outlier （codellama-34b-instruct 在 GSM8K 上 Δlz*=8.7，远超 group mean）。这个 outlier 的出现是 best 档独有的——它提供了 \\\"自然实验中发现疑似污染\\\" 的 case study evidence。 HellaSwag 的 negative shift 解释：chat SFT 训练中包含了对话/常识推理数据， 这些与 HellaSwag 的 commonsense completion task 有 domain overlap，导致泛化性提升 但 pattern 变得 less aberrant（更符合 IRT 预测）。GSM8K positive shift： chat 模型的 math instruction tuning 不是 benchmark-specific memorization 而是 reasoning capability，但少数模型可能直接接触了 GSM8K items。 由于 a_r=0.111 的 discrimination failure，此实验只能作为 converging evidence，不是 primary claim。\\n\"\n  },\n  {\n    \"name\": \"V1 IRT Refit Expanded (N=178)\",\n    \"description\": \"扩大 v1 IRT 重拟合样本量至 N≥178，最终验证 Path D（large-scale audit）是否可行。\\n\",\n    \"results\": {\n      \"n_models\": 178,\n      \"n_items\": 14042,\n      \"3pl_a_pearson_r\": 0.13,\n      \"2pl_a_pearson_r\": -0.03,\n      \"3pl_b_pearson_r\": 0.66,\n      \"a_r_below_threshold\": true,\n      \"conclusion\": \"Path D confirmed dead. Classical MML-EM cannot recover IRT discrimination from LLM response data at available sample sizes.\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: IRT Parameter Recovery (Classical vs PSN-IRT)\",\n        \"columns\": [\n          \"method\",\n          \"N_models\",\n          \"a_pearson_r\",\n          \"b_pearson_r\",\n          \"conclusion\"\n        ],\n        \"rows\": [\n          [\n            \"MML-EM 3PL (N=63)\",\n            63,\n            0.111,\n            0.626,\n            \"a failure\"\n          ],\n          [\n            \"MML-EM 3PL (N=178)\",\n            178,\n            0.13,\n            0.66,\n            \"a failure persists\"\n          ],\n          [\n            \"PSN-IRT (neural)\",\n            12,\n            \"validated\",\n            \"validated\",\n            \"reference standard\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Path D 的确定性关闭是 paper structure 的关键节点。它确立了 \\\"why ctrl-contam, not leaderboard audit\\\" 的 methodological justification，并为 Future Work 中的 \\\"neural IRT at scale\\\" 提供了动机。\\n\\n\\n即使在 best 档，Path D（leaderboard-scale audit via classical IRT refit）仍然失败。 这不是 experiment failure 而是 honest negative result：classical IRT estimation 需要 hundreds of examinees with similar ability distributions，而 LLM response data 的特殊性（模型间 ability range 极大，item response 非 locally independent） 使得 MML-EM 无法恢复 discrimination parameters。a_r=0.13 << 0.4 threshold 确认 discriminability failure 不是样本量问题而是 structural incompatibility。 这本身是 Claim 3(c) 的贡献：quantifying the estimation challenge for neural IRT。\\n\"\n  },\n  {\n    \"name\": \"4PL vs 3PL Ablation\",\n    \"description\": \"4PL vs 3PL(d=1) 消融实验：量化 d 参数对检测灵敏度的影响。\\n\",\n    \"results\": {\n      \"mean_power_gain_4pl_vs_3pl\": {\n        \"MMLU\": \"+28pp\",\n        \"HellaSwag\": \"+27pp\",\n        \"GSM8K\": \"+21pp\",\n        \"ARC_C\": \"+15pp\",\n        \"HumanEval\": \"+14pp\"\n      },\n      \"far_4pl\": 0.05,\n      \"far_3pl\": \"0.05-0.17 (inflated)\",\n      \"far_2pl\": \"0.50-1.00 (catastrophic)\",\n      \"items_with_d_lt_095_mmlu\": \"46%\",\n      \"ctrl_contam_4pl_d_15pct\": -3.95,\n      \"ctrl_contam_3pl_d_15pct\": -1.82,\n      \"power_loss_without_d\": \"54%\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: 4PL vs 3PL Detection Performance\",\n        \"columns\": [\n          \"benchmark\",\n          \"n_items\",\n          \"power_4pl_25pct\",\n          \"power_3pl_25pct\",\n          \"gain\",\n          \"pct_items_d_lt_095\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            14042,\n            0.776,\n            0.329,\n            \"+44.7pp\",\n            \"46%\"\n          ],\n          [\n            \"HellaSwag\",\n            10042,\n            0.534,\n            0.28,\n            \"+25.4pp\",\n            \"38%\"\n          ],\n          [\n            \"GSM8K\",\n            1319,\n            0.73,\n            0.334,\n            \"+39.6pp\",\n            \"42%\"\n          ],\n          [\n            \"ARC-C\",\n            295,\n            0.132,\n            0.091,\n            \"+4.1pp\",\n            \"29%\"\n          ],\n          [\n            \"HumanEval\",\n            164,\n            0.318,\n            0.165,\n            \"+15.3pp\",\n            \"35%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"4PL ablation 是 methodological rigor 的体现。Reviewer 可能质疑 \\\"为什么不用更简单的 3PL\\\"， 此实验给出定量答案：+28pp average power gain，54% signal loss without d。 结合 exp-4pl-real-data-degradation（r=0.225 between 4PL/3PL lz*）， establishes 4PL 作为 LLM person-fit 的 minimum viable parameterization。\\n\\n\\n4PL 的 d 参数（upper asymptote）对高能力 LLM 至关重要：当 d<1 时，P(correct) 的上限低于 1.0， 高能力模型在这些 items 上 \\\"应该\\\" 答错（按 4PL 预测）。如果忽略 d（设 d=1）， model 预测所有高能力模型都应该答对所有题——这会让 few errors 变成 extreme aberrance（false alarm）。 MMLU 46% items 有 d<0.95 意味着将近一半的题目有上限效应，忽略这些会产生巨大的 FAR 膨胀。 在 best 档下，ctrl-contam 进一步确认：同一污染实验用 3PL 分析时 |d| 从 3.95 降到 1.82， 因为 3PL 的 inflated null variance 稀释了真实信号。这证明 4PL 不是 \\\"nice-to-have\\\" 而是 LLM person-fit 分析的 necessary condition。\\n\"\n  },\n  {\n    \"name\": \"Baseline Comparison — Accuracy Z-Score (completed)\",\n    \"description\": \"Accuracy z-score 作为 same-level binary-only baseline 的扩展对比， 整合入完整 baseline comparison 实验中。\\n\",\n    \"results\": {\n      \"acc_zscore_auroc_5pct\": 0.55,\n      \"acc_zscore_auroc_10pct\": 0.63,\n      \"acc_zscore_auroc_15pct\": 0.71,\n      \"acc_zscore_auroc_25pct\": 0.78,\n      \"lz_star_advantage_over_zscore_5pct\": \"+0.23 AUROC\",\n      \"lz_star_advantage_over_zscore_15pct\": \"+0.21 AUROC\",\n      \"lz_star_advantage_over_zscore_25pct\": \"+0.16 AUROC\"\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Accuracy z-score 是 \\\"straw-man\\\" 但也是 fair comparison：它是唯一的 same-information-level baseline （binary only, no training data）。lz* 的 consistent +0.16-0.23 AUROC advantage 直接证明 IRT item parameters 提供了有价值的 structural information。\\n\\n\\nAccuracy z-score 只利用 total score（sum of binary responses）而丢失所有 item-level pattern information。lz* 的优势正来自于 item-level aberrance detection： 它区分 \\\"总分高因为答对了该对的题\\\" vs \\\"总分高因为答对了不该对的题\\\"。 在 5% 低污染时，只有 ~700 items（14042×5%）被 contaminate，total score change 微乎其微 （+2-3 pp accuracy），z-score 几乎无法检测。但 lz* 能捕捉到这 700 items 中的 \\\"不可能正确\\\" 模式。 这是 \\\"IRT structure as inductive bias\\\" 的最直接证明。\\n\"\n  },\n  {\n    \"name\": \"Domain-Level Analysis\",\n    \"description\": \"MMLU domain-level 分析：按 subject category 分别计算 person-fit，识别污染的 domain 分布。\\n\",\n    \"results\": {\n      \"gemini_subjects_flagged\": \"50/57 (87.7%)\",\n      \"gemini_contamination_uniform\": true,\n      \"gemini_category_lz_range\": [\n        15.3,\n        21.2\n      ],\n      \"ctrl_contam_domain_uniformity\": \"uniform (as expected, since QLoRA trains on random 15% sample)\",\n      \"ctrl_contam_stem_lz\": 3.8,\n      \"ctrl_contam_humanities_lz\": 3.3,\n      \"ctrl_contam_social_sci_lz\": 3.5,\n      \"ctrl_contam_other_lz\": 3.2,\n      \"doubao_selective_domains\": true,\n      \"doubao_negative_pattern\": \"STEM and Humanities strongly negative, Other positive\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: MMLU Domain-Level lz* (Gemini-1.5 vs Ctrl-Contam)\",\n        \"columns\": [\n          \"domain\",\n          \"gemini_lz\",\n          \"ctrl_contam_15_lz\",\n          \"ctrl_contam_clean_lz\"\n        ],\n        \"rows\": [\n          [\n            \"STEM\",\n            21.2,\n            3.8,\n            0.1\n          ],\n          [\n            \"Humanities\",\n            17.9,\n            3.3,\n            -0.2\n          ],\n          [\n            \"Social Sciences\",\n            15.9,\n            3.5,\n            0.0\n          ],\n          [\n            \"Other\",\n            15.3,\n            3.2,\n            0.1\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Domain analysis 提供了 contamination 的 \\\"spatial resolution\\\"：从 aggregate model-level detection 到 domain-level localization。在 paper 中服务于两个目的：(a) 验证 ctrl-contam 内部一致性 （random sampling → uniform signal），(b) case study 中展示不同 contamination type 的 domain fingerprint。\\n\\n\\nDomain analysis 在 best 档下产生两个 clear findings：(1) Gemini-1.5 的 contamination 是 uniform across domains（所有 subject 都被 memorize），consistent with \\\"bulk training data leak\\\" 而非 \\\"selective domain tuning\\\"；(2) ctrl-contam 模型的 domain-level signal 也是 uniform （因为 QLoRA 训练样本是 randomly sampled across all subjects），验证了实验设计的 internal consistency。 Doubao 的 selective negative pattern 则展示了不同类型的 anomaly：可能是 domain-specific training data 导致某些 domains 泛化过强（lz*<0 = over-consistent pattern）。\\n\"\n  },\n  {\n    \"name\": \"Leaderboard Audit (Abandoned)\",\n    \"description\": \"Open LLM Leaderboard v1 大规模 13K+ 模型扫描。因 IRT refit failure 放弃。\\n\",\n    \"results\": {\n      \"status\": \"ABANDONED\",\n      \"reason\": \"a_r=0.111 discrimination failure makes lz* degenerate to accuracy-like metric at scale\",\n      \"paper_treatment\": \"Data availability noted in Discussion/Future Work; 13K+ per-item data available for future neural IRT estimation\"\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"ABANDONED。在 paper 中转化为 methodological contribution：量化了 classical vs neural IRT 在 LLM context 中的 gap，为 future work 提供了 concrete roadmap（13K+ data available, awaiting better estimation methods）。\\n\\n即使在 best 档，leaderboard audit 仍然 abandoned。这不影响 best 档的叙事， 因为 ctrl-contam 提供了比 leaderboard audit 更强的 ground-truth validation。 Audit 的 abandonment 本身是 honest negative result (Claim 3c)：classical IRT 的 sample size requirement 与 LLM evaluation ecosystem 不兼容。 Paper 中将其定位为 \\\"future work when neural IRT estimation at scale becomes feasible\\\"。\\n\"\n  }\n]",
      "numLines": 1066,
      "startLine": 1,
      "totalLines": 1066
    }
  },
  "sourceToolAssistantUUID": "c22630af-1a38-47d4-8e10-f4019fda80b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-20T19:22:28.205Z_

<details><summary>↩ Tool result · `toolu_01JxWdFwFH6hRNN4Rw4nXYFj`</summary>

```text
1	# Paper Framing — irt_personfit_contam
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (用户确认；ARR submission DDL 5/25 — 需确认可行性)
5	- Fallback: AAAI 2027 (abstract 7/21, full paper 7/28, ~10 weeks)
6	- Backup: ICLR 2027 (~Sep 2026, ~17 weeks)
7	
8	## Core Claims (3 条)
9	
10	**Claim 1 (Minimal-Information Detection Framework + Controlled Validation)**:
11	IRT person-fit statistics provide a principled contamination detection framework at the minimal-information operating point — requiring only binary response patterns. Simulation establishes high theoretical detection power (97.9% on MMLU-scale benchmarks), and bootstrap null distributions are well-calibrated (near-perfect N(0,1) for large benchmarks, KS reject rate 8.3%). In simulation, lz* matches or outperforms supervised binary classifiers (LR/RF with oracle labels) at low contamination (5-10%), leveraging IRT structure as inductive bias. Controlled contamination experiments (QLoRA SFT injection on Qwen2.5-7B-Instruct) validate the framework on real models: at 15% contamination, |Cohen's d|=3.85 with clear seen/unseen memorization fingerprint (seen lz*≈0 vs unseen=3.1). θ-fixed analysis reveals a θ-shift boundary condition: when θ is re-estimated on contaminated data, detection sensitivity degrades at high contamination (50%), but fixing θ to pre-contamination baseline restores monotonic dose-response (ratio=2.93). The memorization fraction (~38% at 15% contamination) quantifies the SFT generalization effect — the gap between theoretical power and actual detection signal.
12	
13	**Claim 2 (Detection Characterization)**:
14	Detection power is a predictable function of benchmark size (n_items) and contamination level, with two distinct signal regimes: partial contamination produces aberrant patterns (lz* << 0), full contamination produces over-consistent patterns (lz* >> 0). For sufficiently large benchmarks (≥10K items), theoretical power exceeds 90% at 15% contamination. Note: power function gives an **upper bound** (assumes all contaminated items produce aberrant signal); SFT generalization reduces effective signal — ctrl-contam measures actual memorization fraction to derive adjusted ("expected") power. Both upper bound and adjusted power should be reported.
15	
16	**Claim 3 (Empirical Findings from Real LLM Data)**:
17	Three empirical findings from applying IRT person-fit to real LLM response data: (a) **Universal 4PL model misfit** — nearly all (model, benchmark) cells produce extreme lz* values (|lz*| >> 5, 57/60 cells flagged after BH-FDR correction), revealing that LLM response patterns fundamentally differ from classical test-taker patterns. This is a genuine property of LLM responses (bootstrap null is well-calibrated), not a statistical artifact. The simulation-to-reality gap motivates the Δlz* design. (b) **PSN-IRT 12-model case study** — detailed anomaly profiles with validated 4PL parameters (Gemini-1.5: 100% MMLU accuracy, lz*=+34.75, θ=0.78; selective vs uniform misfit patterns across benchmarks; Ward clustering reveals contamination typology). (c) **IRT parameter estimation challenges** — MML-EM refit from v1 leaderboard data (N=63→178, covering all available models) yields b_r=0.66 (partial difficulty validation) but a_r≈0.13 (discrimination failure, well below 0.2 threshold), quantifying the sample size gap between classical IRT and neural IRT estimation in LLM contexts. 13K+ model per-item data is publicly available for future large-scale audits once estimation challenges are resolved.
18	
19	## Story Spine
20	
21	**Problem**: Benchmark contamination undermines LLM evaluation reliability. As benchmarks proliferate and training corpora grow, contamination risk increases, but all existing detection methods require privileged access — training data (n-gram overlap), token probabilities (Min-K%, MIA), model weights (internal probing), or specially crafted prompts (Time Travel). A contaminated LLM is functionally analogous to an examinee with item preknowledge, yet no work has connected the mature psychometric literature on cheating detection to LLM benchmark integrity.
22	
23	**Existing approaches & gaps**: Detection methods circa 2026 span five families: time-based partition, MIA/Min-K%++ (ICLR 2024), Time Travel probing (ICLR 2024 Spotlight), ConStat performance-based testing (NeurIPS 2024), and CoDeC in-context learning effects (ICLR 2026). Wang et al. (2025) show all MIA-based methods fail under post-RL contamination. Critically, ALL require more than binary response patterns — no method operates at the minimal-information level.
24	
25	**Our framing**: We establish the minimal-information operating point on the contamination detection frontier. By repurposing IRT person-fit statistics — developed over decades for detecting exam cheating — we ask: "What can be detected from binary response patterns alone?" We show: (1) in simulation, person-fit statistics achieve high detection power (97.9% on MMLU-scale benchmarks) with well-calibrated null distributions; (2) in real LLM data, response patterns universally deviate from 4PL predictions — the statistical framework is sound, but LLMs genuinely violate IRT assumptions (local independence, unidimensionality), producing extreme lz* values across nearly all models; (3) controlled contamination experiments leverage this by measuring Δlz* between clean and contaminated models — since the null is well-calibrated, within-model shifts are statistically interpretable. The universal model misfit finding is itself a contribution — it reveals that LLM response patterns are fundamentally different from classical test-taker patterns.
26	
27	**Headline result template**: "Using only binary response patterns, IRT-FIT achieves 97.9% simulated detection power on MMLU (14K items) with well-calibrated null distributions. In simulation, lz* matches or outperforms supervised binary classifiers (LR/RF with oracle labels) at practically relevant low contamination levels (5-10%), leveraging IRT structure as an inductive bias that compensates for the absence of labeled data. While all LLMs exhibit universal 4PL model misfit (a finding in itself), controlled experiments show contamination induces a measurable Δlz* shift of X SD above each model's baseline misfit, enabling detection even in the presence of universal misfit."
28	
29	## Venue Fit Risks
30	
31	- **EMNLP**: NLP evaluation methodology fits well. Risk: "no new NLP model/technique" → mitigate by positioning as foundational evaluation methodology with direct community impact (leaderboard integrity).
32	- **AAAI**: PSN-IRT was AAAI 2026 Oral — strong psychometrics+AI audience. Risk: less NLP-specific reviewer pool.
33	- **Cross-discipline concern**: IRT/psychometrics may be unfamiliar to ML reviewers → need self-contained exposition in Section 3 (IRT background), avoid jargon, provide intuitive explanations.
34	
35	## Anticipated Reviewer Concerns & Planned Responses
36	
37	| # | Concern | Response Strategy | Supporting Experiment |
38	|---|---------|------------------|----------------------|
39	| R1 | "Just applying existing IRT to LLMs" | Frame as establishing new operating point, not cross-domain transfer. Person-fit for contamination is unexplored. Downgrade "cross-domain" from contribution to background. | — |
40	| R2 | "No ground truth contamination labels" | Controlled contamination experiment (fine-tune clean models on benchmark items). Phase B anomalies are converging evidence, not proof. | exp-ctrl-contam |
41	| R3 | "Power too low for small benchmarks" | Present power function analysis as contribution, not limitation. Derive theoretical relationship. | exp-power-theory |
42	| R4 | "Only 12 models" | 12 models with validated 4PL parameters provide detailed anomaly profiles. Universal misfit (57/60 flagged) spans sufficient models to establish the pattern. 13K+ v1 per-item data availability discussed as future work. Ctrl-contam covers 4-5 model families. | exp-ctrl-contam, phase_b_personfit |
43	| R5 | "SFT generalization smooths signal" | Controlled experiment includes domain-level analysis. Discuss hard-item contamination resistance. | exp-ctrl-contam |
44	| R6 | "Absolute lz* thresholds don't work on real data" | Bootstrap null is well-calibrated (KS pass for large benchmarks); the issue is LLMs genuinely deviate from 4PL. Universal model misfit is a finding, not an artifact. Δlz* leverages the well-calibrated null for within-model comparisons. | exp-ctrl-contam, exp-empirical-null |
45	| R7 | "Post-RL contamination?" | Hypothesis test: GRPO after SFT contamination on Qwen 3.5-9B. | exp-post-rl |
46	| R8 | "4PL vs 3PL — does d parameter matter?" | Ablation comparing 4PL vs 3PL(d=1) detection sensitivity. | exp-4pl-ablation |
47	| R9 | "No same-level binary-only baselines" | accuracy z-score (done, lz* dominates 57/60 vs 4/60) + ML classifier on binary vectors (simulation train, ctrl-contam test). lz* advantage: per-cell statistic needing no training data. | exp-accuracy-zscore-baseline, exp-ml-classifier-baseline |
48	| R10 | "Leaderboard audit baseline unreliable" | Leaderboard audit abandoned (D011). ctrl-contam is the validated detection. 12-model case study uses PSN-IRT validated parameters directly (no baseline estimation needed). v1 data availability noted as future work. | exp-ctrl-contam |
49	| R11 | "Power function is upper bound" | Report both theoretical upper bound AND adjusted power (memorization fraction from ctrl-contam seen/unseen split). Gap = SFT generalization effect quantification. | exp-ctrl-contam, exp-power-theory |
50	
51	## Key Narrative Elements (from External Review + Distillation)
52	
53	1. **Detection frontier framing** — Systematically rank all methods by information access level (binary < rephrased retest < token probs < logits < weights). IRT-FIT defines the bottom of this frontier.
54	2. **Definitional pivot (à la ConStat)** — "All prior contamination detection methods require privileged access. We ask a more fundamental question: what can be detected from binary response patterns alone?" This reframes our work as problem reformulation, not just cross-domain transfer.
55	3. **RL-robustness as structural advantage** — Wang et al. (ICLR 2026) proves all 10 log-prob methods ≈ random on RL-trained reasoning models. Person-fit operates on binary response patterns, not token distributions — structurally immune to RL-induced distributional shifts. This is our strongest motivation against log-prob baselines.
56	4. **Scalability potential (deferred to future work)** — 13K+ v1 per-item data publicly available. IRT-FIT is uniquely suited for retrospective audit (only needs archival binary data). BUT: current paper does NOT include large-scale audit (D011: IRT refit failed). Mention data availability + roadmap in Discussion/Future Work. NEVER claim "leaderboard audit" or "large-scale detection" in current paper.
57	5. **Inverted-U as theoretical characterization** — Not just empirical observation. Derive from: (a) contamination→0%: signal drowned in sampling noise; (b) contamination→100%: identifiability collapse. Theory gives R²=0.957 fit.
58	6. **Scope precision** — Target: "intentional SFT contamination / leaderboard gaming". Pretraining exposure → smooth distributional improvement, not in scope. Honest scoping > vague claims.
59	7. **Terminology guard** — NEVER use "binary information bottleneck" or "information-theoretic lower bound for all binary-only methods." We can only claim lz* (a specific statistic) has limitations under SFT generalization — NOT that all binary-only methods fail. Correct framing: "IRT person-fit as a principled framework at the minimal-information operating point."
60	8. **Validation hierarchy** — ctrl-contam = primary validation (ground truth, same model clean vs contaminated); 12-model case study = empirical findings (no ground truth, but validated parameters); v1 data = future work roadmap. Paper structure should reflect this priority.
61	9. **lz* measures memorization, not generalization** — lz* detects aberrant patterns (memorization signature), not smooth ability improvement (generalization). This is a feature: it distinguishes genuine learning from rote memorization. Power function gives upper bound; ctrl-contam measures actual memorization fraction.
62	10. **Negative results as contributions** — D007 (universal misfit) and D008 (empirical null well-calibrated) are "honest negative results that become positive contributions": universal misfit is a novel finding about LLM response patterns; the simulation-reality gap motivates Δlz* and quantifies SFT generalization. D011 (MML-EM refit failure) is a methodological caveat (classical vs neural IRT sample requirements). D009 (item alignment) is a data engineering detail (1 sentence in Data section). Present negatives with the framing: "the gap between where IRT works perfectly (simulation) and where it struggles (real LLM data) is itself informative."
63	11. **ctrl-contam actual results (D015)** — contam_15 |d|=3.85 (strong), contam_50 non-monotonic under free-θ but **monotonic under θ-fixed** (ratio=2.93). θ-shift is the mechanism: contamination→higher θ_MLE→absorbs aberrance signal. Frame as "principled detection with quantified operating characteristics + θ-shift boundary condition." Headline: "We don't just detect — we characterize, including the conditions under which detection degrades." Do NOT claim "state-of-the-art detection."
64	12. **θ-shift as methodological contribution (D015)** — Person-fit sensitivity degrades when θ is re-estimated on contaminated data. This is a novel finding for contamination detection: (a) θ-fixed analysis recovers monotonic dose-response, (b) the θ-shift magnitude (0.47 at 50% contamination) quantifies the confound, (c) practical implication: use pre-contamination θ baseline or cross-validated θ. Present as a contribution, not a limitation.
65	13. **seen/unseen split as strongest signal** — contam_15 seen lz*≈0 (memorized items look "normal") vs unseen lz*=3.1. This is the clearest contamination fingerprint: items that should produce aberrant responses instead produce expected responses. More interpretable than aggregate Δlz*.
66	
67	## Writing Strategy (from Distillation)
68	
69	- **Story type**: "跨界迁移型" — unused in 0/8 peer papers. Our unique angle.
70	- **Figure 1**: Problem illustration (dual-panel: contaminated vs clean response pattern). Use psychometric hook — impossible response pattern (hard items right, easy wrong).
71	- **Contribution structure**: 3 contributions (method + characterization + empirical findings), escalating scope. Standard in 5/8 papers.
72	- **Result tables**: Row=methods, col=datasets×metrics. Bold-best. Average column.
73	- **Numbered findings**: Adopt PSN-IRT's "Key Discoveries" strategy for scannable presentation.
74	- **CIs as differentiator**: 6/8 peer papers report no variance. Our bootstrap CIs are a competitive advantage.
75	- **Baseline count**: Peer median ~5. Target ≥5 baselines.
76	
77	## Evidence Summary
78	
79	- **Phase A (simulation)**: Null check passed (4PL compatible with lz* theory). MMLU power@15%=97.9%. Power ∝ n_items confirmed. Simulation results stand — they establish theoretical detection capacity within the 4PL model.
80	- **Phase B (real data)**: Gemini-1.5 MMLU acc=1.000, θ=0.78, lz*=+34.75. Cross-benchmark anomaly profiles identified.
81	- **Empirical null analysis (exp-empirical-null)**: Bootstrap null distributions are well-calibrated — MMLU null mean bias 0.041, std 1.003, KS reject 8.3%. The statistical framework is sound. 57/60 real-data cells flagged because LLM lz* values are genuinely extreme (|lz*| >> 5), not because of null miscalibration. Universal 4PL model misfit is a real property of LLM response patterns.
82	- **Calibration gap reframed (D007→D008)**: The gap is not "null is biased" but "real LLM data genuinely deviates from 4PL". This strengthens Δlz* approach: well-calibrated null means within-model shifts are statistically meaningful.
83	- **Controlled contamination (exp-ctrl-contam-pilot, D015)**: Qwen2.5-7B-Instruct × MMLU, 4 conditions (0%×2 seeds, 15%, 50%). Key results: (a) contam_15 |Cohen's d|=3.85 (strong detection signal); (b) free-θ dose-response non-monotonic (contam_50 Δlz*=1.53 < contam_15 Δlz*=3.97) due to θ-shift confound; (c) **θ-fixed analysis restores monotonicity** (Δlz*_fixed: contam_15=+2.96, contam_50=+8.67, ratio=2.93); (d) seen/unseen split: contam_15 seen lz*≈0 vs unseen=3.1 (clear memorization fingerprint); (e) memorization_fraction=0.38 (15%) and 0.29 (50%). θ-shift mechanism: contamination raises θ_MLE, absorbing aberrance signal — this is a methodological contribution.
84	- **4PL real-data degradation**: 3PL(d=1) vs 4PL lz* correlation r=0.225, RMSE=68.41. d parameter essential for high-ability models (DeepSeek-V3 Δ=357). Complements simulation ablation (+14-27pp power gain).
85	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60999672-183f-459d-8674-1c2cdd67dbe1",
  "isSidechain": false,
  "promptId": "eb66b833-472c-4a64-b5b3-e6647c252907",
  "type": "user",
  "uuid": "95347878-5e7d-473d-8584-3f6a5be88b0f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best/paper_framing.md",
      "content": "# Paper Framing — irt_personfit_contam\n\n## Target Venue\n- Primary: EMNLP 2026 Main (用户确认；ARR submission DDL 5/25 — 需确认可行性)\n- Fallback: AAAI 2027 (abstract 7/21, full paper 7/28, ~10 weeks)\n- Backup: ICLR 2027 (~Sep 2026, ~17 weeks)\n\n## Core Claims (3 条)\n\n**Claim 1 (Minimal-Information Detection Framework + Controlled Validation)**:\nIRT person-fit statistics provide a principled contamination detection framework at the minimal-information operating point — requiring only binary response patterns. Simulation establishes high theoretical detection power (97.9% on MMLU-scale benchmarks), and bootstrap null distributions are well-calibrated (near-perfect N(0,1) for large benchmarks, KS reject rate 8.3%). In simulation, lz* matches or outperforms supervised binary classifiers (LR/RF with oracle labels) at low contamination (5-10%), leveraging IRT structure as inductive bias. Controlled contamination experiments (QLoRA SFT injection on Qwen2.5-7B-Instruct) validate the framework on real models: at 15% contamination, |Cohen's d|=3.85 with clear seen/unseen memorization fingerprint (seen lz*≈0 vs unseen=3.1). θ-fixed analysis reveals a θ-shift boundary condition: when θ is re-estimated on contaminated data, detection sensitivity degrades at high contamination (50%), but fixing θ to pre-contamination baseline restores monotonic dose-response (ratio=2.93). The memorization fraction (~38% at 15% contamination) quantifies the SFT generalization effect — the gap between theoretical power and actual detection signal.\n\n**Claim 2 (Detection Characterization)**:\nDetection power is a predictable function of benchmark size (n_items) and contamination level, with two distinct signal regimes: partial contamination produces aberrant patterns (lz* << 0), full contamination produces over-consistent patterns (lz* >> 0). For sufficiently large benchmarks (≥10K items), theoretical power exceeds 90% at 15% contamination. Note: power function gives an **upper bound** (assumes all contaminated items produce aberrant signal); SFT generalization reduces effective signal — ctrl-contam measures actual memorization fraction to derive adjusted (\"expected\") power. Both upper bound and adjusted power should be reported.\n\n**Claim 3 (Empirical Findings from Real LLM Data)**:\nThree empirical findings from applying IRT person-fit to real LLM response data: (a) **Universal 4PL model misfit** — nearly all (model, benchmark) cells produce extreme lz* values (|lz*| >> 5, 57/60 cells flagged after BH-FDR correction), revealing that LLM response patterns fundamentally differ from classical test-taker patterns. This is a genuine property of LLM responses (bootstrap null is well-calibrated), not a statistical artifact. The simulation-to-reality gap motivates the Δlz* design. (b) **PSN-IRT 12-model case study** — detailed anomaly profiles with validated 4PL parameters (Gemini-1.5: 100% MMLU accuracy, lz*=+34.75, θ=0.78; selective vs uniform misfit patterns across benchmarks; Ward clustering reveals contamination typology). (c) **IRT parameter estimation challenges** — MML-EM refit from v1 leaderboard data (N=63→178, covering all available models) yields b_r=0.66 (partial difficulty validation) but a_r≈0.13 (discrimination failure, well below 0.2 threshold), quantifying the sample size gap between classical IRT and neural IRT estimation in LLM contexts. 13K+ model per-item data is publicly available for future large-scale audits once estimation challenges are resolved.\n\n## Story Spine\n\n**Problem**: Benchmark contamination undermines LLM evaluation reliability. As benchmarks proliferate and training corpora grow, contamination risk increases, but all existing detection methods require privileged access — training data (n-gram overlap), token probabilities (Min-K%, MIA), model weights (internal probing), or specially crafted prompts (Time Travel). A contaminated LLM is functionally analogous to an examinee with item preknowledge, yet no work has connected the mature psychometric literature on cheating detection to LLM benchmark integrity.\n\n**Existing approaches & gaps**: Detection methods circa 2026 span five families: time-based partition, MIA/Min-K%++ (ICLR 2024), Time Travel probing (ICLR 2024 Spotlight), ConStat performance-based testing (NeurIPS 2024), and CoDeC in-context learning effects (ICLR 2026). Wang et al. (2025) show all MIA-based methods fail under post-RL contamination. Critically, ALL require more than binary response patterns — no method operates at the minimal-information level.\n\n**Our framing**: We establish the minimal-information operating point on the contamination detection frontier. By repurposing IRT person-fit statistics — developed over decades for detecting exam cheating — we ask: \"What can be detected from binary response patterns alone?\" We show: (1) in simulation, person-fit statistics achieve high detection power (97.9% on MMLU-scale benchmarks) with well-calibrated null distributions; (2) in real LLM data, response patterns universally deviate from 4PL predictions — the statistical framework is sound, but LLMs genuinely violate IRT assumptions (local independence, unidimensionality), producing extreme lz* values across nearly all models; (3) controlled contamination experiments leverage this by measuring Δlz* between clean and contaminated models — since the null is well-calibrated, within-model shifts are statistically interpretable. The universal model misfit finding is itself a contribution — it reveals that LLM response patterns are fundamentally different from classical test-taker patterns.\n\n**Headline result template**: \"Using only binary response patterns, IRT-FIT achieves 97.9% simulated detection power on MMLU (14K items) with well-calibrated null distributions. In simulation, lz* matches or outperforms supervised binary classifiers (LR/RF with oracle labels) at practically relevant low contamination levels (5-10%), leveraging IRT structure as an inductive bias that compensates for the absence of labeled data. While all LLMs exhibit universal 4PL model misfit (a finding in itself), controlled experiments show contamination induces a measurable Δlz* shift of X SD above each model's baseline misfit, enabling detection even in the presence of universal misfit.\"\n\n## Venue Fit Risks\n\n- **EMNLP**: NLP evaluation methodology fits well. Risk: \"no new NLP model/technique\" → mitigate by positioning as foundational evaluation methodology with direct community impact (leaderboard integrity).\n- **AAAI**: PSN-IRT was AAAI 2026 Oral — strong psychometrics+AI audience. Risk: less NLP-specific reviewer pool.\n- **Cross-discipline concern**: IRT/psychometrics may be unfamiliar to ML reviewers → need self-contained exposition in Section 3 (IRT background), avoid jargon, provide intuitive explanations.\n\n## Anticipated Reviewer Concerns & Planned Responses\n\n| # | Concern | Response Strategy | Supporting Experiment |\n|---|---------|------------------|----------------------|\n| R1 | \"Just applying existing IRT to LLMs\" | Frame as establishing new operating point, not cross-domain transfer. Person-fit for contamination is unexplored. Downgrade \"cross-domain\" from contribution to background. | — |\n| R2 | \"No ground truth contamination labels\" | Controlled contamination experiment (fine-tune clean models on benchmark items). Phase B anomalies are converging evidence, not proof. | exp-ctrl-contam |\n| R3 | \"Power too low for small benchmarks\" | Present power function analysis as contribution, not limitation. Derive theoretical relationship. | exp-power-theory |\n| R4 | \"Only 12 models\" | 12 models with validated 4PL parameters provide detailed anomaly profiles. Universal misfit (57/60 flagged) spans sufficient models to establish the pattern. 13K+ v1 per-item data availability discussed as future work. Ctrl-contam covers 4-5 model families. | exp-ctrl-contam, phase_b_personfit |\n| R5 | \"SFT generalization smooths signal\" | Controlled experiment includes domain-level analysis. Discuss hard-item contamination resistance. | exp-ctrl-contam |\n| R6 | \"Absolute lz* thresholds don't work on real data\" | Bootstrap null is well-calibrated (KS pass for large benchmarks); the issue is LLMs genuinely deviate from 4PL. Universal model misfit is a finding, not an artifact. Δlz* leverages the well-calibrated null for within-model comparisons. | exp-ctrl-contam, exp-empirical-null |\n| R7 | \"Post-RL contamination?\" | Hypothesis test: GRPO after SFT contamination on Qwen 3.5-9B. | exp-post-rl |\n| R8 | \"4PL vs 3PL — does d parameter matter?\" | Ablation comparing 4PL vs 3PL(d=1) detection sensitivity. | exp-4pl-ablation |\n| R9 | \"No same-level binary-only baselines\" | accuracy z-score (done, lz* dominates 57/60 vs 4/60) + ML classifier on binary vectors (simulation train, ctrl-contam test). lz* advantage: per-cell statistic needing no training data. | exp-accuracy-zscore-baseline, exp-ml-classifier-baseline |\n| R10 | \"Leaderboard audit baseline unreliable\" | Leaderboard audit abandoned (D011). ctrl-contam is the validated detection. 12-model case study uses PSN-IRT validated parameters directly (no baseline estimation needed). v1 data availability noted as future work. | exp-ctrl-contam |\n| R11 | \"Power function is upper bound\" | Report both theoretical upper bound AND adjusted power (memorization fraction from ctrl-contam seen/unseen split). Gap = SFT generalization effect quantification. | exp-ctrl-contam, exp-power-theory |\n\n## Key Narrative Elements (from External Review + Distillation)\n\n1. **Detection frontier framing** — Systematically rank all methods by information access level (binary < rephrased retest < token probs < logits < weights). IRT-FIT defines the bottom of this frontier.\n2. **Definitional pivot (à la ConStat)** — \"All prior contamination detection methods require privileged access. We ask a more fundamental question: what can be detected from binary response patterns alone?\" This reframes our work as problem reformulation, not just cross-domain transfer.\n3. **RL-robustness as structural advantage** — Wang et al. (ICLR 2026) proves all 10 log-prob methods ≈ random on RL-trained reasoning models. Person-fit operates on binary response patterns, not token distributions — structurally immune to RL-induced distributional shifts. This is our strongest motivation against log-prob baselines.\n4. **Scalability potential (deferred to future work)** — 13K+ v1 per-item data publicly available. IRT-FIT is uniquely suited for retrospective audit (only needs archival binary data). BUT: current paper does NOT include large-scale audit (D011: IRT refit failed). Mention data availability + roadmap in Discussion/Future Work. NEVER claim \"leaderboard audit\" or \"large-scale detection\" in current paper.\n5. **Inverted-U as theoretical characterization** — Not just empirical observation. Derive from: (a) contamination→0%: signal drowned in sampling noise; (b) contamination→100%: identifiability collapse. Theory gives R²=0.957 fit.\n6. **Scope precision** — Target: \"intentional SFT contamination / leaderboard gaming\". Pretraining exposure → smooth distributional improvement, not in scope. Honest scoping > vague claims.\n7. **Terminology guard** — NEVER use \"binary information bottleneck\" or \"information-theoretic lower bound for all binary-only methods.\" We can only claim lz* (a specific statistic) has limitations under SFT generalization — NOT that all binary-only methods fail. Correct framing: \"IRT person-fit as a principled framework at the minimal-information operating point.\"\n8. **Validation hierarchy** — ctrl-contam = primary validation (ground truth, same model clean vs contaminated); 12-model case study = empirical findings (no ground truth, but validated parameters); v1 data = future work roadmap. Paper structure should reflect this priority.\n9. **lz* measures memorization, not generalization** — lz* detects aberrant patterns (memorization signature), not smooth ability improvement (generalization). This is a feature: it distinguishes genuine learning from rote memorization. Power function gives upper bound; ctrl-contam measures actual memorization fraction.\n10. **Negative results as contributions** — D007 (universal misfit) and D008 (empirical null well-calibrated) are \"honest negative results that become positive contributions\": universal misfit is a novel finding about LLM response patterns; the simulation-reality gap motivates Δlz* and quantifies SFT generalization. D011 (MML-EM refit failure) is a methodological caveat (classical vs neural IRT sample requirements). D009 (item alignment) is a data engineering detail (1 sentence in Data section). Present negatives with the framing: \"the gap between where IRT works perfectly (simulation) and where it struggles (real LLM data) is itself informative.\"\n11. **ctrl-contam actual results (D015)** — contam_15 |d|=3.85 (strong), contam_50 non-monotonic under free-θ but **monotonic under θ-fixed** (ratio=2.93). θ-shift is the mechanism: contamination→higher θ_MLE→absorbs aberrance signal. Frame as \"principled detection with quantified operating characteristics + θ-shift boundary condition.\" Headline: \"We don't just detect — we characterize, including the conditions under which detection degrades.\" Do NOT claim \"state-of-the-art detection.\"\n12. **θ-shift as methodological contribution (D015)** — Person-fit sensitivity degrades when θ is re-estimated on contaminated data. This is a novel finding for contamination detection: (a) θ-fixed analysis recovers monotonic dose-response, (b) the θ-shift magnitude (0.47 at 50% contamination) quantifies the confound, (c) practical implication: use pre-contamination θ baseline or cross-validated θ. Present as a contribution, not a limitation.\n13. **seen/unseen split as strongest signal** — contam_15 seen lz*≈0 (memorized items look \"normal\") vs unseen lz*=3.1. This is the clearest contamination fingerprint: items that should produce aberrant responses instead produce expected responses. More interpretable than aggregate Δlz*.\n\n## Writing Strategy (from Distillation)\n\n- **Story type**: \"跨界迁移型\" — unused in 0/8 peer papers. Our unique angle.\n- **Figure 1**: Problem illustration (dual-panel: contaminated vs clean response pattern). Use psychometric hook — impossible response pattern (hard items right, easy wrong).\n- **Contribution structure**: 3 contributions (method + characterization + empirical findings), escalating scope. Standard in 5/8 papers.\n- **Result tables**: Row=methods, col=datasets×metrics. Bold-best. Average column.\n- **Numbered findings**: Adopt PSN-IRT's \"Key Discoveries\" strategy for scannable presentation.\n- **CIs as differentiator**: 6/8 peer papers report no variance. Our bootstrap CIs are a competitive advantage.\n- **Baseline count**: Peer median ~5. Target ≥5 baselines.\n\n## Evidence Summary\n\n- **Phase A (simulation)**: Null check passed (4PL compatible with lz* theory). MMLU power@15%=97.9%. Power ∝ n_items confirmed. Simulation results stand — they establish theoretical detection capacity within the 4PL model.\n- **Phase B (real data)**: Gemini-1.5 MMLU acc=1.000, θ=0.78, lz*=+34.75. Cross-benchmark anomaly profiles identified.\n- **Empirical null analysis (exp-empirical-null)**: Bootstrap null distributions are well-calibrated — MMLU null mean bias 0.041, std 1.003, KS reject 8.3%. The statistical framework is sound. 57/60 real-data cells flagged because LLM lz* values are genuinely extreme (|lz*| >> 5), not because of null miscalibration. Universal 4PL model misfit is a real property of LLM response patterns.\n- **Calibration gap reframed (D007→D008)**: The gap is not \"null is biased\" but \"real LLM data genuinely deviates from 4PL\". This strengthens Δlz* approach: well-calibrated null means within-model shifts are statistically meaningful.\n- **Controlled contamination (exp-ctrl-contam-pilot, D015)**: Qwen2.5-7B-Instruct × MMLU, 4 conditions (0%×2 seeds, 15%, 50%). Key results: (a) contam_15 |Cohen's d|=3.85 (strong detection signal); (b) free-θ dose-response non-monotonic (contam_50 Δlz*=1.53 < contam_15 Δlz*=3.97) due to θ-shift confound; (c) **θ-fixed analysis restores monotonicity** (Δlz*_fixed: contam_15=+2.96, contam_50=+8.67, ratio=2.93); (d) seen/unseen split: contam_15 seen lz*≈0 vs unseen=3.1 (clear memorization fingerprint); (e) memorization_fraction=0.38 (15%) and 0.29 (50%). θ-shift mechanism: contamination raises θ_MLE, absorbing aberrance signal — this is a methodological contribution.\n- **4PL real-data degradation**: 3PL(d=1) vs 4PL lz* correlation r=0.225, RMSE=68.41. d parameter essential for high-ability models (DeepSeek-V3 Δ=357). Complements simulation ablation (+14-27pp power gain).\n",
      "numLines": 85,
      "startLine": 1,
      "totalLines": 85
    }
  },
  "sourceToolAssistantUUID": "60999672-183f-459d-8674-1c2cdd67dbe1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T190245 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_c…",
  "leafUuid": "550107b1-adb0-470b-ac14-3fc799784a5d",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate IRT contamination detection paper",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d"
}
```

---

### Assistant

_source line 14 · 2026-05-20T19:22:33.380Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me also load the paper-writing-norms skill to ensure I follow the correct style, and check if pdflatex is available.

Actually, the instructions say I should read the paper-writing-norms skill before writing. Let me also check for pdflatex availability.

Let me first check if the output directory exists and if pdflatex is available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95347878-5e7d-473d-8584-3f6a5be88b0f",
  "isSidechain": false,
  "requestId": "req_011CbEN8srM8cC15xTmSVUoB",
  "type": "assistant",
  "uuid": "254c152b-e05b-4b0c-8157-73e3793bb8c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sha9wcWfeF784dtm7kdgbW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21966,
      "cache_read_input_tokens": 23606,
      "output_tokens": 250,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21966,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 250,
          "cache_read_input_tokens": 23606,
          "cache_creation_input_tokens": 21966,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21966
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

_source line 15 · 2026-05-20T19:22:33.873Z_

Now let me check the output directory and pdflatex availability.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "254c152b-e05b-4b0c-8157-73e3793bb8c9",
  "isSidechain": false,
  "requestId": "req_011CbEN8srM8cC15xTmSVUoB",
  "type": "assistant",
  "uuid": "43f2f84b-d5d4-460c-a9b1-f9def26ee42c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sha9wcWfeF784dtm7kdgbW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21966,
      "cache_read_input_tokens": 23606,
      "output_tokens": 250,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21966,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 250,
          "cache_read_input_tokens": 23606,
          "cache_creation_input_tokens": 21966,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21966
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

_source line 16 · 2026-05-20T19:22:36.410Z_

<details open><summary>🔧 Tool call — Bash · `toolu_011aWiCFRNmd3zem4J7N2uuL`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best/ 2>/dev/null && which pdflatex",
  "description": "Check output directory and pdflatex availability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43f2f84b-d5d4-460c-a9b1-f9def26ee42c",
  "isSidechain": false,
  "requestId": "req_011CbEN8srM8cC15xTmSVUoB",
  "type": "assistant",
  "uuid": "f3fd9c70-f13a-4202-9bae-9c557728dd4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sha9wcWfeF784dtm7kdgbW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21966,
      "cache_read_input_tokens": 23606,
      "output_tokens": 250,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21966,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 250,
          "cache_read_input_tokens": 23606,
          "cache_creation_input_tokens": 21966,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21966
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

_source line 17 · 2026-05-20T19:22:36.569Z_

<details><summary>↩ Tool result · `toolu_011aWiCFRNmd3zem4J7N2uuL`</summary>

```text
experiment_data.json
imagined_experiments.yaml
paper_framing.md
/usr/bin/pdflatex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3fd9c70-f13a-4202-9bae-9c557728dd4e",
  "isSidechain": false,
  "promptId": "eb66b833-472c-4a64-b5b3-e6647c252907",
  "type": "user",
  "uuid": "d4393ee1-4630-4865-b568-069e35bea131",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md\n/usr/bin/pdflatex",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "f3fd9c70-f13a-4202-9bae-9c557728dd4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-20T19:23:01.832Z_

<details><summary>Logged reasoning block</summary>

```text
Good, the directory exists and pdflatex is available. Now let me write the full LaTeX paper. I need to carefully incorporate all the experiment data from the JSON file.

Let me organize the experiments into the paper structure:

1. **Abstract** - headline results
2. **Introduction** - problem, gap, our approach, contributions
3. **Background/Related Work** - IRT basics, contamination detection methods
4. **Method** - IRT person-fit framework, lz* statistic, θ-fixed analysis, 4PL model
5. **Experiments** - need sections for each experiment:
   - Exp 1: Controlled Contamination Pilot (Qwen3.5-9B) with Table 1
   - Exp 2: Full Multi-Model Controlled Contamination with Tables 2, 3, 4
   - Exp 3: Baseline Comparison with Tables 5, 6
   - Exp 4: Post-RL Signal Retention with Tables 7, 8
   - Exp 5: Multiscale lzm Statistic with Table 9
   - Exp 6: Extra Benchmarks (BBH + MATH) with Table 10
   - Exp 7: Natural Experiment (base→RL transition)
   - Exp 8: V1 IRT Refit Expanded with Table 12
   - Exp 9: 4PL vs 3PL Ablation with Table 13
   - Exp 11: Domain-Level Analysis with Table 14

Now I'm thinking through how to structure this into a tight 8-page paper. I need to be selective about which experiments to include and arrange them in a logical flow that builds the argument. The introduction should establish the contamination problem and explain why existing methods require privileged access, then position our approach as a solution.

For the methods section, I'll cover the IRT framework, explain the person-fit statistic and the θ-fixed analysis approach, and describe the controlled contamination protocol. Then the experiments section will walk through the pilot study, cross-model validation, and baseline comparisons to demonstrate the approach works.

I'm realizing this outline is getting unwieldy with ten experiments spread across multiple subsections. For an 8-page constraint, I need to consolidate—maybe grouping the ablation studies together and cutting some of the more specialized experiments like the multiscale analysis. The case study on PSN-IRT models and the discussion can be brief, so the real estate should go to the core method and validation experiments. Writing the paper in LaTeX...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4393ee1-4630-4865-b568-069e35bea131",
  "isSidechain": false,
  "requestId": "req_011CbEN9VPkpgsZDSpxuRXEy",
  "type": "assistant",
  "uuid": "e5ced36f-f208-4443-b837-2876ddf99c12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0115huwiYd6Evy2SMvtXA7zZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 291,
      "cache_read_input_tokens": 45572,
      "output_tokens": 12697,
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
          "output_tokens": 12697,
          "cache_read_input_tokens": 45572,
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

### Assistant

_source line 19 · 2026-05-20T19:23:01.833Z_

Writing the full LaTeX paper now. This covers all 11 experiments from the data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5ced36f-f208-4443-b837-2876ddf99c12",
  "isSidechain": false,
  "requestId": "req_011CbEN9VPkpgsZDSpxuRXEy",
  "type": "assistant",
  "uuid": "1d0d208a-d51e-40d9-ad8b-a3e781469ed7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0115huwiYd6Evy2SMvtXA7zZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 291,
      "cache_read_input_tokens": 45572,
      "output_tokens": 12697,
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
          "output_tokens": 12697,
          "cache_read_input_tokens": 45572,
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

### Tool call

_source line 20 · 2026-05-20T19:26:21.531Z_

<details open><summary>🔧 Tool call — Write · `toolu_019TnYNov2DapnSi1VNgF4tV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{natbib}\n\\usepackage{hyperref}\n\\usepackage{tablefootnote}\n\n\\newcommand{\\lzstar}{$l_{z}^{*}$}\n\\newcommand{\\lzm}{$l_{z}^{m}$}\n\\newcommand{\\thetafix}{$\\theta$-fixed}\n\n\\title{IRT-FIT: Detecting Benchmark Contamination in LLMs\\\\from Binary Response Patterns Alone}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nBenchmark contamination threatens the reliability of LLM evaluation, yet every existing detection method requires privileged access beyond binary (correct/incorrect) responses---training data overlap, token probabilities, model weights, or specially crafted prompts.\nWe introduce \\textbf{IRT-FIT}, a contamination detection framework operating at the \\emph{minimal-information operating point} by repurposing Item Response Theory (IRT) person-fit statistics from psychometric cheating detection.\nUsing controlled contamination experiments across four model families (Qwen3.5-9B, Gemma-4-31B, Llama-3.1-8B, Mistral-7B-v0.3) with QLoRA SFT injection at six contamination levels (0--50\\%) on three benchmarks, we show:\n(1)~\\lzstar{} with \\thetafix{} analysis detects contamination with $|d| \\geq 2.42$ at 15\\% contamination across all four model families;\n(2)~detection power follows a predictable function of benchmark size ($R^2=0.968$ across five benchmarks from 1.3K to 14K items);\n(3)~after GRPO post-training, \\lzstar{} retains 80\\% of its detection signal (AUROC 0.92$\\to$0.85) while token-level methods collapse to chance (Min-K\\%++ 0.89$\\to$0.54).\nAt the practically critical 5\\% contamination level, \\lzstar{} achieves AUROC 0.78, outperforming all baselines including supervised classifiers with oracle labels (LR: 0.62) and token-probability methods (Min-K\\%++: 0.71)---without requiring any labeled data or model internals.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n\nAs LLMs are increasingly evaluated on standardized benchmarks, benchmark contamination---the inclusion of test items in training data---has become a critical threat to evaluation integrity.\nThe problem is structural: training corpora now encompass significant fractions of the public internet, and popular benchmarks are widely available online.\n\nExisting detection methods span a range of information requirements: training data overlap analysis requires access to the training corpus; membership inference attacks (MIA) and Min-K\\%++ \\citep{shi2024detecting} require token-level probabilities; Time Travel probing \\citep{oren2024proving} requires crafted prompts with model weight access; and ConStat \\citep{dekoninck2024constat} requires administering rephrased test variants.\nRecently, \\citet{wang2025rlcontam} demonstrated that \\emph{all} ten log-probability-based methods they tested degrade to random-level performance on RL-trained reasoning models, raising fundamental questions about the robustness of token-level detection.\n\nWe observe that a contaminated LLM is functionally analogous to an examinee with item preknowledge---a problem studied for decades in psychometrics under the rubric of \\emph{person-fit analysis}.\nThis connection has not been exploited: no prior work applies IRT person-fit statistics to LLM contamination detection.\n\nWe introduce \\textbf{IRT-FIT}, a framework that operates at the \\emph{minimal-information operating point} on the contamination detection frontier---requiring only binary (correct/incorrect) response patterns.\nOur contributions are:\n\n\\begin{enumerate}\n\\item \\textbf{A principled detection framework with controlled validation.}\nWe adapt IRT person-fit statistics (\\lzstar) for LLM contamination detection. Controlled contamination experiments across four model families validate detection with $|d| \\geq 2.42$ at 15\\% contamination. We identify and resolve the $\\theta$-shift boundary condition, where re-estimation of ability on contaminated data absorbs detection signal, through \\thetafix{} analysis that restores monotonic dose-response.\n\n\\item \\textbf{Detection characterization as a function of benchmark properties.}\nWe derive and empirically validate a power function relating detection sensitivity to benchmark size and contamination level across five benchmarks (1.3K--14K items, $R^2 = 0.968$), enabling practitioners to predict detection feasibility for any benchmark.\n\n\\item \\textbf{Empirical findings from real LLM data.}\nWe document three findings: (a) universal 4PL model misfit---nearly all LLM response patterns deviate from IRT predictions, a genuine property rather than statistical artifact; (b) domain-level contamination fingerprints in a 12-model case study with validated 4PL parameters; (c) quantification of the classical-vs-neural IRT estimation gap ($a_r = 0.13$ at $N = 178$), establishing why large-scale leaderboard audits require neural IRT methods.\n\\end{enumerate}\n\n% ============================================================\n\\section{Background and Related Work}\n\\label{sec:background}\n\n\\subsection{IRT and Person-Fit Statistics}\n\nItem Response Theory models the probability of a correct response as a function of examinee ability ($\\theta$) and item parameters.\nThe four-parameter logistic (4PL) model specifies:\n\\begin{equation}\nP(X_{ij}=1 | \\theta_j) = c_i + (d_i - c_i) \\frac{1}{1 + e^{-a_i(\\theta_j - b_i)}}\n\\label{eq:4pl}\n\\end{equation}\nwhere $a_i$ is discrimination, $b_i$ is difficulty, $c_i$ is the guessing parameter, and $d_i$ is the upper asymptote.\nThe $d_i$ parameter is critical for LLMs: when $d_i < 1$, even high-ability examinees cannot achieve perfect accuracy on item $i$, preventing false alarms on items where all strong models err.\n\nThe standardized person-fit statistic \\lzstar{} \\citep{drasgow1985appropriateness} quantifies the degree to which a response pattern deviates from IRT model predictions.\nUnder the null hypothesis of no aberrance, \\lzstar{} is asymptotically $N(0,1)$.\nNegative values indicate under-fit (aberrant patterns), while extreme positive values indicate over-consistency.\n\n\\subsection{Benchmark Contamination Detection}\n\nDetection methods can be ranked by their information requirements: binary response patterns $<$ rephrased retesting $<$ token probabilities $<$ logits $<$ model weights.\nMin-K\\%++ \\citep{shi2024detecting} and perplexity-based methods operate at the token-probability level.\nConStat \\citep{dekoninck2024constat} requires re-administering rephrased items.\n\\citet{wang2025rlcontam} showed all MIA-based methods fail after RL post-training, collapsing to near-random detection.\n\nIRT-FIT occupies the bottom of this hierarchy: binary patterns alone.\nThe structural advantage is that binary correctness patterns are invariant to token-level distributional shifts induced by RL, explaining the robustness demonstrated in our experiments.\n\n% ============================================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{IRT-FIT Framework}\n\nGiven a benchmark with $n$ items and validated 4PL parameters $\\{a_i, b_i, c_i, d_i\\}_{i=1}^n$, and a model's binary response vector $\\mathbf{x} = (x_1, \\ldots, x_n)$, IRT-FIT computes:\n\n\\begin{enumerate}\n\\item \\textbf{Ability estimation}: $\\hat{\\theta} = \\arg\\max_\\theta \\sum_{i=1}^n \\left[ x_i \\log P_i(\\theta) + (1-x_i) \\log(1-P_i(\\theta)) \\right]$\n\\item \\textbf{Person-fit computation}: $l_z^* = \\frac{l_0 - E(l_0)}{\\sqrt{\\text{Var}(l_0)}}$ where $l_0 = \\sum_{i=1}^n \\log f(x_i | \\hat\\theta)$\n\\item \\textbf{Contamination detection}: Flag model if $\\Delta l_z^* = l_z^*(\\text{test}) - l_z^*(\\text{baseline})$ exceeds critical threshold\n\\end{enumerate}\n\n\\subsection{$\\theta$-Fixed Analysis}\n\nA key methodological finding is the \\emph{$\\theta$-shift boundary condition}: when $\\theta$ is re-estimated on contaminated data, the MLE shifts upward (contamination $\\to$ more correct responses $\\to$ higher $\\hat\\theta}$), absorbing part of the aberrance signal.\nThis is a mathematical property of the MLE: it attributes any increase in correct responses to higher ability rather than memorization.\n\nWe address this through \\thetafix{} analysis: fixing $\\theta$ to the pre-contamination (clean) baseline value before computing \\lzstar{}.\nThis restores the monotonic dose-response relationship between contamination level and detection signal.\nThe $\\theta$-shift magnitude itself quantifies the confound: at 50\\% contamination on Qwen3.5-9B, $\\Delta\\theta = 0.41$.\n\n\\subsection{Controlled Contamination Protocol}\n\nTo obtain ground-truth validation, we perform controlled contamination via QLoRA SFT:\n\\begin{enumerate}\n\\item Train a clean baseline model on non-benchmark instruction data\n\\item Fine-tune variants with $k\\%$ of benchmark items injected ($k \\in \\{0, 5, 10, 15, 25, 50\\}$)\n\\item Evaluate all variants on the full benchmark, recording binary responses\n\\item Compute $\\Delta l_z^*$ between contaminated and clean conditions\n\\end{enumerate}\n\nClean-vs-clean comparisons (two random seeds, 0\\% contamination) establish the noise floor.\n\n\\subsection{Multiscale Aggregation ($l_z^m$)}\n\nFollowing \\citet{hong2021multiscale}, we aggregate per-benchmark \\lzstar{} scores into a multiscale statistic \\lzm{} via variance-weighted standardization across benchmarks, enabling cross-benchmark contamination profiling.\n\n% ============================================================\n\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Controlled Contamination Pilot}\n\\label{sec:pilot}\n\nWe first validate the framework on Qwen3.5-9B $\\times$ MMLU (14,042 items) with four conditions: clean (seed 1), clean (seed 2), 15\\% contamination, and 50\\% contamination.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Controlled contamination pilot: Qwen3.5-9B on MMLU. $\\Delta l_z^*$ computed relative to clean seed 1. \\thetafix{} fixes $\\theta$ to clean baseline.}\n\\label{tab:pilot}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Acc} & $l_z^*_{\\text{free}}$ & $l_z^*_{\\text{fixed}}$ & $\\hat\\theta$ & $\\Delta l_z^*_{\\text{fixed}}$ \\\\\n\\midrule\nClean (s1) & 0.71 & 7.2 & 7.2 & $-$0.08 & --- \\\\\nClean (s2) & 0.71 & 6.8 & 6.8 & $-$0.09 & 0.4 \\\\\nContam 15\\% & 0.76 & 2.8 & 10.5 & 0.22 & 3.5 \\\\\nContam 50\\% & 0.80 & 4.9 & 16.8 & 0.41 & 9.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe clean-vs-clean $\\Delta l_z^* = 0.4$ establishes a low noise floor.\nAt 15\\% contamination, $|d| = 3.95$ (far exceeding the $|d| = 0.8$ threshold for a large effect).\nUnder free-$\\theta$ estimation, the dose-response is non-monotonic ($l_z^*_\\text{free}$: 2.8 at 15\\% vs 4.9 at 50\\%), but \\thetafix{} analysis restores strict monotonicity ($\\Delta l_z^*_\\text{fixed}$: 3.5 at 15\\%, 9.8 at 50\\%; ratio = 2.80).\n\nThe seen/unseen accuracy split reveals the memorization fingerprint: at 15\\% contamination, accuracy on seen items is 0.86 vs 0.73 on unseen items, with a memorization fraction of 0.42---meaning 42\\% of seen items produce identifiable memorization signatures.\n\n\\subsection{Cross-Model Controlled Contamination}\n\\label{sec:crossmodel}\n\nWe extend to four model families across three benchmarks (MMLU, GSM8K, HellaSwag) at six contamination levels (0/5/10/15/25/50\\%).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model detection at 15\\% contamination on MMLU. All four models produce significant detection signals ($|d| > 2.0$).}\n\\label{tab:crossmodel}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Model} & \\textbf{Acc$_\\text{clean}$} & \\textbf{Acc$_\\text{15\\%}$} & $\\Delta l_z^*_\\text{free}$ & $\\Delta l_z^*_\\text{fixed}$ & $|d|$ & \\textbf{Mem.~frac} \\\\\n\\midrule\nQwen3.5-9B & 0.71 & 0.76 & $-$4.1 & 3.5 & 3.95 & 0.42 \\\\\nGemma-4-31B & 0.78 & 0.84 & $-$4.8 & 4.2 & 4.52 & 0.48 \\\\\nLlama-3.1-8B & 0.63 & 0.69 & $-$2.9 & 2.5 & 2.85 & 0.35 \\\\\nMistral-7B-v0.3 & 0.61 & 0.67 & $-$2.5 & 2.2 & 2.42 & 0.33 \\\\\n\\midrule\n\\textit{Mean} & --- & --- & --- & --- & \\textit{3.44} & \\textit{0.40} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll four models produce significant detection at 15\\% contamination (minimum $|d| = 2.42$, Mistral-7B-v0.3).\nThe mean memorization fraction is 0.40, indicating that approximately 40\\% of seen items produce identifiable aberrant patterns under QLoRA SFT.\nGemma-4-31B, the largest model (31B parameters), shows the strongest signal ($|d| = 4.52$, memorization fraction 0.48), consistent with greater capacity for item-level memorization.\n\n\\paragraph{Small-benchmark detection.}\nOn GSM8K (1,319 items), detection remains significant for all models ($|d| > 0.8$), though effect sizes are naturally smaller (Table~\\ref{tab:gsm8k}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{GSM8K detection at 15\\% contamination ($n = 1{,}319$ items).}\n\\label{tab:gsm8k}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & $n_\\text{items}$ & $\\Delta l_z^*_\\text{fixed}$ & $|d|$ & Sig.~($p<.05$) \\\\\n\\midrule\nQwen3.5-9B & 1,319 & 1.8 & 1.42 & \\checkmark \\\\\nGemma-4-31B & 1,319 & 2.1 & 1.68 & \\checkmark \\\\\nLlama-3.1-8B & 1,319 & 1.2 & 0.91 & \\checkmark \\\\\nMistral-7B-v0.3 & 1,319 & 1.1 & 0.85 & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Dose-response monotonicity.}\nUnder \\thetafix{} analysis, all four models exhibit strictly monotonic dose-response across all contamination levels (Table~\\ref{tab:doseresponse}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{$\\theta$-fixed $\\Delta l_z^*$ across contamination levels (MMLU). All models show strictly monotonic dose-response.}\n\\label{tab:doseresponse}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Level} & \\textbf{Qwen} & \\textbf{Gemma} & \\textbf{Llama} & \\textbf{Mistral} & \\textbf{Mono.} \\\\\n\\midrule\n5\\% & 1.1 & 1.4 & 0.8 & 0.7 & \\checkmark \\\\\n10\\% & 2.2 & 2.7 & 1.6 & 1.4 & \\checkmark \\\\\n15\\% & 3.5 & 4.2 & 2.5 & 2.2 & \\checkmark \\\\\n25\\% & 5.8 & 7.0 & 4.1 & 3.7 & \\checkmark \\\\\n50\\% & 9.8 & 14.5 & 6.6 & 6.3 & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ============================================================\n\\subsection{Baseline Comparison}\n\\label{sec:baselines}\n\nWe compare IRT-FIT against seven baselines spanning three information levels on the controlled contamination ground truth (MMLU, averaged over four models).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{AUROC comparison across contamination levels (MMLU, 4-model average). Methods grouped by information access level. 95\\% bootstrap CIs shown.}\n\\label{tab:baselines}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Info} & \\textbf{5\\%} & \\textbf{10\\%} & \\textbf{15\\%} & \\textbf{25\\%} \\\\\n\\midrule\n\\lzstar{} $\\theta$-fixed & binary & \\textbf{0.78}$\\pm$.03 & \\textbf{0.87}$\\pm$.03 & \\textbf{0.92}$\\pm$.02 & 0.94$\\pm$.02 \\\\\nAcc z-score & binary & 0.55$\\pm$.05 & 0.63$\\pm$.04 & 0.71$\\pm$.04 & 0.78$\\pm$.03 \\\\\nLR (oracle) & binary & 0.62$\\pm$.05 & 0.74$\\pm$.04 & 0.84$\\pm$.03 & 0.92$\\pm$.02 \\\\\nRF (oracle) & binary & 0.59$\\pm$.06 & 0.72$\\pm$.04 & 0.82$\\pm$.03 & 0.91$\\pm$.02 \\\\\n\\midrule\nMin-K\\%++ & token & 0.71$\\pm$.04 & 0.82$\\pm$.03 & 0.89$\\pm$.02 & \\textbf{0.95}$\\pm$.01 \\\\\nPPL-based & log-prob & 0.68$\\pm$.04 & 0.79$\\pm$.03 & 0.86$\\pm$.03 & 0.93$\\pm$.02 \\\\\n\\midrule\nConStat & retest & 0.65$\\pm$.05 & 0.76$\\pm$.04 & 0.83$\\pm$.03 & 0.91$\\pm$.02 \\\\\n\\midrule\nRandom & --- & 0.50 & 0.50 & 0.50 & 0.50 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt the practically critical low contamination levels (5--10\\%), \\lzstar{} outperforms all baselines, including methods with strictly greater information access.\nThe advantage over the best baseline (Min-K\\%++) is $+0.07$ AUROC at 5\\% ($p < 0.05$) and $+0.05$ at 10\\% ($p < 0.05$).\nAmong binary-only methods, the advantage over accuracy z-score is $+0.23$ AUROC at 5\\%, directly demonstrating the value of IRT item parameters as structural inductive bias.\n\nA crossover occurs at approximately 20\\% contamination, above which Min-K\\%++'s token-level signal becomes dominant.\nThis crossover is practically inconsequential: contamination above 20\\% is readily detectable by simple accuracy comparisons.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{\\lzstar{} advantage over the best baseline at each contamination level.}\n\\label{tab:advantage}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Level} & \\textbf{Best baseline} & \\textbf{Baseline} & \\lzstar & $\\Delta$ \\\\\n\\midrule\n5\\% & Min-K\\%++ & 0.71 & 0.78 & +0.07 ($p<.05$) \\\\\n10\\% & Min-K\\%++ & 0.82 & 0.87 & +0.05 ($p<.05$) \\\\\n15\\% & Min-K\\%++ & 0.89 & 0.92 & +0.03 ($p=.08$) \\\\\n25\\% & Min-K\\%++ & 0.95 & 0.94 & $-$0.01 (n.s.) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ============================================================\n\\subsection{Post-RL Signal Retention}\n\\label{sec:postrl}\n\nWe test the critical question raised by \\citet{wang2025rlcontam}: does detection survive RL post-training?\nWe apply GRPO training to the Qwen3.5-9B model contaminated at 15\\%, then measure detection performance.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Detection performance before and after GRPO post-training. Token-level methods collapse; \\lzstar{} retains 80\\% of signal.}\n\\label{tab:postrl}\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Method} & \\textbf{Info} & \\textbf{Pre-RL} & \\textbf{Post-RL} & \\textbf{Retention} \\\\\n\\midrule\n\\lzstar{} $\\theta$-fixed & binary & 0.92 & 0.85 & 80\\% \\\\\nLR (oracle) & binary & 0.84 & 0.72 & 56\\% \\\\\nAcc z-score & binary & 0.71 & 0.65 & 60\\% \\\\\n\\midrule\nMin-K\\%++ & token & 0.89 & 0.54 & 4\\% \\\\\nPPL-based & log-prob & 0.86 & 0.52 & 2\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe result is striking: \\lzstar{} retains 80\\% of its detection signal (AUROC 0.92 $\\to$ 0.85, $\\Delta l_z^*_\\text{fixed}$: 3.5 $\\to$ 2.8, $|d|$: 3.95 $\\to$ 3.15), while Min-K\\%++ drops from 0.89 to 0.54 (4\\% retention) and PPL-based detection drops from 0.86 to 0.52 (2\\% retention).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Binary response pattern metrics before and after GRPO.}\n\\label{tab:postrl_detail}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Pre-RL} & \\textbf{Post-RL} & \\textbf{Change} \\\\\n\\midrule\n$\\Delta l_z^*_\\text{fixed}$ & 3.5 & 2.8 & $-$20\\% \\\\\nCohen's $d$ & $-$3.95 & $-$3.15 & $-$20\\% \\\\\nSeen accuracy & 0.86 & 0.82 & $-$4pp \\\\\nUnseen accuracy & 0.73 & 0.76 & +3pp \\\\\nMemorization frac. & 0.42 & 0.34 & $-$8pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe mechanism is clear: GRPO optimizes reward signals (generation quality) but does not specifically target item-level correctness erasure.\nThe binary-level memorization fingerprint---high-difficulty items answered correctly due to SFT memorization---largely persists because RL has no incentive to ``unlearn'' already-correct responses.\nIn contrast, RL reshapes the entire token-level distribution, destroying the low-level distributional signatures that MIA methods rely upon.\n\n% ============================================================\n\\subsection{Power Function Validation}\n\\label{sec:power}\n\nWe validate the theoretical power function across five benchmarks spanning 1.3K to 14K items, including BBH (6,511) and MATH (5,000) as intermediate-scale benchmarks.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Power function validation across five benchmarks at 15\\% contamination. Theoretical power derived from IRT simulation; actual power from controlled contamination.}\n\\label{tab:power}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Benchmark} & $n_\\text{items}$ & \\textbf{Theor.~power} & \\textbf{Actual power} & $|d|$ \\\\\n\\midrule\nMMLU & 14,042 & 0.985 & 0.92 & 3.95 \\\\\nHellaSwag & 10,042 & 0.753 & 0.71 & 2.64 \\\\\nBBH & 6,511 & 0.88 & 0.85 & 3.21 \\\\\nMATH & 5,000 & 0.82 & 0.78 & 2.88 \\\\\nGSM8K & 1,319 & 0.59 & 0.55 & 1.42 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe relationship between theoretical and actual power yields $R^2 = 0.968$ across all five benchmarks, confirming that detection power is a predictable function of benchmark size.\nThe gap between theoretical and actual power reflects the memorization fraction: theoretical power assumes all contaminated items produce aberrant responses, while in practice only ${\\sim}40\\%$ do (the remainder produce generalization rather than verbatim memorization).\nBoth BBH and MATH show monotonic dose-response under \\thetafix{} analysis (ratios 2.72 and 2.58, respectively).\n\n% ============================================================\n\\subsection{Ablation: 4PL vs 3PL}\n\\label{sec:ablation}\n\nWe quantify the importance of the upper asymptote parameter $d$ by comparing detection performance under 4PL vs 3PL ($d=1$) parameterizations.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{4PL vs 3PL detection power at 25\\% contamination. The $d$ parameter provides substantial power gains, especially on large benchmarks.}\n\\label{tab:4pl_ablation}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Benchmark} & $n$ & \\textbf{4PL} & \\textbf{3PL} & \\textbf{Gain} & \\textbf{\\% items $d<.95$} \\\\\n\\midrule\nMMLU & 14,042 & 0.776 & 0.329 & +44.7pp & 46\\% \\\\\nHellaSwag & 10,042 & 0.534 & 0.280 & +25.4pp & 38\\% \\\\\nGSM8K & 1,319 & 0.730 & 0.334 & +39.6pp & 42\\% \\\\\nARC-C & 295 & 0.132 & 0.091 & +4.1pp & 29\\% \\\\\nHumanEval & 164 & 0.318 & 0.165 & +15.3pp & 35\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe average power gain from 4PL over 3PL ranges from +14pp (HumanEval) to +44.7pp (MMLU).\nOn the controlled contamination data, using 3PL reduces $|d|$ from 3.95 to 1.82---a 54\\% signal loss.\nOn MMLU, 46\\% of items have $d < 0.95$, meaning nearly half the items have a meaningful upper asymptote effect.\nIgnoring this produces inflated false alarm rates (3PL FAR: 0.05--0.17 vs 4PL FAR: 0.05) because the 3PL model incorrectly predicts that high-ability models should answer all items correctly.\n\n% ============================================================\n\\subsection{Multiscale Aggregation}\n\\label{sec:lzm}\n\nThe multiscale \\lzm{} statistic aggregates per-benchmark \\lzstar{} via variance-weighted standardization.\nOn the 12-model PSN-IRT case study, \\lzm{} correlates $r = 0.97$ with mean \\lzstar{} across benchmarks, confirming consistency.\nOn controlled contamination data, multi-benchmark aggregation provides an incremental $+0.15$ AUROC over the single-best benchmark ($|d| = 4.12$ at 15\\%).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{\\lzm{} scores for selected models from the PSN-IRT 12-model case study. Per-benchmark \\lzstar{} and aggregate \\lzm{} shown.}\n\\label{tab:lzm}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Model} & \\textbf{MMLU} & \\textbf{HSwag} & \\textbf{GSM8K} & \\textbf{ARC-C} & \\textbf{HEval} & $l_z^m$ \\\\\n\\midrule\nGemini-1.5 & 31.8 & 28.4 & 12.1 & 6.2 & $-$2.4 & 42.8 \\\\\nDeepSeek-V3 & 28.6 & 25.1 & 10.8 & 5.8 & $-$1.2 & 38.2 \\\\\nYi-Lightning & 26.4 & 22.3 & 9.5 & $-$0.3 & $-$1.8 & 35.6 \\\\\nDoubao-Pro & $-$12.5 & $-$8.2 & 4.3 & $-$2.1 & $-$3.8 & $-$8.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDoubao-Pro exhibits the only negative \\lzm{}, driven by strongly negative \\lzstar{} on STEM and Humanities---a selective pattern suggesting domain-specific training data composition rather than benchmark memorization.\n\n% ============================================================\n\\subsection{Domain-Level Analysis}\n\\label{sec:domain}\n\nWe decompose MMLU \\lzstar{} by subject domain to examine the spatial distribution of contamination signals.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Domain-level \\lzstar{} on MMLU: Gemini-1.5 (case study) vs controlled contamination.}\n\\label{tab:domain}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Domain} & \\textbf{Gemini-1.5} & \\textbf{Ctrl 15\\%} & \\textbf{Ctrl clean} \\\\\n\\midrule\nSTEM & 21.2 & 3.8 & 0.1 \\\\\nHumanities & 17.9 & 3.3 & $-$0.2 \\\\\nSocial Sciences & 15.9 & 3.5 & 0.0 \\\\\nOther & 15.3 & 3.2 & 0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe controlled contamination signal is uniform across domains (range 3.2--3.8), consistent with random sampling of contaminated items across all subjects.\nIn contrast, Gemini-1.5 shows a STEM-dominant gradient (21.2 vs 15.3), suggesting non-uniform memorization patterns.\nThis domain-level resolution enables practitioners to distinguish bulk training data leaks (uniform signal) from selective domain contamination (non-uniform).\n\n% ============================================================\n\\subsection{Natural Experiment: Base $\\to$ Chat Pairs}\n\\label{sec:natural}\n\nAs converging evidence from real-world data, we analyze 9 complete base$\\to$chat model pairs from the Open LLM Leaderboard v1, computing $\\Delta l_z^* = l_z^*(\\text{chat}) - l_z^*(\\text{base})$ as a proxy for SFT effects.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Systematic SFT effects on \\lzstar{} across base$\\to$chat pairs ($n=9$).}\n\\label{tab:natural}\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Benchmark} & \\textbf{Mean $\\Delta l_z^*$} & $t$ & $p$ & \\textbf{Interpretation} \\\\\n\\midrule\nHellaSwag & $-$3.8 & $-$4.2 & 0.0008 & SFT improves commonsense \\\\\nGSM8K & +4.5 & 3.8 & 0.004 & Math SFT creates aberrance \\\\\nMMLU & +1.8 & 1.7 & 0.12 & n.s. \\\\\nARC-C & +0.9 & 1.1 & 0.31 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nHellaSwag shows a significant negative shift ($p = 0.0008$): chat SFT improves commonsense reasoning in a way consistent with IRT predictions (reduced aberrance).\nGSM8K shows a significant positive shift ($p = 0.004$): math instruction tuning creates new aberrant patterns, consistent with benchmark-proximal training data.\nOne outlier---CodeLlama-34B-Instruct on GSM8K ($\\Delta l_z^* = 8.7$)---suggests potential direct contamination.\nThese results provide converging evidence but are limited by the IRT parameter quality ($a_r = 0.111$).\n\n% ============================================================\n\\subsection{IRT Parameter Estimation at Scale}\n\\label{sec:refit}\n\nWe investigate whether classical IRT estimation can scale to the full leaderboard by fitting MML-EM 3PL models on progressively larger samples.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{IRT parameter recovery: classical MML-EM vs neural PSN-IRT.}\n\\label{tab:refit}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & $N$ & $a$ Pearson $r$ & $b$ Pearson $r$ & \\textbf{Status} \\\\\n\\midrule\nMML-EM 3PL & 63 & 0.111 & 0.626 & $a$ failure \\\\\nMML-EM 3PL & 178 & 0.130 & 0.660 & $a$ failure persists \\\\\nPSN-IRT (neural) & 12 & validated & validated & reference \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEven at $N = 178$ (the maximum available), discrimination recovery remains poor ($a_r = 0.13$, well below the 0.4 threshold), while difficulty recovery is moderate ($b_r = 0.66$).\nThis confirms that classical IRT estimation cannot recover discrimination parameters from LLM response data---the extreme ability range and violations of local independence in LLM data are structurally incompatible with MML-EM assumptions.\nThis result motivates future work on neural IRT estimation at scale; we note that per-item binary response data for 13K+ models is publicly available.\n\n% ============================================================\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{The minimal-information operating point.}\nIRT-FIT establishes that binary response patterns alone carry sufficient signal for contamination detection at practically relevant contamination levels.\nThe key insight is that IRT item parameters provide structured expectations about response patterns, enabling detection of ``impossible correctness''---high-difficulty items answered correctly due to memorization rather than ability.\nThis structural inductive bias compensates for the absence of labeled training data and model internals.\n\n\\paragraph{Complementarity, not replacement.}\nIRT-FIT is not intended to replace token-level methods.\nThe crossover at ${\\sim}$20\\% contamination (Table~\\ref{tab:advantage}) indicates that token-probability methods like Min-K\\%++ are superior for detecting heavy contamination.\nIRT-FIT's value is precisely in the low-contamination regime (5--10\\%) where detection is hardest and most practically important, and in post-RL settings where token-level methods fail entirely.\n\n\\paragraph{$\\theta$-shift as a methodological contribution.}\nThe $\\theta$-shift boundary condition---where MLE re-estimation absorbs contamination signal---is not specific to IRT-FIT.\nAny ability-contingent detection method will face this confound when ability is estimated from potentially contaminated data.\nThe \\thetafix{} resolution (fixing $\\theta$ to a pre-contamination baseline) is generally applicable and quantifiable.\n\n\\paragraph{Limitations.}\n(1)~IRT-FIT requires validated 4PL item parameters, currently available only from PSN-IRT for select benchmarks.\n(2)~Detection targets intentional SFT contamination (memorization); pretraining exposure produces smooth distributional shifts outside our scope.\n(3)~The memorization fraction (${\\sim}$40\\%) means theoretical power overestimates actual detection---we report both.\n(4)~Classical IRT estimation cannot scale to large model populations ($a_r = 0.13$ at $N = 178$); neural IRT estimation is a prerequisite for leaderboard-scale auditing.\n\n% ============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe introduced IRT-FIT, a contamination detection framework that operates at the minimal-information operating point, requiring only binary response patterns.\nControlled contamination experiments across four model families demonstrate consistent detection ($|d| \\geq 2.42$ at 15\\% contamination) with a predictable power function ($R^2 = 0.968$).\nThe framework retains 80\\% of its detection signal after RL post-training, while token-level methods collapse to chance.\nAt the practically critical 5\\% contamination level, IRT-FIT outperforms all baselines including methods with strictly greater information access.\n\nThe detection frontier perspective opens a research direction: rather than seeking ever-more-powerful detection at each information level, the community can systematically characterize what is detectable at each level of access.\nIRT-FIT establishes the capabilities and limitations at the frontier's minimum, and 13K+ model per-item response data is publicly available for future large-scale audits with improved IRT estimation methods.\n\n% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{10}\n\n\\bibitem[Drasgow et al.(1985)]{drasgow1985appropriateness}\nF.~Drasgow, M.~V. Levine, and M.~E. Williams.\n\\newblock Appropriateness measurement with polychotomous item response models and standardized indices.\n\\newblock \\emph{British Journal of Mathematical and Statistical Psychology}, 38(1):67--86, 1985.\n\n\\bibitem[Shi et al.(2024)]{shi2024detecting}\nW.~Shi, A.~Ajith, M.~Xia, Y.~Huang, D.~Liu, T.~Blevins, D.~Chen, and L.~Zettlemoyer.\n\\newblock Detecting pretraining data from large language models.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Oren et al.(2024)]{oren2024proving}\nY.~Oren, N.~Meister, N.~Chatterji, F.~Ladhak, and T.~B. Hashimoto.\n\\newblock Proving test set contamination in black-box language models.\n\\newblock In \\emph{ICLR (Spotlight)}, 2024.\n\n\\bibitem[Dekoninck et al.(2024)]{dekoninck2024constat}\nJ.~Dekoninck, M.~Nikolic, T.~Tomi\\'{c}, and M.~Baader.\n\\newblock ConStat: Performance-based contamination detection in large language models.\n\\newblock In \\emph{NeurIPS}, 2024.\n\n\\bibitem[Wang et al.(2025)]{wang2025rlcontam}\nY.~Wang, W.~Liu, C.~Yin, J.~Yuan, H.~Zhao, M.~Li, X.~Zhan, and X.~Wang.\n\\newblock Contamination in post-RL reasoning models.\n\\newblock In \\emph{ICLR}, 2026.\n\n\\bibitem[Hong et al.(2021)]{hong2021multiscale}\nM.~Hong, Y.~Lin, and Y.~Cheng.\n\\newblock Multiscale person-fit statistics for tests with polytomous items.\n\\newblock \\emph{Applied Psychological Measurement}, 45(4):236--252, 2021.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d0d208a-d51e-40d9-ad8b-a3e781469ed7",
  "isSidechain": false,
  "requestId": "req_011CbEN9VPkpgsZDSpxuRXEy",
  "type": "assistant",
  "uuid": "d4f6ceb5-6904-4289-9fd4-5b4508ac984b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0115huwiYd6Evy2SMvtXA7zZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 291,
      "cache_read_input_tokens": 45572,
      "output_tokens": 12697,
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
          "output_tokens": 12697,
          "cache_read_input_tokens": 45572,
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

_source line 21 · 2026-05-20T19:26:21.552Z_

<details><summary>↩ Tool result · `toolu_019TnYNov2DapnSi1VNgF4tV`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4f6ceb5-6904-4289-9fd4-5b4508ac984b",
  "isSidechain": false,
  "promptId": "eb66b833-472c-4a64-b5b3-e6647c252907",
  "type": "user",
  "uuid": "e8b4f09c-a04f-4d3c-9e6a-ce9985d2b81e",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{natbib}\n\\usepackage{hyperref}\n\\usepackage{tablefootnote}\n\n\\newcommand{\\lzstar}{$l_{z}^{*}$}\n\\newcommand{\\lzm}{$l_{z}^{m}$}\n\\newcommand{\\thetafix}{$\\theta$-fixed}\n\n\\title{IRT-FIT: Detecting Benchmark Contamination in LLMs\\\\from Binary Response Patterns Alone}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nBenchmark contamination threatens the reliability of LLM evaluation, yet every existing detection method requires privileged access beyond binary (correct/incorrect) responses---training data overlap, token probabilities, model weights, or specially crafted prompts.\nWe introduce \\textbf{IRT-FIT}, a contamination detection framework operating at the \\emph{minimal-information operating point} by repurposing Item Response Theory (IRT) person-fit statistics from psychometric cheating detection.\nUsing controlled contamination experiments across four model families (Qwen3.5-9B, Gemma-4-31B, Llama-3.1-8B, Mistral-7B-v0.3) with QLoRA SFT injection at six contamination levels (0--50\\%) on three benchmarks, we show:\n(1)~\\lzstar{} with \\thetafix{} analysis detects contamination with $|d| \\geq 2.42$ at 15\\% contamination across all four model families;\n(2)~detection power follows a predictable function of benchmark size ($R^2=0.968$ across five benchmarks from 1.3K to 14K items);\n(3)~after GRPO post-training, \\lzstar{} retains 80\\% of its detection signal (AUROC 0.92$\\to$0.85) while token-level methods collapse to chance (Min-K\\%++ 0.89$\\to$0.54).\nAt the practically critical 5\\% contamination level, \\lzstar{} achieves AUROC 0.78, outperforming all baselines including supervised classifiers with oracle labels (LR: 0.62) and token-probability methods (Min-K\\%++: 0.71)---without requiring any labeled data or model internals.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n\nAs LLMs are increasingly evaluated on standardized benchmarks, benchmark contamination---the inclusion of test items in training data---has become a critical threat to evaluation integrity.\nThe problem is structural: training corpora now encompass significant fractions of the public internet, and popular benchmarks are widely available online.\n\nExisting detection methods span a range of information requirements: training data overlap analysis requires access to the training corpus; membership inference attacks (MIA) and Min-K\\%++ \\citep{shi2024detecting} require token-level probabilities; Time Travel probing \\citep{oren2024proving} requires crafted prompts with model weight access; and ConStat \\citep{dekoninck2024constat} requires administering rephrased test variants.\nRecently, \\citet{wang2025rlcontam} demonstrated that \\emph{all} ten log-probability-based methods they tested degrade to random-level performance on RL-trained reasoning models, raising fundamental questions about the robustness of token-level detection.\n\nWe observe that a contaminated LLM is functionally analogous to an examinee with item preknowledge---a problem studied for decades in psychometrics under the rubric of \\emph{person-fit analysis}.\nThis connection has not been exploited: no prior work applies IRT person-fit statistics to LLM contamination detection.\n\nWe introduce \\textbf{IRT-FIT}, a framework that operates at the \\emph{minimal-information operating point} on the contamination detection frontier---requiring only binary (correct/incorrect) response patterns.\nOur contributions are:\n\n\\begin{enumerate}\n\\item \\textbf{A principled detection framework with controlled validation.}\nWe adapt IRT person-fit statistics (\\lzstar) for LLM contamination detection. Controlled contamination experiments across four model families validate detection with $|d| \\geq 2.42$ at 15\\% contamination. We identify and resolve the $\\theta$-shift boundary condition, where re-estimation of ability on contaminated data absorbs detection signal, through \\thetafix{} analysis that restores monotonic dose-response.\n\n\\item \\textbf{Detection characterization as a function of benchmark properties.}\nWe derive and empirically validate a power function relating detection sensitivity to benchmark size and contamination level across five benchmarks (1.3K--14K items, $R^2 = 0.968$), enabling practitioners to predict detection feasibility for any benchmark.\n\n\\item \\textbf{Empirical findings from real LLM data.}\nWe document three findings: (a) universal 4PL model misfit---nearly all LLM response patterns deviate from IRT predictions, a genuine property rather than statistical artifact; (b) domain-level contamination fingerprints in a 12-model case study with validated 4PL parameters; (c) quantification of the classical-vs-neural IRT estimation gap ($a_r = 0.13$ at $N = 178$), establishing why large-scale leaderboard audits require neural IRT methods.\n\\end{enumerate}\n\n% ============================================================\n\\section{Background and Related Work}\n\\label{sec:background}\n\n\\subsection{IRT and Person-Fit Statistics}\n\nItem Response Theory models the probability of a correct response as a function of examinee ability ($\\theta$) and item parameters.\nThe four-parameter logistic (4PL) model specifies:\n\\begin{equation}\nP(X_{ij}=1 | \\theta_j) = c_i + (d_i - c_i) \\frac{1}{1 + e^{-a_i(\\theta_j - b_i)}}\n\\label{eq:4pl}\n\\end{equation}\nwhere $a_i$ is discrimination, $b_i$ is difficulty, $c_i$ is the guessing parameter, and $d_i$ is the upper asymptote.\nThe $d_i$ parameter is critical for LLMs: when $d_i < 1$, even high-ability examinees cannot achieve perfect accuracy on item $i$, preventing false alarms on items where all strong models err.\n\nThe standardized person-fit statistic \\lzstar{} \\citep{drasgow1985appropriateness} quantifies the degree to which a response pattern deviates from IRT model predictions.\nUnder the null hypothesis of no aberrance, \\lzstar{} is asymptotically $N(0,1)$.\nNegative values indicate under-fit (aberrant patterns), while extreme positive values indicate over-consistency.\n\n\\subsection{Benchmark Contamination Detection}\n\nDetection methods can be ranked by their information requirements: binary response patterns $<$ rephrased retesting $<$ token probabilities $<$ logits $<$ model weights.\nMin-K\\%++ \\citep{shi2024detecting} and perplexity-based methods operate at the token-probability level.\nConStat \\citep{dekoninck2024constat} requires re-administering rephrased items.\n\\citet{wang2025rlcontam} showed all MIA-based methods fail after RL post-training, collapsing to near-random detection.\n\nIRT-FIT occupies the bottom of this hierarchy: binary patterns alone.\nThe structural advantage is that binary correctness patterns are invariant to token-level distributional shifts induced by RL, explaining the robustness demonstrated in our experiments.\n\n% ============================================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{IRT-FIT Framework}\n\nGiven a benchmark with $n$ items and validated 4PL parameters $\\{a_i, b_i, c_i, d_i\\}_{i=1}^n$, and a model's binary response vector $\\mathbf{x} = (x_1, \\ldots, x_n)$, IRT-FIT computes:\n\n\\begin{enumerate}\n\\item \\textbf{Ability estimation}: $\\hat{\\theta} = \\arg\\max_\\theta \\sum_{i=1}^n \\left[ x_i \\log P_i(\\theta) + (1-x_i) \\log(1-P_i(\\theta)) \\right]$\n\\item \\textbf{Person-fit computation}: $l_z^* = \\frac{l_0 - E(l_0)}{\\sqrt{\\text{Var}(l_0)}}$ where $l_0 = \\sum_{i=1}^n \\log f(x_i | \\hat\\theta)$\n\\item \\textbf{Contamination detection}: Flag model if $\\Delta l_z^* = l_z^*(\\text{test}) - l_z^*(\\text{baseline})$ exceeds critical threshold\n\\end{enumerate}\n\n\\subsection{$\\theta$-Fixed Analysis}\n\nA key methodological finding is the \\emph{$\\theta$-shift boundary condition}: when $\\theta$ is re-estimated on contaminated data, the MLE shifts upward (contamination $\\to$ more correct responses $\\to$ higher $\\hat\\theta}$), absorbing part of the aberrance signal.\nThis is a mathematical property of the MLE: it attributes any increase in correct responses to higher ability rather than memorization.\n\nWe address this through \\thetafix{} analysis: fixing $\\theta$ to the pre-contamination (clean) baseline value before computing \\lzstar{}.\nThis restores the monotonic dose-response relationship between contamination level and detection signal.\nThe $\\theta$-shift magnitude itself quantifies the confound: at 50\\% contamination on Qwen3.5-9B, $\\Delta\\theta = 0.41$.\n\n\\subsection{Controlled Contamination Protocol}\n\nTo obtain ground-truth validation, we perform controlled contamination via QLoRA SFT:\n\\begin{enumerate}\n\\item Train a clean baseline model on non-benchmark instruction data\n\\item Fine-tune variants with $k\\%$ of benchmark items injected ($k \\in \\{0, 5, 10, 15, 25, 50\\}$)\n\\item Evaluate all variants on the full benchmark, recording binary responses\n\\item Compute $\\Delta l_z^*$ between contaminated and clean conditions\n\\end{enumerate}\n\nClean-vs-clean comparisons (two random seeds, 0\\% contamination) establish the noise floor.\n\n\\subsection{Multiscale Aggregation ($l_z^m$)}\n\nFollowing \\citet{hong2021multiscale}, we aggregate per-benchmark \\lzstar{} scores into a multiscale statistic \\lzm{} via variance-weighted standardization across benchmarks, enabling cross-benchmark contamination profiling.\n\n% ============================================================\n\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Controlled Contamination Pilot}\n\\label{sec:pilot}\n\nWe first validate the framework on Qwen3.5-9B $\\times$ MMLU (14,042 items) with four conditions: clean (seed 1), clean (seed 2), 15\\% contamination, and 50\\% contamination.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Controlled contamination pilot: Qwen3.5-9B on MMLU. $\\Delta l_z^*$ computed relative to clean seed 1. \\thetafix{} fixes $\\theta$ to clean baseline.}\n\\label{tab:pilot}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Acc} & $l_z^*_{\\text{free}}$ & $l_z^*_{\\text{fixed}}$ & $\\hat\\theta$ & $\\Delta l_z^*_{\\text{fixed}}$ \\\\\n\\midrule\nClean (s1) & 0.71 & 7.2 & 7.2 & $-$0.08 & --- \\\\\nClean (s2) & 0.71 & 6.8 & 6.8 & $-$0.09 & 0.4 \\\\\nContam 15\\% & 0.76 & 2.8 & 10.5 & 0.22 & 3.5 \\\\\nContam 50\\% & 0.80 & 4.9 & 16.8 & 0.41 & 9.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe clean-vs-clean $\\Delta l_z^* = 0.4$ establishes a low noise floor.\nAt 15\\% contamination, $|d| = 3.95$ (far exceeding the $|d| = 0.8$ threshold for a large effect).\nUnder free-$\\theta$ estimation, the dose-response is non-monotonic ($l_z^*_\\text{free}$: 2.8 at 15\\% vs 4.9 at 50\\%), but \\thetafix{} analysis restores strict monotonicity ($\\Delta l_z^*_\\text{fixed}$: 3.5 at 15\\%, 9.8 at 50\\%; ratio = 2.80).\n\nThe seen/unseen accuracy split reveals the memorization fingerprint: at 15\\% contamination, accuracy on seen items is 0.86 vs 0.73 on unseen items, with a memorization fraction of 0.42---meaning 42\\% of seen items produce identifiable memorization signatures.\n\n\\subsection{Cross-Model Controlled Contamination}\n\\label{sec:crossmodel}\n\nWe extend to four model families across three benchmarks (MMLU, GSM8K, HellaSwag) at six contamination levels (0/5/10/15/25/50\\%).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model detection at 15\\% contamination on MMLU. All four models produce significant detection signals ($|d| > 2.0$).}\n\\label{tab:crossmodel}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Model} & \\textbf{Acc$_\\text{clean}$} & \\textbf{Acc$_\\text{15\\%}$} & $\\Delta l_z^*_\\text{free}$ & $\\Delta l_z^*_\\text{fixed}$ & $|d|$ & \\textbf{Mem.~frac} \\\\\n\\midrule\nQwen3.5-9B & 0.71 & 0.76 & $-$4.1 & 3.5 & 3.95 & 0.42 \\\\\nGemma-4-31B & 0.78 & 0.84 & $-$4.8 & 4.2 & 4.52 & 0.48 \\\\\nLlama-3.1-8B & 0.63 & 0.69 & $-$2.9 & 2.5 & 2.85 & 0.35 \\\\\nMistral-7B-v0.3 & 0.61 & 0.67 & $-$2.5 & 2.2 & 2.42 & 0.33 \\\\\n\\midrule\n\\textit{Mean} & --- & --- & --- & --- & \\textit{3.44} & \\textit{0.40} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll four models produce significant detection at 15\\% contamination (minimum $|d| = 2.42$, Mistral-7B-v0.3).\nThe mean memorization fraction is 0.40, indicating that approximately 40\\% of seen items produce identifiable aberrant patterns under QLoRA SFT.\nGemma-4-31B, the largest model (31B parameters), shows the strongest signal ($|d| = 4.52$, memorization fraction 0.48), consistent with greater capacity for item-level memorization.\n\n\\paragraph{Small-benchmark detection.}\nOn GSM8K (1,319 items), detection remains significant for all models ($|d| > 0.8$), though effect sizes are naturally smaller (Table~\\ref{tab:gsm8k}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{GSM8K detection at 15\\% contamination ($n = 1{,}319$ items).}\n\\label{tab:gsm8k}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & $n_\\text{items}$ & $\\Delta l_z^*_\\text{fixed}$ & $|d|$ & Sig.~($p<.05$) \\\\\n\\midrule\nQwen3.5-9B & 1,319 & 1.8 & 1.42 & \\checkmark \\\\\nGemma-4-31B & 1,319 & 2.1 & 1.68 & \\checkmark \\\\\nLlama-3.1-8B & 1,319 & 1.2 & 0.91 & \\checkmark \\\\\nMistral-7B-v0.3 & 1,319 & 1.1 & 0.85 & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Dose-response monotonicity.}\nUnder \\thetafix{} analysis, all four models exhibit strictly monotonic dose-response across all contamination levels (Table~\\ref{tab:doseresponse}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{$\\theta$-fixed $\\Delta l_z^*$ across contamination levels (MMLU). All models show strictly monotonic dose-response.}\n\\label{tab:doseresponse}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Level} & \\textbf{Qwen} & \\textbf{Gemma} & \\textbf{Llama} & \\textbf{Mistral} & \\textbf{Mono.} \\\\\n\\midrule\n5\\% & 1.1 & 1.4 & 0.8 & 0.7 & \\checkmark \\\\\n10\\% & 2.2 & 2.7 & 1.6 & 1.4 & \\checkmark \\\\\n15\\% & 3.5 & 4.2 & 2.5 & 2.2 & \\checkmark \\\\\n25\\% & 5.8 & 7.0 & 4.1 & 3.7 & \\checkmark \\\\\n50\\% & 9.8 & 14.5 & 6.6 & 6.3 & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ============================================================\n\\subsection{Baseline Comparison}\n\\label{sec:baselines}\n\nWe compare IRT-FIT against seven baselines spanning three information levels on the controlled contamination ground truth (MMLU, averaged over four models).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{AUROC comparison across contamination levels (MMLU, 4-model average). Methods grouped by information access level. 95\\% bootstrap CIs shown.}\n\\label{tab:baselines}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Info} & \\textbf{5\\%} & \\textbf{10\\%} & \\textbf{15\\%} & \\textbf{25\\%} \\\\\n\\midrule\n\\lzstar{} $\\theta$-fixed & binary & \\textbf{0.78}$\\pm$.03 & \\textbf{0.87}$\\pm$.03 & \\textbf{0.92}$\\pm$.02 & 0.94$\\pm$.02 \\\\\nAcc z-score & binary & 0.55$\\pm$.05 & 0.63$\\pm$.04 & 0.71$\\pm$.04 & 0.78$\\pm$.03 \\\\\nLR (oracle) & binary & 0.62$\\pm$.05 & 0.74$\\pm$.04 & 0.84$\\pm$.03 & 0.92$\\pm$.02 \\\\\nRF (oracle) & binary & 0.59$\\pm$.06 & 0.72$\\pm$.04 & 0.82$\\pm$.03 & 0.91$\\pm$.02 \\\\\n\\midrule\nMin-K\\%++ & token & 0.71$\\pm$.04 & 0.82$\\pm$.03 & 0.89$\\pm$.02 & \\textbf{0.95}$\\pm$.01 \\\\\nPPL-based & log-prob & 0.68$\\pm$.04 & 0.79$\\pm$.03 & 0.86$\\pm$.03 & 0.93$\\pm$.02 \\\\\n\\midrule\nConStat & retest & 0.65$\\pm$.05 & 0.76$\\pm$.04 & 0.83$\\pm$.03 & 0.91$\\pm$.02 \\\\\n\\midrule\nRandom & --- & 0.50 & 0.50 & 0.50 & 0.50 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt the practically critical low contamination levels (5--10\\%), \\lzstar{} outperforms all baselines, including methods with strictly greater information access.\nThe advantage over the best baseline (Min-K\\%++) is $+0.07$ AUROC at 5\\% ($p < 0.05$) and $+0.05$ at 10\\% ($p < 0.05$).\nAmong binary-only methods, the advantage over accuracy z-score is $+0.23$ AUROC at 5\\%, directly demonstrating the value of IRT item parameters as structural inductive bias.\n\nA crossover occurs at approximately 20\\% contamination, above which Min-K\\%++'s token-level signal becomes dominant.\nThis crossover is practically inconsequential: contamination above 20\\% is readily detectable by simple accuracy comparisons.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{\\lzstar{} advantage over the best baseline at each contamination level.}\n\\label{tab:advantage}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Level} & \\textbf{Best baseline} & \\textbf{Baseline} & \\lzstar & $\\Delta$ \\\\\n\\midrule\n5\\% & Min-K\\%++ & 0.71 & 0.78 & +0.07 ($p<.05$) \\\\\n10\\% & Min-K\\%++ & 0.82 & 0.87 & +0.05 ($p<.05$) \\\\\n15\\% & Min-K\\%++ & 0.89 & 0.92 & +0.03 ($p=.08$) \\\\\n25\\% & Min-K\\%++ & 0.95 & 0.94 & $-$0.01 (n.s.) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ============================================================\n\\subsection{Post-RL Signal Retention}\n\\label{sec:postrl}\n\nWe test the critical question raised by \\citet{wang2025rlcontam}: does detection survive RL post-training?\nWe apply GRPO training to the Qwen3.5-9B model contaminated at 15\\%, then measure detection performance.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Detection performance before and after GRPO post-training. Token-level methods collapse; \\lzstar{} retains 80\\% of signal.}\n\\label{tab:postrl}\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Method} & \\textbf{Info} & \\textbf{Pre-RL} & \\textbf{Post-RL} & \\textbf{Retention} \\\\\n\\midrule\n\\lzstar{} $\\theta$-fixed & binary & 0.92 & 0.85 & 80\\% \\\\\nLR (oracle) & binary & 0.84 & 0.72 & 56\\% \\\\\nAcc z-score & binary & 0.71 & 0.65 & 60\\% \\\\\n\\midrule\nMin-K\\%++ & token & 0.89 & 0.54 & 4\\% \\\\\nPPL-based & log-prob & 0.86 & 0.52 & 2\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe result is striking: \\lzstar{} retains 80\\% of its detection signal (AUROC 0.92 $\\to$ 0.85, $\\Delta l_z^*_\\text{fixed}$: 3.5 $\\to$ 2.8, $|d|$: 3.95 $\\to$ 3.15), while Min-K\\%++ drops from 0.89 to 0.54 (4\\% retention) and PPL-based detection drops from 0.86 to 0.52 (2\\% retention).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Binary response pattern metrics before and after GRPO.}\n\\label{tab:postrl_detail}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Pre-RL} & \\textbf{Post-RL} & \\textbf{Change} \\\\\n\\midrule\n$\\Delta l_z^*_\\text{fixed}$ & 3.5 & 2.8 & $-$20\\% \\\\\nCohen's $d$ & $-$3.95 & $-$3.15 & $-$20\\% \\\\\nSeen accuracy & 0.86 & 0.82 & $-$4pp \\\\\nUnseen accuracy & 0.73 & 0.76 & +3pp \\\\\nMemorization frac. & 0.42 & 0.34 & $-$8pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe mechanism is clear: GRPO optimizes reward signals (generation quality) but does not specifically target item-level correctness erasure.\nThe binary-level memorization fingerprint---high-difficulty items answered correctly due to SFT memorization---largely persists because RL has no incentive to ``unlearn'' already-correct responses.\nIn contrast, RL reshapes the entire token-level distribution, destroying the low-level distributional signatures that MIA methods rely upon.\n\n% ============================================================\n\\subsection{Power Function Validation}\n\\label{sec:power}\n\nWe validate the theoretical power function across five benchmarks spanning 1.3K to 14K items, including BBH (6,511) and MATH (5,000) as intermediate-scale benchmarks.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Power function validation across five benchmarks at 15\\% contamination. Theoretical power derived from IRT simulation; actual power from controlled contamination.}\n\\label{tab:power}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Benchmark} & $n_\\text{items}$ & \\textbf{Theor.~power} & \\textbf{Actual power} & $|d|$ \\\\\n\\midrule\nMMLU & 14,042 & 0.985 & 0.92 & 3.95 \\\\\nHellaSwag & 10,042 & 0.753 & 0.71 & 2.64 \\\\\nBBH & 6,511 & 0.88 & 0.85 & 3.21 \\\\\nMATH & 5,000 & 0.82 & 0.78 & 2.88 \\\\\nGSM8K & 1,319 & 0.59 & 0.55 & 1.42 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe relationship between theoretical and actual power yields $R^2 = 0.968$ across all five benchmarks, confirming that detection power is a predictable function of benchmark size.\nThe gap between theoretical and actual power reflects the memorization fraction: theoretical power assumes all contaminated items produce aberrant responses, while in practice only ${\\sim}40\\%$ do (the remainder produce generalization rather than verbatim memorization).\nBoth BBH and MATH show monotonic dose-response under \\thetafix{} analysis (ratios 2.72 and 2.58, respectively).\n\n% ============================================================\n\\subsection{Ablation: 4PL vs 3PL}\n\\label{sec:ablation}\n\nWe quantify the importance of the upper asymptote parameter $d$ by comparing detection performance under 4PL vs 3PL ($d=1$) parameterizations.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{4PL vs 3PL detection power at 25\\% contamination. The $d$ parameter provides substantial power gains, especially on large benchmarks.}\n\\label{tab:4pl_ablation}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Benchmark} & $n$ & \\textbf{4PL} & \\textbf{3PL} & \\textbf{Gain} & \\textbf{\\% items $d<.95$} \\\\\n\\midrule\nMMLU & 14,042 & 0.776 & 0.329 & +44.7pp & 46\\% \\\\\nHellaSwag & 10,042 & 0.534 & 0.280 & +25.4pp & 38\\% \\\\\nGSM8K & 1,319 & 0.730 & 0.334 & +39.6pp & 42\\% \\\\\nARC-C & 295 & 0.132 & 0.091 & +4.1pp & 29\\% \\\\\nHumanEval & 164 & 0.318 & 0.165 & +15.3pp & 35\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe average power gain from 4PL over 3PL ranges from +14pp (HumanEval) to +44.7pp (MMLU).\nOn the controlled contamination data, using 3PL reduces $|d|$ from 3.95 to 1.82---a 54\\% signal loss.\nOn MMLU, 46\\% of items have $d < 0.95$, meaning nearly half the items have a meaningful upper asymptote effect.\nIgnoring this produces inflated false alarm rates (3PL FAR: 0.05--0.17 vs 4PL FAR: 0.05) because the 3PL model incorrectly predicts that high-ability models should answer all items correctly.\n\n% ============================================================\n\\subsection{Multiscale Aggregation}\n\\label{sec:lzm}\n\nThe multiscale \\lzm{} statistic aggregates per-benchmark \\lzstar{} via variance-weighted standardization.\nOn the 12-model PSN-IRT case study, \\lzm{} correlates $r = 0.97$ with mean \\lzstar{} across benchmarks, confirming consistency.\nOn controlled contamination data, multi-benchmark aggregation provides an incremental $+0.15$ AUROC over the single-best benchmark ($|d| = 4.12$ at 15\\%).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{\\lzm{} scores for selected models from the PSN-IRT 12-model case study. Per-benchmark \\lzstar{} and aggregate \\lzm{} shown.}\n\\label{tab:lzm}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Model} & \\textbf{MMLU} & \\textbf{HSwag} & \\textbf{GSM8K} & \\textbf{ARC-C} & \\textbf{HEval} & $l_z^m$ \\\\\n\\midrule\nGemini-1.5 & 31.8 & 28.4 & 12.1 & 6.2 & $-$2.4 & 42.8 \\\\\nDeepSeek-V3 & 28.6 & 25.1 & 10.8 & 5.8 & $-$1.2 & 38.2 \\\\\nYi-Lightning & 26.4 & 22.3 & 9.5 & $-$0.3 & $-$1.8 & 35.6 \\\\\nDoubao-Pro & $-$12.5 & $-$8.2 & 4.3 & $-$2.1 & $-$3.8 & $-$8.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDoubao-Pro exhibits the only negative \\lzm{}, driven by strongly negative \\lzstar{} on STEM and Humanities---a selective pattern suggesting domain-specific training data composition rather than benchmark memorization.\n\n% ============================================================\n\\subsection{Domain-Level Analysis}\n\\label{sec:domain}\n\nWe decompose MMLU \\lzstar{} by subject domain to examine the spatial distribution of contamination signals.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Domain-level \\lzstar{} on MMLU: Gemini-1.5 (case study) vs controlled contamination.}\n\\label{tab:domain}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Domain} & \\textbf{Gemini-1.5} & \\textbf{Ctrl 15\\%} & \\textbf{Ctrl clean} \\\\\n\\midrule\nSTEM & 21.2 & 3.8 & 0.1 \\\\\nHumanities & 17.9 & 3.3 & $-$0.2 \\\\\nSocial Sciences & 15.9 & 3.5 & 0.0 \\\\\nOther & 15.3 & 3.2 & 0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe controlled contamination signal is uniform across domains (range 3.2--3.8), consistent with random sampling of contaminated items across all subjects.\nIn contrast, Gemini-1.5 shows a STEM-dominant gradient (21.2 vs 15.3), suggesting non-uniform memorization patterns.\nThis domain-level resolution enables practitioners to distinguish bulk training data leaks (uniform signal) from selective domain contamination (non-uniform).\n\n% ============================================================\n\\subsection{Natural Experiment: Base $\\to$ Chat Pairs}\n\\label{sec:natural}\n\nAs converging evidence from real-world data, we analyze 9 complete base$\\to$chat model pairs from the Open LLM Leaderboard v1, computing $\\Delta l_z^* = l_z^*(\\text{chat}) - l_z^*(\\text{base})$ as a proxy for SFT effects.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Systematic SFT effects on \\lzstar{} across base$\\to$chat pairs ($n=9$).}\n\\label{tab:natural}\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Benchmark} & \\textbf{Mean $\\Delta l_z^*$} & $t$ & $p$ & \\textbf{Interpretation} \\\\\n\\midrule\nHellaSwag & $-$3.8 & $-$4.2 & 0.0008 & SFT improves commonsense \\\\\nGSM8K & +4.5 & 3.8 & 0.004 & Math SFT creates aberrance \\\\\nMMLU & +1.8 & 1.7 & 0.12 & n.s. \\\\\nARC-C & +0.9 & 1.1 & 0.31 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nHellaSwag shows a significant negative shift ($p = 0.0008$): chat SFT improves commonsense reasoning in a way consistent with IRT predictions (reduced aberrance).\nGSM8K shows a significant positive shift ($p = 0.004$): math instruction tuning creates new aberrant patterns, consistent with benchmark-proximal training data.\nOne outlier---CodeLlama-34B-Instruct on GSM8K ($\\Delta l_z^* = 8.7$)---suggests potential direct contamination.\nThese results provide converging evidence but are limited by the IRT parameter quality ($a_r = 0.111$).\n\n% ============================================================\n\\subsection{IRT Parameter Estimation at Scale}\n\\label{sec:refit}\n\nWe investigate whether classical IRT estimation can scale to the full leaderboard by fitting MML-EM 3PL models on progressively larger samples.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{IRT parameter recovery: classical MML-EM vs neural PSN-IRT.}\n\\label{tab:refit}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & $N$ & $a$ Pearson $r$ & $b$ Pearson $r$ & \\textbf{Status} \\\\\n\\midrule\nMML-EM 3PL & 63 & 0.111 & 0.626 & $a$ failure \\\\\nMML-EM 3PL & 178 & 0.130 & 0.660 & $a$ failure persists \\\\\nPSN-IRT (neural) & 12 & validated & validated & reference \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEven at $N = 178$ (the maximum available), discrimination recovery remains poor ($a_r = 0.13$, well below the 0.4 threshold), while difficulty recovery is moderate ($b_r = 0.66$).\nThis confirms that classical IRT estimation cannot recover discrimination parameters from LLM response data---the extreme ability range and violations of local independence in LLM data are structurally incompatible with MML-EM assumptions.\nThis result motivates future work on neural IRT estimation at scale; we note that per-item binary response data for 13K+ models is publicly available.\n\n% ============================================================\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{The minimal-information operating point.}\nIRT-FIT establishes that binary response patterns alone carry sufficient signal for contamination detection at practically relevant contamination levels.\nThe key insight is that IRT item parameters provide structured expectations about response patterns, enabling detection of ``impossible correctness''---high-difficulty items answered correctly due to memorization rather than ability.\nThis structural inductive bias compensates for the absence of labeled training data and model internals.\n\n\\paragraph{Complementarity, not replacement.}\nIRT-FIT is not intended to replace token-level methods.\nThe crossover at ${\\sim}$20\\% contamination (Table~\\ref{tab:advantage}) indicates that token-probability methods like Min-K\\%++ are superior for detecting heavy contamination.\nIRT-FIT's value is precisely in the low-contamination regime (5--10\\%) where detection is hardest and most practically important, and in post-RL settings where token-level methods fail entirely.\n\n\\paragraph{$\\theta$-shift as a methodological contribution.}\nThe $\\theta$-shift boundary condition---where MLE re-estimation absorbs contamination signal---is not specific to IRT-FIT.\nAny ability-contingent detection method will face this confound when ability is estimated from potentially contaminated data.\nThe \\thetafix{} resolution (fixing $\\theta$ to a pre-contamination baseline) is generally applicable and quantifiable.\n\n\\paragraph{Limitations.}\n(1)~IRT-FIT requires validated 4PL item parameters, currently available only from PSN-IRT for select benchmarks.\n(2)~Detection targets intentional SFT contamination (memorization); pretraining exposure produces smooth distributional shifts outside our scope.\n(3)~The memorization fraction (${\\sim}$40\\%) means theoretical power overestimates actual detection---we report both.\n(4)~Classical IRT estimation cannot scale to large model populations ($a_r = 0.13$ at $N = 178$); neural IRT estimation is a prerequisite for leaderboard-scale auditing.\n\n% ============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe introduced IRT-FIT, a contamination detection framework that operates at the minimal-information operating point, requiring only binary response patterns.\nControlled contamination experiments across four model families demonstrate consistent detection ($|d| \\geq 2.42$ at 15\\% contamination) with a predictable power function ($R^2 = 0.968$).\nThe framework retains 80\\% of its detection signal after RL post-training, while token-level methods collapse to chance.\nAt the practically critical 5\\% contamination level, IRT-FIT outperforms all baselines including methods with strictly greater information access.\n\nThe detection frontier perspective opens a research direction: rather than seeking ever-more-powerful detection at each information level, the community can systematically characterize what is detectable at each level of access.\nIRT-FIT establishes the capabilities and limitations at the frontier's minimum, and 13K+ model per-item response data is publicly available for future large-scale audits with improved IRT estimation methods.\n\n% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{10}\n\n\\bibitem[Drasgow et al.(1985)]{drasgow1985appropriateness}\nF.~Drasgow, M.~V. Levine, and M.~E. Williams.\n\\newblock Appropriateness measurement with polychotomous item response models and standardized indices.\n\\newblock \\emph{British Journal of Mathematical and Statistical Psychology}, 38(1):67--86, 1985.\n\n\\bibitem[Shi et al.(2024)]{shi2024detecting}\nW.~Shi, A.~Ajith, M.~Xia, Y.~Huang, D.~Liu, T.~Blevins, D.~Chen, and L.~Zettlemoyer.\n\\newblock Detecting pretraining data from large language models.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Oren et al.(2024)]{oren2024proving}\nY.~Oren, N.~Meister, N.~Chatterji, F.~Ladhak, and T.~B. Hashimoto.\n\\newblock Proving test set contamination in black-box language models.\n\\newblock In \\emph{ICLR (Spotlight)}, 2024.\n\n\\bibitem[Dekoninck et al.(2024)]{dekoninck2024constat}\nJ.~Dekoninck, M.~Nikolic, T.~Tomi\\'{c}, and M.~Baader.\n\\newblock ConStat: Performance-based contamination detection in large language models.\n\\newblock In \\emph{NeurIPS}, 2024.\n\n\\bibitem[Wang et al.(2025)]{wang2025rlcontam}\nY.~Wang, W.~Liu, C.~Yin, J.~Yuan, H.~Zhao, M.~Li, X.~Zhan, and X.~Wang.\n\\newblock Contamination in post-RL reasoning models.\n\\newblock In \\emph{ICLR}, 2026.\n\n\\bibitem[Hong et al.(2021)]{hong2021multiscale}\nM.~Hong, Y.~Lin, and Y.~Cheng.\n\\newblock Multiscale person-fit statistics for tests with polytomous items.\n\\newblock \\emph{Applied Psychological Measurement}, 45(4):236--252, 2021.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "d4f6ceb5-6904-4289-9fd4-5b4508ac984b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T190245 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_c…",
  "leafUuid": "e8b4f09c-a04f-4d3c-9e6a-ce9985d2b81e",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate IRT contamination detection paper",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d"
}
```

---

### Tool call

_source line 24 · 2026-05-20T19:26:26.322Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01GH8SdLm32sd9263BXc2Miv`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8b4f09c-a04f-4d3c-9e6a-ce9985d2b81e",
  "isSidechain": false,
  "requestId": "req_011CbENS5ckEwLvnG3nZ8x7m",
  "type": "assistant",
  "uuid": "e1a4c0d2-c1cb-45e7-8d00-568218064784",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QPty9khHxqSYwUJmPQ9LC7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12764,
      "cache_read_input_tokens": 45863,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12764,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 45863,
          "cache_creation_input_tokens": 12764,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12764
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

_source line 25 · 2026-05-20T19:26:27.061Z_

<details><summary>↩ Tool result · reported error · `toolu_01GH8SdLm32sd9263BXc2Miv`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
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
(/usr/share/texlive/texmf-dist/tex/latex/tablefootnote/tablefootnote.sty
(/usr/share/texlive/texmf-dist/tex/latex/letltxmacro/letltxmacro.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xifthen/xifthen.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/calc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/ifthen.sty)
(/usr/share/texlive/texmf-dist/tex/latex/ifmtarg/ifmtarg.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)
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

Package natbib Warning: Citation `shi2024detecting' on page 1 undefined on inpu
t line 46.


Package natbib Warning: Citation `oren2024proving' on page 1 undefined on input
 line 46.


Package natbib Warning: Citation `dekoninck2024constat' on page 1 undefined on 
input line 46.


Package natbib Warning: Citation `wang2025rlcontam' on page 1 undefined on inpu
t line 47.


Overfull \hbox (19.4167pt too wide) in paragraph at lines 49--51
[]\T1/pt

... [1383 characters truncated] ...

                           $), absorbing part of the ...

[2]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 130.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `subscript' on input line 130.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `superscript' on input line 130.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 130.


Package natbib Warning: Citation `hong2021multiscale' on page 3 undefined on in
put line 132.

! Double subscript.
l.150 \textbf{Condition} & \textbf{Acc} & $l_z^*_
                                                 {\text{free}}$ & $l_z^*_{\t...

! Double subscript.
l.150 ...bf{Acc} & $l_z^*_{\text{free}}$ & $l_z^*_
                                                  {\text{fixed}}$ & $\hat\th...

! Double subscript.
l.150 ...{fixed}}$ & $\hat\theta$ & $\Delta l_z^*_
                                                  {\text{fixed}}$ \\
! Double subscript.
l.162 ...e dose-response is non-monotonic ($l_z^*_
                                                  \text{free}$: 2.8 at 15\% ...

! Double subscript.
l.162 ...tores strict monotonicity ($\Delta l_z^*_
                                                  \text{fixed}$: 3.5 at 15\%...

! Double subscript.
l.178 ...extbf{Acc$_\text{15\%}$} & $\Delta l_z^*_
                                                  \text{free}$ & $\Delta l_z...

! Double subscript.
l.178 ...Delta l_z^*_\text{free}$ & $\Delta l_z^*_
                                                  \text{fixed}$ & $|d|$ & \t...

[3]

LaTeX Warning: Reference `tab:gsm8k' on page 4 undefined on input line 195.

! Double subscript.
l.204 ...odel} & $n_\text{items}$ & $\Delta l_z^*_
                                                  \text{fixed}$ & $|d|$ & Si...


LaTeX Warning: Reference `tab:doseresponse' on page 4 undefined on input line 2
15.


LaTeX Warning: `h' float specifier changed to `ht'.

[4]

Package natbib Warning: Citation `wang2025rlcontam' on page 5 undefined on inpu
t line 293.

! Double subscript.
l.315 ...al (AUROC 0.92 $\to$ 0.85, $\Delta l_z^*_
                                                  \text{fixed}$: 3.5 $\to$ 2...

! Double subscript.
l.326 $\Delta l_z^*_
                    \text{fixed}$ & 3.5 & 2.8 & $-$20\% \\

LaTeX Warning: `h' float specifier changed to `ht'.

[5] [6]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 451.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\to' on input line 451.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 451.

[7]

LaTeX Warning: Reference `tab:advantage' on page 8 undefined on input line 515.


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
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts
/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmm
i8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>
&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist
/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p
ublic/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/ur
w/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (9 pages, 219876 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e1a4c0d2-c1cb-45e7-8d00-568218064784",
  "isSidechain": false,
  "promptId": "eb66b833-472c-4a64-b5b3-e6647c252907",
  "type": "user",
  "uuid": "0db2b830-f4a7-4806-b0ec-4d82c49899a9",
  "toolUseResult": "Error: Exit code 1\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/tablefootnote/tablefootnote.sty\n(/usr/share/texlive/texmf-dist/tex/latex/letltxmacro/letltxmacro.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xifthen/xifthen.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/calc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/ifthen.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/ifmtarg/ifmtarg.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `shi2024detecting' on page 1 undefined on inpu\nt line 46.\n\n\nPackage natbib Warning: Citation `oren2024proving' on page 1 undefined on input\n line 46.\n\n\nPackage natbib Warning: Citation `dekoninck2024constat' on page 1 undefined on \ninput line 46.\n\n\nPackage natbib Warning: Citation `wang2025rlcontam' on page 1 undefined on inpu\nt line 47.\n\n\nOverfull \\hbox (19.4167pt too wide) in paragraph at lines 49--51\n[]\\T1/pt\n\n... [1383 characters truncated] ...\n\n                           $), absorbing part of the ...\n\n[2]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 130.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `subscript' on input line 130.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `superscript' on input line 130.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 130.\n\n\nPackage natbib Warning: Citation `hong2021multiscale' on page 3 undefined on in\nput line 132.\n\n! Double subscript.\nl.150 \\textbf{Condition} & \\textbf{Acc} & $l_z^*_\n                                                 {\\text{free}}$ & $l_z^*_{\\t...\n\n! Double subscript.\nl.150 ...bf{Acc} & $l_z^*_{\\text{free}}$ & $l_z^*_\n                                                  {\\text{fixed}}$ & $\\hat\\th...\n\n! Double subscript.\nl.150 ...{fixed}}$ & $\\hat\\theta$ & $\\Delta l_z^*_\n                                                  {\\text{fixed}}$ \\\\\n! Double subscript.\nl.162 ...e dose-response is non-monotonic ($l_z^*_\n                                                  \\text{free}$: 2.8 at 15\\% ...\n\n! Double subscript.\nl.162 ...tores strict monotonicity ($\\Delta l_z^*_\n                                                  \\text{fixed}$: 3.5 at 15\\%...\n\n! Double subscript.\nl.178 ...extbf{Acc$_\\text{15\\%}$} & $\\Delta l_z^*_\n                                                  \\text{free}$ & $\\Delta l_z...\n\n! Double subscript.\nl.178 ...Delta l_z^*_\\text{free}$ & $\\Delta l_z^*_\n                                                  \\text{fixed}$ & $|d|$ & \\t...\n\n[3]\n\nLaTeX Warning: Reference `tab:gsm8k' on page 4 undefined on input line 195.\n\n! Double subscript.\nl.204 ...odel} & $n_\\text{items}$ & $\\Delta l_z^*_\n                                                  \\text{fixed}$ & $|d|$ & Si...\n\n\nLaTeX Warning: Reference `tab:doseresponse' on page 4 undefined on input line 2\n15.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[4]\n\nPackage natbib Warning: Citation `wang2025rlcontam' on page 5 undefined on inpu\nt line 293.\n\n! Double subscript.\nl.315 ...al (AUROC 0.92 $\\to$ 0.85, $\\Delta l_z^*_\n                                                  \\text{fixed}$: 3.5 $\\to$ 2...\n\n! Double subscript.\nl.326 $\\Delta l_z^*_\n                    \\text{fixed}$ & 3.5 & 2.8 & $-$20\\% \\\\\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[5] [6]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 451.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\to' on input line 451.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 451.\n\n[7]\n\nLaTeX Warning: Reference `tab:advantage' on page 8 undefined on input line 515.\n\n\n[8]\n\nPackage natbib Warning: There were undefined citations.\n\n[9] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts\n/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmm\ni8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/sh\nare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist\n/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\nublic/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/ur\nw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (9 pages, 219876 bytes).\nTranscript written on paper.log.",
  "sourceToolAssistantUUID": "e1a4c0d2-c1cb-45e7-8d00-568218064784",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-20T19:26:39.342Z_

<details><summary>Logged reasoning block</summary>

```text
The PDF was generated (9 pages, 219876 bytes) but there are "double subscript" errors due to `l_z^*_{\text{free}}` syntax. In LaTeX, `^*_{\text{free}}` is a double subscript because `^*` is a superscript and then `_` tries to add a subscript to something that already has a subscript. I need to fix the LaTeX math expressions to use proper grouping like `{l_z^*}_{\text{free}}` or `l_z^{*\text{free}}` or use a different approach.


I'll restructure these expressions to resolve the double subscript conflicts—either by grouping the base with its superscript first like `${l_z^*}_{\text{free}}$`, or by reorganizing to `$l_{z,\text{free}}^{*}$` to separate the subscript and superscript cleanly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0db2b830-f4a7-4806-b0ec-4d82c49899a9",
  "isSidechain": false,
  "requestId": "req_011CbENSUqzdPC8B7TVqhayv",
  "type": "assistant",
  "uuid": "3967f834-7b4a-4f03-b394-0dd24d95975f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TnkZpFK2HCCeKmUFofAtWo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4270,
      "cache_read_input_tokens": 58627,
      "output_tokens": 387,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4270,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 387,
          "cache_read_input_tokens": 58627,
          "cache_creation_input_tokens": 4270,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4270
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

_source line 27 · 2026-05-20T19:26:39.348Z_

PDF generated but with double-subscript errors. Fixing the LaTeX math notation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3967f834-7b4a-4f03-b394-0dd24d95975f",
  "isSidechain": false,
  "requestId": "req_011CbENSUqzdPC8B7TVqhayv",
  "type": "assistant",
  "uuid": "8b3df25b-ea93-472f-a1f5-95dc0568c08b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TnkZpFK2HCCeKmUFofAtWo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4270,
      "cache_read_input_tokens": 58627,
      "output_tokens": 387,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4270,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 387,
          "cache_read_input_tokens": 58627,
          "cache_creation_input_tokens": 4270,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4270
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

_source line 28 · 2026-05-20T19:26:39.443Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RE7D3cwXrHtAhaytmeAErg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best/paper.tex",
  "offset": 145,
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b3df25b-ea93-472f-a1f5-95dc0568c08b",
  "isSidechain": false,
  "requestId": "req_011CbENSUqzdPC8B7TVqhayv",
  "type": "assistant",
  "uuid": "9a175c38-c9a2-47a4-ae44-c9db950d9a57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TnkZpFK2HCCeKmUFofAtWo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4270,
      "cache_read_input_tokens": 58627,
      "output_tokens": 387,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4270,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 387,
          "cache_read_input_tokens": 58627,
          "cache_creation_input_tokens": 4270,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4270
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

_source line 29 · 2026-05-20T19:26:39.451Z_

<details><summary>↩ Tool result · `toolu_01RE7D3cwXrHtAhaytmeAErg`</summary>

```text
145	\small
146	\caption{Controlled contamination pilot: Qwen3.5-9B on MMLU. $\Delta l_z^*$ computed relative to clean seed 1. \thetafix{} fixes $\theta$ to clean baseline.}
147	\label{tab:pilot}
148	\begin{tabular}{lccccc}
149	\toprule
150	\textbf{Condition} & \textbf{Acc} & $l_z^*_{\text{free}}$ & $l_z^*_{\text{fixed}}$ & $\hat\theta$ & $\Delta l_z^*_{\text{fixed}}$ \\
151	\midrule
152	Clean (s1) & 0.71 & 7.2 & 7.2 & $-$0.08 & --- \\
153	Clean (s2) & 0.71 & 6.8 & 6.8 & $-$0.09 & 0.4 \\
154	Contam 15\% & 0.76 & 2.8 & 10.5 & 0.22 & 3.5 \\
155	Contam 50\% & 0.80 & 4.9 & 16.8 & 0.41 & 9.8 \\
156	\bottomrule
157	\end{tabular}
158	\end{table}
159	
160	The clean-vs-clean $\Delta l_z^* = 0.4$ establishes a low noise floor.
161	At 15\% contamination, $|d| = 3.95$ (far exceeding the $|d| = 0.8$ threshold for a large effect).
162	Under free-$\theta$ estimation, the dose-response is non-monotonic ($l_z^*_\text{free}$: 2.8 at 15\% vs 4.9 at 50\%), but \thetafix{} analysis restores strict monotonicity ($\Delta l_z^*_\text{fixed}$: 3.5 at 15\%, 9.8 at 50\%; ratio = 2.80).
163	
164	The seen/unseen accuracy split reveals the memorization fingerprint: at 15\% contamination, accuracy on seen items is 0.86 vs 0.73 on unseen items, with a memorization fraction of 0.42---meaning 42\% of seen items produce identifiable memorization signatures.
165	
166	\subsection{Cross-Model Controlled Contamination}
167	\label{sec:crossmodel}
168	
169	We extend to four model families across three benchmarks (MMLU, GSM8K, HellaSwag) at six contamination levels (0/5/10/15/25/50\%).
170	
171	\begin{table}[h]
172	\centering
173	\small
174	\caption{Cross-model detection at 15\% contamination on MMLU. All four models produce significant detection signals ($|d| > 2.0$).}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a175c38-c9a2-47a4-ae44-c9db950d9a57",
  "isSidechain": false,
  "promptId": "eb66b833-472c-4a64-b5b3-e6647c252907",
  "type": "user",
  "uuid": "ea66875a-9805-47a4-9b6a-98ed88d8f1bf",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best/paper.tex",
      "content": "\\small\n\\caption{Controlled contamination pilot: Qwen3.5-9B on MMLU. $\\Delta l_z^*$ computed relative to clean seed 1. \\thetafix{} fixes $\\theta$ to clean baseline.}\n\\label{tab:pilot}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Acc} & $l_z^*_{\\text{free}}$ & $l_z^*_{\\text{fixed}}$ & $\\hat\\theta$ & $\\Delta l_z^*_{\\text{fixed}}$ \\\\\n\\midrule\nClean (s1) & 0.71 & 7.2 & 7.2 & $-$0.08 & --- \\\\\nClean (s2) & 0.71 & 6.8 & 6.8 & $-$0.09 & 0.4 \\\\\nContam 15\\% & 0.76 & 2.8 & 10.5 & 0.22 & 3.5 \\\\\nContam 50\\% & 0.80 & 4.9 & 16.8 & 0.41 & 9.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe clean-vs-clean $\\Delta l_z^* = 0.4$ establishes a low noise floor.\nAt 15\\% contamination, $|d| = 3.95$ (far exceeding the $|d| = 0.8$ threshold for a large effect).\nUnder free-$\\theta$ estimation, the dose-response is non-monotonic ($l_z^*_\\text{free}$: 2.8 at 15\\% vs 4.9 at 50\\%), but \\thetafix{} analysis restores strict monotonicity ($\\Delta l_z^*_\\text{fixed}$: 3.5 at 15\\%, 9.8 at 50\\%; ratio = 2.80).\n\nThe seen/unseen accuracy split reveals the memorization fingerprint: at 15\\% contamination, accuracy on seen items is 0.86 vs 0.73 on unseen items, with a memorization fraction of 0.42---meaning 42\\% of seen items produce identifiable memorization signatures.\n\n\\subsection{Cross-Model Controlled Contamination}\n\\label{sec:crossmodel}\n\nWe extend to four model families across three benchmarks (MMLU, GSM8K, HellaSwag) at six contamination levels (0/5/10/15/25/50\\%).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model detection at 15\\% contamination on MMLU. All four models produce significant detection signals ($|d| > 2.0$).}",
      "numLines": 30,
      "startLine": 145,
      "totalLines": 579
    }
  },
  "sourceToolAssistantUUID": "9a175c38-c9a2-47a4-ae44-c9db950d9a57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-20T19:26:39.456Z_

```json
{
  "parentUuid": "ea66875a-9805-47a4-9b6a-98ed88d8f1bf",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "2de50cd5-bed9-4650-827c-56672b41b66f",
  "timestamp": "2026-05-20T19:26:39.456Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T190245 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_c…",
  "leafUuid": "2de50cd5-bed9-4650-827c-56672b41b66f",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate IRT contamination detection paper",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d"
}
```

---

### Assistant

_source line 33 · 2026-05-20T19:26:43.931Z_

I need to fix all double-subscript expressions. The issue is `l_z^*_{\text{...}}` — I'll use `{l_z^*}_{\text{...}}` throughout.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2de50cd5-bed9-4650-827c-56672b41b66f",
  "isSidechain": false,
  "requestId": "req_011CbENTPpA3ztv9Xxecz7Z5",
  "type": "assistant",
  "uuid": "a7fe8f7b-328e-4b21-a750-dee56a20b42c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ToUgb11k82d2pGd31GdpeV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1275,
      "cache_read_input_tokens": 62897,
      "output_tokens": 329,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1275,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 329,
          "cache_read_input_tokens": 62897,
          "cache_creation_input_tokens": 1275,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1275
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

_source line 34 · 2026-05-20T19:26:46.588Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01Y6h3PenNx2L327wRFcNxXQ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best/paper.tex",
  "old_string": "\\textbf{Condition} & \\textbf{Acc} & $l_z^*_{\\text{free}}$ & $l_z^*_{\\text{fixed}}$ & $\\hat\\theta$ & $\\Delta l_z^*_{\\text{fixed}}$ \\\\",
  "new_string": "\\textbf{Condition} & \\textbf{Acc} & ${l_z^*}_{\\text{free}}$ & ${l_z^*}_{\\text{fixed}}$ & $\\hat\\theta$ & ${\\Delta l_z^*}_{\\text{fixed}}$ \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7fe8f7b-328e-4b21-a750-dee56a20b42c",
  "isSidechain": false,
  "requestId": "req_011CbENTPpA3ztv9Xxecz7Z5",
  "type": "assistant",
  "uuid": "b85d58d2-ccca-42e9-bd39-83ab01f69df8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ToUgb11k82d2pGd31GdpeV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1275,
      "cache_read_input_tokens": 62897,
      "output_tokens": 329,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1275,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 329,
          "cache_read_input_tokens": 62897,
          "cache_creation_input_tokens": 1275,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1275
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

_source line 35 · 2026-05-20T19:26:46.609Z_

<details><summary>↩ Tool result · `toolu_01Y6h3PenNx2L327wRFcNxXQ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b85d58d2-ccca-42e9-bd39-83ab01f69df8",
  "isSidechain": false,
  "promptId": "eb66b833-472c-4a64-b5b3-e6647c252907",
  "type": "user",
  "uuid": "c7c70cd9-9d5b-4a15-9d4d-ee0741e9ae8a",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best/paper.tex",
    "oldString": "\\textbf{Condition} & \\textbf{Acc} & $l_z^*_{\\text{free}}$ & $l_z^*_{\\text{fixed}}$ & $\\hat\\theta$ & $\\Delta l_z^*_{\\text{fixed}}$ \\\\",
    "newString": "\\textbf{Condition} & \\textbf{Acc} & ${l_z^*}_{\\text{free}}$ & ${l_z^*}_{\\text{fixed}}$ & $\\hat\\theta$ & ${\\Delta l_z^*}_{\\text{fixed}}$ \\\\",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 147,
        "oldLines": 7,
        "newStart": 147,
        "newLines": 7,
        "lines": [
          " \\label{tab:pilot}",
          " \\begin{tabular}{lccccc}",
          " \\toprule",
          "-\\textbf{Condition} & \\textbf{Acc} & $l_z^*_{\\text{free}}$ & $l_z^*_{\\text{fixed}}$ & $\\hat\\theta$ & $\\Delta l_z^*_{\\text{fixed}}$ \\\\",
          "+\\textbf{Condition} & \\textbf{Acc} & ${l_z^*}_{\\text{free}}$ & ${l_z^*}_{\\text{fixed}}$ & $\\hat\\theta$ & ${\\Delta l_z^*}_{\\text{fixed}}$ \\\\",
          " \\midrule",
          " Clean (s1) & 0.71 & 7.2 & 7.2 & $-$0.08 & --- \\\\",
          " Clean (s2) & 0.71 & 6.8 & 6.8 & $-$0.09 & 0.4 \\\\"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "b85d58d2-ccca-42e9-bd39-83ab01f69df8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-20T19:26:51.652Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01WRCu1L42x6ZaVMwoopSNDJ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best/paper.tex",
  "old_string": "Under free-$\\theta$ estimation, the dose-response is non-monotonic ($l_z^*_\\text{free}$: 2.8 at 15\\% vs 4.9 at 50\\%), but \\thetafix{} analysis restores strict monotonicity ($\\Delta l_z^*_\\text{fixed}$: 3.5 at 15\\%, 9.8 at 50\\%; ratio = 2.80).",
  "new_string": "Under free-$\\theta$ estimation, the dose-response is non-monotonic (${l_z^*}_\\text{free}$: 2.8 at 15\\% vs 4.9 at 50\\%), but \\thetafix{} analysis restores strict monotonicity (${\\Delta l_z^*}_\\text{fixed}$: 3.5 at 15\\%, 9.8 at 50\\%; ratio = 2.80)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7c70cd9-9d5b-4a15-9d4d-ee0741e9ae8a",
  "isSidechain": false,
  "requestId": "req_011CbENTvQuftpegFuBTRkrw",
  "type": "assistant",
  "uuid": "28766e78-220b-4ec8-8ee8-52c08e199bce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ucj1BiBUwu2m5Y5TADEf11",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 419,
      "cache_read_input_tokens": 64172,
      "output_tokens": 383,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 419,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 383,
          "cache_read_input_tokens": 64172,
          "cache_creation_input_tokens": 419,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 419
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

_source line 37 · 2026-05-20T19:26:51.667Z_

<details><summary>↩ Tool result · `toolu_01WRCu1L42x6ZaVMwoopSNDJ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28766e78-220b-4ec8-8ee8-52c08e199bce",
  "isSidechain": false,
  "promptId": "eb66b833-472c-4a64-b5b3-e6647c252907",
  "type": "user",
  "uuid": "ff78b3c2-aaab-4ee0-92bb-d58bf7aaceea",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best/paper.tex",
    "oldString": "Under free-$\\theta$ estimation, the dose-response is non-monotonic ($l_z^*_\\text{free}$: 2.8 at 15\\% vs 4.9 at 50\\%), but \\thetafix{} analysis restores strict monotonicity ($\\Delta l_z^*_\\text{fixed}$: 3.5 at 15\\%, 9.8 at 50\\%; ratio = 2.80).",
    "newString": "Under free-$\\theta$ estimation, the dose-response is non-monotonic (${l_z^*}_\\text{free}$: 2.8 at 15\\% vs 4.9 at 50\\%), but \\thetafix{} analysis restores strict monotonicity (${\\Delta l_z^*}_\\text{fixed}$: 3.5 at 15\\%, 9.8 at 50\\%; ratio = 2.80).",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 159,
        "oldLines": 7,
        "newStart": 159,
        "newLines": 7,
        "lines": [
          " ",
          " The clean-vs-clean $\\Delta l_z^* = 0.4$ establishes a low noise floor.",
          " At 15\\% contamination, $|d| = 3.95$ (far exceeding the $|d| = 0.8$ threshold for a large effect).",
          "-Under free-$\\theta$ estimation, the dose-response is non-monotonic ($l_z^*_\\text{free}$: 2.8 at 15\\% vs 4.9 at 50\\%), but \\thetafix{} analysis restores strict monotonicity ($\\Delta l_z^*_\\text{fixed}$: 3.5 at 15\\%, 9.8 at 50\\%; ratio = 2.80).",
          "+Under free-$\\theta$ estimation, the dose-response is non-monotonic (${l_z^*}_\\text{free}$: 2.8 at 15\\% vs 4.9 at 50\\%), but \\thetafix{} analysis restores strict monotonicity (${\\Delta l_z^*}_\\text{fixed}$: 3.5 at 15\\%, 9.8 at 50\\%; ratio = 2.80).",
          " ",
          " The seen/unseen accuracy split reveals the memorization fingerprint: at 15\\% contamination, accuracy on seen items is 0.86 vs 0.73 on unseen items, with a memorization fraction of 0.42---meaning 42\\% of seen items produce identifiable memorization signatures.",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "28766e78-220b-4ec8-8ee8-52c08e199bce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-20T19:26:56.211Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01SUKkFYUPdzfgikgpd2iZVs`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best/paper.tex",
  "old_string": "\\textbf{Acc$_\\text{15\\%}$} & $\\Delta l_z^*_\\text{free}$ & $\\Delta l_z^*_\\text{fixed}$ & $|d|$ & \\textbf{Mem.~frac} \\\\",
  "new_string": "\\textbf{Acc$_\\text{15\\%}$} & ${\\Delta l_z^*}_\\text{free}$ & ${\\Delta l_z^*}_\\text{fixed}$ & $|d|$ & \\textbf{Mem.~frac} \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff78b3c2-aaab-4ee0-92bb-d58bf7aaceea",
  "isSidechain": false,
  "requestId": "req_011CbENUJ1RyTtDdFz9vaEqY",
  "type": "assistant",
  "uuid": "62f31b51-9b74-42d1-a759-53f78976a1db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ufp2oK62eeswZbeex6XXVp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 454,
      "cache_read_input_tokens": 64591,
      "output_tokens": 302,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 454,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 302,
          "cache_read_input_tokens": 64591,
          "cache_creation_input_tokens": 454,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 454
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

_source line 39 · 2026-05-20T19:26:56.220Z_

<details><summary>↩ Tool result · `toolu_01SUKkFYUPdzfgikgpd2iZVs`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62f31b51-9b74-42d1-a759-53f78976a1db",
  "isSidechain": false,
  "promptId": "eb66b833-472c-4a64-b5b3-e6647c252907",
  "type": "user",
  "uuid": "a0bff5bb-d9df-4f29-9741-afab7cc8630b",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best/paper.tex",
    "oldString": "\\textbf{Acc$_\\text{15\\%}$} & $\\Delta l_z^*_\\text{free}$ & $\\Delta l_z^*_\\text{fixed}$ & $|d|$ & \\textbf{Mem.~frac} \\\\",
    "newString": "\\textbf{Acc$_\\text{15\\%}$} & ${\\Delta l_z^*}_\\text{free}$ & ${\\Delta l_z^*}_\\text{fixed}$ & $|d|$ & \\textbf{Mem.~frac} \\\\",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 175,
        "oldLines": 7,
        "newStart": 175,
        "newLines": 7,
        "lines": [
          " \\label{tab:crossmodel}",
          " \\begin{tabular}{lcccccc}",
          " \\toprule",
          "-\\textbf{Model} & \\textbf{Acc$_\\text{clean}$} & \\textbf{Acc$_\\text{15\\%}$} & $\\Delta l_z^*_\\text{free}$ & $\\Delta l_z^*_\\text{fixed}$ & $|d|$ & \\textbf{Mem.~frac} \\\\",
          "+\\textbf{Model} & \\textbf{Acc$_\\text{clean}$} & \\textbf{Acc$_\\text{15\\%}$} & ${\\Delta l_z^*}_\\text{free}$ & ${\\Delta l_z^*}_\\text{fixed}$ & $|d|$ & \\textbf{Mem.~frac} \\\\",
          " \\midrule",
          " Qwen3.5-9B & 0.71 & 0.76 & $-$4.1 & 3.5 & 3.95 & 0.42 \\\\",
          " Gemma-4-31B & 0.78 & 0.84 & $-$4.8 & 4.2 & 4.52 & 0.48 \\\\"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "62f31b51-9b74-42d1-a759-53f78976a1db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-20T19:26:58.605Z_

Now let me find and fix the remaining double-subscript instances.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0bff5bb-d9df-4f29-9741-afab7cc8630b",
  "isSidechain": false,
  "requestId": "req_011CbENUdbADPq47jTCZh8yq",
  "type": "assistant",
  "uuid": "700bd495-acb4-4feb-89f8-8560aede6cad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RBTYyXdqRLQ2WMLsjJ6cTP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 373,
      "cache_read_input_tokens": 65045,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 373,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 161,
          "cache_read_input_tokens": 65045,
          "cache_creation_input_tokens": 373,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 373
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

_source line 41 · 2026-05-20T19:26:59.546Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01JLiDNRzRp4JqSFT8R9BxmD`</summary>

```json
{
  "pattern": "l_z\\^\\*_",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best/paper.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "700bd495-acb4-4feb-89f8-8560aede6cad",
  "isSidechain": false,
  "requestId": "req_011CbENUdbADPq47jTCZh8yq",
  "type": "assistant",
  "uuid": "e373d057-cfb1-4669-879c-8dcecb79f50a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RBTYyXdqRLQ2WMLsjJ6cTP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 373,
      "cache_read_input_tokens": 65045,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 373,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 161,
          "cache_read_input_tokens": 65045,
          "cache_creation_input_tokens": 373,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 373
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

_source line 42 · 2026-05-20T19:26:59.563Z_

<details><summary>↩ Tool result · `toolu_01JLiDNRzRp4JqSFT8R9BxmD`</summary>

```text
204:\textbf{Model} & $n_\text{items}$ & $\Delta l_z^*_\text{fixed}$ & $|d|$ & Sig.~($p<.05$) \\
315:The result is striking: \lzstar{} retains 80\% of its detection signal (AUROC 0.92 $\to$ 0.85, $\Delta l_z^*_\text{fixed}$: 3.5 $\to$ 2.8, $|d|$: 3.95 $\to$ 3.15), while Min-K\%++ drops from 0.89 to 0.54 (4\% retention) and PPL-based detection drops from 0.86 to 0.52 (2\% retention).
326:$\Delta l_z^*_\text{fixed}$ & 3.5 & 2.8 & $-$20\% \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e373d057-cfb1-4669-879c-8dcecb79f50a",
  "isSidechain": false,
  "promptId": "eb66b833-472c-4a64-b5b3-e6647c252907",
  "type": "user",
  "uuid": "21587aca-674c-4c83-bfd2-956438202bd9",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "204:\\textbf{Model} & $n_\\text{items}$ & $\\Delta l_z^*_\\text{fixed}$ & $|d|$ & Sig.~($p<.05$) \\\\\n315:The result is striking: \\lzstar{} retains 80\\% of its detection signal (AUROC 0.92 $\\to$ 0.85, $\\Delta l_z^*_\\text{fixed}$: 3.5 $\\to$ 2.8, $|d|$: 3.95 $\\to$ 3.15), while Min-K\\%++ drops from 0.89 to 0.54 (4\\% retention) and PPL-based detection drops from 0.86 to 0.52 (2\\% retention).\n326:$\\Delta l_z^*_\\text{fixed}$ & 3.5 & 2.8 & $-$20\\% \\\\",
    "numLines": 3
  },
  "sourceToolAssistantUUID": "e373d057-cfb1-4669-879c-8dcecb79f50a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T19:27:03.200Z_

<details open><summary>🔧 Tool call — Edit · `toolu_014tV36nqmNcsMBDETKyAbRg`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best/paper.tex",
  "old_string": "$\\Delta l_z^*_\\text{fixed}$",
  "new_string": "${\\Delta l_z^*}_\\text{fixed}$"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21587aca-674c-4c83-bfd2-956438202bd9",
  "isSidechain": false,
  "requestId": "req_011CbENUsusiatrbzxqfq4jG",
  "type": "assistant",
  "uuid": "b79ae727-5ea7-4b0c-b3d1-48aa52809d9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qes8iGsrTDYEZaefZ8Wiph",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 409,
      "cache_read_input_tokens": 65418,
      "output_tokens": 190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 409,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 190,
          "cache_read_input_tokens": 65418,
          "cache_creation_input_tokens": 409,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 409
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

_source line 44 · 2026-05-20T19:27:03.215Z_

<details><summary>↩ Tool result · `toolu_014tV36nqmNcsMBDETKyAbRg`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best/paper.tex has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b79ae727-5ea7-4b0c-b3d1-48aa52809d9e",
  "isSidechain": false,
  "promptId": "eb66b833-472c-4a64-b5b3-e6647c252907",
  "type": "user",
  "uuid": "28268018-a9db-4c5e-bd1e-45b2568d1f00",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best/paper.tex",
    "oldString": "$\\Delta l_z^*_\\text{fixed}$",
    "newString": "${\\Delta l_z^*}_\\text{fixed}$",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 201,
        "oldLines": 7,
        "newStart": 201,
        "newLines": 7,
        "lines": [
          " \\label{tab:gsm8k}",
          " \\begin{tabular}{lcccc}",
          " \\toprule",
          "-\\textbf{Model} & $n_\\text{items}$ & $\\Delta l_z^*_\\text{fixed}$ & $|d|$ & Sig.~($p<.05$) \\\\",
          "+\\textbf{Model} & $n_\\text{items}$ & ${\\Delta l_z^*}_\\text{fixed}$ & $|d|$ & Sig.~($p<.05$) \\\\",
          " \\midrule",
          " Qwen3.5-9B & 1,319 & 1.8 & 1.42 & \\checkmark \\\\",
          " Gemma-4-31B & 1,319 & 2.1 & 1.68 & \\checkmark \\\\"
        ]
      },
      {
        "oldStart": 312,
        "oldLines": 7,
        "newStart": 312,
        "newLines": 7,
        "lines": [
          " \\end{tabular}",
          " \\end{table}",
          " ",
          "-The result is striking: \\lzstar{} retains 80\\% of its detection signal (AUROC 0.92 $\\to$ 0.85, $\\Delta l_z^*_\\text{fixed}$: 3.5 $\\to$ 2.8, $|d|$: 3.95 $\\to$ 3.15), while Min-K\\%++ drops from 0.89 to 0.54 (4\\% retention) and PPL-based detection drops from 0.86 to 0.52 (2\\% retention).",
          "+The result is striking: \\lzstar{} retains 80\\% of its detection signal (AUROC 0.92 $\\to$ 0.85, ${\\Delta l_z^*}_\\text{fixed}$: 3.5 $\\to$ 2.8, $|d|$: 3.95 $\\to$ 3.15), while Min-K\\%++ drops from 0.89 to 0.54 (4\\% retention) and PPL-based detection drops from 0.86 to 0.52 (2\\% retention).",
          " ",
          " \\begin{table}[h]",
          " \\centering"
        ]
      },
      {
        "oldStart": 323,
        "oldLines": 7,
        "newStart": 323,
        "newLines": 7,
        "lines": [
          " \\toprule",
          " \\textbf{Metric} & \\textbf{Pre-RL} & \\textbf{Post-RL} & \\textbf{Change} \\\\",
          " \\midrule",
          "-$\\Delta l_z^*_\\text{fixed}$ & 3.5 & 2.8 & $-$20\\% \\\\",
          "+${\\Delta l_z^*}_\\text{fixed}$ & 3.5 & 2.8 & $-$20\\% \\\\",
          " Cohen's $d$ & $-$3.95 & $-$3.15 & $-$20\\% \\\\",
          " Seen accuracy & 0.86 & 0.82 & $-$4pp \\\\",
          " Unseen accuracy & 0.73 & 0.76 & +3pp \\\\"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  },
  "sourceToolAssistantUUID": "b79ae727-5ea7-4b0c-b3d1-48aa52809d9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-20T19:27:05.759Z_

Now recompile.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28268018-a9db-4c5e-bd1e-45b2568d1f00",
  "isSidechain": false,
  "requestId": "req_011CbENV9ZD8UJdzLbw3t4fZ",
  "type": "assistant",
  "uuid": "f4a36b25-50c0-461b-b5dd-22f417a287d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V8E8J741m28MtX1uHDMgS9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 268,
      "cache_read_input_tokens": 65827,
      "output_tokens": 184,
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
          "output_tokens": 184,
          "cache_read_input_tokens": 65827,
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

### Tool call

_source line 46 · 2026-05-20T19:27:07.382Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01UHS3VL9huMX345rS2LAD9Y`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best && pdflatex -interaction=nonstopmode paper.tex 2>&1 | grep -E \"^!|Output written|pages\"",
  "description": "Recompile LaTeX and check for errors",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4a36b25-50c0-461b-b5dd-22f417a287d0",
  "isSidechain": false,
  "requestId": "req_011CbENV9ZD8UJdzLbw3t4fZ",
  "type": "assistant",
  "uuid": "495b54f8-e563-41a0-9377-ea21420b7c04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V8E8J741m28MtX1uHDMgS9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 268,
      "cache_read_input_tokens": 65827,
      "output_tokens": 184,
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
          "output_tokens": 184,
          "cache_read_input_tokens": 65827,
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

_source line 47 · 2026-05-20T19:27:07.892Z_

<details><summary>↩ Tool result · `toolu_01UHS3VL9huMX345rS2LAD9Y`</summary>

```text
! Extra }, or forgotten $.
Output written on paper.pdf (9 pages, 222835 bytes).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "495b54f8-e563-41a0-9377-ea21420b7c04",
  "isSidechain": false,
  "promptId": "eb66b833-472c-4a64-b5b3-e6647c252907",
  "type": "user",
  "uuid": "a1010a33-c906-49dd-ba2d-57fd12f67713",
  "toolUseResult": {
    "stdout": "! Extra }, or forgotten $.\nOutput written on paper.pdf (9 pages, 222835 bytes).",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "495b54f8-e563-41a0-9377-ea21420b7c04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-20T19:27:10.388Z_

<details><summary>Logged reasoning block</summary>

```text
There's still an error. Let me check which line has the "Extra }, or forgotten $" issue.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1010a33-c906-49dd-ba2d-57fd12f67713",
  "isSidechain": false,
  "requestId": "req_011CbENVVQoz6MGahVGezmYW",
  "type": "assistant",
  "uuid": "278ab89a-0be3-4b9d-936f-2cf52e1c8aab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Ns6rDRvvpZ3zyzo8gnrC7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 220,
      "cache_read_input_tokens": 66095,
      "output_tokens": 219,
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
          "output_tokens": 219,
          "cache_read_input_tokens": 66095,
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

_source line 49 · 2026-05-20T19:27:10.870Z_

Still an error. Let me find it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "278ab89a-0be3-4b9d-936f-2cf52e1c8aab",
  "isSidechain": false,
  "requestId": "req_011CbENVVQoz6MGahVGezmYW",
  "type": "assistant",
  "uuid": "1ee20e37-37a9-4088-b14d-a3c68b8bc698",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Ns6rDRvvpZ3zyzo8gnrC7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 220,
      "cache_read_input_tokens": 66095,
      "output_tokens": 219,
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
          "output_tokens": 219,
          "cache_read_input_tokens": 66095,
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

_source line 50 · 2026-05-20T19:27:11.740Z_

<details open><summary>🔧 Tool call — Bash · `toolu_013PfqXiEA2CPwRHRbCxmwRW`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | grep -B2 \"Extra }\"",
  "description": "Find exact location of LaTeX error",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ee20e37-37a9-4088-b14d-a3c68b8bc698",
  "isSidechain": false,
  "requestId": "req_011CbENVVQoz6MGahVGezmYW",
  "type": "assistant",
  "uuid": "5238d902-76cb-4ac3-a255-e7b9b48a9b70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Ns6rDRvvpZ3zyzo8gnrC7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 220,
      "cache_read_input_tokens": 66095,
      "output_tokens": 219,
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
          "output_tokens": 219,
          "cache_read_input_tokens": 66095,
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

_source line 51 · 2026-05-20T19:27:12.241Z_

<details><summary>↩ Tool result · `toolu_013PfqXiEA2CPwRHRbCxmwRW`</summary>

```text
(hyperref)                removing `math shift' on input line 109.

! Extra }, or forgotten $.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5238d902-76cb-4ac3-a255-e7b9b48a9b70",
  "isSidechain": false,
  "promptId": "eb66b833-472c-4a64-b5b3-e6647c252907",
  "type": "user",
  "uuid": "a9f5025d-f29e-41a2-9b72-18783de2b6b2",
  "toolUseResult": {
    "stdout": "(hyperref)                removing `math shift' on input line 109.\n\n! Extra }, or forgotten $.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "5238d902-76cb-4ac3-a255-e7b9b48a9b70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 52 · 2026-05-20T19:27:12.243Z_

```json
{
  "parentUuid": "a9f5025d-f29e-41a2-9b72-18783de2b6b2",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "aa535728-171f-47a5-b66c-19126715864e",
  "timestamp": "2026-05-20T19:27:12.243Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 53 · 2026-05-20T19:27:15.531Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Wbo2Q1gtyr3JCd1uqKMey7`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | grep -A2 \"Extra }\"",
  "description": "Find line number of LaTeX error",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa535728-171f-47a5-b66c-19126715864e",
  "isSidechain": false,
  "requestId": "req_011CbENVozkuFfB28bb85yLz",
  "type": "assistant",
  "uuid": "9599f87b-0eba-4228-9d74-be4acae42a2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qHwAwFeTUQ2552qfKQ9B4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 305,
      "cache_read_input_tokens": 66315,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 305,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 66315,
          "cache_creation_input_tokens": 305,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 305
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

_source line 54_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T190245 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_c…",
  "leafUuid": "9599f87b-0eba-4228-9d74-be4acae42a2c",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d"
}
```

---

### Runtime record

_source line 55_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate IRT contamination detection paper",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d"
}
```

---

### Tool result

_source line 56 · 2026-05-20T19:27:16.028Z_

<details><summary>↩ Tool result · `toolu_01Wbo2Q1gtyr3JCd1uqKMey7`</summary>

```text
! Extra }, or forgotten $.
l.111 ...rrect responses $\to$ higher $\hat\theta}
                                                  $), absorbing part of the ...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9599f87b-0eba-4228-9d74-be4acae42a2c",
  "isSidechain": false,
  "promptId": "eb66b833-472c-4a64-b5b3-e6647c252907",
  "type": "user",
  "uuid": "bb59ba4d-6fa6-4c54-adcc-99250338112d",
  "toolUseResult": {
    "stdout": "! Extra }, or forgotten $.\nl.111 ...rrect responses $\\to$ higher $\\hat\\theta}\n                                                  $), absorbing part of the ...",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "9599f87b-0eba-4228-9d74-be4acae42a2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-20T19:27:20.124Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Seijyp6HnMoLjWv3pfo3ji`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best/paper.tex",
  "offset": 109,
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb59ba4d-6fa6-4c54-adcc-99250338112d",
  "isSidechain": false,
  "requestId": "req_011CbENW6A6cCDuHPeqYCyKi",
  "type": "assistant",
  "uuid": "39d4bae1-e2d9-48bd-8fa3-e0369a738928",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012iumTzrsKqq68fFFKvYwSj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 173,
      "cache_read_input_tokens": 66620,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 173,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 139,
          "cache_read_input_tokens": 66620,
          "cache_creation_input_tokens": 173,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 173
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

_source line 58 · 2026-05-20T19:27:20.130Z_

<details><summary>↩ Tool result · `toolu_01Seijyp6HnMoLjWv3pfo3ji`</summary>

```text
109	\subsection{$\theta$-Fixed Analysis}
110	
111	A key methodological finding is the \emph{$\theta$-shift boundary condition}: when $\theta$ is re-estimated on contaminated data, the MLE shifts upward (contamination $\to$ more correct responses $\to$ higher $\hat\theta}$), absorbing part of the aberrance signal.
112	This is a mathematical property of the MLE: it attributes any increase in correct responses to higher ability rather than memorization.
113	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "39d4bae1-e2d9-48bd-8fa3-e0369a738928",
  "isSidechain": false,
  "promptId": "eb66b833-472c-4a64-b5b3-e6647c252907",
  "type": "user",
  "uuid": "58872e01-35fb-426c-ae46-d13c8c1eed71",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best/paper.tex",
      "content": "\\subsection{$\\theta$-Fixed Analysis}\n\nA key methodological finding is the \\emph{$\\theta$-shift boundary condition}: when $\\theta$ is re-estimated on contaminated data, the MLE shifts upward (contamination $\\to$ more correct responses $\\to$ higher $\\hat\\theta}$), absorbing part of the aberrance signal.\nThis is a mathematical property of the MLE: it attributes any increase in correct responses to higher ability rather than memorization.\n",
      "numLines": 5,
      "startLine": 109,
      "totalLines": 579
    }
  },
  "sourceToolAssistantUUID": "39d4bae1-e2d9-48bd-8fa3-e0369a738928",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 59 · 2026-05-20T19:27:23.470Z_

Extra `}` after `\hat\theta`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58872e01-35fb-426c-ae46-d13c8c1eed71",
  "isSidechain": false,
  "requestId": "req_011CbENWQ672ZNQaSVF6Y1Hd",
  "type": "assistant",
  "uuid": "7674ffa0-826f-4144-8c19-f96f9452cbfd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wn3zNKyKBLQmQzFUTpAjcL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 274,
      "cache_read_input_tokens": 66793,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 274,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 66793,
          "cache_creation_input_tokens": 274,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 274
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

_source line 60 · 2026-05-20T19:27:24.638Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01WchQyrrR5Ptxb9aRZ3Jsds`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best/paper.tex",
  "old_string": "higher $\\hat\\theta}$)",
  "new_string": "higher $\\hat\\theta$)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7674ffa0-826f-4144-8c19-f96f9452cbfd",
  "isSidechain": false,
  "requestId": "req_011CbENWQ672ZNQaSVF6Y1Hd",
  "type": "assistant",
  "uuid": "aea94b3e-e332-4c76-8102-57c9b796b0b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wn3zNKyKBLQmQzFUTpAjcL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 274,
      "cache_read_input_tokens": 66793,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 274,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 66793,
          "cache_creation_input_tokens": 274,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 274
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

_source line 61 · 2026-05-20T19:27:24.649Z_

<details><summary>↩ Tool result · `toolu_01WchQyrrR5Ptxb9aRZ3Jsds`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aea94b3e-e332-4c76-8102-57c9b796b0b9",
  "isSidechain": false,
  "promptId": "eb66b833-472c-4a64-b5b3-e6647c252907",
  "type": "user",
  "uuid": "8e1a11e9-cc38-4a00-b0e2-9c29ae6f2856",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best/paper.tex",
    "oldString": "higher $\\hat\\theta}$)",
    "newString": "higher $\\hat\\theta$)",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 108,
        "oldLines": 7,
        "newStart": 108,
        "newLines": 7,
        "lines": [
          " ",
          " \\subsection{$\\theta$-Fixed Analysis}",
          " ",
          "-A key methodological finding is the \\emph{$\\theta$-shift boundary condition}: when $\\theta$ is re-estimated on contaminated data, the MLE shifts upward (contamination $\\to$ more correct responses $\\to$ higher $\\hat\\theta}$), absorbing part of the aberrance signal.",
          "+A key methodological finding is the \\emph{$\\theta$-shift boundary condition}: when $\\theta$ is re-estimated on contaminated data, the MLE shifts upward (contamination $\\to$ more correct responses $\\to$ higher $\\hat\\theta$), absorbing part of the aberrance signal.",
          " This is a mathematical property of the MLE: it attributes any increase in correct responses to higher ability rather than memorization.",
          " ",
          " We address this through \\thetafix{} analysis: fixing $\\theta$ to the pre-contamination (clean) baseline value before computing \\lzstar{}."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "aea94b3e-e332-4c76-8102-57c9b796b0b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-20T19:27:27.848Z_

<details open><summary>🔧 Tool call — Bash · `toolu_016eQQ6MRMb5FQP5YtJmJoGq`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | grep -E \"^!|Output written\"",
  "description": "Recompile and check for errors",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e1a11e9-cc38-4a00-b0e2-9c29ae6f2856",
  "isSidechain": false,
  "requestId": "req_011CbENWjKzsVgc25KfcRH8J",
  "type": "assistant",
  "uuid": "34da52e6-b41a-4f52-a5c4-427a77a5f519",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0153dmHWryMSpFiBEj5WY7BE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 258,
      "cache_read_input_tokens": 67067,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 258,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 174,
          "cache_read_input_tokens": 67067,
          "cache_creation_input_tokens": 258,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 258
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

_source line 63 · 2026-05-20T19:27:28.344Z_

<details><summary>↩ Tool result · `toolu_016eQQ6MRMb5FQP5YtJmJoGq`</summary>

```text
Output written on paper.pdf (9 pages, 222835 bytes).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34da52e6-b41a-4f52-a5c4-427a77a5f519",
  "isSidechain": false,
  "promptId": "eb66b833-472c-4a64-b5b3-e6647c252907",
  "type": "user",
  "uuid": "390d1120-6990-4788-9150-56125ed95bb3",
  "toolUseResult": {
    "stdout": "Output written on paper.pdf (9 pages, 222835 bytes).",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "34da52e6-b41a-4f52-a5c4-427a77a5f519",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 64 · 2026-05-20T19:27:31.574Z_

No errors. Run second pass for references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "390d1120-6990-4788-9150-56125ed95bb3",
  "isSidechain": false,
  "requestId": "req_011CbENWzpuHDjf54LxPy7bq",
  "type": "assistant",
  "uuid": "2647a750-49de-48c4-9cb9-4155975083df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D3QCagkxBeGmazJC2EZ3XA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 152,
      "cache_read_input_tokens": 67325,
      "output_tokens": 188,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 152,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 188,
          "cache_read_input_tokens": 67325,
          "cache_creation_input_tokens": 152,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 152
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

_source line 65 · 2026-05-20T19:27:32.547Z_

<details open><summary>🔧 Tool call — Bash · `toolu_015EoDN2PMwxUt5yJStFx3G6`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | grep -E \"^!|Output written|Warning.*undefined\"",
  "description": "Second LaTeX pass for cross-references",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2647a750-49de-48c4-9cb9-4155975083df",
  "isSidechain": false,
  "requestId": "req_011CbENWzpuHDjf54LxPy7bq",
  "type": "assistant",
  "uuid": "64622956-b9a6-4572-b50a-1840ab7b639a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D3QCagkxBeGmazJC2EZ3XA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 152,
      "cache_read_input_tokens": 67325,
      "output_tokens": 188,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 152,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 188,
          "cache_read_input_tokens": 67325,
          "cache_creation_input_tokens": 152,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 152
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

_source line 66 · 2026-05-20T19:27:33.056Z_

<details><summary>↩ Tool result · `toolu_015EoDN2PMwxUt5yJStFx3G6`</summary>

```text
Output written on paper.pdf (9 pages, 222835 bytes).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "64622956-b9a6-4572-b50a-1840ab7b639a",
  "isSidechain": false,
  "promptId": "eb66b833-472c-4a64-b5b3-e6647c252907",
  "type": "user",
  "uuid": "218da389-13e6-41b1-9e23-97ebe1ab1deb",
  "toolUseResult": {
    "stdout": "Output written on paper.pdf (9 pages, 222835 bytes).",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "64622956-b9a6-4572-b50a-1840ab7b639a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 67 · 2026-05-20T19:27:44.225Z_

Clean compilation. Paper written to `paper.pdf` (9 pages). 

The paper covers all 11 experiments from `experiment_data.json`:
- **Controlled contamination pilot** (Table 1) — Qwen3.5-9B × 4 conditions
- **Cross-model validation** (Tables 2–4) — 4 models × 3 benchmarks × 6 levels
- **Baseline comparison** (Tables 5–6) — 7 baselines, AUROC at 4 contamination levels
- **Post-RL signal retention** (Tables 7–8) — lz* retains 80%, token methods collapse
- **Power function validation** (Table 9) — 5 benchmarks, R²=0.968
- **4PL vs 3PL ablation** (Table 10) — +28pp mean power gain
- **Multiscale lzm** (Table 11) — cross-benchmark aggregation
- **Domain-level analysis** (Table 12) — MMLU by subject domain
- **Natural experiment** (Table 13) — 9 base→chat pairs
- **IRT refit at scale** (Table 14) — N=178, a_r=0.13 confirms failure
- **Leaderboard audit** — discussed in limitations as abandoned

All numbers come directly from `experiment_data.json`. The abandoned leaderboard audit is addressed in Discussion/Limitations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "218da389-13e6-41b1-9e23-97ebe1ab1deb",
  "isSidechain": false,
  "requestId": "req_011CbENXM16pfJ8nv21kaYPE",
  "type": "assistant",
  "uuid": "825c7b3e-e3f0-4dac-bbaa-afb5496a534e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T190245/best",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TjxPHzrmKZqskoPnJwsXEr",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 166,
      "cache_read_input_tokens": 67477,
      "output_tokens": 341,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 166,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 341,
          "cache_read_input_tokens": 67477,
          "cache_creation_input_tokens": 166,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 166
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

_source line 68_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T190245 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_c…",
  "leafUuid": "825c7b3e-e3f0-4dac-bbaa-afb5496a534e",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d"
}
```

---

### Runtime record

_source line 69_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate IRT contamination detection paper",
  "sessionId": "f4e042fb-0a90-4bbe-8eb1-3013bf130d8d"
}
```

---
