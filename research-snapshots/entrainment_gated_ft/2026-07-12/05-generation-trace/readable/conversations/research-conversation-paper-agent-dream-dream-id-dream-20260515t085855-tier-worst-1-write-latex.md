# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T085855 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-3/60b94339-87f0-47ef-aa74-b7c45d2f68d8.jsonl`
- **Structured JSON:** [`c1351a2a14940be5027f.json`](../../sessions/c1/c1351a2a14940be5027f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T09:54:28.176Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T09:54:28.176Z",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T085855 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/worst/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：放弃 \"diagnostic/decision rule\" 作为核心 contribution，reframe 为三条新主线： (1) Cardinality constraint as universal safeguard — 不依赖 diagnostic，所有 5-6 个模型上 constraint 都 ≤ uniform 或防止 catastrophe，architecture-agnostic practical fix； (2) Systematic negative result — \"we tested 5+ architectures and found non-uniform KV cache quantization is beneficial in only 1/5-6 cases\"，saves practitioners time，framing 类似 \"Challenging common assumptions about mixed-precision KV cache\"； (3) Compounding effect characterization — 即使 diagnostic 不成立，discrete non-consecutive bit-width 上 solver 失败的机制分析（W9 data + Qwen catastrophe）仍是 novel contribution。 三档标签改为纯描述性（按倍数分 tier，不绑定 distribution shape 解释）。 论文标题从 \"When Does X Help\" 转向 \"The Cardinality Constraint You Need for Hardware-Aligned KV Cache Quantization\"。 仍投 EMNLP Main Efficient Methods，卖点从 analysis 转向 practical method + surprising negative results。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T09:54:28.180Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T09:54:28.180Z",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8"
}
```

---

## Round 1

46 recorded events

### User

_source line 3 · 2026-05-15T09:54:28.200Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T085855 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/worst/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：放弃 "diagnostic/decision rule" 作为核心 contribution，reframe 为三条新主线： (1) Cardinality constraint as universal safeguard — 不依赖 diagnostic，所有 5-6 个模型上 constraint 都 ≤ uniform 或防止 catastrophe，architecture-agnostic practical fix； (2) Systematic negative result — "we tested 5+ architectures and found non-uniform KV cache quantization is beneficial in only 1/5-6 cases"，saves practitioners time，framing 类似 "Challenging common assumptions about mixed-precision KV cache"； (3) Compounding effect characterization — 即使 diagnostic 不成立，discrete non-consecutive bit-width 上 solver 失败的机制分析（W9 data + Qwen catastrophe）仍是 novel contribution。 三档标签改为纯描述性（按倍数分 tier，不绑定 distribution shape 解释）。 论文标题从 "When Does X Help" 转向 "The Cardinality Constraint You Need for Hardware-Aligned KV Cache Quantization"。 仍投 EMNLP Main Efficient Methods，卖点从 analysis 转向 practical method + surprising negative results。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "e8e8fea0-d6a9-4b91-8885-3140c3cbe799",
  "type": "user",
  "uuid": "9e5c2bc8-a136-4bdc-8028-f8dc0a36460e",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T09:54:28.199Z_

```json
{
  "parentUuid": "9e5c2bc8-a136-4bdc-8028-f8dc0a36460e",
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
  "uuid": "b34742e6-fabc-41c2-8548-09a65d93477c",
  "timestamp": "2026-05-15T09:54:28.199Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T09:54:28.199Z_

```json
{
  "parentUuid": "b34742e6-fabc-41c2-8548-09a65d93477c",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "acd60247-c4aa-4205-b829-1ffb9237ff60",
  "timestamp": "2026-05-15T09:54:28.199Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8",
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
  "aiTitle": "Generate worst-tier simulated paper for dream_20260515T085855",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8"
}
```

---

### Assistant

_source line 7 · 2026-05-15T09:54:31.247Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "acd60247-c4aa-4205-b829-1ffb9237ff60",
  "isSidechain": false,
  "requestId": "req_011Cb49n7TdRXXZb9eAbsxoC",
  "type": "assistant",
  "uuid": "dc6cc355-e0c8-45cd-be21-86ee04a61df7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDu35AgxUv1Y7B3KckEPX9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12234,
      "cache_read_input_tokens": 11841,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12234,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12234,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12234
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

_source line 8 · 2026-05-15T09:54:31.741Z_

<details open><summary>🔧 Tool call — Read · `toolu_01N9hZLdANfkufWzR427dgVg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc6cc355-e0c8-45cd-be21-86ee04a61df7",
  "isSidechain": false,
  "requestId": "req_011Cb49n7TdRXXZb9eAbsxoC",
  "type": "assistant",
  "uuid": "4b31af4c-7a94-48d3-b0b2-b2eaaa336867",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDu35AgxUv1Y7B3KckEPX9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12234,
      "cache_read_input_tokens": 11841,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12234,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12234,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12234
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

_source line 9 · 2026-05-15T09:54:32.094Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AnvGvhzwTCHdooGEQt252p`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b31af4c-7a94-48d3-b0b2-b2eaaa336867",
  "isSidechain": false,
  "requestId": "req_011Cb49n7TdRXXZb9eAbsxoC",
  "type": "assistant",
  "uuid": "fe671b0c-f9d0-40fc-a9de-b685a76d4ead",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDu35AgxUv1Y7B3KckEPX9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12234,
      "cache_read_input_tokens": 11841,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12234,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12234,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12234
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

_source line 10 · 2026-05-15T09:54:32.358Z_

<details><summary>↩ Tool result · `toolu_01N9hZLdANfkufWzR427dgVg`</summary>

```text
1	[
2	  {
3	    "name": "Qwen2.5-14B Hires Profiling",
4	    "description": "Qwen2.5-14B hires bf16 2-bit-only profiling（48 layers × 8 KV heads = 384 heads）。 测试 diagnostic 是否在 Qwen 模型族内泛化。\n",
5	    "results": {
6	      "qwen14b_baseline_ppl": 5.84,
7	      "qwen14b_top5_concentration": 0.55,
8	      "qwen14b_t1_t5": 0.63,
9	      "qwen14b_l0_dominance_ratio": 8.2,
10	      "qwen14b_top1_head": "L0H2",
11	      "qwen14b_top1_delta_2bit": 3.81,
12	      "qwen14b_l0_4heads_total_share": 0.41,
13	      "qwen14b_delta_2bit_cv": 5.12,
14	      "qwen14b_positive_delta_heads": 370,
15	      "qwen14b_total_heads": 384,
16	      "qwen14b_distribution_shape": "borderline_spread",
17	      "diagnostic_prediction": "Spread (conc≥0.50 AND t₁/t₅≤0.70)",
18	      "diagnostic_correct": false
19	    },
20	    "tables": [
21	      {
22	        "name": "Qwen Family Profiling Comparison",
23	        "columns": [
24	          "model",
25	          "layers",
26	          "kv_heads",
27	          "concentration",
28	          "t1_t5",
29	          "l0_share",
30	          "top1_delta",
31	          "shape"
32	        ],
33	        "rows": [
34	          [
35	            "Qwen2.5-7B",
36	            28,
37	            112,
38	            0.61,
39	            0.57,
40	            "58.6%",
41	            6.74,
42	            "Spread"
43	          ],
44	          [
45	            "Qwen2.5-14B",
46	            48,
47	            384,
48	            0.55,
49	            0.63,
50	            "41.0%",
51	            3.81,
52	            "Diluted Spread"
53	          ]
54	        ]
55	      }
56	    ],
57	    "figures": [],
58	    "analysis": "Diagnostic 两个指标都刚过阈值（concentration 0.55 > 0.50, t₁/t₅ 0.63 < 0.70）， 但边际通过。14B 的关键问题：更多层分摊了 sensitivity，使得 L0 的 dominance 不足以 让 MCKP 产生有意义的 allocation 差异。这暴露了 joint diagnostic 的 boundary fragility—— 阈值在 border 附近不 robust。\n\n\nQwen2.5-14B 有 48 layers × 8 KV heads = 384 heads（vs 7B 的 28×4=112）。 GQA 仍是 7:1，保留 L0 某些 heads 的较高 sensitivity（concentration=0.55，刚过 0.50 阈值）。 但 14B 的 L0 cluster 比 7B 弱得多：7B 的 L0 4 heads 占 total delta 的 58.6%， 而 14B 的 L0 heads 仅占 41%——48 层分摊了 sensitivity。t₁/t₅=0.63（<0.70）， 表面看满足 Spread 两个条件。但实际上 14B 的 \"spread\" 是 illusory： L0 heads 的 cross-bitwidth gradient 比 7B 弱（top1 delta=3.81 vs 7B 的 6.74）， 且 sensitivity 在 L0-L3 多层间分散而非集中在 L0 单层。 这是一种 \"diluted spread\"——diagnostic 判定为 Spread 但 MCKP 无法有效利用。\n"
59	  },
60	  {
61	    "name": "Qwen2.5-14B Constrained MCKP",
62	    "description": "基于 14B hires profiling 跑 constrained MCKP（k=8），评估 PPL。 如果 improvement ≈0%，则 diagnostic 出现 false positive。\n",
63	    "results": {
64	      "qwen14b_baseline_ppl": 5.84,
65	      "qwen14b_uniform_4bit_ppl": 7.02,
66	      "qwen14b_mckp_constrained_k8_ppl": 6.94,
67	      "qwen14b_mckp_improvement_over_uniform_pct": 1.2,
68	      "qwen14b_mckp_unconstrained_ppl": 8.41,
69	      "qwen14b_unconstrained_ratio": 1.44,
70	      "qwen14b_bit_distribution": {
71	        "2": 8,
72	        "4": 372,
73	        "8": 4
74	      },
75	      "qwen14b_greedy_constrained_ppl": 6.94,
76	      "qwen14b_solver_equivalence_delta": 0.0,
77	      "decision_rule_accuracy_6models": 5,
78	      "decision_rule_total_models": 6,
79	      "false_positive_model": "Qwen2.5-14B"
80	    },
81	    "tables": [
82	      {
83	        "name": "Qwen2.5-14B Allocation Results",
84	        "columns": [
85	          "method",
86	          "ppl",
87	          "compression",
88	          "vs_uniform"
89	        ],
90	        "rows": [
91	          [
92	            "baseline bf16",
93	            5.84,
94	            "1×",
95	            "—"
96	          ],
97	          [
98	            "uniform 4-bit",
99	            7.02,
100	            "4×",
101	            "baseline"
102	          ],
103	          [
104	            "constrained MCKP k=8",
105	            6.94,
106	            "4×",
107	            "+1.2%"
108	          ],
109	          [
110	            "unconstrained MCKP",
111	            8.41,
112	            "4×",
113	            "-19.8%"
114	          ],
115	          [
116	            "constrained greedy k=8",
117	            6.94,
118	            "4×",
119	            "+1.2%"
120	          ]
121	        ]
122	      },
123	      {
124	        "name": "Decision Rule Accuracy (6 Models)",
125	        "columns": [
126	          "model",
127	          "concentration",
128	          "t1_t5",
129	          "diagnostic_prediction",
130	          "actual_benefit",
131	          "correct"
132	        ],
133	        "rows": [
134	          [
135	            "Qwen2.5-7B",
136	            0.61,
137	            0.57,
138	            "Spread",
139	            "+27.3%",
140	            "✅"
141	          ],
142	          [
143	            "Qwen2.5-14B",
144	            0.55,
145	            0.63,
146	            "Spread",
147	            "+1.2%",
148	            "❌ FP"
149	          ],
150	          [
151	            "Yi-1.5-9B",
152	            0.71,
153	            0.9,
154	            "Spike",
155	            "≈0%",
156	            "✅"
157	          ],
158	          [
159	            "Llama-3.1-8B",
160	            0.57,
161	            0.71,
162	            "Spike",
163	            "+0.2%",
164	            "✅"
165	          ],
166	          [
167	            "Mistral-7B",
168	            0.24,
169	            0.18,
170	            "Flat",
171	            "-0.4%",
172	            "✅"
173	          ],
174	          [
175	            "Gemma-2-9B",
176	            0.23,
177	            0.38,
178	            "Flat",
179	            "-0.3%",
180	            "✅"
181	          ]
182	        ]
183	      }
184	    ],
185	    "figures": [],
186	    "analysis": "Qwen14B 是 diagnostic 的致命反例：同一模型族（Qwen），同一 GQA ratio（7:1）， concentration 和 t₁/t₅ 都满足 Spread 条件，但 MCKP 改进仅 1.2%。 根本原因是 more layers dilute sensitivity，使得 per-head allocation 无法 exploit  sufficient heterogeneity。这说明 diagnostic 缺少第三个维度：total_kv_heads 或 layer_count。 但增加维度后 N=6 的样本量完全不足以 fit 三维 boundary。 Decision rule 降至 5/6 且 failure 发生在 high-confidence prediction（both metrics pass）， 这不是 borderline miss 而是 systematic failure — 严重削弱 diagnostic claim。\n\n\nMCKP constrained PPL=6.94 vs uniform=7.02，improvement 仅 +1.2%（0.08 PPL gap）。 对比 Qwen7B 的 +27.3%（4.53 PPL gap），14B 的 improvement 在噪声范围内。 原因：14B 有 384 heads，每个 head 承载的 information 更少（head_dim 同为 128，但 48 层分摊）， 2-bit 降级的 per-head cost 更小。MCKP 将 L0 的 4 heads 分配到 8-bit，但这仅节省了 total budget 的很小部分——384 heads 中 4 个 8-bit heads 的 budget 释放被稀释到其余 380 heads， 每个 head 只多获得 ~0.01 bit，不足以改变 bit-width assignment。 Unconstrained ratio=1.44×（类似 Gemma-2 的 1.47×），solver 将 ~80 heads 分配到 2-bit， 产生 moderate 而非 catastrophic degradation。 Decision rule accuracy 从 5/5 降至 5/6：14B 是 false positive（diagnostic 预测 benefit，实际无）。\n"
187	  },
188	  {
189	    "name": "Gemma-2 Constrained MCKP with BOS Fix",
190	    "description": "用 sliding_window + BOS prepend 修正 eval，重测 Gemma-2 constrained MCKP 和 unconstrained baselines。 BOS bug 可能导致之前的 1.47× unconstrained ratio 和 -0.3% constrained delta 不准确。\n",
191	    "results": {
192	      "gemma2_bos_fix_baseline_ppl": 6.03,
193	      "gemma2_bos_fix_uniform_4bit_ppl": 6.17,
194	      "gemma2_bos_fix_constrained_mckp_ppl": 6.22,
195	      "gemma2_bos_fix_constrained_vs_uniform_pct": -0.8,
196	      "gemma2_bos_fix_unconstrained_greedy_ppl": 7.38,
197	      "gemma2_bos_fix_unconstrained_ratio": 1.22,
198	      "gemma2_bos_fix_n2bit_unconstrained": 106,
199	      "gemma2_bos_fix_constrained_bit_dist": {
200	        "2": 8,
201	        "4": 324,
202	        "8": 4
203	      },
204	      "gemma2_old_unconstrained_ratio": 1.47,
205	      "gemma2_ratio_shift": -0.25
206	    },
207	    "tables": [
208	      {
209	        "name": "Gemma-2 BOS Fix Impact",
210	        "columns": [
211	          "metric",
212	          "before_bos_fix",
213	          "after_bos_fix",
214	          "delta"
215	        ],
216	        "rows": [
217	          [
218	            "baseline PPL",
219	            "711.6 (buggy) / 6.03 (corrected)",
220	            6.03,
221	            "—"
222	          ],
223	          [
224	            "uniform 4-bit PPL",
225	            6.17,
226	            6.17,
227	            "0.00"
228	          ],
229	          [
230	            "unconstrained ratio",
231	            "1.47×",
232	            "1.22×",
233	            "-0.25×"
234	          ],
235	          [
236	            "constrained vs uniform",
237	            "-0.3%",
238	            "-0.8%",
239	            "-0.5pp"
240	          ],
241	          [
242	            "2-bit heads (unconstrained)",
243	            106,
244	            106,
245	            "0"
246	          ]
247	        ]
248	      },
249	      {
250	        "name": "Revised Three-Tier Labels (COLLAPSED)",
251	        "columns": [
252	          "tier",
253	          "ratio_range",
254	          "models",
255	          "count"
256	        ],
257	        "rows": [
258	          [
259	            "Catastrophic",
260	            "≥2.0×",
261	            "Qwen2.5-7B (3.31×)",
262	            1
263	          ],
264	          [
265	            "Moderate (EMPTY)",
266	            "1.25-2.0×",
267	            "—",
268	            0
269	          ],
270	          [
271	            "Mild",
272	            "1.0-1.25×",
273	            "Yi 1.08×, Llama 1.07×, Mistral 1.08×, Gemma-2 1.22×",
274	            4
275	          ]
276	        ]
277	      }
278	    ],
279	    "figures": [],
280	    "analysis": "三档标签失去 moderate 层：Catastrophic (1 model) + Mild (4 models)， 变成 binary 而非 gradient。原本 \"concentration-dependent gradient\" 叙事中 Gemma-2 是关键中间证据（flat-high-2bit mechanism），现在该机制的 magnitude  被 BOS bug 虚增。修正后 1.22× 的 over-allocation 仍比 Yi/Llama/Mistral 高， 但 gap 缩小到 0.14-0.15×，可能在 noise 范围内。 论文需要重新校准：要么放弃三档（改用连续变量 regression）， 要么承认 moderate tier 的 evidence 不 robust。\n\n\nBOS fix 降低了 baseline PPL（711.6→6.03 已确认），也降低了 quantized PPL。 关键：BOS bug 对 unconstrained allocation 的影响是 non-uniform 的—— 106 个 2-bit heads 的 joint distortion 在有 BOS token 时部分被 BOS 的 attention mass 吸收 （BOS 通常获得高 attention weight，为后续 token 提供 anchor）， 没有 BOS 时这些 heads 的 distortion 被放大。 修正后 unconstrained ratio 从 1.47× 降至 1.22×，落入 mild 范围（1.07-1.22×）， 与 Yi/Llama/Mistral 的 1.07-1.08× 更接近。 三档标签崩塌：原本 Gemma-2 是 \"moderate\" 独占，现在没有 moderate 了—— 只有 catastrophic（Qwen7B 3.31×）和 mild（其余 4 个模型 1.07-1.22×）。 Constrained vs uniform 变为 -0.8%（从 -0.3%），方向不变但幅度增大。\n"
281	  },
282	  {
283	    "name": "L0 Auto-Discovery (No L0 Exclusion)",
284	    "description": "去掉 L0 exclusion 硬约束，仅保留 max_2bit=8，观察 solver 是否仍将 L0 heads 分配到 8-bit。\n",
285	    "results": {
286	      "qwen7b_no_l0excl_ppl": 11.23,
287	      "qwen7b_l0_heads_assigned_8bit": 4,
288	      "qwen7b_solver_auto_discovers_l0": true,
289	      "qwen14b_no_l0excl_ppl": 6.97,
290	      "qwen14b_l0_heads_assigned_8bit": 2,
291	      "qwen14b_solver_partial_discovery": true
292	    },
293	    "tables": [
294	      {
295	        "name": "L0 Auto-Discovery Across Qwen Family",
296	        "columns": [
297	          "model",
298	          "l0_dominance",
299	          "l0_8bit_heads",
300	          "total_8bit_budget",
301	          "ppl",
302	          "auto_discovery"
303	        ],
304	        "rows": [
305	          [
306	            "Qwen2.5-7B",
307	            "26×",
308	            "4/4",
309	            4,
310	            11.23,
311	            "Full ✅"
312	          ],
313	          [
314	            "Qwen2.5-14B",
315	            "8.2×",
316	            "2/8",
317	            4,
318	            6.97,
319	            "Partial ⚠️"
320	          ]
321	        ]
322	      }
323	    ],
324	    "figures": [],
325	    "analysis": "Auto-discovery 在 7B 上完美，在 14B 上部分失败。 Reframed narrative 中这不是 critical：constraint 的价值不依赖 auto-discovery， constraint 的 contribution 是 preventing compounding 而非 discovering structure。\n\n\nQwen7B：solver 从 profiling data 自动将 L0 全部 4 heads 分配到 8-bit（delta 极高，cost-benefit ratio 最优），PPL=11.23 不变。这在 7B 上 works 因为 L0 dominance ratio=26×。 Qwen14B：solver 仅将 L0 的 2/8 heads 分配到 8-bit（L0 dominance ratio 仅 8.2×，不够突出）， 其余 2 个 8-bit 名额给了 L2-L3 的 moderate-delta heads。PPL=6.97（vs constrained 6.94）， 差异很小但说明 14B 的 L0 不再是 unambiguous dominant——auto-discovery 部分失败。\n"
326	  },
327	  {
328	    "name": "Llama-3.1-8B Full Pipeline",
329	    "description": "Llama-3.1-8B (GQA 4:1) 全 pipeline：profile → constrained MCKP → eval。\n",
330	    "results": {
331	      "llama_baseline_ppl": 8.09,
332	      "llama_uniform_4bit_ppl": 8.47,
333	      "llama_mckp_constrained_ppl": 8.45,
334	      "llama_improvement_pct": 0.2,
335	      "llama_unconstrained_ratio": 1.07,
336	      "llama_concentration": 0.57,
337	      "llama_t1_t5": 0.71,
338	      "llama_shape": "Spike (borderline)",
339	      "llama_natural_k": 2
340	    },
341	    "tables": [
342	      {
343	        "name": "Llama-3.1-8B Results",
344	        "columns": [
345	          "method",
346	          "ppl",
347	          "compression",
348	          "vs_uniform"
349	        ],
350	        "rows": [
351	          [
352	            "baseline bf16",
353	            8.09,
354	            "1×",
355	            "—"
356	          ],
357	          [
358	            "uniform 4-bit",
359	            8.47,
360	            "4×",
361	            "baseline"
362	          ],
363	          [
364	            "constrained MCKP k=8",
365	            8.45,
366	            "4×",
367	            "+0.2%"
368	          ],
369	          [
370	            "unconstrained",
371	            8.63,
372	            "4×",
373	            "-1.9%"
374	          ]
375	        ]
376	      }
377	    ],
378	    "figures": [],
379	    "analysis": "Negative result 在 worst tier 下保持。但 t₁/t₅=0.71 的 borderline 值  使 diagnostic 对 Llama 的分类依赖 ±0.01 的阈值精度——如果阈值设为 0.75， Llama 会被误分为 Spread，增加 false positive 风险。\n\n\nLlama 的 concentration=0.57 接近 0.50 阈值但 t₁/t₅=0.71 刚好超过 0.70， 被分类为 Spike。实际上 MCKP 仅选择 2 个 heads 做 2-bit（natural k=2）， constraint 从不 bind。+0.2% improvement 在 noise 范围内。 在 worst tier 下，Llama 的 borderline t₁/t₅=0.71 使得 diagnostic boundary  的 robustness 受质疑——0.70 是 arbitrary cutoff。\n"
380	  },
381	  {
382	    "name": "Mistral-7B-v0.3 Full Pipeline",
383	    "description": "Mistral-7B-v0.3 全 pipeline，Flat distribution 代表。\n",
384	    "results": {
385	      "mistral_baseline_ppl": 7.04,
386	      "mistral_uniform_4bit_ppl": 7.13,
387	      "mistral_mckp_constrained_ppl": 7.16,
388	      "mistral_improvement_pct": -0.4,
389	      "mistral_unconstrained_ratio": 1.08,
390	      "mistral_concentration": 0.24,
391	      "mistral_t1_t5": 0.18,
392	      "mistral_shape": "Flat",
393	      "mistral_k_monotonic": true
394	    },
395	    "tables": [
396	      {
397	        "name": "Mistral-7B Results",
398	        "columns": [
399	          "method",
400	          "ppl",
401	          "compression",
402	          "vs_uniform"
403	        ],
404	        "rows": [
405	          [
406	            "baseline bf16",
407	            7.04,
408	            "1×",
409	            "—"
410	          ],
411	          [
412	            "uniform 4-bit",
413	            7.13,
414	            "4×",
415	            "baseline"
416	          ],
417	          [
418	            "constrained MCKP k=4",
419	            7.16,
420	            "4×",
421	            "-0.4%"
422	          ],
423	          [
424	            "unconstrained",
425	            7.57,
426	            "4×",
427	            "-6.2%"
428	          ]
429	        ]
430	      }
431	    ],
432	    "figures": [],
433	    "analysis": "Mistral 是最 clean 的 negative case——profiler signal ≈0， 任何 non-uniform allocation 都 ≤ uniform。在 reframed narrative 中 是 \"systematic negative result\" 的核心证据之一。\n\n\nMistral concentration=0.24（远低于 0.50），profiler 信号几乎为零。 Constrained MCKP 比 uniform 差 0.4%——solver 分配的 2-bit heads  实际上比 uniform 的 all-4bit 更差。k ablation 单调递增证明  每多一个 2-bit head 都 hurts。在 worst tier 下这是 clean negative， 直接支持 \"uniform suffices on flat models\" 的叙事。\n"
434	  },
435	  {
436	    "name": "Compounding Effect Sweep (Qwen7B)",
437	    "description": "Qwen2.5-7B 上 sweep max_2bit 从 0 到 112，绘制 PPL vs k curve。\n",
438	    "results": {
439	      "qwen_k0_ppl": 15.45,
440	      "qwen_k4_ppl": 11.93,
441	      "qwen_k8_ppl": 11.23,
442	      "qwen_k10_ppl": 11.18,
443	      "qwen_k12_ppl": 11.21,
444	      "qwen_k16_ppl": 11.52,
445	      "qwen_k24_ppl": 13.07,
446	      "qwen_k48_ppl": 19.84,
447	      "qwen_k75_ppl": 28.36,
448	      "qwen_k112_ppl": 36.92,
449	      "elbow_k": 8,
450	      "curve_shape": "U-shape with clear minimum at k≈8-10"
451	    },
452	    "tables": [
453	      {
454	        "name": "Compounding Sweep (Qwen2.5-7B, budget=0.25)",
455	        "columns": [
456	          "max_2bit_k",
457	          "ppl",
458	          "delta_vs_k8"
459	        ],
460	        "rows": [
461	          [
462	            0,
463	            15.45,
464	            "+37.6%"
465	          ],
466	          [
467	            4,
468	            11.93,
469	            "+6.2%"
470	          ],
471	          [
472	            8,
473	            11.23,
474	            "baseline (optimal)"
475	          ],
476	          [
477	            12,
478	            11.21,
479	            "-0.2%"
480	          ],
481	          [
482	            16,
483	            11.52,
484	            "+2.6%"
485	          ],
486	          [
487	            24,
488	            13.07,
489	            "+16.4%"
490	          ],
491	          [
492	            48,
493	            19.84,
494	            "+76.7%"
495	          ],
496	          [
497	            112,
498	            36.92,
499	            "+228.8%"
500	          ]
501	        ]
502	      }
503	    ],
504	    "figures": [],
505	    "analysis": "Compounding curve 是 paper 的 core figure 之一，在 Qwen 上有力。 但在 worst tier 下，其意义从 \"universal phenomenon\" 缩小为 \"Spread-model-specific phenomenon\"。Reframe:  compounding 的 magnitude 和 shape 是 architecture-dependent， 但 constraint 在所有模型上都是 safe（≤ uniform）。\n\n\nQwen7B 的 compounding curve 有清晰 U-shape：k 太小（budget 浪费在不需要的 higher-bit heads）， k 太大（compounding 恶化）。Optimal k=8-10 对应 L0 cluster 的 head 数量。 这是 Qwen7B 的固有特性，worst tier 不改变此结果。 但 worst tier 的问题是：此 curve 是否跨模型可复现？ Llama/Mistral 的 k-PPL curve 平坦或单调，没有 U-shape—— compounding 的 \"dramatic elbow\" 是 Spread-specific，不 universal。\n"
506	  },
507	  {
508	    "name": "Budget Sweep (Qwen7B, 2×/4×/8×)",
509	    "description": "Qwen2.5-7B 在三种压缩率下 constrained MCKP vs uniform。\n",
510	    "results": {
511	      "qwen_2x_uniform_ppl": 10.07,
512	      "qwen_2x_mckp_ppl": 9.89,
513	      "qwen_2x_improvement_pct": 1.8,
514	      "qwen_4x_uniform_ppl": 15.45,
515	      "qwen_4x_mckp_ppl": 11.23,
516	      "qwen_4x_improvement_pct": 27.3,
517	      "qwen_8x_uniform_ppl": 2644.0,
518	      "qwen_8x_mckp_ppl": 42.6,
519	      "qwen_8x_improvement_pct": 98.4
520	    },
521	    "tables": [
522	      {
523	        "name": "Budget Sweep (Qwen2.5-7B)",
524	        "columns": [
525	          "compression",
526	          "uniform_ppl",
527	          "mckp_ppl",
528	          "improvement"
529	        ],
530	        "rows": [
531	          [
532	            "2× (0.50)",
533	            10.07,
534	            9.89,
535	            "+1.8%"
536	          ],
537	          [
538	            "4× (0.25)",
539	            15.45,
540	            11.23,
541	            "+27.3%"
542	          ],
543	          [
544	            "8× (0.125)",
545	            2644.0,
546	            42.6,
547	            "+98.4%"
548	          ]
549	        ]
550	      }
551	    ],
552	    "figures": [],
553	    "analysis": "Budget sweep 在 Qwen 上 compelling。Reframe under worst tier: aggressive compression（5.3×+）即使在 non-Spread 模型上也有 cardinality constraint  的价值（Llama 5.3×: 57.60 vs 2644）——constraint 在极端场景下 universally 有用。\n\n\n2× 压缩：budget 充裕（avg 8-bit），大部分 heads 在安全区，仅 1.8% 改进。 4× 是 sweet spot（27.3%），与已有结果一致。 8× 极端压缩下 uniform = all 2-bit（PPL 2644），constrained MCKP 保护 critical heads 大幅降低 PPL（42.6），但绝对质量仍很差。 Worst tier 不改变 Qwen7B 数字，但 cross-model budget sweep （如果做的话）会显示 Llama/Mistral 在 2× 和 4× 都无 improvement。\n"
554	  },
555	  {
556	    "name": "High-Resolution Profiling (Qwen7B)",
557	    "description": "64 seq × 2048 tokens hires profiling，重跑 MCKP。\n",
558	    "results": {
559	      "hires_constrained_ppl": 10.91,
560	      "lowres_constrained_ppl": 11.23,
561	      "hires_improvement_over_lowres_pct": 2.8,
562	      "hires_nonzero_2bit": 100,
563	      "lowres_nonzero_2bit": 37,
564	      "hires_profiling_time_min": 65.5,
565	      "allocation_diff_count": 8
566	    },
567	    "tables": [
568	      {
569	        "name": "Profiling Resolution Comparison",
570	        "columns": [
571	          "resolution",
572	          "nonzero_heads",
573	          "constrained_ppl",
574	          "time_min"
575	        ],
576	        "rows": [
577	          [
578	            "16×512 (lowres)",
579	            37,
580	            11.23,
581	            "~10"
582	          ],
583	          [
584	            "64×2048 (hires)",
585	            100,
586	            10.91,
587	            65.5
588	          ]
589	        ]
590	      }
591	    ],
592	    "figures": [],
593	    "analysis": "Hires 提供 modest improvement，但 profiling cost 6× 增加。 在 reframed narrative 中，hires vs lowres 是 secondary concern—— constraint 的 contribution 不依赖 profiling resolution。\n\n\nHires profiling 发现更多 non-zero 2-bit delta heads（100 vs 37）， 改善 MCKP allocation（PPL 10.91 vs 11.23，+2.8%）。 8 个 heads 的 allocation 改变（从 4-bit 到 2-bit 或反向）， 说明 lowres 有 ~7% 的 misallocation。 在 worst tier 下，hires 对 Qwen7B 有 modest benefit， 但对 non-Spread 模型（Llama hires: 8.45 vs 8.50）几乎无差。 且 hires profiling 耗时 65 min（vs lowres ~10 min）， cost/benefit ratio 在非 Spread 模型上 unjustified。\n"
594	  },
595	  {
596	    "name": "C4 Cross-Dataset Evaluation (Qwen7B)",
597	    "description": "C4 calibration + WikiText-2 evaluation，测试跨 dataset robustness。\n",
598	    "results": {
599	      "c4_cal_wt2_eval_mckp_ppl": 11.29,
600	      "c4_cal_wt2_eval_uniform_ppl": 15.45,
601	      "c4_cal_wt2_eval_improvement_pct": 26.9,
602	      "allocation_agreement_c4_vs_wt2": 0.964,
603	      "agreement_heads": "108/112",
604	      "cross_domain_wt2_to_c4_mckp_ppl": 20.56,
605	      "cross_domain_wt2_to_c4_uniform_ppl": 35.42
606	    },
607	    "tables": [
608	      {
609	        "name": "C4 Cross-Dataset (Qwen2.5-7B)",
610	        "columns": [
611	          "calibration",
612	          "eval",
613	          "mckp_ppl",
614	          "uniform_ppl",
615	          "improvement"
616	        ],
617	        "rows": [
618	          [
619	            "WikiText-2",
620	            "WikiText-2",
621	            11.29,
622	            15.45,
623	            "26.9%"
624	          ],
625	          [
626	            "C4",
627	            "WikiText-2",
628	            11.29,
629	            15.45,
630	            "26.9%"
631	          ],
632	          [
633	            "WikiText-2",
634	            "C4",
635	            20.56,
636	            35.42,
637	            "42.0%"
638	          ]
639	        ]
640	      }
641	    ],
642	    "figures": [],
643	    "analysis": "Cross-dataset robustness 在 Qwen7B 上 strong（L0 dominance 使得 allocation 稳定）。 但这不 extend 到 non-Spread 模型或 14B（where L0 is less dominant）。\n\n\nAllocation agreement 96.4% 说明 calibration source 对 Qwen7B 影响很小 （112 heads 中仅 4 个 disagree）。这是 因为 L0 的 extreme dominance  在任何 distribution 上都一致——agreement 本质上是 \"L0 is always dominant\"。 Cross-domain PPL（20.56）比 same-domain（11.29）高很多， 但 vs uniform 仍有大幅改善（20.56 vs 35.42）。 Worst tier 的问题：14B 上 agreement 可能更低（L0 dominance 弱， mid-layer allocation 更 distribution-dependent）。\n"
644	  },
645	  {
646	    "name": "RateQuant Greedy Comparison",
647	    "description": "RateQuant greedy (Algorithm 1) on {2,4,8,16} vs constrained MCKP。\n",
648	    "results": {
649	      "greedy_unconstrained_ppl": 32.45,
650	      "mckp_unconstrained_ppl": 36.92,
651	      "greedy_constrained_k8_ppl": 11.23,
652	      "mckp_constrained_k8_ppl": 11.23,
653	      "greedy_constrained_delta_vs_mckp": 0.0012,
654	      "bit_distribution": {
655	        "2": 8,
656	        "4": 100,
657	        "8": 4
658	      }
659	    },
660	    "tables": [
661	      {
662	        "name": "Solver Comparison (Qwen2.5-7B, budget=0.25)",
663	        "columns": [
664	          "method",
665	          "unconstrained_ppl",
666	          "constrained_k8_ppl"
667	        ],
668	        "rows": [
669	          [
670	            "RateQuant Greedy",
671	            32.45,
672	            11.23
673	          ],
674	          [
675	            "MCKP",
676	            36.92,
677	            11.23
678	          ],
679	          [
680	            "Uniform 4-bit",
681	            "—",
682	            15.45
683	          ]
684	        ]
685	      }
686	    ],
687	    "figures": [],
688	    "analysis": "Solver equivalence under constraint 是 robust result，在 worst tier 下 成为 paper 的 core contribution 之一（不依赖 diagnostic）。\n\n\nUnconstrained greedy (32.45) 和 MCKP (36.92) 都 catastrophically fail。 Constrained 后两者 converge（Δ=0.0012 ≈ 0）。 这是 \"constraint is the contribution, not the solver\" 的 strongest evidence。 Worst tier 不改变此结论——solver equivalence under constraint  是 Qwen7B 的数学属性（constrained feasible set small enough）， 无论 diagnostic 是否成立。\n"
689	  },
690	  {
691	    "name": "Oracle Comparison (Brute-Force Subset)",
692	    "description": "Qwen7B 3-4 layer groups 上 brute-force optimal vs MCKP。\n",
693	    "results": {
694	      "mckp_ppl": 10.91,
695	      "max_oracle_gap_ppl": 0.0183,
696	      "avg_oracle_gap_ppl": 0.0046,
697	      "layers_mckp_optimal": "5/8",
698	      "gap_nature": "2-bit head position swap within same bit budget"
699	    },
700	    "tables": [
701	      {
702	        "name": "Oracle vs MCKP (Qwen2.5-7B Subset)",
703	        "columns": [
704	          "layer_group",
705	          "mckp_ppl",
706	          "oracle_ppl",
707	          "gap"
708	        ],
709	        "rows": [
710	          [
711	            "L0-L3",
712	            10.91,
713	            10.91,
714	            0.0
715	          ],
716	          [
717	            "L1",
718	            "—",
719	            "—",
720	            0.0183
721	          ],
722	          [
723	            "L4",
724	            "—",
725	            "—",
726	            0.0045
727	          ],
728	          [
729	            "L11",
730	            "—",
731	            "—",
732	            0.0136
733	          ]
734	        ]
735	      }
736	    ],
737	    "figures": [],
738	    "analysis": "Near-optimality 是 standalone result，加强 constraint contribution。\n\n\nMCKP gap to oracle 极小（max 0.0183 PPL），5/8 layers 完全 optimal。 Gap 来源：3 个 layer 上 MCKP 选了 slightly suboptimal 的 2-bit head 位置， 但 bit budget 完全相同——差异仅在 which head gets 2-bit，非结构性错误。 即使在 worst tier 下，MCKP near-optimality 成立——这不依赖 diagnostic。\n"
739	  },
740	  {
741	    "name": "Cross-Domain Calibration Robustness",
742	    "description": "C4 calibrate / WikiText-2 evaluate 及反向，报告 allocation agreement。\n",
743	    "results": {
744	      "qwen_agreement": 0.964,
745	      "llama_agreement": 0.977,
746	      "mistral_agreement": 0.965,
747	      "qwen14b_predicted_agreement": 0.88
748	    },
749	    "tables": [
750	      {
751	        "name": "Cross-Calibration Agreement",
752	        "columns": [
753	          "model",
754	          "agreement",
755	          "heads_agree",
756	          "total"
757	        ],
758	        "rows": [
759	          [
760	            "Qwen2.5-7B",
761	            "96.4%",
762	            108,
763	            112
764	          ],
765	          [
766	            "Llama-3.1-8B",
767	            "97.7%",
768	            250,
769	            256
770	          ],
771	          [
772	            "Mistral-7B",
773	            "96.5%",
774	            247,
775	            256
776	          ],
777	          [
778	            "Qwen2.5-14B (predicted)",
779	            "~88%",
780	            "~338",
781	            384
782	          ]
783	        ]
784	      }
785	    ],
786	    "figures": [],
787	    "analysis": "Cross-calibration robustness 在小模型上 strong， 但可能不 scale to larger models（more heads → more ambiguity）。\n\n\n三个 7-9B 模型都有 >96% agreement，说明 calibration robust。 但 worst tier 预测 Qwen14B 的 agreement 可能降至 ~88%， 因为 14B 的 sensitivity 更分散、mid-layer heads 的 ranking  更 distribution-dependent。这削弱 \"one-shot calibration\" 的 practicality claim。\n"
788	  },
789	  {
790	    "name": "Head Sensitivity Visualization",
791	    "description": "Paper-quality figures: per-head delta heatmap, compounding curve, allocation comparison。\n",
792	    "results": {
793	      "figures_generated": 5,
794	      "key_visual": "5-model heatmap comparison shows architecture diversity",
795	      "worst_tier_impact": "14B heatmap looks like diluted version of 7B, weakens family consistency"
796	    },
797	    "tables": [],
798	    "figures": [],
799	    "analysis": "Visualization 诚实展示 diagnostic 的 limitation 反而增加 credibility。 14B false positive 在 scatter plot 上是 visible anomaly，需要 explicit 讨论。\n\n\nVisualization 不产生新数据但在 worst tier 下需要更新： (1) 加入 14B heatmap 显示 diluted spread pattern（与 7B 对比削弱 Qwen family story） (2) 三档 gradient bar chart 中 moderate 消失（Gemma-2 BOS fix） (3) Decision rule scatter 中 14B 落在 Spread 象限但标记为 false positive\n"
800	  },
801	  {
802	    "name": "Downstream Task Evaluation (Qwen7B)",
803	    "description": "ARC-C / HellaSwag / PIQA / WinoGrande on Qwen7B + 4 non-Spread models at 4×。\n",
804	    "results": {
805	      "qwen_avg_recovery": 0.728,
806	      "qwen_arc_c_delta_pp": 3.16,
807	      "qwen_hellaswag_delta_pp": 4.0,
808	      "yi_mckp_vs_uniform_pp": -0.77,
809	      "llama_mckp_vs_uniform_pp": -0.99,
810	      "mistral_mckp_vs_uniform_pp": -0.48,
811	      "gemma2_mckp_vs_uniform_pp": 0.14,
812	      "qwen14b_predicted_mckp_vs_uniform_pp": -0.2
813	    },
814	    "tables": [
815	      {
816	        "name": "Downstream Summary (6 Models)",
817	        "columns": [
818	          "model",
819	          "shape",
820	          "mckp_vs_uniform_pp",
821	          "diagnostic_correct"
822	        ],
823	        "rows": [
824	          [
825	            "Qwen2.5-7B",
826	            "Spread",
827	            "+2.60pp",
828	            "✅"
829	          ],
830	          [
831	            "Qwen2.5-14B",
832	            "Diluted Spread",
833	            "-0.2pp (noise)",
834	            "❌ FP"
835	          ],
836	          [
837	            "Yi-1.5-9B",
838	            "Spike",
839	            "-0.77pp",
840	            "✅"
841	          ],
842	          [
843	            "Llama-3.1-8B",
844	            "Spike",
845	            "-0.99pp",
846	            "✅"
847	          ],
848	          [
849	            "Mistral-7B",
850	            "Flat",
851	            "-0.48pp",
852	            "✅"
853	          ],
854	          [
855	            "Gemma-2-9B",
856	            "Flat",
857	            "+0.14pp (noise)",
858	            "✅"
859	          ]
860	        ]
861	      }
862	    ],
863	    "figures": [],
864	    "analysis": "Downstream data 在 worst tier 下 reinforces \"1/6 models benefit\"—— 更适合 framing 为 systematic negative result + one strong positive case study。\n\n\n5-model downstream data 完整，结果与 PPL 一致。 Worst tier 预测 Qwen14B downstream：MCKP vs uniform ≈ -0.2pp（与 PPL 的 +1.2% 不一致方向？ 不，PPL improvement +1.2% 意味着 MCKP 稍好，downstream 可能 +0.1-0.3pp 或 noise）。 但 14B 的 downstream 数据不足以区分 signal vs noise（无 multi-seed CI）。 论文需报告 14B 但不能 claim benefit。\n"
865	  },
866	  {
867	    "name": "70B Profiling-Only (Qwen2.5-72B)",
868	    "description": "Qwen2.5-72B distortion profiling（不做 eval），分析 sensitivity 是否随 model size 缩放。\n",
869	    "results": {
870	      "qwen72b_concentration": 0.48,
871	      "qwen72b_t1_t5": 0.69,
872	      "qwen72b_l0_dominance_ratio": 5.1,
873	      "qwen72b_total_heads": 640,
874	      "qwen72b_diagnostic_prediction": "borderline (conc<0.50)"
875	    },
876	    "tables": [
877	      {
878	        "name": "Qwen Family Scaling",
879	        "columns": [
880	          "model",
881	          "params",
882	          "layers",
883	          "kv_heads",
884	          "concentration",
885	          "t1_t5",
886	          "predicted_shape"
887	        ],
888	        "rows": [
889	          [
890	            "Qwen2.5-7B",
891	            "7B",
892	            28,
893	            112,
894	            0.61,
895	            0.57,
896	            "Spread"
897	          ],
898	          [
899	            "Qwen2.5-14B",
900	            "14B",
901	            48,
902	            384,
903	            0.55,
904	            0.63,
905	            "Diluted Spread"
906	          ],
907	          [
908	            "Qwen2.5-72B",
909	            "72B",
910	            80,
911	            640,
912	            0.48,
913	            0.69,
914	            "Borderline/Flat"
915	          ]
916	        ]
917	      }
918	    ],
919	    "figures": [],
920	    "analysis": "如果 72B profiling 证实 concentration < 0.50，则 Spread pattern  不是 Qwen architecture 的固有属性而是 small-model artifact。 这对 diagnostic 的 practical value 是致命打击—— practitioner 最关心的 large models 恰恰最不可能是 Spread。\n\n\n72B 有 80 layers × 8 KV heads = 640 heads。更多层进一步稀释 concentration。 Concentration=0.48（刚低于 0.50 阈值），t₁/t₅=0.69（刚低于 0.70）。 Diagnostic 预测 borderline/Flat——如果确实如此， 则 Qwen 模型族呈现 \"7B=Spread, 14B=Diluted Spread, 72B=Flat\" 的递减梯度， 说明 model size increase 系统性地 dilute sensitivity concentration。 这直接挑战 \"Qwen family is Spread\" 的 assumption。\n"
921	  },
922	  {
923	    "name": "K/V Separation",
924	    "description": "将 K 和 V heads 作为独立 MCKP items，允许 asymmetric K/V budget。\n",
925	    "results": {
926	      "kv_sep_ppl": 11.22,
927	      "joint_kv_ppl": 10.91,
928	      "uniform_4bit_ppl": 15.45,
929	      "delta_sep_vs_joint": 0.31,
930	      "sep_k_2bit_count": 16,
931	      "sep_v_uniform_4bit": true
932	    },
933	    "tables": [
934	      {
935	        "name": "K/V Separation (Qwen2.5-7B)",
936	        "columns": [
937	          "method",
938	          "ppl",
939	          "k_2bit",
940	          "v_2bit",
941	          "vs_joint"
942	        ],
943	        "rows": [
944	          [
945	            "Joint K+V",
946	            10.91,
947	            4,
948	            4,
949	            "baseline"
950	          ],
951	          [
952	            "K/V separated",
953	            11.22,
954	            16,
955	            0,
956	            "+2.8%"
957	          ],
958	          [
959	            "Uniform 4-bit",
960	            15.45,
961	            0,
962	            0,
963	            "+41.6%"
964	          ]
965	        ]
966	      }
967	    ],
968	    "figures": [],
969	    "analysis": "Negative result：K/V separation 不如 joint optimization。 论文用 1 paragraph 报告，作为 RateQuant comparison 的补充。\n\n\nK/V separation 让 solver 独立优化 K 和 V 的 budget。 结果：V heads 全部 4-bit（sensitivity 低），K heads 有 16 个 2-bit（budget 被 V 让渡）。 但 PPL 11.22 略差于 joint optimization 的 10.91（Δ=0.31）， 因为 K-only 2-bit 的 compounding 比 joint 分配更 aggressive。 在 worst tier 下，这是 negative result——joint optimization 优于 separation， 说明 K/V interaction matters，简单的 asymmetric budget 不够。\n"
970	  },
971	  {
972	    "name": "L0-Only Heuristic Baseline",
973	    "description": "最简单的 non-uniform 策略：L0 全部 8-bit，其余 uniform 4-bit。 如果匹配 MCKP，则 full optimization 不必要。\n",
974	    "results": {
975	      "qwen_l0_random_mean": 11.69,
976	      "qwen_l0_random_median": 11.52,
977	      "qwen_l0_random_std": 0.47,
978	      "qwen_naive_positional_ppl": 12.23,
979	      "qwen_mckp_ppl": 10.91,
980	      "llama_l0_random_mean": 10.48,
981	      "llama_mckp_ppl": 8.45,
982	      "mistral_l0_random_mean": 7.56,
983	      "mistral_mckp_ppl": 7.16
984	    },
985	    "tables": [
986	      {
987	        "name": "L0 Heuristic vs MCKP",
988	        "columns": [
989	          "model",
990	          "l0_random_median",
991	          "mckp",
992	          "uniform",
993	          "mckp_vs_heuristic_gap"
994	        ],
995	        "rows": [
996	          [
997	            "Qwen2.5-7B",
998	            11.52,
999	            10.91,
1000	            15.45,
1001	            "5.6%"
1002	          ],
1003	          [
1004	            "Llama-3.1-8B",
1005	            10.04,
1006	            8.45,
1007	            8.47,
1008	            "18.8%"
1009	          ],
1010	          [
1011	            "Mistral-7B",
1012	            7.59,
1013	            7.16,
1014	            7.13,
1015	            "6.0%"
1016	          ]
1017	        ]
1018	      }
1019	    ],
1020	    "figures": [],
1021	    "analysis": "MCKP outperforms heuristic on all models，但 gap varies。 在 non-Spread models，MCKP 和 heuristic 都 ≤ uniform—— the right choice is \"don't bother\" rather than \"optimize better\"。\n\n\nL0-random heuristic（随机选 k 个 non-L0 heads 做 2-bit）在 Qwen 上 median=11.52 vs MCKP=10.91（gap 5.6%）。MCKP 的优势来自  precisely 选择 which non-L0 heads 做 2-bit（vs random）。 在 Llama/Mistral 上 L0-random 显著差于 MCKP（且 MCKP ≈ uniform）， 说明 heuristic 不是 universal substitute。 Worst tier 的 concern：14B 上 L0-random 可能 ≈ MCKP（因为 14B 的 MCKP 本身 ≈ uniform）， 进一步削弱 MCKP 的 value proposition。\n"
1022	  },
1023	  {
1024	    "name": "RateQuant Greedy + Cardinality Constraint",
1025	    "description": "验证 constraint 是否是 key contribution（vs solver choice）。 Greedy + k=8 vs MCKP + k=8 vs both unconstrained。\n",
1026	    "results": {
1027	      "greedy_unconstrained_ppl": 32.45,
1028	      "mckp_unconstrained_ppl": 36.92,
1029	      "greedy_constrained_k8_ppl": 11.23,
1030	      "mckp_constrained_k8_ppl": 11.23,
1031	      "delta_greedy_vs_mckp_constrained": 0.0012,
1032	      "solver_equivalence": true
1033	    },
1034	    "tables": [
1035	      {
1036	        "name": "Solver Equivalence Under Constraint",
1037	        "columns": [
1038	          "method",
1039	          "unconstrained",
1040	          "constrained_k8",
1041	          "delta"
1042	        ],
1043	        "rows": [
1044	          [
1045	            "RateQuant Greedy",
1046	            32.45,
1047	            11.23,
1048	            "—"
1049	          ],
1050	          [
1051	            "MCKP",
1052	            36.92,
1053	            11.23,
1054	            "Δ=0.0012"
1055	          ]
1056	        ]
1057	      }
1058	    ],
1059	    "figures": [],
1060	    "analysis": "在 reframed worst-tier narrative 中，solver equivalence under constraint  成为 Claim 1 的 core evidence。不需要 diagnostic 来 motivate。\n\n\nCore finding：constraint 使 greedy = MCKP（Δ=0.0012 ≈ 0）。 Constrained feasible set 小到 greedy 的 local search 等于 global optimum。 这是 paper 最 robust 的 result——不依赖 diagnostic，不依赖 model choice， 纯数学属性。在 worst tier 下这是 anchor result。\n"
1061	  },
1062	  {
1063	    "name": "Multi-Seed Error Bars (Qwen7B)",
1064	    "description": "3 个 calibration seed 的 constrained MCKP，报告 mean±std。\n",
1065	    "results": {
1066	      "mckp_seed0": 11.02,
1067	      "mckp_seed1": 10.9,
1068	      "mckp_seed2": 11.05,
1069	      "mckp_mean": 10.99,
1070	      "mckp_std": 0.065,
1071	      "uniform_ppl": 15.45,
1072	      "allocation_agreement_3way": 0.902,
1073	      "bit_dist_all_seeds": "2:8, 4:100, 8:4"
1074	    },
1075	    "tables": [
1076	      {
1077	        "name": "Multi-Seed Results (Qwen2.5-7B)",
1078	        "columns": [
1079	          "seed",
1080	          "mckp_ppl",
1081	          "bit_dist",
1082	          "agreement_with_seed0"
1083	        ],
1084	        "rows": [
1085	          [
1086	            "seed_0",
1087	            11.02,
1088	            "8:100:4",
1089	            "—"
1090	          ],
1091	          [
1092	            "seed_1",
1093	            10.9,
1094	            "8:100:4",
1095	            "94.6%"
1096	          ],
1097	          [
1098	            "seed_2",
1099	            11.05,
1100	            "8:100:4",
1101	            "91.1%"
1102	          ],
1103	          [
1104	            "mean±std",
1105	            "10.99±0.065",
1106	            "—",
1107	            "—"
1108	          ]
1109	        ]
1110	      }
1111	    ],
1112	    "figures": [],
1113	    "analysis": "Qwen7B 的 statistical robustness 是 solid。但 N=3 seeds 仍然 limited。 论文应报告 \"our main result is robust to calibration variation\" 但  not claim \"statistical significance\" formally。\n\n\n三个 seed 的 MCKP PPL std=0.065（mean=10.99），95% CI = [10.86, 11.12]。 与 uniform 的 gap（15.45 - 10.99 = 4.46）远大于 CI width（0.26）， Qwen7B 上的 improvement 是 statistically robust。 Bit distribution 三个 seed 完全一致（8:100:4），allocation agreement 90.2% （head-level 有 10% variation 但 bit-level distribution 不变）。 Worst tier 的 concern：14B 上 std 可能更大（sensitivity 更分散 → calibration noise 更大）， 且 improvement 本身在 noise 范围内。\n"
1114	  },
1115	  {
1116	    "name": "Runtime/Latency Benchmark (Qwen7B)",
1117	    "description": "端到端 inference latency 和 throughput。\n",
1118	    "results": {
1119	      "bf16_prefill_ms": 45.86,
1120	      "bf16_decode_ms": 33.78,
1121	      "uniform4_prefill_ms": 54.25,
1122	      "uniform4_decode_ms": 42.46,
1123	      "mckp_prefill_ms": 57.03,
1124	      "mckp_decode_ms": 46.09,
1125	      "mckp_throughput_tok_s": 21.8,
1126	      "uniform4_throughput_tok_s": 23.6,
1127	      "mckp_solver_sec": 0.005,
1128	      "mckp_overhead_vs_uniform_pct": 8.5
1129	    },
1130	    "tables": [
1131	      {
1132	        "name": "Runtime Benchmark (Qwen2.5-7B)",
1133	        "columns": [
1134	          "config",
1135	          "prefill_ms",
1136	          "decode_ms",
1137	          "throughput",
1138	          "memory_MB"
1139	        ],
1140	        "rows": [
1141	          [
1142	            "bf16",
1143	            45.86,
1144	            33.78,
1145	            "29.6 tok/s",
1146	            21.0
1147	          ],
1148	          [
1149	            "uniform 4-bit",
1150	            54.25,
1151	            42.46,
1152	            "23.6 tok/s",
1153	            5.25
1154	          ],
1155	          [
1156	            "MCKP constrained",
1157	            57.03,
1158	            46.09,
1159	            "21.8 tok/s",
1160	            5.25
1161	          ]
1162	        ]
1163	      }
1164	    ],
1165	    "figures": [],
1166	    "analysis": "8.5% latency overhead 是 acceptable trade-off 但仅在 Spread models 上。 Reframe: \"if diagnostic uncertain, use uniform 4-bit to avoid latency cost\"  — 这与 worst-tier narrative 的 \"conservative recommendation\" 一致。\n\n\nMixed-precision MCKP 比 uniform 4-bit 慢 ~8.5%（decode 46.09 vs 42.46 ms/tok）， 因为 mixed bit-width 需要 per-head dequantize dispatch（vs uniform 的 vectorized batch dequant）。 内存相同（5.25 MB），solver 本身 negligible（5ms）。 Worst tier 的 concern：8.5% latency overhead 换 PPL improvement 仅在 Qwen7B 上 worth it—— 在 non-Spread 模型上 overhead 仍存在但 PPL 无 improvement， 纯亏损。Reviewer 会问 \"when is the latency cost justified?\"\n"
1167	  },
1168	  {
1169	    "name": "W9 Compounding Scaling (Worst Tier)",
1170	    "description": "Qwen7B 上 top-k vs random-k 2-bit assignment sweep，刻画 super-additivity。\n",
1171	    "results": {
1172	      "k1_topk_ppl": 9.83,
1173	      "k1_randomk_ppl": 9.89,
1174	      "k4_topk_ppl": 9.85,
1175	      "k4_randomk_ppl": 10.06,
1176	      "k8_topk_ppl": 10.04,
1177	      "k8_randomk_ppl": 11.07,
1178	      "k16_topk_ppl": 10.42,
1179	      "k16_randomk_ppl": 12.91,
1180	      "k32_topk_ppl": 11.6,
1181	      "k32_randomk_ppl": 18.33,
1182	      "k64_topk_ppl": 22.95,
1183	      "k64_randomk_ppl": 55.94,
1184	      "k64_randomk_topk_ratio": 1.45,
1185	      "k32_randomk_topk_ratio": 1.58,
1186	      "k16_randomk_topk_ratio": 1.24,
1187	      "non_monotonic_flag": true,
1188	      "variance_at_k16_masks_trend": true
1189	    },
1190	    "tables": [
1191	      {
1192	        "name": "W9 Compounding (Worst-Tier Interpretation)",
1193	        "columns": [
1194	          "k",
1195	          "topk_ppl",
1196	          "randomk_ppl",
1197	          "randomk_std",
1198	          "ratio",
1199	          "monotonic"
1200	        ],
1201	        "rows": [
1202	          [
1203	            1,
1204	            9.83,
1205	            9.89,
1206	            0.05,
1207	            1.0,
1208	            "—"
1209	          ],
1210	          [
1211	            4,
1212	            9.85,
1213	            10.06,
1214	            0.06,
1215	            1.24,
1216	            "↑"
1217	          ],
1218	          [
1219	            8,
1220	            10.04,
1221	            11.07,
1222	            0.69,
1223	            1.76,
1224	            "↑"
1225	          ],
1226	          [
1227	            16,
1228	            10.42,
1229	            12.91,
1230	            0.4,
1231	            1.24,
1232	            "↓ ⚠️"
1233	          ],
1234	          [
1235	            32,
1236	            11.6,
1237	            18.33,
1238	            2.53,
1239	            1.58,
1240	            "↑"
1241	          ],
1242	          [
1243	            64,
1244	            22.95,
1245	            55.94,
1246	            9.73,
1247	            1.45,
1248	            "↓ ⚠️"
1249	          ]
1250	        ]
1251	      }
1252	    ],
1253	    "figures": [],
1254	    "analysis": "在 worst tier 下，W9 data 的 non-monotonicity 和 high variance  使得 formal super-additivity claim 不成立。 Reframe: 报告为 \"empirical observation of compounding trend with substantial variance\"， 不 formalize 为 theorem 或 proposition。 Compounding 的 qualitative story 仍 hold（ratio >1 at all k>1）， 但 quantitative precision 不足以支撑 formal contribution。\n\n\nWorst-tier 下 k=64 的 randomk/topk ratio 降至 1.45（vs 实际 2.44 的 actual data 中位估计）。 k=8-16 区间出现 non-monotonic：k=8 ratio=1.76 但 k=16 ratio 回落到 1.24， 然后 k=32 又升到 1.58。这种 non-monotonicity 可能来自： (1) random-k 的 seed variance（std=0.4-2.5 across seeds）， (2) top-k 在某些 k 值恰好避开 interaction cluster 而 random 没有。 Non-monotonic behavior 使得 \"super-additivity monotonically increases with k\"  的 clean story 不成立。论文需要 acknowledge variance 并报告 CI。 ratio 的 overall trend 仍是 increasing（1.24→1.45→1.58→1.45）， 但 non-monotonicity at intermediate k 削弱 formalization strength。\n"
1255	  },
1256	  {
1257	    "name": "Qwen2.5-14B Downstream Eval (Predicted)",
1258	    "description": "如果 14B profiling + MCKP 完成，需跑 downstream eval 验证 PPL 与 downstream 一致性。\n",
1259	    "results": {
1260	      "qwen14b_baseline_avg": 0.72,
1261	      "qwen14b_uniform_avg": 0.71,
1262	      "qwen14b_mckp_avg": 0.71,
1263	      "qwen14b_mckp_vs_uniform_pp": 0.1,
1264	      "qwen14b_arc_challenge_delta_pp": -0.5,
1265	      "qwen14b_hellaswag_delta_pp": 0.3
1266	    },
1267	    "tables": [
1268	      {
1269	        "name": "Qwen14B Downstream (Predicted)",
1270	        "columns": [
1271	          "task",
1272	          "uniform",
1273	          "mckp",
1274	          "delta_pp"
1275	        ],
1276	        "rows": [
1277	          [
1278	            "arc_challenge",
1279	            0.58,
1280	            0.575,
1281	            "-0.5"
1282	          ],
1283	          [
1284	            "hellaswag",
1285	            0.72,
1286	            0.723,
1287	            "+0.3"
1288	          ],
1289	          [
1290	            "piqa",
1291	            0.81,
1292	            0.811,
1293	            "+0.1"
1294	          ],
1295	          [
1296	            "winogrande",
1297	            0.73,
1298	            0.728,
1299	            "-0.2"
1300	          ],
1301	          [
1302	            "average",
1303	            0.71,
1304	            0.71,
1305	            "+0.1"
1306	          ]
1307	        ]
1308	      }
1309	    ],
1310	    "figures": [],
1311	    "analysis": "Downstream 确认 14B false positive——不仅 PPL 无 improvement， downstream 也在 noise。论文需要 transparent reporting。\n\nPPL improvement +1.2% → downstream ≈ 0pp（noise）。 arc_challenge 可能略负（-0.5pp），与跨模型的 arc_challenge 系统性敏感一致。 hellaswag 略正（+0.3pp）但在 seed noise 范围内。 整体结论：14B downstream 与 PPL 一致——MCKP 无 meaningful benefit。\n"
1312	  }
1313	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b31af4c-7a94-48d3-b0b2-b2eaaa336867",
  "isSidechain": false,
  "promptId": "e8e8fea0-d6a9-4b91-8885-3140c3cbe799",
  "type": "user",
  "uuid": "5462c821-0f6b-4b98-9268-9911ff1d8362",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Qwen2.5-14B Hires Profiling\",\n    \"description\": \"Qwen2.5-14B hires bf16 2-bit-only profiling（48 layers × 8 KV heads = 384 heads）。 测试 diagnostic 是否在 Qwen 模型族内泛化。\\n\",\n    \"results\": {\n      \"qwen14b_baseline_ppl\": 5.84,\n      \"qwen14b_top5_concentration\": 0.55,\n      \"qwen14b_t1_t5\": 0.63,\n      \"qwen14b_l0_dominance_ratio\": 8.2,\n      \"qwen14b_top1_head\": \"L0H2\",\n      \"qwen14b_top1_delta_2bit\": 3.81,\n      \"qwen14b_l0_4heads_total_share\": 0.41,\n      \"qwen14b_delta_2bit_cv\": 5.12,\n      \"qwen14b_positive_delta_heads\": 370,\n      \"qwen14b_total_heads\": 384,\n      \"qwen14b_distribution_shape\": \"borderline_spread\",\n      \"diagnostic_prediction\": \"Spread (conc≥0.50 AND t₁/t₅≤0.70)\",\n      \"diagnostic_correct\": false\n    },\n    \"tables\": [\n      {\n        \"name\": \"Qwen Family Profiling Comparison\",\n        \"columns\": [\n          \"model\",\n          \"layers\",\n          \"kv_heads\",\n          \"concentration\",\n          \"t1_t5\",\n          \"l0_share\",\n          \"top1_delta\",\n          \"shape\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen2.5-7B\",\n            28,\n            112,\n            0.61,\n            0.57,\n            \"58.6%\",\n            6.74,\n            \"Spread\"\n          ],\n          [\n            \"Qwen2.5-14B\",\n            48,\n            384,\n            0.55,\n            0.63,\n            \"41.0%\",\n            3.81,\n            \"Diluted Spread\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Diagnostic 两个指标都刚过阈值（concentration 0.55 > 0.50, t₁/t₅ 0.63 < 0.70）， 但边际通过。14B 的关键问题：更多层分摊了 sensitivity，使得 L0 的 dominance 不足以 让 MCKP 产生有意义的 allocation 差异。这暴露了 joint diagnostic 的 boundary fragility—— 阈值在 border 附近不 robust。\\n\\n\\nQwen2.5-14B 有 48 layers × 8 KV heads = 384 heads（vs 7B 的 28×4=112）。 GQA 仍是 7:1，保留 L0 某些 heads 的较高 sensitivity（concentration=0.55，刚过 0.50 阈值）。 但 14B 的 L0 cluster 比 7B 弱得多：7B 的 L0 4 heads 占 total delta 的 58.6%， 而 14B 的 L0 heads 仅占 41%——48 层分摊了 sensitivity。t₁/t₅=0.63（<0.70）， 表面看满足 Spread 两个条件。但实际上 14B 的 \\\"spread\\\" 是 illusory： L0 heads 的 cross-bitwidth gradient 比 7B 弱（top1 delta=3.81 vs 7B 的 6.74）， 且 sensitivity 在 L0-L3 多层间分散而非集中在 L0 单层。 这是一种 \\\"diluted spread\\\"——diagnostic 判定为 Spread 但 MCKP 无法有效利用。\\n\"\n  },\n  {\n    \"name\": \"Qwen2.5-14B Constrained MCKP\",\n    \"description\": \"基于 14B hires profiling 跑 constrained MCKP（k=8），评估 PPL。 如果 improvement ≈0%，则 diagnostic 出现 false positive。\\n\",\n    \"results\": {\n      \"qwen14b_baseline_ppl\": 5.84,\n      \"qwen14b_uniform_4bit_ppl\": 7.02,\n      \"qwen14b_mckp_constrained_k8_ppl\": 6.94,\n      \"qwen14b_mckp_improvement_over_uniform_pct\": 1.2,\n      \"qwen14b_mckp_unconstrained_ppl\": 8.41,\n      \"qwen14b_unconstrained_ratio\": 1.44,\n      \"qwen14b_bit_distribution\": {\n        \"2\": 8,\n        \"4\": 372,\n        \"8\": 4\n      },\n      \"qwen14b_greedy_constrained_ppl\": 6.94,\n      \"qwen14b_solver_equivalence_delta\": 0.0,\n      \"decision_rule_accuracy_6models\": 5,\n      \"decision_rule_total_models\": 6,\n      \"false_positive_model\": \"Qwen2.5-14B\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Qwen2.5-14B Allocation Results\",\n        \"columns\": [\n          \"method\",\n          \"ppl\",\n          \"compression\",\n          \"vs_uniform\"\n        ],\n        \"rows\": [\n          [\n            \"baseline bf16\",\n            5.84,\n            \"1×\",\n            \"—\"\n          ],\n          [\n            \"uniform 4-bit\",\n            7.02,\n            \"4×\",\n            \"baseline\"\n          ],\n          [\n            \"constrained MCKP k=8\",\n            6.94,\n            \"4×\",\n            \"+1.2%\"\n          ],\n          [\n            \"unconstrained MCKP\",\n            8.41,\n            \"4×\",\n            \"-19.8%\"\n          ],\n          [\n            \"constrained greedy k=8\",\n            6.94,\n            \"4×\",\n            \"+1.2%\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Decision Rule Accuracy (6 Models)\",\n        \"columns\": [\n          \"model\",\n          \"concentration\",\n          \"t1_t5\",\n          \"diagnostic_prediction\",\n          \"actual_benefit\",\n          \"correct\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen2.5-7B\",\n            0.61,\n            0.57,\n            \"Spread\",\n            \"+27.3%\",\n            \"✅\"\n          ],\n          [\n            \"Qwen2.5-14B\",\n            0.55,\n            0.63,\n            \"Spread\",\n            \"+1.2%\",\n            \"❌ FP\"\n          ],\n          [\n            \"Yi-1.5-9B\",\n            0.71,\n            0.9,\n            \"Spike\",\n            \"≈0%\",\n            \"✅\"\n          ],\n          [\n            \"Llama-3.1-8B\",\n            0.57,\n            0.71,\n            \"Spike\",\n            \"+0.2%\",\n            \"✅\"\n          ],\n          [\n            \"Mistral-7B\",\n            0.24,\n            0.18,\n            \"Flat\",\n            \"-0.4%\",\n            \"✅\"\n          ],\n          [\n            \"Gemma-2-9B\",\n            0.23,\n            0.38,\n            \"Flat\",\n            \"-0.3%\",\n            \"✅\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Qwen14B 是 diagnostic 的致命反例：同一模型族（Qwen），同一 GQA ratio（7:1）， concentration 和 t₁/t₅ 都满足 Spread 条件，但 MCKP 改进仅 1.2%。 根本原因是 more layers dilute sensitivity，使得 per-head allocation 无法 exploit  sufficient heterogeneity。这说明 diagnostic 缺少第三个维度：total_kv_heads 或 layer_count。 但增加维度后 N=6 的样本量完全不足以 fit 三维 boundary。 Decision rule 降至 5/6 且 failure 发生在 high-confidence prediction（both metrics pass）， 这不是 borderline miss 而是 systematic failure — 严重削弱 diagnostic claim。\\n\\n\\nMCKP constrained PPL=6.94 vs uniform=7.02，improvement 仅 +1.2%（0.08 PPL gap）。 对比 Qwen7B 的 +27.3%（4.53 PPL gap），14B 的 improvement 在噪声范围内。 原因：14B 有 384 heads，每个 head 承载的 information 更少（head_dim 同为 128，但 48 层分摊）， 2-bit 降级的 per-head cost 更小。MCKP 将 L0 的 4 heads 分配到 8-bit，但这仅节省了 total budget 的很小部分——384 heads 中 4 个 8-bit heads 的 budget 释放被稀释到其余 380 heads， 每个 head 只多获得 ~0.01 bit，不足以改变 bit-width assignment。 Unconstrained ratio=1.44×（类似 Gemma-2 的 1.47×），solver 将 ~80 heads 分配到 2-bit， 产生 moderate 而非 catastrophic degradation。 Decision rule accuracy 从 5/5 降至 5/6：14B 是 false positive（diagnostic 预测 benefit，实际无）。\\n\"\n  },\n  {\n    \"name\": \"Gemma-2 Constrained MCKP with BOS Fix\",\n    \"description\": \"用 sliding_window + BOS prepend 修正 eval，重测 Gemma-2 constrained MCKP 和 unconstrained baselines。 BOS bug 可能导致之前的 1.47× unconstrained ratio 和 -0.3% constrained delta 不准确。\\n\",\n    \"results\": {\n      \"gemma2_bos_fix_baseline_ppl\": 6.03,\n      \"gemma2_bos_fix_uniform_4bit_ppl\": 6.17,\n      \"gemma2_bos_fix_constrained_mckp_ppl\": 6.22,\n      \"gemma2_bos_fix_constrained_vs_uniform_pct\": -0.8,\n      \"gemma2_bos_fix_unconstrained_greedy_ppl\": 7.38,\n      \"gemma2_bos_fix_unconstrained_ratio\": 1.22,\n      \"gemma2_bos_fix_n2bit_unconstrained\": 106,\n      \"gemma2_bos_fix_constrained_bit_dist\": {\n        \"2\": 8,\n        \"4\": 324,\n        \"8\": 4\n      },\n      \"gemma2_old_unconstrained_ratio\": 1.47,\n      \"gemma2_ratio_shift\": -0.25\n    },\n    \"tables\": [\n      {\n        \"name\": \"Gemma-2 BOS Fix Impact\",\n        \"columns\": [\n          \"metric\",\n          \"before_bos_fix\",\n          \"after_bos_fix\",\n          \"delta\"\n        ],\n        \"rows\": [\n          [\n            \"baseline PPL\",\n            \"711.6 (buggy) / 6.03 (corrected)\",\n            6.03,\n            \"—\"\n          ],\n          [\n            \"uniform 4-bit PPL\",\n            6.17,\n            6.17,\n            \"0.00\"\n          ],\n          [\n            \"unconstrained ratio\",\n            \"1.47×\",\n            \"1.22×\",\n            \"-0.25×\"\n          ],\n          [\n            \"constrained vs uniform\",\n            \"-0.3%\",\n            \"-0.8%\",\n            \"-0.5pp\"\n          ],\n          [\n            \"2-bit heads (unconstrained)\",\n            106,\n            106,\n            \"0\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Revised Three-Tier Labels (COLLAPSED)\",\n        \"columns\": [\n          \"tier\",\n          \"ratio_range\",\n          \"models\",\n          \"count\"\n        ],\n        \"rows\": [\n          [\n            \"Catastrophic\",\n            \"≥2.0×\",\n            \"Qwen2.5-7B (3.31×)\",\n            1\n          ],\n          [\n            \"Moderate (EMPTY)\",\n            \"1.25-2.0×\",\n            \"—\",\n            0\n          ],\n          [\n            \"Mild\",\n            \"1.0-1.25×\",\n            \"Yi 1.08×, Llama 1.07×, Mistral 1.08×, Gemma-2 1.22×\",\n            4\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"三档标签失去 moderate 层：Catastrophic (1 model) + Mild (4 models)， 变成 binary 而非 gradient。原本 \\\"concentration-dependent gradient\\\" 叙事中 Gemma-2 是关键中间证据（flat-high-2bit mechanism），现在该机制的 magnitude  被 BOS bug 虚增。修正后 1.22× 的 over-allocation 仍比 Yi/Llama/Mistral 高， 但 gap 缩小到 0.14-0.15×，可能在 noise 范围内。 论文需要重新校准：要么放弃三档（改用连续变量 regression）， 要么承认 moderate tier 的 evidence 不 robust。\\n\\n\\nBOS fix 降低了 baseline PPL（711.6→6.03 已确认），也降低了 quantized PPL。 关键：BOS bug 对 unconstrained allocation 的影响是 non-uniform 的—— 106 个 2-bit heads 的 joint distortion 在有 BOS token 时部分被 BOS 的 attention mass 吸收 （BOS 通常获得高 attention weight，为后续 token 提供 anchor）， 没有 BOS 时这些 heads 的 distortion 被放大。 修正后 unconstrained ratio 从 1.47× 降至 1.22×，落入 mild 范围（1.07-1.22×）， 与 Yi/Llama/Mistral 的 1.07-1.08× 更接近。 三档标签崩塌：原本 Gemma-2 是 \\\"moderate\\\" 独占，现在没有 moderate 了—— 只有 catastrophic（Qwen7B 3.31×）和 mild（其余 4 个模型 1.07-1.22×）。 Constrained vs uniform 变为 -0.8%（从 -0.3%），方向不变但幅度增大。\\n\"\n  },\n  {\n    \"name\": \"L0 Auto-Discovery (No L0 Exclusion)\",\n    \"description\": \"去掉 L0 exclusion 硬约束，仅保留 max_2bit=8，观察 solver 是否仍将 L0 heads 分配到 8-bit。\\n\",\n    \"results\": {\n      \"qwen7b_no_l0excl_ppl\": 11.23,\n      \"qwen7b_l0_heads_assigned_8bit\": 4,\n      \"qwen7b_solver_auto_discovers_l0\": true,\n      \"qwen14b_no_l0excl_ppl\": 6.97,\n      \"qwen14b_l0_heads_assigned_8bit\": 2,\n      \"qwen14b_solver_partial_discovery\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"L0 Auto-Discovery Across Qwen Family\",\n        \"columns\": [\n          \"model\",\n          \"l0_dominance\",\n          \"l0_8bit_heads\",\n          \"total_8bit_budget\",\n          \"ppl\",\n          \"auto_discovery\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen2.5-7B\",\n            \"26×\",\n            \"4/4\",\n            4,\n            11.23,\n            \"Full ✅\"\n          ],\n          [\n            \"Qwen2.5-14B\",\n            \"8.2×\",\n            \"2/8\",\n            4,\n            6.97,\n            \"Partial ⚠️\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Auto-discovery 在 7B 上完美，在 14B 上部分失败。 Reframed narrative 中这不是 critical：constraint 的价值不依赖 auto-discovery， constraint 的 contribution 是 preventing compounding 而非 discovering structure。\\n\\n\\nQwen7B：solver 从 profiling data 自动将 L0 全部 4 heads 分配到 8-bit（delta 极高，cost-benefit ratio 最优），PPL=11.23 不变。这在 7B 上 works 因为 L0 dominance ratio=26×。 Qwen14B：solver 仅将 L0 的 2/8 heads 分配到 8-bit（L0 dominance ratio 仅 8.2×，不够突出）， 其余 2 个 8-bit 名额给了 L2-L3 的 moderate-delta heads。PPL=6.97（vs constrained 6.94）， 差异很小但说明 14B 的 L0 不再是 unambiguous dominant——auto-discovery 部分失败。\\n\"\n  },\n  {\n    \"name\": \"Llama-3.1-8B Full Pipeline\",\n    \"description\": \"Llama-3.1-8B (GQA 4:1) 全 pipeline：profile → constrained MCKP → eval。\\n\",\n    \"results\": {\n      \"llama_baseline_ppl\": 8.09,\n      \"llama_uniform_4bit_ppl\": 8.47,\n      \"llama_mckp_constrained_ppl\": 8.45,\n      \"llama_improvement_pct\": 0.2,\n      \"llama_unconstrained_ratio\": 1.07,\n      \"llama_concentration\": 0.57,\n      \"llama_t1_t5\": 0.71,\n      \"llama_shape\": \"Spike (borderline)\",\n      \"llama_natural_k\": 2\n    },\n    \"tables\": [\n      {\n        \"name\": \"Llama-3.1-8B Results\",\n        \"columns\": [\n          \"method\",\n          \"ppl\",\n          \"compression\",\n          \"vs_uniform\"\n        ],\n        \"rows\": [\n          [\n            \"baseline bf16\",\n            8.09,\n            \"1×\",\n            \"—\"\n          ],\n          [\n            \"uniform 4-bit\",\n            8.47,\n            \"4×\",\n            \"baseline\"\n          ],\n          [\n            \"constrained MCKP k=8\",\n            8.45,\n            \"4×\",\n            \"+0.2%\"\n          ],\n          [\n            \"unconstrained\",\n            8.63,\n            \"4×\",\n            \"-1.9%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Negative result 在 worst tier 下保持。但 t₁/t₅=0.71 的 borderline 值  使 diagnostic 对 Llama 的分类依赖 ±0.01 的阈值精度——如果阈值设为 0.75， Llama 会被误分为 Spread，增加 false positive 风险。\\n\\n\\nLlama 的 concentration=0.57 接近 0.50 阈值但 t₁/t₅=0.71 刚好超过 0.70， 被分类为 Spike。实际上 MCKP 仅选择 2 个 heads 做 2-bit（natural k=2）， constraint 从不 bind。+0.2% improvement 在 noise 范围内。 在 worst tier 下，Llama 的 borderline t₁/t₅=0.71 使得 diagnostic boundary  的 robustness 受质疑——0.70 是 arbitrary cutoff。\\n\"\n  },\n  {\n    \"name\": \"Mistral-7B-v0.3 Full Pipeline\",\n    \"description\": \"Mistral-7B-v0.3 全 pipeline，Flat distribution 代表。\\n\",\n    \"results\": {\n      \"mistral_baseline_ppl\": 7.04,\n      \"mistral_uniform_4bit_ppl\": 7.13,\n      \"mistral_mckp_constrained_ppl\": 7.16,\n      \"mistral_improvement_pct\": -0.4,\n      \"mistral_unconstrained_ratio\": 1.08,\n      \"mistral_concentration\": 0.24,\n      \"mistral_t1_t5\": 0.18,\n      \"mistral_shape\": \"Flat\",\n      \"mistral_k_monotonic\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Mistral-7B Results\",\n        \"columns\": [\n          \"method\",\n          \"ppl\",\n          \"compression\",\n          \"vs_uniform\"\n        ],\n        \"rows\": [\n          [\n            \"baseline bf16\",\n            7.04,\n            \"1×\",\n            \"—\"\n          ],\n          [\n            \"uniform 4-bit\",\n            7.13,\n            \"4×\",\n            \"baseline\"\n          ],\n          [\n            \"constrained MCKP k=4\",\n            7.16,\n            \"4×\",\n            \"-0.4%\"\n          ],\n          [\n            \"unconstrained\",\n            7.57,\n            \"4×\",\n            \"-6.2%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Mistral 是最 clean 的 negative case——profiler signal ≈0， 任何 non-uniform allocation 都 ≤ uniform。在 reframed narrative 中 是 \\\"systematic negative result\\\" 的核心证据之一。\\n\\n\\nMistral concentration=0.24（远低于 0.50），profiler 信号几乎为零。 Constrained MCKP 比 uniform 差 0.4%——solver 分配的 2-bit heads  实际上比 uniform 的 all-4bit 更差。k ablation 单调递增证明  每多一个 2-bit head 都 hurts。在 worst tier 下这是 clean negative， 直接支持 \\\"uniform suffices on flat models\\\" 的叙事。\\n\"\n  },\n  {\n    \"name\": \"Compounding Effect Sweep (Qwen7B)\",\n    \"description\": \"Qwen2.5-7B 上 sweep max_2bit 从 0 到 112，绘制 PPL vs k curve。\\n\",\n    \"results\": {\n      \"qwen_k0_ppl\": 15.45,\n      \"qwen_k4_ppl\": 11.93,\n      \"qwen_k8_ppl\": 11.23,\n      \"qwen_k10_ppl\": 11.18,\n      \"qwen_k12_ppl\": 11.21,\n      \"qwen_k16_ppl\": 11.52,\n      \"qwen_k24_ppl\": 13.07,\n      \"qwen_k48_ppl\": 19.84,\n      \"qwen_k75_ppl\": 28.36,\n      \"qwen_k112_ppl\": 36.92,\n      \"elbow_k\": 8,\n      \"curve_shape\": \"U-shape with clear minimum at k≈8-10\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Compounding Sweep (Qwen2.5-7B, budget=0.25)\",\n        \"columns\": [\n          \"max_2bit_k\",\n          \"ppl\",\n          \"delta_vs_k8\"\n        ],\n        \"rows\": [\n          [\n            0,\n            15.45,\n            \"+37.6%\"\n          ],\n          [\n            4,\n            11.93,\n            \"+6.2%\"\n          ],\n          [\n            8,\n            11.23,\n            \"baseline (optimal)\"\n          ],\n          [\n            12,\n            11.21,\n            \"-0.2%\"\n          ],\n          [\n            16,\n            11.52,\n            \"+2.6%\"\n          ],\n          [\n            24,\n            13.07,\n            \"+16.4%\"\n          ],\n          [\n            48,\n            19.84,\n            \"+76.7%\"\n          ],\n          [\n            112,\n            36.92,\n            \"+228.8%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Compounding curve 是 paper 的 core figure 之一，在 Qwen 上有力。 但在 worst tier 下，其意义从 \\\"universal phenomenon\\\" 缩小为 \\\"Spread-model-specific phenomenon\\\"。Reframe:  compounding 的 magnitude 和 shape 是 architecture-dependent， 但 constraint 在所有模型上都是 safe（≤ uniform）。\\n\\n\\nQwen7B 的 compounding curve 有清晰 U-shape：k 太小（budget 浪费在不需要的 higher-bit heads）， k 太大（compounding 恶化）。Optimal k=8-10 对应 L0 cluster 的 head 数量。 这是 Qwen7B 的固有特性，worst tier 不改变此结果。 但 worst tier 的问题是：此 curve 是否跨模型可复现？ Llama/Mistral 的 k-PPL curve 平坦或单调，没有 U-shape—— compounding 的 \\\"dramatic elbow\\\" 是 Spread-specific，不 universal。\\n\"\n  },\n  {\n    \"name\": \"Budget Sweep (Qwen7B, 2×/4×/8×)\",\n    \"description\": \"Qwen2.5-7B 在三种压缩率下 constrained MCKP vs uniform。\\n\",\n    \"results\": {\n      \"qwen_2x_uniform_ppl\": 10.07,\n      \"qwen_2x_mckp_ppl\": 9.89,\n      \"qwen_2x_improvement_pct\": 1.8,\n      \"qwen_4x_uniform_ppl\": 15.45,\n      \"qwen_4x_mckp_ppl\": 11.23,\n      \"qwen_4x_improvement_pct\": 27.3,\n      \"qwen_8x_uniform_ppl\": 2644.0,\n      \"qwen_8x_mckp_ppl\": 42.6,\n      \"qwen_8x_improvement_pct\": 98.4\n    },\n    \"tables\": [\n      {\n        \"name\": \"Budget Sweep (Qwen2.5-7B)\",\n        \"columns\": [\n          \"compression\",\n          \"uniform_ppl\",\n          \"mckp_ppl\",\n          \"improvement\"\n        ],\n        \"rows\": [\n          [\n            \"2× (0.50)\",\n            10.07,\n            9.89,\n            \"+1.8%\"\n          ],\n          [\n            \"4× (0.25)\",\n            15.45,\n            11.23,\n            \"+27.3%\"\n          ],\n          [\n            \"8× (0.125)\",\n            2644.0,\n            42.6,\n            \"+98.4%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Budget sweep 在 Qwen 上 compelling。Reframe under worst tier: aggressive compression（5.3×+）即使在 non-Spread 模型上也有 cardinality constraint  的价值（Llama 5.3×: 57.60 vs 2644）——constraint 在极端场景下 universally 有用。\\n\\n\\n2× 压缩：budget 充裕（avg 8-bit），大部分 heads 在安全区，仅 1.8% 改进。 4× 是 sweet spot（27.3%），与已有结果一致。 8× 极端压缩下 uniform = all 2-bit（PPL 2644），constrained MCKP 保护 critical heads 大幅降低 PPL（42.6），但绝对质量仍很差。 Worst tier 不改变 Qwen7B 数字，但 cross-model budget sweep （如果做的话）会显示 Llama/Mistral 在 2× 和 4× 都无 improvement。\\n\"\n  },\n  {\n    \"name\": \"High-Resolution Profiling (Qwen7B)\",\n    \"description\": \"64 seq × 2048 tokens hires profiling，重跑 MCKP。\\n\",\n    \"results\": {\n      \"hires_constrained_ppl\": 10.91,\n      \"lowres_constrained_ppl\": 11.23,\n      \"hires_improvement_over_lowres_pct\": 2.8,\n      \"hires_nonzero_2bit\": 100,\n      \"lowres_nonzero_2bit\": 37,\n      \"hires_profiling_time_min\": 65.5,\n      \"allocation_diff_count\": 8\n    },\n    \"tables\": [\n      {\n        \"name\": \"Profiling Resolution Comparison\",\n        \"columns\": [\n          \"resolution\",\n          \"nonzero_heads\",\n          \"constrained_ppl\",\n          \"time_min\"\n        ],\n        \"rows\": [\n          [\n            \"16×512 (lowres)\",\n            37,\n            11.23,\n            \"~10\"\n          ],\n          [\n            \"64×2048 (hires)\",\n            100,\n            10.91,\n            65.5\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Hires 提供 modest improvement，但 profiling cost 6× 增加。 在 reframed narrative 中，hires vs lowres 是 secondary concern—— constraint 的 contribution 不依赖 profiling resolution。\\n\\n\\nHires profiling 发现更多 non-zero 2-bit delta heads（100 vs 37）， 改善 MCKP allocation（PPL 10.91 vs 11.23，+2.8%）。 8 个 heads 的 allocation 改变（从 4-bit 到 2-bit 或反向）， 说明 lowres 有 ~7% 的 misallocation。 在 worst tier 下，hires 对 Qwen7B 有 modest benefit， 但对 non-Spread 模型（Llama hires: 8.45 vs 8.50）几乎无差。 且 hires profiling 耗时 65 min（vs lowres ~10 min）， cost/benefit ratio 在非 Spread 模型上 unjustified。\\n\"\n  },\n  {\n    \"name\": \"C4 Cross-Dataset Evaluation (Qwen7B)\",\n    \"description\": \"C4 calibration + WikiText-2 evaluation，测试跨 dataset robustness。\\n\",\n    \"results\": {\n      \"c4_cal_wt2_eval_mckp_ppl\": 11.29,\n      \"c4_cal_wt2_eval_uniform_ppl\": 15.45,\n      \"c4_cal_wt2_eval_improvement_pct\": 26.9,\n      \"allocation_agreement_c4_vs_wt2\": 0.964,\n      \"agreement_heads\": \"108/112\",\n      \"cross_domain_wt2_to_c4_mckp_ppl\": 20.56,\n      \"cross_domain_wt2_to_c4_uniform_ppl\": 35.42\n    },\n    \"tables\": [\n      {\n        \"name\": \"C4 Cross-Dataset (Qwen2.5-7B)\",\n        \"columns\": [\n          \"calibration\",\n          \"eval\",\n          \"mckp_ppl\",\n          \"uniform_ppl\",\n          \"improvement\"\n        ],\n        \"rows\": [\n          [\n            \"WikiText-2\",\n            \"WikiText-2\",\n            11.29,\n            15.45,\n            \"26.9%\"\n          ],\n          [\n            \"C4\",\n            \"WikiText-2\",\n            11.29,\n            15.45,\n            \"26.9%\"\n          ],\n          [\n            \"WikiText-2\",\n            \"C4\",\n            20.56,\n            35.42,\n            \"42.0%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cross-dataset robustness 在 Qwen7B 上 strong（L0 dominance 使得 allocation 稳定）。 但这不 extend 到 non-Spread 模型或 14B（where L0 is less dominant）。\\n\\n\\nAllocation agreement 96.4% 说明 calibration source 对 Qwen7B 影响很小 （112 heads 中仅 4 个 disagree）。这是 因为 L0 的 extreme dominance  在任何 distribution 上都一致——agreement 本质上是 \\\"L0 is always dominant\\\"。 Cross-domain PPL（20.56）比 same-domain（11.29）高很多， 但 vs uniform 仍有大幅改善（20.56 vs 35.42）。 Worst tier 的问题：14B 上 agreement 可能更低（L0 dominance 弱， mid-layer allocation 更 distribution-dependent）。\\n\"\n  },\n  {\n    \"name\": \"RateQuant Greedy Comparison\",\n    \"description\": \"RateQuant greedy (Algorithm 1) on {2,4,8,16} vs constrained MCKP。\\n\",\n    \"results\": {\n      \"greedy_unconstrained_ppl\": 32.45,\n      \"mckp_unconstrained_ppl\": 36.92,\n      \"greedy_constrained_k8_ppl\": 11.23,\n      \"mckp_constrained_k8_ppl\": 11.23,\n      \"greedy_constrained_delta_vs_mckp\": 0.0012,\n      \"bit_distribution\": {\n        \"2\": 8,\n        \"4\": 100,\n        \"8\": 4\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Solver Comparison (Qwen2.5-7B, budget=0.25)\",\n        \"columns\": [\n          \"method\",\n          \"unconstrained_ppl\",\n          \"constrained_k8_ppl\"\n        ],\n        \"rows\": [\n          [\n            \"RateQuant Greedy\",\n            32.45,\n            11.23\n          ],\n          [\n            \"MCKP\",\n            36.92,\n            11.23\n          ],\n          [\n            \"Uniform 4-bit\",\n            \"—\",\n            15.45\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Solver equivalence under constraint 是 robust result，在 worst tier 下 成为 paper 的 core contribution 之一（不依赖 diagnostic）。\\n\\n\\nUnconstrained greedy (32.45) 和 MCKP (36.92) 都 catastrophically fail。 Constrained 后两者 converge（Δ=0.0012 ≈ 0）。 这是 \\\"constraint is the contribution, not the solver\\\" 的 strongest evidence。 Worst tier 不改变此结论——solver equivalence under constraint  是 Qwen7B 的数学属性（constrained feasible set small enough）， 无论 diagnostic 是否成立。\\n\"\n  },\n  {\n    \"name\": \"Oracle Comparison (Brute-Force Subset)\",\n    \"description\": \"Qwen7B 3-4 layer groups 上 brute-force optimal vs MCKP。\\n\",\n    \"results\": {\n      \"mckp_ppl\": 10.91,\n      \"max_oracle_gap_ppl\": 0.0183,\n      \"avg_oracle_gap_ppl\": 0.0046,\n      \"layers_mckp_optimal\": \"5/8\",\n      \"gap_nature\": \"2-bit head position swap within same bit budget\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Oracle vs MCKP (Qwen2.5-7B Subset)\",\n        \"columns\": [\n          \"layer_group\",\n          \"mckp_ppl\",\n          \"oracle_ppl\",\n          \"gap\"\n        ],\n        \"rows\": [\n          [\n            \"L0-L3\",\n            10.91,\n            10.91,\n            0.0\n          ],\n          [\n            \"L1\",\n            \"—\",\n            \"—\",\n            0.0183\n          ],\n          [\n            \"L4\",\n            \"—\",\n            \"—\",\n            0.0045\n          ],\n          [\n            \"L11\",\n            \"—\",\n            \"—\",\n            0.0136\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Near-optimality 是 standalone result，加强 constraint contribution。\\n\\n\\nMCKP gap to oracle 极小（max 0.0183 PPL），5/8 layers 完全 optimal。 Gap 来源：3 个 layer 上 MCKP 选了 slightly suboptimal 的 2-bit head 位置， 但 bit budget 完全相同——差异仅在 which head gets 2-bit，非结构性错误。 即使在 worst tier 下，MCKP near-optimality 成立——这不依赖 diagnostic。\\n\"\n  },\n  {\n    \"name\": \"Cross-Domain Calibration Robustness\",\n    \"description\": \"C4 calibrate / WikiText-2 evaluate 及反向，报告 allocation agreement。\\n\",\n    \"results\": {\n      \"qwen_agreement\": 0.964,\n      \"llama_agreement\": 0.977,\n      \"mistral_agreement\": 0.965,\n      \"qwen14b_predicted_agreement\": 0.88\n    },\n    \"tables\": [\n      {\n        \"name\": \"Cross-Calibration Agreement\",\n        \"columns\": [\n          \"model\",\n          \"agreement\",\n          \"heads_agree\",\n          \"total\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen2.5-7B\",\n            \"96.4%\",\n            108,\n            112\n          ],\n          [\n            \"Llama-3.1-8B\",\n            \"97.7%\",\n            250,\n            256\n          ],\n          [\n            \"Mistral-7B\",\n            \"96.5%\",\n            247,\n            256\n          ],\n          [\n            \"Qwen2.5-14B (predicted)\",\n            \"~88%\",\n            \"~338\",\n            384\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cross-calibration robustness 在小模型上 strong， 但可能不 scale to larger models（more heads → more ambiguity）。\\n\\n\\n三个 7-9B 模型都有 >96% agreement，说明 calibration robust。 但 worst tier 预测 Qwen14B 的 agreement 可能降至 ~88%， 因为 14B 的 sensitivity 更分散、mid-layer heads 的 ranking  更 distribution-dependent。这削弱 \\\"one-shot calibration\\\" 的 practicality claim。\\n\"\n  },\n  {\n    \"name\": \"Head Sensitivity Visualization\",\n    \"description\": \"Paper-quality figures: per-head delta heatmap, compounding curve, allocation comparison。\\n\",\n    \"results\": {\n      \"figures_generated\": 5,\n      \"key_visual\": \"5-model heatmap comparison shows architecture diversity\",\n      \"worst_tier_impact\": \"14B heatmap looks like diluted version of 7B, weakens family consistency\"\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Visualization 诚实展示 diagnostic 的 limitation 反而增加 credibility。 14B false positive 在 scatter plot 上是 visible anomaly，需要 explicit 讨论。\\n\\n\\nVisualization 不产生新数据但在 worst tier 下需要更新： (1) 加入 14B heatmap 显示 diluted spread pattern（与 7B 对比削弱 Qwen family story） (2) 三档 gradient bar chart 中 moderate 消失（Gemma-2 BOS fix） (3) Decision rule scatter 中 14B 落在 Spread 象限但标记为 false positive\\n\"\n  },\n  {\n    \"name\": \"Downstream Task Evaluation (Qwen7B)\",\n    \"description\": \"ARC-C / HellaSwag / PIQA / WinoGrande on Qwen7B + 4 non-Spread models at 4×。\\n\",\n    \"results\": {\n      \"qwen_avg_recovery\": 0.728,\n      \"qwen_arc_c_delta_pp\": 3.16,\n      \"qwen_hellaswag_delta_pp\": 4.0,\n      \"yi_mckp_vs_uniform_pp\": -0.77,\n      \"llama_mckp_vs_uniform_pp\": -0.99,\n      \"mistral_mckp_vs_uniform_pp\": -0.48,\n      \"gemma2_mckp_vs_uniform_pp\": 0.14,\n      \"qwen14b_predicted_mckp_vs_uniform_pp\": -0.2\n    },\n    \"tables\": [\n      {\n        \"name\": \"Downstream Summary (6 Models)\",\n        \"columns\": [\n          \"model\",\n          \"shape\",\n          \"mckp_vs_uniform_pp\",\n          \"diagnostic_correct\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen2.5-7B\",\n            \"Spread\",\n            \"+2.60pp\",\n            \"✅\"\n          ],\n          [\n            \"Qwen2.5-14B\",\n            \"Diluted Spread\",\n            \"-0.2pp (noise)\",\n            \"❌ FP\"\n          ],\n          [\n            \"Yi-1.5-9B\",\n            \"Spike\",\n            \"-0.77pp\",\n            \"✅\"\n          ],\n          [\n            \"Llama-3.1-8B\",\n            \"Spike\",\n            \"-0.99pp\",\n            \"✅\"\n          ],\n          [\n            \"Mistral-7B\",\n            \"Flat\",\n            \"-0.48pp\",\n            \"✅\"\n          ],\n          [\n            \"Gemma-2-9B\",\n            \"Flat\",\n            \"+0.14pp (noise)\",\n            \"✅\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Downstream data 在 worst tier 下 reinforces \\\"1/6 models benefit\\\"—— 更适合 framing 为 systematic negative result + one strong positive case study。\\n\\n\\n5-model downstream data 完整，结果与 PPL 一致。 Worst tier 预测 Qwen14B downstream：MCKP vs uniform ≈ -0.2pp（与 PPL 的 +1.2% 不一致方向？ 不，PPL improvement +1.2% 意味着 MCKP 稍好，downstream 可能 +0.1-0.3pp 或 noise）。 但 14B 的 downstream 数据不足以区分 signal vs noise（无 multi-seed CI）。 论文需报告 14B 但不能 claim benefit。\\n\"\n  },\n  {\n    \"name\": \"70B Profiling-Only (Qwen2.5-72B)\",\n    \"description\": \"Qwen2.5-72B distortion profiling（不做 eval），分析 sensitivity 是否随 model size 缩放。\\n\",\n    \"results\": {\n      \"qwen72b_concentration\": 0.48,\n      \"qwen72b_t1_t5\": 0.69,\n      \"qwen72b_l0_dominance_ratio\": 5.1,\n      \"qwen72b_total_heads\": 640,\n      \"qwen72b_diagnostic_prediction\": \"borderline (conc<0.50)\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Qwen Family Scaling\",\n        \"columns\": [\n          \"model\",\n          \"params\",\n          \"layers\",\n          \"kv_heads\",\n          \"concentration\",\n          \"t1_t5\",\n          \"predicted_shape\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen2.5-7B\",\n            \"7B\",\n            28,\n            112,\n            0.61,\n            0.57,\n            \"Spread\"\n          ],\n          [\n            \"Qwen2.5-14B\",\n            \"14B\",\n            48,\n            384,\n            0.55,\n            0.63,\n            \"Diluted Spread\"\n          ],\n          [\n            \"Qwen2.5-72B\",\n            \"72B\",\n            80,\n            640,\n            0.48,\n            0.69,\n            \"Borderline/Flat\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"如果 72B profiling 证实 concentration < 0.50，则 Spread pattern  不是 Qwen architecture 的固有属性而是 small-model artifact。 这对 diagnostic 的 practical value 是致命打击—— practitioner 最关心的 large models 恰恰最不可能是 Spread。\\n\\n\\n72B 有 80 layers × 8 KV heads = 640 heads。更多层进一步稀释 concentration。 Concentration=0.48（刚低于 0.50 阈值），t₁/t₅=0.69（刚低于 0.70）。 Diagnostic 预测 borderline/Flat——如果确实如此， 则 Qwen 模型族呈现 \\\"7B=Spread, 14B=Diluted Spread, 72B=Flat\\\" 的递减梯度， 说明 model size increase 系统性地 dilute sensitivity concentration。 这直接挑战 \\\"Qwen family is Spread\\\" 的 assumption。\\n\"\n  },\n  {\n    \"name\": \"K/V Separation\",\n    \"description\": \"将 K 和 V heads 作为独立 MCKP items，允许 asymmetric K/V budget。\\n\",\n    \"results\": {\n      \"kv_sep_ppl\": 11.22,\n      \"joint_kv_ppl\": 10.91,\n      \"uniform_4bit_ppl\": 15.45,\n      \"delta_sep_vs_joint\": 0.31,\n      \"sep_k_2bit_count\": 16,\n      \"sep_v_uniform_4bit\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"K/V Separation (Qwen2.5-7B)\",\n        \"columns\": [\n          \"method\",\n          \"ppl\",\n          \"k_2bit\",\n          \"v_2bit\",\n          \"vs_joint\"\n        ],\n        \"rows\": [\n          [\n            \"Joint K+V\",\n            10.91,\n            4,\n            4,\n            \"baseline\"\n          ],\n          [\n            \"K/V separated\",\n            11.22,\n            16,\n            0,\n            \"+2.8%\"\n          ],\n          [\n            \"Uniform 4-bit\",\n            15.45,\n            0,\n            0,\n            \"+41.6%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Negative result：K/V separation 不如 joint optimization。 论文用 1 paragraph 报告，作为 RateQuant comparison 的补充。\\n\\n\\nK/V separation 让 solver 独立优化 K 和 V 的 budget。 结果：V heads 全部 4-bit（sensitivity 低），K heads 有 16 个 2-bit（budget 被 V 让渡）。 但 PPL 11.22 略差于 joint optimization 的 10.91（Δ=0.31）， 因为 K-only 2-bit 的 compounding 比 joint 分配更 aggressive。 在 worst tier 下，这是 negative result——joint optimization 优于 separation， 说明 K/V interaction matters，简单的 asymmetric budget 不够。\\n\"\n  },\n  {\n    \"name\": \"L0-Only Heuristic Baseline\",\n    \"description\": \"最简单的 non-uniform 策略：L0 全部 8-bit，其余 uniform 4-bit。 如果匹配 MCKP，则 full optimization 不必要。\\n\",\n    \"results\": {\n      \"qwen_l0_random_mean\": 11.69,\n      \"qwen_l0_random_median\": 11.52,\n      \"qwen_l0_random_std\": 0.47,\n      \"qwen_naive_positional_ppl\": 12.23,\n      \"qwen_mckp_ppl\": 10.91,\n      \"llama_l0_random_mean\": 10.48,\n      \"llama_mckp_ppl\": 8.45,\n      \"mistral_l0_random_mean\": 7.56,\n      \"mistral_mckp_ppl\": 7.16\n    },\n    \"tables\": [\n      {\n        \"name\": \"L0 Heuristic vs MCKP\",\n        \"columns\": [\n          \"model\",\n          \"l0_random_median\",\n          \"mckp\",\n          \"uniform\",\n          \"mckp_vs_heuristic_gap\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen2.5-7B\",\n            11.52,\n            10.91,\n            15.45,\n            \"5.6%\"\n          ],\n          [\n            \"Llama-3.1-8B\",\n            10.04,\n            8.45,\n            8.47,\n            \"18.8%\"\n          ],\n          [\n            \"Mistral-7B\",\n            7.59,\n            7.16,\n            7.13,\n            \"6.0%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"MCKP outperforms heuristic on all models，但 gap varies。 在 non-Spread models，MCKP 和 heuristic 都 ≤ uniform—— the right choice is \\\"don't bother\\\" rather than \\\"optimize better\\\"。\\n\\n\\nL0-random heuristic（随机选 k 个 non-L0 heads 做 2-bit）在 Qwen 上 median=11.52 vs MCKP=10.91（gap 5.6%）。MCKP 的优势来自  precisely 选择 which non-L0 heads 做 2-bit（vs random）。 在 Llama/Mistral 上 L0-random 显著差于 MCKP（且 MCKP ≈ uniform）， 说明 heuristic 不是 universal substitute。 Worst tier 的 concern：14B 上 L0-random 可能 ≈ MCKP（因为 14B 的 MCKP 本身 ≈ uniform）， 进一步削弱 MCKP 的 value proposition。\\n\"\n  },\n  {\n    \"name\": \"RateQuant Greedy + Cardinality Constraint\",\n    \"description\": \"验证 constraint 是否是 key contribution（vs solver choice）。 Greedy + k=8 vs MCKP + k=8 vs both unconstrained。\\n\",\n    \"results\": {\n      \"greedy_unconstrained_ppl\": 32.45,\n      \"mckp_unconstrained_ppl\": 36.92,\n      \"greedy_constrained_k8_ppl\": 11.23,\n      \"mckp_constrained_k8_ppl\": 11.23,\n      \"delta_greedy_vs_mckp_constrained\": 0.0012,\n      \"solver_equivalence\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Solver Equivalence Under Constraint\",\n        \"columns\": [\n          \"method\",\n          \"unconstrained\",\n          \"constrained_k8\",\n          \"delta\"\n        ],\n        \"rows\": [\n          [\n            \"RateQuant Greedy\",\n            32.45,\n            11.23,\n            \"—\"\n          ],\n          [\n            \"MCKP\",\n            36.92,\n            11.23,\n            \"Δ=0.0012\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"在 reframed worst-tier narrative 中，solver equivalence under constraint  成为 Claim 1 的 core evidence。不需要 diagnostic 来 motivate。\\n\\n\\nCore finding：constraint 使 greedy = MCKP（Δ=0.0012 ≈ 0）。 Constrained feasible set 小到 greedy 的 local search 等于 global optimum。 这是 paper 最 robust 的 result——不依赖 diagnostic，不依赖 model choice， 纯数学属性。在 worst tier 下这是 anchor result。\\n\"\n  },\n  {\n    \"name\": \"Multi-Seed Error Bars (Qwen7B)\",\n    \"description\": \"3 个 calibration seed 的 constrained MCKP，报告 mean±std。\\n\",\n    \"results\": {\n      \"mckp_seed0\": 11.02,\n      \"mckp_seed1\": 10.9,\n      \"mckp_seed2\": 11.05,\n      \"mckp_mean\": 10.99,\n      \"mckp_std\": 0.065,\n      \"uniform_ppl\": 15.45,\n      \"allocation_agreement_3way\": 0.902,\n      \"bit_dist_all_seeds\": \"2:8, 4:100, 8:4\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Multi-Seed Results (Qwen2.5-7B)\",\n        \"columns\": [\n          \"seed\",\n          \"mckp_ppl\",\n          \"bit_dist\",\n          \"agreement_with_seed0\"\n        ],\n        \"rows\": [\n          [\n            \"seed_0\",\n            11.02,\n            \"8:100:4\",\n            \"—\"\n          ],\n          [\n            \"seed_1\",\n            10.9,\n            \"8:100:4\",\n            \"94.6%\"\n          ],\n          [\n            \"seed_2\",\n            11.05,\n            \"8:100:4\",\n            \"91.1%\"\n          ],\n          [\n            \"mean±std\",\n            \"10.99±0.065\",\n            \"—\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Qwen7B 的 statistical robustness 是 solid。但 N=3 seeds 仍然 limited。 论文应报告 \\\"our main result is robust to calibration variation\\\" 但  not claim \\\"statistical significance\\\" formally。\\n\\n\\n三个 seed 的 MCKP PPL std=0.065（mean=10.99），95% CI = [10.86, 11.12]。 与 uniform 的 gap（15.45 - 10.99 = 4.46）远大于 CI width（0.26）， Qwen7B 上的 improvement 是 statistically robust。 Bit distribution 三个 seed 完全一致（8:100:4），allocation agreement 90.2% （head-level 有 10% variation 但 bit-level distribution 不变）。 Worst tier 的 concern：14B 上 std 可能更大（sensitivity 更分散 → calibration noise 更大）， 且 improvement 本身在 noise 范围内。\\n\"\n  },\n  {\n    \"name\": \"Runtime/Latency Benchmark (Qwen7B)\",\n    \"description\": \"端到端 inference latency 和 throughput。\\n\",\n    \"results\": {\n      \"bf16_prefill_ms\": 45.86,\n      \"bf16_decode_ms\": 33.78,\n      \"uniform4_prefill_ms\": 54.25,\n      \"uniform4_decode_ms\": 42.46,\n      \"mckp_prefill_ms\": 57.03,\n      \"mckp_decode_ms\": 46.09,\n      \"mckp_throughput_tok_s\": 21.8,\n      \"uniform4_throughput_tok_s\": 23.6,\n      \"mckp_solver_sec\": 0.005,\n      \"mckp_overhead_vs_uniform_pct\": 8.5\n    },\n    \"tables\": [\n      {\n        \"name\": \"Runtime Benchmark (Qwen2.5-7B)\",\n        \"columns\": [\n          \"config\",\n          \"prefill_ms\",\n          \"decode_ms\",\n          \"throughput\",\n          \"memory_MB\"\n        ],\n        \"rows\": [\n          [\n            \"bf16\",\n            45.86,\n            33.78,\n            \"29.6 tok/s\",\n            21.0\n          ],\n          [\n            \"uniform 4-bit\",\n            54.25,\n            42.46,\n            \"23.6 tok/s\",\n            5.25\n          ],\n          [\n            \"MCKP constrained\",\n            57.03,\n            46.09,\n            \"21.8 tok/s\",\n            5.25\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"8.5% latency overhead 是 acceptable trade-off 但仅在 Spread models 上。 Reframe: \\\"if diagnostic uncertain, use uniform 4-bit to avoid latency cost\\\"  — 这与 worst-tier narrative 的 \\\"conservative recommendation\\\" 一致。\\n\\n\\nMixed-precision MCKP 比 uniform 4-bit 慢 ~8.5%（decode 46.09 vs 42.46 ms/tok）， 因为 mixed bit-width 需要 per-head dequantize dispatch（vs uniform 的 vectorized batch dequant）。 内存相同（5.25 MB），solver 本身 negligible（5ms）。 Worst tier 的 concern：8.5% latency overhead 换 PPL improvement 仅在 Qwen7B 上 worth it—— 在 non-Spread 模型上 overhead 仍存在但 PPL 无 improvement， 纯亏损。Reviewer 会问 \\\"when is the latency cost justified?\\\"\\n\"\n  },\n  {\n    \"name\": \"W9 Compounding Scaling (Worst Tier)\",\n    \"description\": \"Qwen7B 上 top-k vs random-k 2-bit assignment sweep，刻画 super-additivity。\\n\",\n    \"results\": {\n      \"k1_topk_ppl\": 9.83,\n      \"k1_randomk_ppl\": 9.89,\n      \"k4_topk_ppl\": 9.85,\n      \"k4_randomk_ppl\": 10.06,\n      \"k8_topk_ppl\": 10.04,\n      \"k8_randomk_ppl\": 11.07,\n      \"k16_topk_ppl\": 10.42,\n      \"k16_randomk_ppl\": 12.91,\n      \"k32_topk_ppl\": 11.6,\n      \"k32_randomk_ppl\": 18.33,\n      \"k64_topk_ppl\": 22.95,\n      \"k64_randomk_ppl\": 55.94,\n      \"k64_randomk_topk_ratio\": 1.45,\n      \"k32_randomk_topk_ratio\": 1.58,\n      \"k16_randomk_topk_ratio\": 1.24,\n      \"non_monotonic_flag\": true,\n      \"variance_at_k16_masks_trend\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"W9 Compounding (Worst-Tier Interpretation)\",\n        \"columns\": [\n          \"k\",\n          \"topk_ppl\",\n          \"randomk_ppl\",\n          \"randomk_std\",\n          \"ratio\",\n          \"monotonic\"\n        ],\n        \"rows\": [\n          [\n            1,\n            9.83,\n            9.89,\n            0.05,\n            1.0,\n            \"—\"\n          ],\n          [\n            4,\n            9.85,\n            10.06,\n            0.06,\n            1.24,\n            \"↑\"\n          ],\n          [\n            8,\n            10.04,\n            11.07,\n            0.69,\n            1.76,\n            \"↑\"\n          ],\n          [\n            16,\n            10.42,\n            12.91,\n            0.4,\n            1.24,\n            \"↓ ⚠️\"\n          ],\n          [\n            32,\n            11.6,\n            18.33,\n            2.53,\n            1.58,\n            \"↑\"\n          ],\n          [\n            64,\n            22.95,\n            55.94,\n            9.73,\n            1.45,\n            \"↓ ⚠️\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"在 worst tier 下，W9 data 的 non-monotonicity 和 high variance  使得 formal super-additivity claim 不成立。 Reframe: 报告为 \\\"empirical observation of compounding trend with substantial variance\\\"， 不 formalize 为 theorem 或 proposition。 Compounding 的 qualitative story 仍 hold（ratio >1 at all k>1）， 但 quantitative precision 不足以支撑 formal contribution。\\n\\n\\nWorst-tier 下 k=64 的 randomk/topk ratio 降至 1.45（vs 实际 2.44 的 actual data 中位估计）。 k=8-16 区间出现 non-monotonic：k=8 ratio=1.76 但 k=16 ratio 回落到 1.24， 然后 k=32 又升到 1.58。这种 non-monotonicity 可能来自： (1) random-k 的 seed variance（std=0.4-2.5 across seeds）， (2) top-k 在某些 k 值恰好避开 interaction cluster 而 random 没有。 Non-monotonic behavior 使得 \\\"super-additivity monotonically increases with k\\\"  的 clean story 不成立。论文需要 acknowledge variance 并报告 CI。 ratio 的 overall trend 仍是 increasing（1.24→1.45→1.58→1.45）， 但 non-monotonicity at intermediate k 削弱 formalization strength。\\n\"\n  },\n  {\n    \"name\": \"Qwen2.5-14B Downstream Eval (Predicted)\",\n    \"description\": \"如果 14B profiling + MCKP 完成，需跑 downstream eval 验证 PPL 与 downstream 一致性。\\n\",\n    \"results\": {\n      \"qwen14b_baseline_avg\": 0.72,\n      \"qwen14b_uniform_avg\": 0.71,\n      \"qwen14b_mckp_avg\": 0.71,\n      \"qwen14b_mckp_vs_uniform_pp\": 0.1,\n      \"qwen14b_arc_challenge_delta_pp\": -0.5,\n      \"qwen14b_hellaswag_delta_pp\": 0.3\n    },\n    \"tables\": [\n      {\n        \"name\": \"Qwen14B Downstream (Predicted)\",\n        \"columns\": [\n          \"task\",\n          \"uniform\",\n          \"mckp\",\n          \"delta_pp\"\n        ],\n        \"rows\": [\n          [\n            \"arc_challenge\",\n            0.58,\n            0.575,\n            \"-0.5\"\n          ],\n          [\n            \"hellaswag\",\n            0.72,\n            0.723,\n            \"+0.3\"\n          ],\n          [\n            \"piqa\",\n            0.81,\n            0.811,\n            \"+0.1\"\n          ],\n          [\n            \"winogrande\",\n            0.73,\n            0.728,\n            \"-0.2\"\n          ],\n          [\n            \"average\",\n            0.71,\n            0.71,\n            \"+0.1\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Downstream 确认 14B false positive——不仅 PPL 无 improvement， downstream 也在 noise。论文需要 transparent reporting。\\n\\nPPL improvement +1.2% → downstream ≈ 0pp（noise）。 arc_challenge 可能略负（-0.5pp），与跨模型的 arc_challenge 系统性敏感一致。 hellaswag 略正（+0.3pp）但在 seed noise 范围内。 整体结论：14B downstream 与 PPL 一致——MCKP 无 meaningful benefit。\\n\"\n  }\n]",
      "numLines": 1313,
      "startLine": 1,
      "totalLines": 1313
    }
  },
  "sourceToolAssistantUUID": "4b31af4c-7a94-48d3-b0b2-b2eaaa336867",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T085855 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/…",
  "leafUuid": "5462c821-0f6b-4b98-9268-9911ff1d8362",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier simulated paper for dream_20260515T085855",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8"
}
```

---

### Tool result

_source line 13 · 2026-05-15T09:54:32.491Z_

<details><summary>↩ Tool result · `toolu_01AnvGvhzwTCHdooGEQt252p`</summary>

```text
1	# Paper Framing — ratekv
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (ARR submission)
5	- Deadline: ARR May 25, 2026 (11 days from today 2026-05-14)
6	- Track: Efficient Methods for NLP
7	
8	## bf16 Consistency Resolution (2026-05-14)
9	
10	**已解决**：qwen_bf16_reeval 确认 bf16 ≈ fp16（baseline delta=0.0006, uniform delta=0.005）。compounding_sweep bf16 rerun 不需要。
11	
12	**eval pipeline 一致性**：exp_e 使用了不同的 eval 参数（baseline=8.82, MCKP=9.57），与主 pipeline（baseline=9.81）不一致。hires_mckp_reeval 用统一 pipeline 重测：MCKP hires bf16=10.9131。**论文使用统一 pipeline 数字**。
13	
14	| 指标 | 统一 pipeline (bf16) | exp_e pipeline (bf16) | fp16 (旧) |
15	|------|---------------------|----------------------|-----------|
16	| Baseline | **9.8106** | 8.819 | 9.81 |
17	| Uniform 4-bit | **15.4454** | — | 15.45 |
18	| MCKP hires (max_2bit=8) | **10.9131** | 9.569 | — |
19	| MCKP lowres (max_2bit=8) | ~11.23 | 11.345 | 11.23 |
20	
21	## Core Insight
22	
23	Per-head KV cache quantization sensitivity varies dramatically across architectures, and the effectiveness of non-uniform mixed-precision allocation is fundamentally determined by the degree of this heterogeneity. We provide both the analysis framework — characterizing when non-uniform quantization helps via per-head sensitivity concentration metrics — and a surprisingly simple method fix: a cardinality constraint (≤k heads at 2-bit) that prevents compounding effects from profiler non-additivity and reduces the search space sufficiently that solver choice becomes irrelevant (greedy and MCKP produce identical allocations).
24	
25	## Core Claims (3 条)
26	
27	1. **Head sensitivity heterogeneity is architecture-dependent and determined by sensitivity *distribution shape*, not GQA ratio or concentration alone**: Per-KV-head quantization sensitivity is extremely non-uniform within models, but whether MCKP can exploit this heterogeneity depends on the *shape* of the sensitivity distribution, not just its magnitude. Critical counterexample: Yi-1.5-9B (GQA 8:1, concentration 0.71 — the *highest* in our lineup) provides *no benefit* from MCKP (7.22 vs 7.22 uniform), while Qwen2.5-7B (GQA 7:1, concentration 0.61) succeeds (+27.3%). The difference is distribution shape: Qwen has a *cluster* of sensitive heads (Layer 0, 4 heads with cross-bitwidth gradients — "spread" pattern, t₁/t₅=0.57), while Yi-1.5 has a single extreme outlier (L4H3, delta=13.12, t₁/t₅=0.90 — "spike" pattern) with sensitivity at only one bitwidth. A joint diagnostic — concentration ≳0.50 AND t₁/t₅ ≲0.70 — correctly separates the beneficial case (Qwen) from all four non-beneficial cases across five architectures. Three shape categories emerge:
28	   - **Spread** (Qwen): high concentration + low t₁/t₅ → multiple heads with cross-bitwidth gradients → MCKP effective
29	   - **Spike** (Yi-1.5, Llama): high t₁/t₅ → single outlier dominates → MCKP ineffective
30	   - **Flat** (Mistral, Gemma-2): low concentration → near-uniform sensitivity → MCKP ineffective (t₁/t₅ irrelevant when concentration < 0.50)
31	
32	2. **Cardinality constraint is the primary intervention; unconstrained catastrophe is Spread-specific**: On non-consecutive discrete bit-widths {2,4,8,16}, unconstrained allocation produces **catastrophic** results on Spread-heterogeneity architectures (Qwen: greedy 32.45, MCKP 36.92 vs uniform 15.45 = 3.31× baseline) because per-head independent profiling distortions compound non-additively when many heads are simultaneously assigned extreme quantization. On non-Spread architectures, unconstrained allocation causes **mild-to-moderate degradation** (Yi 1.08×, Llama 1.07×, Mistral 1.08×, Gemma-2 1.47×) but still underperforms uniform 4-bit in all cases — the solver over-allocates 2-bit heads even when individual distortions appear small. A cardinality constraint (max_2bit≤k) is a simple and sufficient condition: it prevents compounding on Spread models, avoids 2-bit over-allocation on non-Spread models, AND reduces the feasible set to where solver choice is irrelevant — constrained greedy and constrained MCKP produce identical bit allocations and PPL (Δ=0.0000, both 11.2312). **Practical implication**: the concentration diagnostic determines whether to invest in MCKP + constraint (Spread models) or simply use uniform 4-bit (non-Spread models — saves solver computation with no quality loss). The profiling benefit beyond the constraint (hires vs lowres) is architecture-dependent: substantial on Spread models (Qwen), marginal on others. The optimal k is determinable via small-scale compounding effect test (plan_004).
33	
34	**Claim 2 three-pillar support** (Reviewer Q4, new narrative STRENGTHENS Claim 2):
35	1. Spread models: constraint prevents catastrophe (Qwen 32.45→11.23)
36	2. Flat models: constraint prevents moderate over-allocation (Gemma-2 8.85→~6.17, 106→8 heads at 2-bit)
37	3. All models: constraint makes solver choice irrelevant (greedy=MCKP, Δ=0.0000)
38	This answers "when" and "why", not just "what" — stronger than original "universal catastrophe" narrative.
39	
40	3. **A joint empirical decision rule correctly separates beneficial from non-beneficial architectures**: Constrained allocation achieves 27.3% PPL improvement on Qwen (spread pattern: concentration 0.61, t₁/t₅=0.57), while providing no benefit on Yi-1.5 (spike: 0.71, t₁/t₅=0.90, ≈0%), Llama (spike: 0.34, t₁/t₅=0.71, +0.2%), Mistral (flat: 0.22, t₁/t₅=0.18, -0.4%), and Gemma-2 (flat: 0.23, t₁/t₅=0.38, -0.3%). The joint condition — concentration ≳0.50 AND t₁/t₅ ≲0.70 — correctly separates the beneficial case from all four non-beneficial cases across five architectures (5/5 accuracy). Concentration alone fails: Yi-1.5 (0.71) exceeds Qwen (0.61) yet gains nothing, because its spike pattern (single outlier, no cross-bitwidth gradient) cannot be exploited. Under aggressive compression (≥5×), constrained allocation prevents catastrophic collapse even on non-beneficial architectures (Llama 5.3×: constrained PPL 57.60 vs uniform 2-bit 2644). This provides practitioners an empirical decision rule for when to invest in mixed-precision KV cache quantization. **Claim strength note (Reviewer-verified)**: N=1 Spread → position as "empirical decision rule", NOT "diagnostic framework". If Qwen2.5-14B also confirms Spread → upgrade to "empirical diagnostic" (N=2).
41	
42	## Story Spine
43	
44	- **Problem**: KV cache quantization typically applies uniform bit-width across all heads. Per-head mixed-precision allocation promises better quality-compression tradeoffs, but two fundamental questions remain unanswered: (1) *when* does non-uniform allocation actually help — i.e., under what architectural and compression conditions does the added complexity pay off? (2) *how* to make existing allocation algorithms (greedy, MCKP) work correctly on hardware-aligned discrete bit-widths {2,4,8,16} where they currently fail catastrophically?
45	
46	- **Existing approaches & gaps**: RateQuant (May 2026) provides R-D optimal per-head allocation via continuous closed-form (Theorem 2) and discrete greedy (Algorithm 1, optimal on consecutive integers {2,...,6} per Proposition 6). However, on hardware-aligned non-consecutive sets {2,4,8,16}, RateQuant's greedy produces PPL 32.45 (vs optimal ~11.23) — the polymatroid structure that guarantees greedy optimality breaks. Moreover, unconstrained MCKP fares even worse (PPL 36.92) due to compounding effects from profiler non-additivity. Critically, neither RateQuant nor ARKV addresses *when* non-uniform allocation is beneficial.
47	
48	- **Our framing**: We present a systematic study of per-head KV cache quantization sensitivity across architectures and identify a surprisingly simple fix for the failure of existing algorithms on hardware-aligned bit-widths: a cardinality constraint limiting the number of heads assigned to extreme quantization levels. This single intervention (a) prevents compounding effects, (b) reduces the search space to where solver choice is irrelevant — greedy and MCKP produce identical optimal allocations, and (c) can be parameterized via a small-scale compounding test. Beyond the method, we establish that the benefit of non-uniform allocation is architecture-dependent and quantifiable via an empirical decision rule (concentration + distribution shape), providing practitioners a two-metric check for when mixed-precision is worthwhile.
49	
50	- **Headline result template**: "We show that the benefit of non-uniform per-head KV cache quantization is concentration-dependent: on spread-heterogeneity architectures (Qwen, concentration 0.61), unconstrained solvers fail catastrophically (PPL 32-37 vs uniform 15.45), while a cardinality constraint (≤k heads at 2-bit) achieves 27.3% PPL improvement with identical results from greedy and MCKP (Δ=0.0000). On non-spread architectures (4 models, 1.07-1.47× baseline), unconstrained solvers cause only mild degradation, and constrained MCKP offers no benefit over uniform 4-bit at either PPL or downstream task level (<1pp avg). An empirical decision rule (concentration ≳0.50 AND t₁/t₅ ≲0.70) correctly separates the beneficial case from all four non-beneficial cases (5/5 accuracy) at both PPL and downstream task level, providing practitioners a two-metric check to determine whether mixed-precision KV cache quantization is worthwhile — or whether uniform quantization suffices."
51	
52	## "When Does Non-Uniform Allocation Help?" — Analysis Chapter
53	
54	Five case studies representing the full spectrum of heterogeneity:
55	
56	| Case | Model | GQA | Top-5% Conc. | Constrained vs Uniform (4×) | Role in Paper |
57	|------|-------|-----|--------------|------------------------------|---------------|
58	| **Strong positive** | Qwen2.5-7B | 7:1 | 0.59-0.66 | **+27.3% (11.23 vs 15.45)** | Primary showcase; "spread" pattern (L0 cluster, 4 heads, 26× dominance) |
59	| **GQA counterexample** | Yi-1.5-9B | 8:1 | 0.71 (hires) | ≈0% (7.22 vs 7.22) | Highest GQA but no benefit; "spike" pattern (L4H3 single outlier, 34% of total delta) |
60	| **Marginal** | Llama-3.1-8B | 4:1 | 0.34-0.59 | +0.2% (8.45 vs 8.47) | Boundary condition; constraint never binds (natural k=2) |
61	| **Negative** | Mistral-7B-v0.3 | 4:1 | 0.22 (hires) | -0.4% (7.16 vs 7.13) | Profiler zero-signal; monotonic k-PPL curve |
62	| **Strongest negative** | Gemma-2-9B | 2:1 | 0.23 (hires) | -0.3% (9.05 vs 9.03) | Low-end anchor; most uniform sensitivity (CV=1.28, t₁/t₅=0.38) |
63	
64	**Spike vs Spread insight**: Yi-1.5 vs Qwen illustrates why GQA ratio alone is insufficient. Both have high GQA (8:1 vs 7:1), but Qwen's L0 *cluster* of sensitive heads creates optimization opportunities for MCKP, while Yi-1.5's single extreme outlier (L4H3) cannot be exploited — the solver assigns 8-bit to that one head but has no other heads to differentiate. Distribution shape matters more than the existence of outliers.
65	
66	**Compression amplifies benefit**: Even on low-heterogeneity Llama, aggressive 5.3× compression yields constrained PPL=57.60 vs uniform 2-bit=2643.77 (45× better).
67	
68	**Joint diagnostic** (n=5, 5/5 correct): concentration ≳0.50 AND t₁/t₅ ≲0.70 → non-uniform allocation recommended (spread pattern). Either condition violated → uniform suffices at moderate compression; non-uniform still valuable at aggressive compression. Yi-1.5 (concentration 0.71 but t₁/t₅=0.90 — spike) and Qwen (0.61, t₁/t₅=0.57 — spread) illustrate why concentration alone is insufficient.
69	
70	## Solver Equivalence Evidence (plan_016, CONFIRMED ✅)
71	
72	| Method | PPL | Bit Distribution | Budget |
73	|--------|-----|-------------------|--------|
74	| Greedy unconstrained | 32.45 | {2:68, 4:30, 8:4, 16:10} | 0.25 |
75	| MCKP unconstrained | 36.92 | — | 0.25 |
76	| **Greedy + max_2bit=8** | **11.2312** | **{8:4, 4:100, 2:8}** | **0.25** |
77	| **MCKP + max_2bit=8** | **11.2312** | **{8:4, 4:100, 2:8}** | **0.25** |
78	| Uniform 4-bit | 15.4454 | all 4-bit | 0.25 |
79	
80	Key takeaway: The constraint is the primary intervention — without it, both solvers fail; with it, solver choice is irrelevant (Δ=0.0000). This powerfully demonstrates the constraint is THE contribution.
81	
82	## Cross-Architecture Evidence Summary
83	
84	| Model | GQA | KV Heads | Top-5% Conc. | Unconstrained ×baseline (W2 v2) | Constrained vs Uniform (4×) | Distribution Shape | Conclusion |
85	|-------|-----|----------|--------------|--------------------------------|------------------------------|-------------------|------------|
86	| Qwen2.5-7B | 7:1 | 112 | **0.61** | **3.31× (32.45)** ☠️ | **+27.3% (11.23 vs 15.45)** | Spread (L0 cluster, 4 heads) | ✅ Strong benefit |
87	| Yi-1.5-9B | 8:1 | 192 | **0.71** (hires) | 1.08× (7.56) | **≈0% (7.22 vs 7.22)** | Spike (L4H3 single outlier) | ❌ GQA counterexample |
88	| Llama-3.1-8B | 4:1 | 256 | 0.57 (hires) | 1.07× (8.63) | **+0.2% (8.45 vs 8.47)** | Spike (borderline t₁/t₅=0.71) | ≈ Marginal |
89	| Mistral-7B-v0.3 | 4:1 | 256 | **0.22** (hires) | 1.08× (7.57) | **-0.4% (7.16 vs 7.13)** | Flat (profiler zero-signal) | ❌ Negative |
90	| Gemma-2-9B | 2:1 | 336 | **0.23** (hires) | 1.47× (8.85) | **-0.3% (9.05 vs 9.03)** | Flat (CV=1.28, t₁/t₅=0.38) | ❌ Strongest negative |
91	
92	**Unconstrained pattern** (W2 v2, all WikiText-2 test eval, gradient narrative): Unconstrained degradation follows a **concentration-dependent gradient**, not a binary catastrophe/benign split:
93	- **Spread** (Qwen, conc=0.61): **3.31×** catastrophic — L0 cluster creates massive compounding
94	- **Flat-high-2bit** (Gemma-2, conc=0.23): **1.47×** moderate — solver assigns 106/336=31.5% heads to 2-bit because distortions are indistinguishable (CV=1.28), cumulative effect significant despite small per-head delta
95	- **Spike/Flat-low-2bit** (Yi 1.08×, Llama 1.07×, Mistral 1.08×): mild — solver selects few 2-bit heads (Yi 11.5%, Llama 4.7%, Mistral 16.4%)
96	- In ALL cases unconstrained ≤ uniform 4-bit — solver consistently over-allocates 2-bit heads
97	
98	**Gemma-2 1.47× must be discussed in paper** (Reviewer mandate, severity: warning):
99	
100	Three-tier labeling (NOT binary catastrophe/benign):
101	- **Catastrophic** (3.31×): Spread model (Qwen) — L0 cluster compounding
102	- **Moderate** (1.47×): Flat-high-2bit (Gemma-2) — solver over-allocation from indistinguishable distortions
103	- **Mild** (1.07-1.08×): Spike/Flat-low-2bit (Yi, Llama, Mistral)
104	
105	Reviewer-suggested paragraph for paper (1 段, 3-4 句):
106	"Gemma-2-9B exhibits a moderate 1.47× degradation under unconstrained allocation, higher than the 1.07–1.08× observed in other non-Spread models. This stems from its flat sensitivity distribution (concentration 0.23, CV 1.28): the solver cannot meaningfully differentiate heads, leading to 31.5% of heads assigned to 2-bit (vs 4.7–16.4% in other models). While not catastrophic, this over-allocation still motivates the cardinality constraint even on flat-distribution architectures. The constraint reduces 2-bit heads from 106 to 8, yielding PPL within 0.3% of uniform — confirming that the constraint universally prevents solver over-allocation regardless of distribution shape."
107	
108	This **strengthens** the paper: (1) honesty → credibility, (2) constraint has universal value (not just Spread), (3) explains solver degradation mechanism under low signal → added insight depth.
109	
110	⚠️ **Data file note**: `artifacts/w2_unconstrained_v2_results.json` still has old Gemma-2 BOS bug data (baseline=711.6). Fix in `artifacts/w2_gemma2_bos_fix_results.json`. Agent tasked to merge.
111	
112	**Key pattern**: Constrained allocation benefit depends on the joint condition (concentration ≳0.50 AND t₁/t₅ ≲0.70, 5/5 correct), NOT GQA ratio or concentration alone. Yi-1.5 (GQA 8:1, concentration 0.71 — highest — yet no benefit) vs Qwen (GQA 7:1, concentration 0.61, +27.3%) demonstrates that neither GQA nor concentration alone is a reliable proxy. The critical factor is sensitivity *distribution shape*: spread (multiple heads with cross-bitwidth gradients) enables MCKP, while spike (single outlier) or flat (uniform sensitivity) does not.
113	
114	**Aggressive compression** (Llama): At 5.3× compression, constrained PPL=57.60 vs uniform 2-bit=2643.77 — prevents catastrophic collapse even on low-heterogeneity architectures.
115	
116	### Mistral k Ablation (256 KV heads, budget=0.25)
117	
118	PPL monotonically increases with k — every additional 2-bit head hurts. Even best k=4 (PPL 7.1648) is worse than uniform (7.131).
119	
120	| k | PPL | 2-bit | 4-bit | 8-bit | 16-bit | mem |
121	|---|-----|-------|-------|-------|--------|-----|
122	| 4 | **7.1648** | 4 | 252 | 0 | 0 | 0.248 |
123	| 8 | 7.1997 | 8 | 247 | 0 | 1 | 0.249 |
124	| 12 | 7.2448 | 12 | 242 | 0 | 2 | 0.250 |
125	| 16 | 7.3106 | 16 | 238 | 0 | 2 | 0.248 |
126	| 18 | 7.3231 | 18 | 235 | 0 | 3 | 0.250 |
127	| uniform 4-bit | 7.131 | 0 | 256 | 0 | 0 | 0.250 |
128	
129	Contrast with Qwen (U-shaped, optimal k=8) and Llama (flat, natural k=2). Mistral's monotonic pattern confirms profiler zero-signal: no head benefits from 2-bit downgrade.
130	
131	### Llama k Ablation (256 KV heads, budget=0.25)
132	
133	All k values produce identical PPL=8.4498. MCKP naturally selects only 2 heads for 2-bit — constraint never binds. Marginal +0.2% over uniform (8.4498 vs 8.469).
134	
135	### Downstream Eval — Cross-Architecture (W3, 0-shot, 5 tasks)
136	
137	**Qwen2.5-7B (Spread) — MCKP benefits translate to downstream** ✅
138	
139	| Task | Uniform 4-bit | MCKP hires | Δ | BF16 Baseline |
140	|------|---------------|------------|---|---------------|
141	| ARC-C | 0.4812 | 0.5137 | **+3.16pp** | 0.5290 |
142	| HellaSwag | 0.7284 | 0.7684 | **+4.00pp** | 0.7833 |
143	| PIQA | 0.7661 | 0.7786 | **+1.25pp** | 0.7932 |
144	| WinoGrande | 0.6622 | 0.6819 | **+1.97pp** | 0.6898 |
145	| **Avg recovery** | — | — | **72.8%** | — |
146	
147	**Yi-1.5-9B (Spike) — No MCKP benefit, consistent with PPL** (W3)
148	
149	| Task | Uniform 4-bit | MCKP (k=8) | Δ |
150	|------|---------------|------------|---|
151	| arc_easy | 0.7946 | 0.7854 | -0.92pp |
152	| arc_challenge | 0.5205 | 0.4881 | **-3.24pp** |
153	| hellaswag | 0.5857 | 0.5797 | -0.60pp |
154	| piqa | 0.7927 | 0.7894 | -0.33pp |
155	| winogrande | 0.7174 | 0.7301 | +1.27pp |
156	| **Average** | **0.6822** | **0.6745** | **-0.77pp** |
157	
158	**Llama-3.1-8B (Spike) — No MCKP benefit, consistent with PPL** (W3)
159	
160	| Task | Uniform 4-bit | MCKP (k=8) | Δ |
161	|------|---------------|------------|---|
162	| arc_easy | 0.8173 | 0.8039 | -1.34pp |
163	| arc_challenge | 0.5256 | 0.4991 | **-2.65pp** |
164	| hellaswag | 0.6026 | 0.6012 | -0.14pp |
165	| piqa | 0.7867 | 0.7802 | -0.65pp |
166	| winogrande | 0.7253 | 0.7238 | -0.15pp |
167	| **Average** | **0.6915** | **0.6816** | **-0.99pp** |
168	
169	**Mistral-7B-v0.3 (Flat) — No MCKP benefit, consistent with PPL** (W3)
170	
171	| Task | Uniform 4-bit | MCKP (k=4) | Δ |
172	|------|---------------|------------|---|
173	| arc_easy | — | — | — |
174	| arc_challenge | — | — | — |
175	| hellaswag | — | — | — |
176	| piqa | — | — | — |
177	| winogrande | — | — | — |
178	| **Average** | **0.6894** | **0.6846** | **-0.48pp** |
179	
180	**Gemma-2-9B (Flat) — Negligible MCKP effect, noise range** (W3)
181	
182	| Task | Uniform 4-bit | MCKP | Δ |
183	|------|---------------|------|---|
184	| **Average** | **0.7251** | **0.7265** | **+0.14pp** (noise) |
185	
186	**Downstream summary (Reviewer-verified framing)**:
187	- Diagnostic correctly predicts both PPL and downstream outcomes across **all 5 tested models**
188	- Spread (Qwen): consistent downstream gains (+1.25 to +4.00pp)
189	- Non-Spread (4 models): MCKP shows **minor systematic degradation** vs uniform (Yi -0.77pp, Llama -0.99pp, Mistral -0.48pp, Gemma-2 +0.14pp noise)
190	- **Llama signal**: 0/5 tasks where MCKP ≥ uniform — degradation is systematic, not task-specific noise
191	- arc_challenge shows largest per-task effect (Yi -3.24pp, Llama -2.65pp)
192	- **Paper must**: (a) report full per-task tables, not just averages, (b) use "shows minor degradation" NOT "preserves accuracy" — the latter has spin, (c) note arc_challenge as worst-case explicitly
193	- **Limitation**: no multi-seed CI for downstream — 0-shot arc_challenge -3.24pp could be questioned for significance
194	- **arc_challenge 系统性信号** (Reviewer 观察): arc_challenge 退化跨模型一致（Yi -3.24pp, Llama -2.65pp, Mistral -1.19pp, Gemma-2 -0.17pp），不是随机噪声。论文应主动讨论："ARC-Challenge shows the largest per-task sensitivity to allocation strategy, consistent with its reliance on multi-step reasoning where subtle KV cache errors accumulate."
195	- **呈现方式**: 主表放完整 per-task 数据，文字用均值+range 概括。建议措辞："Across four non-Spread architectures, constrained MCKP shows minor average degradation vs uniform 4-bit (Yi -0.77pp, Llama -0.99pp, Mistral -0.48pp, Gemma-2 +0.14pp). Per-task variation ranges from +1.27pp (Yi, WinoGrande) to -3.24pp (Yi, ARC-Challenge)."
196	
197	## Allocation Baseline Evidence (plan_015, mckp_reeval)
198	
199	All numbers from unified bf16 eval pipeline, budget=0.25.
200	
201	| Model | Baseline | Uniform 4-bit | MCKP | L0-random (mean±std) | L0-random (median) | Naive Positional | MCKP improvement |
202	|-------|----------|---------------|------|----------------------|---------------------|------------------|------------------|
203	| Qwen2.5-7B (k=8) | 9.8106 | 15.4454 | 10.9131 | 11.691±0.422 | **11.515** | 12.230 | 27.3% vs uniform (standard); 29.4% (hires, §5.4) |
204	| Llama-3.1-8B (k=2) | 8.0918 | 8.469 | 8.4498 | 10.479±1.033 | **10.038** | 9.941 | +0.2% vs uniform |
205	| Mistral-7B-v0.3 (k=4) | 7.035 | 7.131 | 7.1648 | 7.560±0.087 | **7.586** | 7.481 | -0.4% vs uniform |
206	
207	**Outlier note**: seed_4 inflates mean on Qwen (12.51) and Llama (12.44). Median is more robust: Qwen median 11.515 vs mean 11.691 (−0.176); Llama median 10.038 vs mean 10.479 (−0.441). Mistral has no outlier (median ≈ mean). Paper should report both mean±std and median.
208	
209	**MCKP vs L0-random (median)**: Qwen 10.91 vs 11.52 (−5.2%); Llama 8.45 vs 10.04 (−15.8%); Mistral 7.16 vs 7.59 (−5.7%). MCKP consistently outperforms random L0-constrained allocation across all architectures.
210	
211	## Differentiation from RateQuant
212	
213	| Aspect | RateQuant | Ours |
214	|--------|-----------|------|
215	| Bit-width selection | Greedy on consecutive integers {2,...,6} (Prop. 6 optimal) + continuous closed-form (Thm. 2) | Cardinality-constrained allocation on hardware-aligned {2,4,8,16}-bit |
216	| Distortion model | Additive, parametric D(b)=α·β^{-b} | Additive + cardinality regularization for non-additivity |
217	| Compounding effects | Acknowledged (Appendix M) but unaddressed | **Core contribution**: cardinality constraint prevents compounding; first quantitative evidence |
218	| Action space | Consecutive integers (polymatroid → greedy optimal) | Non-consecutive hardware-aligned (polymatroid breaks → constraint needed, solver doesn't matter) |
219	| Solver requirement | Greedy (provably optimal in their setting) | **Any solver** — constrained greedy = constrained MCKP (Δ=0.0000 PPL) |
220	| K/V allocation | Asymmetric K/V budget (e.g. K=2.85, V=2.15) | MCKP/greedy treats K/V heads as independent items (natural extension) |
221	| **Applicability analysis** | **Not addressed — assumes non-uniform always helps** | **Systematic study of when non-uniform allocation is beneficial (new contribution)** |
222	
223	## Venue Fit Risks
224	
225	- **"The constraint is just a heuristic, not a real contribution"**: Strongest reviewer attack under new framing. Defense: (a) principled motivation from compounding effect non-additivity with first quantitative evidence, (b) constraint parameterization via systematic compounding test, (c) the finding that constraint alone makes solver choice irrelevant is a surprising and practically useful result — practitioners need only add one parameter to existing pipelines.
226	- **Incrementality over RateQuant**: Defense: (a) RateQuant's greedy is suboptimal unconstrained on {2,4,8,16} (PPL 32.45), (b) our constraint fixes RateQuant's greedy to match MCKP — we're improving their method, not replacing it, (c) applicability analysis is entirely new.
227	- **Method only strong on one architecture (Qwen)**: 5 models tested, only Qwen shows clear benefit. Mitigate: (a) analysis contribution framing — characterizing boundary conditions is more useful than universal positive, (b) honest negative/marginal results (Yi-1.5, Gemma-2, Mistral, Llama) strengthen credibility, (c) unlike prior work that assumes non-uniform always helps, we provide the first systematic study of *when it fails*, (d) Yi-1.5 (GQA 8:1, FAIL) is particularly powerful — it disproves the naive "higher GQA = more benefit" hypothesis and shows our diagnostic is needed.
228	- **GQA ratio is not a reliable proxy**: Yi-1.5 (GQA 8:1) directly contradicts a GQA-based prediction. Do NOT present GQA ratio as a predictor — present it as one contributing factor. The reliable predictor is Top-5% concentration (0.50 threshold, 5/5 correct). The "spike vs spread" analysis explains WHY same-GQA models differ.
229	- **Statistical power**: n=5 models is directional evidence, not statistical claim. Do NOT claim "significant correlation" — use "consistent pattern across 5 architectures" or "5/5 correctly classified by the 0.50 threshold."
230	- **No eviction arm**: Mention as negative finding; framework extends naturally to eviction.
231	
232	## Anticipated Reviewer Concerns
233	
234	1. **"The cardinality constraint is trivial — just cap the extreme allocations"** → (a) Trivial in retrospect, but without it both greedy (PPL 32.45) and MCKP (PPL 36.92) fail catastrophically — the failure mode is non-obvious, (b) principled motivation from compounding effect characterization (plan_004), (c) optimal k selection via systematic small-scale test, (d) the finding that this single intervention eliminates solver complexity is surprising and practically valuable.
235	2. **"This is just RateQuant with a constraint added"** → (a) We agree — and that's the point: RateQuant's greedy + our constraint achieves identical results to MCKP + constraint, (b) the constraint addresses a real gap: compounding effects on {2,4,8,16} that RateQuant acknowledges but doesn't solve, (c) applicability analysis is new.
236	3. **"The method only works on Qwen — isn't this a Qwen paper?"** → We systematically test 4-5 architectures spanning GQA 2:1 to 8:1 and honestly report negative results (Gemma-2, Mistral). The analysis contribution — characterizing *boundary conditions* of non-uniform quantization — generalizes beyond any single model and is more useful than a universally positive but misleading claim.
237	4. **"How does this work at different compression ratios?"** → Budget sweep across 2×, 4×, 8× (plan_005). Aggressive compression on Llama shows benefit amplifies even on low-heterogeneity models.
238	5. **"n=3/4/5 models is not enough for the heterogeneity claim"** → Acknowledged as limitation. We present directional evidence across 4-5 architectures spanning GQA 2:1 to 8:1, with a monotonic trend between GQA ratio, heterogeneity, and MCKP benefit. The Top-5% concentration diagnostic is a testable hypothesis, not a statistical claim.
239	6. **"RateQuant does K/V asymmetric allocation, do you?"** → Framework naturally treats K and V heads as independent items; plan_014 tests K/V separation.
240	7. **"Where are the downstream task results?"** → ✅ DONE (plan_012 + W3, all 5 models): Qwen (Spread): +1.25 to +4.00pp across 4 tasks, 72.8% avg recovery. Yi-1.5 (Spike): avg -0.77pp. Llama (Spike): avg -0.99pp (0/5 tasks positive — systematic). Mistral (Flat): avg -0.48pp. Gemma-2 (Flat): avg +0.14pp (noise). **Diagnostic predicts both PPL and downstream correctly across all 5 architectures**. Must report full per-task tables; use "shows minor degradation" not "preserves accuracy".
241	8. **"The profiler distortion=0.0 on Mistral suggests the profiling method is broken"** → Profiler correctly reports near-zero sensitivity differences. Some architectures genuinely have homogeneous head sensitivity, making non-uniform allocation futile.
242	9. **"If solver doesn't matter, why present MCKP at all?"** → (a) MCKP provides the formal framework for the constrained allocation problem — it's the lens through which we analyze the problem even if greedy solves it equally well, (b) presenting both solvers with identical results IS the evidence that the constraint is what matters, (c) for future extensions (more bit-widths, per-layer budgets), MCKP may regain advantage — we keep it as general framework.
243	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe671b0c-f9d0-40fc-a9de-b685a76d4ead",
  "isSidechain": false,
  "promptId": "e8e8fea0-d6a9-4b91-8885-3140c3cbe799",
  "type": "user",
  "uuid": "5bbd3489-c8ec-45e1-b2d2-e21ba2cf2e4e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/worst/paper_framing.md",
      "content": "# Paper Framing — ratekv\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission)\n- Deadline: ARR May 25, 2026 (11 days from today 2026-05-14)\n- Track: Efficient Methods for NLP\n\n## bf16 Consistency Resolution (2026-05-14)\n\n**已解决**：qwen_bf16_reeval 确认 bf16 ≈ fp16（baseline delta=0.0006, uniform delta=0.005）。compounding_sweep bf16 rerun 不需要。\n\n**eval pipeline 一致性**：exp_e 使用了不同的 eval 参数（baseline=8.82, MCKP=9.57），与主 pipeline（baseline=9.81）不一致。hires_mckp_reeval 用统一 pipeline 重测：MCKP hires bf16=10.9131。**论文使用统一 pipeline 数字**。\n\n| 指标 | 统一 pipeline (bf16) | exp_e pipeline (bf16) | fp16 (旧) |\n|------|---------------------|----------------------|-----------|\n| Baseline | **9.8106** | 8.819 | 9.81 |\n| Uniform 4-bit | **15.4454** | — | 15.45 |\n| MCKP hires (max_2bit=8) | **10.9131** | 9.569 | — |\n| MCKP lowres (max_2bit=8) | ~11.23 | 11.345 | 11.23 |\n\n## Core Insight\n\nPer-head KV cache quantization sensitivity varies dramatically across architectures, and the effectiveness of non-uniform mixed-precision allocation is fundamentally determined by the degree of this heterogeneity. We provide both the analysis framework — characterizing when non-uniform quantization helps via per-head sensitivity concentration metrics — and a surprisingly simple method fix: a cardinality constraint (≤k heads at 2-bit) that prevents compounding effects from profiler non-additivity and reduces the search space sufficiently that solver choice becomes irrelevant (greedy and MCKP produce identical allocations).\n\n## Core Claims (3 条)\n\n1. **Head sensitivity heterogeneity is architecture-dependent and determined by sensitivity *distribution shape*, not GQA ratio or concentration alone**: Per-KV-head quantization sensitivity is extremely non-uniform within models, but whether MCKP can exploit this heterogeneity depends on the *shape* of the sensitivity distribution, not just its magnitude. Critical counterexample: Yi-1.5-9B (GQA 8:1, concentration 0.71 — the *highest* in our lineup) provides *no benefit* from MCKP (7.22 vs 7.22 uniform), while Qwen2.5-7B (GQA 7:1, concentration 0.61) succeeds (+27.3%). The difference is distribution shape: Qwen has a *cluster* of sensitive heads (Layer 0, 4 heads with cross-bitwidth gradients — \"spread\" pattern, t₁/t₅=0.57), while Yi-1.5 has a single extreme outlier (L4H3, delta=13.12, t₁/t₅=0.90 — \"spike\" pattern) with sensitivity at only one bitwidth. A joint diagnostic — concentration ≳0.50 AND t₁/t₅ ≲0.70 — correctly separates the beneficial case (Qwen) from all four non-beneficial cases across five architectures. Three shape categories emerge:\n   - **Spread** (Qwen): high concentration + low t₁/t₅ → multiple heads with cross-bitwidth gradients → MCKP effective\n   - **Spike** (Yi-1.5, Llama): high t₁/t₅ → single outlier dominates → MCKP ineffective\n   - **Flat** (Mistral, Gemma-2): low concentration → near-uniform sensitivity → MCKP ineffective (t₁/t₅ irrelevant when concentration < 0.50)\n\n2. **Cardinality constraint is the primary intervention; unconstrained catastrophe is Spread-specific**: On non-consecutive discrete bit-widths {2,4,8,16}, unconstrained allocation produces **catastrophic** results on Spread-heterogeneity architectures (Qwen: greedy 32.45, MCKP 36.92 vs uniform 15.45 = 3.31× baseline) because per-head independent profiling distortions compound non-additively when many heads are simultaneously assigned extreme quantization. On non-Spread architectures, unconstrained allocation causes **mild-to-moderate degradation** (Yi 1.08×, Llama 1.07×, Mistral 1.08×, Gemma-2 1.47×) but still underperforms uniform 4-bit in all cases — the solver over-allocates 2-bit heads even when individual distortions appear small. A cardinality constraint (max_2bit≤k) is a simple and sufficient condition: it prevents compounding on Spread models, avoids 2-bit over-allocation on non-Spread models, AND reduces the feasible set to where solver choice is irrelevant — constrained greedy and constrained MCKP produce identical bit allocations and PPL (Δ=0.0000, both 11.2312). **Practical implication**: the concentration diagnostic determines whether to invest in MCKP + constraint (Spread models) or simply use uniform 4-bit (non-Spread models — saves solver computation with no quality loss). The profiling benefit beyond the constraint (hires vs lowres) is architecture-dependent: substantial on Spread models (Qwen), marginal on others. The optimal k is determinable via small-scale compounding effect test (plan_004).\n\n**Claim 2 three-pillar support** (Reviewer Q4, new narrative STRENGTHENS Claim 2):\n1. Spread models: constraint prevents catastrophe (Qwen 32.45→11.23)\n2. Flat models: constraint prevents moderate over-allocation (Gemma-2 8.85→~6.17, 106→8 heads at 2-bit)\n3. All models: constraint makes solver choice irrelevant (greedy=MCKP, Δ=0.0000)\nThis answers \"when\" and \"why\", not just \"what\" — stronger than original \"universal catastrophe\" narrative.\n\n3. **A joint empirical decision rule correctly separates beneficial from non-beneficial architectures**: Constrained allocation achieves 27.3% PPL improvement on Qwen (spread pattern: concentration 0.61, t₁/t₅=0.57), while providing no benefit on Yi-1.5 (spike: 0.71, t₁/t₅=0.90, ≈0%), Llama (spike: 0.34, t₁/t₅=0.71, +0.2%), Mistral (flat: 0.22, t₁/t₅=0.18, -0.4%), and Gemma-2 (flat: 0.23, t₁/t₅=0.38, -0.3%). The joint condition — concentration ≳0.50 AND t₁/t₅ ≲0.70 — correctly separates the beneficial case from all four non-beneficial cases across five architectures (5/5 accuracy). Concentration alone fails: Yi-1.5 (0.71) exceeds Qwen (0.61) yet gains nothing, because its spike pattern (single outlier, no cross-bitwidth gradient) cannot be exploited. Under aggressive compression (≥5×), constrained allocation prevents catastrophic collapse even on non-beneficial architectures (Llama 5.3×: constrained PPL 57.60 vs uniform 2-bit 2644). This provides practitioners an empirical decision rule for when to invest in mixed-precision KV cache quantization. **Claim strength note (Reviewer-verified)**: N=1 Spread → position as \"empirical decision rule\", NOT \"diagnostic framework\". If Qwen2.5-14B also confirms Spread → upgrade to \"empirical diagnostic\" (N=2).\n\n## Story Spine\n\n- **Problem**: KV cache quantization typically applies uniform bit-width across all heads. Per-head mixed-precision allocation promises better quality-compression tradeoffs, but two fundamental questions remain unanswered: (1) *when* does non-uniform allocation actually help — i.e., under what architectural and compression conditions does the added complexity pay off? (2) *how* to make existing allocation algorithms (greedy, MCKP) work correctly on hardware-aligned discrete bit-widths {2,4,8,16} where they currently fail catastrophically?\n\n- **Existing approaches & gaps**: RateQuant (May 2026) provides R-D optimal per-head allocation via continuous closed-form (Theorem 2) and discrete greedy (Algorithm 1, optimal on consecutive integers {2,...,6} per Proposition 6). However, on hardware-aligned non-consecutive sets {2,4,8,16}, RateQuant's greedy produces PPL 32.45 (vs optimal ~11.23) — the polymatroid structure that guarantees greedy optimality breaks. Moreover, unconstrained MCKP fares even worse (PPL 36.92) due to compounding effects from profiler non-additivity. Critically, neither RateQuant nor ARKV addresses *when* non-uniform allocation is beneficial.\n\n- **Our framing**: We present a systematic study of per-head KV cache quantization sensitivity across architectures and identify a surprisingly simple fix for the failure of existing algorithms on hardware-aligned bit-widths: a cardinality constraint limiting the number of heads assigned to extreme quantization levels. This single intervention (a) prevents compounding effects, (b) reduces the search space to where solver choice is irrelevant — greedy and MCKP produce identical optimal allocations, and (c) can be parameterized via a small-scale compounding test. Beyond the method, we establish that the benefit of non-uniform allocation is architecture-dependent and quantifiable via an empirical decision rule (concentration + distribution shape), providing practitioners a two-metric check for when mixed-precision is worthwhile.\n\n- **Headline result template**: \"We show that the benefit of non-uniform per-head KV cache quantization is concentration-dependent: on spread-heterogeneity architectures (Qwen, concentration 0.61), unconstrained solvers fail catastrophically (PPL 32-37 vs uniform 15.45), while a cardinality constraint (≤k heads at 2-bit) achieves 27.3% PPL improvement with identical results from greedy and MCKP (Δ=0.0000). On non-spread architectures (4 models, 1.07-1.47× baseline), unconstrained solvers cause only mild degradation, and constrained MCKP offers no benefit over uniform 4-bit at either PPL or downstream task level (<1pp avg). An empirical decision rule (concentration ≳0.50 AND t₁/t₅ ≲0.70) correctly separates the beneficial case from all four non-beneficial cases (5/5 accuracy) at both PPL and downstream task level, providing practitioners a two-metric check to determine whether mixed-precision KV cache quantization is worthwhile — or whether uniform quantization suffices.\"\n\n## \"When Does Non-Uniform Allocation Help?\" — Analysis Chapter\n\nFive case studies representing the full spectrum of heterogeneity:\n\n| Case | Model | GQA | Top-5% Conc. | Constrained vs Uniform (4×) | Role in Paper |\n|------|-------|-----|--------------|------------------------------|---------------|\n| **Strong positive** | Qwen2.5-7B | 7:1 | 0.59-0.66 | **+27.3% (11.23 vs 15.45)** | Primary showcase; \"spread\" pattern (L0 cluster, 4 heads, 26× dominance) |\n| **GQA counterexample** | Yi-1.5-9B | 8:1 | 0.71 (hires) | ≈0% (7.22 vs 7.22) | Highest GQA but no benefit; \"spike\" pattern (L4H3 single outlier, 34% of total delta) |\n| **Marginal** | Llama-3.1-8B | 4:1 | 0.34-0.59 | +0.2% (8.45 vs 8.47) | Boundary condition; constraint never binds (natural k=2) |\n| **Negative** | Mistral-7B-v0.3 | 4:1 | 0.22 (hires) | -0.4% (7.16 vs 7.13) | Profiler zero-signal; monotonic k-PPL curve |\n| **Strongest negative** | Gemma-2-9B | 2:1 | 0.23 (hires) | -0.3% (9.05 vs 9.03) | Low-end anchor; most uniform sensitivity (CV=1.28, t₁/t₅=0.38) |\n\n**Spike vs Spread insight**: Yi-1.5 vs Qwen illustrates why GQA ratio alone is insufficient. Both have high GQA (8:1 vs 7:1), but Qwen's L0 *cluster* of sensitive heads creates optimization opportunities for MCKP, while Yi-1.5's single extreme outlier (L4H3) cannot be exploited — the solver assigns 8-bit to that one head but has no other heads to differentiate. Distribution shape matters more than the existence of outliers.\n\n**Compression amplifies benefit**: Even on low-heterogeneity Llama, aggressive 5.3× compression yields constrained PPL=57.60 vs uniform 2-bit=2643.77 (45× better).\n\n**Joint diagnostic** (n=5, 5/5 correct): concentration ≳0.50 AND t₁/t₅ ≲0.70 → non-uniform allocation recommended (spread pattern). Either condition violated → uniform suffices at moderate compression; non-uniform still valuable at aggressive compression. Yi-1.5 (concentration 0.71 but t₁/t₅=0.90 — spike) and Qwen (0.61, t₁/t₅=0.57 — spread) illustrate why concentration alone is insufficient.\n\n## Solver Equivalence Evidence (plan_016, CONFIRMED ✅)\n\n| Method | PPL | Bit Distribution | Budget |\n|--------|-----|-------------------|--------|\n| Greedy unconstrained | 32.45 | {2:68, 4:30, 8:4, 16:10} | 0.25 |\n| MCKP unconstrained | 36.92 | — | 0.25 |\n| **Greedy + max_2bit=8** | **11.2312** | **{8:4, 4:100, 2:8}** | **0.25** |\n| **MCKP + max_2bit=8** | **11.2312** | **{8:4, 4:100, 2:8}** | **0.25** |\n| Uniform 4-bit | 15.4454 | all 4-bit | 0.25 |\n\nKey takeaway: The constraint is the primary intervention — without it, both solvers fail; with it, solver choice is irrelevant (Δ=0.0000). This powerfully demonstrates the constraint is THE contribution.\n\n## Cross-Architecture Evidence Summary\n\n| Model | GQA | KV Heads | Top-5% Conc. | Unconstrained ×baseline (W2 v2) | Constrained vs Uniform (4×) | Distribution Shape | Conclusion |\n|-------|-----|----------|--------------|--------------------------------|------------------------------|-------------------|------------|\n| Qwen2.5-7B | 7:1 | 112 | **0.61** | **3.31× (32.45)** ☠️ | **+27.3% (11.23 vs 15.45)** | Spread (L0 cluster, 4 heads) | ✅ Strong benefit |\n| Yi-1.5-9B | 8:1 | 192 | **0.71** (hires) | 1.08× (7.56) | **≈0% (7.22 vs 7.22)** | Spike (L4H3 single outlier) | ❌ GQA counterexample |\n| Llama-3.1-8B | 4:1 | 256 | 0.57 (hires) | 1.07× (8.63) | **+0.2% (8.45 vs 8.47)** | Spike (borderline t₁/t₅=0.71) | ≈ Marginal |\n| Mistral-7B-v0.3 | 4:1 | 256 | **0.22** (hires) | 1.08× (7.57) | **-0.4% (7.16 vs 7.13)** | Flat (profiler zero-signal) | ❌ Negative |\n| Gemma-2-9B | 2:1 | 336 | **0.23** (hires) | 1.47× (8.85) | **-0.3% (9.05 vs 9.03)** | Flat (CV=1.28, t₁/t₅=0.38) | ❌ Strongest negative |\n\n**Unconstrained pattern** (W2 v2, all WikiText-2 test eval, gradient narrative): Unconstrained degradation follows a **concentration-dependent gradient**, not a binary catastrophe/benign split:\n- **Spread** (Qwen, conc=0.61): **3.31×** catastrophic — L0 cluster creates massive compounding\n- **Flat-high-2bit** (Gemma-2, conc=0.23): **1.47×** moderate — solver assigns 106/336=31.5% heads to 2-bit because distortions are indistinguishable (CV=1.28), cumulative effect significant despite small per-head delta\n- **Spike/Flat-low-2bit** (Yi 1.08×, Llama 1.07×, Mistral 1.08×): mild — solver selects few 2-bit heads (Yi 11.5%, Llama 4.7%, Mistral 16.4%)\n- In ALL cases unconstrained ≤ uniform 4-bit — solver consistently over-allocates 2-bit heads\n\n**Gemma-2 1.47× must be discussed in paper** (Reviewer mandate, severity: warning):\n\nThree-tier labeling (NOT binary catastrophe/benign):\n- **Catastrophic** (3.31×): Spread model (Qwen) — L0 cluster compounding\n- **Moderate** (1.47×): Flat-high-2bit (Gemma-2) — solver over-allocation from indistinguishable distortions\n- **Mild** (1.07-1.08×): Spike/Flat-low-2bit (Yi, Llama, Mistral)\n\nReviewer-suggested paragraph for paper (1 段, 3-4 句):\n\"Gemma-2-9B exhibits a moderate 1.47× degradation under unconstrained allocation, higher than the 1.07–1.08× observed in other non-Spread models. This stems from its flat sensitivity distribution (concentration 0.23, CV 1.28): the solver cannot meaningfully differentiate heads, leading to 31.5% of heads assigned to 2-bit (vs 4.7–16.4% in other models). While not catastrophic, this over-allocation still motivates the cardinality constraint even on flat-distribution architectures. The constraint reduces 2-bit heads from 106 to 8, yielding PPL within 0.3% of uniform — confirming that the constraint universally prevents solver over-allocation regardless of distribution shape.\"\n\nThis **strengthens** the paper: (1) honesty → credibility, (2) constraint has universal value (not just Spread), (3) explains solver degradation mechanism under low signal → added insight depth.\n\n⚠️ **Data file note**: `artifacts/w2_unconstrained_v2_results.json` still has old Gemma-2 BOS bug data (baseline=711.6). Fix in `artifacts/w2_gemma2_bos_fix_results.json`. Agent tasked to merge.\n\n**Key pattern**: Constrained allocation benefit depends on the joint condition (concentration ≳0.50 AND t₁/t₅ ≲0.70, 5/5 correct), NOT GQA ratio or concentration alone. Yi-1.5 (GQA 8:1, concentration 0.71 — highest — yet no benefit) vs Qwen (GQA 7:1, concentration 0.61, +27.3%) demonstrates that neither GQA nor concentration alone is a reliable proxy. The critical factor is sensitivity *distribution shape*: spread (multiple heads with cross-bitwidth gradients) enables MCKP, while spike (single outlier) or flat (uniform sensitivity) does not.\n\n**Aggressive compression** (Llama): At 5.3× compression, constrained PPL=57.60 vs uniform 2-bit=2643.77 — prevents catastrophic collapse even on low-heterogeneity architectures.\n\n### Mistral k Ablation (256 KV heads, budget=0.25)\n\nPPL monotonically increases with k — every additional 2-bit head hurts. Even best k=4 (PPL 7.1648) is worse than uniform (7.131).\n\n| k | PPL | 2-bit | 4-bit | 8-bit | 16-bit | mem |\n|---|-----|-------|-------|-------|--------|-----|\n| 4 | **7.1648** | 4 | 252 | 0 | 0 | 0.248 |\n| 8 | 7.1997 | 8 | 247 | 0 | 1 | 0.249 |\n| 12 | 7.2448 | 12 | 242 | 0 | 2 | 0.250 |\n| 16 | 7.3106 | 16 | 238 | 0 | 2 | 0.248 |\n| 18 | 7.3231 | 18 | 235 | 0 | 3 | 0.250 |\n| uniform 4-bit | 7.131 | 0 | 256 | 0 | 0 | 0.250 |\n\nContrast with Qwen (U-shaped, optimal k=8) and Llama (flat, natural k=2). Mistral's monotonic pattern confirms profiler zero-signal: no head benefits from 2-bit downgrade.\n\n### Llama k Ablation (256 KV heads, budget=0.25)\n\nAll k values produce identical PPL=8.4498. MCKP naturally selects only 2 heads for 2-bit — constraint never binds. Marginal +0.2% over uniform (8.4498 vs 8.469).\n\n### Downstream Eval — Cross-Architecture (W3, 0-shot, 5 tasks)\n\n**Qwen2.5-7B (Spread) — MCKP benefits translate to downstream** ✅\n\n| Task | Uniform 4-bit | MCKP hires | Δ | BF16 Baseline |\n|------|---------------|------------|---|---------------|\n| ARC-C | 0.4812 | 0.5137 | **+3.16pp** | 0.5290 |\n| HellaSwag | 0.7284 | 0.7684 | **+4.00pp** | 0.7833 |\n| PIQA | 0.7661 | 0.7786 | **+1.25pp** | 0.7932 |\n| WinoGrande | 0.6622 | 0.6819 | **+1.97pp** | 0.6898 |\n| **Avg recovery** | — | — | **72.8%** | — |\n\n**Yi-1.5-9B (Spike) — No MCKP benefit, consistent with PPL** (W3)\n\n| Task | Uniform 4-bit | MCKP (k=8) | Δ |\n|------|---------------|------------|---|\n| arc_easy | 0.7946 | 0.7854 | -0.92pp |\n| arc_challenge | 0.5205 | 0.4881 | **-3.24pp** |\n| hellaswag | 0.5857 | 0.5797 | -0.60pp |\n| piqa | 0.7927 | 0.7894 | -0.33pp |\n| winogrande | 0.7174 | 0.7301 | +1.27pp |\n| **Average** | **0.6822** | **0.6745** | **-0.77pp** |\n\n**Llama-3.1-8B (Spike) — No MCKP benefit, consistent with PPL** (W3)\n\n| Task | Uniform 4-bit | MCKP (k=8) | Δ |\n|------|---------------|------------|---|\n| arc_easy | 0.8173 | 0.8039 | -1.34pp |\n| arc_challenge | 0.5256 | 0.4991 | **-2.65pp** |\n| hellaswag | 0.6026 | 0.6012 | -0.14pp |\n| piqa | 0.7867 | 0.7802 | -0.65pp |\n| winogrande | 0.7253 | 0.7238 | -0.15pp |\n| **Average** | **0.6915** | **0.6816** | **-0.99pp** |\n\n**Mistral-7B-v0.3 (Flat) — No MCKP benefit, consistent with PPL** (W3)\n\n| Task | Uniform 4-bit | MCKP (k=4) | Δ |\n|------|---------------|------------|---|\n| arc_easy | — | — | — |\n| arc_challenge | — | — | — |\n| hellaswag | — | — | — |\n| piqa | — | — | — |\n| winogrande | — | — | — |\n| **Average** | **0.6894** | **0.6846** | **-0.48pp** |\n\n**Gemma-2-9B (Flat) — Negligible MCKP effect, noise range** (W3)\n\n| Task | Uniform 4-bit | MCKP | Δ |\n|------|---------------|------|---|\n| **Average** | **0.7251** | **0.7265** | **+0.14pp** (noise) |\n\n**Downstream summary (Reviewer-verified framing)**:\n- Diagnostic correctly predicts both PPL and downstream outcomes across **all 5 tested models**\n- Spread (Qwen): consistent downstream gains (+1.25 to +4.00pp)\n- Non-Spread (4 models): MCKP shows **minor systematic degradation** vs uniform (Yi -0.77pp, Llama -0.99pp, Mistral -0.48pp, Gemma-2 +0.14pp noise)\n- **Llama signal**: 0/5 tasks where MCKP ≥ uniform — degradation is systematic, not task-specific noise\n- arc_challenge shows largest per-task effect (Yi -3.24pp, Llama -2.65pp)\n- **Paper must**: (a) report full per-task tables, not just averages, (b) use \"shows minor degradation\" NOT \"preserves accuracy\" — the latter has spin, (c) note arc_challenge as worst-case explicitly\n- **Limitation**: no multi-seed CI for downstream — 0-shot arc_challenge -3.24pp could be questioned for significance\n- **arc_challenge 系统性信号** (Reviewer 观察): arc_challenge 退化跨模型一致（Yi -3.24pp, Llama -2.65pp, Mistral -1.19pp, Gemma-2 -0.17pp），不是随机噪声。论文应主动讨论：\"ARC-Challenge shows the largest per-task sensitivity to allocation strategy, consistent with its reliance on multi-step reasoning where subtle KV cache errors accumulate.\"\n- **呈现方式**: 主表放完整 per-task 数据，文字用均值+range 概括。建议措辞：\"Across four non-Spread architectures, constrained MCKP shows minor average degradation vs uniform 4-bit (Yi -0.77pp, Llama -0.99pp, Mistral -0.48pp, Gemma-2 +0.14pp). Per-task variation ranges from +1.27pp (Yi, WinoGrande) to -3.24pp (Yi, ARC-Challenge).\"\n\n## Allocation Baseline Evidence (plan_015, mckp_reeval)\n\nAll numbers from unified bf16 eval pipeline, budget=0.25.\n\n| Model | Baseline | Uniform 4-bit | MCKP | L0-random (mean±std) | L0-random (median) | Naive Positional | MCKP improvement |\n|-------|----------|---------------|------|----------------------|---------------------|------------------|------------------|\n| Qwen2.5-7B (k=8) | 9.8106 | 15.4454 | 10.9131 | 11.691±0.422 | **11.515** | 12.230 | 27.3% vs uniform (standard); 29.4% (hires, §5.4) |\n| Llama-3.1-8B (k=2) | 8.0918 | 8.469 | 8.4498 | 10.479±1.033 | **10.038** | 9.941 | +0.2% vs uniform |\n| Mistral-7B-v0.3 (k=4) | 7.035 | 7.131 | 7.1648 | 7.560±0.087 | **7.586** | 7.481 | -0.4% vs uniform |\n\n**Outlier note**: seed_4 inflates mean on Qwen (12.51) and Llama (12.44). Median is more robust: Qwen median 11.515 vs mean 11.691 (−0.176); Llama median 10.038 vs mean 10.479 (−0.441). Mistral has no outlier (median ≈ mean). Paper should report both mean±std and median.\n\n**MCKP vs L0-random (median)**: Qwen 10.91 vs 11.52 (−5.2%); Llama 8.45 vs 10.04 (−15.8%); Mistral 7.16 vs 7.59 (−5.7%). MCKP consistently outperforms random L0-constrained allocation across all architectures.\n\n## Differentiation from RateQuant\n\n| Aspect | RateQuant | Ours |\n|--------|-----------|------|\n| Bit-width selection | Greedy on consecutive integers {2,...,6} (Prop. 6 optimal) + continuous closed-form (Thm. 2) | Cardinality-constrained allocation on hardware-aligned {2,4,8,16}-bit |\n| Distortion model | Additive, parametric D(b)=α·β^{-b} | Additive + cardinality regularization for non-additivity |\n| Compounding effects | Acknowledged (Appendix M) but unaddressed | **Core contribution**: cardinality constraint prevents compounding; first quantitative evidence |\n| Action space | Consecutive integers (polymatroid → greedy optimal) | Non-consecutive hardware-aligned (polymatroid breaks → constraint needed, solver doesn't matter) |\n| Solver requirement | Greedy (provably optimal in their setting) | **Any solver** — constrained greedy = constrained MCKP (Δ=0.0000 PPL) |\n| K/V allocation | Asymmetric K/V budget (e.g. K=2.85, V=2.15) | MCKP/greedy treats K/V heads as independent items (natural extension) |\n| **Applicability analysis** | **Not addressed — assumes non-uniform always helps** | **Systematic study of when non-uniform allocation is beneficial (new contribution)** |\n\n## Venue Fit Risks\n\n- **\"The constraint is just a heuristic, not a real contribution\"**: Strongest reviewer attack under new framing. Defense: (a) principled motivation from compounding effect non-additivity with first quantitative evidence, (b) constraint parameterization via systematic compounding test, (c) the finding that constraint alone makes solver choice irrelevant is a surprising and practically useful result — practitioners need only add one parameter to existing pipelines.\n- **Incrementality over RateQuant**: Defense: (a) RateQuant's greedy is suboptimal unconstrained on {2,4,8,16} (PPL 32.45), (b) our constraint fixes RateQuant's greedy to match MCKP — we're improving their method, not replacing it, (c) applicability analysis is entirely new.\n- **Method only strong on one architecture (Qwen)**: 5 models tested, only Qwen shows clear benefit. Mitigate: (a) analysis contribution framing — characterizing boundary conditions is more useful than universal positive, (b) honest negative/marginal results (Yi-1.5, Gemma-2, Mistral, Llama) strengthen credibility, (c) unlike prior work that assumes non-uniform always helps, we provide the first systematic study of *when it fails*, (d) Yi-1.5 (GQA 8:1, FAIL) is particularly powerful — it disproves the naive \"higher GQA = more benefit\" hypothesis and shows our diagnostic is needed.\n- **GQA ratio is not a reliable proxy**: Yi-1.5 (GQA 8:1) directly contradicts a GQA-based prediction. Do NOT present GQA ratio as a predictor — present it as one contributing factor. The reliable predictor is Top-5% concentration (0.50 threshold, 5/5 correct). The \"spike vs spread\" analysis explains WHY same-GQA models differ.\n- **Statistical power**: n=5 models is directional evidence, not statistical claim. Do NOT claim \"significant correlation\" — use \"consistent pattern across 5 architectures\" or \"5/5 correctly classified by the 0.50 threshold.\"\n- **No eviction arm**: Mention as negative finding; framework extends naturally to eviction.\n\n## Anticipated Reviewer Concerns\n\n1. **\"The cardinality constraint is trivial — just cap the extreme allocations\"** → (a) Trivial in retrospect, but without it both greedy (PPL 32.45) and MCKP (PPL 36.92) fail catastrophically — the failure mode is non-obvious, (b) principled motivation from compounding effect characterization (plan_004), (c) optimal k selection via systematic small-scale test, (d) the finding that this single intervention eliminates solver complexity is surprising and practically valuable.\n2. **\"This is just RateQuant with a constraint added\"** → (a) We agree — and that's the point: RateQuant's greedy + our constraint achieves identical results to MCKP + constraint, (b) the constraint addresses a real gap: compounding effects on {2,4,8,16} that RateQuant acknowledges but doesn't solve, (c) applicability analysis is new.\n3. **\"The method only works on Qwen — isn't this a Qwen paper?\"** → We systematically test 4-5 architectures spanning GQA 2:1 to 8:1 and honestly report negative results (Gemma-2, Mistral). The analysis contribution — characterizing *boundary conditions* of non-uniform quantization — generalizes beyond any single model and is more useful than a universally positive but misleading claim.\n4. **\"How does this work at different compression ratios?\"** → Budget sweep across 2×, 4×, 8× (plan_005). Aggressive compression on Llama shows benefit amplifies even on low-heterogeneity models.\n5. **\"n=3/4/5 models is not enough for the heterogeneity claim\"** → Acknowledged as limitation. We present directional evidence across 4-5 architectures spanning GQA 2:1 to 8:1, with a monotonic trend between GQA ratio, heterogeneity, and MCKP benefit. The Top-5% concentration diagnostic is a testable hypothesis, not a statistical claim.\n6. **\"RateQuant does K/V asymmetric allocation, do you?\"** → Framework naturally treats K and V heads as independent items; plan_014 tests K/V separation.\n7. **\"Where are the downstream task results?\"** → ✅ DONE (plan_012 + W3, all 5 models): Qwen (Spread): +1.25 to +4.00pp across 4 tasks, 72.8% avg recovery. Yi-1.5 (Spike): avg -0.77pp. Llama (Spike): avg -0.99pp (0/5 tasks positive — systematic). Mistral (Flat): avg -0.48pp. Gemma-2 (Flat): avg +0.14pp (noise). **Diagnostic predicts both PPL and downstream correctly across all 5 architectures**. Must report full per-task tables; use \"shows minor degradation\" not \"preserves accuracy\".\n8. **\"The profiler distortion=0.0 on Mistral suggests the profiling method is broken\"** → Profiler correctly reports near-zero sensitivity differences. Some architectures genuinely have homogeneous head sensitivity, making non-uniform allocation futile.\n9. **\"If solver doesn't matter, why present MCKP at all?\"** → (a) MCKP provides the formal framework for the constrained allocation problem — it's the lens through which we analyze the problem even if greedy solves it equally well, (b) presenting both solvers with identical results IS the evidence that the constraint is what matters, (c) for future extensions (more bit-widths, per-layer budgets), MCKP may regain advantage — we keep it as general framework.\n",
      "numLines": 243,
      "startLine": 1,
      "totalLines": 243
    }
  },
  "sourceToolAssistantUUID": "fe671b0c-f9d0-40fc-a9de-b685a76d4ead",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T085855 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/…",
  "leafUuid": "5bbd3489-c8ec-45e1-b2d2-e21ba2cf2e4e",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier simulated paper for dream_20260515T085855",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8"
}
```

---

### Assistant

_source line 16 · 2026-05-15T09:54:54.254Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the experiment data and paper framing. Let me construct a complete LaTeX paper based on the "worst" tier narrative guidance:

Key narrative reframing for worst tier:
1. Cardinality constraint as universal safeguard (architecture-agnostic)
2. Systematic negative result (non-uniform beneficial in only 1/6 cases)
3. Compounding effect characterization (mechanism analysis)

The diagnostic/decision rule is downgraded since it has a false positive (Qwen14B). Title shifts to emphasize the cardinality constraint.


I'm now compiling all ten experiments from the dataset into a comprehensive paper structure with corresponding tables and results sections for each. 4 Cross-Dataset Evaluation (Qwen7B)
11. RateQuant Greedy Comparison
12. Oracle Comparison
13. Cross-Domain Calibration Robustness
14. Head Sensitivity Visualization
15. Downstream Task Evaluation
16. 70B Profiling-Only
17. K/V Separation
18. L0-Only Heuristic Baseline
19. RateQuant Greedy + Cardinality Constraint
20. Multi-Seed Error Bars
21. Runtime/Latency Benchmark
22. W9 Compounding Scaling
23. Qwen2.5-14B Downstream Eval

Let me organize these into a coherent paper structure:

- Abstract
- Introduction
- Related Work (brief)
- Method
  - Problem formulation (MCKP for KV cache)
  - Cardinality constraint
  - Profiling
- Experiments
  - Setup
  - Cross-architecture profiling (covers exps 1, 5, 6, 16 - the profiling results)
  - Cardinality constraint effectiveness (covers exps 2, 3, 7, 11, 19 - constraint results)
  - Systematic negative result (covers exps 2, 5, 6, 15, 23 - the negative results)
  - Compounding effect characterization (covers exps 7, 22 - compounding)
  - Budget sweep (exp 8)
  - Solver equivalence (exps 11, 12, 19)
  - Ablations & robustness (exps 4, 9, 10, 13, 17, 18, 20, 21)
- Analysis / Discussion
- Conclusion

Now I'm ready to write the full paper, pulling data from the experiments and structuring everything around the core narrative: constraints as a safeguard mechanism, the systematic negative result showing where the approach fails, and the compounding effect that emerges under certain conditions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bbd3489-c8ec-45e1-b2d2-e21ba2cf2e4e",
  "isSidechain": false,
  "requestId": "req_011Cb49nRowGkQzeZFXmTzyK",
  "type": "assistant",
  "uuid": "02c4d23d-36f7-42bf-a911-5af0ed4fc026",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MpZHsFreGDESX2QDLrw9vZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30744,
      "cache_read_input_tokens": 24075,
      "output_tokens": 938,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30744,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 938,
          "cache_read_input_tokens": 24075,
          "cache_creation_input_tokens": 30744,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30744
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

_source line 17 · 2026-05-15T09:54:54.281Z_

Now let me check if the output directory exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02c4d23d-36f7-42bf-a911-5af0ed4fc026",
  "isSidechain": false,
  "requestId": "req_011Cb49nRowGkQzeZFXmTzyK",
  "type": "assistant",
  "uuid": "e1359b4d-2fa5-40d2-8a4d-69f7e41bfd09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MpZHsFreGDESX2QDLrw9vZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30744,
      "cache_read_input_tokens": 24075,
      "output_tokens": 938,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30744,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 938,
          "cache_read_input_tokens": 24075,
          "cache_creation_input_tokens": 30744,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30744
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

_source line 18 · 2026-05-15T09:54:55.628Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01SQTUwZSvSAbhgcZ8wrjrmp`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/worst/",
  "description": "List target directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1359b4d-2fa5-40d2-8a4d-69f7e41bfd09",
  "isSidechain": false,
  "requestId": "req_011Cb49nRowGkQzeZFXmTzyK",
  "type": "assistant",
  "uuid": "9bd3eeac-0e3e-475d-99a1-e59c867bb65f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MpZHsFreGDESX2QDLrw9vZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30744,
      "cache_read_input_tokens": 24075,
      "output_tokens": 938,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30744,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 938,
          "cache_read_input_tokens": 24075,
          "cache_creation_input_tokens": 30744,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30744
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

_source line 19 · 2026-05-15T09:54:55.773Z_

<details><summary>↩ Tool result · `toolu_01SQTUwZSvSAbhgcZ8wrjrmp`</summary>

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
  "parentUuid": "9bd3eeac-0e3e-475d-99a1-e59c867bb65f",
  "isSidechain": false,
  "promptId": "e8e8fea0-d6a9-4b91-8885-3140c3cbe799",
  "type": "user",
  "uuid": "d1d528ac-6eff-4d84-8f63-eb76624586b2",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "9bd3eeac-0e3e-475d-99a1-e59c867bb65f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-15T09:54:58.841Z_

Now I'll write the complete LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1d528ac-6eff-4d84-8f63-eb76624586b2",
  "isSidechain": false,
  "requestId": "req_011Cb49p9KJd8xdrK6JRvKHs",
  "type": "assistant",
  "uuid": "b62b381a-1ed4-47d8-bba2-e1fa499e0c82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Wgtjvfz9toTm23wUN8xY9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 965,
      "cache_read_input_tokens": 54819,
      "output_tokens": 10927,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 965,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10927,
          "cache_read_input_tokens": 54819,
          "cache_creation_input_tokens": 965,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 965
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

_source line 21 · 2026-05-15T10:00:19.226Z_

<details open><summary>🔧 Tool call — Write · `toolu_01PVYABphHwosyxrHVXsZRa6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/worst/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{tablefootnote}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\n\\newcommand{\\ttt}[1]{\\texttt{#1}}\n\\newcommand{\\ppl}{\\text{PPL}}\n\n\\title{The Cardinality Constraint You Need for\\\\Hardware-Aligned KV Cache Quantization}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n%% ============================================================\n%% ABSTRACT\n%% ============================================================\n\\begin{abstract}\nPer-head mixed-precision KV cache quantization promises better quality--compression trade-offs than uniform bit-width assignment, yet we find it is beneficial in only one out of six architectures tested.\nWe conduct a systematic study across six models (Qwen2.5-7B/14B/72B, Yi-1.5-9B, Llama-3.1-8B, Mistral-7B, Gemma-2-9B) and identify three contributions.\n\\textbf{(1)}~A cardinality constraint---limiting the number of KV heads assigned to 2-bit precision---acts as a universal safeguard: it prevents catastrophic compounding on the one architecture where non-uniform allocation helps (Qwen2.5-7B: PPL 11.23 vs.\\ unconstrained 36.92) and is harmless ($\\leq$uniform) on all others.\nThe constraint further makes solver choice irrelevant: constrained greedy and constrained MCKP produce identical allocations ($\\Delta$=0.00).\n\\textbf{(2)}~We document a systematic negative result: across five of six architectures, constrained non-uniform allocation provides no meaningful improvement over uniform 4-bit quantization (range $-$0.8\\% to +1.2\\%), challenging the common assumption that mixed-precision KV cache quantization is universally beneficial.\n\\textbf{(3)}~We characterize the compounding effect on non-consecutive hardware-aligned bit-widths \\{2,4,8,16\\}: unconstrained solvers over-allocate 2-bit heads, and the resulting degradation is super-additive with a U-shaped PPL--$k$ curve whose elbow determines the optimal constraint parameter.\n\\end{abstract}\n\n%% ============================================================\n%% 1  INTRODUCTION\n%% ============================================================\n\\section{Introduction}\n\nKV cache quantization is a standard technique for reducing the memory footprint of autoregressive language model inference.\nMost deployed systems use uniform bit-width assignment---every KV head receives the same precision.\nAn appealing alternative is \\emph{mixed-precision} allocation, where a solver (greedy or MCKP) assigns per-head bit-widths to maximize quality under a total memory budget.\nPrior work such as RateQuant demonstrates that this is optimal for consecutive integer bit-widths \\{2,\\ldots,6\\} via polymatroid greedy~\\cite{ratequant2026}.\n\nHowever, modern hardware natively supports only \\emph{non-consecutive} bit-widths \\{2,4,8,16\\}.\nOn this action space, the polymatroid structure that guarantees greedy optimality breaks down.\nWe find that both unconstrained greedy (PPL~32.45) and unconstrained MCKP (PPL~36.92) fail catastrophically on Qwen2.5-7B compared to uniform 4-bit (PPL~15.45), producing allocations that are $2$--$3\\times$ worse than the baseline they are supposed to improve.\nOn the remaining five architectures, unconstrained allocation produces mild-to-moderate degradation ($1.07$--$1.22\\times$ baseline) but still never outperforms uniform.\n\nOur key finding is that a single, architecture-agnostic intervention---a \\emph{cardinality constraint} limiting the number of heads assigned to the most aggressive quantization level---is both necessary and sufficient:\n\\begin{itemize}\n\\item On the one architecture where mixed-precision helps (Qwen2.5-7B, ``spread'' sensitivity pattern), the constraint prevents compounding and achieves 27.3\\% PPL improvement over uniform.\n\\item On all other architectures, the constrained allocation matches or is within noise of uniform---it never hurts.\n\\item Under the constraint, solver choice is irrelevant: greedy and MCKP produce identical bit allocations and PPL ($\\Delta$=0.0012).\n\\end{itemize}\n\nBeyond the method, we document a \\emph{systematic negative result}: non-uniform KV cache quantization is beneficial in only 1 out of 6 architectures at standard 4$\\times$ compression.\nThis challenges the implicit assumption in prior work that per-head allocation is universally helpful, and provides practitioners with evidence that uniform 4-bit is sufficient for most models.\nWe also characterize the \\emph{compounding effect}---the mechanism by which per-head profiling distortions accumulate super-additively when many heads are simultaneously assigned extreme bit-widths---and show that the cardinality constraint directly addresses this mechanism.\n\n%% ============================================================\n%% 2  RELATED WORK\n%% ============================================================\n\\section{Related Work}\n\n\\paragraph{KV Cache Quantization.}\nKIVI~\\cite{kivi2024} and KVQuant~\\cite{kvquant2024} demonstrate that KV caches can be quantized to low precision with modest quality loss. These systems use uniform bit-width across all heads.\n\n\\paragraph{Per-Head Mixed Precision.}\nRateQuant~\\cite{ratequant2026} formulates per-head KV cache allocation as a rate--distortion optimization problem, proving greedy optimality on consecutive integer bit-widths via polymatroid structure (Proposition~6). Their continuous closed-form (Theorem~2) and discrete greedy (Algorithm~1) assume $\\{2,\\ldots,6\\}$. On hardware-aligned $\\{2,4,8,16\\}$, the polymatroid property does not hold, and their greedy produces suboptimal allocations. RateQuant acknowledges compounding effects (Appendix~M) but does not address them.\n\n\\paragraph{Quantization-Aware Allocation.}\nARKV and related methods use learned or heuristic per-head budgets. None systematically studies \\emph{when} non-uniform allocation is beneficial across architectures.\n\n%% ============================================================\n%% 3  METHOD\n%% ============================================================\n\\section{Method}\n\n\\subsection{Problem Formulation}\n\nGiven a model with $N$ KV heads, a set of hardware-aligned bit-widths $\\mathcal{B} = \\{2, 4, 8, 16\\}$, and a total memory budget $B$ (expressed as average bits per head), we seek an assignment $b_i \\in \\mathcal{B}$ for each head $i$ that minimizes perplexity subject to $\\frac{1}{N}\\sum_i b_i \\leq B$.\n\nWe formulate this as a Multiple-Choice Knapsack Problem (MCKP): each head $i$ is an item group with $|\\mathcal{B}|$ choices, the ``weight'' of choice $b$ for head $i$ is $b$, and the ``profit'' is the negative distortion $-\\delta_i(b)$ measured by per-head profiling.\n\n\\subsection{Per-Head Sensitivity Profiling}\n\nFor each head $i$ and bit-width $b \\in \\mathcal{B}$, we measure the distortion $\\delta_i(b)$: quantize only head $i$ to $b$-bit while keeping all other heads at 16-bit, and record the PPL change on a calibration set.\nWe use WikiText-2 with 16 sequences of 512 tokens (low-resolution) or 64 sequences of 2048 tokens (high-resolution).\n\n\\subsection{Cardinality Constraint}\n\nThe profiling procedure measures distortions \\emph{independently}: $\\delta_i(b)$ is the effect of quantizing head $i$ alone. When the solver assigns $k$ heads to 2-bit simultaneously, the joint distortion is not $\\sum_i \\delta_i(2)$ but empirically larger---a \\emph{compounding effect}. On non-consecutive bit-widths, this non-additivity is severe because the gap between 2-bit and 4-bit is large.\n\nWe introduce a cardinality constraint: $|\\{i : b_i = 2\\}| \\leq k$, limiting the number of heads at the most aggressive quantization level. This single parameter:\n\\begin{enumerate}\n\\item Prevents compounding by limiting simultaneous extreme assignments.\n\\item Reduces the feasible set sufficiently that solver choice is irrelevant.\n\\item Can be set via a small-scale sweep of $k$ vs.\\ PPL (Section~\\ref{sec:compounding}).\n\\end{enumerate}\n\n\\subsection{Solver Equivalence}\n\nUnder the cardinality constraint, the constrained MCKP feasible set is small enough that a simple greedy algorithm (assign 2-bit to the $k$ heads with highest $\\delta_i(2) - \\delta_i(4)$, then fill remaining budget optimally) produces the same allocation as full MCKP. We verify this empirically: on Qwen2.5-7B with $k{=}8$, greedy PPL = MCKP PPL = 11.23 ($\\Delta$=0.0012).\n\n%% ============================================================\n%% 4  EXPERIMENTS\n%% ============================================================\n\\section{Experiments}\n\n\\subsection{Setup}\n\nWe evaluate six models spanning diverse architectures and GQA configurations:\nQwen2.5-7B (GQA 7:1, 112 KV heads),\nQwen2.5-14B (GQA 7:1, 384 heads),\nYi-1.5-9B (GQA 8:1, 192 heads),\nLlama-3.1-8B (GQA 4:1, 256 heads),\nMistral-7B-v0.3 (GQA 4:1, 256 heads),\nand Gemma-2-9B (GQA 2:1, 336 heads).\nWe additionally profile Qwen2.5-72B (640 heads) without full evaluation.\nAll experiments use WikiText-2 for calibration and evaluation unless noted; budget is 0.25 (4$\\times$ compression).\n\n%% ---- 4.2 Cross-Architecture Profiling ----\n\\subsection{Cross-Architecture Sensitivity Profiling}\n\\label{sec:profiling}\n\nTable~\\ref{tab:profiling} summarizes per-head sensitivity profiling across all models. The metrics are: \\emph{top-5\\% concentration} (fraction of total $\\delta$ in the top 5\\% of heads) and $t_1/t_5$ (ratio of the single largest $\\delta$ to the 5th-largest, measuring spike vs.\\ spread).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccl}\n\\toprule\n\\textbf{Model} & \\textbf{Heads} & \\textbf{Conc.} & $t_1/t_5$ & \\textbf{L0 dom.} & \\textbf{Shape} \\\\\n\\midrule\nQwen2.5-7B  & 112 & 0.61 & 0.57 & 26$\\times$ & Spread \\\\\nQwen2.5-14B & 384 & 0.55 & 0.63 & 8.2$\\times$ & Diluted \\\\\nQwen2.5-72B & 640 & 0.48 & 0.69 & 5.1$\\times$ & Borderline \\\\\nYi-1.5-9B   & 192 & 0.71 & 0.90 & --- & Spike \\\\\nLlama-3.1-8B & 256 & 0.57 & 0.71 & --- & Spike \\\\\nMistral-7B  & 256 & 0.24 & 0.18 & --- & Flat \\\\\nGemma-2-9B  & 336 & 0.23 & 0.38 & --- & Flat \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-head sensitivity profiling summary. ``Conc.'' = top-5\\% concentration. L0 dominance ratio is the ratio of the top-1 head $\\delta$ to the median.}\n\\label{tab:profiling}\n\\end{table}\n\n\\paragraph{Qwen Family Scaling.}\nWithin the Qwen family, concentration decreases monotonically with model size: 7B (0.61) $\\to$ 14B (0.55) $\\to$ 72B (0.48). The 14B model has 48 layers distributing sensitivity more uniformly; its Layer~0 heads account for only 41\\% of total $\\delta$ (vs.\\ 58.6\\% in 7B). The 72B falls below the 0.50 concentration threshold entirely, suggesting the ``spread'' pattern is a small-model artifact within this family.\n\n%% ---- 4.3 Main Results: Constrained Allocation ----\n\\subsection{Main Results: Constrained vs.\\ Uniform}\n\\label{sec:main_results}\n\nTable~\\ref{tab:main} reports the core comparison: constrained MCKP vs.\\ uniform 4-bit across all six evaluated models.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccr}\n\\toprule\n\\textbf{Model} & \\textbf{BF16} & \\textbf{Unif.\\ 4b} & \\textbf{Constr.} & \\textbf{$\\Delta$(\\%)} \\\\\n\\midrule\nQwen2.5-7B   & 5.84 & 15.45 & 11.23 & +27.3 \\\\\nQwen2.5-14B  & 5.84 &  7.02 &  6.94 & +1.2 \\\\\nYi-1.5-9B    & ---  &  7.22 &  7.22 & $\\approx$0 \\\\\nLlama-3.1-8B & 8.09 &  8.47 &  8.45 & +0.2 \\\\\nMistral-7B   & 7.04 &  7.13 &  7.16 & $-$0.4 \\\\\nGemma-2-9B   & 6.03 &  6.17 &  6.22 & $-$0.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Constrained MCKP vs.\\ uniform 4-bit (budget=0.25). $\\Delta$(\\%) = (uniform$-$MCKP)/uniform $\\times$ 100; positive = MCKP better.}\n\\label{tab:main}\n\\end{table}\n\nOnly Qwen2.5-7B shows meaningful improvement (+27.3\\%). The remaining five models range from +1.2\\% (Qwen2.5-14B, within noise) to $-$0.8\\% (Gemma-2, slightly worse). Notably, Qwen2.5-14B---same architecture family as the 7B with identical GQA ratio---gains only 1.2\\%, a false positive for any diagnostic predicting benefit from profiling metrics alone.\n\n\\paragraph{Llama-3.1-8B.}\nConstrained MCKP selects only $k{=}2$ heads for 2-bit (the constraint never binds at $k{=}8$). PPL 8.45 vs.\\ uniform 8.47: +0.2\\% improvement, within noise. The borderline $t_1/t_5 = 0.71$ places Llama exactly at the spike/spread boundary.\n\n\\paragraph{Mistral-7B.}\nThe cleanest negative case: concentration 0.24 (far below 0.50), profiler signal near zero. Constrained MCKP at $k{=}4$ yields PPL 7.16 vs.\\ uniform 7.13: the solver's 2-bit assignments actively hurt ($-$0.4\\%). The $k$-ablation is monotonically increasing---every additional 2-bit head degrades quality.\n\n\\paragraph{Gemma-2-9B (BOS-corrected).}\nAfter correcting a BOS-token evaluation bug, the unconstrained degradation ratio drops from 1.47$\\times$ to 1.22$\\times$, collapsing the previously reported ``moderate'' tier. Constrained vs.\\ uniform: $-$0.8\\%, confirming no benefit.\n\n%% ---- 4.4 Unconstrained Catastrophe ----\n\\subsection{Unconstrained Allocation Failure}\n\\label{sec:unconstrained}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Unif.} & \\textbf{Unconstr.} & \\textbf{Ratio} & \\textbf{2b heads} \\\\\n\\midrule\nQwen2.5-7B  & 15.45 & 36.92 & 3.31$\\times$ & 68/112 \\\\\nQwen2.5-14B &  7.02 &  8.41 & 1.44$\\times$ & --- \\\\\nLlama-3.1-8B & 8.47 &  8.63 & 1.07$\\times$ & 12/256 \\\\\nMistral-7B  &  7.13 &  7.57 & 1.08$\\times$ & 42/256 \\\\\nGemma-2-9B  &  6.17 &  7.38 & 1.22$\\times$ & 106/336 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Unconstrained allocation vs.\\ uniform. ``Ratio'' = unconstrained PPL / uniform PPL. In all cases unconstrained $\\leq$ uniform.}\n\\label{tab:unconstrained}\n\\end{table}\n\nTable~\\ref{tab:unconstrained} shows that unconstrained allocation \\emph{never outperforms uniform}. The degradation ranges from catastrophic (Qwen 3.31$\\times$) to mild (Llama 1.07$\\times$). The cardinality constraint addresses all cases: on Qwen it prevents catastrophe; on others it reduces 2-bit head count to where over-allocation cannot accumulate.\n\nAfter the BOS evaluation fix, the three-tier degradation gradient collapses to two tiers: catastrophic (Qwen2.5-7B, 3.31$\\times$) and mild (all others, 1.07--1.22$\\times$). The previously ``moderate'' Gemma-2 (1.47$\\times$) drops to 1.22$\\times$, within the mild range.\n\n%% ---- 4.5 Compounding Effect ----\n\\subsection{Compounding Effect Characterization}\n\\label{sec:compounding}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{rrrr}\n\\toprule\n\\textbf{max\\_2bit $k$} & \\textbf{PPL} & \\textbf{$\\Delta$ vs.\\ $k{=}8$} \\\\\n\\midrule\n0  & 15.45 & +37.6\\% \\\\\n4  & 11.93 & +6.2\\% \\\\\n8  & 11.23 & baseline \\\\\n12 & 11.21 & $-$0.2\\% \\\\\n16 & 11.52 & +2.6\\% \\\\\n24 & 13.07 & +16.4\\% \\\\\n48 & 19.84 & +76.7\\% \\\\\n112 & 36.92 & +228.8\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Compounding sweep on Qwen2.5-7B (budget=0.25). PPL vs.\\ max 2-bit heads $k$ shows a U-shape with optimum at $k \\approx 8$--10.}\n\\label{tab:compounding}\n\\end{table}\n\nTable~\\ref{tab:compounding} presents the compounding sweep on Qwen2.5-7B. The PPL--$k$ curve is U-shaped: too few 2-bit heads wastes budget on unnecessary higher precision ($k{=}0$ is uniform 4-bit, PPL 15.45); too many triggers super-additive compounding ($k{=}112$ is unconstrained, PPL 36.92). The elbow at $k \\approx 8$ corresponds to the number of heads in the Layer-0 cluster.\n\n\\paragraph{Super-Additivity Analysis.}\nTable~\\ref{tab:w9} compares top-$k$ (sensitivity-ranked) vs.\\ random-$k$ 2-bit assignments. The random/top-$k$ PPL ratio exceeds 1.0 at all $k > 1$, confirming super-additive interaction. However, the ratio is non-monotonic (1.76 at $k{=}8$, dropping to 1.24 at $k{=}16$, then 1.58 at $k{=}32$) with substantial variance at higher $k$ (std up to 9.73 at $k{=}64$). We report this as an empirical trend rather than a formal super-additivity claim.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{rrrrc}\n\\toprule\n$k$ & \\textbf{Top-$k$} & \\textbf{Rand-$k$} & \\textbf{Ratio} & \\textbf{Mono.} \\\\\n\\midrule\n1  &  9.83 &  9.89 $\\pm$ 0.05 & 1.00 & --- \\\\\n4  &  9.85 & 10.06 $\\pm$ 0.06 & 1.24 & $\\uparrow$ \\\\\n8  & 10.04 & 11.07 $\\pm$ 0.69 & 1.76 & $\\uparrow$ \\\\\n16 & 10.42 & 12.91 $\\pm$ 0.40 & 1.24 & $\\downarrow$ \\\\\n32 & 11.60 & 18.33 $\\pm$ 2.53 & 1.58 & $\\uparrow$ \\\\\n64 & 22.95 & 55.94 $\\pm$ 9.73 & 1.45 & $\\downarrow$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Top-$k$ vs.\\ random-$k$ 2-bit assignment (Qwen2.5-7B). Ratio = random PPL / top-$k$ PPL. Non-monotonic but consistently $>$1.}\n\\label{tab:w9}\n\\end{table}\n\n%% ---- 4.6 Solver Equivalence ----\n\\subsection{Solver Equivalence Under Constraint}\n\\label{sec:solver}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & \\textbf{Unconstr.\\ PPL} & \\textbf{Constr.\\ $k{=}8$} \\\\\n\\midrule\nRateQuant Greedy & 32.45 & 11.23 \\\\\nMCKP             & 36.92 & 11.23 \\\\\nUniform 4-bit    & ---   & 15.45 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Solver comparison (Qwen2.5-7B, budget=0.25). Constrained greedy = constrained MCKP ($\\Delta$=0.0012).}\n\\label{tab:solver}\n\\end{table}\n\nTable~\\ref{tab:solver} demonstrates that under the cardinality constraint, solver choice is irrelevant. Both greedy and MCKP produce identical allocations (bit distribution: \\{8:4, 4:100, 2:8\\}) with PPL difference of 0.0012. Without the constraint, both fail catastrophically but differently (greedy 32.45 vs.\\ MCKP 36.92). The constraint is the contribution, not the solver.\n\n\\paragraph{Near-Optimality.}\nOn layer subgroups of Qwen2.5-7B, brute-force oracle search shows constrained MCKP is near-optimal: maximum gap 0.0183 PPL, average gap 0.0046. MCKP is exactly optimal on 5 of 8 layer groups; the remaining gaps arise from position swaps of 2-bit heads within identical bit budgets.\n\n%% ---- 4.7 Budget Sweep ----\n\\subsection{Compression Ratio Sweep}\n\\label{sec:budget}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Compression} & \\textbf{Uniform} & \\textbf{MCKP} & \\textbf{Improv.} \\\\\n\\midrule\n2$\\times$ (0.50) & 10.07 &  9.89 & +1.8\\% \\\\\n4$\\times$ (0.25) & 15.45 & 11.23 & +27.3\\% \\\\\n8$\\times$ (0.125) & 2644 & 42.6 & +98.4\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Budget sweep on Qwen2.5-7B. Benefit increases with compression aggressiveness.}\n\\label{tab:budget}\n\\end{table}\n\nTable~\\ref{tab:budget} shows that the cardinality-constrained approach scales with compression aggressiveness. At 2$\\times$ (mild compression), the benefit is marginal (+1.8\\%). At 8$\\times$ (extreme), uniform assignment (all 2-bit) is catastrophic (PPL 2644) while constrained MCKP protects critical heads (PPL 42.6).\n\n%% ---- 4.8 Systematic Negative Result ----\n\\subsection{Systematic Negative Result: 5/6 Models}\n\\label{sec:negative}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{llccccccc}\n\\toprule\n\\textbf{Model} & \\textbf{Shape} & \\textbf{Conc.} & $t_1/t_5$ & \\textbf{MCKP vs.\\ Unif.\\ (\\%)} & \\textbf{Down.\\ $\\Delta$pp} & \\textbf{Benefit?} \\\\\n\\midrule\nQwen2.5-7B  & Spread         & 0.61 & 0.57 & +27.3 & +2.60 & \\checkmark \\\\\nQwen2.5-14B & Diluted Spread & 0.55 & 0.63 & +1.2  & +0.1 (noise)  & $\\times$ \\\\\nYi-1.5-9B   & Spike          & 0.71 & 0.90 & $\\approx$0 & $-$0.77 & $\\times$ \\\\\nLlama-3.1-8B & Spike         & 0.57 & 0.71 & +0.2  & $-$0.99 & $\\times$ \\\\\nMistral-7B  & Flat           & 0.24 & 0.18 & $-$0.4 & $-$0.48 & $\\times$ \\\\\nGemma-2-9B  & Flat           & 0.23 & 0.38 & $-$0.3 & +0.14 (noise) & $\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-architecture summary. Only Qwen2.5-7B benefits from constrained non-uniform allocation at both PPL and downstream task levels. ``Down.\\ $\\Delta$pp'' is average downstream accuracy change (MCKP $-$ uniform) across 4--5 tasks.}\n\\label{tab:negative}\n\\end{table*}\n\nTable~\\ref{tab:negative} presents the central negative finding: 5 of 6 models show no meaningful benefit from non-uniform allocation.\nQwen2.5-14B is particularly instructive: it shares the same architecture family and GQA ratio (7:1) as the successful 7B, and its profiling metrics border on the ``spread'' pattern (concentration 0.55, $t_1/t_5$ = 0.63). Yet its 384 heads dilute per-head sensitivity to the point where MCKP cannot exploit heterogeneity---improvement is only 1.2\\% (PPL 6.94 vs.\\ 7.02), and downstream accuracy shows $+$0.1pp (noise).\n\nThis negative result is practically valuable: it saves practitioners the overhead of profiling, solver optimization, and mixed-precision kernel dispatch on the majority of architectures.\n\n%% ---- 4.9 Downstream ----\n\\subsection{Downstream Task Evaluation}\n\\label{sec:downstream}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Task} & \\textbf{Unif.} & \\textbf{MCKP} & $\\Delta$\\textbf{pp} & \\textbf{BF16} \\\\\n\\midrule\n\\multicolumn{5}{c}{\\emph{Qwen2.5-7B (Spread)}} \\\\\nARC-C     & 0.481 & 0.514 & +3.16 & 0.529 \\\\\nHellaSwag & 0.728 & 0.768 & +4.00 & 0.783 \\\\\nPIQA      & 0.766 & 0.779 & +1.25 & 0.793 \\\\\nWinoGr.   & 0.662 & 0.682 & +1.97 & 0.690 \\\\\n\\textbf{Avg recov.} & --- & --- & \\textbf{72.8\\%} & --- \\\\\n\\midrule\n\\multicolumn{5}{c}{\\emph{Yi-1.5-9B (Spike): avg $-$0.77pp}} \\\\\n\\multicolumn{5}{c}{\\emph{Llama-3.1-8B (Spike): avg $-$0.99pp}} \\\\\n\\multicolumn{5}{c}{\\emph{Mistral-7B (Flat): avg $-$0.48pp}} \\\\\n\\multicolumn{5}{c}{\\emph{Gemma-2-9B (Flat): avg $+$0.14pp (noise)}} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Downstream evaluation (0-shot). Qwen2.5-7B shows consistent gains; four non-Spread models show minor degradation or noise.}\n\\label{tab:downstream}\n\\end{table}\n\nTable~\\ref{tab:downstream} confirms that PPL results translate to downstream tasks.\nQwen2.5-7B achieves +1.25 to +4.00pp improvement across four tasks with 72.8\\% average recovery of the bf16--uniform gap.\nAcross four non-Spread architectures, constrained MCKP shows minor average degradation vs.\\ uniform (Yi $-$0.77pp, Llama $-$0.99pp, Mistral $-$0.48pp, Gemma-2 $+$0.14pp noise).\nPer-task variation ranges from $+$1.27pp (Yi, WinoGrande) to $-$3.24pp (Yi, ARC-Challenge).\nARC-Challenge shows the largest per-task sensitivity across models, consistent with its reliance on multi-step reasoning where subtle KV cache errors may accumulate.\n\n\\paragraph{Qwen2.5-14B Downstream.}\nPredicted downstream results for the 14B false positive: average $\\Delta$ = $+$0.1pp (ARC-C $-$0.5pp, HellaSwag $+$0.3pp, PIQA $+$0.1pp, WinoGrande $-$0.2pp). Consistent with PPL: no meaningful benefit.\n\n%% ---- 4.10 Ablations ----\n\\subsection{Ablation Studies}\n\n\\paragraph{L0 Auto-Discovery.}\nWithout an explicit Layer-0 exclusion constraint, the solver's behavior depends on L0 dominance. On Qwen2.5-7B (L0 dominance 26$\\times$), the solver auto-discovers all 4 L0 heads for 8-bit assignment ($k{=}8$ total, PPL 11.23 unchanged). On Qwen2.5-14B (L0 dominance 8.2$\\times$), only 2 of 8 L0 heads receive 8-bit (PPL 6.97 vs.\\ constrained 6.94)---partial auto-discovery.\n\n\\paragraph{High-Resolution Profiling.}\nIncreasing profiling resolution from 16$\\times$512 to 64$\\times$2048 on Qwen2.5-7B discovers more non-zero heads (100 vs.\\ 37) and improves constrained PPL from 11.23 to 10.91 (+2.8\\%). However, profiling time increases 6$\\times$ (10~min to 65.5~min). On non-Spread models the improvement is negligible.\n\n\\paragraph{K/V Separation.}\nTreating K and V heads as independent MCKP items on Qwen2.5-7B yields PPL 11.22 (V all 4-bit, K has 16 heads at 2-bit)---slightly worse than joint optimization (10.91, $\\Delta$=0.31). K-only aggressive quantization causes more compounding than joint allocation.\n\n\\paragraph{L0-Only Heuristic.}\nA simple heuristic (Layer-0 heads at 8-bit, remaining heads randomly assigned to 2-bit subject to budget) achieves median PPL 11.52 on Qwen2.5-7B vs.\\ MCKP 10.91 (gap 5.6\\%). On non-Spread models (Llama median 10.04, Mistral median 7.59), the heuristic is substantially worse than both MCKP and uniform---confirming that the solver's precise head selection matters even under the constraint.\n\n%% ---- 4.11 Robustness ----\n\\subsection{Robustness}\n\n\\paragraph{Cross-Dataset Calibration.}\nAllocation agreement between C4-calibrated and WikiText-2-calibrated profiles is $>$96\\% for all 7--9B models (Qwen 96.4\\%, Llama 97.7\\%, Mistral 96.5\\%). C4-calibrated allocation evaluated on WikiText-2 yields identical PPL to WikiText-2-calibrated (11.29 for Qwen2.5-7B). Cross-domain evaluation (calibrate WikiText-2, evaluate C4) shows MCKP PPL 20.56 vs.\\ uniform 35.42---the allocation transfers robustly.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{Agreement} & \\textbf{Heads} \\\\\n\\midrule\nQwen2.5-7B  & 96.4\\% & 108/112 \\\\\nLlama-3.1-8B & 97.7\\% & 250/256 \\\\\nMistral-7B   & 96.5\\% & 247/256 \\\\\nQwen2.5-14B (est.) & $\\sim$88\\% & $\\sim$338/384 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-calibration agreement (C4 vs.\\ WikiText-2).}\n\\label{tab:crosscal}\n\\end{table}\n\n\\paragraph{Multi-Seed Stability.}\nThree calibration seeds on Qwen2.5-7B yield PPL 10.99$\\pm$0.065 (seeds: 11.02, 10.90, 11.05). The bit distribution is identical across seeds (\\{2:8, 4:100, 8:4\\}), and head-level allocation agreement is 90.2\\%. The 95\\% CI [10.86, 11.12] is far from the uniform baseline (15.45), confirming the Qwen2.5-7B result is robust to calibration variation.\n\n\\paragraph{Runtime Overhead.}\nMixed-precision MCKP inference on Qwen2.5-7B incurs 8.5\\% latency overhead vs.\\ uniform 4-bit (decode: 46.09 vs.\\ 42.46 ms/token; throughput: 21.8 vs.\\ 23.6 tok/s) due to per-head dequantization dispatch. Memory footprint is identical (5.25~MB KV cache). The MCKP solver itself runs in 5~ms. This overhead is justified only when the PPL improvement is meaningful (i.e., on Spread-pattern models).\n\n%% ============================================================\n%% 5  ANALYSIS\n%% ============================================================\n\\section{Analysis}\n\n\\paragraph{Why Does the Constraint Work Universally?}\nThe cardinality constraint is effective because unconstrained solvers systematically \\emph{over-allocate} 2-bit heads. On Spread models (Qwen2.5-7B), this triggers catastrophic compounding. On Flat models (Gemma-2), the solver assigns 31.5\\% of heads to 2-bit because per-head distortions are indistinguishable---the constraint reduces this to 2.4\\% (8/336). On Spike models (Yi-1.5), few heads are assigned 2-bit naturally ($\\sim$11.5\\%), so the constraint rarely binds but provides a safety floor.\n\n\\paragraph{Why Does Scaling Dilute Benefit?}\nThe Qwen family demonstrates a clear scaling trend: as model size increases from 7B to 14B to 72B, concentration decreases (0.61 $\\to$ 0.55 $\\to$ 0.48) and L0 dominance weakens (26$\\times$ $\\to$ 8.2$\\times$ $\\to$ 5.1$\\times$). More layers distribute sensitivity more uniformly, reducing the heterogeneity that MCKP exploits. This suggests that the benefit of non-uniform allocation diminishes for larger models---precisely the regime practitioners care most about.\n\n\\paragraph{Diagnostic Limitations.}\nA joint condition (concentration $\\gtrsim$0.50 AND $t_1/t_5 \\lesssim$0.70) correctly classifies 5 of 6 models. The false positive is Qwen2.5-14B, which passes both thresholds marginally (0.55, 0.63) but gains only 1.2\\%. The diagnostic lacks a third dimension (total head count or layer count) that would capture the dilution effect, but $N{=}6$ models is insufficient to fit a higher-dimensional boundary. We present this as a descriptive observation, not a validated diagnostic.\n\n%% ============================================================\n%% 6  CONCLUSION\n%% ============================================================\n\\section{Conclusion}\n\nWe present a systematic study of per-head mixed-precision KV cache quantization across six architectures and find three results.\nFirst, a cardinality constraint on the number of 2-bit heads is an architecture-agnostic safeguard: it prevents catastrophic compounding where it occurs and is harmless elsewhere, while making solver choice irrelevant.\nSecond, non-uniform allocation benefits only 1 of 6 tested models at standard 4$\\times$ compression---a systematic negative result that challenges the assumption of universal mixed-precision benefit and can save practitioners significant implementation effort.\nThird, we characterize the compounding effect on hardware-aligned bit-widths, showing the U-shaped PPL--$k$ curve that motivates and parameterizes the constraint.\n\n\\paragraph{Limitations.}\nOur study covers six architectures, which provides directional evidence but is insufficient for statistical claims.\nThe single positive case (Qwen2.5-7B) limits the generalizability of our ``when it helps'' analysis.\nWe do not evaluate KV cache eviction strategies or attention-sink-aware allocation.\nMulti-seed confidence intervals are available only for Qwen2.5-7B; other models report single-seed results.\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{9}\n\n\\bibitem[\\protect\\citename{RateQuant}2026]{ratequant2026}\nAnonymous.\n\\newblock 2026.\n\\newblock {RateQuant: Rate-Distortion Optimal KV Cache Quantization}.\n\\newblock In \\emph{Proceedings of ICML 2026}.\n\n\\bibitem[\\protect\\citename{KIVI}2024]{kivi2024}\nZirui Liu, Jiayi Yuan, Hongye Jin, Shaochen Zhong, Zhaozhuo Xu, Vladimir Braverman, Beidi Chen, and Xia Hu.\n\\newblock 2024.\n\\newblock {KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache}.\n\\newblock In \\emph{Proceedings of ICML 2024}.\n\n\\bibitem[\\protect\\citename{KVQuant}2024]{kvquant2024}\nColeman Hooper, Sehoon Kim, Hiva Mohammadzadeh, Michael W.\\ Mahoney, Yakun Sophia Shao, Kurt Keutzer, and Amir Gholami.\n\\newblock 2024.\n\\newblock {KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization}.\n\\newblock \\emph{arXiv preprint arXiv:2401.18079}.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b62b381a-1ed4-47d8-bba2-e1fa499e0c82",
  "isSidechain": false,
  "requestId": "req_011Cb49p9KJd8xdrK6JRvKHs",
  "type": "assistant",
  "uuid": "0fb410f7-17b5-4ead-9251-e4046bb5b74c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Wgtjvfz9toTm23wUN8xY9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 965,
      "cache_read_input_tokens": 54819,
      "output_tokens": 10927,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 965,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10927,
          "cache_read_input_tokens": 54819,
          "cache_creation_input_tokens": 965,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 965
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

_source line 22 · 2026-05-15T10:00:19.253Z_

<details><summary>↩ Tool result · `toolu_01PVYABphHwosyxrHVXsZRa6`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0fb410f7-17b5-4ead-9251-e4046bb5b74c",
  "isSidechain": false,
  "promptId": "e8e8fea0-d6a9-4b91-8885-3140c3cbe799",
  "type": "user",
  "uuid": "d1d0c218-7143-4cfa-87bd-7a8296c21c0a",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/worst/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{tablefootnote}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\n\\newcommand{\\ttt}[1]{\\texttt{#1}}\n\\newcommand{\\ppl}{\\text{PPL}}\n\n\\title{The Cardinality Constraint You Need for\\\\Hardware-Aligned KV Cache Quantization}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n%% ============================================================\n%% ABSTRACT\n%% ============================================================\n\\begin{abstract}\nPer-head mixed-precision KV cache quantization promises better quality--compression trade-offs than uniform bit-width assignment, yet we find it is beneficial in only one out of six architectures tested.\nWe conduct a systematic study across six models (Qwen2.5-7B/14B/72B, Yi-1.5-9B, Llama-3.1-8B, Mistral-7B, Gemma-2-9B) and identify three contributions.\n\\textbf{(1)}~A cardinality constraint---limiting the number of KV heads assigned to 2-bit precision---acts as a universal safeguard: it prevents catastrophic compounding on the one architecture where non-uniform allocation helps (Qwen2.5-7B: PPL 11.23 vs.\\ unconstrained 36.92) and is harmless ($\\leq$uniform) on all others.\nThe constraint further makes solver choice irrelevant: constrained greedy and constrained MCKP produce identical allocations ($\\Delta$=0.00).\n\\textbf{(2)}~We document a systematic negative result: across five of six architectures, constrained non-uniform allocation provides no meaningful improvement over uniform 4-bit quantization (range $-$0.8\\% to +1.2\\%), challenging the common assumption that mixed-precision KV cache quantization is universally beneficial.\n\\textbf{(3)}~We characterize the compounding effect on non-consecutive hardware-aligned bit-widths \\{2,4,8,16\\}: unconstrained solvers over-allocate 2-bit heads, and the resulting degradation is super-additive with a U-shaped PPL--$k$ curve whose elbow determines the optimal constraint parameter.\n\\end{abstract}\n\n%% ============================================================\n%% 1  INTRODUCTION\n%% ============================================================\n\\section{Introduction}\n\nKV cache quantization is a standard technique for reducing the memory footprint of autoregressive language model inference.\nMost deployed systems use uniform bit-width assignment---every KV head receives the same precision.\nAn appealing alternative is \\emph{mixed-precision} allocation, where a solver (greedy or MCKP) assigns per-head bit-widths to maximize quality under a total memory budget.\nPrior work such as RateQuant demonstrates that this is optimal for consecutive integer bit-widths \\{2,\\ldots,6\\} via polymatroid greedy~\\cite{ratequant2026}.\n\nHowever, modern hardware natively supports only \\emph{non-consecutive} bit-widths \\{2,4,8,16\\}.\nOn this action space, the polymatroid structure that guarantees greedy optimality breaks down.\nWe find that both unconstrained greedy (PPL~32.45) and unconstrained MCKP (PPL~36.92) fail catastrophically on Qwen2.5-7B compared to uniform 4-bit (PPL~15.45), producing allocations that are $2$--$3\\times$ worse than the baseline they are supposed to improve.\nOn the remaining five architectures, unconstrained allocation produces mild-to-moderate degradation ($1.07$--$1.22\\times$ baseline) but still never outperforms uniform.\n\nOur key finding is that a single, architecture-agnostic intervention---a \\emph{cardinality constraint} limiting the number of heads assigned to the most aggressive quantization level---is both necessary and sufficient:\n\\begin{itemize}\n\\item On the one architecture where mixed-precision helps (Qwen2.5-7B, ``spread'' sensitivity pattern), the constraint prevents compounding and achieves 27.3\\% PPL improvement over uniform.\n\\item On all other architectures, the constrained allocation matches or is within noise of uniform---it never hurts.\n\\item Under the constraint, solver choice is irrelevant: greedy and MCKP produce identical bit allocations and PPL ($\\Delta$=0.0012).\n\\end{itemize}\n\nBeyond the method, we document a \\emph{systematic negative result}: non-uniform KV cache quantization is beneficial in only 1 out of 6 architectures at standard 4$\\times$ compression.\nThis challenges the implicit assumption in prior work that per-head allocation is universally helpful, and provides practitioners with evidence that uniform 4-bit is sufficient for most models.\nWe also characterize the \\emph{compounding effect}---the mechanism by which per-head profiling distortions accumulate super-additively when many heads are simultaneously assigned extreme bit-widths---and show that the cardinality constraint directly addresses this mechanism.\n\n%% ============================================================\n%% 2  RELATED WORK\n%% ============================================================\n\\section{Related Work}\n\n\\paragraph{KV Cache Quantization.}\nKIVI~\\cite{kivi2024} and KVQuant~\\cite{kvquant2024} demonstrate that KV caches can be quantized to low precision with modest quality loss. These systems use uniform bit-width across all heads.\n\n\\paragraph{Per-Head Mixed Precision.}\nRateQuant~\\cite{ratequant2026} formulates per-head KV cache allocation as a rate--distortion optimization problem, proving greedy optimality on consecutive integer bit-widths via polymatroid structure (Proposition~6). Their continuous closed-form (Theorem~2) and discrete greedy (Algorithm~1) assume $\\{2,\\ldots,6\\}$. On hardware-aligned $\\{2,4,8,16\\}$, the polymatroid property does not hold, and their greedy produces suboptimal allocations. RateQuant acknowledges compounding effects (Appendix~M) but does not address them.\n\n\\paragraph{Quantization-Aware Allocation.}\nARKV and related methods use learned or heuristic per-head budgets. None systematically studies \\emph{when} non-uniform allocation is beneficial across architectures.\n\n%% ============================================================\n%% 3  METHOD\n%% ============================================================\n\\section{Method}\n\n\\subsection{Problem Formulation}\n\nGiven a model with $N$ KV heads, a set of hardware-aligned bit-widths $\\mathcal{B} = \\{2, 4, 8, 16\\}$, and a total memory budget $B$ (expressed as average bits per head), we seek an assignment $b_i \\in \\mathcal{B}$ for each head $i$ that minimizes perplexity subject to $\\frac{1}{N}\\sum_i b_i \\leq B$.\n\nWe formulate this as a Multiple-Choice Knapsack Problem (MCKP): each head $i$ is an item group with $|\\mathcal{B}|$ choices, the ``weight'' of choice $b$ for head $i$ is $b$, and the ``profit'' is the negative distortion $-\\delta_i(b)$ measured by per-head profiling.\n\n\\subsection{Per-Head Sensitivity Profiling}\n\nFor each head $i$ and bit-width $b \\in \\mathcal{B}$, we measure the distortion $\\delta_i(b)$: quantize only head $i$ to $b$-bit while keeping all other heads at 16-bit, and record the PPL change on a calibration set.\nWe use WikiText-2 with 16 sequences of 512 tokens (low-resolution) or 64 sequences of 2048 tokens (high-resolution).\n\n\\subsection{Cardinality Constraint}\n\nThe profiling procedure measures distortions \\emph{independently}: $\\delta_i(b)$ is the effect of quantizing head $i$ alone. When the solver assigns $k$ heads to 2-bit simultaneously, the joint distortion is not $\\sum_i \\delta_i(2)$ but empirically larger---a \\emph{compounding effect}. On non-consecutive bit-widths, this non-additivity is severe because the gap between 2-bit and 4-bit is large.\n\nWe introduce a cardinality constraint: $|\\{i : b_i = 2\\}| \\leq k$, limiting the number of heads at the most aggressive quantization level. This single parameter:\n\\begin{enumerate}\n\\item Prevents compounding by limiting simultaneous extreme assignments.\n\\item Reduces the feasible set sufficiently that solver choice is irrelevant.\n\\item Can be set via a small-scale sweep of $k$ vs.\\ PPL (Section~\\ref{sec:compounding}).\n\\end{enumerate}\n\n\\subsection{Solver Equivalence}\n\nUnder the cardinality constraint, the constrained MCKP feasible set is small enough that a simple greedy algorithm (assign 2-bit to the $k$ heads with highest $\\delta_i(2) - \\delta_i(4)$, then fill remaining budget optimally) produces the same allocation as full MCKP. We verify this empirically: on Qwen2.5-7B with $k{=}8$, greedy PPL = MCKP PPL = 11.23 ($\\Delta$=0.0012).\n\n%% ============================================================\n%% 4  EXPERIMENTS\n%% ============================================================\n\\section{Experiments}\n\n\\subsection{Setup}\n\nWe evaluate six models spanning diverse architectures and GQA configurations:\nQwen2.5-7B (GQA 7:1, 112 KV heads),\nQwen2.5-14B (GQA 7:1, 384 heads),\nYi-1.5-9B (GQA 8:1, 192 heads),\nLlama-3.1-8B (GQA 4:1, 256 heads),\nMistral-7B-v0.3 (GQA 4:1, 256 heads),\nand Gemma-2-9B (GQA 2:1, 336 heads).\nWe additionally profile Qwen2.5-72B (640 heads) without full evaluation.\nAll experiments use WikiText-2 for calibration and evaluation unless noted; budget is 0.25 (4$\\times$ compression).\n\n%% ---- 4.2 Cross-Architecture Profiling ----\n\\subsection{Cross-Architecture Sensitivity Profiling}\n\\label{sec:profiling}\n\nTable~\\ref{tab:profiling} summarizes per-head sensitivity profiling across all models. The metrics are: \\emph{top-5\\% concentration} (fraction of total $\\delta$ in the top 5\\% of heads) and $t_1/t_5$ (ratio of the single largest $\\delta$ to the 5th-largest, measuring spike vs.\\ spread).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccl}\n\\toprule\n\\textbf{Model} & \\textbf{Heads} & \\textbf{Conc.} & $t_1/t_5$ & \\textbf{L0 dom.} & \\textbf{Shape} \\\\\n\\midrule\nQwen2.5-7B  & 112 & 0.61 & 0.57 & 26$\\times$ & Spread \\\\\nQwen2.5-14B & 384 & 0.55 & 0.63 & 8.2$\\times$ & Diluted \\\\\nQwen2.5-72B & 640 & 0.48 & 0.69 & 5.1$\\times$ & Borderline \\\\\nYi-1.5-9B   & 192 & 0.71 & 0.90 & --- & Spike \\\\\nLlama-3.1-8B & 256 & 0.57 & 0.71 & --- & Spike \\\\\nMistral-7B  & 256 & 0.24 & 0.18 & --- & Flat \\\\\nGemma-2-9B  & 336 & 0.23 & 0.38 & --- & Flat \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-head sensitivity profiling summary. ``Conc.'' = top-5\\% concentration. L0 dominance ratio is the ratio of the top-1 head $\\delta$ to the median.}\n\\label{tab:profiling}\n\\end{table}\n\n\\paragraph{Qwen Family Scaling.}\nWithin the Qwen family, concentration decreases monotonically with model size: 7B (0.61) $\\to$ 14B (0.55) $\\to$ 72B (0.48). The 14B model has 48 layers distributing sensitivity more uniformly; its Layer~0 heads account for only 41\\% of total $\\delta$ (vs.\\ 58.6\\% in 7B). The 72B falls below the 0.50 concentration threshold entirely, suggesting the ``spread'' pattern is a small-model artifact within this family.\n\n%% ---- 4.3 Main Results: Constrained Allocation ----\n\\subsection{Main Results: Constrained vs.\\ Uniform}\n\\label{sec:main_results}\n\nTable~\\ref{tab:main} reports the core comparison: constrained MCKP vs.\\ uniform 4-bit across all six evaluated models.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccr}\n\\toprule\n\\textbf{Model} & \\textbf{BF16} & \\textbf{Unif.\\ 4b} & \\textbf{Constr.} & \\textbf{$\\Delta$(\\%)} \\\\\n\\midrule\nQwen2.5-7B   & 5.84 & 15.45 & 11.23 & +27.3 \\\\\nQwen2.5-14B  & 5.84 &  7.02 &  6.94 & +1.2 \\\\\nYi-1.5-9B    & ---  &  7.22 &  7.22 & $\\approx$0 \\\\\nLlama-3.1-8B & 8.09 &  8.47 &  8.45 & +0.2 \\\\\nMistral-7B   & 7.04 &  7.13 &  7.16 & $-$0.4 \\\\\nGemma-2-9B   & 6.03 &  6.17 &  6.22 & $-$0.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Constrained MCKP vs.\\ uniform 4-bit (budget=0.25). $\\Delta$(\\%) = (uniform$-$MCKP)/uniform $\\times$ 100; positive = MCKP better.}\n\\label{tab:main}\n\\end{table}\n\nOnly Qwen2.5-7B shows meaningful improvement (+27.3\\%). The remaining five models range from +1.2\\% (Qwen2.5-14B, within noise) to $-$0.8\\% (Gemma-2, slightly worse). Notably, Qwen2.5-14B---same architecture family as the 7B with identical GQA ratio---gains only 1.2\\%, a false positive for any diagnostic predicting benefit from profiling metrics alone.\n\n\\paragraph{Llama-3.1-8B.}\nConstrained MCKP selects only $k{=}2$ heads for 2-bit (the constraint never binds at $k{=}8$). PPL 8.45 vs.\\ uniform 8.47: +0.2\\% improvement, within noise. The borderline $t_1/t_5 = 0.71$ places Llama exactly at the spike/spread boundary.\n\n\\paragraph{Mistral-7B.}\nThe cleanest negative case: concentration 0.24 (far below 0.50), profiler signal near zero. Constrained MCKP at $k{=}4$ yields PPL 7.16 vs.\\ uniform 7.13: the solver's 2-bit assignments actively hurt ($-$0.4\\%). The $k$-ablation is monotonically increasing---every additional 2-bit head degrades quality.\n\n\\paragraph{Gemma-2-9B (BOS-corrected).}\nAfter correcting a BOS-token evaluation bug, the unconstrained degradation ratio drops from 1.47$\\times$ to 1.22$\\times$, collapsing the previously reported ``moderate'' tier. Constrained vs.\\ uniform: $-$0.8\\%, confirming no benefit.\n\n%% ---- 4.4 Unconstrained Catastrophe ----\n\\subsection{Unconstrained Allocation Failure}\n\\label{sec:unconstrained}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Unif.} & \\textbf{Unconstr.} & \\textbf{Ratio} & \\textbf{2b heads} \\\\\n\\midrule\nQwen2.5-7B  & 15.45 & 36.92 & 3.31$\\times$ & 68/112 \\\\\nQwen2.5-14B &  7.02 &  8.41 & 1.44$\\times$ & --- \\\\\nLlama-3.1-8B & 8.47 &  8.63 & 1.07$\\times$ & 12/256 \\\\\nMistral-7B  &  7.13 &  7.57 & 1.08$\\times$ & 42/256 \\\\\nGemma-2-9B  &  6.17 &  7.38 & 1.22$\\times$ & 106/336 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Unconstrained allocation vs.\\ uniform. ``Ratio'' = unconstrained PPL / uniform PPL. In all cases unconstrained $\\leq$ uniform.}\n\\label{tab:unconstrained}\n\\end{table}\n\nTable~\\ref{tab:unconstrained} shows that unconstrained allocation \\emph{never outperforms uniform}. The degradation ranges from catastrophic (Qwen 3.31$\\times$) to mild (Llama 1.07$\\times$). The cardinality constraint addresses all cases: on Qwen it prevents catastrophe; on others it reduces 2-bit head count to where over-allocation cannot accumulate.\n\nAfter the BOS evaluation fix, the three-tier degradation gradient collapses to two tiers: catastrophic (Qwen2.5-7B, 3.31$\\times$) and mild (all others, 1.07--1.22$\\times$). The previously ``moderate'' Gemma-2 (1.47$\\times$) drops to 1.22$\\times$, within the mild range.\n\n%% ---- 4.5 Compounding Effect ----\n\\subsection{Compounding Effect Characterization}\n\\label{sec:compounding}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{rrrr}\n\\toprule\n\\textbf{max\\_2bit $k$} & \\textbf{PPL} & \\textbf{$\\Delta$ vs.\\ $k{=}8$} \\\\\n\\midrule\n0  & 15.45 & +37.6\\% \\\\\n4  & 11.93 & +6.2\\% \\\\\n8  & 11.23 & baseline \\\\\n12 & 11.21 & $-$0.2\\% \\\\\n16 & 11.52 & +2.6\\% \\\\\n24 & 13.07 & +16.4\\% \\\\\n48 & 19.84 & +76.7\\% \\\\\n112 & 36.92 & +228.8\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Compounding sweep on Qwen2.5-7B (budget=0.25). PPL vs.\\ max 2-bit heads $k$ shows a U-shape with optimum at $k \\approx 8$--10.}\n\\label{tab:compounding}\n\\end{table}\n\nTable~\\ref{tab:compounding} presents the compounding sweep on Qwen2.5-7B. The PPL--$k$ curve is U-shaped: too few 2-bit heads wastes budget on unnecessary higher precision ($k{=}0$ is uniform 4-bit, PPL 15.45); too many triggers super-additive compounding ($k{=}112$ is unconstrained, PPL 36.92). The elbow at $k \\approx 8$ corresponds to the number of heads in the Layer-0 cluster.\n\n\\paragraph{Super-Additivity Analysis.}\nTable~\\ref{tab:w9} compares top-$k$ (sensitivity-ranked) vs.\\ random-$k$ 2-bit assignments. The random/top-$k$ PPL ratio exceeds 1.0 at all $k > 1$, confirming super-additive interaction. However, the ratio is non-monotonic (1.76 at $k{=}8$, dropping to 1.24 at $k{=}16$, then 1.58 at $k{=}32$) with substantial variance at higher $k$ (std up to 9.73 at $k{=}64$). We report this as an empirical trend rather than a formal super-additivity claim.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{rrrrc}\n\\toprule\n$k$ & \\textbf{Top-$k$} & \\textbf{Rand-$k$} & \\textbf{Ratio} & \\textbf{Mono.} \\\\\n\\midrule\n1  &  9.83 &  9.89 $\\pm$ 0.05 & 1.00 & --- \\\\\n4  &  9.85 & 10.06 $\\pm$ 0.06 & 1.24 & $\\uparrow$ \\\\\n8  & 10.04 & 11.07 $\\pm$ 0.69 & 1.76 & $\\uparrow$ \\\\\n16 & 10.42 & 12.91 $\\pm$ 0.40 & 1.24 & $\\downarrow$ \\\\\n32 & 11.60 & 18.33 $\\pm$ 2.53 & 1.58 & $\\uparrow$ \\\\\n64 & 22.95 & 55.94 $\\pm$ 9.73 & 1.45 & $\\downarrow$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Top-$k$ vs.\\ random-$k$ 2-bit assignment (Qwen2.5-7B). Ratio = random PPL / top-$k$ PPL. Non-monotonic but consistently $>$1.}\n\\label{tab:w9}\n\\end{table}\n\n%% ---- 4.6 Solver Equivalence ----\n\\subsection{Solver Equivalence Under Constraint}\n\\label{sec:solver}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & \\textbf{Unconstr.\\ PPL} & \\textbf{Constr.\\ $k{=}8$} \\\\\n\\midrule\nRateQuant Greedy & 32.45 & 11.23 \\\\\nMCKP             & 36.92 & 11.23 \\\\\nUniform 4-bit    & ---   & 15.45 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Solver comparison (Qwen2.5-7B, budget=0.25). Constrained greedy = constrained MCKP ($\\Delta$=0.0012).}\n\\label{tab:solver}\n\\end{table}\n\nTable~\\ref{tab:solver} demonstrates that under the cardinality constraint, solver choice is irrelevant. Both greedy and MCKP produce identical allocations (bit distribution: \\{8:4, 4:100, 2:8\\}) with PPL difference of 0.0012. Without the constraint, both fail catastrophically but differently (greedy 32.45 vs.\\ MCKP 36.92). The constraint is the contribution, not the solver.\n\n\\paragraph{Near-Optimality.}\nOn layer subgroups of Qwen2.5-7B, brute-force oracle search shows constrained MCKP is near-optimal: maximum gap 0.0183 PPL, average gap 0.0046. MCKP is exactly optimal on 5 of 8 layer groups; the remaining gaps arise from position swaps of 2-bit heads within identical bit budgets.\n\n%% ---- 4.7 Budget Sweep ----\n\\subsection{Compression Ratio Sweep}\n\\label{sec:budget}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Compression} & \\textbf{Uniform} & \\textbf{MCKP} & \\textbf{Improv.} \\\\\n\\midrule\n2$\\times$ (0.50) & 10.07 &  9.89 & +1.8\\% \\\\\n4$\\times$ (0.25) & 15.45 & 11.23 & +27.3\\% \\\\\n8$\\times$ (0.125) & 2644 & 42.6 & +98.4\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Budget sweep on Qwen2.5-7B. Benefit increases with compression aggressiveness.}\n\\label{tab:budget}\n\\end{table}\n\nTable~\\ref{tab:budget} shows that the cardinality-constrained approach scales with compression aggressiveness. At 2$\\times$ (mild compression), the benefit is marginal (+1.8\\%). At 8$\\times$ (extreme), uniform assignment (all 2-bit) is catastrophic (PPL 2644) while constrained MCKP protects critical heads (PPL 42.6).\n\n%% ---- 4.8 Systematic Negative Result ----\n\\subsection{Systematic Negative Result: 5/6 Models}\n\\label{sec:negative}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{llccccccc}\n\\toprule\n\\textbf{Model} & \\textbf{Shape} & \\textbf{Conc.} & $t_1/t_5$ & \\textbf{MCKP vs.\\ Unif.\\ (\\%)} & \\textbf{Down.\\ $\\Delta$pp} & \\textbf{Benefit?} \\\\\n\\midrule\nQwen2.5-7B  & Spread         & 0.61 & 0.57 & +27.3 & +2.60 & \\checkmark \\\\\nQwen2.5-14B & Diluted Spread & 0.55 & 0.63 & +1.2  & +0.1 (noise)  & $\\times$ \\\\\nYi-1.5-9B   & Spike          & 0.71 & 0.90 & $\\approx$0 & $-$0.77 & $\\times$ \\\\\nLlama-3.1-8B & Spike         & 0.57 & 0.71 & +0.2  & $-$0.99 & $\\times$ \\\\\nMistral-7B  & Flat           & 0.24 & 0.18 & $-$0.4 & $-$0.48 & $\\times$ \\\\\nGemma-2-9B  & Flat           & 0.23 & 0.38 & $-$0.3 & +0.14 (noise) & $\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-architecture summary. Only Qwen2.5-7B benefits from constrained non-uniform allocation at both PPL and downstream task levels. ``Down.\\ $\\Delta$pp'' is average downstream accuracy change (MCKP $-$ uniform) across 4--5 tasks.}\n\\label{tab:negative}\n\\end{table*}\n\nTable~\\ref{tab:negative} presents the central negative finding: 5 of 6 models show no meaningful benefit from non-uniform allocation.\nQwen2.5-14B is particularly instructive: it shares the same architecture family and GQA ratio (7:1) as the successful 7B, and its profiling metrics border on the ``spread'' pattern (concentration 0.55, $t_1/t_5$ = 0.63). Yet its 384 heads dilute per-head sensitivity to the point where MCKP cannot exploit heterogeneity---improvement is only 1.2\\% (PPL 6.94 vs.\\ 7.02), and downstream accuracy shows $+$0.1pp (noise).\n\nThis negative result is practically valuable: it saves practitioners the overhead of profiling, solver optimization, and mixed-precision kernel dispatch on the majority of architectures.\n\n%% ---- 4.9 Downstream ----\n\\subsection{Downstream Task Evaluation}\n\\label{sec:downstream}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Task} & \\textbf{Unif.} & \\textbf{MCKP} & $\\Delta$\\textbf{pp} & \\textbf{BF16} \\\\\n\\midrule\n\\multicolumn{5}{c}{\\emph{Qwen2.5-7B (Spread)}} \\\\\nARC-C     & 0.481 & 0.514 & +3.16 & 0.529 \\\\\nHellaSwag & 0.728 & 0.768 & +4.00 & 0.783 \\\\\nPIQA      & 0.766 & 0.779 & +1.25 & 0.793 \\\\\nWinoGr.   & 0.662 & 0.682 & +1.97 & 0.690 \\\\\n\\textbf{Avg recov.} & --- & --- & \\textbf{72.8\\%} & --- \\\\\n\\midrule\n\\multicolumn{5}{c}{\\emph{Yi-1.5-9B (Spike): avg $-$0.77pp}} \\\\\n\\multicolumn{5}{c}{\\emph{Llama-3.1-8B (Spike): avg $-$0.99pp}} \\\\\n\\multicolumn{5}{c}{\\emph{Mistral-7B (Flat): avg $-$0.48pp}} \\\\\n\\multicolumn{5}{c}{\\emph{Gemma-2-9B (Flat): avg $+$0.14pp (noise)}} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Downstream evaluation (0-shot). Qwen2.5-7B shows consistent gains; four non-Spread models show minor degradation or noise.}\n\\label{tab:downstream}\n\\end{table}\n\nTable~\\ref{tab:downstream} confirms that PPL results translate to downstream tasks.\nQwen2.5-7B achieves +1.25 to +4.00pp improvement across four tasks with 72.8\\% average recovery of the bf16--uniform gap.\nAcross four non-Spread architectures, constrained MCKP shows minor average degradation vs.\\ uniform (Yi $-$0.77pp, Llama $-$0.99pp, Mistral $-$0.48pp, Gemma-2 $+$0.14pp noise).\nPer-task variation ranges from $+$1.27pp (Yi, WinoGrande) to $-$3.24pp (Yi, ARC-Challenge).\nARC-Challenge shows the largest per-task sensitivity across models, consistent with its reliance on multi-step reasoning where subtle KV cache errors may accumulate.\n\n\\paragraph{Qwen2.5-14B Downstream.}\nPredicted downstream results for the 14B false positive: average $\\Delta$ = $+$0.1pp (ARC-C $-$0.5pp, HellaSwag $+$0.3pp, PIQA $+$0.1pp, WinoGrande $-$0.2pp). Consistent with PPL: no meaningful benefit.\n\n%% ---- 4.10 Ablations ----\n\\subsection{Ablation Studies}\n\n\\paragraph{L0 Auto-Discovery.}\nWithout an explicit Layer-0 exclusion constraint, the solver's behavior depends on L0 dominance. On Qwen2.5-7B (L0 dominance 26$\\times$), the solver auto-discovers all 4 L0 heads for 8-bit assignment ($k{=}8$ total, PPL 11.23 unchanged). On Qwen2.5-14B (L0 dominance 8.2$\\times$), only 2 of 8 L0 heads receive 8-bit (PPL 6.97 vs.\\ constrained 6.94)---partial auto-discovery.\n\n\\paragraph{High-Resolution Profiling.}\nIncreasing profiling resolution from 16$\\times$512 to 64$\\times$2048 on Qwen2.5-7B discovers more non-zero heads (100 vs.\\ 37) and improves constrained PPL from 11.23 to 10.91 (+2.8\\%). However, profiling time increases 6$\\times$ (10~min to 65.5~min). On non-Spread models the improvement is negligible.\n\n\\paragraph{K/V Separation.}\nTreating K and V heads as independent MCKP items on Qwen2.5-7B yields PPL 11.22 (V all 4-bit, K has 16 heads at 2-bit)---slightly worse than joint optimization (10.91, $\\Delta$=0.31). K-only aggressive quantization causes more compounding than joint allocation.\n\n\\paragraph{L0-Only Heuristic.}\nA simple heuristic (Layer-0 heads at 8-bit, remaining heads randomly assigned to 2-bit subject to budget) achieves median PPL 11.52 on Qwen2.5-7B vs.\\ MCKP 10.91 (gap 5.6\\%). On non-Spread models (Llama median 10.04, Mistral median 7.59), the heuristic is substantially worse than both MCKP and uniform---confirming that the solver's precise head selection matters even under the constraint.\n\n%% ---- 4.11 Robustness ----\n\\subsection{Robustness}\n\n\\paragraph{Cross-Dataset Calibration.}\nAllocation agreement between C4-calibrated and WikiText-2-calibrated profiles is $>$96\\% for all 7--9B models (Qwen 96.4\\%, Llama 97.7\\%, Mistral 96.5\\%). C4-calibrated allocation evaluated on WikiText-2 yields identical PPL to WikiText-2-calibrated (11.29 for Qwen2.5-7B). Cross-domain evaluation (calibrate WikiText-2, evaluate C4) shows MCKP PPL 20.56 vs.\\ uniform 35.42---the allocation transfers robustly.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{Agreement} & \\textbf{Heads} \\\\\n\\midrule\nQwen2.5-7B  & 96.4\\% & 108/112 \\\\\nLlama-3.1-8B & 97.7\\% & 250/256 \\\\\nMistral-7B   & 96.5\\% & 247/256 \\\\\nQwen2.5-14B (est.) & $\\sim$88\\% & $\\sim$338/384 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-calibration agreement (C4 vs.\\ WikiText-2).}\n\\label{tab:crosscal}\n\\end{table}\n\n\\paragraph{Multi-Seed Stability.}\nThree calibration seeds on Qwen2.5-7B yield PPL 10.99$\\pm$0.065 (seeds: 11.02, 10.90, 11.05). The bit distribution is identical across seeds (\\{2:8, 4:100, 8:4\\}), and head-level allocation agreement is 90.2\\%. The 95\\% CI [10.86, 11.12] is far from the uniform baseline (15.45), confirming the Qwen2.5-7B result is robust to calibration variation.\n\n\\paragraph{Runtime Overhead.}\nMixed-precision MCKP inference on Qwen2.5-7B incurs 8.5\\% latency overhead vs.\\ uniform 4-bit (decode: 46.09 vs.\\ 42.46 ms/token; throughput: 21.8 vs.\\ 23.6 tok/s) due to per-head dequantization dispatch. Memory footprint is identical (5.25~MB KV cache). The MCKP solver itself runs in 5~ms. This overhead is justified only when the PPL improvement is meaningful (i.e., on Spread-pattern models).\n\n%% ============================================================\n%% 5  ANALYSIS\n%% ============================================================\n\\section{Analysis}\n\n\\paragraph{Why Does the Constraint Work Universally?}\nThe cardinality constraint is effective because unconstrained solvers systematically \\emph{over-allocate} 2-bit heads. On Spread models (Qwen2.5-7B), this triggers catastrophic compounding. On Flat models (Gemma-2), the solver assigns 31.5\\% of heads to 2-bit because per-head distortions are indistinguishable---the constraint reduces this to 2.4\\% (8/336). On Spike models (Yi-1.5), few heads are assigned 2-bit naturally ($\\sim$11.5\\%), so the constraint rarely binds but provides a safety floor.\n\n\\paragraph{Why Does Scaling Dilute Benefit?}\nThe Qwen family demonstrates a clear scaling trend: as model size increases from 7B to 14B to 72B, concentration decreases (0.61 $\\to$ 0.55 $\\to$ 0.48) and L0 dominance weakens (26$\\times$ $\\to$ 8.2$\\times$ $\\to$ 5.1$\\times$). More layers distribute sensitivity more uniformly, reducing the heterogeneity that MCKP exploits. This suggests that the benefit of non-uniform allocation diminishes for larger models---precisely the regime practitioners care most about.\n\n\\paragraph{Diagnostic Limitations.}\nA joint condition (concentration $\\gtrsim$0.50 AND $t_1/t_5 \\lesssim$0.70) correctly classifies 5 of 6 models. The false positive is Qwen2.5-14B, which passes both thresholds marginally (0.55, 0.63) but gains only 1.2\\%. The diagnostic lacks a third dimension (total head count or layer count) that would capture the dilution effect, but $N{=}6$ models is insufficient to fit a higher-dimensional boundary. We present this as a descriptive observation, not a validated diagnostic.\n\n%% ============================================================\n%% 6  CONCLUSION\n%% ============================================================\n\\section{Conclusion}\n\nWe present a systematic study of per-head mixed-precision KV cache quantization across six architectures and find three results.\nFirst, a cardinality constraint on the number of 2-bit heads is an architecture-agnostic safeguard: it prevents catastrophic compounding where it occurs and is harmless elsewhere, while making solver choice irrelevant.\nSecond, non-uniform allocation benefits only 1 of 6 tested models at standard 4$\\times$ compression---a systematic negative result that challenges the assumption of universal mixed-precision benefit and can save practitioners significant implementation effort.\nThird, we characterize the compounding effect on hardware-aligned bit-widths, showing the U-shaped PPL--$k$ curve that motivates and parameterizes the constraint.\n\n\\paragraph{Limitations.}\nOur study covers six architectures, which provides directional evidence but is insufficient for statistical claims.\nThe single positive case (Qwen2.5-7B) limits the generalizability of our ``when it helps'' analysis.\nWe do not evaluate KV cache eviction strategies or attention-sink-aware allocation.\nMulti-seed confidence intervals are available only for Qwen2.5-7B; other models report single-seed results.\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{9}\n\n\\bibitem[\\protect\\citename{RateQuant}2026]{ratequant2026}\nAnonymous.\n\\newblock 2026.\n\\newblock {RateQuant: Rate-Distortion Optimal KV Cache Quantization}.\n\\newblock In \\emph{Proceedings of ICML 2026}.\n\n\\bibitem[\\protect\\citename{KIVI}2024]{kivi2024}\nZirui Liu, Jiayi Yuan, Hongye Jin, Shaochen Zhong, Zhaozhuo Xu, Vladimir Braverman, Beidi Chen, and Xia Hu.\n\\newblock 2024.\n\\newblock {KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache}.\n\\newblock In \\emph{Proceedings of ICML 2024}.\n\n\\bibitem[\\protect\\citename{KVQuant}2024]{kvquant2024}\nColeman Hooper, Sehoon Kim, Hiva Mohammadzadeh, Michael W.\\ Mahoney, Yakun Sophia Shao, Kurt Keutzer, and Amir Gholami.\n\\newblock 2024.\n\\newblock {KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization}.\n\\newblock \\emph{arXiv preprint arXiv:2401.18079}.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "0fb410f7-17b5-4ead-9251-e4046bb5b74c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T085855 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/…",
  "leafUuid": "d1d0c218-7143-4cfa-87bd-7a8296c21c0a",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier simulated paper for dream_20260515T085855",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8"
}
```

---

### Assistant

_source line 25 · 2026-05-15T10:00:23.128Z_

Now compile the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1d0c218-7143-4cfa-87bd-7a8296c21c0a",
  "isSidechain": false,
  "requestId": "req_011Cb4ADzMDw6VGxEciYZcv7",
  "type": "assistant",
  "uuid": "5c6c7b89-6b42-4ea2-aa99-1c50cf60bbcc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XFMD5M9y4rjbMVNaW3VtMN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10990,
      "cache_read_input_tokens": 55784,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10990,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 183,
          "cache_read_input_tokens": 55784,
          "cache_creation_input_tokens": 10990,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10990
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

_source line 26 · 2026-05-15T10:00:24.265Z_

<details open><summary>🔧 Tool call — Bash · `toolu_017igPsTG1y4A9jyXqBFMUK2`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c6c7b89-6b42-4ea2-aa99-1c50cf60bbcc",
  "isSidechain": false,
  "requestId": "req_011Cb4ADzMDw6VGxEciYZcv7",
  "type": "assistant",
  "uuid": "2092c1d7-ec3a-4cdf-b35a-fb5dfa2722f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XFMD5M9y4rjbMVNaW3VtMN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10990,
      "cache_read_input_tokens": 55784,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10990,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 183,
          "cache_read_input_tokens": 55784,
          "cache_creation_input_tokens": 10990,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10990
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

_source line 27 · 2026-05-15T10:00:24.417Z_

<details><summary>↩ Tool result · reported error · `toolu_017igPsTG1y4A9jyXqBFMUK2`</summary>

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
  "parentUuid": "2092c1d7-ec3a-4cdf-b35a-fb5dfa2722f6",
  "isSidechain": false,
  "promptId": "e8e8fea0-d6a9-4b91-8885-3140c3cbe799",
  "type": "user",
  "uuid": "b143307c-2085-4c62-afd5-bc38ccf0c28d",
  "toolUseResult": "Error: Exit code 1\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `acl.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
  "sourceToolAssistantUUID": "2092c1d7-ec3a-4cdf-b35a-fb5dfa2722f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-15T10:00:27.898Z_

<details><summary>Logged reasoning block</summary>

```text
The `acl.sty` is not available. Let me switch to a simpler document class setup that doesn't require `acl.sty`.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b143307c-2085-4c62-afd5-bc38ccf0c28d",
  "isSidechain": false,
  "requestId": "req_011Cb4AENN3eRG5sPfBuR3bn",
  "type": "assistant",
  "uuid": "d7857031-95a0-448c-98c0-f48cc13e26ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Heyzj4JgQmQTzZsN2KVcJd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 477,
      "cache_read_input_tokens": 66774,
      "output_tokens": 483,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 477,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 483,
          "cache_read_input_tokens": 66774,
          "cache_creation_input_tokens": 477,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 477
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

_source line 29 · 2026-05-15T10:00:28.358Z_

ACL style file not available. I'll switch to a standard article class.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7857031-95a0-448c-98c0-f48cc13e26ad",
  "isSidechain": false,
  "requestId": "req_011Cb4AENN3eRG5sPfBuR3bn",
  "type": "assistant",
  "uuid": "9e2f85d7-0b6a-4b37-a54a-ef40f8aab9dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Heyzj4JgQmQTzZsN2KVcJd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 477,
      "cache_read_input_tokens": 66774,
      "output_tokens": 483,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 477,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 483,
          "cache_read_input_tokens": 66774,
          "cache_creation_input_tokens": 477,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 477
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

_source line 30 · 2026-05-15T10:00:31.940Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01GQNHDsxV8x3h91fLDd4MVc`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/worst/paper.tex",
  "old_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{tablefootnote}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{natbib}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e2f85d7-0b6a-4b37-a54a-ef40f8aab9dc",
  "isSidechain": false,
  "requestId": "req_011Cb4AENN3eRG5sPfBuR3bn",
  "type": "assistant",
  "uuid": "5734ffb3-43ba-4dcf-89a4-8bb45d797b14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Heyzj4JgQmQTzZsN2KVcJd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 477,
      "cache_read_input_tokens": 66774,
      "output_tokens": 483,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 477,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 483,
          "cache_read_input_tokens": 66774,
          "cache_creation_input_tokens": 477,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 477
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

_source line 31 · 2026-05-15T10:00:31.965Z_

<details><summary>↩ Tool result · `toolu_01GQNHDsxV8x3h91fLDd4MVc`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/worst/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5734ffb3-43ba-4dcf-89a4-8bb45d797b14",
  "isSidechain": false,
  "promptId": "e8e8fea0-d6a9-4b91-8885-3140c3cbe799",
  "type": "user",
  "uuid": "49f09a1c-6ccc-4a2a-a4a2-a96637a3f5a2",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/worst/paper.tex",
    "oldString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{tablefootnote}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{natbib}",
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
          " \\usepackage{amsmath}"
        ]
      },
      {
        "oldStart": 8,
        "oldLines": 9,
        "newStart": 8,
        "newLines": 10,
        "lines": [
          " \\usepackage{multirow}",
          " \\usepackage{graphicx}",
          " \\usepackage{xcolor}",
          "-\\usepackage{tablefootnote}",
          "+\\usepackage{hyperref}",
          " \\usepackage[T1]{fontenc}",
          " \\usepackage[utf8]{inputenc}",
          "+\\usepackage{natbib}",
          " ",
          " \\newcommand{\\ttt}[1]{\\texttt{#1}}",
          " \\newcommand{\\ppl}{\\text{PPL}}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "5734ffb3-43ba-4dcf-89a4-8bb45d797b14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-15T10:00:31.997Z_

```json
{
  "parentUuid": "49f09a1c-6ccc-4a2a-a4a2-a96637a3f5a2",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "1076a737-6eef-4ed7-9968-47800039394b",
  "timestamp": "2026-05-15T10:00:31.997Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Tool call

_source line 33 · 2026-05-15T10:00:37.316Z_

<details open><summary>🔧 Tool call — Bash · `toolu_012JGhW2Qkfc3ak9o4YtHAPD`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "Compile LaTeX paper twice",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1076a737-6eef-4ed7-9968-47800039394b",
  "isSidechain": false,
  "requestId": "req_011Cb4AEvzLtncwzv1KF3kbY",
  "type": "assistant",
  "uuid": "a6d5e54e-0afa-4fa4-bd5e-1cc8e9568bf9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AXVadoMmhHHaPQTyLpt6k4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 670,
      "cache_read_input_tokens": 67251,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 670,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 67251,
          "cache_creation_input_tokens": 670,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 670
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

_source line 34 · 2026-05-15T10:00:37.823Z_

<details><summary>↩ Tool result · reported error · `toolu_012JGhW2Qkfc3ak9o4YtHAPD`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd))
(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
No file paper.aux.
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)

Package natbib Warning: Citation `ratequant2026' on page 1 undefined on input l
ine 46.

(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips
/base/8r.enc}]

Package natbib Warning: Citation `kivi2024' on page 2 undefined on input line 7
0.


Package natbib Warning: Citation `kvquant2024' on page 2 undefined on input lin
e 70.


Package natbib Warning: Citation `ratequant2026' on page 2 undefined on input l
ine 73.


Overfull \hbox (0.87076pt too wide) in paragraph at lines 73--74
 []\T1/ptm/b/n/10.95 Per-Head Mixed Pre-ci-sion.[] \T1/ptm/m/n/10.95 Rate-Quant
 \T1/ptm/b/n/10.95 ? \T1/ptm/m/n/10.95 for-mu-lates per-head KV cache al-lo-ca-
tion as a rate--distortion

LaTeX Warning: Reference `sec:compounding' on page 2 undefined on input line 10
2.

[2]

LaTeX Warning: Reference `tab:profiling' on page 3 undefined on input line 130.



LaTeX Warning: Reference `tab:main' on page 3 undefined on input line 159.

[3]
Overfull \hbox (7.39783pt too wide) in paragraph at lines 189--190
 []\T1/ptm/b/n/10.95 Gemma-2-9B (BOS-corrected).[] \T1/ptm/m/n/10.95 Af-ter cor
-rect-ing a BOS-token eval-u-a-tion bug, the un-con-strained degra-

LaTeX Warning: Reference `tab:unconstrained' on page 4 undefined on input line 
213.


LaTeX Warning: Reference `tab:compounding' on page 4 undefined on input line 24
2.


LaTeX Warning: Reference `tab:w9' on page 4 undefined on input line 245.

[4]

LaTeX Warning: Reference `tab:solver' on page 5 undefined on input line 286.


LaTeX Warning: Reference `tab:budget' on page 5 undefined on input line 311.


LaTeX Warning: Reference `tab:negative' on page 5 undefined on input line 336.

[5]

LaTeX Warning: Reference `tab:downstream' on page 6 undefined on input line 369
.

[6] [7]
No file paper.bbl.
Runaway argument?
\@nil {ratequant2026} Anonymous. \newblock 2026. \newblock {RateQuant\ETC.
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.462 
      
Runaway argument?
Jiayi Yuan, Hongye Jin, Shaochen Zhong, Zhaozhuo Xu, Vladimir Braverm\ETC.
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.468 
      
Runaway argument?
Sehoon Kim, Hiva Mohammadzadeh, Michael W.\ Mahoney, Yakun Sophia Sha\ETC.
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.474 
      
[8]

Package natbib Warning: There were undefined citations.

[9] (./paper.aux)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


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
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msam10.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/
texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (9 pages, 154498 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6d5e54e-0afa-4fa4-bd5e-1cc8e9568bf9",
  "isSidechain": false,
  "promptId": "e8e8fea0-d6a9-4b91-8885-3140c3cbe799",
  "type": "user",
  "uuid": "fa32575c-a749-492c-ac3e-00be310a96a8",
  "toolUseResult": "Error: Exit code 1\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `ratequant2026' on page 1 undefined on input l\nine 46.\n\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips\n/base/8r.enc}]\n\nPackage natbib Warning: Citation `kivi2024' on page 2 undefined on input line 7\n0.\n\n\nPackage natbib Warning: Citation `kvquant2024' on page 2 undefined on input lin\ne 70.\n\n\nPackage natbib Warning: Citation `ratequant2026' on page 2 undefined on input l\nine 73.\n\n\nOverfull \\hbox (0.87076pt too wide) in paragraph at lines 73--74\n []\\T1/ptm/b/n/10.95 Per-Head Mixed Pre-ci-sion.[] \\T1/ptm/m/n/10.95 Rate-Quant\n \\T1/ptm/b/n/10.95 ? \\T1/ptm/m/n/10.95 for-mu-lates per-head KV cache al-lo-ca-\ntion as a rate--distortion\n\nLaTeX Warning: Reference `sec:compounding' on page 2 undefined on input line 10\n2.\n\n[2]\n\nLaTeX Warning: Reference `tab:profiling' on page 3 undefined on input line 130.\n\n\n\nLaTeX Warning: Reference `tab:main' on page 3 undefined on input line 159.\n\n[3]\nOverfull \\hbox (7.39783pt too wide) in paragraph at lines 189--190\n []\\T1/ptm/b/n/10.95 Gemma-2-9B (BOS-corrected).[] \\T1/ptm/m/n/10.95 Af-ter cor\n-rect-ing a BOS-token eval-u-a-tion bug, the un-con-strained degra-\n\nLaTeX Warning: Reference `tab:unconstrained' on page 4 undefined on input line \n213.\n\n\nLaTeX Warning: Reference `tab:compounding' on page 4 undefined on input line 24\n2.\n\n\nLaTeX Warning: Reference `tab:w9' on page 4 undefined on input line 245.\n\n[4]\n\nLaTeX Warning: Reference `tab:solver' on page 5 undefined on input line 286.\n\n\nLaTeX Warning: Reference `tab:budget' on page 5 undefined on input line 311.\n\n\nLaTeX Warning: Reference `tab:negative' on page 5 undefined on input line 336.\n\n[5]\n\nLaTeX Warning: Reference `tab:downstream' on page 6 undefined on input line 369\n.\n\n[6] [7]\nNo file paper.bbl.\nRunaway argument?\n\\@nil {ratequant2026} Anonymous. \\newblock 2026. \\newblock {RateQuant\\ETC.\n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.462 \n      \nRunaway argument?\nJiayi Yuan, Hongye Jin, Shaochen Zhong, Zhaozhuo Xu, Vladimir Braverm\\ETC.\n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.468 \n      \nRunaway argument?\nSehoon Kim, Hiva Mohammadzadeh, Michael W.\\ Mahoney, Yakun Sophia Sha\\ETC.\n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.474 \n      \n[8]\n\nPackage natbib Warning: There were undefined citations.\n\n[9] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\n/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msam10.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/\ntexlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (9 pages, 154498 bytes).\nTranscript written on paper.log.",
  "sourceToolAssistantUUID": "a6d5e54e-0afa-4fa4-bd5e-1cc8e9568bf9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-15T10:00:44.073Z_

<details><summary>Logged reasoning block</summary>

```text
The first pass generated the PDF but with errors from the `\bibliography` command conflicting with the manual `thebibliography` environment, and natbib parsing issues with the manual bib entries. Let me fix the bibliography section - remove the `\bibliography{references}` and `\bibliographystyle` lines, and fix the natbib-compatible `thebibliography` format. The second pass failed because of these errors.

The exit code 1 is because of the natbib parsing errors. Let me fix the bibliography to be natbib-compatible.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa32575c-a749-492c-ac3e-00be310a96a8",
  "isSidechain": false,
  "requestId": "req_011Cb4AFMkMuKBZD1yASiXJ3",
  "type": "assistant",
  "uuid": "fa79e860-02c9-4026-bcb0-9a5330a6ea19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpRQWddBUzcDXPr5rcRe7C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3654,
      "cache_read_input_tokens": 67921,
      "output_tokens": 1020,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3654,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1020,
          "cache_read_input_tokens": 67921,
          "cache_creation_input_tokens": 3654,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3654
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

_source line 36 · 2026-05-15T10:00:44.584Z_

The PDF was generated (9 pages) but has bibliography formatting issues. Let me fix the natbib-compatible bibliography.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa79e860-02c9-4026-bcb0-9a5330a6ea19",
  "isSidechain": false,
  "requestId": "req_011Cb4AFMkMuKBZD1yASiXJ3",
  "type": "assistant",
  "uuid": "1e0e885b-3f61-4fd9-8a8b-6f881f1f8b02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpRQWddBUzcDXPr5rcRe7C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3654,
      "cache_read_input_tokens": 67921,
      "output_tokens": 1020,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3654,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1020,
          "cache_read_input_tokens": 67921,
          "cache_creation_input_tokens": 3654,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3654
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

_source line 37 · 2026-05-15T10:00:54.459Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01CM8HvPCM9t5UaLgbTf2pJh`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/worst/paper.tex",
  "old_string": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{9}\n\n\\bibitem[\\protect\\citename{RateQuant}2026]{ratequant2026}\nAnonymous.\n\\newblock 2026.\n\\newblock {RateQuant: Rate-Distortion Optimal KV Cache Quantization}.\n\\newblock In \\emph{Proceedings of ICML 2026}.\n\n\\bibitem[\\protect\\citename{KIVI}2024]{kivi2024}\nZirui Liu, Jiayi Yuan, Hongye Jin, Shaochen Zhong, Zhaozhuo Xu, Vladimir Braverman, Beidi Chen, and Xia Hu.\n\\newblock 2024.\n\\newblock {KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache}.\n\\newblock In \\emph{Proceedings of ICML 2024}.\n\n\\bibitem[\\protect\\citename{KVQuant}2024]{kvquant2024}\nColeman Hooper, Sehoon Kim, Hiva Mohammadzadeh, Michael W.\\ Mahoney, Yakun Sophia Shao, Kurt Keutzer, and Amir Gholami.\n\\newblock 2024.\n\\newblock {KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization}.\n\\newblock \\emph{arXiv preprint arXiv:2401.18079}.\n\n\\end{thebibliography}",
  "new_string": "\\begin{thebibliography}{3}\n\n\\bibitem[{Anonymous(2026)}]{ratequant2026}\nAnonymous. 2026.\n{RateQuant: Rate-Distortion Optimal KV Cache Quantization}.\nIn \\emph{Proceedings of ICML 2026}.\n\n\\bibitem[{Liu et~al.(2024)}]{kivi2024}\nZirui Liu, Jiayi Yuan, Hongye Jin, Shaochen Zhong, Zhaozhuo Xu, Vladimir Braverman, Beidi Chen, and Xia Hu. 2024.\n{KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache}.\nIn \\emph{Proceedings of ICML 2024}.\n\n\\bibitem[{Hooper et~al.(2024)}]{kvquant2024}\nColeman Hooper, Sehoon Kim, Hiva Mohammadzadeh, Michael W.\\ Mahoney, Yakun Sophia Shao, Kurt Keutzer, and Amir Gholami. 2024.\n{KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization}.\n\\emph{arXiv preprint arXiv:2401.18079}.\n\n\\end{thebibliography}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e0e885b-3f61-4fd9-8a8b-6f881f1f8b02",
  "isSidechain": false,
  "requestId": "req_011Cb4AFMkMuKBZD1yASiXJ3",
  "type": "assistant",
  "uuid": "206c0b8d-8c72-4e4a-a898-77bd13d282e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpRQWddBUzcDXPr5rcRe7C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3654,
      "cache_read_input_tokens": 67921,
      "output_tokens": 1020,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3654,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1020,
          "cache_read_input_tokens": 67921,
          "cache_creation_input_tokens": 3654,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3654
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

_source line 38 · 2026-05-15T10:00:54.481Z_

<details><summary>↩ Tool result · `toolu_01CM8HvPCM9t5UaLgbTf2pJh`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/worst/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "206c0b8d-8c72-4e4a-a898-77bd13d282e9",
  "isSidechain": false,
  "promptId": "e8e8fea0-d6a9-4b91-8885-3140c3cbe799",
  "type": "user",
  "uuid": "8d2b6272-c60d-4134-a2b2-15d2742e8d27",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/worst/paper.tex",
    "oldString": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{9}\n\n\\bibitem[\\protect\\citename{RateQuant}2026]{ratequant2026}\nAnonymous.\n\\newblock 2026.\n\\newblock {RateQuant: Rate-Distortion Optimal KV Cache Quantization}.\n\\newblock In \\emph{Proceedings of ICML 2026}.\n\n\\bibitem[\\protect\\citename{KIVI}2024]{kivi2024}\nZirui Liu, Jiayi Yuan, Hongye Jin, Shaochen Zhong, Zhaozhuo Xu, Vladimir Braverman, Beidi Chen, and Xia Hu.\n\\newblock 2024.\n\\newblock {KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache}.\n\\newblock In \\emph{Proceedings of ICML 2024}.\n\n\\bibitem[\\protect\\citename{KVQuant}2024]{kvquant2024}\nColeman Hooper, Sehoon Kim, Hiva Mohammadzadeh, Michael W.\\ Mahoney, Yakun Sophia Shao, Kurt Keutzer, and Amir Gholami.\n\\newblock 2024.\n\\newblock {KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization}.\n\\newblock \\emph{arXiv preprint arXiv:2401.18079}.\n\n\\end{thebibliography}",
    "newString": "\\begin{thebibliography}{3}\n\n\\bibitem[{Anonymous(2026)}]{ratequant2026}\nAnonymous. 2026.\n{RateQuant: Rate-Distortion Optimal KV Cache Quantization}.\nIn \\emph{Proceedings of ICML 2026}.\n\n\\bibitem[{Liu et~al.(2024)}]{kivi2024}\nZirui Liu, Jiayi Yuan, Hongye Jin, Shaochen Zhong, Zhaozhuo Xu, Vladimir Braverman, Beidi Chen, and Xia Hu. 2024.\n{KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache}.\nIn \\emph{Proceedings of ICML 2024}.\n\n\\bibitem[{Hooper et~al.(2024)}]{kvquant2024}\nColeman Hooper, Sehoon Kim, Hiva Mohammadzadeh, Michael W.\\ Mahoney, Yakun Sophia Shao, Kurt Keutzer, and Amir Gholami. 2024.\n{KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization}.\n\\emph{arXiv preprint arXiv:2401.18079}.\n\n\\end{thebibliography}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 449,
        "oldLines": 29,
        "newStart": 449,
        "newLines": 23,
        "lines": [
          " We do not evaluate KV cache eviction strategies or attention-sink-aware allocation.",
          " Multi-seed confidence intervals are available only for Qwen2.5-7B; other models report single-seed results.",
          " ",
          "-\\bibliography{references}",
          "-\\bibliographystyle{acl_natbib}",
          "+\\begin{thebibliography}{3}",
          " ",
          "-\\begin{thebibliography}{9}",
          "+\\bibitem[{Anonymous(2026)}]{ratequant2026}",
          "+Anonymous. 2026.",
          "+{RateQuant: Rate-Distortion Optimal KV Cache Quantization}.",
          "+In \\emph{Proceedings of ICML 2026}.",
          " ",
          "-\\bibitem[\\protect\\citename{RateQuant}2026]{ratequant2026}",
          "-Anonymous.",
          "-\\newblock 2026.",
          "-\\newblock {RateQuant: Rate-Distortion Optimal KV Cache Quantization}.",
          "-\\newblock In \\emph{Proceedings of ICML 2026}.",
          "+\\bibitem[{Liu et~al.(2024)}]{kivi2024}",
          "+Zirui Liu, Jiayi Yuan, Hongye Jin, Shaochen Zhong, Zhaozhuo Xu, Vladimir Braverman, Beidi Chen, and Xia Hu. 2024.",
          "+{KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache}.",
          "+In \\emph{Proceedings of ICML 2024}.",
          " ",
          "-\\bibitem[\\protect\\citename{KIVI}2024]{kivi2024}",
          "-Zirui Liu, Jiayi Yuan, Hongye Jin, Shaochen Zhong, Zhaozhuo Xu, Vladimir Braverman, Beidi Chen, and Xia Hu.",
          "-\\newblock 2024.",
          "-\\newblock {KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache}.",
          "-\\newblock In \\emph{Proceedings of ICML 2024}.",
          "+\\bibitem[{Hooper et~al.(2024)}]{kvquant2024}",
          "+Coleman Hooper, Sehoon Kim, Hiva Mohammadzadeh, Michael W.\\ Mahoney, Yakun Sophia Shao, Kurt Keutzer, and Amir Gholami. 2024.",
          "+{KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization}.",
          "+\\emph{arXiv preprint arXiv:2401.18079}.",
          " ",
          "-\\bibitem[\\protect\\citename{KVQuant}2024]{kvquant2024}",
          "-Coleman Hooper, Sehoon Kim, Hiva Mohammadzadeh, Michael W.\\ Mahoney, Yakun Sophia Shao, Kurt Keutzer, and Amir Gholami.",
          "-\\newblock 2024.",
          "-\\newblock {KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization}.",
          "-\\newblock \\emph{arXiv preprint arXiv:2401.18079}.",
          "-",
          " \\end{thebibliography}",
          " ",
          " \\end{document}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "206c0b8d-8c72-4e4a-a898-77bd13d282e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T085855 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/…",
  "leafUuid": "8d2b6272-c60d-4134-a2b2-15d2742e8d27",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier simulated paper for dream_20260515T085855",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8"
}
```

---

### Tool call

_source line 41 · 2026-05-15T10:00:58.352Z_

<details open><summary>🔧 Tool call — Bash · `toolu_011RA13im4J3Xiixk1Lb1qMt`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -10",
  "description": "Recompile LaTeX paper",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d2b6272-c60d-4134-a2b2-15d2742e8d27",
  "isSidechain": false,
  "requestId": "req_011Cb4AGb5pm5CNRSmXLvY4R",
  "type": "assistant",
  "uuid": "16ad33a8-63f6-444c-809d-fc550b0df156",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NkH46gxz7nFG6jiCHipztD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1103,
      "cache_read_input_tokens": 71575,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1103,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 174,
          "cache_read_input_tokens": 71575,
          "cache_creation_input_tokens": 1103,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1103
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

_source line 42 · 2026-05-15T10:00:59.247Z_

<details><summary>↩ Tool result · `toolu_011RA13im4J3Xiixk1Lb1qMt`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd))
(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
(./paper.aux)
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(./paper.out) (./paper.out)
(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)

Package natbib Warning: Citation `ratequant2026' on page 1 undefined on input l
ine 46.

(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips
/base/8r.enc}]

Package natbib Warning: Citation `kivi2024' on page 2 undefined on input line 7
0.


Package natbib Warning: Citation `kvquant2024' on page 2 undefined on input lin
e 70.


Package natbib Warning: Citation `ratequant2026' on page 2 undefined on input l
ine 73.


Overfull \hbox (0.87076pt too wide) in paragraph at lines 73--74
 []\T1/ptm/b/n/10.95 Per-Head Mixed Pre-ci-sion.[] \T1/ptm/m/n/10.95 Rate-Quant
 \T1/ptm/b/n/10.95 ? \T1/ptm/m/n/10.95 for-mu-lates per-head KV cache al-lo-ca-
tion as a rate--distortion
[2] [3]
Overfull \hbox (7.39783pt too wide) in paragraph at lines 189--190
 []\T1/ptm/b/n/10.95 Gemma-2-9B (BOS-corrected).[] \T1/ptm/m/n/10.95 Af-ter cor
-rect-ing a BOS-token eval-u-a-tion bug, the un-con-strained degra-
[4] [5] [6] [7] [8]

Package natbib Warning: There were undefined citations.

[9] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm
/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msam10.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/
texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (9 pages, 158238 bytes).
Transcript written on paper.log.
pe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm
/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msam10.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/
texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (9 pages, 158564 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "16ad33a8-63f6-444c-809d-fc550b0df156",
  "isSidechain": false,
  "promptId": "e8e8fea0-d6a9-4b91-8885-3140c3cbe799",
  "type": "user",
  "uuid": "b939cd90-5d4b-4a30-b877-58ef21e8ba1d",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `ratequant2026' on page 1 undefined on input l\nine 46.\n\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips\n/base/8r.enc}]\n\nPackage natbib Warning: Citation `kivi2024' on page 2 undefined on input line 7\n0.\n\n\nPackage natbib Warning: Citation `kvquant2024' on page 2 undefined on input lin\ne 70.\n\n\nPackage natbib Warning: Citation `ratequant2026' on page 2 undefined on input l\nine 73.\n\n\nOverfull \\hbox (0.87076pt too wide) in paragraph at lines 73--74\n []\\T1/ptm/b/n/10.95 Per-Head Mixed Pre-ci-sion.[] \\T1/ptm/m/n/10.95 Rate-Quant\n \\T1/ptm/b/n/10.95 ? \\T1/ptm/m/n/10.95 for-mu-lates per-head KV cache al-lo-ca-\ntion as a rate--distortion\n[2] [3]\nOverfull \\hbox (7.39783pt too wide) in paragraph at lines 189--190\n []\\T1/ptm/b/n/10.95 Gemma-2-9B (BOS-corrected).[] \\T1/ptm/m/n/10.95 Af-ter cor\n-rect-ing a BOS-token eval-u-a-tion bug, the un-con-strained degra-\n[4] [5] [6] [7] [8]\n\nPackage natbib Warning: There were undefined citations.\n\n[9] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n) )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\n/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msam10.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/\ntexlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (9 pages, 158238 bytes).\nTranscript written on paper.log.\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\n/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msam10.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/\ntexlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (9 pages, 158564 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "16ad33a8-63f6-444c-809d-fc550b0df156",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/worst",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-15T10:01:05.631Z_

<details><summary>Logged reasoning block</summary>

```text
Citations are still undefined because the `thebibliography` entries need to be processed first. Let me do a third pass.

Actually, looking at the output, the second pdflatex run produced the PDF with 9 pages. The "citations undefined" warning may persist because natbib needs the entries to match a specific format. Let me run one more time.

Wait, looking more carefully - the second run output says "Citation(s) may have changed. Rerun to get citations correct." So I need a third run. But the PDF was produced successfully. Let me do one more pass.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b939cd90-5d4b-4a30-b877-58ef21e8ba1d",
  "isSidechain": false,
  "requestId": "req_011Cb4AGwHWQ3SYjFDu9y9FJ",
  "type": "assistant",
  "uuid": "0ad19250-8796-468e-9eb0-b9f0ef6e0728",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/worst",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018fAqFMix2EsUNUVe16vKxM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3449,
      "cache_read_input_tokens": 72678,
      "output_tokens": 313,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3449,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 313,
          "cache_read_input_tokens": 72678,
          "cache_creation_input_tokens": 3449,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3449
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

_source line 44 · 2026-05-15T10:01:07.052Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01FpMuwAsUrVddBawt9gJs6m`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | grep -E \"Output written|Warning.*Citation|Error\"",
  "description": "Third LaTeX pass to resolve citations",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ad19250-8796-468e-9eb0-b9f0ef6e0728",
  "isSidechain": false,
  "requestId": "req_011Cb4AGwHWQ3SYjFDu9y9FJ",
  "type": "assistant",
  "uuid": "59426995-6222-4368-a081-d81ee62329a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/worst",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018fAqFMix2EsUNUVe16vKxM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3449,
      "cache_read_input_tokens": 72678,
      "output_tokens": 313,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3449,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 313,
          "cache_read_input_tokens": 72678,
          "cache_creation_input_tokens": 3449,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3449
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

_source line 45 · 2026-05-15T10:01:07.542Z_

<details><summary>↩ Tool result · `toolu_01FpMuwAsUrVddBawt9gJs6m`</summary>

```text
Output written on paper.pdf (9 pages, 158564 bytes).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59426995-6222-4368-a081-d81ee62329a6",
  "isSidechain": false,
  "promptId": "e8e8fea0-d6a9-4b91-8885-3140c3cbe799",
  "type": "user",
  "uuid": "0679d5ea-87e2-4b12-b32a-fb450039f2fd",
  "toolUseResult": {
    "stdout": "Output written on paper.pdf (9 pages, 158564 bytes).",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "59426995-6222-4368-a081-d81ee62329a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/worst",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-15T10:01:20.963Z_

Paper compiled cleanly on the third pass. 9 pages, no errors, no citation warnings.

Output: `paper.tex` (source) and `paper.pdf` (9 pages) written to `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/worst/`.

The paper covers all 22 experiments from `experiment_data.json` across these sections:
- **Abstract** — three contributions (cardinality constraint, systematic negative result, compounding characterization)
- **Introduction** — reframed around constraint-as-safeguard, not diagnostic
- **Method** — MCKP formulation, per-head profiling, cardinality constraint, solver equivalence
- **Experiments** — cross-architecture profiling (7 models incl. 72B), main constrained vs uniform results (6 models), unconstrained failure analysis (BOS-corrected Gemma-2, collapsed tiers), compounding sweep + super-additivity (W9), solver equivalence + oracle, budget sweep, systematic negative result table, downstream tasks (per-task for Qwen + summaries for 5 others), ablations (L0 auto-discovery, hires profiling, K/V separation, L0 heuristic), robustness (cross-dataset, multi-seed, runtime)
- **Analysis** — why constraint works universally, scaling dilution, diagnostic limitations (5/6 with Qwen14B false positive)
- **Conclusion + Limitations**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0679d5ea-87e2-4b12-b32a-fb450039f2fd",
  "isSidechain": false,
  "requestId": "req_011Cb4AHYnwXXojikzjFfKof",
  "type": "assistant",
  "uuid": "4429e51e-c120-4e17-9d2f-08810b2d1e10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260515T085855/worst",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BytMQc4z8SeJVgGYaaVsEd",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 298,
      "cache_read_input_tokens": 76127,
      "output_tokens": 365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 298,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 365,
          "cache_read_input_tokens": 76127,
          "cache_creation_input_tokens": 298,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 298
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T085855 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/…",
  "leafUuid": "4429e51e-c120-4e17-9d2f-08810b2d1e10",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier simulated paper for dream_20260515T085855",
  "sessionId": "60b94339-87f0-47ef-aa74-b7c45d2f68d8"
}
```

---
