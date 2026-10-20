# Research conversation: [DREAM Review Director] dream_id=20260521T122440 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 3
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/48af77a8-24b1-406c-8f2b-6ae7c5af4a8e.jsonl`
- **Structured JSON:** [`b51da49bf36ab0b7e26f.json`](../../sessions/b5/b51da49bf36ab0b7e26f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T13:13:22.332Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T13:13:22.332Z",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e",
  "content": "[DREAM Review Director]\ndream_id=20260521T122440 | review_mode=simple | review_visible=True\nPDF: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/median/review_input_e90a5c14.pdf\n\n（内部编排信息：tier=median，仅用于 submit_dream_review_report 调用。\n你在向 Reviewer 发送审稿任务时，**严禁**提及档位名称 best/median/worst，\n也不要暗示论文结果的好坏。Reviewer 必须盲审。）\n\n任务：对上述 PDF 进行 simple 模式审稿。 使用 `dream-review-simple` skill 的 dispatch 模板（1 Reviewer 全面覆盖，跳过 Step 2 交叉分享 + Step 3 收敛）。\n\n## 目标 Venue 审稿标准（emnlp-2026）\n\n评分刻度（ARR Overall Assessment，1-5 半分制）：\n- 5 = 可考虑最佳论文奖（top 2.5%）\n- 4 = 可被 ACL 会议接收\n- 3 = 可被 Findings 接收\n- 2 = 需大幅修改重投\n- 1 = 不要重投\n\n接受率：ACL/EMNLP Main ~21%（约 5 篇投稿接收 1 篇）\n评审维度：Soundness (1-5) + Excitement (1-5) + Reproducibility (1-5)\n强制 Responsible NLP Research Checklist（Section A-E），不完整/误导性填写被 desk reject。\n自动 reject 信号：匿名性违规、超页数限制、缺 Limitations section、幻觉引用。\n\n请严格按照上述评分刻度和接受率校准你的评分。\n\n## 实验设计参考\n\n完整实验设计（含想象实验列表）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/median/review_context.yaml`\n论文可能未完整反映所有实验——参考此文件判断覆盖度。\n完成后必须调用 `submit_dream_review_report(report, project=\"irt_equated_bench_regen\", tier=\"median\", dream_id=\"20260521T122440\", review_visible=True)` —— 报告会写入 dream_reports/dream_20260521T122440/median/review_report.md，编排进程通过 subprocess 退出读取它。\n不要调用 submit_review_report_to_research_director / update_review_issues / request_external_review —— 这些工具不在 Dream Review Director 白名单内。\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T13:13:22.346Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T13:13:22.346Z",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e"
}
```

---

## Round 1

17 recorded events

### User

_source line 3 · 2026-05-21T13:13:22.462Z_

[DREAM Review Director]
dream_id=20260521T122440 | review_mode=simple | review_visible=True
PDF: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/median/review_input_e90a5c14.pdf

（内部编排信息：tier=median，仅用于 submit_dream_review_report 调用。
你在向 Reviewer 发送审稿任务时，**严禁**提及档位名称 best/median/worst，
也不要暗示论文结果的好坏。Reviewer 必须盲审。）

任务：对上述 PDF 进行 simple 模式审稿。 使用 `dream-review-simple` skill 的 dispatch 模板（1 Reviewer 全面覆盖，跳过 Step 2 交叉分享 + Step 3 收敛）。

## 目标 Venue 审稿标准（emnlp-2026）

评分刻度（ARR Overall Assessment，1-5 半分制）：
- 5 = 可考虑最佳论文奖（top 2.5%）
- 4 = 可被 ACL 会议接收
- 3 = 可被 Findings 接收
- 2 = 需大幅修改重投
- 1 = 不要重投

接受率：ACL/EMNLP Main ~21%（约 5 篇投稿接收 1 篇）
评审维度：Soundness (1-5) + Excitement (1-5) + Reproducibility (1-5)
强制 Responsible NLP Research Checklist（Section A-E），不完整/误导性填写被 desk reject。
自动 reject 信号：匿名性违规、超页数限制、缺 Limitations section、幻觉引用。

请严格按照上述评分刻度和接受率校准你的评分。

## 实验设计参考

完整实验设计（含想象实验列表）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/median/review_context.yaml`
论文可能未完整反映所有实验——参考此文件判断覆盖度。
完成后必须调用 `submit_dream_review_report(report, project="irt_equated_bench_regen", tier="median", dream_id="20260521T122440", review_visible=True)` —— 报告会写入 dream_reports/dream_20260521T122440/median/review_report.md，编排进程通过 subprocess 退出读取它。
不要调用 submit_review_report_to_research_director / update_review_issues / request_external_review —— 这些工具不在 Dream Review Director 白名单内。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "574ea9fb-2433-4f53-83c6-6ff0f801abc3",
  "type": "user",
  "uuid": "894ce6df-10b7-42e3-b485-81ae1c460d40",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T13:13:22.461Z_

```json
{
  "parentUuid": "894ce6df-10b7-42e3-b485-81ae1c460d40",
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
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
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
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "7560d2ba-0a88-4df2-92f3-20b4ad918310",
  "timestamp": "2026-05-21T13:13:22.461Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T13:13:22.461Z_

```json
{
  "parentUuid": "7560d2ba-0a88-4df2-92f3-20b4ad918310",
  "isSidechain": false,
  "attachment": {
    "type": "mcp_instructions_delta",
    "addedNames": [
      "agent-ml-research"
    ],
    "addedBlocks": [
      "## agent-ml-research\nML research experiment management tools"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "7cdbfb61-2c76-4d16-a28b-7dd5de6645b8",
  "timestamp": "2026-05-21T13:13:22.461Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 6 · 2026-05-21T13:13:22.461Z_

```json
{
  "parentUuid": "7cdbfb61-2c76-4d16-a28b-7dd5de6645b8",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c6f89367-2acc-41c1-bd77-b0dd72602b7c",
  "timestamp": "2026-05-21T13:13:22.461Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e",
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
  "aiTitle": "Review IRT equated benchmark paper",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e"
}
```

---

### Assistant

_source line 8 · 2026-05-21T13:13:27.310Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to perform a dream review of a paper PDF. Let me break down the task:

1. I need to review a PDF at a specific path
2. Use the `dream-review-simple` skill dispatch template (1 Reviewer, skip Step 2 and Step 3)
3. Review against EMNLP 2026 standards
4. Submit the review via `submit_dream_review_report`

Let me start by:
1. Reading the PDF
2. Reading the review context YAML
3. Then performing the review and submitting

Let me read the PDF and the review context in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6f89367-2acc-41c1-bd77-b0dd72602b7c",
  "isSidechain": false,
  "requestId": "req_011CbFmoMB9Ld78eGvCdhbKx",
  "type": "assistant",
  "uuid": "e6592fd0-ab7f-44ed-91ee-33c22d700050",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Anrc3k9wovUp6HaYdyWoZ1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12333,
      "cache_read_input_tokens": 11841,
      "output_tokens": 360,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12333,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 360,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12333,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12333
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

_source line 9 · 2026-05-21T13:13:28.369Z_

<details open><summary>🔧 Tool call — Read · `toolu_01488ia8VJfVU3jsAh9k8EK5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/median/review_input_e90a5c14.pdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6592fd0-ab7f-44ed-91ee-33c22d700050",
  "isSidechain": false,
  "requestId": "req_011CbFmoMB9Ld78eGvCdhbKx",
  "type": "assistant",
  "uuid": "131b3cd5-5d1b-498f-a31b-bd2f44595494",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Anrc3k9wovUp6HaYdyWoZ1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12333,
      "cache_read_input_tokens": 11841,
      "output_tokens": 360,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12333,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 360,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12333,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12333
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

_source line 10 · 2026-05-21T13:13:28.530Z_

<details><summary>↩ Tool result · reported error · `toolu_01488ia8VJfVU3jsAh9k8EK5`</summary>

```text
This PDF has 11 pages, which is too many to read at once. Use the pages parameter to read specific page ranges (e.g., pages: "1-5"). Maximum 20 pages per request.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "131b3cd5-5d1b-498f-a31b-bd2f44595494",
  "isSidechain": false,
  "promptId": "574ea9fb-2433-4f53-83c6-6ff0f801abc3",
  "type": "user",
  "uuid": "b6dd1c39-8d75-4df6-8e3e-df7098ad732f",
  "toolUseResult": "Error: This PDF has 11 pages, which is too many to read at once. Use the pages parameter to read specific page ranges (e.g., pages: \"1-5\"). Maximum 20 pages per request.",
  "sourceToolAssistantUUID": "131b3cd5-5d1b-498f-a31b-bd2f44595494",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T13:13:28.707Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PtdG7xKAj9AcS3Eoo69hNn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/median/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6dd1c39-8d75-4df6-8e3e-df7098ad732f",
  "isSidechain": false,
  "requestId": "req_011CbFmoMB9Ld78eGvCdhbKx",
  "type": "assistant",
  "uuid": "1aaeaba9-4e3e-43f2-a359-9efff8d2f7fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Anrc3k9wovUp6HaYdyWoZ1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12333,
      "cache_read_input_tokens": 11841,
      "output_tokens": 360,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12333,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 360,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12333,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12333
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

_source line 12 · 2026-05-21T13:13:29.297Z_

<details><summary>↩ Tool result · `toolu_01PtdG7xKAj9AcS3Eoo69hNn`</summary>

```text
1	narrative_guidance: 'Median 档下 permutation null C% 落在 2–8%，表明 temporal label 本身携带弱结构性信号
2	  （model release date 与 ability 不完全正交），但 31% 仍为 null 的 4–15×，统计意义明确。 Claim 1 headline
3	  须从 ''31%'' 调整为 ''~25–29% after confound controls''，permutation null 显式报告为 calibration
4	  baseline。Claim 2 meta-critique 软化为 ''complementary approaches needed''， 不再用 ''fundamentally
5	  mismatched''。Claim 3 cross-benchmark 证据降级 appendix，主体仅保留 MMLU。 Claim 4 diagnostic
6	  lens 升格为 abstract 第二句，强调 audit protocol 实用价值以对冲 ''applying textbook psychometrics''
7	  的 novelty 质疑。Rebuttal 准备 ''psychometric tools are mature but their application to
8	  LLM benchmarks at this scale is novel'' 防线。 Simpson''s paradox（plan_030 Model 2
9	  vs Model 1）需谨慎处理因果表述，仅作为 supplementary evidence。 预期 reviewer score 2.5–3.5，borderline
10	  accept/weak reject，需要 rebuttal 翻盘。
11	
12	  '
13	imagined_experiments:
14	- name: real_data_dif_mmlu
15	  plan_id: plan_001
16	  description: '对 METABENCH MMLU 响应矩阵 (5219×12508) 执行全面 MH-DIF 分析， 包含 temporal/ability
17	    cohort、within-family confound control、domain specificity。
18	
19	    '
20	  expected_results:
21	    temporal_ets_c_pct: 31.3
22	    temporal_fpr_li_clean: 0.322
23	    temporal_enrichment: 0.964
24	    ability_ets_c_pct: 3.1
25	    ability_fpr_li_clean: 0.029
26	    ability_enrichment: 1.15
27	    within_family_llama2v3_c_pct: 58.7
28	    within_family_mistral_mixtral_c_pct: 36.2
29	    domain_spearman_rho: 0.32
30	    domain_spearman_p: 0.016
31	    sanity_random_split_c_pct: 0.21
32	    temporal_ability_jaccard: 0.016
33	    n_subjects_with_c_gt20pct: 57
34	    unweighted_subject_mean_c_pct: 30.4
35	    subject_c_range: 20.1–47.8%
36	    decoder_only_pct: 99.98
37	  result_rationale: 'Median 档下 temporal C%=31.3% 与已有 registry 一致（这是实测值，不受 tier 影响）。
38	    关键区别在于后续 controls 将把 residual 压至 25–29%。Within-family Llama-2v3 C% 略低于 registry
39	    的 61.3%（~58.7%），因为 median 档假设 ability confound 解释更多 variance （d=-0.99 对中 ability
40	    gap 较大）。Domain ρ=0.32 表明 subject-level accuracy improvement 与 DIF 存在弱正相关，但 item-level
41	    decomposition 将显示域改善仅解释 ≤3.5pp。Random-split sanity check 0.21% 确认 temporal signal
42	    非统计噪声。 Enrichment≈0.96 确认 DIF 与 web-overlap labels 正交——这是预期行为，非方法失败。
43	
44	    '
45	  tables:
46	  - name: 'Table 1: Temporal DIF Summary by Cohort Definition'
47	    columns:
48	    - cohort
49	    - n_ref
50	    - n_foc
51	    - n_items
52	    - c_pct
53	    - fpr_li_clean
54	    - enrichment
55	    rows:
56	    - - temporal_2023v2024
57	      - 1080
58	      - 807
59	      - 12508
60	      - 31.3
61	      - 0.322
62	      - 0.964
63	    - - ability_quintile
64	      - 2610
65	      - 2609
66	      - 12508
67	      - 3.1
68	      - 0.029
69	      - 1.15
70	    - - random_split_sanity
71	      - 950
72	      - 950
73	      - 12508
74	      - 0.21
75	      - 0.002
76	      - 1.01
77	  - name: 'Table 2: Within-Family Confound Control'
78	    columns:
79	    - family_pair
80	    - n_ref
81	    - n_foc
82	    - c_pct
83	    - overlap_with_temporal
84	    rows:
85	    - - Llama-2 vs Llama-3
86	      - 161
87	      - 308
88	      - 58.7
89	      - Jaccard=0.38
90	    - - Mistral vs Mixtral
91	      - 89
92	      - 112
93	      - 36.2
94	      - Jaccard=0.29
95	  figures_description:
96	  - 'Fig 1: 57-subject heatmap showing per-subject C% (rows) × cohort (cols), 色阶 20–48%'
97	  - 'Fig 2: Scatter plot of subject-level accuracy Δ vs C%, ρ=0.32, p=0.016'
98	  analysis: '31.3% temporal instability 是 robust finding。Ability cohort 的 3.1% 确认
99	    DIF signal 与 temporal split 强关联而非 ability artifact。Within-family 的高 C% （Llama-2v3:
100	    58.7%）混淆了 capability gain 和 contamination——这不是理想的 confound control 因为 family 内
101	    ability gap 过大（d≈-0.99）。Domain ρ=0.32 是 ecological correlation，item-level decomposition
102	    将在 plan_019/030 中展开。
103	
104	    '
105	- name: rl_robustness_validation
106	  plan_id: plan_002
107	  description: '验证 DIF 对 RL-trained models 的鲁棒性：alignment-RL (DPO/ORPO) cohort 从 METABENCH
108	    提取，reasoning-RL (GRPO/PPO) 10–15 个模型需额外推理。
109	
110	    '
111	  expected_results:
112	    n_alignment_rl_models: 477
113	    n_reasoning_rl_models: 13
114	    dif_c_pct_baseline_sft_only: 30.8
115	    dif_c_pct_with_alignment_rl: 31.1
116	    dif_c_pct_with_reasoning_rl: 30.5
117	    jaccard_sft_vs_alignment: 0.91
118	    jaccard_sft_vs_reasoning: 0.84
119	    constat_auroc_non_rl: 0.72
120	    constat_auroc_reasoning_rl: 0.58
121	    mink_auroc_non_rl: 0.68
122	    mink_auroc_reasoning_rl: 0.51
123	    delong_dif_vs_constat_p: 0.34
124	    tost_equivalence_dif_retention: 90% CI [0.88, 0.97], equivalence bound ±0.10
125	    tost_conclusion: equivalent
126	    power_analysis_detection_boundary_p: 0.45
127	    bootstrap_ci_auroc_dif:
128	    - 0.76
129	    - 0.89
130	  result_rationale: 'Median 档下 DIF 作为 group-level method 对 cohort composition 变化不敏感——添加
131	    13 个 reasoning-RL 模型到 N=807 focal cohort 几乎不改变 group statistics。 Jaccard=0.84（vs
132	    reasoning-RL）略低于 alignment-RL 的 0.91，因为 reasoning-RL 模型在部分 hard items 上的 response
133	    pattern 与 SFT 模型有系统性差异（GRPO 训练 改变了 reasoning chain 而非单纯记忆）。传统 per-model detectors
134	    在 reasoning-RL 上退化显著（ConStat 从 0.72→0.58, Min-K% 从 0.68→0.51），因为 RL 训练平滑了 NLL
135	    distribution。但 N=13 使得所有 pairwise comparison 的 CI 极宽，DeLong test 无显著差异（p=0.34），TOST
136	    equivalence 勉强成立。这是 median 档的典型情况： 方向正确但统计力不足以支撑强 claim。
137	
138	    '
139	  tables:
140	  - name: 'Table: DIF Stability Across Cohort Compositions'
141	    columns:
142	    - cohort_composition
143	    - n_focal
144	    - c_pct
145	    - jaccard_vs_baseline
146	    rows:
147	    - - SFT-only baseline
148	      - 620
149	      - 30.8
150	      - 1.0
151	    - - + alignment-RL (DPO/ORPO)
152	      - 807
153	      - 31.1
154	      - 0.91
155	    - - + reasoning-RL (GRPO/PPO)
156	      - 820
157	      - 30.5
158	      - 0.84
159	  - name: 'Table: Per-Model Detector AUROC Comparison'
160	    columns:
161	    - detector
162	    - non_rl
163	    - alignment_rl
164	    - reasoning_rl
165	    rows:
166	    - - DIF (group)
167	      - N/A
168	      - N/A
169	      - N/A
170	    - - ConStat
171	      - 0.72
172	      - 0.67
173	      - 0.58
174	    - - Min-K%
175	      - 0.68
176	      - 0.64
177	      - 0.51
178	  figures_description:
179	  - 'Fig: Detection power curve — DIF ΔTPR vs exploitation rate p ∈ [0.4, 1.0], 标注
180	    detection boundary p≈0.45'
181	  analysis: 'DIF 的 group-level 设计使其对 cohort composition 天然鲁棒——13 个 RL 模型在 N=807 中占比
182	    <2%，统计影响可忽略。真正的 claim 应限定为 "DIF 在 cohort 中 RL 占比 <5% 时 robust"，而非 "DIF 对 RL 鲁棒"。Per-model
183	    detector 退化方向正确但 N=13 使结论 仅为 suggestive。降级为 limitations 中 disclosure，不作为 numbered
184	    contribution。
185	
186	    '
187	- name: constat_perturbation_eval
188	  plan_id: plan_003a
189	  description: '独立评估 ConStat-style perturbation testing：LLM 生成 200+ MMLU items 的语义等价
190	    reformulation，比较原始与改写版本的 model performance。
191	
192	    '
193	  expected_results:
194	    n_items_reformulated: 220
195	    reformulation_semantic_sim: 0.92
196	    constat_fdr_controlled_flags: 47
197	    constat_flag_rate: 0.214
198	    constat_overlap_with_dif_c: Jaccard=0.18
199	    constat_tpr_non_rl_known_contam: 0.61
200	    constat_tpr_rl_known_contam: 0.29
201	    constat_fpr: 0.08
202	    effect_size_non_rl: 0.74
203	    effect_size_rl: 0.31
204	    gpu_hours_used: 65
205	  result_rationale: 'Median 档下 ConStat 在 non-RL 模型上表现尚可（TPR=0.61, effect size=0.74），因为
206	    verbatim memorization 使模型对 surface-form 变化敏感。但 RL-trained 模型（尤其 GRPO/PPO）通过 reasoning
207	    generalization 降低了对 exact wording 的依赖，TPR 降至 0.29。与 DIF 的低重叠（Jaccard=0.18）符合预期：ConStat
208	    检测 per-model surface-level memorization，DIF 检测 group-level differential functioning，二者捕捉不同信号。
209	    FDR-controlled flag rate 21.4% 低于 DIF 的 31.3%，因为 ConStat 需要更强的 per-item evidence。GPU
210	    成本 65h 主要用于 reformulation generation 和 inference。
211	
212	    '
213	  tables:
214	  - name: 'Table: ConStat Detection Power by Model Type'
215	    columns:
216	    - model_type
217	    - n_models
218	    - tpr
219	    - fpr
220	    - effect_size
221	    rows:
222	    - - SFT-only
223	      - 15
224	      - 0.61
225	      - 0.08
226	      - 0.74
227	    - - Alignment-RL
228	      - 10
229	      - 0.48
230	      - 0.07
231	      - 0.55
232	    - - Reasoning-RL
233	      - 8
234	      - 0.29
235	      - 0.09
236	      - 0.31
237	  figures_description:
238	  - 'Fig: ConStat flag rate vs DIF C% per subject — weak positive correlation'
239	  analysis: 'ConStat 作为 standalone baseline 有价值但不足以支撑 paper claim。与 DIF 的互补性 是 ensemble
240	    fusion（plan_003c）的理论基础，但 median 档下 RL 模型上的退化使得 ensemble 增益有限。结果降级为 appendix baseline
241	    comparison。
242	
243	    '
244	- name: dvd_generation_variance_eval
245	  plan_id: plan_003b
246	  description: '独立评估 DVD generation variance：10–15 个 open-weight 模型在每个 item 上生成 50
247	    次 response，计算 generation variance 并检测 bimodal distribution。
248	
249	    '
250	  expected_results:
251	    n_models_tested: 12
252	    n_items_scored: 12508
253	    responses_per_item: 50
254	    dvd_bimodal_flag_rate: 0.089
255	    dvd_tpr_verbatim_contam: 0.43
256	    dvd_tpr_variant_contam: 0.52
257	    dvd_fpr: 0.062
258	    dvd_overlap_with_dif_c: Jaccard=0.11
259	    gpu_hours_used: 58
260	    temperature_sensitivity: 'T=0.7: flag_rate=0.089; T=1.0: flag_rate=0.142'
261	  result_rationale: 'Median 档下 DVD 的 bimodal detection 在 variant contamination 上略优于
262	    verbatim （TPR 0.52 vs 0.43），因为 variant contamination 产生更明显的 generation variance
263	    bimodality（模型在 "近似记忆" 和 "真正推理" 之间切换）。但整体 flag rate 仅 8.9%， 远低于 DIF 的 31.3%，因为
264	    DVD 需要 per-model inference 且仅在 generation distribution 层面操作。与 DIF 的极低重叠（Jaccard=0.11）表明二者检测完全不同维度。
265	    Temperature 敏感性（T=1.0 时 flag rate 翻倍至 14.2%）暴露了 hyperparameter tuning 问题。GPU 成本
266	    58h 用于 12 模型 × 12508 items × 50 responses 的推理。
267	
268	    '
269	  tables:
270	  - name: 'Table: DVD Detection by Contamination Type'
271	    columns:
272	    - contam_type
273	    - tpr
274	    - fpr
275	    - bimodal_strength
276	    rows:
277	    - - verbatim
278	      - 0.43
279	      - 0.062
280	      - Cohen's h=0.38
281	    - - variant
282	      - 0.52
283	      - 0.058
284	      - Cohen's h=0.47
285	    - - clean
286	      - N/A
287	      - 0.062
288	      - Cohen's h=0.04
289	  figures_description:
290	  - 'Fig: Generation variance distribution — bimodal (contaminated) vs unimodal (clean)
291	    items'
292	  analysis: 'DVD 捕捉的是 per-model generation-level signal，与 DIF 的 group-level item functioning
293	    signal 几乎不重叠。作为独立检测器价值有限（TPR<0.55），但为 ensemble 提供了独特的 variant contamination 覆盖。Temperature
294	    敏感性需要在 paper 中 disclose。
295	
296	    '
297	- name: ensemble_fusion
298	  plan_id: plan_003c
299	  description: '将 DIF + ConStat + DVD 融合为 multi-signal ensemble，评估 majority voting
300	    和 weighted fusion 策略。
301	
302	    '
303	  expected_results:
304	    ensemble_2of3_tpr: 0.54
305	    ensemble_2of3_fpr: 0.045
306	    ensemble_weighted_tpr: 0.59
307	    ensemble_weighted_fpr: 0.052
308	    ensemble_coverage_dif_only: δ≥1.4
309	    ensemble_coverage_constat_only: non-RL δ≥0.6
310	    ensemble_coverage_dvd_only: variant contamination
311	    cross_val_weight_stability: 'DIF: 0.52±0.08, ConStat: 0.31±0.06, DVD: 0.17±0.05'
312	    uniform_vs_optimized_tpr_delta: 0.03
313	    fpr_all_configs_below_010: true
314	  result_rationale: 'Median 档下 ensemble 增益有限，因为三个信号的重叠极低（pairwise Jaccard 0.11–0.18），
315	    majority voting 在 low-overlap 情况下倾向于保守（TPR=0.54）。Weighted fusion 略优（TPR=0.59）但
316	    cross-validation weight stability 显示 DIF 权重主导（0.52）， ConStat 和 DVD 的贡献边际化。关键问题：DIF
317	    是 group-level，ConStat/DVD 是 per-model-level，fusion 的语义不一致使 ensemble 设计缺乏理论基础。Median
318	    档下 reviewers 会质疑 "为什么要 fuse fundamentally different signal types"。 结论：ensemble
319	    负面结果，not executed in final paper，降级为 future work。
320	
321	    '
322	  tables:
323	  - name: 'Table: Ensemble Fusion Comparison'
324	    columns:
325	    - strategy
326	    - tpr
327	    - fpr
328	    - coverage_description
329	    rows:
330	    - - DIF only
331	      - 0.508
332	      - 0.314
333	      - group-level, δ≥1.4
334	    - - 2-of-3 majority
335	      - 0.54
336	      - 0.045
337	      - intersection of signals
338	    - - weighted fusion
339	      - 0.59
340	      - 0.052
341	      - combined coverage
342	    - - uniform weight
343	      - 0.56
344	      - 0.048
345	      - unweighted average
346	  figures_description:
347	  - 'Fig: Venn diagram of flag overlap — DIF ∩ ConStat ∩ DVD showing minimal 3-way
348	    overlap'
349	  analysis: 'Ensemble 的 FPR 显著改善（0.045 vs DIF 单独的 0.314），但代价是 TPR 仅从 DIF ΔTPR 基线略有提升。信号类型不同质（group
350	    vs per-model）使 fusion 缺乏 principled justification。Median 档下这是 negative result——not
351	    executed, dropped to future work。
352	
353	    '
354	- name: cross_benchmark_gsm8k
355	  plan_id: plan_004
356	  description: '在 GSM8K 上复制 DIF 分析，使用 GSM1K 作为 contamination ground truth， 验证 cross-benchmark
357	    泛化性。
358	
359	    '
360	  expected_results:
361	    gsm8k_n_items: 1319
362	    gsm8k_n_ref: 1017
363	    gsm8k_n_foc: 804
364	    gsm8k_standard_c_pct: 18.9
365	    gsm8k_external_c_pct: 45.1
366	    gsm8k_sanity_c_pct: 0.35
367	    semi_synthetic_delta_tpr_p10: 0.78
368	    semi_synthetic_delta_tpr_p05: 0.44
369	    semi_synthetic_external_delta_tpr_p10: 0.49
370	    gsm1k_n_models: 33
371	    gsm1k_pearson_r: -0.478
372	    gsm1k_pearson_p: 0.005
373	    gsm1k_spearman_rho: -0.39
374	    gsm1k_spearman_p: 0.025
375	    gsm1k_partial_r: -0.37
376	    gsm1k_partial_p: 0.035
377	    gsm1k_ci_upper_abs_r: 0.155
378	    direction: NEGATIVE — opposite to contamination hypothesis
379	    cook_d_max_model: Deepseek-math-7b-rl
380	    leave_one_out_r_range:
381	    - -0.52
382	    - -0.36
383	  result_rationale: 'Median 档下 GSM8K temporal C%=18.9% 低于 MMLU 的 31.3%，因为 GSM8K 是
384	    single-domain math benchmark（1319 items），domain homogeneity 降低了 DIF 的 item-level
385	    variance。 Semi-synthetic ΔTPR 在 p=0.5 时为 0.44，落在 median 档范围 [0.35, 0.5] 内。 GSM1K
386	    negative correlation（r=-0.478）是 median 档核心尴尬点：DIF-C items anti-correlate with
387	    contamination gap，需要额外解释 "DIF ≠ contamination detector, DIF detects differential
388	    item functioning which may reflect capability gain on hard items rather than memorization"。N=33
389	    使 CI 宽且 upper bound |r|=0.155 允许 near-zero true effect。Spearman ρ=-0.39 弱于 Pearson，暗示
390	    outlier 影响。 整体降级为 exploratory，不进 abstract/conclusion。
391	
392	    '
393	  tables:
394	  - name: 'Table: GSM8K Temporal DIF Summary'
395	    columns:
396	    - metric
397	    - standard_mh
398	    - external_matching
399	    - sanity
400	    rows:
401	    - - C%
402	      - 18.9
403	      - 45.1
404	      - 0.35
405	    - - n_items_flagged
406	      - 249
407	      - 595
408	      - 5
409	    - - DIF favor 2024
410	      - 78
411	      - 210
412	      - 2
413	    - - DIF favor 2023
414	      - 171
415	      - 385
416	      - 3
417	  - name: 'Table: GSM1K Correlation Analysis'
418	    columns:
419	    - statistic
420	    - value
421	    - p_value
422	    - 95% CI
423	    rows:
424	    - - Pearson r
425	      - -0.478
426	      - 0.005
427	      - '[-0.71, -0.16]'
428	    - - Spearman ρ
429	      - -0.39
430	      - 0.025
431	      - '[-0.66, -0.03]'
432	    - - Partial r (ctrl accuracy)
433	      - -0.37
434	      - 0.035
435	      - '[-0.64, -0.01]'
436	  figures_description:
437	  - 'Fig: Scatter of per-model DIF-C proportion vs GSM8K-GSM1K gap, r=-0.478, 标注 Cook''s
438	    D outliers'
439	  analysis: 'GSM8K 复制确认了 framework portability（ΔTPR 有效），但 GSM1K correlation 的负方向 是
440	    median 档的关键弱点。必须在 paper 中用一段专门解释：DIF flags items whose functioning changed across
441	    generations, not items that are contaminated. Hard items where 2024 models improve
442	    may simultaneously show DIF (functioning changed) AND small contamination gap
443	    (capability improvement, not memorization)。 降级为 exploratory per Dream #6 consensus。
444	
445	    '
446	- name: bifactor_irt_equating_pilot
447	  plan_id: plan_005
448	  description: '在 METABENCH MMLU 数据上拟合 bifactor IRT 模型（general factor + 57 subject-specific
449	    factors），选择 anchor items 并执行 fixed-parameter calibration。
450	
451	    '
452	  expected_results:
453	    bifactor_rmsea: 0.038
454	    bifactor_cfi: 0.87
455	    bifactor_tli: 0.85
456	    bifactor_srmr: 0.052
457	    general_factor_variance_explained: 0.41
458	    n_anchor_items_selected: 2800
459	    anchor_stability_criterion: '|Δ_MH|<0.43 (ETS A)'
460	    equated_rho_vs_original: 0.94
461	    target_rho_met: false
462	    convergence_issues: 3 subjects failed to converge; fixed to unidimensional
463	    computation_time_hours: 38
464	  result_rationale: 'Median 档下 bifactor model 的 fit 低于 acceptable thresholds（CFI<0.90,
465	    TLI<0.90）， 因为 MMLU 的 57 subjects 引入了 57 个 specific factors 加 general factor =
466	    58 latent dimensions，5219 models 的 sample size 对此维度不足。General factor 仅解释 41% variance（理想
467	    >60%），说明 MMLU 本质上高度多维。3 个小样本 subjects 收敛失败 需要降级为 unidimensional。Equated ρ=0.94
468	    未达 target ρ≥0.95，主要因为 anchor item selection 受 bifactor misfit 影响。Median 档结论：bifactor
469	    equating 在 MMLU 上不 可行，confirmed paper_framing.md 中 "killed by plan_014 pre-check"
470	    的判断。 作为 negative result 报告在 limitations 中，motivate future multidimensional IRT。
471	
472	    '
473	  tables:
474	  - name: 'Table: Bifactor IRT Fit Indices'
475	    columns:
476	    - index
477	    - value
478	    - acceptable_threshold
479	    - verdict
480	    rows:
481	    - - RMSEA
482	      - 0.038
483	      - <0.06
484	      - PASS
485	    - - CFI
486	      - 0.87
487	      - '>0.90'
488	      - FAIL
489	    - - TLI
490	      - 0.85
491	      - '>0.90'
492	      - FAIL
493	    - - SRMR
494	      - 0.052
495	      - <0.08
496	      - PASS
497	    - - General factor ω_h
498	      - 0.41
499	      - '>0.60'
500	      - FAIL
501	  figures_description:
502	  - 'Fig: Scree plot — eigenvalue decay showing 57 factors above noise floor, no dominant
503	    general factor'
504	  analysis: 'Bifactor IRT equating killed。MMLU 的多维性使得单一 general factor 无法充分 表征 model
505	    ability，anchor item 选择受 model misfit 污染。这是 structural limitation 而非 implementation
506	    failure。Paper 中作为 "empirical observation that motivates future multidimensional
507	    IRT" 报告，不作为 contribution。
508	
509	    '
510	- name: item_generation_calibration
511	  plan_id: plan_006
512	  description: '为 DIF-flagged MMLU items 生成替换项，使用 LLM generation + student simulation
513	    进行 difficulty calibration。
514	
515	    '
516	  expected_results:
517	    n_items_generated: 500
518	    n_dif_items_targeted: 200
519	    difficulty_correlation_prompt_based: 0.28
520	    difficulty_correlation_student_sim: 0.71
521	    difficulty_correlation_empirical: 0.65
522	    construct_coverage_semantic_sim: 0.88
523	    holdout_panel_rho: 0.91
524	    gpu_hours_used: 160
525	    items_passing_quality_filter: 340
526	    quality_filter_rate: 0.68
527	  result_rationale: 'Median 档下 prompt-based difficulty targeting 的 ρ=0.28 远低于 student
528	    simulation 的 ρ=0.71，符合文献报告（arXiv 2602.06631: ρ=0.10–0.45）。Student simulation （arXiv
529	    2601.09953）的 ρ=0.71 低于该文献报告的 r=0.75–0.82，因为 MMLU 的 domain diversity 使 universal
530	    student simulator 难以 calibrate across 57 subjects。 Empirical calibration（实际跑 holdout
531	    model panel）的 ρ=0.65 进一步降低，因为 simulation-to-reality gap。Holdout panel ρ=0.91 低于
532	    equating target 0.95。 整体结论：item generation pipeline 可行但 precision 不足以支撑 equated
533	    replacement claim。降级为 supplementary methodology contribution。
534	
535	    '
536	  tables:
537	  - name: 'Table: Difficulty Estimation Method Comparison'
538	    columns:
539	    - method
540	    - difficulty_rho
541	    - n_items
542	    - compute_cost
543	    rows:
544	    - - Prompt-based targeting
545	      - 0.28
546	      - 500
547	      - 8 GPU-h
548	    - - Student simulation
549	      - 0.71
550	      - 500
551	      - 45 GPU-h
552	    - - Empirical (holdout panel)
553	      - 0.65
554	      - 340
555	      - 107 GPU-h
556	  figures_description:
557	  - 'Fig: Predicted vs actual difficulty scatter — student sim (ρ=0.71) vs prompt
558	    (ρ=0.28)'
559	  analysis: 'Item generation pipeline 的核心瓶颈是 difficulty calibration precision。 ρ=0.65–0.71
560	    不足以保证 equated score equivalence（需要 item-level precision 而非 correlation）。作为 methodology
561	    贡献有价值但不足以支撑 Claim 3 的 regeneration narrative。与 plan_005 bifactor failure 共同导致
562	    regeneration storyline 被完全 dropped。
563	
564	    '
565	- name: cumulative_bayesian_dif
566	  plan_id: plan_007
567	  description: '实现 cumulative Bayesian DIF priors (Sinharay et al., 2006)，模拟 4 轮连续
568	    benchmark administration，展示 evidence accumulation 带来的 power improvement。
569	
570	    '
571	  expected_results:
572	    single_admin_power_d10: 0.38
573	    cumulative_2_admin_power_d10: 0.52
574	    cumulative_3_admin_power_d10: 0.64
575	    cumulative_4_admin_power_d10: 0.71
576	    single_admin_power_d14: 0.68
577	    cumulative_3_admin_power_d14: 0.85
578	    fpr_single: 0.042
579	    fpr_cumulative_3: 0.048
580	    simulation_n_per_admin: 200
581	    simulation_n_items: 500
582	    simulation_n_reps: 1000
583	  result_rationale: 'Median 档下 cumulative Bayesian DIF 的 power improvement 从 0.38→0.71（d=1.0,
584	    4 administrations），符合 Sinharay et al. 的理论预测但略低于原文（原文 0.40→0.70 at 3 administrations，我们在
585	    4 administrations 才达到 0.71）。差距因为 LLM benchmark 的 non-stationarity——successive
586	    administrations 间 DIF pattern 不完全 stable（model ecosystem evolves），violating Bayesian
587	    prior 的 stationarity assumption。 FPR 从 0.042 到 0.048 的轻微 inflation 是 informative
588	    prior 带来的 false alarm cost。整体结论：simulation-only result，对 real-world benchmark
589	    monitoring 有 suggestive value 但未在真实数据上验证。降级为 appendix。
590	
591	    '
592	  tables:
593	  - name: 'Table: Cumulative Bayesian DIF Power by Administration'
594	    columns:
595	    - n_admins
596	    - power_d10
597	    - power_d14
598	    - fpr
599	    rows:
600	    - - 1
601	      - 0.38
602	      - 0.68
603	      - 0.042
604	    - - 2
605	      - 0.52
606	      - 0.78
607	      - 0.044
608	    - - 3
609	      - 0.64
610	      - 0.85
611	      - 0.046
612	    - - 4
613	      - 0.71
614	      - 0.89
615	      - 0.048
616	  figures_description:
617	  - 'Fig: Power accumulation curve — d=1.0 and d=1.4, showing diminishing returns
618	    after 3 administrations'
619	  analysis: 'Simulation-only, underdeveloped for main body。核心 insight（evidence accumulation
620	    improves detection of medium effects）是 textbook result，novelty 仅在 LLM benchmark
621	    场景化。Median 档 reviewers 会 flag "this is just running Sinharay''s method on simulated
622	    data"。降级为 appendix discussion。
623	
624	    '
625	- name: graceful_degradation_analysis
626	  plan_id: plan_008
627	  description: '分析 benchmark validity 在 progressive item replacement 下的 degradation：
628	    5%, 10%, 20%, 50% items replaced，评估 ranking stability, reliability, construct
629	    coverage。
630	
631	    '
632	  expected_results:
633	    rho_at_5pct_replacement: 0.999
634	    rho_at_10pct_replacement: 0.998
635	    rho_at_20pct_replacement: 0.995
636	    rho_at_50pct_replacement: 0.983
637	    reliability_alpha_original: 0.946
638	    reliability_alpha_at_20pct: 0.938
639	    reliability_alpha_at_50pct: 0.912
640	    construct_coverage_original: 57
641	    construct_coverage_at_50pct: 57
642	    n_subjects_losing_items_at_50pct: 12
643	    min_items_per_subject_at_50pct: 31
644	    theoretical_lower_bound_rho: ρ ≥ 1 - 2r/(1+r) where r = replacement rate
645	  result_rationale: 'Median 档下 MMLU 的极高 measurement redundancy（12,508 items across
646	    57 subjects） 使得即使 50% replacement 也仅将 ρ 降至 0.983。这是因为 MMLU 的 per-subject item
647	    pools 足够大（median 200+ items），random replacement 均匀分布在 subjects 间， 每个 subject 保留足够
648	    items 维持 reliable estimation。Reliability α 从 0.946 降至 0.912（50%）仍在 acceptable
649	    range。Construct coverage 不受影响因为 replacement 是 within-subject。关键 caveat：这假设 replacement
650	    items 的 psychometric properties 与 original 相近——plan_006 显示这不成立（ρ=0.65），实际 degradation
651	    会更严重。
652	
653	    '
654	  tables:
655	  - name: 'Table: Validity Metrics Under Progressive Replacement'
656	    columns:
657	    - replacement_rate
658	    - ranking_rho
659	    - cronbach_alpha
660	    - min_items_per_subject
661	    rows:
662	    - - 0%
663	      - 1.0
664	      - 0.946
665	      - 63
666	    - - 5%
667	      - 0.999
668	      - 0.944
669	      - 60
670	    - - 10%
671	      - 0.998
672	      - 0.941
673	      - 57
674	    - - 20%
675	      - 0.995
676	      - 0.938
677	      - 50
678	    - - 50%
679	      - 0.983
680	      - 0.912
681	      - 31
682	  figures_description:
683	  - 'Fig: Degradation curves — ρ and α as function of replacement rate, with theoretical
684	    lower bound'
685	  analysis: '结果实际上强化了 Claim 4 的 redundancy narrative：MMLU 的 ranking stability 对 item
686	    removal/replacement 极其鲁棒。但 median 档下这个结果是 double-edged—— 如果 removing 31% DIF items
687	    doesn''t matter（ρ=0.997），reviewer 会问 "so what''s the practical impact of your
688	    finding?" 需要 reframe 为 diagnostic value 而非 quality concern。降级为 supplementary evidence
689	    for Claim 4.1 redundancy。
690	
691	    '
692	- name: item_focused_trees
693	  plan_id: plan_009
694	  description: '实现 Item-Focused Trees (Tutz & Berger, 2016) 作为 categorical cohort
695	    DIF 的 替代方案，将 model release date 作为 continuous covariate。
696	
697	    '
698	  expected_results:
699	    n_items_analyzed: 12508
700	    ift_flagged_items: 4150
701	    ift_flag_rate: 0.332
702	    ift_dif_mh_jaccard: 0.72
703	    ift_dif_mh_concordance: 0.85
704	    ift_unique_flags: 890
705	    mh_unique_flags: 658
706	    ift_split_point_median_date: 2023-09
707	    ift_nonlinear_items: 1230
708	    ift_nonlinear_pct: 0.098
709	    computation_time_hours: 12
710	  result_rationale: 'Median 档下 IFT 的 flag rate（33.2%）略高于 MH（31.3%），因为 continuous covariate
711	    模型捕捉了 MH 的 binary split 遗漏的 nonlinear trends（9.8% items 显示 non-monotonic DIF pattern）。Jaccard=0.72
712	    的 moderate overlap 表明两种方法 largely agree 但 IFT 的 continuous modeling 额外捕捉了 gradual
713	    drift items。IFT split point median 在 2023-09 附近，接近 MH 使用的 temporal cutoff，增加了
714	    MH cohort definition 的 合理性。Median 档下 IFT 的价值是 robustness check 而非 primary method——
715	    "MH results are robust to categorical vs continuous covariate modeling"。
716	
717	    '
718	  tables:
719	  - name: 'Table: IFT vs MH-DIF Comparison'
720	    columns:
721	    - metric
722	    - MH_DIF
723	    - IFT
724	    - overlap
725	    rows:
726	    - - flag_rate
727	      - 31.3%
728	      - 33.2%
729	      - Jaccard=0.72
730	    - - n_flagged
731	      - 3918
732	      - 4150
733	      - concordance=0.85
734	    - - nonlinear_items
735	      - N/A
736	      - 1230
737	      - 9.8% of total
738	    - - computation_time
739	      - 2h
740	      - 12h
741	      - —
742	  figures_description:
743	  - 'Fig: IFT tree visualization for 3 example items — showing split points and DIF
744	    magnitude per branch'
745	  analysis: 'IFT 确认 MH 结果的 robustness 并提供了 continuous DIF trend 的 additional insight。
746	    9.8% nonlinear items 是 interesting finding 但不影响 main claims。降级为 appendix robustness
747	    check——"results hold whether we use categorical (MH) or continuous (IFT) covariate
748	    modeling"。
749	
750	    '
751	- name: architecture_stratified_dif
752	  plan_id: plan_010
753	  description: '在 architecture-homogeneous subpopulation (decoder-only only) 上运行 DIF，
754	    测试 IRT model fit 是否改善、spurious DIF 是否减少。
755	
756	    '
757	  expected_results:
758	    n_decoder_only: 5226
759	    n_non_decoder: 1
760	    decoder_only_pct: 99.98
761	    dif_c_pct_decoder_only: 31.3
762	    dif_c_pct_full: 31.3
763	    jaccard_decoder_vs_full: 1.0
764	    irt_rmsea_decoder: 0.042
765	    irt_rmsea_full: 0.042
766	    irt_cfi_decoder: 0.78
767	    irt_cfi_full: 0.78
768	    pct_models_lz_gt2_decoder: 97.8
769	    pct_models_lz_gt2_full: 98.0
770	    conclusion: architecture heterogeneity is a non-issue
771	  result_rationale: 'Median 档下这是最 clear-cut 的实验：METABENCH MMLU 中 99.98% (5226/5227)
772	    模型是 decoder-only，排除 1 个 non-decoder 模型完全不改变任何结果（Jaccard=1.0）。 IRT fit 同样不变，因为
773	    misfit (|Lz|>2 for 98%) 源于 MMLU 的 inherent multidimensionality（57 subjects → 多维
774	    ability），而非 architecture heterogeneity。 这是 proactive defense 实验：reviewer 无法质疑
775	    "architecture confound inflates DIF" 因为 population 几乎完全 homogeneous。Zero GPU cost,
776	    纯 data subsetting。
777	
778	    '
779	  tables:
780	  - name: 'Table: Architecture Stratification Results'
781	    columns:
782	    - population
783	    - n_models
784	    - c_pct
785	    - irt_rmsea
786	    - pct_lz_gt2
787	    rows:
788	    - - Full
789	      - 5227
790	      - 31.3
791	      - 0.042
792	      - 98.0
793	    - - Decoder-only
794	      - 5226
795	      - 31.3
796	      - 0.042
797	      - 97.8
798	    - - Delta
799	      - -1
800	      - 0.0
801	      - 0.0
802	      - -0.2
803	  figures_description:
804	  - 'Fig: Architecture composition pie chart — 99.98% decoder-only (appendix only)'
805	  analysis: 'Architecture stratification 是 one-line result: "METABENCH MMLU is 99.98%
806	    decoder-only; excluding the single non-decoder model changes nothing (Jaccard=1.0)."
807	    Main body 一句话 + footnote，不需要 dedicated section。
808	
809	    '
810	- name: semi_synthetic_contamination_validation
811	  plan_id: plan_011
812	  description: '向 METABENCH response matrix 注入已知 contamination，测量 DIF 在 controlled
813	    ground truth 下的 detection power，解决 ground truth circularity concern。
814	
815	    '
816	  expected_results:
817	    n_clean_items_selected: 500
818	    n_injection_items: 150
819	    temporal_external_tpr_p0: 0.33
820	    temporal_external_tpr_p03: 0.52
821	    temporal_external_tpr_p05: 0.74
822	    temporal_external_tpr_p07: 0.93
823	    temporal_external_tpr_p10: 1.0
824	    temporal_external_fpr: 0.318
825	    temporal_external_delta_tpr_p05: 0.41
826	    temporal_external_delta_tpr_p10: 0.67
827	    ability_external_tpr_p10: 0.77
828	    ability_external_fpr: 0.49
829	    standard_mh_fpr_inflation_at_p10: 0.30→0.59
830	    matching_variable_contamination: true
831	    dose_response_monotonic: true
832	  result_rationale: 'Median 档下 ΔTPR(p=0.5)=0.41 落在 key indicator range [0.35, 0.50]
833	    内。 这比 registry 实际值 (ΔTPR(p=0.5)=0.508) 低约 0.1，因为 median 档假设 temporal label 携带的弱结构性（permutation
834	    null 2–8%）吃掉了一部分 detection headroom。FPR=0.318 反映 temporal cohort 的 baseline instability（即使
835	    clean items 中有 ~31.8% 被 flag，因为 "clean" is defined by Li et al. labels which don''t
836	    capture differential effects）。Dose-response 从 p=0.3 到 p=1.0 单调增长确认了 injection
837	    validity。Standard MH 的 FPR inflation（0.30→0.59 at p=1.0）确认了 matching variable
838	    contamination——within-group matching variable 被 injection 污染导致 FPR 膨胀，这是 cross-subject
839	    matching 的动机。
840	
841	    '
842	  tables:
843	  - name: 'Table: Semi-Synthetic Detection Power (Temporal, External Matching)'
844	    columns:
845	    - exploitation_rate_p
846	    - tpr
847	    - fpr
848	    - delta_tpr
849	    rows:
850	    - - 0.0 (baseline)
851	      - 0.33
852	      - 0.318
853	      - 0.0
854	    - - 0.3
855	      - 0.52
856	      - 0.32
857	      - 0.19
858	    - - 0.5
859	      - 0.74
860	      - 0.318
861	      - 0.41
862	    - - 0.7
863	      - 0.93
864	      - 0.317
865	      - 0.61
866	    - - 1.0
867	      - 1.0
868	      - 0.316
869	      - 0.67
870	  - name: 'Table: Matching Variable Contamination Effect'
871	    columns:
872	    - matching_method
873	    - fpr_p0
874	    - fpr_p10
875	    - delta_fpr
876	    rows:
877	    - - Standard (within-group)
878	      - 0.298
879	      - 0.59
880	      - 0.292
881	    - - External (cross-benchmark)
882	      - 0.318
883	      - 0.316
884	      - -0.002
885	  figures_description:
886	  - 'Fig: Dose-response curve — TPR vs exploitation rate p, with 95% CI bands'
887	  - 'Fig: FPR comparison — standard vs external matching as injection increases'
888	  analysis: 'ΔTPR(p=0.5)=0.41 是 median 档的核心指标，表明 DIF 在 moderate exploitation rate
889	    下有 meaningful detection power but not overwhelming。Reviewer 会追问 "p=0.5 是否 realistic?"——需要在
890	    paper 中 argue contamination exploitation rates 在文献 中缺乏 empirical estimates，p=0.5
891	    是 conservative middle ground。External matching 的 ΔFPR≈0 是 methodological highlight，直接支撑
892	    cross-subject matching recommendation。
893	
894	    '
895	- name: multi_benchmark_temporal_dif
896	  plan_id: plan_028
897	  description: '在 METABENCH 中的 ARC, HellaSwag, WinoGrande, TruthfulQA 上运行 temporal
898	    DIF， 验证 cross-benchmark 泛化性。
899	
900	    '
901	  expected_results:
902	    mmlu_c_pct: 31.3
903	    mmlu_random_c_pct: 0.18
904	    winogrande_c_pct: 28.8
905	    winogrande_random_c_pct: 0.35
906	    truthfulqa_c_pct: 27.4
907	    truthfulqa_random_c_pct: 0.4
908	    arc_c_pct: 24.5
909	    arc_random_c_pct: 0.55
910	    gsm8k_c_pct: 18.9
911	    gsm8k_random_c_pct: 0.3
912	    hellaswag_c_pct: 17.2
913	    hellaswag_random_c_pct: 0.3
914	    cross_benchmark_range: 17.2–31.3%
915	    all_random_below_1pct: true
916	    min_enrichment_ratio: 31
917	    n_benchmarks: 6
918	  result_rationale: 'Median 档下 cross-benchmark C% range 为 17.2–31.3%，落在 key indicator
919	    range [15.0, 32.0] 内。排序 MMLU > WinoGrande > TruthfulQA > ARC > GSM8K > HellaSwag
920	    反映了各 benchmark 的 structural properties：MMLU（57 subjects, 12K items）和 WinoGrande（commonsense
921	    reasoning, 高 memorization vulnerability）C% 最高； HellaSwag（sentence completion,
922	    10K items 但 item homogeneity 高）和 GSM8K （math, single domain）C% 最低。所有 random-split
923	    controls <1% 确认 temporal signal 在每个 benchmark 上都是 genuine。Median 档下 HellaSwag
924	    和 GSM8K 的较低 C% 会被 reviewer 追问——需要解释 domain homogeneity 降低 DIF variance。
925	
926	    '
927	  tables:
928	  - name: 'Table: Cross-Benchmark Temporal DIF Summary'
929	    columns:
930	    - benchmark
931	    - n_items
932	    - n_ref
933	    - n_foc
934	    - c_pct
935	    - random_c_pct
936	    - enrichment_ratio
937	    rows:
938	    - - MMLU
939	      - 12508
940	      - 1080
941	      - 807
942	      - 31.3
943	      - 0.18
944	      - 174
945	    - - WinoGrande
946	      - 1267
947	      - 1017
948	      - 803
949	      - 28.8
950	      - 0.35
951	      - 82
952	    - - TruthfulQA
953	      - 817
954	      - 1080
955	      - 807
956	      - 27.4
957	      - 0.4
958	      - 69
959	    - - ARC-Challenge
960	      - 1172
961	      - 1080
962	      - 807
963	      - 24.5
964	      - 0.55
965	      - 45
966	    - - GSM8K
967	      - 1319
968	      - 1017
969	      - 804
970	      - 18.9
971	      - 0.3
972	      - 63
973	    - - HellaSwag
974	      - 10042
975	      - 1080
976	      - 807
977	      - 17.2
978	      - 0.3
979	      - 57
980	  figures_description:
981	  - 'Fig: Bar chart — C% across 6 benchmarks with random-split control overlay'
982	  analysis: '6 个 benchmark 的一致 temporal DIF pattern (17–31%, all >>random) 是 median
983	    档下 最强的 generalizability evidence。但 Claim 3 的 cross-benchmark 证据被降级至 appendix（8
984	    页限制），main body 仅保留 MMLU 结果 + 一句 "consistent across 5 additional benchmarks (see
985	    Appendix X)"。
986	
987	    '
988	- name: permutation_null_c_rate
989	  plan_id: plan_029
990	  description: '1000× permutation test：随机重新分配 2023/2024 temporal labels（保持 N_ref=1080,
991	    N_foc=807），每次运行 MH-DIF，建立 C% 的 null distribution。
992	
993	    '
994	  expected_results:
995	    n_permutations: 1000
996	    null_c_pct_mean: 4.8
997	    null_c_pct_median: 4.6
998	    null_c_pct_sd: 1.2
999	    null_c_pct_95ci:
1000	    - 2.7
1001	    - 7.3
1002	    null_c_pct_99ci:
1003	    - 1.9
1004	    - 8.4
1005	    null_c_pct_max: 9.1
1006	    observed_c_pct: 31.3
1007	    z_score_vs_null: 22.1
1008	    p_value: <1e-50
1009	    ratio_observed_to_null_mean: 6.5
1010	    random_split_c_pct: 0.18
1011	    null_vs_random_split_ratio: 26.7
1012	  result_rationale: 'Median 档下 permutation null C% mean=4.8% 落在 key indicator range
1013	    [2.0, 8.0]。 Permutation null 显著高于 random-split control（4.8% vs 0.18%），因为 temporal
1014	    labels 与 ability 不完全正交：2024 模型平均 stronger（d=-0.17），permutation 打断了 true temporal
1015	    signal 但保留了 ability distribution 的 marginal structure。 Random-split 在 within-cohort
1016	    内操作所以 ability 完全 balanced，产生 near-zero C%。Permutation null 的 4.8% 表明 ~5% 的 "DIF"
1017	    可归因于 temporal label 本身 携带的 ability confound structure，但 31.3% 仍为 null 的 6.5× (z=22.1)。
1018	    Median 档下 reviewer 会追问 "4.8% null 是否意味着 temporal cohort design 有 systematic bias?"——需要在
1019	    paper 中解释这是 expected property of any non-randomized group comparison in observational
1020	    studies，并引用 plan_027 的 matched-ability analysis (C%=28.9%) 作为 complementary evidence。
1021	
1022	    '
1023	  tables:
1024	  - name: 'Table: Permutation Null Distribution'
1025	    columns:
1026	    - statistic
1027	    - value
1028	    rows:
1029	    - - Null mean C%
1030	      - 4.8
1031	    - - Null median C%
1032	      - 4.6
1033	    - - Null SD
1034	      - 1.2
1035	    - - Null 95% CI
1036	      - '[2.7, 7.3]'
1037	    - - Null max
1038	      - 9.1
1039	    - - Observed C%
1040	      - 31.3
1041	    - - z-score
1042	      - 22.1
1043	    - - Observed / Null mean
1044	      - 6.5×
1045	  - name: 'Table: Three Baselines Comparison'
1046	    columns:
1047	    - baseline
1048	    - c_pct
1049	    - interpretation
1050	    rows:
1051	    - - Random split (within-cohort)
1052	      - 0.18
1053	      - statistical noise floor
1054	    - - Permutation null (label shuffle)
1055	      - 4.8
1056	      - temporal label structure
1057	    - - Observed temporal DIF
1058	      - 31.3
1059	      - genuine + structural
1060	    - - Matched-ability (plan_027)
1061	      - 28.9
1062	      - genuine after ability control
1063	  figures_description:
1064	  - 'Fig: Histogram of 1000 permutation null C% values with observed 31.3% marked
1065	    as vertical line'
1066	  - 'Fig: Three-baseline comparison bar chart — random (0.18%), permutation (4.8%),
1067	    observed (31.3%)'
1068	  analysis: 'Permutation null 是 median 档下 Claim 1 的关键 calibration baseline。31.3% vs
1069	    4.8% null 给出 "genuine DIF ≈ 26.5%" 的 conservative estimate，与 plan_027 的 matched-ability
1070	    C%=28.9% convergent。Paper 应报告为 "~25–29% depending on confound controls"（取 plan_027
1071	    matched 28.9% 与 observed-null=26.5% 的 range）。 Permutation null 显式报告为 calibration
1072	    baseline 是对 reviewer "is 31% above chance?" 的 definitive answer。
1073	
1074	    '
1075	- name: odds_ratio_regression_transparency
1076	  plan_id: plan_030
1077	  description: '补充 pseudo R²=0.0007 的 odds ratio + 95% CI + McFadden/Nagelkerke R²
1078	    + deviance ratio，并构建更精细的 item-level model。
1079	
1080	    '
1081	  expected_results:
1082	    model1_domain_delta:
1083	      mcfadden_r2: 0.0007
1084	      nagelkerke_r2: 0.0013
1085	      subject_acc_delta_or_per_010: 1.58
1086	      subject_acc_delta_ci_per_010:
1087	      - 1.21
1088	      - 2.06
1089	      deviance_ratio: 0.0007
1090	    model2_domain_delta_plus_items:
1091	      mcfadden_r2: 0.044
1092	      nagelkerke_r2: 0.074
1093	      subject_acc_delta_or_per_010: 0.71
1094	      ctt_difficulty_or_per_010: 0.76
1095	      ctt_discrimination_or_per_010: 1.54
1096	    model3_item_delta:
1097	      mcfadden_r2: 0.0013
1098	      nagelkerke_r2: 0.0022
1099	      item_acc_change_or_per_010: 1.09
1100	      item_acc_change_ci:
1101	      - 1.53
1102	      - 2.99
1103	    model4_item_delta_plus_items:
1104	      mcfadden_r2: 0.045
1105	      nagelkerke_r2: 0.076
1106	      item_acc_change_or_per_010: 0.91
1107	      ctt_difficulty_or_per_010: 0.75
1108	      ctt_discrimination_or_per_010: 1.56
1109	    simpsons_paradox: true
1110	    lr_test_m1_vs_m2_chi2: 640.5
1111	    lr_test_m3_vs_m4_chi2: 648.2
1112	    best_model_mcfadden: 0.045
1113	    ability_confound_explained_pp: 4.2
1114	  result_rationale: 'Median 档下 Simpson''s paradox (Model 2 vs Model 1) 是核心 methodological
1115	    finding： domain accuracy Δ 的 OR 从 1.58 (Model 1, positive) 翻转为 0.71 (Model 2,
1116	    negative) after controlling for item properties。这是因为 high-discrimination items
1117	    (OR=1.54) 同时是 DIF-prone items AND high-accuracy-change items，产生 confound。McFadden
1118	    R² 即使在 best model (0.045) 下也极低，说明 DIF 的 item-level variance 绝大部分无法由 observed item
1119	    properties 解释。Median 档下 ability confound explained pp=4.2，落在 [3.0, 6.0] 范围内——高于
1120	    plan_027 的 2.4pp 因为 regression 捕捉了额外的 item-level confounding pathway。 Reviewer
1121	    会追问 Simpson''s paradox 的因果解释——需谨慎表述为 "item difficulty may be a mediator rather
1122	    than confounder; Model 1 (marginal) and Model 2 (conditional) answer different
1123	    causal questions"。
1124	
1125	    '
1126	  tables:
1127	  - name: 'Table: Logistic Regression Model Comparison'
1128	    columns:
1129	    - model
1130	    - predictors
1131	    - mcfadden_r2
1132	    - nagelkerke_r2
1133	    - aic
1134	    rows:
1135	    - - Model 1
1136	      - subject acc Δ
1137	      - 0.0007
1138	      - 0.0013
1139	      - 15548
1140	    - - Model 2
1141	      - subject acc Δ + CTT props
1142	      - 0.044
1143	      - 0.074
1144	      - 14910
1145	    - - Model 3
1146	      - item acc Δ
1147	      - 0.0013
1148	      - 0.0022
1149	      - 15539
1150	    - - Model 4
1151	      - item acc Δ + CTT props
1152	      - 0.045
1153	      - 0.076
1154	      - 14892
1155	  - name: 'Table: Simpson''s Paradox in Accuracy Δ Effect'
1156	    columns:
1157	    - model
1158	    - acc_delta_or
1159	    - direction
1160	    - interpretation
1161	    rows:
1162	    - - Model 1 (marginal)
1163	      - 1.58
1164	      - positive
1165	      - higher acc Δ → more DIF
1166	    - - Model 2 (conditional)
1167	      - 0.71
1168	      - negative
1169	      - higher acc Δ → LESS DIF after controlling item props
1170	  figures_description:
1171	  - 'Fig: Simpson''s paradox visualization — marginal vs conditional effect of accuracy
1172	    Δ on DIF probability'
1173	  analysis: Simpson's paradox 需要在 paper 中小心处理。Model 1 的 marginal positive effect 支持
1174	    "capability gain causes DIF" 的 naive interpretation，但 Model 2 的 conditional negative
1175	    effect 表明 item properties (especially discrimination) 是 confound。 Median 档下建议
1176	    Model 1 as primary (conservative, 不做因果 claim)，Model 2 as supplementary (illustrating
1177	    confound structure)。总 explained variance <5% (McFadden R²=0.045) 意味着 95%+ 的 DIF
1178	    variance 是 item-specific 且无法归因于 observed covariates——这实际上强化了 "DIF captures genuine
1179	    item-level differential functioning, not a proxy for aggregate trends" 的 narrative。
1180	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1aaeaba9-4e3e-43f2-a359-9efff8d2f7fb",
  "isSidechain": false,
  "promptId": "574ea9fb-2433-4f53-83c6-6ff0f801abc3",
  "type": "user",
  "uuid": "3162777d-9bba-43f7-a8b5-43922fb7c86d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/median/review_context.yaml",
      "content": "narrative_guidance: 'Median 档下 permutation null C% 落在 2–8%，表明 temporal label 本身携带弱结构性信号\n  （model release date 与 ability 不完全正交），但 31% 仍为 null 的 4–15×，统计意义明确。 Claim 1 headline\n  须从 ''31%'' 调整为 ''~25–29% after confound controls''，permutation null 显式报告为 calibration\n  baseline。Claim 2 meta-critique 软化为 ''complementary approaches needed''， 不再用 ''fundamentally\n  mismatched''。Claim 3 cross-benchmark 证据降级 appendix，主体仅保留 MMLU。 Claim 4 diagnostic\n  lens 升格为 abstract 第二句，强调 audit protocol 实用价值以对冲 ''applying textbook psychometrics''\n  的 novelty 质疑。Rebuttal 准备 ''psychometric tools are mature but their application to\n  LLM benchmarks at this scale is novel'' 防线。 Simpson''s paradox（plan_030 Model 2\n  vs Model 1）需谨慎处理因果表述，仅作为 supplementary evidence。 预期 reviewer score 2.5–3.5，borderline\n  accept/weak reject，需要 rebuttal 翻盘。\n\n  '\nimagined_experiments:\n- name: real_data_dif_mmlu\n  plan_id: plan_001\n  description: '对 METABENCH MMLU 响应矩阵 (5219×12508) 执行全面 MH-DIF 分析， 包含 temporal/ability\n    cohort、within-family confound control、domain specificity。\n\n    '\n  expected_results:\n    temporal_ets_c_pct: 31.3\n    temporal_fpr_li_clean: 0.322\n    temporal_enrichment: 0.964\n    ability_ets_c_pct: 3.1\n    ability_fpr_li_clean: 0.029\n    ability_enrichment: 1.15\n    within_family_llama2v3_c_pct: 58.7\n    within_family_mistral_mixtral_c_pct: 36.2\n    domain_spearman_rho: 0.32\n    domain_spearman_p: 0.016\n    sanity_random_split_c_pct: 0.21\n    temporal_ability_jaccard: 0.016\n    n_subjects_with_c_gt20pct: 57\n    unweighted_subject_mean_c_pct: 30.4\n    subject_c_range: 20.1–47.8%\n    decoder_only_pct: 99.98\n  result_rationale: 'Median 档下 temporal C%=31.3% 与已有 registry 一致（这是实测值，不受 tier 影响）。\n    关键区别在于后续 controls 将把 residual 压至 25–29%。Within-family Llama-2v3 C% 略低于 registry\n    的 61.3%（~58.7%），因为 median 档假设 ability confound 解释更多 variance （d=-0.99 对中 ability\n    gap 较大）。Domain ρ=0.32 表明 subject-level accuracy improvement 与 DIF 存在弱正相关，但 item-level\n    decomposition 将显示域改善仅解释 ≤3.5pp。Random-split sanity check 0.21% 确认 temporal signal\n    非统计噪声。 Enrichment≈0.96 确认 DIF 与 web-overlap labels 正交——这是预期行为，非方法失败。\n\n    '\n  tables:\n  - name: 'Table 1: Temporal DIF Summary by Cohort Definition'\n    columns:\n    - cohort\n    - n_ref\n    - n_foc\n    - n_items\n    - c_pct\n    - fpr_li_clean\n    - enrichment\n    rows:\n    - - temporal_2023v2024\n      - 1080\n      - 807\n      - 12508\n      - 31.3\n      - 0.322\n      - 0.964\n    - - ability_quintile\n      - 2610\n      - 2609\n      - 12508\n      - 3.1\n      - 0.029\n      - 1.15\n    - - random_split_sanity\n      - 950\n      - 950\n      - 12508\n      - 0.21\n      - 0.002\n      - 1.01\n  - name: 'Table 2: Within-Family Confound Control'\n    columns:\n    - family_pair\n    - n_ref\n    - n_foc\n    - c_pct\n    - overlap_with_temporal\n    rows:\n    - - Llama-2 vs Llama-3\n      - 161\n      - 308\n      - 58.7\n      - Jaccard=0.38\n    - - Mistral vs Mixtral\n      - 89\n      - 112\n      - 36.2\n      - Jaccard=0.29\n  figures_description:\n  - 'Fig 1: 57-subject heatmap showing per-subject C% (rows) × cohort (cols), 色阶 20–48%'\n  - 'Fig 2: Scatter plot of subject-level accuracy Δ vs C%, ρ=0.32, p=0.016'\n  analysis: '31.3% temporal instability 是 robust finding。Ability cohort 的 3.1% 确认\n    DIF signal 与 temporal split 强关联而非 ability artifact。Within-family 的高 C% （Llama-2v3:\n    58.7%）混淆了 capability gain 和 contamination——这不是理想的 confound control 因为 family 内\n    ability gap 过大（d≈-0.99）。Domain ρ=0.32 是 ecological correlation，item-level decomposition\n    将在 plan_019/030 中展开。\n\n    '\n- name: rl_robustness_validation\n  plan_id: plan_002\n  description: '验证 DIF 对 RL-trained models 的鲁棒性：alignment-RL (DPO/ORPO) cohort 从 METABENCH\n    提取，reasoning-RL (GRPO/PPO) 10–15 个模型需额外推理。\n\n    '\n  expected_results:\n    n_alignment_rl_models: 477\n    n_reasoning_rl_models: 13\n    dif_c_pct_baseline_sft_only: 30.8\n    dif_c_pct_with_alignment_rl: 31.1\n    dif_c_pct_with_reasoning_rl: 30.5\n    jaccard_sft_vs_alignment: 0.91\n    jaccard_sft_vs_reasoning: 0.84\n    constat_auroc_non_rl: 0.72\n    constat_auroc_reasoning_rl: 0.58\n    mink_auroc_non_rl: 0.68\n    mink_auroc_reasoning_rl: 0.51\n    delong_dif_vs_constat_p: 0.34\n    tost_equivalence_dif_retention: 90% CI [0.88, 0.97], equivalence bound ±0.10\n    tost_conclusion: equivalent\n    power_analysis_detection_boundary_p: 0.45\n    bootstrap_ci_auroc_dif:\n    - 0.76\n    - 0.89\n  result_rationale: 'Median 档下 DIF 作为 group-level method 对 cohort composition 变化不敏感——添加\n    13 个 reasoning-RL 模型到 N=807 focal cohort 几乎不改变 group statistics。 Jaccard=0.84（vs\n    reasoning-RL）略低于 alignment-RL 的 0.91，因为 reasoning-RL 模型在部分 hard items 上的 response\n    pattern 与 SFT 模型有系统性差异（GRPO 训练 改变了 reasoning chain 而非单纯记忆）。传统 per-model detectors\n    在 reasoning-RL 上退化显著（ConStat 从 0.72→0.58, Min-K% 从 0.68→0.51），因为 RL 训练平滑了 NLL\n    distribution。但 N=13 使得所有 pairwise comparison 的 CI 极宽，DeLong test 无显著差异（p=0.34），TOST\n    equivalence 勉强成立。这是 median 档的典型情况： 方向正确但统计力不足以支撑强 claim。\n\n    '\n  tables:\n  - name: 'Table: DIF Stability Across Cohort Compositions'\n    columns:\n    - cohort_composition\n    - n_focal\n    - c_pct\n    - jaccard_vs_baseline\n    rows:\n    - - SFT-only baseline\n      - 620\n      - 30.8\n      - 1.0\n    - - + alignment-RL (DPO/ORPO)\n      - 807\n      - 31.1\n      - 0.91\n    - - + reasoning-RL (GRPO/PPO)\n      - 820\n      - 30.5\n      - 0.84\n  - name: 'Table: Per-Model Detector AUROC Comparison'\n    columns:\n    - detector\n    - non_rl\n    - alignment_rl\n    - reasoning_rl\n    rows:\n    - - DIF (group)\n      - N/A\n      - N/A\n      - N/A\n    - - ConStat\n      - 0.72\n      - 0.67\n      - 0.58\n    - - Min-K%\n      - 0.68\n      - 0.64\n      - 0.51\n  figures_description:\n  - 'Fig: Detection power curve — DIF ΔTPR vs exploitation rate p ∈ [0.4, 1.0], 标注\n    detection boundary p≈0.45'\n  analysis: 'DIF 的 group-level 设计使其对 cohort composition 天然鲁棒——13 个 RL 模型在 N=807 中占比\n    <2%，统计影响可忽略。真正的 claim 应限定为 \"DIF 在 cohort 中 RL 占比 <5% 时 robust\"，而非 \"DIF 对 RL 鲁棒\"。Per-model\n    detector 退化方向正确但 N=13 使结论 仅为 suggestive。降级为 limitations 中 disclosure，不作为 numbered\n    contribution。\n\n    '\n- name: constat_perturbation_eval\n  plan_id: plan_003a\n  description: '独立评估 ConStat-style perturbation testing：LLM 生成 200+ MMLU items 的语义等价\n    reformulation，比较原始与改写版本的 model performance。\n\n    '\n  expected_results:\n    n_items_reformulated: 220\n    reformulation_semantic_sim: 0.92\n    constat_fdr_controlled_flags: 47\n    constat_flag_rate: 0.214\n    constat_overlap_with_dif_c: Jaccard=0.18\n    constat_tpr_non_rl_known_contam: 0.61\n    constat_tpr_rl_known_contam: 0.29\n    constat_fpr: 0.08\n    effect_size_non_rl: 0.74\n    effect_size_rl: 0.31\n    gpu_hours_used: 65\n  result_rationale: 'Median 档下 ConStat 在 non-RL 模型上表现尚可（TPR=0.61, effect size=0.74），因为\n    verbatim memorization 使模型对 surface-form 变化敏感。但 RL-trained 模型（尤其 GRPO/PPO）通过 reasoning\n    generalization 降低了对 exact wording 的依赖，TPR 降至 0.29。与 DIF 的低重叠（Jaccard=0.18）符合预期：ConStat\n    检测 per-model surface-level memorization，DIF 检测 group-level differential functioning，二者捕捉不同信号。\n    FDR-controlled flag rate 21.4% 低于 DIF 的 31.3%，因为 ConStat 需要更强的 per-item evidence。GPU\n    成本 65h 主要用于 reformulation generation 和 inference。\n\n    '\n  tables:\n  - name: 'Table: ConStat Detection Power by Model Type'\n    columns:\n    - model_type\n    - n_models\n    - tpr\n    - fpr\n    - effect_size\n    rows:\n    - - SFT-only\n      - 15\n      - 0.61\n      - 0.08\n      - 0.74\n    - - Alignment-RL\n      - 10\n      - 0.48\n      - 0.07\n      - 0.55\n    - - Reasoning-RL\n      - 8\n      - 0.29\n      - 0.09\n      - 0.31\n  figures_description:\n  - 'Fig: ConStat flag rate vs DIF C% per subject — weak positive correlation'\n  analysis: 'ConStat 作为 standalone baseline 有价值但不足以支撑 paper claim。与 DIF 的互补性 是 ensemble\n    fusion（plan_003c）的理论基础，但 median 档下 RL 模型上的退化使得 ensemble 增益有限。结果降级为 appendix baseline\n    comparison。\n\n    '\n- name: dvd_generation_variance_eval\n  plan_id: plan_003b\n  description: '独立评估 DVD generation variance：10–15 个 open-weight 模型在每个 item 上生成 50\n    次 response，计算 generation variance 并检测 bimodal distribution。\n\n    '\n  expected_results:\n    n_models_tested: 12\n    n_items_scored: 12508\n    responses_per_item: 50\n    dvd_bimodal_flag_rate: 0.089\n    dvd_tpr_verbatim_contam: 0.43\n    dvd_tpr_variant_contam: 0.52\n    dvd_fpr: 0.062\n    dvd_overlap_with_dif_c: Jaccard=0.11\n    gpu_hours_used: 58\n    temperature_sensitivity: 'T=0.7: flag_rate=0.089; T=1.0: flag_rate=0.142'\n  result_rationale: 'Median 档下 DVD 的 bimodal detection 在 variant contamination 上略优于\n    verbatim （TPR 0.52 vs 0.43），因为 variant contamination 产生更明显的 generation variance\n    bimodality（模型在 \"近似记忆\" 和 \"真正推理\" 之间切换）。但整体 flag rate 仅 8.9%， 远低于 DIF 的 31.3%，因为\n    DVD 需要 per-model inference 且仅在 generation distribution 层面操作。与 DIF 的极低重叠（Jaccard=0.11）表明二者检测完全不同维度。\n    Temperature 敏感性（T=1.0 时 flag rate 翻倍至 14.2%）暴露了 hyperparameter tuning 问题。GPU 成本\n    58h 用于 12 模型 × 12508 items × 50 responses 的推理。\n\n    '\n  tables:\n  - name: 'Table: DVD Detection by Contamination Type'\n    columns:\n    - contam_type\n    - tpr\n    - fpr\n    - bimodal_strength\n    rows:\n    - - verbatim\n      - 0.43\n      - 0.062\n      - Cohen's h=0.38\n    - - variant\n      - 0.52\n      - 0.058\n      - Cohen's h=0.47\n    - - clean\n      - N/A\n      - 0.062\n      - Cohen's h=0.04\n  figures_description:\n  - 'Fig: Generation variance distribution — bimodal (contaminated) vs unimodal (clean)\n    items'\n  analysis: 'DVD 捕捉的是 per-model generation-level signal，与 DIF 的 group-level item functioning\n    signal 几乎不重叠。作为独立检测器价值有限（TPR<0.55），但为 ensemble 提供了独特的 variant contamination 覆盖。Temperature\n    敏感性需要在 paper 中 disclose。\n\n    '\n- name: ensemble_fusion\n  plan_id: plan_003c\n  description: '将 DIF + ConStat + DVD 融合为 multi-signal ensemble，评估 majority voting\n    和 weighted fusion 策略。\n\n    '\n  expected_results:\n    ensemble_2of3_tpr: 0.54\n    ensemble_2of3_fpr: 0.045\n    ensemble_weighted_tpr: 0.59\n    ensemble_weighted_fpr: 0.052\n    ensemble_coverage_dif_only: δ≥1.4\n    ensemble_coverage_constat_only: non-RL δ≥0.6\n    ensemble_coverage_dvd_only: variant contamination\n    cross_val_weight_stability: 'DIF: 0.52±0.08, ConStat: 0.31±0.06, DVD: 0.17±0.05'\n    uniform_vs_optimized_tpr_delta: 0.03\n    fpr_all_configs_below_010: true\n  result_rationale: 'Median 档下 ensemble 增益有限，因为三个信号的重叠极低（pairwise Jaccard 0.11–0.18），\n    majority voting 在 low-overlap 情况下倾向于保守（TPR=0.54）。Weighted fusion 略优（TPR=0.59）但\n    cross-validation weight stability 显示 DIF 权重主导（0.52）， ConStat 和 DVD 的贡献边际化。关键问题：DIF\n    是 group-level，ConStat/DVD 是 per-model-level，fusion 的语义不一致使 ensemble 设计缺乏理论基础。Median\n    档下 reviewers 会质疑 \"为什么要 fuse fundamentally different signal types\"。 结论：ensemble\n    负面结果，not executed in final paper，降级为 future work。\n\n    '\n  tables:\n  - name: 'Table: Ensemble Fusion Comparison'\n    columns:\n    - strategy\n    - tpr\n    - fpr\n    - coverage_description\n    rows:\n    - - DIF only\n      - 0.508\n      - 0.314\n      - group-level, δ≥1.4\n    - - 2-of-3 majority\n      - 0.54\n      - 0.045\n      - intersection of signals\n    - - weighted fusion\n      - 0.59\n      - 0.052\n      - combined coverage\n    - - uniform weight\n      - 0.56\n      - 0.048\n      - unweighted average\n  figures_description:\n  - 'Fig: Venn diagram of flag overlap — DIF ∩ ConStat ∩ DVD showing minimal 3-way\n    overlap'\n  analysis: 'Ensemble 的 FPR 显著改善（0.045 vs DIF 单独的 0.314），但代价是 TPR 仅从 DIF ΔTPR 基线略有提升。信号类型不同质（group\n    vs per-model）使 fusion 缺乏 principled justification。Median 档下这是 negative result——not\n    executed, dropped to future work。\n\n    '\n- name: cross_benchmark_gsm8k\n  plan_id: plan_004\n  description: '在 GSM8K 上复制 DIF 分析，使用 GSM1K 作为 contamination ground truth， 验证 cross-benchmark\n    泛化性。\n\n    '\n  expected_results:\n    gsm8k_n_items: 1319\n    gsm8k_n_ref: 1017\n    gsm8k_n_foc: 804\n    gsm8k_standard_c_pct: 18.9\n    gsm8k_external_c_pct: 45.1\n    gsm8k_sanity_c_pct: 0.35\n    semi_synthetic_delta_tpr_p10: 0.78\n    semi_synthetic_delta_tpr_p05: 0.44\n    semi_synthetic_external_delta_tpr_p10: 0.49\n    gsm1k_n_models: 33\n    gsm1k_pearson_r: -0.478\n    gsm1k_pearson_p: 0.005\n    gsm1k_spearman_rho: -0.39\n    gsm1k_spearman_p: 0.025\n    gsm1k_partial_r: -0.37\n    gsm1k_partial_p: 0.035\n    gsm1k_ci_upper_abs_r: 0.155\n    direction: NEGATIVE — opposite to contamination hypothesis\n    cook_d_max_model: Deepseek-math-7b-rl\n    leave_one_out_r_range:\n    - -0.52\n    - -0.36\n  result_rationale: 'Median 档下 GSM8K temporal C%=18.9% 低于 MMLU 的 31.3%，因为 GSM8K 是\n    single-domain math benchmark（1319 items），domain homogeneity 降低了 DIF 的 item-level\n    variance。 Semi-synthetic ΔTPR 在 p=0.5 时为 0.44，落在 median 档范围 [0.35, 0.5] 内。 GSM1K\n    negative correlation（r=-0.478）是 median 档核心尴尬点：DIF-C items anti-correlate with\n    contamination gap，需要额外解释 \"DIF ≠ contamination detector, DIF detects differential\n    item functioning which may reflect capability gain on hard items rather than memorization\"。N=33\n    使 CI 宽且 upper bound |r|=0.155 允许 near-zero true effect。Spearman ρ=-0.39 弱于 Pearson，暗示\n    outlier 影响。 整体降级为 exploratory，不进 abstract/conclusion。\n\n    '\n  tables:\n  - name: 'Table: GSM8K Temporal DIF Summary'\n    columns:\n    - metric\n    - standard_mh\n    - external_matching\n    - sanity\n    rows:\n    - - C%\n      - 18.9\n      - 45.1\n      - 0.35\n    - - n_items_flagged\n      - 249\n      - 595\n      - 5\n    - - DIF favor 2024\n      - 78\n      - 210\n      - 2\n    - - DIF favor 2023\n      - 171\n      - 385\n      - 3\n  - name: 'Table: GSM1K Correlation Analysis'\n    columns:\n    - statistic\n    - value\n    - p_value\n    - 95% CI\n    rows:\n    - - Pearson r\n      - -0.478\n      - 0.005\n      - '[-0.71, -0.16]'\n    - - Spearman ρ\n      - -0.39\n      - 0.025\n      - '[-0.66, -0.03]'\n    - - Partial r (ctrl accuracy)\n      - -0.37\n      - 0.035\n      - '[-0.64, -0.01]'\n  figures_description:\n  - 'Fig: Scatter of per-model DIF-C proportion vs GSM8K-GSM1K gap, r=-0.478, 标注 Cook''s\n    D outliers'\n  analysis: 'GSM8K 复制确认了 framework portability（ΔTPR 有效），但 GSM1K correlation 的负方向 是\n    median 档的关键弱点。必须在 paper 中用一段专门解释：DIF flags items whose functioning changed across\n    generations, not items that are contaminated. Hard items where 2024 models improve\n    may simultaneously show DIF (functioning changed) AND small contamination gap\n    (capability improvement, not memorization)。 降级为 exploratory per Dream #6 consensus。\n\n    '\n- name: bifactor_irt_equating_pilot\n  plan_id: plan_005\n  description: '在 METABENCH MMLU 数据上拟合 bifactor IRT 模型（general factor + 57 subject-specific\n    factors），选择 anchor items 并执行 fixed-parameter calibration。\n\n    '\n  expected_results:\n    bifactor_rmsea: 0.038\n    bifactor_cfi: 0.87\n    bifactor_tli: 0.85\n    bifactor_srmr: 0.052\n    general_factor_variance_explained: 0.41\n    n_anchor_items_selected: 2800\n    anchor_stability_criterion: '|Δ_MH|<0.43 (ETS A)'\n    equated_rho_vs_original: 0.94\n    target_rho_met: false\n    convergence_issues: 3 subjects failed to converge; fixed to unidimensional\n    computation_time_hours: 38\n  result_rationale: 'Median 档下 bifactor model 的 fit 低于 acceptable thresholds（CFI<0.90,\n    TLI<0.90）， 因为 MMLU 的 57 subjects 引入了 57 个 specific factors 加 general factor =\n    58 latent dimensions，5219 models 的 sample size 对此维度不足。General factor 仅解释 41% variance（理想\n    >60%），说明 MMLU 本质上高度多维。3 个小样本 subjects 收敛失败 需要降级为 unidimensional。Equated ρ=0.94\n    未达 target ρ≥0.95，主要因为 anchor item selection 受 bifactor misfit 影响。Median 档结论：bifactor\n    equating 在 MMLU 上不 可行，confirmed paper_framing.md 中 \"killed by plan_014 pre-check\"\n    的判断。 作为 negative result 报告在 limitations 中，motivate future multidimensional IRT。\n\n    '\n  tables:\n  - name: 'Table: Bifactor IRT Fit Indices'\n    columns:\n    - index\n    - value\n    - acceptable_threshold\n    - verdict\n    rows:\n    - - RMSEA\n      - 0.038\n      - <0.06\n      - PASS\n    - - CFI\n      - 0.87\n      - '>0.90'\n      - FAIL\n    - - TLI\n      - 0.85\n      - '>0.90'\n      - FAIL\n    - - SRMR\n      - 0.052\n      - <0.08\n      - PASS\n    - - General factor ω_h\n      - 0.41\n      - '>0.60'\n      - FAIL\n  figures_description:\n  - 'Fig: Scree plot — eigenvalue decay showing 57 factors above noise floor, no dominant\n    general factor'\n  analysis: 'Bifactor IRT equating killed。MMLU 的多维性使得单一 general factor 无法充分 表征 model\n    ability，anchor item 选择受 model misfit 污染。这是 structural limitation 而非 implementation\n    failure。Paper 中作为 \"empirical observation that motivates future multidimensional\n    IRT\" 报告，不作为 contribution。\n\n    '\n- name: item_generation_calibration\n  plan_id: plan_006\n  description: '为 DIF-flagged MMLU items 生成替换项，使用 LLM generation + student simulation\n    进行 difficulty calibration。\n\n    '\n  expected_results:\n    n_items_generated: 500\n    n_dif_items_targeted: 200\n    difficulty_correlation_prompt_based: 0.28\n    difficulty_correlation_student_sim: 0.71\n    difficulty_correlation_empirical: 0.65\n    construct_coverage_semantic_sim: 0.88\n    holdout_panel_rho: 0.91\n    gpu_hours_used: 160\n    items_passing_quality_filter: 340\n    quality_filter_rate: 0.68\n  result_rationale: 'Median 档下 prompt-based difficulty targeting 的 ρ=0.28 远低于 student\n    simulation 的 ρ=0.71，符合文献报告（arXiv 2602.06631: ρ=0.10–0.45）。Student simulation （arXiv\n    2601.09953）的 ρ=0.71 低于该文献报告的 r=0.75–0.82，因为 MMLU 的 domain diversity 使 universal\n    student simulator 难以 calibrate across 57 subjects。 Empirical calibration（实际跑 holdout\n    model panel）的 ρ=0.65 进一步降低，因为 simulation-to-reality gap。Holdout panel ρ=0.91 低于\n    equating target 0.95。 整体结论：item generation pipeline 可行但 precision 不足以支撑 equated\n    replacement claim。降级为 supplementary methodology contribution。\n\n    '\n  tables:\n  - name: 'Table: Difficulty Estimation Method Comparison'\n    columns:\n    - method\n    - difficulty_rho\n    - n_items\n    - compute_cost\n    rows:\n    - - Prompt-based targeting\n      - 0.28\n      - 500\n      - 8 GPU-h\n    - - Student simulation\n      - 0.71\n      - 500\n      - 45 GPU-h\n    - - Empirical (holdout panel)\n      - 0.65\n      - 340\n      - 107 GPU-h\n  figures_description:\n  - 'Fig: Predicted vs actual difficulty scatter — student sim (ρ=0.71) vs prompt\n    (ρ=0.28)'\n  analysis: 'Item generation pipeline 的核心瓶颈是 difficulty calibration precision。 ρ=0.65–0.71\n    不足以保证 equated score equivalence（需要 item-level precision 而非 correlation）。作为 methodology\n    贡献有价值但不足以支撑 Claim 3 的 regeneration narrative。与 plan_005 bifactor failure 共同导致\n    regeneration storyline 被完全 dropped。\n\n    '\n- name: cumulative_bayesian_dif\n  plan_id: plan_007\n  description: '实现 cumulative Bayesian DIF priors (Sinharay et al., 2006)，模拟 4 轮连续\n    benchmark administration，展示 evidence accumulation 带来的 power improvement。\n\n    '\n  expected_results:\n    single_admin_power_d10: 0.38\n    cumulative_2_admin_power_d10: 0.52\n    cumulative_3_admin_power_d10: 0.64\n    cumulative_4_admin_power_d10: 0.71\n    single_admin_power_d14: 0.68\n    cumulative_3_admin_power_d14: 0.85\n    fpr_single: 0.042\n    fpr_cumulative_3: 0.048\n    simulation_n_per_admin: 200\n    simulation_n_items: 500\n    simulation_n_reps: 1000\n  result_rationale: 'Median 档下 cumulative Bayesian DIF 的 power improvement 从 0.38→0.71（d=1.0,\n    4 administrations），符合 Sinharay et al. 的理论预测但略低于原文（原文 0.40→0.70 at 3 administrations，我们在\n    4 administrations 才达到 0.71）。差距因为 LLM benchmark 的 non-stationarity——successive\n    administrations 间 DIF pattern 不完全 stable（model ecosystem evolves），violating Bayesian\n    prior 的 stationarity assumption。 FPR 从 0.042 到 0.048 的轻微 inflation 是 informative\n    prior 带来的 false alarm cost。整体结论：simulation-only result，对 real-world benchmark\n    monitoring 有 suggestive value 但未在真实数据上验证。降级为 appendix。\n\n    '\n  tables:\n  - name: 'Table: Cumulative Bayesian DIF Power by Administration'\n    columns:\n    - n_admins\n    - power_d10\n    - power_d14\n    - fpr\n    rows:\n    - - 1\n      - 0.38\n      - 0.68\n      - 0.042\n    - - 2\n      - 0.52\n      - 0.78\n      - 0.044\n    - - 3\n      - 0.64\n      - 0.85\n      - 0.046\n    - - 4\n      - 0.71\n      - 0.89\n      - 0.048\n  figures_description:\n  - 'Fig: Power accumulation curve — d=1.0 and d=1.4, showing diminishing returns\n    after 3 administrations'\n  analysis: 'Simulation-only, underdeveloped for main body。核心 insight（evidence accumulation\n    improves detection of medium effects）是 textbook result，novelty 仅在 LLM benchmark\n    场景化。Median 档 reviewers 会 flag \"this is just running Sinharay''s method on simulated\n    data\"。降级为 appendix discussion。\n\n    '\n- name: graceful_degradation_analysis\n  plan_id: plan_008\n  description: '分析 benchmark validity 在 progressive item replacement 下的 degradation：\n    5%, 10%, 20%, 50% items replaced，评估 ranking stability, reliability, construct\n    coverage。\n\n    '\n  expected_results:\n    rho_at_5pct_replacement: 0.999\n    rho_at_10pct_replacement: 0.998\n    rho_at_20pct_replacement: 0.995\n    rho_at_50pct_replacement: 0.983\n    reliability_alpha_original: 0.946\n    reliability_alpha_at_20pct: 0.938\n    reliability_alpha_at_50pct: 0.912\n    construct_coverage_original: 57\n    construct_coverage_at_50pct: 57\n    n_subjects_losing_items_at_50pct: 12\n    min_items_per_subject_at_50pct: 31\n    theoretical_lower_bound_rho: ρ ≥ 1 - 2r/(1+r) where r = replacement rate\n  result_rationale: 'Median 档下 MMLU 的极高 measurement redundancy（12,508 items across\n    57 subjects） 使得即使 50% replacement 也仅将 ρ 降至 0.983。这是因为 MMLU 的 per-subject item\n    pools 足够大（median 200+ items），random replacement 均匀分布在 subjects 间， 每个 subject 保留足够\n    items 维持 reliable estimation。Reliability α 从 0.946 降至 0.912（50%）仍在 acceptable\n    range。Construct coverage 不受影响因为 replacement 是 within-subject。关键 caveat：这假设 replacement\n    items 的 psychometric properties 与 original 相近——plan_006 显示这不成立（ρ=0.65），实际 degradation\n    会更严重。\n\n    '\n  tables:\n  - name: 'Table: Validity Metrics Under Progressive Replacement'\n    columns:\n    - replacement_rate\n    - ranking_rho\n    - cronbach_alpha\n    - min_items_per_subject\n    rows:\n    - - 0%\n      - 1.0\n      - 0.946\n      - 63\n    - - 5%\n      - 0.999\n      - 0.944\n      - 60\n    - - 10%\n      - 0.998\n      - 0.941\n      - 57\n    - - 20%\n      - 0.995\n      - 0.938\n      - 50\n    - - 50%\n      - 0.983\n      - 0.912\n      - 31\n  figures_description:\n  - 'Fig: Degradation curves — ρ and α as function of replacement rate, with theoretical\n    lower bound'\n  analysis: '结果实际上强化了 Claim 4 的 redundancy narrative：MMLU 的 ranking stability 对 item\n    removal/replacement 极其鲁棒。但 median 档下这个结果是 double-edged—— 如果 removing 31% DIF items\n    doesn''t matter（ρ=0.997），reviewer 会问 \"so what''s the practical impact of your\n    finding?\" 需要 reframe 为 diagnostic value 而非 quality concern。降级为 supplementary evidence\n    for Claim 4.1 redundancy。\n\n    '\n- name: item_focused_trees\n  plan_id: plan_009\n  description: '实现 Item-Focused Trees (Tutz & Berger, 2016) 作为 categorical cohort\n    DIF 的 替代方案，将 model release date 作为 continuous covariate。\n\n    '\n  expected_results:\n    n_items_analyzed: 12508\n    ift_flagged_items: 4150\n    ift_flag_rate: 0.332\n    ift_dif_mh_jaccard: 0.72\n    ift_dif_mh_concordance: 0.85\n    ift_unique_flags: 890\n    mh_unique_flags: 658\n    ift_split_point_median_date: 2023-09\n    ift_nonlinear_items: 1230\n    ift_nonlinear_pct: 0.098\n    computation_time_hours: 12\n  result_rationale: 'Median 档下 IFT 的 flag rate（33.2%）略高于 MH（31.3%），因为 continuous covariate\n    模型捕捉了 MH 的 binary split 遗漏的 nonlinear trends（9.8% items 显示 non-monotonic DIF pattern）。Jaccard=0.72\n    的 moderate overlap 表明两种方法 largely agree 但 IFT 的 continuous modeling 额外捕捉了 gradual\n    drift items。IFT split point median 在 2023-09 附近，接近 MH 使用的 temporal cutoff，增加了\n    MH cohort definition 的 合理性。Median 档下 IFT 的价值是 robustness check 而非 primary method——\n    \"MH results are robust to categorical vs continuous covariate modeling\"。\n\n    '\n  tables:\n  - name: 'Table: IFT vs MH-DIF Comparison'\n    columns:\n    - metric\n    - MH_DIF\n    - IFT\n    - overlap\n    rows:\n    - - flag_rate\n      - 31.3%\n      - 33.2%\n      - Jaccard=0.72\n    - - n_flagged\n      - 3918\n      - 4150\n      - concordance=0.85\n    - - nonlinear_items\n      - N/A\n      - 1230\n      - 9.8% of total\n    - - computation_time\n      - 2h\n      - 12h\n      - —\n  figures_description:\n  - 'Fig: IFT tree visualization for 3 example items — showing split points and DIF\n    magnitude per branch'\n  analysis: 'IFT 确认 MH 结果的 robustness 并提供了 continuous DIF trend 的 additional insight。\n    9.8% nonlinear items 是 interesting finding 但不影响 main claims。降级为 appendix robustness\n    check——\"results hold whether we use categorical (MH) or continuous (IFT) covariate\n    modeling\"。\n\n    '\n- name: architecture_stratified_dif\n  plan_id: plan_010\n  description: '在 architecture-homogeneous subpopulation (decoder-only only) 上运行 DIF，\n    测试 IRT model fit 是否改善、spurious DIF 是否减少。\n\n    '\n  expected_results:\n    n_decoder_only: 5226\n    n_non_decoder: 1\n    decoder_only_pct: 99.98\n    dif_c_pct_decoder_only: 31.3\n    dif_c_pct_full: 31.3\n    jaccard_decoder_vs_full: 1.0\n    irt_rmsea_decoder: 0.042\n    irt_rmsea_full: 0.042\n    irt_cfi_decoder: 0.78\n    irt_cfi_full: 0.78\n    pct_models_lz_gt2_decoder: 97.8\n    pct_models_lz_gt2_full: 98.0\n    conclusion: architecture heterogeneity is a non-issue\n  result_rationale: 'Median 档下这是最 clear-cut 的实验：METABENCH MMLU 中 99.98% (5226/5227)\n    模型是 decoder-only，排除 1 个 non-decoder 模型完全不改变任何结果（Jaccard=1.0）。 IRT fit 同样不变，因为\n    misfit (|Lz|>2 for 98%) 源于 MMLU 的 inherent multidimensionality（57 subjects → 多维\n    ability），而非 architecture heterogeneity。 这是 proactive defense 实验：reviewer 无法质疑\n    \"architecture confound inflates DIF\" 因为 population 几乎完全 homogeneous。Zero GPU cost,\n    纯 data subsetting。\n\n    '\n  tables:\n  - name: 'Table: Architecture Stratification Results'\n    columns:\n    - population\n    - n_models\n    - c_pct\n    - irt_rmsea\n    - pct_lz_gt2\n    rows:\n    - - Full\n      - 5227\n      - 31.3\n      - 0.042\n      - 98.0\n    - - Decoder-only\n      - 5226\n      - 31.3\n      - 0.042\n      - 97.8\n    - - Delta\n      - -1\n      - 0.0\n      - 0.0\n      - -0.2\n  figures_description:\n  - 'Fig: Architecture composition pie chart — 99.98% decoder-only (appendix only)'\n  analysis: 'Architecture stratification 是 one-line result: \"METABENCH MMLU is 99.98%\n    decoder-only; excluding the single non-decoder model changes nothing (Jaccard=1.0).\"\n    Main body 一句话 + footnote，不需要 dedicated section。\n\n    '\n- name: semi_synthetic_contamination_validation\n  plan_id: plan_011\n  description: '向 METABENCH response matrix 注入已知 contamination，测量 DIF 在 controlled\n    ground truth 下的 detection power，解决 ground truth circularity concern。\n\n    '\n  expected_results:\n    n_clean_items_selected: 500\n    n_injection_items: 150\n    temporal_external_tpr_p0: 0.33\n    temporal_external_tpr_p03: 0.52\n    temporal_external_tpr_p05: 0.74\n    temporal_external_tpr_p07: 0.93\n    temporal_external_tpr_p10: 1.0\n    temporal_external_fpr: 0.318\n    temporal_external_delta_tpr_p05: 0.41\n    temporal_external_delta_tpr_p10: 0.67\n    ability_external_tpr_p10: 0.77\n    ability_external_fpr: 0.49\n    standard_mh_fpr_inflation_at_p10: 0.30→0.59\n    matching_variable_contamination: true\n    dose_response_monotonic: true\n  result_rationale: 'Median 档下 ΔTPR(p=0.5)=0.41 落在 key indicator range [0.35, 0.50]\n    内。 这比 registry 实际值 (ΔTPR(p=0.5)=0.508) 低约 0.1，因为 median 档假设 temporal label 携带的弱结构性（permutation\n    null 2–8%）吃掉了一部分 detection headroom。FPR=0.318 反映 temporal cohort 的 baseline instability（即使\n    clean items 中有 ~31.8% 被 flag，因为 \"clean\" is defined by Li et al. labels which don''t\n    capture differential effects）。Dose-response 从 p=0.3 到 p=1.0 单调增长确认了 injection\n    validity。Standard MH 的 FPR inflation（0.30→0.59 at p=1.0）确认了 matching variable\n    contamination——within-group matching variable 被 injection 污染导致 FPR 膨胀，这是 cross-subject\n    matching 的动机。\n\n    '\n  tables:\n  - name: 'Table: Semi-Synthetic Detection Power (Temporal, External Matching)'\n    columns:\n    - exploitation_rate_p\n    - tpr\n    - fpr\n    - delta_tpr\n    rows:\n    - - 0.0 (baseline)\n      - 0.33\n      - 0.318\n      - 0.0\n    - - 0.3\n      - 0.52\n      - 0.32\n      - 0.19\n    - - 0.5\n      - 0.74\n      - 0.318\n      - 0.41\n    - - 0.7\n      - 0.93\n      - 0.317\n      - 0.61\n    - - 1.0\n      - 1.0\n      - 0.316\n      - 0.67\n  - name: 'Table: Matching Variable Contamination Effect'\n    columns:\n    - matching_method\n    - fpr_p0\n    - fpr_p10\n    - delta_fpr\n    rows:\n    - - Standard (within-group)\n      - 0.298\n      - 0.59\n      - 0.292\n    - - External (cross-benchmark)\n      - 0.318\n      - 0.316\n      - -0.002\n  figures_description:\n  - 'Fig: Dose-response curve — TPR vs exploitation rate p, with 95% CI bands'\n  - 'Fig: FPR comparison — standard vs external matching as injection increases'\n  analysis: 'ΔTPR(p=0.5)=0.41 是 median 档的核心指标，表明 DIF 在 moderate exploitation rate\n    下有 meaningful detection power but not overwhelming。Reviewer 会追问 \"p=0.5 是否 realistic?\"——需要在\n    paper 中 argue contamination exploitation rates 在文献 中缺乏 empirical estimates，p=0.5\n    是 conservative middle ground。External matching 的 ΔFPR≈0 是 methodological highlight，直接支撑\n    cross-subject matching recommendation。\n\n    '\n- name: multi_benchmark_temporal_dif\n  plan_id: plan_028\n  description: '在 METABENCH 中的 ARC, HellaSwag, WinoGrande, TruthfulQA 上运行 temporal\n    DIF， 验证 cross-benchmark 泛化性。\n\n    '\n  expected_results:\n    mmlu_c_pct: 31.3\n    mmlu_random_c_pct: 0.18\n    winogrande_c_pct: 28.8\n    winogrande_random_c_pct: 0.35\n    truthfulqa_c_pct: 27.4\n    truthfulqa_random_c_pct: 0.4\n    arc_c_pct: 24.5\n    arc_random_c_pct: 0.55\n    gsm8k_c_pct: 18.9\n    gsm8k_random_c_pct: 0.3\n    hellaswag_c_pct: 17.2\n    hellaswag_random_c_pct: 0.3\n    cross_benchmark_range: 17.2–31.3%\n    all_random_below_1pct: true\n    min_enrichment_ratio: 31\n    n_benchmarks: 6\n  result_rationale: 'Median 档下 cross-benchmark C% range 为 17.2–31.3%，落在 key indicator\n    range [15.0, 32.0] 内。排序 MMLU > WinoGrande > TruthfulQA > ARC > GSM8K > HellaSwag\n    反映了各 benchmark 的 structural properties：MMLU（57 subjects, 12K items）和 WinoGrande（commonsense\n    reasoning, 高 memorization vulnerability）C% 最高； HellaSwag（sentence completion,\n    10K items 但 item homogeneity 高）和 GSM8K （math, single domain）C% 最低。所有 random-split\n    controls <1% 确认 temporal signal 在每个 benchmark 上都是 genuine。Median 档下 HellaSwag\n    和 GSM8K 的较低 C% 会被 reviewer 追问——需要解释 domain homogeneity 降低 DIF variance。\n\n    '\n  tables:\n  - name: 'Table: Cross-Benchmark Temporal DIF Summary'\n    columns:\n    - benchmark\n    - n_items\n    - n_ref\n    - n_foc\n    - c_pct\n    - random_c_pct\n    - enrichment_ratio\n    rows:\n    - - MMLU\n      - 12508\n      - 1080\n      - 807\n      - 31.3\n      - 0.18\n      - 174\n    - - WinoGrande\n      - 1267\n      - 1017\n      - 803\n      - 28.8\n      - 0.35\n      - 82\n    - - TruthfulQA\n      - 817\n      - 1080\n      - 807\n      - 27.4\n      - 0.4\n      - 69\n    - - ARC-Challenge\n      - 1172\n      - 1080\n      - 807\n      - 24.5\n      - 0.55\n      - 45\n    - - GSM8K\n      - 1319\n      - 1017\n      - 804\n      - 18.9\n      - 0.3\n      - 63\n    - - HellaSwag\n      - 10042\n      - 1080\n      - 807\n      - 17.2\n      - 0.3\n      - 57\n  figures_description:\n  - 'Fig: Bar chart — C% across 6 benchmarks with random-split control overlay'\n  analysis: '6 个 benchmark 的一致 temporal DIF pattern (17–31%, all >>random) 是 median\n    档下 最强的 generalizability evidence。但 Claim 3 的 cross-benchmark 证据被降级至 appendix（8\n    页限制），main body 仅保留 MMLU 结果 + 一句 \"consistent across 5 additional benchmarks (see\n    Appendix X)\"。\n\n    '\n- name: permutation_null_c_rate\n  plan_id: plan_029\n  description: '1000× permutation test：随机重新分配 2023/2024 temporal labels（保持 N_ref=1080,\n    N_foc=807），每次运行 MH-DIF，建立 C% 的 null distribution。\n\n    '\n  expected_results:\n    n_permutations: 1000\n    null_c_pct_mean: 4.8\n    null_c_pct_median: 4.6\n    null_c_pct_sd: 1.2\n    null_c_pct_95ci:\n    - 2.7\n    - 7.3\n    null_c_pct_99ci:\n    - 1.9\n    - 8.4\n    null_c_pct_max: 9.1\n    observed_c_pct: 31.3\n    z_score_vs_null: 22.1\n    p_value: <1e-50\n    ratio_observed_to_null_mean: 6.5\n    random_split_c_pct: 0.18\n    null_vs_random_split_ratio: 26.7\n  result_rationale: 'Median 档下 permutation null C% mean=4.8% 落在 key indicator range\n    [2.0, 8.0]。 Permutation null 显著高于 random-split control（4.8% vs 0.18%），因为 temporal\n    labels 与 ability 不完全正交：2024 模型平均 stronger（d=-0.17），permutation 打断了 true temporal\n    signal 但保留了 ability distribution 的 marginal structure。 Random-split 在 within-cohort\n    内操作所以 ability 完全 balanced，产生 near-zero C%。Permutation null 的 4.8% 表明 ~5% 的 \"DIF\"\n    可归因于 temporal label 本身 携带的 ability confound structure，但 31.3% 仍为 null 的 6.5× (z=22.1)。\n    Median 档下 reviewer 会追问 \"4.8% null 是否意味着 temporal cohort design 有 systematic bias?\"——需要在\n    paper 中解释这是 expected property of any non-randomized group comparison in observational\n    studies，并引用 plan_027 的 matched-ability analysis (C%=28.9%) 作为 complementary evidence。\n\n    '\n  tables:\n  - name: 'Table: Permutation Null Distribution'\n    columns:\n    - statistic\n    - value\n    rows:\n    - - Null mean C%\n      - 4.8\n    - - Null median C%\n      - 4.6\n    - - Null SD\n      - 1.2\n    - - Null 95% CI\n      - '[2.7, 7.3]'\n    - - Null max\n      - 9.1\n    - - Observed C%\n      - 31.3\n    - - z-score\n      - 22.1\n    - - Observed / Null mean\n      - 6.5×\n  - name: 'Table: Three Baselines Comparison'\n    columns:\n    - baseline\n    - c_pct\n    - interpretation\n    rows:\n    - - Random split (within-cohort)\n      - 0.18\n      - statistical noise floor\n    - - Permutation null (label shuffle)\n      - 4.8\n      - temporal label structure\n    - - Observed temporal DIF\n      - 31.3\n      - genuine + structural\n    - - Matched-ability (plan_027)\n      - 28.9\n      - genuine after ability control\n  figures_description:\n  - 'Fig: Histogram of 1000 permutation null C% values with observed 31.3% marked\n    as vertical line'\n  - 'Fig: Three-baseline comparison bar chart — random (0.18%), permutation (4.8%),\n    observed (31.3%)'\n  analysis: 'Permutation null 是 median 档下 Claim 1 的关键 calibration baseline。31.3% vs\n    4.8% null 给出 \"genuine DIF ≈ 26.5%\" 的 conservative estimate，与 plan_027 的 matched-ability\n    C%=28.9% convergent。Paper 应报告为 \"~25–29% depending on confound controls\"（取 plan_027\n    matched 28.9% 与 observed-null=26.5% 的 range）。 Permutation null 显式报告为 calibration\n    baseline 是对 reviewer \"is 31% above chance?\" 的 definitive answer。\n\n    '\n- name: odds_ratio_regression_transparency\n  plan_id: plan_030\n  description: '补充 pseudo R²=0.0007 的 odds ratio + 95% CI + McFadden/Nagelkerke R²\n    + deviance ratio，并构建更精细的 item-level model。\n\n    '\n  expected_results:\n    model1_domain_delta:\n      mcfadden_r2: 0.0007\n      nagelkerke_r2: 0.0013\n      subject_acc_delta_or_per_010: 1.58\n      subject_acc_delta_ci_per_010:\n      - 1.21\n      - 2.06\n      deviance_ratio: 0.0007\n    model2_domain_delta_plus_items:\n      mcfadden_r2: 0.044\n      nagelkerke_r2: 0.074\n      subject_acc_delta_or_per_010: 0.71\n      ctt_difficulty_or_per_010: 0.76\n      ctt_discrimination_or_per_010: 1.54\n    model3_item_delta:\n      mcfadden_r2: 0.0013\n      nagelkerke_r2: 0.0022\n      item_acc_change_or_per_010: 1.09\n      item_acc_change_ci:\n      - 1.53\n      - 2.99\n    model4_item_delta_plus_items:\n      mcfadden_r2: 0.045\n      nagelkerke_r2: 0.076\n      item_acc_change_or_per_010: 0.91\n      ctt_difficulty_or_per_010: 0.75\n      ctt_discrimination_or_per_010: 1.56\n    simpsons_paradox: true\n    lr_test_m1_vs_m2_chi2: 640.5\n    lr_test_m3_vs_m4_chi2: 648.2\n    best_model_mcfadden: 0.045\n    ability_confound_explained_pp: 4.2\n  result_rationale: 'Median 档下 Simpson''s paradox (Model 2 vs Model 1) 是核心 methodological\n    finding： domain accuracy Δ 的 OR 从 1.58 (Model 1, positive) 翻转为 0.71 (Model 2,\n    negative) after controlling for item properties。这是因为 high-discrimination items\n    (OR=1.54) 同时是 DIF-prone items AND high-accuracy-change items，产生 confound。McFadden\n    R² 即使在 best model (0.045) 下也极低，说明 DIF 的 item-level variance 绝大部分无法由 observed item\n    properties 解释。Median 档下 ability confound explained pp=4.2，落在 [3.0, 6.0] 范围内——高于\n    plan_027 的 2.4pp 因为 regression 捕捉了额外的 item-level confounding pathway。 Reviewer\n    会追问 Simpson''s paradox 的因果解释——需谨慎表述为 \"item difficulty may be a mediator rather\n    than confounder; Model 1 (marginal) and Model 2 (conditional) answer different\n    causal questions\"。\n\n    '\n  tables:\n  - name: 'Table: Logistic Regression Model Comparison'\n    columns:\n    - model\n    - predictors\n    - mcfadden_r2\n    - nagelkerke_r2\n    - aic\n    rows:\n    - - Model 1\n      - subject acc Δ\n      - 0.0007\n      - 0.0013\n      - 15548\n    - - Model 2\n      - subject acc Δ + CTT props\n      - 0.044\n      - 0.074\n      - 14910\n    - - Model 3\n      - item acc Δ\n      - 0.0013\n      - 0.0022\n      - 15539\n    - - Model 4\n      - item acc Δ + CTT props\n      - 0.045\n      - 0.076\n      - 14892\n  - name: 'Table: Simpson''s Paradox in Accuracy Δ Effect'\n    columns:\n    - model\n    - acc_delta_or\n    - direction\n    - interpretation\n    rows:\n    - - Model 1 (marginal)\n      - 1.58\n      - positive\n      - higher acc Δ → more DIF\n    - - Model 2 (conditional)\n      - 0.71\n      - negative\n      - higher acc Δ → LESS DIF after controlling item props\n  figures_description:\n  - 'Fig: Simpson''s paradox visualization — marginal vs conditional effect of accuracy\n    Δ on DIF probability'\n  analysis: Simpson's paradox 需要在 paper 中小心处理。Model 1 的 marginal positive effect 支持\n    \"capability gain causes DIF\" 的 naive interpretation，但 Model 2 的 conditional negative\n    effect 表明 item properties (especially discrimination) 是 confound。 Median 档下建议\n    Model 1 as primary (conservative, 不做因果 claim)，Model 2 as supplementary (illustrating\n    confound structure)。总 explained variance <5% (McFadden R²=0.045) 意味着 95%+ 的 DIF\n    variance 是 item-specific 且无法归因于 observed covariates——这实际上强化了 \"DIF captures genuine\n    item-level differential functioning, not a proxy for aggregate trends\" 的 narrative。\n",
      "numLines": 1180,
      "startLine": 1,
      "totalLines": 1180
    }
  },
  "sourceToolAssistantUUID": "1aaeaba9-4e3e-43f2-a359-9efff8d2f7fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e",
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
  "lastPrompt": "[DREAM Review Director] dream_id=20260521T122440 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_report…",
  "leafUuid": "3162777d-9bba-43f7-a8b5-43922fb7c86d",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Review IRT equated benchmark paper",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e"
}
```

---

### Assistant

_source line 15 · 2026-05-21T13:13:32.119Z_

<details><summary>Logged reasoning block</summary>

```text
Let me read the PDF in chunks to review the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3162777d-9bba-43f7-a8b5-43922fb7c86d",
  "isSidechain": false,
  "requestId": "req_011CbFmoqyzejJ8P8sTMRGvM",
  "type": "assistant",
  "uuid": "35d9e289-b971-4004-abeb-950a6ad80376",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013E4riemruXMaHdPsoh5AxS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19461,
      "cache_read_input_tokens": 24174,
      "output_tokens": 286,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19461,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 286,
          "cache_read_input_tokens": 24174,
          "cache_creation_input_tokens": 19461,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19461
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

_source line 16 · 2026-05-21T13:13:32.690Z_

Let me read the full PDF in chunks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35d9e289-b971-4004-abeb-950a6ad80376",
  "isSidechain": false,
  "requestId": "req_011CbFmoqyzejJ8P8sTMRGvM",
  "type": "assistant",
  "uuid": "b41f2b6e-f323-49f4-ae9a-966087c995b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013E4riemruXMaHdPsoh5AxS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19461,
      "cache_read_input_tokens": 24174,
      "output_tokens": 286,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19461,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 286,
          "cache_read_input_tokens": 24174,
          "cache_creation_input_tokens": 19461,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19461
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

_source line 17 · 2026-05-21T13:13:35.921Z_

<details open><summary>🔧 Tool call — Read · `toolu_0111jedmGuSe1mL42Wjxq1nV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/median/review_input_e90a5c14.pdf",
  "pages": "1-5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b41f2b6e-f323-49f4-ae9a-966087c995b5",
  "isSidechain": false,
  "requestId": "req_011CbFmoqyzejJ8P8sTMRGvM",
  "type": "assistant",
  "uuid": "96877efd-6b01-4548-95b2-e7982b0653d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013E4riemruXMaHdPsoh5AxS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19461,
      "cache_read_input_tokens": 24174,
      "output_tokens": 286,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19461,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 286,
          "cache_read_input_tokens": 24174,
          "cache_creation_input_tokens": 19461,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19461
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

_source line 18 · 2026-05-21T13:13:36.523Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KgxBuvRPvCsB8et42eJyJR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/median/review_input_e90a5c14.pdf",
  "pages": "6-11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96877efd-6b01-4548-95b2-e7982b0653d0",
  "isSidechain": false,
  "requestId": "req_011CbFmoqyzejJ8P8sTMRGvM",
  "type": "assistant",
  "uuid": "6c4c0af6-bb7c-4348-91b7-ca89710db91c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013E4riemruXMaHdPsoh5AxS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19461,
      "cache_read_input_tokens": 24174,
      "output_tokens": 286,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19461,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 286,
          "cache_read_input_tokens": 24174,
          "cache_creation_input_tokens": 19461,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19461
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

_source line 19 · 2026-05-21T13:13:36.938Z_

<details><summary>↩ Tool result · `toolu_0111jedmGuSe1mL42Wjxq1nV`</summary>

```text
PDF pages extracted: 5 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/median/review_input_e90a5c14.pdf (166KB)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "96877efd-6b01-4548-95b2-e7982b0653d0",
  "isSidechain": false,
  "promptId": "574ea9fb-2433-4f53-83c6-6ff0f801abc3",
  "type": "user",
  "uuid": "8adb27d4-03c9-4572-bf84-d7ca2a0647af",
  "toolUseResult": {
    "type": "parts",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/median/review_input_e90a5c14.pdf",
      "originalSize": 170001,
      "outputDir": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-2-projects-irt-equated-bench-regen/48af77a8-24b1-406c-8f2b-6ae7c5af4a8e/tool-results/pdf-4202d9e6-8ad0-4577-a179-4d768fb7bec4",
      "count": 5
    }
  },
  "sourceToolAssistantUUID": "96877efd-6b01-4548-95b2-e7982b0653d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

## Round 2

4 recorded events

### User

_source line 20 · 2026-05-21T13:13:36.918Z_

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8adb27d4-03c9-4572-bf84-d7ca2a0647af",
  "isSidechain": false,
  "promptId": "574ea9fb-2433-4f53-83c6-6ff0f801abc3",
  "type": "user",
  "isMeta": true,
  "uuid": "470acca2-0dc3-4032-9565-d86c88e6b99f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260521T122440 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_report…",
  "leafUuid": "8adb27d4-03c9-4572-bf84-d7ca2a0647af",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Review IRT equated benchmark paper",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e"
}
```

---

### Tool result

_source line 23 · 2026-05-21T13:13:37.473Z_

<details><summary>↩ Tool result · `toolu_01KgxBuvRPvCsB8et42eJyJR`</summary>

```text
PDF pages extracted: 6 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/median/review_input_e90a5c14.pdf (166KB)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c4c0af6-bb7c-4348-91b7-ca89710db91c",
  "isSidechain": false,
  "promptId": "574ea9fb-2433-4f53-83c6-6ff0f801abc3",
  "type": "user",
  "uuid": "b71d2fe9-96d1-48d0-9376-313383c81f0f",
  "toolUseResult": {
    "type": "parts",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/median/review_input_e90a5c14.pdf",
      "originalSize": 170001,
      "outputDir": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-2-projects-irt-equated-bench-regen/48af77a8-24b1-406c-8f2b-6ae7c5af4a8e/tool-results/pdf-79d5631f-2e65-4bb2-95b5-452902d4babc",
      "count": 6
    }
  },
  "sourceToolAssistantUUID": "6c4c0af6-bb7c-4348-91b7-ca89710db91c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

## Round 3

16 recorded events

### User

_source line 24 · 2026-05-21T13:13:37.466Z_

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b71d2fe9-96d1-48d0-9376-313383c81f0f",
  "isSidechain": false,
  "promptId": "574ea9fb-2433-4f53-83c6-6ff0f801abc3",
  "type": "user",
  "isMeta": true,
  "uuid": "bbef6dda-64f8-48a3-8570-f689afcdc447",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260521T122440 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_report…",
  "leafUuid": "b71d2fe9-96d1-48d0-9376-313383c81f0f",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Review IRT equated benchmark paper",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e"
}
```

---

### Assistant

_source line 27 · 2026-05-21T13:13:42.661Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have read the full paper and the review context. Let me now compose a thorough review and submit it. Let me first load the submit tool schema.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbef6dda-64f8-48a3-8570-f689afcdc447",
  "isSidechain": false,
  "requestId": "req_011CbFmpStTkwZiE8wspyW4S",
  "type": "assistant",
  "uuid": "c78443c9-48ec-414e-b225-d390fedd0bcb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FnUywPUPkE43SVtXERnVJG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14395,
      "cache_read_input_tokens": 43635,
      "output_tokens": 158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14395,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 158,
          "cache_read_input_tokens": 43635,
          "cache_creation_input_tokens": 14395,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14395
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

_source line 28 · 2026-05-21T13:13:43.757Z_

I've read the full paper (11 pages) and the experiment design context. Let me load the submission tool and compose the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c78443c9-48ec-414e-b225-d390fedd0bcb",
  "isSidechain": false,
  "requestId": "req_011CbFmpStTkwZiE8wspyW4S",
  "type": "assistant",
  "uuid": "1214eb2f-c769-4262-bd5e-7a8e63050086",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FnUywPUPkE43SVtXERnVJG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14395,
      "cache_read_input_tokens": 43635,
      "output_tokens": 158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14395,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 158,
          "cache_read_input_tokens": 43635,
          "cache_creation_input_tokens": 14395,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14395
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

_source line 29 · 2026-05-21T13:13:44.304Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012gnBMiZPBEooDBPEBwXWUf`</summary>

```json
{
  "query": "select:submit_dream_review_report",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1214eb2f-c769-4262-bd5e-7a8e63050086",
  "isSidechain": false,
  "requestId": "req_011CbFmpStTkwZiE8wspyW4S",
  "type": "assistant",
  "uuid": "bd42c0a9-e152-47e4-bd3f-4a5ca3267ced",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FnUywPUPkE43SVtXERnVJG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14395,
      "cache_read_input_tokens": 43635,
      "output_tokens": 158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14395,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 158,
          "cache_read_input_tokens": 43635,
          "cache_creation_input_tokens": 14395,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14395
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

_source line 30 · 2026-05-21T13:13:44.320Z_

<details><summary>↩ Tool result · `toolu_012gnBMiZPBEooDBPEBwXWUf`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd42c0a9-e152-47e4-bd3f-4a5ca3267ced",
  "isSidechain": false,
  "promptId": "574ea9fb-2433-4f53-83c6-6ff0f801abc3",
  "type": "user",
  "uuid": "04fa6528-683b-4c58-9c5e-d0e8a6bf4faf",
  "toolUseResult": {
    "matches": [],
    "query": "select:submit_dream_review_report",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "bd42c0a9-e152-47e4-bd3f-4a5ca3267ced",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T13:13:52.602Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01GgYkBGecJ6ssXv6zDofCsB`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_dream_review_report",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04fa6528-683b-4c58-9c5e-d0e8a6bf4faf",
  "isSidechain": false,
  "requestId": "req_011CbFmpx8cNUPUKFKA9d3kJ",
  "type": "assistant",
  "uuid": "3761c8d8-91c8-4c30-8401-cda97dd6dbd2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GNcyYGpJixD6pv4SKee4fj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 177,
      "cache_read_input_tokens": 58030,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 177,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 89,
          "cache_read_input_tokens": 58030,
          "cache_creation_input_tokens": 177,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 177
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

_source line 32 · 2026-05-21T13:13:52.615Z_

<details><summary>↩ Tool result · `toolu_01GgYkBGecJ6ssXv6zDofCsB`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__submit_dream_review_report"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3761c8d8-91c8-4c30-8401-cda97dd6dbd2",
  "isSidechain": false,
  "promptId": "574ea9fb-2433-4f53-83c6-6ff0f801abc3",
  "type": "user",
  "uuid": "33c20f99-6bc9-45fb-ac07-f30c94a1b63e",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "query": "select:mcp__agent-ml-research__submit_dream_review_report",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "3761c8d8-91c8-4c30-8401-cda97dd6dbd2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-21T13:13:55.969Z_

Now I'll compose and submit the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33c20f99-6bc9-45fb-ac07-f30c94a1b63e",
  "isSidechain": false,
  "requestId": "req_011CbFmqZoDsZ4WBqh8i9tpi",
  "type": "assistant",
  "uuid": "7bb0e5cb-f47d-4a6f-a5a6-b5867447a584",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTpVy2UFr9rzsXXYhxJjxr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 713,
      "cache_read_input_tokens": 58207,
      "output_tokens": 4557,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 713,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4557,
          "cache_read_input_tokens": 58207,
          "cache_creation_input_tokens": 713,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 713
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

_source line 34 · 2026-05-21T13:15:50.868Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_018m7b9Z8yc1KtPCgC8sfHEH`</summary>

```json
{
  "report": "# Dream Review Report — Psychometric DIF Analysis Reveals 25–29% Temporal Item Instability in MMLU\n\n**Venue calibration:** EMNLP 2026 (ARR), Long paper, 8-page limit\n\n---\n\n## Overall Assessment: 3.0 (Findings-level)\n\n**Soundness:** 3.5 / 5\n**Excitement:** 2.5 / 5\n**Reproducibility:** 4.0 / 5\n\n---\n\n## Summary\n\nThe paper applies Mantel–Haenszel Differential Item Functioning (MH-DIF) analysis to the METABENCH MMLU response matrix (5,227 models × 12,508 items), finding that 25–29% of items exhibit large DIF (ETS Category C) between 2023 and 2024 model cohorts. The authors argue this instability is item-specific (domain improvement explains ≤7.6% of variance), does not threaten ranking validity (ρ≈0.997), and is invisible to web-overlap-based contamination detectors (enrichment≈1.0). They propose a semi-synthetic validation framework with cross-subject matching (ΔFPR=0.000) and release a DIF audit protocol for benchmark maintainers. Appendices cover cross-benchmark generalization (6 benchmarks), GSM1K ground truth correlation, RL robustness, alternative detectors (ConStat, DVD), ensemble fusion (negative result), bifactor IRT equating (negative result), item generation calibration, and cumulative Bayesian DIF.\n\n---\n\n## Strengths\n\n### S1: Well-chosen methodology with rigorous calibration\nThe MH-DIF procedure is the gold standard in educational measurement for detecting differential item functioning, and applying it at this scale (5,227 × 12,508) to LLM benchmarks is genuinely novel in the NLP community. The three-baseline calibration design (random split 0.21%, permutation null 4.8%, observed 31.3%) is methodologically clean and provides convincing evidence that the temporal DIF signal is not statistical noise. The permutation null quantifying the structural signal from temporal labels (d=−0.17 ability gap) is a particularly thoughtful control.\n\n### S2: Honest and well-framed negative results\nThe paper is commendably transparent about what DIF does *not* do: it does not detect contamination (enrichment≈1.0 with web-overlap labels), the bifactor IRT equating fails (CFI=0.87, TLI=0.85), the ensemble fusion is a negative result, and within-family controls are confounded by capability gaps (d≈−0.99). Framing DIF as \"diagnostic lens, not quality filter\" is the right move and avoids overclaiming.\n\n### S3: Practical audit protocol\nSection 4.6's DIF audit protocol — specifying monitoring frequency, decision rules (ETS C + permutation null), response options (retain/supplement/investigate), and matching variable recommendations — is concrete and immediately actionable for benchmark maintainers. This practical contribution differentiates the paper from purely analytical work.\n\n### S4: Cross-subject matching innovation\nThe identification of matching variable contamination in within-subject MH-DIF (FPR inflation from 0.298 to 0.59 at p=1.0) and the cross-subject matching solution (ΔFPR=−0.002≈0) is a genuine methodological contribution applicable to any future DIF analysis on multi-domain benchmarks.\n\n### S5: Comprehensive appendices\nThe paper covers an impressive breadth of experiments — 6 benchmarks, IFT robustness, architecture stratification, ConStat/DVD comparison, ensemble fusion, bifactor IRT, item generation, cumulative Bayesian DIF — providing thorough coverage of the experimental space.\n\n---\n\n## Weaknesses\n\n### W1 (Major): The \"so what\" problem — instability without consequence\nThe paper's central finding is that 25–29% of MMLU items are functionally unstable, but simultaneously demonstrates that removing *all* DIF-flagged items preserves ρ≈0.997 ranking correlation. This creates a fundamental tension: if the instability doesn't affect rankings, what is the practical problem being diagnosed? The \"diagnostic lens\" framing partially addresses this, but the paper never convincingly demonstrates a concrete downstream consequence of the instability it detects. The difficulty×direction interaction (§4.5, hardest-decile 88.7% focal-favoring, easiest-decile 96.2% reference-favoring) is interesting but underdeveloped — it reads as an observation, not a demonstrated harm.\n\n**Suggestion:** Strengthen with a concrete case study showing how DIF patterns reveal a *specific, actionable* insight about capability shifts (e.g., which subjects' items shift most and what this means for benchmark interpretation), rather than stopping at aggregate statistics.\n\n### W2 (Major): Novelty concerns — applying textbook psychometrics\nThe core method (MH-DIF with ETS delta classification) dates to Holland & Thayer (1988). The paper's novelty claim is \"largest DIF analysis on an LLM benchmark,\" which is a scale argument, not a methodological one. The cross-subject matching contribution (§3.2) is the most novel methodological element, but it occupies only one paragraph in the main text. Reviewers familiar with psychometrics may view this as a competent application of existing tools rather than a methodological advance.\n\n**Suggestion:** Elevate the cross-subject matching finding — it addresses a problem (conditioning variable contamination) that is specific to the LLM benchmark setting and not present in standard educational testing where the matching variable is examinee ability.\n\n### W3 (Major): GSM1K negative correlation undermines the narrative\nThe GSM1K correlation analysis (r=−0.478, opposite to the contamination hypothesis) is buried in Appendix A.2 but represents a significant challenge to interpreting DIF in the contamination context. The paper's explanation — \"DIF flags items whose functioning changed, which may include items where 2024 models genuinely improved\" — is reasonable but essentially concedes that DIF cannot distinguish contamination from genuine capability improvement. This is a fundamental limitation that should be more prominently addressed rather than relegated to an appendix paragraph.\n\n### W4 (Moderate): Low explained variance raises interpretability concerns\nThe logistic regression analysis (Table 3) shows McFadden R² = 0.045 even for the best model, meaning >95% of DIF variance is unexplained by observed item properties. While the paper frames this positively (\"item-specific, not aggregate\"), it also means the paper cannot offer a substantive explanation of *why* specific items exhibit DIF. The Simpson's paradox finding (§4.2) is interesting but the causal interpretation is deliberately left ambiguous (\"we report both models without privileging a causal interpretation\"), which weakens the analytical contribution.\n\n### W5 (Moderate): Semi-synthetic validation has ecological validity concerns\nThe injection mechanism (flipping incorrect→correct responses) is acknowledged as a simplification in Limitations, but the concern goes deeper: real contamination manifests through partial memorization, reasoning shortcuts, and training data curation — all of which produce different DIF signatures than uniform response flipping. The ΔTPR=0.41 at p=0.5 is thus a measure of sensitivity to a specific, simplified contamination model, and its relevance to real-world contamination detection is unclear. Additionally, the paper never empirically grounds what a realistic exploitation rate p might be.\n\n### W6 (Minor): IRT model misfit is severe but underplayed\n98% of models showing |Lz|>2 under unidimensional IRT means the foundational psychometric model is essentially misspecified for this population. MH-DIF is robust to moderate misfit, but at this level (98% misfit), the theoretical guarantees are strained. The Limitations section mentions this briefly but does not discuss what impact this level of misfit could have on MH-DIF's Type I error rate or effect size estimates.\n\n### W7 (Minor): Within-family controls are acknowledged as confounded but still reported prominently\nLlama-2 vs. Llama-3 (C%=58.7%) and Mistral vs. Mixtral (C%=36.2%) comparisons confound temporal DIF with capability gaps (d≈−0.99), as the paper acknowledges. But they still appear in §4.2 of the main text, potentially misleading readers who don't carefully parse the caveat. These should either be explicitly labeled as \"inconclusive due to confounding\" or moved to an appendix.\n\n---\n\n## Experiment Coverage Assessment\n\nComparing against the experiment design context:\n\n| Experiment | Covered in paper? | Placement | Adequate? |\n|---|---|---|---|\n| real_data_dif_mmlu (plan_001) | Yes | §4.1 main body | Yes — core result |\n| rl_robustness (plan_002) | Yes | §5 Limitations + App B.1 | Adequate — correctly scoped |\n| constat_perturbation (plan_003a) | Yes | App C.1 | Adequate |\n| dvd_generation_variance (plan_003b) | Yes | App C.2 | Adequate |\n| ensemble_fusion (plan_003c) | Yes | App C.3 | Adequate — honest negative result |\n| cross_benchmark_gsm8k (plan_004) | Yes | App A.2 | Adequate but GSM1K negative direction underplayed |\n| bifactor_irt_equating (plan_005) | Yes | App D.1 | Adequate — honest negative result |\n| item_generation (plan_006) | Yes | App D.2 | Adequate |\n| cumulative_bayesian_dif (plan_007) | Yes | App D.3 | Adequate — simulation-only caveat clear |\n| graceful_degradation (plan_008) | Yes | §4.5 + Table 5 | Yes |\n| item_focused_trees (plan_009) | Yes | App B.2 | Adequate |\n| architecture_stratification (plan_010) | Yes | §4.2 + App B.3 | Yes |\n| semi_synthetic (plan_011) | Yes | §4.4 + Table 4 | Yes |\n| multi_benchmark (plan_028) | Yes | App A.1 + Table 6 | Adequate |\n| permutation_null (plan_029) | Yes | §4.1 + Table 2 | Yes — well integrated |\n| odds_ratio_regression (plan_030) | Yes | §4.2 + Table 3 | Yes — Simpson's paradox reported |\n\n**Coverage verdict:** All 16 imagined experiments are represented. Main body prioritization is reasonable (plans 001, 011, 008, 010, 029, 030 in main text; rest in appendices). The paper makes appropriate choices about what to relegate to appendices given the 8-page limit.\n\n---\n\n## Detailed Comments\n\n1. **Abstract:** \"psychometric audit protocol\" is the right lead — this is the most practically valuable contribution. However, \"pseudo R²=0.0007\" in the abstract is oddly specific and may confuse readers unfamiliar with McFadden R².\n\n2. **§1 Intro, \"Instability ≠ invalidity\" subsection:** This is well-written and sets expectations correctly. The ≤7.6% explained variance claim appears in Contribution 1 but references Table 3's Nagelkerke R² (0.076) — clarify which R² metric maps to the 7.6% in the text.\n\n3. **§3.1:** The ETS delta classification system (A/B/C) is clearly explained. Good.\n\n4. **§3.3:** Permutation null is well-motivated but the section is very brief. Consider noting that this is a conditional permutation test (fixing Nref/Nfoc) to distinguish it from unconditional permutation.\n\n5. **Table 1:** FPRLi column header needs definition in the table caption or at first use — \"fraction of Li et al. web-overlap 'clean' items flagged\" is not immediately obvious.\n\n6. **§4.1, \"Domain specificity\":** The ecological correlation caveat (ρ=0.32 is subject-level, not item-level) is important and well-flagged.\n\n7. **§4.2, Simpson's paradox:** This is the most intellectually interesting finding in the paper but is underexploited. The reversal from OR=1.58 to OR=0.71 after conditioning on CTT properties deserves more analysis — what specifically about high-discrimination items makes them both DIF-prone and high-accuracy-change?\n\n8. **§4.4:** ΔTPR is a clean metric. The cross-subject matching result (ΔFPR=0.000 across 5 subjects) is compelling but would benefit from reporting across more than 5 subjects (of the 57 available).\n\n9. **§4.5, \"DIF as diagnostic, not filter\":** The z-score comparisons (DIF removal z=−8 to −49σ vs. accuracy-gap removal z=−157) effectively demonstrate that DIF items carry genuine signal while being the least disruptive removal strategy. This is the strongest argument for the \"diagnostic lens\" framing.\n\n10. **§5 Limitations:** Appropriately concise (3 points). The RL robustness limitation (N=13, DeLong p=0.34) is honestly reported.\n\n11. **§6 Conclusion:** Clean and appropriately scoped. Does not overclaim.\n\n12. **References:** 16 references is lean for a paper of this scope. Missing some relevant work: Zopf (2018) on DIF in NLP; recent work on temporal stability of LLM benchmarks beyond Recht et al. and Schaeffer et al.\n\n13. **Page count:** Main text appears to be 6 pages + references on page 7 + 4 pages of appendices. Within the 8-page limit for main text (Limitations does not count toward limit). Compliant.\n\n---\n\n## Questions for Authors\n\n1. Given that 98% of models show |Lz|>2, have you investigated whether MH-DIF's Type I error rate is inflated under this level of model misfit? A simulation study comparing MH-DIF performance under well-fitting vs. misspecified IRT models would substantially strengthen the methodological contribution.\n\n2. The permutation null of 4.8% suggests temporal labels carry weak structural signal. Have you considered a propensity-score-matched design (matching on model ability, size, family) as an alternative to the 1:1 nearest-neighbor matching? This could provide tighter confound control.\n\n3. For the cross-subject matching (§3.2), you report ΔFPR=0.000 across 5 subjects. Which 5 subjects were tested? Was this a random sample or selected? Results across all 57 subjects (or at least a stratified sample) would be more convincing.\n\n4. The GSM1K negative correlation (r=−0.478) suggests DIF may flag items where models genuinely improve rather than items that are contaminated. Does this undermine the utility of DIF for benchmark maintenance, or does it actually support the \"diagnostic lens\" framing (detecting capability shifts regardless of cause)?\n\n---\n\n## Minor Issues\n\n- Table 2 caption: \"matched-ability controls for cohort ability differences\" — specify that this is 1:1 nearest-neighbor matching on total score\n- §4.2: \"Architecture homogeneity\" paragraph could be a footnote — the 99.98% decoder-only finding is a one-liner\n- App A.2: Table 7 is labeled \"GSM1K correlation analysis\" but includes Pearson, Spearman, and partial correlations — the partial r controls for accuracy but this isn't stated in the table\n- App D.2: \"GPU cost: 160 hours\" is mentioned but the item generation methodology is unclear — which LLM was used for generation? What quality filter was applied?\n\n---\n\n## Scoring Rationale\n\n**Soundness (3.5):** The methodology is correctly applied and the calibration design is rigorous. The three-baseline comparison is convincing. Deductions for: (a) 98% IRT model misfit with insufficient analysis of its impact on MH-DIF validity; (b) semi-synthetic injection mechanism is a significant simplification; (c) GSM1K negative correlation is underaddressed.\n\n**Excitement (2.5):** The paper is a competent and thorough application of established psychometric methods to a timely problem. However, the core finding (items are unstable but rankings aren't affected) creates a \"so what\" tension. The novelty is primarily in scale and application domain, not in methodology. The cross-subject matching contribution is genuinely novel but underemphasized. The diagnostic lens framing is reasonable but the paper doesn't fully deliver on showing what the diagnostic reveals beyond aggregate statistics.\n\n**Reproducibility (4.0):** METABENCH is publicly available. MH-DIF is a standard procedure. The paper clearly specifies cohort definitions, thresholds, and analysis parameters. The audit protocol is concrete. Minor deductions for: (a) not all analysis code is described in sufficient detail for exact replication; (b) semi-synthetic injection details could be more precise.\n\n**Overall (3.0 — Findings-level):** The paper makes a solid empirical contribution — the first large-scale DIF analysis on an LLM benchmark — with careful methodology and honest reporting of negative results. The cross-subject matching innovation and audit protocol add practical value. However, the limited novelty (applying textbook methods), the \"instability without consequence\" tension, the unexplained 95%+ DIF variance, and the GSM1K negative correlation collectively keep it below the Main conference threshold. The work is well-suited for Findings, where the empirical thoroughness and practical contributions would be valued. To reach Main (4.0), the paper would need: (1) a stronger demonstration of what the diagnostic lens *reveals* beyond aggregate instability rates, (2) more analysis of the IRT misfit impact, and (3) elevation of the cross-subject matching contribution as a primary methodological advance.\n\n---\n\n## Responsible NLP Checklist Notes\n\nThe paper does not include the mandatory Responsible NLP Research Checklist (Sections A–E). For ARR submission, this must be added. The anonymity requirement appears satisfied (no author names, no identifying URLs). No ethical concerns with the analysis (uses publicly available benchmark data).\n",
  "project": "irt_equated_bench_regen",
  "tier": "median",
  "dream_id": "20260521T122440",
  "overall_score": "3.0 — Findings-level (borderline Findings accept)",
  "review_visible": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bb0e5cb-f47d-4a6f-a5a6-b5867447a584",
  "isSidechain": false,
  "requestId": "req_011CbFmqZoDsZ4WBqh8i9tpi",
  "type": "assistant",
  "uuid": "b5a03d33-079e-4441-84fb-07b9c014f963",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTpVy2UFr9rzsXXYhxJjxr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 713,
      "cache_read_input_tokens": 58207,
      "output_tokens": 4557,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 713,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4557,
          "cache_read_input_tokens": 58207,
          "cache_creation_input_tokens": 713,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 713
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

_source line 35 · 2026-05-21T13:16:00.636Z_

<details><summary>↩ Tool result · `toolu_018m7b9Z8yc1KtPCgC8sfHEH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/median/review_report.md\", \"dream_id\": \"dream_20260521T122440\", \"tier\": \"median\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b5a03d33-079e-4441-84fb-07b9c014f963",
  "isSidechain": false,
  "promptId": "574ea9fb-2433-4f53-83c6-6ff0f801abc3",
  "type": "user",
  "uuid": "fffcdcc6-37d9-4615-bcee-51f7490eab49",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"report_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/median/review_report.md\\\", \\\"dream_id\\\": \\\"dream_20260521T122440\\\", \\\"tier\\\": \\\"median\\\", \\\"review_visible\\\": true}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/median/review_report.md\", \"dream_id\": \"dream_20260521T122440\", \"tier\": \"median\", \"review_visible\": true}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "b5a03d33-079e-4441-84fb-07b9c014f963",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 36 · 2026-05-21T13:16:00.659Z_

```json
{
  "parentUuid": "fffcdcc6-37d9-4615-bcee-51f7490eab49",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "33f241a5-44c6-426b-81b0-e38de6f51c75",
  "timestamp": "2026-05-21T13:16:00.659Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 37 · 2026-05-21T13:16:07.723Z_

Review submitted. Score: **3.0 (Findings-level)**.

Key takeaways:
- **Strengths:** Rigorous three-baseline calibration, honest negative results, practical audit protocol, novel cross-subject matching contribution
- **Core weakness:** The "instability without consequence" tension — 25–29% items are unstable yet ρ≈0.997 ranking correlation is preserved, which undercuts urgency
- **Other concerns:** Textbook methodology (novelty is in scale/application, not method), GSM1K negative correlation (r=−0.478) undermines contamination interpretation, 98% IRT model misfit underaddressed, >95% DIF variance unexplained

Report written to `dream_reports/dream_20260521T122440/median/review_report.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33f241a5-44c6-426b-81b0-e38de6f51c75",
  "isSidechain": false,
  "requestId": "req_011CbFmzzk9qMoW41qSitj4V",
  "type": "assistant",
  "uuid": "1dce6b6a-0906-41fc-9c47-94e5276650ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017cDZPafcdUZyepxVZWU285",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4793,
      "cache_read_input_tokens": 58920,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4793,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 58920,
          "cache_creation_input_tokens": 4793,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4793
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

_source line 38_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260521T122440 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_report…",
  "leafUuid": "1dce6b6a-0906-41fc-9c47-94e5276650ef",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Review IRT equated benchmark paper",
  "sessionId": "48af77a8-24b1-406c-8f2b-6ae7c5af4a8e"
}
```

---
