# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260524T081135 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-3/3d2d4040-5c67-4419-9f32-36942b3022a1.jsonl`
- **Structured JSON:** [`8921fcdaec9eaf291dba.json`](../../sessions/89/8921fcdaec9eaf291dba.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-24T08:57:51.505Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-24T08:57:51.505Z",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260524T081135 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst/experiment_data.json`（先 Read 此文件）\n- Venue：emnlp-2026\n- Narrative guidance：放弃 'discover→diagnose→remedy' 弧。Llama SS 失败（AR GAR β=0 ≈ 0.04，gap ~12×）证明 SS 是 model-specific，不可泛化为 general mitigation。 Reframe 为纯 mechanistic diagnostic paper。Title 改为 'Why Auxiliary Attention Losses Fail Under Exposure Bias: A Multi-Model Diagnostic Study'。 SS 从 Results 独立小节降级为 Discussion 'attempted mitigation'，承认 model-specific 局限。核心卖点转为 failure mode taxonomy （NF1 反向 turn conditioning + NF2 distribution shift + NF3 干预强度不足）的系统分类学价值。 加强 PCGrad 'first empirical elimination of gradient conflict hypothesis' 叙事。加强 Dongre convergent failure evidence： 两种干预 × 两种模型 = 4 paths all fail on Llama。Introduction 结尾加 'our negative results establish concrete failure modes that future work must overcome'。Discussion 加 concrete next steps（data-dependent SS schedule、curriculum exposure、inference-time only）。 仍冲 EMNLP Findings 2.5-3.0，靠 systematic rigor + cross-model replication + failure taxonomy。 审稿人 novelty objection probability 0.7-1.0，fatal/severe concerns 3-5 remaining。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-24T08:57:51.508Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-24T08:57:51.508Z",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1"
}
```

---

## Round 1

43 recorded events

### User

_source line 3 · 2026-05-24T08:57:51.530Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260524T081135 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst/experiment_data.json`（先 Read 此文件）
- Venue：emnlp-2026
- Narrative guidance：放弃 'discover→diagnose→remedy' 弧。Llama SS 失败（AR GAR β=0 ≈ 0.04，gap ~12×）证明 SS 是 model-specific，不可泛化为 general mitigation。 Reframe 为纯 mechanistic diagnostic paper。Title 改为 'Why Auxiliary Attention Losses Fail Under Exposure Bias: A Multi-Model Diagnostic Study'。 SS 从 Results 独立小节降级为 Discussion 'attempted mitigation'，承认 model-specific 局限。核心卖点转为 failure mode taxonomy （NF1 反向 turn conditioning + NF2 distribution shift + NF3 干预强度不足）的系统分类学价值。 加强 PCGrad 'first empirical elimination of gradient conflict hypothesis' 叙事。加强 Dongre convergent failure evidence： 两种干预 × 两种模型 = 4 paths all fail on Llama。Introduction 结尾加 'our negative results establish concrete failure modes that future work must overcome'。Discussion 加 concrete next steps（data-dependent SS schedule、curriculum exposure、inference-time only）。 仍冲 EMNLP Findings 2.5-3.0，靠 systematic rigor + cross-model replication + failure taxonomy。 审稿人 novelty objection probability 0.7-1.0，fatal/severe concerns 3-5 remaining。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "4e9b6b3b-bc11-45d7-a0d2-4aaa1c0c9272",
  "type": "user",
  "uuid": "da9c1e1d-1784-40f1-8233-93568cb7fff7",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-24T08:57:51.529Z_

```json
{
  "parentUuid": "da9c1e1d-1784-40f1-8233-93568cb7fff7",
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
  "uuid": "b07d85b9-f21f-4b8e-ba92-3e607774c4a6",
  "timestamp": "2026-05-24T08:57:51.529Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-24T08:57:51.529Z_

```json
{
  "parentUuid": "b07d85b9-f21f-4b8e-ba92-3e607774c4a6",
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
  "uuid": "7b6fe1b6-e9fc-4226-9057-7afdc84c2354",
  "timestamp": "2026-05-24T08:57:51.529Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 6 · 2026-05-24T08:57:51.529Z_

```json
{
  "parentUuid": "7b6fe1b6-e9fc-4226-9057-7afdc84c2354",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "3afbfc5b-0941-4096-9740-ad3a51b741e3",
  "timestamp": "2026-05-24T08:57:51.529Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier diagnostic paper for dream_20260524T081135",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1"
}
```

---

### Assistant

_source line 8 · 2026-05-24T08:57:54.851Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3afbfc5b-0941-4096-9740-ad3a51b741e3",
  "isSidechain": false,
  "requestId": "req_011CbM7jyFnyKmEHmsQTUsuU",
  "type": "assistant",
  "uuid": "612d1246-d48b-493a-8f4b-321262cc4049",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RYbw6r2nCrk4tniiVDmxTs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13904,
      "cache_read_input_tokens": 11447,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13904,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 13904,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13904
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

_source line 9 · 2026-05-24T08:57:55.507Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TPPUP1CCWFxjzpB7MieJBm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "612d1246-d48b-493a-8f4b-321262cc4049",
  "isSidechain": false,
  "requestId": "req_011CbM7jyFnyKmEHmsQTUsuU",
  "type": "assistant",
  "uuid": "61f2a39c-4a7d-4e5a-8c32-7886c8ffd677",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RYbw6r2nCrk4tniiVDmxTs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13904,
      "cache_read_input_tokens": 11447,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13904,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 13904,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13904
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

_source line 10 · 2026-05-24T08:57:55.864Z_

<details><summary>↩ Tool result · `toolu_01TPPUP1CCWFxjzpB7MieJBm`</summary>

```text
1	[
2	  {
3	    "name": "Llama Gradient Conflict Analysis",
4	    "description": "Llama-3.1-8B 上对 3 个 epoch checkpoint 计算 NTP-GAR 梯度 cos_sim 和 magnitude ratio， 验证梯度方向冲突是否跨模型存在。\n",
5	    "results": {
6	      "cos_sim_mean": 0.005,
7	      "cos_sim_std": 0.07,
8	      "neg_cos_sim_layers_pct": 53.1,
9	      "pos_cos_sim_layers_pct": 46.9,
10	      "mag_ratio_median": 25.7,
11	      "mag_ratio_range": "[12.0, 45.0]",
12	      "epoch0_cos_sim": 0.012,
13	      "epoch0_neg_layers_pct": 50.0,
14	      "epoch1_cos_sim": 0.003,
15	      "epoch1_neg_layers_pct": 53.1,
16	      "epoch2_cos_sim": -0.001,
17	      "epoch2_neg_layers_pct": 56.3,
18	      "gpu_hours": 0.3
19	    },
20	    "tables": [
21	      {
22	        "caption": "Cross-Model Gradient Geometry Comparison",
23	        "columns": [
24	          "Model",
25	          "cos_sim (mean)",
26	          "neg_layers (%)",
27	          "mag_ratio (median)",
28	          "Interpretation"
29	        ],
30	        "rows": [
31	          [
32	            "Qwen-2.5-7B (ep0→ep2)",
33	            "-0.062",
34	            "72.6",
35	            "11.9×",
36	            "Mild conflict + NTP dominance"
37	          ],
38	          [
39	            "Llama-3.1-8B (ep0→ep2)",
40	            "+0.005",
41	            "53.1",
42	            "25.7×",
43	            "Orthogonal + extreme NTP dominance"
44	          ]
45	        ]
46	      },
47	      {
48	        "caption": "Llama Per-Epoch Gradient Statistics",
49	        "columns": [
50	          "Epoch",
51	          "cos_sim",
52	          "neg_layers (%)",
53	          "mag_ratio"
54	        ],
55	        "rows": [
56	          [
57	            "0",
58	            "+0.012",
59	            "50.0",
60	            "18.3"
61	          ],
62	          [
63	            "1",
64	            "+0.003",
65	            "53.1",
66	            "24.1"
67	          ],
68	          [
69	            "2",
70	            "-0.001",
71	            "56.3",
72	            "25.7"
73	          ]
74	        ]
75	      }
76	    ],
77	    "figures": [],
78	    "analysis": "PCGrad 叙事在 worst case 下从 \"cross-model causal exclusion\" 收缩为 \"Qwen-specific observation\"。 Paper 需改叙事为 \"NTP magnitude dominance is the universal mechanism; gradient direction geometry varies by model but is inconsequential in both cases—on Qwen because PCGrad removes conflict without changing outcomes, on Llama because conflict doesn't exist.\" 这让 PCGrad section 的 weight 降低，审稿人可能认为 'PCGrad ablation on one model is insufficient evidence for a general claim about gradient conflict irrelevance.'\n\n\nWorst case：Llama 梯度是 near-orthogonal（cos_sim ≈ 0），不是 conflict（cos_sim < 0）。 neg_layers 53.1% 接近随机水平（50%），与 Qwen 的 67-79% 系统性 negative 模式不同。 这意味着两模型的梯度几何结构不一致——Qwen 有 mild conflict，Llama 没有。审稿人会说： \"gradient conflict 不是 cross-model mechanism，那你为什么用一整个 section（§6.2）讨论它？\" Magnitude ratio 25.7× 比 Qwen（7.5-14.7×）更极端，但方向冲突不存在使 PCGrad 在 Llama 上 没有可消除的 conflict。总体：数据支持 NTP 幅度主导，但削弱 gradient conflict 作为 universal mechanism 的叙事。PCGrad 变成 \"only relevant on Qwen，model-specific finding\"。\n"
79	  },
80	  {
81	    "name": "Expanded Eval Set (200 Conversations)",
82	    "description": "TF eval 从 50 扩展到 200 conversations（idx>=7000 from UltraChat），提高 bootstrap CI 统计功效。 AR eval 保持 N=50（效应量极端，无需扩展）。\n",
83	    "results": {
84	      "tf_n200_tg_gar_ours": 0.501,
85	      "tf_n200_tg_gar_ours_ci95": [
86	        0.488,
87	        0.514
88	      ],
89	      "tf_n200_lo_gar_ours": 0.497,
90	      "tf_n200_lo_gar_ours_ci95": [
91	        0.484,
92	        0.51
93	      ],
94	      "tf_n200_ug_gar_ours": 0.503,
95	      "tf_n200_ug_gar_ours_ci95": [
96	        0.49,
97	        0.516
98	      ],
99	      "tf_n200_tg_minus_lo_ci95": [
100	        -0.008,
101	        0.016
102	      ],
103	      "tf_n200_tg_minus_lo_p": 0.52,
104	      "tf_n200_ppl_tg": 2.78,
105	      "tf_n200_ppl_lo": 2.78,
106	      "tf_n200_ppl_ug": 2.78,
107	      "tf_n200_base_gar_ours": 0.013,
108	      "ar_n50_unchanged": true,
109	      "gpu_hours": 1.5
110	    },
111	    "tables": [
112	      {
113	        "caption": "TF Eval: N=50 vs N=200 Comparison",
114	        "columns": [
115	          "Variant",
116	          "GAR-ours (N=50)",
117	          "GAR-ours (N=200)",
118	          "95% CI (N=200)",
119	          "PPL"
120	        ],
121	        "rows": [
122	          [
123	            "TG v7",
124	            "0.504",
125	            "0.501",
126	            "[0.488, 0.514]",
127	            "2.78"
128	          ],
129	          [
130	            "LoRA-only",
131	            "0.498",
132	            "0.497",
133	            "[0.484, 0.510]",
134	            "2.78"
135	          ],
136	          [
137	            "UG",
138	            "0.505",
139	            "0.503",
140	            "[0.490, 0.516]",
141	            "2.78"
142	          ],
143	          [
144	            "Base",
145	            "0.013",
146	            "0.013",
147	            "[0.010, 0.016]",
148	            "4.34"
149	          ]
150	        ]
151	      },
152	      {
153	        "caption": "Pairwise Differences (N=200, 95% Bootstrap CI)",
154	        "columns": [
155	          "Comparison",
156	          "Mean Diff",
157	          "95% CI",
158	          "Contains 0?"
159	        ],
160	        "rows": [
161	          [
162	            "TG - LO",
163	            "+0.004",
164	            "[-0.008, +0.016]",
165	            "Yes"
166	          ],
167	          [
168	            "UG - LO",
169	            "+0.006",
170	            "[-0.006, +0.018]",
171	            "Yes"
172	          ],
173	          [
174	            "TG - UG",
175	            "-0.002",
176	            "[-0.014, +0.010]",
177	            "Yes"
178	          ]
179	        ]
180	      }
181	    ],
182	    "figures": [],
183	    "analysis": "N=200 TF eval 在 worst case 下是 low-value experiment。确认 gating zero-increment 但审稿人 不在意 TF regime。GPU 预算（1.5h）不高，可保留为 Appendix 但不应在 main text 突出。 不改变 paper 竞争力评估。\n\n\n扩展到 200 convs 后 CI 更窄但 TG-LO 差异仍包含 0（[-0.008, +0.016]），统计确认 gating zero-increment。但这只是 TF eval——审稿人关注 AR eval 不关注 TF。TF convergence 是 trivially expected，200 conversations 只是让已知结论更精确。Worst case：per-conversation variance 暴露部分对话 TG GAR < LO GAR，让 gating 故事更 noisy。不产生新 insight， 不改变 paper score。审稿人可能说 'N=200 for teacher-forcing is overkill; the real test is autoregressive where you only have N=50.'\n"
184	  },
185	  {
186	    "name": "λ_GAR Sensitivity Analysis",
187	    "description": "训练 v7 with λ_GAR=10（1 epoch）和 λ_GAR=0.1（1 epoch），展示梯度竞争在不同 loss 权重下的表现。\n",
188	    "results": {
189	      "lambda10_epoch1_ntp_loss": 1.05,
190	      "lambda10_epoch1_gar_loss": 0.015,
191	      "lambda10_epoch1_total_loss": 1.2,
192	      "lambda10_gate_mean": 0.82,
193	      "lambda10_gate_std": 0.12,
194	      "lambda10_gate_min": 0.45,
195	      "lambda10_ppl": 3.8,
196	      "lambda10_tf_gar_ours": 0.52,
197	      "lambda10_ar_gar_ours": 0.018,
198	      "lambda10_gap_ratio": 28.9,
199	      "lambda10_training_stable": false,
200	      "lambda10_ntp_ppl_degradation_pct": 36.7,
201	      "lambda01_epoch1_ntp_loss": 0.93,
202	      "lambda01_epoch1_gar_loss": 0.0003,
203	      "lambda01_gate_mean": 0.98,
204	      "lambda01_gate_std": 0.01,
205	      "lambda01_ppl": 2.78,
206	      "lambda01_tf_gar_ours": 0.49,
207	      "lambda01_ar_gar_ours": 0.015,
208	      "lambda01_gap_ratio": 32.7,
209	      "gpu_hours": 2.0
210	    },
211	    "tables": [
212	      {
213	        "caption": "λ_GAR Sensitivity: Impact on Training-Inference Gap",
214	        "columns": [
215	          "λ_GAR",
216	          "TF GAR-ours",
217	          "AR GAR-ours",
218	          "Gap Ratio",
219	          "PPL",
220	          "Training Stable?"
221	        ],
222	        "rows": [
223	          [
224	            "0.1",
225	            "0.49",
226	            "0.015",
227	            "32.7×",
228	            "2.78",
229	            "Yes (≈ LoRA-only)"
230	          ],
231	          [
232	            "1.0 (v7 default)",
233	            "0.50",
234	            "0.016",
235	            "31.3×",
236	            "2.78",
237	            "Yes"
238	          ],
239	          [
240	            "10.0",
241	            "0.52",
242	            "0.018",
243	            "28.9×",
244	            "3.80",
245	            "No (oscillation)"
246	          ]
247	        ]
248	      }
249	    ],
250	    "figures": [],
251	    "analysis": "λ sensitivity 在 worst case 下可放入 Appendix 但 paper value 极低。核心 takeaway（distribution shift independent of λ）是 correct 但 trivially expected。审稿人 'this confirms what we already know—the problem is not hyperparameter tuning but fundamental distribution mismatch.' 不给 novelty credit。 建议：仅在 Discussion 一句带过 'λ sensitivity analysis (Appendix X) confirms gap independence from loss weighting'，不要展开讨论。\n\n\nλ=10：gate 远离 identity（mean 0.82，min 0.45），TF GAR 略高（0.52），但 PPL 严重恶化（3.80， +36.7% vs v7 2.78）。关键：AR GAR 仍崩溃到 0.018，gap 28.9×——distribution shift 不随 λ 改变。 Gate 学到更激进的 TF-context-specific attenuation，推理时这些模式无用。训练不稳定（loss oscillation）。 λ=0.1：GAR 信号太弱（loss 0.0003），gate frozen near 1.0（std 0.01），等价 LoRA-only。Gap 更大 32.7×。 两端都不改变核心结论。审稿人会说 'obviously increasing λ hurts NTP and decreasing it removes GAR signal—this is a trivial sensitivity analysis that adds nothing new.' 特别是 worst case 下审稿人 已认为 negative result incremental，再加一个 'trivial sensitivity' 只会 reinforce 这个印象。\n"
252	  },
253	  {
254	    "name": "TF vs AR Attention KL Divergence",
255	    "description": "计算 per-head KL(P_TF || P_AR) 量化 attention distribution shift。 测试 GAR-relevant heads 是否显示更大 KL → exposure bias 的机制证据。\n",
256	    "results": {
257	      "tg_mean_kl": 0.054,
258	      "base_mean_kl": 0.043,
259	      "tg_max_kl_layer": "L23",
260	      "tg_max_kl_value": 0.15,
261	      "high_kl_layers": "L9, L23-L27",
262	      "gate_kl_correlation": 0.11,
263	      "gate_kl_p_value": 0.18,
264	      "gar_relevant_heads_mean_kl": 0.072,
265	      "non_gar_relevant_heads_mean_kl": 0.048,
266	      "kl_ratio_gar_vs_nongar": 1.5,
267	      "n_conversations": 50,
268	      "n_heads_per_layer": 28,
269	      "n_layers": 28,
270	      "n_total_head_layer_pairs": 784,
271	      "gpu_hours": 0
272	    },
273	    "tables": [
274	      {
275	        "caption": "Per-Layer-Group Attention KL Divergence (TF→AR)",
276	        "columns": [
277	          "Layer Group",
278	          "Mean KL (TG)",
279	          "Mean KL (Base)",
280	          "Mean Gate Value"
281	        ],
282	        "rows": [
283	          [
284	            "L0-L7 (shallow)",
285	            "0.032",
286	            "0.029",
287	            "0.94"
288	          ],
289	          [
290	            "L8-L15 (mid)",
291	            "0.048",
292	            "0.039",
293	            "0.93"
294	          ],
295	          [
296	            "L16-L23 (deep-mid)",
297	            "0.065",
298	            "0.050",
299	            "0.92"
300	          ],
301	          [
302	            "L24-L27 (deep)",
303	            "0.089",
304	            "0.068",
305	            "0.95"
306	          ]
307	        ]
308	      },
309	      {
310	        "caption": "GAR-Relevant vs Non-Relevant Head KL",
311	        "columns": [
312	          "Head Category",
313	          "Mean KL",
314	          "N heads",
315	          "Interpretation"
316	        ],
317	        "rows": [
318	          [
319	            "GAR-relevant (top-10% goal-attention)",
320	            "0.072",
321	            "78",
322	            "Slightly higher shift"
323	          ],
324	          [
325	            "Non-GAR-relevant",
326	            "0.048",
327	            "706",
328	            "Background level"
329	          ],
330	          [
331	            "Ratio",
332	            "1.50×",
333	            "-",
334	            "Weak selectivity signal"
335	          ]
336	        ]
337	      }
338	    ],
339	    "figures": [],
340	    "analysis": "KL 分析在 worst case 下是 underwhelming supplementary evidence。0.054 mean KL 是 small effect， 不足以 standalone support distribution shift claim。作为 Appendix 可保留（诚实报告），但 main text 不应过度强调。审稿人可能 ignore 或 attack：\"if KL is this small, maybe distribution shift isn't really the mechanism—maybe it's something else entirely that you haven't measured.\" Worst case 下这部分损害论文更多（给审稿人攻击弹药）而非帮助。建议 Appendix only。\n\n\nKL divergence 整体偏小（mean 0.054 nat），不到 0.1。虽然 GAR-relevant heads 略高（0.072 vs 0.048）， ratio 仅 1.5×——不够 dramatic 来解释 8× GAR gap。Gate-KL correlation 极弱（r=0.11, p=0.18 不显著）， 说明 gate 与 attention distribution shift 无关联——gate 未学到在 high-shift layers 做更强干预。 High-KL layers（L23-L27）在深层，但与 gate attenuation 集中层不完全吻合（gate 最低在 L3-L5）。 审稿人两个攻击角度：(1) \"KL 0.054 解释不了 8× gap——一定有其他因素（error accumulation、 sequential compounding）你没测到\"；(2) \"gate-KL 无相关说明 gate 根本不 tracking the relevant signal\"。 总体：提供 weak supplementary evidence，但不能作为 independent contribution。\n"
341	  },
342	  {
343	    "name": "Llama-3.1-8B Scheduled Sampling",
344	    "description": "在 Llama-3.1-8B 上复现 SS 训练（time-scheduled sampling + GAR auxiliary loss）， 验证 gap 压缩是否跨模型泛化。若 Llama gap 同样压缩 → SS 是 general mitigation。\n",
345	    "results": {
346	      "training_converged": true,
347	      "epochs_completed": 3,
348	      "total_steps": 3000,
349	      "wall_clock_hours": 10.5,
350	      "final_ntp_loss": 0.928,
351	      "final_gar_loss": 0.0012,
352	      "final_gate_mean": 0.92,
353	      "final_gate_std": 0.065,
354	      "ss_ratio_final": 0.5,
355	      "ss_steps_used": 5100,
356	      "tf_eval": {
357	        "gar_ours": 0.47,
358	        "gar_dongre": 0.35,
359	        "ppl": 2.6,
360	        "n_conversations": 50
361	      },
362	      "ar_eval_beta0": {
363	        "gar_ours": 0.04,
364	        "gar_ours_std": 0.03,
365	        "gar_dongre": 0.025,
366	        "ppl": 1.4,
367	        "n_conversations": 20
368	      },
369	      "ar_eval_beta3": {
370	        "gar_ours": 0.52,
371	        "ppl": 1.58
372	      },
373	      "ar_eval_beta5": {
374	        "gar_ours": 0.68,
375	        "ppl": 1.75
376	      },
377	      "gap_ratio_beta0": 11.75,
378	      "gap_ratio_vs_llama_tg": 0.74,
379	      "gap_ratio_vs_qwen_ss": "Qwen 1.3× vs Llama 11.75×",
380	      "ss_independent_benefit_beta0": 0.01
381	    },
382	    "tables": [
383	      {
384	        "caption": "Scheduled Sampling Cross-Model Comparison (β=0, AR eval)",
385	        "columns": [
386	          "Model",
387	          "SS TF GAR",
388	          "SS AR GAR (β=0)",
389	          "Gap Ratio",
390	          "TG AR GAR (β=0)",
391	          "SS Benefit"
392	        ],
393	        "rows": [
394	          [
395	            "Qwen-2.5-7B (3-seed)",
396	            "0.498±0.004",
397	            "0.390±0.036",
398	            "1.28×",
399	            "0.064",
400	            "+0.326"
401	          ],
402	          [
403	            "Llama-3.1-8B",
404	            "0.47",
405	            "0.04",
406	            "11.75×",
407	            "0.030",
408	            "+0.010"
409	          ]
410	        ]
411	      },
412	      {
413	        "caption": "Llama SS β-Sweep (AR eval, N=20)",
414	        "columns": [
415	          "β",
416	          "SS AR GAR",
417	          "TG AR GAR (no SS)",
418	          "SS Incremental",
419	          "PPL"
420	        ],
421	        "rows": [
422	          [
423	            "0",
424	            "0.040",
425	            "0.030",
426	            "+0.010",
427	            "1.40"
428	          ],
429	          [
430	            "3",
431	            "0.520",
432	            "0.556",
433	            "-0.036",
434	            "1.58"
435	          ],
436	          [
437	            "5",
438	            "0.680",
439	            "0.727",
440	            "-0.047",
441	            "1.75"
442	          ]
443	        ]
444	      },
445	      {
446	        "caption": "Llama TF Eval Comparison",
447	        "columns": [
448	          "Variant",
449	          "GAR-ours",
450	          "GAR-Dongre",
451	          "PPL"
452	        ],
453	        "rows": [
454	          [
455	            "Base",
456	            "0.017",
457	            "0.004",
458	            "3.45"
459	          ],
460	          [
461	            "TG v7",
462	            "0.484",
463	            "0.018",
464	            "2.57"
465	          ],
466	          [
467	            "SS",
468	            "0.470",
469	            "0.350",
470	            "2.60"
471	          ]
472	        ]
473	      }
474	    ],
475	    "figures": [],
476	    "analysis": "Llama SS failure 是 worst tier 的 cascade trigger： (1) SS 不能作为论文第 5 个 contribution——cross-model failure 意味着 'SS transfers to multi-turn transformer attention objectives' 的 claim 不成立（只在 1/2 模型上成立）。 (2) 论文必须放弃完整弧叙事。Title 不能暗示 recovery/remedy。 (3) SS 降级为 Discussion 的 'attempted mitigation, model-specific partial success'。 (4) 但 SS failure 本身有 diagnostic value：even explicitly exposing model to its own generation doesn't bridge distribution shift on Llama → 更强的 impossibility signal。 (5) 与 Dongre convergent evidence 更强：gating fails × 2 models + SS fails on Llama =  5/6 intervention-model combinations fail（只有 Qwen SS 成功）。 (6) Paper score 从 best-case 3.5 降到 2.5-3.0。Main conference 无望，Findings borderline。\n\n\n这是 worst tier 的 defining failure point。Llama SS 训练正常收敛（loss 与 Llama TG v7 comparable）， TF eval 显示 SS 确实学到 GAR pattern（TF GAR 0.47 ≈ Llama TG 0.48）。但 AR eval β=0 仅 0.04， 远低于 Qwen SS 的 0.39。Gap ratio 11.75× 仍是 dramatic failure。\nSS 在 Llama 上失败的可能机制： (1) Llama tokenizer 与 Qwen 不同（BPE vocab 128k vs 151k），model-generated text 的分布偏离 gold text 更远——SS 暴露的分布与推理分布仍不匹配。 (2) Llama 32 层 + 更深的 gate attenuation pattern（L25 gate 0.719）意味着 SS 需更长训练 才能 penetrate deeper layers。3 epochs 不够。 (3) Llama base GAR 更低（0.009 vs Qwen 0.019），从更低起点恢复更困难。 (4) Llama 在 SS step 上生成文本质量更低（更多 hallucination/repetition），SS exposure 引入的分布 noise 大于 signal。\nβ=3/5 时 inference-time steering 仍有效（0.52, 0.68），但这是 steering 功劳而非 SS。 SS 在 Llama 上的 independent value（β=0 增量 +0.01 over TG baseline 0.03）接近 0。\n结论：SS 是 model-specific mitigation，不是 general solution。论文必须放弃 'discover→diagnose→remedy' 弧，SS 不能作为第 5 个 contribution。\n"
477	  },
478	  {
479	    "name": "SS 3-Seed Validation (Qwen)",
480	    "description": "Qwen SS 3 seeds (s42/s123/s456) 的 AR eval with β=0,3,5，提供 mean±std。回应 W7 单 seed 质疑。\n",
481	    "results": {
482	      "tf_gar_ours": {
483	        "s42": 0.503,
484	        "s123": 0.495,
485	        "s456": 0.496,
486	        "mean": 0.498,
487	        "std": 0.004
488	      },
489	      "ar_beta0_gar": {
490	        "s42": 0.347,
491	        "s123": 0.4,
492	        "s456": 0.422,
493	        "mean": 0.39,
494	        "std": 0.036,
495	        "cv_pct": 9.2
496	      },
497	      "ar_beta3_gar": {
498	        "s42": 0.593,
499	        "s123": 0.59,
500	        "s456": 0.605,
501	        "mean": 0.596,
502	        "std": 0.008
503	      },
504	      "ar_beta5_gar": {
505	        "s42": 0.717,
506	        "s123": 0.717,
507	        "s456": 0.716,
508	        "mean": 0.717,
509	        "std": 0.001
510	      },
511	      "ppl_beta0": {
512	        "s42": 1.44,
513	        "s123": 1.441,
514	        "s456": 1.442,
515	        "mean": 1.441,
516	        "std": 0.001
517	      },
518	      "gap_ratio": {
519	        "s42": 1.45,
520	        "s123": 1.24,
521	        "s456": 1.18,
522	        "mean": 1.29,
523	        "range": "[1.18, 1.45]"
524	      },
525	      "s42_is_outlier_at_beta0": true,
526	      "n_ar_conversations_per_seed": 39
527	    },
528	    "tables": [
529	      {
530	        "caption": "SS 3-Seed AR Eval Results (Qwen-2.5-7B, N=39 valid conversations per seed)",
531	        "columns": [
532	          "Metric",
533	          "s42",
534	          "s123",
535	          "s456",
536	          "Mean±Std"
537	        ],
538	        "rows": [
539	          [
540	            "TF GAR-ours",
541	            "0.503",
542	            "0.495",
543	            "0.496",
544	            "0.498±0.004"
545	          ],
546	          [
547	            "AR GAR β=0",
548	            "0.347",
549	            "0.400",
550	            "0.422",
551	            "0.390±0.036"
552	          ],
553	          [
554	            "AR GAR β=3",
555	            "0.593",
556	            "0.590",
557	            "0.605",
558	            "0.596±0.008"
559	          ],
560	          [
561	            "AR GAR β=5",
562	            "0.717",
563	            "0.717",
564	            "0.716",
565	            "0.717±0.001"
566	          ],
567	          [
568	            "PPL β=0",
569	            "1.440",
570	            "1.441",
571	            "1.442",
572	            "1.441±0.001"
573	          ],
574	          [
575	            "Gap Ratio",
576	            "1.45×",
577	            "1.24×",
578	            "1.18×",
579	            "1.29±0.14"
580	          ]
581	        ]
582	      }
583	    ],
584	    "figures": [],
585	    "analysis": "3-seed 在 worst case 下是 necessary but insufficient。W7 partially addressed（有 variance estimate）， 但审稿人重心转移到 Llama failure。'You showed 3 seeds on the model where it works, but it completely fails on the other model. The 3-seed result is uninteresting because cross-model generalization is the real test, and you failed it.' SS contribution 无论在 Qwen 上多稳定， 只要 Llama 失败就无法 claim generalizability。在 worst tier 中 SS 从 contribution #5 移除， 3-seed 数据放 Appendix。\n\n\n3-seed mean AR GAR β=0 = 0.390 在 worst 范围 [0.38, 0.45] 的下端。s42 是明显 outlier （0.347 vs s123 0.400 / s456 0.422），std = 0.036，CV = 9.2%。\nWorst case 审稿人攻击角度： (1) \"CV 9.2% 对 main result 偏高——3 seeds 中 s42 远低于其他两个，说明结果对 initialization 敏感。\" (2) \"s42 恰好是你 main paper 中展示的 seed，也是最差的——虽然不是 cherry-pick，但 optics 不好。\" (3) β=3/5 极稳定（std<0.01）说明 high-β steering 效果 robust，但 β=0 的 SS independent value 有 seed sensitivity。SS 真正的 independent contribution（β=0 without steering assist）不够 stable。 (4) 结合 Llama SS failure：\"3 seeds on one model proves nothing when the other model fails completely.\"\nPPL 方差极小（±0.001），确认 SS 无 PPL cost。但 worst case 下审稿人不给 PPL neutrality credit。\n"
586	  },
587	  {
588	    "name": "Alternative GAR Definition Robustness",
589	    "description": "4 种 token selection（last/all/first/goal-only）× 3 checkpoints（Base/TG/SS）， 测试 GAR 改善是否 robust across definitions。需 GPU re-eval（raw attention 未保存）。\n",
590	    "results": {
591	      "base": {
592	        "last_token": 0.019,
593	        "all_token": 0.022,
594	        "first_token": 0.021,
595	        "goal_only": 0.015
596	      },
597	      "tg": {
598	        "last_token": 0.325,
599	        "all_token": 0.025,
600	        "first_token": 0.039,
601	        "goal_only": 0.018
602	      },
603	      "ss": {
604	        "last_token": 0.39,
605	        "all_token": 0.062,
606	        "first_token": 0.045,
607	        "goal_only": 0.03
608	      },
609	      "n_defs_tg_improves_clearly": 1,
610	      "n_defs_ss_improves_clearly": 1,
611	      "n_defs_ss_improves_marginally": 1,
612	      "improved_definition": "last-token (ours)",
613	      "marginal_definition": "all-token",
614	      "not_improved": [
615	        "first-token",
616	        "goal-only"
617	      ],
618	      "gpu_hours": 0.5
619	    },
620	    "tables": [
621	      {
622	        "caption": "GAR Across Token Selection Definitions (AR eval, Qwen-2.5-7B)",
623	        "columns": [
624	          "Token Selection",
625	          "Base",
626	          "TG v7",
627	          "SS v8b",
628	          "SS/Base Ratio",
629	          "Clearly Improved?"
630	        ],
631	        "rows": [
632	          [
633	            "Last-token (ours)",
634	            "0.019",
635	            "0.325",
636	            "0.390",
637	            "20.5×",
638	            "Yes"
639	          ],
640	          [
641	            "All-token (≈Dongre)",
642	            "0.022",
643	            "0.025",
644	            "0.062",
645	            "2.8×",
646	            "Marginal"
647	          ],
648	          [
649	            "First-token",
650	            "0.021",
651	            "0.039",
652	            "0.045",
653	            "2.1×",
654	            "No (within noise)"
655	          ],
656	          [
657	            "Goal-only tokens",
658	            "0.015",
659	            "0.018",
660	            "0.030",
661	            "2.0×",
662	            "No (within noise)"
663	          ]
664	        ]
665	      }
666	    ],
667	    "figures": [],
668	    "analysis": "Alternative GAR 分析在 worst case 下 damages the paper more than it helps。 审稿人会认为 GAR 改善是 metric-specific artifact：只有特定的 last-token summary-position 定义下才有效果。这触发 W3 escalation chain： (1) GAR 只对 last-token 有效 → metric fragility (2) Instruction retention r=0.2 → weak downstream correlation (3) Alternative definitions 无改善 → 'what exactly are you measuring?' 建议：在 worst case 叙事中将此放入 Appendix，main text 仅一句提及 'robustness analysis in Appendix X shows improvement concentrated on summary-position tokens, consistent with the training objective design.' 不要让审稿人在 main text 看到这个弱点。\n\n\nWorst case：alternative_gar_defs_ss_improves 在 [0, 2] 范围内，取 1。\nTG 只改善 last-token（0.325 vs base 0.019, 17×），all/first/goal-only 接近 baseline。 这说明 TG 学到的 attention pattern 高度 position-specific：只对 assistant response 最后 一个 token 的 goal attention 有效，对其他 response token positions 无效。\nSS 同样主要改善 last-token（0.390），all-token 有 marginal 提升（0.062 vs 0.022, 2.8×） 但绝对值仍很低。First-token 和 goal-only 基本无改善（2× within noise level）。\n审稿人会用这个数据攻击 GAR metric 本身的 validity： (1) \"GAR improvement is position-specific overfitting to last-token——不是真正改善了 goal attention\"。 (2) \"All-token GAR（最接近 Dongre 定义）在 SS 后仍然很低（0.062），说明你的方法没有 真正 address Dongre 发现的问题\"。 (3) W3 escalation 加剧：GAR 作为代理指标的 validity 被质疑 + instruction retention r=0.2 太弱 + 换个 GAR 定义结果就消失 = triple weakness。\n"
669	  },
670	  {
671	    "name": "SS 4th Seed (s789)",
672	    "description": "第 4 个 Qwen SS seed 加强统计。ROI 低于 Llama SS 实验。\n",
673	    "results": {
674	      "training": {
675	        "epochs_completed": 3,
676	        "wall_clock_hours": 6.5,
677	        "final_loss": 0.932,
678	        "final_gate_mean": 0.955,
679	        "ss_ratio_final": 0.5
680	      },
681	      "s789_tf_gar_ours": 0.5,
682	      "s789_ar_beta0_gar": 0.3,
683	      "s789_ar_beta3_gar": 0.58,
684	      "s789_ar_beta5_gar": 0.71,
685	      "s789_ppl_beta0": 1.442,
686	      "s789_gap_ratio": 1.67,
687	      "four_seed_stats": {
688	        "mean_beta0": 0.367,
689	        "std_beta0": 0.054,
690	        "cv_beta0_pct": 14.7,
691	        "range_beta0": "[0.300, 0.422]",
692	        "mean_gap": 1.39,
693	        "std_gap": 0.22
694	      },
695	      "vs_three_seed": {
696	        "mean_delta": -0.023,
697	        "std_delta": 0.018,
698	        "cv_delta": 5.5
699	      }
700	    },
701	    "tables": [
702	      {
703	        "caption": "SS 4-Seed Comparison (if run)",
704	        "columns": [
705	          "Seed",
706	          "AR GAR β=0",
707	          "AR GAR β=3",
708	          "AR GAR β=5",
709	          "Gap Ratio"
710	        ],
711	        "rows": [
712	          [
713	            "42",
714	            "0.347",
715	            "0.593",
716	            "0.717",
717	            "1.45×"
718	          ],
719	          [
720	            "123",
721	            "0.400",
722	            "0.590",
723	            "0.717",
724	            "1.24×"
725	          ],
726	          [
727	            "456",
728	            "0.422",
729	            "0.605",
730	            "0.716",
731	            "1.18×"
732	          ],
733	          [
734	            "789",
735	            "0.300",
736	            "0.580",
737	            "0.710",
738	            "1.67×"
739	          ],
740	          [
741	            "4-seed Mean±Std",
742	            "0.367±0.054",
743	            "0.592±0.010",
744	            "0.715±0.003",
745	            "1.39±0.22"
746	          ]
747	        ]
748	      }
749	    ],
750	    "figures": [],
751	    "analysis": "在 worst case 下 s789 是 actively harmful data point。建议决策矩阵： - 如果 s789 ≥ 0.37：加入增强统计 → run - 如果 s789 < 0.35：拉低 mean + 增大 CV → do not report - Worst case s789 = 0.30 → definitely do not run / do not include 此实验应 deprioritize below Llama SS 和所有 P0/P1 实验。8 GPU-hours 可更好地用于 Llama SS 或 paper writing。\n\n\ns789 是 worst case 中的 low outlier（AR GAR β=0 = 0.300，gap 1.67×）。4-seed mean 拉低到 0.367，std 从 0.036 升到 0.054，CV 从 9.2% 升到 14.7%。\n更多 seeds 反而暴露更大 variance，削弱 SS 可靠性叙事： (1) \"CV 14.7% 意味着 SS 的 independent value（β=0）高度依赖 random initialization\"。 (2) \"4 seeds 范围 0.30-0.42，跨越了 'meaningful improvement' 和 'marginal' 的分界线\"。 (3) \"s789 gap 1.67× 接近 Qwen TG v7 的 gap regime，说明某些 seed 下 SS 几乎不起作用\"。\nβ=3/5 仍然稳定（0.580/0.710），因为 high-β steering 效果 dominant 且 seed-insensitive。 但 β=0 是 SS 独立价值的唯一指标，14.7% CV 不够 convincing。\n强烈建议 worst case 下 NOT running s789。3-seed 的 0.390±0.036 虽不完美但可接受。 第 4 个 seed 如果拉低 mean 是自找麻烦。审稿人要求时可在 rebuttal 中补充。\n"
752	  },
753	  {
754	    "name": "Long Conversation Eval (>10 turns)",
755	    "description": "测试 exposure bias gap 是否随对话长度增加而恶化。需从 UltraChat 筛选长对话。\n",
756	    "results": {
757	      "turns_5": {
758	        "base_ar_gar": 0.02,
759	        "tg_ar_gar": 0.06,
760	        "ss_ar_gar": 0.42,
761	        "ss_benefit": 0.4
762	      },
763	      "turns_10": {
764	        "base_ar_gar": 0.01,
765	        "tg_ar_gar": 0.02,
766	        "ss_ar_gar": 0.38,
767	        "ss_benefit": 0.37
768	      },
769	      "turns_15": {
770	        "base_ar_gar": 0.006,
771	        "tg_ar_gar": 0.008,
772	        "ss_ar_gar": 0.22,
773	        "ss_benefit": 0.214
774	      },
775	      "turns_20": {
776	        "base_ar_gar": 0.004,
777	        "tg_ar_gar": 0.005,
778	        "ss_ar_gar": 0.12,
779	        "ss_benefit": 0.116
780	      },
781	      "ss_decay_rate_per_5turns_after_10": "~48%",
782	      "tg_base_convergence_at_turns": 15,
783	      "n_long_conversations": 10,
784	      "eval_tokens_per_conversation": "~8000-12000",
785	      "gpu_hours": 2.0
786	    },
787	    "tables": [
788	      {
789	        "caption": "GAR by Conversation Length (AR eval, Qwen-2.5-7B)",
790	        "columns": [
791	          "Turns",
792	          "Base",
793	          "TG v7",
794	          "SS v8b",
795	          "SS Benefit vs Base"
796	        ],
797	        "rows": [
798	          [
799	            "5",
800	            "0.020",
801	            "0.060",
802	            "0.420",
803	            "+0.400"
804	          ],
805	          [
806	            "10",
807	            "0.010",
808	            "0.020",
809	            "0.380",
810	            "+0.370"
811	          ],
812	          [
813	            "15",
814	            "0.006",
815	            "0.008",
816	            "0.220",
817	            "+0.214"
818	          ],
819	          [
820	            "20",
821	            "0.004",
822	            "0.005",
823	            "0.120",
824	            "+0.116"
825	          ]
826	        ]
827	      },
828	      {
829	        "caption": "SS Effectiveness Decay",
830	        "columns": [
831	          "Turn Range",
832	          "SS AR GAR",
833	          "Δ from turns 5",
834	          "Decay (%)"
835	        ],
836	        "rows": [
837	          [
838	            "1-5",
839	            "0.420",
840	            "-",
841	            "-"
842	          ],
843	          [
844	            "6-10",
845	            "0.380",
846	            "-0.040",
847	            "9.5%"
848	          ],
849	          [
850	            "11-15",
851	            "0.220",
852	            "-0.200",
853	            "47.6%"
854	          ],
855	          [
856	            "16-20",
857	            "0.120",
858	            "-0.300",
859	            "71.4%"
860	          ]
861	        ]
862	      }
863	    ],
864	    "figures": [],
865	    "analysis": "Long conversation eval 在 worst case 下提供 damaging but honest evidence。它表明 SS mitigation 有 limited effective range（≤10 turns）。结合 Llama failure，SS 的 contribution 变成 'limited preliminary result on one model for short conversations only'——不够 conference contribution。 建议：在 worst case diagnostic paper 中诚实报告此 limitation，放入 Discussion §7.3 'Scalability Limitations of Scheduled Sampling'。诚实承认 limitation 可能 earn reviewer respect ('self-aware about limitations')，比隐瞒好。但不改变 paper 从 3.0 以上下降的趋势。\n总体 worst case paper structure 调整： §5 Results 只含 main negative findings（NF1-NF3, gating zero-increment, cross-model replication）。 §6 Analysis 含 PCGrad causal exclusion + distribution shift。 §7 Discussion 含 SS attempted mitigation（Qwen partial success, Llama failure, length limitation） + Dongre convergent evidence + concrete future directions。 §8 Conclusion 重述 failure mode taxonomy 的系统分类学价值。 Expected Findings score: 2.5-3.0。\n\nSS 在 ≤10 turns 维持 0.38-0.42 AR GAR（与 3-seed mean 一致），但 15 turns 后急剧下降到 0.22，20 turns 降到 0.12。每 5 turns 衰减约 48%。\n机制推测：SS 训练数据中 model-generated context 比例线性递增（scheduled），但长对话中 error accumulation 是 super-linear——每个 turn 的小偏差在后续 turns 被 compound。SS 暴露 的训练分布（线性 mix）与 20-turn 推理分布（exponential error accumulation）仍有 gap。\n审稿人 devastating critique： (1) \"SS 只在短对话（≤10 turns）有效，但 GAR 退化本身就是长对话问题（Dongre 测了 50 turns） ——你的 mitigation 恰好在最需要的地方失效。\" (2) \"你论文的 motivation 来自 Dongre 的 50-turn scenario，但你的 fix 在 15+ turns 就崩溃。\" (3) \"这与 scope limitation（W2/R1）结合——不仅 method-specific + model-specific，还 length-specific。\"\nTG 和 Base 在 15+ turns 已无区分（0.008 vs 0.006），再次确认 gating zero-increment 在长对话中成立。\n但有一个 silver lining：SS 衰减曲线本身是有价值的 diagnostic insight——它量化了 SS 暴露 与真实推理分布的 gap 如何随 conversation length 增长。可作为 Discussion 中 'limitations of time-scheduled SS' 的 empirical evidence。\n"
866	  }
867	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61f2a39c-4a7d-4e5a-8c32-7886c8ffd677",
  "isSidechain": false,
  "promptId": "4e9b6b3b-bc11-45d7-a0d2-4aaa1c0c9272",
  "type": "user",
  "uuid": "d9bd8604-67aa-4918-ac73-c23ae34b0be5",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Llama Gradient Conflict Analysis\",\n    \"description\": \"Llama-3.1-8B 上对 3 个 epoch checkpoint 计算 NTP-GAR 梯度 cos_sim 和 magnitude ratio， 验证梯度方向冲突是否跨模型存在。\\n\",\n    \"results\": {\n      \"cos_sim_mean\": 0.005,\n      \"cos_sim_std\": 0.07,\n      \"neg_cos_sim_layers_pct\": 53.1,\n      \"pos_cos_sim_layers_pct\": 46.9,\n      \"mag_ratio_median\": 25.7,\n      \"mag_ratio_range\": \"[12.0, 45.0]\",\n      \"epoch0_cos_sim\": 0.012,\n      \"epoch0_neg_layers_pct\": 50.0,\n      \"epoch1_cos_sim\": 0.003,\n      \"epoch1_neg_layers_pct\": 53.1,\n      \"epoch2_cos_sim\": -0.001,\n      \"epoch2_neg_layers_pct\": 56.3,\n      \"gpu_hours\": 0.3\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Cross-Model Gradient Geometry Comparison\",\n        \"columns\": [\n          \"Model\",\n          \"cos_sim (mean)\",\n          \"neg_layers (%)\",\n          \"mag_ratio (median)\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen-2.5-7B (ep0→ep2)\",\n            \"-0.062\",\n            \"72.6\",\n            \"11.9×\",\n            \"Mild conflict + NTP dominance\"\n          ],\n          [\n            \"Llama-3.1-8B (ep0→ep2)\",\n            \"+0.005\",\n            \"53.1\",\n            \"25.7×\",\n            \"Orthogonal + extreme NTP dominance\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Llama Per-Epoch Gradient Statistics\",\n        \"columns\": [\n          \"Epoch\",\n          \"cos_sim\",\n          \"neg_layers (%)\",\n          \"mag_ratio\"\n        ],\n        \"rows\": [\n          [\n            \"0\",\n            \"+0.012\",\n            \"50.0\",\n            \"18.3\"\n          ],\n          [\n            \"1\",\n            \"+0.003\",\n            \"53.1\",\n            \"24.1\"\n          ],\n          [\n            \"2\",\n            \"-0.001\",\n            \"56.3\",\n            \"25.7\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"PCGrad 叙事在 worst case 下从 \\\"cross-model causal exclusion\\\" 收缩为 \\\"Qwen-specific observation\\\"。 Paper 需改叙事为 \\\"NTP magnitude dominance is the universal mechanism; gradient direction geometry varies by model but is inconsequential in both cases—on Qwen because PCGrad removes conflict without changing outcomes, on Llama because conflict doesn't exist.\\\" 这让 PCGrad section 的 weight 降低，审稿人可能认为 'PCGrad ablation on one model is insufficient evidence for a general claim about gradient conflict irrelevance.'\\n\\n\\nWorst case：Llama 梯度是 near-orthogonal（cos_sim ≈ 0），不是 conflict（cos_sim < 0）。 neg_layers 53.1% 接近随机水平（50%），与 Qwen 的 67-79% 系统性 negative 模式不同。 这意味着两模型的梯度几何结构不一致——Qwen 有 mild conflict，Llama 没有。审稿人会说： \\\"gradient conflict 不是 cross-model mechanism，那你为什么用一整个 section（§6.2）讨论它？\\\" Magnitude ratio 25.7× 比 Qwen（7.5-14.7×）更极端，但方向冲突不存在使 PCGrad 在 Llama 上 没有可消除的 conflict。总体：数据支持 NTP 幅度主导，但削弱 gradient conflict 作为 universal mechanism 的叙事。PCGrad 变成 \\\"only relevant on Qwen，model-specific finding\\\"。\\n\"\n  },\n  {\n    \"name\": \"Expanded Eval Set (200 Conversations)\",\n    \"description\": \"TF eval 从 50 扩展到 200 conversations（idx>=7000 from UltraChat），提高 bootstrap CI 统计功效。 AR eval 保持 N=50（效应量极端，无需扩展）。\\n\",\n    \"results\": {\n      \"tf_n200_tg_gar_ours\": 0.501,\n      \"tf_n200_tg_gar_ours_ci95\": [\n        0.488,\n        0.514\n      ],\n      \"tf_n200_lo_gar_ours\": 0.497,\n      \"tf_n200_lo_gar_ours_ci95\": [\n        0.484,\n        0.51\n      ],\n      \"tf_n200_ug_gar_ours\": 0.503,\n      \"tf_n200_ug_gar_ours_ci95\": [\n        0.49,\n        0.516\n      ],\n      \"tf_n200_tg_minus_lo_ci95\": [\n        -0.008,\n        0.016\n      ],\n      \"tf_n200_tg_minus_lo_p\": 0.52,\n      \"tf_n200_ppl_tg\": 2.78,\n      \"tf_n200_ppl_lo\": 2.78,\n      \"tf_n200_ppl_ug\": 2.78,\n      \"tf_n200_base_gar_ours\": 0.013,\n      \"ar_n50_unchanged\": true,\n      \"gpu_hours\": 1.5\n    },\n    \"tables\": [\n      {\n        \"caption\": \"TF Eval: N=50 vs N=200 Comparison\",\n        \"columns\": [\n          \"Variant\",\n          \"GAR-ours (N=50)\",\n          \"GAR-ours (N=200)\",\n          \"95% CI (N=200)\",\n          \"PPL\"\n        ],\n        \"rows\": [\n          [\n            \"TG v7\",\n            \"0.504\",\n            \"0.501\",\n            \"[0.488, 0.514]\",\n            \"2.78\"\n          ],\n          [\n            \"LoRA-only\",\n            \"0.498\",\n            \"0.497\",\n            \"[0.484, 0.510]\",\n            \"2.78\"\n          ],\n          [\n            \"UG\",\n            \"0.505\",\n            \"0.503\",\n            \"[0.490, 0.516]\",\n            \"2.78\"\n          ],\n          [\n            \"Base\",\n            \"0.013\",\n            \"0.013\",\n            \"[0.010, 0.016]\",\n            \"4.34\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Pairwise Differences (N=200, 95% Bootstrap CI)\",\n        \"columns\": [\n          \"Comparison\",\n          \"Mean Diff\",\n          \"95% CI\",\n          \"Contains 0?\"\n        ],\n        \"rows\": [\n          [\n            \"TG - LO\",\n            \"+0.004\",\n            \"[-0.008, +0.016]\",\n            \"Yes\"\n          ],\n          [\n            \"UG - LO\",\n            \"+0.006\",\n            \"[-0.006, +0.018]\",\n            \"Yes\"\n          ],\n          [\n            \"TG - UG\",\n            \"-0.002\",\n            \"[-0.014, +0.010]\",\n            \"Yes\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"N=200 TF eval 在 worst case 下是 low-value experiment。确认 gating zero-increment 但审稿人 不在意 TF regime。GPU 预算（1.5h）不高，可保留为 Appendix 但不应在 main text 突出。 不改变 paper 竞争力评估。\\n\\n\\n扩展到 200 convs 后 CI 更窄但 TG-LO 差异仍包含 0（[-0.008, +0.016]），统计确认 gating zero-increment。但这只是 TF eval——审稿人关注 AR eval 不关注 TF。TF convergence 是 trivially expected，200 conversations 只是让已知结论更精确。Worst case：per-conversation variance 暴露部分对话 TG GAR < LO GAR，让 gating 故事更 noisy。不产生新 insight， 不改变 paper score。审稿人可能说 'N=200 for teacher-forcing is overkill; the real test is autoregressive where you only have N=50.'\\n\"\n  },\n  {\n    \"name\": \"λ_GAR Sensitivity Analysis\",\n    \"description\": \"训练 v7 with λ_GAR=10（1 epoch）和 λ_GAR=0.1（1 epoch），展示梯度竞争在不同 loss 权重下的表现。\\n\",\n    \"results\": {\n      \"lambda10_epoch1_ntp_loss\": 1.05,\n      \"lambda10_epoch1_gar_loss\": 0.015,\n      \"lambda10_epoch1_total_loss\": 1.2,\n      \"lambda10_gate_mean\": 0.82,\n      \"lambda10_gate_std\": 0.12,\n      \"lambda10_gate_min\": 0.45,\n      \"lambda10_ppl\": 3.8,\n      \"lambda10_tf_gar_ours\": 0.52,\n      \"lambda10_ar_gar_ours\": 0.018,\n      \"lambda10_gap_ratio\": 28.9,\n      \"lambda10_training_stable\": false,\n      \"lambda10_ntp_ppl_degradation_pct\": 36.7,\n      \"lambda01_epoch1_ntp_loss\": 0.93,\n      \"lambda01_epoch1_gar_loss\": 0.0003,\n      \"lambda01_gate_mean\": 0.98,\n      \"lambda01_gate_std\": 0.01,\n      \"lambda01_ppl\": 2.78,\n      \"lambda01_tf_gar_ours\": 0.49,\n      \"lambda01_ar_gar_ours\": 0.015,\n      \"lambda01_gap_ratio\": 32.7,\n      \"gpu_hours\": 2.0\n    },\n    \"tables\": [\n      {\n        \"caption\": \"λ_GAR Sensitivity: Impact on Training-Inference Gap\",\n        \"columns\": [\n          \"λ_GAR\",\n          \"TF GAR-ours\",\n          \"AR GAR-ours\",\n          \"Gap Ratio\",\n          \"PPL\",\n          \"Training Stable?\"\n        ],\n        \"rows\": [\n          [\n            \"0.1\",\n            \"0.49\",\n            \"0.015\",\n            \"32.7×\",\n            \"2.78\",\n            \"Yes (≈ LoRA-only)\"\n          ],\n          [\n            \"1.0 (v7 default)\",\n            \"0.50\",\n            \"0.016\",\n            \"31.3×\",\n            \"2.78\",\n            \"Yes\"\n          ],\n          [\n            \"10.0\",\n            \"0.52\",\n            \"0.018\",\n            \"28.9×\",\n            \"3.80\",\n            \"No (oscillation)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"λ sensitivity 在 worst case 下可放入 Appendix 但 paper value 极低。核心 takeaway（distribution shift independent of λ）是 correct 但 trivially expected。审稿人 'this confirms what we already know—the problem is not hyperparameter tuning but fundamental distribution mismatch.' 不给 novelty credit。 建议：仅在 Discussion 一句带过 'λ sensitivity analysis (Appendix X) confirms gap independence from loss weighting'，不要展开讨论。\\n\\n\\nλ=10：gate 远离 identity（mean 0.82，min 0.45），TF GAR 略高（0.52），但 PPL 严重恶化（3.80， +36.7% vs v7 2.78）。关键：AR GAR 仍崩溃到 0.018，gap 28.9×——distribution shift 不随 λ 改变。 Gate 学到更激进的 TF-context-specific attenuation，推理时这些模式无用。训练不稳定（loss oscillation）。 λ=0.1：GAR 信号太弱（loss 0.0003），gate frozen near 1.0（std 0.01），等价 LoRA-only。Gap 更大 32.7×。 两端都不改变核心结论。审稿人会说 'obviously increasing λ hurts NTP and decreasing it removes GAR signal—this is a trivial sensitivity analysis that adds nothing new.' 特别是 worst case 下审稿人 已认为 negative result incremental，再加一个 'trivial sensitivity' 只会 reinforce 这个印象。\\n\"\n  },\n  {\n    \"name\": \"TF vs AR Attention KL Divergence\",\n    \"description\": \"计算 per-head KL(P_TF || P_AR) 量化 attention distribution shift。 测试 GAR-relevant heads 是否显示更大 KL → exposure bias 的机制证据。\\n\",\n    \"results\": {\n      \"tg_mean_kl\": 0.054,\n      \"base_mean_kl\": 0.043,\n      \"tg_max_kl_layer\": \"L23\",\n      \"tg_max_kl_value\": 0.15,\n      \"high_kl_layers\": \"L9, L23-L27\",\n      \"gate_kl_correlation\": 0.11,\n      \"gate_kl_p_value\": 0.18,\n      \"gar_relevant_heads_mean_kl\": 0.072,\n      \"non_gar_relevant_heads_mean_kl\": 0.048,\n      \"kl_ratio_gar_vs_nongar\": 1.5,\n      \"n_conversations\": 50,\n      \"n_heads_per_layer\": 28,\n      \"n_layers\": 28,\n      \"n_total_head_layer_pairs\": 784,\n      \"gpu_hours\": 0\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Per-Layer-Group Attention KL Divergence (TF→AR)\",\n        \"columns\": [\n          \"Layer Group\",\n          \"Mean KL (TG)\",\n          \"Mean KL (Base)\",\n          \"Mean Gate Value\"\n        ],\n        \"rows\": [\n          [\n            \"L0-L7 (shallow)\",\n            \"0.032\",\n            \"0.029\",\n            \"0.94\"\n          ],\n          [\n            \"L8-L15 (mid)\",\n            \"0.048\",\n            \"0.039\",\n            \"0.93\"\n          ],\n          [\n            \"L16-L23 (deep-mid)\",\n            \"0.065\",\n            \"0.050\",\n            \"0.92\"\n          ],\n          [\n            \"L24-L27 (deep)\",\n            \"0.089\",\n            \"0.068\",\n            \"0.95\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"GAR-Relevant vs Non-Relevant Head KL\",\n        \"columns\": [\n          \"Head Category\",\n          \"Mean KL\",\n          \"N heads\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"GAR-relevant (top-10% goal-attention)\",\n            \"0.072\",\n            \"78\",\n            \"Slightly higher shift\"\n          ],\n          [\n            \"Non-GAR-relevant\",\n            \"0.048\",\n            \"706\",\n            \"Background level\"\n          ],\n          [\n            \"Ratio\",\n            \"1.50×\",\n            \"-\",\n            \"Weak selectivity signal\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"KL 分析在 worst case 下是 underwhelming supplementary evidence。0.054 mean KL 是 small effect， 不足以 standalone support distribution shift claim。作为 Appendix 可保留（诚实报告），但 main text 不应过度强调。审稿人可能 ignore 或 attack：\\\"if KL is this small, maybe distribution shift isn't really the mechanism—maybe it's something else entirely that you haven't measured.\\\" Worst case 下这部分损害论文更多（给审稿人攻击弹药）而非帮助。建议 Appendix only。\\n\\n\\nKL divergence 整体偏小（mean 0.054 nat），不到 0.1。虽然 GAR-relevant heads 略高（0.072 vs 0.048）， ratio 仅 1.5×——不够 dramatic 来解释 8× GAR gap。Gate-KL correlation 极弱（r=0.11, p=0.18 不显著）， 说明 gate 与 attention distribution shift 无关联——gate 未学到在 high-shift layers 做更强干预。 High-KL layers（L23-L27）在深层，但与 gate attenuation 集中层不完全吻合（gate 最低在 L3-L5）。 审稿人两个攻击角度：(1) \\\"KL 0.054 解释不了 8× gap——一定有其他因素（error accumulation、 sequential compounding）你没测到\\\"；(2) \\\"gate-KL 无相关说明 gate 根本不 tracking the relevant signal\\\"。 总体：提供 weak supplementary evidence，但不能作为 independent contribution。\\n\"\n  },\n  {\n    \"name\": \"Llama-3.1-8B Scheduled Sampling\",\n    \"description\": \"在 Llama-3.1-8B 上复现 SS 训练（time-scheduled sampling + GAR auxiliary loss）， 验证 gap 压缩是否跨模型泛化。若 Llama gap 同样压缩 → SS 是 general mitigation。\\n\",\n    \"results\": {\n      \"training_converged\": true,\n      \"epochs_completed\": 3,\n      \"total_steps\": 3000,\n      \"wall_clock_hours\": 10.5,\n      \"final_ntp_loss\": 0.928,\n      \"final_gar_loss\": 0.0012,\n      \"final_gate_mean\": 0.92,\n      \"final_gate_std\": 0.065,\n      \"ss_ratio_final\": 0.5,\n      \"ss_steps_used\": 5100,\n      \"tf_eval\": {\n        \"gar_ours\": 0.47,\n        \"gar_dongre\": 0.35,\n        \"ppl\": 2.6,\n        \"n_conversations\": 50\n      },\n      \"ar_eval_beta0\": {\n        \"gar_ours\": 0.04,\n        \"gar_ours_std\": 0.03,\n        \"gar_dongre\": 0.025,\n        \"ppl\": 1.4,\n        \"n_conversations\": 20\n      },\n      \"ar_eval_beta3\": {\n        \"gar_ours\": 0.52,\n        \"ppl\": 1.58\n      },\n      \"ar_eval_beta5\": {\n        \"gar_ours\": 0.68,\n        \"ppl\": 1.75\n      },\n      \"gap_ratio_beta0\": 11.75,\n      \"gap_ratio_vs_llama_tg\": 0.74,\n      \"gap_ratio_vs_qwen_ss\": \"Qwen 1.3× vs Llama 11.75×\",\n      \"ss_independent_benefit_beta0\": 0.01\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Scheduled Sampling Cross-Model Comparison (β=0, AR eval)\",\n        \"columns\": [\n          \"Model\",\n          \"SS TF GAR\",\n          \"SS AR GAR (β=0)\",\n          \"Gap Ratio\",\n          \"TG AR GAR (β=0)\",\n          \"SS Benefit\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen-2.5-7B (3-seed)\",\n            \"0.498±0.004\",\n            \"0.390±0.036\",\n            \"1.28×\",\n            \"0.064\",\n            \"+0.326\"\n          ],\n          [\n            \"Llama-3.1-8B\",\n            \"0.47\",\n            \"0.04\",\n            \"11.75×\",\n            \"0.030\",\n            \"+0.010\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Llama SS β-Sweep (AR eval, N=20)\",\n        \"columns\": [\n          \"β\",\n          \"SS AR GAR\",\n          \"TG AR GAR (no SS)\",\n          \"SS Incremental\",\n          \"PPL\"\n        ],\n        \"rows\": [\n          [\n            \"0\",\n            \"0.040\",\n            \"0.030\",\n            \"+0.010\",\n            \"1.40\"\n          ],\n          [\n            \"3\",\n            \"0.520\",\n            \"0.556\",\n            \"-0.036\",\n            \"1.58\"\n          ],\n          [\n            \"5\",\n            \"0.680\",\n            \"0.727\",\n            \"-0.047\",\n            \"1.75\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Llama TF Eval Comparison\",\n        \"columns\": [\n          \"Variant\",\n          \"GAR-ours\",\n          \"GAR-Dongre\",\n          \"PPL\"\n        ],\n        \"rows\": [\n          [\n            \"Base\",\n            \"0.017\",\n            \"0.004\",\n            \"3.45\"\n          ],\n          [\n            \"TG v7\",\n            \"0.484\",\n            \"0.018\",\n            \"2.57\"\n          ],\n          [\n            \"SS\",\n            \"0.470\",\n            \"0.350\",\n            \"2.60\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Llama SS failure 是 worst tier 的 cascade trigger： (1) SS 不能作为论文第 5 个 contribution——cross-model failure 意味着 'SS transfers to multi-turn transformer attention objectives' 的 claim 不成立（只在 1/2 模型上成立）。 (2) 论文必须放弃完整弧叙事。Title 不能暗示 recovery/remedy。 (3) SS 降级为 Discussion 的 'attempted mitigation, model-specific partial success'。 (4) 但 SS failure 本身有 diagnostic value：even explicitly exposing model to its own generation doesn't bridge distribution shift on Llama → 更强的 impossibility signal。 (5) 与 Dongre convergent evidence 更强：gating fails × 2 models + SS fails on Llama =  5/6 intervention-model combinations fail（只有 Qwen SS 成功）。 (6) Paper score 从 best-case 3.5 降到 2.5-3.0。Main conference 无望，Findings borderline。\\n\\n\\n这是 worst tier 的 defining failure point。Llama SS 训练正常收敛（loss 与 Llama TG v7 comparable）， TF eval 显示 SS 确实学到 GAR pattern（TF GAR 0.47 ≈ Llama TG 0.48）。但 AR eval β=0 仅 0.04， 远低于 Qwen SS 的 0.39。Gap ratio 11.75× 仍是 dramatic failure。\\nSS 在 Llama 上失败的可能机制： (1) Llama tokenizer 与 Qwen 不同（BPE vocab 128k vs 151k），model-generated text 的分布偏离 gold text 更远——SS 暴露的分布与推理分布仍不匹配。 (2) Llama 32 层 + 更深的 gate attenuation pattern（L25 gate 0.719）意味着 SS 需更长训练 才能 penetrate deeper layers。3 epochs 不够。 (3) Llama base GAR 更低（0.009 vs Qwen 0.019），从更低起点恢复更困难。 (4) Llama 在 SS step 上生成文本质量更低（更多 hallucination/repetition），SS exposure 引入的分布 noise 大于 signal。\\nβ=3/5 时 inference-time steering 仍有效（0.52, 0.68），但这是 steering 功劳而非 SS。 SS 在 Llama 上的 independent value（β=0 增量 +0.01 over TG baseline 0.03）接近 0。\\n结论：SS 是 model-specific mitigation，不是 general solution。论文必须放弃 'discover→diagnose→remedy' 弧，SS 不能作为第 5 个 contribution。\\n\"\n  },\n  {\n    \"name\": \"SS 3-Seed Validation (Qwen)\",\n    \"description\": \"Qwen SS 3 seeds (s42/s123/s456) 的 AR eval with β=0,3,5，提供 mean±std。回应 W7 单 seed 质疑。\\n\",\n    \"results\": {\n      \"tf_gar_ours\": {\n        \"s42\": 0.503,\n        \"s123\": 0.495,\n        \"s456\": 0.496,\n        \"mean\": 0.498,\n        \"std\": 0.004\n      },\n      \"ar_beta0_gar\": {\n        \"s42\": 0.347,\n        \"s123\": 0.4,\n        \"s456\": 0.422,\n        \"mean\": 0.39,\n        \"std\": 0.036,\n        \"cv_pct\": 9.2\n      },\n      \"ar_beta3_gar\": {\n        \"s42\": 0.593,\n        \"s123\": 0.59,\n        \"s456\": 0.605,\n        \"mean\": 0.596,\n        \"std\": 0.008\n      },\n      \"ar_beta5_gar\": {\n        \"s42\": 0.717,\n        \"s123\": 0.717,\n        \"s456\": 0.716,\n        \"mean\": 0.717,\n        \"std\": 0.001\n      },\n      \"ppl_beta0\": {\n        \"s42\": 1.44,\n        \"s123\": 1.441,\n        \"s456\": 1.442,\n        \"mean\": 1.441,\n        \"std\": 0.001\n      },\n      \"gap_ratio\": {\n        \"s42\": 1.45,\n        \"s123\": 1.24,\n        \"s456\": 1.18,\n        \"mean\": 1.29,\n        \"range\": \"[1.18, 1.45]\"\n      },\n      \"s42_is_outlier_at_beta0\": true,\n      \"n_ar_conversations_per_seed\": 39\n    },\n    \"tables\": [\n      {\n        \"caption\": \"SS 3-Seed AR Eval Results (Qwen-2.5-7B, N=39 valid conversations per seed)\",\n        \"columns\": [\n          \"Metric\",\n          \"s42\",\n          \"s123\",\n          \"s456\",\n          \"Mean±Std\"\n        ],\n        \"rows\": [\n          [\n            \"TF GAR-ours\",\n            \"0.503\",\n            \"0.495\",\n            \"0.496\",\n            \"0.498±0.004\"\n          ],\n          [\n            \"AR GAR β=0\",\n            \"0.347\",\n            \"0.400\",\n            \"0.422\",\n            \"0.390±0.036\"\n          ],\n          [\n            \"AR GAR β=3\",\n            \"0.593\",\n            \"0.590\",\n            \"0.605\",\n            \"0.596±0.008\"\n          ],\n          [\n            \"AR GAR β=5\",\n            \"0.717\",\n            \"0.717\",\n            \"0.716\",\n            \"0.717±0.001\"\n          ],\n          [\n            \"PPL β=0\",\n            \"1.440\",\n            \"1.441\",\n            \"1.442\",\n            \"1.441±0.001\"\n          ],\n          [\n            \"Gap Ratio\",\n            \"1.45×\",\n            \"1.24×\",\n            \"1.18×\",\n            \"1.29±0.14\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"3-seed 在 worst case 下是 necessary but insufficient。W7 partially addressed（有 variance estimate）， 但审稿人重心转移到 Llama failure。'You showed 3 seeds on the model where it works, but it completely fails on the other model. The 3-seed result is uninteresting because cross-model generalization is the real test, and you failed it.' SS contribution 无论在 Qwen 上多稳定， 只要 Llama 失败就无法 claim generalizability。在 worst tier 中 SS 从 contribution #5 移除， 3-seed 数据放 Appendix。\\n\\n\\n3-seed mean AR GAR β=0 = 0.390 在 worst 范围 [0.38, 0.45] 的下端。s42 是明显 outlier （0.347 vs s123 0.400 / s456 0.422），std = 0.036，CV = 9.2%。\\nWorst case 审稿人攻击角度： (1) \\\"CV 9.2% 对 main result 偏高——3 seeds 中 s42 远低于其他两个，说明结果对 initialization 敏感。\\\" (2) \\\"s42 恰好是你 main paper 中展示的 seed，也是最差的——虽然不是 cherry-pick，但 optics 不好。\\\" (3) β=3/5 极稳定（std<0.01）说明 high-β steering 效果 robust，但 β=0 的 SS independent value 有 seed sensitivity。SS 真正的 independent contribution（β=0 without steering assist）不够 stable。 (4) 结合 Llama SS failure：\\\"3 seeds on one model proves nothing when the other model fails completely.\\\"\\nPPL 方差极小（±0.001），确认 SS 无 PPL cost。但 worst case 下审稿人不给 PPL neutrality credit。\\n\"\n  },\n  {\n    \"name\": \"Alternative GAR Definition Robustness\",\n    \"description\": \"4 种 token selection（last/all/first/goal-only）× 3 checkpoints（Base/TG/SS）， 测试 GAR 改善是否 robust across definitions。需 GPU re-eval（raw attention 未保存）。\\n\",\n    \"results\": {\n      \"base\": {\n        \"last_token\": 0.019,\n        \"all_token\": 0.022,\n        \"first_token\": 0.021,\n        \"goal_only\": 0.015\n      },\n      \"tg\": {\n        \"last_token\": 0.325,\n        \"all_token\": 0.025,\n        \"first_token\": 0.039,\n        \"goal_only\": 0.018\n      },\n      \"ss\": {\n        \"last_token\": 0.39,\n        \"all_token\": 0.062,\n        \"first_token\": 0.045,\n        \"goal_only\": 0.03\n      },\n      \"n_defs_tg_improves_clearly\": 1,\n      \"n_defs_ss_improves_clearly\": 1,\n      \"n_defs_ss_improves_marginally\": 1,\n      \"improved_definition\": \"last-token (ours)\",\n      \"marginal_definition\": \"all-token\",\n      \"not_improved\": [\n        \"first-token\",\n        \"goal-only\"\n      ],\n      \"gpu_hours\": 0.5\n    },\n    \"tables\": [\n      {\n        \"caption\": \"GAR Across Token Selection Definitions (AR eval, Qwen-2.5-7B)\",\n        \"columns\": [\n          \"Token Selection\",\n          \"Base\",\n          \"TG v7\",\n          \"SS v8b\",\n          \"SS/Base Ratio\",\n          \"Clearly Improved?\"\n        ],\n        \"rows\": [\n          [\n            \"Last-token (ours)\",\n            \"0.019\",\n            \"0.325\",\n            \"0.390\",\n            \"20.5×\",\n            \"Yes\"\n          ],\n          [\n            \"All-token (≈Dongre)\",\n            \"0.022\",\n            \"0.025\",\n            \"0.062\",\n            \"2.8×\",\n            \"Marginal\"\n          ],\n          [\n            \"First-token\",\n            \"0.021\",\n            \"0.039\",\n            \"0.045\",\n            \"2.1×\",\n            \"No (within noise)\"\n          ],\n          [\n            \"Goal-only tokens\",\n            \"0.015\",\n            \"0.018\",\n            \"0.030\",\n            \"2.0×\",\n            \"No (within noise)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Alternative GAR 分析在 worst case 下 damages the paper more than it helps。 审稿人会认为 GAR 改善是 metric-specific artifact：只有特定的 last-token summary-position 定义下才有效果。这触发 W3 escalation chain： (1) GAR 只对 last-token 有效 → metric fragility (2) Instruction retention r=0.2 → weak downstream correlation (3) Alternative definitions 无改善 → 'what exactly are you measuring?' 建议：在 worst case 叙事中将此放入 Appendix，main text 仅一句提及 'robustness analysis in Appendix X shows improvement concentrated on summary-position tokens, consistent with the training objective design.' 不要让审稿人在 main text 看到这个弱点。\\n\\n\\nWorst case：alternative_gar_defs_ss_improves 在 [0, 2] 范围内，取 1。\\nTG 只改善 last-token（0.325 vs base 0.019, 17×），all/first/goal-only 接近 baseline。 这说明 TG 学到的 attention pattern 高度 position-specific：只对 assistant response 最后 一个 token 的 goal attention 有效，对其他 response token positions 无效。\\nSS 同样主要改善 last-token（0.390），all-token 有 marginal 提升（0.062 vs 0.022, 2.8×） 但绝对值仍很低。First-token 和 goal-only 基本无改善（2× within noise level）。\\n审稿人会用这个数据攻击 GAR metric 本身的 validity： (1) \\\"GAR improvement is position-specific overfitting to last-token——不是真正改善了 goal attention\\\"。 (2) \\\"All-token GAR（最接近 Dongre 定义）在 SS 后仍然很低（0.062），说明你的方法没有 真正 address Dongre 发现的问题\\\"。 (3) W3 escalation 加剧：GAR 作为代理指标的 validity 被质疑 + instruction retention r=0.2 太弱 + 换个 GAR 定义结果就消失 = triple weakness。\\n\"\n  },\n  {\n    \"name\": \"SS 4th Seed (s789)\",\n    \"description\": \"第 4 个 Qwen SS seed 加强统计。ROI 低于 Llama SS 实验。\\n\",\n    \"results\": {\n      \"training\": {\n        \"epochs_completed\": 3,\n        \"wall_clock_hours\": 6.5,\n        \"final_loss\": 0.932,\n        \"final_gate_mean\": 0.955,\n        \"ss_ratio_final\": 0.5\n      },\n      \"s789_tf_gar_ours\": 0.5,\n      \"s789_ar_beta0_gar\": 0.3,\n      \"s789_ar_beta3_gar\": 0.58,\n      \"s789_ar_beta5_gar\": 0.71,\n      \"s789_ppl_beta0\": 1.442,\n      \"s789_gap_ratio\": 1.67,\n      \"four_seed_stats\": {\n        \"mean_beta0\": 0.367,\n        \"std_beta0\": 0.054,\n        \"cv_beta0_pct\": 14.7,\n        \"range_beta0\": \"[0.300, 0.422]\",\n        \"mean_gap\": 1.39,\n        \"std_gap\": 0.22\n      },\n      \"vs_three_seed\": {\n        \"mean_delta\": -0.023,\n        \"std_delta\": 0.018,\n        \"cv_delta\": 5.5\n      }\n    },\n    \"tables\": [\n      {\n        \"caption\": \"SS 4-Seed Comparison (if run)\",\n        \"columns\": [\n          \"Seed\",\n          \"AR GAR β=0\",\n          \"AR GAR β=3\",\n          \"AR GAR β=5\",\n          \"Gap Ratio\"\n        ],\n        \"rows\": [\n          [\n            \"42\",\n            \"0.347\",\n            \"0.593\",\n            \"0.717\",\n            \"1.45×\"\n          ],\n          [\n            \"123\",\n            \"0.400\",\n            \"0.590\",\n            \"0.717\",\n            \"1.24×\"\n          ],\n          [\n            \"456\",\n            \"0.422\",\n            \"0.605\",\n            \"0.716\",\n            \"1.18×\"\n          ],\n          [\n            \"789\",\n            \"0.300\",\n            \"0.580\",\n            \"0.710\",\n            \"1.67×\"\n          ],\n          [\n            \"4-seed Mean±Std\",\n            \"0.367±0.054\",\n            \"0.592±0.010\",\n            \"0.715±0.003\",\n            \"1.39±0.22\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"在 worst case 下 s789 是 actively harmful data point。建议决策矩阵： - 如果 s789 ≥ 0.37：加入增强统计 → run - 如果 s789 < 0.35：拉低 mean + 增大 CV → do not report - Worst case s789 = 0.30 → definitely do not run / do not include 此实验应 deprioritize below Llama SS 和所有 P0/P1 实验。8 GPU-hours 可更好地用于 Llama SS 或 paper writing。\\n\\n\\ns789 是 worst case 中的 low outlier（AR GAR β=0 = 0.300，gap 1.67×）。4-seed mean 拉低到 0.367，std 从 0.036 升到 0.054，CV 从 9.2% 升到 14.7%。\\n更多 seeds 反而暴露更大 variance，削弱 SS 可靠性叙事： (1) \\\"CV 14.7% 意味着 SS 的 independent value（β=0）高度依赖 random initialization\\\"。 (2) \\\"4 seeds 范围 0.30-0.42，跨越了 'meaningful improvement' 和 'marginal' 的分界线\\\"。 (3) \\\"s789 gap 1.67× 接近 Qwen TG v7 的 gap regime，说明某些 seed 下 SS 几乎不起作用\\\"。\\nβ=3/5 仍然稳定（0.580/0.710），因为 high-β steering 效果 dominant 且 seed-insensitive。 但 β=0 是 SS 独立价值的唯一指标，14.7% CV 不够 convincing。\\n强烈建议 worst case 下 NOT running s789。3-seed 的 0.390±0.036 虽不完美但可接受。 第 4 个 seed 如果拉低 mean 是自找麻烦。审稿人要求时可在 rebuttal 中补充。\\n\"\n  },\n  {\n    \"name\": \"Long Conversation Eval (>10 turns)\",\n    \"description\": \"测试 exposure bias gap 是否随对话长度增加而恶化。需从 UltraChat 筛选长对话。\\n\",\n    \"results\": {\n      \"turns_5\": {\n        \"base_ar_gar\": 0.02,\n        \"tg_ar_gar\": 0.06,\n        \"ss_ar_gar\": 0.42,\n        \"ss_benefit\": 0.4\n      },\n      \"turns_10\": {\n        \"base_ar_gar\": 0.01,\n        \"tg_ar_gar\": 0.02,\n        \"ss_ar_gar\": 0.38,\n        \"ss_benefit\": 0.37\n      },\n      \"turns_15\": {\n        \"base_ar_gar\": 0.006,\n        \"tg_ar_gar\": 0.008,\n        \"ss_ar_gar\": 0.22,\n        \"ss_benefit\": 0.214\n      },\n      \"turns_20\": {\n        \"base_ar_gar\": 0.004,\n        \"tg_ar_gar\": 0.005,\n        \"ss_ar_gar\": 0.12,\n        \"ss_benefit\": 0.116\n      },\n      \"ss_decay_rate_per_5turns_after_10\": \"~48%\",\n      \"tg_base_convergence_at_turns\": 15,\n      \"n_long_conversations\": 10,\n      \"eval_tokens_per_conversation\": \"~8000-12000\",\n      \"gpu_hours\": 2.0\n    },\n    \"tables\": [\n      {\n        \"caption\": \"GAR by Conversation Length (AR eval, Qwen-2.5-7B)\",\n        \"columns\": [\n          \"Turns\",\n          \"Base\",\n          \"TG v7\",\n          \"SS v8b\",\n          \"SS Benefit vs Base\"\n        ],\n        \"rows\": [\n          [\n            \"5\",\n            \"0.020\",\n            \"0.060\",\n            \"0.420\",\n            \"+0.400\"\n          ],\n          [\n            \"10\",\n            \"0.010\",\n            \"0.020\",\n            \"0.380\",\n            \"+0.370\"\n          ],\n          [\n            \"15\",\n            \"0.006\",\n            \"0.008\",\n            \"0.220\",\n            \"+0.214\"\n          ],\n          [\n            \"20\",\n            \"0.004\",\n            \"0.005\",\n            \"0.120\",\n            \"+0.116\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"SS Effectiveness Decay\",\n        \"columns\": [\n          \"Turn Range\",\n          \"SS AR GAR\",\n          \"Δ from turns 5\",\n          \"Decay (%)\"\n        ],\n        \"rows\": [\n          [\n            \"1-5\",\n            \"0.420\",\n            \"-\",\n            \"-\"\n          ],\n          [\n            \"6-10\",\n            \"0.380\",\n            \"-0.040\",\n            \"9.5%\"\n          ],\n          [\n            \"11-15\",\n            \"0.220\",\n            \"-0.200\",\n            \"47.6%\"\n          ],\n          [\n            \"16-20\",\n            \"0.120\",\n            \"-0.300\",\n            \"71.4%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Long conversation eval 在 worst case 下提供 damaging but honest evidence。它表明 SS mitigation 有 limited effective range（≤10 turns）。结合 Llama failure，SS 的 contribution 变成 'limited preliminary result on one model for short conversations only'——不够 conference contribution。 建议：在 worst case diagnostic paper 中诚实报告此 limitation，放入 Discussion §7.3 'Scalability Limitations of Scheduled Sampling'。诚实承认 limitation 可能 earn reviewer respect ('self-aware about limitations')，比隐瞒好。但不改变 paper 从 3.0 以上下降的趋势。\\n总体 worst case paper structure 调整： §5 Results 只含 main negative findings（NF1-NF3, gating zero-increment, cross-model replication）。 §6 Analysis 含 PCGrad causal exclusion + distribution shift。 §7 Discussion 含 SS attempted mitigation（Qwen partial success, Llama failure, length limitation） + Dongre convergent evidence + concrete future directions。 §8 Conclusion 重述 failure mode taxonomy 的系统分类学价值。 Expected Findings score: 2.5-3.0。\\n\\nSS 在 ≤10 turns 维持 0.38-0.42 AR GAR（与 3-seed mean 一致），但 15 turns 后急剧下降到 0.22，20 turns 降到 0.12。每 5 turns 衰减约 48%。\\n机制推测：SS 训练数据中 model-generated context 比例线性递增（scheduled），但长对话中 error accumulation 是 super-linear——每个 turn 的小偏差在后续 turns 被 compound。SS 暴露 的训练分布（线性 mix）与 20-turn 推理分布（exponential error accumulation）仍有 gap。\\n审稿人 devastating critique： (1) \\\"SS 只在短对话（≤10 turns）有效，但 GAR 退化本身就是长对话问题（Dongre 测了 50 turns） ——你的 mitigation 恰好在最需要的地方失效。\\\" (2) \\\"你论文的 motivation 来自 Dongre 的 50-turn scenario，但你的 fix 在 15+ turns 就崩溃。\\\" (3) \\\"这与 scope limitation（W2/R1）结合——不仅 method-specific + model-specific，还 length-specific。\\\"\\nTG 和 Base 在 15+ turns 已无区分（0.008 vs 0.006），再次确认 gating zero-increment 在长对话中成立。\\n但有一个 silver lining：SS 衰减曲线本身是有价值的 diagnostic insight——它量化了 SS 暴露 与真实推理分布的 gap 如何随 conversation length 增长。可作为 Discussion 中 'limitations of time-scheduled SS' 的 empirical evidence。\\n\"\n  }\n]",
      "numLines": 867,
      "startLine": 1,
      "totalLines": 867
    }
  },
  "sourceToolAssistantUUID": "61f2a39c-4a7d-4e5a-8c32-7886c8ffd677",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-24T08:57:56.125Z_

<details open><summary>🔧 Tool call — Read · `toolu_01R9dF1qANjAMJUh4hkSFJds`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9bd8604-67aa-4918-ac73-c23ae34b0be5",
  "isSidechain": false,
  "requestId": "req_011CbM7jyFnyKmEHmsQTUsuU",
  "type": "assistant",
  "uuid": "8416a7ef-17cf-40f7-bcfb-a980ebc3f927",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RYbw6r2nCrk4tniiVDmxTs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13904,
      "cache_read_input_tokens": 11447,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13904,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 13904,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13904
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

_source line 12 · 2026-05-24T08:57:56.134Z_

<details><summary>↩ Tool result · `toolu_01R9dF1qANjAMJUh4hkSFJds`</summary>

```text
1	# Paper Framing: Mechanistic Analysis of Training-Inference Distribution Shift in Attention Steering
2	
3	> 定位: **Mechanistic insight paper**（不是简单 negative result）。核心卖点是 teacher-forcing→generation 分布偏移如何摧毁 lightweight residual gating 的 auxiliary attention loss 泛化性（8×–27× gap，Qwen 7.8× / Llama 27× median）。这个 insight 为 auxiliary attention loss 在 teacher-forcing 下的 exposure bias 脆弱性提供首个实证刻画。**SS 初步修复: AR GAR 0.401±0.047（3-seed mean±std），TF/AR gap ~1.3×（range 1.15–1.45×）。**
4	> Novelty 排序: (1) exposure bias 对 auxiliary attention loss 泛化性的首个实证刻画 (8×–27× gap) > (2) PCGrad 因果排除梯度方向冲突 + "观察→假设→排除→指向真因" 完整因果链 (D028) > (3) SS 迁移到 multi-turn transformer attention objectives (AR GAR 0.401±0.047, 3-seed) > (4) principled intervention + systematic ablation 的 negative result
5	> **⚠️ Dream review D024: "Cannot" overclaims, novelty "first measurement" 过高, 缺 gradient surgery baseline (PCGrad). 标题改 "Fails to", novelty 降级 "first empirical characterization"**
6	> 目标会议: EMNLP 2026, ARR August cycle, deadline 2026-08-03 (~10.5 weeks)
7	> 最后更新: 2026-05-24 (3-seed SS 数据完成: AR GAR 0.401±0.047, gap ~1.3× range 1.15–1.45×; β=3/5 跨 seed 极稳定 std<0.01; s42 是 β=0 outlier)
8	> **⚠️ Llama-3 跨模型验证 = MUST-HAVE**（不含 → Findings 3.0 紧绷；含 → 3.0-3.5）
9	> **Framing 升级目标 3.5**: 对标 gromov2024/sun2025/xiao2024 "发现→定位→修复" 模式。SS AR GAR 0.401±0.047 (3-seed, vs base 0.019) 是真正的 positive result，不应埋在 Discussion。
10	
11	---
12	
13	## 1. Title Candidates
14	
15	- **T0 (当前)**: Exposure Bias Selectively Destroys Auxiliary Attention Losses in Multi-Turn Dialogue: A Diagnostic Analysis of Per-Layer Residual Gating
16	- **T1**: Exposure Bias Selectively Destroys Auxiliary Attention Losses in Multi-Turn Dialogue （去掉副标题，更简洁有力）
17	- **T2**: From Collapse to Recovery: Diagnosing and Mitigating Exposure Bias in Multi-Turn Attention Objectives （强调完整弧：发现+定位+修复）
18	- **T3**: The Exposure Bias Barrier: Why Auxiliary Attention Losses Fail at Multi-Turn Inference （barrier metaphor，聚焦机制）
19	
20	推荐 T1 或 T2。T1 保留当前论文最有记忆点的短语 "selectively destroys"，去掉冗长副标题。T2 强调 "发现→定位→修复" 完整弧，与 gromov2024/xiao2024 对标。T0 过长（20 词），审稿人可能记不住。T3 偏负面。
21	
22	---
23	
24	## 2. Story Arc
25	
26	Multi-turn dialogue performance in LLMs degrades as conversations grow longer. Dongre et al. (2026) quantified this through the Goal Accessibility Ratio (GAR), showing 27-48% drops over 50 turns, while their residual stream probes reveal that goal information persists (AUC up to 0.98) even as the attention channel closes. This creates a natural hypothesis: if the information is in the residual stream but attention fails to access it, a learnable gate on the residual connection should recover it. We implement this hypothesis as ThreadGate, a per-layer gating module trained with joint NTP and GAR objectives. ThreadGate successfully optimizes GAR during training (0.02 to 0.48), and this improvement transfers perfectly when evaluated on same-distribution text at inference (GAR-ours = 0.49). However, on model-generated text, GAR-ours collapses to 0.064 (Qwen N=50, 7.8× gap) or 0.018 (Llama N=20, 27× gap), driven by text distribution shift. Our central finding is that attention patterns learned under teacher-forced contexts (gold text) do not generalize to autoregressive generation contexts (model-generated text), the classic exposure bias phenomenon. This distribution shift is structural, independent of loss design or gating architecture. We further identify two coupled mechanisms that amplify the shift: (1) NTP loss dominates gate gradients, causing gates to learn reverse turn conditioning (suppressing at early turns where GAR is high, becoming passive at late turns where intervention is needed); (2) at inference time, gates attenuate residual updates by only 2-7%, far too weak to shift attention patterns. Four-way ablation (ThreadGate vs. Uniform Gate vs. LoRA-only vs. Base) confirms gating provides zero incremental contribution. Notably, this 8×–27× gap is specific to GAR-ours (last-token attention to goals); GAR-Dongre (all-token attention) shows uniformly low values regardless of text distribution, revealing that exposure bias selectively disrupts summary-position attention patterns. Combined with Dongre et al.'s independent failure of goal re-injection, our results provide the first empirical characterization of how text distribution shift (exposure bias) selectively destroys attention patterns learned through auxiliary losses, and identify the specific mechanisms through which this vulnerability manifests. Crucially, we show that scheduled sampling—originally designed for RNN sequence models—transfers to multi-turn transformer attention objectives, compressing the TF–AR gap from 8× to ~1.3× with no perplexity cost (3-seed: AR GAR 0.401±0.047, PPL 1.441±0.001). Inference-time β-steering independently recovers GAR from 0.064 to 0.727. These mitigation results upgrade the paper from pure negative result to a complete "discover → diagnose → initial remedy" arc, matching the narrative pattern of high-impact diagnostic papers (gromov2024, sun2025, xiao2024).
27	
28	---
29	
30	## 3. Core Claims
31	
32	| # | Claim | 支撑 | 状态 |
33	|---|-------|------|------|
34	| C1 | GAR 衰减是真实且严重的结构性现象: Qwen-2.5-7B raw GAR 下降 70.8%, normalized GAR 下降 ~21% | Phase 1 GAR 诊断 | ✅ 已验证 |
35	| C2 | Residual gating 训练时在 same-distribution text 上有效优化 GAR-ours (TF GAR=0.50)，但在 model-generated text 上完全失败 (AR GAR=0.064, 7.8× gap on Qwen N=50; 27× median on Llama N=20)。GAR-Dongre 在两种分布上均低，无 gap——说明分布偏移选择性影响 summary-position attention pattern。 | v7 训练 + d048 N=50 eval + Llama eval + Reviewer 独立验证 | ✅ 已验证（N=50 precision） |
36	| C3 | 失败机制的因果分析: (1) Distribution shift 是主因（D028 PCGrad 因果排除梯度方向冲突）; (2) NTP 幅度主导 gate 学习 → NF1 反向 turn conditioning; (3) NF3 gate 干预强度不足 2-7%。PCGrad ablation: 消除方向冲突后 cos_sim 围绕 0 震荡(range -0.151 to +0.091)，但 L_GAR 坍塌轨迹不变且无延迟 → 方向冲突非因果因素。**推理端确认（IID same-protocol）**: v9 GAR-ours=0.0151 vs v7=0.0157 (差<0.1pp), **v9 IID PPL=2.780 vs v7=2.784 (差0.004，无改善)**——PCGrad 消除方向冲突后所有可观测指标均 ≈ v7，方向冲突因 NTP 幅度主导而完全 inconsequential | D014 gate-profile + 梯度冲突量化 + **D028 PCGrad 因果排除** + v9 推理 eval + **M017 PPL 修正** | ✅ **End-to-end 完成**: 训练端 + 推理端均确认梯度方向冲突对 GAR 和 PPL 均无因果影响 |
37	| C4 | Gating 无增量贡献: 四路消融 LoRA-only ≈ TG ≈ UG（GAR + PPL 双指标）。IID: GAR 差异<0.6pp, PPL 均 ~2.78。**Model-gen (D033): v9 PCGrad=0.0151, UG=0.0149, LoRA-only=0.0245 均接近 baseline 0.0122——8×–27× gap 在所有训练变体上普遍存在，排除 gating mechanism / turn-conditioning / gradient conflict 作为因果因素** | D021 四路 eval + D033 model-gen eval | ✅ **双重验证**: IID (D021) + model-gen (D033)。model-gen regime 进一步确认 gating 零增量且 GAR collapse 是训练-推理分布偏移的普遍现象 |
38	| C5 | 跨模型验证: Llama-3.1-8B 上复现同样的失败模式 | Phase 1 ✅ (GAR decay 80.2%, D042), Phase 2 ✅ (TG gap 27× median, gating zero-increment TG≈LO, LoRA-only N=20 eval) | ✅ Fully confirmed |
39	
40	---
41	
42	## 4. Negative Findings (NF)
43	
44	| # | Finding | 证据 | 叙事角色 |
45	|---|---------|------|----------|
46	| NF1 | Gate turn conditioning 方向反转: 27/28 层 gate diff (turn1-turn21) < 0，早期 turn 强抑制，晚期 turn passive | D014 eval gate-profile | 解释 why gating fails: NTP 梯度推 gate→1.0，晚期 turn 推力最强 |
47	| NF2 | 8×–27× text distribution shift gap (GAR-ours): TF GAR=0.50 vs AR GAR=0.064 (Qwen N=50, 7.8× gap); Llama AR GAR=0.018 (27× median gap, N=20)。Same-distribution 泛化成功（TF eval GAR=0.50），cross-distribution 泛化失败。**D033 跨变体确认**: v9 PCGrad, UG, LoRA-only model-gen GAR 均接近 baseline——gap 独立于训练策略，是 exposure bias 的普遍表现。GAR-Dongre 在两种分布上均低，无 gap——分布偏移选择性影响 summary-position (last token) attention pattern | d048 N=50 eval + Llama eval + D033 cross-variant | 核心 negative finding。精确定位为 TEXT DISTRIBUTION SHIFT（exposure bias）。 |
48	| NF3 | 推理时 gate attenuation 仅 2-7% (gate_mean=0.93-0.98)，近乎 identity | D014 gate dynamic range 数据 | 解释 why 推理时 GAR 不改善: 干预强度不足 |
49	| NF4 | Eval baseline confound (Phase1 base vs Phase2 LoRA 文本不同) | P0 代码分析 | 已修正 → standard_conversations.json 统一 eval |
50	
51	---
52	
53	## 5. Key Selling Points
54	
55	**SP1 (核心卖点): Exposure bias 对 auxiliary attention loss 泛化性的首个实证刻画。** 8×–27× training-inference GAR-ours gap（Qwen 7.8×, Llama 27× median）提供了 teacher-forcing distribution shift 如何摧毁 auxiliary attention loss 泛化性的实证证据。训练时模型在 gold context 上优化 attention pattern，推理时在自身生成的 context 上条件化——两者分布不同导致 attention pattern 不迁移。虽然 exposure bias 概念本身已知 (Bengio et al. 2015)，且 sequence generation 中有量化先例 (Ranzato et al. 2016, Wiseman & Rush 2016)，但此前无人刻画其对 auxiliary attention loss 的具体影响。我们的 8×–27× gap 测量展示了这种脆弱性在 attention steering 场景下的严重程度。**注意：(1) claim scope 严格限于 lightweight residual gating + GAR auxiliary loss 的实测范围，不泛化到所有 attention steering 方法。(2) gap 在 GAR-ours（last token only, summary-position attention）上测得（TF 0.50 vs AR 0.064 Qwen / 0.018 Llama）；GAR-Dongre（all response tokens）在两种分布上均低，无 gap——表明 exposure bias 选择性影响 summary-position attention pattern，这一差异本身有分析价值。**
56	
57	**SP2: NTP-GAR 梯度动力学 + PCGrad 因果排除（gradient conflict is inconsequential）。** 观察到 67-79% 的层 NTP-GAR 梯度方向冲突（cos_sim<0）+ NTP 幅度 3-15x 压制 GAR（mag_ratio 7.5→14.7x）。**PCGrad 消融（D028）因果排除方向冲突**：投影后 cos_sim 围绕 0 震荡（range -0.151 to +0.091），L_GAR 坍塌轨迹不变。**推理端确认（IID same-protocol）**: v9 IID PPL = 2.780 vs v7 = 2.784（差 0.004，无改善）; v9 GAR-ours = 0.0151 vs v7 = 0.0157（差 <0.1pp）——**PCGrad 消除方向冲突后所有可观测指标均无变化**（GAR、PPL、NTP 均 ≈ v7）。方向冲突虽然可测量存在于 v7 中，但对训练和推理结果无任何因果影响——7.5–14.7× NTP 幅度主导使方向冲突完全无关紧要（inconsequential）。**⚠️ M017: 此前 "PPL -46%" 和 "selective dissociation" 论述为跨协议对比伪影（model-gen PPL 1.50 vs IID PPL 2.78），已撤回。** **精确 claim scope**: gradient direction conflict is **neither necessary nor sufficient** for the 8×–27× GAR gap; exposure bias alone is sufficient。NOT necessary: 移除冲突→gap仍在; NOT sufficient: v7有冲突但L_GAR训练时收敛; Exposure bias is sufficient: 训练≠推理分布→GAR泛化失败。**Gate 行为额外 insight**: v9 gate dynamic range 比 v7 更宽 (L15 range 0.33 vs v7 0.21)——PCGrad 给 gate 更大自由度，但 gate 用该自由度更激进地优化 NTP 而非 GAR，说明优化景观固有偏好语言建模目标。
58	
59	**SP3: Principled 设计动机 + 系统性探索。** Dongre 发现 goal info 在 residual stream 持续存在 (probe AUC=0.98)，residual gating 是最直接的架构响应。v1-v7 覆盖 4 种核心 loss 设计 across 7 training configurations，MSE+gate_div 是唯一训练收敛方案。四路消融严格隔离贡献: TG (learned gate + GAR loss) / UG (uniform gate + GAR loss) / LoRA-only (gate=1.0 fixed + GAR loss, 无 gating 机制) / Base。注意：三个 fine-tuned 变体均使用 GAR loss，消融测试的是 gating 机制的增量贡献，而非 GAR loss 本身的效果。
60	
61	**SP4: Convergent evidence with Dongre。** Dongre diagnosed the problem; we attempted the first systematic cure and uncovered fundamental limitations。两种独立干预路线（goal re-injection + residual gating）均失败，共同指向 NTP 优化压力下 attention steering 的根本困难。
62	
63	**SP5: 三阶段训练动力学。** v7 展现 plateau → phase transition → convergence 的清晰训练动力学，证明 MSE 双向 loss 设计本身是 sound 的，问题在泛化而非训练。
64	
65	---
66	
67	## 6. Anticipated Reviewer Concerns
68	
69	| # | 严重度 | 预期质疑 | 回应策略 |
70	|---|--------|----------|----------|
71	| W1 | **致命** | 单模型验证不够 | Llama-3.1-8B 跨模型验证是 **MUST-HAVE**。Qwen 完整消融 + Llama 复现。不含 Llama → Findings 3.0 紧绷，含 → 3.0-3.5。 |
72	| W2 | **严重** | "你只是没调对参数" | D018 的 teacher-forcing 分布偏移是结构性的，与 loss 设计无关。v1-v7 已覆盖 4 种核心 loss (cumulative v1-v2, maximize v3-v5, smooth_saturation v6, mse_target v7)，MSE+gate_div 是唯一训练收敛方案。四路消融隔离 turn conditioning (TG vs UG) 和 gating 本身 (TG vs LoRA-only)，消除超参解释。 |
73	| W3 | **严重** | GAR 作为唯一代理指标 | 考虑加 1 个简单下游任务 sanity check（如 system prompt instruction following accuracy）。PPL 对比已加入四路 eval（TG PPL > LoRA-only → gates 有害的额外证据）。 |
74	| W4 | **中等** | 无建设性贡献 | Discussion 需要 constructive future directions section: (1) inference-time attention intervention 绕过训练泛化问题; (2) decoupled goal-processing pathway; (3) GAR-aware decoding 而非 GAR-aware training; (4) exposure bias mitigation 技术应用到 auxiliary attention loss。 |
75	| W5 | **中等** | Teacher-forcing insight 不新（exposure bias 文献已知） | 我们的增量: 定量展示 distribution shift 如何具体破坏 auxiliary attention loss（8×–27× 断层），现有 exposure bias 文献无此分析。Exposure bias 讨论集中在 generation quality degradation，未涉及 auxiliary attention loss 的泛化失败。 |
76	| R1 | 中等 | Novelty of negative result | 核心增量不是 negative result 本身，而是 distribution shift insight（SP1）+ 梯度竞争量化（SP2）+ failure mode taxonomy。 |
77	| R2 | 中等 | 与 Dongre et al. 的关系 | 不说 "we extend Dongre"，而是 "Dongre diagnosed; we attempted the first systematic cure and uncovered fundamental limitations"。核心叙事是 mechanism discovery，非 follow-up work。 |
78	| W6 | **严重** | 引用不足（Dream review: 11篇远不够）| 目标 25-30 篇。必须覆盖: attention sinks (Xiao et al. 2024), Found-in-the-Middle (Ko et al. 2024), gated attention (Qiu et al. 2025), transformer circuits (Elhage et al. 2021), FlexiDepth (Luo et al. 2025), multi-turn eval (MT-Bench-101, MultiChallenge), exposure bias mitigation (Professor Forcing, SEARNN) 等。Paper Agent 写作时负责扩充。|
79	| W7 | **严重** | 单 seed 无方差估计 | 所有实验 seed=42，TG-LoRA 差异 ±0.001 在噪声层。回应: held-out eval 50 conversations 提供 paired bootstrap CI，若 CI 包含 0 则统计支持 "zero benefit"。必要时追加 2 个 seed 的训练。|
80	| W8 | **中等** | 缺 exposure-bias mitigation 实验 | 测试 scheduled sampling / model-generated context 训练能否缩小 8×–27× gap。加入 experiment_plan (P1)。如果实验表明 mitigation 确实缩小 gap，论文从 "negative result" 升级为 "negative result + constructive direction"。|
81	| R1 | 中等 | Novelty of negative result | 核心增量不是 negative result 本身，而是 exposure bias 的定量测量（SP1）+ 梯度竞争量化（SP2）+ failure mode taxonomy。 |
82	| R2 | 中等 | 与 Dongre et al. 的关系 | 不说 "we extend Dongre"，而是 "Dongre diagnosed; we attempted the first systematic cure and uncovered fundamental limitations"。核心叙事是 mechanism discovery，非 follow-up work。 |
83	| R3 | 低 | 8×–27× gap 是否可能是实现 bug | D015 代码逐行对比 + D017 controlled experiments 确认非 bug。Base model 在 ultrachat 和 eval data 上 GAR 均 ~0.01，排除数据分布解释。 |
84	| R4 | ~~低~~ **已核实** | Code-paper 公式语义相反 | **已确认不一致（plan_017 DONE）**。代码正确实现 ReZero-style: `x_{l+1} = x_l + g_l · f_l(x_l)`（gate 缩放子层输出，g→0=层 no-op）。Dream paper.tex 错误写为 `x_{l+1} = g_l · x_l + f_l(x_l)`（gate 缩放残差流，g→0=破坏 skip connection）。**实验数据不受影响**（所有实验用同一份代码）。**Paper Agent 写作时必须**: (1) Method section 用正确公式 `x + g·f(x)`; (2) 机制叙事修正: g→0 = 子层输出被抑制（层变 no-op），NTP 推 g→1 是为保留层计算能力，不是保留 skip connection; (3) NF3 "gate attenuation 2-7%" 指子层贡献缩放，表述正确但需明确。|
85	
86	---
87	
88	## 7. Dongre et al. 关系定位
89	
90	| 维度 | Dongre et al. | 本文 |
91	|------|---------------|------|
92	| 核心问题 | "发生了什么" + "为什么" | "怎么干预" + "为什么干预失败" |
93	| GAR 衰减 | 定义 GAR，12 模型量化衰减 | 独立确认 (Qwen 70.8% raw, 21% normalized) |
94	| 机制分析 | residual probe AUC=0.98 (goal info 持续存在) | NTP-GAR 梯度冲突 + 8×–27× 泛化 gap + turn conditioning 反转 |
95	| 干预尝试 | goal re-injection (Appendix H, 失败) | ThreadGate residual gating (失败) + UG/LoRA-only 消融 |
96	| 结论 | attention 通道关闭但 residual stream 保留 goal info | 即使在 residual stream 上施加 principled gating，NTP 梯度压制使 gate 无法学到正确的 turn-selective 干预 |
97	
98	**定位语**: Dongre diagnosed the problem; we attempted the first systematic cure and uncovered fundamental limitations. 核心叙事是 mechanism discovery（distribution shift + gradient competition），不是 Dongre 的 follow-up。
99	
100	共同推论: 两种独立干预路线均失败 → lightweight residual gating with auxiliary attention loss 在 teacher-forcing 下面临严重泛化障碍（8×–27× gap）→ 需要 inference-time 干预或 exposure bias mitigation（SS 已验证可将 gap 压缩到 ~1.3×（3-seed: AR GAR 0.401±0.047））。（注意：scope 限于 lightweight gating，不泛化到所有 attention steering 方法。）
101	
102	---
103	
104	## 8. GAR 定义策略
105	
106	| 用途 | 定义 | Goal tokens | Response tokens | 理由 |
107	|------|------|------------|----------------|------|
108	| 训练信号 | GAR-ours | system prompt + first user query | last token per assistant turn | 更丰富的 goal 信号; last token 作为 summary position 更稳定 |
109	| 主表评估 | GAR-Dongre | system prompt task tokens only | all response tokens | 与 Dongre 可比，审稿人可直接对照 |
110	| 附录评估 | GAR-ours | system prompt + first user query | last token per assistant turn | 两种定义一致性 |
111	
112	**D024 精确化（d048 N=50 更新）**: GAR-ours TF=0.50, AR=0.064（Qwen 7.8× gap）; Llama AR=0.018（27× median gap）。GAR-Dongre 在两种分布上均低，无 gap。8×–27× gap 是 text distribution shift 现象，特定于 summary-position attention (GAR-ours)。
113	
114	---
115	
116	## 9. 论文结构草案
117	
118	1. **Abstract** (150-250 words): GAR 衰减问题 → residual probe 证据支撑 gating 动机 → ThreadGate 方法 → 训练成功但推理失败 → 三个失败机制 → 对 attention steering 方法的启示
119	2. **Introduction** (5 段): 多轮对话退化现象 → Dongre 诊断 + residual stream 持续性 → 自然推论: residual gating 应能恢复 → ThreadGate 实验结果: 训练有效推理失败 → 三个失败机制 + 贡献列表
120	3. **Related Work**: multi-turn degradation / residual gating & adaptive depth / attention steering & intervention
121	4. **Background**: GAR 定义 (cite Dongre) + residual stream persistence 证据
122	5. **Method**: ThreadGate 架构（⚠️ 非简单标量 gate：per-layer 2 层 MLP + turn embedding，接收 hidden_state + turn_distance/turn_index，输出 per-token per-layer sigmoid gate 值。公式 g_l = σ(W_2·ReLU(W_1·[proj(x_l); emb(t_d, t_i)] + b_1) + b_2)。Uniform Gate = 同架构但用 constant_vector 替代 turn embedding，仍然 per-layer content-dependent）+ MSE+gate_div loss + v1-v7 loss 设计演化 + 训练设置
123	6. **Experiments**: §5.1 Setup → §5.2 Main Results (五路消融 TG/+PCGrad/UG/LoRA-only/Base) → §5.3 Inference-Time Steering (β-steering, GAR 0.727) → **§5.4 Scheduled Sampling (gap 8×→~1.3×, 独立 Results 小节)**
124	7. **Analysis**: §6.1 Gate Turn Conditioning → §6.2 PCGrad Gradient Conflict Exclusion → §6.3 Distribution Shift Analysis → §6.4 Mechanism Specificity → §6.5 Cross-Model Replication
125	8. **Discussion**: exposure bias 对 auxiliary attention loss 的具体影响机制 + Why NTP self-recovers but GAR does not + Downstream effects (instruction retention)。**SS 已移至 §5.4**
126	9. **Conclusion**: 完整弧总结——发现 (8×–27× collapse) + 定位 (PCGrad modus tollens) + 修复 (steering + SS)
127	
128	### 贡献列表（按 novelty 排序）
129	
130	1. **Exposure bias 对 auxiliary attention loss 泛化性的首个实证刻画**: 实证展示 teacher-forcing distribution shift 如何摧毁 lightweight residual gating 的 auxiliary attention loss 泛化性（8×–27× training-inference GAR-ours gap），为 teacher-forcing 下的 attention steering 方法提供具体风险标杆
131	2. **NTP-GAR 梯度竞争的逐层量化**: NTP loss 在 gate 参数上的梯度与 GAR loss 冲突，导致 gates 学到反向 turn conditioning（27/28 层 gate 在晚期 turn 趋向 identity）
132	3. **首个 principled residual gating 干预 + 系统性消融**: 基于 Dongre 的 residual stream persistence 证据设计 ThreadGate，v1-v7 覆盖 4 种核心 loss (cumulative v1-v2, maximize v3-v5, smooth_saturation v6, mse_target v7) + 四路消融隔离贡献，为后续研究提供 negative baseline
133	4. **跨模型验证** (Qwen-2.5-7B + Llama-3.1-8B) 确认失败机制的普遍性
134	5. **Scheduled sampling 作为初步修复**: 首次证明 time-scheduled sampling（linearly mixing model-generated context，原为 RNN 设计）可迁移到 auxiliary attention objectives in multi-turn transformers，将 TF–AR gap 从 8× 压缩到 ~1.3×（3-seed: AR GAR 0.401±0.047, PPL 1.441±0.001），无 PPL 代价。配合 inference-time β-steering（GAR 0.064→0.727），构成完整的 mitigation toolkit。**注意**：Dou & Gales (2022) "Parallel Attention Forcing" 使用 data-dependent attention KL 选择训练模式（单轮 NMT），与我们的 time-scheduled + multi-turn + auxiliary attention 目标有三重区分。必须引用并区分。SS 与 steering 是替代关系而非互补——高 β 时两者趋同（β=5: SS 0.717 ≈ TG 0.727），Discussion 需明确说明
135	
136	---
137	
138	## 10. 竞争力评估
139	
140	### Dream Review 结果 (2026-05-19, dream_20260519T135115)
141	- **Best case**: 3.0 (Weak Reject / Findings-level)。主要扣分: claim 过度泛化 (W1), 引用不足 (W6), 单 seed (W7)。
142	- **Median case**: 3.0 (Weak Reject)。同上 + distribution shift insight incremental (W5)。
143	- **Worst case**: 未完成 review（crash），但 imagined experiments 显示最坏情况下 Llama-3 不复现 dramatic pattern。
144	
145	### 修正后预期（2026-05-23 Framing 升级后）
146	- **当前状态**: SS 升级为独立 Results + 5th contribution + 56 references + Llama 跨模型 + 3-seed 统计中 + bootstrap CI。
147	- **Best case**: 3.5 (Borderline Conference / Accept)。完整 "发现→定位→修复" 弧匹配 gromov/sun/xiao 模式。
148	- **Median case**: 3.0-3.5 (Findings-Conference borderline)。若 SS+steering 联合 eval 接近 TF parity → 推向 3.5。
149	- **冲 Main 条件**: SS+steering 联合接近 parity + Llama SS 跨模型复现 + KL divergence 机制证据 + 3-seed 正式统计。
150	- **核心差异化**: 不是 "gating 失败了"（弱），而是 "exposure bias 在 auxiliary attention loss 上的首个定量测量 + PCGrad 因果排除 + SS/steering 初步修复"（强）。
151	- **关键风险**: W5（exposure bias 已知）需要精确定位增量；SS+steering 联合是否真能接近 parity 待验证。
152	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8416a7ef-17cf-40f7-bcfb-a980ebc3f927",
  "isSidechain": false,
  "promptId": "4e9b6b3b-bc11-45d7-a0d2-4aaa1c0c9272",
  "type": "user",
  "uuid": "2670496a-f53b-4794-a37f-2f50dbf2752f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst/paper_framing.md",
      "content": "# Paper Framing: Mechanistic Analysis of Training-Inference Distribution Shift in Attention Steering\n\n> 定位: **Mechanistic insight paper**（不是简单 negative result）。核心卖点是 teacher-forcing→generation 分布偏移如何摧毁 lightweight residual gating 的 auxiliary attention loss 泛化性（8×–27× gap，Qwen 7.8× / Llama 27× median）。这个 insight 为 auxiliary attention loss 在 teacher-forcing 下的 exposure bias 脆弱性提供首个实证刻画。**SS 初步修复: AR GAR 0.401±0.047（3-seed mean±std），TF/AR gap ~1.3×（range 1.15–1.45×）。**\n> Novelty 排序: (1) exposure bias 对 auxiliary attention loss 泛化性的首个实证刻画 (8×–27× gap) > (2) PCGrad 因果排除梯度方向冲突 + \"观察→假设→排除→指向真因\" 完整因果链 (D028) > (3) SS 迁移到 multi-turn transformer attention objectives (AR GAR 0.401±0.047, 3-seed) > (4) principled intervention + systematic ablation 的 negative result\n> **⚠️ Dream review D024: \"Cannot\" overclaims, novelty \"first measurement\" 过高, 缺 gradient surgery baseline (PCGrad). 标题改 \"Fails to\", novelty 降级 \"first empirical characterization\"**\n> 目标会议: EMNLP 2026, ARR August cycle, deadline 2026-08-03 (~10.5 weeks)\n> 最后更新: 2026-05-24 (3-seed SS 数据完成: AR GAR 0.401±0.047, gap ~1.3× range 1.15–1.45×; β=3/5 跨 seed 极稳定 std<0.01; s42 是 β=0 outlier)\n> **⚠️ Llama-3 跨模型验证 = MUST-HAVE**（不含 → Findings 3.0 紧绷；含 → 3.0-3.5）\n> **Framing 升级目标 3.5**: 对标 gromov2024/sun2025/xiao2024 \"发现→定位→修复\" 模式。SS AR GAR 0.401±0.047 (3-seed, vs base 0.019) 是真正的 positive result，不应埋在 Discussion。\n\n---\n\n## 1. Title Candidates\n\n- **T0 (当前)**: Exposure Bias Selectively Destroys Auxiliary Attention Losses in Multi-Turn Dialogue: A Diagnostic Analysis of Per-Layer Residual Gating\n- **T1**: Exposure Bias Selectively Destroys Auxiliary Attention Losses in Multi-Turn Dialogue （去掉副标题，更简洁有力）\n- **T2**: From Collapse to Recovery: Diagnosing and Mitigating Exposure Bias in Multi-Turn Attention Objectives （强调完整弧：发现+定位+修复）\n- **T3**: The Exposure Bias Barrier: Why Auxiliary Attention Losses Fail at Multi-Turn Inference （barrier metaphor，聚焦机制）\n\n推荐 T1 或 T2。T1 保留当前论文最有记忆点的短语 \"selectively destroys\"，去掉冗长副标题。T2 强调 \"发现→定位→修复\" 完整弧，与 gromov2024/xiao2024 对标。T0 过长（20 词），审稿人可能记不住。T3 偏负面。\n\n---\n\n## 2. Story Arc\n\nMulti-turn dialogue performance in LLMs degrades as conversations grow longer. Dongre et al. (2026) quantified this through the Goal Accessibility Ratio (GAR), showing 27-48% drops over 50 turns, while their residual stream probes reveal that goal information persists (AUC up to 0.98) even as the attention channel closes. This creates a natural hypothesis: if the information is in the residual stream but attention fails to access it, a learnable gate on the residual connection should recover it. We implement this hypothesis as ThreadGate, a per-layer gating module trained with joint NTP and GAR objectives. ThreadGate successfully optimizes GAR during training (0.02 to 0.48), and this improvement transfers perfectly when evaluated on same-distribution text at inference (GAR-ours = 0.49). However, on model-generated text, GAR-ours collapses to 0.064 (Qwen N=50, 7.8× gap) or 0.018 (Llama N=20, 27× gap), driven by text distribution shift. Our central finding is that attention patterns learned under teacher-forced contexts (gold text) do not generalize to autoregressive generation contexts (model-generated text), the classic exposure bias phenomenon. This distribution shift is structural, independent of loss design or gating architecture. We further identify two coupled mechanisms that amplify the shift: (1) NTP loss dominates gate gradients, causing gates to learn reverse turn conditioning (suppressing at early turns where GAR is high, becoming passive at late turns where intervention is needed); (2) at inference time, gates attenuate residual updates by only 2-7%, far too weak to shift attention patterns. Four-way ablation (ThreadGate vs. Uniform Gate vs. LoRA-only vs. Base) confirms gating provides zero incremental contribution. Notably, this 8×–27× gap is specific to GAR-ours (last-token attention to goals); GAR-Dongre (all-token attention) shows uniformly low values regardless of text distribution, revealing that exposure bias selectively disrupts summary-position attention patterns. Combined with Dongre et al.'s independent failure of goal re-injection, our results provide the first empirical characterization of how text distribution shift (exposure bias) selectively destroys attention patterns learned through auxiliary losses, and identify the specific mechanisms through which this vulnerability manifests. Crucially, we show that scheduled sampling—originally designed for RNN sequence models—transfers to multi-turn transformer attention objectives, compressing the TF–AR gap from 8× to ~1.3× with no perplexity cost (3-seed: AR GAR 0.401±0.047, PPL 1.441±0.001). Inference-time β-steering independently recovers GAR from 0.064 to 0.727. These mitigation results upgrade the paper from pure negative result to a complete \"discover → diagnose → initial remedy\" arc, matching the narrative pattern of high-impact diagnostic papers (gromov2024, sun2025, xiao2024).\n\n---\n\n## 3. Core Claims\n\n| # | Claim | 支撑 | 状态 |\n|---|-------|------|------|\n| C1 | GAR 衰减是真实且严重的结构性现象: Qwen-2.5-7B raw GAR 下降 70.8%, normalized GAR 下降 ~21% | Phase 1 GAR 诊断 | ✅ 已验证 |\n| C2 | Residual gating 训练时在 same-distribution text 上有效优化 GAR-ours (TF GAR=0.50)，但在 model-generated text 上完全失败 (AR GAR=0.064, 7.8× gap on Qwen N=50; 27× median on Llama N=20)。GAR-Dongre 在两种分布上均低，无 gap——说明分布偏移选择性影响 summary-position attention pattern。 | v7 训练 + d048 N=50 eval + Llama eval + Reviewer 独立验证 | ✅ 已验证（N=50 precision） |\n| C3 | 失败机制的因果分析: (1) Distribution shift 是主因（D028 PCGrad 因果排除梯度方向冲突）; (2) NTP 幅度主导 gate 学习 → NF1 反向 turn conditioning; (3) NF3 gate 干预强度不足 2-7%。PCGrad ablation: 消除方向冲突后 cos_sim 围绕 0 震荡(range -0.151 to +0.091)，但 L_GAR 坍塌轨迹不变且无延迟 → 方向冲突非因果因素。**推理端确认（IID same-protocol）**: v9 GAR-ours=0.0151 vs v7=0.0157 (差<0.1pp), **v9 IID PPL=2.780 vs v7=2.784 (差0.004，无改善)**——PCGrad 消除方向冲突后所有可观测指标均 ≈ v7，方向冲突因 NTP 幅度主导而完全 inconsequential | D014 gate-profile + 梯度冲突量化 + **D028 PCGrad 因果排除** + v9 推理 eval + **M017 PPL 修正** | ✅ **End-to-end 完成**: 训练端 + 推理端均确认梯度方向冲突对 GAR 和 PPL 均无因果影响 |\n| C4 | Gating 无增量贡献: 四路消融 LoRA-only ≈ TG ≈ UG（GAR + PPL 双指标）。IID: GAR 差异<0.6pp, PPL 均 ~2.78。**Model-gen (D033): v9 PCGrad=0.0151, UG=0.0149, LoRA-only=0.0245 均接近 baseline 0.0122——8×–27× gap 在所有训练变体上普遍存在，排除 gating mechanism / turn-conditioning / gradient conflict 作为因果因素** | D021 四路 eval + D033 model-gen eval | ✅ **双重验证**: IID (D021) + model-gen (D033)。model-gen regime 进一步确认 gating 零增量且 GAR collapse 是训练-推理分布偏移的普遍现象 |\n| C5 | 跨模型验证: Llama-3.1-8B 上复现同样的失败模式 | Phase 1 ✅ (GAR decay 80.2%, D042), Phase 2 ✅ (TG gap 27× median, gating zero-increment TG≈LO, LoRA-only N=20 eval) | ✅ Fully confirmed |\n\n---\n\n## 4. Negative Findings (NF)\n\n| # | Finding | 证据 | 叙事角色 |\n|---|---------|------|----------|\n| NF1 | Gate turn conditioning 方向反转: 27/28 层 gate diff (turn1-turn21) < 0，早期 turn 强抑制，晚期 turn passive | D014 eval gate-profile | 解释 why gating fails: NTP 梯度推 gate→1.0，晚期 turn 推力最强 |\n| NF2 | 8×–27× text distribution shift gap (GAR-ours): TF GAR=0.50 vs AR GAR=0.064 (Qwen N=50, 7.8× gap); Llama AR GAR=0.018 (27× median gap, N=20)。Same-distribution 泛化成功（TF eval GAR=0.50），cross-distribution 泛化失败。**D033 跨变体确认**: v9 PCGrad, UG, LoRA-only model-gen GAR 均接近 baseline——gap 独立于训练策略，是 exposure bias 的普遍表现。GAR-Dongre 在两种分布上均低，无 gap——分布偏移选择性影响 summary-position (last token) attention pattern | d048 N=50 eval + Llama eval + D033 cross-variant | 核心 negative finding。精确定位为 TEXT DISTRIBUTION SHIFT（exposure bias）。 |\n| NF3 | 推理时 gate attenuation 仅 2-7% (gate_mean=0.93-0.98)，近乎 identity | D014 gate dynamic range 数据 | 解释 why 推理时 GAR 不改善: 干预强度不足 |\n| NF4 | Eval baseline confound (Phase1 base vs Phase2 LoRA 文本不同) | P0 代码分析 | 已修正 → standard_conversations.json 统一 eval |\n\n---\n\n## 5. Key Selling Points\n\n**SP1 (核心卖点): Exposure bias 对 auxiliary attention loss 泛化性的首个实证刻画。** 8×–27× training-inference GAR-ours gap（Qwen 7.8×, Llama 27× median）提供了 teacher-forcing distribution shift 如何摧毁 auxiliary attention loss 泛化性的实证证据。训练时模型在 gold context 上优化 attention pattern，推理时在自身生成的 context 上条件化——两者分布不同导致 attention pattern 不迁移。虽然 exposure bias 概念本身已知 (Bengio et al. 2015)，且 sequence generation 中有量化先例 (Ranzato et al. 2016, Wiseman & Rush 2016)，但此前无人刻画其对 auxiliary attention loss 的具体影响。我们的 8×–27× gap 测量展示了这种脆弱性在 attention steering 场景下的严重程度。**注意：(1) claim scope 严格限于 lightweight residual gating + GAR auxiliary loss 的实测范围，不泛化到所有 attention steering 方法。(2) gap 在 GAR-ours（last token only, summary-position attention）上测得（TF 0.50 vs AR 0.064 Qwen / 0.018 Llama）；GAR-Dongre（all response tokens）在两种分布上均低，无 gap——表明 exposure bias 选择性影响 summary-position attention pattern，这一差异本身有分析价值。**\n\n**SP2: NTP-GAR 梯度动力学 + PCGrad 因果排除（gradient conflict is inconsequential）。** 观察到 67-79% 的层 NTP-GAR 梯度方向冲突（cos_sim<0）+ NTP 幅度 3-15x 压制 GAR（mag_ratio 7.5→14.7x）。**PCGrad 消融（D028）因果排除方向冲突**：投影后 cos_sim 围绕 0 震荡（range -0.151 to +0.091），L_GAR 坍塌轨迹不变。**推理端确认（IID same-protocol）**: v9 IID PPL = 2.780 vs v7 = 2.784（差 0.004，无改善）; v9 GAR-ours = 0.0151 vs v7 = 0.0157（差 <0.1pp）——**PCGrad 消除方向冲突后所有可观测指标均无变化**（GAR、PPL、NTP 均 ≈ v7）。方向冲突虽然可测量存在于 v7 中，但对训练和推理结果无任何因果影响——7.5–14.7× NTP 幅度主导使方向冲突完全无关紧要（inconsequential）。**⚠️ M017: 此前 \"PPL -46%\" 和 \"selective dissociation\" 论述为跨协议对比伪影（model-gen PPL 1.50 vs IID PPL 2.78），已撤回。** **精确 claim scope**: gradient direction conflict is **neither necessary nor sufficient** for the 8×–27× GAR gap; exposure bias alone is sufficient。NOT necessary: 移除冲突→gap仍在; NOT sufficient: v7有冲突但L_GAR训练时收敛; Exposure bias is sufficient: 训练≠推理分布→GAR泛化失败。**Gate 行为额外 insight**: v9 gate dynamic range 比 v7 更宽 (L15 range 0.33 vs v7 0.21)——PCGrad 给 gate 更大自由度，但 gate 用该自由度更激进地优化 NTP 而非 GAR，说明优化景观固有偏好语言建模目标。\n\n**SP3: Principled 设计动机 + 系统性探索。** Dongre 发现 goal info 在 residual stream 持续存在 (probe AUC=0.98)，residual gating 是最直接的架构响应。v1-v7 覆盖 4 种核心 loss 设计 across 7 training configurations，MSE+gate_div 是唯一训练收敛方案。四路消融严格隔离贡献: TG (learned gate + GAR loss) / UG (uniform gate + GAR loss) / LoRA-only (gate=1.0 fixed + GAR loss, 无 gating 机制) / Base。注意：三个 fine-tuned 变体均使用 GAR loss，消融测试的是 gating 机制的增量贡献，而非 GAR loss 本身的效果。\n\n**SP4: Convergent evidence with Dongre。** Dongre diagnosed the problem; we attempted the first systematic cure and uncovered fundamental limitations。两种独立干预路线（goal re-injection + residual gating）均失败，共同指向 NTP 优化压力下 attention steering 的根本困难。\n\n**SP5: 三阶段训练动力学。** v7 展现 plateau → phase transition → convergence 的清晰训练动力学，证明 MSE 双向 loss 设计本身是 sound 的，问题在泛化而非训练。\n\n---\n\n## 6. Anticipated Reviewer Concerns\n\n| # | 严重度 | 预期质疑 | 回应策略 |\n|---|--------|----------|----------|\n| W1 | **致命** | 单模型验证不够 | Llama-3.1-8B 跨模型验证是 **MUST-HAVE**。Qwen 完整消融 + Llama 复现。不含 Llama → Findings 3.0 紧绷，含 → 3.0-3.5。 |\n| W2 | **严重** | \"你只是没调对参数\" | D018 的 teacher-forcing 分布偏移是结构性的，与 loss 设计无关。v1-v7 已覆盖 4 种核心 loss (cumulative v1-v2, maximize v3-v5, smooth_saturation v6, mse_target v7)，MSE+gate_div 是唯一训练收敛方案。四路消融隔离 turn conditioning (TG vs UG) 和 gating 本身 (TG vs LoRA-only)，消除超参解释。 |\n| W3 | **严重** | GAR 作为唯一代理指标 | 考虑加 1 个简单下游任务 sanity check（如 system prompt instruction following accuracy）。PPL 对比已加入四路 eval（TG PPL > LoRA-only → gates 有害的额外证据）。 |\n| W4 | **中等** | 无建设性贡献 | Discussion 需要 constructive future directions section: (1) inference-time attention intervention 绕过训练泛化问题; (2) decoupled goal-processing pathway; (3) GAR-aware decoding 而非 GAR-aware training; (4) exposure bias mitigation 技术应用到 auxiliary attention loss。 |\n| W5 | **中等** | Teacher-forcing insight 不新（exposure bias 文献已知） | 我们的增量: 定量展示 distribution shift 如何具体破坏 auxiliary attention loss（8×–27× 断层），现有 exposure bias 文献无此分析。Exposure bias 讨论集中在 generation quality degradation，未涉及 auxiliary attention loss 的泛化失败。 |\n| R1 | 中等 | Novelty of negative result | 核心增量不是 negative result 本身，而是 distribution shift insight（SP1）+ 梯度竞争量化（SP2）+ failure mode taxonomy。 |\n| R2 | 中等 | 与 Dongre et al. 的关系 | 不说 \"we extend Dongre\"，而是 \"Dongre diagnosed; we attempted the first systematic cure and uncovered fundamental limitations\"。核心叙事是 mechanism discovery，非 follow-up work。 |\n| W6 | **严重** | 引用不足（Dream review: 11篇远不够）| 目标 25-30 篇。必须覆盖: attention sinks (Xiao et al. 2024), Found-in-the-Middle (Ko et al. 2024), gated attention (Qiu et al. 2025), transformer circuits (Elhage et al. 2021), FlexiDepth (Luo et al. 2025), multi-turn eval (MT-Bench-101, MultiChallenge), exposure bias mitigation (Professor Forcing, SEARNN) 等。Paper Agent 写作时负责扩充。|\n| W7 | **严重** | 单 seed 无方差估计 | 所有实验 seed=42，TG-LoRA 差异 ±0.001 在噪声层。回应: held-out eval 50 conversations 提供 paired bootstrap CI，若 CI 包含 0 则统计支持 \"zero benefit\"。必要时追加 2 个 seed 的训练。|\n| W8 | **中等** | 缺 exposure-bias mitigation 实验 | 测试 scheduled sampling / model-generated context 训练能否缩小 8×–27× gap。加入 experiment_plan (P1)。如果实验表明 mitigation 确实缩小 gap，论文从 \"negative result\" 升级为 \"negative result + constructive direction\"。|\n| R1 | 中等 | Novelty of negative result | 核心增量不是 negative result 本身，而是 exposure bias 的定量测量（SP1）+ 梯度竞争量化（SP2）+ failure mode taxonomy。 |\n| R2 | 中等 | 与 Dongre et al. 的关系 | 不说 \"we extend Dongre\"，而是 \"Dongre diagnosed; we attempted the first systematic cure and uncovered fundamental limitations\"。核心叙事是 mechanism discovery，非 follow-up work。 |\n| R3 | 低 | 8×–27× gap 是否可能是实现 bug | D015 代码逐行对比 + D017 controlled experiments 确认非 bug。Base model 在 ultrachat 和 eval data 上 GAR 均 ~0.01，排除数据分布解释。 |\n| R4 | ~~低~~ **已核实** | Code-paper 公式语义相反 | **已确认不一致（plan_017 DONE）**。代码正确实现 ReZero-style: `x_{l+1} = x_l + g_l · f_l(x_l)`（gate 缩放子层输出，g→0=层 no-op）。Dream paper.tex 错误写为 `x_{l+1} = g_l · x_l + f_l(x_l)`（gate 缩放残差流，g→0=破坏 skip connection）。**实验数据不受影响**（所有实验用同一份代码）。**Paper Agent 写作时必须**: (1) Method section 用正确公式 `x + g·f(x)`; (2) 机制叙事修正: g→0 = 子层输出被抑制（层变 no-op），NTP 推 g→1 是为保留层计算能力，不是保留 skip connection; (3) NF3 \"gate attenuation 2-7%\" 指子层贡献缩放，表述正确但需明确。|\n\n---\n\n## 7. Dongre et al. 关系定位\n\n| 维度 | Dongre et al. | 本文 |\n|------|---------------|------|\n| 核心问题 | \"发生了什么\" + \"为什么\" | \"怎么干预\" + \"为什么干预失败\" |\n| GAR 衰减 | 定义 GAR，12 模型量化衰减 | 独立确认 (Qwen 70.8% raw, 21% normalized) |\n| 机制分析 | residual probe AUC=0.98 (goal info 持续存在) | NTP-GAR 梯度冲突 + 8×–27× 泛化 gap + turn conditioning 反转 |\n| 干预尝试 | goal re-injection (Appendix H, 失败) | ThreadGate residual gating (失败) + UG/LoRA-only 消融 |\n| 结论 | attention 通道关闭但 residual stream 保留 goal info | 即使在 residual stream 上施加 principled gating，NTP 梯度压制使 gate 无法学到正确的 turn-selective 干预 |\n\n**定位语**: Dongre diagnosed the problem; we attempted the first systematic cure and uncovered fundamental limitations. 核心叙事是 mechanism discovery（distribution shift + gradient competition），不是 Dongre 的 follow-up。\n\n共同推论: 两种独立干预路线均失败 → lightweight residual gating with auxiliary attention loss 在 teacher-forcing 下面临严重泛化障碍（8×–27× gap）→ 需要 inference-time 干预或 exposure bias mitigation（SS 已验证可将 gap 压缩到 ~1.3×（3-seed: AR GAR 0.401±0.047））。（注意：scope 限于 lightweight gating，不泛化到所有 attention steering 方法。）\n\n---\n\n## 8. GAR 定义策略\n\n| 用途 | 定义 | Goal tokens | Response tokens | 理由 |\n|------|------|------------|----------------|------|\n| 训练信号 | GAR-ours | system prompt + first user query | last token per assistant turn | 更丰富的 goal 信号; last token 作为 summary position 更稳定 |\n| 主表评估 | GAR-Dongre | system prompt task tokens only | all response tokens | 与 Dongre 可比，审稿人可直接对照 |\n| 附录评估 | GAR-ours | system prompt + first user query | last token per assistant turn | 两种定义一致性 |\n\n**D024 精确化（d048 N=50 更新）**: GAR-ours TF=0.50, AR=0.064（Qwen 7.8× gap）; Llama AR=0.018（27× median gap）。GAR-Dongre 在两种分布上均低，无 gap。8×–27× gap 是 text distribution shift 现象，特定于 summary-position attention (GAR-ours)。\n\n---\n\n## 9. 论文结构草案\n\n1. **Abstract** (150-250 words): GAR 衰减问题 → residual probe 证据支撑 gating 动机 → ThreadGate 方法 → 训练成功但推理失败 → 三个失败机制 → 对 attention steering 方法的启示\n2. **Introduction** (5 段): 多轮对话退化现象 → Dongre 诊断 + residual stream 持续性 → 自然推论: residual gating 应能恢复 → ThreadGate 实验结果: 训练有效推理失败 → 三个失败机制 + 贡献列表\n3. **Related Work**: multi-turn degradation / residual gating & adaptive depth / attention steering & intervention\n4. **Background**: GAR 定义 (cite Dongre) + residual stream persistence 证据\n5. **Method**: ThreadGate 架构（⚠️ 非简单标量 gate：per-layer 2 层 MLP + turn embedding，接收 hidden_state + turn_distance/turn_index，输出 per-token per-layer sigmoid gate 值。公式 g_l = σ(W_2·ReLU(W_1·[proj(x_l); emb(t_d, t_i)] + b_1) + b_2)。Uniform Gate = 同架构但用 constant_vector 替代 turn embedding，仍然 per-layer content-dependent）+ MSE+gate_div loss + v1-v7 loss 设计演化 + 训练设置\n6. **Experiments**: §5.1 Setup → §5.2 Main Results (五路消融 TG/+PCGrad/UG/LoRA-only/Base) → §5.3 Inference-Time Steering (β-steering, GAR 0.727) → **§5.4 Scheduled Sampling (gap 8×→~1.3×, 独立 Results 小节)**\n7. **Analysis**: §6.1 Gate Turn Conditioning → §6.2 PCGrad Gradient Conflict Exclusion → §6.3 Distribution Shift Analysis → §6.4 Mechanism Specificity → §6.5 Cross-Model Replication\n8. **Discussion**: exposure bias 对 auxiliary attention loss 的具体影响机制 + Why NTP self-recovers but GAR does not + Downstream effects (instruction retention)。**SS 已移至 §5.4**\n9. **Conclusion**: 完整弧总结——发现 (8×–27× collapse) + 定位 (PCGrad modus tollens) + 修复 (steering + SS)\n\n### 贡献列表（按 novelty 排序）\n\n1. **Exposure bias 对 auxiliary attention loss 泛化性的首个实证刻画**: 实证展示 teacher-forcing distribution shift 如何摧毁 lightweight residual gating 的 auxiliary attention loss 泛化性（8×–27× training-inference GAR-ours gap），为 teacher-forcing 下的 attention steering 方法提供具体风险标杆\n2. **NTP-GAR 梯度竞争的逐层量化**: NTP loss 在 gate 参数上的梯度与 GAR loss 冲突，导致 gates 学到反向 turn conditioning（27/28 层 gate 在晚期 turn 趋向 identity）\n3. **首个 principled residual gating 干预 + 系统性消融**: 基于 Dongre 的 residual stream persistence 证据设计 ThreadGate，v1-v7 覆盖 4 种核心 loss (cumulative v1-v2, maximize v3-v5, smooth_saturation v6, mse_target v7) + 四路消融隔离贡献，为后续研究提供 negative baseline\n4. **跨模型验证** (Qwen-2.5-7B + Llama-3.1-8B) 确认失败机制的普遍性\n5. **Scheduled sampling 作为初步修复**: 首次证明 time-scheduled sampling（linearly mixing model-generated context，原为 RNN 设计）可迁移到 auxiliary attention objectives in multi-turn transformers，将 TF–AR gap 从 8× 压缩到 ~1.3×（3-seed: AR GAR 0.401±0.047, PPL 1.441±0.001），无 PPL 代价。配合 inference-time β-steering（GAR 0.064→0.727），构成完整的 mitigation toolkit。**注意**：Dou & Gales (2022) \"Parallel Attention Forcing\" 使用 data-dependent attention KL 选择训练模式（单轮 NMT），与我们的 time-scheduled + multi-turn + auxiliary attention 目标有三重区分。必须引用并区分。SS 与 steering 是替代关系而非互补——高 β 时两者趋同（β=5: SS 0.717 ≈ TG 0.727），Discussion 需明确说明\n\n---\n\n## 10. 竞争力评估\n\n### Dream Review 结果 (2026-05-19, dream_20260519T135115)\n- **Best case**: 3.0 (Weak Reject / Findings-level)。主要扣分: claim 过度泛化 (W1), 引用不足 (W6), 单 seed (W7)。\n- **Median case**: 3.0 (Weak Reject)。同上 + distribution shift insight incremental (W5)。\n- **Worst case**: 未完成 review（crash），但 imagined experiments 显示最坏情况下 Llama-3 不复现 dramatic pattern。\n\n### 修正后预期（2026-05-23 Framing 升级后）\n- **当前状态**: SS 升级为独立 Results + 5th contribution + 56 references + Llama 跨模型 + 3-seed 统计中 + bootstrap CI。\n- **Best case**: 3.5 (Borderline Conference / Accept)。完整 \"发现→定位→修复\" 弧匹配 gromov/sun/xiao 模式。\n- **Median case**: 3.0-3.5 (Findings-Conference borderline)。若 SS+steering 联合 eval 接近 TF parity → 推向 3.5。\n- **冲 Main 条件**: SS+steering 联合接近 parity + Llama SS 跨模型复现 + KL divergence 机制证据 + 3-seed 正式统计。\n- **核心差异化**: 不是 \"gating 失败了\"（弱），而是 \"exposure bias 在 auxiliary attention loss 上的首个定量测量 + PCGrad 因果排除 + SS/steering 初步修复\"（强）。\n- **关键风险**: W5（exposure bias 已知）需要精确定位增量；SS+steering 联合是否真能接近 parity 待验证。\n",
      "numLines": 152,
      "startLine": 1,
      "totalLines": 152
    }
  },
  "sourceToolAssistantUUID": "8416a7ef-17cf-40f7-bcfb-a980ebc3f927",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260524T081135 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_ga…",
  "leafUuid": "2670496a-f53b-4794-a37f-2f50dbf2752f",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier diagnostic paper for dream_20260524T081135",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1"
}
```

---

### Assistant

_source line 15 · 2026-05-24T08:58:11.530Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the experiment data and paper framing. Let me now read the paper-writing-norms skill and the distilled-writing skill to get guidance on writing conventions.

Let me also check what LaTeX packages are available by looking at the existing paper.tex or any other LaTeX files in the project.

Actually, the task is clear: I need to write a "worst tier" dream paper. The narrative guidance tells me to:

1. Abandon the 'discover→diagnose→remedy' arc
2. Reframe as pure mechanistic diagnostic paper
3. Title: 'Why Auxiliary Attention Losses Fail Under Exposure Bias: A Multi-Model Diagnostic Study'


4. Move scheduled sampling from Results to Discussion as an attempted mitigation
5. Build the paper around a failure mode taxonomy with three distinct failure patterns
6. Emphasize the PCGrad analysis as a key diagnostic tool
7. Include evidence of convergent failures across models
8. Aim for EMNLP Findings scope at 2.5-3.0 pages

Now I'm structuring the paper to systematically cover all six experiments: the gradient conflict analysis on Llama, the expanded evaluation across 200 conversations, the sensitivity sweep over the auxiliary loss weight, the attention divergence measurements between training and autoregressive modes, the scheduled sampling results on Llama-3.1-8B, and the final scheduled sampling experiment.

I also need to incorporate the additional validation experiments: seed robustness on Qwen, the alternative GAR formulation, the fourth scheduled sampling seed, and the long conversation evaluation beyond 10 turns. Let me set up the directory structure and start writing the full paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2670496a-f53b-4794-a37f-2f50dbf2752f",
  "isSidechain": false,
  "requestId": "req_011CbM7kJvE5nAgv3AeMnFsp",
  "type": "assistant",
  "uuid": "170346c5-b308-482f-89b7-2d9edf5f8e1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UGqCgmGoCxjbbZ474GTqMG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23984,
      "cache_read_input_tokens": 25351,
      "output_tokens": 557,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23984,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 557,
          "cache_read_input_tokens": 25351,
          "cache_creation_input_tokens": 23984,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23984
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

_source line 16 · 2026-05-24T08:58:11.532Z_

Let me check if the output directory exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "170346c5-b308-482f-89b7-2d9edf5f8e1c",
  "isSidechain": false,
  "requestId": "req_011CbM7kJvE5nAgv3AeMnFsp",
  "type": "assistant",
  "uuid": "078d0d34-582c-4990-89be-62eabb627c07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UGqCgmGoCxjbbZ474GTqMG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23984,
      "cache_read_input_tokens": 25351,
      "output_tokens": 557,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23984,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 557,
          "cache_read_input_tokens": 25351,
          "cache_creation_input_tokens": 23984,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23984
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

_source line 17 · 2026-05-24T08:58:13.260Z_

<details open><summary>🔧 Tool call — Bash · `toolu_019ocC6USc9bFgXSJnNUKHtb`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
  "description": "Check if output directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "078d0d34-582c-4990-89be-62eabb627c07",
  "isSidechain": false,
  "requestId": "req_011CbM7kJvE5nAgv3AeMnFsp",
  "type": "assistant",
  "uuid": "4e2b605a-5eac-4652-9268-98a74993ee0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UGqCgmGoCxjbbZ474GTqMG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23984,
      "cache_read_input_tokens": 25351,
      "output_tokens": 557,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23984,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 557,
          "cache_read_input_tokens": 25351,
          "cache_creation_input_tokens": 23984,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23984
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

_source line 18 · 2026-05-24T08:58:13.431Z_

<details><summary>↩ Tool result · `toolu_019ocC6USc9bFgXSJnNUKHtb`</summary>

```text
total 104
drwxr-xr-x 2 ubuntu ubuntu  4096 May 24 08:57 .
drwxr-xr-x 6 ubuntu ubuntu  4096 May 24 08:57 ..
-rw-r--r-- 1 ubuntu ubuntu 33833 May 24 08:57 experiment_data.json
-rw-r--r-- 1 ubuntu ubuntu 32170 May 24 08:57 imagined_experiments.yaml
-rw-r--r-- 1 ubuntu ubuntu 24904 May 24 08:57 paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e2b605a-5eac-4652-9268-98a74993ee0c",
  "isSidechain": false,
  "promptId": "4e9b6b3b-bc11-45d7-a0d2-4aaa1c0c9272",
  "type": "user",
  "uuid": "49f4134d-7aac-43b8-9e98-470aea5674df",
  "toolUseResult": {
    "stdout": "total 104\ndrwxr-xr-x 2 ubuntu ubuntu  4096 May 24 08:57 .\ndrwxr-xr-x 6 ubuntu ubuntu  4096 May 24 08:57 ..\n-rw-r--r-- 1 ubuntu ubuntu 33833 May 24 08:57 experiment_data.json\n-rw-r--r-- 1 ubuntu ubuntu 32170 May 24 08:57 imagined_experiments.yaml\n-rw-r--r-- 1 ubuntu ubuntu 24904 May 24 08:57 paper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "4e2b605a-5eac-4652-9268-98a74993ee0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-24T08:58:51.735Z_

<details><summary>Logged reasoning block</summary>

```text
Good, directory exists. Let me write the full LaTeX paper. I need to be careful to:

1. Cover ALL 9 experiments from experiment_data.json
2. Frame as a pure mechanistic diagnostic paper (worst tier narrative)
3. Title: 'Why Auxiliary Attention Losses Fail Under Exposure Bias: A Multi-Model Diagnostic Study'
4. SS demoted to Discussion
5. All numbers from experiment_data.json, no fabrication

Let me structure the paper:

- Abstract
- Introduction
- Related Work
- Background & Method


- Experiments section with the core findings: the training-inference gap showing the 8x-27x performance degradation, the four-way ablation isolating gating and zero-increment effects, gradient conflict analysis using PCGrad to demonstrate causal mechanisms, cross-model validation on Llama, sensitivity sweeps over the GAR weight parameter, robustness checks with alternative GAR formulations, and expanded evaluation at N=200 samples
- Analysis diving into attention KL divergence patterns between teacher-forcing and autoregressive modes, plus a taxonomy of failure modes
- Discussion with the demoted statistical significance section

, attempted mitigation strategies like scheduled sampling across multiple seeds and conversation lengths, convergent evidence aligning with Dongre's findings, and future research directions
- Conclusion and limitations sections

The paper's narrative arc centers on mechanistic diagnosis: establishing the failure mode taxonomy as the core contribution, using PCGrad as the first empirical elimination of the gradient conflict hypothesis, and building convergent evidence across models and conditions.

Now I'm reviewing the key experimental results to ground the analysis—looking at gradient statistics from Llama showing near-zero cosine similarity with 53 negative layers, the expanded evaluation across 200 samples where all methods cluster around 0.5 with overlapping confidence intervals, sensitivity analysis showing the gap persists across different λ values despite PPL degradation, KL divergence patterns distinguishing GAR-relevant heads, and the critical finding that scheduled sampling fails on Llama while showing modest performance on Qwen across multiple seeds. token improves. Looking at the 4-seed results, I see s789 at 0.300 compared to the mean of 0.367±0.054 with a CV of 14.7%. Long conversations show SS decaying significantly from 0.42 at 5 turns down to 0.12 at 20 turns. From the paper framing notes, I'm also tracking the cross-model comparisons: Qwen shows a 7.8x gap between TF and AR GAR, while Llama has an even larger 27x gap. PCGrad's cosine similarity ranges from -0.151 to +0.091 but doesn't change the GAR collapse trajectory. The v9 IID variant is nearly identical to v7 in both GAR and perplexity metrics. Gate attention shows 2-7% fluctuation with mean values between 0.93-0.98, and 27 out of 28 layers exhibit negative gate differences indicating reverse turn conditioning. Base GAR sits around 0.019 for Qwen and 0.009 for Llama.

Now I'm ready to write the paper using standard LaTeX formatting. I'll structure it with the typical sections and include all these empirical findings, checking what document class and packages will work best for this output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49f4134d-7aac-43b8-9e98-470aea5674df",
  "isSidechain": false,
  "requestId": "req_011CbM7marTSkTKggrAeCkto",
  "type": "assistant",
  "uuid": "6ef0491a-d876-44b2-a9c6-f120ce5fe619",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0176Kvhs5aaF2LTTcxttHfz5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 719,
      "cache_read_input_tokens": 49335,
      "output_tokens": 1339,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 719,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1339,
          "cache_read_input_tokens": 49335,
          "cache_creation_input_tokens": 719,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 719
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

_source line 20 · 2026-05-24T08:58:51.736Z_

Let me check what LaTeX templates are available in the project.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ef0491a-d876-44b2-a9c6-f120ce5fe619",
  "isSidechain": false,
  "requestId": "req_011CbM7marTSkTKggrAeCkto",
  "type": "assistant",
  "uuid": "f4cf1b8a-c28d-45d4-a35d-240edac34606",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0176Kvhs5aaF2LTTcxttHfz5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 719,
      "cache_read_input_tokens": 49335,
      "output_tokens": 1339,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 719,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1339,
          "cache_read_input_tokens": 49335,
          "cache_creation_input_tokens": 719,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 719
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

_source line 21 · 2026-05-24T08:58:51.890Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01RJKrqY7wuxmuYJcDon4VEx`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4cf1b8a-c28d-45d4-a35d-240edac34606",
  "isSidechain": false,
  "requestId": "req_011CbM7marTSkTKggrAeCkto",
  "type": "assistant",
  "uuid": "a80e5189-82d1-48d3-88d1-09d9006c08f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0176Kvhs5aaF2LTTcxttHfz5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 719,
      "cache_read_input_tokens": 49335,
      "output_tokens": 1339,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 719,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1339,
          "cache_read_input_tokens": 49335,
          "cache_creation_input_tokens": 719,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 719
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

_source line 22 · 2026-05-24T08:58:51.893Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01G8R2wcBCfEuo2j1PL6qNsx`</summary>

```json
{
  "pattern": "**/*.sty",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a80e5189-82d1-48d3-88d1-09d9006c08f9",
  "isSidechain": false,
  "requestId": "req_011CbM7marTSkTKggrAeCkto",
  "type": "assistant",
  "uuid": "e675201e-5c3d-4a6c-b67c-65c28b947166",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0176Kvhs5aaF2LTTcxttHfz5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 719,
      "cache_read_input_tokens": 49335,
      "output_tokens": 1339,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 719,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1339,
          "cache_read_input_tokens": 49335,
          "cache_creation_input_tokens": 719,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 719
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

_source line 23 · 2026-05-24T08:58:51.921Z_

<details><summary>↩ Tool result · `toolu_01RJKrqY7wuxmuYJcDon4VEx`</summary>

```text
artifacts/dream_reports/dream_20260519T135115/best/paper.tex
artifacts/dream_reports/dream_20260519T135115/median/paper.tex
artifacts/dream_reports/dream_20260519T135115/worst/paper.tex
artifacts/dream_reports/dream_20260519T143220/best/paper.tex
artifacts/dream_reports/dream_20260519T143220/median/paper.tex
artifacts/dream_reports/dream_20260519T145320/best/paper.tex
artifacts/dream_reports/dream_20260519T145320/median/paper.tex
artifacts/dream_reports/dream_20260519T145320/worst/paper.tex
docs/paper/background.tex
artifacts/_project/paper/analysis.tex
docs/paper/related_work.tex
docs/paper/experiments.tex
docs/paper/method.tex
docs/paper/introduction.tex
docs/paper/analysis.tex
docs/paper/discussion.tex
docs/paper/conclusion.tex
docs/paper/limitations.tex
docs/paper/abstract.tex
artifacts/_project/paper/table_steering_full.tex
artifacts/table_steering_full.tex
paper/sections/related_work.tex
paper/main.tex
paper/sections/abstract.tex
paper/sections/introduction.tex
paper/sections/limitations.tex
paper/sections/experiments.tex
paper/sections/analysis.tex
paper/sections/method.tex
paper/sections/discussion.tex
paper/sections/conclusion.tex
paper/sections/appendix.tex
artifacts/dream_reports/dream_20260524T081135/best/paper.tex
artifacts/dream_reports/dream_20260524T081135/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a80e5189-82d1-48d3-88d1-09d9006c08f9",
  "isSidechain": false,
  "promptId": "4e9b6b3b-bc11-45d7-a0d2-4aaa1c0c9272",
  "type": "user",
  "uuid": "cb1391fb-f33d-4e9f-8fde-2d561d8af905",
  "toolUseResult": {
    "filenames": [
      "artifacts/dream_reports/dream_20260519T135115/best/paper.tex",
      "artifacts/dream_reports/dream_20260519T135115/median/paper.tex",
      "artifacts/dream_reports/dream_20260519T135115/worst/paper.tex",
      "artifacts/dream_reports/dream_20260519T143220/best/paper.tex",
      "artifacts/dream_reports/dream_20260519T143220/median/paper.tex",
      "artifacts/dream_reports/dream_20260519T145320/best/paper.tex",
      "artifacts/dream_reports/dream_20260519T145320/median/paper.tex",
      "artifacts/dream_reports/dream_20260519T145320/worst/paper.tex",
      "docs/paper/background.tex",
      "artifacts/_project/paper/analysis.tex",
      "docs/paper/related_work.tex",
      "docs/paper/experiments.tex",
      "docs/paper/method.tex",
      "docs/paper/introduction.tex",
      "docs/paper/analysis.tex",
      "docs/paper/discussion.tex",
      "docs/paper/conclusion.tex",
      "docs/paper/limitations.tex",
      "docs/paper/abstract.tex",
      "artifacts/_project/paper/table_steering_full.tex",
      "artifacts/table_steering_full.tex",
      "paper/sections/related_work.tex",
      "paper/main.tex",
      "paper/sections/abstract.tex",
      "paper/sections/introduction.tex",
      "paper/sections/limitations.tex",
      "paper/sections/experiments.tex",
      "paper/sections/analysis.tex",
      "paper/sections/method.tex",
      "paper/sections/discussion.tex",
      "paper/sections/conclusion.tex",
      "paper/sections/appendix.tex",
      "artifacts/dream_reports/dream_20260524T081135/best/paper.tex",
      "artifacts/dream_reports/dream_20260524T081135/median/paper.tex"
    ],
    "durationMs": 18,
    "numFiles": 34,
    "truncated": false
  },
  "sourceToolAssistantUUID": "a80e5189-82d1-48d3-88d1-09d9006c08f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-24T08:58:51.925Z_

<details><summary>↩ Tool result · `toolu_01G8R2wcBCfEuo2j1PL6qNsx`</summary>

```text
artifacts/dream_reports/dream_20260519T145320/best/acl.sty
artifacts/dream_reports/dream_20260519T145320/median/acl.sty
paper/acl.sty
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e675201e-5c3d-4a6c-b67c-65c28b947166",
  "isSidechain": false,
  "promptId": "4e9b6b3b-bc11-45d7-a0d2-4aaa1c0c9272",
  "type": "user",
  "uuid": "8212e789-1c95-4583-8720-67939aac2726",
  "toolUseResult": {
    "filenames": [
      "artifacts/dream_reports/dream_20260519T145320/best/acl.sty",
      "artifacts/dream_reports/dream_20260519T145320/median/acl.sty",
      "paper/acl.sty"
    ],
    "durationMs": 20,
    "numFiles": 3,
    "truncated": false
  },
  "sourceToolAssistantUUID": "e675201e-5c3d-4a6c-b67c-65c28b947166",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-24T08:58:54.720Z_

<details open><summary>🔧 Tool call — Read · `toolu_0159xammv4LzZX4q8vMCVrC3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/best/paper.tex",
  "limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8212e789-1c95-4583-8720-67939aac2726",
  "isSidechain": false,
  "requestId": "req_011CbM7pRSzfPqhHSZeMeY64",
  "type": "assistant",
  "uuid": "958a4c47-b9b1-49b9-adc4-8193e35e3040",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DCNw3aUEeZ33qQ44Wd4AxT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1863,
      "cache_read_input_tokens": 50054,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1863,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 119,
          "cache_read_input_tokens": 50054,
          "cache_creation_input_tokens": 1863,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1863
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

_source line 26 · 2026-05-24T08:58:54.727Z_

<details><summary>↩ Tool result · `toolu_0159xammv4LzZX4q8vMCVrC3`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{times}
5	\usepackage{amsmath,amssymb}
6	\usepackage{booktabs}
7	\usepackage{multirow}
8	\usepackage{graphicx}
9	\usepackage{xcolor}
10	\usepackage{hyperref}
11	\usepackage{url}
12	\usepackage[margin=1in]{geometry}
13	\usepackage{natbib}
14	\usepackage{subcaption}
15	\usepackage{tablefootnote}
16	
17	\newcommand{\gar}{\textsc{GAR}}
18	\newcommand{\garours}{\textsc{GAR}\textsubscript{ours}}
19	\newcommand{\gardongre}{\textsc{GAR}\textsubscript{Dongre}}
20	\newcommand{\tg}{\textsc{ThreadGate}}
21	\newcommand{\ug}{\textsc{UniformGate}}
22	\newcommand{\lo}{\textsc{LoRA-only}}
23	\renewcommand{\ss}{\textsc{SS}}
24	
25	\title{From Collapse to Recovery: Diagnosing and Mitigating\\ Exposure Bias in Multi-Turn Attention Objectives}
26	
27	\author{Anonymous}
28	\date{}
29	
30	\begin{document}
31	\maketitle
32	
33	% ============================================================
34	% ABSTRACT
35	% ============================================================
36	\begin{abstract}
37	Multi-turn dialogue models suffer progressive goal-attention degradation as conversations grow longer. Prior work shows goal information persists in residual streams (probe AUC$=$0.98) even as attention access declines, motivating learnable residual gating to recover it. We implement this hypothesis as \tg{}, a per-layer gating module trained jointly with next-token prediction (NTP) and an auxiliary Goal Accessibility Ratio (\gar{}) loss. \tg{} successfully optimizes \gar{} under teacher-forcing (TF \gar{}$=$0.50), yet collapses at inference on model-generated text (AR \gar{}$=$0.064 on Qwen-2.5-7B, 0.030 on Llama-3.1-8B), revealing an 8$\times$--27$\times$ training--inference gap. Through PCGrad causal ablation, per-head KL divergence analysis, and cross-model replication, we identify exposure bias---not gradient competition---as the root cause. This gap selectively disrupts summary-position attention patterns while leaving all-token attention unaffected. Scheduled sampling (SS) compresses the gap from 8$\times$ to ${\sim}$1.3$\times$ on both Qwen and Llama (3-seed AR \gar{}$=$0.40$\pm$0.05, no perplexity cost), and inference-time $\beta$-steering further recovers \gar{} to 0.72. Our results provide the first empirical characterization of how exposure bias destroys auxiliary attention objectives and demonstrate that classical mitigation transfers effectively to multi-turn transformer settings.
38	\end{abstract}
39	
40	% ============================================================
41	% 1. INTRODUCTION
42	% ============================================================
43	\section{Introduction}
44	
45	Large Language Models (LLMs) exhibit progressive degradation in multi-turn dialogue: as conversations grow longer, models increasingly fail to maintain attention to the user's original goals and instructions \citep{dongre2026goal,liu2024lost,hsieh2024ruler}. \citet{dongre2026goal} formalized this through the Goal Accessibility Ratio (\gar{}), demonstrating 27--48\% declines across 12 models over 50 conversational turns. This degradation directly impacts practical deployments where sustained goal-tracking is essential---customer service, tutoring, and collaborative problem-solving.
46	
47	A striking observation from \citet{dongre2026goal} is that goal information \emph{persists} in the residual stream even as the attention channel closes: linear probes achieve AUC$=$0.98 on goal-presence classification at late layers. This creates a natural hypothesis: if goal-relevant information survives in residual representations but attention fails to route it, a learnable gate on the residual connection should modulate layer contributions to recover goal accessibility.
48	
49	We implement this hypothesis as \tg{}, a per-layer gating module that receives hidden states and turn-position embeddings, producing per-token, per-layer gate values trained jointly with NTP and a \gar{} auxiliary loss. Under teacher-forcing, \tg{} raises \gar{} from 0.02 to 0.50---a successful optimization. However, when evaluated on model-generated text (the autoregressive regime), \gar{} collapses to 0.064 on Qwen-2.5-7B (7.8$\times$ gap) and 0.030 on Llama-3.1-8B (15.9$\times$ gap). This dramatic training--inference discrepancy is our central finding.
50	
51	Through systematic causal analysis, we establish that exposure bias---the distribution shift between gold training contexts and model-generated inference contexts---is the sole root cause of this collapse. PCGrad \citep{yu2020gradient} ablation eliminates gradient direction conflicts between NTP and \gar{} losses without reducing the gap (modus tollens). A $\lambda_{\text{GAR}}$ sweep across two orders of magnitude (0.1--10) eliminates gradient magnitude imbalance without reducing the gap. Per-head KL divergence analysis reveals that the heads most disrupted by distribution shift ($r=0.38$, $p=0.002$) are precisely those responsible for goal-relevant attention routing. Cross-model replication on Llama-3.1-8B confirms the pattern is architecture-general.
52	
53	Crucially, we demonstrate that scheduled sampling (SS)---originally designed for RNN sequence models \citep{bengio2015scheduled}---transfers effectively to multi-turn transformer attention objectives. SS compresses the TF--AR gap from 8$\times$ to ${\sim}$1.3$\times$ on Qwen-2.5-7B (3-seed: AR \gar{}$=$0.401$\pm$0.047) and from 15.9$\times$ to 1.34$\times$ on Llama-3.1-8B, with no perplexity cost. Inference-time $\beta$-steering independently recovers \gar{} from 0.064 to 0.727. Our contributions are:
54	
55	\begin{enumerate}
56	    \item The first empirical characterization of how exposure bias destroys auxiliary attention objectives: an 8$\times$--27$\times$ TF--AR gap specific to summary-position attention patterns (Qwen 7.8$\times$, Llama 15.9$\times$).
57	    \item Causal exclusion of gradient competition via PCGrad ablation and $\lambda$ sensitivity analysis, isolating exposure bias as the sole mechanism.
58	    \item Per-head KL divergence analysis localizing the distribution shift to late-layer goal-routing heads ($r=0.38$, $p=0.002$), explaining the selectivity of the collapse.
59	    \item Cross-model validation on two architectures (Qwen-2.5-7B MHA and Llama-3.1-8B GQA) confirming architecture-general failure and recovery.
60	    \item Scheduled sampling as an effective mitigation, compressing the gap to ${\sim}$1.3$\times$ on both models (3-seed validated), demonstrating that classical exposure bias remedies transfer to multi-turn attention objectives.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "958a4c47-b9b1-49b9-adc4-8193e35e3040",
  "isSidechain": false,
  "promptId": "4e9b6b3b-bc11-45d7-a0d2-4aaa1c0c9272",
  "type": "user",
  "uuid": "cf1d0855-4e69-44ab-8f07-18a1de848c87",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/best/paper.tex",
      "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{url}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{natbib}\n\\usepackage{subcaption}\n\\usepackage{tablefootnote}\n\n\\newcommand{\\gar}{\\textsc{GAR}}\n\\newcommand{\\garours}{\\textsc{GAR}\\textsubscript{ours}}\n\\newcommand{\\gardongre}{\\textsc{GAR}\\textsubscript{Dongre}}\n\\newcommand{\\tg}{\\textsc{ThreadGate}}\n\\newcommand{\\ug}{\\textsc{UniformGate}}\n\\newcommand{\\lo}{\\textsc{LoRA-only}}\n\\renewcommand{\\ss}{\\textsc{SS}}\n\n\\title{From Collapse to Recovery: Diagnosing and Mitigating\\\\ Exposure Bias in Multi-Turn Attention Objectives}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nMulti-turn dialogue models suffer progressive goal-attention degradation as conversations grow longer. Prior work shows goal information persists in residual streams (probe AUC$=$0.98) even as attention access declines, motivating learnable residual gating to recover it. We implement this hypothesis as \\tg{}, a per-layer gating module trained jointly with next-token prediction (NTP) and an auxiliary Goal Accessibility Ratio (\\gar{}) loss. \\tg{} successfully optimizes \\gar{} under teacher-forcing (TF \\gar{}$=$0.50), yet collapses at inference on model-generated text (AR \\gar{}$=$0.064 on Qwen-2.5-7B, 0.030 on Llama-3.1-8B), revealing an 8$\\times$--27$\\times$ training--inference gap. Through PCGrad causal ablation, per-head KL divergence analysis, and cross-model replication, we identify exposure bias---not gradient competition---as the root cause. This gap selectively disrupts summary-position attention patterns while leaving all-token attention unaffected. Scheduled sampling (SS) compresses the gap from 8$\\times$ to ${\\sim}$1.3$\\times$ on both Qwen and Llama (3-seed AR \\gar{}$=$0.40$\\pm$0.05, no perplexity cost), and inference-time $\\beta$-steering further recovers \\gar{} to 0.72. Our results provide the first empirical characterization of how exposure bias destroys auxiliary attention objectives and demonstrate that classical mitigation transfers effectively to multi-turn transformer settings.\n\\end{abstract}\n\n% ============================================================\n% 1. INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nLarge Language Models (LLMs) exhibit progressive degradation in multi-turn dialogue: as conversations grow longer, models increasingly fail to maintain attention to the user's original goals and instructions \\citep{dongre2026goal,liu2024lost,hsieh2024ruler}. \\citet{dongre2026goal} formalized this through the Goal Accessibility Ratio (\\gar{}), demonstrating 27--48\\% declines across 12 models over 50 conversational turns. This degradation directly impacts practical deployments where sustained goal-tracking is essential---customer service, tutoring, and collaborative problem-solving.\n\nA striking observation from \\citet{dongre2026goal} is that goal information \\emph{persists} in the residual stream even as the attention channel closes: linear probes achieve AUC$=$0.98 on goal-presence classification at late layers. This creates a natural hypothesis: if goal-relevant information survives in residual representations but attention fails to route it, a learnable gate on the residual connection should modulate layer contributions to recover goal accessibility.\n\nWe implement this hypothesis as \\tg{}, a per-layer gating module that receives hidden states and turn-position embeddings, producing per-token, per-layer gate values trained jointly with NTP and a \\gar{} auxiliary loss. Under teacher-forcing, \\tg{} raises \\gar{} from 0.02 to 0.50---a successful optimization. However, when evaluated on model-generated text (the autoregressive regime), \\gar{} collapses to 0.064 on Qwen-2.5-7B (7.8$\\times$ gap) and 0.030 on Llama-3.1-8B (15.9$\\times$ gap). This dramatic training--inference discrepancy is our central finding.\n\nThrough systematic causal analysis, we establish that exposure bias---the distribution shift between gold training contexts and model-generated inference contexts---is the sole root cause of this collapse. PCGrad \\citep{yu2020gradient} ablation eliminates gradient direction conflicts between NTP and \\gar{} losses without reducing the gap (modus tollens). A $\\lambda_{\\text{GAR}}$ sweep across two orders of magnitude (0.1--10) eliminates gradient magnitude imbalance without reducing the gap. Per-head KL divergence analysis reveals that the heads most disrupted by distribution shift ($r=0.38$, $p=0.002$) are precisely those responsible for goal-relevant attention routing. Cross-model replication on Llama-3.1-8B confirms the pattern is architecture-general.\n\nCrucially, we demonstrate that scheduled sampling (SS)---originally designed for RNN sequence models \\citep{bengio2015scheduled}---transfers effectively to multi-turn transformer attention objectives. SS compresses the TF--AR gap from 8$\\times$ to ${\\sim}$1.3$\\times$ on Qwen-2.5-7B (3-seed: AR \\gar{}$=$0.401$\\pm$0.047) and from 15.9$\\times$ to 1.34$\\times$ on Llama-3.1-8B, with no perplexity cost. Inference-time $\\beta$-steering independently recovers \\gar{} from 0.064 to 0.727. Our contributions are:\n\n\\begin{enumerate}\n    \\item The first empirical characterization of how exposure bias destroys auxiliary attention objectives: an 8$\\times$--27$\\times$ TF--AR gap specific to summary-position attention patterns (Qwen 7.8$\\times$, Llama 15.9$\\times$).\n    \\item Causal exclusion of gradient competition via PCGrad ablation and $\\lambda$ sensitivity analysis, isolating exposure bias as the sole mechanism.\n    \\item Per-head KL divergence analysis localizing the distribution shift to late-layer goal-routing heads ($r=0.38$, $p=0.002$), explaining the selectivity of the collapse.\n    \\item Cross-model validation on two architectures (Qwen-2.5-7B MHA and Llama-3.1-8B GQA) confirming architecture-general failure and recovery.\n    \\item Scheduled sampling as an effective mitigation, compressing the gap to ${\\sim}$1.3$\\times$ on both models (3-seed validated), demonstrating that classical exposure bias remedies transfer to multi-turn attention objectives.",
      "numLines": 60,
      "startLine": 1,
      "totalLines": 613
    }
  },
  "sourceToolAssistantUUID": "958a4c47-b9b1-49b9-adc4-8193e35e3040",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 27_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260524T081135 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_ga…",
  "leafUuid": "cf1d0855-4e69-44ab-8f07-18a1de848c87",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier diagnostic paper for dream_20260524T081135",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1"
}
```

---

### Assistant

_source line 29 · 2026-05-24T08:59:21.529Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I can see the template style. Now let me write the worst-tier paper. The key differences from the best tier:

1. Title: "Why Auxiliary Attention Losses Fail Under Exposure Bias: A Multi-Model Diagnostic Study"
2. SS demoted from Results to Discussion "attempted mitigation"
3. Core selling point: failure mode taxonomy
4. Llama SS FAILS (AR GAR β=0 = 0.04, gap 11.75x)
5. SS is model-specific, not generalizable
6. PCGrad narrative: "first empirical elimination of gradient conflict hypothesis" 


7. Llama's gradient geometry shows orthogonal vectors rather than conflicting ones, which contradicts the standard narrative
8. One seed variant pushes CV to 14.7%, and alternative GAR definitions only help with last-token metrics while failing elsewhere
9. Long conversations reveal SS effectiveness decays sharply after 10 turns, and the KL divergence stays minimal at 0.054, suggesting the mechanism isn't what we thought

Now I'm structuring the paper with an abstract, introduction, related work, background on the method, and experiments covering the training-inference gap across different model scales.

The ablations will examine PCGrad's causal role including the gradient geometry findings, cross-model validation, and sensitivity to the loss weighting parameter, while the analysis section breaks down failure modes and attention shifts.

For discussion, I'm covering the scheduled sampling attempts—where Qwen showed partial recovery but Llama didn't budge—alongside the convergent findings with prior work and concrete directions forward, then wrapping with limitations and appendices for the expanded evaluation, alternative metrics, and sensitivity details.

Now I need to map all nine experiments into the paper structure to ensure complete coverage: the gradient conflict analysis goes into the cross-model section, the 200-conversation evaluation becomes an appendix, sensitivity analysis gets its own subsection, attention divergence metrics go into the analysis, and the scheduled sampling results split between Llama's failure and Qwen's partial success in the mitigation section, with robustness checks for alternative definitions in the appendices.

I'm ready to write the full LaTeX paper now, aiming for comprehensive coverage with honest treatment of negative results while staying within reasonable bounds.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf1d0855-4e69-44ab-8f07-18a1de848c87",
  "isSidechain": false,
  "requestId": "req_011CbM7pdcyYweJZpJcN68iz",
  "type": "assistant",
  "uuid": "1e7076e9-b1ba-4402-afdb-666c7aced7d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AH1yqfshPf6uGQ2t1MyiMb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2085,
      "cache_read_input_tokens": 51917,
      "output_tokens": 17838,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2085,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17838,
          "cache_read_input_tokens": 51917,
          "cache_creation_input_tokens": 2085,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2085
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

_source line 30 · 2026-05-24T08:59:21.535Z_

Now I'll write the full worst-tier paper. This reframes as a pure mechanistic diagnostic with SS demoted to Discussion.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e7076e9-b1ba-4402-afdb-666c7aced7d9",
  "isSidechain": false,
  "requestId": "req_011CbM7pdcyYweJZpJcN68iz",
  "type": "assistant",
  "uuid": "dca75964-585b-41b5-b163-1f722fe87f6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AH1yqfshPf6uGQ2t1MyiMb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2085,
      "cache_read_input_tokens": 51917,
      "output_tokens": 17838,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2085,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17838,
          "cache_read_input_tokens": 51917,
          "cache_creation_input_tokens": 2085,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2085
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

_source line 31 · 2026-05-24T09:04:26.446Z_

<details open><summary>🔧 Tool call — Write · `toolu_01Jhv9uvafnUBijKYmYd1zxK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{url}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{natbib}\n\\usepackage{subcaption}\n\n\\newcommand{\\gar}{\\textsc{GAR}}\n\\newcommand{\\garours}{\\textsc{GAR}\\textsubscript{ours}}\n\\newcommand{\\gardongre}{\\textsc{GAR}\\textsubscript{Dongre}}\n\\newcommand{\\tg}{\\textsc{ThreadGate}}\n\\newcommand{\\ug}{\\textsc{UniformGate}}\n\\newcommand{\\lo}{\\textsc{LoRA-only}}\n\\renewcommand{\\ss}{\\textsc{SS}}\n\n\\title{Why Auxiliary Attention Losses Fail Under Exposure Bias:\\\\A Multi-Model Diagnostic Study}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nMulti-turn dialogue models progressively lose attention to user goals as conversations grow longer. Prior work shows goal information persists in residual streams (probe AUC$=$0.98) even as attention access declines, motivating learnable residual gating. We implement this as \\tg{}, a per-layer gating module trained with an auxiliary Goal Accessibility Ratio (\\gar{}) loss. \\tg{} optimizes \\gar{} under teacher-forcing (TF \\gar{}$=$0.50) but collapses on model-generated text (AR \\gar{}$=$0.064 on Qwen-2.5-7B, 0.018 on Llama-3.1-8B), revealing an 8--27$\\times$ training--inference gap. Through PCGrad ablation, $\\lambda$ sensitivity analysis, and cross-model replication, we causally exclude gradient competition and isolate exposure bias as the root cause. We identify three failure modes: (NF1) reverse turn conditioning from NTP gradient dominance, (NF2) structural distribution shift independent of loss design, and (NF3) insufficient gate intervention strength (2--7\\%). Attempted scheduled sampling mitigation succeeds partially on Qwen (AR \\gar{}$=$0.39$\\pm$0.04, 3-seed) but fails on Llama (AR \\gar{}$=$0.04, gap 11.75$\\times$), demonstrating model-specificity. Our negative results establish concrete failure modes that future work must overcome to make auxiliary attention losses viable under autoregressive generation.\n\\end{abstract}\n\n% ============================================================\n% 1. INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nLarge language models exhibit progressive degradation in multi-turn dialogue: as conversations grow longer, models fail to maintain attention to the user's original goals \\citep{dongre2026goal,liu2024lost,hsieh2024ruler}. \\citet{dongre2026goal} formalized this through the Goal Accessibility Ratio (\\gar{}), demonstrating 27--48\\% declines across 12 models over 50 turns.\n\nA key observation from \\citet{dongre2026goal} is that goal information \\emph{persists} in the residual stream even as attention degrades: linear probes achieve AUC$=$0.98 at late layers. This creates a natural hypothesis: if goal information survives in representations but attention fails to route it, a learnable gate on the residual connection should recover goal accessibility. We test this hypothesis systematically.\n\nWe implement \\tg{}, a per-layer gating module trained jointly with next-token prediction (NTP) and a \\gar{} auxiliary loss. Under teacher-forcing, \\tg{} raises \\gar{} from 0.02 to 0.50. However, on model-generated text, \\gar{} collapses to 0.064 on Qwen-2.5-7B (7.8$\\times$ gap) and 0.018 on Llama-3.1-8B (27$\\times$ gap). This dramatic training--inference discrepancy---rather than any particular fix---is our central finding.\n\nThrough systematic causal analysis, we establish three failure modes that jointly explain the collapse:\n\\begin{itemize}\n    \\item \\textbf{NF1 (Reverse turn conditioning):} NTP gradients dominate gate parameters (magnitude ratio 12--25$\\times$), causing 27/28 layers to learn reversed turn-dependent gating that suppresses at early turns (where \\gar{} is high) and becomes passive at late turns (where intervention is needed).\n    \\item \\textbf{NF2 (Structural distribution shift):} The 8--27$\\times$ gap persists across all training variants (ThreadGate, PCGrad, UniformGate, LoRA-only), loss weightings ($\\lambda \\in \\{0.1, 1.0, 10.0\\}$), and architectures (Qwen MHA, Llama GQA), confirming exposure bias as the structural root cause.\n    \\item \\textbf{NF3 (Insufficient intervention strength):} At inference, gates attenuate sub-layer outputs by only 2--7\\% (gate mean 0.93--0.98), providing negligible modulation.\n\\end{itemize}\n\nPCGrad ablation \\citep{yu2020gradient} eliminates gradient direction conflicts without reducing the gap, providing the first empirical elimination of the gradient conflict hypothesis for auxiliary attention losses. Cross-model replication on Llama-3.1-8B confirms the failure pattern is architecture-general, with even more severe collapse (27$\\times$ gap).\n\nCombined with \\citet{dongre2026goal}'s independent failure of goal re-injection, our results reveal convergent evidence: two independent intervention routes (goal re-injection and residual gating) $\\times$ two models $=$~four paths, all failing to bridge the exposure bias gap. Our negative results establish concrete failure modes that future work must overcome.\n\n\\paragraph{Contributions.}\n\\begin{enumerate}\n    \\item A failure mode taxonomy (NF1--NF3) for auxiliary attention losses under exposure bias, providing the first systematic characterization of how teacher-forcing distribution shift destroys learned attention patterns (8--27$\\times$ gap).\n    \\item The first empirical elimination of gradient competition as a causal factor: PCGrad removes direction conflicts with no effect on any observable metric (GAR, PPL, NTP loss).\n    \\item Cross-model validation on Qwen-2.5-7B (MHA) and Llama-3.1-8B (GQA) establishing architecture-generality of the failure.\n    \\item Convergent evidence across two independent intervention designs and two models, narrowing the space of viable future approaches.\n\\end{enumerate}\n\n% ============================================================\n% 2. RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Multi-turn dialogue degradation.}\nGoal-tracking in long conversations has been studied through instruction retention \\citep{qin2024infobench,dongre2026goal}, context utilization \\citep{liu2024lost,hsieh2024ruler}, and dialogue coherence \\citep{ko2024multichallenge}. \\citet{dongre2026goal} provide the most systematic analysis, defining \\gar{} and demonstrating degradation across 12 models. MT-Bench-101 \\citep{bai2024mtbench101} similarly evaluates multi-turn capabilities.\n\n\\paragraph{Residual gating and adaptive depth.}\nLearnable gates on residual connections have been explored for adaptive computation: LayerDrop \\citep{fan2020layerdrop}, early exit \\citep{schuster2022confident}, and layer-wise scaling \\citep{bachlechner2021rezero}. FlexiDepth \\citep{luo2025flexidepth} learns layer selection, while \\citet{gromov2024unreasonable} show many layers are prunable. Our gating formulation follows the ReZero parameterization $x + g \\cdot f(x)$ but applies it to auxiliary attention objectives rather than efficiency.\n\n\\paragraph{Attention steering and intervention.}\nAttention intervention techniques include attention head pruning \\citep{voita2019analyzing,michel2019sixteen}, activation steering \\citep{li2024inference,turner2023activation}, and attention loss regularization \\citep{ghader2017does,strubell2018linguistically}. \\citet{qiu2025gated} propose gated attention for selective processing. The key distinction of our work is diagnosing \\emph{why} attention-based auxiliary losses fail at inference rather than proposing new interventions.\n\n\\paragraph{Exposure bias in sequence models.}\nExposure bias---the mismatch between teacher-forced training and autoregressive inference---is well-documented \\citep{ranzato2016sequence,wiseman2016sequence,bengio2015scheduled}. Mitigation approaches include scheduled sampling \\citep{bengio2015scheduled}, Professor Forcing \\citep{lamb2016professor}, SEARNN \\citep{leblond2018searnn}, and parallel attention forcing \\citep{dou2022parallel}. While exposure bias has been extensively studied for generation quality, its impact on \\emph{auxiliary attention losses} has not been characterized.\n\n\\paragraph{Gradient conflicts in multi-task learning.}\nPCGrad \\citep{yu2020gradient}, CAGrad \\citep{liu2021conflict}, and Nash-MTL \\citep{navon2022multi} address gradient conflicts in multi-objective optimization. We use PCGrad specifically as a \\emph{diagnostic tool}: by eliminating gradient direction conflicts and observing no change in outcomes, we causally exclude this mechanism.\n\n% ============================================================\n% 3. BACKGROUND\n% ============================================================\n\\section{Background}\n\n\\subsection{Goal Accessibility Ratio}\n\nThe Goal Accessibility Ratio (\\gar{}) \\citep{dongre2026goal} measures how strongly attention heads attend to goal-relevant tokens from response positions. We use two variants:\n\n\\textbf{\\garours{}} computes attention from the \\emph{last token} of each assistant turn to all goal tokens (system prompt + first user query). The last token serves as a summary position where the model aggregates context for next-token prediction.\n\n\\textbf{\\gardongre{}} computes attention from \\emph{all response tokens} to system prompt task tokens, following the original definition.\n\n\\subsection{Residual Stream Persistence}\n\n\\citet{dongre2026goal} demonstrated that goal information persists in residual stream representations (linear probe AUC$=$0.98) even as attention-based \\gar{} declines. This dissociation motivates architectural interventions on the residual connection: if information exists but attention cannot access it, modulating the residual pathway should help.\n\n% ============================================================\n% 4. METHOD\n% ============================================================\n\\section{Method}\n\n\\subsection{ThreadGate Architecture}\n\n\\tg{} adds a learnable gate $g_l \\in (0,1)$ to each transformer layer $l$, modulating the sub-layer output via a ReZero-style \\citep{bachlechner2021rezero} residual connection:\n\\begin{equation}\n    x_{l+1} = x_l + g_l \\cdot f_l(x_l)\n\\end{equation}\nwhere $f_l$ denotes the $l$-th transformer block (attention + FFN). When $g_l \\to 0$, the layer becomes a no-op (identity); when $g_l \\to 1$, the layer operates normally.\n\nEach gate is parameterized by a 2-layer MLP that receives the hidden state projection and turn-position embeddings:\n\\begin{equation}\n    g_l = \\sigma\\big(W_2 \\cdot \\text{ReLU}(W_1 \\cdot [\\text{proj}(x_l); \\text{emb}(t_d, t_i)] + b_1) + b_2\\big)\n\\end{equation}\nwhere $t_d$ is the turn distance from the current position and $t_i$ is the absolute turn index. The gate produces per-token, per-layer scalar values.\n\n\\textbf{UniformGate (\\ug{})} uses the same architecture but replaces turn embeddings with a constant vector, yielding content-dependent but turn-agnostic gating. This ablation isolates whether turn conditioning contributes to the failure.\n\n\\textbf{LoRA-only (\\lo{})} fixes $g=1.0$ (no gating mechanism) while retaining the \\gar{} auxiliary loss, isolating the contribution of gating itself versus the auxiliary loss signal.\n\n\\subsection{Training Objective}\n\nThe total loss combines NTP and \\gar{} objectives:\n\\begin{equation}\n    \\mathcal{L} = \\mathcal{L}_{\\text{NTP}} + \\lambda_{\\text{GAR}} \\cdot \\mathcal{L}_{\\text{GAR}} + \\lambda_{\\text{div}} \\cdot \\mathcal{L}_{\\text{div}}\n\\end{equation}\n\n$\\mathcal{L}_{\\text{GAR}}$ uses MSE to push gate-modulated attention toward target \\gar{} values. $\\mathcal{L}_{\\text{div}}$ is a gate diversity regularizer preventing all gates from collapsing to the same value. We set $\\lambda_{\\text{GAR}} = 1.0$ and $\\lambda_{\\text{div}} = 0.1$ by default (v7 configuration), selected after iterating through cumulative (v1--v2), maximize (v3--v5), smooth saturation (v6), and MSE target (v7) loss designs.\n\n\\subsection{Training Setup}\n\nAll experiments fine-tune with LoRA ($r=16$, $\\alpha=32$) on UltraChat \\citep{ding2023enhancing}. Qwen-2.5-7B \\citep{qwen2025qwen25} and Llama-3.1-8B \\citep{dubey2024llama3} serve as base models. Training runs for 3 epochs with batch size 4 and learning rate $2\\times10^{-4}$.\n\n% ============================================================\n% 5. EXPERIMENTS\n% ============================================================\n\\section{Experiments}\n\n\\subsection{Evaluation Protocol}\n\nWe evaluate under two regimes:\n\n\\textbf{Teacher-forcing (TF):} Model processes gold conversation text. \\gar{} is computed from attention patterns over ground-truth contexts.\n\n\\textbf{Autoregressive (AR):} Model generates responses given only the conversation history. \\gar{} is computed from attention over model-generated text. The $\\beta$-steering parameter scales gate values at inference: $g'_l = \\min(1, \\beta \\cdot g_l)$, with $\\beta=0$ (gates disabled, pure LoRA) as the default AR evaluation setting.\n\nWe report \\garours{} (last-token to goals) as the primary metric and \\gardongre{} (all-token) for cross-study comparison. Perplexity (PPL) measured on held-out data monitors language modeling quality.\n\n\\subsection{Main Result: The Training--Inference Gap}\n\\label{sec:main_result}\n\nTable~\\ref{tab:main_gap} presents our central finding. \\tg{} achieves TF \\garours{}$=$0.50 on Qwen-2.5-7B, a 25$\\times$ improvement over the base model (0.02). However, AR evaluation with gates disabled ($\\beta=0$) yields \\garours{}$=$0.064---a 7.8$\\times$ training--inference gap. On Llama-3.1-8B, the collapse is even more severe: TF \\garours{}$=$0.484, AR \\garours{}$=$0.018, a 27$\\times$ gap.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Training--inference gap across models. TF \\gar{} is evaluated on gold text; AR \\gar{} on model-generated text ($\\beta=0$). Gap ratio $=$ TF/AR.}\n\\label{tab:main_gap}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{TF \\garours{}} & \\textbf{AR \\garours{}} & \\textbf{Gap} & \\textbf{PPL} \\\\\n\\midrule\nQwen Base & 0.013 & 0.019 & 0.7$\\times$ & 4.34 \\\\\nQwen \\tg{} v7 & 0.501 & 0.064 & 7.8$\\times$ & 2.78 \\\\\nLlama Base & 0.017 & 0.009 & 1.9$\\times$ & 3.45 \\\\\nLlama \\tg{} v7 & 0.484 & 0.018 & 27$\\times$ & 2.57 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe base models show no meaningful gap (TF$\\approx$AR$\\approx$0.01--0.02), confirming that the gap is introduced by the auxiliary \\gar{} loss training rather than being inherent to autoregressive generation.\n\n\\subsection{Four-Way Ablation: Gating Provides Zero Increment}\n\\label{sec:ablation}\n\nTo isolate the source of failure, we compare four training variants on Qwen-2.5-7B with expanded evaluation (N$=$200 conversations for TF, N$=$50 for AR):\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Four-way ablation (Qwen-2.5-7B). TF eval N$=$200 with 95\\% bootstrap CI. All fine-tuned variants include the \\gar{} auxiliary loss; the ablation tests gating mechanism contribution.}\n\\label{tab:ablation}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Variant} & \\textbf{TF \\garours{}} & \\textbf{95\\% CI} & \\textbf{AR \\garours{}} & \\textbf{PPL} \\\\\n\\midrule\nBase & 0.013 & [0.010, 0.016] & 0.019 & 4.34 \\\\\n\\lo{} & 0.497 & [0.484, 0.510] & 0.025 & 2.78 \\\\\n\\ug{} & 0.503 & [0.490, 0.516] & 0.015 & 2.78 \\\\\n\\tg{} v7 & 0.501 & [0.488, 0.514] & 0.016 & 2.78 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:ablation} reveals that all three fine-tuned variants achieve statistically indistinguishable TF \\gar{} ($\\sim$0.50) and identical PPL (2.78). Pairwise bootstrap comparisons confirm no significant differences: TG$-$LO $=$ $+$0.004, 95\\% CI [$-$0.008, $+$0.016]; UG$-$LO $=$ $+$0.006, 95\\% CI [$-$0.006, $+$0.018]. All confidence intervals contain zero.\n\nThis zero-increment result is devastating for the gating hypothesis: neither learned turn conditioning (\\tg{}) nor content-dependent gating (\\ug{}) provides any benefit over simply adding a \\gar{} loss to LoRA fine-tuning (\\lo{}). The gating mechanism is entirely redundant.\n\n\\subsection{PCGrad Causal Exclusion of Gradient Conflict}\n\\label{sec:pcgrad}\n\nA natural hypothesis for the failure is gradient competition: NTP and \\gar{} losses produce conflicting gradients that prevent effective gate learning. We test this by training a PCGrad variant (v9) that projects conflicting gradients to be orthogonal \\citep{yu2020gradient}.\n\n\\paragraph{Qwen gradient geometry.} On Qwen-2.5-7B, 67--79\\% of layers show negative NTP-\\gar{} cosine similarity (mild gradient conflict), with NTP magnitude dominating by 7.5--14.7$\\times$. PCGrad successfully eliminates direction conflicts: post-projection cosine similarity oscillates around zero (range [$-$0.151, $+$0.091]). However, the \\gar{} loss collapse trajectory is unchanged, and inference evaluation shows no improvement: v9 \\garours{}$=$0.0151 vs.\\ v7$=$0.0157 (difference $<$0.1 percentage points), v9 PPL$=$2.780 vs.\\ v7$=$2.784.\n\n\\paragraph{Llama gradient geometry.} On Llama-3.1-8B, the gradient geometry differs qualitatively (Table~\\ref{tab:gradient_geometry}). Mean cosine similarity is $+$0.005 (near-orthogonal, not conflicting), with only 53.1\\% of layers showing negative cosine similarity---near the 50\\% random baseline. NTP magnitude dominance is even more extreme (25.7$\\times$ median). The gradient geometry progressively shifts across epochs: cos\\_sim declines from $+$0.012 (epoch 0) to $-$0.001 (epoch 2), and negative-layer percentage rises from 50.0\\% to 56.3\\%.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model gradient geometry comparison. Llama shows near-orthogonal (not conflicting) gradients with extreme NTP magnitude dominance, contrasting Qwen's mild conflict pattern.}\n\\label{tab:gradient_geometry}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{cos\\_sim} & \\textbf{neg layers (\\%)} & \\textbf{mag ratio} & \\textbf{Pattern} \\\\\n\\midrule\nQwen-2.5-7B & $-$0.062 & 72.6 & 11.9$\\times$ & Mild conflict \\\\\nLlama-3.1-8B & $+$0.005 & 53.1 & 25.7$\\times$ & Orthogonal \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Llama per-epoch gradient statistics showing progressive drift toward orthogonality.}\n\\label{tab:llama_epochs}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Epoch} & \\textbf{cos\\_sim} & \\textbf{neg layers (\\%)} & \\textbf{mag ratio} \\\\\n\\midrule\n0 & $+$0.012 & 50.0 & 18.3$\\times$ \\\\\n1 & $+$0.003 & 53.1 & 24.1$\\times$ \\\\\n2 & $-$0.001 & 56.3 & 25.7$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe cross-model comparison strengthens the causal exclusion argument through a different path: on Qwen, PCGrad \\emph{removes} conflict with no effect; on Llama, conflict \\emph{does not exist} yet the same failure occurs. In both cases, NTP magnitude dominance (12--26$\\times$) is the consistent factor, but this dominance alone does not cause the gap---it merely ensures that gates optimize primarily for NTP rather than \\gar{}.\n\n\\subsection{$\\lambda_{\\text{GAR}}$ Sensitivity Analysis}\n\\label{sec:lambda}\n\nIf NTP magnitude dominance drives the failure, increasing $\\lambda_{\\text{GAR}}$ should help by rebalancing gradient magnitudes. Table~\\ref{tab:lambda} shows this is not the case.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{$\\lambda_{\\text{GAR}}$ sensitivity (Qwen-2.5-7B, 1 epoch). The training--inference gap persists across two orders of magnitude, confirming distribution shift independence from loss weighting.}\n\\label{tab:lambda}\n\\begin{tabular}{lccccc}\n\\toprule\n$\\lambda_{\\text{GAR}}$ & \\textbf{TF \\garours{}} & \\textbf{AR \\garours{}} & \\textbf{Gap} & \\textbf{PPL} & \\textbf{Stable?} \\\\\n\\midrule\n0.1 & 0.49 & 0.015 & 32.7$\\times$ & 2.78 & Yes \\\\\n1.0 (default) & 0.50 & 0.016 & 31.3$\\times$ & 2.78 & Yes \\\\\n10.0 & 0.52 & 0.018 & 28.9$\\times$ & 3.80 & No \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt $\\lambda=0.1$, the \\gar{} signal is too weak (loss$=$0.0003), gates freeze near identity (mean$=$0.98, std$=$0.01), and the variant is functionally equivalent to \\lo{}. At $\\lambda=10.0$, gates deviate further from identity (mean$=$0.82, min$=$0.45), TF \\gar{} increases marginally to 0.52, but PPL degrades severely ($+$36.7\\%) and training becomes unstable. Crucially, the AR gap remains 28.9--32.7$\\times$ across all settings. The training--inference gap is \\emph{independent of loss weighting}, further confirming distribution shift as the structural cause.\n\n\\subsection{Cross-Model Replication on Llama-3.1-8B}\n\\label{sec:cross_model}\n\nWe replicate the full experimental pipeline on Llama-3.1-8B (32 layers, GQA with 8 KV heads) to test architecture-generality. Table~\\ref{tab:main_gap} (bottom rows) shows that Llama exhibits the same failure pattern with amplified severity: TF \\garours{}$=$0.484, AR \\garours{}$=$0.018 (27$\\times$ gap vs.\\ Qwen's 7.8$\\times$). The gating zero-increment finding also replicates: Llama \\tg{} AR \\gar{} (0.018) is indistinguishable from \\lo{} (0.025) at the noise floor. Llama's lower base \\gar{} (0.009 vs.\\ Qwen 0.019) and more extreme NTP magnitude dominance (25.7$\\times$ vs.\\ 11.9$\\times$) likely contribute to the amplified collapse.\n\n% ============================================================\n% 6. ANALYSIS\n% ============================================================\n\\section{Analysis}\n\n\\subsection{Failure Mode Taxonomy}\n\nWe organize our findings into three failure modes that jointly explain why auxiliary attention losses trained under teacher-forcing fail at autoregressive inference.\n\n\\paragraph{NF1: Reverse turn conditioning.} Gate profile analysis reveals that 27/28 Qwen layers show gate differential (turn 1 $-$ turn 21) $< 0$: gates suppress sub-layer outputs more at early turns (where \\gar{} is naturally high) and become passive (gate $\\to$ 1.0) at late turns (where intervention is most needed). This reverse pattern arises because NTP loss increases at late turns (more context $=$ harder prediction), creating stronger gradients pushing $g \\to 1.0$ to preserve layer computation. The \\gar{} loss, with 12--26$\\times$ smaller magnitude, cannot override this pressure.\n\n\\paragraph{NF2: Structural distribution shift.} The 8--27$\\times$ gap persists across:\n\\begin{itemize}\n    \\item Gating variants: \\tg{}, \\ug{}, \\lo{} (Table~\\ref{tab:ablation})\n    \\item Gradient surgery: PCGrad v9 $\\approx$ v7 (\\S\\ref{sec:pcgrad})\n    \\item Loss weighting: $\\lambda \\in \\{0.1, 1.0, 10.0\\}$ (Table~\\ref{tab:lambda})\n    \\item Architectures: Qwen MHA, Llama GQA (\\S\\ref{sec:cross_model})\n\\end{itemize}\nNo intervention on the training side reduces the gap. The failure is structural: attention patterns optimized on gold context do not transfer to model-generated context.\n\n\\paragraph{NF3: Insufficient intervention strength.} At inference, gate values cluster near identity (mean 0.93--0.98 across layers), attenuating sub-layer outputs by only 2--7\\%. Even with $\\lambda=10.0$, the minimum gate value is 0.45. The gates lack the dynamic range to meaningfully modulate attention routing, as NTP pressure dominates the optimization landscape.\n\n\\subsection{Attention Distribution Shift Analysis}\n\\label{sec:kl}\n\nTo directly measure the distribution shift between teacher-forcing and autoregressive contexts, we compute per-head KL divergence $\\text{KL}(P_{\\text{TF}} \\| P_{\\text{AR}})$ across all 784 layer-head pairs (28 layers $\\times$ 28 heads) on Qwen-2.5-7B (Table~\\ref{tab:kl_layers}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Per-layer-group attention KL divergence (TF$\\to$AR). Deep layers show larger shift, particularly for \\tg{}.}\n\\label{tab:kl_layers}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Layer Group} & \\textbf{KL (\\tg{})} & \\textbf{KL (Base)} & \\textbf{Gate Mean} \\\\\n\\midrule\nL0--L7 (shallow) & 0.032 & 0.029 & 0.94 \\\\\nL8--L15 (mid) & 0.048 & 0.039 & 0.93 \\\\\nL16--L23 (deep-mid) & 0.065 & 0.050 & 0.92 \\\\\nL24--L27 (deep) & 0.089 & 0.068 & 0.95 \\\\\n\\midrule\nOverall mean & 0.054 & 0.043 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMean KL divergence is 0.054 nats for \\tg{} vs.\\ 0.043 for the base model. KL increases with depth, peaking at L24--L27 (0.089). \\gar{}-relevant heads (top-10\\% goal attention) show 1.5$\\times$ higher KL than non-relevant heads (0.072 vs.\\ 0.048; Table~\\ref{tab:kl_heads}), suggesting that heads responsible for goal routing are disproportionately affected by distribution shift.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{\\gar{}-relevant vs.\\ non-relevant head KL divergence. Goal-routing heads show larger but modest distribution shift.}\n\\label{tab:kl_heads}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Head Category} & \\textbf{Mean KL} & \\textbf{N heads} & \\textbf{Interpretation} \\\\\n\\midrule\n\\gar{}-relevant (top 10\\%) & 0.072 & 78 & Slightly higher shift \\\\\nNon-\\gar{}-relevant & 0.048 & 706 & Background level \\\\\nRatio & 1.50$\\times$ & --- & Weak selectivity \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nHowever, gate-KL correlation is weak and non-significant ($r=0.11$, $p=0.18$), indicating that gate values do not track the attention distribution shift. The small absolute KL (0.054) also suggests that the 8$\\times$ \\gar{} gap may involve additional compounding mechanisms (e.g., error accumulation across turns) beyond per-position attention divergence.\n\n\\subsection{Metric Specificity: Alternative \\gar{} Definitions}\n\\label{sec:alt_gar}\n\nA critical question is whether the 8$\\times$ gap is specific to our last-token \\gar{} definition or reflects a broader failure. Table~\\ref{tab:alt_gar} evaluates four token-selection definitions on Qwen-2.5-7B AR evaluation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{\\gar{} across alternative token selection definitions (AR eval, Qwen-2.5-7B). Improvement is concentrated on last-token (our training objective), with marginal improvement on all-token.}\n\\label{tab:alt_gar}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Token Selection} & \\textbf{Base} & \\textbf{\\tg{}} & \\textbf{\\ss{}} & \\textbf{SS/Base} & \\textbf{Improved?} \\\\\n\\midrule\nLast-token (ours) & 0.019 & 0.325 & 0.390 & 20.5$\\times$ & Yes \\\\\nAll-token ($\\approx$Dongre) & 0.022 & 0.025 & 0.062 & 2.8$\\times$ & Marginal \\\\\nFirst-token & 0.021 & 0.039 & 0.045 & 2.1$\\times$ & No \\\\\nGoal-only tokens & 0.015 & 0.018 & 0.030 & 2.0$\\times$ & No \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\gar{} improvement is overwhelmingly concentrated on the last-token definition that matches the training objective. All-token \\gar{} (closest to \\gardongre{}) shows only marginal improvement with \\ss{} (0.062 vs.\\ 0.022 baseline), and first-token and goal-only definitions show no improvement beyond noise. This indicates that the learned attention patterns are position-specific to the summary token, consistent with the training objective design but limiting the generality of the intervention.\n\n% ============================================================\n% 7. DISCUSSION\n% ============================================================\n\\section{Discussion}\n\n\\subsection{Attempted Mitigation: Scheduled Sampling}\n\\label{sec:ss}\n\nScheduled sampling (SS) \\citep{bengio2015scheduled} addresses exposure bias by progressively replacing gold context with model-generated text during training. We test whether SS can bridge the 8--27$\\times$ gap when applied to multi-turn attention objectives.\n\n\\paragraph{Qwen-2.5-7B: Partial success.}\nOn Qwen, SS compresses the gap substantially. Across 3 seeds (s42, s123, s456), AR \\garours{} at $\\beta=0$ reaches 0.390$\\pm$0.036 (mean$\\pm$std), reducing the gap from 7.8$\\times$ to $\\sim$1.3$\\times$ (range 1.18--1.45$\\times$) with no PPL cost (1.441$\\pm$0.001). However, seed sensitivity is notable: s42 yields 0.347 while s456 yields 0.422 (CV$=$9.2\\%).\n\nA fourth seed (s789) reveals further instability: AR \\gar{}$=$0.300, the lowest value observed, increasing the 4-seed mean to 0.367$\\pm$0.054 (CV$=$14.7\\%) and the gap range to 1.18--1.67$\\times$ (Table~\\ref{tab:ss_4seed}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{\\ss{} 4-seed comparison (Qwen-2.5-7B, AR eval). At $\\beta=0$ (no inference-time steering), the CV of 14.7\\% indicates high initialization sensitivity.}\n\\label{tab:ss_4seed}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Seed} & \\textbf{AR \\gar{} $\\beta$=0} & \\textbf{AR \\gar{} $\\beta$=3} & \\textbf{AR \\gar{} $\\beta$=5} & \\textbf{Gap} \\\\\n\\midrule\n42 & 0.347 & 0.593 & 0.717 & 1.45$\\times$ \\\\\n123 & 0.400 & 0.590 & 0.717 & 1.24$\\times$ \\\\\n456 & 0.422 & 0.605 & 0.716 & 1.18$\\times$ \\\\\n789 & 0.300 & 0.580 & 0.710 & 1.67$\\times$ \\\\\n\\midrule\nMean$\\pm$Std & 0.367$\\pm$0.054 & 0.592$\\pm$0.010 & 0.715$\\pm$0.003 & 1.39$\\pm$0.22 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nInference-time $\\beta$-steering shows much higher stability: $\\beta=3$ yields 0.592$\\pm$0.010 and $\\beta=5$ yields 0.715$\\pm$0.003 across 4 seeds, suggesting that high-$\\beta$ steering dominates the signal and SS provides diminishing independent value at higher $\\beta$.\n\n\\paragraph{Llama-3.1-8B: Complete failure.}\nOn Llama, SS fails to bridge the gap (Table~\\ref{tab:llama_ss}). Despite normal training convergence (final NTP loss 0.928, gate mean 0.92) and TF \\gar{} of 0.47 (comparable to Llama \\tg{}), AR \\gar{} at $\\beta=0$ is only 0.04---a gap of 11.75$\\times$. The SS independent benefit is $+$0.01 over the Llama \\tg{} baseline (0.030), functionally zero.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model scheduled sampling comparison ($\\beta=0$, AR eval). SS dramatically reduces the gap on Qwen but fails on Llama.}\n\\label{tab:llama_ss}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{SS TF \\gar{}} & \\textbf{SS AR \\gar{}} & \\textbf{Gap} & \\textbf{SS Benefit} \\\\\n\\midrule\nQwen (3-seed) & 0.498$\\pm$0.004 & 0.390$\\pm$0.036 & 1.28$\\times$ & $+$0.326 \\\\\nLlama & 0.470 & 0.040 & 11.75$\\times$ & $+$0.010 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Llama SS $\\beta$-sweep (AR eval, N$=$20). SS provides no incremental benefit at any $\\beta$ level; at $\\beta \\geq 3$, SS actually underperforms \\tg{} without SS.}\n\\label{tab:llama_beta}\n\\begin{tabular}{lcccc}\n\\toprule\n$\\beta$ & \\textbf{SS AR \\gar{}} & \\textbf{\\tg{} AR \\gar{}} & \\textbf{SS Increment} & \\textbf{PPL} \\\\\n\\midrule\n0 & 0.040 & 0.030 & $+$0.010 & 1.40 \\\\\n3 & 0.520 & 0.556 & $-$0.036 & 1.58 \\\\\n5 & 0.680 & 0.727 & $-$0.047 & 1.75 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt $\\beta \\geq 3$, SS actually \\emph{underperforms} \\tg{} without SS ($-$0.036 at $\\beta=3$, $-$0.047 at $\\beta=5$), suggesting that SS training interferes with the attention patterns that $\\beta$-steering exploits on Llama.\n\nThe cross-model divergence (Qwen success vs.\\ Llama failure) demonstrates that SS is \\textbf{model-specific} rather than a general mitigation. Contributing factors may include: (a)~Llama's different tokenizer (BPE 128K vs.\\ Qwen's 151K) creating larger model-generated vs.\\ gold text distribution mismatch; (b)~Llama's deeper architecture (32 vs.\\ 28 layers) requiring longer SS training to penetrate deeper layers; (c)~Llama's lower base \\gar{} (0.009 vs.\\ 0.019) providing a weaker starting signal.\n\n\\subsection{Scalability Limitations}\n\\label{sec:long_conv}\n\nWe evaluate whether SS effectiveness degrades with conversation length on Qwen-2.5-7B (Table~\\ref{tab:long_conv}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{\\gar{} by conversation length (AR eval, Qwen-2.5-7B). SS effectiveness decays sharply beyond 10 turns. \\tg{} and Base converge by 15 turns.}\n\\label{tab:long_conv}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Turns} & \\textbf{Base} & \\textbf{\\tg{}} & \\textbf{\\ss{}} & \\textbf{SS Benefit} \\\\\n\\midrule\n5 & 0.020 & 0.060 & 0.420 & $+$0.400 \\\\\n10 & 0.010 & 0.020 & 0.380 & $+$0.370 \\\\\n15 & 0.006 & 0.008 & 0.220 & $+$0.214 \\\\\n20 & 0.004 & 0.005 & 0.120 & $+$0.116 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSS maintains effectiveness up to $\\sim$10 turns (AR \\gar{} 0.38--0.42) but decays sharply thereafter: 47.6\\% decline at 15 turns, 71.4\\% at 20 turns, corresponding to $\\sim$48\\% decay per 5 additional turns beyond 10. \\tg{} without SS converges to baseline by 15 turns (0.008 vs.\\ 0.006). The decay reflects SS's fundamental limitation: its training distribution (linear mix of gold and model-generated context) diverges from the true inference distribution as error compounds super-linearly across turns. This is particularly concerning given that the motivation for \\gar{} intervention comes from Dongre et al.'s 50-turn scenarios---precisely the regime where all tested mitigations fail.\n\n\\subsection{Convergent Evidence and Implications}\n\\label{sec:convergent}\n\nOur results, combined with \\citet{dongre2026goal}'s independent goal re-injection failure, create a convergent evidence matrix:\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Convergent failure evidence. Two intervention designs $\\times$ two models $=$ four paths. Five of six intervention$\\times$model combinations fail.}\n\\label{tab:convergent}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Intervention} & \\textbf{Qwen} & \\textbf{Llama} \\\\\n\\midrule\nResidual gating (\\tg{}) & Fail (7.8$\\times$) & Fail (27$\\times$) \\\\\nScheduled sampling & Partial (1.3$\\times$) & Fail (11.75$\\times$) \\\\\nGoal re-injection (Dongre) & Fail & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFive of six tested intervention$\\times$model combinations fail to bridge the exposure bias gap. The single partial success (Qwen SS) is seed-sensitive (CV$=$14.7\\%), model-specific, and length-limited ($>$10 turns). This convergent pattern strongly suggests that lightweight training-time interventions cannot overcome the structural distribution mismatch between teacher-forcing and autoregressive generation for auxiliary attention objectives.\n\n\\subsection{Concrete Future Directions}\n\nOur failure mode taxonomy points to specific requirements for viable approaches:\n\n\\textbf{NF2 $\\to$ Inference-time intervention.} Since training-time methods cannot overcome distribution shift, inference-time approaches (activation steering, attention head masking) that operate directly on model-generated contexts bypass the exposure bias entirely.\n\n\\textbf{NF2 $\\to$ Data-dependent SS schedules.} The linear mixing schedule used in standard SS may be inadequate for multi-turn settings where error accumulation is super-linear. Curriculum-based exposure schedules that account for per-conversation difficulty could improve SS's effective range.\n\n\\textbf{NF1 $\\to$ Decoupled goal processing.} The reverse turn conditioning (NF1) arises from NTP gradient dominance. Architectures that process goal information in a pathway decoupled from the NTP objective (e.g., cross-attention to a frozen goal encoder) would avoid this failure mode.\n\n\\textbf{NF3 $\\to$ Stronger intervention mechanisms.} The 2--7\\% gate attenuation (NF3) is insufficient for meaningful modulation. Approaches with higher intervention strength---such as attention head replacement or direct attention weight modification---may overcome this limitation, though at the risk of degrading language modeling quality.\n\n% ============================================================\n% 8. CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe presented a systematic diagnostic study of why auxiliary attention losses fail under exposure bias in multi-turn dialogue. Through per-layer residual gating (\\tg{}), PCGrad ablation, $\\lambda$ sensitivity analysis, and cross-model replication on Qwen-2.5-7B and Llama-3.1-8B, we identified three failure modes: reverse turn conditioning from NTP gradient dominance (NF1), structural distribution shift creating 8--27$\\times$ training--inference gaps (NF2), and insufficient gate intervention strength (NF3). PCGrad causal exclusion provides the first empirical elimination of gradient competition for auxiliary attention losses. Attempted scheduled sampling mitigation succeeds partially on one model (Qwen, AR \\gar{}$=$0.37$\\pm$0.05) but fails on the other (Llama, AR \\gar{}$=$0.04), demonstrating model-specificity and limiting generalizability claims. Combined with independent evidence from \\citet{dongre2026goal}, our results establish that lightweight training-time interventions face fundamental barriers from exposure bias when applied to auxiliary attention objectives. The failure mode taxonomy (NF1--NF3) provides concrete constraints that future approaches must satisfy.\n\n% ============================================================\n% LIMITATIONS\n% ============================================================\n\\section*{Limitations}\n\nOur study has three main limitations. First, all experiments use auxiliary attention losses with lightweight residual gating; our negative findings may not generalize to fundamentally different attention steering approaches (e.g., direct attention weight modification, heavy architectural changes). Second, evaluation is limited to two 7--8B parameter models (Qwen-2.5-7B and Llama-3.1-8B); larger models may exhibit different gradient dynamics and exposure bias severity. Third, \\gar{} is a proxy metric for goal-tracking quality, and the correlation between \\gar{} improvement and downstream task performance remains underexplored---improvements on our last-token \\gar{} definition do not transfer to alternative token selection definitions (\\S\\ref{sec:alt_gar}), raising questions about the practical significance of the measured gaps.\n\n% ============================================================\n% REFERENCES\n% ============================================================\n\\bibliographystyle{acl_natbib}\n\\begin{thebibliography}{40}\n\n\\bibitem[Bachlechner et~al.(2021)]{bachlechner2021rezero}\nT.~Bachlechner, B.~Majumder, H.~Mao, G.~Cottrell, and J.~McAuley. 2021.\n\\newblock ReZero is all you need: Fast convergence at large depth.\n\\newblock In \\emph{UAI}.\n\n\\bibitem[Bai et~al.(2024)]{bai2024mtbench101}\nY.~Bai, J.~Liu, J.~Feng, H.~Zhang, and L.~Shang. 2024.\n\\newblock MT-Bench-101: A fine-grained benchmark for evaluating large language models in multi-turn dialogue.\n\\newblock \\emph{arXiv preprint arXiv:2402.14762}.\n\n\\bibitem[Bengio et~al.(2015)]{bengio2015scheduled}\nS.~Bengio, O.~Vinyals, N.~Jaitly, and N.~Shazeer. 2015.\n\\newblock Scheduled sampling for sequence prediction with recurrent neural networks.\n\\newblock In \\emph{NeurIPS}.\n\n\\bibitem[Ding et~al.(2023)]{ding2023enhancing}\nN.~Ding, Y.~Chen, B.~Xu, Y.~Qin, Z.~Zheng, S.~Hu, Z.~Liu, M.~Sun, and B.~Zhou. 2023.\n\\newblock Enhancing chat language models by scaling high-quality instructional conversations.\n\\newblock \\emph{arXiv preprint arXiv:2305.14233}.\n\n\\bibitem[Dongre et~al.(2026)]{dongre2026goal}\nA.~Dongre, et~al. 2026.\n\\newblock Goal accessibility ratio: Measuring attention degradation in multi-turn dialogue.\n\\newblock In \\emph{Proceedings of NAACL 2026}.\n\n\\bibitem[Dou and Gales(2022)]{dou2022parallel}\nZ.~Dou and M.~Gales. 2022.\n\\newblock Parallel attention forcing for machine translation.\n\\newblock In \\emph{EMNLP}.\n\n\\bibitem[Dubey et~al.(2024)]{dubey2024llama3}\nA.~Dubey et~al. 2024.\n\\newblock The Llama 3 herd of models.\n\\newblock \\emph{arXiv preprint arXiv:2407.21783}.\n\n\\bibitem[Elhage et~al.(2021)]{elhage2021mathematical}\nN.~Elhage, N.~Nanda, C.~Olsson, et~al. 2021.\n\\newblock A mathematical framework for transformer circuits.\n\\newblock \\emph{Transformer Circuits Thread}.\n\n\\bibitem[Fan et~al.(2020)]{fan2020layerdrop}\nA.~Fan, E.~Grave, and A.~Joulin. 2020.\n\\newblock Reducing transformer depth on demand with structured dropout.\n\\newblock In \\emph{ICLR}.\n\n\\bibitem[Ghader and Monz(2017)]{ghader2017does}\nH.~Ghader and C.~Monz. 2017.\n\\newblock What does attention in neural machine translation pay attention to?\n\\newblock In \\emph{IJCNLP}.\n\n\\bibitem[Gromov et~al.(2024)]{gromov2024unreasonable}\nA.~Gromov, K.~Tirumala, H.~Shapourian, P.~Glorioso, and D.~Roberts. 2024.\n\\newblock The unreasonable ineffectiveness of the deeper layers.\n\\newblock \\emph{arXiv preprint arXiv:2403.17887}.\n\n\\bibitem[Hsieh et~al.(2024)]{hsieh2024ruler}\nC.~Hsieh, S.~Li, C.~Yeh, H.~Hajishirzi, and W.~Chen. 2024.\n\\newblock RULER: What's the real context size of your long-context language models?\n\\newblock \\emph{arXiv preprint arXiv:2404.06654}.\n\n\\bibitem[Ko et~al.(2024)]{ko2024multichallenge}\nH.~Ko, J.~Yang, J.~Kim, and S.~Yun. 2024.\n\\newblock MultiChallenge: A realistic multi-turn dialogue benchmark.\n\\newblock \\emph{arXiv preprint arXiv:2410.00000}.\n\n\\bibitem[Lamb et~al.(2016)]{lamb2016professor}\nA.~Lamb, A.~Goyal, Y.~Zhang, S.~Zhang, A.~Courville, and Y.~Bengio. 2016.\n\\newblock Professor forcing: A new algorithm for training recurrent networks.\n\\newblock In \\emph{NeurIPS}.\n\n\\bibitem[Leblond et~al.(2018)]{leblond2018searnn}\nR.~Leblond, J.~Alayrac, L.~Sifre, M.~Pislar, J.~Lespiau, I.~Antonoglou, K.~Simonyan, and O.~Vinyals. 2018.\n\\newblock {SEARNN}: Training RNNs with global-local losses.\n\\newblock In \\emph{ICLR}.\n\n\\bibitem[Li et~al.(2024)]{li2024inference}\nK.~Li, O.~Patel, F.~Vi{\\'e}gas, H.~Pfister, and M.~Wattenberg. 2024.\n\\newblock Inference-time intervention: Eliciting truthful answers from a language model.\n\\newblock In \\emph{NeurIPS}.\n\n\\bibitem[Liu et~al.(2024)]{liu2024lost}\nN.~Liu, K.~Lin, J.~Hewitt, A.~Paranjape, M.~Bevilacqua, F.~Petroni, and P.~Liang. 2024.\n\\newblock Lost in the middle: How language models use long contexts.\n\\newblock \\emph{TACL}.\n\n\\bibitem[Liu et~al.(2021)]{liu2021conflict}\nB.~Liu, X.~Liu, X.~Jin, P.~Stone, and Q.~Liu. 2021.\n\\newblock Conflict-averse gradient descent for multi-task learning.\n\\newblock In \\emph{NeurIPS}.\n\n\\bibitem[Luo et~al.(2025)]{luo2025flexidepth}\nH.~Luo, et~al. 2025.\n\\newblock FlexiDepth: Learning to flexibly select layer depth for inference.\n\\newblock \\emph{arXiv preprint arXiv:2501.00000}.\n\n\\bibitem[Michel et~al.(2019)]{michel2019sixteen}\nP.~Michel, O.~Levy, and G.~Neubig. 2019.\n\\newblock Are sixteen heads really better than one?\n\\newblock In \\emph{NeurIPS}.\n\n\\bibitem[Navon et~al.(2022)]{navon2022multi}\nA.~Navon, A.~Shamsian, I.~Achituve, H.~Maron, K.~Kawaguchi, G.~Chechik, and E.~Fetaya. 2022.\n\\newblock Multi-task learning as a bargaining game.\n\\newblock In \\emph{ICML}.\n\n\\bibitem[Qin et~al.(2024)]{qin2024infobench}\nY.~Qin, et~al. 2024.\n\\newblock InfoBench: Evaluating instruction following ability of language models.\n\\newblock \\emph{arXiv preprint arXiv:2401.03601}.\n\n\\bibitem[Qiu et~al.(2025)]{qiu2025gated}\nY.~Qiu, et~al. 2025.\n\\newblock Gated attention for efficient transformer processing.\n\\newblock \\emph{arXiv preprint}.\n\n\\bibitem[Qwen Team(2025)]{qwen2025qwen25}\nQwen Team. 2025.\n\\newblock Qwen2.5 technical report.\n\\newblock \\emph{arXiv preprint arXiv:2412.15115}.\n\n\\bibitem[Ranzato et~al.(2016)]{ranzato2016sequence}\nM.~Ranzato, S.~Chopra, M.~Auli, and W.~Zaremba. 2016.\n\\newblock Sequence level training with recurrent neural networks.\n\\newblock In \\emph{ICLR}.\n\n\\bibitem[Schuster et~al.(2022)]{schuster2022confident}\nT.~Schuster, A.~Fisch, J.~Gupta, M.~Dehghani, D.~Bahri, V.~Tran, Y.~Tay, and D.~Metzler. 2022.\n\\newblock Confident adaptive language modeling.\n\\newblock In \\emph{NeurIPS}.\n\n\\bibitem[Strubell et~al.(2018)]{strubell2018linguistically}\nE.~Strubell, P.~Verga, D.~Belanger, and A.~McCallum. 2018.\n\\newblock Linguistically-informed self-attention for semantic role labeling.\n\\newblock In \\emph{EMNLP}.\n\n\\bibitem[Sun et~al.(2025)]{sun2025massive}\nZ.~Sun, et~al. 2025.\n\\newblock A massive-scale study of attention and transformer depth.\n\\newblock \\emph{arXiv preprint}.\n\n\\bibitem[Turner et~al.(2023)]{turner2023activation}\nA.~Turner, L.~Thiergart, D.~Udell, G.~Leech, U.~Mini, and M.~MacDiarmid. 2023.\n\\newblock Activation addition: Steering language models without optimization.\n\\newblock \\emph{arXiv preprint arXiv:2308.10248}.\n\n\\bibitem[Voita et~al.(2019)]{voita2019analyzing}\nE.~Voita, D.~Talbot, F.~Moiseev, R.~Sennrich, and I.~Titov. 2019.\n\\newblock Analyzing multi-head self-attention: Specialized heads do the heavy lifting, the rest can be pruned.\n\\newblock In \\emph{ACL}.\n\n\\bibitem[Wiseman and Rush(2016)]{wiseman2016sequence}\nS.~Wiseman and A.~Rush. 2016.\n\\newblock Sequence-to-sequence learning as beam-search optimization.\n\\newblock In \\emph{EMNLP}.\n\n\\bibitem[Xiao et~al.(2024)]{xiao2024efficient}\nG.~Xiao, Y.~Tian, B.~Chen, S.~Han, and M.~Lewis. 2024.\n\\newblock Efficient streaming language models with attention sinks.\n\\newblock In \\emph{ICLR}.\n\n\\bibitem[Yu et~al.(2020)]{yu2020gradient}\nT.~Yu, S.~Kumar, A.~Gupta, S.~Levine, K.~Hausman, and C.~Finn. 2020.\n\\newblock Gradient surgery for multi-task learning.\n\\newblock In \\emph{NeurIPS}.\n\n\\end{thebibliography}\n\n% ============================================================\n% APPENDIX\n% ============================================================\n\\appendix\n\n\\section{Expanded TF Evaluation (N$=$200)}\n\\label{app:expanded_eval}\n\nWe expand TF evaluation from 50 to 200 conversations (UltraChat idx$\\geq$7000) to tighten bootstrap confidence intervals (Table~\\ref{tab:expanded_eval}). AR evaluation is maintained at N$=$50 since the effect size is extreme and additional power is unnecessary.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{TF Eval: N$=$50 vs.\\ N$=$200 comparison on Qwen-2.5-7B. Expanded evaluation confirms zero gating increment with tighter confidence intervals.}\n\\label{tab:expanded_eval}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Variant} & \\textbf{\\gar{} (N=50)} & \\textbf{\\gar{} (N=200)} & \\textbf{95\\% CI} & \\textbf{PPL} \\\\\n\\midrule\n\\tg{} v7 & 0.504 & 0.501 & [0.488, 0.514] & 2.78 \\\\\n\\lo{} & 0.498 & 0.497 & [0.484, 0.510] & 2.78 \\\\\n\\ug{} & 0.505 & 0.503 & [0.490, 0.516] & 2.78 \\\\\nBase & 0.013 & 0.013 & [0.010, 0.016] & 4.34 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nPairwise differences with N$=$200 (Table~\\ref{tab:pairwise_n200}) confirm all confidence intervals contain zero, statistically establishing the gating zero-increment finding.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Pairwise differences (N$=$200, 95\\% bootstrap CI). All intervals contain zero.}\n\\label{tab:pairwise_n200}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Comparison} & \\textbf{Mean Diff} & \\textbf{95\\% CI} & \\textbf{Contains 0?} \\\\\n\\midrule\nTG $-$ LO & $+$0.004 & [$-$0.008, $+$0.016] & Yes \\\\\nUG $-$ LO & $+$0.006 & [$-$0.006, $+$0.018] & Yes \\\\\nTG $-$ UG & $-$0.002 & [$-$0.014, $+$0.010] & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{$\\lambda_{\\text{GAR}}$ Sensitivity Details}\n\\label{app:lambda}\n\nAt $\\lambda=10.0$, training exhibits loss oscillation. The gate distribution shifts substantially: mean drops to 0.82 (vs.\\ 0.95 at $\\lambda=1.0$), minimum reaches 0.45, and standard deviation increases to 0.12. Despite gates learning to deviate further from identity, TF \\garours{} improves only marginally (0.52 vs.\\ 0.50), while NTP PPL degrades by 36.7\\% (3.80 vs.\\ 2.78). The AR \\garours{} of 0.018 remains at the noise floor, confirming that the distribution shift gap is independent of how aggressively the training objective pushes gate values.\n\nAt $\\lambda=0.1$, the \\gar{} loss (0.0003) is negligible relative to NTP. Gates freeze near identity (std$=$0.01), and the variant is functionally equivalent to \\lo{}: same PPL (2.78), comparable TF \\gar{} (0.49), and identical AR collapse.\n\n\\section{SS Effectiveness Decay by Conversation Length}\n\\label{app:long_conv}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{SS effectiveness decay analysis. Percentage decline is relative to the 5-turn baseline.}\n\\label{tab:ss_decay}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Turn Range} & \\textbf{SS AR \\gar{}} & $\\Delta$ \\textbf{from 5 turns} & \\textbf{Decay (\\%)} \\\\\n\\midrule\n1--5 & 0.420 & --- & --- \\\\\n6--10 & 0.380 & $-$0.040 & 9.5 \\\\\n11--15 & 0.220 & $-$0.200 & 47.6 \\\\\n16--20 & 0.120 & $-$0.300 & 71.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe $\\sim$48\\% per-5-turn decay rate beyond 10 turns reflects the mismatch between SS's linear context mixing schedule and the super-linear error accumulation in long autoregressive generation. N$=$10 long conversations were evaluated; tokens per conversation range from 8,000 to 12,000.\n\n\\section{Llama TF Evaluation Comparison}\n\\label{app:llama_tf}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Llama-3.1-8B TF evaluation. SS achieves notably higher \\gardongre{} (0.350 vs.\\ \\tg{}'s 0.018), but this does not transfer to AR evaluation.}\n\\label{tab:llama_tf}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Variant} & \\textbf{\\garours{}} & \\textbf{\\gardongre{}} & \\textbf{PPL} \\\\\n\\midrule\nBase & 0.017 & 0.004 & 3.45 \\\\\n\\tg{} v7 & 0.484 & 0.018 & 2.57 \\\\\n\\ss{} & 0.470 & 0.350 & 2.60 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dca75964-585b-41b5-b163-1f722fe87f6d",
  "isSidechain": false,
  "requestId": "req_011CbM7pdcyYweJZpJcN68iz",
  "type": "assistant",
  "uuid": "7e960bad-baca-464f-bfb1-cefdfe05e6dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AH1yqfshPf6uGQ2t1MyiMb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2085,
      "cache_read_input_tokens": 51917,
      "output_tokens": 17838,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2085,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17838,
          "cache_read_input_tokens": 51917,
          "cache_creation_input_tokens": 2085,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2085
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

_source line 32 · 2026-05-24T09:04:26.476Z_

<details><summary>↩ Tool result · `toolu_01Jhv9uvafnUBijKYmYd1zxK`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e960bad-baca-464f-bfb1-cefdfe05e6dd",
  "isSidechain": false,
  "promptId": "4e9b6b3b-bc11-45d7-a0d2-4aaa1c0c9272",
  "type": "user",
  "uuid": "f600125f-0016-4eda-90e3-8b5ff4418fd9",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{url}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{natbib}\n\\usepackage{subcaption}\n\n\\newcommand{\\gar}{\\textsc{GAR}}\n\\newcommand{\\garours}{\\textsc{GAR}\\textsubscript{ours}}\n\\newcommand{\\gardongre}{\\textsc{GAR}\\textsubscript{Dongre}}\n\\newcommand{\\tg}{\\textsc{ThreadGate}}\n\\newcommand{\\ug}{\\textsc{UniformGate}}\n\\newcommand{\\lo}{\\textsc{LoRA-only}}\n\\renewcommand{\\ss}{\\textsc{SS}}\n\n\\title{Why Auxiliary Attention Losses Fail Under Exposure Bias:\\\\A Multi-Model Diagnostic Study}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nMulti-turn dialogue models progressively lose attention to user goals as conversations grow longer. Prior work shows goal information persists in residual streams (probe AUC$=$0.98) even as attention access declines, motivating learnable residual gating. We implement this as \\tg{}, a per-layer gating module trained with an auxiliary Goal Accessibility Ratio (\\gar{}) loss. \\tg{} optimizes \\gar{} under teacher-forcing (TF \\gar{}$=$0.50) but collapses on model-generated text (AR \\gar{}$=$0.064 on Qwen-2.5-7B, 0.018 on Llama-3.1-8B), revealing an 8--27$\\times$ training--inference gap. Through PCGrad ablation, $\\lambda$ sensitivity analysis, and cross-model replication, we causally exclude gradient competition and isolate exposure bias as the root cause. We identify three failure modes: (NF1) reverse turn conditioning from NTP gradient dominance, (NF2) structural distribution shift independent of loss design, and (NF3) insufficient gate intervention strength (2--7\\%). Attempted scheduled sampling mitigation succeeds partially on Qwen (AR \\gar{}$=$0.39$\\pm$0.04, 3-seed) but fails on Llama (AR \\gar{}$=$0.04, gap 11.75$\\times$), demonstrating model-specificity. Our negative results establish concrete failure modes that future work must overcome to make auxiliary attention losses viable under autoregressive generation.\n\\end{abstract}\n\n% ============================================================\n% 1. INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nLarge language models exhibit progressive degradation in multi-turn dialogue: as conversations grow longer, models fail to maintain attention to the user's original goals \\citep{dongre2026goal,liu2024lost,hsieh2024ruler}. \\citet{dongre2026goal} formalized this through the Goal Accessibility Ratio (\\gar{}), demonstrating 27--48\\% declines across 12 models over 50 turns.\n\nA key observation from \\citet{dongre2026goal} is that goal information \\emph{persists} in the residual stream even as attention degrades: linear probes achieve AUC$=$0.98 at late layers. This creates a natural hypothesis: if goal information survives in representations but attention fails to route it, a learnable gate on the residual connection should recover goal accessibility. We test this hypothesis systematically.\n\nWe implement \\tg{}, a per-layer gating module trained jointly with next-token prediction (NTP) and a \\gar{} auxiliary loss. Under teacher-forcing, \\tg{} raises \\gar{} from 0.02 to 0.50. However, on model-generated text, \\gar{} collapses to 0.064 on Qwen-2.5-7B (7.8$\\times$ gap) and 0.018 on Llama-3.1-8B (27$\\times$ gap). This dramatic training--inference discrepancy---rather than any particular fix---is our central finding.\n\nThrough systematic causal analysis, we establish three failure modes that jointly explain the collapse:\n\\begin{itemize}\n    \\item \\textbf{NF1 (Reverse turn conditioning):} NTP gradients dominate gate parameters (magnitude ratio 12--25$\\times$), causing 27/28 layers to learn reversed turn-dependent gating that suppresses at early turns (where \\gar{} is high) and becomes passive at late turns (where intervention is needed).\n    \\item \\textbf{NF2 (Structural distribution shift):} The 8--27$\\times$ gap persists across all training variants (ThreadGate, PCGrad, UniformGate, LoRA-only), loss weightings ($\\lambda \\in \\{0.1, 1.0, 10.0\\}$), and architectures (Qwen MHA, Llama GQA), confirming exposure bias as the structural root cause.\n    \\item \\textbf{NF3 (Insufficient intervention strength):} At inference, gates attenuate sub-layer outputs by only 2--7\\% (gate mean 0.93--0.98), providing negligible modulation.\n\\end{itemize}\n\nPCGrad ablation \\citep{yu2020gradient} eliminates gradient direction conflicts without reducing the gap, providing the first empirical elimination of the gradient conflict hypothesis for auxiliary attention losses. Cross-model replication on Llama-3.1-8B confirms the failure pattern is architecture-general, with even more severe collapse (27$\\times$ gap).\n\nCombined with \\citet{dongre2026goal}'s independent failure of goal re-injection, our results reveal convergent evidence: two independent intervention routes (goal re-injection and residual gating) $\\times$ two models $=$~four paths, all failing to bridge the exposure bias gap. Our negative results establish concrete failure modes that future work must overcome.\n\n\\paragraph{Contributions.}\n\\begin{enumerate}\n    \\item A failure mode taxonomy (NF1--NF3) for auxiliary attention losses under exposure bias, providing the first systematic characterization of how teacher-forcing distribution shift destroys learned attention patterns (8--27$\\times$ gap).\n    \\item The first empirical elimination of gradient competition as a causal factor: PCGrad removes direction conflicts with no effect on any observable metric (GAR, PPL, NTP loss).\n    \\item Cross-model validation on Qwen-2.5-7B (MHA) and Llama-3.1-8B (GQA) establishing architecture-generality of the failure.\n    \\item Convergent evidence across two independent intervention designs and two models, narrowing the space of viable future approaches.\n\\end{enumerate}\n\n% ============================================================\n% 2. RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Multi-turn dialogue degradation.}\nGoal-tracking in long conversations has been studied through instruction retention \\citep{qin2024infobench,dongre2026goal}, context utilization \\citep{liu2024lost,hsieh2024ruler}, and dialogue coherence \\citep{ko2024multichallenge}. \\citet{dongre2026goal} provide the most systematic analysis, defining \\gar{} and demonstrating degradation across 12 models. MT-Bench-101 \\citep{bai2024mtbench101} similarly evaluates multi-turn capabilities.\n\n\\paragraph{Residual gating and adaptive depth.}\nLearnable gates on residual connections have been explored for adaptive computation: LayerDrop \\citep{fan2020layerdrop}, early exit \\citep{schuster2022confident}, and layer-wise scaling \\citep{bachlechner2021rezero}. FlexiDepth \\citep{luo2025flexidepth} learns layer selection, while \\citet{gromov2024unreasonable} show many layers are prunable. Our gating formulation follows the ReZero parameterization $x + g \\cdot f(x)$ but applies it to auxiliary attention objectives rather than efficiency.\n\n\\paragraph{Attention steering and intervention.}\nAttention intervention techniques include attention head pruning \\citep{voita2019analyzing,michel2019sixteen}, activation steering \\citep{li2024inference,turner2023activation}, and attention loss regularization \\citep{ghader2017does,strubell2018linguistically}. \\citet{qiu2025gated} propose gated attention for selective processing. The key distinction of our work is diagnosing \\emph{why} attention-based auxiliary losses fail at inference rather than proposing new interventions.\n\n\\paragraph{Exposure bias in sequence models.}\nExposure bias---the mismatch between teacher-forced training and autoregressive inference---is well-documented \\citep{ranzato2016sequence,wiseman2016sequence,bengio2015scheduled}. Mitigation approaches include scheduled sampling \\citep{bengio2015scheduled}, Professor Forcing \\citep{lamb2016professor}, SEARNN \\citep{leblond2018searnn}, and parallel attention forcing \\citep{dou2022parallel}. While exposure bias has been extensively studied for generation quality, its impact on \\emph{auxiliary attention losses} has not been characterized.\n\n\\paragraph{Gradient conflicts in multi-task learning.}\nPCGrad \\citep{yu2020gradient}, CAGrad \\citep{liu2021conflict}, and Nash-MTL \\citep{navon2022multi} address gradient conflicts in multi-objective optimization. We use PCGrad specifically as a \\emph{diagnostic tool}: by eliminating gradient direction conflicts and observing no change in outcomes, we causally exclude this mechanism.\n\n% ============================================================\n% 3. BACKGROUND\n% ============================================================\n\\section{Background}\n\n\\subsection{Goal Accessibility Ratio}\n\nThe Goal Accessibility Ratio (\\gar{}) \\citep{dongre2026goal} measures how strongly attention heads attend to goal-relevant tokens from response positions. We use two variants:\n\n\\textbf{\\garours{}} computes attention from the \\emph{last token} of each assistant turn to all goal tokens (system prompt + first user query). The last token serves as a summary position where the model aggregates context for next-token prediction.\n\n\\textbf{\\gardongre{}} computes attention from \\emph{all response tokens} to system prompt task tokens, following the original definition.\n\n\\subsection{Residual Stream Persistence}\n\n\\citet{dongre2026goal} demonstrated that goal information persists in residual stream representations (linear probe AUC$=$0.98) even as attention-based \\gar{} declines. This dissociation motivates architectural interventions on the residual connection: if information exists but attention cannot access it, modulating the residual pathway should help.\n\n% ============================================================\n% 4. METHOD\n% ============================================================\n\\section{Method}\n\n\\subsection{ThreadGate Architecture}\n\n\\tg{} adds a learnable gate $g_l \\in (0,1)$ to each transformer layer $l$, modulating the sub-layer output via a ReZero-style \\citep{bachlechner2021rezero} residual connection:\n\\begin{equation}\n    x_{l+1} = x_l + g_l \\cdot f_l(x_l)\n\\end{equation}\nwhere $f_l$ denotes the $l$-th transformer block (attention + FFN). When $g_l \\to 0$, the layer becomes a no-op (identity); when $g_l \\to 1$, the layer operates normally.\n\nEach gate is parameterized by a 2-layer MLP that receives the hidden state projection and turn-position embeddings:\n\\begin{equation}\n    g_l = \\sigma\\big(W_2 \\cdot \\text{ReLU}(W_1 \\cdot [\\text{proj}(x_l); \\text{emb}(t_d, t_i)] + b_1) + b_2\\big)\n\\end{equation}\nwhere $t_d$ is the turn distance from the current position and $t_i$ is the absolute turn index. The gate produces per-token, per-layer scalar values.\n\n\\textbf{UniformGate (\\ug{})} uses the same architecture but replaces turn embeddings with a constant vector, yielding content-dependent but turn-agnostic gating. This ablation isolates whether turn conditioning contributes to the failure.\n\n\\textbf{LoRA-only (\\lo{})} fixes $g=1.0$ (no gating mechanism) while retaining the \\gar{} auxiliary loss, isolating the contribution of gating itself versus the auxiliary loss signal.\n\n\\subsection{Training Objective}\n\nThe total loss combines NTP and \\gar{} objectives:\n\\begin{equation}\n    \\mathcal{L} = \\mathcal{L}_{\\text{NTP}} + \\lambda_{\\text{GAR}} \\cdot \\mathcal{L}_{\\text{GAR}} + \\lambda_{\\text{div}} \\cdot \\mathcal{L}_{\\text{div}}\n\\end{equation}\n\n$\\mathcal{L}_{\\text{GAR}}$ uses MSE to push gate-modulated attention toward target \\gar{} values. $\\mathcal{L}_{\\text{div}}$ is a gate diversity regularizer preventing all gates from collapsing to the same value. We set $\\lambda_{\\text{GAR}} = 1.0$ and $\\lambda_{\\text{div}} = 0.1$ by default (v7 configuration), selected after iterating through cumulative (v1--v2), maximize (v3--v5), smooth saturation (v6), and MSE target (v7) loss designs.\n\n\\subsection{Training Setup}\n\nAll experiments fine-tune with LoRA ($r=16$, $\\alpha=32$) on UltraChat \\citep{ding2023enhancing}. Qwen-2.5-7B \\citep{qwen2025qwen25} and Llama-3.1-8B \\citep{dubey2024llama3} serve as base models. Training runs for 3 epochs with batch size 4 and learning rate $2\\times10^{-4}$.\n\n% ============================================================\n% 5. EXPERIMENTS\n% ============================================================\n\\section{Experiments}\n\n\\subsection{Evaluation Protocol}\n\nWe evaluate under two regimes:\n\n\\textbf{Teacher-forcing (TF):} Model processes gold conversation text. \\gar{} is computed from attention patterns over ground-truth contexts.\n\n\\textbf{Autoregressive (AR):} Model generates responses given only the conversation history. \\gar{} is computed from attention over model-generated text. The $\\beta$-steering parameter scales gate values at inference: $g'_l = \\min(1, \\beta \\cdot g_l)$, with $\\beta=0$ (gates disabled, pure LoRA) as the default AR evaluation setting.\n\nWe report \\garours{} (last-token to goals) as the primary metric and \\gardongre{} (all-token) for cross-study comparison. Perplexity (PPL) measured on held-out data monitors language modeling quality.\n\n\\subsection{Main Result: The Training--Inference Gap}\n\\label{sec:main_result}\n\nTable~\\ref{tab:main_gap} presents our central finding. \\tg{} achieves TF \\garours{}$=$0.50 on Qwen-2.5-7B, a 25$\\times$ improvement over the base model (0.02). However, AR evaluation with gates disabled ($\\beta=0$) yields \\garours{}$=$0.064---a 7.8$\\times$ training--inference gap. On Llama-3.1-8B, the collapse is even more severe: TF \\garours{}$=$0.484, AR \\garours{}$=$0.018, a 27$\\times$ gap.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Training--inference gap across models. TF \\gar{} is evaluated on gold text; AR \\gar{} on model-generated text ($\\beta=0$). Gap ratio $=$ TF/AR.}\n\\label{tab:main_gap}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{TF \\garours{}} & \\textbf{AR \\garours{}} & \\textbf{Gap} & \\textbf{PPL} \\\\\n\\midrule\nQwen Base & 0.013 & 0.019 & 0.7$\\times$ & 4.34 \\\\\nQwen \\tg{} v7 & 0.501 & 0.064 & 7.8$\\times$ & 2.78 \\\\\nLlama Base & 0.017 & 0.009 & 1.9$\\times$ & 3.45 \\\\\nLlama \\tg{} v7 & 0.484 & 0.018 & 27$\\times$ & 2.57 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe base models show no meaningful gap (TF$\\approx$AR$\\approx$0.01--0.02), confirming that the gap is introduced by the auxiliary \\gar{} loss training rather than being inherent to autoregressive generation.\n\n\\subsection{Four-Way Ablation: Gating Provides Zero Increment}\n\\label{sec:ablation}\n\nTo isolate the source of failure, we compare four training variants on Qwen-2.5-7B with expanded evaluation (N$=$200 conversations for TF, N$=$50 for AR):\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Four-way ablation (Qwen-2.5-7B). TF eval N$=$200 with 95\\% bootstrap CI. All fine-tuned variants include the \\gar{} auxiliary loss; the ablation tests gating mechanism contribution.}\n\\label{tab:ablation}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Variant} & \\textbf{TF \\garours{}} & \\textbf{95\\% CI} & \\textbf{AR \\garours{}} & \\textbf{PPL} \\\\\n\\midrule\nBase & 0.013 & [0.010, 0.016] & 0.019 & 4.34 \\\\\n\\lo{} & 0.497 & [0.484, 0.510] & 0.025 & 2.78 \\\\\n\\ug{} & 0.503 & [0.490, 0.516] & 0.015 & 2.78 \\\\\n\\tg{} v7 & 0.501 & [0.488, 0.514] & 0.016 & 2.78 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:ablation} reveals that all three fine-tuned variants achieve statistically indistinguishable TF \\gar{} ($\\sim$0.50) and identical PPL (2.78). Pairwise bootstrap comparisons confirm no significant differences: TG$-$LO $=$ $+$0.004, 95\\% CI [$-$0.008, $+$0.016]; UG$-$LO $=$ $+$0.006, 95\\% CI [$-$0.006, $+$0.018]. All confidence intervals contain zero.\n\nThis zero-increment result is devastating for the gating hypothesis: neither learned turn conditioning (\\tg{}) nor content-dependent gating (\\ug{}) provides any benefit over simply adding a \\gar{} loss to LoRA fine-tuning (\\lo{}). The gating mechanism is entirely redundant.\n\n\\subsection{PCGrad Causal Exclusion of Gradient Conflict}\n\\label{sec:pcgrad}\n\nA natural hypothesis for the failure is gradient competition: NTP and \\gar{} losses produce conflicting gradients that prevent effective gate learning. We test this by training a PCGrad variant (v9) that projects conflicting gradients to be orthogonal \\citep{yu2020gradient}.\n\n\\paragraph{Qwen gradient geometry.} On Qwen-2.5-7B, 67--79\\% of layers show negative NTP-\\gar{} cosine similarity (mild gradient conflict), with NTP magnitude dominating by 7.5--14.7$\\times$. PCGrad successfully eliminates direction conflicts: post-projection cosine similarity oscillates around zero (range [$-$0.151, $+$0.091]). However, the \\gar{} loss collapse trajectory is unchanged, and inference evaluation shows no improvement: v9 \\garours{}$=$0.0151 vs.\\ v7$=$0.0157 (difference $<$0.1 percentage points), v9 PPL$=$2.780 vs.\\ v7$=$2.784.\n\n\\paragraph{Llama gradient geometry.} On Llama-3.1-8B, the gradient geometry differs qualitatively (Table~\\ref{tab:gradient_geometry}). Mean cosine similarity is $+$0.005 (near-orthogonal, not conflicting), with only 53.1\\% of layers showing negative cosine similarity---near the 50\\% random baseline. NTP magnitude dominance is even more extreme (25.7$\\times$ median). The gradient geometry progressively shifts across epochs: cos\\_sim declines from $+$0.012 (epoch 0) to $-$0.001 (epoch 2), and negative-layer percentage rises from 50.0\\% to 56.3\\%.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model gradient geometry comparison. Llama shows near-orthogonal (not conflicting) gradients with extreme NTP magnitude dominance, contrasting Qwen's mild conflict pattern.}\n\\label{tab:gradient_geometry}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{cos\\_sim} & \\textbf{neg layers (\\%)} & \\textbf{mag ratio} & \\textbf{Pattern} \\\\\n\\midrule\nQwen-2.5-7B & $-$0.062 & 72.6 & 11.9$\\times$ & Mild conflict \\\\\nLlama-3.1-8B & $+$0.005 & 53.1 & 25.7$\\times$ & Orthogonal \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Llama per-epoch gradient statistics showing progressive drift toward orthogonality.}\n\\label{tab:llama_epochs}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Epoch} & \\textbf{cos\\_sim} & \\textbf{neg layers (\\%)} & \\textbf{mag ratio} \\\\\n\\midrule\n0 & $+$0.012 & 50.0 & 18.3$\\times$ \\\\\n1 & $+$0.003 & 53.1 & 24.1$\\times$ \\\\\n2 & $-$0.001 & 56.3 & 25.7$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe cross-model comparison strengthens the causal exclusion argument through a different path: on Qwen, PCGrad \\emph{removes} conflict with no effect; on Llama, conflict \\emph{does not exist} yet the same failure occurs. In both cases, NTP magnitude dominance (12--26$\\times$) is the consistent factor, but this dominance alone does not cause the gap---it merely ensures that gates optimize primarily for NTP rather than \\gar{}.\n\n\\subsection{$\\lambda_{\\text{GAR}}$ Sensitivity Analysis}\n\\label{sec:lambda}\n\nIf NTP magnitude dominance drives the failure, increasing $\\lambda_{\\text{GAR}}$ should help by rebalancing gradient magnitudes. Table~\\ref{tab:lambda} shows this is not the case.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{$\\lambda_{\\text{GAR}}$ sensitivity (Qwen-2.5-7B, 1 epoch). The training--inference gap persists across two orders of magnitude, confirming distribution shift independence from loss weighting.}\n\\label{tab:lambda}\n\\begin{tabular}{lccccc}\n\\toprule\n$\\lambda_{\\text{GAR}}$ & \\textbf{TF \\garours{}} & \\textbf{AR \\garours{}} & \\textbf{Gap} & \\textbf{PPL} & \\textbf{Stable?} \\\\\n\\midrule\n0.1 & 0.49 & 0.015 & 32.7$\\times$ & 2.78 & Yes \\\\\n1.0 (default) & 0.50 & 0.016 & 31.3$\\times$ & 2.78 & Yes \\\\\n10.0 & 0.52 & 0.018 & 28.9$\\times$ & 3.80 & No \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt $\\lambda=0.1$, the \\gar{} signal is too weak (loss$=$0.0003), gates freeze near identity (mean$=$0.98, std$=$0.01), and the variant is functionally equivalent to \\lo{}. At $\\lambda=10.0$, gates deviate further from identity (mean$=$0.82, min$=$0.45), TF \\gar{} increases marginally to 0.52, but PPL degrades severely ($+$36.7\\%) and training becomes unstable. Crucially, the AR gap remains 28.9--32.7$\\times$ across all settings. The training--inference gap is \\emph{independent of loss weighting}, further confirming distribution shift as the structural cause.\n\n\\subsection{Cross-Model Replication on Llama-3.1-8B}\n\\label{sec:cross_model}\n\nWe replicate the full experimental pipeline on Llama-3.1-8B (32 layers, GQA with 8 KV heads) to test architecture-generality. Table~\\ref{tab:main_gap} (bottom rows) shows that Llama exhibits the same failure pattern with amplified severity: TF \\garours{}$=$0.484, AR \\garours{}$=$0.018 (27$\\times$ gap vs.\\ Qwen's 7.8$\\times$). The gating zero-increment finding also replicates: Llama \\tg{} AR \\gar{} (0.018) is indistinguishable from \\lo{} (0.025) at the noise floor. Llama's lower base \\gar{} (0.009 vs.\\ Qwen 0.019) and more extreme NTP magnitude dominance (25.7$\\times$ vs.\\ 11.9$\\times$) likely contribute to the amplified collapse.\n\n% ============================================================\n% 6. ANALYSIS\n% ============================================================\n\\section{Analysis}\n\n\\subsection{Failure Mode Taxonomy}\n\nWe organize our findings into three failure modes that jointly explain why auxiliary attention losses trained under teacher-forcing fail at autoregressive inference.\n\n\\paragraph{NF1: Reverse turn conditioning.} Gate profile analysis reveals that 27/28 Qwen layers show gate differential (turn 1 $-$ turn 21) $< 0$: gates suppress sub-layer outputs more at early turns (where \\gar{} is naturally high) and become passive (gate $\\to$ 1.0) at late turns (where intervention is most needed). This reverse pattern arises because NTP loss increases at late turns (more context $=$ harder prediction), creating stronger gradients pushing $g \\to 1.0$ to preserve layer computation. The \\gar{} loss, with 12--26$\\times$ smaller magnitude, cannot override this pressure.\n\n\\paragraph{NF2: Structural distribution shift.} The 8--27$\\times$ gap persists across:\n\\begin{itemize}\n    \\item Gating variants: \\tg{}, \\ug{}, \\lo{} (Table~\\ref{tab:ablation})\n    \\item Gradient surgery: PCGrad v9 $\\approx$ v7 (\\S\\ref{sec:pcgrad})\n    \\item Loss weighting: $\\lambda \\in \\{0.1, 1.0, 10.0\\}$ (Table~\\ref{tab:lambda})\n    \\item Architectures: Qwen MHA, Llama GQA (\\S\\ref{sec:cross_model})\n\\end{itemize}\nNo intervention on the training side reduces the gap. The failure is structural: attention patterns optimized on gold context do not transfer to model-generated context.\n\n\\paragraph{NF3: Insufficient intervention strength.} At inference, gate values cluster near identity (mean 0.93--0.98 across layers), attenuating sub-layer outputs by only 2--7\\%. Even with $\\lambda=10.0$, the minimum gate value is 0.45. The gates lack the dynamic range to meaningfully modulate attention routing, as NTP pressure dominates the optimization landscape.\n\n\\subsection{Attention Distribution Shift Analysis}\n\\label{sec:kl}\n\nTo directly measure the distribution shift between teacher-forcing and autoregressive contexts, we compute per-head KL divergence $\\text{KL}(P_{\\text{TF}} \\| P_{\\text{AR}})$ across all 784 layer-head pairs (28 layers $\\times$ 28 heads) on Qwen-2.5-7B (Table~\\ref{tab:kl_layers}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Per-layer-group attention KL divergence (TF$\\to$AR). Deep layers show larger shift, particularly for \\tg{}.}\n\\label{tab:kl_layers}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Layer Group} & \\textbf{KL (\\tg{})} & \\textbf{KL (Base)} & \\textbf{Gate Mean} \\\\\n\\midrule\nL0--L7 (shallow) & 0.032 & 0.029 & 0.94 \\\\\nL8--L15 (mid) & 0.048 & 0.039 & 0.93 \\\\\nL16--L23 (deep-mid) & 0.065 & 0.050 & 0.92 \\\\\nL24--L27 (deep) & 0.089 & 0.068 & 0.95 \\\\\n\\midrule\nOverall mean & 0.054 & 0.043 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMean KL divergence is 0.054 nats for \\tg{} vs.\\ 0.043 for the base model. KL increases with depth, peaking at L24--L27 (0.089). \\gar{}-relevant heads (top-10\\% goal attention) show 1.5$\\times$ higher KL than non-relevant heads (0.072 vs.\\ 0.048; Table~\\ref{tab:kl_heads}), suggesting that heads responsible for goal routing are disproportionately affected by distribution shift.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{\\gar{}-relevant vs.\\ non-relevant head KL divergence. Goal-routing heads show larger but modest distribution shift.}\n\\label{tab:kl_heads}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Head Category} & \\textbf{Mean KL} & \\textbf{N heads} & \\textbf{Interpretation} \\\\\n\\midrule\n\\gar{}-relevant (top 10\\%) & 0.072 & 78 & Slightly higher shift \\\\\nNon-\\gar{}-relevant & 0.048 & 706 & Background level \\\\\nRatio & 1.50$\\times$ & --- & Weak selectivity \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nHowever, gate-KL correlation is weak and non-significant ($r=0.11$, $p=0.18$), indicating that gate values do not track the attention distribution shift. The small absolute KL (0.054) also suggests that the 8$\\times$ \\gar{} gap may involve additional compounding mechanisms (e.g., error accumulation across turns) beyond per-position attention divergence.\n\n\\subsection{Metric Specificity: Alternative \\gar{} Definitions}\n\\label{sec:alt_gar}\n\nA critical question is whether the 8$\\times$ gap is specific to our last-token \\gar{} definition or reflects a broader failure. Table~\\ref{tab:alt_gar} evaluates four token-selection definitions on Qwen-2.5-7B AR evaluation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{\\gar{} across alternative token selection definitions (AR eval, Qwen-2.5-7B). Improvement is concentrated on last-token (our training objective), with marginal improvement on all-token.}\n\\label{tab:alt_gar}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Token Selection} & \\textbf{Base} & \\textbf{\\tg{}} & \\textbf{\\ss{}} & \\textbf{SS/Base} & \\textbf{Improved?} \\\\\n\\midrule\nLast-token (ours) & 0.019 & 0.325 & 0.390 & 20.5$\\times$ & Yes \\\\\nAll-token ($\\approx$Dongre) & 0.022 & 0.025 & 0.062 & 2.8$\\times$ & Marginal \\\\\nFirst-token & 0.021 & 0.039 & 0.045 & 2.1$\\times$ & No \\\\\nGoal-only tokens & 0.015 & 0.018 & 0.030 & 2.0$\\times$ & No \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\gar{} improvement is overwhelmingly concentrated on the last-token definition that matches the training objective. All-token \\gar{} (closest to \\gardongre{}) shows only marginal improvement with \\ss{} (0.062 vs.\\ 0.022 baseline), and first-token and goal-only definitions show no improvement beyond noise. This indicates that the learned attention patterns are position-specific to the summary token, consistent with the training objective design but limiting the generality of the intervention.\n\n% ============================================================\n% 7. DISCUSSION\n% ============================================================\n\\section{Discussion}\n\n\\subsection{Attempted Mitigation: Scheduled Sampling}\n\\label{sec:ss}\n\nScheduled sampling (SS) \\citep{bengio2015scheduled} addresses exposure bias by progressively replacing gold context with model-generated text during training. We test whether SS can bridge the 8--27$\\times$ gap when applied to multi-turn attention objectives.\n\n\\paragraph{Qwen-2.5-7B: Partial success.}\nOn Qwen, SS compresses the gap substantially. Across 3 seeds (s42, s123, s456), AR \\garours{} at $\\beta=0$ reaches 0.390$\\pm$0.036 (mean$\\pm$std), reducing the gap from 7.8$\\times$ to $\\sim$1.3$\\times$ (range 1.18--1.45$\\times$) with no PPL cost (1.441$\\pm$0.001). However, seed sensitivity is notable: s42 yields 0.347 while s456 yields 0.422 (CV$=$9.2\\%).\n\nA fourth seed (s789) reveals further instability: AR \\gar{}$=$0.300, the lowest value observed, increasing the 4-seed mean to 0.367$\\pm$0.054 (CV$=$14.7\\%) and the gap range to 1.18--1.67$\\times$ (Table~\\ref{tab:ss_4seed}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{\\ss{} 4-seed comparison (Qwen-2.5-7B, AR eval). At $\\beta=0$ (no inference-time steering), the CV of 14.7\\% indicates high initialization sensitivity.}\n\\label{tab:ss_4seed}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Seed} & \\textbf{AR \\gar{} $\\beta$=0} & \\textbf{AR \\gar{} $\\beta$=3} & \\textbf{AR \\gar{} $\\beta$=5} & \\textbf{Gap} \\\\\n\\midrule\n42 & 0.347 & 0.593 & 0.717 & 1.45$\\times$ \\\\\n123 & 0.400 & 0.590 & 0.717 & 1.24$\\times$ \\\\\n456 & 0.422 & 0.605 & 0.716 & 1.18$\\times$ \\\\\n789 & 0.300 & 0.580 & 0.710 & 1.67$\\times$ \\\\\n\\midrule\nMean$\\pm$Std & 0.367$\\pm$0.054 & 0.592$\\pm$0.010 & 0.715$\\pm$0.003 & 1.39$\\pm$0.22 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nInference-time $\\beta$-steering shows much higher stability: $\\beta=3$ yields 0.592$\\pm$0.010 and $\\beta=5$ yields 0.715$\\pm$0.003 across 4 seeds, suggesting that high-$\\beta$ steering dominates the signal and SS provides diminishing independent value at higher $\\beta$.\n\n\\paragraph{Llama-3.1-8B: Complete failure.}\nOn Llama, SS fails to bridge the gap (Table~\\ref{tab:llama_ss}). Despite normal training convergence (final NTP loss 0.928, gate mean 0.92) and TF \\gar{} of 0.47 (comparable to Llama \\tg{}), AR \\gar{} at $\\beta=0$ is only 0.04---a gap of 11.75$\\times$. The SS independent benefit is $+$0.01 over the Llama \\tg{} baseline (0.030), functionally zero.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model scheduled sampling comparison ($\\beta=0$, AR eval). SS dramatically reduces the gap on Qwen but fails on Llama.}\n\\label{tab:llama_ss}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{SS TF \\gar{}} & \\textbf{SS AR \\gar{}} & \\textbf{Gap} & \\textbf{SS Benefit} \\\\\n\\midrule\nQwen (3-seed) & 0.498$\\pm$0.004 & 0.390$\\pm$0.036 & 1.28$\\times$ & $+$0.326 \\\\\nLlama & 0.470 & 0.040 & 11.75$\\times$ & $+$0.010 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Llama SS $\\beta$-sweep (AR eval, N$=$20). SS provides no incremental benefit at any $\\beta$ level; at $\\beta \\geq 3$, SS actually underperforms \\tg{} without SS.}\n\\label{tab:llama_beta}\n\\begin{tabular}{lcccc}\n\\toprule\n$\\beta$ & \\textbf{SS AR \\gar{}} & \\textbf{\\tg{} AR \\gar{}} & \\textbf{SS Increment} & \\textbf{PPL} \\\\\n\\midrule\n0 & 0.040 & 0.030 & $+$0.010 & 1.40 \\\\\n3 & 0.520 & 0.556 & $-$0.036 & 1.58 \\\\\n5 & 0.680 & 0.727 & $-$0.047 & 1.75 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt $\\beta \\geq 3$, SS actually \\emph{underperforms} \\tg{} without SS ($-$0.036 at $\\beta=3$, $-$0.047 at $\\beta=5$), suggesting that SS training interferes with the attention patterns that $\\beta$-steering exploits on Llama.\n\nThe cross-model divergence (Qwen success vs.\\ Llama failure) demonstrates that SS is \\textbf{model-specific} rather than a general mitigation. Contributing factors may include: (a)~Llama's different tokenizer (BPE 128K vs.\\ Qwen's 151K) creating larger model-generated vs.\\ gold text distribution mismatch; (b)~Llama's deeper architecture (32 vs.\\ 28 layers) requiring longer SS training to penetrate deeper layers; (c)~Llama's lower base \\gar{} (0.009 vs.\\ 0.019) providing a weaker starting signal.\n\n\\subsection{Scalability Limitations}\n\\label{sec:long_conv}\n\nWe evaluate whether SS effectiveness degrades with conversation length on Qwen-2.5-7B (Table~\\ref{tab:long_conv}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{\\gar{} by conversation length (AR eval, Qwen-2.5-7B). SS effectiveness decays sharply beyond 10 turns. \\tg{} and Base converge by 15 turns.}\n\\label{tab:long_conv}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Turns} & \\textbf{Base} & \\textbf{\\tg{}} & \\textbf{\\ss{}} & \\textbf{SS Benefit} \\\\\n\\midrule\n5 & 0.020 & 0.060 & 0.420 & $+$0.400 \\\\\n10 & 0.010 & 0.020 & 0.380 & $+$0.370 \\\\\n15 & 0.006 & 0.008 & 0.220 & $+$0.214 \\\\\n20 & 0.004 & 0.005 & 0.120 & $+$0.116 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSS maintains effectiveness up to $\\sim$10 turns (AR \\gar{} 0.38--0.42) but decays sharply thereafter: 47.6\\% decline at 15 turns, 71.4\\% at 20 turns, corresponding to $\\sim$48\\% decay per 5 additional turns beyond 10. \\tg{} without SS converges to baseline by 15 turns (0.008 vs.\\ 0.006). The decay reflects SS's fundamental limitation: its training distribution (linear mix of gold and model-generated context) diverges from the true inference distribution as error compounds super-linearly across turns. This is particularly concerning given that the motivation for \\gar{} intervention comes from Dongre et al.'s 50-turn scenarios---precisely the regime where all tested mitigations fail.\n\n\\subsection{Convergent Evidence and Implications}\n\\label{sec:convergent}\n\nOur results, combined with \\citet{dongre2026goal}'s independent goal re-injection failure, create a convergent evidence matrix:\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Convergent failure evidence. Two intervention designs $\\times$ two models $=$ four paths. Five of six intervention$\\times$model combinations fail.}\n\\label{tab:convergent}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Intervention} & \\textbf{Qwen} & \\textbf{Llama} \\\\\n\\midrule\nResidual gating (\\tg{}) & Fail (7.8$\\times$) & Fail (27$\\times$) \\\\\nScheduled sampling & Partial (1.3$\\times$) & Fail (11.75$\\times$) \\\\\nGoal re-injection (Dongre) & Fail & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFive of six tested intervention$\\times$model combinations fail to bridge the exposure bias gap. The single partial success (Qwen SS) is seed-sensitive (CV$=$14.7\\%), model-specific, and length-limited ($>$10 turns). This convergent pattern strongly suggests that lightweight training-time interventions cannot overcome the structural distribution mismatch between teacher-forcing and autoregressive generation for auxiliary attention objectives.\n\n\\subsection{Concrete Future Directions}\n\nOur failure mode taxonomy points to specific requirements for viable approaches:\n\n\\textbf{NF2 $\\to$ Inference-time intervention.} Since training-time methods cannot overcome distribution shift, inference-time approaches (activation steering, attention head masking) that operate directly on model-generated contexts bypass the exposure bias entirely.\n\n\\textbf{NF2 $\\to$ Data-dependent SS schedules.} The linear mixing schedule used in standard SS may be inadequate for multi-turn settings where error accumulation is super-linear. Curriculum-based exposure schedules that account for per-conversation difficulty could improve SS's effective range.\n\n\\textbf{NF1 $\\to$ Decoupled goal processing.} The reverse turn conditioning (NF1) arises from NTP gradient dominance. Architectures that process goal information in a pathway decoupled from the NTP objective (e.g., cross-attention to a frozen goal encoder) would avoid this failure mode.\n\n\\textbf{NF3 $\\to$ Stronger intervention mechanisms.} The 2--7\\% gate attenuation (NF3) is insufficient for meaningful modulation. Approaches with higher intervention strength---such as attention head replacement or direct attention weight modification---may overcome this limitation, though at the risk of degrading language modeling quality.\n\n% ============================================================\n% 8. CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe presented a systematic diagnostic study of why auxiliary attention losses fail under exposure bias in multi-turn dialogue. Through per-layer residual gating (\\tg{}), PCGrad ablation, $\\lambda$ sensitivity analysis, and cross-model replication on Qwen-2.5-7B and Llama-3.1-8B, we identified three failure modes: reverse turn conditioning from NTP gradient dominance (NF1), structural distribution shift creating 8--27$\\times$ training--inference gaps (NF2), and insufficient gate intervention strength (NF3). PCGrad causal exclusion provides the first empirical elimination of gradient competition for auxiliary attention losses. Attempted scheduled sampling mitigation succeeds partially on one model (Qwen, AR \\gar{}$=$0.37$\\pm$0.05) but fails on the other (Llama, AR \\gar{}$=$0.04), demonstrating model-specificity and limiting generalizability claims. Combined with independent evidence from \\citet{dongre2026goal}, our results establish that lightweight training-time interventions face fundamental barriers from exposure bias when applied to auxiliary attention objectives. The failure mode taxonomy (NF1--NF3) provides concrete constraints that future approaches must satisfy.\n\n% ============================================================\n% LIMITATIONS\n% ============================================================\n\\section*{Limitations}\n\nOur study has three main limitations. First, all experiments use auxiliary attention losses with lightweight residual gating; our negative findings may not generalize to fundamentally different attention steering approaches (e.g., direct attention weight modification, heavy architectural changes). Second, evaluation is limited to two 7--8B parameter models (Qwen-2.5-7B and Llama-3.1-8B); larger models may exhibit different gradient dynamics and exposure bias severity. Third, \\gar{} is a proxy metric for goal-tracking quality, and the correlation between \\gar{} improvement and downstream task performance remains underexplored---improvements on our last-token \\gar{} definition do not transfer to alternative token selection definitions (\\S\\ref{sec:alt_gar}), raising questions about the practical significance of the measured gaps.\n\n% ============================================================\n% REFERENCES\n% ============================================================\n\\bibliographystyle{acl_natbib}\n\\begin{thebibliography}{40}\n\n\\bibitem[Bachlechner et~al.(2021)]{bachlechner2021rezero}\nT.~Bachlechner, B.~Majumder, H.~Mao, G.~Cottrell, and J.~McAuley. 2021.\n\\newblock ReZero is all you need: Fast convergence at large depth.\n\\newblock In \\emph{UAI}.\n\n\\bibitem[Bai et~al.(2024)]{bai2024mtbench101}\nY.~Bai, J.~Liu, J.~Feng, H.~Zhang, and L.~Shang. 2024.\n\\newblock MT-Bench-101: A fine-grained benchmark for evaluating large language models in multi-turn dialogue.\n\\newblock \\emph{arXiv preprint arXiv:2402.14762}.\n\n\\bibitem[Bengio et~al.(2015)]{bengio2015scheduled}\nS.~Bengio, O.~Vinyals, N.~Jaitly, and N.~Shazeer. 2015.\n\\newblock Scheduled sampling for sequence prediction with recurrent neural networks.\n\\newblock In \\emph{NeurIPS}.\n\n\\bibitem[Ding et~al.(2023)]{ding2023enhancing}\nN.~Ding, Y.~Chen, B.~Xu, Y.~Qin, Z.~Zheng, S.~Hu, Z.~Liu, M.~Sun, and B.~Zhou. 2023.\n\\newblock Enhancing chat language models by scaling high-quality instructional conversations.\n\\newblock \\emph{arXiv preprint arXiv:2305.14233}.\n\n\\bibitem[Dongre et~al.(2026)]{dongre2026goal}\nA.~Dongre, et~al. 2026.\n\\newblock Goal accessibility ratio: Measuring attention degradation in multi-turn dialogue.\n\\newblock In \\emph{Proceedings of NAACL 2026}.\n\n\\bibitem[Dou and Gales(2022)]{dou2022parallel}\nZ.~Dou and M.~Gales. 2022.\n\\newblock Parallel attention forcing for machine translation.\n\\newblock In \\emph{EMNLP}.\n\n\\bibitem[Dubey et~al.(2024)]{dubey2024llama3}\nA.~Dubey et~al. 2024.\n\\newblock The Llama 3 herd of models.\n\\newblock \\emph{arXiv preprint arXiv:2407.21783}.\n\n\\bibitem[Elhage et~al.(2021)]{elhage2021mathematical}\nN.~Elhage, N.~Nanda, C.~Olsson, et~al. 2021.\n\\newblock A mathematical framework for transformer circuits.\n\\newblock \\emph{Transformer Circuits Thread}.\n\n\\bibitem[Fan et~al.(2020)]{fan2020layerdrop}\nA.~Fan, E.~Grave, and A.~Joulin. 2020.\n\\newblock Reducing transformer depth on demand with structured dropout.\n\\newblock In \\emph{ICLR}.\n\n\\bibitem[Ghader and Monz(2017)]{ghader2017does}\nH.~Ghader and C.~Monz. 2017.\n\\newblock What does attention in neural machine translation pay attention to?\n\\newblock In \\emph{IJCNLP}.\n\n\\bibitem[Gromov et~al.(2024)]{gromov2024unreasonable}\nA.~Gromov, K.~Tirumala, H.~Shapourian, P.~Glorioso, and D.~Roberts. 2024.\n\\newblock The unreasonable ineffectiveness of the deeper layers.\n\\newblock \\emph{arXiv preprint arXiv:2403.17887}.\n\n\\bibitem[Hsieh et~al.(2024)]{hsieh2024ruler}\nC.~Hsieh, S.~Li, C.~Yeh, H.~Hajishirzi, and W.~Chen. 2024.\n\\newblock RULER: What's the real context size of your long-context language models?\n\\newblock \\emph{arXiv preprint arXiv:2404.06654}.\n\n\\bibitem[Ko et~al.(2024)]{ko2024multichallenge}\nH.~Ko, J.~Yang, J.~Kim, and S.~Yun. 2024.\n\\newblock MultiChallenge: A realistic multi-turn dialogue benchmark.\n\\newblock \\emph{arXiv preprint arXiv:2410.00000}.\n\n\\bibitem[Lamb et~al.(2016)]{lamb2016professor}\nA.~Lamb, A.~Goyal, Y.~Zhang, S.~Zhang, A.~Courville, and Y.~Bengio. 2016.\n\\newblock Professor forcing: A new algorithm for training recurrent networks.\n\\newblock In \\emph{NeurIPS}.\n\n\\bibitem[Leblond et~al.(2018)]{leblond2018searnn}\nR.~Leblond, J.~Alayrac, L.~Sifre, M.~Pislar, J.~Lespiau, I.~Antonoglou, K.~Simonyan, and O.~Vinyals. 2018.\n\\newblock {SEARNN}: Training RNNs with global-local losses.\n\\newblock In \\emph{ICLR}.\n\n\\bibitem[Li et~al.(2024)]{li2024inference}\nK.~Li, O.~Patel, F.~Vi{\\'e}gas, H.~Pfister, and M.~Wattenberg. 2024.\n\\newblock Inference-time intervention: Eliciting truthful answers from a language model.\n\\newblock In \\emph{NeurIPS}.\n\n\\bibitem[Liu et~al.(2024)]{liu2024lost}\nN.~Liu, K.~Lin, J.~Hewitt, A.~Paranjape, M.~Bevilacqua, F.~Petroni, and P.~Liang. 2024.\n\\newblock Lost in the middle: How language models use long contexts.\n\\newblock \\emph{TACL}.\n\n\\bibitem[Liu et~al.(2021)]{liu2021conflict}\nB.~Liu, X.~Liu, X.~Jin, P.~Stone, and Q.~Liu. 2021.\n\\newblock Conflict-averse gradient descent for multi-task learning.\n\\newblock In \\emph{NeurIPS}.\n\n\\bibitem[Luo et~al.(2025)]{luo2025flexidepth}\nH.~Luo, et~al. 2025.\n\\newblock FlexiDepth: Learning to flexibly select layer depth for inference.\n\\newblock \\emph{arXiv preprint arXiv:2501.00000}.\n\n\\bibitem[Michel et~al.(2019)]{michel2019sixteen}\nP.~Michel, O.~Levy, and G.~Neubig. 2019.\n\\newblock Are sixteen heads really better than one?\n\\newblock In \\emph{NeurIPS}.\n\n\\bibitem[Navon et~al.(2022)]{navon2022multi}\nA.~Navon, A.~Shamsian, I.~Achituve, H.~Maron, K.~Kawaguchi, G.~Chechik, and E.~Fetaya. 2022.\n\\newblock Multi-task learning as a bargaining game.\n\\newblock In \\emph{ICML}.\n\n\\bibitem[Qin et~al.(2024)]{qin2024infobench}\nY.~Qin, et~al. 2024.\n\\newblock InfoBench: Evaluating instruction following ability of language models.\n\\newblock \\emph{arXiv preprint arXiv:2401.03601}.\n\n\\bibitem[Qiu et~al.(2025)]{qiu2025gated}\nY.~Qiu, et~al. 2025.\n\\newblock Gated attention for efficient transformer processing.\n\\newblock \\emph{arXiv preprint}.\n\n\\bibitem[Qwen Team(2025)]{qwen2025qwen25}\nQwen Team. 2025.\n\\newblock Qwen2.5 technical report.\n\\newblock \\emph{arXiv preprint arXiv:2412.15115}.\n\n\\bibitem[Ranzato et~al.(2016)]{ranzato2016sequence}\nM.~Ranzato, S.~Chopra, M.~Auli, and W.~Zaremba. 2016.\n\\newblock Sequence level training with recurrent neural networks.\n\\newblock In \\emph{ICLR}.\n\n\\bibitem[Schuster et~al.(2022)]{schuster2022confident}\nT.~Schuster, A.~Fisch, J.~Gupta, M.~Dehghani, D.~Bahri, V.~Tran, Y.~Tay, and D.~Metzler. 2022.\n\\newblock Confident adaptive language modeling.\n\\newblock In \\emph{NeurIPS}.\n\n\\bibitem[Strubell et~al.(2018)]{strubell2018linguistically}\nE.~Strubell, P.~Verga, D.~Belanger, and A.~McCallum. 2018.\n\\newblock Linguistically-informed self-attention for semantic role labeling.\n\\newblock In \\emph{EMNLP}.\n\n\\bibitem[Sun et~al.(2025)]{sun2025massive}\nZ.~Sun, et~al. 2025.\n\\newblock A massive-scale study of attention and transformer depth.\n\\newblock \\emph{arXiv preprint}.\n\n\\bibitem[Turner et~al.(2023)]{turner2023activation}\nA.~Turner, L.~Thiergart, D.~Udell, G.~Leech, U.~Mini, and M.~MacDiarmid. 2023.\n\\newblock Activation addition: Steering language models without optimization.\n\\newblock \\emph{arXiv preprint arXiv:2308.10248}.\n\n\\bibitem[Voita et~al.(2019)]{voita2019analyzing}\nE.~Voita, D.~Talbot, F.~Moiseev, R.~Sennrich, and I.~Titov. 2019.\n\\newblock Analyzing multi-head self-attention: Specialized heads do the heavy lifting, the rest can be pruned.\n\\newblock In \\emph{ACL}.\n\n\\bibitem[Wiseman and Rush(2016)]{wiseman2016sequence}\nS.~Wiseman and A.~Rush. 2016.\n\\newblock Sequence-to-sequence learning as beam-search optimization.\n\\newblock In \\emph{EMNLP}.\n\n\\bibitem[Xiao et~al.(2024)]{xiao2024efficient}\nG.~Xiao, Y.~Tian, B.~Chen, S.~Han, and M.~Lewis. 2024.\n\\newblock Efficient streaming language models with attention sinks.\n\\newblock In \\emph{ICLR}.\n\n\\bibitem[Yu et~al.(2020)]{yu2020gradient}\nT.~Yu, S.~Kumar, A.~Gupta, S.~Levine, K.~Hausman, and C.~Finn. 2020.\n\\newblock Gradient surgery for multi-task learning.\n\\newblock In \\emph{NeurIPS}.\n\n\\end{thebibliography}\n\n% ============================================================\n% APPENDIX\n% ============================================================\n\\appendix\n\n\\section{Expanded TF Evaluation (N$=$200)}\n\\label{app:expanded_eval}\n\nWe expand TF evaluation from 50 to 200 conversations (UltraChat idx$\\geq$7000) to tighten bootstrap confidence intervals (Table~\\ref{tab:expanded_eval}). AR evaluation is maintained at N$=$50 since the effect size is extreme and additional power is unnecessary.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{TF Eval: N$=$50 vs.\\ N$=$200 comparison on Qwen-2.5-7B. Expanded evaluation confirms zero gating increment with tighter confidence intervals.}\n\\label{tab:expanded_eval}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Variant} & \\textbf{\\gar{} (N=50)} & \\textbf{\\gar{} (N=200)} & \\textbf{95\\% CI} & \\textbf{PPL} \\\\\n\\midrule\n\\tg{} v7 & 0.504 & 0.501 & [0.488, 0.514] & 2.78 \\\\\n\\lo{} & 0.498 & 0.497 & [0.484, 0.510] & 2.78 \\\\\n\\ug{} & 0.505 & 0.503 & [0.490, 0.516] & 2.78 \\\\\nBase & 0.013 & 0.013 & [0.010, 0.016] & 4.34 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nPairwise differences with N$=$200 (Table~\\ref{tab:pairwise_n200}) confirm all confidence intervals contain zero, statistically establishing the gating zero-increment finding.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Pairwise differences (N$=$200, 95\\% bootstrap CI). All intervals contain zero.}\n\\label{tab:pairwise_n200}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Comparison} & \\textbf{Mean Diff} & \\textbf{95\\% CI} & \\textbf{Contains 0?} \\\\\n\\midrule\nTG $-$ LO & $+$0.004 & [$-$0.008, $+$0.016] & Yes \\\\\nUG $-$ LO & $+$0.006 & [$-$0.006, $+$0.018] & Yes \\\\\nTG $-$ UG & $-$0.002 & [$-$0.014, $+$0.010] & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{$\\lambda_{\\text{GAR}}$ Sensitivity Details}\n\\label{app:lambda}\n\nAt $\\lambda=10.0$, training exhibits loss oscillation. The gate distribution shifts substantially: mean drops to 0.82 (vs.\\ 0.95 at $\\lambda=1.0$), minimum reaches 0.45, and standard deviation increases to 0.12. Despite gates learning to deviate further from identity, TF \\garours{} improves only marginally (0.52 vs.\\ 0.50), while NTP PPL degrades by 36.7\\% (3.80 vs.\\ 2.78). The AR \\garours{} of 0.018 remains at the noise floor, confirming that the distribution shift gap is independent of how aggressively the training objective pushes gate values.\n\nAt $\\lambda=0.1$, the \\gar{} loss (0.0003) is negligible relative to NTP. Gates freeze near identity (std$=$0.01), and the variant is functionally equivalent to \\lo{}: same PPL (2.78), comparable TF \\gar{} (0.49), and identical AR collapse.\n\n\\section{SS Effectiveness Decay by Conversation Length}\n\\label{app:long_conv}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{SS effectiveness decay analysis. Percentage decline is relative to the 5-turn baseline.}\n\\label{tab:ss_decay}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Turn Range} & \\textbf{SS AR \\gar{}} & $\\Delta$ \\textbf{from 5 turns} & \\textbf{Decay (\\%)} \\\\\n\\midrule\n1--5 & 0.420 & --- & --- \\\\\n6--10 & 0.380 & $-$0.040 & 9.5 \\\\\n11--15 & 0.220 & $-$0.200 & 47.6 \\\\\n16--20 & 0.120 & $-$0.300 & 71.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe $\\sim$48\\% per-5-turn decay rate beyond 10 turns reflects the mismatch between SS's linear context mixing schedule and the super-linear error accumulation in long autoregressive generation. N$=$10 long conversations were evaluated; tokens per conversation range from 8,000 to 12,000.\n\n\\section{Llama TF Evaluation Comparison}\n\\label{app:llama_tf}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Llama-3.1-8B TF evaluation. SS achieves notably higher \\gardongre{} (0.350 vs.\\ \\tg{}'s 0.018), but this does not transfer to AR evaluation.}\n\\label{tab:llama_tf}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Variant} & \\textbf{\\garours{}} & \\textbf{\\gardongre{}} & \\textbf{PPL} \\\\\n\\midrule\nBase & 0.017 & 0.004 & 3.45 \\\\\n\\tg{} v7 & 0.484 & 0.018 & 2.57 \\\\\n\\ss{} & 0.470 & 0.350 & 2.60 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "7e960bad-baca-464f-bfb1-cefdfe05e6dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 33 · 2026-05-24T09:04:26.483Z_

```json
{
  "parentUuid": "f600125f-0016-4eda-90e3-8b5ff4418fd9",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "776dcf33-ea47-465c-83d4-097f686e7c97",
  "timestamp": "2026-05-24T09:04:26.483Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260524T081135 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_ga…",
  "leafUuid": "776dcf33-ea47-465c-83d4-097f686e7c97",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier diagnostic paper for dream_20260524T081135",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1"
}
```

---

### Assistant

_source line 36 · 2026-05-24T09:04:29.563Z_

Now compiling the LaTeX.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "776dcf33-ea47-465c-83d4-097f686e7c97",
  "isSidechain": false,
  "requestId": "req_011CbM8F5tTLUmVQonnKPt4W",
  "type": "assistant",
  "uuid": "969de150-4ec8-4165-a3d6-ff4b3bdc0ae0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011rJoRTqUhevSXXijNAnZKX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18007,
      "cache_read_input_tokens": 54002,
      "output_tokens": 152,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18007,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 152,
          "cache_read_input_tokens": 54002,
          "cache_creation_input_tokens": 18007,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18007
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

_source line 37 · 2026-05-24T09:04:30.804Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Rao88tFAfMF2MrcFyXsbs1`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "First pdflatex pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "969de150-4ec8-4165-a3d6-ff4b3bdc0ae0",
  "isSidechain": false,
  "requestId": "req_011CbM8F5tTLUmVQonnKPt4W",
  "type": "assistant",
  "uuid": "99c9b574-10fa-4cba-9957-e23d111d5c1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011rJoRTqUhevSXXijNAnZKX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18007,
      "cache_read_input_tokens": 54002,
      "output_tokens": 152,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18007,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 152,
          "cache_read_input_tokens": 54002,
          "cache_creation_input_tokens": 18007,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18007
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

_source line 38 · 2026-05-24T09:04:31.601Z_

<details><summary>↩ Tool result · `toolu_01Rao88tFAfMF2MrcFyXsbs1`</summary>

```text
[14] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/us
r/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist
/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8
a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (14 pages, 182628 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99c9b574-10fa-4cba-9957-e23d111d5c1c",
  "isSidechain": false,
  "promptId": "4e9b6b3b-bc11-45d7-a0d2-4aaa1c0c9272",
  "type": "user",
  "uuid": "2c08dfb0-f723-4472-bac7-6d5db48d6e9d",
  "toolUseResult": {
    "stdout": "[14] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/us\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist\n/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8\na.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (14 pages, 182628 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "99c9b574-10fa-4cba-9957-e23d111d5c1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-24T09:04:34.197Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01QiS56LH14VrU1qxjn47R7x`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -15",
  "description": "Second pdflatex pass for cross-references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c08dfb0-f723-4472-bac7-6d5db48d6e9d",
  "isSidechain": false,
  "requestId": "req_011CbM8FTg8v2WaVwXeTfTid",
  "type": "assistant",
  "uuid": "f97c3be7-e379-4279-a40f-09396ed47830",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011qu9XSK9XpU1Y8reuZ8FgD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 745,
      "cache_read_input_tokens": 72009,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 745,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 148,
          "cache_read_input_tokens": 72009,
          "cache_creation_input_tokens": 745,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 745
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

_source line 40 · 2026-05-24T09:04:34.962Z_

<details><summary>↩ Tool result · `toolu_01QiS56LH14VrU1qxjn47R7x`</summary>

```text
LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.

 )&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/us
r/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist
/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8
a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (14 pages, 189488 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f97c3be7-e379-4279-a40f-09396ed47830",
  "isSidechain": false,
  "promptId": "4e9b6b3b-bc11-45d7-a0d2-4aaa1c0c9272",
  "type": "user",
  "uuid": "49b3006f-1fdc-4144-9635-bd81f0b338f2",
  "toolUseResult": {
    "stdout": "LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n )&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/us\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist\n/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8\na.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (14 pages, 189488 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "f97c3be7-e379-4279-a40f-09396ed47830",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-24T09:04:39.593Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Rv3UsvYnbsRZxz9muesQTG`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | grep -E \"(Warning|Error|Output written)\"",
  "description": "Third pdflatex pass to resolve remaining references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49b3006f-1fdc-4144-9635-bd81f0b338f2",
  "isSidechain": false,
  "requestId": "req_011CbM8Fi2LjFGhzXqcPsQzM",
  "type": "assistant",
  "uuid": "5b611830-c325-4e39-9f24-cf15b3feb61d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GkzMmK6dHEnN5VmDRZCdoU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 596,
      "cache_read_input_tokens": 72754,
      "output_tokens": 156,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 596,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 156,
          "cache_read_input_tokens": 72754,
          "cache_creation_input_tokens": 596,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 596
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

_source line 42 · 2026-05-24T09:04:40.742Z_

<details><summary>↩ Tool result · `toolu_01Rv3UsvYnbsRZxz9muesQTG`</summary>

```text
Package hyperref Warning: Token not allowed in a PDF string (Unicode):
Package hyperref Warning: Token not allowed in a PDF string (Unicode):
Package hyperref Warning: Token not allowed in a PDF string (Unicode):
Package hyperref Warning: Token not allowed in a PDF string (Unicode):
LaTeX Warning: `h' float specifier changed to `ht'.
Package hyperref Warning: Token not allowed in a PDF string (Unicode):
Package hyperref Warning: Token not allowed in a PDF string (Unicode):
Package hyperref Warning: Token not allowed in a PDF string (Unicode):
Package hyperref Warning: Token not allowed in a PDF string (Unicode):
Package hyperref Warning: Token not allowed in a PDF string (Unicode):
Package hyperref Warning: Token not allowed in a PDF string (Unicode):
LaTeX Warning: `h' float specifier changed to `ht'.
Output written on paper.pdf (14 pages, 189488 bytes).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5b611830-c325-4e39-9f24-cf15b3feb61d",
  "isSidechain": false,
  "promptId": "4e9b6b3b-bc11-45d7-a0d2-4aaa1c0c9272",
  "type": "user",
  "uuid": "7a9c32d0-944f-465c-9e2b-e16cdb7f9efe",
  "toolUseResult": {
    "stdout": "Package hyperref Warning: Token not allowed in a PDF string (Unicode):\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\nLaTeX Warning: `h' float specifier changed to `ht'.\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\nLaTeX Warning: `h' float specifier changed to `ht'.\nOutput written on paper.pdf (14 pages, 189488 bytes).",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "5b611830-c325-4e39-9f24-cf15b3feb61d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-24T09:04:55.973Z_

编译成功，14 页 PDF（含 appendix）。所有 warnings 是 hyperref PDF 字符串和 float specifier 的常规警告，无 error。

论文结构覆盖了 experiment_data.json 中全部 9 个实验：
- **§5.2** Main gap (8×–27×) + **§5.3** Four-way ablation (N=200 expanded eval)
- **§5.4** PCGrad + Llama gradient geometry (cross-model gradient analysis)
- **§5.5** λ sensitivity
- **§5.6** Cross-model replication (Llama)
- **§6.2** KL divergence analysis + **§6.3** Alternative GAR definitions
- **§7.1** SS attempted mitigation (Qwen 3-seed + 4th seed + Llama SS failure)
- **§7.2** Long conversation scalability

叙事已按 worst tier 指引重构：SS 降级为 Discussion "attempted mitigation"，核心卖点转为 failure mode taxonomy (NF1–NF3) + PCGrad causal exclusion + convergent failure evidence。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a9c32d0-944f-465c-9e2b-e16cdb7f9efe",
  "isSidechain": false,
  "requestId": "req_011CbM8G8jdtgjKu4cv8FDhW",
  "type": "assistant",
  "uuid": "db9e1502-9d15-4639-971a-f52429a1c5ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BwbNHaMD6HCEDA5hEEX1t1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 331,
      "cache_read_input_tokens": 73350,
      "output_tokens": 297,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 331,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 297,
          "cache_read_input_tokens": 73350,
          "cache_creation_input_tokens": 331,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 331
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

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260524T081135 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_ga…",
  "leafUuid": "db9e1502-9d15-4639-971a-f52429a1c5ba",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier diagnostic paper for dream_20260524T081135",
  "sessionId": "3d2d4040-5c67-4419-9f32-36942b3022a1"
}
```

---
