# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T073533 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-1/4d779de5-396b-49dc-acca-1976fdd39e66.jsonl`
- **Structured JSON:** [`9eb4efa0c976f6ccdbff.json`](../../sessions/9e/9eb4efa0c976f6ccdbff.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T07:58:14.583Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T07:58:14.583Z",
  "sessionId": "4d779de5-396b-49dc-acca-1976fdd39e66",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T073533 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/median/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Pairwise confusability signal 跨任务复现但效应量偏小（r=0.11-0.13），FewRel Δ=-31pp 是 headline 但被部分 reviewer 质疑为 RE-specific。Error taxonomy 无争议（A2 成立）。SDGD 全线负面， \"no practical method\" 是 1-2 位 reviewer 的 major weakness。LLaMA Few-NERD 多次失败是  generalizability 短板。MAVEN per-type 正方向需更强的 centrality confound 定量论证。 整体落入 Findings 或需 rebuttal 挽救。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-16T07:58:14.587Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T07:58:14.587Z",
  "sessionId": "4d779de5-396b-49dc-acca-1976fdd39e66"
}
```

---

## Round 1

30 recorded events

### User

_source line 3 · 2026-05-16T07:58:14.615Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T073533 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/median/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Pairwise confusability signal 跨任务复现但效应量偏小（r=0.11-0.13），FewRel Δ=-31pp 是 headline 但被部分 reviewer 质疑为 RE-specific。Error taxonomy 无争议（A2 成立）。SDGD 全线负面， "no practical method" 是 1-2 位 reviewer 的 major weakness。LLaMA Few-NERD 多次失败是  generalizability 短板。MAVEN per-type 正方向需更强的 centrality confound 定量论证。 整体落入 Findings 或需 rebuttal 挽救。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "fc49f735-e722-4cc2-9426-bb861b70dea7",
  "type": "user",
  "uuid": "df818296-95e4-46cf-ae40-d7678e78f018",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "4d779de5-396b-49dc-acca-1976fdd39e66",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T07:58:14.614Z_

```json
{
  "parentUuid": "df818296-95e4-46cf-ae40-d7678e78f018",
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
  "uuid": "bb0ec3af-c951-449e-b614-f63cd49715ac",
  "timestamp": "2026-05-16T07:58:14.614Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "4d779de5-396b-49dc-acca-1976fdd39e66",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T07:58:14.614Z_

```json
{
  "parentUuid": "bb0ec3af-c951-449e-b614-f63cd49715ac",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "6cd90237-478c-4c33-a3f9-77eca0900e97",
  "timestamp": "2026-05-16T07:58:14.614Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "4d779de5-396b-49dc-acca-1976fdd39e66",
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
  "aiTitle": "Generate simulated research paper with LaTeX compilation",
  "sessionId": "4d779de5-396b-49dc-acca-1976fdd39e66"
}
```

---

### Assistant

_source line 7 · 2026-05-16T07:58:17.021Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6cd90237-478c-4c33-a3f9-77eca0900e97",
  "isSidechain": false,
  "requestId": "req_011Cb5tiyb31WFYwu93ez3pB",
  "type": "assistant",
  "uuid": "dae510cc-8dc3-4e1a-829c-36e4f2b656be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "4d779de5-396b-49dc-acca-1976fdd39e66",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E82iDzdwEpFSp3on8i6jHh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11208,
      "cache_read_input_tokens": 11841,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11208,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11208,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11208
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

_source line 8 · 2026-05-16T07:58:17.983Z_

<details open><summary>🔧 Tool call — Read · `toolu_015g2LvRZBLvzKoW3FQnX4ag`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dae510cc-8dc3-4e1a-829c-36e4f2b656be",
  "isSidechain": false,
  "requestId": "req_011Cb5tiyb31WFYwu93ez3pB",
  "type": "assistant",
  "uuid": "c3bae5ee-bc53-406c-8a1f-f25d1d145454",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "4d779de5-396b-49dc-acca-1976fdd39e66",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E82iDzdwEpFSp3on8i6jHh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11208,
      "cache_read_input_tokens": 11841,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11208,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11208,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11208
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

_source line 9 · 2026-05-16T07:58:18.226Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PM8oF1ZpEuUYFBcnbfJuTa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3bae5ee-bc53-406c-8a1f-f25d1d145454",
  "isSidechain": false,
  "requestId": "req_011Cb5tiyb31WFYwu93ez3pB",
  "type": "assistant",
  "uuid": "356606e2-38c5-46ed-bedd-02bb5110fadb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "4d779de5-396b-49dc-acca-1976fdd39e66",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E82iDzdwEpFSp3on8i6jHh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11208,
      "cache_read_input_tokens": 11841,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11208,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11208,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11208
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

_source line 10 · 2026-05-16T07:58:18.245Z_

<details><summary>↩ Tool result · `toolu_015g2LvRZBLvzKoW3FQnX4ag`</summary>

```text
1	[
2	  {
3	    "name": "DocRED Confusability Study",
4	    "description": "DocRED 96 relation types count curve + BCS 控制实验，跨 NER→sentRE→docRE 验证",
5	    "results": {
6	      "count_curve": {
7	        "count_1_acc": 0.74,
8	        "count_4_acc": 0.66,
9	        "count_8_acc": 0.59,
10	        "count_16_acc": 0.48,
11	        "count_32_acc": 0.43,
12	        "count_64_acc": 0.36,
13	        "count_96_acc": 0.32,
14	        "degradation_pp": -42.0
15	      },
16	      "bcs_controlled_count16": {
17	        "low_bcs_acc": 0.56,
18	        "high_bcs_acc": 0.4,
19	        "delta_pp": -16.0,
20	        "spearman_r": -0.42,
21	        "spearman_p": 0.028
22	      },
23	      "bcs_controlled_count32": {
24	        "low_bcs_acc": 0.5,
25	        "high_bcs_acc": 0.37,
26	        "delta_pp": -13.0,
27	        "spearman_r": -0.36,
28	        "spearman_p": 0.055
29	      },
30	      "pairwise_scs_confusion": {
31	        "pearson_r": 0.09,
32	        "ci_95": [
33	          0.04,
34	          0.14
35	        ],
36	        "n_pairs": 4560
37	      }
38	    },
39	    "tables": [
40	      {
41	        "name": "Table: DocRED Count Curve (Qwen3-32B)",
42	        "content": "| Count | Acc   | BCS_mean | N_batches |\n|-------|-------|----------|-----------|\n| 1     | 0.740 | 0        | 96        |\n| 4     | 0.660 | 0.53     | 5         |\n| 8     | 0.590 | 0.64     | 5         |\n| 16    | 0.480 | 0.73     | 5         |\n| 32    | 0.430 | 0.83     | 5         |\n| 64    | 0.360 | 0.91     | 5         |\n| 96    | 0.320 | 0.95     | 5         |\n"
43	      },
44	      {
45	        "name": "Table: DocRED BCS-Controlled",
46	        "content": "| Count | Low-BCS Acc | High-BCS Acc | Δ(pp)  | ρ     | p     |\n|-------|-------------|--------------|--------|-------|-------|\n| 16    | 0.560       | 0.400        | -16.0  | -0.42 | 0.028 |\n| 32    | 0.500       | 0.370        | -13.0  | -0.36 | 0.055 |\n"
47	      }
48	    ],
49	    "figures": [],
50	    "analysis": "方向复现但信号偏弱。Reviewer 会指出：(1) count_32 p 值 borderline；(2) document-level  引入未控制的 confound（entity pair distance, 跨句推理）；(3) pairwise r=0.09 低于  Few-NERD/MAVEN 的 0.11-0.13。Rebuttal 需强调 harder setting 下方向一致的价值， 并补充 entity-pair distance 控制分析。\n\n\nDocRED 是 document-level RE，baseline 比 sentence-level FewRel 低 ~12pp（跨句推理、 多 entity-pair 干扰）。Count curve 退化 42pp，与 FewRel 80-rel 的 35pp 量级一致但 更大——96 types + document-level complexity 双重加剧。BCS 效应 Δ=-16pp 存在但弱于  FewRel 的 -31pp：document-level 的每篇文档含多个 entity pairs，relation 决策受  entity pair distance、跨句推理等非 confusability 因素影响，稀释了纯 BCS 信号。 Pairwise r=0.09 刚好显著（CI 排除零但上界仅 0.14），reviewer 会质疑 document-level  增加的噪声源是否被充分控制。count_32 p=0.055 刚好不显著，给 reviewer 留下\"cherry-pick  count 条件\"的把柄。Median 档位下，DocRED 提供\"方向一致但不具决定性\"的第四任务证据。\n"
51	  },
52	  {
53	    "name": "Interaction Effect 2×2",
54	    "description": "{low/high count} × {low/high BCS} 检验 count 和 confusability 的交互效应",
55	    "results": {
56	      "cell_means_f1": {
57	        "low_count_low_bcs": 0.324,
58	        "low_count_high_bcs": 0.313,
59	        "high_count_low_bcs": 0.325,
60	        "high_count_high_bcs": 0.277
61	      },
62	      "main_effect_count_pp": -1.8,
63	      "main_effect_bcs_pp": -2.9,
64	      "interaction_z": -0.67,
65	      "interaction_p": 0.5,
66	      "bcs_effect_at_low_count_pp": -1.1,
67	      "bcs_effect_at_high_count_pp": -4.8
68	    },
69	    "tables": [
70	      {
71	        "name": "Table: 2×2 Interaction Design (Few-NERD F1)",
72	        "content": "|              | Low BCS | High BCS | BCS Δ  |\n|--------------|---------|----------|--------|\n| Count=6      | 0.324   | 0.313    | -0.011 |\n| Count=12     | 0.325   | 0.277    | -0.048 |\n| Count Δ      | +0.001  | -0.036   |        |\n| Interaction: z=-0.67, p=0.50 (n.s.)        |\n"
73	      }
74	    ],
75	    "figures": [],
76	    "analysis": "需要在论文中如实报告 null result 并提供 power analysis。FewRel 16→80 的 3.4×  amplification 作为 indirect interaction evidence。Reviewer 可能要求在 80-rel pool  上做正式 2×2 作为 rebuttal 补充分析。\n\n\n交互方向符合 multiplicative 假设（高 count 下 BCS 效应 4.4× 于低 count），但  p=0.50 远不显著。根本原因是 Few-NERD 实验设计的固有限制：(1) count 对比仅 6 vs 12， 差异过小（FewRel 的 3.4× amplification 用的是 16 vs 80）；(2) BCS 范围窄  (0.75-0.90)，Few-NERD 66 types 中高相似度集中在 person 子类、location 子类； (3) n=27 per cell，power analysis 估计需 n≈80 才能在此效应量下达到 0.8 power。 这不是假设被否定——是实验 underpowered。但 median 档 reviewer 不会区分 \"underpowered  null\" 和 \"true null\"，会标注为 \"interaction claim not supported\"。\n"
77	  },
78	  {
79	    "name": "Error Taxonomy",
80	    "description": "系统性 FP 分类跨 BCS bins，multi-channel 机械性证据",
81	    "results": {
82	      "fewnerd_intra_sub_by_bcs": {
83	        "bcs_zero_pct": 0.0,
84	        "bcs_low_pct": 1.6,
85	        "bcs_medium_pct": 10.6,
86	        "bcs_high_pct": 49.4,
87	        "rho": 1.0,
88	        "p": "<0.001"
89	      },
90	      "fewrel_intra_sub_by_bcs": {
91	        "bcs_zero_pct": 0.0,
92	        "bcs_low_pct": 4.2,
93	        "bcs_medium_pct": 13.0,
94	        "bcs_high_pct": 20.3,
95	        "bcs_very_high_pct": 32.3,
96	        "rho": 0.954,
97	        "p": "<1e-6"
98	      },
99	      "cross_task": {
100	        "ner_rho": 1.0,
101	        "re_rho": 0.954
102	      },
103	      "extra_sub": 0.0,
104	      "hallucination_pct": "<3%",
105	      "missed_rate_range": "10-16%"
106	    },
107	    "tables": [
108	      {
109	        "name": "Table: Error Taxonomy — Few-NERD (NER)",
110	        "content": "| BCS Bin  | N_FP | IntraSub% | ExtraSub% | Other%  |\n|----------|------|-----------|-----------|---------|\n| 0        | 6172 | 0.0       | 90.3      | 9.7     |\n| Low      | 2231 | 1.6       | 89.9      | 8.5     |\n| Medium   | 3843 | 10.6      | 78.1      | 11.3    |\n| High     | 6188 | 49.4      | 30.8      | 19.8    |\n"
111	      },
112	      {
113	        "name": "Table: Error Taxonomy — FewRel 80-rel (RE)",
114	        "content": "| BCS Bin    | Correct% | IntraSub% | Missed% |\n|------------|----------|-----------|---------|\n| Zero       | 85.7     | 0.0       | 14.3    |\n| Low        | 85.4     | 4.2       | 10.4    |\n| Medium     | 75.7     | 13.0      | 11.3    |\n| High       | 66.7     | 20.3      | 13.0    |\n| Very High  | 52.0     | 32.3      | 15.7    |\n"
115	      },
116	      {
117	        "name": "Table: Cross-task Monotonicity",
118	        "content": "| Task | IntraSub vs BCS ρ | p       |\n|------|-------------------|---------|\n| NER  | 1.000             | <0.001  |\n| RE   | 0.954             | <1e-6   |\n"
119	      }
120	    ],
121	    "figures": [],
122	    "analysis": "论文最强的机械性证据，也是 Claim 2 的核心支撑。Cross-task ρ={1.0, 0.954} 是整篇论文 中最具说服力的数字。Median 档 reviewer 对此无异议。建议在论文中将此作为 Section 4  的第一个分析呈现（先建立机制理解，再展示 pairwise/scaling 证据）。\n\n\nError taxonomy 是 median 档中最无争议的证据（A2 完全成立）。IntraSub 与 BCS 的  perfect/near-perfect monotonic 关系直接验证了 multi-channel model 的核心机制： confusability 导致 type confusion（IntraSub）而非 detection failure（missed rate  不变 10-16%）。几个关键支撑点：(1) extra_sub=0，type confusion 严格是 intra-batch  现象，模型只从当前 schema 中选类型；(2) hallucination<3%，LLM 的主错误模式是  \"选错类型\" 而非 \"编造实体\"；(3) cross-task replication 几乎完美（NER ρ=1.0,  RE ρ=0.954），同一机制跨 NER 和 RE。即使在 median 档位，reviewer 也不会质疑这个分析。 这是论文的 \"safe anchor\"。\n"
123	  },
124	  {
125	    "name": "SDGD-zero on MAVEN",
126	    "description": "SDGD-zero 在 MAVEN 168 event types 上测试，对比 single-pass + random",
127	    "results": {
128	      "single_pass": {
129	        "relaxed_f1": 0.247,
130	        "precision": 0.32,
131	        "recall": 0.2,
132	        "batches": 1,
133	        "time_s": 130
134	      },
135	      "random_batch": {
136	        "relaxed_f1": 0.175,
137	        "precision": 0.14,
138	        "recall": 0.23,
139	        "batches": 12,
140	        "time_s": 950
141	      },
142	      "sdgd_zero": {
143	        "relaxed_f1": 0.135,
144	        "precision": 0.12,
145	        "recall": 0.155,
146	        "batches": 8,
147	        "time_s": 680
148	      },
149	      "per_type": {
150	        "relaxed_f1": 0.11,
151	        "precision": 0.07,
152	        "recall": 0.3,
153	        "batches": 168,
154	        "time_s": 9200
155	      }
156	    },
157	    "tables": [
158	      {
159	        "name": "Table: SDGD Comparison — MAVEN 168 types",
160	        "content": "| Method      | Relaxed F1 | P     | R     | k   | Time(s) |\n|-------------|------------|-------|-------|-----|---------|\n| Single-pass | 0.247      | 0.320 | 0.200 | 1   | 130     |\n| Random      | 0.175      | 0.140 | 0.230 | 12  | 950     |\n| SDGD-zero   | 0.135      | 0.120 | 0.155 | 8   | 680     |\n| Per-type    | 0.110      | 0.070 | 0.300 | 168 | 9200    |\n"
161	      }
162	    ],
163	    "figures": [],
164	    "analysis": "与 Few-NERD 模式完全一致。论文中应将 Few-NERD + MAVEN 的 SDGD 负面结果并排呈现， 强调 \"decomposition penalty 是 task-agnostic 的结构性问题\"。同时明确指出 merge  strategy 是瓶颈（不是 grouping quality），为 future work 指明方向。Reviewer 的核心 质疑仍然是 \"如果你的方法不 work，这篇论文的 practical value 是什么？\"。\n\n\nMAVEN 168 types 使所有 decomposition 方法的表现更差，原因层叠：(1) 168 types 产生  更多 batches，每次 merge 引入更多冲突——merge amplification 与 batch 数量超线性增长； (2) MAVEN event types 语义高度同质（均为 FrameNet 层级，SCS mean=0.216,  119 pairs>0.5），SDGD-zero 的 graph coloring 无法有效分离——色数极高，被迫使用  大量 small batches 或在同 batch 内保留高 SCS pairs；(3) event trigger boundary  本身模糊（exact F1 仅 0.01-0.03），decomposition 后 merge 多个 batch 的 trigger  predictions 进一步恶化边界匹配。SDGD-zero F1=0.135 vs single-pass 0.247，退化比 (0.55) 与 Few-NERD 上一致 (0.24/0.45=0.53)。Random batch 再次优于 SDGD-zero  (0.175 vs 0.135)——SDGD 的不均匀 batch size 在 MAVEN 上伤害更大。Per-type (168 batches)  recall 最高但 precision 崩溃（0.07），9200s 延迟不可接受。 Median 档位下，此实验巩固 \"merge amplification 是跨任务的结构性障碍\"，但同时加深  \"no practical method\" 这一 major weakness。\n"
165	  },
166	  {
167	    "name": "SDGD-cal on Few-NERD",
168	    "description": "基于 5-10 个 calibration examples 的 empirical confusability graph，对比 SDGD-zero",
169	    "results": {
170	      "sdgd_cal_5shot": {
171	        "f1": 0.295,
172	        "precision": 0.34,
173	        "recall": 0.26,
174	        "batches": 5,
175	        "time_s": 370,
176	        "calibration_overhead_s": 50
177	      },
178	      "sdgd_cal_10shot": {
179	        "f1": 0.315,
180	        "precision": 0.36,
181	        "recall": 0.28,
182	        "batches": 5,
183	        "time_s": 370,
184	        "calibration_overhead_s": 90
185	      },
186	      "vs_baselines": {
187	        "sdgd_zero_f1": 0.241,
188	        "random_batch_f1": 0.301,
189	        "single_pass_f1": 0.445,
190	        "cal5_vs_zero_pp": "+5.4",
191	        "cal10_vs_zero_pp": "+7.4",
192	        "cal10_vs_single_pass_pp": "-13.0"
193	      }
194	    },
195	    "tables": [
196	      {
197	        "name": "Table: SDGD-cal vs Baselines (Few-NERD)",
198	        "content": "| Method        | F1    | P     | R     | k | Extra(s) |\n|---------------|-------|-------|-------|---|----------|\n| Single-pass   | 0.445 | 0.563 | 0.368 | 1 | 0        |\n| Random        | 0.301 | 0.331 | 0.276 | 8 | 0        |\n| SDGD-zero     | 0.241 | 0.324 | 0.191 | 4 | 0        |\n| SDGD-cal (5)  | 0.295 | 0.340 | 0.260 | 5 | 50       |\n| SDGD-cal (10) | 0.315 | 0.360 | 0.280 | 5 | 90       |\n"
199	      }
200	    ],
201	    "figures": [],
202	    "analysis": "SDGD-cal ≈ Random batch 的事实 is telling：即使用最好的 grouping signal，结果也不比 随机好多少。这进一步证实瓶颈是 merge 不是 grouping。论文中应明确写出这个 implication。 Reviewer 的追问：\"为什么不探索 confidence-weighted merge / NMS-style 去重？\"—— 这是合理的 future work 方向，v2 已尝试 confidence-gated 但未奏效，说明问题比  simple filtering 更深。\n\n\nCalibration 用 empirical confusion matrix 替代 embedding SCS，绕过了 embedding  选择问题，直接捕捉模型实际 confusion pattern。改善来源：(1) empirical confusion  比 SCS 更准确地识别 true confusion pairs（SCS 只解释 ~3% 方差，empirical 解释更多）； (2) 基于实际错误的 graph 更 sparse（大部分 type pairs 从不 confused），graph coloring  产生更均衡的 batches。但仍远低于 single-pass (-13pp) 的原因不变：merge amplification  与 grouping quality 关系不大，是 decomposition 本身的结构性问题——即使完美分组避免了  所有 confusion pairs，合并多个 batch 的输出时同一 span 仍会被多个 batch \"认领\"。 5-shot vs 10-shot 差异小（0.295 vs 0.315），因为 5 个样本已识别出主要 confusion  clusters（person 子类、location 子类）。Median 档位下，SDGD-cal 展示了 \"right  direction\" 但 Δ=+7pp 不构成 practical improvement，reviewer 评价 \"interesting  diagnostically but not actionable\"。\n"
203	  },
204	  {
205	    "name": "SDGD-cal on MAVEN",
206	    "description": "SDGD-cal 在 MAVEN 168 types 上的表现",
207	    "results": {
208	      "sdgd_cal_5shot": {
209	        "relaxed_f1": 0.165,
210	        "precision": 0.15,
211	        "recall": 0.185,
212	        "batches": 10,
213	        "calibration_overhead_s": 200
214	      },
215	      "sdgd_cal_10shot": {
216	        "relaxed_f1": 0.18,
217	        "precision": 0.17,
218	        "recall": 0.195,
219	        "batches": 10,
220	        "calibration_overhead_s": 380
221	      },
222	      "vs_baselines": {
223	        "single_pass_f1": 0.247,
224	        "sdgd_zero_f1": 0.135,
225	        "cal10_vs_zero_pp": "+4.5",
226	        "cal10_vs_single_pass_pp": "-6.7"
227	      }
228	    },
229	    "tables": [
230	      {
231	        "name": "Table: SDGD-cal vs Baselines (MAVEN)",
232	        "content": "| Method        | Relaxed F1 | k  | Calibration(s) |\n|---------------|------------|----|----------------|\n| Single-pass   | 0.247      | 1  | 0              |\n| Random        | 0.175      | 12 | 0              |\n| SDGD-zero     | 0.135      | 8  | 0              |\n| SDGD-cal (5)  | 0.165      | 10 | 200            |\n| SDGD-cal (10) | 0.180      | 10 | 380            |\n"
233	      }
234	    ],
235	    "figures": [],
236	    "analysis": "建议在论文中将 exp-009 和 exp-011 合并为一个 \"SDGD Results\" subsection，呈现  cross-task 一致的 hierarchy: single-pass > random ≈ cal > zero。 明确定位为 \"negative result with diagnostic value\"——理解 WHY decomposition fails  本身是贡献，指向 calibration-aware merge (非 calibration-aware grouping) 作为  correct next step。\n\n\nMAVEN 上 calibration 的边际改善比 Few-NERD 更小（+4.5pp vs +7.4pp），原因： (1) 168 types 的 confusion space 更大（14028 pairs），5-10 个 calibration samples  覆盖率更低——每个 sample 最多涉及 ~10 types，需要 O(168) 个 samples 才能充分覆盖； (2) MAVEN 语义同质性导致 confusion graph 极其 dense（几乎所有 type pairs 都有非零  confusion），graph coloring 的 chromatic number 很高，无论怎么分组都有大量 high-SCS  pairs 共存；(3) 200-380s 的 calibration overhead 在 168 types 上不可忽略，但换来的  仅 4.5pp 改善，投资回报率极低。SDGD-cal 仍远低于 single-pass (-6.7pp)。 Cross-task 一致的负面结果强化了结论，但也强化了 \"no practical method\" 的弱点。\n"
237	  },
238	  {
239	    "name": "Random Batching Ablation",
240	    "description": "与 SDGD 相同 batch count k 的 random composition，隔离 confusability-aware grouping 的增量",
241	    "results": {
242	      "fewnerd_k4": {
243	        "random_f1": 0.305,
244	        "sdgd_zero_f1": 0.241,
245	        "delta_pp": "+6.4"
246	      },
247	      "fewnerd_k8": {
248	        "random_f1": 0.295,
249	        "sdgd_zero_f1": 0.22,
250	        "delta_pp": "+7.5"
251	      },
252	      "maven_k8": {
253	        "random_f1": 0.175,
254	        "sdgd_zero_f1": 0.135,
255	        "delta_pp": "+4.0"
256	      },
257	      "single_pass_f1_fewnerd": 0.445,
258	      "single_pass_f1_maven": 0.247
259	    },
260	    "tables": [
261	      {
262	        "name": "Table: Random vs SDGD-zero Ablation",
263	        "content": "| Dataset  | k | Random F1 | SDGD-zero F1 | Single-pass F1 |\n|----------|---|-----------|--------------|----------------|\n| Few-NERD | 4 | 0.305     | 0.241        | 0.445          |\n| Few-NERD | 8 | 0.295     | 0.220        | 0.445          |\n| MAVEN    | 8 | 0.175     | 0.135        | 0.247          |\n"
264	      }
265	    ],
266	    "figures": [],
267	    "analysis": "关键 takeaway 不是 \"confusability-aware grouping 无用\"，而是 \"当前的 SDGD-zero  实现的分组策略有副作用（batch size 不均匀、hard type 集中化）抵消了 grouping 收益\"。 论文应 (1) 诚实报告 random > SDGD-zero；(2) 分析原因（batch size distribution,  hard-batch concentration）；(3) 指出 all decomposition << single-pass，真正的瓶颈是  merge 不是 grouping。Reviewer 可能追问 \"为什么不修复 SDGD 的 batch size 问题？\"—— 合理的 rebuttal 是 exp-010 的 SDGD-cal 部分解决了这个问题但仍低于 single-pass。\n\n\nRandom batching 在所有条件下优于 SDGD-zero，看似反直觉但有清晰解释： (1) SDGD-zero 的 graph coloring + min_batch_size 约束产生高度不均匀的 batch sizes—— 某些 batch 仅含 3-4 types，prompt 中类型太少时模型缺乏任务范围 context，对每个类型  过度 predict（high recall, terrible precision）；random batching 的 batch size 更均匀， 避免了这一退化模式；(2) SDGD-zero 将所有 \"hard\" (high-SCS) types 集中到同一个  batch，这些 batch 的 precision 崩溃；random 分散了 hard pairs，每个 batch 混合  easy+hard，整体更 balanced；(3) confusability-aware grouping 的正确 operationalization  应是 \"将 confusable pairs 分开\"，但 SDGD-zero 的贪心 coloring 在约束下反而集中了  难题。这说明 SDGD-zero 的分组算法有 design flaw，不否定 confusability signal 本身。 Median 档位下，\"SDGD-zero < random\" 是 reviewer 最容易攻击的点之一。\n"
268	  },
269	  {
270	    "name": "Per-type Splitting (UniNER-style)",
271	    "description": "每 batch 仅含 1 type，decomposition 的理论上限",
272	    "results": {
273	      "fewnerd": {
274	        "f1": 0.29,
275	        "precision": 0.195,
276	        "recall": 0.585,
277	        "batches": 66,
278	        "time_s": 2550,
279	        "intra_sub_rate": 0.0,
280	        "recall_vs_single_pass_pp": "+21.7",
281	        "precision_vs_single_pass_pp": "-36.8",
282	        "f1_vs_single_pass_pp": "-15.5"
283	      },
284	      "maven": {
285	        "relaxed_f1": 0.145,
286	        "precision": 0.085,
287	        "recall": 0.46,
288	        "batches": 168,
289	        "time_s": 9500
290	      }
291	    },
292	    "tables": [
293	      {
294	        "name": "Table: Full Decomposition Spectrum (Few-NERD)",
295	        "content": "| Method      | F1    | P     | R     | k  | IntraSub | Time(s) |\n|-------------|-------|-------|-------|----|----------|---------|\n| Single-pass | 0.445 | 0.563 | 0.368 | 1  | baseline | 79      |\n| Random (k=8)| 0.295 | 0.330 | 0.270 | 8  | moderate | 494     |\n| SDGD-zero   | 0.241 | 0.324 | 0.191 | 4  | low      | 261     |\n| SDGD-cal    | 0.315 | 0.360 | 0.280 | 5  | low      | 460     |\n| Per-type    | 0.290 | 0.195 | 0.585 | 66 | 0        | 2550    |\n"
296	      }
297	    ],
298	    "figures": [],
299	    "analysis": "Per-type 的 recall 优势是 decomposition 正确直觉的最好证据——问题确实在 merge。 论文结构建议：先展示 per-type 的 recall gain (证明 decomposition 有理论价值)， 再展示所有方法的 precision collapse (证明 merge amplification 是瓶颈)， 最后指出 \"future work needs better merge, not better grouping\"。 Reviewer 会欣赏这个清晰的 ablation 分析。1-2 位 reviewer 仍会标注 \"the paper  identifies the problem but doesn't solve it\" 作为 major weakness，这是 median 档 避不开的。\n\n\nPer-type splitting 完全消除了 type confusion (IntraSub=0)——每个 batch 只有一个类型， 不可能把 entity 标为 \"wrong\" type。这验证了 multi-channel model 的 Channel 1 预测： Recall 从 0.368 跃升至 0.585 (+21.7pp)，因为每个 prompt 只需关注一个类型， attention 不被稀释，不遗漏。但 Precision 从 0.563 崩溃到 0.195 (-36.8pp)—— 66 个 batch 的 union merge 引入大量冲突：同一 text span 被 person-scholar、 person-scientist、person-other 各自 \"认领\"，union merge 保留所有 predictions， precision 崩溃。F1 净效果为负 (-15.5pp)。 MAVEN 168 types 更极端——recall 高但 precision 更低（0.085），因为 168 个 single-type  batch 的 merge 冲突呈 O(k²) 增长。 这清晰展示了 decomposition 的 fundamental tradeoff：分解减少 miss (Channel 1 benefit)， 但 merge 产生 false positives (new Channel 3 problem)。当前所有 merge strategy  （union, confidence-gated）都不能解决 O(k) batches 的冲突。\n"
300	  },
301	  {
302	    "name": "SCS Validation",
303	    "description": "Spearman/Kendall correlation between embedding SCS 和 empirical confusion matrix",
304	    "results": {
305	      "all_pairs": {
306	        "n": 1953,
307	        "qwen3_spearman": 0.168,
308	        "qwen3_p": "7.3e-14",
309	        "qwen3_kendall": 0.135,
310	        "minilm_spearman": 0.144,
311	        "minilm_p": "1.7e-10",
312	        "minilm_kendall": 0.115
313	      },
314	      "nonzero_only": {
315	        "n": 216,
316	        "qwen3_spearman": 0.272,
317	        "qwen3_p": "5.0e-5",
318	        "qwen3_kendall": 0.2,
319	        "minilm_spearman": 0.306,
320	        "minilm_p": "4.6e-6",
321	        "minilm_kendall": 0.228
322	      },
323	      "variance_explained": {
324	        "all_pairs_r_squared": "2.8-4.8%",
325	        "nonzero_r_squared": "7.4-9.4%"
326	      }
327	    },
328	    "tables": [
329	      {
330	        "name": "Table: SCS → Empirical Confusion Validation",
331	        "content": "| Subset        | Embedding | Spearman ρ | p        | Kendall τ | R²     |\n|---------------|-----------|------------|----------|-----------|--------|\n| All (n=1953)  | Qwen3     | 0.168      | 7.3e-14  | 0.135     | ~4.8%  |\n| All (n=1953)  | MiniLM    | 0.144      | 1.7e-10  | 0.115     | ~2.8%  |\n| Nonzero (216) | Qwen3     | 0.272      | 5.0e-5   | 0.200     | ~7.4%  |\n| Nonzero (216) | MiniLM    | 0.306      | 4.6e-6   | 0.228     | ~9.4%  |\n"
332	      }
333	    ],
334	    "figures": [],
335	    "analysis": "SCS validation 支撑了 \"confusability signal exists\" 但也暴露了 \"signal is weak for  practical use\"。这与 SDGD 的负面结果形成一致叙事：pairwise SCS 作为分析工具有效 （cross-task 显著），作为工程工具不足（R²太低）。论文应诚实呈现这个 gap，并将  SDGD-cal (bypassing embedding entirely) 作为 pragmatic 替代方案。 Reviewer 可能追问 AUC（SCS 预测 nonzero confusion 的分类能力），预估 AUC≈0.65-0.70， 属于 \"above chance but far from reliable\" 水平。\n\nSCS 是有效但不完美的 confusion proxy。All-pairs ρ 偏低（0.14-0.17）的根本原因是  data 极度 zero-inflated：88.9% 的 type pairs 从未被混淆（confusion=0），产生大量  ties 压缩 rank correlation。Nonzero-only ρ 跳升到 0.27-0.31，说明 SCS 能有效区分  \"哪些 pairs 被混淆得更多\" 但不太能预测 \"哪些 pairs 会被混淆\"。 Qwen3 在 all-pairs 上更好（ρ=0.168 vs 0.144）——extraction model 的 embedding  更好地捕捉 \"是否会混淆\" 的 threshold，因为 embedding space 与 model 的 internal  representation 对齐。MiniLM 在 nonzero-only 上更好（ρ=0.306 vs 0.272）——sentence  similarity model 的 fine-grained similarity gradient 更平滑，更好地排序 confusion  程度。 Median 档位下，reviewer 的主要质疑是 R²=3-5%：如果你的 proxy 只解释 3-5% 的方差， 基于它构建的 SDGD 分组怎么可能有效？这恰好与 SDGD-zero 的失败一致——SCS 作为 grouping  signal 太 noisy。论文应将此定位为 \"validating the existence of the signal\" 而非  \"validating its practical sufficiency\"，并指向 SDGD-cal (empirical confusion)  作为正确的 operationalization 路径。\n"
336	  }
337	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3bae5ee-bc53-406c-8a1f-f25d1d145454",
  "isSidechain": false,
  "promptId": "fc49f735-e722-4cc2-9426-bb861b70dea7",
  "type": "user",
  "uuid": "76b93b2b-6348-42d9-b8b6-809b0a475f6a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"DocRED Confusability Study\",\n    \"description\": \"DocRED 96 relation types count curve + BCS 控制实验，跨 NER→sentRE→docRE 验证\",\n    \"results\": {\n      \"count_curve\": {\n        \"count_1_acc\": 0.74,\n        \"count_4_acc\": 0.66,\n        \"count_8_acc\": 0.59,\n        \"count_16_acc\": 0.48,\n        \"count_32_acc\": 0.43,\n        \"count_64_acc\": 0.36,\n        \"count_96_acc\": 0.32,\n        \"degradation_pp\": -42.0\n      },\n      \"bcs_controlled_count16\": {\n        \"low_bcs_acc\": 0.56,\n        \"high_bcs_acc\": 0.4,\n        \"delta_pp\": -16.0,\n        \"spearman_r\": -0.42,\n        \"spearman_p\": 0.028\n      },\n      \"bcs_controlled_count32\": {\n        \"low_bcs_acc\": 0.5,\n        \"high_bcs_acc\": 0.37,\n        \"delta_pp\": -13.0,\n        \"spearman_r\": -0.36,\n        \"spearman_p\": 0.055\n      },\n      \"pairwise_scs_confusion\": {\n        \"pearson_r\": 0.09,\n        \"ci_95\": [\n          0.04,\n          0.14\n        ],\n        \"n_pairs\": 4560\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: DocRED Count Curve (Qwen3-32B)\",\n        \"content\": \"| Count | Acc   | BCS_mean | N_batches |\\n|-------|-------|----------|-----------|\\n| 1     | 0.740 | 0        | 96        |\\n| 4     | 0.660 | 0.53     | 5         |\\n| 8     | 0.590 | 0.64     | 5         |\\n| 16    | 0.480 | 0.73     | 5         |\\n| 32    | 0.430 | 0.83     | 5         |\\n| 64    | 0.360 | 0.91     | 5         |\\n| 96    | 0.320 | 0.95     | 5         |\\n\"\n      },\n      {\n        \"name\": \"Table: DocRED BCS-Controlled\",\n        \"content\": \"| Count | Low-BCS Acc | High-BCS Acc | Δ(pp)  | ρ     | p     |\\n|-------|-------------|--------------|--------|-------|-------|\\n| 16    | 0.560       | 0.400        | -16.0  | -0.42 | 0.028 |\\n| 32    | 0.500       | 0.370        | -13.0  | -0.36 | 0.055 |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"方向复现但信号偏弱。Reviewer 会指出：(1) count_32 p 值 borderline；(2) document-level  引入未控制的 confound（entity pair distance, 跨句推理）；(3) pairwise r=0.09 低于  Few-NERD/MAVEN 的 0.11-0.13。Rebuttal 需强调 harder setting 下方向一致的价值， 并补充 entity-pair distance 控制分析。\\n\\n\\nDocRED 是 document-level RE，baseline 比 sentence-level FewRel 低 ~12pp（跨句推理、 多 entity-pair 干扰）。Count curve 退化 42pp，与 FewRel 80-rel 的 35pp 量级一致但 更大——96 types + document-level complexity 双重加剧。BCS 效应 Δ=-16pp 存在但弱于  FewRel 的 -31pp：document-level 的每篇文档含多个 entity pairs，relation 决策受  entity pair distance、跨句推理等非 confusability 因素影响，稀释了纯 BCS 信号。 Pairwise r=0.09 刚好显著（CI 排除零但上界仅 0.14），reviewer 会质疑 document-level  增加的噪声源是否被充分控制。count_32 p=0.055 刚好不显著，给 reviewer 留下\\\"cherry-pick  count 条件\\\"的把柄。Median 档位下，DocRED 提供\\\"方向一致但不具决定性\\\"的第四任务证据。\\n\"\n  },\n  {\n    \"name\": \"Interaction Effect 2×2\",\n    \"description\": \"{low/high count} × {low/high BCS} 检验 count 和 confusability 的交互效应\",\n    \"results\": {\n      \"cell_means_f1\": {\n        \"low_count_low_bcs\": 0.324,\n        \"low_count_high_bcs\": 0.313,\n        \"high_count_low_bcs\": 0.325,\n        \"high_count_high_bcs\": 0.277\n      },\n      \"main_effect_count_pp\": -1.8,\n      \"main_effect_bcs_pp\": -2.9,\n      \"interaction_z\": -0.67,\n      \"interaction_p\": 0.5,\n      \"bcs_effect_at_low_count_pp\": -1.1,\n      \"bcs_effect_at_high_count_pp\": -4.8\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: 2×2 Interaction Design (Few-NERD F1)\",\n        \"content\": \"|              | Low BCS | High BCS | BCS Δ  |\\n|--------------|---------|----------|--------|\\n| Count=6      | 0.324   | 0.313    | -0.011 |\\n| Count=12     | 0.325   | 0.277    | -0.048 |\\n| Count Δ      | +0.001  | -0.036   |        |\\n| Interaction: z=-0.67, p=0.50 (n.s.)        |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"需要在论文中如实报告 null result 并提供 power analysis。FewRel 16→80 的 3.4×  amplification 作为 indirect interaction evidence。Reviewer 可能要求在 80-rel pool  上做正式 2×2 作为 rebuttal 补充分析。\\n\\n\\n交互方向符合 multiplicative 假设（高 count 下 BCS 效应 4.4× 于低 count），但  p=0.50 远不显著。根本原因是 Few-NERD 实验设计的固有限制：(1) count 对比仅 6 vs 12， 差异过小（FewRel 的 3.4× amplification 用的是 16 vs 80）；(2) BCS 范围窄  (0.75-0.90)，Few-NERD 66 types 中高相似度集中在 person 子类、location 子类； (3) n=27 per cell，power analysis 估计需 n≈80 才能在此效应量下达到 0.8 power。 这不是假设被否定——是实验 underpowered。但 median 档 reviewer 不会区分 \\\"underpowered  null\\\" 和 \\\"true null\\\"，会标注为 \\\"interaction claim not supported\\\"。\\n\"\n  },\n  {\n    \"name\": \"Error Taxonomy\",\n    \"description\": \"系统性 FP 分类跨 BCS bins，multi-channel 机械性证据\",\n    \"results\": {\n      \"fewnerd_intra_sub_by_bcs\": {\n        \"bcs_zero_pct\": 0.0,\n        \"bcs_low_pct\": 1.6,\n        \"bcs_medium_pct\": 10.6,\n        \"bcs_high_pct\": 49.4,\n        \"rho\": 1.0,\n        \"p\": \"<0.001\"\n      },\n      \"fewrel_intra_sub_by_bcs\": {\n        \"bcs_zero_pct\": 0.0,\n        \"bcs_low_pct\": 4.2,\n        \"bcs_medium_pct\": 13.0,\n        \"bcs_high_pct\": 20.3,\n        \"bcs_very_high_pct\": 32.3,\n        \"rho\": 0.954,\n        \"p\": \"<1e-6\"\n      },\n      \"cross_task\": {\n        \"ner_rho\": 1.0,\n        \"re_rho\": 0.954\n      },\n      \"extra_sub\": 0.0,\n      \"hallucination_pct\": \"<3%\",\n      \"missed_rate_range\": \"10-16%\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Error Taxonomy — Few-NERD (NER)\",\n        \"content\": \"| BCS Bin  | N_FP | IntraSub% | ExtraSub% | Other%  |\\n|----------|------|-----------|-----------|---------|\\n| 0        | 6172 | 0.0       | 90.3      | 9.7     |\\n| Low      | 2231 | 1.6       | 89.9      | 8.5     |\\n| Medium   | 3843 | 10.6      | 78.1      | 11.3    |\\n| High     | 6188 | 49.4      | 30.8      | 19.8    |\\n\"\n      },\n      {\n        \"name\": \"Table: Error Taxonomy — FewRel 80-rel (RE)\",\n        \"content\": \"| BCS Bin    | Correct% | IntraSub% | Missed% |\\n|------------|----------|-----------|---------|\\n| Zero       | 85.7     | 0.0       | 14.3    |\\n| Low        | 85.4     | 4.2       | 10.4    |\\n| Medium     | 75.7     | 13.0      | 11.3    |\\n| High       | 66.7     | 20.3      | 13.0    |\\n| Very High  | 52.0     | 32.3      | 15.7    |\\n\"\n      },\n      {\n        \"name\": \"Table: Cross-task Monotonicity\",\n        \"content\": \"| Task | IntraSub vs BCS ρ | p       |\\n|------|-------------------|---------|\\n| NER  | 1.000             | <0.001  |\\n| RE   | 0.954             | <1e-6   |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"论文最强的机械性证据，也是 Claim 2 的核心支撑。Cross-task ρ={1.0, 0.954} 是整篇论文 中最具说服力的数字。Median 档 reviewer 对此无异议。建议在论文中将此作为 Section 4  的第一个分析呈现（先建立机制理解，再展示 pairwise/scaling 证据）。\\n\\n\\nError taxonomy 是 median 档中最无争议的证据（A2 完全成立）。IntraSub 与 BCS 的  perfect/near-perfect monotonic 关系直接验证了 multi-channel model 的核心机制： confusability 导致 type confusion（IntraSub）而非 detection failure（missed rate  不变 10-16%）。几个关键支撑点：(1) extra_sub=0，type confusion 严格是 intra-batch  现象，模型只从当前 schema 中选类型；(2) hallucination<3%，LLM 的主错误模式是  \\\"选错类型\\\" 而非 \\\"编造实体\\\"；(3) cross-task replication 几乎完美（NER ρ=1.0,  RE ρ=0.954），同一机制跨 NER 和 RE。即使在 median 档位，reviewer 也不会质疑这个分析。 这是论文的 \\\"safe anchor\\\"。\\n\"\n  },\n  {\n    \"name\": \"SDGD-zero on MAVEN\",\n    \"description\": \"SDGD-zero 在 MAVEN 168 event types 上测试，对比 single-pass + random\",\n    \"results\": {\n      \"single_pass\": {\n        \"relaxed_f1\": 0.247,\n        \"precision\": 0.32,\n        \"recall\": 0.2,\n        \"batches\": 1,\n        \"time_s\": 130\n      },\n      \"random_batch\": {\n        \"relaxed_f1\": 0.175,\n        \"precision\": 0.14,\n        \"recall\": 0.23,\n        \"batches\": 12,\n        \"time_s\": 950\n      },\n      \"sdgd_zero\": {\n        \"relaxed_f1\": 0.135,\n        \"precision\": 0.12,\n        \"recall\": 0.155,\n        \"batches\": 8,\n        \"time_s\": 680\n      },\n      \"per_type\": {\n        \"relaxed_f1\": 0.11,\n        \"precision\": 0.07,\n        \"recall\": 0.3,\n        \"batches\": 168,\n        \"time_s\": 9200\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: SDGD Comparison — MAVEN 168 types\",\n        \"content\": \"| Method      | Relaxed F1 | P     | R     | k   | Time(s) |\\n|-------------|------------|-------|-------|-----|---------|\\n| Single-pass | 0.247      | 0.320 | 0.200 | 1   | 130     |\\n| Random      | 0.175      | 0.140 | 0.230 | 12  | 950     |\\n| SDGD-zero   | 0.135      | 0.120 | 0.155 | 8   | 680     |\\n| Per-type    | 0.110      | 0.070 | 0.300 | 168 | 9200    |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"与 Few-NERD 模式完全一致。论文中应将 Few-NERD + MAVEN 的 SDGD 负面结果并排呈现， 强调 \\\"decomposition penalty 是 task-agnostic 的结构性问题\\\"。同时明确指出 merge  strategy 是瓶颈（不是 grouping quality），为 future work 指明方向。Reviewer 的核心 质疑仍然是 \\\"如果你的方法不 work，这篇论文的 practical value 是什么？\\\"。\\n\\n\\nMAVEN 168 types 使所有 decomposition 方法的表现更差，原因层叠：(1) 168 types 产生  更多 batches，每次 merge 引入更多冲突——merge amplification 与 batch 数量超线性增长； (2) MAVEN event types 语义高度同质（均为 FrameNet 层级，SCS mean=0.216,  119 pairs>0.5），SDGD-zero 的 graph coloring 无法有效分离——色数极高，被迫使用  大量 small batches 或在同 batch 内保留高 SCS pairs；(3) event trigger boundary  本身模糊（exact F1 仅 0.01-0.03），decomposition 后 merge 多个 batch 的 trigger  predictions 进一步恶化边界匹配。SDGD-zero F1=0.135 vs single-pass 0.247，退化比 (0.55) 与 Few-NERD 上一致 (0.24/0.45=0.53)。Random batch 再次优于 SDGD-zero  (0.175 vs 0.135)——SDGD 的不均匀 batch size 在 MAVEN 上伤害更大。Per-type (168 batches)  recall 最高但 precision 崩溃（0.07），9200s 延迟不可接受。 Median 档位下，此实验巩固 \\\"merge amplification 是跨任务的结构性障碍\\\"，但同时加深  \\\"no practical method\\\" 这一 major weakness。\\n\"\n  },\n  {\n    \"name\": \"SDGD-cal on Few-NERD\",\n    \"description\": \"基于 5-10 个 calibration examples 的 empirical confusability graph，对比 SDGD-zero\",\n    \"results\": {\n      \"sdgd_cal_5shot\": {\n        \"f1\": 0.295,\n        \"precision\": 0.34,\n        \"recall\": 0.26,\n        \"batches\": 5,\n        \"time_s\": 370,\n        \"calibration_overhead_s\": 50\n      },\n      \"sdgd_cal_10shot\": {\n        \"f1\": 0.315,\n        \"precision\": 0.36,\n        \"recall\": 0.28,\n        \"batches\": 5,\n        \"time_s\": 370,\n        \"calibration_overhead_s\": 90\n      },\n      \"vs_baselines\": {\n        \"sdgd_zero_f1\": 0.241,\n        \"random_batch_f1\": 0.301,\n        \"single_pass_f1\": 0.445,\n        \"cal5_vs_zero_pp\": \"+5.4\",\n        \"cal10_vs_zero_pp\": \"+7.4\",\n        \"cal10_vs_single_pass_pp\": \"-13.0\"\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: SDGD-cal vs Baselines (Few-NERD)\",\n        \"content\": \"| Method        | F1    | P     | R     | k | Extra(s) |\\n|---------------|-------|-------|-------|---|----------|\\n| Single-pass   | 0.445 | 0.563 | 0.368 | 1 | 0        |\\n| Random        | 0.301 | 0.331 | 0.276 | 8 | 0        |\\n| SDGD-zero     | 0.241 | 0.324 | 0.191 | 4 | 0        |\\n| SDGD-cal (5)  | 0.295 | 0.340 | 0.260 | 5 | 50       |\\n| SDGD-cal (10) | 0.315 | 0.360 | 0.280 | 5 | 90       |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"SDGD-cal ≈ Random batch 的事实 is telling：即使用最好的 grouping signal，结果也不比 随机好多少。这进一步证实瓶颈是 merge 不是 grouping。论文中应明确写出这个 implication。 Reviewer 的追问：\\\"为什么不探索 confidence-weighted merge / NMS-style 去重？\\\"—— 这是合理的 future work 方向，v2 已尝试 confidence-gated 但未奏效，说明问题比  simple filtering 更深。\\n\\n\\nCalibration 用 empirical confusion matrix 替代 embedding SCS，绕过了 embedding  选择问题，直接捕捉模型实际 confusion pattern。改善来源：(1) empirical confusion  比 SCS 更准确地识别 true confusion pairs（SCS 只解释 ~3% 方差，empirical 解释更多）； (2) 基于实际错误的 graph 更 sparse（大部分 type pairs 从不 confused），graph coloring  产生更均衡的 batches。但仍远低于 single-pass (-13pp) 的原因不变：merge amplification  与 grouping quality 关系不大，是 decomposition 本身的结构性问题——即使完美分组避免了  所有 confusion pairs，合并多个 batch 的输出时同一 span 仍会被多个 batch \\\"认领\\\"。 5-shot vs 10-shot 差异小（0.295 vs 0.315），因为 5 个样本已识别出主要 confusion  clusters（person 子类、location 子类）。Median 档位下，SDGD-cal 展示了 \\\"right  direction\\\" 但 Δ=+7pp 不构成 practical improvement，reviewer 评价 \\\"interesting  diagnostically but not actionable\\\"。\\n\"\n  },\n  {\n    \"name\": \"SDGD-cal on MAVEN\",\n    \"description\": \"SDGD-cal 在 MAVEN 168 types 上的表现\",\n    \"results\": {\n      \"sdgd_cal_5shot\": {\n        \"relaxed_f1\": 0.165,\n        \"precision\": 0.15,\n        \"recall\": 0.185,\n        \"batches\": 10,\n        \"calibration_overhead_s\": 200\n      },\n      \"sdgd_cal_10shot\": {\n        \"relaxed_f1\": 0.18,\n        \"precision\": 0.17,\n        \"recall\": 0.195,\n        \"batches\": 10,\n        \"calibration_overhead_s\": 380\n      },\n      \"vs_baselines\": {\n        \"single_pass_f1\": 0.247,\n        \"sdgd_zero_f1\": 0.135,\n        \"cal10_vs_zero_pp\": \"+4.5\",\n        \"cal10_vs_single_pass_pp\": \"-6.7\"\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: SDGD-cal vs Baselines (MAVEN)\",\n        \"content\": \"| Method        | Relaxed F1 | k  | Calibration(s) |\\n|---------------|------------|----|----------------|\\n| Single-pass   | 0.247      | 1  | 0              |\\n| Random        | 0.175      | 12 | 0              |\\n| SDGD-zero     | 0.135      | 8  | 0              |\\n| SDGD-cal (5)  | 0.165      | 10 | 200            |\\n| SDGD-cal (10) | 0.180      | 10 | 380            |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"建议在论文中将 exp-009 和 exp-011 合并为一个 \\\"SDGD Results\\\" subsection，呈现  cross-task 一致的 hierarchy: single-pass > random ≈ cal > zero。 明确定位为 \\\"negative result with diagnostic value\\\"——理解 WHY decomposition fails  本身是贡献，指向 calibration-aware merge (非 calibration-aware grouping) 作为  correct next step。\\n\\n\\nMAVEN 上 calibration 的边际改善比 Few-NERD 更小（+4.5pp vs +7.4pp），原因： (1) 168 types 的 confusion space 更大（14028 pairs），5-10 个 calibration samples  覆盖率更低——每个 sample 最多涉及 ~10 types，需要 O(168) 个 samples 才能充分覆盖； (2) MAVEN 语义同质性导致 confusion graph 极其 dense（几乎所有 type pairs 都有非零  confusion），graph coloring 的 chromatic number 很高，无论怎么分组都有大量 high-SCS  pairs 共存；(3) 200-380s 的 calibration overhead 在 168 types 上不可忽略，但换来的  仅 4.5pp 改善，投资回报率极低。SDGD-cal 仍远低于 single-pass (-6.7pp)。 Cross-task 一致的负面结果强化了结论，但也强化了 \\\"no practical method\\\" 的弱点。\\n\"\n  },\n  {\n    \"name\": \"Random Batching Ablation\",\n    \"description\": \"与 SDGD 相同 batch count k 的 random composition，隔离 confusability-aware grouping 的增量\",\n    \"results\": {\n      \"fewnerd_k4\": {\n        \"random_f1\": 0.305,\n        \"sdgd_zero_f1\": 0.241,\n        \"delta_pp\": \"+6.4\"\n      },\n      \"fewnerd_k8\": {\n        \"random_f1\": 0.295,\n        \"sdgd_zero_f1\": 0.22,\n        \"delta_pp\": \"+7.5\"\n      },\n      \"maven_k8\": {\n        \"random_f1\": 0.175,\n        \"sdgd_zero_f1\": 0.135,\n        \"delta_pp\": \"+4.0\"\n      },\n      \"single_pass_f1_fewnerd\": 0.445,\n      \"single_pass_f1_maven\": 0.247\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Random vs SDGD-zero Ablation\",\n        \"content\": \"| Dataset  | k | Random F1 | SDGD-zero F1 | Single-pass F1 |\\n|----------|---|-----------|--------------|----------------|\\n| Few-NERD | 4 | 0.305     | 0.241        | 0.445          |\\n| Few-NERD | 8 | 0.295     | 0.220        | 0.445          |\\n| MAVEN    | 8 | 0.175     | 0.135        | 0.247          |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"关键 takeaway 不是 \\\"confusability-aware grouping 无用\\\"，而是 \\\"当前的 SDGD-zero  实现的分组策略有副作用（batch size 不均匀、hard type 集中化）抵消了 grouping 收益\\\"。 论文应 (1) 诚实报告 random > SDGD-zero；(2) 分析原因（batch size distribution,  hard-batch concentration）；(3) 指出 all decomposition << single-pass，真正的瓶颈是  merge 不是 grouping。Reviewer 可能追问 \\\"为什么不修复 SDGD 的 batch size 问题？\\\"—— 合理的 rebuttal 是 exp-010 的 SDGD-cal 部分解决了这个问题但仍低于 single-pass。\\n\\n\\nRandom batching 在所有条件下优于 SDGD-zero，看似反直觉但有清晰解释： (1) SDGD-zero 的 graph coloring + min_batch_size 约束产生高度不均匀的 batch sizes—— 某些 batch 仅含 3-4 types，prompt 中类型太少时模型缺乏任务范围 context，对每个类型  过度 predict（high recall, terrible precision）；random batching 的 batch size 更均匀， 避免了这一退化模式；(2) SDGD-zero 将所有 \\\"hard\\\" (high-SCS) types 集中到同一个  batch，这些 batch 的 precision 崩溃；random 分散了 hard pairs，每个 batch 混合  easy+hard，整体更 balanced；(3) confusability-aware grouping 的正确 operationalization  应是 \\\"将 confusable pairs 分开\\\"，但 SDGD-zero 的贪心 coloring 在约束下反而集中了  难题。这说明 SDGD-zero 的分组算法有 design flaw，不否定 confusability signal 本身。 Median 档位下，\\\"SDGD-zero < random\\\" 是 reviewer 最容易攻击的点之一。\\n\"\n  },\n  {\n    \"name\": \"Per-type Splitting (UniNER-style)\",\n    \"description\": \"每 batch 仅含 1 type，decomposition 的理论上限\",\n    \"results\": {\n      \"fewnerd\": {\n        \"f1\": 0.29,\n        \"precision\": 0.195,\n        \"recall\": 0.585,\n        \"batches\": 66,\n        \"time_s\": 2550,\n        \"intra_sub_rate\": 0.0,\n        \"recall_vs_single_pass_pp\": \"+21.7\",\n        \"precision_vs_single_pass_pp\": \"-36.8\",\n        \"f1_vs_single_pass_pp\": \"-15.5\"\n      },\n      \"maven\": {\n        \"relaxed_f1\": 0.145,\n        \"precision\": 0.085,\n        \"recall\": 0.46,\n        \"batches\": 168,\n        \"time_s\": 9500\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Full Decomposition Spectrum (Few-NERD)\",\n        \"content\": \"| Method      | F1    | P     | R     | k  | IntraSub | Time(s) |\\n|-------------|-------|-------|-------|----|----------|---------|\\n| Single-pass | 0.445 | 0.563 | 0.368 | 1  | baseline | 79      |\\n| Random (k=8)| 0.295 | 0.330 | 0.270 | 8  | moderate | 494     |\\n| SDGD-zero   | 0.241 | 0.324 | 0.191 | 4  | low      | 261     |\\n| SDGD-cal    | 0.315 | 0.360 | 0.280 | 5  | low      | 460     |\\n| Per-type    | 0.290 | 0.195 | 0.585 | 66 | 0        | 2550    |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Per-type 的 recall 优势是 decomposition 正确直觉的最好证据——问题确实在 merge。 论文结构建议：先展示 per-type 的 recall gain (证明 decomposition 有理论价值)， 再展示所有方法的 precision collapse (证明 merge amplification 是瓶颈)， 最后指出 \\\"future work needs better merge, not better grouping\\\"。 Reviewer 会欣赏这个清晰的 ablation 分析。1-2 位 reviewer 仍会标注 \\\"the paper  identifies the problem but doesn't solve it\\\" 作为 major weakness，这是 median 档 避不开的。\\n\\n\\nPer-type splitting 完全消除了 type confusion (IntraSub=0)——每个 batch 只有一个类型， 不可能把 entity 标为 \\\"wrong\\\" type。这验证了 multi-channel model 的 Channel 1 预测： Recall 从 0.368 跃升至 0.585 (+21.7pp)，因为每个 prompt 只需关注一个类型， attention 不被稀释，不遗漏。但 Precision 从 0.563 崩溃到 0.195 (-36.8pp)—— 66 个 batch 的 union merge 引入大量冲突：同一 text span 被 person-scholar、 person-scientist、person-other 各自 \\\"认领\\\"，union merge 保留所有 predictions， precision 崩溃。F1 净效果为负 (-15.5pp)。 MAVEN 168 types 更极端——recall 高但 precision 更低（0.085），因为 168 个 single-type  batch 的 merge 冲突呈 O(k²) 增长。 这清晰展示了 decomposition 的 fundamental tradeoff：分解减少 miss (Channel 1 benefit)， 但 merge 产生 false positives (new Channel 3 problem)。当前所有 merge strategy  （union, confidence-gated）都不能解决 O(k) batches 的冲突。\\n\"\n  },\n  {\n    \"name\": \"SCS Validation\",\n    \"description\": \"Spearman/Kendall correlation between embedding SCS 和 empirical confusion matrix\",\n    \"results\": {\n      \"all_pairs\": {\n        \"n\": 1953,\n        \"qwen3_spearman\": 0.168,\n        \"qwen3_p\": \"7.3e-14\",\n        \"qwen3_kendall\": 0.135,\n        \"minilm_spearman\": 0.144,\n        \"minilm_p\": \"1.7e-10\",\n        \"minilm_kendall\": 0.115\n      },\n      \"nonzero_only\": {\n        \"n\": 216,\n        \"qwen3_spearman\": 0.272,\n        \"qwen3_p\": \"5.0e-5\",\n        \"qwen3_kendall\": 0.2,\n        \"minilm_spearman\": 0.306,\n        \"minilm_p\": \"4.6e-6\",\n        \"minilm_kendall\": 0.228\n      },\n      \"variance_explained\": {\n        \"all_pairs_r_squared\": \"2.8-4.8%\",\n        \"nonzero_r_squared\": \"7.4-9.4%\"\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: SCS → Empirical Confusion Validation\",\n        \"content\": \"| Subset        | Embedding | Spearman ρ | p        | Kendall τ | R²     |\\n|---------------|-----------|------------|----------|-----------|--------|\\n| All (n=1953)  | Qwen3     | 0.168      | 7.3e-14  | 0.135     | ~4.8%  |\\n| All (n=1953)  | MiniLM    | 0.144      | 1.7e-10  | 0.115     | ~2.8%  |\\n| Nonzero (216) | Qwen3     | 0.272      | 5.0e-5   | 0.200     | ~7.4%  |\\n| Nonzero (216) | MiniLM    | 0.306      | 4.6e-6   | 0.228     | ~9.4%  |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"SCS validation 支撑了 \\\"confusability signal exists\\\" 但也暴露了 \\\"signal is weak for  practical use\\\"。这与 SDGD 的负面结果形成一致叙事：pairwise SCS 作为分析工具有效 （cross-task 显著），作为工程工具不足（R²太低）。论文应诚实呈现这个 gap，并将  SDGD-cal (bypassing embedding entirely) 作为 pragmatic 替代方案。 Reviewer 可能追问 AUC（SCS 预测 nonzero confusion 的分类能力），预估 AUC≈0.65-0.70， 属于 \\\"above chance but far from reliable\\\" 水平。\\n\\nSCS 是有效但不完美的 confusion proxy。All-pairs ρ 偏低（0.14-0.17）的根本原因是  data 极度 zero-inflated：88.9% 的 type pairs 从未被混淆（confusion=0），产生大量  ties 压缩 rank correlation。Nonzero-only ρ 跳升到 0.27-0.31，说明 SCS 能有效区分  \\\"哪些 pairs 被混淆得更多\\\" 但不太能预测 \\\"哪些 pairs 会被混淆\\\"。 Qwen3 在 all-pairs 上更好（ρ=0.168 vs 0.144）——extraction model 的 embedding  更好地捕捉 \\\"是否会混淆\\\" 的 threshold，因为 embedding space 与 model 的 internal  representation 对齐。MiniLM 在 nonzero-only 上更好（ρ=0.306 vs 0.272）——sentence  similarity model 的 fine-grained similarity gradient 更平滑，更好地排序 confusion  程度。 Median 档位下，reviewer 的主要质疑是 R²=3-5%：如果你的 proxy 只解释 3-5% 的方差， 基于它构建的 SDGD 分组怎么可能有效？这恰好与 SDGD-zero 的失败一致——SCS 作为 grouping  signal 太 noisy。论文应将此定位为 \\\"validating the existence of the signal\\\" 而非  \\\"validating its practical sufficiency\\\"，并指向 SDGD-cal (empirical confusion)  作为正确的 operationalization 路径。\\n\"\n  }\n]",
      "numLines": 337,
      "startLine": 1,
      "totalLines": 337
    }
  },
  "sourceToolAssistantUUID": "c3bae5ee-bc53-406c-8a1f-f25d1d145454",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "4d779de5-396b-49dc-acca-1976fdd39e66",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-16T07:58:18.233Z_

<details><summary>↩ Tool result · `toolu_01PM8oF1ZpEuUYFBcnbfJuTa`</summary>

```text
1	# Paper Framing — schema-dag-extraction
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (ARR May 25 cycle)
5	- Commitment deadline: August 2, 2026
6	- Fallback: EMNLP 2026 Findings (same ARR cycle, commitment August 26)
7	- Deadline: ARR May 25, 2026 (10 days from today)
8	
9	## Core Claims (2 claims) — Revised per D019
10	
11	1. **Confusability Independence**: Type confusability independently predicts extraction quality degradation in training-free LLM IE, beyond what type count alone explains. The signal is strongest and most robust at the **type-pair level** (pairwise SCS → confusion), validated across NER (Few-NERD), RE (FewRel), and ED (MAVEN with MiniLM). Per-type aggregation (mean BCS) introduces a centrality confound in semantically homogeneous schemas. The effect amplifies with schema complexity (3.4× between 16-type and 80-type schemas). Evidence required: (a) significant pairwise SCS-confusion correlation on >=2 datasets, (b) BCS-controlled accuracy gap on FewRel, (c) >=2 models.
12	
13	2. **Multi-Channel Degradation**: Count and confusability degrade extraction through orthogonal channels -- count causes entity omission (recall decline), while confusability causes type confusion errors (correct spans labeled with wrong types). Cross-task validated: NER IntraSub ρ=1.0, RE IntraSub ρ=0.954. Evidence required: error taxonomy showing differential error types per channel, monotonic trends in separate metrics.
14	
15	~~3. **SDGD Effectiveness**~~ — **DROPPED (D019)**: SDGD-zero v1 F1=0.251, v2 F1=0.241, both far below single-pass baseline 0.445. Merge amplification is an intrinsic challenge of schema decomposition that merge strategies (union+dedup, confidence-gated) cannot resolve. **Discussed as negative result + future work direction** — "why naive decomposition fails" is itself a contribution.
16	
17	## Story Spine — Revised per D012
18	
19	- **Problem**: Training-free LLM IE degrades severely on complex schemas (20-60 F1 gap vs supervised). All existing decomposition approaches operate on unvalidated assumptions about WHAT makes schemas complex for LLMs.
20	
21	- **Existing approaches & their gaps**: UniNER splits per-type (gains 3.3 F1 but loses cross-type context, no criterion for when to split). LLM-PEE uses similarity as implicit confusability proxy (never validated empirically). No prior work isolates confusability from count, or characterizes when aggregated confusability measures lose signal.
22	
23	- **Our framing**: We conduct the first controlled empirical study isolating type confusability from type count in training-free LLM IE across three tasks (NER, RE, ED). We discover: (1) a multi-channel degradation model (count→recall, confusability→type confusion), (2) pairwise type confusability is a robust cross-task signal that amplifies with schema complexity, (3) per-type aggregation of confusability is confounded by type centrality in homogeneous schemas. We further show that naive confusability-aware decomposition (SDGD) fails due to merge amplification — a structural challenge that points to calibration-based approaches as future work.
24	
25	- **Three-task validation**:
26	  - NER (Few-NERD, 66 types, cross-domain): Pairwise r=0.112 [0.076, 0.156] (n=1953), per-type ρ=-0.293 [-0.492, -0.054] (p=0.02), 10-28x confusion ratio
27	  - RE (FewRel, 80 relations, cross-domain): BCS-controlled Δ=-31.2pp (80-rel formal); count curve acc 85.7%→50.4%; BCS effect scales 3.4x vs 16-rel
28	  - ED (MAVEN, 168 event types, same-domain): Pairwise MiniLM r=0.120 (p≈0); per-type positive (centrality confound case study)
29	
30	- **Headline result template**: "Pairwise type confusability independently predicts extraction degradation across NER, RE, and ED tasks (r=0.11-0.13, all CIs exclude zero), with 10-28x more type confusion errors in high-confusability batches. The effect amplifies with schema complexity: 3.4× stronger BCS effect on 80-type vs 16-type schemas (Δ=-31.2pp vs -9.1pp). On semantically homogeneous schemas, per-type aggregation obscures the signal through centrality confounding, but pairwise confusability remains valid."
31	
32	## Core Insight — Multi-Channel Degradation + Pairwise Robustness
33	
34	Schema-induced degradation in LLM IE is not a single phenomenon but a multi-channel process:
35	- **Channel 1 (Count -> Recall)**: More types in the prompt → attention dilution → entities missed. Monotonic, near-linear. Addressable by reducing batch size.
36	- **Channel 2 (Confusability -> Type Confusion)**: Semantically similar co-present types → interference during type assignment → correct entities labeled with wrong types. Addressable by separating confusable types into different batches.
37	
38	These channels are orthogonal and independently addressable.
39	
40	**Pairwise vs Aggregated Confusability**:
41	- **Pairwise confusability** (SCS between type pairs) is robust across all tasks and schema types. Validated on Few-NERD (Qwen3, r=0.112 [0.076, 0.156]) and MAVEN (MiniLM, r=0.129 [0.104, 0.156]). SCS validated as effective confusion proxy: Qwen3 ρ=0.168 (p=7e-14), MiniLM ρ=0.306 nonzero-only (p=5e-6).
42	- **Per-type aggregation** (mean BCS = average pairwise similarity to all other types) introduces a centrality confound: in semantically homogeneous schemas (MAVEN), types with many semantic neighbors are central, well-represented types that LLMs extract well → positive correlation (high mean BCS → high F1), masking the pairwise confusability signal.
43	- **SDGD operates at pairwise level**, directly using the validated signal to construct the confusability graph for decomposition. It avoids the aggregation confound entirely.
44	
45	## Evidence Hierarchy (D012)
46	
47	### Tier 1: PRIMARY — Pairwise SCS → Confusion
48	
49	The cleanest evidence. Directly measures: are semantically similar type pairs more often confused?
50	
51	**Few-NERD (NER)** — Qwen3 embeddings:
52	- Pearson r=0.112 [0.076, 0.156] (n=1953 type pairs) — corrected via bootstrap recomputation
53	- Nonzero-only Spearman ρ=0.272 (p=5e-5)
54	- Top confused pairs are all high-BCS semantic neighbors (person-other ↔ person-politician, BCS=0.934)
55	- Immune to type frequency confound (operates at type-pair level)
56	
57	**MAVEN (ED)** — MiniLM embeddings:
58	- Pearson r=+0.129 [0.104, 0.156] (n=11026 type pairs) — corrected via bootstrap
59	- Nonzero-only Spearman ρ=+0.191 (p<0.001)
60	- Cross-task replication on same-domain schema
61	- Note: Qwen3 pairwise not significant on MAVEN (r=-0.007, p=0.41) — embedding choice matters for pairwise signal in homogeneous schemas
62	
63	### Tier 2: STRONG SECONDARY — FewRel Cross-Task Replication
64	
65	Large effect size, cross-task (RE), scaling with schema complexity:
66	
67	**Formal 80-rel study** (exp_fewrel_formal_80rel):
68	- Count curve: acc 85.7% (count=1) → 50.4% (count=80), BCS 0→0.97
69	- BCS-controlled: count_8 low-BCS 82.3% vs high-BCS 51.0% (Δ=-31.2pp)
70	- BCS-controlled: count_16 low-BCS 82.8% vs high-BCS 51.6% (Δ=-31.2pp)
71	- **Scaling**: vs 16-rel, degradation 2.8x (35.3pp vs 12.6pp), BCS effect 3.4x (-31.2pp vs -9.1pp)
72	
73	**16-rel sanity check** (exp_fewrel_formal):
74	- count_8: low-BCS 88.9% vs high-BCS 79.8% (Δ=-9.1pp)
75	
76	**Pilot extreme batches** (fewrel_pilot, MiniLM):
77	- count_4: Δ=-20.9pp, count_8: Δ=-50.0pp, count_16: Δ=-48.6pp
78	
79	Key insight: confusability effect amplifies with schema size — direct evidence for multi-channel degradation scaling
80	
81	### Tier 3: SUPPORTING — Few-NERD Per-type Analysis
82	
83	Bridges pairwise and batch-level, demonstrates per-type signal in cross-domain schema:
84	- Spearman ρ=-0.293 (p=0.020, n=63 types, freq≥5) — Qwen3 embeddings
85	- Partial r=-0.200 (p=0.116) controlling for log-frequency
86	- Quartile comparison: high-BCS types F1=0.228 vs low-BCS F1=0.310 (Δ=-8.2pp)
87	- BCS-frequency uncorrelated at type level (r=0.042, p=0.74)
88	- MiniLM per-type: ρ≈0 (p=0.97) — extraction model alignment required for per-type signal
89	
90	### Tier 4: DISCUSSION — MAVEN Per-type Centrality Confound
91	
92	Methodological case study on when aggregated confusability measures fail:
93	- Qwen3 per-type: ρ=+0.189 (p=0.021) — OPPOSITE direction
94	- MiniLM per-type: ρ=+0.208 (p=0.011) — ALSO positive, ruling out embedding compression as sole explanation
95	- Both embeddings agree: positive direction on MAVEN is an intrinsic property of the type structure
96	- Explanation: in homogeneous schemas, mean BCS conflates confusability with type centrality (types with many semantic neighbors → common/central types → higher F1)
97	- This is stronger than "domain boundary" — it identifies the specific mechanism (aggregation confound) rather than just the boundary condition
98	
99	### Tier 5: MECHANISTIC — Error Taxonomy (Cross-Task)
100	
101	IntraSub rate monotonically increases with BCS on both NER and RE:
102	
103	**Few-NERD (NER, exp-007)**: IntraSub 0%→1.6%→10.6%→49.4%, ρ=1.0
104	**FewRel 80-rel (RE)**: IntraSub 0%→4.2%→13.0%→20.3%→32.3%, ρ=0.954 (p=0.0, n=154 batches)
105	- extra_sub=0 on both tasks — type confusion is purely intra-batch phenomenon
106	- Same mechanism, different absolute magnitudes — consistent with cross-task expectations
107	
108	Additional from extreme batch design:
109	- Extreme batches: high-BCS 10-28x more type confusion errors vs low-BCS
110	- Random batches: 1.7-2.4x ratio (still significant, smaller effect)
111	
112	## Embedding Ablation (D010)
113	
114	2×3 matrix: {Qwen3, MiniLM} × {Few-NERD, FewRel, MAVEN}
115	
116	### Per-type (Layer 2)
117	| | Few-NERD | FewRel | MAVEN |
118	|---|---|---|---|
119	| Qwen3 | ρ=-0.293 ✓ | pending | ρ=+0.189 ✗ |
120	| MiniLM | ρ≈0 ✗ | Δ=21-50pp ✓ | ρ=+0.208 ✗ |
121	
122	### Pairwise (Layer 1)
123	| | Few-NERD | MAVEN |
124	|---|---|---|
125	| Qwen3 | r=0.112 [0.076,0.156] ✓ | r=-0.007 ✗ |
126	| MiniLM | — | r=+0.129 [0.104,0.156] ✓ |
127	
128	### SCS→Empirical Confusion Validation (exp-015 fast)
129	| | Qwen3 | MiniLM |
130	|---|---|---|
131	| All pairs ρ | 0.168 (p=7e-14) ✓ | 0.144 (p=2e-10) ✓ |
132	| Nonzero-only ρ | 0.272 (p=5e-5) | 0.306 (p=5e-6) ✓ |
133	
134	**Interpretation**: No single embedding dominates. Extraction-model embeddings (Qwen3) capture per-type confusability in cross-domain schemas. Generic embeddings (MiniLM) capture pairwise confusability in same-domain schemas. SDGD should use task-appropriate embeddings; SDGD-cal (empirical confusion) bypasses embedding choice entirely.
135	
136	## Venue Fit Risks
137	
138	- **"Just an empirical study"**: Mitigated by SDGD as direct operationalization. Controlled experimental design parallels "Lost in the Middle" (TACL 2024).
139	- **Training-free IE relevance**: Cite deployment scenarios — clinical, regulatory, multilingual.
140	- **Multi-model generalizability**: Qwen3-32B primary + LLaMA-3.3-70B (exp-012).
141	- **MAVEN doesn't support hypothesis?**: Pairwise MiniLM does support it. Per-type centrality confound is methodological contribution, not failure.
142	- **Embedding sensitivity**: 2×3 ablation matrix is itself a contribution — characterizes when which proxy works.
143	
144	## Anticipated Reviewer Concerns
145	
146	| Concern | Response Strategy | Experiment |
147	|---------|------------------|------------|
148	| Only one model | LLaMA-3.3-70B replication | exp-012 |
149	| Cross-task replication | Pairwise: Few-NERD ✓ + MAVEN MiniLM ✓. Batch: FewRel ✓. Three tasks. | exp-002, exp-004, fewrel |
150	| No practical method | SDGD framework (-zero, -cal) | exp-008 to exp-011 |
151	| Confusability measure validity | Embedding ablation (D010) + pairwise vs per-type analysis | D010, exp-015 |
152	| Effect size small | Pairwise r=0.12-0.16 + FewRel Δ=21-50pp + confusion ratio 10-28x | multiple |
153	| MAVEN per-type opposite | Centrality confound analysis; pairwise still works | MAVEN MiniLM |
154	| Embedding choice matters? | 2×3 ablation table; SDGD-cal bypasses embedding entirely | D010 |
155	| Why not per-type splitting? | SDGD vs per-type vs random ablation | exp-013, exp-014 |
156	| Latency overhead | Report API calls and wall-clock time | exp-008 |
157	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "356606e2-38c5-46ed-bedd-02bb5110fadb",
  "isSidechain": false,
  "promptId": "fc49f735-e722-4cc2-9426-bb861b70dea7",
  "type": "user",
  "uuid": "eab0a797-34cd-48e9-bdf5-39b63aff603e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/median/paper_framing.md",
      "content": "# Paper Framing — schema-dag-extraction\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25 cycle)\n- Commitment deadline: August 2, 2026\n- Fallback: EMNLP 2026 Findings (same ARR cycle, commitment August 26)\n- Deadline: ARR May 25, 2026 (10 days from today)\n\n## Core Claims (2 claims) — Revised per D019\n\n1. **Confusability Independence**: Type confusability independently predicts extraction quality degradation in training-free LLM IE, beyond what type count alone explains. The signal is strongest and most robust at the **type-pair level** (pairwise SCS → confusion), validated across NER (Few-NERD), RE (FewRel), and ED (MAVEN with MiniLM). Per-type aggregation (mean BCS) introduces a centrality confound in semantically homogeneous schemas. The effect amplifies with schema complexity (3.4× between 16-type and 80-type schemas). Evidence required: (a) significant pairwise SCS-confusion correlation on >=2 datasets, (b) BCS-controlled accuracy gap on FewRel, (c) >=2 models.\n\n2. **Multi-Channel Degradation**: Count and confusability degrade extraction through orthogonal channels -- count causes entity omission (recall decline), while confusability causes type confusion errors (correct spans labeled with wrong types). Cross-task validated: NER IntraSub ρ=1.0, RE IntraSub ρ=0.954. Evidence required: error taxonomy showing differential error types per channel, monotonic trends in separate metrics.\n\n~~3. **SDGD Effectiveness**~~ — **DROPPED (D019)**: SDGD-zero v1 F1=0.251, v2 F1=0.241, both far below single-pass baseline 0.445. Merge amplification is an intrinsic challenge of schema decomposition that merge strategies (union+dedup, confidence-gated) cannot resolve. **Discussed as negative result + future work direction** — \"why naive decomposition fails\" is itself a contribution.\n\n## Story Spine — Revised per D012\n\n- **Problem**: Training-free LLM IE degrades severely on complex schemas (20-60 F1 gap vs supervised). All existing decomposition approaches operate on unvalidated assumptions about WHAT makes schemas complex for LLMs.\n\n- **Existing approaches & their gaps**: UniNER splits per-type (gains 3.3 F1 but loses cross-type context, no criterion for when to split). LLM-PEE uses similarity as implicit confusability proxy (never validated empirically). No prior work isolates confusability from count, or characterizes when aggregated confusability measures lose signal.\n\n- **Our framing**: We conduct the first controlled empirical study isolating type confusability from type count in training-free LLM IE across three tasks (NER, RE, ED). We discover: (1) a multi-channel degradation model (count→recall, confusability→type confusion), (2) pairwise type confusability is a robust cross-task signal that amplifies with schema complexity, (3) per-type aggregation of confusability is confounded by type centrality in homogeneous schemas. We further show that naive confusability-aware decomposition (SDGD) fails due to merge amplification — a structural challenge that points to calibration-based approaches as future work.\n\n- **Three-task validation**:\n  - NER (Few-NERD, 66 types, cross-domain): Pairwise r=0.112 [0.076, 0.156] (n=1953), per-type ρ=-0.293 [-0.492, -0.054] (p=0.02), 10-28x confusion ratio\n  - RE (FewRel, 80 relations, cross-domain): BCS-controlled Δ=-31.2pp (80-rel formal); count curve acc 85.7%→50.4%; BCS effect scales 3.4x vs 16-rel\n  - ED (MAVEN, 168 event types, same-domain): Pairwise MiniLM r=0.120 (p≈0); per-type positive (centrality confound case study)\n\n- **Headline result template**: \"Pairwise type confusability independently predicts extraction degradation across NER, RE, and ED tasks (r=0.11-0.13, all CIs exclude zero), with 10-28x more type confusion errors in high-confusability batches. The effect amplifies with schema complexity: 3.4× stronger BCS effect on 80-type vs 16-type schemas (Δ=-31.2pp vs -9.1pp). On semantically homogeneous schemas, per-type aggregation obscures the signal through centrality confounding, but pairwise confusability remains valid.\"\n\n## Core Insight — Multi-Channel Degradation + Pairwise Robustness\n\nSchema-induced degradation in LLM IE is not a single phenomenon but a multi-channel process:\n- **Channel 1 (Count -> Recall)**: More types in the prompt → attention dilution → entities missed. Monotonic, near-linear. Addressable by reducing batch size.\n- **Channel 2 (Confusability -> Type Confusion)**: Semantically similar co-present types → interference during type assignment → correct entities labeled with wrong types. Addressable by separating confusable types into different batches.\n\nThese channels are orthogonal and independently addressable.\n\n**Pairwise vs Aggregated Confusability**:\n- **Pairwise confusability** (SCS between type pairs) is robust across all tasks and schema types. Validated on Few-NERD (Qwen3, r=0.112 [0.076, 0.156]) and MAVEN (MiniLM, r=0.129 [0.104, 0.156]). SCS validated as effective confusion proxy: Qwen3 ρ=0.168 (p=7e-14), MiniLM ρ=0.306 nonzero-only (p=5e-6).\n- **Per-type aggregation** (mean BCS = average pairwise similarity to all other types) introduces a centrality confound: in semantically homogeneous schemas (MAVEN), types with many semantic neighbors are central, well-represented types that LLMs extract well → positive correlation (high mean BCS → high F1), masking the pairwise confusability signal.\n- **SDGD operates at pairwise level**, directly using the validated signal to construct the confusability graph for decomposition. It avoids the aggregation confound entirely.\n\n## Evidence Hierarchy (D012)\n\n### Tier 1: PRIMARY — Pairwise SCS → Confusion\n\nThe cleanest evidence. Directly measures: are semantically similar type pairs more often confused?\n\n**Few-NERD (NER)** — Qwen3 embeddings:\n- Pearson r=0.112 [0.076, 0.156] (n=1953 type pairs) — corrected via bootstrap recomputation\n- Nonzero-only Spearman ρ=0.272 (p=5e-5)\n- Top confused pairs are all high-BCS semantic neighbors (person-other ↔ person-politician, BCS=0.934)\n- Immune to type frequency confound (operates at type-pair level)\n\n**MAVEN (ED)** — MiniLM embeddings:\n- Pearson r=+0.129 [0.104, 0.156] (n=11026 type pairs) — corrected via bootstrap\n- Nonzero-only Spearman ρ=+0.191 (p<0.001)\n- Cross-task replication on same-domain schema\n- Note: Qwen3 pairwise not significant on MAVEN (r=-0.007, p=0.41) — embedding choice matters for pairwise signal in homogeneous schemas\n\n### Tier 2: STRONG SECONDARY — FewRel Cross-Task Replication\n\nLarge effect size, cross-task (RE), scaling with schema complexity:\n\n**Formal 80-rel study** (exp_fewrel_formal_80rel):\n- Count curve: acc 85.7% (count=1) → 50.4% (count=80), BCS 0→0.97\n- BCS-controlled: count_8 low-BCS 82.3% vs high-BCS 51.0% (Δ=-31.2pp)\n- BCS-controlled: count_16 low-BCS 82.8% vs high-BCS 51.6% (Δ=-31.2pp)\n- **Scaling**: vs 16-rel, degradation 2.8x (35.3pp vs 12.6pp), BCS effect 3.4x (-31.2pp vs -9.1pp)\n\n**16-rel sanity check** (exp_fewrel_formal):\n- count_8: low-BCS 88.9% vs high-BCS 79.8% (Δ=-9.1pp)\n\n**Pilot extreme batches** (fewrel_pilot, MiniLM):\n- count_4: Δ=-20.9pp, count_8: Δ=-50.0pp, count_16: Δ=-48.6pp\n\nKey insight: confusability effect amplifies with schema size — direct evidence for multi-channel degradation scaling\n\n### Tier 3: SUPPORTING — Few-NERD Per-type Analysis\n\nBridges pairwise and batch-level, demonstrates per-type signal in cross-domain schema:\n- Spearman ρ=-0.293 (p=0.020, n=63 types, freq≥5) — Qwen3 embeddings\n- Partial r=-0.200 (p=0.116) controlling for log-frequency\n- Quartile comparison: high-BCS types F1=0.228 vs low-BCS F1=0.310 (Δ=-8.2pp)\n- BCS-frequency uncorrelated at type level (r=0.042, p=0.74)\n- MiniLM per-type: ρ≈0 (p=0.97) — extraction model alignment required for per-type signal\n\n### Tier 4: DISCUSSION — MAVEN Per-type Centrality Confound\n\nMethodological case study on when aggregated confusability measures fail:\n- Qwen3 per-type: ρ=+0.189 (p=0.021) — OPPOSITE direction\n- MiniLM per-type: ρ=+0.208 (p=0.011) — ALSO positive, ruling out embedding compression as sole explanation\n- Both embeddings agree: positive direction on MAVEN is an intrinsic property of the type structure\n- Explanation: in homogeneous schemas, mean BCS conflates confusability with type centrality (types with many semantic neighbors → common/central types → higher F1)\n- This is stronger than \"domain boundary\" — it identifies the specific mechanism (aggregation confound) rather than just the boundary condition\n\n### Tier 5: MECHANISTIC — Error Taxonomy (Cross-Task)\n\nIntraSub rate monotonically increases with BCS on both NER and RE:\n\n**Few-NERD (NER, exp-007)**: IntraSub 0%→1.6%→10.6%→49.4%, ρ=1.0\n**FewRel 80-rel (RE)**: IntraSub 0%→4.2%→13.0%→20.3%→32.3%, ρ=0.954 (p=0.0, n=154 batches)\n- extra_sub=0 on both tasks — type confusion is purely intra-batch phenomenon\n- Same mechanism, different absolute magnitudes — consistent with cross-task expectations\n\nAdditional from extreme batch design:\n- Extreme batches: high-BCS 10-28x more type confusion errors vs low-BCS\n- Random batches: 1.7-2.4x ratio (still significant, smaller effect)\n\n## Embedding Ablation (D010)\n\n2×3 matrix: {Qwen3, MiniLM} × {Few-NERD, FewRel, MAVEN}\n\n### Per-type (Layer 2)\n| | Few-NERD | FewRel | MAVEN |\n|---|---|---|---|\n| Qwen3 | ρ=-0.293 ✓ | pending | ρ=+0.189 ✗ |\n| MiniLM | ρ≈0 ✗ | Δ=21-50pp ✓ | ρ=+0.208 ✗ |\n\n### Pairwise (Layer 1)\n| | Few-NERD | MAVEN |\n|---|---|---|\n| Qwen3 | r=0.112 [0.076,0.156] ✓ | r=-0.007 ✗ |\n| MiniLM | — | r=+0.129 [0.104,0.156] ✓ |\n\n### SCS→Empirical Confusion Validation (exp-015 fast)\n| | Qwen3 | MiniLM |\n|---|---|---|\n| All pairs ρ | 0.168 (p=7e-14) ✓ | 0.144 (p=2e-10) ✓ |\n| Nonzero-only ρ | 0.272 (p=5e-5) | 0.306 (p=5e-6) ✓ |\n\n**Interpretation**: No single embedding dominates. Extraction-model embeddings (Qwen3) capture per-type confusability in cross-domain schemas. Generic embeddings (MiniLM) capture pairwise confusability in same-domain schemas. SDGD should use task-appropriate embeddings; SDGD-cal (empirical confusion) bypasses embedding choice entirely.\n\n## Venue Fit Risks\n\n- **\"Just an empirical study\"**: Mitigated by SDGD as direct operationalization. Controlled experimental design parallels \"Lost in the Middle\" (TACL 2024).\n- **Training-free IE relevance**: Cite deployment scenarios — clinical, regulatory, multilingual.\n- **Multi-model generalizability**: Qwen3-32B primary + LLaMA-3.3-70B (exp-012).\n- **MAVEN doesn't support hypothesis?**: Pairwise MiniLM does support it. Per-type centrality confound is methodological contribution, not failure.\n- **Embedding sensitivity**: 2×3 ablation matrix is itself a contribution — characterizes when which proxy works.\n\n## Anticipated Reviewer Concerns\n\n| Concern | Response Strategy | Experiment |\n|---------|------------------|------------|\n| Only one model | LLaMA-3.3-70B replication | exp-012 |\n| Cross-task replication | Pairwise: Few-NERD ✓ + MAVEN MiniLM ✓. Batch: FewRel ✓. Three tasks. | exp-002, exp-004, fewrel |\n| No practical method | SDGD framework (-zero, -cal) | exp-008 to exp-011 |\n| Confusability measure validity | Embedding ablation (D010) + pairwise vs per-type analysis | D010, exp-015 |\n| Effect size small | Pairwise r=0.12-0.16 + FewRel Δ=21-50pp + confusion ratio 10-28x | multiple |\n| MAVEN per-type opposite | Centrality confound analysis; pairwise still works | MAVEN MiniLM |\n| Embedding choice matters? | 2×3 ablation table; SDGD-cal bypasses embedding entirely | D010 |\n| Why not per-type splitting? | SDGD vs per-type vs random ablation | exp-013, exp-014 |\n| Latency overhead | Report API calls and wall-clock time | exp-008 |\n",
      "numLines": 157,
      "startLine": 1,
      "totalLines": 157
    }
  },
  "sourceToolAssistantUUID": "356606e2-38c5-46ed-bedd-02bb5110fadb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "4d779de5-396b-49dc-acca-1976fdd39e66",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T073533 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extr…",
  "leafUuid": "76b93b2b-6348-42d9-b8b6-809b0a475f6a",
  "sessionId": "4d779de5-396b-49dc-acca-1976fdd39e66"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper with LaTeX compilation",
  "sessionId": "4d779de5-396b-49dc-acca-1976fdd39e66"
}
```

---

### Assistant

_source line 14 · 2026-05-16T07:59:17.043Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now synthesize all this information and write a complete LaTeX paper. Let me organize the key elements:

**Title**: Something about schema confusability in training-free LLM information extraction

**Core Claims**:
1. Confusability Independence: Type confusability independently predicts extraction quality degradation
2. Multi-Channel Degradation: Count→recall decline, confusability→type confusion errors

**Experiments from experiment_data.json** (8 experiments):
1. DocRED Confusability Study - count curve + BCS controlled
2. Interaction Effect 2×2 - {low/high count} × {low/high BCS}


3. Error Taxonomy - FP classification across BCS bins
4. SDGD-zero on MAVEN - decomposition comparison
5. SDGD-cal on Few-NERD - calibration-based decomposition
6. SDGD-cal on MAVEN - calibration on MAVEN
7. Random Batching Ablation - random vs SDGD-zero
8. Per-type Splitting (UniNER-style) - one type per batch
9. SCS Validation - embedding SCS vs empirical confusion

**Narrative guidance** (median tier): Pairwise confusability signal re

-emerges across tasks but with modest effect sizes, FewRel's large performance drop is noteworthy though potentially RE-specific, and the error taxonomy holds up well. The SDGD results are consistently negative which is a significant limitation, LLaMA's struggles on Few-NERD raise generalizability concerns, and while MAVEN shows promise with per-type splitting I need a stronger argument about the confound. This positions the work somewhere between a solid findings paper and something needing substantial rebuttal to be publication-ready.

Now I'm structuring the paper outline starting with the abstract and introduction, moving through related work and the core methodology sections covering the multi-channel degradation model, schema confusability scoring, and the SDGD framework, then laying out the experiments beginning with the DocRED confusability study.

Looking back at the actual experiment data I have available—there are nine experiments total including the DocRED confusability study, the 2×2 interaction effect, error taxonomy validation, SDGD results across MAVEN and Few-NERD with different calibration approaches, an ablation on random batching, per-type splitting analysis, and SCS validation—which maps differently than what the paper framing initially suggested.

The framing references earlier experiments with specific quantitative results (like FewRel and Few-NERD findings) that aren't in my current dataset, so I need to be careful to only cite numbers that actually appear in the experiment_data.json while using the framing primarily for narrative context and structure. Looking at the experimental results across the datasets, I have nine key experiments to work with: DocRED shows a scaling pattern with controlled comparisons, Few-NERD reveals a non-significant interaction effect, and the error taxonomy analysis covers both NER and RE tasks. The SDGD experiments demonstrate consistent patterns where zero-shot and calibration approaches reduce error rates compared to baselines across MAVEN and Few-NERD, with random batching showing mixed results relative to the zero-shot method.

Per-type analysis shows a precision-recall tradeoff where Few-NERD maintains reasonable F1 but MAVEN suffers from precision collapse despite higher recall. For validation, I'm checking whether model-based similarity metrics from Qwen and MiniLM correlate with the actual confusion patterns observed empirically.

The framing numbers from earlier experiments establish the core theoretical claims, while the JSON and SDGD experiments provide practical validation. I'll structure the paper to use the JSON data for concrete numbers in tables and reference the established framing results with proper attribution to show how the practical methods align with the theoretical foundation.

Wait, rereading the constraints more carefully—every quantitative claim needs to be grounded in the JSON data, and each experiment in the JSON needs its own section or table. The framing is narrative guidance, not a data source. So I should focus the paper entirely on what's in the JSON, using the framing only to shape how I present that evidence.

Looking at what's actually available: the JSON contains DocRED validation results and the SDGD/practical method experiments, while the framing references earlier results like Few-NERD pairwise correlations and FewRel performance deltas. These framing numbers are core to the argument but aren't in the JSON itself.

The Error Taxonomy does include FewRel data, and the SCS Validation has Few-NERD results, so some of the key evidence is there—just organized differently than the framing suggests. But the specific numbers from the framing (the 85.7%→50.4% curve, the -31.2pp delta, the r=0.112 correlation) don't appear in the JSON.

I think the right approach is to build the paper around the nine experiments that are actually in the JSON, using the framing as a guide for how to structure and narrate those results. Let me map out the paper structure based on what's available.

For the abstract, I'm capturing the core narrative: a multi-channel degradation model where count and confusability independently drive performance loss, with SDGD explored as a negative result. The introduction sets up why training-free LLM IE struggles on complex schemas. Then I move into the model itself—laying out the two channels, introducing the Schema Confusability Score, and describing the SDGD framework. The experiments section starts with setup, then walks through the DocRED confusability study with the count curve and BCS-controlled analysis, followed by the error taxonomy as mechanical evidence.

Now I'm detailing the remaining experiments: validating SCS through embedding comparisons against empirical confusion patterns, testing the interaction between count and confusability with a 2×2 design, and then the schema decomposition experiments across multiple datasets and ablation conditions. The discussion addresses why SDGD didn't work as expected, the centrality confound issue, and key limitations before wrapping up.

I'm noticing the FewRel data appears in the error taxonomy table and is mentioned throughout the framing, though I need to clarify exactly which FewRel counts are being referenced in that specific analysis.

I'll anchor the paper strictly to what's in the JSON data and avoid citing numbers that aren't there. The narrative will stay coherent by focusing on the experiments and results that are actually documented. Now I'm ready to write out the full paper, making sure every experiment gets proper coverage, all numbers come directly from the JSON, and the writing follows the findings-level framing without referencing the guidance itself.

Writing the LaTeX paper...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eab0a797-34cd-48e9-bdf5-39b63aff603e",
  "isSidechain": false,
  "requestId": "req_011Cb5tjFAf3Wx6qdCt1Zy35",
  "type": "assistant",
  "uuid": "ae9201a0-c03d-4fc3-bcb0-b20bd4a70081",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "4d779de5-396b-49dc-acca-1976fdd39e66",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016yxtf7Lwa6ytKdQLj6dLh2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15170,
      "cache_read_input_tokens": 23049,
      "output_tokens": 3084,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15170,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3084,
          "cache_read_input_tokens": 23049,
          "cache_creation_input_tokens": 15170,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15170
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

_source line 15 · 2026-05-16T07:59:17.178Z_

Let me check the output directory exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae9201a0-c03d-4fc3-bcb0-b20bd4a70081",
  "isSidechain": false,
  "requestId": "req_011Cb5tjFAf3Wx6qdCt1Zy35",
  "type": "assistant",
  "uuid": "ff38cb55-b5e1-4002-a79b-7937cdc2f046",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "4d779de5-396b-49dc-acca-1976fdd39e66",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016yxtf7Lwa6ytKdQLj6dLh2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15170,
      "cache_read_input_tokens": 23049,
      "output_tokens": 3084,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15170,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3084,
          "cache_read_input_tokens": 23049,
          "cache_creation_input_tokens": 15170,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15170
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

_source line 16 · 2026-05-16T07:59:19.073Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01LYb9AQ92VV6Axq8NdyfQn9`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/median/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
  "description": "Check output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff38cb55-b5e1-4002-a79b-7937cdc2f046",
  "isSidechain": false,
  "requestId": "req_011Cb5tjFAf3Wx6qdCt1Zy35",
  "type": "assistant",
  "uuid": "d6491fd3-2e1b-421c-a737-86ed8dce9282",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "4d779de5-396b-49dc-acca-1976fdd39e66",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016yxtf7Lwa6ytKdQLj6dLh2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15170,
      "cache_read_input_tokens": 23049,
      "output_tokens": 3084,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15170,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3084,
          "cache_read_input_tokens": 23049,
          "cache_creation_input_tokens": 15170,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15170
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

_source line 17 · 2026-05-16T07:59:19.242Z_

<details><summary>↩ Tool result · `toolu_01LYb9AQ92VV6Axq8NdyfQn9`</summary>

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
  "parentUuid": "d6491fd3-2e1b-421c-a737-86ed8dce9282",
  "isSidechain": false,
  "promptId": "fc49f735-e722-4cc2-9426-bb861b70dea7",
  "type": "user",
  "uuid": "9bc7720c-78b4-462c-ae5d-7f59037f2349",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "d6491fd3-2e1b-421c-a737-86ed8dce9282",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "4d779de5-396b-49dc-acca-1976fdd39e66",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-16T07:59:22.046Z_

<details><summary>Logged reasoning block</summary>

```text
Good, the directory exists. Let me now write the full LaTeX paper. I need to check if pdflatex and ACL style files are available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9bc7720c-78b4-462c-ae5d-7f59037f2349",
  "isSidechain": false,
  "requestId": "req_011Cb5tojoCji1WMLG94MHzE",
  "type": "assistant",
  "uuid": "06a28724-c7a7-4856-a6b9-2ccfe5f3865a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "4d779de5-396b-49dc-acca-1976fdd39e66",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013mnonryneAYMRSenFqWsUT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3110,
      "cache_read_input_tokens": 38219,
      "output_tokens": 155,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3110,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 155,
          "cache_read_input_tokens": 38219,
          "cache_creation_input_tokens": 3110,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3110
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

_source line 19 · 2026-05-16T07:59:22.204Z_

Now writing the full LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06a28724-c7a7-4856-a6b9-2ccfe5f3865a",
  "isSidechain": false,
  "requestId": "req_011Cb5tojoCji1WMLG94MHzE",
  "type": "assistant",
  "uuid": "daf44596-ad0d-4d92-ad50-d5432c8be48f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "4d779de5-396b-49dc-acca-1976fdd39e66",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013mnonryneAYMRSenFqWsUT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3110,
      "cache_read_input_tokens": 38219,
      "output_tokens": 155,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3110,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 155,
          "cache_read_input_tokens": 38219,
          "cache_creation_input_tokens": 3110,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3110
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

_source line 20 · 2026-05-16T07:59:22.840Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01T65iuAjzEU2ygK94MGS1w8`</summary>

```json
{
  "command": "which pdflatex 2>/dev/null && echo \"FOUND\" || echo \"NOT_FOUND\"",
  "description": "Check pdflatex availability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "daf44596-ad0d-4d92-ad50-d5432c8be48f",
  "isSidechain": false,
  "requestId": "req_011Cb5tojoCji1WMLG94MHzE",
  "type": "assistant",
  "uuid": "173e27d2-827e-4ff5-962b-de20bb1d4d88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "4d779de5-396b-49dc-acca-1976fdd39e66",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013mnonryneAYMRSenFqWsUT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3110,
      "cache_read_input_tokens": 38219,
      "output_tokens": 155,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3110,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 155,
          "cache_read_input_tokens": 38219,
          "cache_creation_input_tokens": 3110,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3110
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

_source line 21 · 2026-05-16T07:59:22.898Z_

<details><summary>↩ Tool result · `toolu_01T65iuAjzEU2ygK94MGS1w8`</summary>

```text
/usr/bin/pdflatex
FOUND
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "173e27d2-827e-4ff5-962b-de20bb1d4d88",
  "isSidechain": false,
  "promptId": "fc49f735-e722-4cc2-9426-bb861b70dea7",
  "type": "user",
  "uuid": "9a7029e2-6dd0-4d8d-8b9d-dc9f4ec8b8f7",
  "toolUseResult": {
    "stdout": "/usr/bin/pdflatex\nFOUND",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "173e27d2-827e-4ff5-962b-de20bb1d4d88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "4d779de5-396b-49dc-acca-1976fdd39e66",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-16T08:02:09.973Z_

<details open><summary>🔧 Tool call — Write · `toolu_01BzR1CtXaU75F7ycNsGBzPu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/median/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{natbib}\n\\bibliographystyle{plainnat}\n\n\\title{Multi-Channel Schema Degradation in Training-Free LLM Information Extraction:\\\\A Controlled Empirical Study}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%% ============================================================\n%% ABSTRACT\n%% ============================================================\n\\begin{abstract}\nTraining-free LLM-based information extraction (IE) degrades severely as schema complexity increases, yet the mechanisms behind this degradation remain poorly characterized.\nWe conduct a controlled empirical study isolating two independent factors---\\emph{type count} and \\emph{type confusability}---across three IE tasks: named entity recognition (NER on Few-NERD), relation extraction (RE on FewRel and DocRED), and event detection (ED on MAVEN).\nWe propose a \\textbf{multi-channel degradation model}: type count primarily causes entity omission (recall decline), while type confusability causes type confusion errors where correct spans are labeled with semantically similar but incorrect types.\nError taxonomy analysis reveals a near-perfect monotonic relationship between pairwise confusability and intra-batch type confusion rate across both NER ($\\rho{=}1.0$) and RE ($\\rho{=}0.954$).\nWe validate embedding-based Schema Confusability Scores (SCS) as significant predictors of empirical confusion ($\\rho{=}0.168$--$0.306$, all $p < 10^{-4}$), though with limited variance explained ($R^2{=}3$--$9\\%$).\nWe further investigate Schema-DAG Guided Decomposition (SDGD) as a practical mitigation, finding that all decomposition strategies---including confusability-aware grouping and calibration-based approaches---underperform a single-pass baseline due to \\emph{merge amplification}: the structural challenge of reconciling predictions from multiple schema partitions.\nThese negative results, combined with ablations showing random batching outperforming graph-coloring-based decomposition, identify merge strategy rather than grouping quality as the critical bottleneck for future work.\n\\end{abstract}\n\n%% ============================================================\n%% 1. INTRODUCTION\n%% ============================================================\n\\section{Introduction}\n\nLarge language models (LLMs) have shown remarkable zero-shot and few-shot capabilities on information extraction tasks when prompted with a target schema---a set of entity types, relation types, or event types to extract.\nHowever, performance degrades dramatically as schema complexity increases: extraction quality can drop 20--60 F1 points when moving from simple schemas ($<10$ types) to complex real-world schemas ($>50$ types), even when the underlying model remains the same.\n\nPrior work has proposed schema decomposition as a remedy. UniNER decomposes extraction into per-type prompts, gaining up to 3.3 F1 but losing cross-type context. LLM-PEE uses embedding similarity as an implicit confusability proxy to group types, but never empirically validates whether similarity actually predicts confusion. Critically, no prior work has \\emph{isolated} confusability from count, or characterized the distinct degradation mechanisms each factor induces.\n\nWe address this gap with three contributions:\n\n\\begin{enumerate}\n\\item \\textbf{Multi-channel degradation model.} We demonstrate that count and confusability operate through orthogonal channels: count primarily reduces recall (entities missed due to attention dilution), while confusability primarily reduces precision (correct entities assigned wrong types). Error taxonomy analysis across NER and RE shows perfect or near-perfect monotonic relationships ($\\rho{=}1.0$ and $\\rho{=}0.954$) between confusability and intra-batch type confusion rate.\n\n\\item \\textbf{Cross-task confusability validation.} We validate pairwise Schema Confusability Scores as significant predictors of empirical model confusion across NER and RE, and extend validation to document-level RE (DocRED, 96 relation types) where confusability effects persist despite additional confounds from cross-sentence reasoning.\n\n\\item \\textbf{Decomposition as negative result.} We systematically evaluate schema decomposition approaches---SDGD-zero (embedding-based graph coloring), SDGD-cal (calibration-based empirical grouping), random batching, and per-type splitting---across two datasets. All underperform single-pass extraction, identifying \\emph{merge amplification} as a structural bottleneck that grouping quality alone cannot overcome.\n\\end{enumerate}\n\n%% ============================================================\n%% 2. RELATED WORK\n%% ============================================================\n\\section{Related Work}\n\n\\paragraph{Training-free LLM IE.}\nRecent work has demonstrated that LLMs can perform zero-shot and few-shot information extraction by prompting with type definitions.\nGPT-NER and GoLLIE formulate NER as sequence generation; InstructUIE provides a unified prompt format across tasks.\nThese approaches share a common failure mode: performance degrades with schema complexity, yet the specific mechanisms remain uncharacterized.\n\n\\paragraph{Schema decomposition.}\nUniNER decomposes NER into per-type queries, improving recall at the cost of cross-type context.\nLLM-PEE groups entity types by embedding similarity, implicitly using confusability as a decomposition criterion without validating whether similarity predicts actual model confusion.\nOur work provides the missing empirical foundation: we validate the confusability signal and demonstrate why current decomposition approaches fail at the merge stage.\n\n\\paragraph{Prompt sensitivity in LLMs.}\nLost in the Middle showed that LLM performance varies with information position in long contexts.\nOur work extends this line of inquiry to schema composition: not just how much information is in the prompt, but which types co-occur and how their semantic similarity affects extraction.\n\n%% ============================================================\n%% 3. MULTI-CHANNEL DEGRADATION FRAMEWORK\n%% ============================================================\n\\section{Multi-Channel Degradation Framework}\n\nWe model schema-induced degradation in LLM IE as a multi-channel process with two independently addressable mechanisms.\n\n\\subsection{Channel 1: Count $\\rightarrow$ Recall Decline}\n\nAs the number of types in a single extraction prompt increases, the model's attention is diluted across more targets. This manifests as \\emph{entity omission}: entities that would be detected with fewer types in the prompt are missed entirely. The effect is approximately monotonic with type count.\n\n\\subsection{Channel 2: Confusability $\\rightarrow$ Type Confusion}\n\nWhen semantically similar types co-occur in the same prompt, the model confuses their boundaries during type assignment. This manifests as \\emph{intra-batch substitution} (IntraSub): a correctly detected span is labeled with a semantically similar but incorrect type from the current prompt. Unlike count-induced degradation, this channel is driven by the \\emph{composition} of types rather than their number.\n\n\\subsection{Schema Confusability Score (SCS)}\n\nWe operationalize pairwise confusability using the \\textbf{Schema Confusability Score} (SCS): the cosine similarity between type-name embeddings. For a schema $\\mathcal{S} = \\{t_1, \\ldots, t_n\\}$:\n\\begin{equation}\n\\text{SCS}(t_i, t_j) = \\frac{\\mathbf{e}(t_i) \\cdot \\mathbf{e}(t_j)}{\\|\\mathbf{e}(t_i)\\| \\|\\mathbf{e}(t_j)\\|}\n\\end{equation}\nwhere $\\mathbf{e}(t)$ is the embedding of type name $t$. We evaluate two embedding models: Qwen3 (extraction-model-aligned) and MiniLM (generic sentence similarity).\n\nFor batch-level aggregation, the \\textbf{Batch Confusability Score} (BCS) is the mean pairwise SCS within a batch of types.\n\n\\subsection{Schema-DAG Guided Decomposition (SDGD)}\n\nSDGD partitions a large schema into smaller batches to reduce within-batch confusability.\nGiven a confusability graph $G = (\\mathcal{S}, E)$ where edge weights are pairwise SCS values, SDGD applies graph coloring to assign types to batches such that highly confusable pairs are separated.\n\nWe evaluate two variants:\n\\begin{itemize}\n\\item \\textbf{SDGD-zero}: Uses embedding-based SCS to construct the confusability graph without any task-specific data.\n\\item \\textbf{SDGD-cal}: Uses a small calibration set (5--10 examples) to construct an empirical confusion matrix, bypassing embedding choice entirely.\n\\end{itemize}\n\nAfter per-batch extraction, predictions are merged via union with span-level deduplication.\n\n%% ============================================================\n%% 4. EXPERIMENTAL SETUP\n%% ============================================================\n\\section{Experimental Setup}\n\n\\paragraph{Datasets.}\nWe evaluate on three IE tasks spanning different schema characteristics:\n\\begin{itemize}\n\\item \\textbf{Few-NERD} (NER): 66 fine-grained entity types across 8 coarse categories (cross-domain, heterogeneous schema).\n\\item \\textbf{FewRel} (sentence-level RE): 80 relation types used in BCS-controlled experiments.\n\\item \\textbf{DocRED} (document-level RE): 96 relation types with cross-sentence reasoning requirements.\n\\item \\textbf{MAVEN} (event detection): 168 event types derived from FrameNet (same-domain, semantically homogeneous schema).\n\\end{itemize}\n\n\\paragraph{Models.} Primary extraction model: Qwen3-32B in zero-shot prompting mode.\n\n\\paragraph{Metrics.} Task-appropriate metrics: span-level F1 for NER, accuracy for RE, relaxed F1 (allowing boundary tolerance) for ED.\n\n%% ============================================================\n%% 5. RESULTS\n%% ============================================================\n\\section{Results}\n\n\\subsection{Error Taxonomy: Mechanistic Evidence}\n\\label{sec:error-taxonomy}\n\nWe classify false positive predictions into error types across BCS bins to directly test the multi-channel model. If confusability drives type confusion rather than detection failure, we expect IntraSub (correct span, wrong type from same batch) to increase monotonically with BCS while missed rate remains stable.\n\n\\begin{table}[t]\n\\centering\n\\caption{Error taxonomy on Few-NERD (NER). IntraSub increases monotonically with BCS ($\\rho{=}1.0$, $p{<}0.001$). ExtraSub is never observed.}\n\\label{tab:error-ner}\n\\begin{tabular}{lrrrr}\n\\toprule\nBCS Bin & N\\_FP & IntraSub\\% & ExtraSub\\% & Other\\% \\\\\n\\midrule\nZero    & 6172 & 0.0  & 90.3 & 9.7  \\\\\nLow     & 2231 & 1.6  & 89.9 & 8.5  \\\\\nMedium  & 3843 & 10.6 & 78.1 & 11.3 \\\\\nHigh    & 6188 & 49.4 & 30.8 & 19.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Error taxonomy on FewRel 80-rel (RE). IntraSub increases with BCS ($\\rho{=}0.954$, $p{<}10^{-6}$). Missed rate remains in 10--16\\%, consistent with a count (not confusability) channel.}\n\\label{tab:error-re}\n\\begin{tabular}{lrrr}\n\\toprule\nBCS Bin    & Correct\\% & IntraSub\\% & Missed\\% \\\\\n\\midrule\nZero       & 85.7 & 0.0  & 14.3 \\\\\nLow        & 85.4 & 4.2  & 10.4 \\\\\nMedium     & 75.7 & 13.0 & 11.3 \\\\\nHigh       & 66.7 & 20.3 & 13.0 \\\\\nVery High  & 52.0 & 32.3 & 15.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTables~\\ref{tab:error-ner} and~\\ref{tab:error-re} present the error taxonomy results. On Few-NERD, IntraSub rate rises from 0\\% (zero BCS) to 49.4\\% (high BCS) with a perfect monotonic trend ($\\rho{=}1.0$). On FewRel 80-rel, the same pattern holds ($\\rho{=}0.954$): IntraSub grows from 0\\% to 32.3\\% across five BCS bins. Critically, the missed rate remains in a narrow 10--16\\% band regardless of BCS, confirming that confusability affects type assignment (Channel 2) rather than entity detection (Channel 1).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-task monotonicity of IntraSub vs.\\ BCS.}\n\\label{tab:cross-task}\n\\begin{tabular}{lrr}\n\\toprule\nTask & IntraSub vs BCS $\\rho$ & $p$ \\\\\n\\midrule\nNER (Few-NERD)  & 1.000 & ${<}0.001$ \\\\\nRE (FewRel)     & 0.954 & ${<}10^{-6}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTwo additional observations strengthen the mechanistic account: (1) ExtraSub rate is exactly 0\\% across all conditions---type confusion is strictly an intra-batch phenomenon where the model selects from co-present types, never hallucinating types outside the current prompt; (2) hallucination rate is below 3\\%, confirming that LLM errors in IE are primarily \\emph{misclassification} rather than \\emph{fabrication}.\n\n\\subsection{DocRED Confusability Study}\n\\label{sec:docred}\n\nTo test whether the confusability signal extends to document-level RE---a harder setting with cross-sentence reasoning and multiple entity pairs per document---we conduct a controlled study on DocRED with 96 relation types.\n\n\\begin{table}[t]\n\\centering\n\\caption{DocRED count curve (Qwen3-32B). Accuracy degrades 42pp from count=1 to count=96.}\n\\label{tab:docred-count}\n\\begin{tabular}{rrrr}\n\\toprule\nCount & Acc & BCS\\_mean & N\\_batches \\\\\n\\midrule\n1  & 0.740 & 0    & 96 \\\\\n4  & 0.660 & 0.53 & 5  \\\\\n8  & 0.590 & 0.64 & 5  \\\\\n16 & 0.480 & 0.73 & 5  \\\\\n32 & 0.430 & 0.83 & 5  \\\\\n64 & 0.360 & 0.91 & 5  \\\\\n96 & 0.320 & 0.95 & 5  \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{DocRED BCS-controlled analysis. At matched type counts, high-BCS batches underperform low-BCS batches, isolating confusability from count.}\n\\label{tab:docred-bcs}\n\\begin{tabular}{rrrrrr}\n\\toprule\nCount & Low-BCS Acc & High-BCS Acc & $\\Delta$(pp) & $\\rho$ & $p$ \\\\\n\\midrule\n16 & 0.560 & 0.400 & $-$16.0 & $-$0.42 & 0.028 \\\\\n32 & 0.500 & 0.370 & $-$13.0 & $-$0.36 & 0.055 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:docred-count} shows a 42 percentage point degradation from single-relation to full-schema extraction, consistent with the count channel. Table~\\ref{tab:docred-bcs} isolates the confusability effect: at count=16, high-BCS batches score 16pp lower than low-BCS batches ($\\rho{=}{-}0.42$, $p{=}0.028$). At count=32, the gap narrows to 13pp ($p{=}0.055$, borderline). The pairwise SCS--confusion correlation on DocRED is $r{=}0.09$ ($95\\%$ CI: $[0.04, 0.14]$, $n{=}4{,}560$ pairs), weaker than Few-NERD or MAVEN, likely due to document-level confounds (entity pair distance, cross-sentence reasoning) that dilute the pure confusability signal.\n\nThe DocRED results provide directionally consistent but weaker evidence compared to sentence-level tasks. The confusability signal persists in the expected direction despite the added complexity of document-level extraction.\n\n\\subsection{SCS Validation: Embedding Proxy Quality}\n\\label{sec:scs-valid}\n\nA key assumption of our framework is that embedding-based SCS approximates actual model confusion. We validate this by correlating pairwise SCS with an empirical confusion matrix constructed from Few-NERD extraction errors.\n\n\\begin{table}[t]\n\\centering\n\\caption{SCS $\\rightarrow$ empirical confusion validation. SCS is a significant but weak predictor of confusion; nonzero-only subset shows stronger ranking ability.}\n\\label{tab:scs-valid}\n\\begin{tabular}{llrrrr}\n\\toprule\nSubset & Embedding & Spearman $\\rho$ & $p$ & Kendall $\\tau$ & $R^2$ \\\\\n\\midrule\nAll ($n{=}1953$)     & Qwen3  & 0.168 & $7.3 \\times 10^{-14}$ & 0.135 & ${\\sim}4.8\\%$ \\\\\nAll ($n{=}1953$)     & MiniLM & 0.144 & $1.7 \\times 10^{-10}$ & 0.115 & ${\\sim}2.8\\%$ \\\\\nNonzero ($n{=}216$)  & Qwen3  & 0.272 & $5.0 \\times 10^{-5}$  & 0.200 & ${\\sim}7.4\\%$ \\\\\nNonzero ($n{=}216$)  & MiniLM & 0.306 & $4.6 \\times 10^{-6}$  & 0.228 & ${\\sim}9.4\\%$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:scs-valid} reports the results. Both embeddings achieve highly significant correlations on the full set of 1,953 type pairs (all $p < 10^{-10}$), confirming that SCS captures a real confusability signal. However, variance explained is low: $R^2 \\approx 3$--$5\\%$ on all pairs, rising to 7--9\\% when restricting to the 216 pairs with nonzero empirical confusion.\n\nThe low all-pairs $R^2$ reflects extreme zero-inflation: 88.9\\% of type pairs are never confused, creating massive ties that compress rank correlations. Qwen3 embeddings better predict \\emph{whether} confusion occurs (higher all-pairs $\\rho$), while MiniLM better ranks \\emph{how much} confusion occurs among actually-confused pairs (higher nonzero-only $\\rho$). Neither embedding dominates, suggesting that SCS is an effective analytical tool for detecting confusability signals but an insufficient engineering tool for precise decomposition---consistent with the SDGD results in Section~\\ref{sec:sdgd}.\n\n\\subsection{Interaction Between Count and Confusability}\n\\label{sec:interaction}\n\nOur multi-channel model predicts that count and confusability interact: confusability effects should amplify at higher type counts, as more co-present confusable types increase interference opportunities. We test this with a 2$\\times$2 factorial design on Few-NERD.\n\n\\begin{table}[t]\n\\centering\n\\caption{2$\\times$2 interaction design on Few-NERD (F1). The BCS effect is 4.4$\\times$ larger at count=12 than count=6, but the interaction is not statistically significant ($z{=}{-}0.67$, $p{=}0.50$).}\n\\label{tab:interaction}\n\\begin{tabular}{lrrr}\n\\toprule\n             & Low BCS & High BCS & BCS $\\Delta$ \\\\\n\\midrule\nCount=6      & 0.324   & 0.313    & $-$0.011 \\\\\nCount=12     & 0.325   & 0.277    & $-$0.048 \\\\\n\\midrule\nCount $\\Delta$ & +0.001  & $-$0.036 & \\\\\n\\bottomrule\n\\multicolumn{4}{l}{\\small Interaction: $z{=}{-}0.67$, $p{=}0.50$ (n.s.)} \\\\\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:interaction} shows that the direction is consistent with the multiplicative hypothesis: the BCS effect at count=12 ($\\Delta{=}{-}4.8$pp) is 4.4$\\times$ larger than at count=6 ($\\Delta{=}{-}1.1$pp). However, the interaction is not statistically significant ($z{=}{-}0.67$, $p{=}0.50$).\n\nThis null result reflects an underpowered design rather than absence of interaction. The count contrast (6 vs.\\ 12) is narrow---Few-NERD's 66 types and the BCS range available (0.75--0.90) constrain the factorial space. Power analysis estimates $n \\approx 80$ per cell to achieve 0.8 power at this effect size, compared to $n{=}27$ in the current design. The main effects are individually small: count $\\Delta{=}{-}1.8$pp, BCS $\\Delta{=}{-}2.9$pp.\n\n\\subsection{Schema Decomposition: SDGD and Alternatives}\n\\label{sec:sdgd}\n\nWe evaluate whether confusability-aware schema decomposition can translate diagnostic insights into practical improvements.\n\n\\subsubsection{SDGD-zero and Random Baselines}\n\n\\begin{table}[t]\n\\centering\n\\caption{Decomposition methods on MAVEN (168 event types). All decomposition approaches underperform single-pass. SDGD-zero underperforms random batching.}\n\\label{tab:sdgd-maven}\n\\begin{tabular}{lrrrrr}\n\\toprule\nMethod & Relaxed F1 & P & R & $k$ & Time(s) \\\\\n\\midrule\nSingle-pass & 0.247 & 0.320 & 0.200 & 1   & 130  \\\\\nRandom      & 0.175 & 0.140 & 0.230 & 12  & 950  \\\\\nSDGD-zero   & 0.135 & 0.120 & 0.155 & 8   & 680  \\\\\nPer-type    & 0.110 & 0.070 & 0.300 & 168 & 9200 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Random batching vs.\\ SDGD-zero at matched $k$. Random consistently outperforms confusability-aware grouping.}\n\\label{tab:random-ablation}\n\\begin{tabular}{llrrr}\n\\toprule\nDataset & $k$ & Random F1 & SDGD-zero F1 & Single-pass F1 \\\\\n\\midrule\nFew-NERD & 4 & 0.305 & 0.241 & 0.445 \\\\\nFew-NERD & 8 & 0.295 & 0.220 & 0.445 \\\\\nMAVEN    & 8 & 0.175 & 0.135 & 0.247 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:sdgd-maven} presents results on MAVEN. Single-pass extraction (F1=0.247) outperforms all decomposition methods. SDGD-zero (F1=0.135) performs worst among multi-batch approaches, even below random batching (F1=0.175). Per-type splitting achieves the highest recall (0.300) but catastrophically low precision (0.070) due to merge conflicts across 168 batches.\n\nTable~\\ref{tab:random-ablation} confirms this pattern across datasets: at matched batch counts, random batching outperforms SDGD-zero by 4--7.5pp F1. This counterintuitive result has a clear explanation: SDGD-zero's graph coloring produces highly uneven batch sizes (some batches contain only 3--4 types, causing over-prediction) and concentrates all ``hard'' high-SCS types into the same batches, where precision collapses. Random batching distributes difficulty more evenly.\n\n\\subsubsection{Calibration-Based Decomposition (SDGD-cal)}\n\nSDGD-cal replaces embedding-based SCS with an empirical confusion matrix from 5--10 calibration examples, directly capturing model-specific confusion patterns.\n\n\\begin{table}[t]\n\\centering\n\\caption{SDGD-cal vs.\\ baselines on Few-NERD. Calibration improves over SDGD-zero but does not reach single-pass performance.}\n\\label{tab:sdgd-cal-fewnerd}\n\\begin{tabular}{lrrrrl}\n\\toprule\nMethod & F1 & P & R & $k$ & Extra(s) \\\\\n\\midrule\nSingle-pass    & 0.445 & 0.563 & 0.368 & 1 & 0  \\\\\nRandom         & 0.301 & 0.331 & 0.276 & 8 & 0  \\\\\nSDGD-zero      & 0.241 & 0.324 & 0.191 & 4 & 0  \\\\\nSDGD-cal (5)   & 0.295 & 0.340 & 0.260 & 5 & 50 \\\\\nSDGD-cal (10)  & 0.315 & 0.360 & 0.280 & 5 & 90 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{SDGD-cal vs.\\ baselines on MAVEN. Same pattern: calibration helps but single-pass remains superior.}\n\\label{tab:sdgd-cal-maven}\n\\begin{tabular}{lrrr}\n\\toprule\nMethod & Relaxed F1 & $k$ & Calibration(s) \\\\\n\\midrule\nSingle-pass    & 0.247 & 1  & 0   \\\\\nRandom         & 0.175 & 12 & 0   \\\\\nSDGD-zero      & 0.135 & 8  & 0   \\\\\nSDGD-cal (5)   & 0.165 & 10 & 200 \\\\\nSDGD-cal (10)  & 0.180 & 10 & 380 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTables~\\ref{tab:sdgd-cal-fewnerd} and~\\ref{tab:sdgd-cal-maven} show that calibration improves over SDGD-zero (+7.4pp on Few-NERD, +4.5pp on MAVEN with 10-shot calibration), bringing performance close to random batching. However, SDGD-cal still falls 13.0pp (Few-NERD) and 6.7pp (MAVEN) below single-pass extraction.\n\nThe convergence of SDGD-cal and random batching is informative: even with the best available grouping signal (empirical confusion), the result barely exceeds random assignment. This confirms that the bottleneck is merge quality, not grouping quality. The 5-shot vs.\\ 10-shot difference is small (2.0pp on Few-NERD, 1.5pp on MAVEN), as 5 calibration examples already capture the dominant confusion clusters.\n\n\\subsubsection{Per-Type Splitting: The Decomposition Ceiling}\n\nPer-type splitting (one type per batch) represents the theoretical ceiling for confusability elimination: IntraSub is guaranteed to be zero.\n\n\\begin{table}[t]\n\\centering\n\\caption{Full decomposition spectrum on Few-NERD. Per-type splitting eliminates type confusion (IntraSub=0) and maximizes recall (+21.7pp) but precision collapses ($-$36.8pp) due to merge conflicts.}\n\\label{tab:pertype}\n\\begin{tabular}{lrrrrrr}\n\\toprule\nMethod & F1 & P & R & $k$ & IntraSub & Time(s) \\\\\n\\midrule\nSingle-pass  & 0.445 & 0.563 & 0.368 & 1  & baseline & 79   \\\\\nRandom ($k{=}8$) & 0.295 & 0.330 & 0.270 & 8  & moderate & 494  \\\\\nSDGD-zero    & 0.241 & 0.324 & 0.191 & 4  & low      & 261  \\\\\nSDGD-cal     & 0.315 & 0.360 & 0.280 & 5  & low      & 460  \\\\\nPer-type     & 0.290 & 0.195 & 0.585 & 66 & 0        & 2550 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:pertype} presents the full decomposition spectrum. Per-type splitting achieves the highest recall by far (0.585, +21.7pp over single-pass): with only one type per prompt, the model's attention is fully concentrated, missing fewer entities. However, precision collapses from 0.563 to 0.195 ($-$36.8pp): 66 independent batches generate overlapping predictions for the same text spans, and union-based merge retains all of them. The net F1 effect is negative ($-$15.5pp).\n\nOn MAVEN, the pattern is more extreme: per-type splitting achieves recall of 0.460 but precision of only 0.085 (relaxed F1=0.145) across 168 batches, with a wall-clock time of 9,500 seconds.\n\nThis result crystallizes the fundamental decomposition tradeoff: splitting reduces type confusion (Channel 2 benefit) but merge amplification creates new false positives (a structural cost that grows with $O(k)$ batches). Current merge strategies---union with deduplication, confidence gating---cannot resolve $O(k)$ conflicting predictions over the same spans.\n\n%% ============================================================\n%% 6. DISCUSSION\n%% ============================================================\n\\section{Discussion}\n\n\\paragraph{The confusability signal: robust but small.}\nPairwise confusability consistently predicts extraction degradation across NER, RE (sentence and document level), and ED. The cross-task error taxonomy ($\\rho{=}1.0$ for NER, $\\rho{=}0.954$ for RE) provides the strongest mechanistic evidence: confusability drives type confusion, not detection failure. However, pairwise effect sizes are modest ($r{=}0.09$--$0.17$), and SCS explains only 3--9\\% of empirical confusion variance. The signal is analytically valuable but practically insufficient for engineering precise decompositions.\n\n\\paragraph{Why decomposition fails.}\nAll decomposition approaches underperform single-pass extraction, with a consistent hierarchy across datasets: single-pass $>$ random $\\approx$ SDGD-cal $>$ SDGD-zero $>$ per-type. The failure is not in grouping quality (SDGD-cal $\\approx$ random confirms this) but in merge amplification: reconciling predictions from $k$ independent batches introduces $O(k)$ conflicting span predictions that no current merge strategy can cleanly resolve.\n\nRandom batching outperforming SDGD-zero ($+$4.0--7.5pp) exposes implementation flaws in the graph-coloring approach: uneven batch sizes and hard-type concentration. SDGD-cal partially addresses these issues but still cannot overcome the structural merge problem.\n\n\\paragraph{Per-type aggregation confound.}\nThe DocRED pairwise correlation ($r{=}0.09$) is weaker than sentence-level tasks, likely because document-level extraction introduces additional confounds (entity pair distance, cross-sentence reasoning) that dilute the confusability signal. This suggests that confusability effects are most cleanly observed in sentence-level settings.\n\n\\paragraph{Limitations.}\nOur study uses a single primary extraction model (Qwen3-32B); multi-model validation would strengthen generalizability claims. The interaction experiment (Section~\\ref{sec:interaction}) is underpowered, and the null result should be interpreted cautiously. The SCS validation (Section~\\ref{sec:scs-valid}) is conducted only on Few-NERD; cross-dataset SCS validation would be valuable. SDGD experiments use a single merge strategy (union with deduplication); more sophisticated merge approaches (e.g., confidence-weighted NMS) may partially mitigate merge amplification.\n\n%% ============================================================\n%% 7. CONCLUSION\n%% ============================================================\n\\section{Conclusion}\n\nWe present a controlled empirical study isolating type count and type confusability as independent drivers of schema-induced degradation in training-free LLM information extraction. Our multi-channel degradation model---count reduces recall, confusability causes type confusion---is supported by cross-task error taxonomy analysis with near-perfect monotonic relationships ($\\rho{=}1.0$ for NER, $\\rho{=}0.954$ for RE) and validated across four datasets spanning NER, sentence-level RE, document-level RE, and event detection.\n\nWe further demonstrate that translating this diagnostic insight into practical improvements via schema decomposition remains an open challenge. All decomposition approaches---embedding-based (SDGD-zero), calibration-based (SDGD-cal), random batching, and per-type splitting---underperform single-pass extraction due to merge amplification. The convergence of calibration-based and random approaches identifies merge strategy, not grouping quality, as the critical bottleneck. Future work should focus on calibration-aware merge mechanisms that can resolve conflicting predictions across batches without amplifying false positives.\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a7029e2-6dd0-4d8d-8b9d-dc9f4ec8b8f7",
  "isSidechain": false,
  "requestId": "req_011Cb5tp1UXg4q2mgPDbynJj",
  "type": "assistant",
  "uuid": "ec124866-856f-45ec-ba68-ee6280af019b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "4d779de5-396b-49dc-acca-1976fdd39e66",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012mx8N6iezn5bbrDzgMcPh6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 178,
      "cache_read_input_tokens": 41329,
      "output_tokens": 9034,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 178,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9034,
          "cache_read_input_tokens": 41329,
          "cache_creation_input_tokens": 178,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 178
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

_source line 23 · 2026-05-16T08:02:09.997Z_

<details><summary>↩ Tool result · `toolu_01BzR1CtXaU75F7ycNsGBzPu`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec124866-856f-45ec-ba68-ee6280af019b",
  "isSidechain": false,
  "promptId": "fc49f735-e722-4cc2-9426-bb861b70dea7",
  "type": "user",
  "uuid": "0882b8ff-01d1-411c-bc09-30c3632a13ca",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/median/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{natbib}\n\\bibliographystyle{plainnat}\n\n\\title{Multi-Channel Schema Degradation in Training-Free LLM Information Extraction:\\\\A Controlled Empirical Study}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%% ============================================================\n%% ABSTRACT\n%% ============================================================\n\\begin{abstract}\nTraining-free LLM-based information extraction (IE) degrades severely as schema complexity increases, yet the mechanisms behind this degradation remain poorly characterized.\nWe conduct a controlled empirical study isolating two independent factors---\\emph{type count} and \\emph{type confusability}---across three IE tasks: named entity recognition (NER on Few-NERD), relation extraction (RE on FewRel and DocRED), and event detection (ED on MAVEN).\nWe propose a \\textbf{multi-channel degradation model}: type count primarily causes entity omission (recall decline), while type confusability causes type confusion errors where correct spans are labeled with semantically similar but incorrect types.\nError taxonomy analysis reveals a near-perfect monotonic relationship between pairwise confusability and intra-batch type confusion rate across both NER ($\\rho{=}1.0$) and RE ($\\rho{=}0.954$).\nWe validate embedding-based Schema Confusability Scores (SCS) as significant predictors of empirical confusion ($\\rho{=}0.168$--$0.306$, all $p < 10^{-4}$), though with limited variance explained ($R^2{=}3$--$9\\%$).\nWe further investigate Schema-DAG Guided Decomposition (SDGD) as a practical mitigation, finding that all decomposition strategies---including confusability-aware grouping and calibration-based approaches---underperform a single-pass baseline due to \\emph{merge amplification}: the structural challenge of reconciling predictions from multiple schema partitions.\nThese negative results, combined with ablations showing random batching outperforming graph-coloring-based decomposition, identify merge strategy rather than grouping quality as the critical bottleneck for future work.\n\\end{abstract}\n\n%% ============================================================\n%% 1. INTRODUCTION\n%% ============================================================\n\\section{Introduction}\n\nLarge language models (LLMs) have shown remarkable zero-shot and few-shot capabilities on information extraction tasks when prompted with a target schema---a set of entity types, relation types, or event types to extract.\nHowever, performance degrades dramatically as schema complexity increases: extraction quality can drop 20--60 F1 points when moving from simple schemas ($<10$ types) to complex real-world schemas ($>50$ types), even when the underlying model remains the same.\n\nPrior work has proposed schema decomposition as a remedy. UniNER decomposes extraction into per-type prompts, gaining up to 3.3 F1 but losing cross-type context. LLM-PEE uses embedding similarity as an implicit confusability proxy to group types, but never empirically validates whether similarity actually predicts confusion. Critically, no prior work has \\emph{isolated} confusability from count, or characterized the distinct degradation mechanisms each factor induces.\n\nWe address this gap with three contributions:\n\n\\begin{enumerate}\n\\item \\textbf{Multi-channel degradation model.} We demonstrate that count and confusability operate through orthogonal channels: count primarily reduces recall (entities missed due to attention dilution), while confusability primarily reduces precision (correct entities assigned wrong types). Error taxonomy analysis across NER and RE shows perfect or near-perfect monotonic relationships ($\\rho{=}1.0$ and $\\rho{=}0.954$) between confusability and intra-batch type confusion rate.\n\n\\item \\textbf{Cross-task confusability validation.} We validate pairwise Schema Confusability Scores as significant predictors of empirical model confusion across NER and RE, and extend validation to document-level RE (DocRED, 96 relation types) where confusability effects persist despite additional confounds from cross-sentence reasoning.\n\n\\item \\textbf{Decomposition as negative result.} We systematically evaluate schema decomposition approaches---SDGD-zero (embedding-based graph coloring), SDGD-cal (calibration-based empirical grouping), random batching, and per-type splitting---across two datasets. All underperform single-pass extraction, identifying \\emph{merge amplification} as a structural bottleneck that grouping quality alone cannot overcome.\n\\end{enumerate}\n\n%% ============================================================\n%% 2. RELATED WORK\n%% ============================================================\n\\section{Related Work}\n\n\\paragraph{Training-free LLM IE.}\nRecent work has demonstrated that LLMs can perform zero-shot and few-shot information extraction by prompting with type definitions.\nGPT-NER and GoLLIE formulate NER as sequence generation; InstructUIE provides a unified prompt format across tasks.\nThese approaches share a common failure mode: performance degrades with schema complexity, yet the specific mechanisms remain uncharacterized.\n\n\\paragraph{Schema decomposition.}\nUniNER decomposes NER into per-type queries, improving recall at the cost of cross-type context.\nLLM-PEE groups entity types by embedding similarity, implicitly using confusability as a decomposition criterion without validating whether similarity predicts actual model confusion.\nOur work provides the missing empirical foundation: we validate the confusability signal and demonstrate why current decomposition approaches fail at the merge stage.\n\n\\paragraph{Prompt sensitivity in LLMs.}\nLost in the Middle showed that LLM performance varies with information position in long contexts.\nOur work extends this line of inquiry to schema composition: not just how much information is in the prompt, but which types co-occur and how their semantic similarity affects extraction.\n\n%% ============================================================\n%% 3. MULTI-CHANNEL DEGRADATION FRAMEWORK\n%% ============================================================\n\\section{Multi-Channel Degradation Framework}\n\nWe model schema-induced degradation in LLM IE as a multi-channel process with two independently addressable mechanisms.\n\n\\subsection{Channel 1: Count $\\rightarrow$ Recall Decline}\n\nAs the number of types in a single extraction prompt increases, the model's attention is diluted across more targets. This manifests as \\emph{entity omission}: entities that would be detected with fewer types in the prompt are missed entirely. The effect is approximately monotonic with type count.\n\n\\subsection{Channel 2: Confusability $\\rightarrow$ Type Confusion}\n\nWhen semantically similar types co-occur in the same prompt, the model confuses their boundaries during type assignment. This manifests as \\emph{intra-batch substitution} (IntraSub): a correctly detected span is labeled with a semantically similar but incorrect type from the current prompt. Unlike count-induced degradation, this channel is driven by the \\emph{composition} of types rather than their number.\n\n\\subsection{Schema Confusability Score (SCS)}\n\nWe operationalize pairwise confusability using the \\textbf{Schema Confusability Score} (SCS): the cosine similarity between type-name embeddings. For a schema $\\mathcal{S} = \\{t_1, \\ldots, t_n\\}$:\n\\begin{equation}\n\\text{SCS}(t_i, t_j) = \\frac{\\mathbf{e}(t_i) \\cdot \\mathbf{e}(t_j)}{\\|\\mathbf{e}(t_i)\\| \\|\\mathbf{e}(t_j)\\|}\n\\end{equation}\nwhere $\\mathbf{e}(t)$ is the embedding of type name $t$. We evaluate two embedding models: Qwen3 (extraction-model-aligned) and MiniLM (generic sentence similarity).\n\nFor batch-level aggregation, the \\textbf{Batch Confusability Score} (BCS) is the mean pairwise SCS within a batch of types.\n\n\\subsection{Schema-DAG Guided Decomposition (SDGD)}\n\nSDGD partitions a large schema into smaller batches to reduce within-batch confusability.\nGiven a confusability graph $G = (\\mathcal{S}, E)$ where edge weights are pairwise SCS values, SDGD applies graph coloring to assign types to batches such that highly confusable pairs are separated.\n\nWe evaluate two variants:\n\\begin{itemize}\n\\item \\textbf{SDGD-zero}: Uses embedding-based SCS to construct the confusability graph without any task-specific data.\n\\item \\textbf{SDGD-cal}: Uses a small calibration set (5--10 examples) to construct an empirical confusion matrix, bypassing embedding choice entirely.\n\\end{itemize}\n\nAfter per-batch extraction, predictions are merged via union with span-level deduplication.\n\n%% ============================================================\n%% 4. EXPERIMENTAL SETUP\n%% ============================================================\n\\section{Experimental Setup}\n\n\\paragraph{Datasets.}\nWe evaluate on three IE tasks spanning different schema characteristics:\n\\begin{itemize}\n\\item \\textbf{Few-NERD} (NER): 66 fine-grained entity types across 8 coarse categories (cross-domain, heterogeneous schema).\n\\item \\textbf{FewRel} (sentence-level RE): 80 relation types used in BCS-controlled experiments.\n\\item \\textbf{DocRED} (document-level RE): 96 relation types with cross-sentence reasoning requirements.\n\\item \\textbf{MAVEN} (event detection): 168 event types derived from FrameNet (same-domain, semantically homogeneous schema).\n\\end{itemize}\n\n\\paragraph{Models.} Primary extraction model: Qwen3-32B in zero-shot prompting mode.\n\n\\paragraph{Metrics.} Task-appropriate metrics: span-level F1 for NER, accuracy for RE, relaxed F1 (allowing boundary tolerance) for ED.\n\n%% ============================================================\n%% 5. RESULTS\n%% ============================================================\n\\section{Results}\n\n\\subsection{Error Taxonomy: Mechanistic Evidence}\n\\label{sec:error-taxonomy}\n\nWe classify false positive predictions into error types across BCS bins to directly test the multi-channel model. If confusability drives type confusion rather than detection failure, we expect IntraSub (correct span, wrong type from same batch) to increase monotonically with BCS while missed rate remains stable.\n\n\\begin{table}[t]\n\\centering\n\\caption{Error taxonomy on Few-NERD (NER). IntraSub increases monotonically with BCS ($\\rho{=}1.0$, $p{<}0.001$). ExtraSub is never observed.}\n\\label{tab:error-ner}\n\\begin{tabular}{lrrrr}\n\\toprule\nBCS Bin & N\\_FP & IntraSub\\% & ExtraSub\\% & Other\\% \\\\\n\\midrule\nZero    & 6172 & 0.0  & 90.3 & 9.7  \\\\\nLow     & 2231 & 1.6  & 89.9 & 8.5  \\\\\nMedium  & 3843 & 10.6 & 78.1 & 11.3 \\\\\nHigh    & 6188 & 49.4 & 30.8 & 19.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Error taxonomy on FewRel 80-rel (RE). IntraSub increases with BCS ($\\rho{=}0.954$, $p{<}10^{-6}$). Missed rate remains in 10--16\\%, consistent with a count (not confusability) channel.}\n\\label{tab:error-re}\n\\begin{tabular}{lrrr}\n\\toprule\nBCS Bin    & Correct\\% & IntraSub\\% & Missed\\% \\\\\n\\midrule\nZero       & 85.7 & 0.0  & 14.3 \\\\\nLow        & 85.4 & 4.2  & 10.4 \\\\\nMedium     & 75.7 & 13.0 & 11.3 \\\\\nHigh       & 66.7 & 20.3 & 13.0 \\\\\nVery High  & 52.0 & 32.3 & 15.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTables~\\ref{tab:error-ner} and~\\ref{tab:error-re} present the error taxonomy results. On Few-NERD, IntraSub rate rises from 0\\% (zero BCS) to 49.4\\% (high BCS) with a perfect monotonic trend ($\\rho{=}1.0$). On FewRel 80-rel, the same pattern holds ($\\rho{=}0.954$): IntraSub grows from 0\\% to 32.3\\% across five BCS bins. Critically, the missed rate remains in a narrow 10--16\\% band regardless of BCS, confirming that confusability affects type assignment (Channel 2) rather than entity detection (Channel 1).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-task monotonicity of IntraSub vs.\\ BCS.}\n\\label{tab:cross-task}\n\\begin{tabular}{lrr}\n\\toprule\nTask & IntraSub vs BCS $\\rho$ & $p$ \\\\\n\\midrule\nNER (Few-NERD)  & 1.000 & ${<}0.001$ \\\\\nRE (FewRel)     & 0.954 & ${<}10^{-6}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTwo additional observations strengthen the mechanistic account: (1) ExtraSub rate is exactly 0\\% across all conditions---type confusion is strictly an intra-batch phenomenon where the model selects from co-present types, never hallucinating types outside the current prompt; (2) hallucination rate is below 3\\%, confirming that LLM errors in IE are primarily \\emph{misclassification} rather than \\emph{fabrication}.\n\n\\subsection{DocRED Confusability Study}\n\\label{sec:docred}\n\nTo test whether the confusability signal extends to document-level RE---a harder setting with cross-sentence reasoning and multiple entity pairs per document---we conduct a controlled study on DocRED with 96 relation types.\n\n\\begin{table}[t]\n\\centering\n\\caption{DocRED count curve (Qwen3-32B). Accuracy degrades 42pp from count=1 to count=96.}\n\\label{tab:docred-count}\n\\begin{tabular}{rrrr}\n\\toprule\nCount & Acc & BCS\\_mean & N\\_batches \\\\\n\\midrule\n1  & 0.740 & 0    & 96 \\\\\n4  & 0.660 & 0.53 & 5  \\\\\n8  & 0.590 & 0.64 & 5  \\\\\n16 & 0.480 & 0.73 & 5  \\\\\n32 & 0.430 & 0.83 & 5  \\\\\n64 & 0.360 & 0.91 & 5  \\\\\n96 & 0.320 & 0.95 & 5  \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{DocRED BCS-controlled analysis. At matched type counts, high-BCS batches underperform low-BCS batches, isolating confusability from count.}\n\\label{tab:docred-bcs}\n\\begin{tabular}{rrrrrr}\n\\toprule\nCount & Low-BCS Acc & High-BCS Acc & $\\Delta$(pp) & $\\rho$ & $p$ \\\\\n\\midrule\n16 & 0.560 & 0.400 & $-$16.0 & $-$0.42 & 0.028 \\\\\n32 & 0.500 & 0.370 & $-$13.0 & $-$0.36 & 0.055 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:docred-count} shows a 42 percentage point degradation from single-relation to full-schema extraction, consistent with the count channel. Table~\\ref{tab:docred-bcs} isolates the confusability effect: at count=16, high-BCS batches score 16pp lower than low-BCS batches ($\\rho{=}{-}0.42$, $p{=}0.028$). At count=32, the gap narrows to 13pp ($p{=}0.055$, borderline). The pairwise SCS--confusion correlation on DocRED is $r{=}0.09$ ($95\\%$ CI: $[0.04, 0.14]$, $n{=}4{,}560$ pairs), weaker than Few-NERD or MAVEN, likely due to document-level confounds (entity pair distance, cross-sentence reasoning) that dilute the pure confusability signal.\n\nThe DocRED results provide directionally consistent but weaker evidence compared to sentence-level tasks. The confusability signal persists in the expected direction despite the added complexity of document-level extraction.\n\n\\subsection{SCS Validation: Embedding Proxy Quality}\n\\label{sec:scs-valid}\n\nA key assumption of our framework is that embedding-based SCS approximates actual model confusion. We validate this by correlating pairwise SCS with an empirical confusion matrix constructed from Few-NERD extraction errors.\n\n\\begin{table}[t]\n\\centering\n\\caption{SCS $\\rightarrow$ empirical confusion validation. SCS is a significant but weak predictor of confusion; nonzero-only subset shows stronger ranking ability.}\n\\label{tab:scs-valid}\n\\begin{tabular}{llrrrr}\n\\toprule\nSubset & Embedding & Spearman $\\rho$ & $p$ & Kendall $\\tau$ & $R^2$ \\\\\n\\midrule\nAll ($n{=}1953$)     & Qwen3  & 0.168 & $7.3 \\times 10^{-14}$ & 0.135 & ${\\sim}4.8\\%$ \\\\\nAll ($n{=}1953$)     & MiniLM & 0.144 & $1.7 \\times 10^{-10}$ & 0.115 & ${\\sim}2.8\\%$ \\\\\nNonzero ($n{=}216$)  & Qwen3  & 0.272 & $5.0 \\times 10^{-5}$  & 0.200 & ${\\sim}7.4\\%$ \\\\\nNonzero ($n{=}216$)  & MiniLM & 0.306 & $4.6 \\times 10^{-6}$  & 0.228 & ${\\sim}9.4\\%$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:scs-valid} reports the results. Both embeddings achieve highly significant correlations on the full set of 1,953 type pairs (all $p < 10^{-10}$), confirming that SCS captures a real confusability signal. However, variance explained is low: $R^2 \\approx 3$--$5\\%$ on all pairs, rising to 7--9\\% when restricting to the 216 pairs with nonzero empirical confusion.\n\nThe low all-pairs $R^2$ reflects extreme zero-inflation: 88.9\\% of type pairs are never confused, creating massive ties that compress rank correlations. Qwen3 embeddings better predict \\emph{whether} confusion occurs (higher all-pairs $\\rho$), while MiniLM better ranks \\emph{how much} confusion occurs among actually-confused pairs (higher nonzero-only $\\rho$). Neither embedding dominates, suggesting that SCS is an effective analytical tool for detecting confusability signals but an insufficient engineering tool for precise decomposition---consistent with the SDGD results in Section~\\ref{sec:sdgd}.\n\n\\subsection{Interaction Between Count and Confusability}\n\\label{sec:interaction}\n\nOur multi-channel model predicts that count and confusability interact: confusability effects should amplify at higher type counts, as more co-present confusable types increase interference opportunities. We test this with a 2$\\times$2 factorial design on Few-NERD.\n\n\\begin{table}[t]\n\\centering\n\\caption{2$\\times$2 interaction design on Few-NERD (F1). The BCS effect is 4.4$\\times$ larger at count=12 than count=6, but the interaction is not statistically significant ($z{=}{-}0.67$, $p{=}0.50$).}\n\\label{tab:interaction}\n\\begin{tabular}{lrrr}\n\\toprule\n             & Low BCS & High BCS & BCS $\\Delta$ \\\\\n\\midrule\nCount=6      & 0.324   & 0.313    & $-$0.011 \\\\\nCount=12     & 0.325   & 0.277    & $-$0.048 \\\\\n\\midrule\nCount $\\Delta$ & +0.001  & $-$0.036 & \\\\\n\\bottomrule\n\\multicolumn{4}{l}{\\small Interaction: $z{=}{-}0.67$, $p{=}0.50$ (n.s.)} \\\\\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:interaction} shows that the direction is consistent with the multiplicative hypothesis: the BCS effect at count=12 ($\\Delta{=}{-}4.8$pp) is 4.4$\\times$ larger than at count=6 ($\\Delta{=}{-}1.1$pp). However, the interaction is not statistically significant ($z{=}{-}0.67$, $p{=}0.50$).\n\nThis null result reflects an underpowered design rather than absence of interaction. The count contrast (6 vs.\\ 12) is narrow---Few-NERD's 66 types and the BCS range available (0.75--0.90) constrain the factorial space. Power analysis estimates $n \\approx 80$ per cell to achieve 0.8 power at this effect size, compared to $n{=}27$ in the current design. The main effects are individually small: count $\\Delta{=}{-}1.8$pp, BCS $\\Delta{=}{-}2.9$pp.\n\n\\subsection{Schema Decomposition: SDGD and Alternatives}\n\\label{sec:sdgd}\n\nWe evaluate whether confusability-aware schema decomposition can translate diagnostic insights into practical improvements.\n\n\\subsubsection{SDGD-zero and Random Baselines}\n\n\\begin{table}[t]\n\\centering\n\\caption{Decomposition methods on MAVEN (168 event types). All decomposition approaches underperform single-pass. SDGD-zero underperforms random batching.}\n\\label{tab:sdgd-maven}\n\\begin{tabular}{lrrrrr}\n\\toprule\nMethod & Relaxed F1 & P & R & $k$ & Time(s) \\\\\n\\midrule\nSingle-pass & 0.247 & 0.320 & 0.200 & 1   & 130  \\\\\nRandom      & 0.175 & 0.140 & 0.230 & 12  & 950  \\\\\nSDGD-zero   & 0.135 & 0.120 & 0.155 & 8   & 680  \\\\\nPer-type    & 0.110 & 0.070 & 0.300 & 168 & 9200 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Random batching vs.\\ SDGD-zero at matched $k$. Random consistently outperforms confusability-aware grouping.}\n\\label{tab:random-ablation}\n\\begin{tabular}{llrrr}\n\\toprule\nDataset & $k$ & Random F1 & SDGD-zero F1 & Single-pass F1 \\\\\n\\midrule\nFew-NERD & 4 & 0.305 & 0.241 & 0.445 \\\\\nFew-NERD & 8 & 0.295 & 0.220 & 0.445 \\\\\nMAVEN    & 8 & 0.175 & 0.135 & 0.247 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:sdgd-maven} presents results on MAVEN. Single-pass extraction (F1=0.247) outperforms all decomposition methods. SDGD-zero (F1=0.135) performs worst among multi-batch approaches, even below random batching (F1=0.175). Per-type splitting achieves the highest recall (0.300) but catastrophically low precision (0.070) due to merge conflicts across 168 batches.\n\nTable~\\ref{tab:random-ablation} confirms this pattern across datasets: at matched batch counts, random batching outperforms SDGD-zero by 4--7.5pp F1. This counterintuitive result has a clear explanation: SDGD-zero's graph coloring produces highly uneven batch sizes (some batches contain only 3--4 types, causing over-prediction) and concentrates all ``hard'' high-SCS types into the same batches, where precision collapses. Random batching distributes difficulty more evenly.\n\n\\subsubsection{Calibration-Based Decomposition (SDGD-cal)}\n\nSDGD-cal replaces embedding-based SCS with an empirical confusion matrix from 5--10 calibration examples, directly capturing model-specific confusion patterns.\n\n\\begin{table}[t]\n\\centering\n\\caption{SDGD-cal vs.\\ baselines on Few-NERD. Calibration improves over SDGD-zero but does not reach single-pass performance.}\n\\label{tab:sdgd-cal-fewnerd}\n\\begin{tabular}{lrrrrl}\n\\toprule\nMethod & F1 & P & R & $k$ & Extra(s) \\\\\n\\midrule\nSingle-pass    & 0.445 & 0.563 & 0.368 & 1 & 0  \\\\\nRandom         & 0.301 & 0.331 & 0.276 & 8 & 0  \\\\\nSDGD-zero      & 0.241 & 0.324 & 0.191 & 4 & 0  \\\\\nSDGD-cal (5)   & 0.295 & 0.340 & 0.260 & 5 & 50 \\\\\nSDGD-cal (10)  & 0.315 & 0.360 & 0.280 & 5 & 90 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{SDGD-cal vs.\\ baselines on MAVEN. Same pattern: calibration helps but single-pass remains superior.}\n\\label{tab:sdgd-cal-maven}\n\\begin{tabular}{lrrr}\n\\toprule\nMethod & Relaxed F1 & $k$ & Calibration(s) \\\\\n\\midrule\nSingle-pass    & 0.247 & 1  & 0   \\\\\nRandom         & 0.175 & 12 & 0   \\\\\nSDGD-zero      & 0.135 & 8  & 0   \\\\\nSDGD-cal (5)   & 0.165 & 10 & 200 \\\\\nSDGD-cal (10)  & 0.180 & 10 & 380 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTables~\\ref{tab:sdgd-cal-fewnerd} and~\\ref{tab:sdgd-cal-maven} show that calibration improves over SDGD-zero (+7.4pp on Few-NERD, +4.5pp on MAVEN with 10-shot calibration), bringing performance close to random batching. However, SDGD-cal still falls 13.0pp (Few-NERD) and 6.7pp (MAVEN) below single-pass extraction.\n\nThe convergence of SDGD-cal and random batching is informative: even with the best available grouping signal (empirical confusion), the result barely exceeds random assignment. This confirms that the bottleneck is merge quality, not grouping quality. The 5-shot vs.\\ 10-shot difference is small (2.0pp on Few-NERD, 1.5pp on MAVEN), as 5 calibration examples already capture the dominant confusion clusters.\n\n\\subsubsection{Per-Type Splitting: The Decomposition Ceiling}\n\nPer-type splitting (one type per batch) represents the theoretical ceiling for confusability elimination: IntraSub is guaranteed to be zero.\n\n\\begin{table}[t]\n\\centering\n\\caption{Full decomposition spectrum on Few-NERD. Per-type splitting eliminates type confusion (IntraSub=0) and maximizes recall (+21.7pp) but precision collapses ($-$36.8pp) due to merge conflicts.}\n\\label{tab:pertype}\n\\begin{tabular}{lrrrrrr}\n\\toprule\nMethod & F1 & P & R & $k$ & IntraSub & Time(s) \\\\\n\\midrule\nSingle-pass  & 0.445 & 0.563 & 0.368 & 1  & baseline & 79   \\\\\nRandom ($k{=}8$) & 0.295 & 0.330 & 0.270 & 8  & moderate & 494  \\\\\nSDGD-zero    & 0.241 & 0.324 & 0.191 & 4  & low      & 261  \\\\\nSDGD-cal     & 0.315 & 0.360 & 0.280 & 5  & low      & 460  \\\\\nPer-type     & 0.290 & 0.195 & 0.585 & 66 & 0        & 2550 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:pertype} presents the full decomposition spectrum. Per-type splitting achieves the highest recall by far (0.585, +21.7pp over single-pass): with only one type per prompt, the model's attention is fully concentrated, missing fewer entities. However, precision collapses from 0.563 to 0.195 ($-$36.8pp): 66 independent batches generate overlapping predictions for the same text spans, and union-based merge retains all of them. The net F1 effect is negative ($-$15.5pp).\n\nOn MAVEN, the pattern is more extreme: per-type splitting achieves recall of 0.460 but precision of only 0.085 (relaxed F1=0.145) across 168 batches, with a wall-clock time of 9,500 seconds.\n\nThis result crystallizes the fundamental decomposition tradeoff: splitting reduces type confusion (Channel 2 benefit) but merge amplification creates new false positives (a structural cost that grows with $O(k)$ batches). Current merge strategies---union with deduplication, confidence gating---cannot resolve $O(k)$ conflicting predictions over the same spans.\n\n%% ============================================================\n%% 6. DISCUSSION\n%% ============================================================\n\\section{Discussion}\n\n\\paragraph{The confusability signal: robust but small.}\nPairwise confusability consistently predicts extraction degradation across NER, RE (sentence and document level), and ED. The cross-task error taxonomy ($\\rho{=}1.0$ for NER, $\\rho{=}0.954$ for RE) provides the strongest mechanistic evidence: confusability drives type confusion, not detection failure. However, pairwise effect sizes are modest ($r{=}0.09$--$0.17$), and SCS explains only 3--9\\% of empirical confusion variance. The signal is analytically valuable but practically insufficient for engineering precise decompositions.\n\n\\paragraph{Why decomposition fails.}\nAll decomposition approaches underperform single-pass extraction, with a consistent hierarchy across datasets: single-pass $>$ random $\\approx$ SDGD-cal $>$ SDGD-zero $>$ per-type. The failure is not in grouping quality (SDGD-cal $\\approx$ random confirms this) but in merge amplification: reconciling predictions from $k$ independent batches introduces $O(k)$ conflicting span predictions that no current merge strategy can cleanly resolve.\n\nRandom batching outperforming SDGD-zero ($+$4.0--7.5pp) exposes implementation flaws in the graph-coloring approach: uneven batch sizes and hard-type concentration. SDGD-cal partially addresses these issues but still cannot overcome the structural merge problem.\n\n\\paragraph{Per-type aggregation confound.}\nThe DocRED pairwise correlation ($r{=}0.09$) is weaker than sentence-level tasks, likely because document-level extraction introduces additional confounds (entity pair distance, cross-sentence reasoning) that dilute the confusability signal. This suggests that confusability effects are most cleanly observed in sentence-level settings.\n\n\\paragraph{Limitations.}\nOur study uses a single primary extraction model (Qwen3-32B); multi-model validation would strengthen generalizability claims. The interaction experiment (Section~\\ref{sec:interaction}) is underpowered, and the null result should be interpreted cautiously. The SCS validation (Section~\\ref{sec:scs-valid}) is conducted only on Few-NERD; cross-dataset SCS validation would be valuable. SDGD experiments use a single merge strategy (union with deduplication); more sophisticated merge approaches (e.g., confidence-weighted NMS) may partially mitigate merge amplification.\n\n%% ============================================================\n%% 7. CONCLUSION\n%% ============================================================\n\\section{Conclusion}\n\nWe present a controlled empirical study isolating type count and type confusability as independent drivers of schema-induced degradation in training-free LLM information extraction. Our multi-channel degradation model---count reduces recall, confusability causes type confusion---is supported by cross-task error taxonomy analysis with near-perfect monotonic relationships ($\\rho{=}1.0$ for NER, $\\rho{=}0.954$ for RE) and validated across four datasets spanning NER, sentence-level RE, document-level RE, and event detection.\n\nWe further demonstrate that translating this diagnostic insight into practical improvements via schema decomposition remains an open challenge. All decomposition approaches---embedding-based (SDGD-zero), calibration-based (SDGD-cal), random batching, and per-type splitting---underperform single-pass extraction due to merge amplification. The convergence of calibration-based and random approaches identifies merge strategy, not grouping quality, as the critical bottleneck. Future work should focus on calibration-aware merge mechanisms that can resolve conflicting predictions across batches without amplifying false positives.\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "ec124866-856f-45ec-ba68-ee6280af019b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "4d779de5-396b-49dc-acca-1976fdd39e66",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T073533 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extr…",
  "leafUuid": "0882b8ff-01d1-411c-bc09-30c3632a13ca",
  "sessionId": "4d779de5-396b-49dc-acca-1976fdd39e66"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper with LaTeX compilation",
  "sessionId": "4d779de5-396b-49dc-acca-1976fdd39e66"
}
```

---

### Tool call

_source line 26 · 2026-05-16T08:02:14.666Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Rn5S2X6hxtwpZSmtAE6gpB`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper (two passes for references)",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0882b8ff-01d1-411c-bc09-30c3632a13ca",
  "isSidechain": false,
  "requestId": "req_011Cb5u2Ktteh1P1Z1eqGPBP",
  "type": "assistant",
  "uuid": "be07ef9e-8466-402b-a05e-102c969858ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "4d779de5-396b-49dc-acca-1976fdd39e66",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Eg9T1iVWNwDQb11HVWTSF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9099,
      "cache_read_input_tokens": 41507,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9099,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 170,
          "cache_read_input_tokens": 41507,
          "cache_creation_input_tokens": 9099,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9099
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

_source line 27 · 2026-05-16T08:02:15.873Z_

<details><summary>↩ Tool result · `toolu_01Rn5S2X6hxtwpZSmtAE6gpB`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
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
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
No file paper.aux.
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 81.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\rightarrow' on input line 81.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 81.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 85.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\rightarrow' on input line 85.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 85.

[2]

LaTeX Warning: Reference `tab:error-ner' on page 3 undefined on input line 173.



LaTeX Warning: Reference `tab:error-re' on page 3 undefined on input line 173.

[3]

LaTeX Warning: Reference `tab:docred-count' on page 4 undefined on input line 2
29.


LaTeX Warning: Reference `tab:docred-bcs' on page 4 undefined on input line 229
.


Overfull \hbox (9.70404pt too wide) in paragraph at lines 231--232
[]\T1/cmr/m/n/10.95 The Do-cRED re-sults pro-vide di-rec-tion-ally con-sis-tent
 but weaker ev-i-dence com-pared to sentence-
[4]

LaTeX Warning: Reference `tab:scs-valid' on page 5 undefined on input line 254.



LaTeX Warning: Reference `sec:sdgd' on page 5 undefined on input line 256.


LaTeX Warning: Reference `tab:interaction' on page 5 undefined on input line 28
0.

[5]

LaTeX Warning: Reference `tab:sdgd-maven' on page 6 undefined on input line 322
.


LaTeX Warning: Reference `tab:random-ablation' on page 6 undefined on input lin
e 324.


LaTeX Warning: Reference `tab:sdgd-cal-fewnerd' on page 6 undefined on input li
ne 364.


LaTeX Warning: Reference `tab:sdgd-cal-maven' on page 6 undefined on input line
 364.


LaTeX Warning: Reference `tab:pertype' on page 6 undefined on input line 389.

[6]

LaTeX Warning: Reference `sec:interaction' on page 7 undefined on input line 41
2.


LaTeX Warning: Reference `sec:scs-valid' on page 7 undefined on input line 412.


[7]
Overfull \hbox (3.18178pt too wide) in paragraph at lines 421--422
\T1/cmr/m/n/10.95 via schema de-com-po-si-tion re-mains an open chal-lenge. All
 de-com-po-si-tion approaches---embedding-
[8] [9] (./paper.aux)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texlive
2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.texli
ve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.tex
live2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/.t
exlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubuntu/
.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubunt
u/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/ubu
ntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home/u
buntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/home
/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share
/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ
ic/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmsy8.pfb>
Output written on paper.pdf (9 pages, 217934 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
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
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
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
nts/map/pdftex/updmap/pdftex.map}]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 81.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\rightarrow' on input line 81.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 81.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 85.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\rightarrow' on input line 85.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 85.

[2] [3]
Overfull \hbox (9.70404pt too wide) in paragraph at lines 231--232
[]\T1/cmr/m/n/10.95 The Do-cRED re-sults pro-vide di-rec-tion-ally con-sis-tent
 but weaker ev-i-dence com-pared to sentence-
[4] [5] [6] [7]
Overfull \hbox (3.18178pt too wide) in paragraph at lines 421--422
\T1/cmr/m/n/10.95 via schema de-com-po-si-tion re-mains an open chal-lenge. All
 de-com-po-si-tion approaches---embedding-
[8] [9] (./paper.aux) )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texlive
2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.texli
ve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.tex
live2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/.t
exlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubuntu/
.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubunt
u/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/ubu
ntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home/u
buntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/home
/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share
/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ
ic/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmsy8.pfb>
Output written on paper.pdf (9 pages, 219484 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be07ef9e-8466-402b-a05e-102c969858ca",
  "isSidechain": false,
  "promptId": "fc49f735-e722-4cc2-9426-bb861b70dea7",
  "type": "user",
  "uuid": "8e3c49a8-68bb-443b-ba99-d02b0a19616d",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 81.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\rightarrow' on input line 81.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 81.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 85.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\rightarrow' on input line 85.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 85.\n\n[2]\n\nLaTeX Warning: Reference `tab:error-ner' on page 3 undefined on input line 173.\n\n\n\nLaTeX Warning: Reference `tab:error-re' on page 3 undefined on input line 173.\n\n[3]\n\nLaTeX Warning: Reference `tab:docred-count' on page 4 undefined on input line 2\n29.\n\n\nLaTeX Warning: Reference `tab:docred-bcs' on page 4 undefined on input line 229\n.\n\n\nOverfull \\hbox (9.70404pt too wide) in paragraph at lines 231--232\n[]\\T1/cmr/m/n/10.95 The Do-cRED re-sults pro-vide di-rec-tion-ally con-sis-tent\n but weaker ev-i-dence com-pared to sentence-\n[4]\n\nLaTeX Warning: Reference `tab:scs-valid' on page 5 undefined on input line 254.\n\n\n\nLaTeX Warning: Reference `sec:sdgd' on page 5 undefined on input line 256.\n\n\nLaTeX Warning: Reference `tab:interaction' on page 5 undefined on input line 28\n0.\n\n[5]\n\nLaTeX Warning: Reference `tab:sdgd-maven' on page 6 undefined on input line 322\n.\n\n\nLaTeX Warning: Reference `tab:random-ablation' on page 6 undefined on input lin\ne 324.\n\n\nLaTeX Warning: Reference `tab:sdgd-cal-fewnerd' on page 6 undefined on input li\nne 364.\n\n\nLaTeX Warning: Reference `tab:sdgd-cal-maven' on page 6 undefined on input line\n 364.\n\n\nLaTeX Warning: Reference `tab:pertype' on page 6 undefined on input line 389.\n\n[6]\n\nLaTeX Warning: Reference `sec:interaction' on page 7 undefined on input line 41\n2.\n\n\nLaTeX Warning: Reference `sec:scs-valid' on page 7 undefined on input line 412.\n\n\n[7]\nOverfull \\hbox (3.18178pt too wide) in paragraph at lines 421--422\n\\T1/cmr/m/n/10.95 via schema de-com-po-si-tion re-mains an open chal-lenge. All\n de-com-po-si-tion approaches---embedding-\n[8] [9] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/home\n/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share\n/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\nic/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\nm/cmsy8.pfb>\nOutput written on paper.pdf (9 pages, 217934 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 81.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\rightarrow' on input line 81.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 81.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 85.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\rightarrow' on input line 85.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 85.\n\n[2] [3]\nOverfull \\hbox (9.70404pt too wide) in paragraph at lines 231--232\n[]\\T1/cmr/m/n/10.95 The Do-cRED re-sults pro-vide di-rec-tion-ally con-sis-tent\n but weaker ev-i-dence com-pared to sentence-\n[4] [5] [6] [7]\nOverfull \\hbox (3.18178pt too wide) in paragraph at lines 421--422\n\\T1/cmr/m/n/10.95 via schema de-com-po-si-tion re-mains an open chal-lenge. All\n de-com-po-si-tion approaches---embedding-\n[8] [9] (./paper.aux) )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/home\n/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share\n/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\nic/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\nm/cmsy8.pfb>\nOutput written on paper.pdf (9 pages, 219484 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "be07ef9e-8466-402b-a05e-102c969858ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/median",
  "sessionId": "4d779de5-396b-49dc-acca-1976fdd39e66",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T073533 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extr…",
  "leafUuid": "8e3c49a8-68bb-443b-ba99-d02b0a19616d",
  "sessionId": "4d779de5-396b-49dc-acca-1976fdd39e66"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper with LaTeX compilation",
  "sessionId": "4d779de5-396b-49dc-acca-1976fdd39e66"
}
```

---

### Assistant

_source line 30 · 2026-05-16T08:02:21.393Z_

编译成功，9 页 PDF，无错误。所有 9 个实验均有对应 table/section，所有数字来自 `experiment_data.json`。

输出文件：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/median/paper.pdf`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e3c49a8-68bb-443b-ba99-d02b0a19616d",
  "isSidechain": false,
  "requestId": "req_011Cb5u2kvHVbSTXtd7TrwS1",
  "type": "assistant",
  "uuid": "3e22cf14-8fca-4b4c-a8b3-b391d62d4767",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/median",
  "sessionId": "4d779de5-396b-49dc-acca-1976fdd39e66",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LVnowkm2Lg9Xfz5Y4ZZChh",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6858,
      "cache_read_input_tokens": 50606,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6858,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 106,
          "cache_read_input_tokens": 50606,
          "cache_creation_input_tokens": 6858,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6858
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

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T073533 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extr…",
  "leafUuid": "3e22cf14-8fca-4b4c-a8b3-b391d62d4767",
  "sessionId": "4d779de5-396b-49dc-acca-1976fdd39e66"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper with LaTeX compilation",
  "sessionId": "4d779de5-396b-49dc-acca-1976fdd39e66"
}
```

---
