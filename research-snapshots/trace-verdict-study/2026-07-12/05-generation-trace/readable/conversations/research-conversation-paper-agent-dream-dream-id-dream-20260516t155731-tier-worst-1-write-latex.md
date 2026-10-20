# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T155731 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-1/34e72d3c-d7c4-44c6-899d-982fad42e8f3.jsonl`
- **Structured JSON:** [`29aa7f3903be69d33f3f.json`](../../sessions/29/29aa7f3903be69d33f3f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T16:22:16.184Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T16:22:16.184Z",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T155731 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/worst/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：原始 'fault semantics' 叙事不成立。nomarker 实验暴露 exception_only 99.83% 中约 10pp 来自格式标记 [No exception data in trace] 的 shortcut 学习。SFT 模型（99.83%）仅比 regex B5（99.33%）高 0.50pp； 移除标记后 SFT 降至 ~89.6%，反而低于 regex。论文贡献 reframe 为：**trace formatting as implicit task specification** —— SFT 中 format/structure choices 对 downstream classification 具有 outsized impact。 核心 decomposition：总 trace lift 24.7pp = content signal ~14.9pp (60%) + format marker ~9.8pp (40%)。 format marker 贡献（~10pp）单独即超过 full_trace 全部 lift（6.6pp），揭示 SFT shortcut learning 的严重性。 Claim 1 重写为 'structured format markers dominate verdict prediction in exception traces'。 Claim 3 重写为 'format engineering > content richness for SFT verdict tasks'。 与 shortcut learning 文献（NLI artifacts, annotation artifacts, Gururangan et al. 2018）对话。 仍冲 EMNLP Main —— angle 从 positive finding 变为 cautionary finding + practical design principle。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-16T16:22:16.188Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T16:22:16.188Z",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3"
}
```

---

## Round 1

46 recorded events

### User

_source line 3 · 2026-05-16T16:22:16.207Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T155731 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/worst/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：原始 'fault semantics' 叙事不成立。nomarker 实验暴露 exception_only 99.83% 中约 10pp 来自格式标记 [No exception data in trace] 的 shortcut 学习。SFT 模型（99.83%）仅比 regex B5（99.33%）高 0.50pp； 移除标记后 SFT 降至 ~89.6%，反而低于 regex。论文贡献 reframe 为：**trace formatting as implicit task specification** —— SFT 中 format/structure choices 对 downstream classification 具有 outsized impact。 核心 decomposition：总 trace lift 24.7pp = content signal ~14.9pp (60%) + format marker ~9.8pp (40%)。 format marker 贡献（~10pp）单独即超过 full_trace 全部 lift（6.6pp），揭示 SFT shortcut learning 的严重性。 Claim 1 重写为 'structured format markers dominate verdict prediction in exception traces'。 Claim 3 重写为 'format engineering > content richness for SFT verdict tasks'。 与 shortcut learning 文献（NLI artifacts, annotation artifacts, Gururangan et al. 2018）对话。 仍冲 EMNLP Main —— angle 从 positive finding 变为 cautionary finding + practical design principle。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "48d55f22-f9cb-4f29-850e-ff4d4525816b",
  "type": "user",
  "uuid": "6677489a-e69a-4a95-9a6b-d242237deb25",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T16:22:16.206Z_

```json
{
  "parentUuid": "6677489a-e69a-4a95-9a6b-d242237deb25",
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
  "uuid": "b9ea7d11-4ac8-44aa-998e-e949966f298e",
  "timestamp": "2026-05-16T16:22:16.206Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T16:22:16.206Z_

```json
{
  "parentUuid": "b9ea7d11-4ac8-44aa-998e-e949966f298e",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4c909cb2-6ad5-46d0-a44b-0fbd48c8f883",
  "timestamp": "2026-05-16T16:22:16.206Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3",
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
  "aiTitle": "Generate worst-case tier paper for dream ID",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3"
}
```

---

### Assistant

_source line 7 · 2026-05-16T16:22:18.541Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c909cb2-6ad5-46d0-a44b-0fbd48c8f883",
  "isSidechain": false,
  "requestId": "req_011Cb6ZADNdBGvMSC353rCFa",
  "type": "assistant",
  "uuid": "9f4bed77-a7a6-47ef-bd6a-92a91e1a6a4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QvsGNi4mHrJ5CP55JJBCRd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11395,
      "cache_read_input_tokens": 11841,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11395,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11395,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11395
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

_source line 8 · 2026-05-16T16:22:19.167Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RXxszEcfNDseeHgxRHPtrS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f4bed77-a7a6-47ef-bd6a-92a91e1a6a4a",
  "isSidechain": false,
  "requestId": "req_011Cb6ZADNdBGvMSC353rCFa",
  "type": "assistant",
  "uuid": "c7d25ec4-7dfc-4bcc-a465-cb669ade29db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QvsGNi4mHrJ5CP55JJBCRd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11395,
      "cache_read_input_tokens": 11841,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11395,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11395,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11395
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

_source line 9 · 2026-05-16T16:22:19.476Z_

<details><summary>↩ Tool result · `toolu_01RXxszEcfNDseeHgxRHPtrS`</summary>

```text
1	[
2	  {
3	    "name": "no_trace baseline",
4	    "description": "无 trace 基线。模型仅凭 code + test input 预测 verdict。",
5	    "results": {
6	      "accuracy": 0.7513,
7	      "pass_recall": 0.7579,
8	      "fail_recall": 0.7345,
9	      "ECE": 0.1715,
10	      "Brier": 0.1972
11	    },
12	    "tables": [
13	      "Table 1: Main results — no_trace 行作为 floor"
14	    ],
15	    "figures": [],
16	    "analysis": "75.13% 是所有 trace 条件的 anchor。worst tier 的核心论点是： exception_only 的 24.7pp lift 中，~40% (10pp) 来自 format marker shortcut， ~60% (14.9pp) 来自 content signal。no_trace 确认 content signal 的起点。\n\n\n（实际数据）无 trace 时模型只能依赖代码表面特征和训练集 prior (71.51% pass)。 75.13% 仅比 majority baseline 高 3.6pp，calibration 严重失调（ECE=0.17）。 在 worst tier 下，这个数字建立了 content-free 的下界：任何高于此的增益 都需要 decompose 为 content signal vs. format shortcut。\n"
17	  },
18	  {
19	    "name": "VOTA baseline",
20	    "description": "VOTA trace SFT MVP。完整 VOTA 表征（loop + exception + ae）。",
21	    "results": {
22	      "accuracy": 0.9941,
23	      "pass_recall": 0.9882,
24	      "fail_recall": 1.0,
25	      "ECE": 0.0054
26	    },
27	    "tables": [
28	      "Table 1: Main results — VOTA 行",
29	      "Table 3: Format dependency decomposition"
30	    ],
31	    "figures": [],
32	    "analysis": "VOTA 99.41% 在 worst tier 下需重新解读：这不是 'trace reasoning' 的证据， 而是 format marker 被保留后 shortcut 仍然有效的结果。CodeLlama-13B 上 VOTA=99.92% 甚至优于 exception_only，说明更大模型能更好利用 VOTA 的 额外 format cues，进一步支持 format engineering > content hypothesis。\n\n\n（实际数据, v5 结果）VOTA 99.41% 包含所有格式标记。在 worst tier 下， VOTA 的高 accuracy 部分归因于 [No exception data in trace] 和 [ERROR] 等 format markers 提供的 shortcut。VOTA 略低于 exception_only (99.83%) 不是因为 添加信息有害，而是 loop/ae tokens 稀释了 format marker 的注意力聚焦。\n"
33	  },
34	  {
35	    "name": "full_trace baseline",
36	    "description": "完整执行 trace SFT。包含所有 trace 行（含格式标记，但被海量 trace tokens 淹没）。",
37	    "results": {
38	      "accuracy": 0.8176,
39	      "pass_recall": 0.866,
40	      "fail_recall": 0.6962,
41	      "ECE": 0.0958
42	    },
43	    "tables": [
44	      "Table 1: Main results — full_trace 行",
45	      "Table 4: Information density vs. format accessibility"
46	    ],
47	    "figures": [],
48	    "analysis": "full_trace 的 81.76% 确认：format markers 需要在 compact 表征中才能被 有效利用。这与 shortcut learning 文献一致——shortcut 的有效性取决于其 accessibility（Geirhos et al. 2020）。exception_only 将 marker 置于最 prominent 位置，最大化 shortcut 的可利用性。\n\n\n（实际数据, v5 结果）full_trace 81.76% 远低于 exception_only 99.83%。 full_trace 也包含 [No exception data in trace] 和 [ERROR] 标记，但被 数千 token 的 trace noise 包围。在 worst tier 下，这证明 format marker 的有效性取决于 signal-to-noise ratio：marker 存在但被稀释时效果大幅下降。 gradient dilution (D1) 和 information overload 共同使模型难以从 full trace 中提取 format shortcut。\n"
49	  },
50	  {
51	    "name": "VOTA minus actual/expected",
52	    "description": "移除 VOTA 中 actual/expected 值对，保留 exception + loop。验证是否为 trivial string comparison。",
53	    "results": {
54	      "accuracy": 0.9941,
55	      "pass_f1": 0.996,
56	      "fail_f1": 0.989
57	    },
58	    "tables": [
59	      "Table 2: Component ablation — vota_no_ae 行"
60	    ],
61	    "figures": [],
62	    "analysis": "vota_no_ae = VOTA 的事实在 worst tier 下有新解读：ae 组件不影响 accuracy 因为分类不依赖 ae content，而是依赖 format marker。ae 的移除没有碰到 真正的 active ingredient（format marker），所以没有效果。\n\n\n（实际数据）99.41% = 完整 VOTA，移除 ae 无影响。在 worst tier 下， 这不是 'exception content 自身 sufficient' 的证据，而是 format marker [No exception data in trace] 独立于 ae 存在——marker 未被移除，shortcut 仍完整可用。真正的 sufficiency test 是 nomarker 实验。\n"
63	  },
64	  {
65	    "name": "full_trace label-only loss",
66	    "description": "full_trace + 仅对 verdict token 计算 loss，mask trace tokens。量化 gradient dilution。",
67	    "results": {
68	      "accuracy": 0.8622,
69	      "lift_vs_standard_fulltrace": 0.0445,
70	      "pass_recall": 0.9318,
71	      "fail_recall": 0.6873
72	    },
73	    "tables": [
74	      "Table 1: Main results — label_only 行",
75	      "Table 4: Gradient dilution decomposition（26% vs 74%）"
76	    ],
77	    "figures": [],
78	    "analysis": "label-only 实验在 worst tier 下保留原有解读（gradient dilution = 26%）， 但 74% 的 information overload 部分现在重新理解为：format marker 的 accessibility bottleneck——不是 trace 内容太多导致模型'迷路'，而是 shortcut pattern 被噪声稀释导致模型无法高效利用。\n\n\n（实际数据）label-only 86.22% 比 standard full_trace 81.76% 高 4.5pp（gradient dilution 贡献）， 但仍远低于 exception_only 99.83%。在 worst tier 下重新解读： label-only 修复了 gradient dilution，但 full trace 中 format markers 仍被海量 tokens 淹没——模型在 2048 tokens 中寻找 [No exception data in trace] 的效率远低于在 exception_only 的 compact 表征中。86.22% ≈ loop_only 85.63%， 说明 label-only full_trace 实质上退化为 loop-level 的行为模式学习。\n"
79	  },
80	  {
81	    "name": "VOTA component ablation (loop/exception/ae)",
82	    "description": "分别测试 loop_only, exception_only, ae_only。量化每个组件贡献。",
83	    "results": {
84	      "exception_only_accuracy": 0.9983,
85	      "ae_only_accuracy": 0.9992,
86	      "loop_only_accuracy": 0.8563,
87	      "vota_full_accuracy": 0.9941
88	    },
89	    "tables": [
90	      "Table 2: Component ablation（reframed as format marker analysis）",
91	      "Table 5: Format marker presence vs. component accuracy"
92	    ],
93	    "figures": [],
94	    "analysis": "worst tier 下 Tier hierarchy 被重新理解为 **format marker strength hierarchy**： Tier 1 (exception/ae) 有强 explicit markers → 99%+； Tier 2 (loop) 无 explicit markers → 85%； format marker contribution ≈ 14pp (99.83 - 85.63)。 这与 nomarker 实验的 ~10pp drop 量级一致，交叉验证了 format shortcut 假说。 loop_only ≈ label_only (85.63 vs 86.22) 进一步确认：无 format marker 时， 不同表征的 content-level 学习效果相似。\n\n\n（实际数据）exception_only 99.83%, ae_only 99.92%, loop_only 85.63%。 在 worst tier 下，Tier 1 组件（exception + ae）的近完美 accuracy 需重新解读： 两者都包含强 format markers —— exception_only 有 [No exception data in trace] / [ERROR]， ae_only 有 assertion 结果的结构化标记。它们的高 accuracy 不是 'diagnostic moment' 的 语义价值，而是 format marker 的 shortcut 效应。loop_only 85.63% 没有这些强标记， 反映的是 content-level 学习的真实水平——这才是 'fault semantics' 的近似上限。\n"
95	  },
96	  {
97	    "name": "DeepSeek-Coder-6.7B 四条件验证",
98	    "description": "DeepSeek 上复现 VOTA/no_trace/full_trace/exception_only。跨模型验证 exception dominance。",
99	    "results": {
100	      "exception_only_seed42": 0.9933,
101	      "exception_only_seed456": 0.9933,
102	      "exception_only_seed123": 0.9109,
103	      "vota": 0.8445,
104	      "no_trace": 0.7336,
105	      "full_trace_v3": 0.7916
106	    },
107	    "tables": [
108	      "Table 1: Cross-model results",
109	      "Table 6: DeepSeek seed analysis — LoRA init vs format learning"
110	    ],
111	    "figures": [],
112	    "analysis": "DeepSeek 数据在 worst tier 下提供额外证据：seed42/456 精确匹配 regex B5 (99.33%) 是巧合但 suggestive——两个 seed 的 SFT 模型和一个简单 regex 达到了完全相同的 accuracy，暗示它们可能在做同一件事。seed123 outlier 的存在说明 format shortcut 的学习也非 guaranteed——LoRA 初始化不佳时 模型可能只学到部分 shortcut。\n\n\n（实际数据）DeepSeek exception_only 2/3 seeds=99.33%，1 outlier=91.09%。 在 worst tier 下：(1) seed42/456=99.33% 与 regex B5=99.33% 完全一致， 进一步暗示 SFT 学到的就是 regex 级别的 format matching； (2) seed123=91.09% 可能更接近 'without format shortcut' 的真实水平—— 该 seed 的 LoRA 初始化恰好未充分学到 format marker → pass 映射 (fail_recall=0.705 说明 [ERROR] marker 的学习也不完整)； (3) VOTA 84.45% 受 truncation 影响，但 format markers 在 VOTA 中 的位置和 accessibility 不如 exception_only compact。\n"
113	  },
114	  {
115	    "name": "DebugBench 跨任务验证",
116	    "description": "DebugBench subset 上测试 exception_only/VOTA/no_trace。验证泛化性。",
117	    "results": {
118	      "exception_only": 1.0,
119	      "vota": 0.9977,
120	      "no_trace": 0.9671
121	    },
122	    "tables": [
123	      "Table 7: DebugBench generalization (secondary evidence)"
124	    ],
125	    "figures": [],
126	    "analysis": "DebugBench 在 worst tier 下的定位不变：泛化性验证，非 mechanism 证据。 但 worst tier 论文会增加一句 caveat：DebugBench 的近完美 no_trace baseline 说明 verdict task 的难度 spectrum 很宽，format shortcut 在 easy benchmarks 上可能被 ceiling 效应掩盖。\n\n\n（实际数据）DebugBench 上 exception_only=100%, no_trace=96.71%。 在 worst tier 下：DebugBench 天花板过高（no_trace 已 96.71%）， trace lift 仅 3.29pp，无法区分 format shortcut vs. content learning。 100% 的 exception_only 不是 'fault semantics 跨数据集 robust' 的证据， 而可能只是 DebugBench 的 bug 结构恰好与 format markers 完美对齐。 此数据集在 worst tier 论文中仅作 secondary generalization validation， 不承担 mechanism 论证的任何权重。\n"
127	  },
128	  {
129	    "name": "trace length ablation (256/512/1024/full)",
130	    "description": "不同截断长度对 full_trace 准确率的影响。",
131	    "results": {
132	      "256tok": 0.7882,
133	      "512tok": 0.8042,
134	      "1024tok": 0.7723,
135	      "full_2048": 0.8176
136	    },
137	    "tables": [
138	      "Table 4: Trace length ablation — format accessibility vs. trace volume"
139	    ],
140	    "figures": [],
141	    "analysis": "trace length 数据在 worst tier 下支持 'format accessibility' 论点： 无论 trace 多长或多短，只要 format marker 不在 compact isolated 位置， 模型就无法有效利用 shortcut。exception_only 的优势不是 content richness， 而是 format marker isolation。\n\n\n（实际数据）256→512→1024→2048 = 78.82→80.42→77.23→81.76%。 非单调，收益递减，全部远低于 exception_only 99.83%。 在 worst tier 下：更多 trace tokens 不帮助 accuracy 是因为 format markers 在 full trace 中被淹没——增加 tokens 不增加 format marker 的 accessibility， 反而增加 noise。这与 shortcut learning 的 accessibility 理论一致。 真正有效的不是 trace 内容量，而是 format marker 的相对 prominence。\n"
142	  },
143	  {
144	    "name": "Calibration analysis (ECE + Brier)",
145	    "description": "ECE + reliability diagrams 对比各条件 calibration。",
146	    "results": {
147	      "exception_only_ECE": 0.0027,
148	      "exception_only_Brier": 0.0013,
149	      "no_trace_ECE": 0.1715,
150	      "no_trace_Brier": 0.1972,
151	      "loop_only_ECE": 0.0831,
152	      "full_trace_ECE": 0.0958
153	    },
154	    "tables": [
155	      "Table 8: Calibration comparison (reframed: shortcut confidence vs. content confidence)"
156	    ],
157	    "figures": [],
158	    "analysis": "worst tier 下 calibration 数据的叙事反转：从 'exception signal 使模型 know what it knows' 变为 'format shortcut 使模型过度自信于一个 brittle rule'。nomarker 实验将验证 这一解读——如果去标记后 calibration 显著恶化（ECE 升至 loop_only 水平）， 则确认 calibration 是 shortcut 的副产物而非 semantic understanding 的证据。\n\n\n（实际数据）exception_only ECE=0.0027（近完美校准）。 在 worst tier 下重新解读：极低 ECE 不是 'model understands fault semantics' 的证据， 而是 format shortcut 提供了几乎 deterministic 的映射——marker 在 → 高置信度 pass， marker 不在 → 高置信度 fail。一个完美的 shortcut 自然产生完美的 calibration。 相比之下，loop_only ECE=0.083 反映的是 content-level 学习的 calibration—— 不完美但非 trivial，这才是 genuine semantic understanding 的 calibration profile。\n"
159	  },
160	  {
161	    "name": "Seed robustness (3 seeds × exception_only + VOTA)",
162	    "description": "3 random seeds 验证 exception_only / VOTA 结果稳定性。",
163	    "results": {
164	      "qwen_exception_only_3seed": [
165	        0.9983,
166	        0.9983,
167	        0.9983
168	      ],
169	      "qwen_exception_only_std": 0.0,
170	      "qwen_vota_seed42": 0.9941,
171	      "qwen_vota_seed456": 0.9908,
172	      "deepseek_exception_only": [
173	        0.9933,
174	        0.9933,
175	        0.9109
176	      ]
177	    },
178	    "tables": [
179	      "Table 9: Seed robustness — with vs without format markers"
180	    ],
181	    "figures": [],
182	    "analysis": "seed robustness 数据在 worst tier 下完成了一个 narrative arc： with markers → perfect reproducibility (shortcut 的 hallmark)； without markers → high variance (content learning 对 init 敏感)。 这与 NLI shortcut 文献中 hypothesis-only models 的 high stability 形成平行对比。\n\n\n（实际数据）Qwen exception_only 3 seeds 完美一致，std=0。 在 worst tier 下：零方差恰好是 shortcut 的 signature——一个 trivial pattern （format marker 有无）会被任何 LoRA 初始化可靠地学到，因此 zero variance 不是 robustness 的证据，而是 simplicity / shortcut 的证据。 对比：nomarker 实验 worst tier 预测 3-seed 方差显著上升（std ~2.6pp）， 因为移除 shortcut 后模型必须学习 harder content patterns，对初始化更敏感。\n"
183	  },
184	  {
185	    "name": "Qwen-2.5-Coder-1.5B 四条件验证",
186	    "description": "1.5B 模型复现 exception_only/vota/no_trace/full_trace。验证 scale invariance。",
187	    "results": {
188	      "exception_only": 0.9983,
189	      "vota": 0.9958,
190	      "no_trace": 0.6731,
191	      "full_trace": 0.7706
192	    },
193	    "tables": [
194	      "Table 1: Cross-scale results",
195	      "Table 10: Scale invariance as shortcut evidence"
196	    ],
197	    "figures": [],
198	    "analysis": "1.5B = 7B 是 worst tier 论文的 'smoking gun' 之一。论文可以写： \"The fact that a 1.5B model achieves identical accuracy to 7B on exception_only (both 99.83%) while showing clear capacity gaps on no_trace (67.31% vs 75.13%) and full_trace (77.06% vs 81.76%) strongly suggests that exception_only success relies on a pattern simple enough to be learned at any scale — consistent with format marker matching rather than fault reasoning.\"\n\n\n（实际数据）1.5B exception_only = 99.83% = 7B。 在 worst tier 下：这是 format shortcut 假说最强的单项证据之一。 一个 1.5B 参数模型精确匹配 7B 模型意味着任务不需要 7B 的 capacity， 1.5B 即可完美学到——这与 'fault semantics' 需要 substantial reasoning capacity 的预期矛盾，却与 'format marker matching is trivial' 完美一致。 如果是 genuine fault detection，我们预期 1.5B 至少有 1-2pp 的 capacity gap。 zero gap 说明任务的 effective complexity 极低——即 regex-level。\n"
199	  },
200	  {
201	    "name": "CodeLlama-13B-Instruct 三条件验证",
202	    "description": "LLaMA 家族 + 13B scale 验证 exception_only/no_trace/vota。",
203	    "results": {
204	      "exception_only": 0.9983,
205	      "no_trace": 0.765,
206	      "vota": {
207	        "accuracy": 0.9992,
208	        "n": 1190,
209	        "errors": 1,
210	        "pass_recall": 0.9988,
211	        "fail_recall": 1.0,
212	        "pass_precision": 1.0,
213	        "fail_precision": 0.9971,
214	        "ECE_estimated": 0.001
215	      }
216	    },
217	    "tables": [
218	      "Table 1: Cross-model results — CodeLlama-13B 行",
219	      "Table 11: Exception dominance breakdown by model scale"
220	    ],
221	    "figures": [],
222	    "analysis": "CodeLlama-13B VOTA=99.92% 在 worst tier 下有双重意义： (1) exception dominance 是 capacity-dependent artifact：小模型无法充分利用 VOTA 的多种 format cues，只能依赖最 salient 的单一 marker (exception)， 给人 'exception is best' 的错觉。大模型同时利用所有 format cues 达到更高 accuracy。 (2) 这进一步支持 'format engineering' 而非 'fault semantics' 叙事—— VOTA 在 13B 上更好不是因为 'better fault reasoning'，而是因为 13B 能 simultaneously exploit multiple format shortcuts。\n\n\nexception_only=99.83%（实际数据，2 errors = GeneratorExit irreducible）。 no_trace=76.5%（实际数据）。 **VOTA=99.92%（预测）**：CodeLlama-13B 是测试的最大模型（13B vs 6.7-7B）， 在 worst tier 下 VOTA ≥ exception_only 因为： (1) 13B 有足够 capacity 利用 VOTA 全部组件（loop/ae/exception）的 format cues； (2) VOTA 的额外组件在强模型上不再是 noise 而是 supplementary signal； (3) 99.92% vs exception_only 99.83% → exception dominance 不成立（Δ = -0.09pp）。 这打破了 'exception_only always best' 的 universal claim， 证明 Claim 3 层级关系是 model-specific：小/弱模型上 exception 优于 VOTA， 大/强模型上 VOTA ≥ exception。\n"
223	  },
224	  {
225	    "name": "Multi-seed: ae_only / label_only / loop_only × 3 seeds",
226	    "description": "Tier 层级划分的 seed robustness 验证。",
227	    "results": {
228	      "ae_only_3seed": [
229	        0.9992,
230	        0.9908,
231	        0.9992
232	      ],
233	      "ae_only_mean": 0.9964,
234	      "ae_only_std": 0.0049,
235	      "label_only_3seed": [
236	        0.8622,
237	        0.8706,
238	        0.859
239	      ],
240	      "label_only_mean": 0.8639,
241	      "loop_only_3seed": [
242	        0.8563,
243	        0.8588,
244	        0.8664
245	      ],
246	      "loop_only_mean": 0.8605,
247	      "loop_only_std": 0.0052
248	    },
249	    "tables": [
250	      "Table 2: Component ablation with seed robustness",
251	      "Table 12: Variance as format marker strength proxy"
252	    ],
253	    "figures": [],
254	    "analysis": "worst tier 下 multi-seed 数据揭示一个 pattern： 高 accuracy + 低 variance = 强 format marker (exception_only: 99.83±0)； 高 accuracy + 中 variance = 中 format marker (ae_only: 99.64±0.49)； 中 accuracy + 低 variance = 无 format marker (loop/label: ~86±0.5)。 这支持 'variance 与 format marker strength 成反比' 的规律。\n\n\n（实际数据）ae_only 高方差（seed123=99.08% outlier），loop_only 和 label_only 稳定。 在 worst tier 下：ae_only 的 seed variance > exception_only 的 zero variance， 说明 ae 的 format marker（assertion 结果标记）比 exception 的 [No exception data in trace] 稍不 deterministic——可能因为 assertion marker 的格式更复杂， 不同 init 学到的程度不同。loop_only 和 label_only 的 ~86% stability 反映了 content-level learning 的 consistent ceiling（无强 format marker 时的上限）。\n"
255	  },
256	  {
257	    "name": "Format marker removal: exception_only_nomarker × 3 seeds",
258	    "description": "移除 [No exception data in trace] 格式标记后重训 exception_only。 pass 样本从 '[No exception data in trace]' 变为空/极短文本； fail 样本保留异常内容但移除 [ERROR] 前缀。 3 seeds (42/123/456) 验证 format marker 的因果贡献。\n",
259	    "results": {
260	      "nomarker_seed42": {
261	        "accuracy": 0.9176,
262	        "pass_recall": 0.887,
263	        "fail_recall": 0.993,
264	        "pass_precision": 0.997,
265	        "fail_precision": 0.778,
266	        "n": 1190,
267	        "errors": 98,
268	        "error_breakdown": "96 pass→fail FN, 2 fail→pass FP",
269	        "train_loss_estimated": 0.16
270	      },
271	      "nomarker_seed123": {
272	        "accuracy": 0.868,
273	        "pass_recall": 0.821,
274	        "fail_recall": 0.985,
275	        "pass_precision": 0.993,
276	        "fail_precision": 0.687,
277	        "n": 1190,
278	        "errors": 157,
279	        "error_breakdown": "152 pass→fail FN, 5 fail→pass FP",
280	        "train_loss_estimated": 0.17
281	      },
282	      "nomarker_seed456": {
283	        "accuracy": 0.9034,
284	        "pass_recall": 0.868,
285	        "fail_recall": 0.991,
286	        "pass_precision": 0.996,
287	        "fail_precision": 0.75,
288	        "n": 1190,
289	        "errors": 115,
290	        "error_breakdown": "112 pass→fail FN, 3 fail→pass FP",
291	        "train_loss_estimated": 0.16
292	      },
293	      "three_seed_summary": {
294	        "mean_accuracy": 0.8963,
295	        "std_accuracy": 0.025,
296	        "worst_seed_accuracy": 0.868,
297	        "best_seed_accuracy": 0.9176,
298	        "format_marker_contribution_pp": 10.2,
299	        "format_marker_pct_of_total_lift": 0.413,
300	        "content_signal_contribution_pp": 14.5
301	      },
302	      "comparison_with_regex_B5": {
303	        "regex_B5": 0.9933,
304	        "nomarker_mean": 0.8963,
305	        "delta": -0.097,
306	        "interpretation": "SFT without markers is 9.7pp BELOW regex; format marker was the mechanism"
307	      },
308	      "comparison_with_loop_only": {
309	        "loop_only_mean": 0.8605,
310	        "nomarker_mean": 0.8963,
311	        "delta": 0.036,
312	        "interpretation": "nomarker barely above loop_only; content contribution similar"
313	      },
314	      "nomarker_calibration_estimated": {
315	        "ECE": 0.065,
316	        "Brier": 0.085,
317	        "interpretation": "Calibration degrades ~24x from exception_only ECE=0.0027 to ~0.065; confirms marker-driven calibration"
318	      }
319	    },
320	    "tables": [
321	      "Table 13 (NEW — 论文核心 table): Format marker removal results",
322	      "| Seed | with marker | without marker | Δ | pass_recall Δ | fail_recall Δ |\n|------|------------|---------------|-----|---------------|---------------|\n| 42   | 99.83%     | 91.76%        | -8.07pp | -0.111  | -0.005  |\n| 123  | 99.83%     | 86.80%        | -13.03pp| -0.177  | -0.013  |\n| 456  | 99.83%     | 90.34%        | -9.49pp | -0.130  | -0.007  |\n| Mean | 99.83%     | 89.63%        | -10.20pp| -0.139  | -0.008  |\n",
323	      "Table 14: SFT vs Regex comparison",
324	      "| Method | Accuracy | Mechanism |\n|--------|----------|-----------|\n| Regex B5 (format marker) | 99.33% | [No exception data in trace] 有无 |\n| SFT exception_only (with markers) | 99.83% | format marker + minor content signal |\n| SFT exception_only (nomarker) | 89.63% | content only |\n| Regex B1 ([ERROR] presence) | 93.45% | [ERROR] keyword 有无 |\n"
325	    ],
326	    "figures": [],
327	    "analysis": "nomarker 是 worst tier 的 defining result。10.2pp drop 意味着：\n(1) FORMAT MARKER AS CLASSIFICATION SHORTCUT：SFT exception_only 学到的主要不是 'exception content → fault detection' 而是 '[No exception data in trace] 有无 → pass/fail'。 移除标记后 accuracy 从 99.83% 降至 89.63%，而 regex B5（纯 marker check）= 99.33%。 SFT with markers (99.83%) ≈ regex (99.33%)，Δ 仅 0.50pp。 SFT without markers (89.63%) < regex (99.33%)，Δ = -9.70pp。 结论：SFT 的 value-add over regex 仅 0.50pp，主要靠 format shortcut。\n(2) CONTENT CONTRIBUTION IS REAL BUT SECONDARY：nomarker 89.63% > no_trace 75.13%， content signal 贡献 14.5pp（占总 lift 的 59%）。exception content 确实有用—— 异常类型和消息文本帮助 fail detection（fail_recall 仍 >98%）。 但 pass detection 严重依赖 format marker（pass_recall 从 0.998 降至 0.86）。\n(3) SEED VARIANCE AS SHORTCUT DEPENDENCY INDICATOR：with markers std=0.0pp →  trivial pattern, perfectly reproducible；without markers std=2.5pp →  content learning is harder, init-sensitive。variance shift 是 shortcut dependency 的 causal evidence。\n(4) NARRATIVE REFRAME：论文从 'exception events as fault detection signal' 变为 'format markers as implicit task specification in SFT'。 贡献 = 揭示 SFT 中 trace format design choices 的 outsized, hidden impact， 与 shortcut learning 文献（Gururangan 2018, McCoy 2019, annotation artifacts）对话。 实践建议：trace format 设计应 explicitly 考虑 downstream task 的 shortcut affordance， 评估 SFT verdict models 时必须包含 format ablation control。\n\n\n移除 [No exception data in trace] 后，pass 样本失去唯一的 explicit classification signal。 模型必须从 'content 为空/极短 → pass' 学习，但这是一个 weaker, indirect cue： (1) 空文本不是 informative feature，而是 absence of feature——学习 absence 比学习 presence 更难； (2) 部分 pass 样本可能仍有少量非异常文本（如 GeneratorExit），制造 noise； (3) fail 样本仍有异常内容（类型 + 消息），但失去 [ERROR] 前缀后， 模型需要从原始异常文本的语义特征（如 'AssertionError', 'TypeError'）学习 fail 映射。\nseed variance 显著上升（std ~2.5pp vs 0.0pp）因为 content-level learning 对 LoRA 初始化更敏感——没有了 deterministic shortcut，模型需要学习更 nuanced 的 pattern， 不同初始化可能学到不同 decision boundaries。\nworst seed (86.8%) 接近 loop_only (85.6%)，说明无 format marker 的 exception content 提供的 signal 与 loop compression 相当——两者都是 content-level 学习，accuracy 相似。\nfail_recall 保持高位 (0.985-0.993) 因为 fail 样本仍有异常文本内容（只是没有 [ERROR] 前缀）， 模型可以从 'AssertionError: expected X got Y' 等文本学习 fail。 pass_recall 大幅下降 (0.82-0.89) 因为 pass 样本的分类依据从 explicit marker 退化为 'content 很短或为空'——这是一个 noisy, indirect signal。\n"
328	  },
329	  {
330	    "name": "Cross-cutting synthesis: format dependency master table",
331	    "description": "跨所有实验的 format marker contribution 综合分析。",
332	    "results": {
333	      "decomposition": {
334	        "total_trace_lift_pp": 24.7,
335	        "content_signal_pp": 14.5,
336	        "format_marker_pp": 10.2,
337	        "format_pct": 0.413
338	      },
339	      "model_scale_pattern": {
340	        "qwen_1.5B_exception": 0.9983,
341	        "qwen_7B_exception": 0.9983,
342	        "deepseek_6.7B_exception_median": 0.9933,
343	        "codellama_13B_exception": 0.9983,
344	        "interpretation": "scale-invariant → trivial pattern"
345	      },
346	      "format_marker_vs_regex": {
347	        "sft_with_markers": 0.9983,
348	        "regex_B5": 0.9933,
349	        "sft_without_markers": 0.8963,
350	        "delta_sft_over_regex_with": 0.005,
351	        "delta_sft_over_regex_without": -0.097
352	      },
353	      "codellama_vota_exception_gap": -0.0009
354	    },
355	    "tables": [
356	      "Table 15 (论文 summary table): Evidence chain for format shortcut hypothesis",
357	      "| Evidence | Value | Interpretation |\n|----------|-------|---------------|\n| SFT with markers | 99.83% | ≈ regex B5 (99.33%), Δ=0.50pp |\n| SFT without markers | 89.63% | < regex B5, format was the mechanism |\n| Format contribution | 10.20pp | 41.3% of total trace lift |\n| Scale invariance | 1.5B=7B=13B | Trivial task (format matching) |\n| Seed variance shift | 0→2.5pp | Shortcut removal increases instability |\n| CodeLlama-13B VOTA≥exception | -0.09pp | Exception dominance model-specific |\n"
358	    ],
359	    "figures": [],
360	    "analysis": "worst tier 论文的核心 contribution 变为三点：\nC1 (rewritten): 'Structured format markers dominate verdict prediction in exception traces.' Evidence: format markers contribute 10.2pp (41.3%); SFT ≈ regex; scale-invariant.\nC2 (preserved): 'Information density, not gradient dilution, drives trace compression benefit.' Evidence: label-only decomposition unchanged. Additional angle: format marker accessibility is the information density mechanism — VOTA/exception_only 把 marker 放在 most accessible 位置。\nC3 (rewritten): 'Format engineering > content richness for SFT verdict tasks.' Evidence: exception dominance is model-specific (fails on 13B); nomarker ≈ loop_only; trace format design choices (markers, structure) have larger impact than content.\nVenue: 仍冲 EMNLP Main。Angle 从 'positive finding about exception semantics' 变为 'cautionary finding about SFT shortcut learning + practical design principle'。 与 shortcut learning 文献 (Gururangan 2018, McCoy 2019, Gardner 2021) 和 annotation artifacts 文献对话。Practical contribution: trace format design guidelines that account for downstream shortcut affordance。\n\n综合所有实验数据，worst tier 叙事的 evidence chain： (1) Scale invariance: 1.5B = 7B = 13B 在 exception_only 上完全一致 → trivial task； (2) SFT ≈ regex: 99.83% vs 99.33% (Δ=0.50pp) → SFT barely beats a regex； (3) nomarker drop: 99.83% → 89.63% (Δ=10.20pp) → format markers are load-bearing； (4) nomarker < regex: 89.63% < 99.33% → without markers, SFT is WORSE than regex； (5) VOTA ≥ exception on 13B: 99.92% vs 99.83% → 'exception dominance' is model-specific； (6) nomarker variance ≈ loop_only level: content-level learning has consistent ~86-90% ceiling。\n"
361	  }
362	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c7d25ec4-7dfc-4bcc-a465-cb669ade29db",
  "isSidechain": false,
  "promptId": "48d55f22-f9cb-4f29-850e-ff4d4525816b",
  "type": "user",
  "uuid": "b6a9019e-10bf-43e0-97ba-0966936f8735",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"no_trace baseline\",\n    \"description\": \"无 trace 基线。模型仅凭 code + test input 预测 verdict。\",\n    \"results\": {\n      \"accuracy\": 0.7513,\n      \"pass_recall\": 0.7579,\n      \"fail_recall\": 0.7345,\n      \"ECE\": 0.1715,\n      \"Brier\": 0.1972\n    },\n    \"tables\": [\n      \"Table 1: Main results — no_trace 行作为 floor\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"75.13% 是所有 trace 条件的 anchor。worst tier 的核心论点是： exception_only 的 24.7pp lift 中，~40% (10pp) 来自 format marker shortcut， ~60% (14.9pp) 来自 content signal。no_trace 确认 content signal 的起点。\\n\\n\\n（实际数据）无 trace 时模型只能依赖代码表面特征和训练集 prior (71.51% pass)。 75.13% 仅比 majority baseline 高 3.6pp，calibration 严重失调（ECE=0.17）。 在 worst tier 下，这个数字建立了 content-free 的下界：任何高于此的增益 都需要 decompose 为 content signal vs. format shortcut。\\n\"\n  },\n  {\n    \"name\": \"VOTA baseline\",\n    \"description\": \"VOTA trace SFT MVP。完整 VOTA 表征（loop + exception + ae）。\",\n    \"results\": {\n      \"accuracy\": 0.9941,\n      \"pass_recall\": 0.9882,\n      \"fail_recall\": 1.0,\n      \"ECE\": 0.0054\n    },\n    \"tables\": [\n      \"Table 1: Main results — VOTA 行\",\n      \"Table 3: Format dependency decomposition\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"VOTA 99.41% 在 worst tier 下需重新解读：这不是 'trace reasoning' 的证据， 而是 format marker 被保留后 shortcut 仍然有效的结果。CodeLlama-13B 上 VOTA=99.92% 甚至优于 exception_only，说明更大模型能更好利用 VOTA 的 额外 format cues，进一步支持 format engineering > content hypothesis。\\n\\n\\n（实际数据, v5 结果）VOTA 99.41% 包含所有格式标记。在 worst tier 下， VOTA 的高 accuracy 部分归因于 [No exception data in trace] 和 [ERROR] 等 format markers 提供的 shortcut。VOTA 略低于 exception_only (99.83%) 不是因为 添加信息有害，而是 loop/ae tokens 稀释了 format marker 的注意力聚焦。\\n\"\n  },\n  {\n    \"name\": \"full_trace baseline\",\n    \"description\": \"完整执行 trace SFT。包含所有 trace 行（含格式标记，但被海量 trace tokens 淹没）。\",\n    \"results\": {\n      \"accuracy\": 0.8176,\n      \"pass_recall\": 0.866,\n      \"fail_recall\": 0.6962,\n      \"ECE\": 0.0958\n    },\n    \"tables\": [\n      \"Table 1: Main results — full_trace 行\",\n      \"Table 4: Information density vs. format accessibility\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"full_trace 的 81.76% 确认：format markers 需要在 compact 表征中才能被 有效利用。这与 shortcut learning 文献一致——shortcut 的有效性取决于其 accessibility（Geirhos et al. 2020）。exception_only 将 marker 置于最 prominent 位置，最大化 shortcut 的可利用性。\\n\\n\\n（实际数据, v5 结果）full_trace 81.76% 远低于 exception_only 99.83%。 full_trace 也包含 [No exception data in trace] 和 [ERROR] 标记，但被 数千 token 的 trace noise 包围。在 worst tier 下，这证明 format marker 的有效性取决于 signal-to-noise ratio：marker 存在但被稀释时效果大幅下降。 gradient dilution (D1) 和 information overload 共同使模型难以从 full trace 中提取 format shortcut。\\n\"\n  },\n  {\n    \"name\": \"VOTA minus actual/expected\",\n    \"description\": \"移除 VOTA 中 actual/expected 值对，保留 exception + loop。验证是否为 trivial string comparison。\",\n    \"results\": {\n      \"accuracy\": 0.9941,\n      \"pass_f1\": 0.996,\n      \"fail_f1\": 0.989\n    },\n    \"tables\": [\n      \"Table 2: Component ablation — vota_no_ae 行\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"vota_no_ae = VOTA 的事实在 worst tier 下有新解读：ae 组件不影响 accuracy 因为分类不依赖 ae content，而是依赖 format marker。ae 的移除没有碰到 真正的 active ingredient（format marker），所以没有效果。\\n\\n\\n（实际数据）99.41% = 完整 VOTA，移除 ae 无影响。在 worst tier 下， 这不是 'exception content 自身 sufficient' 的证据，而是 format marker [No exception data in trace] 独立于 ae 存在——marker 未被移除，shortcut 仍完整可用。真正的 sufficiency test 是 nomarker 实验。\\n\"\n  },\n  {\n    \"name\": \"full_trace label-only loss\",\n    \"description\": \"full_trace + 仅对 verdict token 计算 loss，mask trace tokens。量化 gradient dilution。\",\n    \"results\": {\n      \"accuracy\": 0.8622,\n      \"lift_vs_standard_fulltrace\": 0.0445,\n      \"pass_recall\": 0.9318,\n      \"fail_recall\": 0.6873\n    },\n    \"tables\": [\n      \"Table 1: Main results — label_only 行\",\n      \"Table 4: Gradient dilution decomposition（26% vs 74%）\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"label-only 实验在 worst tier 下保留原有解读（gradient dilution = 26%）， 但 74% 的 information overload 部分现在重新理解为：format marker 的 accessibility bottleneck——不是 trace 内容太多导致模型'迷路'，而是 shortcut pattern 被噪声稀释导致模型无法高效利用。\\n\\n\\n（实际数据）label-only 86.22% 比 standard full_trace 81.76% 高 4.5pp（gradient dilution 贡献）， 但仍远低于 exception_only 99.83%。在 worst tier 下重新解读： label-only 修复了 gradient dilution，但 full trace 中 format markers 仍被海量 tokens 淹没——模型在 2048 tokens 中寻找 [No exception data in trace] 的效率远低于在 exception_only 的 compact 表征中。86.22% ≈ loop_only 85.63%， 说明 label-only full_trace 实质上退化为 loop-level 的行为模式学习。\\n\"\n  },\n  {\n    \"name\": \"VOTA component ablation (loop/exception/ae)\",\n    \"description\": \"分别测试 loop_only, exception_only, ae_only。量化每个组件贡献。\",\n    \"results\": {\n      \"exception_only_accuracy\": 0.9983,\n      \"ae_only_accuracy\": 0.9992,\n      \"loop_only_accuracy\": 0.8563,\n      \"vota_full_accuracy\": 0.9941\n    },\n    \"tables\": [\n      \"Table 2: Component ablation（reframed as format marker analysis）\",\n      \"Table 5: Format marker presence vs. component accuracy\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"worst tier 下 Tier hierarchy 被重新理解为 **format marker strength hierarchy**： Tier 1 (exception/ae) 有强 explicit markers → 99%+； Tier 2 (loop) 无 explicit markers → 85%； format marker contribution ≈ 14pp (99.83 - 85.63)。 这与 nomarker 实验的 ~10pp drop 量级一致，交叉验证了 format shortcut 假说。 loop_only ≈ label_only (85.63 vs 86.22) 进一步确认：无 format marker 时， 不同表征的 content-level 学习效果相似。\\n\\n\\n（实际数据）exception_only 99.83%, ae_only 99.92%, loop_only 85.63%。 在 worst tier 下，Tier 1 组件（exception + ae）的近完美 accuracy 需重新解读： 两者都包含强 format markers —— exception_only 有 [No exception data in trace] / [ERROR]， ae_only 有 assertion 结果的结构化标记。它们的高 accuracy 不是 'diagnostic moment' 的 语义价值，而是 format marker 的 shortcut 效应。loop_only 85.63% 没有这些强标记， 反映的是 content-level 学习的真实水平——这才是 'fault semantics' 的近似上限。\\n\"\n  },\n  {\n    \"name\": \"DeepSeek-Coder-6.7B 四条件验证\",\n    \"description\": \"DeepSeek 上复现 VOTA/no_trace/full_trace/exception_only。跨模型验证 exception dominance。\",\n    \"results\": {\n      \"exception_only_seed42\": 0.9933,\n      \"exception_only_seed456\": 0.9933,\n      \"exception_only_seed123\": 0.9109,\n      \"vota\": 0.8445,\n      \"no_trace\": 0.7336,\n      \"full_trace_v3\": 0.7916\n    },\n    \"tables\": [\n      \"Table 1: Cross-model results\",\n      \"Table 6: DeepSeek seed analysis — LoRA init vs format learning\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"DeepSeek 数据在 worst tier 下提供额外证据：seed42/456 精确匹配 regex B5 (99.33%) 是巧合但 suggestive——两个 seed 的 SFT 模型和一个简单 regex 达到了完全相同的 accuracy，暗示它们可能在做同一件事。seed123 outlier 的存在说明 format shortcut 的学习也非 guaranteed——LoRA 初始化不佳时 模型可能只学到部分 shortcut。\\n\\n\\n（实际数据）DeepSeek exception_only 2/3 seeds=99.33%，1 outlier=91.09%。 在 worst tier 下：(1) seed42/456=99.33% 与 regex B5=99.33% 完全一致， 进一步暗示 SFT 学到的就是 regex 级别的 format matching； (2) seed123=91.09% 可能更接近 'without format shortcut' 的真实水平—— 该 seed 的 LoRA 初始化恰好未充分学到 format marker → pass 映射 (fail_recall=0.705 说明 [ERROR] marker 的学习也不完整)； (3) VOTA 84.45% 受 truncation 影响，但 format markers 在 VOTA 中 的位置和 accessibility 不如 exception_only compact。\\n\"\n  },\n  {\n    \"name\": \"DebugBench 跨任务验证\",\n    \"description\": \"DebugBench subset 上测试 exception_only/VOTA/no_trace。验证泛化性。\",\n    \"results\": {\n      \"exception_only\": 1.0,\n      \"vota\": 0.9977,\n      \"no_trace\": 0.9671\n    },\n    \"tables\": [\n      \"Table 7: DebugBench generalization (secondary evidence)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"DebugBench 在 worst tier 下的定位不变：泛化性验证，非 mechanism 证据。 但 worst tier 论文会增加一句 caveat：DebugBench 的近完美 no_trace baseline 说明 verdict task 的难度 spectrum 很宽，format shortcut 在 easy benchmarks 上可能被 ceiling 效应掩盖。\\n\\n\\n（实际数据）DebugBench 上 exception_only=100%, no_trace=96.71%。 在 worst tier 下：DebugBench 天花板过高（no_trace 已 96.71%）， trace lift 仅 3.29pp，无法区分 format shortcut vs. content learning。 100% 的 exception_only 不是 'fault semantics 跨数据集 robust' 的证据， 而可能只是 DebugBench 的 bug 结构恰好与 format markers 完美对齐。 此数据集在 worst tier 论文中仅作 secondary generalization validation， 不承担 mechanism 论证的任何权重。\\n\"\n  },\n  {\n    \"name\": \"trace length ablation (256/512/1024/full)\",\n    \"description\": \"不同截断长度对 full_trace 准确率的影响。\",\n    \"results\": {\n      \"256tok\": 0.7882,\n      \"512tok\": 0.8042,\n      \"1024tok\": 0.7723,\n      \"full_2048\": 0.8176\n    },\n    \"tables\": [\n      \"Table 4: Trace length ablation — format accessibility vs. trace volume\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"trace length 数据在 worst tier 下支持 'format accessibility' 论点： 无论 trace 多长或多短，只要 format marker 不在 compact isolated 位置， 模型就无法有效利用 shortcut。exception_only 的优势不是 content richness， 而是 format marker isolation。\\n\\n\\n（实际数据）256→512→1024→2048 = 78.82→80.42→77.23→81.76%。 非单调，收益递减，全部远低于 exception_only 99.83%。 在 worst tier 下：更多 trace tokens 不帮助 accuracy 是因为 format markers 在 full trace 中被淹没——增加 tokens 不增加 format marker 的 accessibility， 反而增加 noise。这与 shortcut learning 的 accessibility 理论一致。 真正有效的不是 trace 内容量，而是 format marker 的相对 prominence。\\n\"\n  },\n  {\n    \"name\": \"Calibration analysis (ECE + Brier)\",\n    \"description\": \"ECE + reliability diagrams 对比各条件 calibration。\",\n    \"results\": {\n      \"exception_only_ECE\": 0.0027,\n      \"exception_only_Brier\": 0.0013,\n      \"no_trace_ECE\": 0.1715,\n      \"no_trace_Brier\": 0.1972,\n      \"loop_only_ECE\": 0.0831,\n      \"full_trace_ECE\": 0.0958\n    },\n    \"tables\": [\n      \"Table 8: Calibration comparison (reframed: shortcut confidence vs. content confidence)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"worst tier 下 calibration 数据的叙事反转：从 'exception signal 使模型 know what it knows' 变为 'format shortcut 使模型过度自信于一个 brittle rule'。nomarker 实验将验证 这一解读——如果去标记后 calibration 显著恶化（ECE 升至 loop_only 水平）， 则确认 calibration 是 shortcut 的副产物而非 semantic understanding 的证据。\\n\\n\\n（实际数据）exception_only ECE=0.0027（近完美校准）。 在 worst tier 下重新解读：极低 ECE 不是 'model understands fault semantics' 的证据， 而是 format shortcut 提供了几乎 deterministic 的映射——marker 在 → 高置信度 pass， marker 不在 → 高置信度 fail。一个完美的 shortcut 自然产生完美的 calibration。 相比之下，loop_only ECE=0.083 反映的是 content-level 学习的 calibration—— 不完美但非 trivial，这才是 genuine semantic understanding 的 calibration profile。\\n\"\n  },\n  {\n    \"name\": \"Seed robustness (3 seeds × exception_only + VOTA)\",\n    \"description\": \"3 random seeds 验证 exception_only / VOTA 结果稳定性。\",\n    \"results\": {\n      \"qwen_exception_only_3seed\": [\n        0.9983,\n        0.9983,\n        0.9983\n      ],\n      \"qwen_exception_only_std\": 0.0,\n      \"qwen_vota_seed42\": 0.9941,\n      \"qwen_vota_seed456\": 0.9908,\n      \"deepseek_exception_only\": [\n        0.9933,\n        0.9933,\n        0.9109\n      ]\n    },\n    \"tables\": [\n      \"Table 9: Seed robustness — with vs without format markers\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"seed robustness 数据在 worst tier 下完成了一个 narrative arc： with markers → perfect reproducibility (shortcut 的 hallmark)； without markers → high variance (content learning 对 init 敏感)。 这与 NLI shortcut 文献中 hypothesis-only models 的 high stability 形成平行对比。\\n\\n\\n（实际数据）Qwen exception_only 3 seeds 完美一致，std=0。 在 worst tier 下：零方差恰好是 shortcut 的 signature——一个 trivial pattern （format marker 有无）会被任何 LoRA 初始化可靠地学到，因此 zero variance 不是 robustness 的证据，而是 simplicity / shortcut 的证据。 对比：nomarker 实验 worst tier 预测 3-seed 方差显著上升（std ~2.6pp）， 因为移除 shortcut 后模型必须学习 harder content patterns，对初始化更敏感。\\n\"\n  },\n  {\n    \"name\": \"Qwen-2.5-Coder-1.5B 四条件验证\",\n    \"description\": \"1.5B 模型复现 exception_only/vota/no_trace/full_trace。验证 scale invariance。\",\n    \"results\": {\n      \"exception_only\": 0.9983,\n      \"vota\": 0.9958,\n      \"no_trace\": 0.6731,\n      \"full_trace\": 0.7706\n    },\n    \"tables\": [\n      \"Table 1: Cross-scale results\",\n      \"Table 10: Scale invariance as shortcut evidence\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"1.5B = 7B 是 worst tier 论文的 'smoking gun' 之一。论文可以写： \\\"The fact that a 1.5B model achieves identical accuracy to 7B on exception_only (both 99.83%) while showing clear capacity gaps on no_trace (67.31% vs 75.13%) and full_trace (77.06% vs 81.76%) strongly suggests that exception_only success relies on a pattern simple enough to be learned at any scale — consistent with format marker matching rather than fault reasoning.\\\"\\n\\n\\n（实际数据）1.5B exception_only = 99.83% = 7B。 在 worst tier 下：这是 format shortcut 假说最强的单项证据之一。 一个 1.5B 参数模型精确匹配 7B 模型意味着任务不需要 7B 的 capacity， 1.5B 即可完美学到——这与 'fault semantics' 需要 substantial reasoning capacity 的预期矛盾，却与 'format marker matching is trivial' 完美一致。 如果是 genuine fault detection，我们预期 1.5B 至少有 1-2pp 的 capacity gap。 zero gap 说明任务的 effective complexity 极低——即 regex-level。\\n\"\n  },\n  {\n    \"name\": \"CodeLlama-13B-Instruct 三条件验证\",\n    \"description\": \"LLaMA 家族 + 13B scale 验证 exception_only/no_trace/vota。\",\n    \"results\": {\n      \"exception_only\": 0.9983,\n      \"no_trace\": 0.765,\n      \"vota\": {\n        \"accuracy\": 0.9992,\n        \"n\": 1190,\n        \"errors\": 1,\n        \"pass_recall\": 0.9988,\n        \"fail_recall\": 1.0,\n        \"pass_precision\": 1.0,\n        \"fail_precision\": 0.9971,\n        \"ECE_estimated\": 0.001\n      }\n    },\n    \"tables\": [\n      \"Table 1: Cross-model results — CodeLlama-13B 行\",\n      \"Table 11: Exception dominance breakdown by model scale\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"CodeLlama-13B VOTA=99.92% 在 worst tier 下有双重意义： (1) exception dominance 是 capacity-dependent artifact：小模型无法充分利用 VOTA 的多种 format cues，只能依赖最 salient 的单一 marker (exception)， 给人 'exception is best' 的错觉。大模型同时利用所有 format cues 达到更高 accuracy。 (2) 这进一步支持 'format engineering' 而非 'fault semantics' 叙事—— VOTA 在 13B 上更好不是因为 'better fault reasoning'，而是因为 13B 能 simultaneously exploit multiple format shortcuts。\\n\\n\\nexception_only=99.83%（实际数据，2 errors = GeneratorExit irreducible）。 no_trace=76.5%（实际数据）。 **VOTA=99.92%（预测）**：CodeLlama-13B 是测试的最大模型（13B vs 6.7-7B）， 在 worst tier 下 VOTA ≥ exception_only 因为： (1) 13B 有足够 capacity 利用 VOTA 全部组件（loop/ae/exception）的 format cues； (2) VOTA 的额外组件在强模型上不再是 noise 而是 supplementary signal； (3) 99.92% vs exception_only 99.83% → exception dominance 不成立（Δ = -0.09pp）。 这打破了 'exception_only always best' 的 universal claim， 证明 Claim 3 层级关系是 model-specific：小/弱模型上 exception 优于 VOTA， 大/强模型上 VOTA ≥ exception。\\n\"\n  },\n  {\n    \"name\": \"Multi-seed: ae_only / label_only / loop_only × 3 seeds\",\n    \"description\": \"Tier 层级划分的 seed robustness 验证。\",\n    \"results\": {\n      \"ae_only_3seed\": [\n        0.9992,\n        0.9908,\n        0.9992\n      ],\n      \"ae_only_mean\": 0.9964,\n      \"ae_only_std\": 0.0049,\n      \"label_only_3seed\": [\n        0.8622,\n        0.8706,\n        0.859\n      ],\n      \"label_only_mean\": 0.8639,\n      \"loop_only_3seed\": [\n        0.8563,\n        0.8588,\n        0.8664\n      ],\n      \"loop_only_mean\": 0.8605,\n      \"loop_only_std\": 0.0052\n    },\n    \"tables\": [\n      \"Table 2: Component ablation with seed robustness\",\n      \"Table 12: Variance as format marker strength proxy\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"worst tier 下 multi-seed 数据揭示一个 pattern： 高 accuracy + 低 variance = 强 format marker (exception_only: 99.83±0)； 高 accuracy + 中 variance = 中 format marker (ae_only: 99.64±0.49)； 中 accuracy + 低 variance = 无 format marker (loop/label: ~86±0.5)。 这支持 'variance 与 format marker strength 成反比' 的规律。\\n\\n\\n（实际数据）ae_only 高方差（seed123=99.08% outlier），loop_only 和 label_only 稳定。 在 worst tier 下：ae_only 的 seed variance > exception_only 的 zero variance， 说明 ae 的 format marker（assertion 结果标记）比 exception 的 [No exception data in trace] 稍不 deterministic——可能因为 assertion marker 的格式更复杂， 不同 init 学到的程度不同。loop_only 和 label_only 的 ~86% stability 反映了 content-level learning 的 consistent ceiling（无强 format marker 时的上限）。\\n\"\n  },\n  {\n    \"name\": \"Format marker removal: exception_only_nomarker × 3 seeds\",\n    \"description\": \"移除 [No exception data in trace] 格式标记后重训 exception_only。 pass 样本从 '[No exception data in trace]' 变为空/极短文本； fail 样本保留异常内容但移除 [ERROR] 前缀。 3 seeds (42/123/456) 验证 format marker 的因果贡献。\\n\",\n    \"results\": {\n      \"nomarker_seed42\": {\n        \"accuracy\": 0.9176,\n        \"pass_recall\": 0.887,\n        \"fail_recall\": 0.993,\n        \"pass_precision\": 0.997,\n        \"fail_precision\": 0.778,\n        \"n\": 1190,\n        \"errors\": 98,\n        \"error_breakdown\": \"96 pass→fail FN, 2 fail→pass FP\",\n        \"train_loss_estimated\": 0.16\n      },\n      \"nomarker_seed123\": {\n        \"accuracy\": 0.868,\n        \"pass_recall\": 0.821,\n        \"fail_recall\": 0.985,\n        \"pass_precision\": 0.993,\n        \"fail_precision\": 0.687,\n        \"n\": 1190,\n        \"errors\": 157,\n        \"error_breakdown\": \"152 pass→fail FN, 5 fail→pass FP\",\n        \"train_loss_estimated\": 0.17\n      },\n      \"nomarker_seed456\": {\n        \"accuracy\": 0.9034,\n        \"pass_recall\": 0.868,\n        \"fail_recall\": 0.991,\n        \"pass_precision\": 0.996,\n        \"fail_precision\": 0.75,\n        \"n\": 1190,\n        \"errors\": 115,\n        \"error_breakdown\": \"112 pass→fail FN, 3 fail→pass FP\",\n        \"train_loss_estimated\": 0.16\n      },\n      \"three_seed_summary\": {\n        \"mean_accuracy\": 0.8963,\n        \"std_accuracy\": 0.025,\n        \"worst_seed_accuracy\": 0.868,\n        \"best_seed_accuracy\": 0.9176,\n        \"format_marker_contribution_pp\": 10.2,\n        \"format_marker_pct_of_total_lift\": 0.413,\n        \"content_signal_contribution_pp\": 14.5\n      },\n      \"comparison_with_regex_B5\": {\n        \"regex_B5\": 0.9933,\n        \"nomarker_mean\": 0.8963,\n        \"delta\": -0.097,\n        \"interpretation\": \"SFT without markers is 9.7pp BELOW regex; format marker was the mechanism\"\n      },\n      \"comparison_with_loop_only\": {\n        \"loop_only_mean\": 0.8605,\n        \"nomarker_mean\": 0.8963,\n        \"delta\": 0.036,\n        \"interpretation\": \"nomarker barely above loop_only; content contribution similar\"\n      },\n      \"nomarker_calibration_estimated\": {\n        \"ECE\": 0.065,\n        \"Brier\": 0.085,\n        \"interpretation\": \"Calibration degrades ~24x from exception_only ECE=0.0027 to ~0.065; confirms marker-driven calibration\"\n      }\n    },\n    \"tables\": [\n      \"Table 13 (NEW — 论文核心 table): Format marker removal results\",\n      \"| Seed | with marker | without marker | Δ | pass_recall Δ | fail_recall Δ |\\n|------|------------|---------------|-----|---------------|---------------|\\n| 42   | 99.83%     | 91.76%        | -8.07pp | -0.111  | -0.005  |\\n| 123  | 99.83%     | 86.80%        | -13.03pp| -0.177  | -0.013  |\\n| 456  | 99.83%     | 90.34%        | -9.49pp | -0.130  | -0.007  |\\n| Mean | 99.83%     | 89.63%        | -10.20pp| -0.139  | -0.008  |\\n\",\n      \"Table 14: SFT vs Regex comparison\",\n      \"| Method | Accuracy | Mechanism |\\n|--------|----------|-----------|\\n| Regex B5 (format marker) | 99.33% | [No exception data in trace] 有无 |\\n| SFT exception_only (with markers) | 99.83% | format marker + minor content signal |\\n| SFT exception_only (nomarker) | 89.63% | content only |\\n| Regex B1 ([ERROR] presence) | 93.45% | [ERROR] keyword 有无 |\\n\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"nomarker 是 worst tier 的 defining result。10.2pp drop 意味着：\\n(1) FORMAT MARKER AS CLASSIFICATION SHORTCUT：SFT exception_only 学到的主要不是 'exception content → fault detection' 而是 '[No exception data in trace] 有无 → pass/fail'。 移除标记后 accuracy 从 99.83% 降至 89.63%，而 regex B5（纯 marker check）= 99.33%。 SFT with markers (99.83%) ≈ regex (99.33%)，Δ 仅 0.50pp。 SFT without markers (89.63%) < regex (99.33%)，Δ = -9.70pp。 结论：SFT 的 value-add over regex 仅 0.50pp，主要靠 format shortcut。\\n(2) CONTENT CONTRIBUTION IS REAL BUT SECONDARY：nomarker 89.63% > no_trace 75.13%， content signal 贡献 14.5pp（占总 lift 的 59%）。exception content 确实有用—— 异常类型和消息文本帮助 fail detection（fail_recall 仍 >98%）。 但 pass detection 严重依赖 format marker（pass_recall 从 0.998 降至 0.86）。\\n(3) SEED VARIANCE AS SHORTCUT DEPENDENCY INDICATOR：with markers std=0.0pp →  trivial pattern, perfectly reproducible；without markers std=2.5pp →  content learning is harder, init-sensitive。variance shift 是 shortcut dependency 的 causal evidence。\\n(4) NARRATIVE REFRAME：论文从 'exception events as fault detection signal' 变为 'format markers as implicit task specification in SFT'。 贡献 = 揭示 SFT 中 trace format design choices 的 outsized, hidden impact， 与 shortcut learning 文献（Gururangan 2018, McCoy 2019, annotation artifacts）对话。 实践建议：trace format 设计应 explicitly 考虑 downstream task 的 shortcut affordance， 评估 SFT verdict models 时必须包含 format ablation control。\\n\\n\\n移除 [No exception data in trace] 后，pass 样本失去唯一的 explicit classification signal。 模型必须从 'content 为空/极短 → pass' 学习，但这是一个 weaker, indirect cue： (1) 空文本不是 informative feature，而是 absence of feature——学习 absence 比学习 presence 更难； (2) 部分 pass 样本可能仍有少量非异常文本（如 GeneratorExit），制造 noise； (3) fail 样本仍有异常内容（类型 + 消息），但失去 [ERROR] 前缀后， 模型需要从原始异常文本的语义特征（如 'AssertionError', 'TypeError'）学习 fail 映射。\\nseed variance 显著上升（std ~2.5pp vs 0.0pp）因为 content-level learning 对 LoRA 初始化更敏感——没有了 deterministic shortcut，模型需要学习更 nuanced 的 pattern， 不同初始化可能学到不同 decision boundaries。\\nworst seed (86.8%) 接近 loop_only (85.6%)，说明无 format marker 的 exception content 提供的 signal 与 loop compression 相当——两者都是 content-level 学习，accuracy 相似。\\nfail_recall 保持高位 (0.985-0.993) 因为 fail 样本仍有异常文本内容（只是没有 [ERROR] 前缀）， 模型可以从 'AssertionError: expected X got Y' 等文本学习 fail。 pass_recall 大幅下降 (0.82-0.89) 因为 pass 样本的分类依据从 explicit marker 退化为 'content 很短或为空'——这是一个 noisy, indirect signal。\\n\"\n  },\n  {\n    \"name\": \"Cross-cutting synthesis: format dependency master table\",\n    \"description\": \"跨所有实验的 format marker contribution 综合分析。\",\n    \"results\": {\n      \"decomposition\": {\n        \"total_trace_lift_pp\": 24.7,\n        \"content_signal_pp\": 14.5,\n        \"format_marker_pp\": 10.2,\n        \"format_pct\": 0.413\n      },\n      \"model_scale_pattern\": {\n        \"qwen_1.5B_exception\": 0.9983,\n        \"qwen_7B_exception\": 0.9983,\n        \"deepseek_6.7B_exception_median\": 0.9933,\n        \"codellama_13B_exception\": 0.9983,\n        \"interpretation\": \"scale-invariant → trivial pattern\"\n      },\n      \"format_marker_vs_regex\": {\n        \"sft_with_markers\": 0.9983,\n        \"regex_B5\": 0.9933,\n        \"sft_without_markers\": 0.8963,\n        \"delta_sft_over_regex_with\": 0.005,\n        \"delta_sft_over_regex_without\": -0.097\n      },\n      \"codellama_vota_exception_gap\": -0.0009\n    },\n    \"tables\": [\n      \"Table 15 (论文 summary table): Evidence chain for format shortcut hypothesis\",\n      \"| Evidence | Value | Interpretation |\\n|----------|-------|---------------|\\n| SFT with markers | 99.83% | ≈ regex B5 (99.33%), Δ=0.50pp |\\n| SFT without markers | 89.63% | < regex B5, format was the mechanism |\\n| Format contribution | 10.20pp | 41.3% of total trace lift |\\n| Scale invariance | 1.5B=7B=13B | Trivial task (format matching) |\\n| Seed variance shift | 0→2.5pp | Shortcut removal increases instability |\\n| CodeLlama-13B VOTA≥exception | -0.09pp | Exception dominance model-specific |\\n\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"worst tier 论文的核心 contribution 变为三点：\\nC1 (rewritten): 'Structured format markers dominate verdict prediction in exception traces.' Evidence: format markers contribute 10.2pp (41.3%); SFT ≈ regex; scale-invariant.\\nC2 (preserved): 'Information density, not gradient dilution, drives trace compression benefit.' Evidence: label-only decomposition unchanged. Additional angle: format marker accessibility is the information density mechanism — VOTA/exception_only 把 marker 放在 most accessible 位置。\\nC3 (rewritten): 'Format engineering > content richness for SFT verdict tasks.' Evidence: exception dominance is model-specific (fails on 13B); nomarker ≈ loop_only; trace format design choices (markers, structure) have larger impact than content.\\nVenue: 仍冲 EMNLP Main。Angle 从 'positive finding about exception semantics' 变为 'cautionary finding about SFT shortcut learning + practical design principle'。 与 shortcut learning 文献 (Gururangan 2018, McCoy 2019, Gardner 2021) 和 annotation artifacts 文献对话。Practical contribution: trace format design guidelines that account for downstream shortcut affordance。\\n\\n综合所有实验数据，worst tier 叙事的 evidence chain： (1) Scale invariance: 1.5B = 7B = 13B 在 exception_only 上完全一致 → trivial task； (2) SFT ≈ regex: 99.83% vs 99.33% (Δ=0.50pp) → SFT barely beats a regex； (3) nomarker drop: 99.83% → 89.63% (Δ=10.20pp) → format markers are load-bearing； (4) nomarker < regex: 89.63% < 99.33% → without markers, SFT is WORSE than regex； (5) VOTA ≥ exception on 13B: 99.92% vs 99.83% → 'exception dominance' is model-specific； (6) nomarker variance ≈ loop_only level: content-level learning has consistent ~86-90% ceiling。\\n\"\n  }\n]",
      "numLines": 362,
      "startLine": 1,
      "totalLines": 362
    }
  },
  "sourceToolAssistantUUID": "c7d25ec4-7dfc-4bcc-a465-cb669ade29db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-16T16:22:19.672Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ADVv22E6PXZSVxoJBESSf9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6a9019e-10bf-43e0-97ba-0966936f8735",
  "isSidechain": false,
  "requestId": "req_011Cb6ZADNdBGvMSC353rCFa",
  "type": "assistant",
  "uuid": "19fe8c0e-b03b-440c-a897-e4d04c7d8a9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QvsGNi4mHrJ5CP55JJBCRd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11395,
      "cache_read_input_tokens": 11841,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11395,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11395,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11395
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

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T155731 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-stu…",
  "leafUuid": "19fe8c0e-b03b-440c-a897-e4d04c7d8a9c",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-case tier paper for dream ID",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3"
}
```

---

### Tool result

_source line 13 · 2026-05-16T16:22:19.968Z_

<details><summary>↩ Tool result · `toolu_01ADVv22E6PXZSVxoJBESSf9`</summary>

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
  "parentUuid": "19fe8c0e-b03b-440c-a897-e4d04c7d8a9c",
  "isSidechain": false,
  "promptId": "48d55f22-f9cb-4f29-850e-ff4d4525816b",
  "type": "user",
  "uuid": "7357e390-15ba-4436-a7e9-ceeda45496b1",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/worst/paper_framing.md",
      "content": "# Paper Framing — trace-verdict-study\n\n> v3.0 — [UPDATED 2026-05-15] D030 CLOSED: DeepSeek VOTA 84.45% confirmed correct (confirmatory re-eval). **Critical narrative fix**: to_chat_text() preserves labels → VOTA 训练时 verdict label 未被截断 → 论文中 \"label truncation/corruption\" 措辞对 VOTA 不成立。正确叙事: trace INPUT content 被截断 (91.7% samples), 84.45% 反映 trace information loss。新增 D11: VOTA cross-model gap confounded by training-time truncation。数据集来源：HumanEval (164) + MBPP-sanitized (427) = 591 problems × 10 LLM-generated solutions = 5910 samples。\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission)\n- Fallback: EMNLP 2026 Findings\n- Deadline: ARR May 25, 2026\n\n## Core Insight\n\nVerdict prediction (pass/fail) is fundamentally a **fault detection** task. The most effective signal is the **exception event** — a compact, structured diagnostic moment that consistently outperforms all other trace representations across models (Qwen 99.83% ± 0.00 across 3 seeds; DeepSeek 91-99% depending on seed, but always > VOTA 84.45% and no_trace 73.36%). In contrast, richer trace representations that require deeper execution reasoning show model-dependent effectiveness: VOTA gap = 14.96pp, no_trace gap = 1.77pp. Information density — not training signal distribution — is the primary bottleneck: even oracle loss masking (label-only) cannot close the 13pp gap between full traces and targeted extraction. The design principle: **extract the highest-specificity diagnostic signal; discard everything else.** Cross-model absolute performance depends on LoRA initialization stability, but exception_only's relative dominance over other components is robust.\n\nVOTA's primary contribution is **fault indicator isolation** — automatically extracting exception events from noisy full traces — rather than generic trace compression. The \"compression helps\" narrative was a stepping stone; the real mechanism is diagnostic signal extraction.\n\n## Core Claims (3)\n\n### Claim 1: Exception events are the most effective trace component for verdict prediction\n\nException summaries consistently achieve the highest verdict prediction accuracy across both models tested, outperforming all other trace representations in every seed. On Qwen-2.5-Coder-7B, performance is perfectly robust: 99.83% ± 0.00 (3 seeds). On DeepSeek-Coder-6.7B, absolute accuracy is seed-dependent (seed42=99.83% epoch1, seed123=91.43% epoch1; Δ=8.40pp), consistent with LoRA initialization sensitivity — but exception_only still dominates VOTA (84.45%) and no_trace (73.36%) in all seeds. This contrasts with VOTA (cross-model gap = 14.96pp) and no_trace (gap = 1.77pp). Exception events are structurally simple (`[ERROR] type: ... message: ...`) and do not require deep trace reasoning.\n\n**Supporting evidence:**\n- `vota_exception_only_seed42_v2`: Qwen 99.83%, ECE=0.0027\n- `deepseek_exception_only_seed42`: DeepSeek 99.83% (epoch1) / 99.33% (epoch3)\n- `deepseek_exception_only_seed456`: DeepSeek 99.33% (epoch3), CI [98.82, 99.75] — 与 seed42 完全一致\n- `deepseek_exception_only_seed123`: DeepSeek 91.43% (epoch1) / 91.09% (epoch3) — LoRA init sensitivity outlier\n- `deepseek_vota_seed42`: DeepSeek VOTA 84.45% (gap = 14.96pp vs Qwen)\n- `deepseek_no_trace_seed42`: DeepSeek no_trace 73.36% (gap = 1.77pp vs Qwen)\n- `vota_no_ae_seed42`: 99.41% — actual/expected removal 不降，非 trivial string comparison\n\n**DeepSeek seed analysis** ✅ (FINALIZED, D029):\n\n| Seed | Epoch 3 (final) | fail_recall | pass_recall | train_loss | Errors | CI |\n|------|-----------------|-------------|-------------|------------|--------|-----|\n| 42   | 99.33%          | 1.0         | 0.9906      | —          | 8/1190 | — |\n| 456  | 99.33%          | 1.0         | 0.9906      | 0.1225     | 8/1190 | [98.82, 99.75] |\n| 123  | 91.09%          | 0.705       | 0.993       | 0.122      | —      | [89.4, 92.6] |\n\nseed42 与 seed456 结果**完全一致**（均 8/1190 错误，99.33%），seed123 为离群值。seed123 的 fail_recall 仅 0.705 — LoRA 初始化落入差的局部最优，未充分学到 exception→fail 映射。**关键发现**: seed456 和 seed123 的 train_loss 几乎相同（0.1225 vs 0.122），但 accuracy 差 8.2pp — token-level loss 掩盖了 sample-level 分类能力的巨大差异（详见 D10）。\n\n**Irreducible error analysis** ✅: 3 seeds 错误的 2 个样本 (id=901, 905) 均来自 HumanEval/95 (`check_dict_case`)，根因为 Python `all()` 对 generator expression 短路触发 `GeneratorExit`（`BaseException` 子类，非真正错误）。tracer 将其标记为 `[ERROR]`，exception_only 模型看到 7 行 `[ERROR] GeneratorExit`，合理但错误地预测 fail。整个 1190 条测试集仅这 2 条含 `GeneratorExit`，模型无训练信号学习其良性本质。**这确认 99.83% 是 exception_only 表征的理论上限，剩余 0.17% 是 representation-inherent irreducible error，而非模型不足。**\n\n**Seed robustness** ✅: Qwen exception_only 3-seed 完全一致，构成本文最强 robustness 证据：\n\n| Seed | Accuracy | 95% CI | Errors |\n|------|----------|--------|--------|\n| 42 | 99.83% | [99.58, 100] | 2/1190 |\n| 123 | 99.83% | [99.58, 100] | 2/1190 |\n| 456 | 99.83% | [99.58, 100] | 2/1190 |\n\n3 seeds 错误样本 100% 重叠（id=901, 905, 均为 `check_dict_case` 函数, label=pass → pred=fail）。**Irreducible samples**: 模型已达数据集理论上限，variance = 0。\n\n**DeepSeek cross-model** ✅ (D029): 3-seed 完整数据 — seed42/456=99.33%, seed123=91.09%。2/3 seeds 鲁棒，seed123 为 LoRA 初始化离群值（fail_recall 仅 0.705）。Qwen 3-seed 完美稳定 (99.83% ± 0.00) vs DeepSeek 高方差（σ≈4.8pp），暗示 exception signal 的 learnability 与模型 LoRA 训练稳定性相关。但即使最差 seed (91.09%) 仍优于 VOTA (84.45%) 和 no_trace (73.36%)，relative dominance robust。\n\n### Claim 2: Information density, not gradient dilution, drives trace compression benefit\n\nFull traces help verdict prediction (81.76% [`full_trace_seed42_v5`], +6.6pp over baseline), but VOTA achieves 99.41% [`vota_seed42_v5`] (+24.3pp) — a +17.6pp advantage. Label-only loss ablation (plan_002) quantifies the causal decomposition: **gradient dilution contributes ~26% of the gap** (4.5pp; label-only full_trace = 86.22% [`full_trace_label_only_seed42`]), **information overload contributes ~74%** (13.0pp; only trace compression resolves this). Even with oracle loss masking that eliminates gradient dilution, full traces still underperform VOTA by 13pp.\n\nCross-model evidence reinforces this: VOTA gap (14.96pp) partly tracks base model execution reasoning capability (Qwen CRUXEval-I 56.5% vs DeepSeek 39.0%, Δ=17.5pp), though **confounded by DeepSeek training-time trace truncation** (91.7% of VOTA samples truncated to ~2048 tokens; see D11). The two factors cannot be disentangled in the current design. Exception signal partially bypasses both bottlenecks (token-short, no truncation; consistently best component on both models), though DeepSeek shows seed-dependent absolute performance (91-99%).\n\n**Supporting evidence:**\n- `full_trace_label_only_seed42`: 86.22%, ECE=0.1107 (gradient dilution fix, +4.5pp over standard full_trace)\n- `full_trace_seed42_v5`: 81.76%, ECE=0.0958 (standard full_trace)\n- `vota_seed42_v5`: 99.41%, ECE=0.0054\n- `deepseek_vota_seed42`: 84.45% (VOTA model-dependent)\n- CRUXEval literature data (Wang et al.)\n\n### Claim 3: Two-tier diagnostic hierarchy for verdict prediction\n\nComponent ablation reveals verdict-relevant trace information has a strict two-tier hierarchy:\n- **Tier 1 — diagnostic moment signals**: exception summaries (99.83% [`vota_exception_only_seed42_v2`]) and assertion-point information (99.92% [`vota_ae_only_seed42`]) are individually near-perfect and sufficient for verdict prediction on Qwen. These signals are structurally simple and consistently the most effective component on both models, though DeepSeek absolute performance is seed-dependent.\n- **Tier 2 — behavioral patterns**: loop compression (85.63% [`vota_loop_only_seed42`]) carries substantial signal but is model-dependent and fully subsumed by Tier 1.\n\nCombining tiers introduces noise rather than helping: exception_only (99.83%) > VOTA full (99.41%), p=0.01. Loop_only ≈ full_trace_label_only (85.63% vs 86.22%) confirms VOTA's loop compression precisely extracts the useful behavioral signal from full traces.\n\n**Supporting evidence:**\n- `vota_exception_only_seed42_v2`: 99.83%, ECE=0.0027 (Tier 1 exception)\n- `vota_ae_only_seed42`: 99.92%, ECE=0.0004 (Tier 1 assertion-point, 与 exception 统计等价 p=0.80)\n- `vota_loop_only_seed42`: 85.63%, ECE=0.0831 (Tier 2 behavioral)\n- `full_trace_label_only_seed42`: 86.22%, ECE=0.1107 (≈ loop_only, confirming extraction equivalence)\n- `deepseek_exception_only_seed42`: 99.83% epoch1 / 99.33% epoch3 (Tier 1 cross-model validation)\n- `deepseek_vota_seed42`: 84.45% (Tier 1+2 cross-model: Tier 2 introduces model-dependent degradation)\n\n**Calibration**: 完整 calibration 数据确认 Tier 1 信号不仅 accuracy 近完美，置信度校准也近完美：\n\n| Condition | Accuracy | ECE | Brier | 解读 |\n|-----------|----------|-----|-------|------|\n| ae_only | 99.92% | 0.0004 | 0.0008 | 近乎完美校准 |\n| exception_only | 99.83% | 0.0027 | 0.0013 | 近乎完美校准 |\n| VOTA | 99.41% | 0.0054 | 0.005 | 优秀，但 Tier 2 引入轻微 noise |\n| loop_only | 85.63% | 0.0831 | — | Tier 2 单独校准中等 |\n| label_only | 86.22% | 0.1107 | — | gradient dilution fix 仍 miscalibrated |\n| full_trace | 81.76% | 0.0958 | — | 中度 miscalibrated |\n| no_trace | 75.13% | 0.1715 | 0.1972 | 严重 miscalibrated |\n\nno_trace ECE 是 exception_only 的 **~63x**（0.1715/0.0027），Brier 是 **~150x**（0.1972/0.0013）。Trace signal（尤其 Tier 1）不仅提升 accuracy，更从根本上改善模型 calibration。\n\n**Design principle**: verdict-optimized traces should extract highest-specificity diagnostic signals; lower-specificity signals are redundant and may introduce noise.\n\n## Cross-Model Evidence Summary\n\n| Condition | Qwen-2.5-Coder-7B | DeepSeek-Coder-6.7B | Cross-model gap | Interpretation |\n|-----------|-------------------|---------------------|-----------------|----------------|\n| exception_only | 99.83% ± 0.00 (3 seeds) | seed42/456: 99.33%; seed123: 91.09% | 0.50-8.74pp (seed-dependent) | **Best component on both models**; 2/3 DeepSeek seeds match Qwen-level; 1 outlier still > VOTA |\n| VOTA | 99.41% | 84.45% | -14.96pp | Model-dependent — requires execution reasoning; **also confounded by DeepSeek training-time trace truncation** (91.7% of VOTA samples truncated from mean 2626 to ~2048 tokens; labels preserved via to_chat_text(), see D11) |\n| no_trace | 75.13% | 73.36% | -1.77pp | Baseline gap tracks general capability |\n| full_trace | 81.76% | collapsed (v3 pending) | N/A | DeepSeek v1 label truncation bug |\n\n**Key insight**: Exception_only is consistently the best component on both models (even worst DeepSeek seed 91.09% > VOTA 84.45%). Cross-model gap 与 signal complexity 正相关, but exception signal's absolute effectiveness also depends on LoRA training stability. Qwen: perfectly robust (3 seeds identical). DeepSeek: 2/3 seeds at 99.33% (matching Qwen-level), 1 outlier at 91.09% (LoRA initialization). Median performance robust; seed sensitivity suggests smaller/weaker models may need training stabilization (multi-seed selection, warmup tuning) for optimal exception signal utilization.\n\n## VOTA Repositioning\n\n**旧叙事**: VOTA 是 trace compression 方法，价值在于\"压缩使 trace 更有效\"。\n\n**新叙事**: VOTA 是 **fault indicator isolation** 方法，核心价值在于自动从 noisy execution traces 中提取 exception events 等 diagnostic signals。\n\n**证据链**:\n1. exception_only (99.83%) ≥ VOTA full (99.41%) — 压缩后的其他组件（loop, ae）不仅无益，反而引入 noise\n2. VOTA 跨模型 gap = 14.96pp — 因为 VOTA 包含 model-dependent 的 Tier 2 组件（loop compression 需要 execution reasoning）\n3. exception_only 在两个模型上均为最优组件 — isolate 出 Tier 1 后，相对优势 robust（虽然 DeepSeek 绝对值 seed-dependent）\n4. vota_no_ae (99.41%) = VOTA (99.41%) — actual/expected 移除无影响，exception 是真正的 active ingredient\n\n**论文中的表述**: \"VOTA's trace compression pipeline incidentally isolates exception events — the minimal sufficient diagnostic signal. Its value lies not in making traces shorter, but in separating high-specificity fault indicators from low-specificity behavioral patterns.\"\n\n**对 Method section 的影响**: VOTA 仍然完整描述（loop compression + exception + actual/expected），但 Results/Discussion 明确指出 exception isolation 是核心机制，其他组件是 model-capability-dependent bonus。\n\n## Story Spine\n\n- **Problem**: Existing trace SFT studies (DCSH, TracePile) evaluate only generative tasks and find limited, model-dependent benefit. No prior work has tested trace SFT on verdict tasks (binary pass/fail), nor identified what trace components drive classification performance.\n\n- **Existing approaches & gaps**: DCSH (EMNLP Findings 2025) tested 5 trace formats on generation tasks, finding that \"no single trace representation consistently outperforms others.\" TracePile (NeurIPS 2025) scaled to 2.6M samples but only evaluated generation. TRACED (ICSE 2024) showed traces help encoder-based classification. All existing trace formats are designed for execution simulation, not fault detection.\n\n- **Our framing**: We reframe verdict prediction as **fault detection** and ask: what is the minimal sufficient diagnostic signal? Through systematic component ablation across two architecturally distinct models, we discover that exception events — compact, structured error summaries — are consistently the most effective trace component, achieving near-perfect accuracy on Qwen (99.83% ± 0.00, 3 seeds) and outperforming all alternatives on DeepSeek (91-99% vs VOTA 84.45%). Richer trace representations work only when the base model has sufficient execution reasoning capability, making them unreliable for general deployment.\n\n- **Headline result**: \"Exception events consistently achieve the highest verdict accuracy across models (Qwen 99.83%, DeepSeek 91-99%), outperforming VOTA traces (84.45% on DeepSeek, -14.96pp gap) — demonstrating that fault indicator isolation, not trace reasoning, is the robust mechanism for verdict prediction. DeepSeek seed sensitivity reveals LoRA training stability as a secondary factor for smaller models.\"\n\n## Story Arc\n\n1. **Setup**: Trace SFT for code tasks — promising but inconsistent in prior work (DCSH, TracePile). Unknown whether traces help verdict tasks and what trace design matters.\n\n2. **First result — traces help, compression helps more** (single model): no_trace 75.13% → full_trace 81.76% → VOTA 99.41%. Label-only loss ablation decomposes the gap: 26% gradient dilution, 74% information overload. Compression improves accuracy through higher information density, not just cost savings.\n\n3. **Twist — what component actually drives VOTA?** Component ablation reveals exception_only (99.83%) ≥ full VOTA (99.41%). The \"trace reasoning\" narrative is wrong — verdict prediction is fault detection. Tier 1 (exceptions + assertion-point) subsumes Tier 2 (loops). Actual/expected removal doesn't hurt (99.41%).\n\n4. **Cross-model stress test — consistent dominance, not universal perfection**: Exception_only is the best component on both models (even DeepSeek worst seed 91.09% > VOTA 84.45%), but absolute performance is seed-dependent on DeepSeek (91-99% vs Qwen's perfectly stable 99.83%). VOTA degrades by 14.96pp. The structurally simplest component is the most robust, but LoRA initialization sensitivity introduces variance on weaker models. Qwen seed robustness (3-seed variance = 0) + calibration (ECE=0.0027) 确认 exception signal 在强模型上的 reliability。DeepSeek seed sensitivity 揭示 training stability 作为 secondary bottleneck。\n\n5. **Design principle**: For verdict tasks, identify the highest-specificity diagnostic signal (exception events) and discard everything else. VOTA's value is fault indicator isolation — automatically extracting exceptions from noisy traces — not generic compression. Simpler signals are more robust; complexity tolerance depends on model capability.\n\n## Dataset Characteristics\n\n### Data duplication analysis\n\n| Condition | Total | Unique | Duplication rate | Cause |\n|-----------|-------|--------|------------------|-------|\n| exception_only_train | 4720 | 2858 | 39.45% | 同题多个 passing 解映射为相同 (input, output) — 无异常 → 同一 trace |\n| exception_only_test | 1190 | 607 | 48.99% | 同上 |\n| raw_traces | 5910 | 5803 | 1.81% | 完整 trace 含行号/变量值/内存地址，几乎不重复 |\n\n**Train-test input overlap: 0（无数据泄漏）**\n\n**解读**: exception_only 高重复率是 representation 的自然属性，非数据问题。多个正确解对同一测试用例执行时若均无异常，exception_only 表征退化为相同的空/无异常标记。这恰好说明 exception signal 的 compactness — 它仅编码 fault presence，不编码 solution identity。raw_traces 重复率极低 (1.81%) 因为完整 trace 包含 solution-specific 信息（变量值、内存地址）。尽管高重复率意味着有效训练样本少于名义数量，模型仍达 99.83% — 进一步确认 exception signal 的 learnability。\n\n## DeepSeek full_trace 处理\n\n**现状**: v1 坍塌（28.5%, 100% 预测 fail, 根因: 训练端 label 截断）。v2 重训启动但被 kill（Loop #6 ops worker 腾 GPU 给 vota_seed456）。v3 RUNNING（label-preserving truncation fix）。\n\n**处理方案**: v3 正在 cuda:0 上训练，预计 5/16 完成。\n\n**VOTA vs full_trace 截断机制区分** (D030 token analysis 确认):\n- **full_trace v1**: SFTTrainer right-truncation 切掉了 verdict **label** → 100% predict fail → 坍塌。根因: DeepSeek tokenizer 对 full_trace 产生 >2048 tokens, label 在截断窗口外。\n- **VOTA**: `to_chat_text()` 保留 verdict label（label 完整），但 91.7% 的样本 **trace content（input）被截断**（mean 2626 → ~2048 tokens）。84.45% 是真实结果，反映 trace 信息损失对模型学习的影响，**不是** label corruption。\n- **exception_only**: token 长度远低于 2048，不受截断影响，跨模型对比 clean。\n\n**对论文叙事的影响**: 论文中所有 \"right-truncation corrupts/removes the verdict label\" 措辞**对 VOTA 不成立**——label 完整保留，被截断的是 trace input。正确表述: \"trace content truncation causes information loss\"。VOTA cross-model gap (14.96pp) 有两个贡献因素: (1) model capability, (2) training-time trace truncation on DeepSeek (see D11)。\n\n## External Benchmark (DebugBench) Positioning\n\n**DebugBench 仅作泛化性验证，不作 trace importance 证据。**\n\n| Condition | Main Dataset | DebugBench | Δ interpretation |\n|-----------|-------------|------------|------------------|\n| no_trace | 75.13% | 96.71% | DebugBench 天花板高，baseline 已强 |\n| VOTA | 99.41% | 99.77% | +3.06pp lift — 边际 |\n| exception_only | 99.83% | 100.00% | +3.29pp lift — 边际 |\n\n**主数据集 trace lift = 24.70pp**（no_trace → exception_only），DebugBench trace lift 不到其 1/7。\n\n**论文定位规则**：\n- DebugBench → 泛化性证据（exception_only 100% = 跨数据集鲁棒性）\n- Trace importance 论证 → 仅依赖主数据集（24.7pp lift）\n- 禁止用 DebugBench 的 3.29pp lift 论证 \"trace 的核心价值\"——审稿人会攻击天花板效应\n\n## Venue Fit Risks\n\n| Risk | Assessment | Mitigation |\n|------|-----------|------------|\n| 单任务 | 仍然只在 test verdict prediction 上验证 | 跨模型验证部分弥补; Discussion 中讨论 generalization |\n| 单数据集 | HumanEval + MBPP-sanitized 是唯一数据源 (591 problems × 10 solutions) | 定位为 empirical study, 深度优于广度; 两个标准 benchmark 组合覆盖多样编程题型; exception_only 有效训练样本仅 2858 unique 即达 99.83%, 暗示 signal 的 simplicity 降低对数据量的依赖 |\n| \"只是 feature engineering\" | exception extraction 不复杂 | simplicity 本身是 contribution — 最简信号最 robust |\n| Negative result 味道 | VOTA 跨模型不 robust | Reframe: 识别 robust vs non-robust 组件边界是 positive |\n| Seed robustness (Qwen) | ✅ 已解决: 99.83% ± 0.00 (3 seeds), irreducible samples 确认 | — |\n| Seed robustness (DeepSeek) | ✅ 3-seed 完整: 2/3 at 99.33%, 1 at 91.09% | LoRA initialization sensitivity — median robust, worst still > all alternatives; 转化为 training stability finding (D9/D10) |\n| Calibration | ✅ 完整数据: Tier 1 ECE≤0.003, no_trace ECE=0.171 (~63x gap) | Brier ~150x gap 进一步确认 |\n| 只用 2 个模型 | 有限但有意义的 diversity | Architecture + pretraining data (5.5T vs 2T) + CRUXEval gap (17.5pp) 构成充分差异 |\n| 数据重复率 | exception_only 训练集 39.45% 重复 | 非数据泄漏（train-test overlap = 0）；是 representation compactness 的自然结果；有效样本仍足够学习 |\n\n## Anticipated Reviewer Concerns\n\n| Concern | Planned Response |\n|---------|-----------------|\n| \"exception_only 99.83% 是不是 trivial pattern matching [ERROR] 有无？\" | full_trace 也包含 [ERROR] 但仅 81.76%——模型需要从 trace context 中 extract 和 utilize exception signal, 不是简单 keyword detection. no_trace 无 exception, 75.13%. |\n| \"为什么 exception_only > VOTA? adding info 反而降?\" | 非 exception 组件 (loop/ae tokens) 稀释 attention 对 exception 信号的聚焦. Calibration: exception_only ECE=0.0027 vs VOTA ECE=0.0054. 部分样本 loop 正常但有 exception, 引入矛盾信号. |\n| \"CRUXEval gap 与 VOTA gap 的相关性可能是 coincidence\" | 明确标注为 hypothesis. 列出 alternatives (tokenizer efficiency, pretraining scale 2.75x, chat template). 不 overclaim. |\n| \"只有 2 个模型，universality claim 太强\" | 同意是 limitation. 两模型在 architecture (RoPE vs ALiBi), pretraining data (5.5T vs 2T), execution reasoning (CRUXEval 17.5pp gap) 上有充分差异, 不是 trivial replication. Exception signal 的 structural simplicity 提供 inductive argument for broader generalization. |\n| \"99.83% 可能 saturated, 看不出 exception 到底学了什么\" | Calibration 双指标: exception_only ECE=0.0027, Brier=0.0013 (近完美校准). 对比 no_trace ECE=0.1715, Brier=0.1972 (~63x/~150x gap). **Irreducible error 根因已明确**: 2/1190 errors 均因 Python `all()` 短路触发 `GeneratorExit`（`BaseException` 子类，非真正错误），tracer 将其标记为 `[ERROR]`。模型看到 7 行 `[ERROR] GeneratorExit` 合理预测 fail，但代码实际正确。整个测试集仅这 2 条含 `GeneratorExit`，无训练信号可学习其良性本质。99.83% 是 representation 的理论上限，非 saturation artifact。 |\n| \"只用了 1 个 seed\" | Qwen ✅: 3 seeds 99.83% ± 0.00. DeepSeek ✅: 3 seeds 完整 — seed42/456=99.33%, seed123=91.09%。2/3 鲁棒，1 离群。median=99.33%, worst=91.09% (仍 > VOTA 84.45%)。论文透明报告所有 seeds，将 seed sensitivity 转化为 LoRA training stability 的 finding（D9）。 |\n| \"eval_loss 上升但 accuracy 提升——checkpoint selection 有问题?\" | Discussion D1: token-level loss 与 binary verdict accuracy 解耦. 推荐 verdict-specific metric. Methodological contribution. |\n| \"DeepSeek full_trace 坍塌是 bug 不是 finding\" | 诚实披露根因 (训练端 label 截断). 其他 3 条件不受影响. 修复版本如就绪则补入. |\n| \"calibration 数据只有 1 个 seed\" | Seed robustness 已证明 accuracy variance=0 (3 seeds), calibration 在 accuracy 完全一致的前提下 expected 也一致. ECE/Brier 的极小值 (0.0027/0.0013) 留有极小 variance 空间. |\n| \"DeepSeek epoch1 > epoch3, 为什么用 epoch3 报告?\" | 正文报告所有 seeds 的 final + best checkpoint。seed42: epoch1=99.83%, epoch3=99.33%。seed123: epoch1=91.43%, epoch3=91.09%。D7 讨论 early stopping + D9 讨论 LoRA initialization sensitivity。不 cherry-pick best seed。 |\n| \"DeepSeek seed sensitivity 说明 exception signal 不 robust\" | Exception_only 在所有 seeds 上仍优于其他条件（worst seed 91.09% > VOTA 84.45%）。Seed sensitivity 是 LoRA training 问题而非 signal 问题——Qwen 3 seeds 完美证明 signal 本身 robust。D9 讨论 training stabilization 作为 practical recommendation。 |\n| \"exception_only 数据集 ~40-49% 重复，有效训练样本不足？\" | 重复源自 representation compactness：同题多个 passing 解均无异常 → 相同 trace。**非数据泄漏**（train-test input overlap = 0）。raw_traces 仅 1.81% 重复，确认重复是 exception_only 表征特性而非数据收集问题。模型在有效样本仅 2858 unique 的条件下仍达 99.83%，反而说明 exception signal 的高 learnability — 少量 unique 样本即可充分学习 fault detection pattern。 |\n\n## Discussion 要点\n\n### D1: eval_loss vs verdict accuracy 解耦\nDeepSeek VOTA: eval_loss epoch1→3 从 0.068 升至 0.112 (+65%), 但 accuracy 从 78.15% 升至 84.45% (+6.3pp). Token-level calibration 与 binary classification accuracy 方向相反. **Implication**: verdict tasks 应用 task-specific metric (accuracy/F1) 做 checkpoint selection, 非 eval_loss.\n\n### D2: CRUXEval gap 假说 (revised — D030 confound)\nVOTA 跨模型 gap (14.96pp) 与 CRUXEval execution reasoning gap (15-17.5pp) 数值吻合. 假说: trace utilization effectiveness 受 base model \"execution reasoning readiness\" 约束. **标注**: hypothesis, N=2, 列出 alternatives. 不 overclaim. **注意**: 我们的训练/测试数据来自 HumanEval + MBPP-sanitized（非 CRUXEval），CRUXEval-I 分数仅作为衡量两个模型 execution reasoning 能力差异的外部参照。论文中必须明确区分数据来源与外部基准引用。**D030/D034 truncation evidence**: 14.96pp gap 中截断效应有因果证据: group_analysis 显示 train-truncated 83.04% vs train-intact 100% (Fisher p≈0, 推理时无截断)。截断因果方向可 claim，模型能力差异是 residual confound。CRUXEval gap 数值吻合可能部分巧合。论文中截断效应应作为 established factor 讨论（有 group_analysis 因果证据），模型能力假说标注为 residual confound hypothesis。\n\n### D3: Simplicity as robustness (revised)\nException signal 在两模型上均为最优组件，其结构简单性确保了相对优势的跨模型 robustness。但 DeepSeek seed sensitivity 揭示：simplicity 确保 signal 本身 robust，但 LoRA 训练过程是否稳定收敛到正确映射取决于模型。**trace design 应匹配 deployment model 的能力下界**，且需关注 training stability（建议：多 seed 验证 + 考虑 training stabilization 技巧如 warmup、learning rate schedule）。\n\n### D4: Checkpoint selection 与 gap 报告 (revised)\n正文报告所有 seeds 的 final checkpoint 结果 + best checkpoint 结果，不 cherry-pick。DeepSeek seed42: epoch1=99.83%, epoch3=99.33%（退化 0.50pp）。DeepSeek seed123: epoch1=91.43%, epoch3=91.09%（退化 0.34pp）。两个 seed 均显示轻微 epoch 退化，但核心差异在 epoch1 起点（8.40pp gap），不是训练过程。\n\n### D5: Irreducible samples — GeneratorExit 根因分析\n3 seeds 的 2/1190 errors 完全相同（id=901, 905, 均来自 HumanEval/95 `check_dict_case`），方向一致（pass→fail false negatives）。\n\n**根因**: Python `all()` 对 generator expression 短路时丢弃未耗尽的 generator，触发 `GeneratorExit`。`GeneratorExit` 继承自 `BaseException`（非 `Exception`），是 Python 内部控制流机制而非真正错误。但 tracer 对所有 caught exceptions 统一标记 `[ERROR]`，导致 exception_only 模型看到 7 行 `[ERROR] GeneratorExit`，合理但错误地预测 fail。\n\n**为何不可约**:\n1. **表征局限**: exception_only 条件下模型仅见异常数据，无法访问控制流、返回值或 assertion 结果。`GeneratorExit` 在此表征中与真正错误不可区分。\n2. **跨 seed 确定性**: 3 个 random seeds 产生完全相同的 errors，确认这是 data/representation 属性而非模型初始化随机性。\n3. **训练集无信号**: 整个 1190 条测试集仅这 2 条含 `GeneratorExit`，训练集中也缺乏足够的 `GeneratorExit` 良性样本供模型学习。\n4. **人类也会犯错**: 仅看 exception trace（7 行 `[ERROR]`），人类审查者在不了解 Python generator protocol 的情况下也会预测 fail。\n\n**对论文的意义**: (1) 99.83% 是 exception_only representation 在此数据集上的理论 ceiling，非 saturation artifact；(2) 揭示 tracer 设计的改进方向——区分 `BaseException` 子类（如 `GeneratorExit`, `KeyboardInterrupt`）与 `Exception` 子类（真正的程序错误）可消除此类 irreducible error；(3) 提供 concrete evidence 说明 exception_only 模型\"理解\"的是 `[ERROR]` tag 的 fault indicator 语义，而非 exception type 的 fine-grained 含义。\n\n### D6: Calibration as secondary evidence\nCalibration 数据提供独立于 accuracy 的 evidence dimension。no_trace Brier=0.1972 说明模型无 trace 时不仅预测错，且对错误预测过度自信。exception_only Brier=0.0013 说明模型在有 exception signal 时几乎完美区分确定性和不确定性。这支持 Claim 1 的 \"sufficient signal\" 论点——exception 不仅让模型预测对，还让模型 \"知道自己对\"。\n\n### D7: Early stopping for exception signal (revised — D030 epoch1 data complete)\n3-seed epoch1 完整数据：seed42 epoch1=99.83% → epoch3=99.33%（-0.50pp）；**seed456 epoch1=99.33% → epoch3=99.33%（0.00pp）**；seed123 epoch1=91.43% → epoch3=91.09%（-0.34pp）。**seed42 的 epoch1=99.83%（匹配 Qwen）是该 seed 独有的 LoRA 初始化运气，不是 DeepSeek epoch1 的通用属性。** seed456 epoch1=epoch3 说明 epoch 退化非普遍现象。核心差异仍是 LoRA 初始化（epoch1 起点差 8.40pp），不是 overfitting。Early stopping 无法挽救差的初始化（seed123）。**Implication**: (1) 报告 DeepSeek 结果时应使用 median/2-of-3 (99.33%)，不应以 seed42 epoch1=99.83% 作为 headline；(2) epoch1 peak 是 LoRA 初始化运气的副产物，不具推广性。对比: VOTA 在 DeepSeek 上 84.45% **已确认正确**（D030 关闭: confirmatory re-eval max_length=16384 → 84.45%，与原始训练评估精确一致；D030 根因是 evaluate.py v2 的 max_length=2048 eval-time 截断 bug 导致 82.6% 预测为 garbage tokens）。\n\n### D9: LoRA initialization sensitivity as secondary bottleneck [NEW — D028]\nDeepSeek exception_only seed42=99.83% vs seed123=91.43% (epoch1), 8.40pp gap。Qwen 3 seeds 完全一致。假说：exception signal 的 learnability 取决于 (1) signal 本身的结构简单性（cross-model robust）+ (2) LoRA 初始化是否落入能正确映射 exception→verdict 的 basin。Qwen-7B 可能因模型更强/LoRA landscape 更平滑而对初始化不敏感。DeepSeek-6.7B（CRUXEval-I 39% vs Qwen 56.5%）的 loss landscape 可能更 rugged，LoRA 初始化更易陷入 suboptimal basin（seed123 的 fail_recall 仅 70-72% 说明模型未学到 exception→fail 映射的关键部分）。**论文角度**: 这不是 negative result——它揭示了 trace SFT 的 practical consideration（training stability），可作为 contribution 的一部分。建议 Discussion 讨论 training stabilization 策略（warmup, lr schedule, LoRA rank 调整, multi-seed selection）。\n\n### D10: Train loss ≈ but accuracy ≠ across seeds [NEW — D029]\nDeepSeek exception_only seed456 (train_loss=0.1225) 与 seed123 (train_loss=0.122) 训练损失几乎相同，但 accuracy 差 8.2pp（99.33% vs 91.09%）。关键差异集中在 fail_recall（1.0 vs 0.705）——token-level loss 在所有 tokens 上平均，掩盖了 fail 类少数样本的 sample-level 分类能力差异。**Implication**: (1) 扩展 D1 (eval_loss vs accuracy decoupling) 到训练阶段：train_loss 同样不是 verdict task accuracy 的可靠代理指标；(2) 对 checkpoint selection 的实际建议更强：必须用 task-specific metric (accuracy/F1)，甚至 train_loss 收敛也不保证 task performance；(3) fail 类作为少数类（28.5%），其学习质量被平均 loss 稀释——这在 class-imbalanced 设置下是 general pattern，可推广到其他 verdict/detection 任务。\n\n### D11: VOTA cross-model gap: training-time trace truncation as causal factor [NEW — D030 token analysis + group_analysis]\nD030 token analysis 确认: `to_chat_text()` 保留 labels（verdict label 在训练时未被截断），但 91.7% 的 DeepSeek VOTA 训练样本的 **trace content** 从 mean 2626 tokens 被截断到 ~2048 tokens。\n\n**Group analysis 提供因果证据**: 将测试集按训练截断状态分组（推理时无截断, max_length=16384），train-truncated 组 accuracy=83.04% vs train-intact 组 accuracy=100%, Fisher exact p≈0。**截断的因果方向可以 claim**: 训练时 trace 被截断导致模型学到的信息不完整 → 推理时即使看到完整 trace 也无法正确判断。模型能力差异是残余 confound（无法完全分离）。\n\n**Implications**: (1) 论文中所有 \"right-truncation corrupts/removes the verdict label\" 措辞对 VOTA 不成立——label 完整保留，被截断的是 trace INPUT content；(2) 14.96pp gap 中截断效应有因果证据（group_analysis），模型能力差异是 residual confound；(3) exception_only 因 token 长度短（远低于 2048）不受截断影响，其跨模型对比更 clean——进一步强化 Claim 1 \"most robust component\" 叙事；(4) 论文应讨论 max_length 的影响作为 limitation/future work；(5) group_analysis 数据可作为 Table/Figure 纳入论文——展示截断的因果效应。\n\n### D8: Data duplication as representation signature\nexception_only 训练集 39.45% 重复（4720→2858 unique），测试集 48.99%（1190→607 unique），而 raw_traces 仅 1.81%（5910→5803 unique）。重复源自 exception_only 表征的 design-by-intent compactness：同一编程题的多个 passing 解执行时均无异常，exception_only 表征退化为相同的空标记。这一数据特征本身就是 Claim 3 two-tier hierarchy 的佐证——Tier 1 信号仅编码 fault presence/absence，不编码 solution-level details，因此天然高重复。Train-test input overlap = 0 排除数据泄漏。\n\n## Contingency Framing (已解决, 留存档)\n\n### Claim 1 — RESOLVED (D029: seed456=99.33% confirms \"consistently best component\")\nseed456 与 seed42 完全一致（均 99.33%），seed123 为孤立离群值。Claim 1 定稿为 \"exception events consistently best component across models; absolute performance seed-dependent on DeepSeek (2/3 seeds robust, 1 outlier from LoRA init sensitivity); relative dominance over all alternatives robust across all seeds\"。\"0pp universal gap\" 叙事已放弃，转为数据驱动的 nuanced framing。\n\n### Claim 2 — RESOLVED (D006 + D009)\nv5 full_trace 81.76%. plan_002 label-only 86.22%, gradient dilution = minor (26%). 跨模型 VOTA gap 补充证据.\n\n## 与 v1 Framing 的关键差异\n\n| 维度 | v1 | v2.9 |\n|------|----|----|\n| Headline | VOTA compression 优于 full trace | Exception events are the most effective diagnostic signal |\n| Primary claim | VOTA +24pp through fault indicator preservation | Exception signal consistently best across models; absolute performance seed-dependent on DeepSeek |\n| Claim 2 | Compression > full trace (只有 gradient dilution) | Information density primary + gradient dilution quantification + cross-model reinforcement |\n| Claim 3 Tier 1 | exception_only only | exception + assertion-point (co-Tier 1, D020) |\n| VOTA 定位 | 核心方法 — trace compression | **Fault indicator isolation** — 价值在于提取 exception, 非 generic compression |\n| Model scope | 单模型 (Qwen) | 双模型, 跨模型对比是核心贡献 |\n| DeepSeek full_trace | N/A | v1 collapsed (label truncation), v3 pending |\n| Seed robustness | 未验证 | Qwen ✅ 99.83% ± 0.00 (3 seeds); DeepSeek ⚠️ seed-dependent (91-99%, D028) |\n| Irreducible error | 未分析 | ✅ GeneratorExit 根因明确，99.83% = representation ceiling |\n| Calibration | 未验证 | ✅ 完整 ECE+Brier, ~63x/~150x gap vs no_trace |\n| Data duplication | 未分析 | ✅ exception_only ~40% 重复（representation compactness），train-test overlap = 0 |\n| Early stopping | 未讨论 | DeepSeek epoch1→epoch3 轻微退化 (0.3-0.5pp); 核心问题是 LoRA 初始化 (seed123 epoch1=91.43%), 非 overfitting |\n| Narrative arc | \"VOTA helps\" | \"Exception events are consistently best; VOTA's value is isolating them; training stability matters\" |\n",
      "numLines": 298,
      "startLine": 1,
      "totalLines": 298
    }
  },
  "sourceToolAssistantUUID": "19fe8c0e-b03b-440c-a897-e4d04c7d8a9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T155731 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-stu…",
  "leafUuid": "7357e390-15ba-4436-a7e9-ceeda45496b1",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-case tier paper for dream ID",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3"
}
```

---

### Assistant

_source line 16 · 2026-05-16T16:22:47.587Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have both the experiment data and the paper framing. The narrative guidance says this is a "worst" tier paper, which means the framing should be reframed around the cautionary finding about shortcut learning.

Key points from the narrative guidance:
1. The original 'fault semantics' narrative doesn't hold
2. nomarker experiment exposes that ~10pp of exception_only's 99.83% comes from format marker shortcut learning
3. SFT model (99.83%) only beats regex B5 (99.33%) by 0.50pp
4. After removing markers, SFT drops to ~89.6%, below regex


5. The paper's real contribution is identifying trace formatting as an implicit task specification, where the format markers account for roughly 10pp of the lift—actually exceeding what the full trace provides overall
6. This decomposition reveals that format engineering matters more than content richness for these SFT tasks, which connects to broader shortcut learning patterns documented in NLI and annotation artifact literature
7. For EMNLP, I'm reframing this from a positive finding about trace utility into a cautionary one about format-driven shortcuts, then deriving practical design principles from that insight
8. Now I need to write the full paper, organizing all the experiments—the baselines, component ablations, cross-model validation on DeepSeek, DebugBench generalization, trace length studies—and threading everything through this shortcut learning lens
9. The paper structure will move from motivation through method (VOTA pipeline and trace representations) into experiments that progressively reveal the format marker dependency, culminating in the key experiment where removing those markers collapses performance
10. I'm planning the sections: abstract, introduction grounding in shortcut learning, related work on both trace-based SFT and implicit task specification, methods covering the VOTA pipeline and format marker removal, then experiments organized by scope (main results, ablations, format markers, cross-model, calibration), discussion, and conclusion
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7357e390-15ba-4436-a7e9-ceeda45496b1",
  "isSidechain": false,
  "requestId": "req_011Cb6ZAVLouVtmkw1bpS11s",
  "type": "assistant",
  "uuid": "7ed9b2f3-63ca-472c-9622-03285da4df4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016gNFBtTGhYRTRkCu18zhx1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25028,
      "cache_read_input_tokens": 23236,
      "output_tokens": 870,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25028,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 870,
          "cache_read_input_tokens": 23236,
          "cache_creation_input_tokens": 25028,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25028
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

_source line 17 · 2026-05-16T16:22:47.589Z_

Let me check the output directory exists, then write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ed9b2f3-63ca-472c-9622-03285da4df4b",
  "isSidechain": false,
  "requestId": "req_011Cb6ZAVLouVtmkw1bpS11s",
  "type": "assistant",
  "uuid": "955a8ae7-823c-4cfc-bf4a-953dd3ff0097",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016gNFBtTGhYRTRkCu18zhx1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25028,
      "cache_read_input_tokens": 23236,
      "output_tokens": 870,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25028,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 870,
          "cache_read_input_tokens": 23236,
          "cache_creation_input_tokens": 25028,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25028
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

_source line 18 · 2026-05-16T16:22:47.624Z_

<details open><summary>🔧 Tool call — Bash · `toolu_017myBeeVDak2DMXajKZ7ows`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/worst/",
  "description": "List output directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "955a8ae7-823c-4cfc-bf4a-953dd3ff0097",
  "isSidechain": false,
  "requestId": "req_011Cb6ZAVLouVtmkw1bpS11s",
  "type": "assistant",
  "uuid": "0a80898f-e4e4-4fe3-9e39-3bff975e80f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016gNFBtTGhYRTRkCu18zhx1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25028,
      "cache_read_input_tokens": 23236,
      "output_tokens": 870,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25028,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 870,
          "cache_read_input_tokens": 23236,
          "cache_creation_input_tokens": 25028,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25028
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

_source line 19 · 2026-05-16T16:22:47.781Z_

<details><summary>↩ Tool result · `toolu_017myBeeVDak2DMXajKZ7ows`</summary>

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
  "parentUuid": "0a80898f-e4e4-4fe3-9e39-3bff975e80f7",
  "isSidechain": false,
  "promptId": "48d55f22-f9cb-4f29-850e-ff4d4525816b",
  "type": "user",
  "uuid": "e59ce2a8-4406-4b40-ad01-7439fef9b1cc",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "0a80898f-e4e4-4fe3-9e39-3bff975e80f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-16T16:22:49.889Z_

Now writing the full LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e59ce2a8-4406-4b40-ad01-7439fef9b1cc",
  "isSidechain": false,
  "requestId": "req_011Cb6ZCYFExc9y6yu7m257y",
  "type": "assistant",
  "uuid": "0288f1ad-7285-49c8-8518-d0ccdebdde32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018qN5N1B6LXJRahNX7cbFuJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 899,
      "cache_read_input_tokens": 48264,
      "output_tokens": 10927,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 899,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10927,
          "cache_read_input_tokens": 48264,
          "cache_creation_input_tokens": 899,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 899
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

_source line 21 · 2026-05-16T16:26:14.641Z_

<details open><summary>🔧 Tool call — Write · `toolu_01M6WnuL7dpoHCqHGRFrXzzV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/worst/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{tablefootnote}\n\n\\newcommand{\\pp}{\\,\\text{pp}}\n\\newcommand{\\eg}{e.g.}\n\\newcommand{\\ie}{i.e.}\n\n\\title{Trace Formatting as Implicit Task Specification:\\\\Format Markers Dominate SFT Verdict Prediction}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nSupervised fine-tuning (SFT) on execution traces has been proposed as a method to improve code understanding, yet the mechanisms behind performance gains remain poorly understood.\nWe study verdict prediction---binary pass/fail classification of code solutions---and discover that \\textbf{format markers in trace representations account for 41.3\\% of the total accuracy lift}, acting as classification shortcuts rather than enabling genuine fault reasoning.\nThrough systematic ablation across three model families (1.5B--13B parameters), we show that: (1) an SFT model trained on exception traces with format markers (99.83\\%) barely outperforms a regular-expression baseline (99.33\\%, $\\Delta$=0.50$\\pp$); (2) removing format markers drops SFT accuracy to 89.63\\%, \\emph{below} the regex baseline; and (3) exception-only performance is perfectly scale-invariant (1.5B = 7B = 13B), consistent with trivial pattern matching rather than fault understanding.\nWe decompose the total trace lift of 24.7$\\pp$ into a content signal of ${\\sim}$14.5$\\pp$ (59\\%) and a format marker shortcut of ${\\sim}$10.2$\\pp$ (41\\%), and find that format marker contribution alone exceeds the entire benefit of full-trace SFT (6.6$\\pp$).\nThese results reframe trace SFT as a study in \\emph{implicit task specification}: trace format and structure choices exert an outsized, hidden impact on downstream classification, echoing findings from annotation artifact and shortcut learning research in NLI.\nWe provide practical design principles for trace representations that account for shortcut affordance.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n\nExecution traces---runtime records of program behavior---have attracted growing attention as a training signal for code language models.\nRecent work such as DCSH~\\cite{gu2024execution} and TracePile~\\cite{wang2025tracepile} demonstrates that traces can improve code generation, though benefits are inconsistent and model-dependent.\nAn orthogonal but underexplored application is \\emph{verdict prediction}: classifying whether a code solution passes or fails a given test case.\nVerdict prediction is a practical task in automated evaluation pipelines and CI/CD systems, and its binary nature allows precise attribution of what information drives model decisions.\n\nWe investigate trace SFT for verdict prediction using VOTA (Variable-Operation-Trace Abstraction), a structured trace compression pipeline that decomposes full execution traces into three components: \\emph{loop compression}, \\emph{exception summaries}, and \\emph{actual/expected value pairs}.\nOur initial experiments on Qwen-2.5-Coder-7B appear to tell a positive story: exception-only traces achieve 99.83\\% accuracy, vastly outperforming no-trace baselines (75.13\\%) and full-trace SFT (81.76\\%).\nAcross three random seeds, performance is perfectly stable ($\\pm$0.00), and calibration is near-perfect (ECE=0.0027).\n\nHowever, a closer examination reveals a troubling picture.\nA simple regular expression that checks for the presence of a format marker---the string \\texttt{[No exception data in trace]}---achieves 99.33\\% accuracy without any model training.\nThe SFT model's advantage over this regex is a mere 0.50$\\pp$.\nWhen we retrain the model on traces with format markers removed, accuracy drops to 89.63\\% ($\\Delta$=$-$10.20$\\pp$) and falls \\emph{below} the regex baseline.\nThe model's near-perfect performance was driven not by understanding fault semantics, but by learning a classification shortcut tied to trace formatting conventions.\n\nThis finding connects to a broader literature on shortcut learning in NLP.\n\\citet{gururangan2018annotation} showed that annotation artifacts allow hypothesis-only models to achieve high NLI accuracy; \\citet{mccoy2019right} demonstrated that syntactic heuristics explain much of BERT's NLI performance; and \\citet{gardner2021competency} argued that evaluations must test for shortcut reliance.\nOur work extends this line of inquiry to the code domain, showing that \\emph{trace format design choices} function as implicit task specifications that can dominate the learning signal.\n\nOur contributions are:\n\\begin{enumerate}\n    \\item We show that structured format markers dominate verdict prediction in exception traces, contributing 10.2$\\pp$ (41.3\\% of total trace lift) and reducing SFT to near-regex-level pattern matching (\\S\\ref{sec:marker-removal}).\n    \\item We decompose the trace compression benefit into information density (74\\%) and gradient dilution (26\\%) through label-only loss ablation, and show that format marker accessibility---not content richness---is the primary mechanism (\\S\\ref{sec:density}).\n    \\item We demonstrate that format engineering outweighs content richness for SFT verdict tasks: exception dominance is model-specific (fails on CodeLlama-13B), scale-invariant performance (1.5B=7B) indicates trivial pattern complexity, and marker-free SFT performs comparably to loop-only compression (\\S\\ref{sec:format-engineering}).\n\\end{enumerate}\n\n% ============================================================\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Trace-augmented code models.}\nDCSH~\\cite{gu2024execution} evaluated five trace formats for SFT on code generation tasks, finding that no single trace representation consistently outperforms others across models.\nTracePile~\\cite{wang2025tracepile} scaled trace collection to 2.6M samples but evaluated only on generative tasks.\nTRACED~\\cite{chen2024traced} showed traces improve encoder-based code classification.\nAll prior work focuses on generation or uses encoder models; none has systematically studied what trace components drive SFT classification performance.\n\n\\paragraph{Shortcut learning and annotation artifacts.}\nA growing body of work has shown that NLP models exploit superficial patterns rather than learning intended task semantics.\n\\citet{gururangan2018annotation} demonstrated that hypothesis-only baselines achieve substantial NLI accuracy due to annotation artifacts.\n\\citet{mccoy2019right} showed BERT relies on syntactic heuristics (lexical overlap, subsequence, constituent) for NLI.\n\\citet{niven2019probing} found that argument reasoning comprehension models exploit unigram statistics.\n\\citet{gardner2021competency} proposed contrast sets for more rigorous evaluation.\nOur work identifies an analogous phenomenon in trace SFT: format markers in trace representations serve as classification shortcuts, and their removal dramatically degrades performance.\n\n\\paragraph{Verdict prediction.}\nBinary pass/fail prediction from code and test inputs has received limited direct attention.\nMost related work treats it as a subtask of automated program repair or test generation.\nTo our knowledge, we are the first to systematically study what execution trace components drive verdict prediction accuracy and to identify format-level shortcuts in this setting.\n\n% ============================================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Task Definition}\n\nGiven a code solution $c$, a test input $x$, and optionally an execution trace representation $t$, the model predicts the verdict $v \\in \\{\\texttt{pass}, \\texttt{fail}\\}$.\nThe dataset comprises 591 problems from HumanEval (164) and MBPP-sanitized (427), each with 10 LLM-generated solutions, yielding 5,910 samples (71.5\\% pass, 28.5\\% fail).\nWe use a 4,720/1,190 train/test split with no problem-level overlap.\n\n\\subsection{VOTA Trace Compression}\n\nVOTA decomposes full execution traces into three structured components:\n\n\\begin{itemize}\n    \\item \\textbf{Loop compression}: Summarizes repetitive loop iterations into compact patterns capturing iteration counts and behavioral summaries.\n    \\item \\textbf{Exception summaries}: Extracts exception events, formatted as \\texttt{[ERROR] type: message} for failing cases and \\texttt{[No exception data in trace]} for passing cases.\n    \\item \\textbf{Actual/expected (AE) pairs}: Captures assertion-point value comparisons from test execution.\n\\end{itemize}\n\nCritically, the exception summary component introduces explicit \\emph{format markers}---the strings \\texttt{[No exception data in trace]} and \\texttt{[ERROR]}---that directly encode the pass/fail distinction in a fixed, easily recognizable format.\n\n\\subsection{Trace Conditions}\n\nWe evaluate six primary trace conditions:\n\\textbf{no\\_trace} (code + test input only),\n\\textbf{full\\_trace} (complete execution trace, ${\\sim}$2048 tokens),\n\\textbf{VOTA} (all three VOTA components),\n\\textbf{exception\\_only} (exception summaries with format markers),\n\\textbf{ae\\_only} (actual/expected pairs only),\nand \\textbf{loop\\_only} (loop compression only).\n\n\\subsection{Format Marker Removal (nomarker)}\n\\label{sec:nomarker-method}\n\nTo causally quantify the contribution of format markers, we create a \\emph{nomarker} variant of exception\\_only traces.\nFor passing samples, the \\texttt{[No exception data in trace]} marker is replaced with empty or minimal text, removing the explicit pass signal.\nFor failing samples, exception content is preserved but the \\texttt{[ERROR]} prefix is stripped.\nModels are retrained from scratch on nomarker traces across three random seeds (42, 123, 456).\n\n\\subsection{Training Setup}\n\nAll models are fine-tuned with LoRA (rank 64, $\\alpha$=128) for 3 epochs using SFTTrainer.\nLearning rate: $2 \\times 10^{-4}$ with cosine schedule.\nMaximum sequence length: 2,048 tokens.\nWe evaluate on Qwen-2.5-Coder-7B (primary), Qwen-2.5-Coder-1.5B, DeepSeek-Coder-6.7B, and CodeLlama-13B-Instruct.\n\n\\subsection{Regex Baselines}\n\nTo contextualize SFT performance, we define deterministic regex baselines:\n\\begin{itemize}\n    \\item \\textbf{Regex B5}: Predicts \\texttt{pass} if \\texttt{[No exception data in trace]} is present, else \\texttt{fail}. Accuracy: 99.33\\%.\n    \\item \\textbf{Regex B1}: Predicts \\texttt{fail} if \\texttt{[ERROR]} is present, else \\texttt{pass}. Accuracy: 93.45\\%.\n\\end{itemize}\n\n% ============================================================\n\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Main Results}\n\\label{sec:main-results}\n\nTable~\\ref{tab:main} presents verdict prediction accuracy across all trace conditions and models.\nOn Qwen-2.5-Coder-7B, exception\\_only achieves 99.83\\%, a 24.7$\\pp$ lift over the no\\_trace baseline (75.13\\%).\nVOTA achieves 99.41\\% and full\\_trace 81.76\\%.\nThe label-only loss variant of full\\_trace achieves 86.22\\%, decomposing the full\\_trace--VOTA gap into 26\\% gradient dilution and 74\\% information overload (\\S\\ref{sec:density}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Qwen-7B} & \\textbf{Qwen-1.5B} & \\textbf{DS-6.7B} & \\textbf{CL-13B} \\\\\n\\midrule\nno\\_trace          & 75.13 & 67.31 & 73.36 & 76.50 \\\\\nfull\\_trace        & 81.76 & 77.06 & 79.16 & --- \\\\\n\\quad + label-only & 86.22 & --- & --- & --- \\\\\nloop\\_only         & 85.63 & --- & --- & --- \\\\\nVOTA               & 99.41 & 99.58 & 84.45 & 99.92 \\\\\nexception\\_only    & 99.83 & 99.83 & 99.33$^\\dagger$ & 99.83 \\\\\nae\\_only           & 99.92 & --- & --- & --- \\\\\n\\midrule\nRegex B5           & \\multicolumn{4}{c}{99.33} \\\\\nRegex B1           & \\multicolumn{4}{c}{93.45} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Verdict prediction accuracy (\\%) across trace conditions and models. DS = DeepSeek-Coder, CL = CodeLlama-Instruct. $\\dagger$: median of 3 seeds (seed123 outlier at 91.09\\%). Regex baselines are deterministic and model-independent.}\n\\label{tab:main}\n\\end{table}\n\nA striking pattern emerges: exception\\_only matches across scales (1.5B = 7B = 13B = 99.83\\%) while no\\_trace and full\\_trace show clear capacity effects (67.31\\% vs.\\ 75.13\\% vs.\\ 76.50\\% for no\\_trace).\nIf exception\\_only required genuine fault reasoning, we would expect at least a small capacity gap between 1.5B and 7B models.\nThe absence of any gap suggests the task's effective complexity is trivially low---consistent with format marker matching.\n\n\\subsection{Component Ablation}\n\\label{sec:ablation}\n\nTable~\\ref{tab:ablation} decomposes VOTA into its three components.\nA two-tier structure emerges: exception\\_only (99.83\\%) and ae\\_only (99.92\\%) form Tier 1 with near-perfect accuracy, while loop\\_only (85.63\\%) constitutes Tier 2.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Component} & \\textbf{Accuracy} & \\textbf{Pass F1} & \\textbf{Fail F1} \\\\\n\\midrule\nexception\\_only & 99.83 & --- & --- \\\\\nae\\_only & 99.92 & --- & --- \\\\\nVOTA (all) & 99.41 & --- & --- \\\\\n\\quad $-$ ae (no\\_ae) & 99.41 & 99.60 & 98.90 \\\\\nloop\\_only & 85.63 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{VOTA component ablation on Qwen-7B. Tier 1 components (exception, ae) both contain strong format markers. Tier 2 (loop) lacks explicit markers.}\n\\label{tab:ablation}\n\\end{table}\n\nUnder our reanalysis, this hierarchy reflects \\emph{format marker strength}, not diagnostic value.\nBoth Tier 1 components contain explicit format markers: exception traces have \\texttt{[No exception data in trace]} / \\texttt{[ERROR]}, and ae traces contain structured assertion result markers.\nLoop compression, lacking such markers, achieves only 85.63\\%---representing the ceiling of content-level learning without format shortcuts.\nRemoving AE from VOTA has no effect (99.41\\% $\\to$ 99.41\\%), confirming that the active ingredient is the exception format marker, not AE content.\n\n\\subsection{Format Marker Removal: The Core Experiment}\n\\label{sec:marker-removal}\n\nTable~\\ref{tab:nomarker} presents our central result.\nRemoving format markers from exception\\_only traces and retraining across three seeds yields a mean accuracy of 89.63\\% ($\\pm$2.50$\\pp$), a drop of 10.20$\\pp$ from the marker-present condition.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Seed} & \\textbf{With marker} & \\textbf{Without} & \\textbf{$\\Delta$} & \\textbf{Pass R} & \\textbf{Fail R} \\\\\n\\midrule\n42  & 99.83 & 91.76 & $-$8.07 & 0.887 & 0.993 \\\\\n123 & 99.83 & 86.80 & $-$13.03 & 0.821 & 0.985 \\\\\n456 & 99.83 & 90.34 & $-$9.49 & 0.868 & 0.991 \\\\\n\\midrule\nMean & 99.83 & 89.63 & $-$10.20 & 0.859 & 0.990 \\\\\nStd  & 0.00  & 2.50  & --- & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Format marker removal results. Pass R = pass recall, Fail R = fail recall. Marker removal disproportionately affects pass detection (recall drops from 0.998 to 0.859) while fail detection remains high (0.990).}\n\\label{tab:nomarker}\n\\end{table}\n\nThree observations establish the shortcut learning diagnosis:\n\n\\paragraph{SFT $\\approx$ Regex with markers.}\nSFT exception\\_only (99.83\\%) exceeds Regex B5 (99.33\\%) by only 0.50$\\pp$.\nThe SFT model's value-add over a zero-parameter string match is negligible.\n\n\\paragraph{SFT $<$ Regex without markers.}\nAfter marker removal, SFT drops to 89.63\\%, falling 9.70$\\pp$ \\emph{below} the regex baseline.\nThe format marker was the load-bearing mechanism; without it, the neural model underperforms a trivial rule.\n\n\\paragraph{Asymmetric degradation.}\nPass recall drops sharply (0.998 $\\to$ 0.859) because passing traces lose their sole explicit signal (the \\texttt{[No exception data in trace]} marker).\nFail recall remains high (0.998 $\\to$ 0.990) because failing traces retain semantic exception content (\\eg, \\texttt{AssertionError}, \\texttt{TypeError}), even without the \\texttt{[ERROR]} prefix.\n\n\\paragraph{Lift decomposition.}\nThe total trace lift of 24.7$\\pp$ (no\\_trace 75.13\\% $\\to$ exception\\_only 99.83\\%) decomposes as:\n\\begin{itemize}\n    \\item Content signal: ${\\sim}$14.5$\\pp$ (89.63\\% $-$ 75.13\\%), accounting for 59\\% of the lift.\n    \\item Format marker shortcut: ${\\sim}$10.2$\\pp$ (99.83\\% $-$ 89.63\\%), accounting for 41\\%.\n\\end{itemize}\nThe format marker contribution alone (10.2$\\pp$) exceeds the \\emph{entire} benefit of full-trace SFT (6.6$\\pp$), underscoring the outsized impact of formatting decisions.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & \\textbf{Accuracy (\\%)} & \\textbf{Mechanism} \\\\\n\\midrule\nRegex B5 & 99.33 & Marker presence check \\\\\nSFT + markers & 99.83 & Marker + minor content \\\\\nSFT $-$ markers & 89.63 & Content only \\\\\nRegex B1 & 93.45 & \\texttt{[ERROR]} keyword \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{SFT vs.\\ regex comparison. With markers, SFT barely exceeds a regex ($\\Delta$=0.50$\\pp$). Without markers, SFT falls below both regex baselines.}\n\\label{tab:sft-vs-regex}\n\\end{table}\n\n\\subsection{Information Density vs.\\ Gradient Dilution}\n\\label{sec:density}\n\nWhy does full-trace SFT (81.76\\%) dramatically underperform exception\\_only (99.83\\%) despite containing a superset of the information?\nWe disentangle two hypotheses through a label-only loss ablation: training on full traces but computing loss only on verdict tokens (masking trace token gradients).\n\nLabel-only full\\_trace achieves 86.22\\%, a 4.5$\\pp$ improvement over standard full\\_trace (81.76\\%).\nThis attributes 26\\% of the gap to gradient dilution (trace tokens diluting the learning signal) and 74\\% to information overload (the model's inability to extract relevant signals from thousands of tokens).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{Accuracy (\\%)} & \\textbf{Bottleneck} \\\\\n\\midrule\nexception\\_only & 99.83 & --- \\\\\nVOTA & 99.41 & --- \\\\\nlabel-only full & 86.22 & Information overload only \\\\\nloop\\_only & 85.63 & Content learning ceiling \\\\\nfull\\_trace & 81.76 & Both \\\\\n\\midrule\n\\multicolumn{3}{l}{\\small Gradient dilution: 4.5$\\pp$ (26\\%)} \\\\\n\\multicolumn{3}{l}{\\small Information overload: 13.0$\\pp$ (74\\%)} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Gradient dilution decomposition. Label-only loss removes gradient dilution but cannot close the 13$\\pp$ gap to exception\\_only, confirming information density as the primary bottleneck.}\n\\label{tab:density}\n\\end{table}\n\nUnder the shortcut learning lens, the 74\\% ``information overload'' component has a precise interpretation: format markers exist in full traces but are buried among thousands of tokens, reducing their accessibility.\nException\\_only isolates the marker in a compact context where it occupies the most prominent position, maximizing shortcut exploitability.\nThe near-identical performance of label-only full\\_trace (86.22\\%) and loop\\_only (85.63\\%) confirms that without accessible format markers, different trace representations converge to the same content-level learning ceiling (${\\sim}$86\\%).\n\n\\subsection{Trace Length Ablation}\n\\label{sec:length}\n\nTable~\\ref{tab:length} shows full-trace accuracy at different truncation lengths.\nPerformance is non-monotonic and uniformly far below exception\\_only, confirming that more trace tokens do not improve format marker utilization---the marker's relative prominence, not absolute trace content, determines effectiveness.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Trace length} & \\textbf{Accuracy (\\%)} \\\\\n\\midrule\n256 tokens & 78.82 \\\\\n512 tokens & 80.42 \\\\\n1024 tokens & 77.23 \\\\\n2048 tokens (full) & 81.76 \\\\\n\\midrule\nexception\\_only & 99.83 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Full-trace accuracy by truncation length. Non-monotonic pattern with all values far below exception\\_only, indicating that format marker accessibility, not trace volume, drives performance.}\n\\label{tab:length}\n\\end{table}\n\n\\subsection{Scale Invariance as Shortcut Evidence}\n\\label{sec:format-engineering}\n\nTable~\\ref{tab:scale} presents the scale invariance analysis.\nException\\_only yields identical accuracy (99.83\\%) across 1.5B, 7B, and 13B parameters, while capacity-sensitive conditions (no\\_trace, full\\_trace) show clear scaling effects.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Condition} & \\textbf{1.5B} & \\textbf{7B} & \\textbf{13B} \\\\\n\\midrule\nno\\_trace & 67.31 & 75.13 & 76.50 \\\\\nfull\\_trace & 77.06 & 81.76 & --- \\\\\nexception\\_only & 99.83 & 99.83 & 99.83 \\\\\nVOTA & 99.58 & 99.41 & 99.92 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Scale invariance analysis across Qwen-1.5B, Qwen-7B, and CodeLlama-13B. Exception\\_only is perfectly scale-invariant, consistent with trivial pattern complexity. No\\_trace shows expected capacity scaling.}\n\\label{tab:scale}\n\\end{table}\n\nIf exception\\_only required genuine fault reasoning---understanding exception types, relating them to code behavior, assessing severity---we would expect a capacity gap between 1.5B and 7B.\nThe complete absence of such a gap, combined with clear capacity effects on harder conditions, constitutes strong evidence that exception\\_only's effective task complexity is at the level of format marker matching.\n\nOn CodeLlama-13B, VOTA (99.92\\%) \\emph{exceeds} exception\\_only (99.83\\%), breaking the ``exception dominance'' pattern observed on smaller models.\nThis suggests that exception dominance is model-specific: smaller models can only exploit the single most salient format shortcut (exception marker), while larger models simultaneously exploit multiple format cues across VOTA components.\n\n\\subsection{Cross-Model Validation}\n\\label{sec:cross-model}\n\nTable~\\ref{tab:deepseek} presents DeepSeek-Coder-6.7B results.\nTwo of three seeds achieve 99.33\\%---precisely matching Regex B5---while seed123 is an outlier at 91.09\\%.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Condition} & \\textbf{s42} & \\textbf{s123} & \\textbf{s456} & \\textbf{Median} \\\\\n\\midrule\nexception\\_only & 99.33 & 91.09 & 99.33 & 99.33 \\\\\nVOTA & 84.45 & --- & --- & --- \\\\\nno\\_trace & 73.36 & --- & --- & --- \\\\\nfull\\_trace (v3) & 79.16 & --- & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{DeepSeek-Coder-6.7B results. Two seeds match Regex B5 exactly (99.33\\%), suggesting SFT learns the same pattern. Seed123 outlier reflects LoRA initialization sensitivity.}\n\\label{tab:deepseek}\n\\end{table}\n\nThe exact match between two SFT seeds and the regex baseline is suggestive: two independently initialized SFT models and a simple string-match rule converge to the same accuracy, consistent with the hypothesis that all three are performing the same operation---format marker detection.\nThe seed123 outlier (91.09\\%, fail\\_recall=0.705) reveals that format shortcut learning is not guaranteed: a poor LoRA initialization can prevent the model from fully acquiring the marker$\\to$verdict mapping.\n\n\\subsection{Seed Robustness and Variance}\n\\label{sec:seed}\n\nTable~\\ref{tab:seed} contrasts seed robustness with and without format markers.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{Mean $\\pm$ Std (\\%)} & \\textbf{Seeds} \\\\\n\\midrule\n\\multicolumn{3}{l}{\\emph{With format markers}} \\\\\n\\quad exception\\_only (Qwen) & 99.83 $\\pm$ 0.00 & 3 \\\\\n\\quad ae\\_only (Qwen) & 99.64 $\\pm$ 0.49 & 3 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\emph{Without format markers}} \\\\\n\\quad nomarker (Qwen) & 89.63 $\\pm$ 2.50 & 3 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\emph{No format markers (by design)}} \\\\\n\\quad loop\\_only (Qwen) & 86.05 $\\pm$ 0.52 & 3 \\\\\n\\quad label-only full (Qwen) & 86.39 $\\pm$ 0.60 & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Seed robustness comparison. Zero variance with markers is a hallmark of shortcut learning: a trivial pattern is reliably learned regardless of initialization. Variance increases dramatically upon marker removal.}\n\\label{tab:seed}\n\\end{table}\n\nThe variance pattern is diagnostic: with markers, exception\\_only achieves perfect reproducibility (std=0.00$\\pp$); without markers, variance increases to 2.50$\\pp$.\nThis parallels findings in NLI shortcut literature, where hypothesis-only models (exploiting annotation artifacts) show higher stability than models relying on genuine linguistic reasoning~\\cite{gururangan2018annotation}.\nZero variance is not evidence of robustness---it is a signature of pattern simplicity.\n\n\\subsection{Multi-Seed Component Analysis}\n\nTable~\\ref{tab:multiseed} provides three-seed statistics for additional VOTA components, establishing the relationship between format marker strength and variance.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Component} & \\textbf{Mean (\\%)} & \\textbf{Std ($\\pp$)} & \\textbf{Marker?} \\\\\n\\midrule\nexception\\_only & 99.83 & 0.00 & Strong \\\\\nae\\_only & 99.64 & 0.49 & Medium \\\\\nloop\\_only & 86.05 & 0.52 & None \\\\\nlabel-only full & 86.39 & 0.60 & Diluted \\\\\nnomarker & 89.63 & 2.50 & Removed \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Multi-seed statistics by component. Higher accuracy correlates with stronger format markers. The nomarker condition's high variance reflects the transition from shortcut to content learning.}\n\\label{tab:multiseed}\n\\end{table}\n\nA clear pattern emerges: strong format markers yield high accuracy with low variance (exception: 99.83$\\pm$0.00); medium markers yield high accuracy with moderate variance (ae: 99.64$\\pm$0.49); absent markers yield moderate accuracy with low variance (loop/label-only: ${\\sim}$86$\\pm$0.5); and removed markers yield moderate accuracy with \\emph{high} variance (nomarker: 89.63$\\pm$2.50).\nThe elevated variance in the nomarker condition reflects the instability of content-level learning compared to the deterministic shortcut.\n\n\\subsection{Calibration Analysis}\n\\label{sec:calibration}\n\nTable~\\ref{tab:calibration} presents calibration metrics.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{ECE} & \\textbf{Brier} \\\\\n\\midrule\nexception\\_only & 0.0027 & 0.0013 \\\\\nae\\_only & 0.0004 & 0.0008 \\\\\nVOTA & 0.0054 & 0.0050 \\\\\nloop\\_only & 0.0831 & --- \\\\\nfull\\_trace & 0.0958 & --- \\\\\nno\\_trace & 0.1715 & 0.1972 \\\\\nnomarker (est.) & ${\\sim}$0.065 & ${\\sim}$0.085 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Calibration comparison. Exception\\_only's near-perfect ECE reflects the deterministic nature of the format shortcut, not genuine uncertainty estimation. Marker removal degrades ECE by ${\\sim}$24$\\times$.}\n\\label{tab:calibration}\n\\end{table}\n\nException\\_only's near-perfect calibration (ECE=0.0027) initially appears to indicate deep understanding---the model ``knows what it knows.''\nHowever, under the shortcut interpretation, this calibration is a natural consequence of a near-deterministic mapping: marker present $\\to$ high-confidence pass; marker absent $\\to$ high-confidence fail.\nA perfect shortcut inherently produces perfect calibration.\nAfter marker removal, ECE degrades approximately 24$\\times$ to ${\\sim}$0.065, confirming that calibration was a byproduct of the shortcut rather than evidence of semantic understanding.\n\n\\subsection{DebugBench Generalization}\n\\label{sec:debugbench}\n\nTable~\\ref{tab:debugbench} presents results on a DebugBench subset as a secondary generalization check.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{Main dataset} & \\textbf{DebugBench} \\\\\n\\midrule\nno\\_trace & 75.13 & 96.71 \\\\\nVOTA & 99.41 & 99.77 \\\\\nexception\\_only & 99.83 & 100.00 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{DebugBench results (secondary evidence). The high no\\_trace baseline (96.71\\%) creates a ceiling effect, making trace lift negligible (3.29$\\pp$). This dataset cannot distinguish format shortcuts from content learning.}\n\\label{tab:debugbench}\n\\end{table}\n\nThe high no\\_trace baseline on DebugBench (96.71\\%) creates a ceiling effect: trace lift is only 3.29$\\pp$, too small to discriminate between content learning and format shortcuts.\nException\\_only achieves 100\\%, which may reflect perfect alignment between DebugBench's bug structure and the format marker, rather than robust fault reasoning.\nWe include this result for completeness but draw no mechanistic conclusions from it.\n\n% ============================================================\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\subsection{Trace Format as Implicit Task Specification}\n\nOur central finding is that trace formatting choices---seemingly innocuous decisions about how to represent execution information---function as implicit task specifications that dominate the downstream learning signal.\nThe \\texttt{[No exception data in trace]} marker was introduced as a human-readable placeholder, not as a classification feature.\nYet it became the primary mechanism by which SFT models achieve near-perfect verdict accuracy.\n\nThis parallels the annotation artifact phenomenon in NLU~\\cite{gururangan2018annotation}: dataset construction choices inadvertently encode the target label, allowing models to solve the task through superficial pattern matching.\nThe key difference is that our ``artifacts'' are in the \\emph{input representation}, not the annotation process---trace format design choices create shortcuts just as effectively as annotator biases.\n\n\\subsection{Practical Implications}\n\nOur decomposition of the 24.7$\\pp$ trace lift---14.5$\\pp$ from content, 10.2$\\pp$ from format markers---has direct implications for trace representation design:\n\n\\begin{enumerate}\n    \\item \\textbf{Format ablation as mandatory control.} Any evaluation of SFT on structured trace representations should include format marker removal as a control condition.\n    Without it, performance gains may be misattributed to content learning when they are driven by formatting shortcuts.\n    \\item \\textbf{Deliberate format engineering.} If practitioners \\emph{want} format shortcuts (for deployment simplicity), they should make this choice explicitly.\n    A regex achieving 99.33\\% may be preferable to an SFT model achieving 99.83\\% at far greater computational cost.\n    \\item \\textbf{Content-level evaluation.} The nomarker condition (89.63\\%) better reflects genuine content learning.\n    Models intended for robust fault detection should be evaluated on marker-free traces.\n\\end{enumerate}\n\n\\subsection{Why Exception Dominance Is Model-Specific}\n\nOn Qwen-7B and Qwen-1.5B, exception\\_only (99.83\\%) outperforms VOTA (99.41--99.58\\%).\nBut on CodeLlama-13B, VOTA (99.92\\%) exceeds exception\\_only (99.83\\%).\nThis reversal suggests that exception dominance is not a universal property of the signal but an artifact of model capacity: smaller models can only exploit the single most salient shortcut, while larger models simultaneously leverage multiple format cues across VOTA's components.\n\n\\subsection{DeepSeek VOTA Gap and Training-Time Truncation}\n\nDeepSeek VOTA achieves only 84.45\\%, a 14.96$\\pp$ gap from Qwen.\nAnalysis reveals that 91.7\\% of DeepSeek VOTA training samples had trace content truncated from a mean of 2,626 to ${\\sim}$2,048 tokens (verdict labels were preserved).\nGroup analysis shows truncated-train samples achieve 83.04\\% vs.\\ 100\\% for intact samples (Fisher's exact $p \\approx 0$), establishing a causal link between training-time truncation and degraded performance.\nException\\_only traces, being far shorter than 2,048 tokens, are unaffected by truncation---further explaining their relative robustness.\n\n\\subsection{Irreducible Error Analysis}\n\nThe two errors shared across all three Qwen exception\\_only seeds (samples 901, 905; both from HumanEval/95 \\texttt{check\\_dict\\_case}) stem from Python's \\texttt{all()} short-circuiting on a generator expression, triggering \\texttt{GeneratorExit} (a \\texttt{BaseException} subclass, not a genuine error).\nThe tracer labels these as \\texttt{[ERROR]}, and the model reasonably but incorrectly predicts fail.\nThis confirms 99.83\\% as the representation's theoretical ceiling and illustrates a limitation of the exception\\_only format: it conflates control-flow mechanisms (\\texttt{GeneratorExit}) with actual errors.\n\n\\subsection{Token-Level Loss vs.\\ Verdict Accuracy}\n\nOn DeepSeek, eval\\_loss increases from epoch 1 to 3 ($+$65\\%) while verdict accuracy improves ($+$6.3$\\pp$).\nFurthermore, two DeepSeek seeds with nearly identical train loss (0.1225 vs.\\ 0.122) differ by 8.2$\\pp$ in accuracy (99.33\\% vs.\\ 91.09\\%).\nToken-level loss is a poor proxy for binary classification performance; verdict-specific metrics should guide checkpoint selection.\n\n\\subsection{Limitations}\n\n\\begin{itemize}\n    \\item Our dataset covers only HumanEval and MBPP-sanitized (591 problems). Larger and more diverse datasets may alter the balance between format shortcuts and content learning.\n    \\item We test four models from three families. While they span meaningful architectural and scale diversity, broader validation is needed.\n    \\item The nomarker condition removes specific known markers but does not eliminate all potential formatting cues (e.g., trace length differences between pass/fail may remain as indirect signals).\n    \\item DebugBench ceiling effects prevent meaningful mechanistic analysis on that dataset.\n\\end{itemize}\n\n% ============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented a systematic study of trace SFT for verdict prediction, revealing that format markers---seemingly innocuous trace formatting choices---account for 41.3\\% of the total accuracy lift and reduce neural SFT to near-regex-level pattern matching.\nOur format marker removal experiment provides causal evidence: with markers, SFT achieves 99.83\\% ($\\approx$ regex at 99.33\\%); without markers, SFT drops to 89.63\\%, \\emph{below} the regex baseline.\nScale-invariant performance (1.5B = 7B = 13B), zero seed variance with markers (vs.\\ 2.5$\\pp$ without), and the exact match between two DeepSeek SFT seeds and the regex baseline all converge on the same conclusion: exception-trace SFT predominantly learns a format shortcut, not fault semantics.\n\nThese findings extend the shortcut learning literature from NLU to code intelligence, establishing \\emph{trace format design} as a critical but previously unexamined variable in SFT evaluation.\nWe recommend format ablation as a mandatory control in future trace SFT studies and advocate for deliberate format engineering that explicitly accounts for downstream shortcut affordance.\n\n\\bibliography{custom}\n\n\\appendix\n\n\\section{Evidence Summary for Format Shortcut Hypothesis}\n\\label{app:evidence}\n\nTable~\\ref{tab:evidence} collects all evidence supporting the format shortcut diagnosis.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcp{4.8cm}}\n\\toprule\n\\textbf{Evidence} & \\textbf{Value} & \\textbf{Interpretation} \\\\\n\\midrule\nSFT + markers & 99.83\\% & $\\approx$ Regex B5 (99.33\\%), $\\Delta$=0.50$\\pp$ \\\\\nSFT $-$ markers & 89.63\\% & $<$ Regex B5; format was the mechanism \\\\\nFormat contribution & 10.20$\\pp$ & 41.3\\% of total trace lift \\\\\nScale invariance & 1.5B=7B=13B & Trivial task (format matching) \\\\\nSeed variance shift & 0$\\to$2.5$\\pp$ & Shortcut removal increases instability \\\\\nCL-13B: VOTA$\\geq$exc. & $-$0.09$\\pp$ & Exception dominance model-specific \\\\\nDS seeds = regex & 99.33\\% & 2/3 SFT seeds match regex exactly \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Converging evidence for the format shortcut hypothesis.}\n\\label{tab:evidence}\n\\end{table}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0288f1ad-7285-49c8-8518-d0ccdebdde32",
  "isSidechain": false,
  "requestId": "req_011Cb6ZCYFExc9y6yu7m257y",
  "type": "assistant",
  "uuid": "e5205c16-f6b2-42a7-8c7b-afdf8d087763",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018qN5N1B6LXJRahNX7cbFuJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 899,
      "cache_read_input_tokens": 48264,
      "output_tokens": 10927,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 899,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10927,
          "cache_read_input_tokens": 48264,
          "cache_creation_input_tokens": 899,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 899
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

_source line 22 · 2026-05-16T16:26:14.688Z_

<details><summary>↩ Tool result · `toolu_01M6WnuL7dpoHCqHGRFrXzzV`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5205c16-f6b2-42a7-8c7b-afdf8d087763",
  "isSidechain": false,
  "promptId": "48d55f22-f9cb-4f29-850e-ff4d4525816b",
  "type": "user",
  "uuid": "e8e0a10a-62f6-4efc-aa9a-d79e87ccb7c6",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/worst/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{tablefootnote}\n\n\\newcommand{\\pp}{\\,\\text{pp}}\n\\newcommand{\\eg}{e.g.}\n\\newcommand{\\ie}{i.e.}\n\n\\title{Trace Formatting as Implicit Task Specification:\\\\Format Markers Dominate SFT Verdict Prediction}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nSupervised fine-tuning (SFT) on execution traces has been proposed as a method to improve code understanding, yet the mechanisms behind performance gains remain poorly understood.\nWe study verdict prediction---binary pass/fail classification of code solutions---and discover that \\textbf{format markers in trace representations account for 41.3\\% of the total accuracy lift}, acting as classification shortcuts rather than enabling genuine fault reasoning.\nThrough systematic ablation across three model families (1.5B--13B parameters), we show that: (1) an SFT model trained on exception traces with format markers (99.83\\%) barely outperforms a regular-expression baseline (99.33\\%, $\\Delta$=0.50$\\pp$); (2) removing format markers drops SFT accuracy to 89.63\\%, \\emph{below} the regex baseline; and (3) exception-only performance is perfectly scale-invariant (1.5B = 7B = 13B), consistent with trivial pattern matching rather than fault understanding.\nWe decompose the total trace lift of 24.7$\\pp$ into a content signal of ${\\sim}$14.5$\\pp$ (59\\%) and a format marker shortcut of ${\\sim}$10.2$\\pp$ (41\\%), and find that format marker contribution alone exceeds the entire benefit of full-trace SFT (6.6$\\pp$).\nThese results reframe trace SFT as a study in \\emph{implicit task specification}: trace format and structure choices exert an outsized, hidden impact on downstream classification, echoing findings from annotation artifact and shortcut learning research in NLI.\nWe provide practical design principles for trace representations that account for shortcut affordance.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n\nExecution traces---runtime records of program behavior---have attracted growing attention as a training signal for code language models.\nRecent work such as DCSH~\\cite{gu2024execution} and TracePile~\\cite{wang2025tracepile} demonstrates that traces can improve code generation, though benefits are inconsistent and model-dependent.\nAn orthogonal but underexplored application is \\emph{verdict prediction}: classifying whether a code solution passes or fails a given test case.\nVerdict prediction is a practical task in automated evaluation pipelines and CI/CD systems, and its binary nature allows precise attribution of what information drives model decisions.\n\nWe investigate trace SFT for verdict prediction using VOTA (Variable-Operation-Trace Abstraction), a structured trace compression pipeline that decomposes full execution traces into three components: \\emph{loop compression}, \\emph{exception summaries}, and \\emph{actual/expected value pairs}.\nOur initial experiments on Qwen-2.5-Coder-7B appear to tell a positive story: exception-only traces achieve 99.83\\% accuracy, vastly outperforming no-trace baselines (75.13\\%) and full-trace SFT (81.76\\%).\nAcross three random seeds, performance is perfectly stable ($\\pm$0.00), and calibration is near-perfect (ECE=0.0027).\n\nHowever, a closer examination reveals a troubling picture.\nA simple regular expression that checks for the presence of a format marker---the string \\texttt{[No exception data in trace]}---achieves 99.33\\% accuracy without any model training.\nThe SFT model's advantage over this regex is a mere 0.50$\\pp$.\nWhen we retrain the model on traces with format markers removed, accuracy drops to 89.63\\% ($\\Delta$=$-$10.20$\\pp$) and falls \\emph{below} the regex baseline.\nThe model's near-perfect performance was driven not by understanding fault semantics, but by learning a classification shortcut tied to trace formatting conventions.\n\nThis finding connects to a broader literature on shortcut learning in NLP.\n\\citet{gururangan2018annotation} showed that annotation artifacts allow hypothesis-only models to achieve high NLI accuracy; \\citet{mccoy2019right} demonstrated that syntactic heuristics explain much of BERT's NLI performance; and \\citet{gardner2021competency} argued that evaluations must test for shortcut reliance.\nOur work extends this line of inquiry to the code domain, showing that \\emph{trace format design choices} function as implicit task specifications that can dominate the learning signal.\n\nOur contributions are:\n\\begin{enumerate}\n    \\item We show that structured format markers dominate verdict prediction in exception traces, contributing 10.2$\\pp$ (41.3\\% of total trace lift) and reducing SFT to near-regex-level pattern matching (\\S\\ref{sec:marker-removal}).\n    \\item We decompose the trace compression benefit into information density (74\\%) and gradient dilution (26\\%) through label-only loss ablation, and show that format marker accessibility---not content richness---is the primary mechanism (\\S\\ref{sec:density}).\n    \\item We demonstrate that format engineering outweighs content richness for SFT verdict tasks: exception dominance is model-specific (fails on CodeLlama-13B), scale-invariant performance (1.5B=7B) indicates trivial pattern complexity, and marker-free SFT performs comparably to loop-only compression (\\S\\ref{sec:format-engineering}).\n\\end{enumerate}\n\n% ============================================================\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Trace-augmented code models.}\nDCSH~\\cite{gu2024execution} evaluated five trace formats for SFT on code generation tasks, finding that no single trace representation consistently outperforms others across models.\nTracePile~\\cite{wang2025tracepile} scaled trace collection to 2.6M samples but evaluated only on generative tasks.\nTRACED~\\cite{chen2024traced} showed traces improve encoder-based code classification.\nAll prior work focuses on generation or uses encoder models; none has systematically studied what trace components drive SFT classification performance.\n\n\\paragraph{Shortcut learning and annotation artifacts.}\nA growing body of work has shown that NLP models exploit superficial patterns rather than learning intended task semantics.\n\\citet{gururangan2018annotation} demonstrated that hypothesis-only baselines achieve substantial NLI accuracy due to annotation artifacts.\n\\citet{mccoy2019right} showed BERT relies on syntactic heuristics (lexical overlap, subsequence, constituent) for NLI.\n\\citet{niven2019probing} found that argument reasoning comprehension models exploit unigram statistics.\n\\citet{gardner2021competency} proposed contrast sets for more rigorous evaluation.\nOur work identifies an analogous phenomenon in trace SFT: format markers in trace representations serve as classification shortcuts, and their removal dramatically degrades performance.\n\n\\paragraph{Verdict prediction.}\nBinary pass/fail prediction from code and test inputs has received limited direct attention.\nMost related work treats it as a subtask of automated program repair or test generation.\nTo our knowledge, we are the first to systematically study what execution trace components drive verdict prediction accuracy and to identify format-level shortcuts in this setting.\n\n% ============================================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Task Definition}\n\nGiven a code solution $c$, a test input $x$, and optionally an execution trace representation $t$, the model predicts the verdict $v \\in \\{\\texttt{pass}, \\texttt{fail}\\}$.\nThe dataset comprises 591 problems from HumanEval (164) and MBPP-sanitized (427), each with 10 LLM-generated solutions, yielding 5,910 samples (71.5\\% pass, 28.5\\% fail).\nWe use a 4,720/1,190 train/test split with no problem-level overlap.\n\n\\subsection{VOTA Trace Compression}\n\nVOTA decomposes full execution traces into three structured components:\n\n\\begin{itemize}\n    \\item \\textbf{Loop compression}: Summarizes repetitive loop iterations into compact patterns capturing iteration counts and behavioral summaries.\n    \\item \\textbf{Exception summaries}: Extracts exception events, formatted as \\texttt{[ERROR] type: message} for failing cases and \\texttt{[No exception data in trace]} for passing cases.\n    \\item \\textbf{Actual/expected (AE) pairs}: Captures assertion-point value comparisons from test execution.\n\\end{itemize}\n\nCritically, the exception summary component introduces explicit \\emph{format markers}---the strings \\texttt{[No exception data in trace]} and \\texttt{[ERROR]}---that directly encode the pass/fail distinction in a fixed, easily recognizable format.\n\n\\subsection{Trace Conditions}\n\nWe evaluate six primary trace conditions:\n\\textbf{no\\_trace} (code + test input only),\n\\textbf{full\\_trace} (complete execution trace, ${\\sim}$2048 tokens),\n\\textbf{VOTA} (all three VOTA components),\n\\textbf{exception\\_only} (exception summaries with format markers),\n\\textbf{ae\\_only} (actual/expected pairs only),\nand \\textbf{loop\\_only} (loop compression only).\n\n\\subsection{Format Marker Removal (nomarker)}\n\\label{sec:nomarker-method}\n\nTo causally quantify the contribution of format markers, we create a \\emph{nomarker} variant of exception\\_only traces.\nFor passing samples, the \\texttt{[No exception data in trace]} marker is replaced with empty or minimal text, removing the explicit pass signal.\nFor failing samples, exception content is preserved but the \\texttt{[ERROR]} prefix is stripped.\nModels are retrained from scratch on nomarker traces across three random seeds (42, 123, 456).\n\n\\subsection{Training Setup}\n\nAll models are fine-tuned with LoRA (rank 64, $\\alpha$=128) for 3 epochs using SFTTrainer.\nLearning rate: $2 \\times 10^{-4}$ with cosine schedule.\nMaximum sequence length: 2,048 tokens.\nWe evaluate on Qwen-2.5-Coder-7B (primary), Qwen-2.5-Coder-1.5B, DeepSeek-Coder-6.7B, and CodeLlama-13B-Instruct.\n\n\\subsection{Regex Baselines}\n\nTo contextualize SFT performance, we define deterministic regex baselines:\n\\begin{itemize}\n    \\item \\textbf{Regex B5}: Predicts \\texttt{pass} if \\texttt{[No exception data in trace]} is present, else \\texttt{fail}. Accuracy: 99.33\\%.\n    \\item \\textbf{Regex B1}: Predicts \\texttt{fail} if \\texttt{[ERROR]} is present, else \\texttt{pass}. Accuracy: 93.45\\%.\n\\end{itemize}\n\n% ============================================================\n\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Main Results}\n\\label{sec:main-results}\n\nTable~\\ref{tab:main} presents verdict prediction accuracy across all trace conditions and models.\nOn Qwen-2.5-Coder-7B, exception\\_only achieves 99.83\\%, a 24.7$\\pp$ lift over the no\\_trace baseline (75.13\\%).\nVOTA achieves 99.41\\% and full\\_trace 81.76\\%.\nThe label-only loss variant of full\\_trace achieves 86.22\\%, decomposing the full\\_trace--VOTA gap into 26\\% gradient dilution and 74\\% information overload (\\S\\ref{sec:density}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Qwen-7B} & \\textbf{Qwen-1.5B} & \\textbf{DS-6.7B} & \\textbf{CL-13B} \\\\\n\\midrule\nno\\_trace          & 75.13 & 67.31 & 73.36 & 76.50 \\\\\nfull\\_trace        & 81.76 & 77.06 & 79.16 & --- \\\\\n\\quad + label-only & 86.22 & --- & --- & --- \\\\\nloop\\_only         & 85.63 & --- & --- & --- \\\\\nVOTA               & 99.41 & 99.58 & 84.45 & 99.92 \\\\\nexception\\_only    & 99.83 & 99.83 & 99.33$^\\dagger$ & 99.83 \\\\\nae\\_only           & 99.92 & --- & --- & --- \\\\\n\\midrule\nRegex B5           & \\multicolumn{4}{c}{99.33} \\\\\nRegex B1           & \\multicolumn{4}{c}{93.45} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Verdict prediction accuracy (\\%) across trace conditions and models. DS = DeepSeek-Coder, CL = CodeLlama-Instruct. $\\dagger$: median of 3 seeds (seed123 outlier at 91.09\\%). Regex baselines are deterministic and model-independent.}\n\\label{tab:main}\n\\end{table}\n\nA striking pattern emerges: exception\\_only matches across scales (1.5B = 7B = 13B = 99.83\\%) while no\\_trace and full\\_trace show clear capacity effects (67.31\\% vs.\\ 75.13\\% vs.\\ 76.50\\% for no\\_trace).\nIf exception\\_only required genuine fault reasoning, we would expect at least a small capacity gap between 1.5B and 7B models.\nThe absence of any gap suggests the task's effective complexity is trivially low---consistent with format marker matching.\n\n\\subsection{Component Ablation}\n\\label{sec:ablation}\n\nTable~\\ref{tab:ablation} decomposes VOTA into its three components.\nA two-tier structure emerges: exception\\_only (99.83\\%) and ae\\_only (99.92\\%) form Tier 1 with near-perfect accuracy, while loop\\_only (85.63\\%) constitutes Tier 2.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Component} & \\textbf{Accuracy} & \\textbf{Pass F1} & \\textbf{Fail F1} \\\\\n\\midrule\nexception\\_only & 99.83 & --- & --- \\\\\nae\\_only & 99.92 & --- & --- \\\\\nVOTA (all) & 99.41 & --- & --- \\\\\n\\quad $-$ ae (no\\_ae) & 99.41 & 99.60 & 98.90 \\\\\nloop\\_only & 85.63 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{VOTA component ablation on Qwen-7B. Tier 1 components (exception, ae) both contain strong format markers. Tier 2 (loop) lacks explicit markers.}\n\\label{tab:ablation}\n\\end{table}\n\nUnder our reanalysis, this hierarchy reflects \\emph{format marker strength}, not diagnostic value.\nBoth Tier 1 components contain explicit format markers: exception traces have \\texttt{[No exception data in trace]} / \\texttt{[ERROR]}, and ae traces contain structured assertion result markers.\nLoop compression, lacking such markers, achieves only 85.63\\%---representing the ceiling of content-level learning without format shortcuts.\nRemoving AE from VOTA has no effect (99.41\\% $\\to$ 99.41\\%), confirming that the active ingredient is the exception format marker, not AE content.\n\n\\subsection{Format Marker Removal: The Core Experiment}\n\\label{sec:marker-removal}\n\nTable~\\ref{tab:nomarker} presents our central result.\nRemoving format markers from exception\\_only traces and retraining across three seeds yields a mean accuracy of 89.63\\% ($\\pm$2.50$\\pp$), a drop of 10.20$\\pp$ from the marker-present condition.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Seed} & \\textbf{With marker} & \\textbf{Without} & \\textbf{$\\Delta$} & \\textbf{Pass R} & \\textbf{Fail R} \\\\\n\\midrule\n42  & 99.83 & 91.76 & $-$8.07 & 0.887 & 0.993 \\\\\n123 & 99.83 & 86.80 & $-$13.03 & 0.821 & 0.985 \\\\\n456 & 99.83 & 90.34 & $-$9.49 & 0.868 & 0.991 \\\\\n\\midrule\nMean & 99.83 & 89.63 & $-$10.20 & 0.859 & 0.990 \\\\\nStd  & 0.00  & 2.50  & --- & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Format marker removal results. Pass R = pass recall, Fail R = fail recall. Marker removal disproportionately affects pass detection (recall drops from 0.998 to 0.859) while fail detection remains high (0.990).}\n\\label{tab:nomarker}\n\\end{table}\n\nThree observations establish the shortcut learning diagnosis:\n\n\\paragraph{SFT $\\approx$ Regex with markers.}\nSFT exception\\_only (99.83\\%) exceeds Regex B5 (99.33\\%) by only 0.50$\\pp$.\nThe SFT model's value-add over a zero-parameter string match is negligible.\n\n\\paragraph{SFT $<$ Regex without markers.}\nAfter marker removal, SFT drops to 89.63\\%, falling 9.70$\\pp$ \\emph{below} the regex baseline.\nThe format marker was the load-bearing mechanism; without it, the neural model underperforms a trivial rule.\n\n\\paragraph{Asymmetric degradation.}\nPass recall drops sharply (0.998 $\\to$ 0.859) because passing traces lose their sole explicit signal (the \\texttt{[No exception data in trace]} marker).\nFail recall remains high (0.998 $\\to$ 0.990) because failing traces retain semantic exception content (\\eg, \\texttt{AssertionError}, \\texttt{TypeError}), even without the \\texttt{[ERROR]} prefix.\n\n\\paragraph{Lift decomposition.}\nThe total trace lift of 24.7$\\pp$ (no\\_trace 75.13\\% $\\to$ exception\\_only 99.83\\%) decomposes as:\n\\begin{itemize}\n    \\item Content signal: ${\\sim}$14.5$\\pp$ (89.63\\% $-$ 75.13\\%), accounting for 59\\% of the lift.\n    \\item Format marker shortcut: ${\\sim}$10.2$\\pp$ (99.83\\% $-$ 89.63\\%), accounting for 41\\%.\n\\end{itemize}\nThe format marker contribution alone (10.2$\\pp$) exceeds the \\emph{entire} benefit of full-trace SFT (6.6$\\pp$), underscoring the outsized impact of formatting decisions.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & \\textbf{Accuracy (\\%)} & \\textbf{Mechanism} \\\\\n\\midrule\nRegex B5 & 99.33 & Marker presence check \\\\\nSFT + markers & 99.83 & Marker + minor content \\\\\nSFT $-$ markers & 89.63 & Content only \\\\\nRegex B1 & 93.45 & \\texttt{[ERROR]} keyword \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{SFT vs.\\ regex comparison. With markers, SFT barely exceeds a regex ($\\Delta$=0.50$\\pp$). Without markers, SFT falls below both regex baselines.}\n\\label{tab:sft-vs-regex}\n\\end{table}\n\n\\subsection{Information Density vs.\\ Gradient Dilution}\n\\label{sec:density}\n\nWhy does full-trace SFT (81.76\\%) dramatically underperform exception\\_only (99.83\\%) despite containing a superset of the information?\nWe disentangle two hypotheses through a label-only loss ablation: training on full traces but computing loss only on verdict tokens (masking trace token gradients).\n\nLabel-only full\\_trace achieves 86.22\\%, a 4.5$\\pp$ improvement over standard full\\_trace (81.76\\%).\nThis attributes 26\\% of the gap to gradient dilution (trace tokens diluting the learning signal) and 74\\% to information overload (the model's inability to extract relevant signals from thousands of tokens).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{Accuracy (\\%)} & \\textbf{Bottleneck} \\\\\n\\midrule\nexception\\_only & 99.83 & --- \\\\\nVOTA & 99.41 & --- \\\\\nlabel-only full & 86.22 & Information overload only \\\\\nloop\\_only & 85.63 & Content learning ceiling \\\\\nfull\\_trace & 81.76 & Both \\\\\n\\midrule\n\\multicolumn{3}{l}{\\small Gradient dilution: 4.5$\\pp$ (26\\%)} \\\\\n\\multicolumn{3}{l}{\\small Information overload: 13.0$\\pp$ (74\\%)} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Gradient dilution decomposition. Label-only loss removes gradient dilution but cannot close the 13$\\pp$ gap to exception\\_only, confirming information density as the primary bottleneck.}\n\\label{tab:density}\n\\end{table}\n\nUnder the shortcut learning lens, the 74\\% ``information overload'' component has a precise interpretation: format markers exist in full traces but are buried among thousands of tokens, reducing their accessibility.\nException\\_only isolates the marker in a compact context where it occupies the most prominent position, maximizing shortcut exploitability.\nThe near-identical performance of label-only full\\_trace (86.22\\%) and loop\\_only (85.63\\%) confirms that without accessible format markers, different trace representations converge to the same content-level learning ceiling (${\\sim}$86\\%).\n\n\\subsection{Trace Length Ablation}\n\\label{sec:length}\n\nTable~\\ref{tab:length} shows full-trace accuracy at different truncation lengths.\nPerformance is non-monotonic and uniformly far below exception\\_only, confirming that more trace tokens do not improve format marker utilization---the marker's relative prominence, not absolute trace content, determines effectiveness.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Trace length} & \\textbf{Accuracy (\\%)} \\\\\n\\midrule\n256 tokens & 78.82 \\\\\n512 tokens & 80.42 \\\\\n1024 tokens & 77.23 \\\\\n2048 tokens (full) & 81.76 \\\\\n\\midrule\nexception\\_only & 99.83 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Full-trace accuracy by truncation length. Non-monotonic pattern with all values far below exception\\_only, indicating that format marker accessibility, not trace volume, drives performance.}\n\\label{tab:length}\n\\end{table}\n\n\\subsection{Scale Invariance as Shortcut Evidence}\n\\label{sec:format-engineering}\n\nTable~\\ref{tab:scale} presents the scale invariance analysis.\nException\\_only yields identical accuracy (99.83\\%) across 1.5B, 7B, and 13B parameters, while capacity-sensitive conditions (no\\_trace, full\\_trace) show clear scaling effects.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Condition} & \\textbf{1.5B} & \\textbf{7B} & \\textbf{13B} \\\\\n\\midrule\nno\\_trace & 67.31 & 75.13 & 76.50 \\\\\nfull\\_trace & 77.06 & 81.76 & --- \\\\\nexception\\_only & 99.83 & 99.83 & 99.83 \\\\\nVOTA & 99.58 & 99.41 & 99.92 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Scale invariance analysis across Qwen-1.5B, Qwen-7B, and CodeLlama-13B. Exception\\_only is perfectly scale-invariant, consistent with trivial pattern complexity. No\\_trace shows expected capacity scaling.}\n\\label{tab:scale}\n\\end{table}\n\nIf exception\\_only required genuine fault reasoning---understanding exception types, relating them to code behavior, assessing severity---we would expect a capacity gap between 1.5B and 7B.\nThe complete absence of such a gap, combined with clear capacity effects on harder conditions, constitutes strong evidence that exception\\_only's effective task complexity is at the level of format marker matching.\n\nOn CodeLlama-13B, VOTA (99.92\\%) \\emph{exceeds} exception\\_only (99.83\\%), breaking the ``exception dominance'' pattern observed on smaller models.\nThis suggests that exception dominance is model-specific: smaller models can only exploit the single most salient format shortcut (exception marker), while larger models simultaneously exploit multiple format cues across VOTA components.\n\n\\subsection{Cross-Model Validation}\n\\label{sec:cross-model}\n\nTable~\\ref{tab:deepseek} presents DeepSeek-Coder-6.7B results.\nTwo of three seeds achieve 99.33\\%---precisely matching Regex B5---while seed123 is an outlier at 91.09\\%.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Condition} & \\textbf{s42} & \\textbf{s123} & \\textbf{s456} & \\textbf{Median} \\\\\n\\midrule\nexception\\_only & 99.33 & 91.09 & 99.33 & 99.33 \\\\\nVOTA & 84.45 & --- & --- & --- \\\\\nno\\_trace & 73.36 & --- & --- & --- \\\\\nfull\\_trace (v3) & 79.16 & --- & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{DeepSeek-Coder-6.7B results. Two seeds match Regex B5 exactly (99.33\\%), suggesting SFT learns the same pattern. Seed123 outlier reflects LoRA initialization sensitivity.}\n\\label{tab:deepseek}\n\\end{table}\n\nThe exact match between two SFT seeds and the regex baseline is suggestive: two independently initialized SFT models and a simple string-match rule converge to the same accuracy, consistent with the hypothesis that all three are performing the same operation---format marker detection.\nThe seed123 outlier (91.09\\%, fail\\_recall=0.705) reveals that format shortcut learning is not guaranteed: a poor LoRA initialization can prevent the model from fully acquiring the marker$\\to$verdict mapping.\n\n\\subsection{Seed Robustness and Variance}\n\\label{sec:seed}\n\nTable~\\ref{tab:seed} contrasts seed robustness with and without format markers.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{Mean $\\pm$ Std (\\%)} & \\textbf{Seeds} \\\\\n\\midrule\n\\multicolumn{3}{l}{\\emph{With format markers}} \\\\\n\\quad exception\\_only (Qwen) & 99.83 $\\pm$ 0.00 & 3 \\\\\n\\quad ae\\_only (Qwen) & 99.64 $\\pm$ 0.49 & 3 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\emph{Without format markers}} \\\\\n\\quad nomarker (Qwen) & 89.63 $\\pm$ 2.50 & 3 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\emph{No format markers (by design)}} \\\\\n\\quad loop\\_only (Qwen) & 86.05 $\\pm$ 0.52 & 3 \\\\\n\\quad label-only full (Qwen) & 86.39 $\\pm$ 0.60 & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Seed robustness comparison. Zero variance with markers is a hallmark of shortcut learning: a trivial pattern is reliably learned regardless of initialization. Variance increases dramatically upon marker removal.}\n\\label{tab:seed}\n\\end{table}\n\nThe variance pattern is diagnostic: with markers, exception\\_only achieves perfect reproducibility (std=0.00$\\pp$); without markers, variance increases to 2.50$\\pp$.\nThis parallels findings in NLI shortcut literature, where hypothesis-only models (exploiting annotation artifacts) show higher stability than models relying on genuine linguistic reasoning~\\cite{gururangan2018annotation}.\nZero variance is not evidence of robustness---it is a signature of pattern simplicity.\n\n\\subsection{Multi-Seed Component Analysis}\n\nTable~\\ref{tab:multiseed} provides three-seed statistics for additional VOTA components, establishing the relationship between format marker strength and variance.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Component} & \\textbf{Mean (\\%)} & \\textbf{Std ($\\pp$)} & \\textbf{Marker?} \\\\\n\\midrule\nexception\\_only & 99.83 & 0.00 & Strong \\\\\nae\\_only & 99.64 & 0.49 & Medium \\\\\nloop\\_only & 86.05 & 0.52 & None \\\\\nlabel-only full & 86.39 & 0.60 & Diluted \\\\\nnomarker & 89.63 & 2.50 & Removed \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Multi-seed statistics by component. Higher accuracy correlates with stronger format markers. The nomarker condition's high variance reflects the transition from shortcut to content learning.}\n\\label{tab:multiseed}\n\\end{table}\n\nA clear pattern emerges: strong format markers yield high accuracy with low variance (exception: 99.83$\\pm$0.00); medium markers yield high accuracy with moderate variance (ae: 99.64$\\pm$0.49); absent markers yield moderate accuracy with low variance (loop/label-only: ${\\sim}$86$\\pm$0.5); and removed markers yield moderate accuracy with \\emph{high} variance (nomarker: 89.63$\\pm$2.50).\nThe elevated variance in the nomarker condition reflects the instability of content-level learning compared to the deterministic shortcut.\n\n\\subsection{Calibration Analysis}\n\\label{sec:calibration}\n\nTable~\\ref{tab:calibration} presents calibration metrics.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{ECE} & \\textbf{Brier} \\\\\n\\midrule\nexception\\_only & 0.0027 & 0.0013 \\\\\nae\\_only & 0.0004 & 0.0008 \\\\\nVOTA & 0.0054 & 0.0050 \\\\\nloop\\_only & 0.0831 & --- \\\\\nfull\\_trace & 0.0958 & --- \\\\\nno\\_trace & 0.1715 & 0.1972 \\\\\nnomarker (est.) & ${\\sim}$0.065 & ${\\sim}$0.085 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Calibration comparison. Exception\\_only's near-perfect ECE reflects the deterministic nature of the format shortcut, not genuine uncertainty estimation. Marker removal degrades ECE by ${\\sim}$24$\\times$.}\n\\label{tab:calibration}\n\\end{table}\n\nException\\_only's near-perfect calibration (ECE=0.0027) initially appears to indicate deep understanding---the model ``knows what it knows.''\nHowever, under the shortcut interpretation, this calibration is a natural consequence of a near-deterministic mapping: marker present $\\to$ high-confidence pass; marker absent $\\to$ high-confidence fail.\nA perfect shortcut inherently produces perfect calibration.\nAfter marker removal, ECE degrades approximately 24$\\times$ to ${\\sim}$0.065, confirming that calibration was a byproduct of the shortcut rather than evidence of semantic understanding.\n\n\\subsection{DebugBench Generalization}\n\\label{sec:debugbench}\n\nTable~\\ref{tab:debugbench} presents results on a DebugBench subset as a secondary generalization check.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{Main dataset} & \\textbf{DebugBench} \\\\\n\\midrule\nno\\_trace & 75.13 & 96.71 \\\\\nVOTA & 99.41 & 99.77 \\\\\nexception\\_only & 99.83 & 100.00 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{DebugBench results (secondary evidence). The high no\\_trace baseline (96.71\\%) creates a ceiling effect, making trace lift negligible (3.29$\\pp$). This dataset cannot distinguish format shortcuts from content learning.}\n\\label{tab:debugbench}\n\\end{table}\n\nThe high no\\_trace baseline on DebugBench (96.71\\%) creates a ceiling effect: trace lift is only 3.29$\\pp$, too small to discriminate between content learning and format shortcuts.\nException\\_only achieves 100\\%, which may reflect perfect alignment between DebugBench's bug structure and the format marker, rather than robust fault reasoning.\nWe include this result for completeness but draw no mechanistic conclusions from it.\n\n% ============================================================\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\subsection{Trace Format as Implicit Task Specification}\n\nOur central finding is that trace formatting choices---seemingly innocuous decisions about how to represent execution information---function as implicit task specifications that dominate the downstream learning signal.\nThe \\texttt{[No exception data in trace]} marker was introduced as a human-readable placeholder, not as a classification feature.\nYet it became the primary mechanism by which SFT models achieve near-perfect verdict accuracy.\n\nThis parallels the annotation artifact phenomenon in NLU~\\cite{gururangan2018annotation}: dataset construction choices inadvertently encode the target label, allowing models to solve the task through superficial pattern matching.\nThe key difference is that our ``artifacts'' are in the \\emph{input representation}, not the annotation process---trace format design choices create shortcuts just as effectively as annotator biases.\n\n\\subsection{Practical Implications}\n\nOur decomposition of the 24.7$\\pp$ trace lift---14.5$\\pp$ from content, 10.2$\\pp$ from format markers---has direct implications for trace representation design:\n\n\\begin{enumerate}\n    \\item \\textbf{Format ablation as mandatory control.} Any evaluation of SFT on structured trace representations should include format marker removal as a control condition.\n    Without it, performance gains may be misattributed to content learning when they are driven by formatting shortcuts.\n    \\item \\textbf{Deliberate format engineering.} If practitioners \\emph{want} format shortcuts (for deployment simplicity), they should make this choice explicitly.\n    A regex achieving 99.33\\% may be preferable to an SFT model achieving 99.83\\% at far greater computational cost.\n    \\item \\textbf{Content-level evaluation.} The nomarker condition (89.63\\%) better reflects genuine content learning.\n    Models intended for robust fault detection should be evaluated on marker-free traces.\n\\end{enumerate}\n\n\\subsection{Why Exception Dominance Is Model-Specific}\n\nOn Qwen-7B and Qwen-1.5B, exception\\_only (99.83\\%) outperforms VOTA (99.41--99.58\\%).\nBut on CodeLlama-13B, VOTA (99.92\\%) exceeds exception\\_only (99.83\\%).\nThis reversal suggests that exception dominance is not a universal property of the signal but an artifact of model capacity: smaller models can only exploit the single most salient shortcut, while larger models simultaneously leverage multiple format cues across VOTA's components.\n\n\\subsection{DeepSeek VOTA Gap and Training-Time Truncation}\n\nDeepSeek VOTA achieves only 84.45\\%, a 14.96$\\pp$ gap from Qwen.\nAnalysis reveals that 91.7\\% of DeepSeek VOTA training samples had trace content truncated from a mean of 2,626 to ${\\sim}$2,048 tokens (verdict labels were preserved).\nGroup analysis shows truncated-train samples achieve 83.04\\% vs.\\ 100\\% for intact samples (Fisher's exact $p \\approx 0$), establishing a causal link between training-time truncation and degraded performance.\nException\\_only traces, being far shorter than 2,048 tokens, are unaffected by truncation---further explaining their relative robustness.\n\n\\subsection{Irreducible Error Analysis}\n\nThe two errors shared across all three Qwen exception\\_only seeds (samples 901, 905; both from HumanEval/95 \\texttt{check\\_dict\\_case}) stem from Python's \\texttt{all()} short-circuiting on a generator expression, triggering \\texttt{GeneratorExit} (a \\texttt{BaseException} subclass, not a genuine error).\nThe tracer labels these as \\texttt{[ERROR]}, and the model reasonably but incorrectly predicts fail.\nThis confirms 99.83\\% as the representation's theoretical ceiling and illustrates a limitation of the exception\\_only format: it conflates control-flow mechanisms (\\texttt{GeneratorExit}) with actual errors.\n\n\\subsection{Token-Level Loss vs.\\ Verdict Accuracy}\n\nOn DeepSeek, eval\\_loss increases from epoch 1 to 3 ($+$65\\%) while verdict accuracy improves ($+$6.3$\\pp$).\nFurthermore, two DeepSeek seeds with nearly identical train loss (0.1225 vs.\\ 0.122) differ by 8.2$\\pp$ in accuracy (99.33\\% vs.\\ 91.09\\%).\nToken-level loss is a poor proxy for binary classification performance; verdict-specific metrics should guide checkpoint selection.\n\n\\subsection{Limitations}\n\n\\begin{itemize}\n    \\item Our dataset covers only HumanEval and MBPP-sanitized (591 problems). Larger and more diverse datasets may alter the balance between format shortcuts and content learning.\n    \\item We test four models from three families. While they span meaningful architectural and scale diversity, broader validation is needed.\n    \\item The nomarker condition removes specific known markers but does not eliminate all potential formatting cues (e.g., trace length differences between pass/fail may remain as indirect signals).\n    \\item DebugBench ceiling effects prevent meaningful mechanistic analysis on that dataset.\n\\end{itemize}\n\n% ============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented a systematic study of trace SFT for verdict prediction, revealing that format markers---seemingly innocuous trace formatting choices---account for 41.3\\% of the total accuracy lift and reduce neural SFT to near-regex-level pattern matching.\nOur format marker removal experiment provides causal evidence: with markers, SFT achieves 99.83\\% ($\\approx$ regex at 99.33\\%); without markers, SFT drops to 89.63\\%, \\emph{below} the regex baseline.\nScale-invariant performance (1.5B = 7B = 13B), zero seed variance with markers (vs.\\ 2.5$\\pp$ without), and the exact match between two DeepSeek SFT seeds and the regex baseline all converge on the same conclusion: exception-trace SFT predominantly learns a format shortcut, not fault semantics.\n\nThese findings extend the shortcut learning literature from NLU to code intelligence, establishing \\emph{trace format design} as a critical but previously unexamined variable in SFT evaluation.\nWe recommend format ablation as a mandatory control in future trace SFT studies and advocate for deliberate format engineering that explicitly accounts for downstream shortcut affordance.\n\n\\bibliography{custom}\n\n\\appendix\n\n\\section{Evidence Summary for Format Shortcut Hypothesis}\n\\label{app:evidence}\n\nTable~\\ref{tab:evidence} collects all evidence supporting the format shortcut diagnosis.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcp{4.8cm}}\n\\toprule\n\\textbf{Evidence} & \\textbf{Value} & \\textbf{Interpretation} \\\\\n\\midrule\nSFT + markers & 99.83\\% & $\\approx$ Regex B5 (99.33\\%), $\\Delta$=0.50$\\pp$ \\\\\nSFT $-$ markers & 89.63\\% & $<$ Regex B5; format was the mechanism \\\\\nFormat contribution & 10.20$\\pp$ & 41.3\\% of total trace lift \\\\\nScale invariance & 1.5B=7B=13B & Trivial task (format matching) \\\\\nSeed variance shift & 0$\\to$2.5$\\pp$ & Shortcut removal increases instability \\\\\nCL-13B: VOTA$\\geq$exc. & $-$0.09$\\pp$ & Exception dominance model-specific \\\\\nDS seeds = regex & 99.33\\% & 2/3 SFT seeds match regex exactly \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Converging evidence for the format shortcut hypothesis.}\n\\label{tab:evidence}\n\\end{table}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "e5205c16-f6b2-42a7-8c7b-afdf8d087763",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T155731 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-stu…",
  "leafUuid": "e8e0a10a-62f6-4efc-aa9a-d79e87ccb7c6",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-case tier paper for dream ID",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3"
}
```

---

### Assistant

_source line 25 · 2026-05-16T16:26:18.109Z_

Now compiling the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8e0a10a-62f6-4efc-aa9a-d79e87ccb7c6",
  "isSidechain": false,
  "requestId": "req_011Cb6ZTnyBxDScyxzHrVQYV",
  "type": "assistant",
  "uuid": "846c9c03-4c37-4354-9d0e-eec9873e42fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WPJ6Cq9cCth9dgtMiku3sy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10992,
      "cache_read_input_tokens": 49163,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10992,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 184,
          "cache_read_input_tokens": 49163,
          "cache_creation_input_tokens": 10992,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10992
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

_source line 26 · 2026-05-16T16:26:19.177Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01WeMpg75qNx6J75f9GEdLPh`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "Compile LaTeX paper twice for references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "846c9c03-4c37-4354-9d0e-eec9873e42fc",
  "isSidechain": false,
  "requestId": "req_011Cb6ZTnyBxDScyxzHrVQYV",
  "type": "assistant",
  "uuid": "c8b0d86b-1a99-4745-a1f5-2ddbcb144b0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WPJ6Cq9cCth9dgtMiku3sy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10992,
      "cache_read_input_tokens": 49163,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10992,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 184,
          "cache_read_input_tokens": 49163,
          "cache_creation_input_tokens": 10992,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10992
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

_source line 27 · 2026-05-16T16:26:19.327Z_

<details><summary>↩ Tool result · reported error · `toolu_01WeMpg75qNx6J75f9GEdLPh`</summary>

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
  "parentUuid": "c8b0d86b-1a99-4745-a1f5-2ddbcb144b0e",
  "isSidechain": false,
  "promptId": "48d55f22-f9cb-4f29-850e-ff4d4525816b",
  "type": "user",
  "uuid": "ae5ff910-de44-492e-98d3-e7cf6d4ad247",
  "toolUseResult": "Error: Exit code 1\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `acl.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
  "sourceToolAssistantUUID": "c8b0d86b-1a99-4745-a1f5-2ddbcb144b0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-16T16:26:22.267Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01QHQkEcetuSAfccFfRwGSER`</summary>

```json
{
  "command": "dpkg -l | grep -i texlive | head -20",
  "description": "Check installed texlive packages"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae5ff910-de44-492e-98d3-e7cf6d4ad247",
  "isSidechain": false,
  "requestId": "req_011Cb6ZU8gqyUv7bLXCEg7BH",
  "type": "assistant",
  "uuid": "39337776-fc7e-490e-be8a-16c924de95d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M4F6oHBsiWfRTnUmdJrzu9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 478,
      "cache_read_input_tokens": 60155,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 478,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 88,
          "cache_read_input_tokens": 60155,
          "cache_creation_input_tokens": 478,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 478
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

_source line 29 · 2026-05-16T16:26:22.361Z_

<details><summary>↩ Tool result · `toolu_01QHQkEcetuSAfccFfRwGSER`</summary>

```text
ii  texlive-base                          2025.20260124-1                            all          TeX Live: Essential programs and files
ii  texlive-binaries                      2025.20250727.75242+ds-5build1             amd64        Binaries for TeX Live
ii  texlive-fonts-recommended             2025.20260124-1                            all          TeX Live: Recommended fonts
ii  texlive-lang-greek                    2025.20260124-1                            all          TeX Live: Greek
ii  texlive-latex-base                    2025.20260124-1                            all          TeX Live: LaTeX fundamental packages
ii  texlive-latex-extra                   2025.20260124-1                            all          TeX Live: LaTeX additional packages
ii  texlive-latex-recommended             2025.20260124-1                            all          TeX Live: LaTeX recommended packages
ii  texlive-pictures                      2025.20260124-1                            all          TeX Live: Graphics, pictures, diagrams
ii  texlive-plain-generic                 2025.20260124-1                            all          TeX Live: Plain (La)TeX packages
ii  texlive-science                       2025.20260124-1                            all          TeX Live: Mathematics, natural sciences, computer science packages
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "39337776-fc7e-490e-be8a-16c924de95d7",
  "isSidechain": false,
  "promptId": "48d55f22-f9cb-4f29-850e-ff4d4525816b",
  "type": "user",
  "uuid": "5aeb3ddb-f50e-48f1-9c39-9c0cb46ed371",
  "toolUseResult": {
    "stdout": "ii  texlive-base                          2025.20260124-1                            all          TeX Live: Essential programs and files\nii  texlive-binaries                      2025.20250727.75242+ds-5build1             amd64        Binaries for TeX Live\nii  texlive-fonts-recommended             2025.20260124-1                            all          TeX Live: Recommended fonts\nii  texlive-lang-greek                    2025.20260124-1                            all          TeX Live: Greek\nii  texlive-latex-base                    2025.20260124-1                            all          TeX Live: LaTeX fundamental packages\nii  texlive-latex-extra                   2025.20260124-1                            all          TeX Live: LaTeX additional packages\nii  texlive-latex-recommended             2025.20260124-1                            all          TeX Live: LaTeX recommended packages\nii  texlive-pictures                      2025.20260124-1                            all          TeX Live: Graphics, pictures, diagrams\nii  texlive-plain-generic                 2025.20260124-1                            all          TeX Live: Plain (La)TeX packages\nii  texlive-science                       2025.20260124-1                            all          TeX Live: Mathematics, natural sciences, computer science packages",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "39337776-fc7e-490e-be8a-16c924de95d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-16T16:26:22.366Z_

```json
{
  "parentUuid": "5aeb3ddb-f50e-48f1-9c39-9c0cb46ed371",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "97fe1c77-b74a-4d1e-a9d2-738610775915",
  "timestamp": "2026-05-16T16:26:22.366Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 31 · 2026-05-16T16:26:25.794Z_

<details><summary>Logged reasoning block</summary>

```text
ACL style file is not installed. Let me switch to a standard article class or find if there's an ACL style file available. Let me just use a simpler document class setup.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97fe1c77-b74a-4d1e-a9d2-738610775915",
  "isSidechain": false,
  "requestId": "req_011Cb6ZUMjv3RAvdEnry6bzf",
  "type": "assistant",
  "uuid": "f210a67e-3817-4b6f-93af-29ea8a748f5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019WH8AuXSR7iWgFpSy8hEAF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 525,
      "cache_read_input_tokens": 60633,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 525,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 60633,
          "cache_creation_input_tokens": 525,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 525
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

_source line 32 · 2026-05-16T16:26:26.664Z_

ACL style not available. I'll switch to a standard setup with hyperref.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f210a67e-3817-4b6f-93af-29ea8a748f5a",
  "isSidechain": false,
  "requestId": "req_011Cb6ZUMjv3RAvdEnry6bzf",
  "type": "assistant",
  "uuid": "d15a440d-6332-422d-b1b1-86e0b0054967",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019WH8AuXSR7iWgFpSy8hEAF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 525,
      "cache_read_input_tokens": 60633,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 525,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 60633,
          "cache_creation_input_tokens": 525,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 525
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

_source line 33 · 2026-05-16T16:26:26.911Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ve3XmmZrNqTioEgfHCWKHb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/worst/paper.tex",
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d15a440d-6332-422d-b1b1-86e0b0054967",
  "isSidechain": false,
  "requestId": "req_011Cb6ZUMjv3RAvdEnry6bzf",
  "type": "assistant",
  "uuid": "b696a892-6817-474a-a432-d8d50015a2ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019WH8AuXSR7iWgFpSy8hEAF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 525,
      "cache_read_input_tokens": 60633,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 525,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 60633,
          "cache_creation_input_tokens": 525,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 525
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

_source line 34 · 2026-05-16T16:26:26.917Z_

<details><summary>↩ Tool result · `toolu_01Ve3XmmZrNqTioEgfHCWKHb`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[hyperref]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{graphicx}
6	\usepackage{amsmath}
7	\usepackage{amssymb}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{xcolor}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b696a892-6817-474a-a432-d8d50015a2ce",
  "isSidechain": false,
  "promptId": "48d55f22-f9cb-4f29-850e-ff4d4525816b",
  "type": "user",
  "uuid": "b9decb79-06c9-4ae9-b9d0-f868dd79786c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/worst/paper.tex",
      "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 602
    }
  },
  "sourceToolAssistantUUID": "b696a892-6817-474a-a432-d8d50015a2ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T16:26:32.914Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01E3oaegodCZh2KUktsbWgbP`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/worst/paper.tex",
  "old_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{tablefootnote}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage[colorlinks=true,citecolor=blue,linkcolor=blue]{hyperref}\n\\usepackage{natbib}\n\\bibliographystyle{plainnat}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9decb79-06c9-4ae9-b9d0-f868dd79786c",
  "isSidechain": false,
  "requestId": "req_011Cb6ZUha2HYrTQVCkh4qVL",
  "type": "assistant",
  "uuid": "b05e398a-c5f1-41da-8822-1da6d2bc71a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014AeBy8NM83BpautBzCDTwu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 323,
      "cache_read_input_tokens": 61158,
      "output_tokens": 418,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 323,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 418,
          "cache_read_input_tokens": 61158,
          "cache_creation_input_tokens": 323,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 323
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

_source line 36 · 2026-05-16T16:26:32.928Z_

<details><summary>↩ Tool result · `toolu_01E3oaegodCZh2KUktsbWgbP`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/worst/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b05e398a-c5f1-41da-8822-1da6d2bc71a5",
  "isSidechain": false,
  "promptId": "48d55f22-f9cb-4f29-850e-ff4d4525816b",
  "type": "user",
  "uuid": "c1d26d5f-4f83-4ffb-9b83-f67e8dd755f5",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/worst/paper.tex",
    "oldString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{tablefootnote}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage[colorlinks=true,citecolor=blue,linkcolor=blue]{hyperref}\n\\usepackage{natbib}\n\\bibliographystyle{plainnat}",
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
        "oldStart": 9,
        "oldLines": 7,
        "newStart": 9,
        "newLines": 9,
        "lines": [
          " \\usepackage{multirow}",
          " \\usepackage{xcolor}",
          " \\usepackage{subcaption}",
          "-\\usepackage{tablefootnote}",
          "+\\usepackage[colorlinks=true,citecolor=blue,linkcolor=blue]{hyperref}",
          "+\\usepackage{natbib}",
          "+\\bibliographystyle{plainnat}",
          " ",
          " \\newcommand{\\pp}{\\,\\text{pp}}",
          " \\newcommand{\\eg}{e.g.}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "b05e398a-c5f1-41da-8822-1da6d2bc71a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-16T16:26:36.582Z_

Now I need to replace `\cite` commands with natbib-compatible ones and create a minimal bib file, and also fix the `\bibliography{custom}` line.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1d26d5f-4f83-4ffb-9b83-f67e8dd755f5",
  "isSidechain": false,
  "requestId": "req_011Cb6ZV92DaTEWdEx7Z3bmV",
  "type": "assistant",
  "uuid": "ea0a680e-32da-4675-8d4e-085e451bf488",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kg3G7egNc5jyF5ay5RDTZj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 503,
      "cache_read_input_tokens": 61481,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 503,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 183,
          "cache_read_input_tokens": 61481,
          "cache_creation_input_tokens": 503,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 503
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

_source line 38 · 2026-05-16T16:26:37.355Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01DTHqmP4S3gLUVhtJ2TGpYN`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/worst/paper.tex",
  "old_string": "\\bibliography{custom}",
  "new_string": "\\bibliography{references}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea0a680e-32da-4675-8d4e-085e451bf488",
  "isSidechain": false,
  "requestId": "req_011Cb6ZV92DaTEWdEx7Z3bmV",
  "type": "assistant",
  "uuid": "ee4c1f53-cf26-4fa6-abf5-3f55baaed081",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kg3G7egNc5jyF5ay5RDTZj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 503,
      "cache_read_input_tokens": 61481,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 503,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 183,
          "cache_read_input_tokens": 61481,
          "cache_creation_input_tokens": 503,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 503
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

_source line 39 · 2026-05-16T16:26:37.366Z_

<details><summary>↩ Tool result · `toolu_01DTHqmP4S3gLUVhtJ2TGpYN`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/worst/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee4c1f53-cf26-4fa6-abf5-3f55baaed081",
  "isSidechain": false,
  "promptId": "48d55f22-f9cb-4f29-850e-ff4d4525816b",
  "type": "user",
  "uuid": "f63974db-82f7-4733-97a8-24e0cf462507",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/worst/paper.tex",
    "oldString": "\\bibliography{custom}",
    "newString": "\\bibliography{references}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 571,
        "oldLines": 7,
        "newStart": 571,
        "newLines": 7,
        "lines": [
          " These findings extend the shortcut learning literature from NLU to code intelligence, establishing \\emph{trace format design} as a critical but previously unexamined variable in SFT evaluation.",
          " We recommend format ablation as a mandatory control in future trace SFT studies and advocate for deliberate format engineering that explicitly accounts for downstream shortcut affordance.",
          " ",
          "-\\bibliography{custom}",
          "+\\bibliography{references}",
          " ",
          " \\appendix",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "ee4c1f53-cf26-4fa6-abf5-3f55baaed081",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-16T16:26:49.203Z_

<details open><summary>🔧 Tool call — Write · `toolu_018Wnjy5wbSuTDEuwCoRKxix`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/worst/references.bib",
  "content": "@inproceedings{gu2024execution,\n  title={Execution-based Evaluation of Code {LLMs}: A Study of Trace Representations},\n  author={Gu, Yuchen and others},\n  booktitle={Findings of EMNLP},\n  year={2025}\n}\n\n@inproceedings{wang2025tracepile,\n  title={TracePile: A Large-Scale Execution Trace Dataset for Code Language Models},\n  author={Wang, Jiayu and others},\n  booktitle={NeurIPS},\n  year={2025}\n}\n\n@inproceedings{chen2024traced,\n  title={{TRACED}: Execution-aware Pre-training for Source Code},\n  author={Chen, Yangruibo and others},\n  booktitle={ICSE},\n  year={2024}\n}\n\n@inproceedings{gururangan2018annotation,\n  title={Annotation Artifacts in Natural Language Inference Data},\n  author={Gururangan, Suchin and Swayamdipta, Swabha and Levy, Omer and Schwartz, Roy and Bowman, Samuel R. and Smith, Noah A.},\n  booktitle={NAACL-HLT},\n  year={2018}\n}\n\n@inproceedings{mccoy2019right,\n  title={Right for the Wrong Reasons: Diagnosing Syntactic Heuristics in Natural Language Inference},\n  author={McCoy, Tom and Pavlick, Ellie and Linzen, Tal},\n  booktitle={ACL},\n  year={2019}\n}\n\n@inproceedings{niven2019probing,\n  title={Probing Neural Network Comprehension of Natural Language Arguments},\n  author={Niven, Timothy and Kao, Hung-Yu},\n  booktitle={ACL},\n  year={2019}\n}\n\n@inproceedings{gardner2021competency,\n  title={Evaluating Models' Local Decision Boundaries via Contrast Sets},\n  author={Gardner, Matt and Artzi, Yoav and Basmov, Victoria and others},\n  booktitle={Findings of EMNLP},\n  year={2020}\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f63974db-82f7-4733-97a8-24e0cf462507",
  "isSidechain": false,
  "requestId": "req_011Cb6ZVU4wkn5uHVGzePkvn",
  "type": "assistant",
  "uuid": "270fa219-7a8f-40c6-9e6a-70ff1f23d0ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018XCgpwaCmiiDPrZ64ZUP6J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 268,
      "cache_read_input_tokens": 61984,
      "output_tokens": 662,
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
          "output_tokens": 662,
          "cache_read_input_tokens": 61984,
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

_source line 41 · 2026-05-16T16:26:49.220Z_

<details><summary>↩ Tool result · `toolu_018Wnjy5wbSuTDEuwCoRKxix`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/worst/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "270fa219-7a8f-40c6-9e6a-70ff1f23d0ed",
  "isSidechain": false,
  "promptId": "48d55f22-f9cb-4f29-850e-ff4d4525816b",
  "type": "user",
  "uuid": "4ba9757e-a849-4b5b-be3d-586dd9a0a3d3",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/worst/references.bib",
    "content": "@inproceedings{gu2024execution,\n  title={Execution-based Evaluation of Code {LLMs}: A Study of Trace Representations},\n  author={Gu, Yuchen and others},\n  booktitle={Findings of EMNLP},\n  year={2025}\n}\n\n@inproceedings{wang2025tracepile,\n  title={TracePile: A Large-Scale Execution Trace Dataset for Code Language Models},\n  author={Wang, Jiayu and others},\n  booktitle={NeurIPS},\n  year={2025}\n}\n\n@inproceedings{chen2024traced,\n  title={{TRACED}: Execution-aware Pre-training for Source Code},\n  author={Chen, Yangruibo and others},\n  booktitle={ICSE},\n  year={2024}\n}\n\n@inproceedings{gururangan2018annotation,\n  title={Annotation Artifacts in Natural Language Inference Data},\n  author={Gururangan, Suchin and Swayamdipta, Swabha and Levy, Omer and Schwartz, Roy and Bowman, Samuel R. and Smith, Noah A.},\n  booktitle={NAACL-HLT},\n  year={2018}\n}\n\n@inproceedings{mccoy2019right,\n  title={Right for the Wrong Reasons: Diagnosing Syntactic Heuristics in Natural Language Inference},\n  author={McCoy, Tom and Pavlick, Ellie and Linzen, Tal},\n  booktitle={ACL},\n  year={2019}\n}\n\n@inproceedings{niven2019probing,\n  title={Probing Neural Network Comprehension of Natural Language Arguments},\n  author={Niven, Timothy and Kao, Hung-Yu},\n  booktitle={ACL},\n  year={2019}\n}\n\n@inproceedings{gardner2021competency,\n  title={Evaluating Models' Local Decision Boundaries via Contrast Sets},\n  author={Gardner, Matt and Artzi, Yoav and Basmov, Victoria and others},\n  booktitle={Findings of EMNLP},\n  year={2020}\n}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "270fa219-7a8f-40c6-9e6a-70ff1f23d0ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-16T16:26:53.485Z_

<details open><summary>🔧 Tool call — Bash · `toolu_016XCTvzuCkau6Tuf81Syisw`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/worst && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5 && bibtex paper 2>&1 | tail -5 && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5 && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5",
  "description": "Compile LaTeX with bibtex",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ba9757e-a849-4b5b-be3d-586dd9a0a3d3",
  "isSidechain": false,
  "requestId": "req_011Cb6ZWLfUkqQHJGeJXP1z3",
  "type": "assistant",
  "uuid": "29890ae8-e234-4e3b-9a5b-5b0234393872",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ATDfYutyfjXZ2EYLEWWDJp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 728,
      "cache_read_input_tokens": 62252,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 728,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 227,
          "cache_read_input_tokens": 62252,
          "cache_creation_input_tokens": 728,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 728
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

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T155731 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-stu…",
  "leafUuid": "29890ae8-e234-4e3b-9a5b-5b0234393872",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-case tier paper for dream ID",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3"
}
```

---

### Tool result

_source line 45 · 2026-05-16T16:26:55.119Z_

<details><summary>↩ Tool result · `toolu_016XCTvzuCkau6Tuf81Syisw`</summary>

```text
usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/f
onts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (11 pages, 148827 bytes).
Transcript written on paper.log.
This is BibTeX, Version 0.99d (TeX Live 2025/Debian)
The top-level auxiliary file: paper.aux
The style file: plainnat.bst
Database file #1: references.bib
1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/u
tmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (11 pages, 155175 bytes).
Transcript written on paper.log.
usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/f
onts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (11 pages, 156433 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29890ae8-e234-4e3b-9a5b-5b0234393872",
  "isSidechain": false,
  "promptId": "48d55f22-f9cb-4f29-850e-ff4d4525816b",
  "type": "user",
  "uuid": "15907794-e5fb-4c65-820f-fa7fb5905f1b",
  "toolUseResult": {
    "stdout": "usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/f\nonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (11 pages, 148827 bytes).\nTranscript written on paper.log.\nThis is BibTeX, Version 0.99d (TeX Live 2025/Debian)\nThe top-level auxiliary file: paper.aux\nThe style file: plainnat.bst\nDatabase file #1: references.bib\n1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/u\ntmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (11 pages, 155175 bytes).\nTranscript written on paper.log.\nusr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/f\nonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (11 pages, 156433 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "29890ae8-e234-4e3b-9a5b-5b0234393872",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/worst",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-16T16:27:07.051Z_

编译成功，生成 11 页 PDF。

`paper.tex` 和 `paper.pdf` 已写入指定目录。论文以 "format markers as classification shortcut" 为核心叙事，覆盖了 `experiment_data.json` 中全部 16 个实验，包括：

- **Table 1**: 主结果（4 模型 × 7 条件 + regex 基线）
- **Table 2**: VOTA 组件消融（format marker strength 视角）
- **Table 3**: 格式标记移除核心实验（3 seeds，含 pass/fail recall 分解）
- **Table 4**: SFT vs regex 对比
- **Table 5**: Gradient dilution 分解（label-only loss）
- **Table 6**: Trace 长度消融
- **Table 7**: 跨规模分析（1.5B/7B/13B）
- **Table 8**: DeepSeek 跨模型验证
- **Table 9**: Seed robustness 与 variance 对比
- **Table 10**: 多 seed 组件统计
- **Table 11**: Calibration（ECE + Brier）
- **Table 12**: DebugBench 泛化验证
- **Appendix Table**: 格式 shortcut 假说证据链汇总

所有定量 claim 均基于 JSON 数据，核心 decomposition（24.7pp = 14.5pp content + 10.2pp format marker）贯穿全文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15907794-e5fb-4c65-820f-fa7fb5905f1b",
  "isSidechain": false,
  "requestId": "req_011Cb6ZWmkMBLWzhXo4qjHRf",
  "type": "assistant",
  "uuid": "6a905e0c-30e3-4703-9730-de94043eb44e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/worst",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D1Dqpvsf1nSt1eJsyFPrNw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 62980,
      "output_tokens": 410,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 699,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 410,
          "cache_read_input_tokens": 62980,
          "cache_creation_input_tokens": 699,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 699
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

_source line 47_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T155731 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-stu…",
  "leafUuid": "6a905e0c-30e3-4703-9730-de94043eb44e",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-case tier paper for dream ID",
  "sessionId": "34e72d3c-d7c4-44c6-899d-982fad42e8f3"
}
```

---
