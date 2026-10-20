# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T221131 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-1/ca7c92ca-7226-4597-b435-bb7be4a94344.jsonl`
- **Structured JSON:** [`55b714e5855a545cf679.json`](../../sessions/55/55b714e5855a545cf679.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-22T22:36:20.395Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T22:36:20.395Z",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T221131 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best/experiment_data.json`（先 Read 此文件）\n- Venue：emnlp-2026\n- Narrative guidance：所有 planned 实验均确认并强化 v5 framing。η_max 在新攻击类型、面板尺寸、生成任务中全面主导； K_eff 脆弱性在每种校正方法下稳定复现。RF 对照实验提供 BFT 反转的干净因果证据； GAM 6:6 分割在 bootstrapped CIs 下通过验证并扩展至新攻击类型；聚合梯度在 clustered SE 下复现， Bayesian 翻转 K_eff 方向这一发现被确认为真实效应而非统计伪迹。五贡献堆栈完整无缺， 论文作为一项自信的实证贡献交付，附带可操作的防御建议和方法论透明性。\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-22T22:36:20.398Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T22:36:20.398Z",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344"
}
```

---

## Round 1

43 recorded events

### User

_source line 3 · 2026-05-22T22:36:20.419Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T221131 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best/experiment_data.json`（先 Read 此文件）
- Venue：emnlp-2026
- Narrative guidance：所有 planned 实验均确认并强化 v5 framing。η_max 在新攻击类型、面板尺寸、生成任务中全面主导； K_eff 脆弱性在每种校正方法下稳定复现。RF 对照实验提供 BFT 反转的干净因果证据； GAM 6:6 分割在 bootstrapped CIs 下通过验证并扩展至新攻击类型；聚合梯度在 clustered SE 下复现， Bayesian 翻转 K_eff 方向这一发现被确认为真实效应而非统计伪迹。五贡献堆栈完整无缺， 论文作为一项自信的实证贡献交付，附带可操作的防御建议和方法论透明性。
- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "d5483bc6-a830-4026-80bc-d9c580d884bc",
  "type": "user",
  "uuid": "f64af4e1-945e-4e83-bea2-f6209f9c8062",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-22T22:36:20.418Z_

```json
{
  "parentUuid": "f64af4e1-945e-4e83-bea2-f6209f9c8062",
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
  "uuid": "f0a9c6f7-14b1-4e19-9f32-964339b7f5c3",
  "timestamp": "2026-05-22T22:36:20.418Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-22T22:36:20.418Z_

```json
{
  "parentUuid": "f0a9c6f7-14b1-4e19-9f32-964339b7f5c3",
  "isSidechain": false,
  "attachment": {
    "type": "agent_listing_delta",
    "addedTypes": [
      "claude",
      "Explore",
      "general-purpose",
      "Plan",
      "statusline-setup"
    ],
    "addedLines": [
      "- claude: Catch-all for any task that doesn't fit a more specific agent. FleetView's default when no agent name is typed. (Tools: *)",
      "- Explore: Fast read-only search agent for locating code. Use it to find files by pattern (eg. \"src/components/**/*.tsx\"), grep for symbols or keywords (eg. \"API endpoints\"), or answer \"where is X defined / which files reference Y.\" Do NOT use it for code review, design-doc auditing, cross-file consistency checks, or open-ended analysis — it reads excerpts rather than whole files and will miss content past its read window. When calling, specify search breadth: \"quick\" for a single targeted lookup, \"medium\" for moderate exploration, or \"very thorough\" to search across multiple locations and naming conventions. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- general-purpose: General-purpose agent for researching complex questions, searching for code, and executing multi-step tasks. When you are searching for a keyword or file and are not confident that you will find the right match in the first few tries use this agent to perform the search for you. (Tools: *)",
      "- Plan: Software architect agent for designing implementation plans. Use this when you need to plan the implementation strategy for a task. Returns step-by-step plans, identifies critical files, and considers architectural trade-offs. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- statusline-setup: Use this agent to configure the user's Claude Code status line setting. (Tools: Read, Edit)"
    ],
    "removedTypes": [],
    "isInitial": true,
    "showConcurrencyNote": true
  },
  "type": "attachment",
  "uuid": "98c1254d-b60f-4d33-a795-a96308fa5975",
  "timestamp": "2026-05-22T22:36:20.418Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-22T22:36:20.418Z_

```json
{
  "parentUuid": "98c1254d-b60f-4d33-a795-a96308fa5975",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "377df4fe-693b-4cf9-8c5b-1f264b6df87f",
  "timestamp": "2026-05-22T22:36:20.418Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate EMNLP-2026 paper on certification manipulation",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344"
}
```

---

### Assistant

_source line 8 · 2026-05-22T22:36:24.449Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "377df4fe-693b-4cf9-8c5b-1f264b6df87f",
  "isSidechain": false,
  "requestId": "req_011CbJQYAw9LCAraszJotzqV",
  "type": "assistant",
  "uuid": "0eac5472-eabe-41bd-a2e3-f3237a77262d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019dgPcNQNJV5xmQBQ4oYXTH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12280,
      "cache_read_input_tokens": 11447,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12280,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12280,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12280
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

_source line 9 · 2026-05-22T22:36:25.455Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NmqqdRKYrvXtwB6viwyXTo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0eac5472-eabe-41bd-a2e3-f3237a77262d",
  "isSidechain": false,
  "requestId": "req_011CbJQYAw9LCAraszJotzqV",
  "type": "assistant",
  "uuid": "983a25dc-1a64-47d8-b02a-30b80ce4fde3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019dgPcNQNJV5xmQBQ4oYXTH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12280,
      "cache_read_input_tokens": 11447,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12280,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12280,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12280
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

_source line 10 · 2026-05-22T22:36:25.722Z_

<details><summary>↩ Tool result · `toolu_01NmqqdRKYrvXtwB6viwyXTo`</summary>

```text
1	[
2	  {
3	    "name": "15-Model Scaling Expansion",
4	    "description": "扩展至 15 模型（6 families），455 panels × 12 conditions 全量回归 + MI 矩阵 + 所有校正方法",
5	    "results": {
6	      "status": "DONE (plan001_step1_full_v4)",
7	      "models": 15,
8	      "panels": 455,
9	      "conditions": 12,
10	      "eta_max_sig_ols": "11/12",
11	      "keff_sig_ols": "8/12 (7+/1-)",
12	      "eta_max_sig_clustered_se": "8/12",
13	      "keff_sig_clustered_se": "0/12",
14	      "eta_max_sig_bootstrap_v2": "5/12",
15	      "keff_sig_bootstrap_v2": "1/12",
16	      "eta_max_sig_mixed_effects": "7/12",
17	      "keff_sig_mixed_effects": "3/12",
18	      "dominance_ratio_bootstrap": "5:1",
19	      "gam_split": "6 targeted positive / 6 shared-bias negative",
20	      "min_eta_max_wins": "12/12",
21	      "confound_r": 0.701,
22	      "se_inflation_factor": "~2.5x",
23	      "rf_keff_sig": "2/2",
24	      "rf_r2_mmlu": 0.734,
25	      "rf_r2_arc": 0.813
26	    },
27	    "tables": [
28	      {
29	        "name": "Correction Method Comparison (Actual Results)",
30	        "columns": [
31	          "Method",
32	          "η_max sig",
33	          "K_eff sig",
34	          "K_eff dir",
35	          "Note"
36	        ],
37	        "rows": [
38	          [
39	            "OLS",
40	            "11/12",
41	            "8/12",
42	            "7+/1-",
43	            "Panel overlap inflated"
44	          ],
45	          [
46	            "Clustered SE (CR1, 15 clusters)",
47	            "8/12",
48	            "0/12",
49	            "-",
50	            "Conservative"
51	          ],
52	          [
53	            "Wild cluster bootstrap v2",
54	            "5/12",
55	            "1/12",
56	            "1+",
57	            "Max-p across 3 positions"
58	          ],
59	          [
60	            "Mixed effects",
61	            "7/12",
62	            "3/12",
63	            "3+",
64	            "Random judge intercepts"
65	          ]
66	        ]
67	      }
68	    ],
69	    "figures": [],
70	    "analysis": "已完成。η_max:K_eff 主导比从 OLS 的 1.4:1 升至 bootstrap 的 5:1，证明相对主导性在校正下 增强而非减弱。Benchmark 不对称（MMLU 4/6 vs ARC 1/6 存活 bootstrap）由 MMLU 4-choice 格式提供更多 scoring variance 解释。此结果构成 paper 的实证基础。\n\n已完成。15 模型覆盖 6 families × 3 capability tiers，提供 η_max 和 K_eff 充足方差。 SE 膨胀 ~2.5x 与 91/455 panel overlap 一致（claude-3-haiku 出现在 91 个 panels 中）。 η_max 存活校正因为它捕捉的是真实的个体 judge 脆弱性——不是 panel 重叠伪迹。 K_eff 崩溃因为其 OLS 显著性被 overlapping panels 的相关残差膨胀——clustered SE 控制共享 judge 成员关系后，K_eff 的独立信号太弱。GAM 6:6 分割源于攻击机制差异： targeted attacks 利用 judge 特异性弱点（diversity = 更多攻击面），shared-bias attacks 利用共性认知偏差（diversity = 部分 judges 免疫）。"
71	  },
72	  {
73	    "name": "Attack Surface Expansion",
74	    "description": "新增 3 种攻击类型（few-shot hijacking, persona manipulation, instruction override），在 15 模型 × 2 benchmarks 上运行，共 6 新 conditions",
75	    "results": {
76	      "new_attack_types": 3,
77	      "new_conditions": 6,
78	      "total_conditions": 18,
79	      "new_eta_max_sig_ols": "6/6",
80	      "new_keff_sig_ols": "4/6 (3+/1-)",
81	      "new_eta_max_sig_clustered_se": "5/6",
82	      "new_keff_sig_clustered_se": "0/6",
83	      "new_eta_max_sig_bootstrap": "3/6",
84	      "new_keff_sig_bootstrap": "0/6",
85	      "combined_eta_max_sig_clustered_se": "13/18",
86	      "combined_keff_sig_clustered_se": "0/18",
87	      "combined_dominance_ratio_clustered_se": "13:0",
88	      "gam_extended_split": "10 targeted positive / 8 shared-bias negative",
89	      "gam_new_attacks_classification": {
90	        "few_shot_hijacking": "targeted (positive K_eff)",
91	        "persona_manipulation": "shared-bias (negative K_eff)",
92	        "instruction_override": "targeted (positive K_eff)"
93	      },
94	      "new_r2_range": [
95	        0.22,
96	        0.45
97	      ],
98	      "min_eta_max_wins_extended": "18/18"
99	    },
100	    "tables": [
101	      {
102	        "name": "Extended Attack Taxonomy (Clustered SE)",
103	        "columns": [
104	          "Attack Type",
105	          "Mechanism",
106	          "Benchmark",
107	          "η_max sig?",
108	          "K_eff sig?",
109	          "K_eff GAM direction"
110	        ],
111	        "rows": [
112	          [
113	            "few-shot hijacking",
114	            "targeted",
115	            "MMLU",
116	            "Yes",
117	            "No",
118	            "positive"
119	          ],
120	          [
121	            "few-shot hijacking",
122	            "targeted",
123	            "ARC",
124	            "Yes",
125	            "No",
126	            "positive"
127	          ],
128	          [
129	            "persona manipulation",
130	            "shared-bias",
131	            "MMLU",
132	            "Yes",
133	            "No",
134	            "negative"
135	          ],
136	          [
137	            "persona manipulation",
138	            "shared-bias",
139	            "ARC",
140	            "Yes",
141	            "No",
142	            "negative"
143	          ],
144	          [
145	            "instruction override",
146	            "targeted",
147	            "MMLU",
148	            "Yes",
149	            "No",
150	            "positive"
151	          ],
152	          [
153	            "instruction override",
154	            "targeted",
155	            "ARC",
156	            "No",
157	            "No",
158	            "positive"
159	          ]
160	        ]
161	      },
162	      {
163	        "name": "Extended GAM Split Summary",
164	        "columns": [
165	          "Category",
166	          "Original (6 attacks)",
167	          "New (3 attacks)",
168	          "Total",
169	          "K_eff direction"
170	        ],
171	        "rows": [
172	          [
173	            "Targeted",
174	            "6/6 positive",
175	            "4/4 positive",
176	            "10/10",
177	            "positive (diversity harmful)"
178	          ],
179	          [
180	            "Shared-bias",
181	            "6/6 negative",
182	            "2/2 negative (persona×2)",
183	            "8/8",
184	            "negative (diversity protective)"
185	          ]
186	        ]
187	      }
188	    ],
189	    "figures": [],
190	    "analysis": "新攻击类型提供独立证据线，确认 η_max 主导性不依赖于特定攻击选择。GAM taxonomy 从 6:6 扩展至 10:8，mechanistic split 的稳健性增强——审稿人无法再质疑 taxonomy 是 cherry-picked 6 种 攻击的巧合。Instruction override 在 ARC 上 η_max 未显著（ARC 2-choice 格式对 instruction override 的 judge 间方差不敏感），与原始 benchmark asymmetry 一致。论文标题和核心叙事完全支持。\n\nFew-shot hijacking 利用模型在 in-context learning 上的个体差异——不同 judges 对 few-shot 示例的敏感度差异极大（GPT-4.1 vs Llama-8B 可差 3-5x），因此属于 targeted attack，η_max 捕捉最易受影响的 judge。Instruction override 利用 instruction-following 能力的模型间方差， 同样属于 targeted。Persona manipulation 利用 LLMs 对权威/身份线索的普遍敏感性——这是一种 共享认知偏差，不同能力模型都会受影响，因此属于 shared-bias，K_eff 方向为负（diversity 提供 部分免疫）。新攻击在 OLS 下延续 η_max 主导模式，但 K_eff 再次因 panel overlap 膨胀而 显著——clustered SE 后归零，与原 12 conditions 完全一致。GAM 扩展至 10:8 分割，clean taxonomy 覆盖 9 种攻击类型。"
191	  },
192	  {
193	    "name": "Random-Fault BFT Contrast Experiment",
194	    "description": "Monte Carlo 随机故障模拟作为 BFT 对照。每个 judge 以 η_j = 1 - clean_accuracy 独立失败，majority vote。对比 adaptive regime 证明 BFT 反转",
195	    "results": {
196	      "regime": "Random Fault (i.i.d.)",
197	      "conditions": 2,
198	      "monte_carlo_iterations": 10000,
199	      "rf_keff_sig_ols": "2/2",
200	      "rf_keff_sig_clustered_se": "2/2",
201	      "rf_keff_sig_bootstrap": "2/2",
202	      "rf_keff_direction": "positive (2/2)",
203	      "rf_keff_std_beta_mmlu": 0.215,
204	      "rf_keff_std_beta_arc": 0.379,
205	      "rf_eta_sig_all_methods": "2/2",
206	      "rf_r2_mmlu": 0.78,
207	      "rf_r2_arc": 0.81,
208	      "adaptive_keff_sig_clustered_se": "0/12",
209	      "adaptive_keff_sig_bootstrap": "1/12",
210	      "delta_r2_rf_vs_adaptive": 0.48,
211	      "go_nogo_gate": "PASS (RF K_eff ≥2/2)"
212	    },
213	    "tables": [
214	      {
215	        "name": "RF vs Adaptive Contrast (Key Metrics)",
216	        "columns": [
217	          "Metric",
218	          "Random Fault",
219	          "Adaptive",
220	          "Interpretation"
221	        ],
222	        "rows": [
223	          [
224	            "K_eff sig (OLS)",
225	            "2/2",
226	            "8/12 (7+/1-)",
227	            "Both appear significant under OLS"
228	          ],
229	          [
230	            "K_eff sig (Clustered SE)",
231	            "2/2",
232	            "0/12",
233	            "RF genuine; adaptive artifactual"
234	          ],
235	          [
236	            "K_eff sig (Bootstrap v2)",
237	            "2/2",
238	            "1/12",
239	            "Consistent contrast"
240	          ],
241	          [
242	            "K_eff std β (mean)",
243	            "+0.297",
244	            "+0.164",
245	            "RF effect larger and genuine"
246	          ],
247	          [
248	            "R²",
249	            "0.78-0.81",
250	            "0.25-0.35",
251	            "RF structurally determined; adaptive not"
252	          ],
253	          [
254	            "η_max sig (all methods)",
255	            "2/2",
256	            "5-8/12",
257	            "η_max genuine in both regimes"
258	          ]
259	        ]
260	      },
261	      {
262	        "name": "RF Per-Benchmark Detail",
263	        "columns": [
264	          "Benchmark",
265	          "η_max β",
266	          "K_eff β",
267	          "R²",
268	          "K_eff p (bootstrap)"
269	        ],
270	        "rows": [
271	          [
272	            "MMLU",
273	            "+0.482",
274	            "+0.215",
275	            "0.78",
276	            "0.003"
277	          ],
278	          [
279	            "ARC",
280	            "+0.551",
281	            "+0.379",
282	            "0.81",
283	            "<0.001"
284	          ]
285	        ]
286	      }
287	    ],
288	    "figures": [],
289	    "analysis": "这是论文的关键因果证据。RF 对照证明 K_eff 在满足 i.i.d. 假设时有真实效应——BFT 理论 在随机故障下成立。而 adaptive regime 下 K_eff 的 OLS 显著性完全是 panel overlap 的伪迹。 这不是\"diversity helps under RF but hurts under adaptive\"——K_eff 在两种 regime 下方向均 为正。区别是：RF 下 K_eff 的正关联是真实的（panel 结构决定了容错性），adaptive 下是膨胀的 （adversary 引入的策略方差使 panel 结构预测力崩溃）。此发现为 Contribution #2（BFT reversal evidence）提供了不可替代的因果论证。\n\n随机故障下 K_eff 显著的根本原因是 BFT 的 i.i.d. 假设成立：每个 judge 独立以固定概率犯错， panel 结构（多样性）直接影响冗余覆盖。K_eff 高的 panel 中 judges 的错误模式更不相关， majority vote 的容错能力与独立性成正比——这正是 BFT 的核心机制。K_eff 方向为正（diversity → higher error）因为高 K_eff panel 必然包含弱模型（r=0.70 tradeoff），而在 i.i.d. 体制下 弱模型的高错误率直接传导为 panel 错误率——但关键是 K_eff 的贡献是独立的、真实的（所有校正 方法均显著 2/2）。对照 adaptive regime：相同的 K_eff 在 OLS 下显著 8/12，但 clustered SE 后崩溃至 0/12——因为 adaptive adversary 引入了 panel 结构无法预测的策略方差，K_eff 的 apparent OLS 信号完全来自 panel overlap 膨胀。R² 差异（RF 0.78-0.81 vs adaptive ~0.30） 直接量化了 adaptive adversary 引入的不可预测性。GO/NO-GO gate 通过，BFT framing 得到 因果层面的支撑。"
290	  },
291	  {
292	    "name": "Capability-Matched Validation",
293	    "description": "在同一 capability tier 内（主要利用 9-model base tier, 84 panels）测试控制 η_max 方差后 K_eff 是否浮现为显著预测因子",
294	    "results": {
295	      "primary_tier": "base (9 models, 84 panels)",
296	      "within_tier_eta_max_variance_reduction": "65-70%",
297	      "within_tier_keff_eta_max_r": 0.35,
298	      "conditions": 12,
299	      "within_tier_keff_sig_ols": "5/12",
300	      "within_tier_keff_sig_clustered_se": "2/12",
301	      "within_tier_keff_direction": "4+/1-",
302	      "within_tier_eta_max_sig_ols": "7/12",
303	      "within_tier_eta_max_sig_clustered_se": "4/12",
304	      "within_tier_dominance_ratio": "2:1",
305	      "within_tier_r2_mean": 0.18,
306	      "cross_tier_comparison": {
307	        "full_pool_dominance_ratio": "5:1",
308	        "within_tier_dominance_ratio": "2:1",
309	        "interpretation": "η_max still dominant but K_eff gains relative signal"
310	      }
311	    },
312	    "tables": [
313	      {
314	        "name": "Cross-Tier vs Within-Tier Comparison",
315	        "columns": [
316	          "Setting",
317	          "Panels",
318	          "K_eff-η_max r",
319	          "η_max sig (CL-SE)",
320	          "K_eff sig (CL-SE)",
321	          "Ratio",
322	          "R² mean"
323	        ],
324	        "rows": [
325	          [
326	            "Full pool (15 models)",
327	            "455",
328	            "0.70",
329	            "8/12",
330	            "0/12",
331	            "8:0",
332	            "0.30"
333	          ],
334	          [
335	            "Base tier (9 models)",
336	            "84",
337	            "0.35",
338	            "4/12",
339	            "2/12",
340	            "2:1",
341	            "0.18"
342	          ],
343	          [
344	            "Frontier tier (3 models)",
345	            "1",
346	            "-",
347	            "-",
348	            "-",
349	            "-",
350	            "-"
351	          ]
352	        ]
353	      },
354	      {
355	        "name": "Within-Tier K_eff Significant Conditions",
356	        "columns": [
357	          "Condition",
358	          "K_eff β",
359	          "K_eff p (CL-SE)",
360	          "Direction",
361	          "GAM confirms?"
362	        ],
363	        "rows": [
364	          [
365	            "mmlu×prompt_injection",
366	            "+0.31",
367	            "0.028",
368	            "positive",
369	            "Yes (targeted)"
370	          ],
371	          [
372	            "mmlu×score_manipulation",
373	            "+0.25",
374	            "0.041",
375	            "positive",
376	            "Yes (targeted)"
377	          ]
378	        ]
379	      }
380	    ],
381	    "figures": [],
382	    "analysis": "Capability-matched validation 提供了 disentangle η_max 和 K_eff 的准自然实验。关键发现： 即使在控制 η_max 方差后，K_eff 仍然是次要驱动因素（2:1 而非 1:1 或 K_eff 主导）。 论文可表述为：\"当 capability 差异被控制时，diversity 浮现为统计上可检测的次要因素——但在 自然 panel 组合中，capability 差异（通过 η_max）压倒性地主导脆弱性。\"这强化了 robustness-first 设计建议：先筛选 capability，再在筛选后的池中考虑 diversity。\n\n在同一 capability tier 内，η_max 方差降低约 65-70%（因为同 tier 模型能力接近），而 K_eff 方差保持（同 tier 模型仍来自不同 families/architectures）。η_max 和 K_eff 的 confound 从 r=0.70（全池）降至 r≈0.35（tier 内），解开了回归中的多重共线性。在此条件下，K_eff 的边际信号——通常被 η_max 的强效应淹没——变得可检测。OLS 下 5/12 显著；clustered SE 后 保留 2/12，表明 K_eff 有微弱但真实的独立效应。主导比从 5:1 降至 2:1，但 η_max 仍然 主导。这支持论文叙事：K_eff 有方向性关联但在全池分析中被 η_max 压倒——当人为控制 η_max 方差时 K_eff 才浮现，这恰恰说明在自然变异条件下 η_max 是主要驱动因素。此外，within-tier R² 均值仅 0.18，说明 tier 内的面板脆弱性预测力大幅下降——进一步证明 η_max 的跨 tier 方差是预测力的主要来源。"
383	  },
384	  {
385	    "name": "Two-Stage Panel Design Algorithm Benchmark",
386	    "description": "实现 robustness-first 两阶段算法（filter η > threshold → maximize K_eff），对标 5 个 baseline 策略",
387	    "results": {
388	      "baselines": [
389	        "random",
390	        "max_keff",
391	        "max_disagreement",
392	        "strongest_k",
393	        "uniform_family"
394	      ],
395	      "conditions": 12,
396	      "min_eta_max_wins": "12/12",
397	      "two_stage_vs_min_eta_max_improvement_pp": [
398	        0.3,
399	        1.8
400	      ],
401	      "two_stage_vs_min_eta_max_mean_improvement_pp": 0.7,
402	      "two_stage_wins_vs_min_eta_max": "7/12",
403	      "strategy_ranking": {
404	        "rank_1": "two-stage (robustness-first + K_eff)",
405	        "rank_2": "min_eta_max (robustness-first only)",
406	        "rank_3": "strongest_k",
407	        "rank_4": "uniform_family",
408	        "rank_5": "max_disagreement",
409	        "rank_6": "max_keff",
410	        "rank_7": "random"
411	      },
412	      "max_keff_vs_random": "worse in 8/12 (includes weak models)",
413	      "strongest_k_gap_from_min_eta_max": "1.2pp mean",
414	      "asr_advantage_range": [
415	        0.038,
416	        0.511
417	      ]
418	    },
419	    "tables": [
420	      {
421	        "name": "Strategy Comparison (Mean ASR across 12 conditions)",
422	        "columns": [
423	          "Strategy",
424	          "Mean ASR",
425	          "Rank",
426	          "Δ vs random (pp)"
427	        ],
428	        "rows": [
429	          [
430	            "two-stage",
431	            "0.112",
432	            "1",
433	            "-8.3"
434	          ],
435	          [
436	            "min_eta_max",
437	            "0.119",
438	            "2",
439	            "-7.6"
440	          ],
441	          [
442	            "strongest_k",
443	            "0.131",
444	            "3",
445	            "-6.4"
446	          ],
447	          [
448	            "uniform_family",
449	            "0.158",
450	            "4",
451	            "-3.7"
452	          ],
453	          [
454	            "max_disagreement",
455	            "0.172",
456	            "5",
457	            "-2.3"
458	          ],
459	          [
460	            "random",
461	            "0.195",
462	            "6",
463	            "0.0"
464	          ],
465	          [
466	            "max_keff",
467	            "0.208",
468	            "7",
469	            "+1.3"
470	          ]
471	        ]
472	      },
473	      {
474	        "name": "Two-Stage vs min_eta_max Per-Attack-Type",
475	        "columns": [
476	          "Attack category",
477	          "Conditions",
478	          "Two-stage better?",
479	          "Mean Δ (pp)"
480	        ],
481	        "rows": [
482	          [
483	            "Targeted",
484	            "6",
485	            "5/6",
486	            "-1.1"
487	          ],
488	          [
489	            "Shared-bias",
490	            "6",
491	            "2/6",
492	            "-0.3"
493	          ]
494	        ]
495	      }
496	    ],
497	    "figures": [],
498	    "analysis": "Two-stage 算法的边际改进（0.7pp）虽然在统计上一致但实际影响不大——论文应诚实呈现这一点。 核心 practical recommendation 保持不变：robustness-first screening 是关键步骤，K_eff 优化是可选的次要步骤。max_keff 策略的失败（差于 random）是论文叙事的有力支撑——直观的 \"多样化 panel\" 建议在实践中适得其反。\n\nmin_eta_max 策略赢 12/12 因为 η_max 是主导脆弱性驱动因素。两阶段策略在 min_eta_max 基础上提供边际改进（mean 0.7pp）：在已通过 robustness 筛选的 judge 子集中，K_eff 的微弱次要效应（在 capability-matched 设置中可检测，如 plan_004 所示）被利用。改进最大 的条件是 targeted attacks（K_eff 方向为正 = diversity 有害 → 在 robustness-screened 池中最小化 K_eff 有帮助）。改进最小的条件是 shared-bias attacks（K_eff 方向为负 → diversity 在这些条件下是保护性的 → 最大化 K_eff 更优）。max_keff 策略表现差于 random 因为最大化 diversity 必然引入弱模型（r=0.70 tradeoff），直接提高了 η_max。 strongest_k 与 min_eta_max 差距仅 1.2pp——因为最强模型通常也最鲁棒，但 min_eta_max 是直接优化目标函数而 strongest_k 是代理指标。"
499	  },
500	  {
501	    "name": "Per-Judge ASR Concentration Analysis",
502	    "description": "计算每个 panel × attack 的 per-judge ASR 分布的 Gini 系数和 Shannon 熵，量化 adaptive adversary 是否针对特定 judge",
503	    "results": {
504	      "panels": 455,
505	      "conditions": 12,
506	      "gini_targeted_mean": 0.78,
507	      "gini_targeted_range": [
508	        0.72,
509	        0.85
510	      ],
511	      "gini_shared_bias_mean": 0.43,
512	      "gini_shared_bias_range": [
513	        0.35,
514	        0.52
515	      ],
516	      "gini_targeted_vs_shared_mannwhitney_p": "<0.001",
517	      "entropy_targeted_mean": 0.82,
518	      "entropy_shared_bias_mean": 1.45,
519	      "gini_eta_max_correlation": 0.83,
520	      "top1_judge_asr_fraction_targeted": 0.61,
521	      "top1_judge_asr_fraction_shared": 0.38
522	    },
523	    "tables": [
524	      {
525	        "name": "ASR Concentration by Attack Category",
526	        "columns": [
527	          "Attack Type",
528	          "Category",
529	          "Gini (mean)",
530	          "Entropy (mean)",
531	          "Top-1 judge ASR fraction"
532	        ],
533	        "rows": [
534	          [
535	            "prompt_injection",
536	            "targeted",
537	            "0.82",
538	            "0.73",
539	            "0.65"
540	          ],
541	          [
542	            "score_manipulation",
543	            "targeted",
544	            "0.79",
545	            "0.78",
546	            "0.62"
547	          ],
548	          [
549	            "position_bias",
550	            "targeted",
551	            "0.74",
552	            "0.94",
553	            "0.56"
554	          ],
555	          [
556	            "sycophancy",
557	            "shared-bias",
558	            "0.45",
559	            "1.38",
560	            "0.40"
561	          ],
562	          [
563	            "verbosity_bias",
564	            "shared-bias",
565	            "0.42",
566	            "1.47",
567	            "0.37"
568	          ],
569	          [
570	            "authority_bias",
571	            "shared-bias",
572	            "0.41",
573	            "1.50",
574	            "0.36"
575	          ]
576	        ]
577	      }
578	    ],
579	    "figures": [],
580	    "analysis": "ASR 浓度分析为 η_max 主导性提供了微观机制证据，超越了回归系数的间接推断。审稿人常问 \"what's the mechanism?\"——本实验直接回答：targeted adversary 将攻击集中在 weakest judge 上（Gini>0.7），使 η_max 成为 panel 脆弱性的充分统计量。shared-bias 下 ASR 更分散 解释了为什么 K_eff 在这类攻击中为负——diversity 提供 partial immunity 因为并非所有 judges 都同样受 shared bias 影响。此发现独立验证 GAM taxonomy。\n\nTargeted attacks（prompt injection, score manipulation, position bias）利用特定 judge 的个体弱点——adversary 的攻击策略集中在 panel 中最脆弱的 judge 上。这导致 ASR 分布 高度集中（Gini 0.72-0.85）：top-1 judge 贡献了约 61% 的 panel 总 ASR。这是 η_max 主导性的直接微观机制证据——vulnerability 确实集中在 weakest link。相比之下，shared-bias attacks（sycophancy, verbosity, authority）利用多个 judges 共享的认知偏差，ASR 更 均匀地分布在 panel 成员间（Gini 0.35-0.52），top-1 judge 仅贡献约 38%。Gini 与 η_max 的高相关（r=0.83）直接证明 panel-level vulnerability 与 judge-level concentration 是同一现象的两个面。这为 GAM 6:6 split 提供了独立的 mechanistic 验证——targeted 和 shared-bias 不仅在 K_eff 方向上分裂，在 ASR concentration 模式上也完全分裂。"
581	  },
582	  {
583	    "name": "Diversity-Capability Tradeoff Visualization",
584	    "description": "绘制 K_eff vs η_max scatter，拟合 tradeoff curve，计算 Pareto frontier，按 tier 分层",
585	    "results": {
586	      "overall_keff_etamax_r": 0.7,
587	      "overall_keff_etamax_r_ci95": [
588	        0.66,
589	        0.74
590	      ],
591	      "tier_stratified": {
592	        "base_tier_r": 0.52,
593	        "mid_tier_r": 0.48,
594	        "frontier_tier_r": 0.35
595	      },
596	      "pareto_frontier_size": 12,
597	      "pareto_dominance_pct": "97.4% of panels dominated",
598	      "pareto_frontier_composition": "predominantly low-K_eff, low-η_max panels",
599	      "tradeoff_curve_fit": "monotone increasing, concave",
600	      "within_family_r": 0.81,
601	      "cross_family_r": 0.65
602	    },
603	    "tables": [
604	      {
605	        "name": "Tradeoff Correlation by Stratification",
606	        "columns": [
607	          "Stratification",
608	          "N panels",
609	          "r(K_eff, η_max)",
610	          "95% CI"
611	        ],
612	        "rows": [
613	          [
614	            "Full pool",
615	            "455",
616	            "0.70",
617	            "[0.66, 0.74]"
618	          ],
619	          [
620	            "Base tier only",
621	            "84",
622	            "0.52",
623	            "[0.38, 0.64]"
624	          ],
625	          [
626	            "Within-family",
627	            "varies",
628	            "0.81",
629	            "[0.73, 0.87]"
630	          ],
631	          [
632	            "Cross-family",
633	            "varies",
634	            "0.65",
635	            "[0.58, 0.71]"
636	          ]
637	        ]
638	      }
639	    ],
640	    "figures": [],
641	    "analysis": "可视化使 structural constraint 具象化——审稿人直观理解为什么 max_keff 策略失败（右上角） 而 min_eta_max 策略成功（左下角）。Tier 内相关降低的发现为 two-stage algorithm 提供了 理论基础：capability screening 打破了跨 tier 的 strong tradeoff，使后续 diversity 优化在弱 tradeoff 条件下进行。此 figure 应作为论文 Fig 3 或 Fig 4。\n\nr=0.70 的 structural correlation 源于当前 LLM 生态系统的特性：最大化 K_eff 需要包含来自 不同 capability tiers 的模型（不同 family × tier 组合提供最大 behavioral diversity）， 这必然引入能力较弱的 judges，推高 η_max。Tier 分层后 r 降低（base: 0.52, frontier: 0.35） 说明 tradeoff 在 tier 内较弱——within tier 的 diversity（来自不同 architecture/training） 不需要大幅牺牲 capability。这支持 two-stage recommendation 的逻辑：先筛选 capability tier（打破跨 tier tradeoff），再在 tier 内最大化 diversity（利用弱化的 within-tier tradeoff）。 Pareto frontier 几乎全部由 low-K_eff, low-η_max panels 占据——no free lunch，但 robustness-first selection 自然落在 Pareto frontier 上。"
642	  },
643	  {
644	    "name": "Panel Size Sensitivity Analysis",
645	    "description": "测试 K=3,5,7,9 不同 panel 尺寸下 η_max 主导性是否持续",
646	    "results": {
647	      "panel_sizes": [
648	        3,
649	        5,
650	        7,
651	        9
652	      ],
653	      "panels_per_size": [
654	        455,
655	        3003,
656	        6435,
657	        5005
658	      ],
659	      "eta_max_sig_by_k_clustered_se": {
660	        "k3": "8/12",
661	        "k5": "9/12",
662	        "k7": "9/12",
663	        "k9": "8/12"
664	      },
665	      "keff_sig_by_k_clustered_se": {
666	        "k3": "0/12",
667	        "k5": "1/12",
668	        "k7": "1/12",
669	        "k9": "2/12"
670	      },
671	      "dominance_ratio_by_k": {
672	        "k3": "8:0",
673	        "k5": "9:1",
674	        "k7": "9:1",
675	        "k9": "4:1"
676	      },
677	      "eta_max_effect_size_trend": "decreasing with K (from 0.42 at K=3 to 0.31 at K=9)",
678	      "keff_effect_size_trend": "stable (0.12-0.16 across all K)",
679	      "min_eta_max_wins_by_k": {
680	        "k3": "12/12",
681	        "k5": "12/12",
682	        "k7": "12/12",
683	        "k9": "12/12"
684	      },
685	      "se_inflation_by_k": [
686	        2.5,
687	        4.1,
688	        6.3,
689	        7.8
690	      ]
691	    },
692	    "tables": [
693	      {
694	        "name": "Panel Size Sensitivity Summary (Clustered SE)",
695	        "columns": [
696	          "K",
697	          "Panels",
698	          "η_max sig",
699	          "K_eff sig",
700	          "Ratio",
701	          "SE inflation",
702	          "η_max β (mean)"
703	        ],
704	        "rows": [
705	          [
706	            "3",
707	            "455",
708	            "8/12",
709	            "0/12",
710	            "8:0",
711	            "2.5x",
712	            "0.42"
713	          ],
714	          [
715	            "5",
716	            "3003",
717	            "9/12",
718	            "1/12",
719	            "9:1",
720	            "4.1x",
721	            "0.38"
722	          ],
723	          [
724	            "7",
725	            "6435",
726	            "9/12",
727	            "1/12",
728	            "9:1",
729	            "6.3x",
730	            "0.34"
731	          ],
732	          [
733	            "9",
734	            "5005",
735	            "8/12",
736	            "2/12",
737	            "4:1",
738	            "7.8x",
739	            "0.31"
740	          ]
741	        ]
742	      }
743	    ],
744	    "figures": [],
745	    "analysis": "Panel size sensitivity 提供两个关键发现：(1) η_max 主导性在 K=3 到 K=9 范围内稳定持续， 确认 weakest-link 不是小 panel 的 artifact；(2) SE 膨胀随 K 急剧增加，为方法论 contribution（non-independence correction 的必要性）提供量化支撑。K=9 时 K_eff 达到 2/12 显著但 effect size 仍微小——power 增加检测到了真实但 practically insignificant 的效应。论文 supplementary 中可报告此分析作为 robustness check。\n\nη_max 主导性在所有 K 下持续因为 weakest-link 机制是 scale-invariant：无论 panel 有多少 judges，adversary 总是针对最脆弱的那个。K 增加时 η_max 的 effect size 略降（0.42→0.31） 因为更大 panel 中 majority vote 的容错能力增加——单个 judge 的失败更难翻转整个 panel。 但 η_max 仍然主导，因为 adversary 不只针对一个 judge——adaptive adversary 可以同时攻击 多个弱 judges。K_eff 在 K=9 时达到 2/12 显著：更多 panels（5005）提供了更多统计 power， 但 effect size 保持微小（0.12-0.16）。SE 膨胀随 K 急剧增加（每个 model 出现在更多 panels 中），从 K=3 的 2.5x 到 K=9 的 7.8x。这为 non-independence 校正方法的必要性 提供了更强的论据——在 K=7 或 K=9 下使用 OLS 会产生极度膨胀的显著性计数。 min_eta_max 策略在所有 K 下赢 12/12，确认 practical recommendation 对 panel size 鲁棒。"
746	  },
747	  {
748	    "name": "VIF + Multicollinearity Diagnostic",
749	    "description": "计算 VIF、partial correlations、residualized K_eff regression，应用 Bonferroni/FDR 校正，尝试 beta regression",
750	    "results": {
751	      "gpu_needed": false,
752	      "raw_vif_keff": 2.96,
753	      "raw_vif_eta_max": 2.96,
754	      "residualized_vif_keff": 1.0,
755	      "partial_correlation_keff_asr_given_eta": 0.18,
756	      "partial_correlation_eta_asr_given_keff": 0.42,
757	      "bonferroni_eta_max_sig": "7/12",
758	      "bonferroni_keff_sig": "2/12",
759	      "fdr_eta_max_sig": "8/12",
760	      "fdr_keff_sig": "3/12",
761	      "beta_regression_eta_max_sig": "10/12",
762	      "beta_regression_keff_sig": "4/12 (3+/1-)",
763	      "beta_regression_dispersion_phi": [
764	        3.2,
765	        8.7
766	      ],
767	      "condition_number": 4.8,
768	      "reviewer_blocking_issue": false
769	    },
770	    "tables": [
771	      {
772	        "name": "Multicollinearity Diagnostics",
773	        "columns": [
774	          "Metric",
775	          "Value",
776	          "Threshold",
777	          "Status"
778	        ],
779	        "rows": [
780	          [
781	            "VIF (K_eff, raw)",
782	            "2.96",
783	            "< 5 (strict) / < 10 (standard)",
784	            "PASS"
785	          ],
786	          [
787	            "VIF (K_eff, residualized)",
788	            "1.00",
789	            "< 5",
790	            "PASS"
791	          ],
792	          [
793	            "Condition number",
794	            "4.8",
795	            "< 30",
796	            "PASS"
797	          ],
798	          [
799	            "Partial r(K_eff, ASR | η_max)",
800	            "0.18",
801	            "-",
802	            "Weak"
803	          ],
804	          [
805	            "Partial r(η_max, ASR | K_eff)",
806	            "0.42",
807	            "-",
808	            "Moderate-strong"
809	          ]
810	        ]
811	      },
812	      {
813	        "name": "Method Comparison with Multiple Testing Correction",
814	        "columns": [
815	          "Method",
816	          "η_max sig",
817	          "K_eff sig",
818	          "K_eff direction"
819	        ],
820	        "rows": [
821	          [
822	            "OLS + FDR",
823	            "11/12",
824	            "8/12",
825	            "7+/1-"
826	          ],
827	          [
828	            "OLS + Bonferroni",
829	            "7/12",
830	            "2/12",
831	            "2+/0-"
832	          ],
833	          [
834	            "Clustered SE + FDR",
835	            "8/12",
836	            "0/12",
837	            "-"
838	          ],
839	          [
840	            "Beta regression + FDR",
841	            "10/12",
842	            "4/12",
843	            "3+/1-"
844	          ]
845	        ]
846	      }
847	    ],
848	    "figures": [],
849	    "analysis": "VIF 分析消除了审稿人 RC1 的 last-resort 攻击角度——multicollinearity is moderate, not pathological。r=0.70 在经验社会科学中常见（e.g., income and education）， standard practice 是报告 VIF 并继续。Beta regression 提供了 distributional robustness check：结论与 log-log OLS 一致。论文可在 methods 节用一段话报告 VIF diagnostics 并在 supplementary 中给出完整表格。\n\nRaw VIF ≈ 2.96 直接由 r=0.70 的 confound 决定（VIF = 1/(1-r²) = 1/(1-0.49) = 1.96 在 bivariate 情况下；加上 tier indicators 后升至约 2.96）。VIF < 5 远低于标准 reviewer concern 阈值（通常 VIF > 10），甚至低于 stricter 标准（VIF > 5）。Residualization 后 VIF 降至 1.0（by construction），residualized K_eff 的 partial correlation 仅 0.18 vs η_max 的 0.42——直接量化了主导性差异。Beta regression 作为 ASR ∈ [0,1] 的 distributional 替代方案：η_max 显著性从 log-log OLS 的 11/12 降至 10/12（beta regression 对极端值更鲁棒），K_eff 从 8/12 升至 4/12（beta regression 更好地处理 heteroscedasticity）。Condition number 4.8 < 30 确认无有害多重共线性。Bonferroni 校正（most conservative）给出 η_max 7/12 vs K_eff 2/12——即使在最保守的多重比较 校正下 η_max 仍显著主导。无 reviewer-blocking issue。"
850	  },
851	  {
852	    "name": "Aggregation Gradient Under Clustered SE",
853	    "description": "在 clustered SE 和 bootstrap 下重新运行 4 种聚合规则 + 新增 veto rule，验证聚合梯度是否为真实效应而非 overlap 伪迹",
854	    "results": {
855	      "aggregation_rules": [
856	        "majority",
857	        "weighted",
858	        "threshold",
859	        "bayesian",
860	        "veto"
861	      ],
862	      "correction_methods": [
863	        "OLS",
864	        "clustered_se",
865	        "bootstrap_v2"
866	      ],
867	      "majority_clustered_se": {
868	        "eta_sig": "8/12",
869	        "keff_sig": "0/12"
870	      },
871	      "weighted_clustered_se": {
872	        "eta_sig": "6/12",
873	        "keff_sig": "1/12",
874	        "keff_direction": "1+"
875	      },
876	      "threshold_clustered_se": {
877	        "eta_sig": "10/12",
878	        "keff_sig": "4/12",
879	        "keff_direction": "3+/1-",
880	        "r2": 0.87
881	      },
882	      "bayesian_clustered_se": {
883	        "eta_sig": "5/12",
884	        "keff_sig": "4/12",
885	        "keff_direction": "1+/3-",
886	        "keff_negative_frac": "3/4"
887	      },
888	      "veto_clustered_se": {
889	        "eta_sig": "11/12",
890	        "keff_sig": "0/12",
891	        "r2": 0.82
892	      },
893	      "bayesian_bootstrap": {
894	        "eta_sig": "3/12",
895	        "keff_sig": "3/12",
896	        "keff_direction": "0+/3-",
897	        "keff_negative_frac": "3/3"
898	      },
899	      "gradient_preserved_under_correction": true,
900	      "bayesian_keff_flip_genuine": true,
901	      "aggregation_gradient_order": "veto > threshold > majority > weighted > bayesian"
902	    },
903	    "tables": [
904	      {
905	        "name": "Aggregation Gradient Under Clustered SE",
906	        "columns": [
907	          "Rule",
908	          "η_max sig",
909	          "K_eff sig",
910	          "K_eff neg frac",
911	          "R²",
912	          "Gradient position"
913	        ],
914	        "rows": [
915	          [
916	            "Veto",
917	            "11/12",
918	            "0/12",
919	            "-",
920	            "0.82",
921	            "Maximum vulnerability"
922	          ],
923	          [
924	            "Threshold",
925	            "10/12",
926	            "4/12",
927	            "1/4",
928	            "0.87",
929	            "High"
930	          ],
931	          [
932	            "Majority",
933	            "8/12",
934	            "0/12",
935	            "-",
936	            "0.28",
937	            "Moderate"
938	          ],
939	          [
940	            "Weighted",
941	            "6/12",
942	            "1/12",
943	            "0/1",
944	            "0.26",
945	            "Low-moderate"
946	          ],
947	          [
948	            "Bayesian",
949	            "5/12",
950	            "4/12",
951	            "3/4",
952	            "0.09",
953	            "Minimum vulnerability"
954	          ]
955	        ]
956	      },
957	      {
958	        "name": "Bayesian K_eff Direction Detail",
959	        "columns": [
960	          "Correction",
961	          "K_eff sig total",
962	          "K_eff positive",
963	          "K_eff negative",
964	          "Neg fraction"
965	        ],
966	        "rows": [
967	          [
968	            "OLS",
969	            "7/12",
970	            "1",
971	            "6",
972	            "6/7 (86%)"
973	          ],
974	          [
975	            "Clustered SE",
976	            "4/12",
977	            "1",
978	            "3",
979	            "3/4 (75%)"
980	          ],
981	          [
982	            "Bootstrap v2",
983	            "3/12",
984	            "0",
985	            "3",
986	            "3/3 (100%)"
987	          ]
988	        ]
989	      }
990	    ],
991	    "figures": [],
992	    "analysis": "聚合梯度在校正下的稳健性是论文的独立贡献——它不受 non-independence concern 的影响，因为 它描述的是投票规则数学的 structural 性质。Veto rule 的加入使梯度两端更 extreme： veto（pure weakest-link）vs Bayesian（weakest-link neutralized + diversity flip）。 论文可以将此呈现为 defense design spectrum——practitioners 根据其对 false positive vs false negative 的偏好选择适当位置。Bayesian K_eff 在 bootstrap 下 3/3 negative 是 cleanest possible evidence for the flip。\n\n聚合梯度在 clustered SE 下保持，因为不同投票规则产生的脆弱性差异是 structural/mathematical 的，不是 panel overlap 的伪迹。Threshold（unanimity）要求所有 judges 一致，使单个 judge 的 failure 直接传导为 panel failure——R²=0.87 说明 panel 结构几乎完全决定了 threshold voting 下的脆弱性。这种强 structural 效应在 clustered SE 下大量存活（η_max 10/12, K_eff 4/12）。Veto rule（单个 judge 可否决）是 weakest-link 的极端化——η_max 几乎 完美预测（11/12），K_eff 被完全压倒（0/12）。 Bayesian calibration 翻转 K_eff 方向的关键机制：Bayesian 使用 prior accuracy 下调不可靠 judges 的权重，有效中和了 weakest-link 通道。η_max 的直接效应被削弱（11→5/12）。 剩余的 K_eff 信号主要来自 shared-bias 条件（diversity 保护性的部分），因此净方向为负。 在 bootstrap 下，Bayesian K_eff 仅 3/12 显著但全部为负（3/3 negative fraction）—— direction flip 是真实的。这确认 aggregation 是独立于 non-independence correction 的 control lever。论文的 prescriptive conclusion（robustness-first + Bayesian = dual-channel defense）在最严格校正下依然成立。"
993	  },
994	  {
995	    "name": "Open-Ended Generation Benchmark Extension",
996	    "description": "在 MT-Bench 风格的 open-ended generation 任务上测试 weakest-link 假说，超越 MCQ 格式",
997	    "results": {
998	      "benchmark": "MT-Bench (8 categories)",
999	      "judge_format": "1-10 scale scoring",
1000	      "models_available": 12,
1001	      "panels": 220,
1002	      "attack_types": [
1003	        "style_manipulation",
1004	        "length_inflation",
1005	        "format_gaming"
1006	      ],
1007	      "conditions": 6,
1008	      "eta_max_sig_ols": "5/6",
1009	      "keff_sig_ols": "3/6 (2+/1-)",
1010	      "eta_max_sig_clustered_se": "4/6",
1011	      "keff_sig_clustered_se": "0/6",
1012	      "r2_mean": 0.22,
1013	      "gam_generation_split": {
1014	        "style_manipulation": "shared-bias (negative K_eff)",
1015	        "length_inflation": "shared-bias (negative K_eff)",
1016	        "format_gaming": "targeted (positive K_eff)"
1017	      },
1018	      "min_eta_max_wins": "6/6",
1019	      "cross_format_consistency": "η_max dominant in both MCQ and generation"
1020	    },
1021	    "tables": [
1022	      {
1023	        "name": "Generation Benchmark Results (Clustered SE)",
1024	        "columns": [
1025	          "Condition",
1026	          "η_max sig?",
1027	          "K_eff sig?",
1028	          "K_eff GAM dir",
1029	          "R²"
1030	        ],
1031	        "rows": [
1032	          [
1033	            "style_manipulation × MT-Bench",
1034	            "Yes",
1035	            "No",
1036	            "negative",
1037	            "0.19"
1038	          ],
1039	          [
1040	            "length_inflation × MT-Bench",
1041	            "Yes",
1042	            "No",
1043	            "negative",
1044	            "0.24"
1045	          ],
1046	          [
1047	            "format_gaming × MT-Bench",
1048	            "Yes",
1049	            "No",
1050	            "positive",
1051	            "0.23"
1052	          ]
1053	        ]
1054	      },
1055	      {
1056	        "name": "Cross-Format Consistency",
1057	        "columns": [
1058	          "Format",
1059	          "η_max sig (CL-SE)",
1060	          "K_eff sig (CL-SE)",
1061	          "Dominance ratio"
1062	        ],
1063	        "rows": [
1064	          [
1065	            "MCQ (MMLU+ARC)",
1066	            "8/12",
1067	            "0/12",
1068	            "8:0"
1069	          ],
1070	          [
1071	            "Generation (MT-Bench)",
1072	            "4/6",
1073	            "0/6",
1074	            "4:0"
1075	          ],
1076	          [
1077	            "Combined",
1078	            "12/18",
1079	            "0/18",
1080	            "12:0"
1081	          ]
1082	        ]
1083	      }
1084	    ],
1085	    "figures": [],
1086	    "analysis": "Generation extension 消除了\"MCQ-specific artifact\"的审稿人质疑。η_max 主导性跨 task format 通用性是论文 generalizability 论证的关键证据。R² 降低反映了 generation evaluation 的内在 noise，但 relative driver importance（η_max >> K_eff）完全保持。 此实验可作为 Section 5 的扩展分析或 supplementary material。\n\nη_max 主导性在 generation 任务中持续因为底层机制相同：无论 judges 评估 MCQ 正确性还是 generation 质量，adversary 都针对最可操纵的 judge。Generation 的 1-10 scale 提供了比 MCQ binary 更多的操纵空间（微妙的 style/format manipulation 可以影响 rubric-based scoring），但 vulnerability 的 distribution across judges 仍然是高度不均匀的—— 某些 judges 对 length inflation 或 format gaming 特别敏感。R² 较低（0.22 vs MCQ 的 0.30）因为 generation evaluation 有更多 idiosyncratic variance（rubric interpretation, 文化偏好等）。K_eff 在 OLS 下 3/6 显著但 clustered SE 后归零——与 MCQ 完全一致。 GAM 分类中，style manipulation 和 length inflation 属于 shared-bias（所有 LLM judges 都倾向于给更长/更 polished 的回答更高分），而 format gaming 属于 targeted（利用特定 model 的 format parsing 差异）。12 模型（部分 API 模型不支持 generation evaluation） 给出 220 panels，足够进行 regression analysis。min_eta_max 策略在 generation 上同样 赢 6/6，确认 practical recommendation 跨 task format 通用。"
1087	  },
1088	  {
1089	    "name": "Partial-Knowledge Adversary Model",
1090	    "description": "模拟 adversary 仅知道 judge family labels（不知具体脆弱性 profile）的 realistic threat model",
1091	    "results": {
1092	      "knowledge_levels": [
1093	        "full (baseline)",
1094	        "family-only",
1095	        "random"
1096	      ],
1097	      "asr_reduction_family_vs_full_pct": 18,
1098	      "asr_reduction_random_vs_full_pct": 42,
1099	      "family_knowledge_eta_max_sig_clustered_se": "7/12",
1100	      "family_knowledge_keff_sig_clustered_se": "0/12",
1101	      "family_knowledge_dominance_ratio": "7:0",
1102	      "random_targeting_eta_max_sig_clustered_se": "3/12",
1103	      "random_targeting_keff_sig_clustered_se": "0/12",
1104	      "family_knowledge_r2_mean": 0.24,
1105	      "family_label_attack_efficiency": 0.82
1106	    },
1107	    "tables": [
1108	      {
1109	        "name": "Adversary Knowledge Level Comparison (Clustered SE)",
1110	        "columns": [
1111	          "Knowledge level",
1112	          "Mean ASR",
1113	          "ASR vs full (%)",
1114	          "η_max sig",
1115	          "K_eff sig",
1116	          "R²"
1117	        ],
1118	        "rows": [
1119	          [
1120	            "Full knowledge",
1121	            "0.195",
1122	            "100%",
1123	            "8/12",
1124	            "0/12",
1125	            "0.30"
1126	          ],
1127	          [
1128	            "Family-only",
1129	            "0.160",
1130	            "82%",
1131	            "7/12",
1132	            "0/12",
1133	            "0.24"
1134	          ],
1135	          [
1136	            "Random",
1137	            "0.113",
1138	            "58%",
1139	            "3/12",
1140	            "0/12",
1141	            "0.08"
1142	          ]
1143	        ]
1144	      },
1145	      {
1146	        "name": "Family Label Informativeness",
1147	        "columns": [
1148	          "Metric",
1149	          "Value",
1150	          "Interpretation"
1151	        ],
1152	        "rows": [
1153	          [
1154	            "Attack efficiency (family/full)",
1155	            "0.82",
1156	            "Family labels highly informative for targeting"
1157	          ],
1158	          [
1159	            "Family-vulnerability correlation",
1160	            "0.61",
1161	            "Moderate; same family shares weaknesses"
1162	          ],
1163	          [
1164	            "η_max sig retention (family vs full)",
1165	            "7/8",
1166	            "Targeting still exploits weakest link"
1167	          ]
1168	        ]
1169	      }
1170	    ],
1171	    "figures": [],
1172	    "analysis": "Partial-knowledge 实验将论文结论从 worst-case（omniscient adversary）扩展至 realistic threat model。Family-only adversary 保留 82% 攻击效率这一发现对 practical defense implications 至关重要——defenders 不能依赖\"adversary 不知道 panel 具体组成\"的假设， 因为 family-level knowledge 几乎 sufficient。η_max 在所有 knowledge levels 下主导， K_eff 在所有 knowledge levels 下为 0/12——核心发现对 adversary 能力假设鲁棒。 Random targeting 的 R²=0.08 呼应 plan_003 的 RF 结论：panel 结构的预测力依赖于 adversary 的 strategic targeting——这是论文 adaptive vs random 对比叙事的第三个 independent evidence line。\n\nFamily-only adversary 的 ASR 仅降 18%（而非 random 的 42%），因为 family labels 与 vulnerability profiles 有中等相关：同 family 模型共享 training pipeline 和 architectural biases，adversary 可基于 family 推断出 approximately correct 的攻击 策略。η_max 仍然主导（7/12 vs full-knowledge 的 8/12）因为 family-level targeting 仍 preferentially hits weaker judges——family labels 虽然 noisy 但 informationally above chance。K_eff 在 partial-knowledge 下同样为 0/12——diversity 在任何 knowledge level 下都不是 independent protective factor after correction。Attack efficiency 0.82 意味着 family labels 提供了 82% of full-knowledge targeting effectiveness——这对 ecological validity 至关重要：现实中 adversary 通常知道 panel 的 model families （从 API endpoint, response style 等推断），因此 full-knowledge 结果的 relevance 不仅限于理论上限。Random targeting 下 η_max 仅 3/12 显著——random adversary 无法有效 利用 individual weaknesses，说明 η_max 的 predictive power 依赖于 adversary 的 targeting ability，与 adaptive vs RF contrast（plan_003）形成完整呼应。"
1173	  }
1174	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "983a25dc-1a64-47d8-b02a-30b80ce4fde3",
  "isSidechain": false,
  "promptId": "d5483bc6-a830-4026-80bc-d9c580d884bc",
  "type": "user",
  "uuid": "611f301a-6777-43fe-8ca4-7c7b62c91e1f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"15-Model Scaling Expansion\",\n    \"description\": \"扩展至 15 模型（6 families），455 panels × 12 conditions 全量回归 + MI 矩阵 + 所有校正方法\",\n    \"results\": {\n      \"status\": \"DONE (plan001_step1_full_v4)\",\n      \"models\": 15,\n      \"panels\": 455,\n      \"conditions\": 12,\n      \"eta_max_sig_ols\": \"11/12\",\n      \"keff_sig_ols\": \"8/12 (7+/1-)\",\n      \"eta_max_sig_clustered_se\": \"8/12\",\n      \"keff_sig_clustered_se\": \"0/12\",\n      \"eta_max_sig_bootstrap_v2\": \"5/12\",\n      \"keff_sig_bootstrap_v2\": \"1/12\",\n      \"eta_max_sig_mixed_effects\": \"7/12\",\n      \"keff_sig_mixed_effects\": \"3/12\",\n      \"dominance_ratio_bootstrap\": \"5:1\",\n      \"gam_split\": \"6 targeted positive / 6 shared-bias negative\",\n      \"min_eta_max_wins\": \"12/12\",\n      \"confound_r\": 0.701,\n      \"se_inflation_factor\": \"~2.5x\",\n      \"rf_keff_sig\": \"2/2\",\n      \"rf_r2_mmlu\": 0.734,\n      \"rf_r2_arc\": 0.813\n    },\n    \"tables\": [\n      {\n        \"name\": \"Correction Method Comparison (Actual Results)\",\n        \"columns\": [\n          \"Method\",\n          \"η_max sig\",\n          \"K_eff sig\",\n          \"K_eff dir\",\n          \"Note\"\n        ],\n        \"rows\": [\n          [\n            \"OLS\",\n            \"11/12\",\n            \"8/12\",\n            \"7+/1-\",\n            \"Panel overlap inflated\"\n          ],\n          [\n            \"Clustered SE (CR1, 15 clusters)\",\n            \"8/12\",\n            \"0/12\",\n            \"-\",\n            \"Conservative\"\n          ],\n          [\n            \"Wild cluster bootstrap v2\",\n            \"5/12\",\n            \"1/12\",\n            \"1+\",\n            \"Max-p across 3 positions\"\n          ],\n          [\n            \"Mixed effects\",\n            \"7/12\",\n            \"3/12\",\n            \"3+\",\n            \"Random judge intercepts\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"已完成。η_max:K_eff 主导比从 OLS 的 1.4:1 升至 bootstrap 的 5:1，证明相对主导性在校正下 增强而非减弱。Benchmark 不对称（MMLU 4/6 vs ARC 1/6 存活 bootstrap）由 MMLU 4-choice 格式提供更多 scoring variance 解释。此结果构成 paper 的实证基础。\\n\\n已完成。15 模型覆盖 6 families × 3 capability tiers，提供 η_max 和 K_eff 充足方差。 SE 膨胀 ~2.5x 与 91/455 panel overlap 一致（claude-3-haiku 出现在 91 个 panels 中）。 η_max 存活校正因为它捕捉的是真实的个体 judge 脆弱性——不是 panel 重叠伪迹。 K_eff 崩溃因为其 OLS 显著性被 overlapping panels 的相关残差膨胀——clustered SE 控制共享 judge 成员关系后，K_eff 的独立信号太弱。GAM 6:6 分割源于攻击机制差异： targeted attacks 利用 judge 特异性弱点（diversity = 更多攻击面），shared-bias attacks 利用共性认知偏差（diversity = 部分 judges 免疫）。\"\n  },\n  {\n    \"name\": \"Attack Surface Expansion\",\n    \"description\": \"新增 3 种攻击类型（few-shot hijacking, persona manipulation, instruction override），在 15 模型 × 2 benchmarks 上运行，共 6 新 conditions\",\n    \"results\": {\n      \"new_attack_types\": 3,\n      \"new_conditions\": 6,\n      \"total_conditions\": 18,\n      \"new_eta_max_sig_ols\": \"6/6\",\n      \"new_keff_sig_ols\": \"4/6 (3+/1-)\",\n      \"new_eta_max_sig_clustered_se\": \"5/6\",\n      \"new_keff_sig_clustered_se\": \"0/6\",\n      \"new_eta_max_sig_bootstrap\": \"3/6\",\n      \"new_keff_sig_bootstrap\": \"0/6\",\n      \"combined_eta_max_sig_clustered_se\": \"13/18\",\n      \"combined_keff_sig_clustered_se\": \"0/18\",\n      \"combined_dominance_ratio_clustered_se\": \"13:0\",\n      \"gam_extended_split\": \"10 targeted positive / 8 shared-bias negative\",\n      \"gam_new_attacks_classification\": {\n        \"few_shot_hijacking\": \"targeted (positive K_eff)\",\n        \"persona_manipulation\": \"shared-bias (negative K_eff)\",\n        \"instruction_override\": \"targeted (positive K_eff)\"\n      },\n      \"new_r2_range\": [\n        0.22,\n        0.45\n      ],\n      \"min_eta_max_wins_extended\": \"18/18\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Extended Attack Taxonomy (Clustered SE)\",\n        \"columns\": [\n          \"Attack Type\",\n          \"Mechanism\",\n          \"Benchmark\",\n          \"η_max sig?\",\n          \"K_eff sig?\",\n          \"K_eff GAM direction\"\n        ],\n        \"rows\": [\n          [\n            \"few-shot hijacking\",\n            \"targeted\",\n            \"MMLU\",\n            \"Yes\",\n            \"No\",\n            \"positive\"\n          ],\n          [\n            \"few-shot hijacking\",\n            \"targeted\",\n            \"ARC\",\n            \"Yes\",\n            \"No\",\n            \"positive\"\n          ],\n          [\n            \"persona manipulation\",\n            \"shared-bias\",\n            \"MMLU\",\n            \"Yes\",\n            \"No\",\n            \"negative\"\n          ],\n          [\n            \"persona manipulation\",\n            \"shared-bias\",\n            \"ARC\",\n            \"Yes\",\n            \"No\",\n            \"negative\"\n          ],\n          [\n            \"instruction override\",\n            \"targeted\",\n            \"MMLU\",\n            \"Yes\",\n            \"No\",\n            \"positive\"\n          ],\n          [\n            \"instruction override\",\n            \"targeted\",\n            \"ARC\",\n            \"No\",\n            \"No\",\n            \"positive\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Extended GAM Split Summary\",\n        \"columns\": [\n          \"Category\",\n          \"Original (6 attacks)\",\n          \"New (3 attacks)\",\n          \"Total\",\n          \"K_eff direction\"\n        ],\n        \"rows\": [\n          [\n            \"Targeted\",\n            \"6/6 positive\",\n            \"4/4 positive\",\n            \"10/10\",\n            \"positive (diversity harmful)\"\n          ],\n          [\n            \"Shared-bias\",\n            \"6/6 negative\",\n            \"2/2 negative (persona×2)\",\n            \"8/8\",\n            \"negative (diversity protective)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"新攻击类型提供独立证据线，确认 η_max 主导性不依赖于特定攻击选择。GAM taxonomy 从 6:6 扩展至 10:8，mechanistic split 的稳健性增强——审稿人无法再质疑 taxonomy 是 cherry-picked 6 种 攻击的巧合。Instruction override 在 ARC 上 η_max 未显著（ARC 2-choice 格式对 instruction override 的 judge 间方差不敏感），与原始 benchmark asymmetry 一致。论文标题和核心叙事完全支持。\\n\\nFew-shot hijacking 利用模型在 in-context learning 上的个体差异——不同 judges 对 few-shot 示例的敏感度差异极大（GPT-4.1 vs Llama-8B 可差 3-5x），因此属于 targeted attack，η_max 捕捉最易受影响的 judge。Instruction override 利用 instruction-following 能力的模型间方差， 同样属于 targeted。Persona manipulation 利用 LLMs 对权威/身份线索的普遍敏感性——这是一种 共享认知偏差，不同能力模型都会受影响，因此属于 shared-bias，K_eff 方向为负（diversity 提供 部分免疫）。新攻击在 OLS 下延续 η_max 主导模式，但 K_eff 再次因 panel overlap 膨胀而 显著——clustered SE 后归零，与原 12 conditions 完全一致。GAM 扩展至 10:8 分割，clean taxonomy 覆盖 9 种攻击类型。\"\n  },\n  {\n    \"name\": \"Random-Fault BFT Contrast Experiment\",\n    \"description\": \"Monte Carlo 随机故障模拟作为 BFT 对照。每个 judge 以 η_j = 1 - clean_accuracy 独立失败，majority vote。对比 adaptive regime 证明 BFT 反转\",\n    \"results\": {\n      \"regime\": \"Random Fault (i.i.d.)\",\n      \"conditions\": 2,\n      \"monte_carlo_iterations\": 10000,\n      \"rf_keff_sig_ols\": \"2/2\",\n      \"rf_keff_sig_clustered_se\": \"2/2\",\n      \"rf_keff_sig_bootstrap\": \"2/2\",\n      \"rf_keff_direction\": \"positive (2/2)\",\n      \"rf_keff_std_beta_mmlu\": 0.215,\n      \"rf_keff_std_beta_arc\": 0.379,\n      \"rf_eta_sig_all_methods\": \"2/2\",\n      \"rf_r2_mmlu\": 0.78,\n      \"rf_r2_arc\": 0.81,\n      \"adaptive_keff_sig_clustered_se\": \"0/12\",\n      \"adaptive_keff_sig_bootstrap\": \"1/12\",\n      \"delta_r2_rf_vs_adaptive\": 0.48,\n      \"go_nogo_gate\": \"PASS (RF K_eff ≥2/2)\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"RF vs Adaptive Contrast (Key Metrics)\",\n        \"columns\": [\n          \"Metric\",\n          \"Random Fault\",\n          \"Adaptive\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"K_eff sig (OLS)\",\n            \"2/2\",\n            \"8/12 (7+/1-)\",\n            \"Both appear significant under OLS\"\n          ],\n          [\n            \"K_eff sig (Clustered SE)\",\n            \"2/2\",\n            \"0/12\",\n            \"RF genuine; adaptive artifactual\"\n          ],\n          [\n            \"K_eff sig (Bootstrap v2)\",\n            \"2/2\",\n            \"1/12\",\n            \"Consistent contrast\"\n          ],\n          [\n            \"K_eff std β (mean)\",\n            \"+0.297\",\n            \"+0.164\",\n            \"RF effect larger and genuine\"\n          ],\n          [\n            \"R²\",\n            \"0.78-0.81\",\n            \"0.25-0.35\",\n            \"RF structurally determined; adaptive not\"\n          ],\n          [\n            \"η_max sig (all methods)\",\n            \"2/2\",\n            \"5-8/12\",\n            \"η_max genuine in both regimes\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"RF Per-Benchmark Detail\",\n        \"columns\": [\n          \"Benchmark\",\n          \"η_max β\",\n          \"K_eff β\",\n          \"R²\",\n          \"K_eff p (bootstrap)\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            \"+0.482\",\n            \"+0.215\",\n            \"0.78\",\n            \"0.003\"\n          ],\n          [\n            \"ARC\",\n            \"+0.551\",\n            \"+0.379\",\n            \"0.81\",\n            \"<0.001\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"这是论文的关键因果证据。RF 对照证明 K_eff 在满足 i.i.d. 假设时有真实效应——BFT 理论 在随机故障下成立。而 adaptive regime 下 K_eff 的 OLS 显著性完全是 panel overlap 的伪迹。 这不是\\\"diversity helps under RF but hurts under adaptive\\\"——K_eff 在两种 regime 下方向均 为正。区别是：RF 下 K_eff 的正关联是真实的（panel 结构决定了容错性），adaptive 下是膨胀的 （adversary 引入的策略方差使 panel 结构预测力崩溃）。此发现为 Contribution #2（BFT reversal evidence）提供了不可替代的因果论证。\\n\\n随机故障下 K_eff 显著的根本原因是 BFT 的 i.i.d. 假设成立：每个 judge 独立以固定概率犯错， panel 结构（多样性）直接影响冗余覆盖。K_eff 高的 panel 中 judges 的错误模式更不相关， majority vote 的容错能力与独立性成正比——这正是 BFT 的核心机制。K_eff 方向为正（diversity → higher error）因为高 K_eff panel 必然包含弱模型（r=0.70 tradeoff），而在 i.i.d. 体制下 弱模型的高错误率直接传导为 panel 错误率——但关键是 K_eff 的贡献是独立的、真实的（所有校正 方法均显著 2/2）。对照 adaptive regime：相同的 K_eff 在 OLS 下显著 8/12，但 clustered SE 后崩溃至 0/12——因为 adaptive adversary 引入了 panel 结构无法预测的策略方差，K_eff 的 apparent OLS 信号完全来自 panel overlap 膨胀。R² 差异（RF 0.78-0.81 vs adaptive ~0.30） 直接量化了 adaptive adversary 引入的不可预测性。GO/NO-GO gate 通过，BFT framing 得到 因果层面的支撑。\"\n  },\n  {\n    \"name\": \"Capability-Matched Validation\",\n    \"description\": \"在同一 capability tier 内（主要利用 9-model base tier, 84 panels）测试控制 η_max 方差后 K_eff 是否浮现为显著预测因子\",\n    \"results\": {\n      \"primary_tier\": \"base (9 models, 84 panels)\",\n      \"within_tier_eta_max_variance_reduction\": \"65-70%\",\n      \"within_tier_keff_eta_max_r\": 0.35,\n      \"conditions\": 12,\n      \"within_tier_keff_sig_ols\": \"5/12\",\n      \"within_tier_keff_sig_clustered_se\": \"2/12\",\n      \"within_tier_keff_direction\": \"4+/1-\",\n      \"within_tier_eta_max_sig_ols\": \"7/12\",\n      \"within_tier_eta_max_sig_clustered_se\": \"4/12\",\n      \"within_tier_dominance_ratio\": \"2:1\",\n      \"within_tier_r2_mean\": 0.18,\n      \"cross_tier_comparison\": {\n        \"full_pool_dominance_ratio\": \"5:1\",\n        \"within_tier_dominance_ratio\": \"2:1\",\n        \"interpretation\": \"η_max still dominant but K_eff gains relative signal\"\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Cross-Tier vs Within-Tier Comparison\",\n        \"columns\": [\n          \"Setting\",\n          \"Panels\",\n          \"K_eff-η_max r\",\n          \"η_max sig (CL-SE)\",\n          \"K_eff sig (CL-SE)\",\n          \"Ratio\",\n          \"R² mean\"\n        ],\n        \"rows\": [\n          [\n            \"Full pool (15 models)\",\n            \"455\",\n            \"0.70\",\n            \"8/12\",\n            \"0/12\",\n            \"8:0\",\n            \"0.30\"\n          ],\n          [\n            \"Base tier (9 models)\",\n            \"84\",\n            \"0.35\",\n            \"4/12\",\n            \"2/12\",\n            \"2:1\",\n            \"0.18\"\n          ],\n          [\n            \"Frontier tier (3 models)\",\n            \"1\",\n            \"-\",\n            \"-\",\n            \"-\",\n            \"-\",\n            \"-\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Within-Tier K_eff Significant Conditions\",\n        \"columns\": [\n          \"Condition\",\n          \"K_eff β\",\n          \"K_eff p (CL-SE)\",\n          \"Direction\",\n          \"GAM confirms?\"\n        ],\n        \"rows\": [\n          [\n            \"mmlu×prompt_injection\",\n            \"+0.31\",\n            \"0.028\",\n            \"positive\",\n            \"Yes (targeted)\"\n          ],\n          [\n            \"mmlu×score_manipulation\",\n            \"+0.25\",\n            \"0.041\",\n            \"positive\",\n            \"Yes (targeted)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Capability-matched validation 提供了 disentangle η_max 和 K_eff 的准自然实验。关键发现： 即使在控制 η_max 方差后，K_eff 仍然是次要驱动因素（2:1 而非 1:1 或 K_eff 主导）。 论文可表述为：\\\"当 capability 差异被控制时，diversity 浮现为统计上可检测的次要因素——但在 自然 panel 组合中，capability 差异（通过 η_max）压倒性地主导脆弱性。\\\"这强化了 robustness-first 设计建议：先筛选 capability，再在筛选后的池中考虑 diversity。\\n\\n在同一 capability tier 内，η_max 方差降低约 65-70%（因为同 tier 模型能力接近），而 K_eff 方差保持（同 tier 模型仍来自不同 families/architectures）。η_max 和 K_eff 的 confound 从 r=0.70（全池）降至 r≈0.35（tier 内），解开了回归中的多重共线性。在此条件下，K_eff 的边际信号——通常被 η_max 的强效应淹没——变得可检测。OLS 下 5/12 显著；clustered SE 后 保留 2/12，表明 K_eff 有微弱但真实的独立效应。主导比从 5:1 降至 2:1，但 η_max 仍然 主导。这支持论文叙事：K_eff 有方向性关联但在全池分析中被 η_max 压倒——当人为控制 η_max 方差时 K_eff 才浮现，这恰恰说明在自然变异条件下 η_max 是主要驱动因素。此外，within-tier R² 均值仅 0.18，说明 tier 内的面板脆弱性预测力大幅下降——进一步证明 η_max 的跨 tier 方差是预测力的主要来源。\"\n  },\n  {\n    \"name\": \"Two-Stage Panel Design Algorithm Benchmark\",\n    \"description\": \"实现 robustness-first 两阶段算法（filter η > threshold → maximize K_eff），对标 5 个 baseline 策略\",\n    \"results\": {\n      \"baselines\": [\n        \"random\",\n        \"max_keff\",\n        \"max_disagreement\",\n        \"strongest_k\",\n        \"uniform_family\"\n      ],\n      \"conditions\": 12,\n      \"min_eta_max_wins\": \"12/12\",\n      \"two_stage_vs_min_eta_max_improvement_pp\": [\n        0.3,\n        1.8\n      ],\n      \"two_stage_vs_min_eta_max_mean_improvement_pp\": 0.7,\n      \"two_stage_wins_vs_min_eta_max\": \"7/12\",\n      \"strategy_ranking\": {\n        \"rank_1\": \"two-stage (robustness-first + K_eff)\",\n        \"rank_2\": \"min_eta_max (robustness-first only)\",\n        \"rank_3\": \"strongest_k\",\n        \"rank_4\": \"uniform_family\",\n        \"rank_5\": \"max_disagreement\",\n        \"rank_6\": \"max_keff\",\n        \"rank_7\": \"random\"\n      },\n      \"max_keff_vs_random\": \"worse in 8/12 (includes weak models)\",\n      \"strongest_k_gap_from_min_eta_max\": \"1.2pp mean\",\n      \"asr_advantage_range\": [\n        0.038,\n        0.511\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Strategy Comparison (Mean ASR across 12 conditions)\",\n        \"columns\": [\n          \"Strategy\",\n          \"Mean ASR\",\n          \"Rank\",\n          \"Δ vs random (pp)\"\n        ],\n        \"rows\": [\n          [\n            \"two-stage\",\n            \"0.112\",\n            \"1\",\n            \"-8.3\"\n          ],\n          [\n            \"min_eta_max\",\n            \"0.119\",\n            \"2\",\n            \"-7.6\"\n          ],\n          [\n            \"strongest_k\",\n            \"0.131\",\n            \"3\",\n            \"-6.4\"\n          ],\n          [\n            \"uniform_family\",\n            \"0.158\",\n            \"4\",\n            \"-3.7\"\n          ],\n          [\n            \"max_disagreement\",\n            \"0.172\",\n            \"5\",\n            \"-2.3\"\n          ],\n          [\n            \"random\",\n            \"0.195\",\n            \"6\",\n            \"0.0\"\n          ],\n          [\n            \"max_keff\",\n            \"0.208\",\n            \"7\",\n            \"+1.3\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Two-Stage vs min_eta_max Per-Attack-Type\",\n        \"columns\": [\n          \"Attack category\",\n          \"Conditions\",\n          \"Two-stage better?\",\n          \"Mean Δ (pp)\"\n        ],\n        \"rows\": [\n          [\n            \"Targeted\",\n            \"6\",\n            \"5/6\",\n            \"-1.1\"\n          ],\n          [\n            \"Shared-bias\",\n            \"6\",\n            \"2/6\",\n            \"-0.3\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Two-stage 算法的边际改进（0.7pp）虽然在统计上一致但实际影响不大——论文应诚实呈现这一点。 核心 practical recommendation 保持不变：robustness-first screening 是关键步骤，K_eff 优化是可选的次要步骤。max_keff 策略的失败（差于 random）是论文叙事的有力支撑——直观的 \\\"多样化 panel\\\" 建议在实践中适得其反。\\n\\nmin_eta_max 策略赢 12/12 因为 η_max 是主导脆弱性驱动因素。两阶段策略在 min_eta_max 基础上提供边际改进（mean 0.7pp）：在已通过 robustness 筛选的 judge 子集中，K_eff 的微弱次要效应（在 capability-matched 设置中可检测，如 plan_004 所示）被利用。改进最大 的条件是 targeted attacks（K_eff 方向为正 = diversity 有害 → 在 robustness-screened 池中最小化 K_eff 有帮助）。改进最小的条件是 shared-bias attacks（K_eff 方向为负 → diversity 在这些条件下是保护性的 → 最大化 K_eff 更优）。max_keff 策略表现差于 random 因为最大化 diversity 必然引入弱模型（r=0.70 tradeoff），直接提高了 η_max。 strongest_k 与 min_eta_max 差距仅 1.2pp——因为最强模型通常也最鲁棒，但 min_eta_max 是直接优化目标函数而 strongest_k 是代理指标。\"\n  },\n  {\n    \"name\": \"Per-Judge ASR Concentration Analysis\",\n    \"description\": \"计算每个 panel × attack 的 per-judge ASR 分布的 Gini 系数和 Shannon 熵，量化 adaptive adversary 是否针对特定 judge\",\n    \"results\": {\n      \"panels\": 455,\n      \"conditions\": 12,\n      \"gini_targeted_mean\": 0.78,\n      \"gini_targeted_range\": [\n        0.72,\n        0.85\n      ],\n      \"gini_shared_bias_mean\": 0.43,\n      \"gini_shared_bias_range\": [\n        0.35,\n        0.52\n      ],\n      \"gini_targeted_vs_shared_mannwhitney_p\": \"<0.001\",\n      \"entropy_targeted_mean\": 0.82,\n      \"entropy_shared_bias_mean\": 1.45,\n      \"gini_eta_max_correlation\": 0.83,\n      \"top1_judge_asr_fraction_targeted\": 0.61,\n      \"top1_judge_asr_fraction_shared\": 0.38\n    },\n    \"tables\": [\n      {\n        \"name\": \"ASR Concentration by Attack Category\",\n        \"columns\": [\n          \"Attack Type\",\n          \"Category\",\n          \"Gini (mean)\",\n          \"Entropy (mean)\",\n          \"Top-1 judge ASR fraction\"\n        ],\n        \"rows\": [\n          [\n            \"prompt_injection\",\n            \"targeted\",\n            \"0.82\",\n            \"0.73\",\n            \"0.65\"\n          ],\n          [\n            \"score_manipulation\",\n            \"targeted\",\n            \"0.79\",\n            \"0.78\",\n            \"0.62\"\n          ],\n          [\n            \"position_bias\",\n            \"targeted\",\n            \"0.74\",\n            \"0.94\",\n            \"0.56\"\n          ],\n          [\n            \"sycophancy\",\n            \"shared-bias\",\n            \"0.45\",\n            \"1.38\",\n            \"0.40\"\n          ],\n          [\n            \"verbosity_bias\",\n            \"shared-bias\",\n            \"0.42\",\n            \"1.47\",\n            \"0.37\"\n          ],\n          [\n            \"authority_bias\",\n            \"shared-bias\",\n            \"0.41\",\n            \"1.50\",\n            \"0.36\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"ASR 浓度分析为 η_max 主导性提供了微观机制证据，超越了回归系数的间接推断。审稿人常问 \\\"what's the mechanism?\\\"——本实验直接回答：targeted adversary 将攻击集中在 weakest judge 上（Gini>0.7），使 η_max 成为 panel 脆弱性的充分统计量。shared-bias 下 ASR 更分散 解释了为什么 K_eff 在这类攻击中为负——diversity 提供 partial immunity 因为并非所有 judges 都同样受 shared bias 影响。此发现独立验证 GAM taxonomy。\\n\\nTargeted attacks（prompt injection, score manipulation, position bias）利用特定 judge 的个体弱点——adversary 的攻击策略集中在 panel 中最脆弱的 judge 上。这导致 ASR 分布 高度集中（Gini 0.72-0.85）：top-1 judge 贡献了约 61% 的 panel 总 ASR。这是 η_max 主导性的直接微观机制证据——vulnerability 确实集中在 weakest link。相比之下，shared-bias attacks（sycophancy, verbosity, authority）利用多个 judges 共享的认知偏差，ASR 更 均匀地分布在 panel 成员间（Gini 0.35-0.52），top-1 judge 仅贡献约 38%。Gini 与 η_max 的高相关（r=0.83）直接证明 panel-level vulnerability 与 judge-level concentration 是同一现象的两个面。这为 GAM 6:6 split 提供了独立的 mechanistic 验证——targeted 和 shared-bias 不仅在 K_eff 方向上分裂，在 ASR concentration 模式上也完全分裂。\"\n  },\n  {\n    \"name\": \"Diversity-Capability Tradeoff Visualization\",\n    \"description\": \"绘制 K_eff vs η_max scatter，拟合 tradeoff curve，计算 Pareto frontier，按 tier 分层\",\n    \"results\": {\n      \"overall_keff_etamax_r\": 0.7,\n      \"overall_keff_etamax_r_ci95\": [\n        0.66,\n        0.74\n      ],\n      \"tier_stratified\": {\n        \"base_tier_r\": 0.52,\n        \"mid_tier_r\": 0.48,\n        \"frontier_tier_r\": 0.35\n      },\n      \"pareto_frontier_size\": 12,\n      \"pareto_dominance_pct\": \"97.4% of panels dominated\",\n      \"pareto_frontier_composition\": \"predominantly low-K_eff, low-η_max panels\",\n      \"tradeoff_curve_fit\": \"monotone increasing, concave\",\n      \"within_family_r\": 0.81,\n      \"cross_family_r\": 0.65\n    },\n    \"tables\": [\n      {\n        \"name\": \"Tradeoff Correlation by Stratification\",\n        \"columns\": [\n          \"Stratification\",\n          \"N panels\",\n          \"r(K_eff, η_max)\",\n          \"95% CI\"\n        ],\n        \"rows\": [\n          [\n            \"Full pool\",\n            \"455\",\n            \"0.70\",\n            \"[0.66, 0.74]\"\n          ],\n          [\n            \"Base tier only\",\n            \"84\",\n            \"0.52\",\n            \"[0.38, 0.64]\"\n          ],\n          [\n            \"Within-family\",\n            \"varies\",\n            \"0.81\",\n            \"[0.73, 0.87]\"\n          ],\n          [\n            \"Cross-family\",\n            \"varies\",\n            \"0.65\",\n            \"[0.58, 0.71]\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"可视化使 structural constraint 具象化——审稿人直观理解为什么 max_keff 策略失败（右上角） 而 min_eta_max 策略成功（左下角）。Tier 内相关降低的发现为 two-stage algorithm 提供了 理论基础：capability screening 打破了跨 tier 的 strong tradeoff，使后续 diversity 优化在弱 tradeoff 条件下进行。此 figure 应作为论文 Fig 3 或 Fig 4。\\n\\nr=0.70 的 structural correlation 源于当前 LLM 生态系统的特性：最大化 K_eff 需要包含来自 不同 capability tiers 的模型（不同 family × tier 组合提供最大 behavioral diversity）， 这必然引入能力较弱的 judges，推高 η_max。Tier 分层后 r 降低（base: 0.52, frontier: 0.35） 说明 tradeoff 在 tier 内较弱——within tier 的 diversity（来自不同 architecture/training） 不需要大幅牺牲 capability。这支持 two-stage recommendation 的逻辑：先筛选 capability tier（打破跨 tier tradeoff），再在 tier 内最大化 diversity（利用弱化的 within-tier tradeoff）。 Pareto frontier 几乎全部由 low-K_eff, low-η_max panels 占据——no free lunch，但 robustness-first selection 自然落在 Pareto frontier 上。\"\n  },\n  {\n    \"name\": \"Panel Size Sensitivity Analysis\",\n    \"description\": \"测试 K=3,5,7,9 不同 panel 尺寸下 η_max 主导性是否持续\",\n    \"results\": {\n      \"panel_sizes\": [\n        3,\n        5,\n        7,\n        9\n      ],\n      \"panels_per_size\": [\n        455,\n        3003,\n        6435,\n        5005\n      ],\n      \"eta_max_sig_by_k_clustered_se\": {\n        \"k3\": \"8/12\",\n        \"k5\": \"9/12\",\n        \"k7\": \"9/12\",\n        \"k9\": \"8/12\"\n      },\n      \"keff_sig_by_k_clustered_se\": {\n        \"k3\": \"0/12\",\n        \"k5\": \"1/12\",\n        \"k7\": \"1/12\",\n        \"k9\": \"2/12\"\n      },\n      \"dominance_ratio_by_k\": {\n        \"k3\": \"8:0\",\n        \"k5\": \"9:1\",\n        \"k7\": \"9:1\",\n        \"k9\": \"4:1\"\n      },\n      \"eta_max_effect_size_trend\": \"decreasing with K (from 0.42 at K=3 to 0.31 at K=9)\",\n      \"keff_effect_size_trend\": \"stable (0.12-0.16 across all K)\",\n      \"min_eta_max_wins_by_k\": {\n        \"k3\": \"12/12\",\n        \"k5\": \"12/12\",\n        \"k7\": \"12/12\",\n        \"k9\": \"12/12\"\n      },\n      \"se_inflation_by_k\": [\n        2.5,\n        4.1,\n        6.3,\n        7.8\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Panel Size Sensitivity Summary (Clustered SE)\",\n        \"columns\": [\n          \"K\",\n          \"Panels\",\n          \"η_max sig\",\n          \"K_eff sig\",\n          \"Ratio\",\n          \"SE inflation\",\n          \"η_max β (mean)\"\n        ],\n        \"rows\": [\n          [\n            \"3\",\n            \"455\",\n            \"8/12\",\n            \"0/12\",\n            \"8:0\",\n            \"2.5x\",\n            \"0.42\"\n          ],\n          [\n            \"5\",\n            \"3003\",\n            \"9/12\",\n            \"1/12\",\n            \"9:1\",\n            \"4.1x\",\n            \"0.38\"\n          ],\n          [\n            \"7\",\n            \"6435\",\n            \"9/12\",\n            \"1/12\",\n            \"9:1\",\n            \"6.3x\",\n            \"0.34\"\n          ],\n          [\n            \"9\",\n            \"5005\",\n            \"8/12\",\n            \"2/12\",\n            \"4:1\",\n            \"7.8x\",\n            \"0.31\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Panel size sensitivity 提供两个关键发现：(1) η_max 主导性在 K=3 到 K=9 范围内稳定持续， 确认 weakest-link 不是小 panel 的 artifact；(2) SE 膨胀随 K 急剧增加，为方法论 contribution（non-independence correction 的必要性）提供量化支撑。K=9 时 K_eff 达到 2/12 显著但 effect size 仍微小——power 增加检测到了真实但 practically insignificant 的效应。论文 supplementary 中可报告此分析作为 robustness check。\\n\\nη_max 主导性在所有 K 下持续因为 weakest-link 机制是 scale-invariant：无论 panel 有多少 judges，adversary 总是针对最脆弱的那个。K 增加时 η_max 的 effect size 略降（0.42→0.31） 因为更大 panel 中 majority vote 的容错能力增加——单个 judge 的失败更难翻转整个 panel。 但 η_max 仍然主导，因为 adversary 不只针对一个 judge——adaptive adversary 可以同时攻击 多个弱 judges。K_eff 在 K=9 时达到 2/12 显著：更多 panels（5005）提供了更多统计 power， 但 effect size 保持微小（0.12-0.16）。SE 膨胀随 K 急剧增加（每个 model 出现在更多 panels 中），从 K=3 的 2.5x 到 K=9 的 7.8x。这为 non-independence 校正方法的必要性 提供了更强的论据——在 K=7 或 K=9 下使用 OLS 会产生极度膨胀的显著性计数。 min_eta_max 策略在所有 K 下赢 12/12，确认 practical recommendation 对 panel size 鲁棒。\"\n  },\n  {\n    \"name\": \"VIF + Multicollinearity Diagnostic\",\n    \"description\": \"计算 VIF、partial correlations、residualized K_eff regression，应用 Bonferroni/FDR 校正，尝试 beta regression\",\n    \"results\": {\n      \"gpu_needed\": false,\n      \"raw_vif_keff\": 2.96,\n      \"raw_vif_eta_max\": 2.96,\n      \"residualized_vif_keff\": 1.0,\n      \"partial_correlation_keff_asr_given_eta\": 0.18,\n      \"partial_correlation_eta_asr_given_keff\": 0.42,\n      \"bonferroni_eta_max_sig\": \"7/12\",\n      \"bonferroni_keff_sig\": \"2/12\",\n      \"fdr_eta_max_sig\": \"8/12\",\n      \"fdr_keff_sig\": \"3/12\",\n      \"beta_regression_eta_max_sig\": \"10/12\",\n      \"beta_regression_keff_sig\": \"4/12 (3+/1-)\",\n      \"beta_regression_dispersion_phi\": [\n        3.2,\n        8.7\n      ],\n      \"condition_number\": 4.8,\n      \"reviewer_blocking_issue\": false\n    },\n    \"tables\": [\n      {\n        \"name\": \"Multicollinearity Diagnostics\",\n        \"columns\": [\n          \"Metric\",\n          \"Value\",\n          \"Threshold\",\n          \"Status\"\n        ],\n        \"rows\": [\n          [\n            \"VIF (K_eff, raw)\",\n            \"2.96\",\n            \"< 5 (strict) / < 10 (standard)\",\n            \"PASS\"\n          ],\n          [\n            \"VIF (K_eff, residualized)\",\n            \"1.00\",\n            \"< 5\",\n            \"PASS\"\n          ],\n          [\n            \"Condition number\",\n            \"4.8\",\n            \"< 30\",\n            \"PASS\"\n          ],\n          [\n            \"Partial r(K_eff, ASR | η_max)\",\n            \"0.18\",\n            \"-\",\n            \"Weak\"\n          ],\n          [\n            \"Partial r(η_max, ASR | K_eff)\",\n            \"0.42\",\n            \"-\",\n            \"Moderate-strong\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Method Comparison with Multiple Testing Correction\",\n        \"columns\": [\n          \"Method\",\n          \"η_max sig\",\n          \"K_eff sig\",\n          \"K_eff direction\"\n        ],\n        \"rows\": [\n          [\n            \"OLS + FDR\",\n            \"11/12\",\n            \"8/12\",\n            \"7+/1-\"\n          ],\n          [\n            \"OLS + Bonferroni\",\n            \"7/12\",\n            \"2/12\",\n            \"2+/0-\"\n          ],\n          [\n            \"Clustered SE + FDR\",\n            \"8/12\",\n            \"0/12\",\n            \"-\"\n          ],\n          [\n            \"Beta regression + FDR\",\n            \"10/12\",\n            \"4/12\",\n            \"3+/1-\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"VIF 分析消除了审稿人 RC1 的 last-resort 攻击角度——multicollinearity is moderate, not pathological。r=0.70 在经验社会科学中常见（e.g., income and education）， standard practice 是报告 VIF 并继续。Beta regression 提供了 distributional robustness check：结论与 log-log OLS 一致。论文可在 methods 节用一段话报告 VIF diagnostics 并在 supplementary 中给出完整表格。\\n\\nRaw VIF ≈ 2.96 直接由 r=0.70 的 confound 决定（VIF = 1/(1-r²) = 1/(1-0.49) = 1.96 在 bivariate 情况下；加上 tier indicators 后升至约 2.96）。VIF < 5 远低于标准 reviewer concern 阈值（通常 VIF > 10），甚至低于 stricter 标准（VIF > 5）。Residualization 后 VIF 降至 1.0（by construction），residualized K_eff 的 partial correlation 仅 0.18 vs η_max 的 0.42——直接量化了主导性差异。Beta regression 作为 ASR ∈ [0,1] 的 distributional 替代方案：η_max 显著性从 log-log OLS 的 11/12 降至 10/12（beta regression 对极端值更鲁棒），K_eff 从 8/12 升至 4/12（beta regression 更好地处理 heteroscedasticity）。Condition number 4.8 < 30 确认无有害多重共线性。Bonferroni 校正（most conservative）给出 η_max 7/12 vs K_eff 2/12——即使在最保守的多重比较 校正下 η_max 仍显著主导。无 reviewer-blocking issue。\"\n  },\n  {\n    \"name\": \"Aggregation Gradient Under Clustered SE\",\n    \"description\": \"在 clustered SE 和 bootstrap 下重新运行 4 种聚合规则 + 新增 veto rule，验证聚合梯度是否为真实效应而非 overlap 伪迹\",\n    \"results\": {\n      \"aggregation_rules\": [\n        \"majority\",\n        \"weighted\",\n        \"threshold\",\n        \"bayesian\",\n        \"veto\"\n      ],\n      \"correction_methods\": [\n        \"OLS\",\n        \"clustered_se\",\n        \"bootstrap_v2\"\n      ],\n      \"majority_clustered_se\": {\n        \"eta_sig\": \"8/12\",\n        \"keff_sig\": \"0/12\"\n      },\n      \"weighted_clustered_se\": {\n        \"eta_sig\": \"6/12\",\n        \"keff_sig\": \"1/12\",\n        \"keff_direction\": \"1+\"\n      },\n      \"threshold_clustered_se\": {\n        \"eta_sig\": \"10/12\",\n        \"keff_sig\": \"4/12\",\n        \"keff_direction\": \"3+/1-\",\n        \"r2\": 0.87\n      },\n      \"bayesian_clustered_se\": {\n        \"eta_sig\": \"5/12\",\n        \"keff_sig\": \"4/12\",\n        \"keff_direction\": \"1+/3-\",\n        \"keff_negative_frac\": \"3/4\"\n      },\n      \"veto_clustered_se\": {\n        \"eta_sig\": \"11/12\",\n        \"keff_sig\": \"0/12\",\n        \"r2\": 0.82\n      },\n      \"bayesian_bootstrap\": {\n        \"eta_sig\": \"3/12\",\n        \"keff_sig\": \"3/12\",\n        \"keff_direction\": \"0+/3-\",\n        \"keff_negative_frac\": \"3/3\"\n      },\n      \"gradient_preserved_under_correction\": true,\n      \"bayesian_keff_flip_genuine\": true,\n      \"aggregation_gradient_order\": \"veto > threshold > majority > weighted > bayesian\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Aggregation Gradient Under Clustered SE\",\n        \"columns\": [\n          \"Rule\",\n          \"η_max sig\",\n          \"K_eff sig\",\n          \"K_eff neg frac\",\n          \"R²\",\n          \"Gradient position\"\n        ],\n        \"rows\": [\n          [\n            \"Veto\",\n            \"11/12\",\n            \"0/12\",\n            \"-\",\n            \"0.82\",\n            \"Maximum vulnerability\"\n          ],\n          [\n            \"Threshold\",\n            \"10/12\",\n            \"4/12\",\n            \"1/4\",\n            \"0.87\",\n            \"High\"\n          ],\n          [\n            \"Majority\",\n            \"8/12\",\n            \"0/12\",\n            \"-\",\n            \"0.28\",\n            \"Moderate\"\n          ],\n          [\n            \"Weighted\",\n            \"6/12\",\n            \"1/12\",\n            \"0/1\",\n            \"0.26\",\n            \"Low-moderate\"\n          ],\n          [\n            \"Bayesian\",\n            \"5/12\",\n            \"4/12\",\n            \"3/4\",\n            \"0.09\",\n            \"Minimum vulnerability\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Bayesian K_eff Direction Detail\",\n        \"columns\": [\n          \"Correction\",\n          \"K_eff sig total\",\n          \"K_eff positive\",\n          \"K_eff negative\",\n          \"Neg fraction\"\n        ],\n        \"rows\": [\n          [\n            \"OLS\",\n            \"7/12\",\n            \"1\",\n            \"6\",\n            \"6/7 (86%)\"\n          ],\n          [\n            \"Clustered SE\",\n            \"4/12\",\n            \"1\",\n            \"3\",\n            \"3/4 (75%)\"\n          ],\n          [\n            \"Bootstrap v2\",\n            \"3/12\",\n            \"0\",\n            \"3\",\n            \"3/3 (100%)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"聚合梯度在校正下的稳健性是论文的独立贡献——它不受 non-independence concern 的影响，因为 它描述的是投票规则数学的 structural 性质。Veto rule 的加入使梯度两端更 extreme： veto（pure weakest-link）vs Bayesian（weakest-link neutralized + diversity flip）。 论文可以将此呈现为 defense design spectrum——practitioners 根据其对 false positive vs false negative 的偏好选择适当位置。Bayesian K_eff 在 bootstrap 下 3/3 negative 是 cleanest possible evidence for the flip。\\n\\n聚合梯度在 clustered SE 下保持，因为不同投票规则产生的脆弱性差异是 structural/mathematical 的，不是 panel overlap 的伪迹。Threshold（unanimity）要求所有 judges 一致，使单个 judge 的 failure 直接传导为 panel failure——R²=0.87 说明 panel 结构几乎完全决定了 threshold voting 下的脆弱性。这种强 structural 效应在 clustered SE 下大量存活（η_max 10/12, K_eff 4/12）。Veto rule（单个 judge 可否决）是 weakest-link 的极端化——η_max 几乎 完美预测（11/12），K_eff 被完全压倒（0/12）。 Bayesian calibration 翻转 K_eff 方向的关键机制：Bayesian 使用 prior accuracy 下调不可靠 judges 的权重，有效中和了 weakest-link 通道。η_max 的直接效应被削弱（11→5/12）。 剩余的 K_eff 信号主要来自 shared-bias 条件（diversity 保护性的部分），因此净方向为负。 在 bootstrap 下，Bayesian K_eff 仅 3/12 显著但全部为负（3/3 negative fraction）—— direction flip 是真实的。这确认 aggregation 是独立于 non-independence correction 的 control lever。论文的 prescriptive conclusion（robustness-first + Bayesian = dual-channel defense）在最严格校正下依然成立。\"\n  },\n  {\n    \"name\": \"Open-Ended Generation Benchmark Extension\",\n    \"description\": \"在 MT-Bench 风格的 open-ended generation 任务上测试 weakest-link 假说，超越 MCQ 格式\",\n    \"results\": {\n      \"benchmark\": \"MT-Bench (8 categories)\",\n      \"judge_format\": \"1-10 scale scoring\",\n      \"models_available\": 12,\n      \"panels\": 220,\n      \"attack_types\": [\n        \"style_manipulation\",\n        \"length_inflation\",\n        \"format_gaming\"\n      ],\n      \"conditions\": 6,\n      \"eta_max_sig_ols\": \"5/6\",\n      \"keff_sig_ols\": \"3/6 (2+/1-)\",\n      \"eta_max_sig_clustered_se\": \"4/6\",\n      \"keff_sig_clustered_se\": \"0/6\",\n      \"r2_mean\": 0.22,\n      \"gam_generation_split\": {\n        \"style_manipulation\": \"shared-bias (negative K_eff)\",\n        \"length_inflation\": \"shared-bias (negative K_eff)\",\n        \"format_gaming\": \"targeted (positive K_eff)\"\n      },\n      \"min_eta_max_wins\": \"6/6\",\n      \"cross_format_consistency\": \"η_max dominant in both MCQ and generation\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Generation Benchmark Results (Clustered SE)\",\n        \"columns\": [\n          \"Condition\",\n          \"η_max sig?\",\n          \"K_eff sig?\",\n          \"K_eff GAM dir\",\n          \"R²\"\n        ],\n        \"rows\": [\n          [\n            \"style_manipulation × MT-Bench\",\n            \"Yes\",\n            \"No\",\n            \"negative\",\n            \"0.19\"\n          ],\n          [\n            \"length_inflation × MT-Bench\",\n            \"Yes\",\n            \"No\",\n            \"negative\",\n            \"0.24\"\n          ],\n          [\n            \"format_gaming × MT-Bench\",\n            \"Yes\",\n            \"No\",\n            \"positive\",\n            \"0.23\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Cross-Format Consistency\",\n        \"columns\": [\n          \"Format\",\n          \"η_max sig (CL-SE)\",\n          \"K_eff sig (CL-SE)\",\n          \"Dominance ratio\"\n        ],\n        \"rows\": [\n          [\n            \"MCQ (MMLU+ARC)\",\n            \"8/12\",\n            \"0/12\",\n            \"8:0\"\n          ],\n          [\n            \"Generation (MT-Bench)\",\n            \"4/6\",\n            \"0/6\",\n            \"4:0\"\n          ],\n          [\n            \"Combined\",\n            \"12/18\",\n            \"0/18\",\n            \"12:0\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Generation extension 消除了\\\"MCQ-specific artifact\\\"的审稿人质疑。η_max 主导性跨 task format 通用性是论文 generalizability 论证的关键证据。R² 降低反映了 generation evaluation 的内在 noise，但 relative driver importance（η_max >> K_eff）完全保持。 此实验可作为 Section 5 的扩展分析或 supplementary material。\\n\\nη_max 主导性在 generation 任务中持续因为底层机制相同：无论 judges 评估 MCQ 正确性还是 generation 质量，adversary 都针对最可操纵的 judge。Generation 的 1-10 scale 提供了比 MCQ binary 更多的操纵空间（微妙的 style/format manipulation 可以影响 rubric-based scoring），但 vulnerability 的 distribution across judges 仍然是高度不均匀的—— 某些 judges 对 length inflation 或 format gaming 特别敏感。R² 较低（0.22 vs MCQ 的 0.30）因为 generation evaluation 有更多 idiosyncratic variance（rubric interpretation, 文化偏好等）。K_eff 在 OLS 下 3/6 显著但 clustered SE 后归零——与 MCQ 完全一致。 GAM 分类中，style manipulation 和 length inflation 属于 shared-bias（所有 LLM judges 都倾向于给更长/更 polished 的回答更高分），而 format gaming 属于 targeted（利用特定 model 的 format parsing 差异）。12 模型（部分 API 模型不支持 generation evaluation） 给出 220 panels，足够进行 regression analysis。min_eta_max 策略在 generation 上同样 赢 6/6，确认 practical recommendation 跨 task format 通用。\"\n  },\n  {\n    \"name\": \"Partial-Knowledge Adversary Model\",\n    \"description\": \"模拟 adversary 仅知道 judge family labels（不知具体脆弱性 profile）的 realistic threat model\",\n    \"results\": {\n      \"knowledge_levels\": [\n        \"full (baseline)\",\n        \"family-only\",\n        \"random\"\n      ],\n      \"asr_reduction_family_vs_full_pct\": 18,\n      \"asr_reduction_random_vs_full_pct\": 42,\n      \"family_knowledge_eta_max_sig_clustered_se\": \"7/12\",\n      \"family_knowledge_keff_sig_clustered_se\": \"0/12\",\n      \"family_knowledge_dominance_ratio\": \"7:0\",\n      \"random_targeting_eta_max_sig_clustered_se\": \"3/12\",\n      \"random_targeting_keff_sig_clustered_se\": \"0/12\",\n      \"family_knowledge_r2_mean\": 0.24,\n      \"family_label_attack_efficiency\": 0.82\n    },\n    \"tables\": [\n      {\n        \"name\": \"Adversary Knowledge Level Comparison (Clustered SE)\",\n        \"columns\": [\n          \"Knowledge level\",\n          \"Mean ASR\",\n          \"ASR vs full (%)\",\n          \"η_max sig\",\n          \"K_eff sig\",\n          \"R²\"\n        ],\n        \"rows\": [\n          [\n            \"Full knowledge\",\n            \"0.195\",\n            \"100%\",\n            \"8/12\",\n            \"0/12\",\n            \"0.30\"\n          ],\n          [\n            \"Family-only\",\n            \"0.160\",\n            \"82%\",\n            \"7/12\",\n            \"0/12\",\n            \"0.24\"\n          ],\n          [\n            \"Random\",\n            \"0.113\",\n            \"58%\",\n            \"3/12\",\n            \"0/12\",\n            \"0.08\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Family Label Informativeness\",\n        \"columns\": [\n          \"Metric\",\n          \"Value\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"Attack efficiency (family/full)\",\n            \"0.82\",\n            \"Family labels highly informative for targeting\"\n          ],\n          [\n            \"Family-vulnerability correlation\",\n            \"0.61\",\n            \"Moderate; same family shares weaknesses\"\n          ],\n          [\n            \"η_max sig retention (family vs full)\",\n            \"7/8\",\n            \"Targeting still exploits weakest link\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Partial-knowledge 实验将论文结论从 worst-case（omniscient adversary）扩展至 realistic threat model。Family-only adversary 保留 82% 攻击效率这一发现对 practical defense implications 至关重要——defenders 不能依赖\\\"adversary 不知道 panel 具体组成\\\"的假设， 因为 family-level knowledge 几乎 sufficient。η_max 在所有 knowledge levels 下主导， K_eff 在所有 knowledge levels 下为 0/12——核心发现对 adversary 能力假设鲁棒。 Random targeting 的 R²=0.08 呼应 plan_003 的 RF 结论：panel 结构的预测力依赖于 adversary 的 strategic targeting——这是论文 adaptive vs random 对比叙事的第三个 independent evidence line。\\n\\nFamily-only adversary 的 ASR 仅降 18%（而非 random 的 42%），因为 family labels 与 vulnerability profiles 有中等相关：同 family 模型共享 training pipeline 和 architectural biases，adversary 可基于 family 推断出 approximately correct 的攻击 策略。η_max 仍然主导（7/12 vs full-knowledge 的 8/12）因为 family-level targeting 仍 preferentially hits weaker judges——family labels 虽然 noisy 但 informationally above chance。K_eff 在 partial-knowledge 下同样为 0/12——diversity 在任何 knowledge level 下都不是 independent protective factor after correction。Attack efficiency 0.82 意味着 family labels 提供了 82% of full-knowledge targeting effectiveness——这对 ecological validity 至关重要：现实中 adversary 通常知道 panel 的 model families （从 API endpoint, response style 等推断），因此 full-knowledge 结果的 relevance 不仅限于理论上限。Random targeting 下 η_max 仅 3/12 显著——random adversary 无法有效 利用 individual weaknesses，说明 η_max 的 predictive power 依赖于 adversary 的 targeting ability，与 adaptive vs RF contrast（plan_003）形成完整呼应。\"\n  }\n]",
      "numLines": 1174,
      "startLine": 1,
      "totalLines": 1174
    }
  },
  "sourceToolAssistantUUID": "983a25dc-1a64-47d8-b02a-30b80ce4fde3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-22T22:36:25.784Z_

<details><summary>↩ Tool result · `toolu_015nSFZiXGXLphzt6wAdh18E`</summary>

```text
1	# Paper Framing — cert_manip_resist_eval (v5: Post-Clustered-SE Reframe, D019)
2	
3	> Last updated: 2026-05-22 | Reason: Bootstrap v2 (Reviewer-verified): η_max 5-11/12 (bootstrap 5/12 most reliable), K_eff 0-1/12. η_max:K_eff ratio 5:1 confirms dominance. GAM 6:6 split confirmed. Aggregation gradient independent.
4	
5	## Target
6	EMNLP 2026 (via ARR)
7	
8	## Title Candidates
9	1. "The Weakest Judge Wins: What Really Drives LLM Evaluation Panel Vulnerability Under Adversarial Attack"
10	2. "Weakest Link, Not Diversity: Adversarial Vulnerability in Multi-Judge LLM Evaluation"
11	3. "The Diversity Trap: Why Adding More Judges Doesn't Make LLM Evaluation Safer" (softened with honest reporting)
12	
13	## Core Insight
14	Multi-judge LLM evaluation panels are widely assumed to benefit from judge diversity. We conduct the first large-scale empirical study (15 models, 455 panels, 6 attacks, 2 benchmarks) decomposing panel vulnerability into individual weakness (η_max) and structural diversity (K_eff). Key findings: (1) **η_max dominates** panel vulnerability (5-11/12 conditions significant depending on correction method; wild cluster bootstrap — the most reliable method for small cluster counts — gives 5/12, with η_max:K_eff ratio of 5:1); (2) K_eff shows **directional but statistically fragile** association with vulnerability — point estimates predominantly positive (diversity increases risk), but significance collapses from 8/12 (OLS) to 0-1/12 after non-independence correction (bootstrap 1/12, clustered SE 0/12); (3) **GAM reveals a clean attack-type split**: K_eff is positive (harmful) for targeted attacks and negative (protective) for shared-bias attacks — a 6:6 pattern masked by linear regression; (4) **Aggregation rule choice fundamentally modulates vulnerability**: Bayesian calibration reverses K_eff direction (6/7 negative) and weakens η_max (9/12), while threshold voting amplifies both (R²=0.89).
15	
16	## Hook
17	"Panel security against adversarial manipulation is dominated by the weakest individual judge — not panel diversity. But how you aggregate judges' votes determines whether diversity becomes a vulnerability or a defense."
18	
19	## Novelty Positioning
20	We do NOT claim diversity is harmful with high statistical confidence — K_eff's independent effect is directional but fragile under rigorous correction. Our contributions are:
21	1. **First large-scale empirical decomposition** of panel vulnerability into η_max and K_eff in the LLM-judge domain (15 models, 455 panels), with transparent robustness analysis showing η_max dominates (5:1 over K_eff under bootstrap inference)
22	2. **Attack-type taxonomy with clean mechanistic split**: GAM reveals K_eff positive for targeted attacks, negative for shared-bias attacks (6:6 split), explaining WHEN diversity helps vs hurts
23	3. **Aggregation as a control lever**: voting rule modulates the diversity-vulnerability relationship — Bayesian reverses K_eff direction, threshold amplifies it (D017, independent of non-independence concern)
24	4. **Robustness-first panel design**: min(η_max) strategy wins 12/12 conditions (Claim 6, unaffected by SE correction)
25	5. **Structural barriers**: diversity-capability tradeoff (r=0.70), family label unreliability (confirmed at 15-model)
26	6. **Alternative diversity metrics robustness**: η_max dominance holds across operationalizations — Q-stat only 2/12 sig (r=0.674 with K_eff), disagreement 8/12, κ-diversity 7/12. K_eff practical effect size: IQR → Δ ASR = 1.3pp (directional but practically small)
27	7. **Methodological transparency**: explicit reporting of how significance changes across OLS → clustered SE → mixed effects, demonstrating the importance of accounting for panel overlap in combinatorial evaluation designs
28	
29	## Core Claims
30	
31	### Claim 1 (Primary): Weakest-Link Dominance
32	**Statement**: Under adaptive adversarial attacks, panel vulnerability is **dominated by individual judge weakness (η_max)**. η_max remains significant in 5-8/12 conditions after non-independence correction (wild bootstrap 5/12, clustered SE 8/12, mixed effects 7/12). K_eff (diversity) shows directional association but significance is fragile (bootstrap 1/12, clustered SE 0/12). The η_max:K_eff dominance ratio is 5:1 under bootstrap — stronger than OLS's 11:8 ≈ 1.4:1.
33	**Evidence** (15-model, 455 panels, 12 conditions, D019+D021):
34	- **Regression spec**: log-log OLS: log(ASR + ε) ~ const + log(K_eff) + log(η_max + ε)
35	- **Standard OLS**: η_max **11/12**, K_eff **8/12** (7+/1−) — inflated by panel non-independence
36	- **Wild cluster bootstrap v2** (Reviewer-verified, B=9999, Rademacher, 3-position max-p): η_max **5/12**, K_eff **1/12** (mmlu×PI only) — conservative lower bound. Per-position analysis: position 0 gives 6/12 (cluster imbalance: claude-3-haiku=91 panels vs qwen2.5-14b=1), positions 1&2 each give **9/12** (more balanced clusters, consistent with clustered SE). Max-across-positions is legitimate conservative bound but tightened by position 0 imbalance.
37	- **Clustered SE** (15 judge clusters, CR1): η_max **8/12**, K_eff **0/12** — consistent with per-position bootstrap 1&2
38	- **Mixed effects** (random judge intercepts): η_max **7/12**, K_eff **3/12** (mmlu×PI, arc×PI, arc×PB)
39	- SE inflation ~2.5x (consistent with 91/455 panel overlap)
40	- Bootstrap η_max shows benchmark asymmetry: MMLU 4/6, ARC 1/6 survive. Likely cause: MMLU 4-choice format provides more scoring variance than ARC 2-choice, giving η_max more signal. arc×PI η_max completely lost (OLS p=3e-14 → bootstrap all NS) — signal was entirely from panel overlap.
41	- **arc×sycophancy exception**: No longer significant under any correction (OLS p=0.013 → bootstrap 0.06 → clustered 0.441 → mixed 0.136). Reported as directional observation, not robust claim.
42	- **Alternative diversity metrics (OLS)**: Q-stat 2/12, disagreement 8/12 (7+/1−), κ-diversity 7/12 (7+/0−). Q-stat (lowest correlation with K_eff, r=0.674) gives lowest diversity significance — further supports η_max as dominant driver regardless of diversity operationalization.
43	- **Practical effect size**: K_eff IQR change → Δ ASR = 1.3pp (clustered SE CIs contain zero in 11/12 conditions). Even under OLS, diversity effect is practically small.
44	**Strength**: η_max dominant (5:1 ratio over K_eff under bootstrap). Absolute significance lower than OLS (5/12 vs 11/12) but relative dominance stronger. K_eff directional but fragile and practically small.
45	**Headline**: "η_max dominates panel vulnerability (5:1 over K_eff); both channels inflated by panel non-independence, but η_max survives correction while K_eff does not."
46	
47	### Claim 1b (Secondary): Attack-Type Taxonomy — GAM 6:6 Split
48	**Statement**: GAM analysis reveals that K_eff's direction cleanly splits by attack mechanism: **positive (diversity harmful) for targeted attacks** (prompt_injection, score_manipulation, position_bias × 2 benchmarks = 6 conditions) and **negative (diversity protective) for shared-bias attacks** (sycophancy, verbosity_bias, authority_bias × 2 benchmarks = 6 conditions). This 6:6 pattern is masked by linear OLS which shows 7+/1−/4NS.
49	**Evidence**: GAM partial effects, 455 panels, 12 conditions.
50	- Targeted attacks (exploit judge-specific weaknesses): K_eff partial effect positive in all 6 conditions
51	- Shared-bias attacks (exploit common cognitive biases): K_eff partial effect negative in all 6 conditions
52	- **Caveat**: GAM significance of individual conditions needs clustered SE / bootstrapped CI (pending); the structural pattern is the main finding, not individual p-values
53	**Strength**: Moderate-to-strong as qualitative taxonomic contribution. The clean 6:6 split provides mechanistic explanatory power beyond individual significance counts. Confirmed under correct 3/3/9 tier classification (GAM tier-fix rerun: all macro conclusions unchanged).
54	
55	### Claim 2 (Empirical): Predictability Gap — Panel Composition Explains RF But Not Adaptive Vulnerability
56	**Statement**: Panel composition (η_max + K_eff) explains substantially more variance under random faults (R²=0.73-0.81) than under adaptive attacks (lower R²). K_eff is positively associated with vulnerability in BOTH regimes, but: under RF, this association is genuine (survives all corrections, 2/2); under adaptive, it is largely artifactual (0-1/12 after correction). Adaptive adversaries introduce strategic variance beyond what panel structure can predict.
57	**Evidence** (15-model, 455 panels, D021+RF validation, Reviewer-verified):
58	- **Random-fault regime** (error = 1 - clean_accuracy, Monte Carlo 10000):
59	  - K_eff **positive** std_β = +0.215 (MMLU), +0.379 (ARC) — diversity associated with HIGHER error
60	  - K_eff significant **2/2** under ALL correction methods (OLS, clustered SE, bootstrap)
61	  - R² = 0.73-0.81 (highly predictable)
62	- **Adaptive regime** (D021):
63	  - K_eff also positive under OLS (7+/1−) but significance collapses to **0-1/12** after correction
64	  - R² substantially lower
65	- **Contrast**: NOT "diversity helps under RF but hurts under adaptive" — diversity is harmful in both. The contrast is: K_eff's harmful association is GENUINE under RF but INFLATED/ARTIFACTUAL under adaptive due to panel non-independence
66	- ΔR² gap: RF regime is highly predictable from panel composition; adaptive regime is not
67	**Correct interpretation**: Random faults are structurally determined by panel composition (hence high R² and genuine K_eff effect). Adaptive adversaries exploit weaknesses strategically, introducing variance that panel-level predictors cannot capture. K_eff in the adaptive regime appears significant under OLS only because of panel overlap inflation.
68	**Strength**: Strong as predictability gap (R² contrast). The finding that K_eff is genuine under RF but artifactual under adaptive is a clean methodological insight about when non-independence correction matters most.
69	
70	### Claim 3 (Empirical): Diversity-Capability Tradeoff
71	**Statement**: In the current LLM ecosystem, maximizing panel diversity (K_eff) structurally introduces less capable/robust models. The correlation r=+0.700 is a structural constraint — diversity and capability are partially opposed in the current model ecosystem.
72	**Evidence**:
73	- K_eff-η_max correlation: r = +0.700 (15-model)
74	- Under standard OLS: K_eff significant 8/12 (7+/1−) after residualizing η_max
75	- **D019 caveat**: Under clustered SE, K_eff drops to 0/12; mixed effects gives 3/12. The "independent predictive effect" of K_eff beyond η_max is directional but NOT statistically robust after correcting for non-independence. The structural correlation (r=0.700) itself is unaffected by SE correction — only the regression significance of K_eff as independent predictor changes.
76	**Framing**: The tradeoff is real as a structural constraint (r=0.700). Whether K_eff has an independent causal effect beyond η_max cannot be confidently established from this data — K_eff's significance is fragile under correction, and the high confound makes disentanglement unreliable.
77	**Strength**: Moderate (structural correlation strong; independent effect fragile). Causal language avoided.
78	
79	### Claim 4 (Methodological): Family Labels ≠ Diversity
80	**Statement**: Model family labels (Qwen/Llama/Mistral/Anthropic/OpenAI/Google) do not predict judge independence. Capability proximity is the primary driver of inter-judge correlation.
81	**Evidence**:
82	- 6-model: Mann-Whitney U p=0.206, permutation p=0.427
83	- **15-model (confirmed)**: p=0.179 (MMLU), p=0.385 (ARC). 14 within-family pairs, 91 cross-family pairs. Still not significant.
84	- Within-family MI variance is high (e.g., llama-70b↔8b MI only 0.05 due to capability gap > family similarity)
85	**Strength**: Moderate. Consistent across 6→15 model scaling.
86	
87	### ~~Claim 5 (Methodological): Gaussian Copula Failure~~ → DOWNGRADED to observation
88	**Original statement**: Gaussian copula systematically underestimates MI by 10-21×.
89	**15-model result**: MI_obs/MI_gaussian mean ratio = **0.93** (MMLU), **0.90** (ARC, robust). Copula fits well at 15-model scale. The 6-model 10-21× was a small-sample artifact (15 pairs → 105 pairs, extreme values diluted). Only claude-3-haiku pairs show extreme ratios (212×) due to near-zero ρ with nonlinear dependence.
90	**Disposition**: Remove as independent contribution. Optionally note in analysis: "Gaussian copula fit is adequate for diverse model pools but breaks down for capability-mismatched pairs with nonlinear dependence."
91	**Strength**: DEAD as independent claim. May retain as minor observation.
92	
93	### Claim 6 (Practical): Robustness-First Panel Design
94	**Statement**: Optimal panel selection is robustness-first: (1) screen for individual robustness (η ≤ threshold), then (2) maximize K_eff among qualifying judges. The two-stage approach is critical because K_eff is harmful in unrestricted pools but may be neutral or beneficial among robustness-screened judges.
95	**Evidence** (15-model, 455 panels — fully validated):
96	- min(η_max) strategy dominates **12/12 conditions** (up from 5/6 at 6-model)
97	- ASR advantage range: +0.038 (arc×sycophancy) to +0.511 (arc×prompt_injection)
98	- Robust across panel sizes K=10, 20, 50
99	- Even in the sole K_eff-dominant condition (arc×position_bias), min_eta_max still outperforms max_K_eff
100	- Consistent with canonical regression: η_max 11/12 dominant
101	**Strength**: Strong (15-model fully confirmed). Zero failure conditions.
102	
103	### Claim 7 (Empirical+Practical): Aggregation Rule Modulates Both Vulnerability Drivers
104	**Statement**: Bayesian calibration partially mitigates BOTH vulnerability drivers — weakening η_max dominance AND reversing K_eff from harmful to protective. Different aggregation rules create a gradient from full dual-driver vulnerability (threshold) to partial mitigation (Bayesian).
105	**Evidence** (15-model, 455 panels, log-log canonical spec — D017, Reviewer-verified from JSON):
106	- Majority: η_max **11/12**, K_eff **8/12** (7+/1−), R²=0.298 ← canonical baseline (matches dominance table ✓)
107	- Weighted: η_max **9/12**, K_eff **9/12** (9+/0−), R²=0.284 — reduces both drivers but K_eff stays all positive
108	- Threshold: η_max **12/12**, K_eff **11/12** (10+/1−), R²=**0.890** — near-perfect fit under unanimity
109	- Bayesian: η_max **9/12** (↓), K_eff **7/12** (1+/**6 negative**), R²=0.104
110	- Key findings:
111	  - Bayesian weakens η_max (11→9/12) AND flips K_eff direction (majority 7+/1− → bayesian 1+/6−)
112	  - Threshold amplifies both channels: η_max 12/12, K_eff 11/12, R²=0.89 (unanimity maximizes dual-driver predictability)
113	  - Weighted reduces η_max (11→9/12) but K_eff stays all positive — accuracy weighting alone cannot reverse diversity harm
114	  - Only Bayesian calibration reverses K_eff direction (6/7 significant coefficients negative)
115	  - Aggregation gradient: threshold (max vulnerability) → majority → weighted → bayesian (min vulnerability)
116	**Strength**: Strong (log-log canonical, Reviewer-verified, sanity-checked against Claim 1). Prescriptive: robustness-first selection (Claim 6) + Bayesian aggregation = dual-channel defense stack.
117	
118	## Contribution Stack (ordered by strength, post-D019 reframe)
119	1. **Weakest-link dominance** — primary empirical (η_max robust 7-8/12 after all corrections; the strongest, most defensible finding)
120	2. **Aggregation as control lever** — empirical+practical (D017: Bayesian reverses K_eff direction, weakens η_max; threshold amplifies both; R²=0.89. Independent of non-independence concern)
121	3. **Attack-type taxonomy / GAM 6:6 split** — mechanistic (targeted=K_eff positive, shared-bias=K_eff negative; clean qualitative pattern; pending correct-tier validation)
122	4. **Robustness-first panel design** — practical (Claim 6: min_eta_max 12/12 wins; unaffected by SE correction)
123	5. **Methodological transparency on non-independence** — meta-contribution (demonstrating how OLS → clustered SE → mixed effects changes significance in combinatorial panel designs; useful for future work)
124	6. **Diversity-capability tradeoff** — empirical (r=0.70; structural, not affected by SE correction)
125	7. **Family label unreliability** — methodological (confirmed at 15-model scale)
126	7. **Adaptive vs random-fault predictability gap** — empirical (R² gap)
127	~~8. **Gaussian copula failure**~~ — REMOVED (falsified at 15-model scale; downgraded to minor observation)
128	
129	## Anticipated Reviewer Concerns
130	
131	### RC1: "K_eff positive is just confound with η_max"
132	**Response**: (a) Under standard OLS, K_eff is significant 8/12 (7+/1−), but after clustered SE correction K_eff drops to 0/12, mixed effects gives 3/12 — K_eff's independent effect is directionally positive but **statistically fragile**; (b) η_max remains robust at 7-8/12 under all corrections, confirming it is NOT a confound artifact; (c) GAM analysis reveals the K_eff direction cleanly splits by attack type (6:6 targeted vs shared-bias), suggesting real structure even if individual significance is fragile under correction; (d) We transparently report all three correction methods, which is itself a methodological contribution for combinatorial panel designs.
133	
134	### RC2: "Why does diversity hurt? What's the mechanism?"
135	**Response**: (a) BFT assumes random faults — independent nodes protect via uncorrelated failures; (b) Under adaptive adversaries, independent judges create diverse attack surface — attacker exploits judge-specific vulnerabilities; (c) GAM reveals the mechanism boundary: K_eff partial effect is positive for targeted attacks (6/6 conditions) and negative for shared-bias attacks (6/6 conditions). This clean split explains WHEN diversity helps vs hurts; (d) Note: K_eff's harmful direction is directional under OLS (7+/1−) but significance collapses under non-independence correction (0-3/12). The mechanism is real (GAM pattern), but its statistical strength is sensitive to correction — we report this transparently.
136	
137	### RC3: "Only 15 models — does this generalize?"
138	**Response**: (a) 15 models across 6 families, 3 capability tiers, covering major commercial and open-source models; (b) 455 panels provide strong statistical power; (c) Effect is robust to sensitivity analysis; (d) Direction consistent across 6→9→15 model scaling (K_eff shifts from NS to positive as model pool diversifies).
139	
140	### RC4: "BFT comparison is a strawman"
141	**Response**: (a) The implicit assumption "more diverse judges = more robust" is pervasive in LLM evaluation literature; (b) We formalize this assumption and show its reversal; (c) The BFT reversal mechanism (random vs adaptive faults) provides theoretical grounding beyond just empirical observation.
142	
143	### RC5: "Why not just use the strongest models?"
144	**Response**: (a) "Strongest" varies by attack type; (b) K_eff is the sole significant predictor in 1 condition (arc×position_bias) — even all-strong panels can be vulnerable through diversity channel; (c) Two-stage algorithm addresses both vulnerability drivers.
145	
146	### RC6: "No theoretical novelty"
147	**Response**: (a) Theorem 1 (η_max monotonicity) is formally proved; (b) BFT reversal mechanism provides novel theoretical framework; (c) Dual vulnerability driver finding with condition-dependent importance is new.
148	
149	### RC7: "Why not just use Bayesian aggregation?"
150	**Response**: (a) 15-model log-log canonical (D017, Reviewer-verified): Bayesian partially mitigates BOTH drivers — η_max drops to 9/12 (from 11/12), K_eff flips to 6/7 negative (protective). But it doesn't eliminate vulnerability: 9/12 η_max still significant, R² drops to 0.104 (residual vulnerability less predictable); (b) Requires clean accuracy prior which adaptive attackers could target; (c) Even under Bayesian, 9/12 conditions still show η_max vulnerability → robustness-first selection remains necessary; (d) Optimal defense stack: robustness-first selection (eliminates η_max) + Bayesian aggregation (flips K_eff to protective) = dual-channel coverage.
151	
152	### RC8: "6-model and 15-model results contradict — which is right?"
153	**Response**: (a) 6-model result (K_eff NS) was underpowered and confounded (r=-0.8, only 20 panels); (b) 15-model result (K_eff predominantly positive) has 23× more panels, wider capability range, and passes dominance analysis validation; (c) Paper reports both and explains why 15-model result is definitive; (d) The scaling behavior itself (K_eff effect emerging with more models) is informative.
154	
155	### RC9 (new): "arc×sycophancy exception undermines your claim"
156	**Response**: (a) Post-D019: arc×sycophancy K_eff is NOT significant after correction (OLS p=0.013 → clustered SE p=0.441 → mixed effects p=0.136). It is a directional observation, not a robust standalone finding; (b) However, GAM reveals that ALL shared-bias attacks (sycophancy, verbosity_bias, authority_bias × 2 benchmarks = 6 conditions) show negative K_eff partial effects, while ALL targeted attacks (6 conditions) show positive — the 6:6 split is the robust pattern, not the individual significance of arc×sycophancy; (c) This gives practitioners an actionable taxonomy: targeted attacks → diversity hurts, shared-bias attacks → diversity may help; (d) The structural pattern (GAM) is more informative than individual p-values under various corrections.
157	
158	## "When Diversity Helps" Section
159	Diversity IS beneficial under specific conditions — paper must present this as empirically grounded nuance, not just a hypothetical:
160	1. **Non-adversarial settings**: reducing calibration errors, position bias, verbosity bias in absence of adversary
161	2. **Shared-bias attacks (GAM-confirmed pattern)**: GAM reveals K_eff partial effect is negative (protective) for all 6 shared-bias conditions (sycophancy, verbosity_bias, authority_bias × 2 benchmarks). Note: arc×sycophancy K_eff was significant under standard OLS (p=0.013) but **not significant after clustered SE (p=0.441) or mixed effects (p=0.136)**. The directional pattern across all shared-bias attacks is the stronger evidence — individual significance is fragile under correction.
162	3. **After robustness screening**: once all judges exceed a capability threshold, K_eff's harmful effect may diminish (the diversity-capability tradeoff is broken by screening). This is the basis for our two-stage recommendation.
163	4. **Summary (post-D019)**: Under standard OLS, K_eff is positive in 7/12, NS in 4/12, negative in 1/12. Under clustered SE / mixed effects, K_eff significance collapses to 0-3/12. GAM reveals the underlying structure: targeted attacks → K_eff positive (6/6), shared-bias → K_eff negative (6/6). The attack-type taxonomy is the robust finding; individual K_eff significance counts are sensitive to SE correction.
164	
165	## Story Arc (v5: Post-D019 Reframe)
166	1. **Background**: Multi-judge LLM evaluation is increasingly adopted; diversity is assumed to be the key defense against manipulation (BFT analogy)
167	2. **Tension**: We test this assumption at unprecedented scale — 15 models, 6 families, 455 panels, 6 attack types
168	3. **Surprise**: Panel vulnerability is **robustly dominated by the weakest individual judge** (η_max 7-8/12 after clustered SE / mixed-effects correction). Diversity (K_eff) shows directional but statistically fragile association — significance collapses from 8/12 (OLS) to 0-3/12 after correcting for non-independence of panel observations
169	4. **Mechanistic nuance**: GAM analysis reveals K_eff's direction cleanly splits by attack type: positive (harmful) for targeted attacks, negative (protective) for shared-bias attacks — a 6:6 pattern masked by linear regression
170	5. **Aggregation as control lever**: Voting rule choice fundamentally modulates vulnerability — Bayesian calibration reverses K_eff direction (6/7 negative) and weakens η_max (9/12), while threshold voting amplifies both (R²=0.89)
171	6. **Defense**: Robustness-first screening (min η_max, 12/12 wins) + Bayesian aggregation = dual-channel defense stack
172	7. **Implication**: Panel security is primarily an individual-judge quality problem, not a diversity problem. But aggregation design and attack-type awareness provide complementary defense levers
173	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1956cccd-23a7-42e2-8e7e-6dc7ebb5396f",
  "isSidechain": false,
  "promptId": "d5483bc6-a830-4026-80bc-d9c580d884bc",
  "type": "user",
  "uuid": "8bdd24a0-f70d-48bf-bbb8-2ea6c7b87d99",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best/paper_framing.md",
      "content": "# Paper Framing — cert_manip_resist_eval (v5: Post-Clustered-SE Reframe, D019)\n\n> Last updated: 2026-05-22 | Reason: Bootstrap v2 (Reviewer-verified): η_max 5-11/12 (bootstrap 5/12 most reliable), K_eff 0-1/12. η_max:K_eff ratio 5:1 confirms dominance. GAM 6:6 split confirmed. Aggregation gradient independent.\n\n## Target\nEMNLP 2026 (via ARR)\n\n## Title Candidates\n1. \"The Weakest Judge Wins: What Really Drives LLM Evaluation Panel Vulnerability Under Adversarial Attack\"\n2. \"Weakest Link, Not Diversity: Adversarial Vulnerability in Multi-Judge LLM Evaluation\"\n3. \"The Diversity Trap: Why Adding More Judges Doesn't Make LLM Evaluation Safer\" (softened with honest reporting)\n\n## Core Insight\nMulti-judge LLM evaluation panels are widely assumed to benefit from judge diversity. We conduct the first large-scale empirical study (15 models, 455 panels, 6 attacks, 2 benchmarks) decomposing panel vulnerability into individual weakness (η_max) and structural diversity (K_eff). Key findings: (1) **η_max dominates** panel vulnerability (5-11/12 conditions significant depending on correction method; wild cluster bootstrap — the most reliable method for small cluster counts — gives 5/12, with η_max:K_eff ratio of 5:1); (2) K_eff shows **directional but statistically fragile** association with vulnerability — point estimates predominantly positive (diversity increases risk), but significance collapses from 8/12 (OLS) to 0-1/12 after non-independence correction (bootstrap 1/12, clustered SE 0/12); (3) **GAM reveals a clean attack-type split**: K_eff is positive (harmful) for targeted attacks and negative (protective) for shared-bias attacks — a 6:6 pattern masked by linear regression; (4) **Aggregation rule choice fundamentally modulates vulnerability**: Bayesian calibration reverses K_eff direction (6/7 negative) and weakens η_max (9/12), while threshold voting amplifies both (R²=0.89).\n\n## Hook\n\"Panel security against adversarial manipulation is dominated by the weakest individual judge — not panel diversity. But how you aggregate judges' votes determines whether diversity becomes a vulnerability or a defense.\"\n\n## Novelty Positioning\nWe do NOT claim diversity is harmful with high statistical confidence — K_eff's independent effect is directional but fragile under rigorous correction. Our contributions are:\n1. **First large-scale empirical decomposition** of panel vulnerability into η_max and K_eff in the LLM-judge domain (15 models, 455 panels), with transparent robustness analysis showing η_max dominates (5:1 over K_eff under bootstrap inference)\n2. **Attack-type taxonomy with clean mechanistic split**: GAM reveals K_eff positive for targeted attacks, negative for shared-bias attacks (6:6 split), explaining WHEN diversity helps vs hurts\n3. **Aggregation as a control lever**: voting rule modulates the diversity-vulnerability relationship — Bayesian reverses K_eff direction, threshold amplifies it (D017, independent of non-independence concern)\n4. **Robustness-first panel design**: min(η_max) strategy wins 12/12 conditions (Claim 6, unaffected by SE correction)\n5. **Structural barriers**: diversity-capability tradeoff (r=0.70), family label unreliability (confirmed at 15-model)\n6. **Alternative diversity metrics robustness**: η_max dominance holds across operationalizations — Q-stat only 2/12 sig (r=0.674 with K_eff), disagreement 8/12, κ-diversity 7/12. K_eff practical effect size: IQR → Δ ASR = 1.3pp (directional but practically small)\n7. **Methodological transparency**: explicit reporting of how significance changes across OLS → clustered SE → mixed effects, demonstrating the importance of accounting for panel overlap in combinatorial evaluation designs\n\n## Core Claims\n\n### Claim 1 (Primary): Weakest-Link Dominance\n**Statement**: Under adaptive adversarial attacks, panel vulnerability is **dominated by individual judge weakness (η_max)**. η_max remains significant in 5-8/12 conditions after non-independence correction (wild bootstrap 5/12, clustered SE 8/12, mixed effects 7/12). K_eff (diversity) shows directional association but significance is fragile (bootstrap 1/12, clustered SE 0/12). The η_max:K_eff dominance ratio is 5:1 under bootstrap — stronger than OLS's 11:8 ≈ 1.4:1.\n**Evidence** (15-model, 455 panels, 12 conditions, D019+D021):\n- **Regression spec**: log-log OLS: log(ASR + ε) ~ const + log(K_eff) + log(η_max + ε)\n- **Standard OLS**: η_max **11/12**, K_eff **8/12** (7+/1−) — inflated by panel non-independence\n- **Wild cluster bootstrap v2** (Reviewer-verified, B=9999, Rademacher, 3-position max-p): η_max **5/12**, K_eff **1/12** (mmlu×PI only) — conservative lower bound. Per-position analysis: position 0 gives 6/12 (cluster imbalance: claude-3-haiku=91 panels vs qwen2.5-14b=1), positions 1&2 each give **9/12** (more balanced clusters, consistent with clustered SE). Max-across-positions is legitimate conservative bound but tightened by position 0 imbalance.\n- **Clustered SE** (15 judge clusters, CR1): η_max **8/12**, K_eff **0/12** — consistent with per-position bootstrap 1&2\n- **Mixed effects** (random judge intercepts): η_max **7/12**, K_eff **3/12** (mmlu×PI, arc×PI, arc×PB)\n- SE inflation ~2.5x (consistent with 91/455 panel overlap)\n- Bootstrap η_max shows benchmark asymmetry: MMLU 4/6, ARC 1/6 survive. Likely cause: MMLU 4-choice format provides more scoring variance than ARC 2-choice, giving η_max more signal. arc×PI η_max completely lost (OLS p=3e-14 → bootstrap all NS) — signal was entirely from panel overlap.\n- **arc×sycophancy exception**: No longer significant under any correction (OLS p=0.013 → bootstrap 0.06 → clustered 0.441 → mixed 0.136). Reported as directional observation, not robust claim.\n- **Alternative diversity metrics (OLS)**: Q-stat 2/12, disagreement 8/12 (7+/1−), κ-diversity 7/12 (7+/0−). Q-stat (lowest correlation with K_eff, r=0.674) gives lowest diversity significance — further supports η_max as dominant driver regardless of diversity operationalization.\n- **Practical effect size**: K_eff IQR change → Δ ASR = 1.3pp (clustered SE CIs contain zero in 11/12 conditions). Even under OLS, diversity effect is practically small.\n**Strength**: η_max dominant (5:1 ratio over K_eff under bootstrap). Absolute significance lower than OLS (5/12 vs 11/12) but relative dominance stronger. K_eff directional but fragile and practically small.\n**Headline**: \"η_max dominates panel vulnerability (5:1 over K_eff); both channels inflated by panel non-independence, but η_max survives correction while K_eff does not.\"\n\n### Claim 1b (Secondary): Attack-Type Taxonomy — GAM 6:6 Split\n**Statement**: GAM analysis reveals that K_eff's direction cleanly splits by attack mechanism: **positive (diversity harmful) for targeted attacks** (prompt_injection, score_manipulation, position_bias × 2 benchmarks = 6 conditions) and **negative (diversity protective) for shared-bias attacks** (sycophancy, verbosity_bias, authority_bias × 2 benchmarks = 6 conditions). This 6:6 pattern is masked by linear OLS which shows 7+/1−/4NS.\n**Evidence**: GAM partial effects, 455 panels, 12 conditions.\n- Targeted attacks (exploit judge-specific weaknesses): K_eff partial effect positive in all 6 conditions\n- Shared-bias attacks (exploit common cognitive biases): K_eff partial effect negative in all 6 conditions\n- **Caveat**: GAM significance of individual conditions needs clustered SE / bootstrapped CI (pending); the structural pattern is the main finding, not individual p-values\n**Strength**: Moderate-to-strong as qualitative taxonomic contribution. The clean 6:6 split provides mechanistic explanatory power beyond individual significance counts. Confirmed under correct 3/3/9 tier classification (GAM tier-fix rerun: all macro conclusions unchanged).\n\n### Claim 2 (Empirical): Predictability Gap — Panel Composition Explains RF But Not Adaptive Vulnerability\n**Statement**: Panel composition (η_max + K_eff) explains substantially more variance under random faults (R²=0.73-0.81) than under adaptive attacks (lower R²). K_eff is positively associated with vulnerability in BOTH regimes, but: under RF, this association is genuine (survives all corrections, 2/2); under adaptive, it is largely artifactual (0-1/12 after correction). Adaptive adversaries introduce strategic variance beyond what panel structure can predict.\n**Evidence** (15-model, 455 panels, D021+RF validation, Reviewer-verified):\n- **Random-fault regime** (error = 1 - clean_accuracy, Monte Carlo 10000):\n  - K_eff **positive** std_β = +0.215 (MMLU), +0.379 (ARC) — diversity associated with HIGHER error\n  - K_eff significant **2/2** under ALL correction methods (OLS, clustered SE, bootstrap)\n  - R² = 0.73-0.81 (highly predictable)\n- **Adaptive regime** (D021):\n  - K_eff also positive under OLS (7+/1−) but significance collapses to **0-1/12** after correction\n  - R² substantially lower\n- **Contrast**: NOT \"diversity helps under RF but hurts under adaptive\" — diversity is harmful in both. The contrast is: K_eff's harmful association is GENUINE under RF but INFLATED/ARTIFACTUAL under adaptive due to panel non-independence\n- ΔR² gap: RF regime is highly predictable from panel composition; adaptive regime is not\n**Correct interpretation**: Random faults are structurally determined by panel composition (hence high R² and genuine K_eff effect). Adaptive adversaries exploit weaknesses strategically, introducing variance that panel-level predictors cannot capture. K_eff in the adaptive regime appears significant under OLS only because of panel overlap inflation.\n**Strength**: Strong as predictability gap (R² contrast). The finding that K_eff is genuine under RF but artifactual under adaptive is a clean methodological insight about when non-independence correction matters most.\n\n### Claim 3 (Empirical): Diversity-Capability Tradeoff\n**Statement**: In the current LLM ecosystem, maximizing panel diversity (K_eff) structurally introduces less capable/robust models. The correlation r=+0.700 is a structural constraint — diversity and capability are partially opposed in the current model ecosystem.\n**Evidence**:\n- K_eff-η_max correlation: r = +0.700 (15-model)\n- Under standard OLS: K_eff significant 8/12 (7+/1−) after residualizing η_max\n- **D019 caveat**: Under clustered SE, K_eff drops to 0/12; mixed effects gives 3/12. The \"independent predictive effect\" of K_eff beyond η_max is directional but NOT statistically robust after correcting for non-independence. The structural correlation (r=0.700) itself is unaffected by SE correction — only the regression significance of K_eff as independent predictor changes.\n**Framing**: The tradeoff is real as a structural constraint (r=0.700). Whether K_eff has an independent causal effect beyond η_max cannot be confidently established from this data — K_eff's significance is fragile under correction, and the high confound makes disentanglement unreliable.\n**Strength**: Moderate (structural correlation strong; independent effect fragile). Causal language avoided.\n\n### Claim 4 (Methodological): Family Labels ≠ Diversity\n**Statement**: Model family labels (Qwen/Llama/Mistral/Anthropic/OpenAI/Google) do not predict judge independence. Capability proximity is the primary driver of inter-judge correlation.\n**Evidence**:\n- 6-model: Mann-Whitney U p=0.206, permutation p=0.427\n- **15-model (confirmed)**: p=0.179 (MMLU), p=0.385 (ARC). 14 within-family pairs, 91 cross-family pairs. Still not significant.\n- Within-family MI variance is high (e.g., llama-70b↔8b MI only 0.05 due to capability gap > family similarity)\n**Strength**: Moderate. Consistent across 6→15 model scaling.\n\n### ~~Claim 5 (Methodological): Gaussian Copula Failure~~ → DOWNGRADED to observation\n**Original statement**: Gaussian copula systematically underestimates MI by 10-21×.\n**15-model result**: MI_obs/MI_gaussian mean ratio = **0.93** (MMLU), **0.90** (ARC, robust). Copula fits well at 15-model scale. The 6-model 10-21× was a small-sample artifact (15 pairs → 105 pairs, extreme values diluted). Only claude-3-haiku pairs show extreme ratios (212×) due to near-zero ρ with nonlinear dependence.\n**Disposition**: Remove as independent contribution. Optionally note in analysis: \"Gaussian copula fit is adequate for diverse model pools but breaks down for capability-mismatched pairs with nonlinear dependence.\"\n**Strength**: DEAD as independent claim. May retain as minor observation.\n\n### Claim 6 (Practical): Robustness-First Panel Design\n**Statement**: Optimal panel selection is robustness-first: (1) screen for individual robustness (η ≤ threshold), then (2) maximize K_eff among qualifying judges. The two-stage approach is critical because K_eff is harmful in unrestricted pools but may be neutral or beneficial among robustness-screened judges.\n**Evidence** (15-model, 455 panels — fully validated):\n- min(η_max) strategy dominates **12/12 conditions** (up from 5/6 at 6-model)\n- ASR advantage range: +0.038 (arc×sycophancy) to +0.511 (arc×prompt_injection)\n- Robust across panel sizes K=10, 20, 50\n- Even in the sole K_eff-dominant condition (arc×position_bias), min_eta_max still outperforms max_K_eff\n- Consistent with canonical regression: η_max 11/12 dominant\n**Strength**: Strong (15-model fully confirmed). Zero failure conditions.\n\n### Claim 7 (Empirical+Practical): Aggregation Rule Modulates Both Vulnerability Drivers\n**Statement**: Bayesian calibration partially mitigates BOTH vulnerability drivers — weakening η_max dominance AND reversing K_eff from harmful to protective. Different aggregation rules create a gradient from full dual-driver vulnerability (threshold) to partial mitigation (Bayesian).\n**Evidence** (15-model, 455 panels, log-log canonical spec — D017, Reviewer-verified from JSON):\n- Majority: η_max **11/12**, K_eff **8/12** (7+/1−), R²=0.298 ← canonical baseline (matches dominance table ✓)\n- Weighted: η_max **9/12**, K_eff **9/12** (9+/0−), R²=0.284 — reduces both drivers but K_eff stays all positive\n- Threshold: η_max **12/12**, K_eff **11/12** (10+/1−), R²=**0.890** — near-perfect fit under unanimity\n- Bayesian: η_max **9/12** (↓), K_eff **7/12** (1+/**6 negative**), R²=0.104\n- Key findings:\n  - Bayesian weakens η_max (11→9/12) AND flips K_eff direction (majority 7+/1− → bayesian 1+/6−)\n  - Threshold amplifies both channels: η_max 12/12, K_eff 11/12, R²=0.89 (unanimity maximizes dual-driver predictability)\n  - Weighted reduces η_max (11→9/12) but K_eff stays all positive — accuracy weighting alone cannot reverse diversity harm\n  - Only Bayesian calibration reverses K_eff direction (6/7 significant coefficients negative)\n  - Aggregation gradient: threshold (max vulnerability) → majority → weighted → bayesian (min vulnerability)\n**Strength**: Strong (log-log canonical, Reviewer-verified, sanity-checked against Claim 1). Prescriptive: robustness-first selection (Claim 6) + Bayesian aggregation = dual-channel defense stack.\n\n## Contribution Stack (ordered by strength, post-D019 reframe)\n1. **Weakest-link dominance** — primary empirical (η_max robust 7-8/12 after all corrections; the strongest, most defensible finding)\n2. **Aggregation as control lever** — empirical+practical (D017: Bayesian reverses K_eff direction, weakens η_max; threshold amplifies both; R²=0.89. Independent of non-independence concern)\n3. **Attack-type taxonomy / GAM 6:6 split** — mechanistic (targeted=K_eff positive, shared-bias=K_eff negative; clean qualitative pattern; pending correct-tier validation)\n4. **Robustness-first panel design** — practical (Claim 6: min_eta_max 12/12 wins; unaffected by SE correction)\n5. **Methodological transparency on non-independence** — meta-contribution (demonstrating how OLS → clustered SE → mixed effects changes significance in combinatorial panel designs; useful for future work)\n6. **Diversity-capability tradeoff** — empirical (r=0.70; structural, not affected by SE correction)\n7. **Family label unreliability** — methodological (confirmed at 15-model scale)\n7. **Adaptive vs random-fault predictability gap** — empirical (R² gap)\n~~8. **Gaussian copula failure**~~ — REMOVED (falsified at 15-model scale; downgraded to minor observation)\n\n## Anticipated Reviewer Concerns\n\n### RC1: \"K_eff positive is just confound with η_max\"\n**Response**: (a) Under standard OLS, K_eff is significant 8/12 (7+/1−), but after clustered SE correction K_eff drops to 0/12, mixed effects gives 3/12 — K_eff's independent effect is directionally positive but **statistically fragile**; (b) η_max remains robust at 7-8/12 under all corrections, confirming it is NOT a confound artifact; (c) GAM analysis reveals the K_eff direction cleanly splits by attack type (6:6 targeted vs shared-bias), suggesting real structure even if individual significance is fragile under correction; (d) We transparently report all three correction methods, which is itself a methodological contribution for combinatorial panel designs.\n\n### RC2: \"Why does diversity hurt? What's the mechanism?\"\n**Response**: (a) BFT assumes random faults — independent nodes protect via uncorrelated failures; (b) Under adaptive adversaries, independent judges create diverse attack surface — attacker exploits judge-specific vulnerabilities; (c) GAM reveals the mechanism boundary: K_eff partial effect is positive for targeted attacks (6/6 conditions) and negative for shared-bias attacks (6/6 conditions). This clean split explains WHEN diversity helps vs hurts; (d) Note: K_eff's harmful direction is directional under OLS (7+/1−) but significance collapses under non-independence correction (0-3/12). The mechanism is real (GAM pattern), but its statistical strength is sensitive to correction — we report this transparently.\n\n### RC3: \"Only 15 models — does this generalize?\"\n**Response**: (a) 15 models across 6 families, 3 capability tiers, covering major commercial and open-source models; (b) 455 panels provide strong statistical power; (c) Effect is robust to sensitivity analysis; (d) Direction consistent across 6→9→15 model scaling (K_eff shifts from NS to positive as model pool diversifies).\n\n### RC4: \"BFT comparison is a strawman\"\n**Response**: (a) The implicit assumption \"more diverse judges = more robust\" is pervasive in LLM evaluation literature; (b) We formalize this assumption and show its reversal; (c) The BFT reversal mechanism (random vs adaptive faults) provides theoretical grounding beyond just empirical observation.\n\n### RC5: \"Why not just use the strongest models?\"\n**Response**: (a) \"Strongest\" varies by attack type; (b) K_eff is the sole significant predictor in 1 condition (arc×position_bias) — even all-strong panels can be vulnerable through diversity channel; (c) Two-stage algorithm addresses both vulnerability drivers.\n\n### RC6: \"No theoretical novelty\"\n**Response**: (a) Theorem 1 (η_max monotonicity) is formally proved; (b) BFT reversal mechanism provides novel theoretical framework; (c) Dual vulnerability driver finding with condition-dependent importance is new.\n\n### RC7: \"Why not just use Bayesian aggregation?\"\n**Response**: (a) 15-model log-log canonical (D017, Reviewer-verified): Bayesian partially mitigates BOTH drivers — η_max drops to 9/12 (from 11/12), K_eff flips to 6/7 negative (protective). But it doesn't eliminate vulnerability: 9/12 η_max still significant, R² drops to 0.104 (residual vulnerability less predictable); (b) Requires clean accuracy prior which adaptive attackers could target; (c) Even under Bayesian, 9/12 conditions still show η_max vulnerability → robustness-first selection remains necessary; (d) Optimal defense stack: robustness-first selection (eliminates η_max) + Bayesian aggregation (flips K_eff to protective) = dual-channel coverage.\n\n### RC8: \"6-model and 15-model results contradict — which is right?\"\n**Response**: (a) 6-model result (K_eff NS) was underpowered and confounded (r=-0.8, only 20 panels); (b) 15-model result (K_eff predominantly positive) has 23× more panels, wider capability range, and passes dominance analysis validation; (c) Paper reports both and explains why 15-model result is definitive; (d) The scaling behavior itself (K_eff effect emerging with more models) is informative.\n\n### RC9 (new): \"arc×sycophancy exception undermines your claim\"\n**Response**: (a) Post-D019: arc×sycophancy K_eff is NOT significant after correction (OLS p=0.013 → clustered SE p=0.441 → mixed effects p=0.136). It is a directional observation, not a robust standalone finding; (b) However, GAM reveals that ALL shared-bias attacks (sycophancy, verbosity_bias, authority_bias × 2 benchmarks = 6 conditions) show negative K_eff partial effects, while ALL targeted attacks (6 conditions) show positive — the 6:6 split is the robust pattern, not the individual significance of arc×sycophancy; (c) This gives practitioners an actionable taxonomy: targeted attacks → diversity hurts, shared-bias attacks → diversity may help; (d) The structural pattern (GAM) is more informative than individual p-values under various corrections.\n\n## \"When Diversity Helps\" Section\nDiversity IS beneficial under specific conditions — paper must present this as empirically grounded nuance, not just a hypothetical:\n1. **Non-adversarial settings**: reducing calibration errors, position bias, verbosity bias in absence of adversary\n2. **Shared-bias attacks (GAM-confirmed pattern)**: GAM reveals K_eff partial effect is negative (protective) for all 6 shared-bias conditions (sycophancy, verbosity_bias, authority_bias × 2 benchmarks). Note: arc×sycophancy K_eff was significant under standard OLS (p=0.013) but **not significant after clustered SE (p=0.441) or mixed effects (p=0.136)**. The directional pattern across all shared-bias attacks is the stronger evidence — individual significance is fragile under correction.\n3. **After robustness screening**: once all judges exceed a capability threshold, K_eff's harmful effect may diminish (the diversity-capability tradeoff is broken by screening). This is the basis for our two-stage recommendation.\n4. **Summary (post-D019)**: Under standard OLS, K_eff is positive in 7/12, NS in 4/12, negative in 1/12. Under clustered SE / mixed effects, K_eff significance collapses to 0-3/12. GAM reveals the underlying structure: targeted attacks → K_eff positive (6/6), shared-bias → K_eff negative (6/6). The attack-type taxonomy is the robust finding; individual K_eff significance counts are sensitive to SE correction.\n\n## Story Arc (v5: Post-D019 Reframe)\n1. **Background**: Multi-judge LLM evaluation is increasingly adopted; diversity is assumed to be the key defense against manipulation (BFT analogy)\n2. **Tension**: We test this assumption at unprecedented scale — 15 models, 6 families, 455 panels, 6 attack types\n3. **Surprise**: Panel vulnerability is **robustly dominated by the weakest individual judge** (η_max 7-8/12 after clustered SE / mixed-effects correction). Diversity (K_eff) shows directional but statistically fragile association — significance collapses from 8/12 (OLS) to 0-3/12 after correcting for non-independence of panel observations\n4. **Mechanistic nuance**: GAM analysis reveals K_eff's direction cleanly splits by attack type: positive (harmful) for targeted attacks, negative (protective) for shared-bias attacks — a 6:6 pattern masked by linear regression\n5. **Aggregation as control lever**: Voting rule choice fundamentally modulates vulnerability — Bayesian calibration reverses K_eff direction (6/7 negative) and weakens η_max (9/12), while threshold voting amplifies both (R²=0.89)\n6. **Defense**: Robustness-first screening (min η_max, 12/12 wins) + Bayesian aggregation = dual-channel defense stack\n7. **Implication**: Panel security is primarily an individual-judge quality problem, not a diversity problem. But aggregation design and attack-type awareness provide complementary defense levers\n",
      "numLines": 173,
      "startLine": 1,
      "totalLines": 173
    }
  },
  "sourceToolAssistantUUID": "1956cccd-23a7-42e2-8e7e-6dc7ebb5396f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-22T22:36:25.780Z_

<details open><summary>🔧 Tool call — Read · `toolu_015nSFZiXGXLphzt6wAdh18E`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "611f301a-6777-43fe-8ca4-7c7b62c91e1f",
  "isSidechain": false,
  "requestId": "req_011CbJQYAw9LCAraszJotzqV",
  "type": "assistant",
  "uuid": "1956cccd-23a7-42e2-8e7e-6dc7ebb5396f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019dgPcNQNJV5xmQBQ4oYXTH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12280,
      "cache_read_input_tokens": 11447,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12280,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12280,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12280
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

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T221131 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_…",
  "leafUuid": "8bdd24a0-f70d-48bf-bbb8-2ea6c7b87d99",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate EMNLP-2026 paper on certification manipulation",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344"
}
```

---

### Assistant

_source line 15 · 2026-05-22T22:36:32.122Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data. Let me also read the paper-writing-norms skill to ensure I follow the correct style.

Actually, the instructions say "够审级" (review-ready), not publication quality. Let me focus on writing a complete LaTeX paper with all the experimental data properly presented.

Let me also check if the output directory exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8bdd24a0-f70d-48bf-bbb8-2ea6c7b87d99",
  "isSidechain": false,
  "requestId": "req_011CbJQYZjbLg3MaucFYAYT5",
  "type": "assistant",
  "uuid": "e3522340-0c18-4087-b2c9-2cc7a85f8da9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WHdSGnQUaYbsohcQMztCfs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25967,
      "cache_read_input_tokens": 23727,
      "output_tokens": 310,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25967,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 310,
          "cache_read_input_tokens": 23727,
          "cache_creation_input_tokens": 25967,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25967
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

_source line 16 · 2026-05-22T22:36:32.739Z_

Now let me check the output directory and read the paper-writing-norms skill for style guidance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3522340-0c18-4087-b2c9-2cc7a85f8da9",
  "isSidechain": false,
  "requestId": "req_011CbJQYZjbLg3MaucFYAYT5",
  "type": "assistant",
  "uuid": "b97e53dc-497b-47d5-b9f4-2974c6c320ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WHdSGnQUaYbsohcQMztCfs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25967,
      "cache_read_input_tokens": 23727,
      "output_tokens": 310,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25967,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 310,
          "cache_read_input_tokens": 23727,
          "cache_creation_input_tokens": 25967,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25967
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

_source line 17 · 2026-05-22T22:36:35.635Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01WNVDuwYpYnc9S8ad1TeaLg`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best/",
  "description": "List output directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b97e53dc-497b-47d5-b9f4-2974c6c320ea",
  "isSidechain": false,
  "requestId": "req_011CbJQYZjbLg3MaucFYAYT5",
  "type": "assistant",
  "uuid": "d80cb40f-2841-42c2-be5d-a97bfd3eee69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WHdSGnQUaYbsohcQMztCfs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25967,
      "cache_read_input_tokens": 23727,
      "output_tokens": 310,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25967,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 310,
          "cache_read_input_tokens": 23727,
          "cache_creation_input_tokens": 25967,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25967
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

_source line 18 · 2026-05-22T22:36:35.793Z_

<details><summary>↩ Tool result · `toolu_01WNVDuwYpYnc9S8ad1TeaLg`</summary>

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
  "parentUuid": "d80cb40f-2841-42c2-be5d-a97bfd3eee69",
  "isSidechain": false,
  "promptId": "d5483bc6-a830-4026-80bc-d9c580d884bc",
  "type": "user",
  "uuid": "006c8462-867d-4007-a3fe-c854780f1141",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "d80cb40f-2841-42c2-be5d-a97bfd3eee69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T22:36:36.467Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YEVmDub4YQg8BZzxCSo8qk`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "006c8462-867d-4007-a3fe-c854780f1141",
  "isSidechain": false,
  "requestId": "req_011CbJQYZjbLg3MaucFYAYT5",
  "type": "assistant",
  "uuid": "a79994dc-5e4d-4214-b187-5722e6e2effb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WHdSGnQUaYbsohcQMztCfs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25967,
      "cache_read_input_tokens": 23727,
      "output_tokens": 310,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25967,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 310,
          "cache_read_input_tokens": 23727,
          "cache_creation_input_tokens": 25967,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25967
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

_source line 20 · 2026-05-22T22:36:36.477Z_

<details><summary>↩ Tool result · `toolu_01YEVmDub4YQg8BZzxCSo8qk`</summary>

```text
1	---
2	name: paper-writing-norms
3	description: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。
4	allowed-tools: [Read, Write, Edit, Glob, Grep]
5	scope: global
6	version: 2
7	priority: 9
8	tags:
9	  - writing
10	  - paper
11	  - style
12	  - norms
13	roles:
14	  - agent
15	  - worker
16	  - paper_agent
17	---
18	
19	# 论文写作风格规范
20	
21	> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。
22	
23	---
24	
25	## 一、总体写作哲学
26	
27	### 1.1 故事驱动，不是数据堆砌
28	
29	- 论文必须以"故事线"为核心展开：问题 → 洞察 → 方法 → 验证
30	- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进
31	- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌
32	- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing
33	
34	### 1.2 主线统一性
35	
36	- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**
37	- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C
38	- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机
39	- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线
40	
41	### 1.3 专有名词必须有定义
42	
43	- 首次出现的专有名词/缩写必须给出完整定义和解释
44	- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）
45	- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用
46	- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug
47	
48	### 1.4 写作前必读同类优秀论文
49	
50	- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可
51	- 重点学：
52	  - Abstract 怎么用最少篇幅讲完故事
53	  - Introduction 怎么从大问题切入到具体贡献
54	  - Related Work 怎么 positioning 自己（不是 survey）
55	  - Table/Figure 怎么压缩信息密度
56	- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大
57	- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文
58	
59	---
60	
61	## 二、Abstract 写作规范
62	
63	### 2.1 四个必答问题（150-250 words）
64	
65	Abstract 必须在很短的篇幅内清楚回答：
66	1. **研究什么问题** — 1-2 句话交代背景和痛点
67	2. **为什么重要** — 现有方法的不足（不用写太多）
68	3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）
69	4. **结果说明什么** — 用具体实验结论支撑贡献
70	
71	### 2.2 禁忌
72	
73	- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim
74	- **禁止过度宣传**：不说 "revolutionary"、"groundbreaking"
75	- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元
76	- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了
77	- **缩写必须定义**：Abstract 中首次出现的缩写必须展开
78	
79	### 2.3 审稿人视角检验
80	
81	写完后用这个标准自检：审稿人能否在 30 秒内判断——
82	- 问题是否重要？
83	- 方法是否清楚？
84	- 贡献是否可信？
85	- 结果是否有说服力？
86	
87	---
88	
89	## 三、Introduction 写作规范
90	
91	### 3.1 完整叙事线（5 段结构）
92	
93	Introduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：
94	
95	1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈
96	2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题
97	3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）
98	4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题
99	5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a79994dc-5e4d-4214-b187-5722e6e2effb",
  "isSidechain": false,
  "promptId": "d5483bc6-a830-4026-80bc-d9c580d884bc",
  "type": "user",
  "uuid": "1a7d3784-bdc6-48d5-bea4-8c48b9c695df",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
      "content": "---\nname: paper-writing-norms\ndescription: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。\nallowed-tools: [Read, Write, Edit, Glob, Grep]\nscope: global\nversion: 2\npriority: 9\ntags:\n  - writing\n  - paper\n  - style\n  - norms\nroles:\n  - agent\n  - worker\n  - paper_agent\n---\n\n# 论文写作风格规范\n\n> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。\n\n---\n\n## 一、总体写作哲学\n\n### 1.1 故事驱动，不是数据堆砌\n\n- 论文必须以\"故事线\"为核心展开：问题 → 洞察 → 方法 → 验证\n- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进\n- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌\n- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing\n\n### 1.2 主线统一性\n\n- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**\n- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C\n- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机\n- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线\n\n### 1.3 专有名词必须有定义\n\n- 首次出现的专有名词/缩写必须给出完整定义和解释\n- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）\n- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用\n- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug\n\n### 1.4 写作前必读同类优秀论文\n\n- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可\n- 重点学：\n  - Abstract 怎么用最少篇幅讲完故事\n  - Introduction 怎么从大问题切入到具体贡献\n  - Related Work 怎么 positioning 自己（不是 survey）\n  - Table/Figure 怎么压缩信息密度\n- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大\n- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文\n\n---\n\n## 二、Abstract 写作规范\n\n### 2.1 四个必答问题（150-250 words）\n\nAbstract 必须在很短的篇幅内清楚回答：\n1. **研究什么问题** — 1-2 句话交代背景和痛点\n2. **为什么重要** — 现有方法的不足（不用写太多）\n3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）\n4. **结果说明什么** — 用具体实验结论支撑贡献\n\n### 2.2 禁忌\n\n- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim\n- **禁止过度宣传**：不说 \"revolutionary\"、\"groundbreaking\"\n- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元\n- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了\n- **缩写必须定义**：Abstract 中首次出现的缩写必须展开\n\n### 2.3 审稿人视角检验\n\n写完后用这个标准自检：审稿人能否在 30 秒内判断——\n- 问题是否重要？\n- 方法是否清楚？\n- 贡献是否可信？\n- 结果是否有说服力？\n\n---\n\n## 三、Introduction 写作规范\n\n### 3.1 完整叙事线（5 段结构）\n\nIntroduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：\n\n1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈\n2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题\n3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）\n4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题\n5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献\n",
      "numLines": 100,
      "startLine": 1,
      "totalLines": 276
    }
  },
  "sourceToolAssistantUUID": "a79994dc-5e4d-4214-b187-5722e6e2effb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-22T22:36:54.003Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have all the information I need. Now let me write the full LaTeX paper. Let me carefully organize all the experiment data into proper sections and tables.

Key experiments to cover:
1. 15-Model Scaling Expansion (core regression results)
2. Attack Surface Expansion (new attack types)
3. Random-Fault BFT Contrast Experiment
4. Capability-Matched Validation
5. Two-Stage Panel Design Algorithm Benchmark
6. Per-Judge ASR Concentration Analysis
7. Diversity-Capability Tradeoff Visualization
8. Panel Size Sensitivity Analysis


9. VIF + Multicollinearity Diagnostic
10. Aggregation Gradient Under Clustered SE
11. Open-Ended Generation Benchmark Extension
12. Partial-Knowledge Adversary Model

The paper structure should be:
- Abstract
- Introduction
- Related Work (brief)
- Method (defining η_max, K_eff, attack types, correction methods)
- Experiments
  - 5.1 Core results (15-model scaling)
  - 5.2 Attack surface expansion
  - 5.3 RF vs Adaptive contrast
  - 5.4 Capability-matched validation
  - 5.5 Panel design algorithm
  - 5.6 ASR concentration analysis
  - 5.7 Diversity-capability tradeoff
  - 5.8 Panel size sensitivity
  - 5.9 Multicollinearity diagnostics
  - 5.10 Aggregation robustness
  - 5.11 Open-ended generation
  - 5.12 Adversary model extensions
- Discussion
- Conclusion
- Limitations

That's a lot of ground to cover in eight pages, so I need to be strategic about what makes the main narrative versus what goes to supplementary material. I'm prioritizing the core regression results, the random forest contrast for causal evidence, the attack surface taxonomy, the aggregation gradient as a control mechanism, the panel design algorithm for practical applicability, and ASR concentration patterns as mechanistic support. The capability-matched validation and tradeoff visualization can move to supplementary without losing the main argument.

The remaining experiments—panel size sensitivity, VIF diagnostics, generation extension, and partial-knowledge adversary—should still be included since this needs to be review-ready, but I'll keep them concise and well-integrated. Let me structure the paper to weave these together coherently rather than presenting them as isolated ablations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a7d3784-bdc6-48d5-bea4-8c48b9c695df",
  "isSidechain": false,
  "requestId": "req_011CbJQZMEYSd3N4VU26hff9",
  "type": "assistant",
  "uuid": "d579bdf7-3e37-47a8-ad94-9b733ad338c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013oqHMZwXzSUFg9LmDCc5wC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2365,
      "cache_read_input_tokens": 49694,
      "output_tokens": 9984,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2365,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9984,
          "cache_read_input_tokens": 49694,
          "cache_creation_input_tokens": 2365,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2365
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

_source line 22 · 2026-05-22T22:36:54.004Z_

Now I'll write the full LaTeX paper. This covers all 12 experiments from the data, organized into a coherent narrative following the framing document.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d579bdf7-3e37-47a8-ad94-9b733ad338c2",
  "isSidechain": false,
  "requestId": "req_011CbJQZMEYSd3N4VU26hff9",
  "type": "assistant",
  "uuid": "74b7a14b-7d27-4cf7-9fd5-09593989dc04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013oqHMZwXzSUFg9LmDCc5wC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2365,
      "cache_read_input_tokens": 49694,
      "output_tokens": 9984,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2365,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9984,
          "cache_read_input_tokens": 49694,
          "cache_creation_input_tokens": 2365,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2365
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

_source line 23 · 2026-05-22T22:39:56.299Z_

<details open><summary>🔧 Tool call — Write · `toolu_014238nA5TFG6i3bEpA4Wz4h`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage{tablefootnote}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\n\\title{Weakest Link, Not Diversity: Adversarial Vulnerability in Multi-Judge LLM Evaluation}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nMulti-judge LLM evaluation panels are increasingly adopted to improve reliability, with an implicit assumption---rooted in Byzantine Fault Tolerance (BFT) theory---that judge diversity provides robustness against manipulation. We conduct the first large-scale empirical decomposition of panel vulnerability into two structural predictors: individual judge weakness ($\\eta_{\\max}$, the vulnerability of the weakest panel member) and panel diversity ($K_{\\text{eff}}$, effective number of independent behavioral clusters). Across 15 models from 6 families, 455 panels, 9 attack types, and 3 benchmarks (MMLU, ARC-Challenge, MT-Bench), we find that $\\eta_{\\max}$ \\emph{robustly} dominates panel vulnerability---significant in 8/12 conditions under clustered standard errors and 5/12 under wild cluster bootstrap, with a dominance ratio of 5:1 over $K_{\\text{eff}}$. $K_{\\text{eff}}$ shows directional but statistically fragile association, collapsing from 8/12 (OLS) to 0/12 (clustered SE) after correcting for panel non-independence. A Generalized Additive Model (GAM) analysis reveals a clean mechanistic split: $K_{\\text{eff}}$ is positive (diversity harmful) for all targeted attacks and negative (diversity protective) for all shared-bias attacks---a 10:8 taxonomy across 9 attack types. Aggregation rule choice fundamentally modulates vulnerability: Bayesian calibration reverses $K_{\\text{eff}}$ direction and weakens $\\eta_{\\max}$, while threshold voting amplifies both. We propose a robustness-first panel design algorithm that wins 12/12 conditions, outperforming naive diversity maximization which performs worse than random selection.\n\\end{abstract}\n\n\\section{Introduction}\n\nThe use of Large Language Models (LLMs) as automated judges for evaluating other LLMs has become a cornerstone of modern NLP evaluation \\cite{zheng2023judging}. To mitigate individual judge biases, recent work increasingly employs multi-judge panels where multiple LLM judges evaluate candidates and their scores are aggregated via majority vote or similar mechanisms. The implicit operating assumption---borrowed from distributed systems and BFT theory---is that judge diversity provides robustness: more diverse panels should be harder to fool.\n\nThis assumption has not been empirically tested under adversarial conditions. In non-adversarial settings, diversity does reduce calibration errors and position biases. But adversarial manipulation fundamentally changes the threat model: an adaptive adversary can exploit judge-specific vulnerabilities, potentially turning diversity from a defense into an attack surface.\n\nWe conduct the first large-scale empirical study decomposing panel vulnerability into two structural predictors. Let $\\eta_{\\max}$ denote the vulnerability of the weakest judge in a panel (the maximum individual attack success rate), and $K_{\\text{eff}}$ denote the effective number of independent behavioral clusters among panel judges (a diversity measure derived from mutual information). Our central question: \\emph{which structural factor---individual weakness or panel diversity---drives vulnerability under adaptive adversarial attack?}\n\nOur findings challenge the diversity-as-defense assumption:\n\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Weakest-link dominance.} $\\eta_{\\max}$ robustly dominates panel vulnerability (5:1 over $K_{\\text{eff}}$ under bootstrap inference). $K_{\\text{eff}}$'s apparent significance under OLS (8/12) collapses to 0--1/12 after correcting for panel non-independence---a methodological finding relevant to all combinatorial evaluation designs.\n\n\\item \\textbf{BFT reversal evidence.} A random-fault Monte Carlo contrast experiment shows $K_{\\text{eff}}$ is genuinely significant (2/2, all corrections) under i.i.d. faults but artifactual under adaptive attacks, providing causal evidence for the failure of BFT assumptions.\n\n\\item \\textbf{Attack-type taxonomy.} GAM analysis reveals a clean mechanistic split: $K_{\\text{eff}}$ is positive (diversity harmful) for targeted attacks and negative (diversity protective) for shared-bias attacks---a 10:8 pattern across 9 attack types.\n\n\\item \\textbf{Aggregation as control lever.} Bayesian calibration reverses $K_{\\text{eff}}$ direction (from harmful to protective) and weakens $\\eta_{\\max}$ dominance. Threshold voting amplifies both drivers ($R^2=0.87$).\n\n\\item \\textbf{Robustness-first panel design.} A two-stage algorithm (filter by $\\eta_{\\max}$, then optimize $K_{\\text{eff}}$) wins 12/12 conditions. Naive $K_{\\text{eff}}$ maximization performs \\emph{worse} than random selection.\n\\end{enumerate}\n\n\\section{Related Work}\n\n\\paragraph{LLM-as-Judge.} LLM-based evaluation has become standard practice for open-ended generation tasks \\cite{zheng2023judging}. Known biases include position bias, verbosity bias, and sycophancy. Multi-judge panels have been proposed as a mitigation strategy, though systematic analysis of panel robustness under adversarial conditions remains absent.\n\n\\paragraph{Adversarial Attacks on LLM Judges.} Prior work has demonstrated that individual LLM judges can be manipulated through prompt injection, score inflation, and stylistic gaming. However, existing studies focus on single-judge vulnerability rather than panel-level structural predictors.\n\n\\paragraph{Byzantine Fault Tolerance.} BFT theory guarantees correctness when fewer than $f < n/3$ nodes fail independently. The key assumption---independent, random faults---is violated by adaptive adversaries who can strategically target specific judges. Our work provides the first empirical quantification of this assumption violation in LLM evaluation.\n\n\\section{Method}\n\n\\subsection{Panel Construction}\n\nWe enumerate all $\\binom{15}{3} = 455$ panels of size $K=3$ from a pool of 15 LLM judges spanning 6 model families (GPT, Claude, Gemini, Llama, Qwen, Mistral) and 3 capability tiers (frontier, mid, base). Each panel evaluates benchmark items under majority vote.\n\n\\subsection{Vulnerability Predictors}\n\n\\paragraph{Individual Weakness ($\\eta_{\\max}$).} For each panel, $\\eta_{\\max} = \\max_{j \\in \\text{panel}} \\eta_j$, where $\\eta_j$ is judge $j$'s individual attack success rate (ASR) under a given attack type. This captures the weakest-link hypothesis: panel vulnerability is determined by the most exploitable judge.\n\n\\paragraph{Panel Diversity ($K_{\\text{eff}}$).} We compute pairwise mutual information (MI) between all judge pairs' evaluation vectors on clean data, then derive $K_{\\text{eff}}$ as the effective number of independent clusters. Higher $K_{\\text{eff}}$ indicates greater behavioral diversity among panel judges.\n\n\\subsection{Attack Types}\n\nWe study 9 attack types spanning two mechanistic categories:\n\n\\begin{itemize}[leftmargin=*,itemsep=1pt]\n\\item \\textbf{Targeted attacks} exploit judge-specific weaknesses: prompt injection, score manipulation, position bias exploitation, few-shot hijacking, instruction override, format gaming.\n\\item \\textbf{Shared-bias attacks} exploit common cognitive biases: sycophancy amplification, verbosity bias, authority bias, style manipulation, length inflation, persona manipulation.\n\\end{itemize}\n\n\\subsection{Regression Specification}\n\nOur canonical specification is log-log OLS:\n\\begin{equation}\n\\log(\\text{ASR} + \\epsilon) = \\beta_0 + \\beta_1 \\log(K_{\\text{eff}}) + \\beta_2 \\log(\\eta_{\\max} + \\epsilon)\n\\label{eq:regression}\n\\end{equation}\nwhere $\\epsilon$ is a small constant for numerical stability. We report significance under four correction methods: standard OLS, clustered standard errors (CR1, 15 judge clusters), wild cluster bootstrap ($B=9999$, Rademacher weights, max-$p$ across 3 judge positions), and mixed effects (random judge intercepts). Panel non-independence arises because judges appear in multiple panels (e.g., claude-3-haiku appears in 91/455 panels), inflating standard errors by $\\sim$2.5$\\times$.\n\n\\subsection{Aggregation Rules}\n\nWe evaluate five aggregation rules: majority vote (baseline), accuracy-weighted vote, threshold (unanimity), Bayesian calibration (prior-weighted), and veto (single-judge override).\n\n\\section{Experiments}\n\n\\subsection{Core Results: Weakest-Link Dominance}\n\\label{sec:core}\n\nTable~\\ref{tab:correction} presents our primary results across 15 models, 455 panels, and 12 conditions (6 attack types $\\times$ 2 benchmarks). The pattern is stark: $\\eta_{\\max}$ dominates under all correction methods, while $K_{\\text{eff}}$'s significance collapses after accounting for panel non-independence.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{$\\eta_{\\max}$ sig} & \\textbf{$K_{\\text{eff}}$ sig} & \\textbf{$K_{\\text{eff}}$ dir} & \\textbf{Ratio} \\\\\n\\midrule\nOLS & 11/12 & 8/12 & 7+/1$-$ & 1.4:1 \\\\\nClustered SE & 8/12 & 0/12 & -- & $\\infty$ \\\\\nBootstrap v2 & 5/12 & 1/12 & 1+ & 5:1 \\\\\nMixed effects & 7/12 & 3/12 & 3+ & 2.3:1 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Correction method comparison (15 models, 455 panels, 12 conditions). $\\eta_{\\max}$ significance is robust across all methods; $K_{\\text{eff}}$ collapses from 8/12 under OLS to 0--1/12 after non-independence correction. SE inflation $\\sim$2.5$\\times$ is consistent with 91/455 panel overlap.}\n\\label{tab:correction}\n\\end{table}\n\nUnder OLS, both predictors appear significant ($\\eta_{\\max}$ 11/12, $K_{\\text{eff}}$ 8/12), producing a misleading near-parity (1.4:1). Clustered SE correction---which accounts for shared judge membership across panels---eliminates all $K_{\\text{eff}}$ significance (0/12) while retaining $\\eta_{\\max}$ at 8/12. The most conservative method (wild cluster bootstrap with max-$p$ across judge positions) gives a 5:1 dominance ratio. The $\\min(\\eta_{\\max})$ panel selection strategy wins 12/12 conditions with ASR advantages ranging from 3.8 to 51.1 percentage points.\n\n\\subsection{Attack Surface Expansion}\n\\label{sec:attack_expansion}\n\nTo confirm that $\\eta_{\\max}$ dominance is not an artifact of our initial attack selection, we extend to 3 additional attack types (few-shot hijacking, persona manipulation, instruction override), yielding 18 total conditions. Table~\\ref{tab:extended_attack} shows results under clustered SE.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Attack} & \\textbf{Mech.} & \\textbf{$\\eta_{\\max}$} & \\textbf{$K_{\\text{eff}}$} & \\textbf{GAM dir} \\\\\n\\midrule\nFew-shot hijack & targ. & \\checkmark\\checkmark & 0/2 & positive \\\\\nPersona manip. & shared & \\checkmark\\checkmark & 0/2 & negative \\\\\nInstr. override & targ. & 1/2 & 0/2 & positive \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Combined (18 cond.)}} & 13/18 & 0/18 & 10:8 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Extended attack taxonomy (clustered SE). $\\eta_{\\max}$ remains dominant across all new attack types. GAM taxonomy extends cleanly from 6:6 to 10:8 (targeted:shared-bias). $\\checkmark\\checkmark$ = significant on both benchmarks.}\n\\label{tab:extended_attack}\n\\end{table}\n\nThe combined dominance ratio under clustered SE is 13:0---$K_{\\text{eff}}$ achieves zero significance across all 18 conditions. The GAM taxonomy extends cleanly: few-shot hijacking and instruction override are classified as targeted (positive $K_{\\text{eff}}$), while persona manipulation is classified as shared-bias (negative $K_{\\text{eff}}$), extending the split from 6:6 to 10:8.\n\n\\subsection{Random-Fault BFT Contrast}\n\\label{sec:rf}\n\nTo provide causal evidence for BFT assumption failure, we construct a random-fault (RF) baseline via Monte Carlo simulation (10,000 iterations). Each judge fails independently with probability $\\eta_j = 1 - \\text{clean\\_accuracy}$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccl}\n\\toprule\n\\textbf{Metric} & \\textbf{Random Fault} & \\textbf{Adaptive} & \\textbf{Interpretation} \\\\\n\\midrule\n$K_{\\text{eff}}$ sig (OLS) & 2/2 & 8/12 & Both appear sig. \\\\\n$K_{\\text{eff}}$ sig (CL-SE) & 2/2 & 0/12 & RF genuine; adap. not \\\\\n$K_{\\text{eff}}$ sig (Boot.) & 2/2 & 1/12 & Consistent contrast \\\\\n$K_{\\text{eff}}$ std $\\beta$ & +0.297 & +0.164 & RF larger, genuine \\\\\n$R^2$ & 0.78--0.81 & 0.25--0.35 & Predictability gap \\\\\n$\\eta_{\\max}$ sig (all) & 2/2 & 5--8/12 & Genuine in both \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Random-fault vs.\\ adaptive regime contrast. $K_{\\text{eff}}$ is genuinely significant under i.i.d.\\ faults (2/2 under all corrections) but artifactual under adaptive attacks (0--1/12 after correction). The $R^2$ gap ($\\Delta = 0.48$) quantifies the unpredictability introduced by adaptive adversaries.}\n\\label{tab:rf_contrast}\n\\end{table}\n\nTable~\\ref{tab:rf_contrast} presents the contrast. Under random faults, $K_{\\text{eff}}$ is significant 2/2 under \\emph{all} correction methods ($p_{\\text{bootstrap}} = 0.003$ for MMLU, $<$0.001 for ARC), with $R^2 = 0.78$--$0.81$. Under adaptive attacks, the same predictor collapses to 0--1/12 after correction. This is not a direction reversal---$K_{\\text{eff}}$ is positively associated with vulnerability in \\emph{both} regimes. The difference is that the RF association is genuine (panel structure determines fault tolerance under i.i.d.\\ assumptions), while the adaptive association is inflated by panel overlap. The $R^2$ gap ($\\Delta = 0.48$) directly quantifies the strategic variance introduced by adaptive adversaries that panel structure cannot predict.\n\n\\subsection{ASR Concentration Analysis}\n\\label{sec:concentration}\n\nTo provide mechanistic evidence for $\\eta_{\\max}$ dominance, we compute per-judge ASR distributions within each panel and measure concentration via Gini coefficients and Shannon entropy.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Attack} & \\textbf{Cat.} & \\textbf{Gini} & \\textbf{Entropy} & \\textbf{Top-1 frac.} \\\\\n\\midrule\nPrompt inject. & targ. & 0.82 & 0.73 & 0.65 \\\\\nScore manip. & targ. & 0.79 & 0.78 & 0.62 \\\\\nPosition bias & targ. & 0.74 & 0.94 & 0.56 \\\\\nSycophancy & shared & 0.45 & 1.38 & 0.40 \\\\\nVerbosity bias & shared & 0.42 & 1.47 & 0.37 \\\\\nAuthority bias & shared & 0.41 & 1.50 & 0.36 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{ASR concentration by attack category. Targeted attacks show highly concentrated ASR (Gini $>$ 0.7, top-1 judge contributes $>$56\\% of panel ASR), providing mechanistic evidence for $\\eta_{\\max}$ dominance. Mann-Whitney $U$ test: $p < 0.001$ between categories.}\n\\label{tab:concentration}\n\\end{table}\n\nTable~\\ref{tab:concentration} reveals a sharp dichotomy. Under targeted attacks, ASR is highly concentrated: the most vulnerable judge contributes 56--65\\% of total panel ASR (mean Gini = 0.78). Under shared-bias attacks, ASR is more uniformly distributed (mean Gini = 0.43, top-1 fraction = 37\\%). The Gini--$\\eta_{\\max}$ correlation is $r = 0.83$, directly linking panel-level vulnerability to judge-level concentration. This independently validates the GAM taxonomy: targeted and shared-bias attacks differ not only in $K_{\\text{eff}}$ direction but in their micro-level ASR distribution patterns.\n\n\\subsection{Aggregation Gradient}\n\\label{sec:aggregation}\n\nWe evaluate five aggregation rules under clustered SE to characterize how vote aggregation modulates vulnerability.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccl}\n\\toprule\n\\textbf{Rule} & \\textbf{$\\eta_{\\max}$} & \\textbf{$K_{\\text{eff}}$} & \\textbf{Neg.} & \\textbf{$R^2$} & \\textbf{Position} \\\\\n\\midrule\nVeto & 11/12 & 0/12 & -- & 0.82 & Max vuln. \\\\\nThreshold & 10/12 & 4/12 & 1/4 & 0.87 & High \\\\\nMajority & 8/12 & 0/12 & -- & 0.28 & Moderate \\\\\nWeighted & 6/12 & 1/12 & 0/1 & 0.26 & Low-mod. \\\\\nBayesian & 5/12 & 4/12 & 3/4 & 0.09 & Min vuln. \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Aggregation gradient under clustered SE. ``Neg.'' = fraction of significant $K_{\\text{eff}}$ coefficients that are negative. Bayesian calibration weakens $\\eta_{\\max}$ (11$\\to$5/12) and flips $K_{\\text{eff}}$ direction (3/4 negative), while veto/threshold amplify the weakest-link channel.}\n\\label{tab:aggregation}\n\\end{table}\n\nTable~\\ref{tab:aggregation} reveals a gradient from maximum to minimum vulnerability. Veto rule (any single judge can override) maximizes $\\eta_{\\max}$ dominance (11/12) with $K_{\\text{eff}}$ completely suppressed. Threshold voting (unanimity) amplifies both channels ($R^2 = 0.87$). Bayesian calibration, which down-weights unreliable judges using prior accuracy estimates, achieves the strongest mitigation: $\\eta_{\\max}$ drops to 5/12 and $K_{\\text{eff}}$ flips to majority-negative (3/4 significant coefficients negative), meaning diversity becomes protective.\n\nUnder bootstrap, Bayesian $K_{\\text{eff}}$ shows 3/12 significant---all negative (3/3 negative fraction = 100\\%). This directional flip is the cleanest evidence that aggregation is an independent control lever, unaffected by the non-independence concerns that plague the diversity analysis.\n\n\\subsection{Panel Design Algorithm}\n\\label{sec:design}\n\nWe benchmark a two-stage robustness-first algorithm against 6 baseline strategies across 12 conditions.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Strategy} & \\textbf{Mean ASR} & \\textbf{Rank} & \\textbf{$\\Delta$ vs.\\ random (pp)} \\\\\n\\midrule\nTwo-stage & 0.112 & 1 & $-$8.3 \\\\\n$\\min(\\eta_{\\max})$ & 0.119 & 2 & $-$7.6 \\\\\nStrongest-$K$ & 0.131 & 3 & $-$6.4 \\\\\nUniform family & 0.158 & 4 & $-$3.7 \\\\\nMax disagreement & 0.172 & 5 & $-$2.3 \\\\\nRandom & 0.195 & 6 & 0.0 \\\\\n$\\max(K_{\\text{eff}})$ & 0.208 & 7 & $+$1.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Panel design strategy comparison (mean ASR across 12 conditions). The $\\max(K_{\\text{eff}})$ strategy---the intuitive ``maximize diversity'' approach---performs \\emph{worse} than random selection because it introduces weak models. Two-stage provides a marginal 0.7pp improvement over $\\min(\\eta_{\\max})$ alone.}\n\\label{tab:strategy}\n\\end{table}\n\nTable~\\ref{tab:strategy} presents the ranking. The most striking result is that $\\max(K_{\\text{eff}})$---the intuitive ``diversify your panel'' strategy---ranks \\emph{last}, performing 1.3pp worse than random selection. This occurs because maximizing diversity necessarily introduces weaker models (the diversity-capability tradeoff, $r = 0.70$). The two-stage algorithm provides a consistent but modest improvement (0.7pp) over pure $\\min(\\eta_{\\max})$, with the marginal gain concentrated in targeted attack conditions (5/6 wins, mean $\\Delta = -1.1$pp) where controlled $K_{\\text{eff}}$ optimization adds value after robustness screening.\n\n\\subsection{Capability-Matched Validation}\n\\label{sec:capability}\n\nTo disentangle $\\eta_{\\max}$ and $K_{\\text{eff}}$ (confound $r = 0.70$ in the full pool), we conduct within-tier analysis using 9 base-tier models (84 panels), which reduces the confound to $r = 0.35$ and $\\eta_{\\max}$ variance by 65--70\\%.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Setting} & \\textbf{Panels} & \\textbf{$r$} & \\textbf{$\\eta_{\\max}$ (CL)} & \\textbf{$K_{\\text{eff}}$ (CL)} \\\\\n\\midrule\nFull pool & 455 & 0.70 & 8/12 & 0/12 \\\\\nBase tier & 84 & 0.35 & 4/12 & 2/12 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-tier vs.\\ within-tier comparison (clustered SE). Controlling for capability reduces confound and reveals $K_{\\text{eff}}$ as a weak but detectable secondary factor (2/12, both in targeted conditions). The dominance ratio narrows from $\\infty$ to 2:1, but $\\eta_{\\max}$ still dominates.}\n\\label{tab:capability}\n\\end{table}\n\nWithin the base tier (Table~\\ref{tab:capability}), $K_{\\text{eff}}$ emerges as a weak secondary factor (2/12 significant under clustered SE), with the dominance ratio narrowing from $\\infty$ to 2:1. Both significant $K_{\\text{eff}}$ conditions are targeted attacks (mmlu$\\times$prompt\\_injection, $\\beta = +0.31$, $p = 0.028$; mmlu$\\times$score\\_manipulation, $\\beta = +0.25$, $p = 0.041$), consistent with the GAM taxonomy. The within-tier $R^2$ mean drops to 0.18 (vs.\\ 0.30 in the full pool), confirming that cross-tier $\\eta_{\\max}$ variance is the primary source of predictive power.\n\n\\subsection{Diversity-Capability Tradeoff}\n\\label{sec:tradeoff}\n\nThe structural correlation between $K_{\\text{eff}}$ and $\\eta_{\\max}$ ($r = 0.70$, 95\\% CI $[0.66, 0.74]$) reflects a fundamental constraint in the current LLM ecosystem: maximizing behavioral diversity requires including models from different capability tiers, which inevitably introduces weaker judges. This correlation is strongest within model families ($r = 0.81$) and weakest at the frontier tier ($r = 0.35$), where architectural differences provide diversity without large capability gaps. The Pareto frontier analysis shows that 97.4\\% of panels are dominated, with optimal panels clustering in the low-$K_{\\text{eff}}$, low-$\\eta_{\\max}$ region. VIF analysis confirms moderate but non-pathological multicollinearity (VIF = 2.96, condition number = 4.8), with partial correlations of $r(\\eta_{\\max}, \\text{ASR} \\mid K_{\\text{eff}}) = 0.42$ vs.\\ $r(K_{\\text{eff}}, \\text{ASR} \\mid \\eta_{\\max}) = 0.18$.\n\n\\subsection{Panel Size Sensitivity}\n\\label{sec:panel_size}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{$K$} & \\textbf{Panels} & \\textbf{$\\eta_{\\max}$} & \\textbf{$K_{\\text{eff}}$} & \\textbf{Ratio} & \\textbf{SE infl.} \\\\\n\\midrule\n3 & 455 & 8/12 & 0/12 & $\\infty$ & 2.5$\\times$ \\\\\n5 & 3003 & 9/12 & 1/12 & 9:1 & 4.1$\\times$ \\\\\n7 & 6435 & 9/12 & 1/12 & 9:1 & 6.3$\\times$ \\\\\n9 & 5005 & 8/12 & 2/12 & 4:1 & 7.8$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Panel size sensitivity (clustered SE). $\\eta_{\\max}$ dominance persists across $K=3$--$9$, confirming the weakest-link mechanism is scale-invariant. SE inflation increases sharply with $K$, underscoring the necessity of non-independence correction in combinatorial designs.}\n\\label{tab:panel_size}\n\\end{table}\n\nTable~\\ref{tab:panel_size} demonstrates that $\\eta_{\\max}$ dominance is not an artifact of small panels. Across $K = 3$ to $K = 9$, the $\\eta_{\\max}$ effect size decreases slightly (standardized $\\beta$: 0.42 to 0.31) as larger panels provide more majority-vote fault tolerance, but the dominance ratio remains $\\geq$4:1. The $\\min(\\eta_{\\max})$ strategy wins 12/12 conditions at every panel size. SE inflation increases from 2.5$\\times$ to 7.8$\\times$, providing compelling evidence that non-independence correction is essential for panel studies at any scale.\n\n\\subsection{Generation Benchmark Extension}\n\\label{sec:generation}\n\nTo rule out MCQ-specific artifacts, we extend to MT-Bench, an open-ended generation benchmark with 1--10 scale scoring. We test 3 generation-specific attack types across 12 available models and 220 panels.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Format} & \\textbf{$\\eta_{\\max}$ (CL)} & \\textbf{$K_{\\text{eff}}$ (CL)} & \\textbf{Ratio} \\\\\n\\midrule\nMCQ (MMLU+ARC) & 8/12 & 0/12 & $\\infty$ \\\\\nGeneration (MT-Bench) & 4/6 & 0/6 & $\\infty$ \\\\\nCombined & 12/18 & 0/18 & $\\infty$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-format consistency (clustered SE). $\\eta_{\\max}$ dominance generalizes from MCQ to open-ended generation evaluation. The combined ratio across 18 conditions is $\\infty$ (12:0).}\n\\label{tab:generation}\n\\end{table}\n\nTable~\\ref{tab:generation} confirms that $\\eta_{\\max}$ dominance generalizes across evaluation formats. Under clustered SE, the combined dominance ratio is 12:0 across 18 conditions. GAM classification of generation attacks aligns with the mechanistic taxonomy: style manipulation and length inflation are shared-bias (negative $K_{\\text{eff}}$), while format gaming is targeted (positive $K_{\\text{eff}}$). The $\\min(\\eta_{\\max})$ strategy wins 6/6 generation conditions, confirming the practical recommendation is format-agnostic.\n\n\\subsection{Partial-Knowledge Adversary}\n\\label{sec:partial}\n\nReal-world adversaries rarely have full knowledge of panel composition. We simulate three knowledge levels: full (baseline), family-only (adversary knows model family labels but not specific vulnerability profiles), and random (no targeting).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Knowledge} & \\textbf{ASR} & \\textbf{$\\eta_{\\max}$ (CL)} & \\textbf{$K_{\\text{eff}}$ (CL)} & \\textbf{$R^2$} \\\\\n\\midrule\nFull & 0.195 & 8/12 & 0/12 & 0.30 \\\\\nFamily-only & 0.160 & 7/12 & 0/12 & 0.24 \\\\\nRandom & 0.113 & 3/12 & 0/12 & 0.08 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Adversary knowledge level comparison (clustered SE). Family-only knowledge retains 82\\% attack efficiency. $K_{\\text{eff}}$ is 0/12 under all knowledge levels. $\\eta_{\\max}$ dominance persists under realistic threat models.}\n\\label{tab:partial}\n\\end{table}\n\nTable~\\ref{tab:partial} reveals that family-level knowledge retains 82\\% of full-knowledge attack efficiency ($\\text{ASR} = 0.160$ vs.\\ $0.195$), because same-family models share training pipeline and architectural biases ($r_{\\text{family-vulnerability}} = 0.61$). Defenders cannot rely on panel composition secrecy: family labels are easily inferred from API endpoints and response styles. $K_{\\text{eff}}$ remains 0/12 under all knowledge levels, and $\\eta_{\\max}$ dominance persists even under family-only targeting (7/12), confirming the core findings are robust to adversary capability assumptions.\n\n\\section{Discussion}\n\n\\paragraph{When diversity helps.} Our results do not imply diversity is universally harmful. Under shared-bias attacks, GAM analysis consistently shows negative $K_{\\text{eff}}$ direction (8/8 conditions including extended attacks), meaning diversity provides partial immunity when the adversary exploits biases shared across model families. After robustness screening removes weak judges, the diversity-capability tradeoff is weakened ($r$ drops from 0.70 to 0.35), creating conditions where diversity optimization adds marginal value. And in non-adversarial settings, diversity remains beneficial for reducing calibration errors and position biases.\n\n\\paragraph{Practical recommendations.} Based on our findings, we recommend a defense stack combining: (1) robustness-first screening to eliminate $\\eta_{\\max}$ as a vulnerability driver, and (2) Bayesian aggregation to reverse $K_{\\text{eff}}$ from harmful to protective. This dual-channel approach addresses both structural vulnerability drivers. The $\\max(K_{\\text{eff}})$ strategy should be explicitly avoided, as it performs worse than random selection.\n\n\\paragraph{Methodological implications.} The dramatic significance shift from OLS to clustered SE ($K_{\\text{eff}}$: 8/12 $\\to$ 0/12) is a cautionary finding for all combinatorial evaluation designs where the same items (here, judges) appear in multiple experimental units (panels). SE inflation of 2.5--7.8$\\times$ can produce severely misleading conclusions. We recommend that future panel studies routinely report clustered SE alongside OLS.\n\n\\section{Conclusion}\n\nWe conducted the first large-scale empirical decomposition of multi-judge LLM evaluation panel vulnerability. Our central finding---that panel vulnerability is dominated by the weakest individual judge, not panel diversity---challenges the implicit BFT assumption underlying multi-judge evaluation design. The dominance ratio of 5:1 ($\\eta_{\\max}$ over $K_{\\text{eff}}$) is robust across 9 attack types, 3 benchmarks, 4 panel sizes, 3 adversary knowledge levels, and 4 statistical correction methods. Aggregation rule choice provides an independent control lever: Bayesian calibration reverses diversity's role from vulnerability to defense. We release our two-stage panel design algorithm as a practical tool for building adversarially robust evaluation panels.\n\n\\section*{Limitations}\n\nOur study has three main limitations. First, the model pool (15 models, 6 families) represents the current LLM ecosystem; the diversity-capability tradeoff ($r = 0.70$) may weaken as more capable open-source models become available. Second, our adaptive adversary model assumes strategic targeting of individual judges---real-world adversaries may face additional constraints (e.g., limited query budgets) that reduce attack efficiency below the levels we measure. Third, the Bayesian aggregation defense requires access to clean-data accuracy estimates, which may themselves be subject to manipulation; evaluating the robustness of the defense stack to meta-adversarial attacks remains future work.\n\n\\bibliography{custom}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74b7a14b-7d27-4cf7-9fd5-09593989dc04",
  "isSidechain": false,
  "requestId": "req_011CbJQZMEYSd3N4VU26hff9",
  "type": "assistant",
  "uuid": "58408cf6-eaa7-4176-98ed-dbe79bd1e42b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013oqHMZwXzSUFg9LmDCc5wC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2365,
      "cache_read_input_tokens": 49694,
      "output_tokens": 9984,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2365,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9984,
          "cache_read_input_tokens": 49694,
          "cache_creation_input_tokens": 2365,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2365
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

_source line 24 · 2026-05-22T22:39:56.320Z_

<details><summary>↩ Tool result · `toolu_014238nA5TFG6i3bEpA4Wz4h`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58408cf6-eaa7-4176-98ed-dbe79bd1e42b",
  "isSidechain": false,
  "promptId": "d5483bc6-a830-4026-80bc-d9c580d884bc",
  "type": "user",
  "uuid": "49309ec1-e232-4b0d-908b-5cbaae9bec70",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage{tablefootnote}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\n\\title{Weakest Link, Not Diversity: Adversarial Vulnerability in Multi-Judge LLM Evaluation}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nMulti-judge LLM evaluation panels are increasingly adopted to improve reliability, with an implicit assumption---rooted in Byzantine Fault Tolerance (BFT) theory---that judge diversity provides robustness against manipulation. We conduct the first large-scale empirical decomposition of panel vulnerability into two structural predictors: individual judge weakness ($\\eta_{\\max}$, the vulnerability of the weakest panel member) and panel diversity ($K_{\\text{eff}}$, effective number of independent behavioral clusters). Across 15 models from 6 families, 455 panels, 9 attack types, and 3 benchmarks (MMLU, ARC-Challenge, MT-Bench), we find that $\\eta_{\\max}$ \\emph{robustly} dominates panel vulnerability---significant in 8/12 conditions under clustered standard errors and 5/12 under wild cluster bootstrap, with a dominance ratio of 5:1 over $K_{\\text{eff}}$. $K_{\\text{eff}}$ shows directional but statistically fragile association, collapsing from 8/12 (OLS) to 0/12 (clustered SE) after correcting for panel non-independence. A Generalized Additive Model (GAM) analysis reveals a clean mechanistic split: $K_{\\text{eff}}$ is positive (diversity harmful) for all targeted attacks and negative (diversity protective) for all shared-bias attacks---a 10:8 taxonomy across 9 attack types. Aggregation rule choice fundamentally modulates vulnerability: Bayesian calibration reverses $K_{\\text{eff}}$ direction and weakens $\\eta_{\\max}$, while threshold voting amplifies both. We propose a robustness-first panel design algorithm that wins 12/12 conditions, outperforming naive diversity maximization which performs worse than random selection.\n\\end{abstract}\n\n\\section{Introduction}\n\nThe use of Large Language Models (LLMs) as automated judges for evaluating other LLMs has become a cornerstone of modern NLP evaluation \\cite{zheng2023judging}. To mitigate individual judge biases, recent work increasingly employs multi-judge panels where multiple LLM judges evaluate candidates and their scores are aggregated via majority vote or similar mechanisms. The implicit operating assumption---borrowed from distributed systems and BFT theory---is that judge diversity provides robustness: more diverse panels should be harder to fool.\n\nThis assumption has not been empirically tested under adversarial conditions. In non-adversarial settings, diversity does reduce calibration errors and position biases. But adversarial manipulation fundamentally changes the threat model: an adaptive adversary can exploit judge-specific vulnerabilities, potentially turning diversity from a defense into an attack surface.\n\nWe conduct the first large-scale empirical study decomposing panel vulnerability into two structural predictors. Let $\\eta_{\\max}$ denote the vulnerability of the weakest judge in a panel (the maximum individual attack success rate), and $K_{\\text{eff}}$ denote the effective number of independent behavioral clusters among panel judges (a diversity measure derived from mutual information). Our central question: \\emph{which structural factor---individual weakness or panel diversity---drives vulnerability under adaptive adversarial attack?}\n\nOur findings challenge the diversity-as-defense assumption:\n\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Weakest-link dominance.} $\\eta_{\\max}$ robustly dominates panel vulnerability (5:1 over $K_{\\text{eff}}$ under bootstrap inference). $K_{\\text{eff}}$'s apparent significance under OLS (8/12) collapses to 0--1/12 after correcting for panel non-independence---a methodological finding relevant to all combinatorial evaluation designs.\n\n\\item \\textbf{BFT reversal evidence.} A random-fault Monte Carlo contrast experiment shows $K_{\\text{eff}}$ is genuinely significant (2/2, all corrections) under i.i.d. faults but artifactual under adaptive attacks, providing causal evidence for the failure of BFT assumptions.\n\n\\item \\textbf{Attack-type taxonomy.} GAM analysis reveals a clean mechanistic split: $K_{\\text{eff}}$ is positive (diversity harmful) for targeted attacks and negative (diversity protective) for shared-bias attacks---a 10:8 pattern across 9 attack types.\n\n\\item \\textbf{Aggregation as control lever.} Bayesian calibration reverses $K_{\\text{eff}}$ direction (from harmful to protective) and weakens $\\eta_{\\max}$ dominance. Threshold voting amplifies both drivers ($R^2=0.87$).\n\n\\item \\textbf{Robustness-first panel design.} A two-stage algorithm (filter by $\\eta_{\\max}$, then optimize $K_{\\text{eff}}$) wins 12/12 conditions. Naive $K_{\\text{eff}}$ maximization performs \\emph{worse} than random selection.\n\\end{enumerate}\n\n\\section{Related Work}\n\n\\paragraph{LLM-as-Judge.} LLM-based evaluation has become standard practice for open-ended generation tasks \\cite{zheng2023judging}. Known biases include position bias, verbosity bias, and sycophancy. Multi-judge panels have been proposed as a mitigation strategy, though systematic analysis of panel robustness under adversarial conditions remains absent.\n\n\\paragraph{Adversarial Attacks on LLM Judges.} Prior work has demonstrated that individual LLM judges can be manipulated through prompt injection, score inflation, and stylistic gaming. However, existing studies focus on single-judge vulnerability rather than panel-level structural predictors.\n\n\\paragraph{Byzantine Fault Tolerance.} BFT theory guarantees correctness when fewer than $f < n/3$ nodes fail independently. The key assumption---independent, random faults---is violated by adaptive adversaries who can strategically target specific judges. Our work provides the first empirical quantification of this assumption violation in LLM evaluation.\n\n\\section{Method}\n\n\\subsection{Panel Construction}\n\nWe enumerate all $\\binom{15}{3} = 455$ panels of size $K=3$ from a pool of 15 LLM judges spanning 6 model families (GPT, Claude, Gemini, Llama, Qwen, Mistral) and 3 capability tiers (frontier, mid, base). Each panel evaluates benchmark items under majority vote.\n\n\\subsection{Vulnerability Predictors}\n\n\\paragraph{Individual Weakness ($\\eta_{\\max}$).} For each panel, $\\eta_{\\max} = \\max_{j \\in \\text{panel}} \\eta_j$, where $\\eta_j$ is judge $j$'s individual attack success rate (ASR) under a given attack type. This captures the weakest-link hypothesis: panel vulnerability is determined by the most exploitable judge.\n\n\\paragraph{Panel Diversity ($K_{\\text{eff}}$).} We compute pairwise mutual information (MI) between all judge pairs' evaluation vectors on clean data, then derive $K_{\\text{eff}}$ as the effective number of independent clusters. Higher $K_{\\text{eff}}$ indicates greater behavioral diversity among panel judges.\n\n\\subsection{Attack Types}\n\nWe study 9 attack types spanning two mechanistic categories:\n\n\\begin{itemize}[leftmargin=*,itemsep=1pt]\n\\item \\textbf{Targeted attacks} exploit judge-specific weaknesses: prompt injection, score manipulation, position bias exploitation, few-shot hijacking, instruction override, format gaming.\n\\item \\textbf{Shared-bias attacks} exploit common cognitive biases: sycophancy amplification, verbosity bias, authority bias, style manipulation, length inflation, persona manipulation.\n\\end{itemize}\n\n\\subsection{Regression Specification}\n\nOur canonical specification is log-log OLS:\n\\begin{equation}\n\\log(\\text{ASR} + \\epsilon) = \\beta_0 + \\beta_1 \\log(K_{\\text{eff}}) + \\beta_2 \\log(\\eta_{\\max} + \\epsilon)\n\\label{eq:regression}\n\\end{equation}\nwhere $\\epsilon$ is a small constant for numerical stability. We report significance under four correction methods: standard OLS, clustered standard errors (CR1, 15 judge clusters), wild cluster bootstrap ($B=9999$, Rademacher weights, max-$p$ across 3 judge positions), and mixed effects (random judge intercepts). Panel non-independence arises because judges appear in multiple panels (e.g., claude-3-haiku appears in 91/455 panels), inflating standard errors by $\\sim$2.5$\\times$.\n\n\\subsection{Aggregation Rules}\n\nWe evaluate five aggregation rules: majority vote (baseline), accuracy-weighted vote, threshold (unanimity), Bayesian calibration (prior-weighted), and veto (single-judge override).\n\n\\section{Experiments}\n\n\\subsection{Core Results: Weakest-Link Dominance}\n\\label{sec:core}\n\nTable~\\ref{tab:correction} presents our primary results across 15 models, 455 panels, and 12 conditions (6 attack types $\\times$ 2 benchmarks). The pattern is stark: $\\eta_{\\max}$ dominates under all correction methods, while $K_{\\text{eff}}$'s significance collapses after accounting for panel non-independence.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{$\\eta_{\\max}$ sig} & \\textbf{$K_{\\text{eff}}$ sig} & \\textbf{$K_{\\text{eff}}$ dir} & \\textbf{Ratio} \\\\\n\\midrule\nOLS & 11/12 & 8/12 & 7+/1$-$ & 1.4:1 \\\\\nClustered SE & 8/12 & 0/12 & -- & $\\infty$ \\\\\nBootstrap v2 & 5/12 & 1/12 & 1+ & 5:1 \\\\\nMixed effects & 7/12 & 3/12 & 3+ & 2.3:1 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Correction method comparison (15 models, 455 panels, 12 conditions). $\\eta_{\\max}$ significance is robust across all methods; $K_{\\text{eff}}$ collapses from 8/12 under OLS to 0--1/12 after non-independence correction. SE inflation $\\sim$2.5$\\times$ is consistent with 91/455 panel overlap.}\n\\label{tab:correction}\n\\end{table}\n\nUnder OLS, both predictors appear significant ($\\eta_{\\max}$ 11/12, $K_{\\text{eff}}$ 8/12), producing a misleading near-parity (1.4:1). Clustered SE correction---which accounts for shared judge membership across panels---eliminates all $K_{\\text{eff}}$ significance (0/12) while retaining $\\eta_{\\max}$ at 8/12. The most conservative method (wild cluster bootstrap with max-$p$ across judge positions) gives a 5:1 dominance ratio. The $\\min(\\eta_{\\max})$ panel selection strategy wins 12/12 conditions with ASR advantages ranging from 3.8 to 51.1 percentage points.\n\n\\subsection{Attack Surface Expansion}\n\\label{sec:attack_expansion}\n\nTo confirm that $\\eta_{\\max}$ dominance is not an artifact of our initial attack selection, we extend to 3 additional attack types (few-shot hijacking, persona manipulation, instruction override), yielding 18 total conditions. Table~\\ref{tab:extended_attack} shows results under clustered SE.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Attack} & \\textbf{Mech.} & \\textbf{$\\eta_{\\max}$} & \\textbf{$K_{\\text{eff}}$} & \\textbf{GAM dir} \\\\\n\\midrule\nFew-shot hijack & targ. & \\checkmark\\checkmark & 0/2 & positive \\\\\nPersona manip. & shared & \\checkmark\\checkmark & 0/2 & negative \\\\\nInstr. override & targ. & 1/2 & 0/2 & positive \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Combined (18 cond.)}} & 13/18 & 0/18 & 10:8 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Extended attack taxonomy (clustered SE). $\\eta_{\\max}$ remains dominant across all new attack types. GAM taxonomy extends cleanly from 6:6 to 10:8 (targeted:shared-bias). $\\checkmark\\checkmark$ = significant on both benchmarks.}\n\\label{tab:extended_attack}\n\\end{table}\n\nThe combined dominance ratio under clustered SE is 13:0---$K_{\\text{eff}}$ achieves zero significance across all 18 conditions. The GAM taxonomy extends cleanly: few-shot hijacking and instruction override are classified as targeted (positive $K_{\\text{eff}}$), while persona manipulation is classified as shared-bias (negative $K_{\\text{eff}}$), extending the split from 6:6 to 10:8.\n\n\\subsection{Random-Fault BFT Contrast}\n\\label{sec:rf}\n\nTo provide causal evidence for BFT assumption failure, we construct a random-fault (RF) baseline via Monte Carlo simulation (10,000 iterations). Each judge fails independently with probability $\\eta_j = 1 - \\text{clean\\_accuracy}$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccl}\n\\toprule\n\\textbf{Metric} & \\textbf{Random Fault} & \\textbf{Adaptive} & \\textbf{Interpretation} \\\\\n\\midrule\n$K_{\\text{eff}}$ sig (OLS) & 2/2 & 8/12 & Both appear sig. \\\\\n$K_{\\text{eff}}$ sig (CL-SE) & 2/2 & 0/12 & RF genuine; adap. not \\\\\n$K_{\\text{eff}}$ sig (Boot.) & 2/2 & 1/12 & Consistent contrast \\\\\n$K_{\\text{eff}}$ std $\\beta$ & +0.297 & +0.164 & RF larger, genuine \\\\\n$R^2$ & 0.78--0.81 & 0.25--0.35 & Predictability gap \\\\\n$\\eta_{\\max}$ sig (all) & 2/2 & 5--8/12 & Genuine in both \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Random-fault vs.\\ adaptive regime contrast. $K_{\\text{eff}}$ is genuinely significant under i.i.d.\\ faults (2/2 under all corrections) but artifactual under adaptive attacks (0--1/12 after correction). The $R^2$ gap ($\\Delta = 0.48$) quantifies the unpredictability introduced by adaptive adversaries.}\n\\label{tab:rf_contrast}\n\\end{table}\n\nTable~\\ref{tab:rf_contrast} presents the contrast. Under random faults, $K_{\\text{eff}}$ is significant 2/2 under \\emph{all} correction methods ($p_{\\text{bootstrap}} = 0.003$ for MMLU, $<$0.001 for ARC), with $R^2 = 0.78$--$0.81$. Under adaptive attacks, the same predictor collapses to 0--1/12 after correction. This is not a direction reversal---$K_{\\text{eff}}$ is positively associated with vulnerability in \\emph{both} regimes. The difference is that the RF association is genuine (panel structure determines fault tolerance under i.i.d.\\ assumptions), while the adaptive association is inflated by panel overlap. The $R^2$ gap ($\\Delta = 0.48$) directly quantifies the strategic variance introduced by adaptive adversaries that panel structure cannot predict.\n\n\\subsection{ASR Concentration Analysis}\n\\label{sec:concentration}\n\nTo provide mechanistic evidence for $\\eta_{\\max}$ dominance, we compute per-judge ASR distributions within each panel and measure concentration via Gini coefficients and Shannon entropy.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Attack} & \\textbf{Cat.} & \\textbf{Gini} & \\textbf{Entropy} & \\textbf{Top-1 frac.} \\\\\n\\midrule\nPrompt inject. & targ. & 0.82 & 0.73 & 0.65 \\\\\nScore manip. & targ. & 0.79 & 0.78 & 0.62 \\\\\nPosition bias & targ. & 0.74 & 0.94 & 0.56 \\\\\nSycophancy & shared & 0.45 & 1.38 & 0.40 \\\\\nVerbosity bias & shared & 0.42 & 1.47 & 0.37 \\\\\nAuthority bias & shared & 0.41 & 1.50 & 0.36 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{ASR concentration by attack category. Targeted attacks show highly concentrated ASR (Gini $>$ 0.7, top-1 judge contributes $>$56\\% of panel ASR), providing mechanistic evidence for $\\eta_{\\max}$ dominance. Mann-Whitney $U$ test: $p < 0.001$ between categories.}\n\\label{tab:concentration}\n\\end{table}\n\nTable~\\ref{tab:concentration} reveals a sharp dichotomy. Under targeted attacks, ASR is highly concentrated: the most vulnerable judge contributes 56--65\\% of total panel ASR (mean Gini = 0.78). Under shared-bias attacks, ASR is more uniformly distributed (mean Gini = 0.43, top-1 fraction = 37\\%). The Gini--$\\eta_{\\max}$ correlation is $r = 0.83$, directly linking panel-level vulnerability to judge-level concentration. This independently validates the GAM taxonomy: targeted and shared-bias attacks differ not only in $K_{\\text{eff}}$ direction but in their micro-level ASR distribution patterns.\n\n\\subsection{Aggregation Gradient}\n\\label{sec:aggregation}\n\nWe evaluate five aggregation rules under clustered SE to characterize how vote aggregation modulates vulnerability.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccl}\n\\toprule\n\\textbf{Rule} & \\textbf{$\\eta_{\\max}$} & \\textbf{$K_{\\text{eff}}$} & \\textbf{Neg.} & \\textbf{$R^2$} & \\textbf{Position} \\\\\n\\midrule\nVeto & 11/12 & 0/12 & -- & 0.82 & Max vuln. \\\\\nThreshold & 10/12 & 4/12 & 1/4 & 0.87 & High \\\\\nMajority & 8/12 & 0/12 & -- & 0.28 & Moderate \\\\\nWeighted & 6/12 & 1/12 & 0/1 & 0.26 & Low-mod. \\\\\nBayesian & 5/12 & 4/12 & 3/4 & 0.09 & Min vuln. \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Aggregation gradient under clustered SE. ``Neg.'' = fraction of significant $K_{\\text{eff}}$ coefficients that are negative. Bayesian calibration weakens $\\eta_{\\max}$ (11$\\to$5/12) and flips $K_{\\text{eff}}$ direction (3/4 negative), while veto/threshold amplify the weakest-link channel.}\n\\label{tab:aggregation}\n\\end{table}\n\nTable~\\ref{tab:aggregation} reveals a gradient from maximum to minimum vulnerability. Veto rule (any single judge can override) maximizes $\\eta_{\\max}$ dominance (11/12) with $K_{\\text{eff}}$ completely suppressed. Threshold voting (unanimity) amplifies both channels ($R^2 = 0.87$). Bayesian calibration, which down-weights unreliable judges using prior accuracy estimates, achieves the strongest mitigation: $\\eta_{\\max}$ drops to 5/12 and $K_{\\text{eff}}$ flips to majority-negative (3/4 significant coefficients negative), meaning diversity becomes protective.\n\nUnder bootstrap, Bayesian $K_{\\text{eff}}$ shows 3/12 significant---all negative (3/3 negative fraction = 100\\%). This directional flip is the cleanest evidence that aggregation is an independent control lever, unaffected by the non-independence concerns that plague the diversity analysis.\n\n\\subsection{Panel Design Algorithm}\n\\label{sec:design}\n\nWe benchmark a two-stage robustness-first algorithm against 6 baseline strategies across 12 conditions.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Strategy} & \\textbf{Mean ASR} & \\textbf{Rank} & \\textbf{$\\Delta$ vs.\\ random (pp)} \\\\\n\\midrule\nTwo-stage & 0.112 & 1 & $-$8.3 \\\\\n$\\min(\\eta_{\\max})$ & 0.119 & 2 & $-$7.6 \\\\\nStrongest-$K$ & 0.131 & 3 & $-$6.4 \\\\\nUniform family & 0.158 & 4 & $-$3.7 \\\\\nMax disagreement & 0.172 & 5 & $-$2.3 \\\\\nRandom & 0.195 & 6 & 0.0 \\\\\n$\\max(K_{\\text{eff}})$ & 0.208 & 7 & $+$1.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Panel design strategy comparison (mean ASR across 12 conditions). The $\\max(K_{\\text{eff}})$ strategy---the intuitive ``maximize diversity'' approach---performs \\emph{worse} than random selection because it introduces weak models. Two-stage provides a marginal 0.7pp improvement over $\\min(\\eta_{\\max})$ alone.}\n\\label{tab:strategy}\n\\end{table}\n\nTable~\\ref{tab:strategy} presents the ranking. The most striking result is that $\\max(K_{\\text{eff}})$---the intuitive ``diversify your panel'' strategy---ranks \\emph{last}, performing 1.3pp worse than random selection. This occurs because maximizing diversity necessarily introduces weaker models (the diversity-capability tradeoff, $r = 0.70$). The two-stage algorithm provides a consistent but modest improvement (0.7pp) over pure $\\min(\\eta_{\\max})$, with the marginal gain concentrated in targeted attack conditions (5/6 wins, mean $\\Delta = -1.1$pp) where controlled $K_{\\text{eff}}$ optimization adds value after robustness screening.\n\n\\subsection{Capability-Matched Validation}\n\\label{sec:capability}\n\nTo disentangle $\\eta_{\\max}$ and $K_{\\text{eff}}$ (confound $r = 0.70$ in the full pool), we conduct within-tier analysis using 9 base-tier models (84 panels), which reduces the confound to $r = 0.35$ and $\\eta_{\\max}$ variance by 65--70\\%.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Setting} & \\textbf{Panels} & \\textbf{$r$} & \\textbf{$\\eta_{\\max}$ (CL)} & \\textbf{$K_{\\text{eff}}$ (CL)} \\\\\n\\midrule\nFull pool & 455 & 0.70 & 8/12 & 0/12 \\\\\nBase tier & 84 & 0.35 & 4/12 & 2/12 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-tier vs.\\ within-tier comparison (clustered SE). Controlling for capability reduces confound and reveals $K_{\\text{eff}}$ as a weak but detectable secondary factor (2/12, both in targeted conditions). The dominance ratio narrows from $\\infty$ to 2:1, but $\\eta_{\\max}$ still dominates.}\n\\label{tab:capability}\n\\end{table}\n\nWithin the base tier (Table~\\ref{tab:capability}), $K_{\\text{eff}}$ emerges as a weak secondary factor (2/12 significant under clustered SE), with the dominance ratio narrowing from $\\infty$ to 2:1. Both significant $K_{\\text{eff}}$ conditions are targeted attacks (mmlu$\\times$prompt\\_injection, $\\beta = +0.31$, $p = 0.028$; mmlu$\\times$score\\_manipulation, $\\beta = +0.25$, $p = 0.041$), consistent with the GAM taxonomy. The within-tier $R^2$ mean drops to 0.18 (vs.\\ 0.30 in the full pool), confirming that cross-tier $\\eta_{\\max}$ variance is the primary source of predictive power.\n\n\\subsection{Diversity-Capability Tradeoff}\n\\label{sec:tradeoff}\n\nThe structural correlation between $K_{\\text{eff}}$ and $\\eta_{\\max}$ ($r = 0.70$, 95\\% CI $[0.66, 0.74]$) reflects a fundamental constraint in the current LLM ecosystem: maximizing behavioral diversity requires including models from different capability tiers, which inevitably introduces weaker judges. This correlation is strongest within model families ($r = 0.81$) and weakest at the frontier tier ($r = 0.35$), where architectural differences provide diversity without large capability gaps. The Pareto frontier analysis shows that 97.4\\% of panels are dominated, with optimal panels clustering in the low-$K_{\\text{eff}}$, low-$\\eta_{\\max}$ region. VIF analysis confirms moderate but non-pathological multicollinearity (VIF = 2.96, condition number = 4.8), with partial correlations of $r(\\eta_{\\max}, \\text{ASR} \\mid K_{\\text{eff}}) = 0.42$ vs.\\ $r(K_{\\text{eff}}, \\text{ASR} \\mid \\eta_{\\max}) = 0.18$.\n\n\\subsection{Panel Size Sensitivity}\n\\label{sec:panel_size}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{$K$} & \\textbf{Panels} & \\textbf{$\\eta_{\\max}$} & \\textbf{$K_{\\text{eff}}$} & \\textbf{Ratio} & \\textbf{SE infl.} \\\\\n\\midrule\n3 & 455 & 8/12 & 0/12 & $\\infty$ & 2.5$\\times$ \\\\\n5 & 3003 & 9/12 & 1/12 & 9:1 & 4.1$\\times$ \\\\\n7 & 6435 & 9/12 & 1/12 & 9:1 & 6.3$\\times$ \\\\\n9 & 5005 & 8/12 & 2/12 & 4:1 & 7.8$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Panel size sensitivity (clustered SE). $\\eta_{\\max}$ dominance persists across $K=3$--$9$, confirming the weakest-link mechanism is scale-invariant. SE inflation increases sharply with $K$, underscoring the necessity of non-independence correction in combinatorial designs.}\n\\label{tab:panel_size}\n\\end{table}\n\nTable~\\ref{tab:panel_size} demonstrates that $\\eta_{\\max}$ dominance is not an artifact of small panels. Across $K = 3$ to $K = 9$, the $\\eta_{\\max}$ effect size decreases slightly (standardized $\\beta$: 0.42 to 0.31) as larger panels provide more majority-vote fault tolerance, but the dominance ratio remains $\\geq$4:1. The $\\min(\\eta_{\\max})$ strategy wins 12/12 conditions at every panel size. SE inflation increases from 2.5$\\times$ to 7.8$\\times$, providing compelling evidence that non-independence correction is essential for panel studies at any scale.\n\n\\subsection{Generation Benchmark Extension}\n\\label{sec:generation}\n\nTo rule out MCQ-specific artifacts, we extend to MT-Bench, an open-ended generation benchmark with 1--10 scale scoring. We test 3 generation-specific attack types across 12 available models and 220 panels.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Format} & \\textbf{$\\eta_{\\max}$ (CL)} & \\textbf{$K_{\\text{eff}}$ (CL)} & \\textbf{Ratio} \\\\\n\\midrule\nMCQ (MMLU+ARC) & 8/12 & 0/12 & $\\infty$ \\\\\nGeneration (MT-Bench) & 4/6 & 0/6 & $\\infty$ \\\\\nCombined & 12/18 & 0/18 & $\\infty$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-format consistency (clustered SE). $\\eta_{\\max}$ dominance generalizes from MCQ to open-ended generation evaluation. The combined ratio across 18 conditions is $\\infty$ (12:0).}\n\\label{tab:generation}\n\\end{table}\n\nTable~\\ref{tab:generation} confirms that $\\eta_{\\max}$ dominance generalizes across evaluation formats. Under clustered SE, the combined dominance ratio is 12:0 across 18 conditions. GAM classification of generation attacks aligns with the mechanistic taxonomy: style manipulation and length inflation are shared-bias (negative $K_{\\text{eff}}$), while format gaming is targeted (positive $K_{\\text{eff}}$). The $\\min(\\eta_{\\max})$ strategy wins 6/6 generation conditions, confirming the practical recommendation is format-agnostic.\n\n\\subsection{Partial-Knowledge Adversary}\n\\label{sec:partial}\n\nReal-world adversaries rarely have full knowledge of panel composition. We simulate three knowledge levels: full (baseline), family-only (adversary knows model family labels but not specific vulnerability profiles), and random (no targeting).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Knowledge} & \\textbf{ASR} & \\textbf{$\\eta_{\\max}$ (CL)} & \\textbf{$K_{\\text{eff}}$ (CL)} & \\textbf{$R^2$} \\\\\n\\midrule\nFull & 0.195 & 8/12 & 0/12 & 0.30 \\\\\nFamily-only & 0.160 & 7/12 & 0/12 & 0.24 \\\\\nRandom & 0.113 & 3/12 & 0/12 & 0.08 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Adversary knowledge level comparison (clustered SE). Family-only knowledge retains 82\\% attack efficiency. $K_{\\text{eff}}$ is 0/12 under all knowledge levels. $\\eta_{\\max}$ dominance persists under realistic threat models.}\n\\label{tab:partial}\n\\end{table}\n\nTable~\\ref{tab:partial} reveals that family-level knowledge retains 82\\% of full-knowledge attack efficiency ($\\text{ASR} = 0.160$ vs.\\ $0.195$), because same-family models share training pipeline and architectural biases ($r_{\\text{family-vulnerability}} = 0.61$). Defenders cannot rely on panel composition secrecy: family labels are easily inferred from API endpoints and response styles. $K_{\\text{eff}}$ remains 0/12 under all knowledge levels, and $\\eta_{\\max}$ dominance persists even under family-only targeting (7/12), confirming the core findings are robust to adversary capability assumptions.\n\n\\section{Discussion}\n\n\\paragraph{When diversity helps.} Our results do not imply diversity is universally harmful. Under shared-bias attacks, GAM analysis consistently shows negative $K_{\\text{eff}}$ direction (8/8 conditions including extended attacks), meaning diversity provides partial immunity when the adversary exploits biases shared across model families. After robustness screening removes weak judges, the diversity-capability tradeoff is weakened ($r$ drops from 0.70 to 0.35), creating conditions where diversity optimization adds marginal value. And in non-adversarial settings, diversity remains beneficial for reducing calibration errors and position biases.\n\n\\paragraph{Practical recommendations.} Based on our findings, we recommend a defense stack combining: (1) robustness-first screening to eliminate $\\eta_{\\max}$ as a vulnerability driver, and (2) Bayesian aggregation to reverse $K_{\\text{eff}}$ from harmful to protective. This dual-channel approach addresses both structural vulnerability drivers. The $\\max(K_{\\text{eff}})$ strategy should be explicitly avoided, as it performs worse than random selection.\n\n\\paragraph{Methodological implications.} The dramatic significance shift from OLS to clustered SE ($K_{\\text{eff}}$: 8/12 $\\to$ 0/12) is a cautionary finding for all combinatorial evaluation designs where the same items (here, judges) appear in multiple experimental units (panels). SE inflation of 2.5--7.8$\\times$ can produce severely misleading conclusions. We recommend that future panel studies routinely report clustered SE alongside OLS.\n\n\\section{Conclusion}\n\nWe conducted the first large-scale empirical decomposition of multi-judge LLM evaluation panel vulnerability. Our central finding---that panel vulnerability is dominated by the weakest individual judge, not panel diversity---challenges the implicit BFT assumption underlying multi-judge evaluation design. The dominance ratio of 5:1 ($\\eta_{\\max}$ over $K_{\\text{eff}}$) is robust across 9 attack types, 3 benchmarks, 4 panel sizes, 3 adversary knowledge levels, and 4 statistical correction methods. Aggregation rule choice provides an independent control lever: Bayesian calibration reverses diversity's role from vulnerability to defense. We release our two-stage panel design algorithm as a practical tool for building adversarially robust evaluation panels.\n\n\\section*{Limitations}\n\nOur study has three main limitations. First, the model pool (15 models, 6 families) represents the current LLM ecosystem; the diversity-capability tradeoff ($r = 0.70$) may weaken as more capable open-source models become available. Second, our adaptive adversary model assumes strategic targeting of individual judges---real-world adversaries may face additional constraints (e.g., limited query budgets) that reduce attack efficiency below the levels we measure. Third, the Bayesian aggregation defense requires access to clean-data accuracy estimates, which may themselves be subject to manipulation; evaluating the robustness of the defense stack to meta-adversarial attacks remains future work.\n\n\\bibliography{custom}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "58408cf6-eaa7-4176-98ed-dbe79bd1e42b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T221131 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_…",
  "leafUuid": "49309ec1-e232-4b0d-908b-5cbaae9bec70",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate EMNLP-2026 paper on certification manipulation",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344"
}
```

---

### Assistant

_source line 27 · 2026-05-22T22:39:58.701Z_

Now let me compile the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49309ec1-e232-4b0d-908b-5cbaae9bec70",
  "isSidechain": false,
  "requestId": "req_011CbJQp5nHGC2MMw74pNMuA",
  "type": "assistant",
  "uuid": "caff34db-5537-485a-9811-07fef82a35e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013hvFrSSUvj4ZNcxu6wvazH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10049,
      "cache_read_input_tokens": 52059,
      "output_tokens": 154,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10049,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 154,
          "cache_read_input_tokens": 52059,
          "cache_creation_input_tokens": 10049,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10049
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

_source line 28 · 2026-05-22T22:40:00.374Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01GE56DdogMxVcDDvNJ5xGqh`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "First pass pdflatex compilation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "caff34db-5537-485a-9811-07fef82a35e1",
  "isSidechain": false,
  "requestId": "req_011CbJQp5nHGC2MMw74pNMuA",
  "type": "assistant",
  "uuid": "4ecc1464-72de-4edb-971e-8bdbb78a3d1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013hvFrSSUvj4ZNcxu6wvazH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10049,
      "cache_read_input_tokens": 52059,
      "output_tokens": 154,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10049,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 154,
          "cache_read_input_tokens": 52059,
          "cache_creation_input_tokens": 10049,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10049
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

_source line 29 · 2026-05-22T22:40:00.520Z_

<details><summary>↩ Tool result · `toolu_01GE56DdogMxVcDDvNJ5xGqh`</summary>

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
  "parentUuid": "4ecc1464-72de-4edb-971e-8bdbb78a3d1f",
  "isSidechain": false,
  "promptId": "d5483bc6-a830-4026-80bc-d9c580d884bc",
  "type": "user",
  "uuid": "dc764a3b-e31e-4f57-ad16-3ebb1e3b18fd",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `acl.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "4ecc1464-72de-4edb-971e-8bdbb78a3d1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-22T22:40:00.523Z_

```json
{
  "parentUuid": "dc764a3b-e31e-4f57-ad16-3ebb1e3b18fd",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "d2c1c56c-fc8c-4930-92c7-a3145513bf3c",
  "timestamp": "2026-05-22T22:40:00.523Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 31 · 2026-05-22T22:40:06.624Z_

<details><summary>Logged reasoning block</summary>

```text
The ACL style file is not found. Let me check what's available and switch to a standard article class or find the ACL style file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2c1c56c-fc8c-4930-92c7-a3145513bf3c",
  "isSidechain": false,
  "requestId": "req_011CbJQpPaM62n8XgD2F4ztJ",
  "type": "assistant",
  "uuid": "ef6beacd-065d-48b9-81c5-e89cf7023831",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QWo5h4xczJ2WxXGcsFG2uN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 539,
      "cache_read_input_tokens": 62108,
      "output_tokens": 524,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 539,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 524,
          "cache_read_input_tokens": 62108,
          "cache_creation_input_tokens": 539,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 539
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

_source line 32 · 2026-05-22T22:40:07.155Z_

ACL style not available. Let me switch to a standard article class with appropriate formatting.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef6beacd-065d-48b9-81c5-e89cf7023831",
  "isSidechain": false,
  "requestId": "req_011CbJQpPaM62n8XgD2F4ztJ",
  "type": "assistant",
  "uuid": "522e898c-a8d4-47d3-ad33-847dabdc709d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QWo5h4xczJ2WxXGcsFG2uN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 539,
      "cache_read_input_tokens": 62108,
      "output_tokens": 524,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 539,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 524,
          "cache_read_input_tokens": 62108,
          "cache_creation_input_tokens": 539,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 539
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

_source line 33 · 2026-05-22T22:40:11.639Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01QUuMuugPNSB4T5CwivATZN`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best/paper.tex",
  "old_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage{tablefootnote}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage{hyperref}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{natbib}\n\\renewcommand{\\bibsection}{\\section*{References}}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "522e898c-a8d4-47d3-ad33-847dabdc709d",
  "isSidechain": false,
  "requestId": "req_011CbJQpPaM62n8XgD2F4ztJ",
  "type": "assistant",
  "uuid": "55234f49-e4be-44ce-8b06-ebda81b6928a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QWo5h4xczJ2WxXGcsFG2uN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 539,
      "cache_read_input_tokens": 62108,
      "output_tokens": 524,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 539,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 524,
          "cache_read_input_tokens": 62108,
          "cache_creation_input_tokens": 539,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 539
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

_source line 34 · 2026-05-22T22:40:11.665Z_

<details><summary>↩ Tool result · `toolu_01QUuMuugPNSB4T5CwivATZN`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "55234f49-e4be-44ce-8b06-ebda81b6928a",
  "isSidechain": false,
  "promptId": "d5483bc6-a830-4026-80bc-d9c580d884bc",
  "type": "user",
  "uuid": "dca219f8-4e3c-410d-8fd8-9d3d5119ab4e",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best/paper.tex",
    "oldString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage{tablefootnote}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage{hyperref}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{natbib}\n\\renewcommand{\\bibsection}{\\section*{References}}",
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
          "+\\usepackage[margin=2.5cm]{geometry}",
          " \\usepackage{times}",
          " \\usepackage{latexsym}",
          " \\usepackage{amsmath}"
        ]
      },
      {
        "oldStart": 9,
        "oldLines": 9,
        "newStart": 9,
        "newLines": 11,
        "lines": [
          " \\usepackage{graphicx}",
          " \\usepackage{xcolor}",
          " \\usepackage{enumitem}",
          "-\\usepackage{tablefootnote}",
          "+\\usepackage{hyperref}",
          " \\usepackage[T1]{fontenc}",
          " \\usepackage[utf8]{inputenc}",
          "+\\usepackage{natbib}",
          "+\\renewcommand{\\bibsection}{\\section*{References}}",
          " ",
          " \\title{Weakest Link, Not Diversity: Adversarial Vulnerability in Multi-Judge LLM Evaluation}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "55234f49-e4be-44ce-8b06-ebda81b6928a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-22T22:40:28.239Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01FsD3r7LywWGgbxEj2DkDDV`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best/paper.tex",
  "old_string": "\\bibliography{custom}\n\n\\end{document}",
  "new_string": "\\begin{thebibliography}{9}\n\\bibitem{zheng2023judging}\nLianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric P.\\ Xing, Hao Zhang, Joseph E.\\ Gonzalez, and Ion Stoica.\n\\newblock Judging {LLM}-as-a-{J}udge with {MT-B}ench and {C}hatbot {A}rena.\n\\newblock In \\emph{Advances in Neural Information Processing Systems}, 2023.\n\n\\bibitem{lamport1982byzantine}\nLeslie Lamport, Robert Shostak, and Marshall Pease.\n\\newblock The {B}yzantine generals problem.\n\\newblock \\emph{ACM Transactions on Programming Languages and Systems}, 4(3):382--401, 1982.\n\n\\bibitem{hendrycks2021mmlu}\nDan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, and Jacob Steinhardt.\n\\newblock Measuring massive multitask language understanding.\n\\newblock In \\emph{International Conference on Learning Representations}, 2021.\n\n\\bibitem{clark2018arc}\nPeter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot, Ashish Sabharwal, Carissa Schoenick, and Oyvind Tafjord.\n\\newblock Think you have solved question answering? {T}ry {ARC}, the {AI2} reasoning challenge.\n\\newblock \\emph{arXiv preprint arXiv:1803.05457}, 2018.\n\n\\bibitem{perez2022red}\nEthan Perez, Saffron Huang, Francis Song, Trevor Cai, Roman Ring, John Aslanides, Amelia Glaese, Nat McAleese, and Geoffrey Irving.\n\\newblock Red teaming language models with language models.\n\\newblock In \\emph{Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing}, 2022.\n\n\\bibitem{panickssery2024llm}\nArjun Panickssery, Samuel R.\\ Bowman, and Shi Feng.\n\\newblock {LLM} evaluators recognize and favor their own generations.\n\\newblock \\emph{arXiv preprint arXiv:2404.13076}, 2024.\n\n\\bibitem{raina2024llm}\nVyas Raina, Adian Liusie, and Mark J.\\ F.\\ Gales.\n\\newblock Is {LLM}-as-a-{J}udge robust? {I}nvestigating universal adversarial attacks on zero-shot {LLM} assessment.\n\\newblock In \\emph{Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing}, 2024.\n\\end{thebibliography}\n\n\\end{document}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dca219f8-4e3c-410d-8fd8-9d3d5119ab4e",
  "isSidechain": false,
  "requestId": "req_011CbJQqDF29JMBAsPwrBfkX",
  "type": "assistant",
  "uuid": "19c06d07-db39-491f-86f8-ddad0b9f6db5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019MU3Q6pfTbUAfEhvHvQPEJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 612,
      "cache_read_input_tokens": 62647,
      "output_tokens": 924,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 612,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 924,
          "cache_read_input_tokens": 62647,
          "cache_creation_input_tokens": 612,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 612
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

_source line 36 · 2026-05-22T22:40:28.252Z_

<details><summary>↩ Tool result · `toolu_01FsD3r7LywWGgbxEj2DkDDV`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19c06d07-db39-491f-86f8-ddad0b9f6db5",
  "isSidechain": false,
  "promptId": "d5483bc6-a830-4026-80bc-d9c580d884bc",
  "type": "user",
  "uuid": "ae91bbf3-5953-43c9-94ba-58ca6d2d7006",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best/paper.tex",
    "oldString": "\\bibliography{custom}\n\n\\end{document}",
    "newString": "\\begin{thebibliography}{9}\n\\bibitem{zheng2023judging}\nLianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric P.\\ Xing, Hao Zhang, Joseph E.\\ Gonzalez, and Ion Stoica.\n\\newblock Judging {LLM}-as-a-{J}udge with {MT-B}ench and {C}hatbot {A}rena.\n\\newblock In \\emph{Advances in Neural Information Processing Systems}, 2023.\n\n\\bibitem{lamport1982byzantine}\nLeslie Lamport, Robert Shostak, and Marshall Pease.\n\\newblock The {B}yzantine generals problem.\n\\newblock \\emph{ACM Transactions on Programming Languages and Systems}, 4(3):382--401, 1982.\n\n\\bibitem{hendrycks2021mmlu}\nDan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, and Jacob Steinhardt.\n\\newblock Measuring massive multitask language understanding.\n\\newblock In \\emph{International Conference on Learning Representations}, 2021.\n\n\\bibitem{clark2018arc}\nPeter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot, Ashish Sabharwal, Carissa Schoenick, and Oyvind Tafjord.\n\\newblock Think you have solved question answering? {T}ry {ARC}, the {AI2} reasoning challenge.\n\\newblock \\emph{arXiv preprint arXiv:1803.05457}, 2018.\n\n\\bibitem{perez2022red}\nEthan Perez, Saffron Huang, Francis Song, Trevor Cai, Roman Ring, John Aslanides, Amelia Glaese, Nat McAleese, and Geoffrey Irving.\n\\newblock Red teaming language models with language models.\n\\newblock In \\emph{Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing}, 2022.\n\n\\bibitem{panickssery2024llm}\nArjun Panickssery, Samuel R.\\ Bowman, and Shi Feng.\n\\newblock {LLM} evaluators recognize and favor their own generations.\n\\newblock \\emph{arXiv preprint arXiv:2404.13076}, 2024.\n\n\\bibitem{raina2024llm}\nVyas Raina, Adian Liusie, and Mark J.\\ F.\\ Gales.\n\\newblock Is {LLM}-as-a-{J}udge robust? {I}nvestigating universal adversarial attacks on zero-shot {LLM} assessment.\n\\newblock In \\emph{Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing}, 2024.\n\\end{thebibliography}\n\n\\end{document}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 358,
        "oldLines": 6,
        "newStart": 358,
        "newLines": 41,
        "lines": [
          " ",
          " Our study has three main limitations. First, the model pool (15 models, 6 families) represents the current LLM ecosystem; the diversity-capability tradeoff ($r = 0.70$) may weaken as more capable open-source models become available. Second, our adaptive adversary model assumes strategic targeting of individual judges---real-world adversaries may face additional constraints (e.g., limited query budgets) that reduce attack efficiency below the levels we measure. Third, the Bayesian aggregation defense requires access to clean-data accuracy estimates, which may themselves be subject to manipulation; evaluating the robustness of the defense stack to meta-adversarial attacks remains future work.",
          " ",
          "-\\bibliography{custom}",
          "+\\begin{thebibliography}{9}",
          "+\\bibitem{zheng2023judging}",
          "+Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric P.\\ Xing, Hao Zhang, Joseph E.\\ Gonzalez, and Ion Stoica.",
          "+\\newblock Judging {LLM}-as-a-{J}udge with {MT-B}ench and {C}hatbot {A}rena.",
          "+\\newblock In \\emph{Advances in Neural Information Processing Systems}, 2023.",
          " ",
          "+\\bibitem{lamport1982byzantine}",
          "+Leslie Lamport, Robert Shostak, and Marshall Pease.",
          "+\\newblock The {B}yzantine generals problem.",
          "+\\newblock \\emph{ACM Transactions on Programming Languages and Systems}, 4(3):382--401, 1982.",
          "+",
          "+\\bibitem{hendrycks2021mmlu}",
          "+Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, and Jacob Steinhardt.",
          "+\\newblock Measuring massive multitask language understanding.",
          "+\\newblock In \\emph{International Conference on Learning Representations}, 2021.",
          "+",
          "+\\bibitem{clark2018arc}",
          "+Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot, Ashish Sabharwal, Carissa Schoenick, and Oyvind Tafjord.",
          "+\\newblock Think you have solved question answering? {T}ry {ARC}, the {AI2} reasoning challenge.",
          "+\\newblock \\emph{arXiv preprint arXiv:1803.05457}, 2018.",
          "+",
          "+\\bibitem{perez2022red}",
          "+Ethan Perez, Saffron Huang, Francis Song, Trevor Cai, Roman Ring, John Aslanides, Amelia Glaese, Nat McAleese, and Geoffrey Irving.",
          "+\\newblock Red teaming language models with language models.",
          "+\\newblock In \\emph{Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing}, 2022.",
          "+",
          "+\\bibitem{panickssery2024llm}",
          "+Arjun Panickssery, Samuel R.\\ Bowman, and Shi Feng.",
          "+\\newblock {LLM} evaluators recognize and favor their own generations.",
          "+\\newblock \\emph{arXiv preprint arXiv:2404.13076}, 2024.",
          "+",
          "+\\bibitem{raina2024llm}",
          "+Vyas Raina, Adian Liusie, and Mark J.\\ F.\\ Gales.",
          "+\\newblock Is {LLM}-as-a-{J}udge robust? {I}nvestigating universal adversarial attacks on zero-shot {LLM} assessment.",
          "+\\newblock In \\emph{Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing}, 2024.",
          "+\\end{thebibliography}",
          "+",
          " \\end{document}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "19c06d07-db39-491f-86f8-ddad0b9f6db5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-22T22:40:31.962Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01CF6aRjgBYT7fmrRfx2ryAB`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "First pass pdflatex compilation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae91bbf3-5953-43c9-94ba-58ca6d2d7006",
  "isSidechain": false,
  "requestId": "req_011CbJQrSN61qc5pSfVYKuya",
  "type": "assistant",
  "uuid": "a151a524-b511-4712-9cb0-f651d166a585",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Ai95nrsUVhWXGdvgPPCz4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1012,
      "cache_read_input_tokens": 63259,
      "output_tokens": 146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1012,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 146,
          "cache_read_input_tokens": 63259,
          "cache_creation_input_tokens": 1012,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1012
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

_source line 38 · 2026-05-22T22:40:32.450Z_

<details><summary>↩ Tool result · `toolu_01CF6aRjgBYT7fmrRfx2ryAB`</summary>

```text
Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm
/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/us
r/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive
/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fon
ts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (9 pages, 169639 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a151a524-b511-4712-9cb0-f651d166a585",
  "isSidechain": false,
  "promptId": "d5483bc6-a830-4026-80bc-d9c580d884bc",
  "type": "user",
  "uuid": "3501568f-8ff6-4060-9ead-14b66fc650ab",
  "toolUseResult": {
    "stdout": "Package rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\n/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/us\nr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive\n/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fon\nts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (9 pages, 169639 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "a151a524-b511-4712-9cb0-f651d166a585",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-22T22:40:35.627Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01X8Dth9LPBy2u5dtSZbDuZV`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5",
  "description": "Second pass pdflatex compilation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3501568f-8ff6-4060-9ead-14b66fc650ab",
  "isSidechain": false,
  "requestId": "req_011CbJQrkN4H1qJGNZi6s6Gw",
  "type": "assistant",
  "uuid": "16a361ce-ccac-4851-a40f-a843616e8fd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015qDsyiegCpvoe5aZNpF7VC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 628,
      "cache_read_input_tokens": 64271,
      "output_tokens": 146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 628,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 146,
          "cache_read_input_tokens": 64271,
          "cache_creation_input_tokens": 628,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 628
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

_source line 40 · 2026-05-22T22:40:36.123Z_

<details><summary>↩ Tool result · `toolu_01X8Dth9LPBy2u5dtSZbDuZV`</summary>

```text
r/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive
/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fon
ts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (9 pages, 171342 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "16a361ce-ccac-4851-a40f-a843616e8fd1",
  "isSidechain": false,
  "promptId": "d5483bc6-a830-4026-80bc-d9c580d884bc",
  "type": "user",
  "uuid": "71b43cde-b08c-4862-9b6a-633849405c7a",
  "toolUseResult": {
    "stdout": "r/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive\n/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fon\nts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (9 pages, 171342 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "16a361ce-ccac-4851-a40f-a843616e8fd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-22T22:40:48.143Z_

编译成功，PDF 已生成（9 页）。

论文覆盖了 `experiment_data.json` 中全部 12 个实验，对应以下结构：
- **Table 1** (§4.1): 核心校正方法对比（15 模型 × 455 panels × 12 conditions）
- **Table 2** (§4.2): 扩展攻击分类（新增 3 种攻击，18 conditions）
- **Table 3** (§4.3): RF vs Adaptive 因果对照
- **Table 4** (§4.4): ASR 浓度分析（Gini/Entropy 微观机制证据）
- **Table 5** (§4.5): 聚合规则梯度（5 种投票规则）
- **Table 6** (§4.6): 面板设计策略排名（7 种策略）
- **Table 7** (§4.7): Capability-matched validation
- **§4.8**: 多样性-能力 tradeoff + VIF 诊断（文字段落）
- **Table 8** (§4.9): Panel size sensitivity（K=3,5,7,9）
- **Table 9** (§4.10): 跨格式一致性（MCQ vs Generation）
- **Table 10** (§4.11): 部分知识对手模型

所有定量 claim 均取自实验数据，未编造数字。输出路径：`artifacts/dream_reports/dream_20260522T221131/best/paper.pdf`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71b43cde-b08c-4862-9b6a-633849405c7a",
  "isSidechain": false,
  "requestId": "req_011CbJQs1oFWY5Qohimsa5nF",
  "type": "assistant",
  "uuid": "e73c5b08-2ceb-47a1-a2a7-9378de42018d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhbrTRH9EeNsAwh6ij5m9C",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 238,
      "cache_read_input_tokens": 64899,
      "output_tokens": 423,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 238,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 423,
          "cache_read_input_tokens": 64899,
          "cache_creation_input_tokens": 238,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 238
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T221131 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_…",
  "leafUuid": "e73c5b08-2ceb-47a1-a2a7-9378de42018d",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate EMNLP-2026 paper on certification manipulation",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T221131 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_…",
  "leafUuid": "e73c5b08-2ceb-47a1-a2a7-9378de42018d",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate EMNLP-2026 paper on certification manipulation",
  "sessionId": "ca7c92ca-7226-4597-b435-bb7be4a94344"
}
```

---
