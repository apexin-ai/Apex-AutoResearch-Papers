# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T125926 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-1/175abc6b-2146-427e-acfe-4e3e17983955.jsonl`
- **Structured JSON:** [`122944800683db703751.json`](../../sessions/12/122944800683db703751.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-18T13:48:14.823Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T13:48:14.823Z",
  "sessionId": "175abc6b-2146-427e-acfe-4e3e17983955",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T125926 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/worst/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Budget curve 4 模型间模式完全分裂，无法提炼 universal phase transition pattern。 Qwen-7B gradual, Qwen-1.5B sharp, DeepSeek early-onset, CodeLlama multi-point anomaly。 Budget curve 必须从 Results → Appendix supplementary。论文 headline 收缩为： \"Exception events as the only universally robust trace signal — all other trace components and budget-length relationships are model-dependent.\" Error analysis 和 cross-model calibration 也出现 model-dependency，无法作为独立 contribution。 Few-shot GPT-4o baseline 接近 SFT 水平（~97% vs 99.83%），需用 cost efficiency + calibration superiority 辩护 SFT 价值。OOD 泛化性有限。Reframe 策略: 以 exception dominance 的 simplicity + universality 为唯一 anchor，将所有 model-dependent 发现 转化为 \"simplicity is robustness\" 的反面教材。EMNLP Main 概率 15-30%。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-18T13:48:14.826Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T13:48:14.826Z",
  "sessionId": "175abc6b-2146-427e-acfe-4e3e17983955"
}
```

---

## Round 1

32 recorded events

### User

_source line 3 · 2026-05-18T13:48:14.846Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T125926 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/worst/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Budget curve 4 模型间模式完全分裂，无法提炼 universal phase transition pattern。 Qwen-7B gradual, Qwen-1.5B sharp, DeepSeek early-onset, CodeLlama multi-point anomaly。 Budget curve 必须从 Results → Appendix supplementary。论文 headline 收缩为： "Exception events as the only universally robust trace signal — all other trace components and budget-length relationships are model-dependent." Error analysis 和 cross-model calibration 也出现 model-dependency，无法作为独立 contribution。 Few-shot GPT-4o baseline 接近 SFT 水平（~97% vs 99.83%），需用 cost efficiency + calibration superiority 辩护 SFT 价值。OOD 泛化性有限。Reframe 策略: 以 exception dominance 的 simplicity + universality 为唯一 anchor，将所有 model-dependent 发现 转化为 "simplicity is robustness" 的反面教材。EMNLP Main 概率 15-30%。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "cde04d7b-c03d-49ea-b3f7-a9fea2ed96f5",
  "type": "user",
  "uuid": "0a293b29-77ec-4697-8e74-e88dd9cf6f1f",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "175abc6b-2146-427e-acfe-4e3e17983955",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-18T13:48:14.846Z_

```json
{
  "parentUuid": "0a293b29-77ec-4697-8e74-e88dd9cf6f1f",
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
  "uuid": "6bc82280-be9f-490a-b4c7-f151e48389d2",
  "timestamp": "2026-05-18T13:48:14.846Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "175abc6b-2146-427e-acfe-4e3e17983955",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-18T13:48:14.846Z_

```json
{
  "parentUuid": "6bc82280-be9f-490a-b4c7-f151e48389d2",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5ce75457-02ce-4662-9530-1f53520e085d",
  "timestamp": "2026-05-18T13:48:14.846Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "175abc6b-2146-427e-acfe-4e3e17983955",
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
  "aiTitle": "Generate worst-tier dream paper for dream_20260518T125926",
  "sessionId": "175abc6b-2146-427e-acfe-4e3e17983955"
}
```

---

### Assistant

_source line 7 · 2026-05-18T13:48:16.917Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ce75457-02ce-4662-9530-1f53520e085d",
  "isSidechain": false,
  "requestId": "req_011CbA92po6K9LenrwdPmgGx",
  "type": "assistant",
  "uuid": "3151d75c-121d-49c9-bf07-1cafa88983ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "175abc6b-2146-427e-acfe-4e3e17983955",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015dbw6GxmD4ehyFHBv6mEj6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12857,
      "cache_read_input_tokens": 11841,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12857,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12857,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12857
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

_source line 8 · 2026-05-18T13:48:18.013Z_

<details open><summary>🔧 Tool call — Read · `toolu_01G8J1KtgAfkWSAHZ9AVnqtk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3151d75c-121d-49c9-bf07-1cafa88983ab",
  "isSidechain": false,
  "requestId": "req_011CbA92po6K9LenrwdPmgGx",
  "type": "assistant",
  "uuid": "91dc17c2-afc8-42b0-bfcb-090e4b1e5670",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "175abc6b-2146-427e-acfe-4e3e17983955",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015dbw6GxmD4ehyFHBv6mEj6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12857,
      "cache_read_input_tokens": 11841,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12857,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12857,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12857
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

_source line 9 · 2026-05-18T13:48:18.205Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ba3ZoeWRYZ2QvFMEiLwcBZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91dc17c2-afc8-42b0-bfcb-090e4b1e5670",
  "isSidechain": false,
  "requestId": "req_011CbA92po6K9LenrwdPmgGx",
  "type": "assistant",
  "uuid": "40a83622-b4f3-45b6-96fb-82e202cc39f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "175abc6b-2146-427e-acfe-4e3e17983955",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015dbw6GxmD4ehyFHBv6mEj6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12857,
      "cache_read_input_tokens": 11841,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12857,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12857,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12857
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

_source line 10 · 2026-05-18T13:48:18.314Z_

<details><summary>↩ Tool result · `toolu_01G8J1KtgAfkWSAHZ9AVnqtk`</summary>

```text
1	[
2	  {
3	    "name": "qwen7b_full_trace_tail384_seed42",
4	    "description": "Qwen-2.5-Coder-7B tail-384 truncation，定位 256→512 transition 位置",
5	    "results": {
6	      "accuracy": 0.847,
7	      "accuracy_ci_lower": 0.826,
8	      "accuracy_ci_upper": 0.868,
9	      "majority_baseline": 0.7151,
10	      "lift_over_majority": 0.132,
11	      "pass_precision": 0.905,
12	      "pass_recall": 0.875,
13	      "pass_f1": 0.89,
14	      "fail_precision": 0.71,
15	      "fail_recall": 0.78,
16	      "fail_f1": 0.743,
17	      "n_test": 1190,
18	      "train_loss": 0.088,
19	      "eval_loss": 0.41
20	    },
21	    "tables": [
22	      {
23	        "name": "Qwen-7B budget curve (updated)",
24	        "data": [
25	          {
26	            "length": "tail-256",
27	            "accuracy": "77.48%",
28	            "delta_vs_prev": "—"
29	          },
30	          {
31	            "length": "tail-384",
32	            "accuracy": "84.7%",
33	            "delta_vs_prev": "+7.2pp"
34	          },
35	          {
36	            "length": "tail-512",
37	            "accuracy": "93.6%",
38	            "delta_vs_prev": "+8.9pp"
39	          },
40	          {
41	            "length": "tail-1024",
42	            "accuracy": "96.5%",
43	            "delta_vs_prev": "+2.9pp"
44	          },
45	          {
46	            "length": "tail-2048",
47	            "accuracy": "97.3%",
48	            "delta_vs_prev": "+0.8pp"
49	          }
50	        ]
51	      }
52	    ],
53	    "figures": [],
54	    "analysis": "Qwen-7B 是 4 模型中唯一呈现 clean monotonic + gradual transition 的模型。 然而 \"gradual\" 意味着无法定义 discrete phase transition point，削弱 \"sharp phase transition\" claim。如果其他模型也 gradual 则可声称 universal gradual pattern；但其他模型模式不同，Qwen-7B 的 gradual 反而成为 model-specific behavior 的证据。\n\n\nQwen-7B tail-256=77.48%, tail-512=93.6%。384 tokens 在 worst 档下处于 transition 中段——提供了约 50% 的 tail-end diagnostic content（包含部分 exception/assertion 数据 但不完整）。Qwen-7B 的 LoRA landscape 平滑（3-seed exception_only variance=0）， 因此即使在 noisy intermediate length 上也能稳定学到部分模式。但 384 tokens 不足以 覆盖多数 fail 样本的完整 exception trace（exception 通常在 trace 最后 200-500 tokens）， 导致 ~50% 的 fail 样本 exception 信息被截断。结果: gradual rise，interpolating between 256 and 512，约 84.7%。这使 Qwen-7B 成为 \"gradual transition\" 模式的代表—— 与 Qwen-1.5B 的 sharp transition 形成对比，破坏 universal pattern 叙事。\n"
55	  },
56	  {
57	    "name": "qwen15b_full_trace_tail384_seed42",
58	    "description": "Qwen-2.5-Coder-1.5B tail-384，验证小模型 transition timing",
59	    "results": {
60	      "accuracy": 0.745,
61	      "accuracy_ci_lower": 0.72,
62	      "accuracy_ci_upper": 0.769,
63	      "majority_baseline": 0.7151,
64	      "lift_over_majority": 0.03,
65	      "pass_precision": 0.835,
66	      "pass_recall": 0.81,
67	      "pass_f1": 0.822,
68	      "fail_precision": 0.545,
69	      "fail_recall": 0.59,
70	      "fail_f1": 0.567,
71	      "n_test": 1190,
72	      "train_loss": 0.25,
73	      "eval_loss": 0.56
74	    },
75	    "tables": [
76	      {
77	        "name": "Qwen-1.5B budget curve (updated)",
78	        "data": [
79	          {
80	            "length": "tail-256",
81	            "accuracy": "72.6%",
82	            "delta_vs_prev": "—"
83	          },
84	          {
85	            "length": "tail-384",
86	            "accuracy": "74.5%",
87	            "delta_vs_prev": "+1.9pp"
88	          },
89	          {
90	            "length": "tail-512",
91	            "accuracy": "95.6%",
92	            "delta_vs_prev": "+21.1pp"
93	          },
94	          {
95	            "length": "tail-1024",
96	            "accuracy": "96.6%",
97	            "delta_vs_prev": "+1.0pp"
98	          },
99	          {
100	            "length": "tail-2048",
101	            "accuracy": "97.9%",
102	            "delta_vs_prev": "+1.3pp"
103	          }
104	        ]
105	      }
106	    ],
107	    "figures": [],
108	    "analysis": "Qwen-1.5B 的 sharp transition 说明小模型的 information utilization threshold 更高——384 tokens 的 partial trace 对 1.5B 几乎无用，但 512 tokens 突然 提供了 sufficient signal。这与 exception_only 的 scale-invariance（1.5B=7B=99.83%） 形成 interesting 对比：exception signal 因其 structural simplicity 对模型容量 无要求，但 full_trace 的 utilization threshold 是 capacity-dependent。然而 这一 finding 无法 universalize——同 scale/同 family 的 7B 模型呈现完全不同 的 gradual pattern。\n\n\nQwen-1.5B tail-256=72.6%, tail-512=95.6%。这个模型在 exception_only 上 与 7B 完全一致（99.83%），但在 noisy full_trace 上更脆弱（head-2048 仅 75.3% vs 7B 的 81.6%）。1.5B 模型容量有限，需要更完整的 diagnostic signal 才能 学到有用模式——384 tokens 提供的 partial information 对它来说 insufficient， 无法从噪声中提取信号。结果: 仅比 tail-256 提升 ~2pp，仍接近 baseline。 真正的 phase transition 发生在 384→512 之间（+21pp 的巨大跳跃），显示 512 tokens 是该模型的 critical threshold——刚好覆盖大多数 fail 样本的完整 exception + assertion 信息。这是 \"sharp transition\" 模式，但 threshold 位置 (384-512) 与 Qwen-7B 的 gradual zone 不同。\n"
109	  },
110	  {
111	    "name": "deepseek_full_trace_tail384_seed42",
112	    "description": "DeepSeek-Coder-6.7B tail-384，验证 alternative architecture transition",
113	    "results": {
114	      "accuracy": 0.883,
115	      "accuracy_ci_lower": 0.863,
116	      "accuracy_ci_upper": 0.902,
117	      "majority_baseline": 0.7151,
118	      "lift_over_majority": 0.168,
119	      "pass_precision": 0.92,
120	      "pass_recall": 0.915,
121	      "pass_f1": 0.917,
122	      "fail_precision": 0.792,
123	      "fail_recall": 0.805,
124	      "fail_f1": 0.798,
125	      "n_test": 1190,
126	      "train_loss": 0.15,
127	      "eval_loss": 0.38
128	    },
129	    "tables": [
130	      {
131	        "name": "DeepSeek budget curve (updated)",
132	        "data": [
133	          {
134	            "length": "tail-256",
135	            "accuracy": "76.4%",
136	            "delta_vs_prev": "—"
137	          },
138	          {
139	            "length": "tail-384",
140	            "accuracy": "88.3%",
141	            "delta_vs_prev": "+11.9pp"
142	          },
143	          {
144	            "length": "tail-512",
145	            "accuracy": "93.9%",
146	            "delta_vs_prev": "+5.6pp"
147	          },
148	          {
149	            "length": "tail-1024",
150	            "accuracy": "96.5%",
151	            "delta_vs_prev": "+2.6pp"
152	          },
153	          {
154	            "length": "tail-2048",
155	            "accuracy": "95.0%",
156	            "delta_vs_prev": "-1.5pp"
157	          }
158	        ]
159	      }
160	    ],
161	    "figures": [],
162	    "analysis": "DeepSeek 的 early-onset transition 与 Qwen 两模型模式都不同。可能原因: (1) tokenizer efficiency 不同导致同 token 数覆盖不同内容量； (2) 预训练数据差异导致 trace 理解的 readiness 不同。 tail-2048 的轻微 regression 虽小（-1.5pp, 可能在 CI 内），但与 CodeLlama 的灾难性 regression 构成连续谱，暗示 long-context full_trace 对 SFT 有普遍 的 diminishing/negative returns 趋势——但程度完全 model-specific。\n\n\nDeepSeek tail-256=76.4%, tail-512=93.9%。DeepSeek tokenizer 在 tail 区域 的 token density 不同于 Qwen（不同 BPE vocabulary），384 DeepSeek tokens 覆盖更多字符内容。加之 DeepSeek 在 full_trace 条件下对 fail 模式的学习 更快（tail-2048 已 95%），transition 更早发生。88.3% 说明 DeepSeek 在 384 tokens 时已经获得了大部分 diagnostic information——与 Qwen-7B (84.7%) 和 Qwen-1.5B (74.5%) 形成第三种不同模式：\"early-onset transition\"。但这也暴露了 DeepSeek tail-2048 (95.0%) 相对 tail-1024 (96.5%) 的轻微非单调性—— longer context 引入 noise。整体模式: 提前进入 transition + 后端轻微 regression。\n"
163	  },
164	  {
165	    "name": "codellama13b_full_trace_tail384_seed42",
166	    "description": "CodeLlama-13B-Instruct tail-384，验证 LLaMA family transition",
167	    "results": {
168	      "accuracy": 0.735,
169	      "accuracy_ci_lower": 0.711,
170	      "accuracy_ci_upper": 0.76,
171	      "majority_baseline": 0.7151,
172	      "lift_over_majority": 0.02,
173	      "pass_precision": 0.8,
174	      "pass_recall": 0.845,
175	      "pass_f1": 0.822,
176	      "fail_precision": 0.555,
177	      "fail_recall": 0.458,
178	      "fail_f1": 0.502,
179	      "n_test": 1190,
180	      "train_loss": 0.28,
181	      "eval_loss": 0.62
182	    },
183	    "tables": [
184	      {
185	        "name": "CodeLlama budget curve (updated)",
186	        "data": [
187	          {
188	            "length": "tail-256",
189	            "accuracy": "77.9%",
190	            "delta_vs_prev": "—"
191	          },
192	          {
193	            "length": "tail-384",
194	            "accuracy": "73.5%",
195	            "delta_vs_prev": "-4.4pp ⚠️"
196	          },
197	          {
198	            "length": "tail-512",
199	            "accuracy": "97.5%",
200	            "delta_vs_prev": "+24.0pp"
201	          },
202	          {
203	            "length": "tail-1024",
204	            "accuracy": "98.2%",
205	            "delta_vs_prev": "+0.7pp"
206	          },
207	          {
208	            "length": "tail-2048",
209	            "accuracy": "41.8%",
210	            "delta_vs_prev": "-56.4pp ⚠️"
211	          }
212	        ]
213	      }
214	    ],
215	    "figures": [],
216	    "analysis": "CodeLlama 的 multi-point anomaly 使 budget curve 作为 universal contribution 彻底失效。任何试图 fit a universal curve 的尝试都会被 CodeLlama 的 W-shape 击碎。 审稿人会质疑 training pipeline 健壮性——为什么同一 codebase 对 CodeLlama 产生如此不稳定的结果？回应策略: (1) 诚实报告所有数据; (2) 指出 CodeLlama 的 LLaMA tokenizer 与 code-specific tokenizers (Qwen/DeepSeek) 的效率差异导致 同 token 数对应不同 content coverage; (3) 将 CodeLlama 的 instability 作为 \"why simplicity matters\" 的反面论据——exception_only 在 CodeLlama 上 99.83% 完美，不受 length budget 影响。\n\n\nCodeLlama tail-256=77.9%, tail-512=97.5%。在 worst 档下 CodeLlama tail-384 出现 anomalous dip——accuracy 73.5% 低于 tail-256 (77.9%) 4.4pp。根因假说: CodeLlama tokenizer 在 384-token window 内截取到 trace 中间位置的 ambiguous content（包含 partial loop iterations 但 exception 被截断），形成比 tail-256 更具误导性的输入。tail-256 因内容极少反而让模型回退到 no_trace-like 的保守策略 （~78%≈no_trace+few pp），而 tail-384 提供了 \"just enough to be dangerous\" 的 partial information——模型看到了 execution trace 但缺少 diagnostic conclusion， 导致 fail_recall 大幅下降 (0.458)。这与 CodeLlama 在 tail-2048 (41.8%) 的 catastrophic failure 以及 tail-1024 v2 的不稳定 (87.6%) 构成系统性 pattern: CodeLlama 对 intermediate-noise trace 特别脆弱。\n"
217	  },
218	  {
219	    "name": "plan_016_cross_model_synthesis",
220	    "description": "tail-384 × 4 模型交叉分析: phase transition 模式分裂总结",
221	    "results": {
222	      "tail384_cross_model_std_pp": 6.4,
223	      "tail384_cross_model_range_pp": 14.8,
224	      "phase_transition_sharpness": 0.2,
225	      "budget_curve_consistent_models": 1,
226	      "transition_patterns": {
227	        "qwen7b": "gradual_monotonic",
228	        "qwen15b": "sharp_delayed",
229	        "deepseek": "early_onset_with_tail_regression",
230	        "codellama": "non_monotonic_W_shape"
231	      }
232	    },
233	    "tables": [
234	      {
235	        "name": "Cross-model tail-384 comparison",
236	        "data": [
237	          {
238	            "model": "Qwen-7B",
239	            "tail256": "77.5%",
240	            "tail384": "84.7%",
241	            "tail512": "93.6%",
242	            "delta_256_384": "+7.2pp",
243	            "delta_384_512": "+8.9pp",
244	            "pattern": "gradual"
245	          },
246	          {
247	            "model": "Qwen-1.5B",
248	            "tail256": "72.6%",
249	            "tail384": "74.5%",
250	            "tail512": "95.6%",
251	            "delta_256_384": "+1.9pp",
252	            "delta_384_512": "+21.1pp",
253	            "pattern": "sharp_delayed"
254	          },
255	          {
256	            "model": "DeepSeek",
257	            "tail256": "76.4%",
258	            "tail384": "88.3%",
259	            "tail512": "93.9%",
260	            "delta_256_384": "+11.9pp",
261	            "delta_384_512": "+5.6pp",
262	            "pattern": "early_onset"
263	          },
264	          {
265	            "model": "CodeLlama",
266	            "tail256": "77.9%",
267	            "tail384": "73.5%",
268	            "tail512": "97.5%",
269	            "delta_256_384": "-4.4pp",
270	            "delta_384_512": "+24.0pp",
271	            "pattern": "non_monotonic"
272	          }
273	        ]
274	      },
275	      {
276	        "name": "Full budget curve matrix (all models)",
277	        "data": [
278	          {
279	            "model": "Qwen-7B",
280	            "t256": "77.5",
281	            "t384": "84.7",
282	            "t512": "93.6",
283	            "t1024": "96.5",
284	            "t2048": "97.3",
285	            "monotonic": "✓",
286	            "pattern": "gradual S-curve"
287	          },
288	          {
289	            "model": "Qwen-1.5B",
290	            "t256": "72.6",
291	            "t384": "74.5",
292	            "t512": "95.6",
293	            "t1024": "96.6",
294	            "t2048": "97.9",
295	            "monotonic": "✓",
296	            "pattern": "step function at 512"
297	          },
298	          {
299	            "model": "DeepSeek",
300	            "t256": "76.4",
301	            "t384": "88.3",
302	            "t512": "93.9",
303	            "t1024": "96.5",
304	            "t2048": "95.0",
305	            "monotonic": "✗",
306	            "pattern": "early rise + tail regression"
307	          },
308	          {
309	            "model": "CodeLlama",
310	            "t256": "77.9",
311	            "t384": "73.5",
312	            "t512": "97.5",
313	            "t1024": "98.2",
314	            "t2048": "41.8",
315	            "monotonic": "✗",
316	            "pattern": "W-shape with 2 anomalies"
317	          }
318	        ]
319	      }
320	    ],
321	    "figures": [],
322	    "analysis": "Budget curve 作为 contribution 在 worst 档下完全失效。4 模型 4 种模式， 无法声称 \"trace length has a universal effect on verdict accuracy\"。 唯一 universal 的 finding 是 exception_only (99.83%) 在所有模型上不受 length budget 影响——这反而强化了 \"simplicity is robustness\" 的 headline。 Budget curve 应移至 Appendix，仅作为 \"why exception_only is preferable\" 的 supporting evidence：同 token budget 下 full_trace 的效果完全不可预测， 而 exception_only 无此问题。\n\n\n4 模型呈现 4 种不同的 budget curve 形态。phase_transition_sharpness=0.2 因为 只有 Qwen-1.5B 显示真正的 sharp transition (tail-384→512 跳 21pp)，其他 模型要么 gradual (Qwen-7B)、要么 early-onset (DeepSeek)、要么 anomalous (CodeLlama)。budget_curve_consistent_models=1 因为只有 Qwen-7B 呈现 clean monotonic pattern（DeepSeek 有 tail regression, CodeLlama 有两处 anomaly, Qwen-1.5B 虽 monotonic 但 step-function 形态不同于 Qwen-7B 的 gradual）。 Cross-model std=6.4pp 在 [5,12] 范围内。这证明 budget curve 形态是 model-specific 的——无法提炼 universal trace-length → accuracy pattern。\n"
323	  },
324	  {
325	    "name": "cross_seed_budget_curve_tail512",
326	    "description": "tail-512 × 4 models × 3 seeds，验证 phase transition 后 convergence band robustness",
327	    "results": {
328	      "qwen7b": {
329	        "seed42": 0.936,
330	        "seed123": 0.924,
331	        "seed456": 0.931,
332	        "mean": 0.93,
333	        "std_pp": 0.6,
334	        "range_pp": 1.2
335	      },
336	      "qwen15b": {
337	        "seed42": 0.956,
338	        "seed123": 0.908,
339	        "seed456": 0.942,
340	        "mean": 0.935,
341	        "std_pp": 2.5,
342	        "range_pp": 4.8
343	      },
344	      "deepseek": {
345	        "seed42": 0.939,
346	        "seed123": 0.876,
347	        "seed456": 0.919,
348	        "mean": 0.911,
349	        "std_pp": 3.2,
350	        "range_pp": 6.3
351	      },
352	      "codellama": {
353	        "seed42": 0.975,
354	        "seed123": 0.809,
355	        "seed456": 0.943,
356	        "mean": 0.909,
357	        "std_pp": 8.7,
358	        "range_pp": 16.6
359	      },
360	      "overall_cross_model_seed_std_mean": 3.75
361	    },
362	    "tables": [
363	      {
364	        "name": "tail-512 × 4 models × 3 seeds",
365	        "data": [
366	          {
367	            "model": "Qwen-7B",
368	            "seed42": "93.6%",
369	            "seed123": "92.4%",
370	            "seed456": "93.1%",
371	            "mean": "93.0%",
372	            "std": "0.6pp",
373	            "verdict": "✓ robust"
374	          },
375	          {
376	            "model": "Qwen-1.5B",
377	            "seed42": "95.6%",
378	            "seed123": "90.8%",
379	            "seed456": "94.2%",
380	            "mean": "93.5%",
381	            "std": "2.5pp",
382	            "verdict": "△ moderate"
383	          },
384	          {
385	            "model": "DeepSeek",
386	            "seed42": "93.9%",
387	            "seed123": "87.6%",
388	            "seed456": "91.9%",
389	            "mean": "91.1%",
390	            "std": "3.2pp",
391	            "verdict": "△ moderate"
392	          },
393	          {
394	            "model": "CodeLlama",
395	            "seed42": "97.5%",
396	            "seed123": "80.9%",
397	            "seed456": "94.3%",
398	            "mean": "90.9%",
399	            "std": "8.7pp",
400	            "verdict": "✗ unstable"
401	          }
402	        ]
403	      },
404	      {
405	        "name": "对比: exception_only seed robustness",
406	        "data": [
407	          {
408	            "model": "Qwen-7B",
409	            "exc_std": "0.00pp",
410	            "tail512_std": "0.6pp",
411	            "ratio": "∞"
412	          },
413	          {
414	            "model": "Qwen-1.5B",
415	            "exc_std": "0.00pp (单 seed)",
416	            "tail512_std": "2.5pp",
417	            "ratio": "—"
418	          },
419	          {
420	            "model": "DeepSeek",
421	            "exc_std": "4.8pp",
422	            "tail512_std": "3.2pp",
423	            "ratio": "0.67"
424	          },
425	          {
426	            "model": "CodeLlama",
427	            "exc_std": "0.10pp",
428	            "tail512_std": "8.7pp",
429	            "ratio": "87x"
430	          }
431	        ]
432	      }
433	    ],
434	    "figures": [],
435	    "analysis": "Cross-seed robustness 进一步削弱 budget curve contribution。即使在 tail-512 这个 \"transition 后最稳定\" 的点，4 模型中只有 Qwen-7B 真正 seed-robust。 CodeLlama 的 σ=8.7pp 使其 single-seed 数据完全不可信——97.5% 可能只是 lucky seed。这意味着论文中报告的所有 single-seed budget curve 数据点都有 潜在的 seed noise 问题，但我们不可能为每个 length × model 组合都跑 3 seeds （预算 24 GPU-hours 只够 tail-512 这一个点）。\n对论文的影响: (1) budget curve 的可信度进一步下降——不仅 model-specific， 还 seed-sensitive; (2) exception_only 的 seed robustness（Qwen 0pp, CodeLlama 0.1pp）与 full_trace tail-512 的 seed variance（CodeLlama 8.7pp）形成 87x 的对比，成为 \"simplicity enables robustness\" 的额外弹药; (3) 建议 仅在 Appendix 报告 tail-512 seed data，不 support 任何 main claim。\n\n\ntail-512 是 transition 后的第一个 \"高 accuracy\" 点，但在 worst 档下 seed robustness 与 signal complexity 正相关。exception_only（最简信号）seed variance 已知: Qwen 0pp, DeepSeek 4.8pp (σ)。full_trace tail-512 的 signal 远比 exception_only complex（包含 loop iterations, variable states, partial traces）， 因此 seed sensitivity 应更严重。\nQwen-7B: LoRA landscape 平滑（exception_only 3-seed variance=0），tail-512 的 seed variance 也最小（σ=0.6pp）。但即使 Qwen-7B 也有 ~1pp 波动—— full_trace 信号的 noise 导致不同 seed 的 LoRA 从 trace 中学到略微不同的 patterns。\nQwen-1.5B: 容量限制放大 seed sensitivity。在 exception_only 上 scale-invariant (99.83%)，但 full_trace 依赖 execution reasoning——1.5B 的 reasoning 容量 有限，seed123 未能充分学到 trace→verdict 映射。σ=2.5pp，moderate。\nDeepSeek: 已知 LoRA initialization sensitivity（exception_only seed123=91.09% vs seed42/456=99.33%）。full_trace 放大此效应。seed123 再次成为 outlier (87.6%)，但 gap 不如 exception_only 的 seed123 极端——因为 full_trace 的 ceiling 本身较低（~94%），outlier seed 的退化空间也较小。σ=3.2pp。\nCodeLlama: training instability 的系统性问题。已知 tail-1024 有 run-to-run variance (87.6% vs 98.2%)，tail-2048 catastrophic。tail-512 虽然是 CodeLlama 的 \"sweet spot\"（single seed=97.5%），但 seed variance 极大——seed123 仅 80.9%，几乎 17pp 退化。根因: CodeLlama 的 LLaMA tokenizer 对 code trace 的 tokenization 效率低，512 tokens 覆盖内容较少，不同 seed 的 LoRA 可能 focus on different trace regions，导致 catastrophic divergence。σ=8.7pp 使 CodeLlama 的 budget curve 在 seed 维度也不 robust。\n"
436	  },
437	  {
438	    "name": "error_analysis_cross_condition",
439	    "description": "用已有 predictions.jsonl 分析 4 条件的 failure modes",
440	    "results": {
441	      "exception_only_errors": {
442	        "total": 2,
443	        "all_generatorexit": true,
444	        "sample_ids": [
445	          901,
446	          905
447	        ],
448	        "function": "check_dict_case (HumanEval/95)",
449	        "error_direction": "pass→fail (false negative)",
450	        "cross_seed_overlap": "100% (3/3 seeds identical)"
451	      },
452	      "vota_errors": {
453	        "total": 7,
454	        "categories": {
455	          "generatorexit": 2,
456	          "long_trace_attention_dilution": 3,
457	          "ambiguous_loop_pattern": 2
458	        },
459	        "false_negative_rate": 0.71,
460	        "overlap_with_exception_only": 2
461	      },
462	      "full_trace_errors": {
463	        "total": 217,
464	        "categories": {
465	          "long_program_overload": 142,
466	          "edge_case_subtle_bug": 38,
467	          "correct_but_verbose_trace": 22,
468	          "random_noise": 15
469	        },
470	        "false_negative_rate": 0.62,
471	        "median_trace_length_errors_vs_correct": "2.3x longer"
472	      },
473	      "no_trace_errors": {
474	        "total": 296,
475	        "categories": {
476	          "subtle_functional_bugs": 108,
477	          "edge_case_only_failures": 87,
478	          "correct_format_wrong_logic": 63,
479	          "random": 38
480	        },
481	        "false_negative_rate": 0.55,
482	        "fail_recall": 0.735
483	      },
484	      "cross_condition_overlap": {
485	        "exc_intersect_vota": 0.286,
486	        "vota_intersect_full": 0.714,
487	        "full_intersect_no_trace": 0.691,
488	        "exc_intersect_no_trace": 0.007
489	      }
490	    },
491	    "tables": [
492	      {
493	        "name": "Error category distribution",
494	        "data": [
495	          {
496	            "condition": "exception_only",
497	            "n_errors": 2,
498	            "primary_category": "GeneratorExit (100%)",
499	            "actionable": "No (irreducible)"
500	          },
501	          {
502	            "condition": "VOTA",
503	            "n_errors": 7,
504	            "primary_category": "Mixed (GenExit 29% / attention dilution 43% / ambiguous loop 29%)",
505	            "actionable": "Partial"
506	          },
507	          {
508	            "condition": "full_trace",
509	            "n_errors": 217,
510	            "primary_category": "Long-trace overload (65%)",
511	            "actionable": "Not without architecture change"
512	          },
513	          {
514	            "condition": "no_trace",
515	            "n_errors": 296,
516	            "primary_category": "Subtle bugs undetectable from code alone (37%)",
517	            "actionable": "No (inherent limitation)"
518	          }
519	        ]
520	      }
521	    ],
522	    "figures": [],
523	    "analysis": "Error analysis 在 worst 档下产出有限。exception_only 的 2 个 error 已在 irreducible error analysis (D5) 中完全解析——无新 finding。VOTA 的 7 个 error 异质但数量太少不支撑 statistical analysis。full_trace 的 217 个 error 有 pattern（long traces dominant）但这是 Claim 2 已覆盖的 information overload finding 的 restatement。no_trace 的 296 个 error 说明 baseline 弱但无新 insight。\nCross-condition overlap 低本身是 interesting finding（不同 representations fail on orthogonal dimensions），但在 worst 档下这无法 crystallize into a clean narrative。建议: 仅在 Appendix 放 error breakdown table，Discussion 简短提及 orthogonal failure modes 现象。不值得作为独立 contribution。\n\n\nexception_only: 2 errors 已知且不可约（GeneratorExit），不提供新 insight。\nVOTA: 7 errors 分为三类。(1) 2 个与 exception_only 重叠的 GeneratorExit—— inherited from Tier 1。(2) 3 个 long-trace samples 中 loop/ae tokens 稀释了 exception signal 的 attention——这些样本在 exception_only 下正确但 VOTA 下 错误，直接支持 \"Tier 2 introduces noise\" claim。(3) 2 个 ambiguous loop patterns——loop 正常但有 exception，模型对 conflicting signals 做出错误判断。 这 7 个 error 的异质性使其无法归为单一 category。\nfull_trace: 217 errors 高度异质。最大类 (142/217) 是 long programs 的 information overload——trace 太长模型无法有效处理。38 个 edge case 中模型 看到了 trace 但未能正确 interpret 细微的 bug pattern。22 个 correct but verbose——trace 的冗余信息误导模型预测 fail。这种高异质性使 error analysis 难以 yield actionable insight。\nno_trace: 296 errors 中最大类是 subtle functional bugs (108)——没有 trace 时模型仅能依赖 code structure/style heuristics，对逻辑正确但风格 unusual 的 代码也会误判。fail_recall 仅 0.735 说明 ~27% 的 fail 样本被漏判。\nCross-condition overlap 低: exception_only 的 2 个 error 仅在 VOTA 的 7 个 error 中出现 2 个（28.6%），说明不同条件的 failure modes 几乎不重叠—— 它们 fail on fundamentally different samples for fundamentally different reasons。\n"
524	  },
525	  {
526	    "name": "cross_model_calibration_exception_only",
527	    "description": "4 模型 × exception_only 的 ECE/Brier 对比",
528	    "results": {
529	      "qwen7b": {
530	        "ece": 0.0027,
531	        "brier": 0.0013,
532	        "mce": 0.835,
533	        "accuracy": 0.9983
534	      },
535	      "qwen15b": {
536	        "ece": 0.0041,
537	        "brier": 0.0019,
538	        "mce": 0.72,
539	        "accuracy": 0.9983
540	      },
541	      "deepseek": {
542	        "ece": 0.0523,
543	        "brier": 0.0318,
544	        "mce": 0.89,
545	        "accuracy": 0.9933
546	      },
547	      "codellama": {
548	        "ece": 0.0183,
549	        "brier": 0.0072,
550	        "mce": 0.78,
551	        "accuracy": 0.9983
552	      },
553	      "cross_model_ece_std": 0.0225,
554	      "cross_model_ece_range": 0.0496,
555	      "universal_calibration": false
556	    },
557	    "tables": [
558	      {
559	        "name": "Cross-model calibration for exception_only",
560	        "data": [
561	          {
562	            "model": "Qwen-7B",
563	            "accuracy": "99.83%",
564	            "ece": 0.0027,
565	            "brier": 0.0013,
566	            "calibration_quality": "Near-perfect"
567	          },
568	          {
569	            "model": "Qwen-1.5B",
570	            "accuracy": "99.83%",
571	            "ece": 0.0041,
572	            "brier": 0.0019,
573	            "calibration_quality": "Excellent"
574	          },
575	          {
576	            "model": "DeepSeek",
577	            "accuracy": "99.33%",
578	            "ece": 0.0523,
579	            "brier": 0.0318,
580	            "calibration_quality": "Moderate"
581	          },
582	          {
583	            "model": "CodeLlama",
584	            "accuracy": "99.83%",
585	            "ece": 0.0183,
586	            "brier": 0.0072,
587	            "calibration_quality": "Good"
588	          }
589	        ]
590	      },
591	      {
592	        "name": "Calibration gap: exception_only vs no_trace (cross-model)",
593	        "data": [
594	          {
595	            "model": "Qwen-7B",
596	            "exc_ece": 0.0027,
597	            "no_trace_ece": 0.1715,
598	            "ratio": "63x"
599	          },
600	          {
601	            "model": "Qwen-1.5B",
602	            "exc_ece": 0.0041,
603	            "no_trace_ece": "~0.21",
604	            "ratio": "~51x"
605	          },
606	          {
607	            "model": "DeepSeek",
608	            "exc_ece": 0.0523,
609	            "no_trace_ece": "~0.18",
610	            "ratio": "~3.4x"
611	          },
612	          {
613	            "model": "CodeLlama",
614	            "exc_ece": 0.0183,
615	            "no_trace_ece": "~0.17",
616	            "ratio": "~9.3x"
617	          }
618	        ]
619	      }
620	    ],
621	    "figures": [],
622	    "analysis": "Cross-model calibration 在 worst 档下呈现 model-dependency。Qwen family (7B + 1.5B) 近完美，但 DeepSeek ECE 比 Qwen 高 ~19x（0.0523 vs 0.0027）， CodeLlama 高 ~7x。这使 \"calibration as secondary evidence\" 从 universal finding 降级为 model-dependent finding。\n然而，calibration improvement ratio (exc vs no_trace) 在所有模型上都存在 （3.4x-63x），只是 magnitude model-dependent。论文可保留 \"exception signal improves calibration\" claim 但需加 \"magnitude varies across models\" qualifier。\nDeepSeek 的 poor calibration (ECE=0.0523) 与其 accuracy (99.33%) 的 disconnect 呼应 D1 (eval_loss vs accuracy decoupling)——token-level confidence 与 sample-level correctness decoupled。审稿人可能质疑: 如果 calibration 是 model-dependent 的，那 calibration evidence 对 Claim 1 的 supporting 作用 大打折扣。\n\n\nQwen-7B ECE=0.0027 已知（近完美）。\nQwen-1.5B: exception_only accuracy 与 7B 完全相同 (99.83%)，但 1.5B 的 logit 分布可能略 less peaked（smaller model capacity → slightly more uncertain probability outputs）。预测 ECE=0.0041，仍然 excellent。\nDeepSeek: 这是 worst 档的关键分歧点。DeepSeek exception_only seed42=99.33% （epoch3），但 epoch1=99.83%→epoch3=99.33% 的退化暗示 training 过程中 calibration 恶化。DeepSeek 的 LoRA 训练不稳定（seed123=91.09%）说明模型 的 probability landscape rugged。即使在 seed42 这个 \"好\" seed 上，model 的 predicted probabilities 可能 systematically miscalibrated——对 pass 样本 过度自信（many samples near 1.0 probability）但对 fail 样本 underconfident （several samples in 0.3-0.6 range instead of near 0.0），导致 ECE=0.0523。 这不是灾难性的 miscalibration，但与 Qwen 的 0.0027 相差 ~19x，破坏了 \"universal near-perfect calibration\" 的叙事。Brier=0.0318 也偏高—— 主要来自 8 个 error samples 的 high predicted pass probability。\nCodeLlama: accuracy=99.83%（与 Qwen 相同），但 CodeLlama 的 LLaMA 架构 在 code domain 的 confidence distribution 不同。ECE=0.0183 处于中等水平—— 优于 DeepSeek 但 ~7x worse than Qwen。可能原因: CodeLlama 虽然 accuracy 完美，但对少数 borderline samples 的 probability assignment 不够 extreme （predicts 0.85 instead of 0.99 for clear pass cases）。\n"
623	  },
624	  {
625	    "name": "few_shot_frontier_baseline",
626	    "description": "GPT-4o / Claude 直接判断 pass/fail (0-shot + 3-shot)，与 SFT exception_only 对比",
627	    "results": {
628	      "gpt4o": {
629	        "zero_shot_no_trace": {
630	          "accuracy": 0.823,
631	          "pass_f1": 0.876,
632	          "fail_f1": 0.687
633	        },
634	        "zero_shot_exception_only": {
635	          "accuracy": 0.955,
636	          "pass_f1": 0.97,
637	          "fail_f1": 0.918
638	        },
639	        "three_shot_exception_only": {
640	          "accuracy": 0.972,
641	          "pass_f1": 0.981,
642	          "fail_f1": 0.95
643	        }
644	      },
645	      "claude_sonnet": {
646	        "zero_shot_no_trace": {
647	          "accuracy": 0.808,
648	          "pass_f1": 0.862,
649	          "fail_f1": 0.667
650	        },
651	        "zero_shot_exception_only": {
652	          "accuracy": 0.948,
653	          "pass_f1": 0.965,
654	          "fail_f1": 0.908
655	        },
656	        "three_shot_exception_only": {
657	          "accuracy": 0.965,
658	          "pass_f1": 0.977,
659	          "fail_f1": 0.934
660	        }
661	      },
662	      "sft_exception_only_qwen7b": {
663	        "accuracy": 0.9983,
664	        "pass_f1": 0.999,
665	        "fail_f1": 0.997
666	      },
667	      "gap_best_fewshot_vs_sft_pp": 2.63,
668	      "gap_pvalue": 0.001,
669	      "api_cost_per_1190_samples_gpt4o": "$12-18",
670	      "sft_inference_cost_per_1190": "$0.02-0.05"
671	    },
672	    "tables": [
673	      {
674	        "name": "SFT vs Few-shot vs Zero-shot comparison",
675	        "data": [
676	          {
677	            "method": "SFT exception_only (Qwen-7B)",
678	            "accuracy": "99.83%",
679	            "cost_per_1190": "~$0.03",
680	            "latency_ms": "~50",
681	            "calibration_ece": 0.0027
682	          },
683	          {
684	            "method": "GPT-4o 3-shot + exception",
685	            "accuracy": "97.2%",
686	            "cost_per_1190": "~$15",
687	            "latency_ms": "~2000",
688	            "calibration_ece": "N/A (no logits)"
689	          },
690	          {
691	            "method": "GPT-4o 0-shot + exception",
692	            "accuracy": "95.5%",
693	            "cost_per_1190": "~$12",
694	            "latency_ms": "~2000",
695	            "calibration_ece": "N/A"
696	          },
697	          {
698	            "method": "Claude 3-shot + exception",
699	            "accuracy": "96.5%",
700	            "cost_per_1190": "~$10",
701	            "latency_ms": "~1800",
702	            "calibration_ece": "N/A"
703	          },
704	          {
705	            "method": "GPT-4o 0-shot no trace",
706	            "accuracy": "82.3%",
707	            "cost_per_1190": "~$8",
708	            "latency_ms": "~1500",
709	            "calibration_ece": "N/A"
710	          },
711	          {
712	            "method": "SFT no_trace (Qwen-7B)",
713	            "accuracy": "75.1%",
714	            "cost_per_1190": "~$0.02",
715	            "latency_ms": "~30",
716	            "calibration_ece": 0.1715
717	          }
718	        ]
719	      }
720	    ],
721	    "figures": [],
722	    "analysis": "在 worst 档下，few-shot baseline 是论文最大的 narrative threat 之一。 GPT-4o 3-shot 97.2% vs SFT 99.83% 的 2.63pp gap 虽 significant， 但审稿人会提出两个攻击:\n(1) \"如果 GPT-4o 加更多 examples 或 chain-of-thought 就能追上 SFT？\" → 无法反驳，因为我们没测。但 3-shot 已经 nearly saturated（0-shot 95.5% → 3-shot 97.2%, diminishing returns），extrapolation 不太可能到 99.8%。\n(2) \"SFT 的 marginal 2.63pp 不值得 training pipeline 的复杂度\" → 需用 cost argument (300x cheaper) + calibration argument (ECE=0.0027 vs GPT-4o no logits) + offline deployment 来反驳。\nReframe: few-shot 结果实际上 STRENGTHENS \"exception signal is key\" claim ——even frontier models benefit most from exception trace (+13pp for GPT-4o)。 SFT 的 advantage 是 practical (cost/calibration)，不是 signal discovery。 Signal discovery (exception > everything else) 是 universal finding， 无论 SFT 还是 prompting。\n\n\nGPT-4o 0-shot no_trace (82.3%): frontier model 可以从 code + test case 推断 correctness，但受限于 cannot actually execute code。类似我们的 no_trace baseline (75.13%)，但 GPT-4o 的 code understanding 远强于 Qwen-7B base， 因此 +7pp。\nGPT-4o 0-shot exception_only (95.5%): 给出 exception trace 后，GPT-4o 能 准确判断 \"[ERROR] TypeError\" → fail, \"[No exception]\" → pass。但 GPT-4o 在 borderline cases（如 GeneratorExit）的判断与 SFT 模型类似——看到 [ERROR] 就 倾向判 fail。同时 GPT-4o 对 exception_only format 未经微调，可能对某些 formatting 不够 sensitive，导致 ~4.5% error rate。\nGPT-4o 3-shot exception_only (97.2%): 3 个 examples 帮助 GPT-4o 理解 exception_only format 的 exact semantics，减少 formatting-related errors。 但仍有 ~2.8% error rate——主要来自 (1) GeneratorExit-like ambiguity, (2) multi-exception traces where GPT-4o must judge severity, (3) occasional refusal to make binary judgment on ambiguous cases。\nSFT gap (2.63pp): 虽小但 statistically significant (n=1190, p=0.001)。 然而审稿人会质疑: \"2.63pp 值得 SFT pipeline 的 engineering effort 吗?\"\nClaude Sonnet 略低于 GPT-4o (~0.7pp)，因为 code-specific training data 量可能略少。\nWorst 档影响: few-shot baseline 接近 SFT，削弱 \"SFT is necessary\" narrative。 但可以 reframe: (1) SFT 7B 的推理成本比 GPT-4o API 低 ~300x; (2) SFT calibration (ECE=0.0027) 远优于 GPT-4o prompt-based output; (3) SFT 可 offline deploy 无 API dependency; (4) 核心 finding 仍然 valid: exception signal 是 key，无论 SFT 还是 few-shot。\n"
723	  },
724	  {
725	    "name": "ood_generalization_test",
726	    "description": "在不同编程语言/项目的 trace 上测试 exception_only 泛化性",
727	    "results": {
728	      "python_ood_dataset": {
729	        "name": "LeetCode-style problems (different distribution from HumanEval/MBPP)",
730	        "exception_only": 0.871,
731	        "vota": 0.793,
732	        "no_trace": 0.682,
733	        "exception_lift_over_notrace": 0.189
734	      },
735	      "cross_language": {
736	        "feasibility": "NOT_FEASIBLE_WITHIN_TIMELINE",
737	        "reason": "需要新的 trace collection pipeline for Java/JS/C++; exception format 跨语言差异大"
738	      },
739	      "domain_shift_analysis": {
740	        "in_distribution_exc_accuracy": 0.9983,
741	        "ood_exc_accuracy": 0.871,
742	        "degradation_pp": 12.7,
743	        "relative_ordering_preserved": true,
744	        "exception_still_best_on_ood": true
745	      }
746	    },
747	    "tables": [
748	      {
749	        "name": "OOD generalization results",
750	        "data": [
751	          {
752	            "condition": "exception_only",
753	            "in_dist": "99.83%",
754	            "ood_python": "87.1%",
755	            "delta": "-12.7pp"
756	          },
757	          {
758	            "condition": "VOTA",
759	            "in_dist": "99.41%",
760	            "ood_python": "79.3%",
761	            "delta": "-20.1pp"
762	          },
763	          {
764	            "condition": "no_trace",
765	            "in_dist": "75.13%",
766	            "ood_python": "68.2%",
767	            "delta": "-6.9pp"
768	          }
769	        ]
770	      }
771	    ],
772	    "figures": [],
773	    "analysis": "OOD 泛化性在 worst 档下是 mixed 结果。正面: relative ordering preserved, exception_only 仍为最佳。负面: 12.7pp degradation 说明 exception_only 的 near-perfect in-distribution accuracy 部分依赖于 HumanEval/MBPP 的 exception pattern 分布（dominated by TypeError, ValueError, AssertionError）， 对 unseen exception types 的 generalization 有限。\n对论文的影响: OOD 结果不应放入 main paper（太弱），只在 Discussion 提 generalization limitation + future work。跨语言完全不可行，成为 explicit limitation。审稿人关于 \"single task, single dataset\" 的 concern 在 OOD 数据上部分证实——exception signal 的 universality 限于 similar exception distributions。\n\n\nPython OOD (LeetCode-style): 训练数据来自 HumanEval + MBPP-sanitized (591 problems)，这些是 relatively simple、well-defined 的编程题。LeetCode-style problems 更复杂（涉及 DP, graph algorithms, complex data structures）， exception patterns 可能包含 training 未见过的 error types (e.g., RecursionError, MemoryError, complex nested exceptions)。\nexception_only 87.1%: 下降 12.7pp 因为 (1) unseen exception types —— 模型 对 RecursionError 等 training 中罕见的 exception 缺乏 calibrated 判断; (2) OOD problems 的 pass/fail 比例可能不同 (training = 71.5% pass); (3) LeetCode problems 可能有 time limit exceeded 等 non-exception failures ——代码不抛异常但 output 错误——exception_only 表征中这些显示为 \"[No exception]\" 但 label=fail，模型在 OOD 上对这类 pattern 的 confusion 更大。\nVOTA 79.3%: 更大的 degradation (20.1pp) 因为 VOTA 的 loop compression 和 ae extraction 对 LeetCode trace 结构的 assumption 不 match—— complex data structures 的 trace 不 follow 简单的 loop iteration pattern。\nno_trace 68.2%: 下降 7pp，说明 LeetCode problems 本身 harder（更难从 code alone 判断 correctness），但 degradation 较小因为 no_trace 的 ceiling 本来就低。\nRelative ordering preserved (exception > VOTA > no_trace) 是正面信号—— 说明 exception dominance 的 conclusion generalizes even if absolute numbers drop。但 12.7pp degradation 被审稿人 ammunition: \"model overfits to HumanEval/MBPP exception distribution\"。\nCross-language (Java/JS/C++): 在 deadline 前 NOT FEASIBLE。需要: (1) trace collection infrastructure per language (Java Jacoco/bytecode, JS Istanbul, C++ sanitizers); (2) exception format normalization (Java stack traces ≠ Python tracebacks); (3) test suite per language。 估计 3-4 weeks 工作量。\n"
774	  },
775	  {
776	    "name": "training_dynamics_comparison",
777	    "description": "exception_only vs full_trace 的 learning curve (每 50 steps eval)",
778	    "results": {
779	      "exception_only_curve": {
780	        "step_0": 0.5,
781	        "step_50": 0.962,
782	        "step_100": 0.991,
783	        "step_150": 0.995,
784	        "step_200": 0.998,
785	        "step_250": 0.998,
786	        "convergence_step": 100
787	      },
788	      "full_trace_curve": {
789	        "step_0": 0.5,
790	        "step_50": 0.721,
791	        "step_100": 0.768,
792	        "step_150": 0.803,
793	        "step_200": 0.812,
794	        "step_250": 0.818,
795	        "convergence_step": 200
796	      },
797	      "speed_ratio": 2.0,
798	      "exception_step50_vs_full_converged": "+14.4pp",
799	      "curve_noise": {
800	        "exception_only_step_std": 0.003,
801	        "full_trace_step_std": 0.018
802	      }
803	    },
804	    "tables": [
805	      {
806	        "name": "Learning curve milestones",
807	        "data": [
808	          {
809	            "condition": "exception_only",
810	            "step_50": "96.2%",
811	            "step_100": "99.1%",
812	            "step_200": "99.8%",
813	            "final": "99.83%",
814	            "converge_step": 100
815	          },
816	          {
817	            "condition": "full_trace",
818	            "step_50": "72.1%",
819	            "step_100": "76.8%",
820	            "step_200": "81.2%",
821	            "final": "81.8%",
822	            "converge_step": 200
823	          },
824	          {
825	            "condition": "no_trace",
826	            "step_50": "71.5%",
827	            "step_100": "73.8%",
828	            "step_200": "75.0%",
829	            "final": "75.1%",
830	            "converge_step": 150
831	          }
832	        ]
833	      }
834	    ],
835	    "figures": [],
836	    "analysis": "Training dynamics 在 worst 档下提供 supporting evidence 但不够强作为 独立 contribution。核心 finding (exception_only 收敛更快) 是 expected 且 trivial——simpler signal naturally easier to learn。2x speed ratio 不够 dramatic（如果是 10x 则更有 narrative value）。\n对论文的影响: 可在 Appendix 放 learning curve figure 作为 supplementary evidence for Claim 2 (information density)。但不应作为 main result—— 审稿人会说 \"of course simpler signals converge faster, this is not a contribution\"。\n唯一 novel 的 data point: exception_only step 50 (96.2%) > full_trace final (81.8%)。这意味着 exception_only 在仅 1/6 的训练时间内就超越了 full_trace 的 theoretical ceiling。可以用一句话在 Results 中提及， 但不值得 dedicated subsection。\n\nexception_only: signal 结构简单（[ERROR] type: ... 或 [No exception]）， 模型在 ~50 steps 即能学到 binary mapping（有 exception → fail, 无 → pass）， 此后 refinement 主要是 calibration improvement 和 edge cases。Step 50 的 96.2% 已经超过 full_trace 的最终 converged accuracy (81.8%)。 这支持 information density 假说——exception signal 的 signal-to-noise ratio 极高，学习效率自然高。\nfull_trace: 模型需要从 long, noisy traces 中学到什么是 relevant， 这本身就是一个 learning problem。Step 50 时模型刚开始区分 trace structure (72.1%≈no_trace baseline + few pp)，到 step 200 才稳定在 ~82%。 Step-to-step variance (std=0.018 per step) 比 exception_only (0.003) 高 6x， 说明 full_trace 的 optimization landscape 更 noisy。\nSpeed ratio 2x: exception_only 在 ~100 steps converge，full_trace 在 ~200 steps。ratio 只有 2x（不是 10x）因为两者都使用相同的 LoRA rank 和 learning rate——exception_only 的主要优势是 ceiling height (99.83% vs 81.8%)，不是 convergence speed 本身。\nWorst 档 caveat: curves are noisy（尤其 full_trace），step-to-step fluctuations 使 figure 不够 clean for publication。exception_only curve 在 step 50 之后几乎 flat（从 96.2% → 99.8%，3.6pp over 200 steps）， 作为 learning curve figure 不 visually interesting。\n"
837	  }
838	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91dc17c2-afc8-42b0-bfcb-090e4b1e5670",
  "isSidechain": false,
  "promptId": "cde04d7b-c03d-49ea-b3f7-a9fea2ed96f5",
  "type": "user",
  "uuid": "824bcef7-4b96-41b4-ab30-20fb4169856c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"qwen7b_full_trace_tail384_seed42\",\n    \"description\": \"Qwen-2.5-Coder-7B tail-384 truncation，定位 256→512 transition 位置\",\n    \"results\": {\n      \"accuracy\": 0.847,\n      \"accuracy_ci_lower\": 0.826,\n      \"accuracy_ci_upper\": 0.868,\n      \"majority_baseline\": 0.7151,\n      \"lift_over_majority\": 0.132,\n      \"pass_precision\": 0.905,\n      \"pass_recall\": 0.875,\n      \"pass_f1\": 0.89,\n      \"fail_precision\": 0.71,\n      \"fail_recall\": 0.78,\n      \"fail_f1\": 0.743,\n      \"n_test\": 1190,\n      \"train_loss\": 0.088,\n      \"eval_loss\": 0.41\n    },\n    \"tables\": [\n      {\n        \"name\": \"Qwen-7B budget curve (updated)\",\n        \"data\": [\n          {\n            \"length\": \"tail-256\",\n            \"accuracy\": \"77.48%\",\n            \"delta_vs_prev\": \"—\"\n          },\n          {\n            \"length\": \"tail-384\",\n            \"accuracy\": \"84.7%\",\n            \"delta_vs_prev\": \"+7.2pp\"\n          },\n          {\n            \"length\": \"tail-512\",\n            \"accuracy\": \"93.6%\",\n            \"delta_vs_prev\": \"+8.9pp\"\n          },\n          {\n            \"length\": \"tail-1024\",\n            \"accuracy\": \"96.5%\",\n            \"delta_vs_prev\": \"+2.9pp\"\n          },\n          {\n            \"length\": \"tail-2048\",\n            \"accuracy\": \"97.3%\",\n            \"delta_vs_prev\": \"+0.8pp\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Qwen-7B 是 4 模型中唯一呈现 clean monotonic + gradual transition 的模型。 然而 \\\"gradual\\\" 意味着无法定义 discrete phase transition point，削弱 \\\"sharp phase transition\\\" claim。如果其他模型也 gradual 则可声称 universal gradual pattern；但其他模型模式不同，Qwen-7B 的 gradual 反而成为 model-specific behavior 的证据。\\n\\n\\nQwen-7B tail-256=77.48%, tail-512=93.6%。384 tokens 在 worst 档下处于 transition 中段——提供了约 50% 的 tail-end diagnostic content（包含部分 exception/assertion 数据 但不完整）。Qwen-7B 的 LoRA landscape 平滑（3-seed exception_only variance=0）， 因此即使在 noisy intermediate length 上也能稳定学到部分模式。但 384 tokens 不足以 覆盖多数 fail 样本的完整 exception trace（exception 通常在 trace 最后 200-500 tokens）， 导致 ~50% 的 fail 样本 exception 信息被截断。结果: gradual rise，interpolating between 256 and 512，约 84.7%。这使 Qwen-7B 成为 \\\"gradual transition\\\" 模式的代表—— 与 Qwen-1.5B 的 sharp transition 形成对比，破坏 universal pattern 叙事。\\n\"\n  },\n  {\n    \"name\": \"qwen15b_full_trace_tail384_seed42\",\n    \"description\": \"Qwen-2.5-Coder-1.5B tail-384，验证小模型 transition timing\",\n    \"results\": {\n      \"accuracy\": 0.745,\n      \"accuracy_ci_lower\": 0.72,\n      \"accuracy_ci_upper\": 0.769,\n      \"majority_baseline\": 0.7151,\n      \"lift_over_majority\": 0.03,\n      \"pass_precision\": 0.835,\n      \"pass_recall\": 0.81,\n      \"pass_f1\": 0.822,\n      \"fail_precision\": 0.545,\n      \"fail_recall\": 0.59,\n      \"fail_f1\": 0.567,\n      \"n_test\": 1190,\n      \"train_loss\": 0.25,\n      \"eval_loss\": 0.56\n    },\n    \"tables\": [\n      {\n        \"name\": \"Qwen-1.5B budget curve (updated)\",\n        \"data\": [\n          {\n            \"length\": \"tail-256\",\n            \"accuracy\": \"72.6%\",\n            \"delta_vs_prev\": \"—\"\n          },\n          {\n            \"length\": \"tail-384\",\n            \"accuracy\": \"74.5%\",\n            \"delta_vs_prev\": \"+1.9pp\"\n          },\n          {\n            \"length\": \"tail-512\",\n            \"accuracy\": \"95.6%\",\n            \"delta_vs_prev\": \"+21.1pp\"\n          },\n          {\n            \"length\": \"tail-1024\",\n            \"accuracy\": \"96.6%\",\n            \"delta_vs_prev\": \"+1.0pp\"\n          },\n          {\n            \"length\": \"tail-2048\",\n            \"accuracy\": \"97.9%\",\n            \"delta_vs_prev\": \"+1.3pp\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Qwen-1.5B 的 sharp transition 说明小模型的 information utilization threshold 更高——384 tokens 的 partial trace 对 1.5B 几乎无用，但 512 tokens 突然 提供了 sufficient signal。这与 exception_only 的 scale-invariance（1.5B=7B=99.83%） 形成 interesting 对比：exception signal 因其 structural simplicity 对模型容量 无要求，但 full_trace 的 utilization threshold 是 capacity-dependent。然而 这一 finding 无法 universalize——同 scale/同 family 的 7B 模型呈现完全不同 的 gradual pattern。\\n\\n\\nQwen-1.5B tail-256=72.6%, tail-512=95.6%。这个模型在 exception_only 上 与 7B 完全一致（99.83%），但在 noisy full_trace 上更脆弱（head-2048 仅 75.3% vs 7B 的 81.6%）。1.5B 模型容量有限，需要更完整的 diagnostic signal 才能 学到有用模式——384 tokens 提供的 partial information 对它来说 insufficient， 无法从噪声中提取信号。结果: 仅比 tail-256 提升 ~2pp，仍接近 baseline。 真正的 phase transition 发生在 384→512 之间（+21pp 的巨大跳跃），显示 512 tokens 是该模型的 critical threshold——刚好覆盖大多数 fail 样本的完整 exception + assertion 信息。这是 \\\"sharp transition\\\" 模式，但 threshold 位置 (384-512) 与 Qwen-7B 的 gradual zone 不同。\\n\"\n  },\n  {\n    \"name\": \"deepseek_full_trace_tail384_seed42\",\n    \"description\": \"DeepSeek-Coder-6.7B tail-384，验证 alternative architecture transition\",\n    \"results\": {\n      \"accuracy\": 0.883,\n      \"accuracy_ci_lower\": 0.863,\n      \"accuracy_ci_upper\": 0.902,\n      \"majority_baseline\": 0.7151,\n      \"lift_over_majority\": 0.168,\n      \"pass_precision\": 0.92,\n      \"pass_recall\": 0.915,\n      \"pass_f1\": 0.917,\n      \"fail_precision\": 0.792,\n      \"fail_recall\": 0.805,\n      \"fail_f1\": 0.798,\n      \"n_test\": 1190,\n      \"train_loss\": 0.15,\n      \"eval_loss\": 0.38\n    },\n    \"tables\": [\n      {\n        \"name\": \"DeepSeek budget curve (updated)\",\n        \"data\": [\n          {\n            \"length\": \"tail-256\",\n            \"accuracy\": \"76.4%\",\n            \"delta_vs_prev\": \"—\"\n          },\n          {\n            \"length\": \"tail-384\",\n            \"accuracy\": \"88.3%\",\n            \"delta_vs_prev\": \"+11.9pp\"\n          },\n          {\n            \"length\": \"tail-512\",\n            \"accuracy\": \"93.9%\",\n            \"delta_vs_prev\": \"+5.6pp\"\n          },\n          {\n            \"length\": \"tail-1024\",\n            \"accuracy\": \"96.5%\",\n            \"delta_vs_prev\": \"+2.6pp\"\n          },\n          {\n            \"length\": \"tail-2048\",\n            \"accuracy\": \"95.0%\",\n            \"delta_vs_prev\": \"-1.5pp\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"DeepSeek 的 early-onset transition 与 Qwen 两模型模式都不同。可能原因: (1) tokenizer efficiency 不同导致同 token 数覆盖不同内容量； (2) 预训练数据差异导致 trace 理解的 readiness 不同。 tail-2048 的轻微 regression 虽小（-1.5pp, 可能在 CI 内），但与 CodeLlama 的灾难性 regression 构成连续谱，暗示 long-context full_trace 对 SFT 有普遍 的 diminishing/negative returns 趋势——但程度完全 model-specific。\\n\\n\\nDeepSeek tail-256=76.4%, tail-512=93.9%。DeepSeek tokenizer 在 tail 区域 的 token density 不同于 Qwen（不同 BPE vocabulary），384 DeepSeek tokens 覆盖更多字符内容。加之 DeepSeek 在 full_trace 条件下对 fail 模式的学习 更快（tail-2048 已 95%），transition 更早发生。88.3% 说明 DeepSeek 在 384 tokens 时已经获得了大部分 diagnostic information——与 Qwen-7B (84.7%) 和 Qwen-1.5B (74.5%) 形成第三种不同模式：\\\"early-onset transition\\\"。但这也暴露了 DeepSeek tail-2048 (95.0%) 相对 tail-1024 (96.5%) 的轻微非单调性—— longer context 引入 noise。整体模式: 提前进入 transition + 后端轻微 regression。\\n\"\n  },\n  {\n    \"name\": \"codellama13b_full_trace_tail384_seed42\",\n    \"description\": \"CodeLlama-13B-Instruct tail-384，验证 LLaMA family transition\",\n    \"results\": {\n      \"accuracy\": 0.735,\n      \"accuracy_ci_lower\": 0.711,\n      \"accuracy_ci_upper\": 0.76,\n      \"majority_baseline\": 0.7151,\n      \"lift_over_majority\": 0.02,\n      \"pass_precision\": 0.8,\n      \"pass_recall\": 0.845,\n      \"pass_f1\": 0.822,\n      \"fail_precision\": 0.555,\n      \"fail_recall\": 0.458,\n      \"fail_f1\": 0.502,\n      \"n_test\": 1190,\n      \"train_loss\": 0.28,\n      \"eval_loss\": 0.62\n    },\n    \"tables\": [\n      {\n        \"name\": \"CodeLlama budget curve (updated)\",\n        \"data\": [\n          {\n            \"length\": \"tail-256\",\n            \"accuracy\": \"77.9%\",\n            \"delta_vs_prev\": \"—\"\n          },\n          {\n            \"length\": \"tail-384\",\n            \"accuracy\": \"73.5%\",\n            \"delta_vs_prev\": \"-4.4pp ⚠️\"\n          },\n          {\n            \"length\": \"tail-512\",\n            \"accuracy\": \"97.5%\",\n            \"delta_vs_prev\": \"+24.0pp\"\n          },\n          {\n            \"length\": \"tail-1024\",\n            \"accuracy\": \"98.2%\",\n            \"delta_vs_prev\": \"+0.7pp\"\n          },\n          {\n            \"length\": \"tail-2048\",\n            \"accuracy\": \"41.8%\",\n            \"delta_vs_prev\": \"-56.4pp ⚠️\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CodeLlama 的 multi-point anomaly 使 budget curve 作为 universal contribution 彻底失效。任何试图 fit a universal curve 的尝试都会被 CodeLlama 的 W-shape 击碎。 审稿人会质疑 training pipeline 健壮性——为什么同一 codebase 对 CodeLlama 产生如此不稳定的结果？回应策略: (1) 诚实报告所有数据; (2) 指出 CodeLlama 的 LLaMA tokenizer 与 code-specific tokenizers (Qwen/DeepSeek) 的效率差异导致 同 token 数对应不同 content coverage; (3) 将 CodeLlama 的 instability 作为 \\\"why simplicity matters\\\" 的反面论据——exception_only 在 CodeLlama 上 99.83% 完美，不受 length budget 影响。\\n\\n\\nCodeLlama tail-256=77.9%, tail-512=97.5%。在 worst 档下 CodeLlama tail-384 出现 anomalous dip——accuracy 73.5% 低于 tail-256 (77.9%) 4.4pp。根因假说: CodeLlama tokenizer 在 384-token window 内截取到 trace 中间位置的 ambiguous content（包含 partial loop iterations 但 exception 被截断），形成比 tail-256 更具误导性的输入。tail-256 因内容极少反而让模型回退到 no_trace-like 的保守策略 （~78%≈no_trace+few pp），而 tail-384 提供了 \\\"just enough to be dangerous\\\" 的 partial information——模型看到了 execution trace 但缺少 diagnostic conclusion， 导致 fail_recall 大幅下降 (0.458)。这与 CodeLlama 在 tail-2048 (41.8%) 的 catastrophic failure 以及 tail-1024 v2 的不稳定 (87.6%) 构成系统性 pattern: CodeLlama 对 intermediate-noise trace 特别脆弱。\\n\"\n  },\n  {\n    \"name\": \"plan_016_cross_model_synthesis\",\n    \"description\": \"tail-384 × 4 模型交叉分析: phase transition 模式分裂总结\",\n    \"results\": {\n      \"tail384_cross_model_std_pp\": 6.4,\n      \"tail384_cross_model_range_pp\": 14.8,\n      \"phase_transition_sharpness\": 0.2,\n      \"budget_curve_consistent_models\": 1,\n      \"transition_patterns\": {\n        \"qwen7b\": \"gradual_monotonic\",\n        \"qwen15b\": \"sharp_delayed\",\n        \"deepseek\": \"early_onset_with_tail_regression\",\n        \"codellama\": \"non_monotonic_W_shape\"\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Cross-model tail-384 comparison\",\n        \"data\": [\n          {\n            \"model\": \"Qwen-7B\",\n            \"tail256\": \"77.5%\",\n            \"tail384\": \"84.7%\",\n            \"tail512\": \"93.6%\",\n            \"delta_256_384\": \"+7.2pp\",\n            \"delta_384_512\": \"+8.9pp\",\n            \"pattern\": \"gradual\"\n          },\n          {\n            \"model\": \"Qwen-1.5B\",\n            \"tail256\": \"72.6%\",\n            \"tail384\": \"74.5%\",\n            \"tail512\": \"95.6%\",\n            \"delta_256_384\": \"+1.9pp\",\n            \"delta_384_512\": \"+21.1pp\",\n            \"pattern\": \"sharp_delayed\"\n          },\n          {\n            \"model\": \"DeepSeek\",\n            \"tail256\": \"76.4%\",\n            \"tail384\": \"88.3%\",\n            \"tail512\": \"93.9%\",\n            \"delta_256_384\": \"+11.9pp\",\n            \"delta_384_512\": \"+5.6pp\",\n            \"pattern\": \"early_onset\"\n          },\n          {\n            \"model\": \"CodeLlama\",\n            \"tail256\": \"77.9%\",\n            \"tail384\": \"73.5%\",\n            \"tail512\": \"97.5%\",\n            \"delta_256_384\": \"-4.4pp\",\n            \"delta_384_512\": \"+24.0pp\",\n            \"pattern\": \"non_monotonic\"\n          }\n        ]\n      },\n      {\n        \"name\": \"Full budget curve matrix (all models)\",\n        \"data\": [\n          {\n            \"model\": \"Qwen-7B\",\n            \"t256\": \"77.5\",\n            \"t384\": \"84.7\",\n            \"t512\": \"93.6\",\n            \"t1024\": \"96.5\",\n            \"t2048\": \"97.3\",\n            \"monotonic\": \"✓\",\n            \"pattern\": \"gradual S-curve\"\n          },\n          {\n            \"model\": \"Qwen-1.5B\",\n            \"t256\": \"72.6\",\n            \"t384\": \"74.5\",\n            \"t512\": \"95.6\",\n            \"t1024\": \"96.6\",\n            \"t2048\": \"97.9\",\n            \"monotonic\": \"✓\",\n            \"pattern\": \"step function at 512\"\n          },\n          {\n            \"model\": \"DeepSeek\",\n            \"t256\": \"76.4\",\n            \"t384\": \"88.3\",\n            \"t512\": \"93.9\",\n            \"t1024\": \"96.5\",\n            \"t2048\": \"95.0\",\n            \"monotonic\": \"✗\",\n            \"pattern\": \"early rise + tail regression\"\n          },\n          {\n            \"model\": \"CodeLlama\",\n            \"t256\": \"77.9\",\n            \"t384\": \"73.5\",\n            \"t512\": \"97.5\",\n            \"t1024\": \"98.2\",\n            \"t2048\": \"41.8\",\n            \"monotonic\": \"✗\",\n            \"pattern\": \"W-shape with 2 anomalies\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Budget curve 作为 contribution 在 worst 档下完全失效。4 模型 4 种模式， 无法声称 \\\"trace length has a universal effect on verdict accuracy\\\"。 唯一 universal 的 finding 是 exception_only (99.83%) 在所有模型上不受 length budget 影响——这反而强化了 \\\"simplicity is robustness\\\" 的 headline。 Budget curve 应移至 Appendix，仅作为 \\\"why exception_only is preferable\\\" 的 supporting evidence：同 token budget 下 full_trace 的效果完全不可预测， 而 exception_only 无此问题。\\n\\n\\n4 模型呈现 4 种不同的 budget curve 形态。phase_transition_sharpness=0.2 因为 只有 Qwen-1.5B 显示真正的 sharp transition (tail-384→512 跳 21pp)，其他 模型要么 gradual (Qwen-7B)、要么 early-onset (DeepSeek)、要么 anomalous (CodeLlama)。budget_curve_consistent_models=1 因为只有 Qwen-7B 呈现 clean monotonic pattern（DeepSeek 有 tail regression, CodeLlama 有两处 anomaly, Qwen-1.5B 虽 monotonic 但 step-function 形态不同于 Qwen-7B 的 gradual）。 Cross-model std=6.4pp 在 [5,12] 范围内。这证明 budget curve 形态是 model-specific 的——无法提炼 universal trace-length → accuracy pattern。\\n\"\n  },\n  {\n    \"name\": \"cross_seed_budget_curve_tail512\",\n    \"description\": \"tail-512 × 4 models × 3 seeds，验证 phase transition 后 convergence band robustness\",\n    \"results\": {\n      \"qwen7b\": {\n        \"seed42\": 0.936,\n        \"seed123\": 0.924,\n        \"seed456\": 0.931,\n        \"mean\": 0.93,\n        \"std_pp\": 0.6,\n        \"range_pp\": 1.2\n      },\n      \"qwen15b\": {\n        \"seed42\": 0.956,\n        \"seed123\": 0.908,\n        \"seed456\": 0.942,\n        \"mean\": 0.935,\n        \"std_pp\": 2.5,\n        \"range_pp\": 4.8\n      },\n      \"deepseek\": {\n        \"seed42\": 0.939,\n        \"seed123\": 0.876,\n        \"seed456\": 0.919,\n        \"mean\": 0.911,\n        \"std_pp\": 3.2,\n        \"range_pp\": 6.3\n      },\n      \"codellama\": {\n        \"seed42\": 0.975,\n        \"seed123\": 0.809,\n        \"seed456\": 0.943,\n        \"mean\": 0.909,\n        \"std_pp\": 8.7,\n        \"range_pp\": 16.6\n      },\n      \"overall_cross_model_seed_std_mean\": 3.75\n    },\n    \"tables\": [\n      {\n        \"name\": \"tail-512 × 4 models × 3 seeds\",\n        \"data\": [\n          {\n            \"model\": \"Qwen-7B\",\n            \"seed42\": \"93.6%\",\n            \"seed123\": \"92.4%\",\n            \"seed456\": \"93.1%\",\n            \"mean\": \"93.0%\",\n            \"std\": \"0.6pp\",\n            \"verdict\": \"✓ robust\"\n          },\n          {\n            \"model\": \"Qwen-1.5B\",\n            \"seed42\": \"95.6%\",\n            \"seed123\": \"90.8%\",\n            \"seed456\": \"94.2%\",\n            \"mean\": \"93.5%\",\n            \"std\": \"2.5pp\",\n            \"verdict\": \"△ moderate\"\n          },\n          {\n            \"model\": \"DeepSeek\",\n            \"seed42\": \"93.9%\",\n            \"seed123\": \"87.6%\",\n            \"seed456\": \"91.9%\",\n            \"mean\": \"91.1%\",\n            \"std\": \"3.2pp\",\n            \"verdict\": \"△ moderate\"\n          },\n          {\n            \"model\": \"CodeLlama\",\n            \"seed42\": \"97.5%\",\n            \"seed123\": \"80.9%\",\n            \"seed456\": \"94.3%\",\n            \"mean\": \"90.9%\",\n            \"std\": \"8.7pp\",\n            \"verdict\": \"✗ unstable\"\n          }\n        ]\n      },\n      {\n        \"name\": \"对比: exception_only seed robustness\",\n        \"data\": [\n          {\n            \"model\": \"Qwen-7B\",\n            \"exc_std\": \"0.00pp\",\n            \"tail512_std\": \"0.6pp\",\n            \"ratio\": \"∞\"\n          },\n          {\n            \"model\": \"Qwen-1.5B\",\n            \"exc_std\": \"0.00pp (单 seed)\",\n            \"tail512_std\": \"2.5pp\",\n            \"ratio\": \"—\"\n          },\n          {\n            \"model\": \"DeepSeek\",\n            \"exc_std\": \"4.8pp\",\n            \"tail512_std\": \"3.2pp\",\n            \"ratio\": \"0.67\"\n          },\n          {\n            \"model\": \"CodeLlama\",\n            \"exc_std\": \"0.10pp\",\n            \"tail512_std\": \"8.7pp\",\n            \"ratio\": \"87x\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cross-seed robustness 进一步削弱 budget curve contribution。即使在 tail-512 这个 \\\"transition 后最稳定\\\" 的点，4 模型中只有 Qwen-7B 真正 seed-robust。 CodeLlama 的 σ=8.7pp 使其 single-seed 数据完全不可信——97.5% 可能只是 lucky seed。这意味着论文中报告的所有 single-seed budget curve 数据点都有 潜在的 seed noise 问题，但我们不可能为每个 length × model 组合都跑 3 seeds （预算 24 GPU-hours 只够 tail-512 这一个点）。\\n对论文的影响: (1) budget curve 的可信度进一步下降——不仅 model-specific， 还 seed-sensitive; (2) exception_only 的 seed robustness（Qwen 0pp, CodeLlama 0.1pp）与 full_trace tail-512 的 seed variance（CodeLlama 8.7pp）形成 87x 的对比，成为 \\\"simplicity enables robustness\\\" 的额外弹药; (3) 建议 仅在 Appendix 报告 tail-512 seed data，不 support 任何 main claim。\\n\\n\\ntail-512 是 transition 后的第一个 \\\"高 accuracy\\\" 点，但在 worst 档下 seed robustness 与 signal complexity 正相关。exception_only（最简信号）seed variance 已知: Qwen 0pp, DeepSeek 4.8pp (σ)。full_trace tail-512 的 signal 远比 exception_only complex（包含 loop iterations, variable states, partial traces）， 因此 seed sensitivity 应更严重。\\nQwen-7B: LoRA landscape 平滑（exception_only 3-seed variance=0），tail-512 的 seed variance 也最小（σ=0.6pp）。但即使 Qwen-7B 也有 ~1pp 波动—— full_trace 信号的 noise 导致不同 seed 的 LoRA 从 trace 中学到略微不同的 patterns。\\nQwen-1.5B: 容量限制放大 seed sensitivity。在 exception_only 上 scale-invariant (99.83%)，但 full_trace 依赖 execution reasoning——1.5B 的 reasoning 容量 有限，seed123 未能充分学到 trace→verdict 映射。σ=2.5pp，moderate。\\nDeepSeek: 已知 LoRA initialization sensitivity（exception_only seed123=91.09% vs seed42/456=99.33%）。full_trace 放大此效应。seed123 再次成为 outlier (87.6%)，但 gap 不如 exception_only 的 seed123 极端——因为 full_trace 的 ceiling 本身较低（~94%），outlier seed 的退化空间也较小。σ=3.2pp。\\nCodeLlama: training instability 的系统性问题。已知 tail-1024 有 run-to-run variance (87.6% vs 98.2%)，tail-2048 catastrophic。tail-512 虽然是 CodeLlama 的 \\\"sweet spot\\\"（single seed=97.5%），但 seed variance 极大——seed123 仅 80.9%，几乎 17pp 退化。根因: CodeLlama 的 LLaMA tokenizer 对 code trace 的 tokenization 效率低，512 tokens 覆盖内容较少，不同 seed 的 LoRA 可能 focus on different trace regions，导致 catastrophic divergence。σ=8.7pp 使 CodeLlama 的 budget curve 在 seed 维度也不 robust。\\n\"\n  },\n  {\n    \"name\": \"error_analysis_cross_condition\",\n    \"description\": \"用已有 predictions.jsonl 分析 4 条件的 failure modes\",\n    \"results\": {\n      \"exception_only_errors\": {\n        \"total\": 2,\n        \"all_generatorexit\": true,\n        \"sample_ids\": [\n          901,\n          905\n        ],\n        \"function\": \"check_dict_case (HumanEval/95)\",\n        \"error_direction\": \"pass→fail (false negative)\",\n        \"cross_seed_overlap\": \"100% (3/3 seeds identical)\"\n      },\n      \"vota_errors\": {\n        \"total\": 7,\n        \"categories\": {\n          \"generatorexit\": 2,\n          \"long_trace_attention_dilution\": 3,\n          \"ambiguous_loop_pattern\": 2\n        },\n        \"false_negative_rate\": 0.71,\n        \"overlap_with_exception_only\": 2\n      },\n      \"full_trace_errors\": {\n        \"total\": 217,\n        \"categories\": {\n          \"long_program_overload\": 142,\n          \"edge_case_subtle_bug\": 38,\n          \"correct_but_verbose_trace\": 22,\n          \"random_noise\": 15\n        },\n        \"false_negative_rate\": 0.62,\n        \"median_trace_length_errors_vs_correct\": \"2.3x longer\"\n      },\n      \"no_trace_errors\": {\n        \"total\": 296,\n        \"categories\": {\n          \"subtle_functional_bugs\": 108,\n          \"edge_case_only_failures\": 87,\n          \"correct_format_wrong_logic\": 63,\n          \"random\": 38\n        },\n        \"false_negative_rate\": 0.55,\n        \"fail_recall\": 0.735\n      },\n      \"cross_condition_overlap\": {\n        \"exc_intersect_vota\": 0.286,\n        \"vota_intersect_full\": 0.714,\n        \"full_intersect_no_trace\": 0.691,\n        \"exc_intersect_no_trace\": 0.007\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Error category distribution\",\n        \"data\": [\n          {\n            \"condition\": \"exception_only\",\n            \"n_errors\": 2,\n            \"primary_category\": \"GeneratorExit (100%)\",\n            \"actionable\": \"No (irreducible)\"\n          },\n          {\n            \"condition\": \"VOTA\",\n            \"n_errors\": 7,\n            \"primary_category\": \"Mixed (GenExit 29% / attention dilution 43% / ambiguous loop 29%)\",\n            \"actionable\": \"Partial\"\n          },\n          {\n            \"condition\": \"full_trace\",\n            \"n_errors\": 217,\n            \"primary_category\": \"Long-trace overload (65%)\",\n            \"actionable\": \"Not without architecture change\"\n          },\n          {\n            \"condition\": \"no_trace\",\n            \"n_errors\": 296,\n            \"primary_category\": \"Subtle bugs undetectable from code alone (37%)\",\n            \"actionable\": \"No (inherent limitation)\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Error analysis 在 worst 档下产出有限。exception_only 的 2 个 error 已在 irreducible error analysis (D5) 中完全解析——无新 finding。VOTA 的 7 个 error 异质但数量太少不支撑 statistical analysis。full_trace 的 217 个 error 有 pattern（long traces dominant）但这是 Claim 2 已覆盖的 information overload finding 的 restatement。no_trace 的 296 个 error 说明 baseline 弱但无新 insight。\\nCross-condition overlap 低本身是 interesting finding（不同 representations fail on orthogonal dimensions），但在 worst 档下这无法 crystallize into a clean narrative。建议: 仅在 Appendix 放 error breakdown table，Discussion 简短提及 orthogonal failure modes 现象。不值得作为独立 contribution。\\n\\n\\nexception_only: 2 errors 已知且不可约（GeneratorExit），不提供新 insight。\\nVOTA: 7 errors 分为三类。(1) 2 个与 exception_only 重叠的 GeneratorExit—— inherited from Tier 1。(2) 3 个 long-trace samples 中 loop/ae tokens 稀释了 exception signal 的 attention——这些样本在 exception_only 下正确但 VOTA 下 错误，直接支持 \\\"Tier 2 introduces noise\\\" claim。(3) 2 个 ambiguous loop patterns——loop 正常但有 exception，模型对 conflicting signals 做出错误判断。 这 7 个 error 的异质性使其无法归为单一 category。\\nfull_trace: 217 errors 高度异质。最大类 (142/217) 是 long programs 的 information overload——trace 太长模型无法有效处理。38 个 edge case 中模型 看到了 trace 但未能正确 interpret 细微的 bug pattern。22 个 correct but verbose——trace 的冗余信息误导模型预测 fail。这种高异质性使 error analysis 难以 yield actionable insight。\\nno_trace: 296 errors 中最大类是 subtle functional bugs (108)——没有 trace 时模型仅能依赖 code structure/style heuristics，对逻辑正确但风格 unusual 的 代码也会误判。fail_recall 仅 0.735 说明 ~27% 的 fail 样本被漏判。\\nCross-condition overlap 低: exception_only 的 2 个 error 仅在 VOTA 的 7 个 error 中出现 2 个（28.6%），说明不同条件的 failure modes 几乎不重叠—— 它们 fail on fundamentally different samples for fundamentally different reasons。\\n\"\n  },\n  {\n    \"name\": \"cross_model_calibration_exception_only\",\n    \"description\": \"4 模型 × exception_only 的 ECE/Brier 对比\",\n    \"results\": {\n      \"qwen7b\": {\n        \"ece\": 0.0027,\n        \"brier\": 0.0013,\n        \"mce\": 0.835,\n        \"accuracy\": 0.9983\n      },\n      \"qwen15b\": {\n        \"ece\": 0.0041,\n        \"brier\": 0.0019,\n        \"mce\": 0.72,\n        \"accuracy\": 0.9983\n      },\n      \"deepseek\": {\n        \"ece\": 0.0523,\n        \"brier\": 0.0318,\n        \"mce\": 0.89,\n        \"accuracy\": 0.9933\n      },\n      \"codellama\": {\n        \"ece\": 0.0183,\n        \"brier\": 0.0072,\n        \"mce\": 0.78,\n        \"accuracy\": 0.9983\n      },\n      \"cross_model_ece_std\": 0.0225,\n      \"cross_model_ece_range\": 0.0496,\n      \"universal_calibration\": false\n    },\n    \"tables\": [\n      {\n        \"name\": \"Cross-model calibration for exception_only\",\n        \"data\": [\n          {\n            \"model\": \"Qwen-7B\",\n            \"accuracy\": \"99.83%\",\n            \"ece\": 0.0027,\n            \"brier\": 0.0013,\n            \"calibration_quality\": \"Near-perfect\"\n          },\n          {\n            \"model\": \"Qwen-1.5B\",\n            \"accuracy\": \"99.83%\",\n            \"ece\": 0.0041,\n            \"brier\": 0.0019,\n            \"calibration_quality\": \"Excellent\"\n          },\n          {\n            \"model\": \"DeepSeek\",\n            \"accuracy\": \"99.33%\",\n            \"ece\": 0.0523,\n            \"brier\": 0.0318,\n            \"calibration_quality\": \"Moderate\"\n          },\n          {\n            \"model\": \"CodeLlama\",\n            \"accuracy\": \"99.83%\",\n            \"ece\": 0.0183,\n            \"brier\": 0.0072,\n            \"calibration_quality\": \"Good\"\n          }\n        ]\n      },\n      {\n        \"name\": \"Calibration gap: exception_only vs no_trace (cross-model)\",\n        \"data\": [\n          {\n            \"model\": \"Qwen-7B\",\n            \"exc_ece\": 0.0027,\n            \"no_trace_ece\": 0.1715,\n            \"ratio\": \"63x\"\n          },\n          {\n            \"model\": \"Qwen-1.5B\",\n            \"exc_ece\": 0.0041,\n            \"no_trace_ece\": \"~0.21\",\n            \"ratio\": \"~51x\"\n          },\n          {\n            \"model\": \"DeepSeek\",\n            \"exc_ece\": 0.0523,\n            \"no_trace_ece\": \"~0.18\",\n            \"ratio\": \"~3.4x\"\n          },\n          {\n            \"model\": \"CodeLlama\",\n            \"exc_ece\": 0.0183,\n            \"no_trace_ece\": \"~0.17\",\n            \"ratio\": \"~9.3x\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cross-model calibration 在 worst 档下呈现 model-dependency。Qwen family (7B + 1.5B) 近完美，但 DeepSeek ECE 比 Qwen 高 ~19x（0.0523 vs 0.0027）， CodeLlama 高 ~7x。这使 \\\"calibration as secondary evidence\\\" 从 universal finding 降级为 model-dependent finding。\\n然而，calibration improvement ratio (exc vs no_trace) 在所有模型上都存在 （3.4x-63x），只是 magnitude model-dependent。论文可保留 \\\"exception signal improves calibration\\\" claim 但需加 \\\"magnitude varies across models\\\" qualifier。\\nDeepSeek 的 poor calibration (ECE=0.0523) 与其 accuracy (99.33%) 的 disconnect 呼应 D1 (eval_loss vs accuracy decoupling)——token-level confidence 与 sample-level correctness decoupled。审稿人可能质疑: 如果 calibration 是 model-dependent 的，那 calibration evidence 对 Claim 1 的 supporting 作用 大打折扣。\\n\\n\\nQwen-7B ECE=0.0027 已知（近完美）。\\nQwen-1.5B: exception_only accuracy 与 7B 完全相同 (99.83%)，但 1.5B 的 logit 分布可能略 less peaked（smaller model capacity → slightly more uncertain probability outputs）。预测 ECE=0.0041，仍然 excellent。\\nDeepSeek: 这是 worst 档的关键分歧点。DeepSeek exception_only seed42=99.33% （epoch3），但 epoch1=99.83%→epoch3=99.33% 的退化暗示 training 过程中 calibration 恶化。DeepSeek 的 LoRA 训练不稳定（seed123=91.09%）说明模型 的 probability landscape rugged。即使在 seed42 这个 \\\"好\\\" seed 上，model 的 predicted probabilities 可能 systematically miscalibrated——对 pass 样本 过度自信（many samples near 1.0 probability）但对 fail 样本 underconfident （several samples in 0.3-0.6 range instead of near 0.0），导致 ECE=0.0523。 这不是灾难性的 miscalibration，但与 Qwen 的 0.0027 相差 ~19x，破坏了 \\\"universal near-perfect calibration\\\" 的叙事。Brier=0.0318 也偏高—— 主要来自 8 个 error samples 的 high predicted pass probability。\\nCodeLlama: accuracy=99.83%（与 Qwen 相同），但 CodeLlama 的 LLaMA 架构 在 code domain 的 confidence distribution 不同。ECE=0.0183 处于中等水平—— 优于 DeepSeek 但 ~7x worse than Qwen。可能原因: CodeLlama 虽然 accuracy 完美，但对少数 borderline samples 的 probability assignment 不够 extreme （predicts 0.85 instead of 0.99 for clear pass cases）。\\n\"\n  },\n  {\n    \"name\": \"few_shot_frontier_baseline\",\n    \"description\": \"GPT-4o / Claude 直接判断 pass/fail (0-shot + 3-shot)，与 SFT exception_only 对比\",\n    \"results\": {\n      \"gpt4o\": {\n        \"zero_shot_no_trace\": {\n          \"accuracy\": 0.823,\n          \"pass_f1\": 0.876,\n          \"fail_f1\": 0.687\n        },\n        \"zero_shot_exception_only\": {\n          \"accuracy\": 0.955,\n          \"pass_f1\": 0.97,\n          \"fail_f1\": 0.918\n        },\n        \"three_shot_exception_only\": {\n          \"accuracy\": 0.972,\n          \"pass_f1\": 0.981,\n          \"fail_f1\": 0.95\n        }\n      },\n      \"claude_sonnet\": {\n        \"zero_shot_no_trace\": {\n          \"accuracy\": 0.808,\n          \"pass_f1\": 0.862,\n          \"fail_f1\": 0.667\n        },\n        \"zero_shot_exception_only\": {\n          \"accuracy\": 0.948,\n          \"pass_f1\": 0.965,\n          \"fail_f1\": 0.908\n        },\n        \"three_shot_exception_only\": {\n          \"accuracy\": 0.965,\n          \"pass_f1\": 0.977,\n          \"fail_f1\": 0.934\n        }\n      },\n      \"sft_exception_only_qwen7b\": {\n        \"accuracy\": 0.9983,\n        \"pass_f1\": 0.999,\n        \"fail_f1\": 0.997\n      },\n      \"gap_best_fewshot_vs_sft_pp\": 2.63,\n      \"gap_pvalue\": 0.001,\n      \"api_cost_per_1190_samples_gpt4o\": \"$12-18\",\n      \"sft_inference_cost_per_1190\": \"$0.02-0.05\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"SFT vs Few-shot vs Zero-shot comparison\",\n        \"data\": [\n          {\n            \"method\": \"SFT exception_only (Qwen-7B)\",\n            \"accuracy\": \"99.83%\",\n            \"cost_per_1190\": \"~$0.03\",\n            \"latency_ms\": \"~50\",\n            \"calibration_ece\": 0.0027\n          },\n          {\n            \"method\": \"GPT-4o 3-shot + exception\",\n            \"accuracy\": \"97.2%\",\n            \"cost_per_1190\": \"~$15\",\n            \"latency_ms\": \"~2000\",\n            \"calibration_ece\": \"N/A (no logits)\"\n          },\n          {\n            \"method\": \"GPT-4o 0-shot + exception\",\n            \"accuracy\": \"95.5%\",\n            \"cost_per_1190\": \"~$12\",\n            \"latency_ms\": \"~2000\",\n            \"calibration_ece\": \"N/A\"\n          },\n          {\n            \"method\": \"Claude 3-shot + exception\",\n            \"accuracy\": \"96.5%\",\n            \"cost_per_1190\": \"~$10\",\n            \"latency_ms\": \"~1800\",\n            \"calibration_ece\": \"N/A\"\n          },\n          {\n            \"method\": \"GPT-4o 0-shot no trace\",\n            \"accuracy\": \"82.3%\",\n            \"cost_per_1190\": \"~$8\",\n            \"latency_ms\": \"~1500\",\n            \"calibration_ece\": \"N/A\"\n          },\n          {\n            \"method\": \"SFT no_trace (Qwen-7B)\",\n            \"accuracy\": \"75.1%\",\n            \"cost_per_1190\": \"~$0.02\",\n            \"latency_ms\": \"~30\",\n            \"calibration_ece\": 0.1715\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"在 worst 档下，few-shot baseline 是论文最大的 narrative threat 之一。 GPT-4o 3-shot 97.2% vs SFT 99.83% 的 2.63pp gap 虽 significant， 但审稿人会提出两个攻击:\\n(1) \\\"如果 GPT-4o 加更多 examples 或 chain-of-thought 就能追上 SFT？\\\" → 无法反驳，因为我们没测。但 3-shot 已经 nearly saturated（0-shot 95.5% → 3-shot 97.2%, diminishing returns），extrapolation 不太可能到 99.8%。\\n(2) \\\"SFT 的 marginal 2.63pp 不值得 training pipeline 的复杂度\\\" → 需用 cost argument (300x cheaper) + calibration argument (ECE=0.0027 vs GPT-4o no logits) + offline deployment 来反驳。\\nReframe: few-shot 结果实际上 STRENGTHENS \\\"exception signal is key\\\" claim ——even frontier models benefit most from exception trace (+13pp for GPT-4o)。 SFT 的 advantage 是 practical (cost/calibration)，不是 signal discovery。 Signal discovery (exception > everything else) 是 universal finding， 无论 SFT 还是 prompting。\\n\\n\\nGPT-4o 0-shot no_trace (82.3%): frontier model 可以从 code + test case 推断 correctness，但受限于 cannot actually execute code。类似我们的 no_trace baseline (75.13%)，但 GPT-4o 的 code understanding 远强于 Qwen-7B base， 因此 +7pp。\\nGPT-4o 0-shot exception_only (95.5%): 给出 exception trace 后，GPT-4o 能 准确判断 \\\"[ERROR] TypeError\\\" → fail, \\\"[No exception]\\\" → pass。但 GPT-4o 在 borderline cases（如 GeneratorExit）的判断与 SFT 模型类似——看到 [ERROR] 就 倾向判 fail。同时 GPT-4o 对 exception_only format 未经微调，可能对某些 formatting 不够 sensitive，导致 ~4.5% error rate。\\nGPT-4o 3-shot exception_only (97.2%): 3 个 examples 帮助 GPT-4o 理解 exception_only format 的 exact semantics，减少 formatting-related errors。 但仍有 ~2.8% error rate——主要来自 (1) GeneratorExit-like ambiguity, (2) multi-exception traces where GPT-4o must judge severity, (3) occasional refusal to make binary judgment on ambiguous cases。\\nSFT gap (2.63pp): 虽小但 statistically significant (n=1190, p=0.001)。 然而审稿人会质疑: \\\"2.63pp 值得 SFT pipeline 的 engineering effort 吗?\\\"\\nClaude Sonnet 略低于 GPT-4o (~0.7pp)，因为 code-specific training data 量可能略少。\\nWorst 档影响: few-shot baseline 接近 SFT，削弱 \\\"SFT is necessary\\\" narrative。 但可以 reframe: (1) SFT 7B 的推理成本比 GPT-4o API 低 ~300x; (2) SFT calibration (ECE=0.0027) 远优于 GPT-4o prompt-based output; (3) SFT 可 offline deploy 无 API dependency; (4) 核心 finding 仍然 valid: exception signal 是 key，无论 SFT 还是 few-shot。\\n\"\n  },\n  {\n    \"name\": \"ood_generalization_test\",\n    \"description\": \"在不同编程语言/项目的 trace 上测试 exception_only 泛化性\",\n    \"results\": {\n      \"python_ood_dataset\": {\n        \"name\": \"LeetCode-style problems (different distribution from HumanEval/MBPP)\",\n        \"exception_only\": 0.871,\n        \"vota\": 0.793,\n        \"no_trace\": 0.682,\n        \"exception_lift_over_notrace\": 0.189\n      },\n      \"cross_language\": {\n        \"feasibility\": \"NOT_FEASIBLE_WITHIN_TIMELINE\",\n        \"reason\": \"需要新的 trace collection pipeline for Java/JS/C++; exception format 跨语言差异大\"\n      },\n      \"domain_shift_analysis\": {\n        \"in_distribution_exc_accuracy\": 0.9983,\n        \"ood_exc_accuracy\": 0.871,\n        \"degradation_pp\": 12.7,\n        \"relative_ordering_preserved\": true,\n        \"exception_still_best_on_ood\": true\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"OOD generalization results\",\n        \"data\": [\n          {\n            \"condition\": \"exception_only\",\n            \"in_dist\": \"99.83%\",\n            \"ood_python\": \"87.1%\",\n            \"delta\": \"-12.7pp\"\n          },\n          {\n            \"condition\": \"VOTA\",\n            \"in_dist\": \"99.41%\",\n            \"ood_python\": \"79.3%\",\n            \"delta\": \"-20.1pp\"\n          },\n          {\n            \"condition\": \"no_trace\",\n            \"in_dist\": \"75.13%\",\n            \"ood_python\": \"68.2%\",\n            \"delta\": \"-6.9pp\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"OOD 泛化性在 worst 档下是 mixed 结果。正面: relative ordering preserved, exception_only 仍为最佳。负面: 12.7pp degradation 说明 exception_only 的 near-perfect in-distribution accuracy 部分依赖于 HumanEval/MBPP 的 exception pattern 分布（dominated by TypeError, ValueError, AssertionError）， 对 unseen exception types 的 generalization 有限。\\n对论文的影响: OOD 结果不应放入 main paper（太弱），只在 Discussion 提 generalization limitation + future work。跨语言完全不可行，成为 explicit limitation。审稿人关于 \\\"single task, single dataset\\\" 的 concern 在 OOD 数据上部分证实——exception signal 的 universality 限于 similar exception distributions。\\n\\n\\nPython OOD (LeetCode-style): 训练数据来自 HumanEval + MBPP-sanitized (591 problems)，这些是 relatively simple、well-defined 的编程题。LeetCode-style problems 更复杂（涉及 DP, graph algorithms, complex data structures）， exception patterns 可能包含 training 未见过的 error types (e.g., RecursionError, MemoryError, complex nested exceptions)。\\nexception_only 87.1%: 下降 12.7pp 因为 (1) unseen exception types —— 模型 对 RecursionError 等 training 中罕见的 exception 缺乏 calibrated 判断; (2) OOD problems 的 pass/fail 比例可能不同 (training = 71.5% pass); (3) LeetCode problems 可能有 time limit exceeded 等 non-exception failures ——代码不抛异常但 output 错误——exception_only 表征中这些显示为 \\\"[No exception]\\\" 但 label=fail，模型在 OOD 上对这类 pattern 的 confusion 更大。\\nVOTA 79.3%: 更大的 degradation (20.1pp) 因为 VOTA 的 loop compression 和 ae extraction 对 LeetCode trace 结构的 assumption 不 match—— complex data structures 的 trace 不 follow 简单的 loop iteration pattern。\\nno_trace 68.2%: 下降 7pp，说明 LeetCode problems 本身 harder（更难从 code alone 判断 correctness），但 degradation 较小因为 no_trace 的 ceiling 本来就低。\\nRelative ordering preserved (exception > VOTA > no_trace) 是正面信号—— 说明 exception dominance 的 conclusion generalizes even if absolute numbers drop。但 12.7pp degradation 被审稿人 ammunition: \\\"model overfits to HumanEval/MBPP exception distribution\\\"。\\nCross-language (Java/JS/C++): 在 deadline 前 NOT FEASIBLE。需要: (1) trace collection infrastructure per language (Java Jacoco/bytecode, JS Istanbul, C++ sanitizers); (2) exception format normalization (Java stack traces ≠ Python tracebacks); (3) test suite per language。 估计 3-4 weeks 工作量。\\n\"\n  },\n  {\n    \"name\": \"training_dynamics_comparison\",\n    \"description\": \"exception_only vs full_trace 的 learning curve (每 50 steps eval)\",\n    \"results\": {\n      \"exception_only_curve\": {\n        \"step_0\": 0.5,\n        \"step_50\": 0.962,\n        \"step_100\": 0.991,\n        \"step_150\": 0.995,\n        \"step_200\": 0.998,\n        \"step_250\": 0.998,\n        \"convergence_step\": 100\n      },\n      \"full_trace_curve\": {\n        \"step_0\": 0.5,\n        \"step_50\": 0.721,\n        \"step_100\": 0.768,\n        \"step_150\": 0.803,\n        \"step_200\": 0.812,\n        \"step_250\": 0.818,\n        \"convergence_step\": 200\n      },\n      \"speed_ratio\": 2.0,\n      \"exception_step50_vs_full_converged\": \"+14.4pp\",\n      \"curve_noise\": {\n        \"exception_only_step_std\": 0.003,\n        \"full_trace_step_std\": 0.018\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Learning curve milestones\",\n        \"data\": [\n          {\n            \"condition\": \"exception_only\",\n            \"step_50\": \"96.2%\",\n            \"step_100\": \"99.1%\",\n            \"step_200\": \"99.8%\",\n            \"final\": \"99.83%\",\n            \"converge_step\": 100\n          },\n          {\n            \"condition\": \"full_trace\",\n            \"step_50\": \"72.1%\",\n            \"step_100\": \"76.8%\",\n            \"step_200\": \"81.2%\",\n            \"final\": \"81.8%\",\n            \"converge_step\": 200\n          },\n          {\n            \"condition\": \"no_trace\",\n            \"step_50\": \"71.5%\",\n            \"step_100\": \"73.8%\",\n            \"step_200\": \"75.0%\",\n            \"final\": \"75.1%\",\n            \"converge_step\": 150\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Training dynamics 在 worst 档下提供 supporting evidence 但不够强作为 独立 contribution。核心 finding (exception_only 收敛更快) 是 expected 且 trivial——simpler signal naturally easier to learn。2x speed ratio 不够 dramatic（如果是 10x 则更有 narrative value）。\\n对论文的影响: 可在 Appendix 放 learning curve figure 作为 supplementary evidence for Claim 2 (information density)。但不应作为 main result—— 审稿人会说 \\\"of course simpler signals converge faster, this is not a contribution\\\"。\\n唯一 novel 的 data point: exception_only step 50 (96.2%) > full_trace final (81.8%)。这意味着 exception_only 在仅 1/6 的训练时间内就超越了 full_trace 的 theoretical ceiling。可以用一句话在 Results 中提及， 但不值得 dedicated subsection。\\n\\nexception_only: signal 结构简单（[ERROR] type: ... 或 [No exception]）， 模型在 ~50 steps 即能学到 binary mapping（有 exception → fail, 无 → pass）， 此后 refinement 主要是 calibration improvement 和 edge cases。Step 50 的 96.2% 已经超过 full_trace 的最终 converged accuracy (81.8%)。 这支持 information density 假说——exception signal 的 signal-to-noise ratio 极高，学习效率自然高。\\nfull_trace: 模型需要从 long, noisy traces 中学到什么是 relevant， 这本身就是一个 learning problem。Step 50 时模型刚开始区分 trace structure (72.1%≈no_trace baseline + few pp)，到 step 200 才稳定在 ~82%。 Step-to-step variance (std=0.018 per step) 比 exception_only (0.003) 高 6x， 说明 full_trace 的 optimization landscape 更 noisy。\\nSpeed ratio 2x: exception_only 在 ~100 steps converge，full_trace 在 ~200 steps。ratio 只有 2x（不是 10x）因为两者都使用相同的 LoRA rank 和 learning rate——exception_only 的主要优势是 ceiling height (99.83% vs 81.8%)，不是 convergence speed 本身。\\nWorst 档 caveat: curves are noisy（尤其 full_trace），step-to-step fluctuations 使 figure 不够 clean for publication。exception_only curve 在 step 50 之后几乎 flat（从 96.2% → 99.8%，3.6pp over 200 steps）， 作为 learning curve figure 不 visually interesting。\\n\"\n  }\n]",
      "numLines": 838,
      "startLine": 1,
      "totalLines": 838
    }
  },
  "sourceToolAssistantUUID": "91dc17c2-afc8-42b0-bfcb-090e4b1e5670",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "175abc6b-2146-427e-acfe-4e3e17983955",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T125926 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-stu…",
  "leafUuid": "824bcef7-4b96-41b4-ab30-20fb4169856c",
  "sessionId": "175abc6b-2146-427e-acfe-4e3e17983955"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier dream paper for dream_20260518T125926",
  "sessionId": "175abc6b-2146-427e-acfe-4e3e17983955"
}
```

---

### Tool result

_source line 13 · 2026-05-18T13:48:18.477Z_

<details><summary>↩ Tool result · `toolu_01Ba3ZoeWRYZ2QvFMEiLwcBZ`</summary>

```text
1	# Paper Framing — trace-verdict-study
2	
3	> v3.0 — [UPDATED 2026-05-15] D030 CLOSED: DeepSeek VOTA 84.45% confirmed correct (confirmatory re-eval). **Critical narrative fix**: to_chat_text() preserves labels → VOTA 训练时 verdict label 未被截断 → 论文中 "label truncation/corruption" 措辞对 VOTA 不成立。正确叙事: trace INPUT content 被截断 (91.7% samples), 84.45% 反映 trace information loss。新增 D11: VOTA cross-model gap confounded by training-time truncation。数据集来源：HumanEval (164) + MBPP-sanitized (427) = 591 problems × 10 LLM-generated solutions = 5910 samples。
4	
5	## Target Venue
6	- Primary: EMNLP 2026 Main (ARR submission)
7	- Fallback: EMNLP 2026 Findings
8	- Deadline: ARR May 25, 2026
9	
10	## Core Insight
11	
12	Verdict prediction (pass/fail) is fundamentally a **fault detection** task. The most effective signal is the **exception event** — a compact, structured diagnostic moment that consistently outperforms all other trace representations across models (Qwen 99.83% ± 0.00 across 3 seeds; DeepSeek 91-99% depending on seed, but always > VOTA 84.45% and no_trace 73.36%). In contrast, richer trace representations that require deeper execution reasoning show model-dependent effectiveness: VOTA gap = 14.96pp, no_trace gap = 1.77pp. Information density — not training signal distribution — is the primary bottleneck: even oracle loss masking (label-only) cannot close the 13pp gap between full traces and targeted extraction. The design principle: **extract the highest-specificity diagnostic signal; discard everything else.** Cross-model absolute performance depends on LoRA initialization stability, but exception_only's relative dominance over other components is robust.
13	
14	VOTA's primary contribution is **fault indicator isolation** — automatically extracting exception events from noisy full traces — rather than generic trace compression. The "compression helps" narrative was a stepping stone; the real mechanism is diagnostic signal extraction.
15	
16	## Core Claims (3)
17	
18	### Claim 1: Exception events are the most effective trace component for verdict prediction
19	
20	Exception summaries consistently achieve the highest verdict prediction accuracy across both models tested, outperforming all other trace representations in every seed. On Qwen-2.5-Coder-7B, performance is perfectly robust: 99.83% ± 0.00 (3 seeds). On DeepSeek-Coder-6.7B, absolute accuracy is seed-dependent (seed42=99.83% epoch1, seed123=91.43% epoch1; Δ=8.40pp), consistent with LoRA initialization sensitivity — but exception_only still dominates VOTA (84.45%) and no_trace (73.36%) in all seeds. This contrasts with VOTA (cross-model gap = 14.96pp) and no_trace (gap = 1.77pp). Exception events are structurally simple (`[ERROR] type: ... message: ...`) and do not require deep trace reasoning.
21	
22	**Supporting evidence:**
23	- `vota_exception_only_seed42_v2`: Qwen 99.83%, ECE=0.0027
24	- `deepseek_exception_only_seed42`: DeepSeek 99.83% (epoch1) / 99.33% (epoch3)
25	- `deepseek_exception_only_seed456`: DeepSeek 99.33% (epoch3), CI [98.82, 99.75] — 与 seed42 完全一致
26	- `deepseek_exception_only_seed123`: DeepSeek 91.43% (epoch1) / 91.09% (epoch3) — LoRA init sensitivity outlier
27	- `deepseek_vota_seed42`: DeepSeek VOTA 84.45% (gap = 14.96pp vs Qwen)
28	- `deepseek_no_trace_seed42`: DeepSeek no_trace 73.36% (gap = 1.77pp vs Qwen)
29	- `vota_no_ae_seed42`: 99.41% — actual/expected removal 不降，非 trivial string comparison
30	
31	**DeepSeek seed analysis** ✅ (FINALIZED, D029):
32	
33	| Seed | Epoch 3 (final) | fail_recall | pass_recall | train_loss | Errors | CI |
34	|------|-----------------|-------------|-------------|------------|--------|-----|
35	| 42   | 99.33%          | 1.0         | 0.9906      | —          | 8/1190 | — |
36	| 456  | 99.33%          | 1.0         | 0.9906      | 0.1225     | 8/1190 | [98.82, 99.75] |
37	| 123  | 91.09%          | 0.705       | 0.993       | 0.122      | —      | [89.4, 92.6] |
38	
39	seed42 与 seed456 结果**完全一致**（均 8/1190 错误，99.33%），seed123 为离群值。seed123 的 fail_recall 仅 0.705 — LoRA 初始化落入差的局部最优，未充分学到 exception→fail 映射。**关键发现**: seed456 和 seed123 的 train_loss 几乎相同（0.1225 vs 0.122），但 accuracy 差 8.2pp — token-level loss 掩盖了 sample-level 分类能力的巨大差异（详见 D10）。
40	
41	**Irreducible error analysis** ✅: 3 seeds 错误的 2 个样本 (id=901, 905) 均来自 HumanEval/95 (`check_dict_case`)，根因为 Python `all()` 对 generator expression 短路触发 `GeneratorExit`（`BaseException` 子类，非真正错误）。tracer 将其标记为 `[ERROR]`，exception_only 模型看到 7 行 `[ERROR] GeneratorExit`，合理但错误地预测 fail。整个 1190 条测试集仅这 2 条含 `GeneratorExit`，模型无训练信号学习其良性本质。**这确认 99.83% 是 exception_only 表征的理论上限，剩余 0.17% 是 representation-inherent irreducible error，而非模型不足。**
42	
43	**Seed robustness** ✅: Qwen exception_only 3-seed 完全一致，构成本文最强 robustness 证据：
44	
45	| Seed | Accuracy | 95% CI | Errors |
46	|------|----------|--------|--------|
47	| 42 | 99.83% | [99.58, 100] | 2/1190 |
48	| 123 | 99.83% | [99.58, 100] | 2/1190 |
49	| 456 | 99.83% | [99.58, 100] | 2/1190 |
50	
51	3 seeds 错误样本 100% 重叠（id=901, 905, 均为 `check_dict_case` 函数, label=pass → pred=fail）。**Irreducible samples**: 模型已达数据集理论上限，variance = 0。
52	
53	**DeepSeek cross-model** ✅ (D029): 3-seed 完整数据 — seed42/456=99.33%, seed123=91.09%。2/3 seeds 鲁棒，seed123 为 LoRA 初始化离群值（fail_recall 仅 0.705）。Qwen 3-seed 完美稳定 (99.83% ± 0.00) vs DeepSeek 高方差（σ≈4.8pp），暗示 exception signal 的 learnability 与模型 LoRA 训练稳定性相关。但即使最差 seed (91.09%) 仍优于 VOTA (84.45%) 和 no_trace (73.36%)，relative dominance robust。
54	
55	### Claim 2: Information density, not gradient dilution, drives trace compression benefit
56	
57	Full traces help verdict prediction (81.76% [`full_trace_seed42_v5`], +6.6pp over baseline), but VOTA achieves 99.41% [`vota_seed42_v5`] (+24.3pp) — a +17.6pp advantage. Label-only loss ablation (plan_002) quantifies the causal decomposition: **gradient dilution contributes ~26% of the gap** (4.5pp; label-only full_trace = 86.22% [`full_trace_label_only_seed42`]), **information overload contributes ~74%** (13.0pp; only trace compression resolves this). Even with oracle loss masking that eliminates gradient dilution, full traces still underperform VOTA by 13pp.
58	
59	Cross-model evidence reinforces this: VOTA gap (14.96pp) partly tracks base model execution reasoning capability (Qwen CRUXEval-I 56.5% vs DeepSeek 39.0%, Δ=17.5pp), though **confounded by DeepSeek training-time trace truncation** (91.7% of VOTA samples truncated to ~2048 tokens; see D11). The two factors cannot be disentangled in the current design. Exception signal partially bypasses both bottlenecks (token-short, no truncation; consistently best component on both models), though DeepSeek shows seed-dependent absolute performance (91-99%).
60	
61	**Supporting evidence:**
62	- `full_trace_label_only_seed42`: 86.22%, ECE=0.1107 (gradient dilution fix, +4.5pp over standard full_trace)
63	- `full_trace_seed42_v5`: 81.76%, ECE=0.0958 (standard full_trace)
64	- `vota_seed42_v5`: 99.41%, ECE=0.0054
65	- `deepseek_vota_seed42`: 84.45% (VOTA model-dependent)
66	- CRUXEval literature data (Wang et al.)
67	
68	### Claim 3: Two-tier diagnostic hierarchy for verdict prediction
69	
70	Component ablation reveals verdict-relevant trace information has a strict two-tier hierarchy:
71	- **Tier 1 — diagnostic moment signals**: exception summaries (99.83% [`vota_exception_only_seed42_v2`]) and assertion-point information (99.92% [`vota_ae_only_seed42`]) are individually near-perfect and sufficient for verdict prediction on Qwen. These signals are structurally simple and consistently the most effective component on both models, though DeepSeek absolute performance is seed-dependent.
72	- **Tier 2 — behavioral patterns**: loop compression (85.63% [`vota_loop_only_seed42`]) carries substantial signal but is model-dependent and fully subsumed by Tier 1.
73	
74	Combining tiers introduces noise rather than helping: exception_only (99.83%) > VOTA full (99.41%), p=0.01. Loop_only ≈ full_trace_label_only (85.63% vs 86.22%) confirms VOTA's loop compression precisely extracts the useful behavioral signal from full traces.
75	
76	**Supporting evidence:**
77	- `vota_exception_only_seed42_v2`: 99.83%, ECE=0.0027 (Tier 1 exception)
78	- `vota_ae_only_seed42`: 99.92%, ECE=0.0004 (Tier 1 assertion-point, 与 exception 统计等价 p=0.80)
79	- `vota_loop_only_seed42`: 85.63%, ECE=0.0831 (Tier 2 behavioral)
80	- `full_trace_label_only_seed42`: 86.22%, ECE=0.1107 (≈ loop_only, confirming extraction equivalence)
81	- `deepseek_exception_only_seed42`: 99.83% epoch1 / 99.33% epoch3 (Tier 1 cross-model validation)
82	- `deepseek_vota_seed42`: 84.45% (Tier 1+2 cross-model: Tier 2 introduces model-dependent degradation)
83	
84	**Calibration**: 完整 calibration 数据确认 Tier 1 信号不仅 accuracy 近完美，置信度校准也近完美：
85	
86	| Condition | Accuracy | ECE | Brier | 解读 |
87	|-----------|----------|-----|-------|------|
88	| ae_only | 99.92% | 0.0004 | 0.0008 | 近乎完美校准 |
89	| exception_only | 99.83% | 0.0027 | 0.0013 | 近乎完美校准 |
90	| VOTA | 99.41% | 0.0054 | 0.005 | 优秀，但 Tier 2 引入轻微 noise |
91	| loop_only | 85.63% | 0.0831 | — | Tier 2 单独校准中等 |
92	| label_only | 86.22% | 0.1107 | — | gradient dilution fix 仍 miscalibrated |
93	| full_trace | 81.76% | 0.0958 | — | 中度 miscalibrated |
94	| no_trace | 75.13% | 0.1715 | 0.1972 | 严重 miscalibrated |
95	
96	no_trace ECE 是 exception_only 的 **~63x**（0.1715/0.0027），Brier 是 **~150x**（0.1972/0.0013）。Trace signal（尤其 Tier 1）不仅提升 accuracy，更从根本上改善模型 calibration。
97	
98	**Design principle**: verdict-optimized traces should extract highest-specificity diagnostic signals; lower-specificity signals are redundant and may introduce noise.
99	
100	## Cross-Model Evidence Summary
101	
102	| Condition | Qwen-2.5-Coder-7B | DeepSeek-Coder-6.7B | Cross-model gap | Interpretation |
103	|-----------|-------------------|---------------------|-----------------|----------------|
104	| exception_only | 99.83% ± 0.00 (3 seeds) | seed42/456: 99.33%; seed123: 91.09% | 0.50-8.74pp (seed-dependent) | **Best component on both models**; 2/3 DeepSeek seeds match Qwen-level; 1 outlier still > VOTA |
105	| VOTA | 99.41% | 84.45% | -14.96pp | Model-dependent — requires execution reasoning; **also confounded by DeepSeek training-time trace truncation** (91.7% of VOTA samples truncated from mean 2626 to ~2048 tokens; labels preserved via to_chat_text(), see D11) |
106	| no_trace | 75.13% | 73.36% | -1.77pp | Baseline gap tracks general capability |
107	| full_trace | 81.76% | collapsed (v3 pending) | N/A | DeepSeek v1 label truncation bug |
108	
109	**Key insight**: Exception_only is consistently the best component on both models (even worst DeepSeek seed 91.09% > VOTA 84.45%). Cross-model gap 与 signal complexity 正相关, but exception signal's absolute effectiveness also depends on LoRA training stability. Qwen: perfectly robust (3 seeds identical). DeepSeek: 2/3 seeds at 99.33% (matching Qwen-level), 1 outlier at 91.09% (LoRA initialization). Median performance robust; seed sensitivity suggests smaller/weaker models may need training stabilization (multi-seed selection, warmup tuning) for optimal exception signal utilization.
110	
111	## VOTA Repositioning
112	
113	**旧叙事**: VOTA 是 trace compression 方法，价值在于"压缩使 trace 更有效"。
114	
115	**新叙事**: VOTA 是 **fault indicator isolation** 方法，核心价值在于自动从 noisy execution traces 中提取 exception events 等 diagnostic signals。
116	
117	**证据链**:
118	1. exception_only (99.83%) ≥ VOTA full (99.41%) — 压缩后的其他组件（loop, ae）不仅无益，反而引入 noise
119	2. VOTA 跨模型 gap = 14.96pp — 因为 VOTA 包含 model-dependent 的 Tier 2 组件（loop compression 需要 execution reasoning）
120	3. exception_only 在两个模型上均为最优组件 — isolate 出 Tier 1 后，相对优势 robust（虽然 DeepSeek 绝对值 seed-dependent）
121	4. vota_no_ae (99.41%) = VOTA (99.41%) — actual/expected 移除无影响，exception 是真正的 active ingredient
122	
123	**论文中的表述**: "VOTA's trace compression pipeline incidentally isolates exception events — the minimal sufficient diagnostic signal. Its value lies not in making traces shorter, but in separating high-specificity fault indicators from low-specificity behavioral patterns."
124	
125	**对 Method section 的影响**: VOTA 仍然完整描述（loop compression + exception + actual/expected），但 Results/Discussion 明确指出 exception isolation 是核心机制，其他组件是 model-capability-dependent bonus。
126	
127	## Story Spine
128	
129	- **Problem**: Existing trace SFT studies (DCSH, TracePile) evaluate only generative tasks and find limited, model-dependent benefit. No prior work has tested trace SFT on verdict tasks (binary pass/fail), nor identified what trace components drive classification performance.
130	
131	- **Existing approaches & gaps**: DCSH (EMNLP Findings 2025) tested 5 trace formats on generation tasks, finding that "no single trace representation consistently outperforms others." TracePile (NeurIPS 2025) scaled to 2.6M samples but only evaluated generation. TRACED (ICSE 2024) showed traces help encoder-based classification. All existing trace formats are designed for execution simulation, not fault detection.
132	
133	- **Our framing**: We reframe verdict prediction as **fault detection** and ask: what is the minimal sufficient diagnostic signal? Through systematic component ablation across two architecturally distinct models, we discover that exception events — compact, structured error summaries — are consistently the most effective trace component, achieving near-perfect accuracy on Qwen (99.83% ± 0.00, 3 seeds) and outperforming all alternatives on DeepSeek (91-99% vs VOTA 84.45%). Richer trace representations work only when the base model has sufficient execution reasoning capability, making them unreliable for general deployment.
134	
135	- **Headline result**: "Exception events consistently achieve the highest verdict accuracy across models (Qwen 99.83%, DeepSeek 91-99%), outperforming VOTA traces (84.45% on DeepSeek, -14.96pp gap) — demonstrating that fault indicator isolation, not trace reasoning, is the robust mechanism for verdict prediction. DeepSeek seed sensitivity reveals LoRA training stability as a secondary factor for smaller models."
136	
137	## Story Arc
138	
139	1. **Setup**: Trace SFT for code tasks — promising but inconsistent in prior work (DCSH, TracePile). Unknown whether traces help verdict tasks and what trace design matters.
140	
141	2. **First result — traces help, compression helps more** (single model): no_trace 75.13% → full_trace 81.76% → VOTA 99.41%. Label-only loss ablation decomposes the gap: 26% gradient dilution, 74% information overload. Compression improves accuracy through higher information density, not just cost savings.
142	
143	3. **Twist — what component actually drives VOTA?** Component ablation reveals exception_only (99.83%) ≥ full VOTA (99.41%). The "trace reasoning" narrative is wrong — verdict prediction is fault detection. Tier 1 (exceptions + assertion-point) subsumes Tier 2 (loops). Actual/expected removal doesn't hurt (99.41%).
144	
145	4. **Cross-model stress test — consistent dominance, not universal perfection**: Exception_only is the best component on both models (even DeepSeek worst seed 91.09% > VOTA 84.45%), but absolute performance is seed-dependent on DeepSeek (91-99% vs Qwen's perfectly stable 99.83%). VOTA degrades by 14.96pp. The structurally simplest component is the most robust, but LoRA initialization sensitivity introduces variance on weaker models. Qwen seed robustness (3-seed variance = 0) + calibration (ECE=0.0027) 确认 exception signal 在强模型上的 reliability。DeepSeek seed sensitivity 揭示 training stability 作为 secondary bottleneck。
146	
147	5. **Design principle**: For verdict tasks, identify the highest-specificity diagnostic signal (exception events) and discard everything else. VOTA's value is fault indicator isolation — automatically extracting exceptions from noisy traces — not generic compression. Simpler signals are more robust; complexity tolerance depends on model capability.
148	
149	## Dataset Characteristics
150	
151	### Data duplication analysis
152	
153	| Condition | Total | Unique | Duplication rate | Cause |
154	|-----------|-------|--------|------------------|-------|
155	| exception_only_train | 4720 | 2858 | 39.45% | 同题多个 passing 解映射为相同 (input, output) — 无异常 → 同一 trace |
156	| exception_only_test | 1190 | 607 | 48.99% | 同上 |
157	| raw_traces | 5910 | 5803 | 1.81% | 完整 trace 含行号/变量值/内存地址，几乎不重复 |
158	
159	**Train-test input overlap: 0（无数据泄漏）**
160	
161	**解读**: exception_only 高重复率是 representation 的自然属性，非数据问题。多个正确解对同一测试用例执行时若均无异常，exception_only 表征退化为相同的空/无异常标记。这恰好说明 exception signal 的 compactness — 它仅编码 fault presence，不编码 solution identity。raw_traces 重复率极低 (1.81%) 因为完整 trace 包含 solution-specific 信息（变量值、内存地址）。尽管高重复率意味着有效训练样本少于名义数量，模型仍达 99.83% — 进一步确认 exception signal 的 learnability。
162	
163	## DeepSeek full_trace 处理
164	
165	**现状**: v1 坍塌（28.5%, 100% 预测 fail, 根因: 训练端 label 截断）。v2 重训启动但被 kill（Loop #6 ops worker 腾 GPU 给 vota_seed456）。v3 RUNNING（label-preserving truncation fix）。
166	
167	**处理方案**: v3 正在 cuda:0 上训练，预计 5/16 完成。
168	
169	**VOTA vs full_trace 截断机制区分** (D030 token analysis 确认):
170	- **full_trace v1**: SFTTrainer right-truncation 切掉了 verdict **label** → 100% predict fail → 坍塌。根因: DeepSeek tokenizer 对 full_trace 产生 >2048 tokens, label 在截断窗口外。
171	- **VOTA**: `to_chat_text()` 保留 verdict label（label 完整），但 91.7% 的样本 **trace content（input）被截断**（mean 2626 → ~2048 tokens）。84.45% 是真实结果，反映 trace 信息损失对模型学习的影响，**不是** label corruption。
172	- **exception_only**: token 长度远低于 2048，不受截断影响，跨模型对比 clean。
173	
174	**对论文叙事的影响**: 论文中所有 "right-truncation corrupts/removes the verdict label" 措辞**对 VOTA 不成立**——label 完整保留，被截断的是 trace input。正确表述: "trace content truncation causes information loss"。VOTA cross-model gap (14.96pp) 有两个贡献因素: (1) model capability, (2) training-time trace truncation on DeepSeek (see D11)。
175	
176	## External Benchmark (DebugBench) Positioning
177	
178	**DebugBench 仅作泛化性验证，不作 trace importance 证据。**
179	
180	| Condition | Main Dataset | DebugBench | Δ interpretation |
181	|-----------|-------------|------------|------------------|
182	| no_trace | 75.13% | 96.71% | DebugBench 天花板高，baseline 已强 |
183	| VOTA | 99.41% | 99.77% | +3.06pp lift — 边际 |
184	| exception_only | 99.83% | 100.00% | +3.29pp lift — 边际 |
185	
186	**主数据集 trace lift = 24.70pp**（no_trace → exception_only），DebugBench trace lift 不到其 1/7。
187	
188	**论文定位规则**：
189	- DebugBench → 泛化性证据（exception_only 100% = 跨数据集鲁棒性）
190	- Trace importance 论证 → 仅依赖主数据集（24.7pp lift）
191	- 禁止用 DebugBench 的 3.29pp lift 论证 "trace 的核心价值"——审稿人会攻击天花板效应
192	
193	## Venue Fit Risks
194	
195	| Risk | Assessment | Mitigation |
196	|------|-----------|------------|
197	| 单任务 | 仍然只在 test verdict prediction 上验证 | 跨模型验证部分弥补; Discussion 中讨论 generalization |
198	| 单数据集 | HumanEval + MBPP-sanitized 是唯一数据源 (591 problems × 10 solutions) | 定位为 empirical study, 深度优于广度; 两个标准 benchmark 组合覆盖多样编程题型; exception_only 有效训练样本仅 2858 unique 即达 99.83%, 暗示 signal 的 simplicity 降低对数据量的依赖 |
199	| "只是 feature engineering" | exception extraction 不复杂 | simplicity 本身是 contribution — 最简信号最 robust |
200	| Negative result 味道 | VOTA 跨模型不 robust | Reframe: 识别 robust vs non-robust 组件边界是 positive |
201	| Seed robustness (Qwen) | ✅ 已解决: 99.83% ± 0.00 (3 seeds), irreducible samples 确认 | — |
202	| Seed robustness (DeepSeek) | ✅ 3-seed 完整: 2/3 at 99.33%, 1 at 91.09% | LoRA initialization sensitivity — median robust, worst still > all alternatives; 转化为 training stability finding (D9/D10) |
203	| Calibration | ✅ 完整数据: Tier 1 ECE≤0.003, no_trace ECE=0.171 (~63x gap) | Brier ~150x gap 进一步确认 |
204	| 只用 2 个模型 | 有限但有意义的 diversity | Architecture + pretraining data (5.5T vs 2T) + CRUXEval gap (17.5pp) 构成充分差异 |
205	| 数据重复率 | exception_only 训练集 39.45% 重复 | 非数据泄漏（train-test overlap = 0）；是 representation compactness 的自然结果；有效样本仍足够学习 |
206	
207	## Anticipated Reviewer Concerns
208	
209	| Concern | Planned Response |
210	|---------|-----------------|
211	| "exception_only 99.83% 是不是 trivial pattern matching [ERROR] 有无？" | full_trace 也包含 [ERROR] 但仅 81.76%——模型需要从 trace context 中 extract 和 utilize exception signal, 不是简单 keyword detection. no_trace 无 exception, 75.13%. |
212	| "为什么 exception_only > VOTA? adding info 反而降?" | 非 exception 组件 (loop/ae tokens) 稀释 attention 对 exception 信号的聚焦. Calibration: exception_only ECE=0.0027 vs VOTA ECE=0.0054. 部分样本 loop 正常但有 exception, 引入矛盾信号. |
213	| "CRUXEval gap 与 VOTA gap 的相关性可能是 coincidence" | 明确标注为 hypothesis. 列出 alternatives (tokenizer efficiency, pretraining scale 2.75x, chat template). 不 overclaim. |
214	| "只有 2 个模型，universality claim 太强" | 同意是 limitation. 两模型在 architecture (RoPE vs ALiBi), pretraining data (5.5T vs 2T), execution reasoning (CRUXEval 17.5pp gap) 上有充分差异, 不是 trivial replication. Exception signal 的 structural simplicity 提供 inductive argument for broader generalization. |
215	| "99.83% 可能 saturated, 看不出 exception 到底学了什么" | Calibration 双指标: exception_only ECE=0.0027, Brier=0.0013 (近完美校准). 对比 no_trace ECE=0.1715, Brier=0.1972 (~63x/~150x gap). **Irreducible error 根因已明确**: 2/1190 errors 均因 Python `all()` 短路触发 `GeneratorExit`（`BaseException` 子类，非真正错误），tracer 将其标记为 `[ERROR]`。模型看到 7 行 `[ERROR] GeneratorExit` 合理预测 fail，但代码实际正确。整个测试集仅这 2 条含 `GeneratorExit`，无训练信号可学习其良性本质。99.83% 是 representation 的理论上限，非 saturation artifact。 |
216	| "只用了 1 个 seed" | Qwen ✅: 3 seeds 99.83% ± 0.00. DeepSeek ✅: 3 seeds 完整 — seed42/456=99.33%, seed123=91.09%。2/3 鲁棒，1 离群。median=99.33%, worst=91.09% (仍 > VOTA 84.45%)。论文透明报告所有 seeds，将 seed sensitivity 转化为 LoRA training stability 的 finding（D9）。 |
217	| "eval_loss 上升但 accuracy 提升——checkpoint selection 有问题?" | Discussion D1: token-level loss 与 binary verdict accuracy 解耦. 推荐 verdict-specific metric. Methodological contribution. |
218	| "DeepSeek full_trace 坍塌是 bug 不是 finding" | 诚实披露根因 (训练端 label 截断). 其他 3 条件不受影响. 修复版本如就绪则补入. |
219	| "calibration 数据只有 1 个 seed" | Seed robustness 已证明 accuracy variance=0 (3 seeds), calibration 在 accuracy 完全一致的前提下 expected 也一致. ECE/Brier 的极小值 (0.0027/0.0013) 留有极小 variance 空间. |
220	| "DeepSeek epoch1 > epoch3, 为什么用 epoch3 报告?" | 正文报告所有 seeds 的 final + best checkpoint。seed42: epoch1=99.83%, epoch3=99.33%。seed123: epoch1=91.43%, epoch3=91.09%。D7 讨论 early stopping + D9 讨论 LoRA initialization sensitivity。不 cherry-pick best seed。 |
221	| "DeepSeek seed sensitivity 说明 exception signal 不 robust" | Exception_only 在所有 seeds 上仍优于其他条件（worst seed 91.09% > VOTA 84.45%）。Seed sensitivity 是 LoRA training 问题而非 signal 问题——Qwen 3 seeds 完美证明 signal 本身 robust。D9 讨论 training stabilization 作为 practical recommendation。 |
222	| "exception_only 数据集 ~40-49% 重复，有效训练样本不足？" | 重复源自 representation compactness：同题多个 passing 解均无异常 → 相同 trace。**非数据泄漏**（train-test input overlap = 0）。raw_traces 仅 1.81% 重复，确认重复是 exception_only 表征特性而非数据收集问题。模型在有效样本仅 2858 unique 的条件下仍达 99.83%，反而说明 exception signal 的高 learnability — 少量 unique 样本即可充分学习 fault detection pattern。 |
223	
224	## Discussion 要点
225	
226	### D1: eval_loss vs verdict accuracy 解耦
227	DeepSeek VOTA: eval_loss epoch1→3 从 0.068 升至 0.112 (+65%), 但 accuracy 从 78.15% 升至 84.45% (+6.3pp). Token-level calibration 与 binary classification accuracy 方向相反. **Implication**: verdict tasks 应用 task-specific metric (accuracy/F1) 做 checkpoint selection, 非 eval_loss.
228	
229	### D2: CRUXEval gap 假说 (revised — D030 confound)
230	VOTA 跨模型 gap (14.96pp) 与 CRUXEval execution reasoning gap (15-17.5pp) 数值吻合. 假说: trace utilization effectiveness 受 base model "execution reasoning readiness" 约束. **标注**: hypothesis, N=2, 列出 alternatives. 不 overclaim. **注意**: 我们的训练/测试数据来自 HumanEval + MBPP-sanitized（非 CRUXEval），CRUXEval-I 分数仅作为衡量两个模型 execution reasoning 能力差异的外部参照。论文中必须明确区分数据来源与外部基准引用。**D030/D034 truncation evidence**: 14.96pp gap 中截断效应有因果证据: group_analysis 显示 train-truncated 83.04% vs train-intact 100% (Fisher p≈0, 推理时无截断)。截断因果方向可 claim，模型能力差异是 residual confound。CRUXEval gap 数值吻合可能部分巧合。论文中截断效应应作为 established factor 讨论（有 group_analysis 因果证据），模型能力假说标注为 residual confound hypothesis。
231	
232	### D3: Simplicity as robustness (revised)
233	Exception signal 在两模型上均为最优组件，其结构简单性确保了相对优势的跨模型 robustness。但 DeepSeek seed sensitivity 揭示：simplicity 确保 signal 本身 robust，但 LoRA 训练过程是否稳定收敛到正确映射取决于模型。**trace design 应匹配 deployment model 的能力下界**，且需关注 training stability（建议：多 seed 验证 + 考虑 training stabilization 技巧如 warmup、learning rate schedule）。
234	
235	### D4: Checkpoint selection 与 gap 报告 (revised)
236	正文报告所有 seeds 的 final checkpoint 结果 + best checkpoint 结果，不 cherry-pick。DeepSeek seed42: epoch1=99.83%, epoch3=99.33%（退化 0.50pp）。DeepSeek seed123: epoch1=91.43%, epoch3=91.09%（退化 0.34pp）。两个 seed 均显示轻微 epoch 退化，但核心差异在 epoch1 起点（8.40pp gap），不是训练过程。
237	
238	### D5: Irreducible samples — GeneratorExit 根因分析
239	3 seeds 的 2/1190 errors 完全相同（id=901, 905, 均来自 HumanEval/95 `check_dict_case`），方向一致（pass→fail false negatives）。
240	
241	**根因**: Python `all()` 对 generator expression 短路时丢弃未耗尽的 generator，触发 `GeneratorExit`。`GeneratorExit` 继承自 `BaseException`（非 `Exception`），是 Python 内部控制流机制而非真正错误。但 tracer 对所有 caught exceptions 统一标记 `[ERROR]`，导致 exception_only 模型看到 7 行 `[ERROR] GeneratorExit`，合理但错误地预测 fail。
242	
243	**为何不可约**:
244	1. **表征局限**: exception_only 条件下模型仅见异常数据，无法访问控制流、返回值或 assertion 结果。`GeneratorExit` 在此表征中与真正错误不可区分。
245	2. **跨 seed 确定性**: 3 个 random seeds 产生完全相同的 errors，确认这是 data/representation 属性而非模型初始化随机性。
246	3. **训练集无信号**: 整个 1190 条测试集仅这 2 条含 `GeneratorExit`，训练集中也缺乏足够的 `GeneratorExit` 良性样本供模型学习。
247	4. **人类也会犯错**: 仅看 exception trace（7 行 `[ERROR]`），人类审查者在不了解 Python generator protocol 的情况下也会预测 fail。
248	
249	**对论文的意义**: (1) 99.83% 是 exception_only representation 在此数据集上的理论 ceiling，非 saturation artifact；(2) 揭示 tracer 设计的改进方向——区分 `BaseException` 子类（如 `GeneratorExit`, `KeyboardInterrupt`）与 `Exception` 子类（真正的程序错误）可消除此类 irreducible error；(3) 提供 concrete evidence 说明 exception_only 模型"理解"的是 `[ERROR]` tag 的 fault indicator 语义，而非 exception type 的 fine-grained 含义。
250	
251	### D6: Calibration as secondary evidence
252	Calibration 数据提供独立于 accuracy 的 evidence dimension。no_trace Brier=0.1972 说明模型无 trace 时不仅预测错，且对错误预测过度自信。exception_only Brier=0.0013 说明模型在有 exception signal 时几乎完美区分确定性和不确定性。这支持 Claim 1 的 "sufficient signal" 论点——exception 不仅让模型预测对，还让模型 "知道自己对"。
253	
254	### D7: Early stopping for exception signal (revised — D030 epoch1 data complete)
255	3-seed epoch1 完整数据：seed42 epoch1=99.83% → epoch3=99.33%（-0.50pp）；**seed456 epoch1=99.33% → epoch3=99.33%（0.00pp）**；seed123 epoch1=91.43% → epoch3=91.09%（-0.34pp）。**seed42 的 epoch1=99.83%（匹配 Qwen）是该 seed 独有的 LoRA 初始化运气，不是 DeepSeek epoch1 的通用属性。** seed456 epoch1=epoch3 说明 epoch 退化非普遍现象。核心差异仍是 LoRA 初始化（epoch1 起点差 8.40pp），不是 overfitting。Early stopping 无法挽救差的初始化（seed123）。**Implication**: (1) 报告 DeepSeek 结果时应使用 median/2-of-3 (99.33%)，不应以 seed42 epoch1=99.83% 作为 headline；(2) epoch1 peak 是 LoRA 初始化运气的副产物，不具推广性。对比: VOTA 在 DeepSeek 上 84.45% **已确认正确**（D030 关闭: confirmatory re-eval max_length=16384 → 84.45%，与原始训练评估精确一致；D030 根因是 evaluate.py v2 的 max_length=2048 eval-time 截断 bug 导致 82.6% 预测为 garbage tokens）。
256	
257	### D9: LoRA initialization sensitivity as secondary bottleneck [NEW — D028]
258	DeepSeek exception_only seed42=99.83% vs seed123=91.43% (epoch1), 8.40pp gap。Qwen 3 seeds 完全一致。假说：exception signal 的 learnability 取决于 (1) signal 本身的结构简单性（cross-model robust）+ (2) LoRA 初始化是否落入能正确映射 exception→verdict 的 basin。Qwen-7B 可能因模型更强/LoRA landscape 更平滑而对初始化不敏感。DeepSeek-6.7B（CRUXEval-I 39% vs Qwen 56.5%）的 loss landscape 可能更 rugged，LoRA 初始化更易陷入 suboptimal basin（seed123 的 fail_recall 仅 70-72% 说明模型未学到 exception→fail 映射的关键部分）。**论文角度**: 这不是 negative result——它揭示了 trace SFT 的 practical consideration（training stability），可作为 contribution 的一部分。建议 Discussion 讨论 training stabilization 策略（warmup, lr schedule, LoRA rank 调整, multi-seed selection）。
259	
260	### D10: Train loss ≈ but accuracy ≠ across seeds [NEW — D029]
261	DeepSeek exception_only seed456 (train_loss=0.1225) 与 seed123 (train_loss=0.122) 训练损失几乎相同，但 accuracy 差 8.2pp（99.33% vs 91.09%）。关键差异集中在 fail_recall（1.0 vs 0.705）——token-level loss 在所有 tokens 上平均，掩盖了 fail 类少数样本的 sample-level 分类能力差异。**Implication**: (1) 扩展 D1 (eval_loss vs accuracy decoupling) 到训练阶段：train_loss 同样不是 verdict task accuracy 的可靠代理指标；(2) 对 checkpoint selection 的实际建议更强：必须用 task-specific metric (accuracy/F1)，甚至 train_loss 收敛也不保证 task performance；(3) fail 类作为少数类（28.5%），其学习质量被平均 loss 稀释——这在 class-imbalanced 设置下是 general pattern，可推广到其他 verdict/detection 任务。
262	
263	### D11: VOTA cross-model gap: training-time trace truncation as causal factor [NEW — D030 token analysis + group_analysis]
264	D030 token analysis 确认: `to_chat_text()` 保留 labels（verdict label 在训练时未被截断），但 91.7% 的 DeepSeek VOTA 训练样本的 **trace content** 从 mean 2626 tokens 被截断到 ~2048 tokens。
265	
266	**Group analysis 提供因果证据**: 将测试集按训练截断状态分组（推理时无截断, max_length=16384），train-truncated 组 accuracy=83.04% vs train-intact 组 accuracy=100%, Fisher exact p≈0。**截断的因果方向可以 claim**: 训练时 trace 被截断导致模型学到的信息不完整 → 推理时即使看到完整 trace 也无法正确判断。模型能力差异是残余 confound（无法完全分离）。
267	
268	**Implications**: (1) 论文中所有 "right-truncation corrupts/removes the verdict label" 措辞对 VOTA 不成立——label 完整保留，被截断的是 trace INPUT content；(2) 14.96pp gap 中截断效应有因果证据（group_analysis），模型能力差异是 residual confound；(3) exception_only 因 token 长度短（远低于 2048）不受截断影响，其跨模型对比更 clean——进一步强化 Claim 1 "most robust component" 叙事；(4) 论文应讨论 max_length 的影响作为 limitation/future work；(5) group_analysis 数据可作为 Table/Figure 纳入论文——展示截断的因果效应。
269	
270	### D8: Data duplication as representation signature
271	exception_only 训练集 39.45% 重复（4720→2858 unique），测试集 48.99%（1190→607 unique），而 raw_traces 仅 1.81%（5910→5803 unique）。重复源自 exception_only 表征的 design-by-intent compactness：同一编程题的多个 passing 解执行时均无异常，exception_only 表征退化为相同的空标记。这一数据特征本身就是 Claim 3 two-tier hierarchy 的佐证——Tier 1 信号仅编码 fault presence/absence，不编码 solution-level details，因此天然高重复。Train-test input overlap = 0 排除数据泄漏。
272	
273	## Contingency Framing (已解决, 留存档)
274	
275	### Claim 1 — RESOLVED (D029: seed456=99.33% confirms "consistently best component")
276	seed456 与 seed42 完全一致（均 99.33%），seed123 为孤立离群值。Claim 1 定稿为 "exception events consistently best component across models; absolute performance seed-dependent on DeepSeek (2/3 seeds robust, 1 outlier from LoRA init sensitivity); relative dominance over all alternatives robust across all seeds"。"0pp universal gap" 叙事已放弃，转为数据驱动的 nuanced framing。
277	
278	### Claim 2 — RESOLVED (D006 + D009)
279	v5 full_trace 81.76%. plan_002 label-only 86.22%, gradient dilution = minor (26%). 跨模型 VOTA gap 补充证据.
280	
281	## 与 v1 Framing 的关键差异
282	
283	| 维度 | v1 | v2.9 |
284	|------|----|----|
285	| Headline | VOTA compression 优于 full trace | Exception events are the most effective diagnostic signal |
286	| Primary claim | VOTA +24pp through fault indicator preservation | Exception signal consistently best across models; absolute performance seed-dependent on DeepSeek |
287	| Claim 2 | Compression > full trace (只有 gradient dilution) | Information density primary + gradient dilution quantification + cross-model reinforcement |
288	| Claim 3 Tier 1 | exception_only only | exception + assertion-point (co-Tier 1, D020) |
289	| VOTA 定位 | 核心方法 — trace compression | **Fault indicator isolation** — 价值在于提取 exception, 非 generic compression |
290	| Model scope | 单模型 (Qwen) | 双模型, 跨模型对比是核心贡献 |
291	| DeepSeek full_trace | N/A | v1 collapsed (label truncation), v3 pending |
292	| Seed robustness | 未验证 | Qwen ✅ 99.83% ± 0.00 (3 seeds); DeepSeek ⚠️ seed-dependent (91-99%, D028) |
293	| Irreducible error | 未分析 | ✅ GeneratorExit 根因明确，99.83% = representation ceiling |
294	| Calibration | 未验证 | ✅ 完整 ECE+Brier, ~63x/~150x gap vs no_trace |
295	| Data duplication | 未分析 | ✅ exception_only ~40% 重复（representation compactness），train-test overlap = 0 |
296	| Early stopping | 未讨论 | DeepSeek epoch1→epoch3 轻微退化 (0.3-0.5pp); 核心问题是 LoRA 初始化 (seed123 epoch1=91.43%), 非 overfitting |
297	| Narrative arc | "VOTA helps" | "Exception events are consistently best; VOTA's value is isolating them; training stability matters" |
298	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40a83622-b4f3-45b6-96fb-82e202cc39f6",
  "isSidechain": false,
  "promptId": "cde04d7b-c03d-49ea-b3f7-a9fea2ed96f5",
  "type": "user",
  "uuid": "e7aa2235-c4b6-409d-9749-f308c5e38a63",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/worst/paper_framing.md",
      "content": "# Paper Framing — trace-verdict-study\n\n> v3.0 — [UPDATED 2026-05-15] D030 CLOSED: DeepSeek VOTA 84.45% confirmed correct (confirmatory re-eval). **Critical narrative fix**: to_chat_text() preserves labels → VOTA 训练时 verdict label 未被截断 → 论文中 \"label truncation/corruption\" 措辞对 VOTA 不成立。正确叙事: trace INPUT content 被截断 (91.7% samples), 84.45% 反映 trace information loss。新增 D11: VOTA cross-model gap confounded by training-time truncation。数据集来源：HumanEval (164) + MBPP-sanitized (427) = 591 problems × 10 LLM-generated solutions = 5910 samples。\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission)\n- Fallback: EMNLP 2026 Findings\n- Deadline: ARR May 25, 2026\n\n## Core Insight\n\nVerdict prediction (pass/fail) is fundamentally a **fault detection** task. The most effective signal is the **exception event** — a compact, structured diagnostic moment that consistently outperforms all other trace representations across models (Qwen 99.83% ± 0.00 across 3 seeds; DeepSeek 91-99% depending on seed, but always > VOTA 84.45% and no_trace 73.36%). In contrast, richer trace representations that require deeper execution reasoning show model-dependent effectiveness: VOTA gap = 14.96pp, no_trace gap = 1.77pp. Information density — not training signal distribution — is the primary bottleneck: even oracle loss masking (label-only) cannot close the 13pp gap between full traces and targeted extraction. The design principle: **extract the highest-specificity diagnostic signal; discard everything else.** Cross-model absolute performance depends on LoRA initialization stability, but exception_only's relative dominance over other components is robust.\n\nVOTA's primary contribution is **fault indicator isolation** — automatically extracting exception events from noisy full traces — rather than generic trace compression. The \"compression helps\" narrative was a stepping stone; the real mechanism is diagnostic signal extraction.\n\n## Core Claims (3)\n\n### Claim 1: Exception events are the most effective trace component for verdict prediction\n\nException summaries consistently achieve the highest verdict prediction accuracy across both models tested, outperforming all other trace representations in every seed. On Qwen-2.5-Coder-7B, performance is perfectly robust: 99.83% ± 0.00 (3 seeds). On DeepSeek-Coder-6.7B, absolute accuracy is seed-dependent (seed42=99.83% epoch1, seed123=91.43% epoch1; Δ=8.40pp), consistent with LoRA initialization sensitivity — but exception_only still dominates VOTA (84.45%) and no_trace (73.36%) in all seeds. This contrasts with VOTA (cross-model gap = 14.96pp) and no_trace (gap = 1.77pp). Exception events are structurally simple (`[ERROR] type: ... message: ...`) and do not require deep trace reasoning.\n\n**Supporting evidence:**\n- `vota_exception_only_seed42_v2`: Qwen 99.83%, ECE=0.0027\n- `deepseek_exception_only_seed42`: DeepSeek 99.83% (epoch1) / 99.33% (epoch3)\n- `deepseek_exception_only_seed456`: DeepSeek 99.33% (epoch3), CI [98.82, 99.75] — 与 seed42 完全一致\n- `deepseek_exception_only_seed123`: DeepSeek 91.43% (epoch1) / 91.09% (epoch3) — LoRA init sensitivity outlier\n- `deepseek_vota_seed42`: DeepSeek VOTA 84.45% (gap = 14.96pp vs Qwen)\n- `deepseek_no_trace_seed42`: DeepSeek no_trace 73.36% (gap = 1.77pp vs Qwen)\n- `vota_no_ae_seed42`: 99.41% — actual/expected removal 不降，非 trivial string comparison\n\n**DeepSeek seed analysis** ✅ (FINALIZED, D029):\n\n| Seed | Epoch 3 (final) | fail_recall | pass_recall | train_loss | Errors | CI |\n|------|-----------------|-------------|-------------|------------|--------|-----|\n| 42   | 99.33%          | 1.0         | 0.9906      | —          | 8/1190 | — |\n| 456  | 99.33%          | 1.0         | 0.9906      | 0.1225     | 8/1190 | [98.82, 99.75] |\n| 123  | 91.09%          | 0.705       | 0.993       | 0.122      | —      | [89.4, 92.6] |\n\nseed42 与 seed456 结果**完全一致**（均 8/1190 错误，99.33%），seed123 为离群值。seed123 的 fail_recall 仅 0.705 — LoRA 初始化落入差的局部最优，未充分学到 exception→fail 映射。**关键发现**: seed456 和 seed123 的 train_loss 几乎相同（0.1225 vs 0.122），但 accuracy 差 8.2pp — token-level loss 掩盖了 sample-level 分类能力的巨大差异（详见 D10）。\n\n**Irreducible error analysis** ✅: 3 seeds 错误的 2 个样本 (id=901, 905) 均来自 HumanEval/95 (`check_dict_case`)，根因为 Python `all()` 对 generator expression 短路触发 `GeneratorExit`（`BaseException` 子类，非真正错误）。tracer 将其标记为 `[ERROR]`，exception_only 模型看到 7 行 `[ERROR] GeneratorExit`，合理但错误地预测 fail。整个 1190 条测试集仅这 2 条含 `GeneratorExit`，模型无训练信号学习其良性本质。**这确认 99.83% 是 exception_only 表征的理论上限，剩余 0.17% 是 representation-inherent irreducible error，而非模型不足。**\n\n**Seed robustness** ✅: Qwen exception_only 3-seed 完全一致，构成本文最强 robustness 证据：\n\n| Seed | Accuracy | 95% CI | Errors |\n|------|----------|--------|--------|\n| 42 | 99.83% | [99.58, 100] | 2/1190 |\n| 123 | 99.83% | [99.58, 100] | 2/1190 |\n| 456 | 99.83% | [99.58, 100] | 2/1190 |\n\n3 seeds 错误样本 100% 重叠（id=901, 905, 均为 `check_dict_case` 函数, label=pass → pred=fail）。**Irreducible samples**: 模型已达数据集理论上限，variance = 0。\n\n**DeepSeek cross-model** ✅ (D029): 3-seed 完整数据 — seed42/456=99.33%, seed123=91.09%。2/3 seeds 鲁棒，seed123 为 LoRA 初始化离群值（fail_recall 仅 0.705）。Qwen 3-seed 完美稳定 (99.83% ± 0.00) vs DeepSeek 高方差（σ≈4.8pp），暗示 exception signal 的 learnability 与模型 LoRA 训练稳定性相关。但即使最差 seed (91.09%) 仍优于 VOTA (84.45%) 和 no_trace (73.36%)，relative dominance robust。\n\n### Claim 2: Information density, not gradient dilution, drives trace compression benefit\n\nFull traces help verdict prediction (81.76% [`full_trace_seed42_v5`], +6.6pp over baseline), but VOTA achieves 99.41% [`vota_seed42_v5`] (+24.3pp) — a +17.6pp advantage. Label-only loss ablation (plan_002) quantifies the causal decomposition: **gradient dilution contributes ~26% of the gap** (4.5pp; label-only full_trace = 86.22% [`full_trace_label_only_seed42`]), **information overload contributes ~74%** (13.0pp; only trace compression resolves this). Even with oracle loss masking that eliminates gradient dilution, full traces still underperform VOTA by 13pp.\n\nCross-model evidence reinforces this: VOTA gap (14.96pp) partly tracks base model execution reasoning capability (Qwen CRUXEval-I 56.5% vs DeepSeek 39.0%, Δ=17.5pp), though **confounded by DeepSeek training-time trace truncation** (91.7% of VOTA samples truncated to ~2048 tokens; see D11). The two factors cannot be disentangled in the current design. Exception signal partially bypasses both bottlenecks (token-short, no truncation; consistently best component on both models), though DeepSeek shows seed-dependent absolute performance (91-99%).\n\n**Supporting evidence:**\n- `full_trace_label_only_seed42`: 86.22%, ECE=0.1107 (gradient dilution fix, +4.5pp over standard full_trace)\n- `full_trace_seed42_v5`: 81.76%, ECE=0.0958 (standard full_trace)\n- `vota_seed42_v5`: 99.41%, ECE=0.0054\n- `deepseek_vota_seed42`: 84.45% (VOTA model-dependent)\n- CRUXEval literature data (Wang et al.)\n\n### Claim 3: Two-tier diagnostic hierarchy for verdict prediction\n\nComponent ablation reveals verdict-relevant trace information has a strict two-tier hierarchy:\n- **Tier 1 — diagnostic moment signals**: exception summaries (99.83% [`vota_exception_only_seed42_v2`]) and assertion-point information (99.92% [`vota_ae_only_seed42`]) are individually near-perfect and sufficient for verdict prediction on Qwen. These signals are structurally simple and consistently the most effective component on both models, though DeepSeek absolute performance is seed-dependent.\n- **Tier 2 — behavioral patterns**: loop compression (85.63% [`vota_loop_only_seed42`]) carries substantial signal but is model-dependent and fully subsumed by Tier 1.\n\nCombining tiers introduces noise rather than helping: exception_only (99.83%) > VOTA full (99.41%), p=0.01. Loop_only ≈ full_trace_label_only (85.63% vs 86.22%) confirms VOTA's loop compression precisely extracts the useful behavioral signal from full traces.\n\n**Supporting evidence:**\n- `vota_exception_only_seed42_v2`: 99.83%, ECE=0.0027 (Tier 1 exception)\n- `vota_ae_only_seed42`: 99.92%, ECE=0.0004 (Tier 1 assertion-point, 与 exception 统计等价 p=0.80)\n- `vota_loop_only_seed42`: 85.63%, ECE=0.0831 (Tier 2 behavioral)\n- `full_trace_label_only_seed42`: 86.22%, ECE=0.1107 (≈ loop_only, confirming extraction equivalence)\n- `deepseek_exception_only_seed42`: 99.83% epoch1 / 99.33% epoch3 (Tier 1 cross-model validation)\n- `deepseek_vota_seed42`: 84.45% (Tier 1+2 cross-model: Tier 2 introduces model-dependent degradation)\n\n**Calibration**: 完整 calibration 数据确认 Tier 1 信号不仅 accuracy 近完美，置信度校准也近完美：\n\n| Condition | Accuracy | ECE | Brier | 解读 |\n|-----------|----------|-----|-------|------|\n| ae_only | 99.92% | 0.0004 | 0.0008 | 近乎完美校准 |\n| exception_only | 99.83% | 0.0027 | 0.0013 | 近乎完美校准 |\n| VOTA | 99.41% | 0.0054 | 0.005 | 优秀，但 Tier 2 引入轻微 noise |\n| loop_only | 85.63% | 0.0831 | — | Tier 2 单独校准中等 |\n| label_only | 86.22% | 0.1107 | — | gradient dilution fix 仍 miscalibrated |\n| full_trace | 81.76% | 0.0958 | — | 中度 miscalibrated |\n| no_trace | 75.13% | 0.1715 | 0.1972 | 严重 miscalibrated |\n\nno_trace ECE 是 exception_only 的 **~63x**（0.1715/0.0027），Brier 是 **~150x**（0.1972/0.0013）。Trace signal（尤其 Tier 1）不仅提升 accuracy，更从根本上改善模型 calibration。\n\n**Design principle**: verdict-optimized traces should extract highest-specificity diagnostic signals; lower-specificity signals are redundant and may introduce noise.\n\n## Cross-Model Evidence Summary\n\n| Condition | Qwen-2.5-Coder-7B | DeepSeek-Coder-6.7B | Cross-model gap | Interpretation |\n|-----------|-------------------|---------------------|-----------------|----------------|\n| exception_only | 99.83% ± 0.00 (3 seeds) | seed42/456: 99.33%; seed123: 91.09% | 0.50-8.74pp (seed-dependent) | **Best component on both models**; 2/3 DeepSeek seeds match Qwen-level; 1 outlier still > VOTA |\n| VOTA | 99.41% | 84.45% | -14.96pp | Model-dependent — requires execution reasoning; **also confounded by DeepSeek training-time trace truncation** (91.7% of VOTA samples truncated from mean 2626 to ~2048 tokens; labels preserved via to_chat_text(), see D11) |\n| no_trace | 75.13% | 73.36% | -1.77pp | Baseline gap tracks general capability |\n| full_trace | 81.76% | collapsed (v3 pending) | N/A | DeepSeek v1 label truncation bug |\n\n**Key insight**: Exception_only is consistently the best component on both models (even worst DeepSeek seed 91.09% > VOTA 84.45%). Cross-model gap 与 signal complexity 正相关, but exception signal's absolute effectiveness also depends on LoRA training stability. Qwen: perfectly robust (3 seeds identical). DeepSeek: 2/3 seeds at 99.33% (matching Qwen-level), 1 outlier at 91.09% (LoRA initialization). Median performance robust; seed sensitivity suggests smaller/weaker models may need training stabilization (multi-seed selection, warmup tuning) for optimal exception signal utilization.\n\n## VOTA Repositioning\n\n**旧叙事**: VOTA 是 trace compression 方法，价值在于\"压缩使 trace 更有效\"。\n\n**新叙事**: VOTA 是 **fault indicator isolation** 方法，核心价值在于自动从 noisy execution traces 中提取 exception events 等 diagnostic signals。\n\n**证据链**:\n1. exception_only (99.83%) ≥ VOTA full (99.41%) — 压缩后的其他组件（loop, ae）不仅无益，反而引入 noise\n2. VOTA 跨模型 gap = 14.96pp — 因为 VOTA 包含 model-dependent 的 Tier 2 组件（loop compression 需要 execution reasoning）\n3. exception_only 在两个模型上均为最优组件 — isolate 出 Tier 1 后，相对优势 robust（虽然 DeepSeek 绝对值 seed-dependent）\n4. vota_no_ae (99.41%) = VOTA (99.41%) — actual/expected 移除无影响，exception 是真正的 active ingredient\n\n**论文中的表述**: \"VOTA's trace compression pipeline incidentally isolates exception events — the minimal sufficient diagnostic signal. Its value lies not in making traces shorter, but in separating high-specificity fault indicators from low-specificity behavioral patterns.\"\n\n**对 Method section 的影响**: VOTA 仍然完整描述（loop compression + exception + actual/expected），但 Results/Discussion 明确指出 exception isolation 是核心机制，其他组件是 model-capability-dependent bonus。\n\n## Story Spine\n\n- **Problem**: Existing trace SFT studies (DCSH, TracePile) evaluate only generative tasks and find limited, model-dependent benefit. No prior work has tested trace SFT on verdict tasks (binary pass/fail), nor identified what trace components drive classification performance.\n\n- **Existing approaches & gaps**: DCSH (EMNLP Findings 2025) tested 5 trace formats on generation tasks, finding that \"no single trace representation consistently outperforms others.\" TracePile (NeurIPS 2025) scaled to 2.6M samples but only evaluated generation. TRACED (ICSE 2024) showed traces help encoder-based classification. All existing trace formats are designed for execution simulation, not fault detection.\n\n- **Our framing**: We reframe verdict prediction as **fault detection** and ask: what is the minimal sufficient diagnostic signal? Through systematic component ablation across two architecturally distinct models, we discover that exception events — compact, structured error summaries — are consistently the most effective trace component, achieving near-perfect accuracy on Qwen (99.83% ± 0.00, 3 seeds) and outperforming all alternatives on DeepSeek (91-99% vs VOTA 84.45%). Richer trace representations work only when the base model has sufficient execution reasoning capability, making them unreliable for general deployment.\n\n- **Headline result**: \"Exception events consistently achieve the highest verdict accuracy across models (Qwen 99.83%, DeepSeek 91-99%), outperforming VOTA traces (84.45% on DeepSeek, -14.96pp gap) — demonstrating that fault indicator isolation, not trace reasoning, is the robust mechanism for verdict prediction. DeepSeek seed sensitivity reveals LoRA training stability as a secondary factor for smaller models.\"\n\n## Story Arc\n\n1. **Setup**: Trace SFT for code tasks — promising but inconsistent in prior work (DCSH, TracePile). Unknown whether traces help verdict tasks and what trace design matters.\n\n2. **First result — traces help, compression helps more** (single model): no_trace 75.13% → full_trace 81.76% → VOTA 99.41%. Label-only loss ablation decomposes the gap: 26% gradient dilution, 74% information overload. Compression improves accuracy through higher information density, not just cost savings.\n\n3. **Twist — what component actually drives VOTA?** Component ablation reveals exception_only (99.83%) ≥ full VOTA (99.41%). The \"trace reasoning\" narrative is wrong — verdict prediction is fault detection. Tier 1 (exceptions + assertion-point) subsumes Tier 2 (loops). Actual/expected removal doesn't hurt (99.41%).\n\n4. **Cross-model stress test — consistent dominance, not universal perfection**: Exception_only is the best component on both models (even DeepSeek worst seed 91.09% > VOTA 84.45%), but absolute performance is seed-dependent on DeepSeek (91-99% vs Qwen's perfectly stable 99.83%). VOTA degrades by 14.96pp. The structurally simplest component is the most robust, but LoRA initialization sensitivity introduces variance on weaker models. Qwen seed robustness (3-seed variance = 0) + calibration (ECE=0.0027) 确认 exception signal 在强模型上的 reliability。DeepSeek seed sensitivity 揭示 training stability 作为 secondary bottleneck。\n\n5. **Design principle**: For verdict tasks, identify the highest-specificity diagnostic signal (exception events) and discard everything else. VOTA's value is fault indicator isolation — automatically extracting exceptions from noisy traces — not generic compression. Simpler signals are more robust; complexity tolerance depends on model capability.\n\n## Dataset Characteristics\n\n### Data duplication analysis\n\n| Condition | Total | Unique | Duplication rate | Cause |\n|-----------|-------|--------|------------------|-------|\n| exception_only_train | 4720 | 2858 | 39.45% | 同题多个 passing 解映射为相同 (input, output) — 无异常 → 同一 trace |\n| exception_only_test | 1190 | 607 | 48.99% | 同上 |\n| raw_traces | 5910 | 5803 | 1.81% | 完整 trace 含行号/变量值/内存地址，几乎不重复 |\n\n**Train-test input overlap: 0（无数据泄漏）**\n\n**解读**: exception_only 高重复率是 representation 的自然属性，非数据问题。多个正确解对同一测试用例执行时若均无异常，exception_only 表征退化为相同的空/无异常标记。这恰好说明 exception signal 的 compactness — 它仅编码 fault presence，不编码 solution identity。raw_traces 重复率极低 (1.81%) 因为完整 trace 包含 solution-specific 信息（变量值、内存地址）。尽管高重复率意味着有效训练样本少于名义数量，模型仍达 99.83% — 进一步确认 exception signal 的 learnability。\n\n## DeepSeek full_trace 处理\n\n**现状**: v1 坍塌（28.5%, 100% 预测 fail, 根因: 训练端 label 截断）。v2 重训启动但被 kill（Loop #6 ops worker 腾 GPU 给 vota_seed456）。v3 RUNNING（label-preserving truncation fix）。\n\n**处理方案**: v3 正在 cuda:0 上训练，预计 5/16 完成。\n\n**VOTA vs full_trace 截断机制区分** (D030 token analysis 确认):\n- **full_trace v1**: SFTTrainer right-truncation 切掉了 verdict **label** → 100% predict fail → 坍塌。根因: DeepSeek tokenizer 对 full_trace 产生 >2048 tokens, label 在截断窗口外。\n- **VOTA**: `to_chat_text()` 保留 verdict label（label 完整），但 91.7% 的样本 **trace content（input）被截断**（mean 2626 → ~2048 tokens）。84.45% 是真实结果，反映 trace 信息损失对模型学习的影响，**不是** label corruption。\n- **exception_only**: token 长度远低于 2048，不受截断影响，跨模型对比 clean。\n\n**对论文叙事的影响**: 论文中所有 \"right-truncation corrupts/removes the verdict label\" 措辞**对 VOTA 不成立**——label 完整保留，被截断的是 trace input。正确表述: \"trace content truncation causes information loss\"。VOTA cross-model gap (14.96pp) 有两个贡献因素: (1) model capability, (2) training-time trace truncation on DeepSeek (see D11)。\n\n## External Benchmark (DebugBench) Positioning\n\n**DebugBench 仅作泛化性验证，不作 trace importance 证据。**\n\n| Condition | Main Dataset | DebugBench | Δ interpretation |\n|-----------|-------------|------------|------------------|\n| no_trace | 75.13% | 96.71% | DebugBench 天花板高，baseline 已强 |\n| VOTA | 99.41% | 99.77% | +3.06pp lift — 边际 |\n| exception_only | 99.83% | 100.00% | +3.29pp lift — 边际 |\n\n**主数据集 trace lift = 24.70pp**（no_trace → exception_only），DebugBench trace lift 不到其 1/7。\n\n**论文定位规则**：\n- DebugBench → 泛化性证据（exception_only 100% = 跨数据集鲁棒性）\n- Trace importance 论证 → 仅依赖主数据集（24.7pp lift）\n- 禁止用 DebugBench 的 3.29pp lift 论证 \"trace 的核心价值\"——审稿人会攻击天花板效应\n\n## Venue Fit Risks\n\n| Risk | Assessment | Mitigation |\n|------|-----------|------------|\n| 单任务 | 仍然只在 test verdict prediction 上验证 | 跨模型验证部分弥补; Discussion 中讨论 generalization |\n| 单数据集 | HumanEval + MBPP-sanitized 是唯一数据源 (591 problems × 10 solutions) | 定位为 empirical study, 深度优于广度; 两个标准 benchmark 组合覆盖多样编程题型; exception_only 有效训练样本仅 2858 unique 即达 99.83%, 暗示 signal 的 simplicity 降低对数据量的依赖 |\n| \"只是 feature engineering\" | exception extraction 不复杂 | simplicity 本身是 contribution — 最简信号最 robust |\n| Negative result 味道 | VOTA 跨模型不 robust | Reframe: 识别 robust vs non-robust 组件边界是 positive |\n| Seed robustness (Qwen) | ✅ 已解决: 99.83% ± 0.00 (3 seeds), irreducible samples 确认 | — |\n| Seed robustness (DeepSeek) | ✅ 3-seed 完整: 2/3 at 99.33%, 1 at 91.09% | LoRA initialization sensitivity — median robust, worst still > all alternatives; 转化为 training stability finding (D9/D10) |\n| Calibration | ✅ 完整数据: Tier 1 ECE≤0.003, no_trace ECE=0.171 (~63x gap) | Brier ~150x gap 进一步确认 |\n| 只用 2 个模型 | 有限但有意义的 diversity | Architecture + pretraining data (5.5T vs 2T) + CRUXEval gap (17.5pp) 构成充分差异 |\n| 数据重复率 | exception_only 训练集 39.45% 重复 | 非数据泄漏（train-test overlap = 0）；是 representation compactness 的自然结果；有效样本仍足够学习 |\n\n## Anticipated Reviewer Concerns\n\n| Concern | Planned Response |\n|---------|-----------------|\n| \"exception_only 99.83% 是不是 trivial pattern matching [ERROR] 有无？\" | full_trace 也包含 [ERROR] 但仅 81.76%——模型需要从 trace context 中 extract 和 utilize exception signal, 不是简单 keyword detection. no_trace 无 exception, 75.13%. |\n| \"为什么 exception_only > VOTA? adding info 反而降?\" | 非 exception 组件 (loop/ae tokens) 稀释 attention 对 exception 信号的聚焦. Calibration: exception_only ECE=0.0027 vs VOTA ECE=0.0054. 部分样本 loop 正常但有 exception, 引入矛盾信号. |\n| \"CRUXEval gap 与 VOTA gap 的相关性可能是 coincidence\" | 明确标注为 hypothesis. 列出 alternatives (tokenizer efficiency, pretraining scale 2.75x, chat template). 不 overclaim. |\n| \"只有 2 个模型，universality claim 太强\" | 同意是 limitation. 两模型在 architecture (RoPE vs ALiBi), pretraining data (5.5T vs 2T), execution reasoning (CRUXEval 17.5pp gap) 上有充分差异, 不是 trivial replication. Exception signal 的 structural simplicity 提供 inductive argument for broader generalization. |\n| \"99.83% 可能 saturated, 看不出 exception 到底学了什么\" | Calibration 双指标: exception_only ECE=0.0027, Brier=0.0013 (近完美校准). 对比 no_trace ECE=0.1715, Brier=0.1972 (~63x/~150x gap). **Irreducible error 根因已明确**: 2/1190 errors 均因 Python `all()` 短路触发 `GeneratorExit`（`BaseException` 子类，非真正错误），tracer 将其标记为 `[ERROR]`。模型看到 7 行 `[ERROR] GeneratorExit` 合理预测 fail，但代码实际正确。整个测试集仅这 2 条含 `GeneratorExit`，无训练信号可学习其良性本质。99.83% 是 representation 的理论上限，非 saturation artifact。 |\n| \"只用了 1 个 seed\" | Qwen ✅: 3 seeds 99.83% ± 0.00. DeepSeek ✅: 3 seeds 完整 — seed42/456=99.33%, seed123=91.09%。2/3 鲁棒，1 离群。median=99.33%, worst=91.09% (仍 > VOTA 84.45%)。论文透明报告所有 seeds，将 seed sensitivity 转化为 LoRA training stability 的 finding（D9）。 |\n| \"eval_loss 上升但 accuracy 提升——checkpoint selection 有问题?\" | Discussion D1: token-level loss 与 binary verdict accuracy 解耦. 推荐 verdict-specific metric. Methodological contribution. |\n| \"DeepSeek full_trace 坍塌是 bug 不是 finding\" | 诚实披露根因 (训练端 label 截断). 其他 3 条件不受影响. 修复版本如就绪则补入. |\n| \"calibration 数据只有 1 个 seed\" | Seed robustness 已证明 accuracy variance=0 (3 seeds), calibration 在 accuracy 完全一致的前提下 expected 也一致. ECE/Brier 的极小值 (0.0027/0.0013) 留有极小 variance 空间. |\n| \"DeepSeek epoch1 > epoch3, 为什么用 epoch3 报告?\" | 正文报告所有 seeds 的 final + best checkpoint。seed42: epoch1=99.83%, epoch3=99.33%。seed123: epoch1=91.43%, epoch3=91.09%。D7 讨论 early stopping + D9 讨论 LoRA initialization sensitivity。不 cherry-pick best seed。 |\n| \"DeepSeek seed sensitivity 说明 exception signal 不 robust\" | Exception_only 在所有 seeds 上仍优于其他条件（worst seed 91.09% > VOTA 84.45%）。Seed sensitivity 是 LoRA training 问题而非 signal 问题——Qwen 3 seeds 完美证明 signal 本身 robust。D9 讨论 training stabilization 作为 practical recommendation。 |\n| \"exception_only 数据集 ~40-49% 重复，有效训练样本不足？\" | 重复源自 representation compactness：同题多个 passing 解均无异常 → 相同 trace。**非数据泄漏**（train-test input overlap = 0）。raw_traces 仅 1.81% 重复，确认重复是 exception_only 表征特性而非数据收集问题。模型在有效样本仅 2858 unique 的条件下仍达 99.83%，反而说明 exception signal 的高 learnability — 少量 unique 样本即可充分学习 fault detection pattern。 |\n\n## Discussion 要点\n\n### D1: eval_loss vs verdict accuracy 解耦\nDeepSeek VOTA: eval_loss epoch1→3 从 0.068 升至 0.112 (+65%), 但 accuracy 从 78.15% 升至 84.45% (+6.3pp). Token-level calibration 与 binary classification accuracy 方向相反. **Implication**: verdict tasks 应用 task-specific metric (accuracy/F1) 做 checkpoint selection, 非 eval_loss.\n\n### D2: CRUXEval gap 假说 (revised — D030 confound)\nVOTA 跨模型 gap (14.96pp) 与 CRUXEval execution reasoning gap (15-17.5pp) 数值吻合. 假说: trace utilization effectiveness 受 base model \"execution reasoning readiness\" 约束. **标注**: hypothesis, N=2, 列出 alternatives. 不 overclaim. **注意**: 我们的训练/测试数据来自 HumanEval + MBPP-sanitized（非 CRUXEval），CRUXEval-I 分数仅作为衡量两个模型 execution reasoning 能力差异的外部参照。论文中必须明确区分数据来源与外部基准引用。**D030/D034 truncation evidence**: 14.96pp gap 中截断效应有因果证据: group_analysis 显示 train-truncated 83.04% vs train-intact 100% (Fisher p≈0, 推理时无截断)。截断因果方向可 claim，模型能力差异是 residual confound。CRUXEval gap 数值吻合可能部分巧合。论文中截断效应应作为 established factor 讨论（有 group_analysis 因果证据），模型能力假说标注为 residual confound hypothesis。\n\n### D3: Simplicity as robustness (revised)\nException signal 在两模型上均为最优组件，其结构简单性确保了相对优势的跨模型 robustness。但 DeepSeek seed sensitivity 揭示：simplicity 确保 signal 本身 robust，但 LoRA 训练过程是否稳定收敛到正确映射取决于模型。**trace design 应匹配 deployment model 的能力下界**，且需关注 training stability（建议：多 seed 验证 + 考虑 training stabilization 技巧如 warmup、learning rate schedule）。\n\n### D4: Checkpoint selection 与 gap 报告 (revised)\n正文报告所有 seeds 的 final checkpoint 结果 + best checkpoint 结果，不 cherry-pick。DeepSeek seed42: epoch1=99.83%, epoch3=99.33%（退化 0.50pp）。DeepSeek seed123: epoch1=91.43%, epoch3=91.09%（退化 0.34pp）。两个 seed 均显示轻微 epoch 退化，但核心差异在 epoch1 起点（8.40pp gap），不是训练过程。\n\n### D5: Irreducible samples — GeneratorExit 根因分析\n3 seeds 的 2/1190 errors 完全相同（id=901, 905, 均来自 HumanEval/95 `check_dict_case`），方向一致（pass→fail false negatives）。\n\n**根因**: Python `all()` 对 generator expression 短路时丢弃未耗尽的 generator，触发 `GeneratorExit`。`GeneratorExit` 继承自 `BaseException`（非 `Exception`），是 Python 内部控制流机制而非真正错误。但 tracer 对所有 caught exceptions 统一标记 `[ERROR]`，导致 exception_only 模型看到 7 行 `[ERROR] GeneratorExit`，合理但错误地预测 fail。\n\n**为何不可约**:\n1. **表征局限**: exception_only 条件下模型仅见异常数据，无法访问控制流、返回值或 assertion 结果。`GeneratorExit` 在此表征中与真正错误不可区分。\n2. **跨 seed 确定性**: 3 个 random seeds 产生完全相同的 errors，确认这是 data/representation 属性而非模型初始化随机性。\n3. **训练集无信号**: 整个 1190 条测试集仅这 2 条含 `GeneratorExit`，训练集中也缺乏足够的 `GeneratorExit` 良性样本供模型学习。\n4. **人类也会犯错**: 仅看 exception trace（7 行 `[ERROR]`），人类审查者在不了解 Python generator protocol 的情况下也会预测 fail。\n\n**对论文的意义**: (1) 99.83% 是 exception_only representation 在此数据集上的理论 ceiling，非 saturation artifact；(2) 揭示 tracer 设计的改进方向——区分 `BaseException` 子类（如 `GeneratorExit`, `KeyboardInterrupt`）与 `Exception` 子类（真正的程序错误）可消除此类 irreducible error；(3) 提供 concrete evidence 说明 exception_only 模型\"理解\"的是 `[ERROR]` tag 的 fault indicator 语义，而非 exception type 的 fine-grained 含义。\n\n### D6: Calibration as secondary evidence\nCalibration 数据提供独立于 accuracy 的 evidence dimension。no_trace Brier=0.1972 说明模型无 trace 时不仅预测错，且对错误预测过度自信。exception_only Brier=0.0013 说明模型在有 exception signal 时几乎完美区分确定性和不确定性。这支持 Claim 1 的 \"sufficient signal\" 论点——exception 不仅让模型预测对，还让模型 \"知道自己对\"。\n\n### D7: Early stopping for exception signal (revised — D030 epoch1 data complete)\n3-seed epoch1 完整数据：seed42 epoch1=99.83% → epoch3=99.33%（-0.50pp）；**seed456 epoch1=99.33% → epoch3=99.33%（0.00pp）**；seed123 epoch1=91.43% → epoch3=91.09%（-0.34pp）。**seed42 的 epoch1=99.83%（匹配 Qwen）是该 seed 独有的 LoRA 初始化运气，不是 DeepSeek epoch1 的通用属性。** seed456 epoch1=epoch3 说明 epoch 退化非普遍现象。核心差异仍是 LoRA 初始化（epoch1 起点差 8.40pp），不是 overfitting。Early stopping 无法挽救差的初始化（seed123）。**Implication**: (1) 报告 DeepSeek 结果时应使用 median/2-of-3 (99.33%)，不应以 seed42 epoch1=99.83% 作为 headline；(2) epoch1 peak 是 LoRA 初始化运气的副产物，不具推广性。对比: VOTA 在 DeepSeek 上 84.45% **已确认正确**（D030 关闭: confirmatory re-eval max_length=16384 → 84.45%，与原始训练评估精确一致；D030 根因是 evaluate.py v2 的 max_length=2048 eval-time 截断 bug 导致 82.6% 预测为 garbage tokens）。\n\n### D9: LoRA initialization sensitivity as secondary bottleneck [NEW — D028]\nDeepSeek exception_only seed42=99.83% vs seed123=91.43% (epoch1), 8.40pp gap。Qwen 3 seeds 完全一致。假说：exception signal 的 learnability 取决于 (1) signal 本身的结构简单性（cross-model robust）+ (2) LoRA 初始化是否落入能正确映射 exception→verdict 的 basin。Qwen-7B 可能因模型更强/LoRA landscape 更平滑而对初始化不敏感。DeepSeek-6.7B（CRUXEval-I 39% vs Qwen 56.5%）的 loss landscape 可能更 rugged，LoRA 初始化更易陷入 suboptimal basin（seed123 的 fail_recall 仅 70-72% 说明模型未学到 exception→fail 映射的关键部分）。**论文角度**: 这不是 negative result——它揭示了 trace SFT 的 practical consideration（training stability），可作为 contribution 的一部分。建议 Discussion 讨论 training stabilization 策略（warmup, lr schedule, LoRA rank 调整, multi-seed selection）。\n\n### D10: Train loss ≈ but accuracy ≠ across seeds [NEW — D029]\nDeepSeek exception_only seed456 (train_loss=0.1225) 与 seed123 (train_loss=0.122) 训练损失几乎相同，但 accuracy 差 8.2pp（99.33% vs 91.09%）。关键差异集中在 fail_recall（1.0 vs 0.705）——token-level loss 在所有 tokens 上平均，掩盖了 fail 类少数样本的 sample-level 分类能力差异。**Implication**: (1) 扩展 D1 (eval_loss vs accuracy decoupling) 到训练阶段：train_loss 同样不是 verdict task accuracy 的可靠代理指标；(2) 对 checkpoint selection 的实际建议更强：必须用 task-specific metric (accuracy/F1)，甚至 train_loss 收敛也不保证 task performance；(3) fail 类作为少数类（28.5%），其学习质量被平均 loss 稀释——这在 class-imbalanced 设置下是 general pattern，可推广到其他 verdict/detection 任务。\n\n### D11: VOTA cross-model gap: training-time trace truncation as causal factor [NEW — D030 token analysis + group_analysis]\nD030 token analysis 确认: `to_chat_text()` 保留 labels（verdict label 在训练时未被截断），但 91.7% 的 DeepSeek VOTA 训练样本的 **trace content** 从 mean 2626 tokens 被截断到 ~2048 tokens。\n\n**Group analysis 提供因果证据**: 将测试集按训练截断状态分组（推理时无截断, max_length=16384），train-truncated 组 accuracy=83.04% vs train-intact 组 accuracy=100%, Fisher exact p≈0。**截断的因果方向可以 claim**: 训练时 trace 被截断导致模型学到的信息不完整 → 推理时即使看到完整 trace 也无法正确判断。模型能力差异是残余 confound（无法完全分离）。\n\n**Implications**: (1) 论文中所有 \"right-truncation corrupts/removes the verdict label\" 措辞对 VOTA 不成立——label 完整保留，被截断的是 trace INPUT content；(2) 14.96pp gap 中截断效应有因果证据（group_analysis），模型能力差异是 residual confound；(3) exception_only 因 token 长度短（远低于 2048）不受截断影响，其跨模型对比更 clean——进一步强化 Claim 1 \"most robust component\" 叙事；(4) 论文应讨论 max_length 的影响作为 limitation/future work；(5) group_analysis 数据可作为 Table/Figure 纳入论文——展示截断的因果效应。\n\n### D8: Data duplication as representation signature\nexception_only 训练集 39.45% 重复（4720→2858 unique），测试集 48.99%（1190→607 unique），而 raw_traces 仅 1.81%（5910→5803 unique）。重复源自 exception_only 表征的 design-by-intent compactness：同一编程题的多个 passing 解执行时均无异常，exception_only 表征退化为相同的空标记。这一数据特征本身就是 Claim 3 two-tier hierarchy 的佐证——Tier 1 信号仅编码 fault presence/absence，不编码 solution-level details，因此天然高重复。Train-test input overlap = 0 排除数据泄漏。\n\n## Contingency Framing (已解决, 留存档)\n\n### Claim 1 — RESOLVED (D029: seed456=99.33% confirms \"consistently best component\")\nseed456 与 seed42 完全一致（均 99.33%），seed123 为孤立离群值。Claim 1 定稿为 \"exception events consistently best component across models; absolute performance seed-dependent on DeepSeek (2/3 seeds robust, 1 outlier from LoRA init sensitivity); relative dominance over all alternatives robust across all seeds\"。\"0pp universal gap\" 叙事已放弃，转为数据驱动的 nuanced framing。\n\n### Claim 2 — RESOLVED (D006 + D009)\nv5 full_trace 81.76%. plan_002 label-only 86.22%, gradient dilution = minor (26%). 跨模型 VOTA gap 补充证据.\n\n## 与 v1 Framing 的关键差异\n\n| 维度 | v1 | v2.9 |\n|------|----|----|\n| Headline | VOTA compression 优于 full trace | Exception events are the most effective diagnostic signal |\n| Primary claim | VOTA +24pp through fault indicator preservation | Exception signal consistently best across models; absolute performance seed-dependent on DeepSeek |\n| Claim 2 | Compression > full trace (只有 gradient dilution) | Information density primary + gradient dilution quantification + cross-model reinforcement |\n| Claim 3 Tier 1 | exception_only only | exception + assertion-point (co-Tier 1, D020) |\n| VOTA 定位 | 核心方法 — trace compression | **Fault indicator isolation** — 价值在于提取 exception, 非 generic compression |\n| Model scope | 单模型 (Qwen) | 双模型, 跨模型对比是核心贡献 |\n| DeepSeek full_trace | N/A | v1 collapsed (label truncation), v3 pending |\n| Seed robustness | 未验证 | Qwen ✅ 99.83% ± 0.00 (3 seeds); DeepSeek ⚠️ seed-dependent (91-99%, D028) |\n| Irreducible error | 未分析 | ✅ GeneratorExit 根因明确，99.83% = representation ceiling |\n| Calibration | 未验证 | ✅ 完整 ECE+Brier, ~63x/~150x gap vs no_trace |\n| Data duplication | 未分析 | ✅ exception_only ~40% 重复（representation compactness），train-test overlap = 0 |\n| Early stopping | 未讨论 | DeepSeek epoch1→epoch3 轻微退化 (0.3-0.5pp); 核心问题是 LoRA 初始化 (seed123 epoch1=91.43%), 非 overfitting |\n| Narrative arc | \"VOTA helps\" | \"Exception events are consistently best; VOTA's value is isolating them; training stability matters\" |\n",
      "numLines": 298,
      "startLine": 1,
      "totalLines": 298
    }
  },
  "sourceToolAssistantUUID": "40a83622-b4f3-45b6-96fb-82e202cc39f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "175abc6b-2146-427e-acfe-4e3e17983955",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T125926 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-stu…",
  "leafUuid": "e7aa2235-c4b6-409d-9749-f308c5e38a63",
  "sessionId": "175abc6b-2146-427e-acfe-4e3e17983955"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier dream paper for dream_20260518T125926",
  "sessionId": "175abc6b-2146-427e-acfe-4e3e17983955"
}
```

---

### Assistant

_source line 16 · 2026-05-18T13:48:22.030Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data. Let me also check what LaTeX template/class is available in the directory.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7aa2235-c4b6-409d-9749-f308c5e38a63",
  "isSidechain": false,
  "requestId": "req_011CbA936EnR8DpEjp7vD4Xz",
  "type": "assistant",
  "uuid": "52eac921-3bbd-44cf-8e6f-37c1a174cdf4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "175abc6b-2146-427e-acfe-4e3e17983955",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XNkBkCHHQgTkAH4ah7GNLe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31225,
      "cache_read_input_tokens": 24698,
      "output_tokens": 149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31225,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 149,
          "cache_read_input_tokens": 24698,
          "cache_creation_input_tokens": 31225,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31225
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

_source line 17 · 2026-05-18T13:48:22.502Z_

Let me check what's already in the output directory.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52eac921-3bbd-44cf-8e6f-37c1a174cdf4",
  "isSidechain": false,
  "requestId": "req_011CbA936EnR8DpEjp7vD4Xz",
  "type": "assistant",
  "uuid": "72cdb790-ed56-40ce-a795-cc328fd4605a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "175abc6b-2146-427e-acfe-4e3e17983955",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XNkBkCHHQgTkAH4ah7GNLe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31225,
      "cache_read_input_tokens": 24698,
      "output_tokens": 149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31225,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 149,
          "cache_read_input_tokens": 24698,
          "cache_creation_input_tokens": 31225,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31225
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

_source line 18 · 2026-05-18T13:48:24.364Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01NEy5hUAAS88KUYXSkSqDk4`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/worst/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72cdb790-ed56-40ce-a795-cc328fd4605a",
  "isSidechain": false,
  "requestId": "req_011CbA936EnR8DpEjp7vD4Xz",
  "type": "assistant",
  "uuid": "d2b29191-3efc-4fd0-a79f-921ad3fde198",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "175abc6b-2146-427e-acfe-4e3e17983955",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XNkBkCHHQgTkAH4ah7GNLe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31225,
      "cache_read_input_tokens": 24698,
      "output_tokens": 149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31225,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 149,
          "cache_read_input_tokens": 24698,
          "cache_creation_input_tokens": 31225,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31225
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

_source line 19 · 2026-05-18T13:48:24.562Z_

<details><summary>↩ Tool result · `toolu_01NEy5hUAAS88KUYXSkSqDk4`</summary>

```text
total 136
drwxr-xr-x 2 ubuntu ubuntu  4096 May 18 13:48 .
drwxr-xr-x 6 ubuntu ubuntu  4096 May 18 13:48 ..
-rw-r--r-- 1 ubuntu ubuntu 43756 May 18 13:48 experiment_data.json
-rw-r--r-- 1 ubuntu ubuntu 41940 May 18 13:48 imagined_experiments.yaml
-rw-r--r-- 1 ubuntu ubuntu 37205 May 18 13:48 paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2b29191-3efc-4fd0-a79f-921ad3fde198",
  "isSidechain": false,
  "promptId": "cde04d7b-c03d-49ea-b3f7-a9fea2ed96f5",
  "type": "user",
  "uuid": "eccb793b-6e6b-42e3-ab16-748edb4d61f4",
  "toolUseResult": {
    "stdout": "total 136\ndrwxr-xr-x 2 ubuntu ubuntu  4096 May 18 13:48 .\ndrwxr-xr-x 6 ubuntu ubuntu  4096 May 18 13:48 ..\n-rw-r--r-- 1 ubuntu ubuntu 43756 May 18 13:48 experiment_data.json\n-rw-r--r-- 1 ubuntu ubuntu 41940 May 18 13:48 imagined_experiments.yaml\n-rw-r--r-- 1 ubuntu ubuntu 37205 May 18 13:48 paper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "d2b29191-3efc-4fd0-a79f-921ad3fde198",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "175abc6b-2146-427e-acfe-4e3e17983955",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-18T13:48:27.135Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01G2esbfaY57L5ie288hjJvG`</summary>

```json
{
  "command": "which pdflatex && pdflatex --version 2>&1 | head -3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eccb793b-6e6b-42e3-ab16-748edb4d61f4",
  "isSidechain": false,
  "requestId": "req_011CbA93YCyzUY8ySJ1iRgbP",
  "type": "assistant",
  "uuid": "6359589d-2aac-4034-b5f8-d48ea69d11d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "175abc6b-2146-427e-acfe-4e3e17983955",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S3URRZ5LAVQRUu9WLKkfUE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 315,
      "cache_read_input_tokens": 55923,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 315,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 55923,
          "cache_creation_input_tokens": 315,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 315
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

_source line 21 · 2026-05-18T13:48:27.218Z_

<details><summary>↩ Tool result · `toolu_01G2esbfaY57L5ie288hjJvG`</summary>

```text
/usr/bin/pdflatex
pdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian)
kpathsea version 6.4.1
Copyright 2025 Han The Thanh (pdfTeX) et al.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6359589d-2aac-4034-b5f8-d48ea69d11d5",
  "isSidechain": false,
  "promptId": "cde04d7b-c03d-49ea-b3f7-a9fea2ed96f5",
  "type": "user",
  "uuid": "e7bd37b5-197d-45eb-b8b2-baa61a8745b5",
  "toolUseResult": {
    "stdout": "/usr/bin/pdflatex\npdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian)\nkpathsea version 6.4.1\nCopyright 2025 Han The Thanh (pdfTeX) et al.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "6359589d-2aac-4034-b5f8-d48ea69d11d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "175abc6b-2146-427e-acfe-4e3e17983955",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-18T13:48:45.183Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information needed. Let me write the complete LaTeX paper. The paper should follow the narrative guidance:

- Exception events as the only universally robust trace signal
- All other trace components and budget-length relationships are model-dependent
- Budget curve moves from Results to Appendix
- Few-shot GPT-4o baseline is close to SFT (~97% vs 99.83%), need cost efficiency + calibration superiority to defend SFT value
- OOD generalization is limited
- Reframe: exception dominance simplicity + universality as the only anchor


- I need to make sure I'm covering all the experiments across different models (Qwen-7B, Qwen-1.5B, DeepSeek, CodeLlama), cross-model synthesis, cross-seed robustness, and error analysis to build a comprehensive narrative.

Now I'm planning the paper structure with an abstract, introduction, related work, and methods section covering VOTA trace compression and exception isolation, followed by experiments that showcase exception dominance, information density, the two-tier hierarchy, cross-model calibration, few-shot baselines against GPT-4o and Claude, budget curves, training dynamics, error analysis, and out-of-distribution generalization.

I need to be precise with the experimental data, avoid common AI writing patterns like dashes and repetitive transitions, and ensure every experiment gets proper coverage while keeping exception dominance as the central narrative thread.

Writing the LaTeX paper now...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7bd37b5-197d-45eb-b8b2-baa61a8745b5",
  "isSidechain": false,
  "requestId": "req_011CbA93jYMkC3sUmhDh3Dpi",
  "type": "assistant",
  "uuid": "689eeb04-e130-4738-94f9-67152c156867",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "175abc6b-2146-427e-acfe-4e3e17983955",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018LW28UiYePFoqjNs9CGvej",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 155,
      "cache_read_input_tokens": 56238,
      "output_tokens": 10002,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 155,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10002,
          "cache_read_input_tokens": 56238,
          "cache_creation_input_tokens": 155,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 155
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

_source line 23 · 2026-05-18T13:48:45.184Z_

Now I'll write the full LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "689eeb04-e130-4738-94f9-67152c156867",
  "isSidechain": false,
  "requestId": "req_011CbA93jYMkC3sUmhDh3Dpi",
  "type": "assistant",
  "uuid": "0119528d-6ec5-4ec0-a007-fadcf2a1759f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "175abc6b-2146-427e-acfe-4e3e17983955",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018LW28UiYePFoqjNs9CGvej",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 155,
      "cache_read_input_tokens": 56238,
      "output_tokens": 10002,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 155,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10002,
          "cache_read_input_tokens": 56238,
          "cache_creation_input_tokens": 155,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 155
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

_source line 24 · 2026-05-18T13:51:55.269Z_

<details open><summary>🔧 Tool call — Write · `toolu_01HUHLbqjV4NxkKCcXEJf8X1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/worst/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage{xcolor}\n\\usepackage{multirow}\n\\usepackage{tablefootnote}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{enumitem}\n\\usepackage{subcaption}\n\n\\title{Exception Events Are All You Need:\\\\Fault Indicator Isolation as the Robust Mechanism\\\\for Execution Trace Verdict Prediction}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\n% ============================================================\n\nExecution traces have been used to improve code understanding through supervised fine-tuning (SFT), but prior work finds inconsistent, model-dependent benefits on generative tasks. We study a different question: what is the minimal sufficient trace signal for \\emph{verdict prediction}, the binary classification of whether code passes or fails a test? Through systematic ablation across four architecturally distinct models (Qwen-2.5-Coder-7B, Qwen-2.5-Coder-1.5B, DeepSeek-Coder-6.7B, CodeLlama-13B-Instruct), we find that \\textbf{exception events} (compact, structured error summaries) are the only universally robust trace component, achieving 99.83\\% accuracy on Qwen-7B ($\\pm$0.00 across 3 seeds) and consistently outperforming all alternatives on every model. All other trace components and budget-length relationships are model-dependent: four models produce four distinct budget curves with no shared phase transition pattern. SFT with exception-only traces achieves 99.83\\% accuracy at \\$0.03 per 1{,}190 samples with near-perfect calibration (ECE\\,=\\,0.0027), compared to GPT-4o few-shot prompting at 97.2\\% accuracy and \\$15 per batch. The design principle is simple: for verdict tasks, extract the highest-specificity diagnostic signal and discard everything else.\n\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n% ============================================================\n\nExecution traces record the runtime behavior of programs and contain rich information about control flow, variable states, and error conditions. Recent work has explored using traces to improve code language models through supervised fine-tuning. DCSH~\\cite{dcsh2025} tested five trace formats on generative tasks and found that ``no single trace representation consistently outperforms others.'' TracePile~\\cite{tracepile2025} scaled trace SFT to 2.6 million samples but evaluated only generation tasks. TRACED~\\cite{traced2024} demonstrated that traces help encoder-based classification. Despite this growing body of work, two fundamental questions remain unanswered: (1) do traces help \\emph{verdict prediction} (binary pass/fail classification), and (2) what specific trace components drive classification performance?\n\nThese questions matter for practical software engineering. Verdict prediction is a core subroutine in automated testing, program repair, and code evaluation pipelines. If traces help, knowing \\emph{which} trace component matters determines the cost and complexity of the required instrumentation. A system that needs only exception events is radically simpler than one that requires full execution traces with loop unrolling and variable tracking.\n\nWe approach verdict prediction as \\textbf{fault detection} rather than execution simulation. This reframing suggests that the most useful trace signal may not be the richest representation but the one with the highest specificity for faults. We test this hypothesis through systematic component ablation of VOTA (Verdict-Optimized Trace Abstraction), a trace compression pipeline that isolates three component types: exception summaries, assertion-point information, and loop compression patterns.\n\nOur experiments across four models reveal a clear finding: exception events are the only universally robust trace component. On Qwen-7B, exception-only SFT achieves 99.83\\% accuracy with zero variance across three random seeds, and the two remaining errors are provably irreducible (caused by Python's \\texttt{GeneratorExit} mechanism). On all four models, exception-only traces outperform every alternative representation. In contrast, all other findings are model-dependent. Budget curves (accuracy as a function of trace length) show four distinct patterns across four models: gradual monotonic (Qwen-7B), sharp delayed transition (Qwen-1.5B), early onset with tail regression (DeepSeek), and non-monotonic W-shape (CodeLlama). No universal phase transition exists.\n\nWe also compare against frontier model baselines. GPT-4o with 3-shot prompting reaches 97.2\\% accuracy on exception traces, close to but significantly below SFT (99.83\\%, $p$\\,=\\,0.001). SFT's practical advantages are cost (300$\\times$ cheaper), calibration (ECE\\,=\\,0.0027 vs.\\ no logit access), and offline deployment without API dependency.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,nosep]\n    \\item We establish that exception events are the most effective and only universally robust trace component for verdict prediction, achieving near-perfect accuracy across four models while all other components show model-dependent behavior.\n    \\item We quantify the information density bottleneck: label-only loss ablation shows gradient dilution accounts for only 26\\% of the full-trace-to-VOTA gap, while information overload accounts for 74\\%.\n    \\item We reveal a two-tier diagnostic hierarchy where Tier~1 signals (exceptions, assertion-points) are individually near-perfect and sufficient, while Tier~2 signals (loop patterns) are model-dependent and introduce noise when combined with Tier~1.\n\\end{enumerate}\n\n% ============================================================\n\\section{Related Work}\n\\label{sec:related}\n% ============================================================\n\n\\paragraph{Trace-augmented code models.}\nDCSH~\\cite{dcsh2025} introduced five trace representation formats for SFT and found that no format consistently outperforms others on generative tasks, with effectiveness varying across models and tasks. TracePile~\\cite{tracepile2025} scaled trace SFT to 2.6M samples and observed benefits for code generation, but did not study classification tasks. TRACED~\\cite{traced2024} used traces for encoder-based test verdict classification and showed improvements over code-only baselines, but did not perform component-level ablation to identify which trace elements are responsible. Our work differs in two ways: we focus on decoder-based SFT for binary verdict prediction, and we perform fine-grained ablation to isolate the active ingredient.\n\n\\paragraph{Code execution prediction.}\nCRUXEval~\\cite{cruxeval2024} introduced benchmarks for predicting execution outputs and inputs, measuring a model's ability to simulate program execution. This execution reasoning capability correlates with trace utilization effectiveness in our cross-model analysis. CodeExecutor~\\cite{codeexecutor2024} trained models to generate execution traces. Our work is complementary: rather than training models to produce traces, we study which trace components are most useful when consumed as input for classification.\n\n\\paragraph{LLM-based test verdict prediction.}\nPrior approaches to automated verdict prediction include rule-based systems using test output parsing and neural approaches using code embeddings. Recent work has explored using large language models for code correctness assessment, typically through prompting. Our few-shot baseline experiments with GPT-4o and Claude situate SFT-based approaches within this landscape.\n\n% ============================================================\n\\section{Method}\n\\label{sec:method}\n% ============================================================\n\n\\subsection{Task Definition}\n\nGiven a programming problem $p$, a candidate solution $s$, a test suite $T$, and optionally an execution trace $\\tau$ produced by running $s$ on $T$, the verdict prediction task is to predict a binary label $y \\in \\{\\texttt{pass}, \\texttt{fail}\\}$ indicating whether $s$ passes all tests in $T$.\n\n\\subsection{Dataset}\n\nWe construct our dataset from HumanEval (164 problems) and MBPP-sanitized (427 problems), totaling 591 unique programming problems. For each problem, we collect 10 LLM-generated candidate solutions, producing 5{,}910 samples. The pass/fail ratio is 71.5\\%/28.5\\%. We split into 4{,}720 training and 1{,}190 test samples with zero train-test input overlap. Execution traces are collected by instrumenting Python's tracing mechanism to record function calls, variable assignments, loop iterations, exceptions, and assertion results.\n\n\\subsection{Trace Representations}\n\nWe compare five trace conditions:\n\n\\paragraph{No-trace baseline.} The model receives only the problem description $p$ and candidate solution $s$, with no execution information.\n\n\\paragraph{Full trace.} The model receives the complete execution trace $\\tau$, including all loop iterations, variable states, function calls, and exceptions. Traces are tail-truncated to fit the model's context window.\n\n\\paragraph{VOTA (Verdict-Optimized Trace Abstraction).} A three-component compression of full traces:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{Loop compression}: Repeated loop iterations are collapsed into a summary showing the first iteration, pattern statistics, and the last iteration.\n    \\item \\textbf{Exception summary}: Exception events are extracted and formatted as structured records: \\texttt{[ERROR] type: ... message: ...} or \\texttt{[No exception]}.\n    \\item \\textbf{Assertion-point information}: Actual vs.\\ expected value comparisons at test assertion points.\n\\end{itemize}\n\n\\paragraph{Exception-only.} Only the exception summary component of VOTA, discarding loop and assertion-point information.\n\n\\paragraph{Component ablations.} We additionally test assertion-point-only (\\texttt{ae\\_only}), loop-only (\\texttt{loop\\_only}), and VOTA without assertion-points (\\texttt{no\\_ae}).\n\n\\subsection{Training Setup}\n\nAll models are fine-tuned using LoRA (rank 16, $\\alpha$\\,=\\,32) with the SFT objective. Training runs for 3 epochs with a learning rate of 2e-4 and batch size 8. We evaluate on four models: Qwen-2.5-Coder-7B, Qwen-2.5-Coder-1.5B, DeepSeek-Coder-6.7B, and CodeLlama-13B-Instruct. For robustness evaluation, we train with three random seeds (42, 123, 456) where compute permits.\n\n% ============================================================\n\\section{Experiments}\n\\label{sec:experiments}\n% ============================================================\n\n\\subsection{Exception Events Dominate All Trace Components}\n\\label{sec:exp-main}\n\nTable~\\ref{tab:main-results} presents the main comparison across trace conditions on Qwen-7B. Exception-only traces achieve 99.83\\% accuracy (2 errors out of 1{,}190 test samples), outperforming full VOTA (99.41\\%), full traces (81.76\\%), and the no-trace baseline (75.13\\%). The exception-only condition exceeds VOTA despite containing strictly less information ($p$\\,=\\,0.01), indicating that non-exception components introduce noise rather than useful signal.\n\n\\begin{table}[t]\n\\centering\n\\caption{Verdict prediction accuracy across trace conditions (Qwen-2.5-Coder-7B, seed 42). Exception-only achieves the highest accuracy despite being the simplest representation.}\n\\label{tab:main-results}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Accuracy} & \\textbf{Pass F1} & \\textbf{Fail F1} & \\textbf{ECE} \\\\\n\\midrule\nexception\\_only & \\textbf{99.83\\%} & \\textbf{0.999} & \\textbf{0.997} & \\textbf{0.0027} \\\\\nae\\_only & 99.92\\% & 0.999 & 0.999 & 0.0004 \\\\\nVOTA (full) & 99.41\\% & 0.996 & 0.989 & 0.0054 \\\\\nno\\_ae & 99.41\\% & 0.996 & 0.989 & 0.0054 \\\\\nloop\\_only & 85.63\\% & --- & --- & 0.0831 \\\\\nlabel\\_only & 86.22\\% & --- & --- & 0.1107 \\\\\nfull\\_trace & 81.76\\% & --- & --- & 0.0958 \\\\\nno\\_trace & 75.13\\% & --- & --- & 0.1715 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nComponent ablation reveals a strict two-tier diagnostic hierarchy. \\textbf{Tier~1} consists of exception summaries (99.83\\%) and assertion-point information (99.92\\%), which are individually near-perfect and statistically equivalent ($p$\\,=\\,0.80). \\textbf{Tier~2} consists of loop compression patterns (85.63\\%), which carry substantial signal above baseline but are fully subsumed by Tier~1. Removing assertion-point information from VOTA does not change accuracy (99.41\\% with and without), confirming that the exception component is VOTA's active ingredient.\n\n\\paragraph{Irreducible error analysis.}\nThe 2 errors made by exception-only (sample ids 901 and 905) are identical across all 3 random seeds. Both come from HumanEval/95 (\\texttt{check\\_dict\\_case}), where Python's \\texttt{all()} short-circuits a generator expression, triggering \\texttt{GeneratorExit} (a \\texttt{BaseException} subclass used for control flow, not a real error). The tracer marks this as \\texttt{[ERROR]}, so the model sees 7 lines of \\texttt{[ERROR] GeneratorExit} and reasonably predicts fail. With only 2 such samples in the entire dataset, the model has no training signal to learn the benign nature of \\texttt{GeneratorExit}. This confirms 99.83\\% is the theoretical ceiling for exception-only representation on this dataset.\n\n\\subsection{Information Density Drives Trace Compression Benefit}\n\\label{sec:exp-density}\n\nFull traces improve over the no-trace baseline (+6.6pp), but VOTA achieves a much larger gain (+24.3pp). What accounts for VOTA's advantage? We decompose the gap using a label-only loss ablation: training on full traces but masking loss to the verdict label token only, eliminating gradient dilution from non-label tokens. This label-only variant achieves 86.22\\%, a +4.5pp improvement over standard full-trace training (81.76\\%). The decomposition yields:\n\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item Gradient dilution accounts for 26\\% of the full-trace-to-VOTA gap (4.5pp out of 17.6pp).\n    \\item Information overload accounts for 74\\% (13.0pp), resolvable only through trace compression.\n\\end{itemize}\n\nEven with oracle loss masking that completely eliminates gradient dilution, full traces still underperform VOTA by 13pp. The bottleneck is information density, not training signal distribution.\n\n\\subsection{Cross-Model Calibration}\n\\label{sec:exp-calibration}\n\nTable~\\ref{tab:calibration} reports calibration metrics for exception-only SFT across all four models. While accuracy is consistently high (99.33--99.83\\%), calibration quality varies. Qwen models achieve near-perfect calibration (ECE $\\leq$ 0.0041), while DeepSeek shows moderate miscalibration (ECE\\,=\\,0.0523) despite high accuracy. All models show substantial calibration improvement over no-trace baselines: the exception-to-no-trace ECE ratio ranges from 3.4$\\times$ (DeepSeek) to 63$\\times$ (Qwen-7B).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model calibration for exception-only SFT. Accuracy is universally high, but calibration quality is model-dependent. All models improve over no-trace baselines.}\n\\label{tab:calibration}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Accuracy} & \\textbf{ECE} & \\textbf{Brier} & \\textbf{ECE ratio vs.\\ no-trace} \\\\\n\\midrule\nQwen-7B & 99.83\\% & 0.0027 & 0.0013 & 63$\\times$ \\\\\nQwen-1.5B & 99.83\\% & 0.0041 & 0.0019 & $\\sim$51$\\times$ \\\\\nDeepSeek-6.7B & 99.33\\% & 0.0523 & 0.0318 & $\\sim$3.4$\\times$ \\\\\nCodeLlama-13B & 99.83\\% & 0.0183 & 0.0072 & $\\sim$9.3$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe calibration data reinforces exception dominance from an independent evidence dimension. Exception-only models not only predict correctly but ``know they are correct'': Qwen-7B's Brier score of 0.0013 is 150$\\times$ lower than the no-trace Brier of 0.1972. The model-dependent calibration magnitudes (DeepSeek ECE is 19$\\times$ higher than Qwen) prevent us from claiming universal near-perfect calibration, but the direction of improvement is consistent.\n\n\\subsection{Few-Shot Frontier Model Baselines}\n\\label{sec:exp-fewshot}\n\nTable~\\ref{tab:fewshot} compares SFT against zero-shot and few-shot prompting with GPT-4o and Claude Sonnet. GPT-4o with 3-shot exception-only prompting achieves 97.2\\% accuracy, 2.63pp below SFT (99.83\\%). This gap is statistically significant ($n$\\,=\\,1{,}190, $p$\\,=\\,0.001) but small in absolute terms.\n\n\\begin{table}[t]\n\\centering\n\\caption{SFT vs.\\ frontier model baselines. SFT achieves the highest accuracy at $\\sim$300$\\times$ lower cost. Frontier models lack logit access for calibration. Exception-only input consistently produces the largest accuracy gain across all methods.}\n\\label{tab:fewshot}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Accuracy} & \\textbf{Cost/1190} & \\textbf{Latency} & \\textbf{ECE} \\\\\n\\midrule\nSFT exc.\\ (Qwen-7B) & \\textbf{99.83\\%} & \\$0.03 & $\\sim$50ms & 0.0027 \\\\\nGPT-4o 3-shot + exc. & 97.2\\% & $\\sim$\\$15 & $\\sim$2s & N/A \\\\\nClaude 3-shot + exc. & 96.5\\% & $\\sim$\\$10 & $\\sim$1.8s & N/A \\\\\nGPT-4o 0-shot + exc. & 95.5\\% & $\\sim$\\$12 & $\\sim$2s & N/A \\\\\nGPT-4o 0-shot no-trace & 82.3\\% & $\\sim$\\$8 & $\\sim$1.5s & N/A \\\\\nSFT no-trace (Qwen-7B) & 75.1\\% & \\$0.02 & $\\sim$30ms & 0.1715 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThree factors justify the SFT approach despite the narrow accuracy gap. First, \\textbf{cost}: SFT inference costs approximately \\$0.03 per 1{,}190 samples versus \\$15 for GPT-4o, a $\\sim$300$\\times$ difference at scale. Second, \\textbf{calibration}: SFT provides logit-level confidence scores (ECE\\,=\\,0.0027) while API-based models do not expose logits, precluding probability calibration. Third, \\textbf{deployment}: SFT models can run offline without API dependency.\n\nThe few-shot results also reinforce the exception dominance finding from a different angle. GPT-4o gains +13.2pp from exception traces (82.3\\% $\\to$ 95.5\\% zero-shot), confirming that the exception signal is valuable regardless of whether the consumer is an SFT model or a prompted frontier model.\n\n\\subsection{Budget Curve Analysis: Model-Dependent Patterns}\n\\label{sec:exp-budget}\n\nTable~\\ref{tab:budget} presents the full budget curve matrix across four models. Each model exhibits a qualitatively different accuracy-vs-length pattern, and no universal phase transition exists.\n\n\\begin{table}[t]\n\\centering\n\\caption{Full trace budget curves across four models. Each model shows a distinct pattern. Only Qwen-7B is monotonically increasing. Accuracy is reported for seed 42.}\n\\label{tab:budget}\n\\small\n\\begin{tabular}{lcccccl}\n\\toprule\n\\textbf{Model} & \\textbf{t-256} & \\textbf{t-384} & \\textbf{t-512} & \\textbf{t-1024} & \\textbf{t-2048} & \\textbf{Pattern} \\\\\n\\midrule\nQwen-7B & 77.5 & 84.7 & 93.6 & 96.5 & 97.3 & gradual S-curve \\\\\nQwen-1.5B & 72.6 & 74.5 & 95.6 & 96.6 & 97.9 & step at 512 \\\\\nDeepSeek & 76.4 & 88.3 & 93.9 & 96.5 & 95.0 & early + tail regr. \\\\\nCodeLlama & 77.9 & 73.5 & 97.5 & 98.2 & 41.8 & W-shape \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Qwen-7B} is the only model with a clean monotonic budget curve, showing gradual improvement from 77.5\\% (tail-256) to 97.3\\% (tail-2048) with consistent gains at each step. \\textbf{Qwen-1.5B} displays a sharp step function: tail-384 provides almost no improvement over tail-256 (+1.9pp), then tail-512 jumps by +21.1pp, suggesting a critical information threshold between 384 and 512 tokens. \\textbf{DeepSeek} shows early-onset improvement (tail-384 already at 88.3\\%, +11.9pp over tail-256) but exhibits a slight regression at tail-2048 (95.0\\% vs.\\ 96.5\\% at tail-1024), indicating that longer context introduces noise. \\textbf{CodeLlama} produces a non-monotonic W-shape: tail-384 is \\emph{worse} than tail-256 ($-$4.4pp), tail-512 jumps to 97.5\\%, and tail-2048 collapses to 41.8\\% ($-$56.4pp).\n\nThe cross-model standard deviation at tail-384 is 6.4pp with a range of 14.8pp (73.5\\% to 88.3\\%). These divergent patterns confirm that the relationship between trace length and verdict accuracy is entirely model-specific. Exception-only traces, by contrast, achieve 99.83\\% on all four models regardless of length budget, because the exception signal is compact enough to never require truncation.\n\n\\subsection{Seed Robustness of Budget Curves}\n\\label{sec:exp-seed-budget}\n\nTable~\\ref{tab:seed-budget} reports tail-512 accuracy across three seeds for each model, assessing whether the single-seed budget curves are reliable. Only Qwen-7B shows robust seed consistency ($\\sigma$\\,=\\,0.6pp). CodeLlama's $\\sigma$\\,=\\,8.7pp (range: 80.9\\%--97.5\\%) makes its single-seed data unreliable.\n\n\\begin{table}[t]\n\\centering\n\\caption{Seed robustness at tail-512 across four models. Exception-only seed variance is shown for comparison. Full-trace seed sensitivity scales with signal complexity.}\n\\label{tab:seed-budget}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Model} & \\textbf{s42} & \\textbf{s123} & \\textbf{s456} & \\textbf{Mean} & \\textbf{$\\sigma$} & \\textbf{Exc.\\ $\\sigma$} \\\\\n\\midrule\nQwen-7B & 93.6 & 92.4 & 93.1 & 93.0 & 0.6pp & 0.00pp \\\\\nQwen-1.5B & 95.6 & 90.8 & 94.2 & 93.5 & 2.5pp & --- \\\\\nDeepSeek & 93.9 & 87.6 & 91.9 & 91.1 & 3.2pp & 4.8pp \\\\\nCodeLlama & 97.5 & 80.9 & 94.3 & 90.9 & 8.7pp & 0.1pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe contrast between exception-only and full-trace seed variance is stark. CodeLlama's exception-only $\\sigma$ is 0.1pp while its tail-512 $\\sigma$ is 8.7pp, an 87$\\times$ ratio. This provides additional evidence for the ``simplicity enables robustness'' principle: the structurally simplest signal produces the most stable training outcomes.\n\n\\subsection{Error Analysis}\n\\label{sec:exp-errors}\n\nTable~\\ref{tab:errors} breaks down prediction errors by trace condition. The error profiles are qualitatively different across conditions, confirming that different representations fail on orthogonal dimensions.\n\n\\begin{table}[t]\n\\centering\n\\caption{Error category distribution across trace conditions (Qwen-7B). Exception-only errors are irreducible; full-trace errors are dominated by information overload.}\n\\label{tab:errors}\n\\small\n\\begin{tabular}{lcll}\n\\toprule\n\\textbf{Condition} & \\textbf{Errors} & \\textbf{Primary category} & \\textbf{Actionable?} \\\\\n\\midrule\nexception\\_only & 2 & GeneratorExit (100\\%) & No (irreducible) \\\\\nVOTA & 7 & Mixed: GenExit/attn.\\ dilution/ambiguous & Partial \\\\\nfull\\_trace & 217 & Long-trace overload (65\\%) & No\\tablefootnote{Would require architectural changes beyond LoRA SFT.} \\\\\nno\\_trace & 296 & Subtle bugs from code alone (37\\%) & No (inherent) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nException-only's 2 errors are \\texttt{GeneratorExit} false negatives, fully characterized in Section~\\ref{sec:exp-main}. VOTA's 7 errors split into three categories: 2 inherited \\texttt{GeneratorExit} cases, 3 caused by loop/ae tokens diluting attention on the exception signal, and 2 from ambiguous conflicting signals (normal loops but abnormal exceptions). Full-trace's 217 errors are dominated by long-program information overload (142/217, 65\\%), where traces are too long for effective processing. Error samples have a median trace length 2.3$\\times$ longer than correctly classified samples. The cross-condition error overlap is low (exception $\\cap$ no-trace overlap: 0.7\\%), confirming orthogonal failure modes.\n\n\\subsection{Training Dynamics}\n\\label{sec:exp-dynamics}\n\nTable~\\ref{tab:dynamics} compares learning curves for exception-only, full-trace, and no-trace conditions. Exception-only converges in approximately 100 training steps, reaching 99.1\\% accuracy. Full-trace converges more slowly (200 steps) to a much lower ceiling (81.8\\%). At step 50, exception-only (96.2\\%) already surpasses the full-trace converged accuracy, meaning exception-only reaches a higher ceiling in one-sixth of the training time. Step-to-step variance for exception-only ($\\sigma$\\,=\\,0.003) is 6$\\times$ lower than full-trace ($\\sigma$\\,=\\,0.018), reflecting the smoother optimization landscape of the simpler signal.\n\n\\begin{table}[t]\n\\centering\n\\caption{Learning curve milestones (Qwen-7B). Exception-only at step 50 already surpasses full-trace's converged accuracy.}\n\\label{tab:dynamics}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Step 50} & \\textbf{Step 100} & \\textbf{Step 200} & \\textbf{Final} & \\textbf{Conv.} & \\textbf{Step $\\sigma$} \\\\\n\\midrule\nexception\\_only & 96.2\\% & 99.1\\% & 99.8\\% & 99.83\\% & 100 & 0.003 \\\\\nfull\\_trace & 72.1\\% & 76.8\\% & 81.2\\% & 81.8\\% & 200 & 0.018 \\\\\nno\\_trace & 71.5\\% & 73.8\\% & 75.0\\% & 75.1\\% & 150 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Out-of-Distribution Generalization}\n\\label{sec:exp-ood}\n\nTable~\\ref{tab:ood} evaluates generalization to LeetCode-style problems drawn from a different distribution than the HumanEval/MBPP training data. Exception-only accuracy drops from 99.83\\% to 87.1\\% ($-$12.7pp), indicating partial overfitting to the training distribution's exception patterns (dominated by \\texttt{TypeError}, \\texttt{ValueError}, \\texttt{AssertionError}). The relative ordering is preserved: exception-only (87.1\\%) outperforms VOTA (79.3\\%) and no-trace (68.2\\%) on OOD data, confirming that exception dominance generalizes even when absolute numbers decline.\n\n\\begin{table}[t]\n\\centering\n\\caption{Out-of-distribution generalization (Qwen-7B). Relative ordering is preserved, but absolute accuracy drops, especially for exception-only ($-$12.7pp).}\n\\label{tab:ood}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Condition} & \\textbf{In-dist.} & \\textbf{OOD (Python)} & \\textbf{$\\Delta$} \\\\\n\\midrule\nexception\\_only & 99.83\\% & 87.1\\% & $-$12.7pp \\\\\nVOTA & 99.41\\% & 79.3\\% & $-$20.1pp \\\\\nno\\_trace & 75.13\\% & 68.2\\% & $-$6.9pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCross-language evaluation (Java, JavaScript, C++) was not feasible within the experimental timeline due to the need for language-specific trace collection infrastructure and exception format normalization. We note this as a limitation.\n\n% ============================================================\n\\section{Discussion}\n\\label{sec:discussion}\n% ============================================================\n\n\\paragraph{Why simplicity is robustness.}\nThe central finding of this work is that the structurally simplest trace component is also the most robust. Exception events are short, structured, and encode a single semantic dimension: fault presence or absence. This simplicity provides robustness along every axis we measured: cross-model accuracy (99.33--99.83\\% on 4 models), seed stability (0.00pp $\\sigma$ on Qwen-7B, 0.1pp on CodeLlama), calibration (ECE as low as 0.0027), and training speed (converges in 100 steps). Every additional trace component introduces model-dependent behavior. Budget curves are the clearest example: four models produce four qualitatively different patterns, with CodeLlama exhibiting catastrophic collapse at tail-2048 (41.8\\%). Exception-only traces are immune to length budget effects because they never approach context limits.\n\n\\paragraph{VOTA as fault indicator isolation.}\nVOTA's value lies not in generic trace compression but in automatically isolating exception events from noisy full traces. Removing assertion-point information from VOTA does not change accuracy (99.41\\% $\\to$ 99.41\\%), and exception-only (99.83\\%) exceeds full VOTA. The ``compression helps'' narrative was a stepping stone; the real mechanism is diagnostic signal extraction.\n\n\\paragraph{Model-dependent calibration.}\nWhile all models show calibration improvement from exception traces, the magnitude varies by 19$\\times$ across models (Qwen-7B ECE 0.0027 vs.\\ DeepSeek 0.0523). DeepSeek's poor calibration despite high accuracy (99.33\\%) parallels a broader pattern we observe: token-level training loss and sample-level classification quality can diverge. In DeepSeek's case, two seeds with nearly identical training loss (0.1225 vs.\\ 0.122) produce accuracy differences of 8.2pp (99.33\\% vs.\\ 91.09\\%), with the gap concentrated in fail recall (1.0 vs.\\ 0.705). This suggests that verdict tasks should use task-specific metrics for checkpoint selection, not standard evaluation loss.\n\n\\paragraph{Limitations.}\nOur dataset covers only Python and two benchmarks (HumanEval + MBPP-sanitized). OOD generalization shows 12.7pp degradation on LeetCode-style problems, and cross-language evaluation was not feasible. The study uses only four models from two architecture families. Exception-only's near-perfect accuracy on in-distribution data partially depends on the distribution of exception types in HumanEval/MBPP. Seed sensitivity on DeepSeek (one outlier seed at 91.09\\%) suggests that models with less stable LoRA training landscapes may require multi-seed selection or training stabilization techniques.\n\n% ============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n% ============================================================\n\nWe studied what trace components matter for verdict prediction across four code language models. The answer is simple: exception events are the only universally robust signal. They achieve near-perfect accuracy on every model tested, with provably irreducible residual errors. All other trace components and length-accuracy relationships are model-dependent. For practitioners building verdict prediction systems, the implication is direct: instrument for exceptions, discard everything else.\n\n% ============================================================\n% References\n% ============================================================\n\\bibliographystyle{plain}\n\\begin{thebibliography}{10}\n\n\\bibitem{dcsh2025}\nDCSH Authors.\n\\newblock Execution Traces for Code Generation: A Systematic Comparison.\n\\newblock In \\emph{EMNLP Findings}, 2025.\n\n\\bibitem{tracepile2025}\nTracePile Authors.\n\\newblock TracePile: Scaling Trace-Augmented Code Training.\n\\newblock In \\emph{NeurIPS}, 2025.\n\n\\bibitem{traced2024}\nTRACED Authors.\n\\newblock TRACED: Execution-aware Pre-training for Source Code.\n\\newblock In \\emph{ICSE}, 2024.\n\n\\bibitem{cruxeval2024}\nA.~Gu, B.~Rozière, H.~Leather, A.~Solar-Lezama, G.~Synnaeve, S.~I.~Wang.\n\\newblock CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem{codeexecutor2024}\nCodeExecutor Authors.\n\\newblock CodeExecutor: Learning to Execute Code with Language Models.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0119528d-6ec5-4ec0-a007-fadcf2a1759f",
  "isSidechain": false,
  "requestId": "req_011CbA93jYMkC3sUmhDh3Dpi",
  "type": "assistant",
  "uuid": "8a45f9a6-8418-4d20-b04e-679b66e2c375",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "175abc6b-2146-427e-acfe-4e3e17983955",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018LW28UiYePFoqjNs9CGvej",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 155,
      "cache_read_input_tokens": 56238,
      "output_tokens": 10002,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 155,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10002,
          "cache_read_input_tokens": 56238,
          "cache_creation_input_tokens": 155,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 155
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

_source line 25 · 2026-05-18T13:51:55.297Z_

<details><summary>↩ Tool result · `toolu_01HUHLbqjV4NxkKCcXEJf8X1`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a45f9a6-8418-4d20-b04e-679b66e2c375",
  "isSidechain": false,
  "promptId": "cde04d7b-c03d-49ea-b3f7-a9fea2ed96f5",
  "type": "user",
  "uuid": "2bb50a0b-1790-45ad-a7ba-3a40699e5638",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/worst/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage{xcolor}\n\\usepackage{multirow}\n\\usepackage{tablefootnote}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{enumitem}\n\\usepackage{subcaption}\n\n\\title{Exception Events Are All You Need:\\\\Fault Indicator Isolation as the Robust Mechanism\\\\for Execution Trace Verdict Prediction}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\n% ============================================================\n\nExecution traces have been used to improve code understanding through supervised fine-tuning (SFT), but prior work finds inconsistent, model-dependent benefits on generative tasks. We study a different question: what is the minimal sufficient trace signal for \\emph{verdict prediction}, the binary classification of whether code passes or fails a test? Through systematic ablation across four architecturally distinct models (Qwen-2.5-Coder-7B, Qwen-2.5-Coder-1.5B, DeepSeek-Coder-6.7B, CodeLlama-13B-Instruct), we find that \\textbf{exception events} (compact, structured error summaries) are the only universally robust trace component, achieving 99.83\\% accuracy on Qwen-7B ($\\pm$0.00 across 3 seeds) and consistently outperforming all alternatives on every model. All other trace components and budget-length relationships are model-dependent: four models produce four distinct budget curves with no shared phase transition pattern. SFT with exception-only traces achieves 99.83\\% accuracy at \\$0.03 per 1{,}190 samples with near-perfect calibration (ECE\\,=\\,0.0027), compared to GPT-4o few-shot prompting at 97.2\\% accuracy and \\$15 per batch. The design principle is simple: for verdict tasks, extract the highest-specificity diagnostic signal and discard everything else.\n\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n% ============================================================\n\nExecution traces record the runtime behavior of programs and contain rich information about control flow, variable states, and error conditions. Recent work has explored using traces to improve code language models through supervised fine-tuning. DCSH~\\cite{dcsh2025} tested five trace formats on generative tasks and found that ``no single trace representation consistently outperforms others.'' TracePile~\\cite{tracepile2025} scaled trace SFT to 2.6 million samples but evaluated only generation tasks. TRACED~\\cite{traced2024} demonstrated that traces help encoder-based classification. Despite this growing body of work, two fundamental questions remain unanswered: (1) do traces help \\emph{verdict prediction} (binary pass/fail classification), and (2) what specific trace components drive classification performance?\n\nThese questions matter for practical software engineering. Verdict prediction is a core subroutine in automated testing, program repair, and code evaluation pipelines. If traces help, knowing \\emph{which} trace component matters determines the cost and complexity of the required instrumentation. A system that needs only exception events is radically simpler than one that requires full execution traces with loop unrolling and variable tracking.\n\nWe approach verdict prediction as \\textbf{fault detection} rather than execution simulation. This reframing suggests that the most useful trace signal may not be the richest representation but the one with the highest specificity for faults. We test this hypothesis through systematic component ablation of VOTA (Verdict-Optimized Trace Abstraction), a trace compression pipeline that isolates three component types: exception summaries, assertion-point information, and loop compression patterns.\n\nOur experiments across four models reveal a clear finding: exception events are the only universally robust trace component. On Qwen-7B, exception-only SFT achieves 99.83\\% accuracy with zero variance across three random seeds, and the two remaining errors are provably irreducible (caused by Python's \\texttt{GeneratorExit} mechanism). On all four models, exception-only traces outperform every alternative representation. In contrast, all other findings are model-dependent. Budget curves (accuracy as a function of trace length) show four distinct patterns across four models: gradual monotonic (Qwen-7B), sharp delayed transition (Qwen-1.5B), early onset with tail regression (DeepSeek), and non-monotonic W-shape (CodeLlama). No universal phase transition exists.\n\nWe also compare against frontier model baselines. GPT-4o with 3-shot prompting reaches 97.2\\% accuracy on exception traces, close to but significantly below SFT (99.83\\%, $p$\\,=\\,0.001). SFT's practical advantages are cost (300$\\times$ cheaper), calibration (ECE\\,=\\,0.0027 vs.\\ no logit access), and offline deployment without API dependency.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,nosep]\n    \\item We establish that exception events are the most effective and only universally robust trace component for verdict prediction, achieving near-perfect accuracy across four models while all other components show model-dependent behavior.\n    \\item We quantify the information density bottleneck: label-only loss ablation shows gradient dilution accounts for only 26\\% of the full-trace-to-VOTA gap, while information overload accounts for 74\\%.\n    \\item We reveal a two-tier diagnostic hierarchy where Tier~1 signals (exceptions, assertion-points) are individually near-perfect and sufficient, while Tier~2 signals (loop patterns) are model-dependent and introduce noise when combined with Tier~1.\n\\end{enumerate}\n\n% ============================================================\n\\section{Related Work}\n\\label{sec:related}\n% ============================================================\n\n\\paragraph{Trace-augmented code models.}\nDCSH~\\cite{dcsh2025} introduced five trace representation formats for SFT and found that no format consistently outperforms others on generative tasks, with effectiveness varying across models and tasks. TracePile~\\cite{tracepile2025} scaled trace SFT to 2.6M samples and observed benefits for code generation, but did not study classification tasks. TRACED~\\cite{traced2024} used traces for encoder-based test verdict classification and showed improvements over code-only baselines, but did not perform component-level ablation to identify which trace elements are responsible. Our work differs in two ways: we focus on decoder-based SFT for binary verdict prediction, and we perform fine-grained ablation to isolate the active ingredient.\n\n\\paragraph{Code execution prediction.}\nCRUXEval~\\cite{cruxeval2024} introduced benchmarks for predicting execution outputs and inputs, measuring a model's ability to simulate program execution. This execution reasoning capability correlates with trace utilization effectiveness in our cross-model analysis. CodeExecutor~\\cite{codeexecutor2024} trained models to generate execution traces. Our work is complementary: rather than training models to produce traces, we study which trace components are most useful when consumed as input for classification.\n\n\\paragraph{LLM-based test verdict prediction.}\nPrior approaches to automated verdict prediction include rule-based systems using test output parsing and neural approaches using code embeddings. Recent work has explored using large language models for code correctness assessment, typically through prompting. Our few-shot baseline experiments with GPT-4o and Claude situate SFT-based approaches within this landscape.\n\n% ============================================================\n\\section{Method}\n\\label{sec:method}\n% ============================================================\n\n\\subsection{Task Definition}\n\nGiven a programming problem $p$, a candidate solution $s$, a test suite $T$, and optionally an execution trace $\\tau$ produced by running $s$ on $T$, the verdict prediction task is to predict a binary label $y \\in \\{\\texttt{pass}, \\texttt{fail}\\}$ indicating whether $s$ passes all tests in $T$.\n\n\\subsection{Dataset}\n\nWe construct our dataset from HumanEval (164 problems) and MBPP-sanitized (427 problems), totaling 591 unique programming problems. For each problem, we collect 10 LLM-generated candidate solutions, producing 5{,}910 samples. The pass/fail ratio is 71.5\\%/28.5\\%. We split into 4{,}720 training and 1{,}190 test samples with zero train-test input overlap. Execution traces are collected by instrumenting Python's tracing mechanism to record function calls, variable assignments, loop iterations, exceptions, and assertion results.\n\n\\subsection{Trace Representations}\n\nWe compare five trace conditions:\n\n\\paragraph{No-trace baseline.} The model receives only the problem description $p$ and candidate solution $s$, with no execution information.\n\n\\paragraph{Full trace.} The model receives the complete execution trace $\\tau$, including all loop iterations, variable states, function calls, and exceptions. Traces are tail-truncated to fit the model's context window.\n\n\\paragraph{VOTA (Verdict-Optimized Trace Abstraction).} A three-component compression of full traces:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{Loop compression}: Repeated loop iterations are collapsed into a summary showing the first iteration, pattern statistics, and the last iteration.\n    \\item \\textbf{Exception summary}: Exception events are extracted and formatted as structured records: \\texttt{[ERROR] type: ... message: ...} or \\texttt{[No exception]}.\n    \\item \\textbf{Assertion-point information}: Actual vs.\\ expected value comparisons at test assertion points.\n\\end{itemize}\n\n\\paragraph{Exception-only.} Only the exception summary component of VOTA, discarding loop and assertion-point information.\n\n\\paragraph{Component ablations.} We additionally test assertion-point-only (\\texttt{ae\\_only}), loop-only (\\texttt{loop\\_only}), and VOTA without assertion-points (\\texttt{no\\_ae}).\n\n\\subsection{Training Setup}\n\nAll models are fine-tuned using LoRA (rank 16, $\\alpha$\\,=\\,32) with the SFT objective. Training runs for 3 epochs with a learning rate of 2e-4 and batch size 8. We evaluate on four models: Qwen-2.5-Coder-7B, Qwen-2.5-Coder-1.5B, DeepSeek-Coder-6.7B, and CodeLlama-13B-Instruct. For robustness evaluation, we train with three random seeds (42, 123, 456) where compute permits.\n\n% ============================================================\n\\section{Experiments}\n\\label{sec:experiments}\n% ============================================================\n\n\\subsection{Exception Events Dominate All Trace Components}\n\\label{sec:exp-main}\n\nTable~\\ref{tab:main-results} presents the main comparison across trace conditions on Qwen-7B. Exception-only traces achieve 99.83\\% accuracy (2 errors out of 1{,}190 test samples), outperforming full VOTA (99.41\\%), full traces (81.76\\%), and the no-trace baseline (75.13\\%). The exception-only condition exceeds VOTA despite containing strictly less information ($p$\\,=\\,0.01), indicating that non-exception components introduce noise rather than useful signal.\n\n\\begin{table}[t]\n\\centering\n\\caption{Verdict prediction accuracy across trace conditions (Qwen-2.5-Coder-7B, seed 42). Exception-only achieves the highest accuracy despite being the simplest representation.}\n\\label{tab:main-results}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Accuracy} & \\textbf{Pass F1} & \\textbf{Fail F1} & \\textbf{ECE} \\\\\n\\midrule\nexception\\_only & \\textbf{99.83\\%} & \\textbf{0.999} & \\textbf{0.997} & \\textbf{0.0027} \\\\\nae\\_only & 99.92\\% & 0.999 & 0.999 & 0.0004 \\\\\nVOTA (full) & 99.41\\% & 0.996 & 0.989 & 0.0054 \\\\\nno\\_ae & 99.41\\% & 0.996 & 0.989 & 0.0054 \\\\\nloop\\_only & 85.63\\% & --- & --- & 0.0831 \\\\\nlabel\\_only & 86.22\\% & --- & --- & 0.1107 \\\\\nfull\\_trace & 81.76\\% & --- & --- & 0.0958 \\\\\nno\\_trace & 75.13\\% & --- & --- & 0.1715 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nComponent ablation reveals a strict two-tier diagnostic hierarchy. \\textbf{Tier~1} consists of exception summaries (99.83\\%) and assertion-point information (99.92\\%), which are individually near-perfect and statistically equivalent ($p$\\,=\\,0.80). \\textbf{Tier~2} consists of loop compression patterns (85.63\\%), which carry substantial signal above baseline but are fully subsumed by Tier~1. Removing assertion-point information from VOTA does not change accuracy (99.41\\% with and without), confirming that the exception component is VOTA's active ingredient.\n\n\\paragraph{Irreducible error analysis.}\nThe 2 errors made by exception-only (sample ids 901 and 905) are identical across all 3 random seeds. Both come from HumanEval/95 (\\texttt{check\\_dict\\_case}), where Python's \\texttt{all()} short-circuits a generator expression, triggering \\texttt{GeneratorExit} (a \\texttt{BaseException} subclass used for control flow, not a real error). The tracer marks this as \\texttt{[ERROR]}, so the model sees 7 lines of \\texttt{[ERROR] GeneratorExit} and reasonably predicts fail. With only 2 such samples in the entire dataset, the model has no training signal to learn the benign nature of \\texttt{GeneratorExit}. This confirms 99.83\\% is the theoretical ceiling for exception-only representation on this dataset.\n\n\\subsection{Information Density Drives Trace Compression Benefit}\n\\label{sec:exp-density}\n\nFull traces improve over the no-trace baseline (+6.6pp), but VOTA achieves a much larger gain (+24.3pp). What accounts for VOTA's advantage? We decompose the gap using a label-only loss ablation: training on full traces but masking loss to the verdict label token only, eliminating gradient dilution from non-label tokens. This label-only variant achieves 86.22\\%, a +4.5pp improvement over standard full-trace training (81.76\\%). The decomposition yields:\n\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item Gradient dilution accounts for 26\\% of the full-trace-to-VOTA gap (4.5pp out of 17.6pp).\n    \\item Information overload accounts for 74\\% (13.0pp), resolvable only through trace compression.\n\\end{itemize}\n\nEven with oracle loss masking that completely eliminates gradient dilution, full traces still underperform VOTA by 13pp. The bottleneck is information density, not training signal distribution.\n\n\\subsection{Cross-Model Calibration}\n\\label{sec:exp-calibration}\n\nTable~\\ref{tab:calibration} reports calibration metrics for exception-only SFT across all four models. While accuracy is consistently high (99.33--99.83\\%), calibration quality varies. Qwen models achieve near-perfect calibration (ECE $\\leq$ 0.0041), while DeepSeek shows moderate miscalibration (ECE\\,=\\,0.0523) despite high accuracy. All models show substantial calibration improvement over no-trace baselines: the exception-to-no-trace ECE ratio ranges from 3.4$\\times$ (DeepSeek) to 63$\\times$ (Qwen-7B).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model calibration for exception-only SFT. Accuracy is universally high, but calibration quality is model-dependent. All models improve over no-trace baselines.}\n\\label{tab:calibration}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Accuracy} & \\textbf{ECE} & \\textbf{Brier} & \\textbf{ECE ratio vs.\\ no-trace} \\\\\n\\midrule\nQwen-7B & 99.83\\% & 0.0027 & 0.0013 & 63$\\times$ \\\\\nQwen-1.5B & 99.83\\% & 0.0041 & 0.0019 & $\\sim$51$\\times$ \\\\\nDeepSeek-6.7B & 99.33\\% & 0.0523 & 0.0318 & $\\sim$3.4$\\times$ \\\\\nCodeLlama-13B & 99.83\\% & 0.0183 & 0.0072 & $\\sim$9.3$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe calibration data reinforces exception dominance from an independent evidence dimension. Exception-only models not only predict correctly but ``know they are correct'': Qwen-7B's Brier score of 0.0013 is 150$\\times$ lower than the no-trace Brier of 0.1972. The model-dependent calibration magnitudes (DeepSeek ECE is 19$\\times$ higher than Qwen) prevent us from claiming universal near-perfect calibration, but the direction of improvement is consistent.\n\n\\subsection{Few-Shot Frontier Model Baselines}\n\\label{sec:exp-fewshot}\n\nTable~\\ref{tab:fewshot} compares SFT against zero-shot and few-shot prompting with GPT-4o and Claude Sonnet. GPT-4o with 3-shot exception-only prompting achieves 97.2\\% accuracy, 2.63pp below SFT (99.83\\%). This gap is statistically significant ($n$\\,=\\,1{,}190, $p$\\,=\\,0.001) but small in absolute terms.\n\n\\begin{table}[t]\n\\centering\n\\caption{SFT vs.\\ frontier model baselines. SFT achieves the highest accuracy at $\\sim$300$\\times$ lower cost. Frontier models lack logit access for calibration. Exception-only input consistently produces the largest accuracy gain across all methods.}\n\\label{tab:fewshot}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Accuracy} & \\textbf{Cost/1190} & \\textbf{Latency} & \\textbf{ECE} \\\\\n\\midrule\nSFT exc.\\ (Qwen-7B) & \\textbf{99.83\\%} & \\$0.03 & $\\sim$50ms & 0.0027 \\\\\nGPT-4o 3-shot + exc. & 97.2\\% & $\\sim$\\$15 & $\\sim$2s & N/A \\\\\nClaude 3-shot + exc. & 96.5\\% & $\\sim$\\$10 & $\\sim$1.8s & N/A \\\\\nGPT-4o 0-shot + exc. & 95.5\\% & $\\sim$\\$12 & $\\sim$2s & N/A \\\\\nGPT-4o 0-shot no-trace & 82.3\\% & $\\sim$\\$8 & $\\sim$1.5s & N/A \\\\\nSFT no-trace (Qwen-7B) & 75.1\\% & \\$0.02 & $\\sim$30ms & 0.1715 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThree factors justify the SFT approach despite the narrow accuracy gap. First, \\textbf{cost}: SFT inference costs approximately \\$0.03 per 1{,}190 samples versus \\$15 for GPT-4o, a $\\sim$300$\\times$ difference at scale. Second, \\textbf{calibration}: SFT provides logit-level confidence scores (ECE\\,=\\,0.0027) while API-based models do not expose logits, precluding probability calibration. Third, \\textbf{deployment}: SFT models can run offline without API dependency.\n\nThe few-shot results also reinforce the exception dominance finding from a different angle. GPT-4o gains +13.2pp from exception traces (82.3\\% $\\to$ 95.5\\% zero-shot), confirming that the exception signal is valuable regardless of whether the consumer is an SFT model or a prompted frontier model.\n\n\\subsection{Budget Curve Analysis: Model-Dependent Patterns}\n\\label{sec:exp-budget}\n\nTable~\\ref{tab:budget} presents the full budget curve matrix across four models. Each model exhibits a qualitatively different accuracy-vs-length pattern, and no universal phase transition exists.\n\n\\begin{table}[t]\n\\centering\n\\caption{Full trace budget curves across four models. Each model shows a distinct pattern. Only Qwen-7B is monotonically increasing. Accuracy is reported for seed 42.}\n\\label{tab:budget}\n\\small\n\\begin{tabular}{lcccccl}\n\\toprule\n\\textbf{Model} & \\textbf{t-256} & \\textbf{t-384} & \\textbf{t-512} & \\textbf{t-1024} & \\textbf{t-2048} & \\textbf{Pattern} \\\\\n\\midrule\nQwen-7B & 77.5 & 84.7 & 93.6 & 96.5 & 97.3 & gradual S-curve \\\\\nQwen-1.5B & 72.6 & 74.5 & 95.6 & 96.6 & 97.9 & step at 512 \\\\\nDeepSeek & 76.4 & 88.3 & 93.9 & 96.5 & 95.0 & early + tail regr. \\\\\nCodeLlama & 77.9 & 73.5 & 97.5 & 98.2 & 41.8 & W-shape \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Qwen-7B} is the only model with a clean monotonic budget curve, showing gradual improvement from 77.5\\% (tail-256) to 97.3\\% (tail-2048) with consistent gains at each step. \\textbf{Qwen-1.5B} displays a sharp step function: tail-384 provides almost no improvement over tail-256 (+1.9pp), then tail-512 jumps by +21.1pp, suggesting a critical information threshold between 384 and 512 tokens. \\textbf{DeepSeek} shows early-onset improvement (tail-384 already at 88.3\\%, +11.9pp over tail-256) but exhibits a slight regression at tail-2048 (95.0\\% vs.\\ 96.5\\% at tail-1024), indicating that longer context introduces noise. \\textbf{CodeLlama} produces a non-monotonic W-shape: tail-384 is \\emph{worse} than tail-256 ($-$4.4pp), tail-512 jumps to 97.5\\%, and tail-2048 collapses to 41.8\\% ($-$56.4pp).\n\nThe cross-model standard deviation at tail-384 is 6.4pp with a range of 14.8pp (73.5\\% to 88.3\\%). These divergent patterns confirm that the relationship between trace length and verdict accuracy is entirely model-specific. Exception-only traces, by contrast, achieve 99.83\\% on all four models regardless of length budget, because the exception signal is compact enough to never require truncation.\n\n\\subsection{Seed Robustness of Budget Curves}\n\\label{sec:exp-seed-budget}\n\nTable~\\ref{tab:seed-budget} reports tail-512 accuracy across three seeds for each model, assessing whether the single-seed budget curves are reliable. Only Qwen-7B shows robust seed consistency ($\\sigma$\\,=\\,0.6pp). CodeLlama's $\\sigma$\\,=\\,8.7pp (range: 80.9\\%--97.5\\%) makes its single-seed data unreliable.\n\n\\begin{table}[t]\n\\centering\n\\caption{Seed robustness at tail-512 across four models. Exception-only seed variance is shown for comparison. Full-trace seed sensitivity scales with signal complexity.}\n\\label{tab:seed-budget}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Model} & \\textbf{s42} & \\textbf{s123} & \\textbf{s456} & \\textbf{Mean} & \\textbf{$\\sigma$} & \\textbf{Exc.\\ $\\sigma$} \\\\\n\\midrule\nQwen-7B & 93.6 & 92.4 & 93.1 & 93.0 & 0.6pp & 0.00pp \\\\\nQwen-1.5B & 95.6 & 90.8 & 94.2 & 93.5 & 2.5pp & --- \\\\\nDeepSeek & 93.9 & 87.6 & 91.9 & 91.1 & 3.2pp & 4.8pp \\\\\nCodeLlama & 97.5 & 80.9 & 94.3 & 90.9 & 8.7pp & 0.1pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe contrast between exception-only and full-trace seed variance is stark. CodeLlama's exception-only $\\sigma$ is 0.1pp while its tail-512 $\\sigma$ is 8.7pp, an 87$\\times$ ratio. This provides additional evidence for the ``simplicity enables robustness'' principle: the structurally simplest signal produces the most stable training outcomes.\n\n\\subsection{Error Analysis}\n\\label{sec:exp-errors}\n\nTable~\\ref{tab:errors} breaks down prediction errors by trace condition. The error profiles are qualitatively different across conditions, confirming that different representations fail on orthogonal dimensions.\n\n\\begin{table}[t]\n\\centering\n\\caption{Error category distribution across trace conditions (Qwen-7B). Exception-only errors are irreducible; full-trace errors are dominated by information overload.}\n\\label{tab:errors}\n\\small\n\\begin{tabular}{lcll}\n\\toprule\n\\textbf{Condition} & \\textbf{Errors} & \\textbf{Primary category} & \\textbf{Actionable?} \\\\\n\\midrule\nexception\\_only & 2 & GeneratorExit (100\\%) & No (irreducible) \\\\\nVOTA & 7 & Mixed: GenExit/attn.\\ dilution/ambiguous & Partial \\\\\nfull\\_trace & 217 & Long-trace overload (65\\%) & No\\tablefootnote{Would require architectural changes beyond LoRA SFT.} \\\\\nno\\_trace & 296 & Subtle bugs from code alone (37\\%) & No (inherent) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nException-only's 2 errors are \\texttt{GeneratorExit} false negatives, fully characterized in Section~\\ref{sec:exp-main}. VOTA's 7 errors split into three categories: 2 inherited \\texttt{GeneratorExit} cases, 3 caused by loop/ae tokens diluting attention on the exception signal, and 2 from ambiguous conflicting signals (normal loops but abnormal exceptions). Full-trace's 217 errors are dominated by long-program information overload (142/217, 65\\%), where traces are too long for effective processing. Error samples have a median trace length 2.3$\\times$ longer than correctly classified samples. The cross-condition error overlap is low (exception $\\cap$ no-trace overlap: 0.7\\%), confirming orthogonal failure modes.\n\n\\subsection{Training Dynamics}\n\\label{sec:exp-dynamics}\n\nTable~\\ref{tab:dynamics} compares learning curves for exception-only, full-trace, and no-trace conditions. Exception-only converges in approximately 100 training steps, reaching 99.1\\% accuracy. Full-trace converges more slowly (200 steps) to a much lower ceiling (81.8\\%). At step 50, exception-only (96.2\\%) already surpasses the full-trace converged accuracy, meaning exception-only reaches a higher ceiling in one-sixth of the training time. Step-to-step variance for exception-only ($\\sigma$\\,=\\,0.003) is 6$\\times$ lower than full-trace ($\\sigma$\\,=\\,0.018), reflecting the smoother optimization landscape of the simpler signal.\n\n\\begin{table}[t]\n\\centering\n\\caption{Learning curve milestones (Qwen-7B). Exception-only at step 50 already surpasses full-trace's converged accuracy.}\n\\label{tab:dynamics}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Step 50} & \\textbf{Step 100} & \\textbf{Step 200} & \\textbf{Final} & \\textbf{Conv.} & \\textbf{Step $\\sigma$} \\\\\n\\midrule\nexception\\_only & 96.2\\% & 99.1\\% & 99.8\\% & 99.83\\% & 100 & 0.003 \\\\\nfull\\_trace & 72.1\\% & 76.8\\% & 81.2\\% & 81.8\\% & 200 & 0.018 \\\\\nno\\_trace & 71.5\\% & 73.8\\% & 75.0\\% & 75.1\\% & 150 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Out-of-Distribution Generalization}\n\\label{sec:exp-ood}\n\nTable~\\ref{tab:ood} evaluates generalization to LeetCode-style problems drawn from a different distribution than the HumanEval/MBPP training data. Exception-only accuracy drops from 99.83\\% to 87.1\\% ($-$12.7pp), indicating partial overfitting to the training distribution's exception patterns (dominated by \\texttt{TypeError}, \\texttt{ValueError}, \\texttt{AssertionError}). The relative ordering is preserved: exception-only (87.1\\%) outperforms VOTA (79.3\\%) and no-trace (68.2\\%) on OOD data, confirming that exception dominance generalizes even when absolute numbers decline.\n\n\\begin{table}[t]\n\\centering\n\\caption{Out-of-distribution generalization (Qwen-7B). Relative ordering is preserved, but absolute accuracy drops, especially for exception-only ($-$12.7pp).}\n\\label{tab:ood}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Condition} & \\textbf{In-dist.} & \\textbf{OOD (Python)} & \\textbf{$\\Delta$} \\\\\n\\midrule\nexception\\_only & 99.83\\% & 87.1\\% & $-$12.7pp \\\\\nVOTA & 99.41\\% & 79.3\\% & $-$20.1pp \\\\\nno\\_trace & 75.13\\% & 68.2\\% & $-$6.9pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCross-language evaluation (Java, JavaScript, C++) was not feasible within the experimental timeline due to the need for language-specific trace collection infrastructure and exception format normalization. We note this as a limitation.\n\n% ============================================================\n\\section{Discussion}\n\\label{sec:discussion}\n% ============================================================\n\n\\paragraph{Why simplicity is robustness.}\nThe central finding of this work is that the structurally simplest trace component is also the most robust. Exception events are short, structured, and encode a single semantic dimension: fault presence or absence. This simplicity provides robustness along every axis we measured: cross-model accuracy (99.33--99.83\\% on 4 models), seed stability (0.00pp $\\sigma$ on Qwen-7B, 0.1pp on CodeLlama), calibration (ECE as low as 0.0027), and training speed (converges in 100 steps). Every additional trace component introduces model-dependent behavior. Budget curves are the clearest example: four models produce four qualitatively different patterns, with CodeLlama exhibiting catastrophic collapse at tail-2048 (41.8\\%). Exception-only traces are immune to length budget effects because they never approach context limits.\n\n\\paragraph{VOTA as fault indicator isolation.}\nVOTA's value lies not in generic trace compression but in automatically isolating exception events from noisy full traces. Removing assertion-point information from VOTA does not change accuracy (99.41\\% $\\to$ 99.41\\%), and exception-only (99.83\\%) exceeds full VOTA. The ``compression helps'' narrative was a stepping stone; the real mechanism is diagnostic signal extraction.\n\n\\paragraph{Model-dependent calibration.}\nWhile all models show calibration improvement from exception traces, the magnitude varies by 19$\\times$ across models (Qwen-7B ECE 0.0027 vs.\\ DeepSeek 0.0523). DeepSeek's poor calibration despite high accuracy (99.33\\%) parallels a broader pattern we observe: token-level training loss and sample-level classification quality can diverge. In DeepSeek's case, two seeds with nearly identical training loss (0.1225 vs.\\ 0.122) produce accuracy differences of 8.2pp (99.33\\% vs.\\ 91.09\\%), with the gap concentrated in fail recall (1.0 vs.\\ 0.705). This suggests that verdict tasks should use task-specific metrics for checkpoint selection, not standard evaluation loss.\n\n\\paragraph{Limitations.}\nOur dataset covers only Python and two benchmarks (HumanEval + MBPP-sanitized). OOD generalization shows 12.7pp degradation on LeetCode-style problems, and cross-language evaluation was not feasible. The study uses only four models from two architecture families. Exception-only's near-perfect accuracy on in-distribution data partially depends on the distribution of exception types in HumanEval/MBPP. Seed sensitivity on DeepSeek (one outlier seed at 91.09\\%) suggests that models with less stable LoRA training landscapes may require multi-seed selection or training stabilization techniques.\n\n% ============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n% ============================================================\n\nWe studied what trace components matter for verdict prediction across four code language models. The answer is simple: exception events are the only universally robust signal. They achieve near-perfect accuracy on every model tested, with provably irreducible residual errors. All other trace components and length-accuracy relationships are model-dependent. For practitioners building verdict prediction systems, the implication is direct: instrument for exceptions, discard everything else.\n\n% ============================================================\n% References\n% ============================================================\n\\bibliographystyle{plain}\n\\begin{thebibliography}{10}\n\n\\bibitem{dcsh2025}\nDCSH Authors.\n\\newblock Execution Traces for Code Generation: A Systematic Comparison.\n\\newblock In \\emph{EMNLP Findings}, 2025.\n\n\\bibitem{tracepile2025}\nTracePile Authors.\n\\newblock TracePile: Scaling Trace-Augmented Code Training.\n\\newblock In \\emph{NeurIPS}, 2025.\n\n\\bibitem{traced2024}\nTRACED Authors.\n\\newblock TRACED: Execution-aware Pre-training for Source Code.\n\\newblock In \\emph{ICSE}, 2024.\n\n\\bibitem{cruxeval2024}\nA.~Gu, B.~Rozière, H.~Leather, A.~Solar-Lezama, G.~Synnaeve, S.~I.~Wang.\n\\newblock CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem{codeexecutor2024}\nCodeExecutor Authors.\n\\newblock CodeExecutor: Learning to Execute Code with Language Models.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "8a45f9a6-8418-4d20-b04e-679b66e2c375",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "175abc6b-2146-427e-acfe-4e3e17983955",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T125926 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-stu…",
  "leafUuid": "2bb50a0b-1790-45ad-a7ba-3a40699e5638",
  "sessionId": "175abc6b-2146-427e-acfe-4e3e17983955"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier dream paper for dream_20260518T125926",
  "sessionId": "175abc6b-2146-427e-acfe-4e3e17983955"
}
```

---

### Tool call

_source line 28 · 2026-05-18T13:51:59.058Z_

<details open><summary>🔧 Tool call — Bash · `toolu_016NTPmFduLPDUzJaoUkQVTk`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2bb50a0b-1790-45ad-a7ba-3a40699e5638",
  "isSidechain": false,
  "requestId": "req_011CbA9K5DDJ5WN43pbp3ApQ",
  "type": "assistant",
  "uuid": "f2df2e37-8ed9-49e3-acba-aeb5fee5c97e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "175abc6b-2146-427e-acfe-4e3e17983955",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DvD6hB7Rb3p6KqvxCi8Gu4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10068,
      "cache_read_input_tokens": 56393,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10068,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 144,
          "cache_read_input_tokens": 56393,
          "cache_creation_input_tokens": 10068,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10068
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

_source line 29 · 2026-05-18T13:52:01.573Z_

<details><summary>↩ Tool result · `toolu_016NTPmFduLPDUzJaoUkQVTk`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))
(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tablefootnote/tablefootnote.sty
(/usr/share/texlive/texmf-dist/tex/latex/letltxmacro/letltxmacro.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xifthen/xifthen.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/calc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/ifthen.sty)
(/usr/share/texlive/texmf-dist/tex/latex/ifmtarg/ifmtarg.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty)))
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

LaTeX Warning: Citation `dcsh2025' on page 1 undefined on input line 36.


LaTeX Warning: Citation `tracepile2025' on page 1 undefined on input line 36.


LaTeX Warning: Citation `traced2024' on page 1 undefined on input line 36.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]

LaTeX Warning: Citation `dcsh2025' on page 2 undefined on input line 59.


LaTeX Warning: Citation `tracepile2025' on page 2 undefined on input line 59.


LaTeX Warning: Citation `traced2024' on page 2 undefined on input line 59.


LaTeX Warning: Citation `cruxeval2024' on page 2 undefined on input line 62.


LaTeX Warning: Citation `codeexecutor2024' on page 2 undefined on input line 62
.

[2]
Overfull \hbox (6.80669pt too wide) in paragraph at lines 88--89
 []\T1/cmr/bx/n/10.95 VOTA (Verdict-Optimized Trace Ab-strac-tion).[] \T1/cmr/m
/n/10.95 A three-component com-pres-sion of full traces: 

Overfull \hbox (4.21848pt too wide) in paragraph at lines 95--96
 []\T1/cmr/bx/n/10.95 Exception-only.[] \T1/cmr/m/n/10.95 Only the ex-cep-tion 
sum-mary com-po-nent of VOTA, dis-card-ing loop and assertion-

Overfull \hbox (15.78882pt too wide) in paragraph at lines 97--98
 []\T1/cmr/bx/n/10.95 Component ab-la-tions.[] \T1/cmr/m/n/10.95 We ad-di-tion-
ally test assertion-point-only (\T1/cmtt/m/n/10.95 ae_only\T1/cmr/m/n/10.95 ), 
loop-only (\T1/cmtt/m/n/10.95 loop_only\T1/cmr/m/n/10.95 ),

LaTeX Warning: Reference `tab:main-results' on page 3 undefined on input line 1
11.

[3]

LaTeX Warning: Reference `tab:calibration' on page 4 undefined on input line 15
4.

[4]

LaTeX Warning: Reference `tab:fewshot' on page 5 undefined on input line 178.


LaTeX Warning: Reference `tab:budget' on page 5 undefined on input line 206.

[5]

LaTeX Warning: Reference `tab:seed-budget' on page 6 undefined on input line 23
2.


Overfull \hbox (4.33124pt too wide) in paragraph at lines 251--252
[]\T1/cmr/m/n/10.95 The con-trast be-tween exception-only and full-trace seed v
ari-ance is stark. CodeL-lama's exception-

LaTeX Warning: Reference `tab:errors' on page 6 undefined on input line 256.

[6]

LaTeX Warning: Reference `sec:exp-main' on page 7 undefined on input line 275.


LaTeX Warning: Reference `tab:dynamics' on page 7 undefined on input line 280.


LaTeX Warning: Reference `tab:ood' on page 7 undefined on input line 301.

[7]
Overfull \hbox (13.19632pt too wide) in paragraph at lines 336--337
 []\T1/cmr/bx/n/10.95 Limitations.[] \T1/cmr/m/n/10.95 Our dataset cov-ers only
 Python and two bench-marks (Hu-manEval + MBPP-sanitized).
[8] [9] (./paper.aux)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0900.600pk>
kpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecrm0600
mktexpk: Running mf-nowin -progname=mf \mode:=ljfour; mag:=1+0/600; nonstopmode; input ecrm0600
This is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)

(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm0600.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf
 Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf
 Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]
[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]
[216] [217] [218] [219] [220] [221] [222] [223])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf
 Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]
[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]
[248] [249] [250] [251] [252] [253] [254] [255])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf
 Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]
[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]
[152] [153] [154] [155] [156] [157])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf
 Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]
[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]
[183] [184] [185] [186] [187] [188])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf
 Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]
[95] [127] [32])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf
 Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]
[59] [61] [96] [189] [17] [45] [16] [21] [22])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf
 Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf
 Ok [24] [34] [35] [36] [37] [64] [191] [159])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf
 Ok [25] [26] [28] [27] [29] [30] [31])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf
 Ok [38] [63] [190])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf
 Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]
[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf
 Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]
[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]
[121] [122])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf
 Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf
 Ok) ) ) )
Font metrics written on ecrm0600.tfm.
Output written on ecrm0600.600gf (256 characters, 32624 bytes).
Transcript written on ecrm0600.log.
mktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0600.600pk: successfully generated.
 &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0600.600pk>
kpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecrm0700
mktexpk: Running mf-nowin -progname=mf \mode:=ljfour; mag:=1+0/600; nonstopmode; input ecrm0700
This is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)

(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm0700.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf
 Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf
 Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]
[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]
[216] [217] [218] [219] [220] [221] [222] [223])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf
 Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]
[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]
[248] [249] [250] [251] [252] [253] [254] [255])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf
 Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]
[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]
[152] [153] [154] [155] [156] [157])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf
 Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]
[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]
[183] [184] [185] [186] [187] [188])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf
 Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]
[95] [127] [32])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf
 Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]
[59] [61] [96] [189] [17] [45] [16] [21] [22])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf
 Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf
 Ok [24] [34] [35] [36] [37] [64] [191] [159])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf
 Ok [25] [26] [28] [27] [29] [30] [31])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf
 Ok [38] [63] [190])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf
 Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]
[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf
 Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]
[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]
[121] [122])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf
 Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf
 Ok) ) ) )
Font metrics written on ecrm0700.tfm.
Output written on ecrm0700.600gf (256 characters, 37344 bytes).
Transcript written on ecrm0700.log.
mktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0700.600pk: successfully generated.
 &lt;/home/ubuntu/.texlive
2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0700.600pk> &lt;/home/ubuntu/.texli
ve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.tex
live2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.t
exlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1095.600pk> &lt;/home/ubuntu/
.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubunt
u/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubu
ntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/u
buntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home
/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/ho
me/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/
home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> 
&lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk
> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600
pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>
Output written on paper.pdf (9 pages, 196046 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))
(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tablefootnote/tablefootnote.sty
(/usr/share/texlive/texmf-dist/tex/latex/letltxmacro/letltxmacro.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xifthen/xifthen.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/calc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/ifthen.sty)
(/usr/share/texlive/texmf-dist/tex/latex/ifmtarg/ifmtarg.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
(./paper.aux)
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(./paper.out) (./paper.out)
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}] [2]
Overfull \hbox (6.80669pt too wide) in paragraph at lines 88--89
 []\T1/cmr/bx/n/10.95 VOTA (Verdict-Optimized Trace Ab-strac-tion).[] \T1/cmr/m
/n/10.95 A three-component com-pres-sion of full traces: 

Overfull \hbox (4.21848pt too wide) in paragraph at lines 95--96
 []\T1/cmr/bx/n/10.95 Exception-only.[] \T1/cmr/m/n/10.95 Only the ex-cep-tion 
sum-mary com-po-nent of VOTA, dis-card-ing loop and assertion-

Overfull \hbox (15.78882pt too wide) in paragraph at lines 97--98
 []\T1/cmr/bx/n/10.95 Component ab-la-tions.[] \T1/cmr/m/n/10.95 We ad-di-tion-
ally test assertion-point-only (\T1/cmtt/m/n/10.95 ae_only\T1/cmr/m/n/10.95 ), 
loop-only (\T1/cmtt/m/n/10.95 loop_only\T1/cmr/m/n/10.95 ),
[3] [4] [5]
Overfull \hbox (4.33124pt too wide) in paragraph at lines 251--252
[]\T1/cmr/m/n/10.95 The con-trast be-tween exception-only and full-trace seed v
ari-ance is stark. CodeL-lama's exception-
[6] [7]
Overfull \hbox (13.19632pt too wide) in paragraph at lines 336--337
 []\T1/cmr/bx/n/10.95 Limitations.[] \T1/cmr/m/n/10.95 Our dataset cov-ers only
 Python and two bench-marks (Hu-manEval + MBPP-sanitized).
[8] [9] (./paper.aux) )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0900.600pk> &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0600.600pk> &lt;/home/ubuntu/.texlive
2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0700.600pk> &lt;/home/ubuntu/.texli
ve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.tex
live2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.t
exlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1095.600pk> &lt;/home/ubuntu/
.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubunt
u/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubu
ntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/u
buntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home
/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/ho
me/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/
home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> 
&lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk
> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600
pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>
Output written on paper.pdf (9 pages, 197701 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2df2e37-8ed9-49e3-acba-aeb5fee5c97e",
  "isSidechain": false,
  "promptId": "cde04d7b-c03d-49ea-b3f7-a9fea2ed96f5",
  "type": "user",
  "uuid": "852734dd-f47b-45d2-9c47-3fbb5fdd7e45",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tablefootnote/tablefootnote.sty\n(/usr/share/texlive/texmf-dist/tex/latex/letltxmacro/letltxmacro.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xifthen/xifthen.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/calc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/ifthen.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/ifmtarg/ifmtarg.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nLaTeX Warning: Citation `dcsh2025' on page 1 undefined on input line 36.\n\n\nLaTeX Warning: Citation `tracepile2025' on page 1 undefined on input line 36.\n\n\nLaTeX Warning: Citation `traced2024' on page 1 undefined on input line 36.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]\n\nLaTeX Warning: Citation `dcsh2025' on page 2 undefined on input line 59.\n\n\nLaTeX Warning: Citation `tracepile2025' on page 2 undefined on input line 59.\n\n\nLaTeX Warning: Citation `traced2024' on page 2 undefined on input line 59.\n\n\nLaTeX Warning: Citation `cruxeval2024' on page 2 undefined on input line 62.\n\n\nLaTeX Warning: Citation `codeexecutor2024' on page 2 undefined on input line 62\n.\n\n[2]\nOverfull \\hbox (6.80669pt too wide) in paragraph at lines 88--89\n []\\T1/cmr/bx/n/10.95 VOTA (Verdict-Optimized Trace Ab-strac-tion).[] \\T1/cmr/m\n/n/10.95 A three-component com-pres-sion of full traces: \n\nOverfull \\hbox (4.21848pt too wide) in paragraph at lines 95--96\n []\\T1/cmr/bx/n/10.95 Exception-only.[] \\T1/cmr/m/n/10.95 Only the ex-cep-tion \nsum-mary com-po-nent of VOTA, dis-card-ing loop and assertion-\n\nOverfull \\hbox (15.78882pt too wide) in paragraph at lines 97--98\n []\\T1/cmr/bx/n/10.95 Component ab-la-tions.[] \\T1/cmr/m/n/10.95 We ad-di-tion-\nally test assertion-point-only (\\T1/cmtt/m/n/10.95 ae_only\\T1/cmr/m/n/10.95 ), \nloop-only (\\T1/cmtt/m/n/10.95 loop_only\\T1/cmr/m/n/10.95 ),\n\nLaTeX Warning: Reference `tab:main-results' on page 3 undefined on input line 1\n11.\n\n[3]\n\nLaTeX Warning: Reference `tab:calibration' on page 4 undefined on input line 15\n4.\n\n[4]\n\nLaTeX Warning: Reference `tab:fewshot' on page 5 undefined on input line 178.\n\n\nLaTeX Warning: Reference `tab:budget' on page 5 undefined on input line 206.\n\n[5]\n\nLaTeX Warning: Reference `tab:seed-budget' on page 6 undefined on input line 23\n2.\n\n\nOverfull \\hbox (4.33124pt too wide) in paragraph at lines 251--252\n[]\\T1/cmr/m/n/10.95 The con-trast be-tween exception-only and full-trace seed v\nari-ance is stark. CodeL-lama's exception-\n\nLaTeX Warning: Reference `tab:errors' on page 6 undefined on input line 256.\n\n[6]\n\nLaTeX Warning: Reference `sec:exp-main' on page 7 undefined on input line 275.\n\n\nLaTeX Warning: Reference `tab:dynamics' on page 7 undefined on input line 280.\n\n\nLaTeX Warning: Reference `tab:ood' on page 7 undefined on input line 301.\n\n[7]\nOverfull \\hbox (13.19632pt too wide) in paragraph at lines 336--337\n []\\T1/cmr/bx/n/10.95 Limitations.[] \\T1/cmr/m/n/10.95 Our dataset cov-ers only\n Python and two bench-marks (Hu-manEval + MBPP-sanitized).\n[8] [9] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0900.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecrm0600\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecrm0600\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm0600.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf\n Ok [25] [26] [28] [27] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf\n Ok) ) ) )\nFont metrics written on ecrm0600.tfm.\nOutput written on ecrm0600.600gf (256 characters, 32624 bytes).\nTranscript written on ecrm0600.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0600.600pk: successfully generated.\n &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0600.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecrm0700\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecrm0700\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm0700.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf\n Ok [25] [26] [28] [27] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf\n Ok) ) ) )\nFont metrics written on ecrm0700.tfm.\nOutput written on ecrm0700.600gf (256 characters, 37344 bytes).\nTranscript written on ecrm0700.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0700.600pk: successfully generated.\n &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0700.600pk> &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1095.600pk> &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home\n/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/ho\nme/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/\nhome/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> \n&lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk\n> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600\npk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>\nOutput written on paper.pdf (9 pages, 196046 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tablefootnote/tablefootnote.sty\n(/usr/share/texlive/texmf-dist/tex/latex/letltxmacro/letltxmacro.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xifthen/xifthen.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/calc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/ifthen.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/ifmtarg/ifmtarg.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}] [2]\nOverfull \\hbox (6.80669pt too wide) in paragraph at lines 88--89\n []\\T1/cmr/bx/n/10.95 VOTA (Verdict-Optimized Trace Ab-strac-tion).[] \\T1/cmr/m\n/n/10.95 A three-component com-pres-sion of full traces: \n\nOverfull \\hbox (4.21848pt too wide) in paragraph at lines 95--96\n []\\T1/cmr/bx/n/10.95 Exception-only.[] \\T1/cmr/m/n/10.95 Only the ex-cep-tion \nsum-mary com-po-nent of VOTA, dis-card-ing loop and assertion-\n\nOverfull \\hbox (15.78882pt too wide) in paragraph at lines 97--98\n []\\T1/cmr/bx/n/10.95 Component ab-la-tions.[] \\T1/cmr/m/n/10.95 We ad-di-tion-\nally test assertion-point-only (\\T1/cmtt/m/n/10.95 ae_only\\T1/cmr/m/n/10.95 ), \nloop-only (\\T1/cmtt/m/n/10.95 loop_only\\T1/cmr/m/n/10.95 ),\n[3] [4] [5]\nOverfull \\hbox (4.33124pt too wide) in paragraph at lines 251--252\n[]\\T1/cmr/m/n/10.95 The con-trast be-tween exception-only and full-trace seed v\nari-ance is stark. CodeL-lama's exception-\n[6] [7]\nOverfull \\hbox (13.19632pt too wide) in paragraph at lines 336--337\n []\\T1/cmr/bx/n/10.95 Limitations.[] \\T1/cmr/m/n/10.95 Our dataset cov-ers only\n Python and two bench-marks (Hu-manEval + MBPP-sanitized).\n[8] [9] (./paper.aux) )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0900.600pk> &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0600.600pk> &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0700.600pk> &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1095.600pk> &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home\n/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/ho\nme/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/\nhome/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> \n&lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk\n> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600\npk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>\nOutput written on paper.pdf (9 pages, 197701 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "f2df2e37-8ed9-49e3-acba-aeb5fee5c97e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/worst",
  "sessionId": "175abc6b-2146-427e-acfe-4e3e17983955",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T125926 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-stu…",
  "leafUuid": "852734dd-f47b-45d2-9c47-3fbb5fdd7e45",
  "sessionId": "175abc6b-2146-427e-acfe-4e3e17983955"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier dream paper for dream_20260518T125926",
  "sessionId": "175abc6b-2146-427e-acfe-4e3e17983955"
}
```

---

### Assistant

_source line 32 · 2026-05-18T13:52:12.720Z_

编译成功，9 页 PDF，无错误。所有 10 个实验均有对应的 section/table 覆盖：

| 实验 | 对应位置 |
|------|---------|
| qwen7b/qwen15b/deepseek/codellama budget curves | Table 4 (Sec 4.5) |
| cross\_model\_synthesis | Table 4 + Sec 4.5 叙事 |
| cross\_seed\_budget\_curve | Table 5 (Sec 4.6) |
| error\_analysis | Table 6 (Sec 4.7) |
| cross\_model\_calibration | Table 3 (Sec 4.3) |
| few\_shot\_frontier\_baseline | Table 2 (Sec 4.4) |
| ood\_generalization | Table 7 (Sec 4.8) |
| training\_dynamics | Table 8 (Sec 4.7) |

论文输出在 `worst/paper.pdf`，按 narrative guidance 将 exception dominance 作为唯一 anchor，budget curves 放在 Results 但定位为 model-dependent 反面教材，few-shot baseline 用 cost/calibration 辩护 SFT 价值。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "852734dd-f47b-45d2-9c47-3fbb5fdd7e45",
  "isSidechain": false,
  "requestId": "req_011CbA9KY3FbeiCvLLYJCPCR",
  "type": "assistant",
  "uuid": "a9d12bc2-5b64-48df-8307-432934c5c2e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260518T125926/worst",
  "sessionId": "175abc6b-2146-427e-acfe-4e3e17983955",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QP5PinPMkYGbjJWnPRn7Mj",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11031,
      "cache_read_input_tokens": 66461,
      "output_tokens": 327,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11031,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 327,
          "cache_read_input_tokens": 66461,
          "cache_creation_input_tokens": 11031,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11031
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

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T125926 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-stu…",
  "leafUuid": "a9d12bc2-5b64-48df-8307-432934c5c2e7",
  "sessionId": "175abc6b-2146-427e-acfe-4e3e17983955"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier dream paper for dream_20260518T125926",
  "sessionId": "175abc6b-2146-427e-acfe-4e3e17983955"
}
```

---
