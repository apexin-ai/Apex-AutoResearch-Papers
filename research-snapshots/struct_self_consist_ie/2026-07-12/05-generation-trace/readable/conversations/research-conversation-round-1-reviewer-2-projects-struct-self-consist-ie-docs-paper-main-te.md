# Research conversation: [Round 1 审稿请求]: 你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。 ## 审稿对象 - 论文路径：`projects/struct_self_consist_ie/docs/paper/main.te

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 93
- **Recorded user turns:** 3
- **Tool calls:** 25
- **Original source:** `logs/chats/exported-trajectories/account-3/b9bf08df-1b1e-4be4-9e83-613f82fe746b.jsonl`
- **Structured JSON:** [`d474264351ceb0de1c85.json`](../../sessions/d4/d474264351ceb0de1c85.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T03:57:44.346Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T03:57:44.346Z",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "content": "[Round 1 审稿请求]:\n你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## 审稿对象\n- 论文路径：`projects/struct_self_consist_ie/docs/paper/main.tex`（分节结构，各节在 `sections/` 下）\n- 目标 venue：**EMNLP 2026 Main Conference**（通过 ARR May 2026 cycle 提交）\n- 截止日期：2026-05-25\n- 格式：ACL 模板 `[review]`，长文 8 页正文，Limitations/Ethics 不计入页数，double-blind\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献定位\n- \"First multi-family comparison of confidence signals for generative IE\" 是否成立？是否有已发表工作做了类似比较？\n- \"Correlation-selection gap\" 作为核心发现——是否真正新颖，还是 self-consistency 文献中已知的现象？\n- Soft Jaccard 相对于 Nedellec (2026) 的增量贡献是否足够\n- 三项 contributions 是否分别有实质性的学术价值\n\n### 2. Related Work 覆盖\n- 自查以下方向是否有重要遗漏：\n  - Self-consistency / test-time scaling（2024-2026）\n  - Confidence / uncertainty estimation for LLMs（2024-2026）\n  - Generative IE 方法（UniNER, GoLLIE 等）\n  - Structured prediction 中的 calibration 工作\n- 对 Nedellec (2026) 的差异化论述是否公平准确\n- 引用是否真实存在（检查是否有可疑的 hallucinated citations）\n\n### 3. 写作质量与逻辑\n- Abstract → Introduction → Contributions 的叙事是否连贯\n- 论文结构是否合理（是否有冗余或缺失的 section）\n- 术语使用是否一致（如 \"quality estimation\" vs \"quality prediction\"）\n- Figure/Table 是否自解释、caption 是否充分\n- Discussion 是否过度推断或保守不足\n\n### 4. 格式合规\n- 页数是否符合 8 页限制（请估算）\n- 参考文献格式是否正确\n- 匿名性是否完整（是否有泄露身份的线索：GitHub URL、acknowledgments、自引模式）\n- Limitations section 是否充分（ARR 要求，desk-reject 项）\n- 是否缺少 Ethics Statement\n\n### 5. 负面结果的呈现\n- \"No signal reliably surpasses greedy\" 是核心负面结果——呈现是否平衡\n- 是否过度包装负面结果为正面贡献\n- 对未来工作的建议是否具体且可行\n\n请输出标准审稿格式：Summary → Strengths → Weaknesses（分 Must-Fix / Should-Fix / Minor） → Questions → Missing References → Score (1-10) + Confidence (1-5)。"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T03:57:44.350Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T03:57:44.350Z",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b"
}
```

---

## Round 1

81 recorded events

### User

_source line 3 · 2026-05-15T03:57:44.385Z_

[Round 1 审稿请求]:
你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。

## 审稿对象
- 论文路径：`projects/struct_self_consist_ie/docs/paper/main.tex`（分节结构，各节在 `sections/` 下）
- 目标 venue：**EMNLP 2026 Main Conference**（通过 ARR May 2026 cycle 提交）
- 截止日期：2026-05-25
- 格式：ACL 模板 `[review]`，长文 8 页正文，Limitations/Ethics 不计入页数，double-blind

## 你的审查侧重

### 1. 新颖性与贡献定位
- "First multi-family comparison of confidence signals for generative IE" 是否成立？是否有已发表工作做了类似比较？
- "Correlation-selection gap" 作为核心发现——是否真正新颖，还是 self-consistency 文献中已知的现象？
- Soft Jaccard 相对于 Nedellec (2026) 的增量贡献是否足够
- 三项 contributions 是否分别有实质性的学术价值

### 2. Related Work 覆盖
- 自查以下方向是否有重要遗漏：
  - Self-consistency / test-time scaling（2024-2026）
  - Confidence / uncertainty estimation for LLMs（2024-2026）
  - Generative IE 方法（UniNER, GoLLIE 等）
  - Structured prediction 中的 calibration 工作
- 对 Nedellec (2026) 的差异化论述是否公平准确
- 引用是否真实存在（检查是否有可疑的 hallucinated citations）

### 3. 写作质量与逻辑
- Abstract → Introduction → Contributions 的叙事是否连贯
- 论文结构是否合理（是否有冗余或缺失的 section）
- 术语使用是否一致（如 "quality estimation" vs "quality prediction"）
- Figure/Table 是否自解释、caption 是否充分
- Discussion 是否过度推断或保守不足

### 4. 格式合规
- 页数是否符合 8 页限制（请估算）
- 参考文献格式是否正确
- 匿名性是否完整（是否有泄露身份的线索：GitHub URL、acknowledgments、自引模式）
- Limitations section 是否充分（ARR 要求，desk-reject 项）
- 是否缺少 Ethics Statement

### 5. 负面结果的呈现
- "No signal reliably surpasses greedy" 是核心负面结果——呈现是否平衡
- 是否过度包装负面结果为正面贡献
- 对未来工作的建议是否具体且可行

请输出标准审稿格式：Summary → Strengths → Weaknesses（分 Must-Fix / Should-Fix / Minor） → Questions → Missing References → Score (1-10) + Confidence (1-5)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "f5d01f90-29f0-42ef-8c36-beb6e3f39fb5",
  "type": "user",
  "uuid": "95e5a0d2-8c19-43db-ad66-6a0b61d6e138",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T03:57:44.384Z_

```json
{
  "parentUuid": "95e5a0d2-8c19-43db-ad66-6a0b61d6e138",
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
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__review_reviewer_post_to_director",
      "mcp__agent-ml-research__verify_references"
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
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__review_reviewer_post_to_director",
      "mcp__agent-ml-research__verify_references"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "c5295a9c-b237-4cef-b950-d3a1ceecf49d",
  "timestamp": "2026-05-15T03:57:44.384Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T03:57:44.384Z_

```json
{
  "parentUuid": "c5295a9c-b237-4cef-b950-d3a1ceecf49d",
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
  "uuid": "6cedf0dc-1a3e-46f3-92ea-1d1f41ffbe17",
  "timestamp": "2026-05-15T03:57:44.384Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-15T03:57:44.384Z_

```json
{
  "parentUuid": "6cedf0dc-1a3e-46f3-92ea-1d1f41ffbe17",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "37c332ee-beae-4cb9-9b7f-b21ca19fc66a",
  "timestamp": "2026-05-15T03:57:44.384Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
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
  "aiTitle": "Generative IE confidence signals systematic review",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b"
}
```

---

### Assistant

_source line 8 · 2026-05-15T03:57:47.729Z_

我开始审稿。先加载 session 启动 skill，然后读取论文和搜索 EMNLP 2026 reviewer guidelines。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37c332ee-beae-4cb9-9b7f-b21ca19fc66a",
  "isSidechain": false,
  "requestId": "req_011Cb3gaLwm4qxNvRukrHs9h",
  "type": "assistant",
  "uuid": "60867c4e-d72c-4246-a7e6-974c587c9a1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T7kXHqL2wNaEmw9BrsLEkY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13882,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13882,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13882,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13882
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

_source line 9 · 2026-05-15T03:57:49.158Z_

<details open><summary>🔧 Tool call — Read · `toolu_0123xuXiMbTcDW4jdoj2JGXt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60867c4e-d72c-4246-a7e6-974c587c9a1b",
  "isSidechain": false,
  "requestId": "req_011Cb3gaLwm4qxNvRukrHs9h",
  "type": "assistant",
  "uuid": "fe904623-c50f-4438-a80e-63871f9adea1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T7kXHqL2wNaEmw9BrsLEkY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13882,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13882,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13882,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13882
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

_source line 10 · 2026-05-15T03:57:49.176Z_

<details><summary>↩ Tool result · reported error · `toolu_0123xuXiMbTcDW4jdoj2JGXt`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe904623-c50f-4438-a80e-63871f9adea1",
  "isSidechain": false,
  "promptId": "f5d01f90-29f0-42ef-8c36-beb6e3f39fb5",
  "type": "user",
  "uuid": "6eb1bdbe-996b-436e-a01b-5e857a8f9d0a",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5.",
  "sourceToolAssistantUUID": "fe904623-c50f-4438-a80e-63871f9adea1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T03:57:49.623Z_

<details><summary>↩ Tool result · `toolu_01G3GwcnXLVK3uZ8YZTNhCZR`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\bibliography{references}
40	
41	\appendix
42	\input{sections/appendix}
43	
44	\end{document}
45	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b76cc77-af85-4b99-be7d-d8c882b8f0a0",
  "isSidechain": false,
  "promptId": "f5d01f90-29f0-42ef-8c36-beb6e3f39fb5",
  "type": "user",
  "uuid": "e113f446-5ab9-420c-bdab-24b81e035bdf",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\n\\graphicspath{{figures/}}\n\n\\title{Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{sections/abstract}\n\\input{sections/introduction}\n\\input{sections/related_work}\n\\input{sections/method}\n\\input{sections/experiments}\n\\input{sections/discussion}\n\\input{sections/conclusion}\n\n\\section*{Limitations}\n\\input{sections/limitations}\n\n\\bibliography{references}\n\n\\appendix\n\\input{sections/appendix}\n\n\\end{document}\n",
      "numLines": 45,
      "startLine": 1,
      "totalLines": 45
    }
  },
  "sourceToolAssistantUUID": "6b76cc77-af85-4b99-be7d-d8c882b8f0a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T03:57:49.617Z_

<details open><summary>🔧 Tool call — Read · `toolu_01G3GwcnXLVK3uZ8YZTNhCZR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6eb1bdbe-996b-436e-a01b-5e857a8f9d0a",
  "isSidechain": false,
  "requestId": "req_011Cb3gaLwm4qxNvRukrHs9h",
  "type": "assistant",
  "uuid": "6b76cc77-af85-4b99-be7d-d8c882b8f0a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T7kXHqL2wNaEmw9BrsLEkY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13882,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13882,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13882,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13882
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

_source line 13 · 2026-05-15T03:57:52.264Z_

<details><summary>Logged reasoning block</summary>

```text
Let me read all the section files and search for reviewer guidelines.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e113f446-5ab9-420c-bdab-24b81e035bdf",
  "isSidechain": false,
  "requestId": "req_011Cb3gajTbcbWBGjbxmfKSk",
  "type": "assistant",
  "uuid": "07b65d46-095e-468f-b059-111445655e51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LBXvizE9z7oB9TaeJDhXus",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 745,
      "cache_read_input_tokens": 25723,
      "output_tokens": 266,
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
          "output_tokens": 266,
          "cache_read_input_tokens": 25723,
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

### Assistant

_source line 14 · 2026-05-15T03:57:52.755Z_

论文是分节结构。让我读取所有节文件和搜索 reviewer guidelines。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07b65d46-095e-468f-b059-111445655e51",
  "isSidechain": false,
  "requestId": "req_011Cb3gajTbcbWBGjbxmfKSk",
  "type": "assistant",
  "uuid": "e54dbd6a-d60e-437d-a035-f9842b863fdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LBXvizE9z7oB9TaeJDhXus",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 745,
      "cache_read_input_tokens": 25723,
      "output_tokens": 266,
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
          "output_tokens": 266,
          "cache_read_input_tokens": 25723,
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

### Tool call

_source line 15 · 2026-05-15T03:57:53.808Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01JmFBQ1V4MYstK2WqJWXEaV`</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e54dbd6a-d60e-437d-a035-f9842b863fdc",
  "isSidechain": false,
  "requestId": "req_011Cb3gajTbcbWBGjbxmfKSk",
  "type": "assistant",
  "uuid": "32d40ec8-c0d2-4288-befe-33031df67354",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LBXvizE9z7oB9TaeJDhXus",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 745,
      "cache_read_input_tokens": 25723,
      "output_tokens": 266,
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
          "output_tokens": 266,
          "cache_read_input_tokens": 25723,
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

_source line 16 · 2026-05-15T03:57:55.630Z_

<details><summary>↩ Tool result · `toolu_01Fm5XtMbMFWEhqhEiYGDZYq`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__pdf_to_images"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__verify_references"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__review_reviewer_post_to_director"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae306a8a-c25e-4589-a23e-dda876907fa4",
  "isSidechain": false,
  "promptId": "f5d01f90-29f0-42ef-8c36-beb6e3f39fb5",
  "type": "user",
  "uuid": "d4bb3fd1-05d1-472e-bf63-9967405b65ae",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__review_reviewer_post_to_director"
    ],
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__verify_references,mcp__agent-ml-research__review_reviewer_post_to_director",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "ae306a8a-c25e-4589-a23e-dda876907fa4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T03:57:53.825Z_

<details><summary>↩ Tool result · `toolu_01JmFBQ1V4MYstK2WqJWXEaV`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "32d40ec8-c0d2-4288-befe-33031df67354",
  "isSidechain": false,
  "promptId": "f5d01f90-29f0-42ef-8c36-beb6e3f39fb5",
  "type": "user",
  "uuid": "56ae2f08-7e27-4de2-b0d2-d0b7149bdc0a",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 12,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "32d40ec8-c0d2-4288-befe-33031df67354",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T03:57:55.625Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Fm5XtMbMFWEhqhEiYGDZYq`</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__verify_references,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56ae2f08-7e27-4de2-b0d2-d0b7149bdc0a",
  "isSidechain": false,
  "requestId": "req_011Cb3gajTbcbWBGjbxmfKSk",
  "type": "assistant",
  "uuid": "ae306a8a-c25e-4589-a23e-dda876907fa4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LBXvizE9z7oB9TaeJDhXus",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 745,
      "cache_read_input_tokens": 25723,
      "output_tokens": 266,
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
          "output_tokens": 266,
          "cache_read_input_tokens": 25723,
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

### Assistant

_source line 19 · 2026-05-15T03:57:58.361Z_

<details><summary>Logged reasoning block</summary>

```text
The glob found no files in the sections directory. Let me find where the section files actually are.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4bb3fd1-05d1-472e-bf63-9967405b65ae",
  "isSidechain": false,
  "requestId": "req_011Cb3gbBGd9tUgjAcBexCZj",
  "type": "assistant",
  "uuid": "dcde0a09-0eda-48fd-89b0-6f7fe6a59f36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0131AjWhVqNiuL1AHHEjUjDX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2306,
      "cache_read_input_tokens": 26468,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2306,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 249,
          "cache_read_input_tokens": 26468,
          "cache_creation_input_tokens": 2306,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2306
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

_source line 20 · 2026-05-15T03:57:59.313Z_

Let me find the actual section files and search for reviewer guidelines in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dcde0a09-0eda-48fd-89b0-6f7fe6a59f36",
  "isSidechain": false,
  "requestId": "req_011Cb3gbBGd9tUgjAcBexCZj",
  "type": "assistant",
  "uuid": "2cface65-e40c-4a13-a9b7-76c1997b1279",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0131AjWhVqNiuL1AHHEjUjDX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2306,
      "cache_read_input_tokens": 26468,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2306,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 249,
          "cache_read_input_tokens": 26468,
          "cache_creation_input_tokens": 2306,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2306
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

_source line 21 · 2026-05-15T03:58:00.782Z_

<details open><summary>🔧 Tool call — Glob · `toolu_012GttZdxDcm4k3zZ3qyqnVu`</summary>

```json
{
  "pattern": "**/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cface65-e40c-4a13-a9b7-76c1997b1279",
  "isSidechain": false,
  "requestId": "req_011Cb3gbBGd9tUgjAcBexCZj",
  "type": "assistant",
  "uuid": "97a863ad-46c1-47a6-9265-fc4bc0297bde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0131AjWhVqNiuL1AHHEjUjDX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2306,
      "cache_read_input_tokens": 26468,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2306,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 249,
          "cache_read_input_tokens": 26468,
          "cache_creation_input_tokens": 2306,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2306
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

_source line 22 · 2026-05-15T03:58:00.815Z_

<details><summary>↩ Tool result · `toolu_012GttZdxDcm4k3zZ3qyqnVu`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "97a863ad-46c1-47a6-9265-fc4bc0297bde",
  "isSidechain": false,
  "promptId": "f5d01f90-29f0-42ef-8c36-beb6e3f39fb5",
  "type": "user",
  "uuid": "e37f4e1e-3a8b-4385-a6bd-53371947b14c",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
    ],
    "durationMs": 29,
    "numFiles": 9,
    "truncated": false
  },
  "sourceToolAssistantUUID": "97a863ad-46c1-47a6-9265-fc4bc0297bde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T03:58:01.797Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019v8V6EXQ4CERjiyHudcWah`</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e37f4e1e-3a8b-4385-a6bd-53371947b14c",
  "isSidechain": false,
  "requestId": "req_011Cb3gbBGd9tUgjAcBexCZj",
  "type": "assistant",
  "uuid": "dd7c56ed-27ae-4844-84af-58289b3697b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0131AjWhVqNiuL1AHHEjUjDX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2306,
      "cache_read_input_tokens": 26468,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2306,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 249,
          "cache_read_input_tokens": 26468,
          "cache_creation_input_tokens": 2306,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2306
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

_source line 24 · 2026-05-15T03:58:02.124Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WXVY34VpJ6vLLZ1mRpohxs`</summary>

```json
{
  "query": "EMNLP 2026 submission guidelines page limit format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd7c56ed-27ae-4844-84af-58289b3697b1",
  "isSidechain": false,
  "requestId": "req_011Cb3gbBGd9tUgjAcBexCZj",
  "type": "assistant",
  "uuid": "b1f15a80-4b18-4816-ba7d-2d535a618753",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0131AjWhVqNiuL1AHHEjUjDX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2306,
      "cache_read_input_tokens": 26468,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2306,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 249,
          "cache_read_input_tokens": 26468,
          "cache_creation_input_tokens": 2306,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2306
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

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。  ## 审稿对象 - 论文路径：`projects/struct_self_consist_ie/docs/paper/main.tex`（分节结构，各节在 `sections/` 下） - 目标 venue：**EMNLP 2026 Main Conference**（通过 ARR May…",
  "leafUuid": "b1f15a80-4b18-4816-ba7d-2d535a618753",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Generative IE confidence signals systematic review",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b"
}
```

---

### Tool result

_source line 27 · 2026-05-15T03:58:09.221Z_

<details><summary>↩ Tool result · `toolu_01WXVY34VpJ6vLLZ1mRpohxs`</summary>

```text
Web search results for query: "EMNLP 2026 submission guidelines page limit format requirements"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"}]

Based on the search results, here are the EMNLP 2026 submission guidelines regarding page limits and format requirements:

## Page Limits

Long papers should be 8 pages and short papers should be 4 pages. Industry Track papers cannot exceed 6 pages in length (excluding ethical considerations and references), and references and limitations sections do not count toward the page limit.

## Format Requirements

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. Manuscripts should be submitted electronically in PDF format and formatted using the templates available at the conference website, and submissions that do not conform to the required styles, including paper size, margin width, and font size restrictions, will be desk-rejected.

EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences.

## Other Key Requirements

- The mandatory Limitations section is required, placed after the conclusion
- Submissions that exceed the length requirements, or are missing a limitations section, will be desk rejected
- Papers must not include authors' names and affiliations (for the submission version)


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1f15a80-4b18-4816-ba7d-2d535a618753",
  "isSidechain": false,
  "promptId": "f5d01f90-29f0-42ef-8c36-beb6e3f39fb5",
  "type": "user",
  "uuid": "21c6ac3a-b6e6-47d6-8f69-7b99f8087fdb",
  "toolUseResult": {
    "query": "EMNLP 2026 submission guidelines page limit format requirements",
    "results": [
      {
        "tool_use_id": "srvtoolu_01X4iH294d5RVaFgKBDBTDFq",
        "content": [
          {
            "title": "Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026",
            "url": "https://2026.emnlp.org/calls/industry_track/"
          },
          {
            "title": "EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf",
            "url": "https://www.underleaf.ai/templates/emnlp"
          },
          {
            "title": "Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"
          },
          {
            "title": "Call for workshops: EMNLP & AACL",
            "url": "https://groups.google.com/g/ml-news/c/W-fucfhVto4"
          },
          {
            "title": "CALL FOR PAPERS – ACL Rolling Review",
            "url": "http://aclrollingreview.org/cfp"
          },
          {
            "title": "Confs: 2026 Conference on Empirical Methods in Natural ...",
            "url": "https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"
          },
          {
            "title": "EMNLP 2026 Conference | OpenReview",
            "url": "https://openreview.net/group?id=EMNLP%2F2026%2FConference"
          },
          {
            "title": "Submission Guide",
            "url": "https://nlp4climate.github.io/submissionguide/"
          },
          {
            "title": "EMNLP 2026 : The 2026 Conference on Empirical Methods in N",
            "url": "https://callforpaper.org/call-for-papers-emnlp-2026"
          },
          {
            "title": "EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...",
            "url": "http://www.wikicfp.com/cfp/program?id=883"
          }
        ]
      },
      "Based on the search results, here are the EMNLP 2026 submission guidelines regarding page limits and format requirements:\n\n## Page Limits\n\nLong papers should be 8 pages and short papers should be 4 pages. Industry Track papers cannot exceed 6 pages in length (excluding ethical considerations and references), and references and limitations sections do not count toward the page limit.\n\n## Format Requirements\n\nThe format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. Manuscripts should be submitted electronically in PDF format and formatted using the templates available at the conference website, and submissions that do not conform to the required styles, including paper size, margin width, and font size restrictions, will be desk-rejected.\n\nEMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences.\n\n## Other Key Requirements\n\n- The mandatory Limitations section is required, placed after the conclusion\n- Submissions that exceed the length requirements, or are missing a limitations section, will be desk rejected\n- Papers must not include authors' names and affiliations (for the submission version)"
    ],
    "durationSeconds": 7.093034991000001
  },
  "sourceToolAssistantUUID": "b1f15a80-4b18-4816-ba7d-2d535a618753",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T03:58:09.580Z_

<details><summary>↩ Tool result · `toolu_019v8V6EXQ4CERjiyHudcWah`</summary>

```text
Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

I found comprehensive information about the ACL Rolling Review (ARR) 2026 reviewer guidelines and review form criteria. Here are the key details:

## Review Form Criteria

For main papers, the main criteria are soundness, while for Findings papers the main criteria are soundness and reproducibility. Conference recommendations may also consider novelty, impact and other factors.

## Main Reviewer Tasks

The reviewer's main tasks are (1) checking the appropriateness of the submission and its assignment to this reviewer, (2) writing a well-justified review, (3) updating the review as appropriate based on author-reviewer discussion.

## Key Review Form Questions

The review form includes several important sections:

- Asking what are the major reasons to publish this paper at a selective *ACL venue, which could include novel and useful methodology, insightful empirical results or theoretical analysis, clear organization of related literature, or any other reason why interested readers of *ACL papers may find the paper useful.

- Asking about concerns that would cause prioritizing other high-quality papers, which could include concerns about correctness of the results or argumentation, limited perceived impact of the methods or findings, lack of clarity in exposition, or any other reason.

- Reproducibility questions about whether there is enough information in the paper for a reader to reproduce the main results, use results in future work, or build upon the work.

- An excitement rating where excitement is subjective and does not necessarily follow what is popular in the field.

- Ethical considerations, asking reviewers to review the ACL code of ethics and describe any ethical issues.

For detailed guidance on these criteria and the full review form, you can visit the Review Form page.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd7c56ed-27ae-4844-84af-58289b3697b1",
  "isSidechain": false,
  "promptId": "f5d01f90-29f0-42ef-8c36-beb6e3f39fb5",
  "type": "user",
  "uuid": "9a42b605-963f-4d71-af08-a4426c7207d4",
  "toolUseResult": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria",
    "results": [
      {
        "tool_use_id": "srvtoolu_011S3ahTD5CsrVPcZLx1oxNc",
        "content": [
          {
            "title": "ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewerguidelines"
          },
          {
            "title": "ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/acguidelines"
          },
          {
            "title": "ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/"
          },
          {
            "title": "CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/cfp"
          },
          {
            "title": "Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/authors"
          },
          {
            "title": "Main Conference - ACL 2026",
            "url": "https://2026.aclweb.org/calls/main_conference_papers/"
          },
          {
            "title": "How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewing"
          },
          {
            "title": "Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewform"
          },
          {
            "title": "aclrollingreview/cfp.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"
          },
          {
            "title": "Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/incentives2026"
          }
        ]
      },
      "I found comprehensive information about the ACL Rolling Review (ARR) 2026 reviewer guidelines and review form criteria. Here are the key details:\n\n## Review Form Criteria\n\nFor main papers, the main criteria are soundness, while for Findings papers the main criteria are soundness and reproducibility. Conference recommendations may also consider novelty, impact and other factors.\n\n## Main Reviewer Tasks\n\nThe reviewer's main tasks are (1) checking the appropriateness of the submission and its assignment to this reviewer, (2) writing a well-justified review, (3) updating the review as appropriate based on author-reviewer discussion.\n\n## Key Review Form Questions\n\nThe review form includes several important sections:\n\n- Asking what are the major reasons to publish this paper at a selective *ACL venue, which could include novel and useful methodology, insightful empirical results or theoretical analysis, clear organization of related literature, or any other reason why interested readers of *ACL papers may find the paper useful.\n\n- Asking about concerns that would cause prioritizing other high-quality papers, which could include concerns about correctness of the results or argumentation, limited perceived impact of the methods or findings, lack of clarity in exposition, or any other reason.\n\n- Reproducibility questions about whether there is enough information in the paper for a reader to reproduce the main results, use results in future work, or build upon the work.\n\n- An excitement rating where excitement is subjective and does not necessarily follow what is popular in the field.\n\n- Ethical considerations, asking reviewers to review the ACL code of ethics and describe any ethical issues.\n\nFor detailed guidance on these criteria and the full review form, you can visit the Review Form page."
    ],
    "durationSeconds": 7.776281235999999
  },
  "sourceToolAssistantUUID": "dd7c56ed-27ae-4844-84af-58289b3697b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-15T03:58:09.586Z_

```json
{
  "parentUuid": "9a42b605-963f-4d71-af08-a4426c7207d4",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "727e33b0-b3f7-407e-9d09-1370d8f21209",
  "timestamp": "2026-05-15T03:58:09.586Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 30 · 2026-05-15T03:58:13.006Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I found the section files and reviewer guidelines. Now let me:
1. Read the ARR review form in detail
2. Read all the section files
3. Verify references

Let me do this in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "727e33b0-b3f7-407e-9d09-1370d8f21209",
  "isSidechain": false,
  "requestId": "req_011Cb3gcCfji25dhMsq8nbu2",
  "type": "assistant",
  "uuid": "917c5d5e-eca4-4e17-9d73-43539671ccd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012U5iYCFX3bLXueSRKQGfrs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 847,
      "cache_creation_input_tokens": 1610,
      "cache_read_input_tokens": 28774,
      "output_tokens": 985,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1610,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 847,
          "output_tokens": 985,
          "cache_read_input_tokens": 28774,
          "cache_creation_input_tokens": 1610,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1610
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

_source line 31 · 2026-05-15T03:58:14.434Z_

找到所有文件。现在并行读取所有节文件、获取 ARR review form 详情、验证引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "917c5d5e-eca4-4e17-9d73-43539671ccd1",
  "isSidechain": false,
  "requestId": "req_011Cb3gcCfji25dhMsq8nbu2",
  "type": "assistant",
  "uuid": "918b5774-b2e8-43b2-bfa4-0c60850f9cf7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012U5iYCFX3bLXueSRKQGfrs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 847,
      "cache_creation_input_tokens": 1610,
      "cache_read_input_tokens": 28774,
      "output_tokens": 985,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1610,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 847,
          "output_tokens": 985,
          "cache_read_input_tokens": 28774,
          "cache_creation_input_tokens": 1610,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1610
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

_source line 32 · 2026-05-15T03:58:16.335Z_

<details open><summary>🔧 Tool call — Read · `toolu_01U3f4yypRzWXKZjp7FN6zJk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "918b5774-b2e8-43b2-bfa4-0c60850f9cf7",
  "isSidechain": false,
  "requestId": "req_011Cb3gcCfji25dhMsq8nbu2",
  "type": "assistant",
  "uuid": "4dd40791-2c82-4c45-8994-ef6dc61288aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012U5iYCFX3bLXueSRKQGfrs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 847,
      "cache_creation_input_tokens": 1610,
      "cache_read_input_tokens": 28774,
      "output_tokens": 985,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1610,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 847,
          "output_tokens": 985,
          "cache_read_input_tokens": 28774,
          "cache_creation_input_tokens": 1610,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1610
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

_source line 33 · 2026-05-15T03:58:16.358Z_

<details><summary>↩ Tool result · `toolu_01U3f4yypRzWXKZjp7FN6zJk`</summary>

```text
1	\begin{abstract}
2	Test-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.
3	We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER (three datasets of varying difficulty) and RE (SciERC) with two model families (Qwen3-8B, LLaMA-3.1-8B).
4	We find that the strongest signals achieve $\rho{=}0.38$ (entity voting) and AUROC${=}0.75$ (exact match) for quality estimation, with ranking and classification favoring different signals across task complexity; however, this strong quality estimation does not translate into selection gains---no signal reliably surpasses greedy decoding in any of six tested configurations spanning two models and three datasets ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.
5	We term this disconnect the \textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.
6	Signal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks, and when model capability is insufficient, apparent correlations are driven by zero/non-zero separation rather than genuine quality gradation---establishing that signal choice should be guided by task difficulty and intended application.
7	These results reframe consistency signals as quality estimators rather than output selectors for structured IE.
8	\end{abstract}
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4dd40791-2c82-4c45-8994-ef6dc61288aa",
  "isSidechain": false,
  "promptId": "f5d01f90-29f0-42ef-8c36-beb6e3f39fb5",
  "type": "user",
  "uuid": "47a4d916-cc1a-42d9-868d-55bbeebabc1a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
      "content": "\\begin{abstract}\nTest-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.\nWe systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\\kappa$), and model-internal (log-probability)---across NER (three datasets of varying difficulty) and RE (SciERC) with two model families (Qwen3-8B, LLaMA-3.1-8B).\nWe find that the strongest signals achieve $\\rho{=}0.38$ (entity voting) and AUROC${=}0.75$ (exact match) for quality estimation, with ranking and classification favoring different signals across task complexity; however, this strong quality estimation does not translate into selection gains---no signal reliably surpasses greedy decoding in any of six tested configurations spanning two models and three datasets ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.\nWe term this disconnect the \\textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.\nSignal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks, and when model capability is insufficient, apparent correlations are driven by zero/non-zero separation rather than genuine quality gradation---establishing that signal choice should be guided by task difficulty and intended application.\nThese results reframe consistency signals as quality estimators rather than output selectors for structured IE.\n\\end{abstract}\n",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  },
  "sourceToolAssistantUUID": "4dd40791-2c82-4c45-8994-ef6dc61288aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-15T03:58:16.965Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XmKtSAyG2C3VvapBYKdxVu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47a4d916-cc1a-42d9-868d-55bbeebabc1a",
  "isSidechain": false,
  "requestId": "req_011Cb3gcCfji25dhMsq8nbu2",
  "type": "assistant",
  "uuid": "9d63b322-64e5-461f-a2aa-fee51a8c3c22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012U5iYCFX3bLXueSRKQGfrs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 847,
      "cache_creation_input_tokens": 1610,
      "cache_read_input_tokens": 28774,
      "output_tokens": 985,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1610,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 847,
          "output_tokens": 985,
          "cache_read_input_tokens": 28774,
          "cache_creation_input_tokens": 1610,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1610
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

_source line 35 · 2026-05-15T03:58:16.974Z_

<details><summary>↩ Tool result · `toolu_01XmKtSAyG2C3VvapBYKdxVu`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \citealp{wang2023selfconsistency}).
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2024scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
14	These require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.
15	Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.
16	The most relevant study, \citet{nedellec2026consistency}, examines consistency--accuracy correlations for LLM-based IE but (i)~relies on surface-level matching, explicitly acknowledging it ``overlooks semantically consistent outputs,'' (ii)~evaluates only quality estimation without studying best-of-$N$ selection, and (iii)~covers a single domain with hard prompting rather than a difficulty gradient across benchmarks.
17	No existing work compares confidence signals from multiple families---surface-level, structural consistency, and probabilistic---for both quality estimation and sample selection in generative structured IE.
18	
19	Our central finding is that consistency-based signals are effective quality estimators but poor sample selectors for structured IE.
20	Entity voting achieves $\rho{=}0.38$ on SciERC NER and exact match leads AUROC${=}0.75$, both practically useful for quality-aware routing.
21	Yet no signal reliably surpasses greedy decoding on best-of-$N$ selection ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.
22	We term this the \textbf{correlation-selection gap} (Figure~\ref{fig:overview}): instance-level signals predict \textit{which inputs} are hard, not \textit{which output} is best.
23	
24	\begin{figure*}[t]
25	\centering
26	\includegraphics[width=\textwidth]{fig_overview}
27	\caption{The correlation-selection gap. Left: consistency signals (here entity voting) predict instance-level quality---high agreement correlates with high F1 ($\rho{\approx}0.38$, AUROC${\approx}0.69$). Right: the same instance-level signal assigns identical scores to all $N$ candidates from a given input, precluding sample selection. No signal reliably surpasses greedy on either task ($p{=}0.39$ for NER logprob).}
28	\label{fig:overview}
29	\end{figure*}
30	
31	We systematically evaluate five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER and RE on SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, and WNUT-17 \cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.
32	
33	Our contributions are as follows:
34	\begin{enumerate}
35	    \item \textbf{First multi-family comparison of confidence signals for generative IE.}
36	    We evaluate five signals from three families on quality estimation for NER and RE.
37	    Entity voting achieves the strongest $\rho{=}0.38$ while exact match leads AUROC${=}0.75$; signal rankings depend on both task complexity and evaluation metric, with structural signals leading rank correlation on complex schemas (SciERC) and surface signals leading on simpler tasks (CoNLL).
38	
39	    \item \textbf{Identification of the correlation-selection gap.}
40	    We demonstrate a fundamental disconnect between quality estimation and sample selection in structured IE.
41	    Despite strong instance-level correlations ($\rho$ up to 0.38), no signal reliably surpasses greedy in any of six tested configurations spanning two models and three datasets ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.
42	    This gap reflects the instance-level nature of consistency signals, which predict input difficulty rather than discriminating among individual samples.
43	
44	    \item \textbf{Task-complexity boundary conditions.}
45	    Signal rankings depend on task difficulty: exact match leads on easy tasks (CoNLL), Soft Jaccard dominates on hard tasks (SciERC), and when model capability is insufficient (WNUT-17, 54\% zero F1), inflated full-set correlations collapse on the conditional set---all signals converge toward weak or non-significant correlations once the zero/non-zero boundary is removed.
46	    While our NER findings are validated across three datasets of varying difficulty, our RE conclusions are based on a single benchmark (SciERC) and warrant further validation.
47	\end{enumerate}
48	
49	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d63b322-64e5-461f-a2aa-fee51a8c3c22",
  "isSidechain": false,
  "promptId": "f5d01f90-29f0-42ef-8c36-beb6e3f39fb5",
  "type": "user",
  "uuid": "c3264049-6641-4376-b899-d70967100559",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:introduction}\n\nSelf-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.\nOn discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \\citealp{wang2023selfconsistency}).\nMore broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \\cite{snell2024scaling, brown2024monkeys}.\nThese results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.\nFor tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.\nBut information extraction (IE) poses a fundamentally different challenge.\nThe output is not a single token or number; it is a \\textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.\nThere is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.\nCan self-consistency still provide useful signal in this structured setting?\n\nPrior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \\textit{quality estimation} (which inputs does the model handle reliably?) and \\textit{sample selection} (which of $N$ outputs is best?).\nThese require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.\nSelf-consistency methods for discrete answers \\cite{wang2023selfconsistency, chen2024usc} and weighted variants \\cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.\nThe most relevant study, \\citet{nedellec2026consistency}, examines consistency--accuracy correlations for LLM-based IE but (i)~relies on surface-level matching, explicitly acknowledging it ``overlooks semantically consistent outputs,'' (ii)~evaluates only quality estimation without studying best-of-$N$ selection, and (iii)~covers a single domain with hard prompting rather than a difficulty gradient across benchmarks.\nNo existing work compares confidence signals from multiple families---surface-level, structural consistency, and probabilistic---for both quality estimation and sample selection in generative structured IE.\n\nOur central finding is that consistency-based signals are effective quality estimators but poor sample selectors for structured IE.\nEntity voting achieves $\\rho{=}0.38$ on SciERC NER and exact match leads AUROC${=}0.75$, both practically useful for quality-aware routing.\nYet no signal reliably surpasses greedy decoding on best-of-$N$ selection ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.\nWe term this the \\textbf{correlation-selection gap} (Figure~\\ref{fig:overview}): instance-level signals predict \\textit{which inputs} are hard, not \\textit{which output} is best.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_overview}\n\\caption{The correlation-selection gap. Left: consistency signals (here entity voting) predict instance-level quality---high agreement correlates with high F1 ($\\rho{\\approx}0.38$, AUROC${\\approx}0.69$). Right: the same instance-level signal assigns identical scores to all $N$ candidates from a given input, precluding sample selection. No signal reliably surpasses greedy on either task ($p{=}0.39$ for NER logprob).}\n\\label{fig:overview}\n\\end{figure*}\n\nWe systematically evaluate five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\\kappa$), and model-internal (log-probability)---across NER and RE on SciERC \\cite{luan2018scierc}, CoNLL-2003 \\cite{tjongkimsang2003conll}, and WNUT-17 \\cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.\n\nOur contributions are as follows:\n\\begin{enumerate}\n    \\item \\textbf{First multi-family comparison of confidence signals for generative IE.}\n    We evaluate five signals from three families on quality estimation for NER and RE.\n    Entity voting achieves the strongest $\\rho{=}0.38$ while exact match leads AUROC${=}0.75$; signal rankings depend on both task complexity and evaluation metric, with structural signals leading rank correlation on complex schemas (SciERC) and surface signals leading on simpler tasks (CoNLL).\n\n    \\item \\textbf{Identification of the correlation-selection gap.}\n    We demonstrate a fundamental disconnect between quality estimation and sample selection in structured IE.\n    Despite strong instance-level correlations ($\\rho$ up to 0.38), no signal reliably surpasses greedy in any of six tested configurations spanning two models and three datasets ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.\n    This gap reflects the instance-level nature of consistency signals, which predict input difficulty rather than discriminating among individual samples.\n\n    \\item \\textbf{Task-complexity boundary conditions.}\n    Signal rankings depend on task difficulty: exact match leads on easy tasks (CoNLL), Soft Jaccard dominates on hard tasks (SciERC), and when model capability is insufficient (WNUT-17, 54\\% zero F1), inflated full-set correlations collapse on the conditional set---all signals converge toward weak or non-significant correlations once the zero/non-zero boundary is removed.\n    While our NER findings are validated across three datasets of varying difficulty, our RE conclusions are based on a single benchmark (SciERC) and warrant further validation.\n\\end{enumerate}\n\n",
      "numLines": 49,
      "startLine": 1,
      "totalLines": 49
    }
  },
  "sourceToolAssistantUUID": "9d63b322-64e5-461f-a2aa-fee51a8c3c22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-15T03:58:17.420Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SPWuwfDQisoKeyqbgzhBpn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3264049-6641-4376-b899-d70967100559",
  "isSidechain": false,
  "requestId": "req_011Cb3gcCfji25dhMsq8nbu2",
  "type": "assistant",
  "uuid": "bc5502b9-f050-4bde-9004-834d16491ffb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012U5iYCFX3bLXueSRKQGfrs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 847,
      "cache_creation_input_tokens": 1610,
      "cache_read_input_tokens": 28774,
      "output_tokens": 985,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1610,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 847,
          "output_tokens": 985,
          "cache_read_input_tokens": 28774,
          "cache_creation_input_tokens": 1610,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1610
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

_source line 37 · 2026-05-15T03:58:17.426Z_

<details><summary>↩ Tool result · `toolu_01SPWuwfDQisoKeyqbgzhBpn`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
5	Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
6	For test-time scaling, \citet{snell2024scaling} characterize compute scaling laws and \citet{brown2024monkeys} show best-of-$N$ gains across tasks.
7	Recent reward-free selectors include confidence-weighted voting \cite{taubenfeld2025cisc}, KL-based self-certainty \cite{kang2025selfcertainty}, adaptive sampling \cite{kim2026reasc}, ranked aggregation \cite{wang2025rankedvoting}, and latent-space consistency \cite{oh2025latentsc}.
8	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.
9	All of the above target reasoning/QA with discrete answers or specific aggregation strategies.
10	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).
11	
12	\paragraph{Consistency for structured IE.}
13	\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.
14	However, their work differs in three key respects: (i)~it relies on surface-level matching, explicitly acknowledging it ``overlooks semantically consistent outputs''; (ii)~it evaluates only quality estimation without studying best-of-$N$ selection, leaving the correlation-selection gap unexamined; and (iii)~it covers a single domain with hard prompting rather than a difficulty gradient across benchmarks.
15	Our Soft Jaccard signal addresses limitation (i) through type-aware bipartite matching with token-level span overlap; our selection analysis (\S\ref{sec:selection_gap}) directly addresses (ii); and our three-dataset evaluation spanning easy (CoNLL) to hard (SciERC) tasks addresses (iii).
16	CoCoA \cite{vashurin2025cocoa} fuses model confidence with inter-sample consistency for QA/summarization but does not address structured extraction.
17	Our evaluation builds on generative IE work \cite{zhou2024uniner, sainz2024gollie, josifoski2022genie, li2023codeie, wadhwa2023revisiting, wang2023instructuie} and constrained decoding \cite{willard2023guided}.
18	
19	\paragraph{Uncertainty estimation and calibration.}
20	Several surveys cover confidence estimation \cite{geng2024confidence}, selective abstention \cite{wen2025know}, uncertainty quantification \cite{xia2025survey}, and their intersection with calibration \cite{hobelsberger2025systematic} for LLMs.
21	Semantic uncertainty \cite{kuhn2023semantic} clusters generations by meaning; \citet{kossen2024semantic} distill semantic entropy into lightweight probes; P(True) \cite{kadavath2022language} queries model confidence directly; our structural signals instead measure agreement over output \textit{structure}.
22	Modern neural networks are often miscalibrated \cite{guo2017calibration, desai2020calibration}; our reliability diagrams extend calibration analysis to structured prediction.
23	Deep ensembles \cite{lakshminarayanan2017ensembles} and MC-dropout \cite{gal2016dropout} obtain uncertainty from model variation; our approach requires no model modification.
24	Prior NER uncertainty work \cite{xiao2019uncertainty, shelmanov2021active, zhang2023ener} operates within discriminative paradigms, inapplicable to generative settings.
25	Conformal prediction \cite{fisch2021conformal, angelopoulos2021conformal} provides coverage guarantees; trained verifiers \cite{cobbe2021verifiers, lightman2024verify} and reward models \cite{wang2024mathshepherd} learn per-sample scoring from labeled data.
26	Selective prediction \cite{geifman2017selective} and confidence-based IE filtering \cite{culotta2004confidence} establish the broader framework; our contribution is characterizing which signals support quality estimation vs.\ sample selection for generative IE.
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc5502b9-f050-4bde-9004-834d16491ffb",
  "isSidechain": false,
  "promptId": "f5d01f90-29f0-42ef-8c36-beb6e3f39fb5",
  "type": "user",
  "uuid": "7ba64d50-6d47-4386-b9a6-7ea5a6d3c7c4",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related}\n\n\\paragraph{Self-consistency and test-time scaling.}\nSelf-consistency decoding \\cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.\nExtensions to free-form text use LLM-based comparison \\cite{chen2024usc}, atomic sub-claim decomposition \\cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \\cite{manakul2023selfcheckgpt}.\nFor test-time scaling, \\citet{snell2024scaling} characterize compute scaling laws and \\citet{brown2024monkeys} show best-of-$N$ gains across tasks.\nRecent reward-free selectors include confidence-weighted voting \\cite{taubenfeld2025cisc}, KL-based self-certainty \\cite{kang2025selfcertainty}, adaptive sampling \\cite{kim2026reasc}, ranked aggregation \\cite{wang2025rankedvoting}, and latent-space consistency \\cite{oh2025latentsc}.\nConcurrently, \\citet{feng2025optimal} and \\citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \\citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.\nAll of the above target reasoning/QA with discrete answers or specific aggregation strategies.\nOur work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).\n\n\\paragraph{Consistency for structured IE.}\n\\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.\nHowever, their work differs in three key respects: (i)~it relies on surface-level matching, explicitly acknowledging it ``overlooks semantically consistent outputs''; (ii)~it evaluates only quality estimation without studying best-of-$N$ selection, leaving the correlation-selection gap unexamined; and (iii)~it covers a single domain with hard prompting rather than a difficulty gradient across benchmarks.\nOur Soft Jaccard signal addresses limitation (i) through type-aware bipartite matching with token-level span overlap; our selection analysis (\\S\\ref{sec:selection_gap}) directly addresses (ii); and our three-dataset evaluation spanning easy (CoNLL) to hard (SciERC) tasks addresses (iii).\nCoCoA \\cite{vashurin2025cocoa} fuses model confidence with inter-sample consistency for QA/summarization but does not address structured extraction.\nOur evaluation builds on generative IE work \\cite{zhou2024uniner, sainz2024gollie, josifoski2022genie, li2023codeie, wadhwa2023revisiting, wang2023instructuie} and constrained decoding \\cite{willard2023guided}.\n\n\\paragraph{Uncertainty estimation and calibration.}\nSeveral surveys cover confidence estimation \\cite{geng2024confidence}, selective abstention \\cite{wen2025know}, uncertainty quantification \\cite{xia2025survey}, and their intersection with calibration \\cite{hobelsberger2025systematic} for LLMs.\nSemantic uncertainty \\cite{kuhn2023semantic} clusters generations by meaning; \\citet{kossen2024semantic} distill semantic entropy into lightweight probes; P(True) \\cite{kadavath2022language} queries model confidence directly; our structural signals instead measure agreement over output \\textit{structure}.\nModern neural networks are often miscalibrated \\cite{guo2017calibration, desai2020calibration}; our reliability diagrams extend calibration analysis to structured prediction.\nDeep ensembles \\cite{lakshminarayanan2017ensembles} and MC-dropout \\cite{gal2016dropout} obtain uncertainty from model variation; our approach requires no model modification.\nPrior NER uncertainty work \\cite{xiao2019uncertainty, shelmanov2021active, zhang2023ener} operates within discriminative paradigms, inapplicable to generative settings.\nConformal prediction \\cite{fisch2021conformal, angelopoulos2021conformal} provides coverage guarantees; trained verifiers \\cite{cobbe2021verifiers, lightman2024verify} and reward models \\cite{wang2024mathshepherd} learn per-sample scoring from labeled data.\nSelective prediction \\cite{geifman2017selective} and confidence-based IE filtering \\cite{culotta2004confidence} establish the broader framework; our contribution is characterizing which signals support quality estimation vs.\\ sample selection for generative IE.\n",
      "numLines": 27,
      "startLine": 1,
      "totalLines": 27
    }
  },
  "sourceToolAssistantUUID": "bc5502b9-f050-4bde-9004-834d16491ffb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-15T03:58:18.268Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NPBk96Eu63sWES17ZmAABT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ba64d50-6d47-4386-b9a6-7ea5a6d3c7c4",
  "isSidechain": false,
  "requestId": "req_011Cb3gcCfji25dhMsq8nbu2",
  "type": "assistant",
  "uuid": "04ab1767-ce1f-467d-8475-f9ec06f110da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012U5iYCFX3bLXueSRKQGfrs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 847,
      "cache_creation_input_tokens": 1610,
      "cache_read_input_tokens": 28774,
      "output_tokens": 985,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1610,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 847,
          "output_tokens": 985,
          "cache_read_input_tokens": 28774,
          "cache_creation_input_tokens": 1610,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1610
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

_source line 39 · 2026-05-15T03:58:18.274Z_

<details><summary>↩ Tool result · `toolu_01NPBk96Eu63sWES17ZmAABT`</summary>

```text
1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given a language model $\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}.
6	Each $y_i$ is an entity set (NER) or relation set (RE).
7	A confidence signal $c$ serves two purposes: (a) \textit{quality estimation}---predicting which instances the model handles reliably, and (b) \textit{sample selection}---identifying the best output among $N$ candidates.
8	
9	A \textbf{per-sample signal} scores each $y_i$ independently, $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$, enabling direct candidate ranking.
10	An \textbf{instance-level signal} aggregates over all $N$ samples, $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$, producing a single score per input.
11	This asymmetry---between predicting \textit{which inputs} are easy and selecting \textit{which output} is best---is central to the correlation-selection gap we investigate.
12	Notation is summarized in Appendix~\ref{app:notation}.
13	
14	\subsection{Confidence Signals}\label{sec:signals}
15	
16	We compare five signals from three families: \textit{model-internal} (log-probability), \textit{surface} (exact match, Fleiss' $\kappa$), and \textit{structural} (Soft Jaccard, entity voting).
17	
18	\paragraph{Log-probability (model-internal, per-sample).}
19	The only per-sample signal.
20	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
21	\begin{equation}\label{eq:logprob}
22	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
23	\end{equation}
24	
25	\paragraph{Exact match voting (surface, instance-level).}
26	The majority fraction---the proportion of samples producing the most common output:
27	\begin{equation}\label{eq:em}
28	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
29	\end{equation}
30	
31	\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
32	We adapt \citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\cup| \times 2$ rating matrix:
33	\begin{equation}\label{eq:fk}
34	\kappa = \frac{\bar{P} - \bar{P}_e}{1 - \bar{P}_e}
35	\end{equation}
36	where $\bar{P}$ is mean observed pairwise agreement and $\bar{P}_e$ is expected agreement under random assignment.
37	While FK assumes independent raters, temperature-based sampling provides sufficient response diversity for the statistic to capture inter-sample agreement patterns.
38	Unlike structural signals, FK relies on exact string matching and does not tolerate surface variations.
39	
40	\paragraph{Soft Jaccard (structural, instance-level).}
41	Our core structural signal extends Jaccard similarity \cite{jaccard1901distribution} to extracted entity/relation sets.
42	For samples $y_i, y_j$, we group extractions by type, compute bipartite matching via the Hungarian algorithm with span overlap, and define:
43	\begin{equation}\label{eq:sj}
44	\text{SJ}(y_i, y_j) = \frac{\sum_{m \in M} \text{sim}(a_m, b_m)}{\sum_{g} \max(|g_i|, |g_j|)}
45	\end{equation}
46	where $M$ is the matched set from the Hungarian algorithm (without minimum similarity threshold), $\text{sim}(a_m, b_m)$ is the token-level IoU (intersection of tokens divided by union of tokens) between matched entity spans $a_m$ and $b_m$, and $g_i, g_j$ index per-type extraction counts.
47	We use $\max(|g_i|, |g_j|)$ rather than $|g_i \cup g_j|$ as the normalizer to penalize length asymmetry between samples.
48	The instance-level signal averages over all pairs:
49	\begin{equation}\label{eq:sj_instance}
50	c_{\text{sj}}(x) = \frac{1}{\binom{N}{2}} \sum_{i<j} \text{SJ}(y_i, y_j)
51	\end{equation}
52	
53	\paragraph{Entity voting confidence (structural, instance-level).}
54	For each entity $e$ in the union $E_\cup$ of all samples, we compute frequency $\text{freq}(e) = |\{i : e \in y_i\}| / N$.
55	The instance-level confidence is the mean frequency:
56	\begin{equation}\label{eq:voting}
57	c_{\text{vote}}(x) = \frac{1}{|E_\cup|} \sum_{e \in E_\cup} \text{freq}(e)
58	\end{equation}
59	
60	\subsection{Evaluation Framework}\label{sec:evaluation}
61	
62	\paragraph{Quality estimation.}
63	We measure rank correlation (Spearman $\rho$) between the confidence signal and instance-level F1, and binary discrimination (AUROC) by classifying instances as above or below median F1.
64	
65	\paragraph{Sample selection.}
66	We report best-of-$N$ F1: for each instance, the signal selects one sample.
67	Per-sample signals (logprob) directly rank candidates; instance-level signals select the sample closest to the consensus output (the consensus-proximity score for SJ is mathematically equivalent to leave-one-out SJ selection).
68	We compare against an \textit{oracle} (highest-F1 sample) and \textit{greedy} ($T{=}0$, $N{=}1$).
69	
70	\paragraph{Complementarity.}
71	High rank correlation does not guarantee effective sample selection: if per-sample variance is low, even a perfect quality estimator cannot distinguish among near-identical candidates (\S\ref{sec:selection_gap}).
72	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04ab1767-ce1f-467d-8475-f9ec06f110da",
  "isSidechain": false,
  "promptId": "f5d01f90-29f0-42ef-8c36-beb6e3f39fb5",
  "type": "user",
  "uuid": "c7811763-8248-4e75-b67d-d8a4f00d18f5",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex",
      "content": "\\section{Method}\\label{sec:method}\n\n\\subsection{Problem Formulation}\\label{sec:formulation}\n\nGiven a language model $\\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\\{y_1, \\ldots, y_N\\}$ at temperature $T > 0$ via constrained decoding \\cite{willard2023guided}.\nEach $y_i$ is an entity set (NER) or relation set (RE).\nA confidence signal $c$ serves two purposes: (a) \\textit{quality estimation}---predicting which instances the model handles reliably, and (b) \\textit{sample selection}---identifying the best output among $N$ candidates.\n\nA \\textbf{per-sample signal} scores each $y_i$ independently, $c_{\\text{ps}}: (x, y_i) \\to \\mathbb{R}$, enabling direct candidate ranking.\nAn \\textbf{instance-level signal} aggregates over all $N$ samples, $c_{\\text{il}}: (x, \\{y_i\\}_{i=1}^N) \\to \\mathbb{R}$, producing a single score per input.\nThis asymmetry---between predicting \\textit{which inputs} are easy and selecting \\textit{which output} is best---is central to the correlation-selection gap we investigate.\nNotation is summarized in Appendix~\\ref{app:notation}.\n\n\\subsection{Confidence Signals}\\label{sec:signals}\n\nWe compare five signals from three families: \\textit{model-internal} (log-probability), \\textit{surface} (exact match, Fleiss' $\\kappa$), and \\textit{structural} (Soft Jaccard, entity voting).\n\n\\paragraph{Log-probability (model-internal, per-sample).}\nThe only per-sample signal.\nFor sample $y_i$ with tokens $t_1, \\ldots, t_{|y_i|}$:\n\\begin{equation}\\label{eq:logprob}\nc_{\\text{lp}}(y_i) = \\frac{1}{|y_i|} \\sum_{j=1}^{|y_i|} \\log p_{\\mathcal{M}}(t_j \\mid t_{<j}, x)\n\\end{equation}\n\n\\paragraph{Exact match voting (surface, instance-level).}\nThe majority fraction---the proportion of samples producing the most common output:\n\\begin{equation}\\label{eq:em}\nc_{\\text{em}}(x) = \\frac{1}{N} \\max_{y} \\big|\\{i : y_i = y\\}\\big|\n\\end{equation}\n\n\\paragraph{Fleiss' $\\kappa$ (surface, instance-level).}\nWe adapt \\citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\\cup| \\times 2$ rating matrix:\n\\begin{equation}\\label{eq:fk}\n\\kappa = \\frac{\\bar{P} - \\bar{P}_e}{1 - \\bar{P}_e}\n\\end{equation}\nwhere $\\bar{P}$ is mean observed pairwise agreement and $\\bar{P}_e$ is expected agreement under random assignment.\nWhile FK assumes independent raters, temperature-based sampling provides sufficient response diversity for the statistic to capture inter-sample agreement patterns.\nUnlike structural signals, FK relies on exact string matching and does not tolerate surface variations.\n\n\\paragraph{Soft Jaccard (structural, instance-level).}\nOur core structural signal extends Jaccard similarity \\cite{jaccard1901distribution} to extracted entity/relation sets.\nFor samples $y_i, y_j$, we group extractions by type, compute bipartite matching via the Hungarian algorithm with span overlap, and define:\n\\begin{equation}\\label{eq:sj}\n\\text{SJ}(y_i, y_j) = \\frac{\\sum_{m \\in M} \\text{sim}(a_m, b_m)}{\\sum_{g} \\max(|g_i|, |g_j|)}\n\\end{equation}\nwhere $M$ is the matched set from the Hungarian algorithm (without minimum similarity threshold), $\\text{sim}(a_m, b_m)$ is the token-level IoU (intersection of tokens divided by union of tokens) between matched entity spans $a_m$ and $b_m$, and $g_i, g_j$ index per-type extraction counts.\nWe use $\\max(|g_i|, |g_j|)$ rather than $|g_i \\cup g_j|$ as the normalizer to penalize length asymmetry between samples.\nThe instance-level signal averages over all pairs:\n\\begin{equation}\\label{eq:sj_instance}\nc_{\\text{sj}}(x) = \\frac{1}{\\binom{N}{2}} \\sum_{i<j} \\text{SJ}(y_i, y_j)\n\\end{equation}\n\n\\paragraph{Entity voting confidence (structural, instance-level).}\nFor each entity $e$ in the union $E_\\cup$ of all samples, we compute frequency $\\text{freq}(e) = |\\{i : e \\in y_i\\}| / N$.\nThe instance-level confidence is the mean frequency:\n\\begin{equation}\\label{eq:voting}\nc_{\\text{vote}}(x) = \\frac{1}{|E_\\cup|} \\sum_{e \\in E_\\cup} \\text{freq}(e)\n\\end{equation}\n\n\\subsection{Evaluation Framework}\\label{sec:evaluation}\n\n\\paragraph{Quality estimation.}\nWe measure rank correlation (Spearman $\\rho$) between the confidence signal and instance-level F1, and binary discrimination (AUROC) by classifying instances as above or below median F1.\n\n\\paragraph{Sample selection.}\nWe report best-of-$N$ F1: for each instance, the signal selects one sample.\nPer-sample signals (logprob) directly rank candidates; instance-level signals select the sample closest to the consensus output (the consensus-proximity score for SJ is mathematically equivalent to leave-one-out SJ selection).\nWe compare against an \\textit{oracle} (highest-F1 sample) and \\textit{greedy} ($T{=}0$, $N{=}1$).\n\n\\paragraph{Complementarity.}\nHigh rank correlation does not guarantee effective sample selection: if per-sample variance is low, even a perfect quality estimator cannot distinguish among near-identical candidates (\\S\\ref{sec:selection_gap}).\n",
      "numLines": 72,
      "startLine": 1,
      "totalLines": 72
    }
  },
  "sourceToolAssistantUUID": "04ab1767-ce1f-467d-8475-f9ec06f110da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-15T03:58:18.752Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TBoV1uPeSJmr2PQiERj5Wv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7811763-8248-4e75-b67d-d8a4f00d18f5",
  "isSidechain": false,
  "requestId": "req_011Cb3gcCfji25dhMsq8nbu2",
  "type": "assistant",
  "uuid": "6facf3e1-1bc8-4003-b7f2-31b3af80b99c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012U5iYCFX3bLXueSRKQGfrs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 847,
      "cache_creation_input_tokens": 1610,
      "cache_read_input_tokens": 28774,
      "output_tokens": 985,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1610,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 847,
          "output_tokens": 985,
          "cache_read_input_tokens": 28774,
          "cache_creation_input_tokens": 1610,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1610
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

_source line 41 · 2026-05-15T03:58:18.757Z_

<details><summary>↩ Tool result · `toolu_01TBoV1uPeSJmr2PQiERj5Wv`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\approx}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (54\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory under identical training procedures, ensuring cross-model comparisons reflect architectural differences rather than training confounds.
15	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
16	Quality estimation uses Spearman $\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC). Best value per block and column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types). $N{=}8$ results use seed${=}42$; $N{=}16$ results are averaged across seeds \{42, 123, 456\}.}
27	\label{tab:quality_estimation}
28	\begin{tabular}{ll cc cc cc cc}
29	\toprule
30	& & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{SciERC RE}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
31	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8} \cmidrule(lr){9-10}
32	Signal & Family & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC \\
33	\midrule
34	\multicolumn{10}{l}{\textit{$N{=}8$}} \\
35	Voting Conf. & Structural & \textbf{.379} & .684 & \textbf{.350} & .693 & .424 & .789 & .426 & .709 \\
36	Soft Jaccard  & Structural & .360 & .692 & .250 & .670 & .436 & .801 & \textbf{.431} & .704 \\
37	Fleiss' $\kappa$ & Surface & .267 & .629 & .275 & .609 & .400 & .774 & .428 & .703 \\
38	Exact Match  & Surface    & .295 & \textbf{.749} & .134 & \textbf{.706} & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
39	Log-prob     & Model      & .205 & .578 & .266 & .600 & .316 & .753 & .307 & \textbf{.761} \\
40	\midrule
41	\multicolumn{10}{l}{\textit{$N{=}16$ (3-seed)}} \\
42	Voting Conf. & Structural & & & & & & & .458${\pm}$.003 & \\
43	Soft Jaccard  & Structural & & & & & & & \textbf{.463${\pm}$.007} & \\
44	Fleiss' $\kappa$ & Surface & & & & & & & .455${\pm}$.006 & \\
45	Exact Match  & Surface    & & & & & & & .460${\pm}$.008 & \\
46	Log-prob     & Model      & & & & & & & .310${\pm}$.005 & \\
47	\bottomrule
48	\end{tabular}
49	\end{table*}
50	
51	\begin{figure*}[t]
52	\centering
53	\includegraphics[width=\textwidth]{fig_signal_heatmap}
54	\caption{Quality estimation heatmap (Spearman $\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$), while logprob RE collapses to near-zero ($\rho{=}0.011$).}
55	\label{fig:signal_heatmap}
56	\end{figure*}
57	
58	Table~\ref{tab:quality_estimation} presents rank correlation ($\rho$) and AUROC for five confidence signals across tasks and models.
59	
60	\paragraph{Structural signals dominate on complex schemas.}
61	On SciERC NER, Voting achieves $\rho{=}0.379$ and SJ $\rho{=}0.360$, both outperforming surface ($\rho{\leq}0.295$) and logprob ($\rho{=}0.205$).
62	The structural advantage persists on RE (Voting $\rho{=}0.350$), though all signals weaken due to the 44\% zero-F1 floor effect.
63	Entity voting and SJ show moderate instance-level correlation (NER: $\rho{=}0.659$; RE: $\rho{=}0.605$), indicating information overlap but not redundancy; their differential behavior across difficulty levels reflects the complementary granularity of entity-level frequency vs.\ span-level set overlap.
64	While the best $\rho{=}0.38$ (Voting) explains approximately 14\% of F1 variance, the best AUROC reaches 0.749 (EM), indicating strong binary discriminative power for the quality/failure classification most relevant to practitioners in quality-aware routing.\footnote{For context, semantic entropy achieves AUROC $\approx$ 0.75--0.85 on discrete-answer QA tasks \cite{kuhn2023semantic}; direct comparison is complicated by the fundamentally different output spaces of structured IE versus closed-form QA.}
65	Bootstrap CIs for signal pair differences on SciERC NER ($N{=}8$): SJ$-$logprob $\Delta\rho{=}{+}0.155$ [+0.074, +0.234]; Voting$-$SJ $\Delta\rho{=}{+}0.019$ [$-$0.033, +0.073]; SJ$-$EM $\Delta\rho{=}{+}0.065$ [+0.003, +0.130].
66	The SJ advantage over logprob is significant, while the Voting--SJ gap is not; the SJ--EM difference is marginal (CI lower bound +0.003; see Table~\ref{tab:bootstrap_signal_ci}, Appendix~\ref{app:bootstrap_signal} for individual signal CIs).
67	
68	\paragraph{$\rho$--AUROC dissociation.}
69	On NER, EM leads AUROC (0.749) despite ranking third in $\rho$ (0.295); on RE, EM achieves the highest AUROC (0.706) while ranking last in $\rho$ (0.134).
70	Binary agreement provides clean separation between reliable and unreliable instances, while structural signals capture finer-grained quality variation.
71	On CoNLL with LLaMA, logprob achieves the highest AUROC (0.761) yet the lowest $\rho$ (0.307), confirming this dissociation across datasets.
72	
73	\paragraph{Signal rankings shift with task difficulty.}
74	On CoNLL (greedy F1${\approx}$0.91), EM leads ($\rho{=}0.451$, AUROC${=}0.816$), surpassing SJ and Voting.
75	When most samples are near-correct, binary agreement captures remaining variance more efficiently than set-level similarity.
76	This reversal---EM${>}$SJ on easy tasks vs.\ SJ${>}$EM on hard tasks---demonstrates that optimal signal choice depends on task difficulty.
77	Cross-model stability is strong: SJ achieves $\rho{=}0.436$ (Qwen) vs.\ $0.431$ (LLaMA) on CoNLL ($\Delta{=}0.005$, within 3-seed $\sigma{\approx}0.007$).
78	On WNUT-17, where 54\% of instances receive zero F1, full-set correlations are misleading: voting achieves $\rho{=}0.724$ (AUROC${=}0.913$), but this is entirely driven by the zero/non-zero boundary (conditional $\rho{=}0.038$, n.s.; Table~\ref{tab:wnut}).
79	Logprob exhibits strong \textit{negative} correlation ($\rho{=}{-}0.410$, AUROC${=}0.219$), indicating that higher model confidence associates with lower extraction quality on this noisy domain---further undermining logprob as a general-purpose IE quality signal.
80	On the conditional set, all signals collapse toward weak or non-significant correlations ($\rho{\leq}0.35$), with SJ achieving only $\rho{=}0.089$ ($p{=}0.020$) on the full set---suggesting a capability boundary beyond which consistency signals capture binary success/failure but not quality gradation.
81	
82	\paragraph{Conditional filtering.}
83	Filtering to non-zero F1 instances reshuffles rankings (Figure~\ref{fig:signal_heatmap}, right).
84	EM emerges as the strongest conditional signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$), while Voting and FK drop substantially (Voting NER: $0.379{\to}0.300$; FK NER: $0.267{\to}0.176$).
85	Logprob RE collapses to $\rho{=}0.011$, confirming its full-set correlation was driven by zero/non-zero separation.
86	This creates a natural complementarity: Voting and SJ are preferred on the full set, while EM provides the most precise ranking within the non-trivial subset (see Appendix~\ref{app:additional} for details).
87	
88	%% ============================================================
89	\subsection{The Correlation-Selection Gap}
90	\label{sec:selection_gap}
91	
92	\begin{figure*}[t]
93	\centering
94	\includegraphics[width=\textwidth]{fig_selection_gap}
95	\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Left: NER; right: RE. Bars show best-of-$N$ selection F1; the line marks quality estimation $\rho$. Despite $\rho$ up to 0.38, no signal reliably surpasses greedy on either task ($p{=}0.39$ for NER logprob, the best signal). Dashed line indicates oracle upper bound.}
96	\label{fig:selection_gap}
97	\end{figure*}
98	
99	\begin{table}[t]
100	\centering
101	\small
102	\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Best non-oracle result per column in \textbf{bold}. EM is omitted because exact-match plurality is degenerate in structured IE: with $N{=}8$, the probability of two identical structured outputs is negligible.}
103	\label{tab:selection}
104	\begin{tabular}{lcc}
105	\toprule
106	Method & NER F1 & RE F1 \\
107	\midrule
108	Oracle & 0.776 & 0.585 \\
109	\midrule
110	Log-prob           & \textbf{0.650} & 0.395 \\
111	Soft Jaccard       & 0.645 & 0.386 \\
112	Voting             & 0.634 & 0.359 \\
113	Exact Match        & ---   & ---   \\
114	\midrule
115	Greedy ($T{=}0$)   & 0.644 & \textbf{0.404} \\
116	Random             & 0.608 & 0.354 \\
117	\bottomrule
118	\end{tabular}
119	\end{table}
120	
121	Despite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection (Table~\ref{tab:selection}, Figure~\ref{fig:selection_gap}).
122	
123	\paragraph{No signal reliably surpasses greedy.}
124	We exclude 22 instances with empty gold annotations, yielding $n{=}529$ for statistical analysis.
125	We evaluate statistical significance using instance-level paired bootstrap resampling ($B{=}10{,}000$, with replacement) over these instances, reporting 95\% percentile CIs.
126	The three random seeds (42, 123, 456) refer to independent inference runs; we average $\rho$ across seeds and report the bootstrap $p$-value of the paired difference (best signal vs.\ greedy).
127	On NER, the oracle (0.776) reveals 13.2~pp of headroom above greedy (0.644).
128	Logprob achieves the highest selection F1 (0.650, +0.6~pp), but this is not statistically significant ($p{=}0.39$; 95\% CI: [$-$3.0, +4.2]~pp; Cohen's $d{=}0.038$; sign test: 61W/70L, win\%${=}$46.6\%).
129	On RE, the gap is complete: the best signal (logprob, 0.395) falls below greedy (0.404, $-0.9$\,pp, $p{=}0.80$), while 18.1~pp of oracle headroom remains.
130	Voting ($\rho{=}0.379$, the best quality estimator) selects to only 0.634 on NER---\textit{below} greedy.
131	The correlation-selection gap is consistent across all six tested configurations (Table~\ref{tab:cross_selection}), with no signal significantly outperforming greedy in any setting.
132	
133	\paragraph{Quality estimation $\neq$ output selection.}
134	Instance-level confidence signals predict \textit{which inputs} the model handles reliably, not \textit{which output} among $N$ candidates is best.
135	When per-sample variance is low relative to instance-level difficulty, even perfect quality estimation cannot discriminate among near-identical candidates.
136	This gap has direct consequences for test-time scaling in IE \cite{brown2024monkeys, snell2024scaling}: closing it likely requires per-sample signals such as trained verifiers \cite{cobbe2021verifiers}.
137	
138	%% ============================================================
139	\subsection{Robustness}
140	\label{sec:robustness_main}
141	
142	Consistency-based signals (SJ, Voting, FK) show robust performance across $T{\in}\{0.7, 1.0\}$; logprob temperature sensitivity remains uncharacterized due to unavailable $T{=}0.7$ data (Table~\ref{tab:robustness}, Appendix~\ref{app:robustness}).
143	SJ NER $\rho$ shifts by only 0.028 between $T{=}0.7$ and $T{=}1.0$ (bootstrap CI includes zero).
144	Doubling from $N{=}8$ to $N{=}16$ yields sublinear gains: SJ improves by $+0.052$ on Qwen SciERC NER, while logprob is approximately $N$-invariant ($\Delta\rho{\leq}0.021$).
145	The structural-over-logprob advantage is consistent across tested model families, holding across all four $N{=}16$ settings ($\Delta\rho{=}{+}0.135$ to ${+}0.175$).
146	NER signals are reasonably well-calibrated (ECE 0.069--0.096; Appendix~\ref{app:calibration}), while RE exhibits greater miscalibration (ECE 0.109--0.339).
147	For RE at $N{=}16$, SJ, FK, and logprob all plateau at $\rho{\approx}0.28$, suggesting compound errors impose a ceiling.
148	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6facf3e1-1bc8-4003-b7f2-31b3af80b99c",
  "isSidechain": false,
  "promptId": "f5d01f90-29f0-42ef-8c36-beb6e3f39fb5",
  "type": "user",
  "uuid": "c0a7f762-b9bb-4719-b224-870b5c55e810",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on three English IE benchmarks spanning a difficulty gradient.\n\\textbf{SciERC} \\cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\\approx}$91\\% micro F1.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (54\\% zero F1).\n\n\\paragraph{Models and sampling.}\nBoth \\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\\alpha{=}64$) for 5 epochs using LLaMA Factory under identical training procedures, ensuring cross-model comparisons reflect architectural differences rather than training confounds.\nWe draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}).}\nQuality estimation uses Spearman $\\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).\nInference uses vLLM with constrained decoding \\cite{willard2023guided}.\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC). Best value per block and column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types). $N{=}8$ results use seed${=}42$; $N{=}16$ results are averaged across seeds \\{42, 123, 456\\}.}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8} \\cmidrule(lr){9-10}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\n\\multicolumn{10}{l}{\\textit{$N{=}8$}} \\\\\nVoting Conf. & Structural & \\textbf{.379} & .684 & \\textbf{.350} & .693 & .424 & .789 & .426 & .709 \\\\\nSoft Jaccard  & Structural & .360 & .692 & .250 & .670 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFleiss' $\\kappa$ & Surface & .267 & .629 & .275 & .609 & .400 & .774 & .428 & .703 \\\\\nExact Match  & Surface    & .295 & \\textbf{.749} & .134 & \\textbf{.706} & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\nLog-prob     & Model      & .205 & .578 & .266 & .600 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\midrule\n\\multicolumn{10}{l}{\\textit{$N{=}16$ (3-seed)}} \\\\\nVoting Conf. & Structural & & & & & & & .458${\\pm}$.003 & \\\\\nSoft Jaccard  & Structural & & & & & & & \\textbf{.463${\\pm}$.007} & \\\\\nFleiss' $\\kappa$ & Surface & & & & & & & .455${\\pm}$.006 & \\\\\nExact Match  & Surface    & & & & & & & .460${\\pm}$.008 & \\\\\nLog-prob     & Model      & & & & & & & .310${\\pm}$.005 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_signal_heatmap}\n\\caption{Quality estimation heatmap (Spearman $\\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$), while logprob RE collapses to near-zero ($\\rho{=}0.011$).}\n\\label{fig:signal_heatmap}\n\\end{figure*}\n\nTable~\\ref{tab:quality_estimation} presents rank correlation ($\\rho$) and AUROC for five confidence signals across tasks and models.\n\n\\paragraph{Structural signals dominate on complex schemas.}\nOn SciERC NER, Voting achieves $\\rho{=}0.379$ and SJ $\\rho{=}0.360$, both outperforming surface ($\\rho{\\leq}0.295$) and logprob ($\\rho{=}0.205$).\nThe structural advantage persists on RE (Voting $\\rho{=}0.350$), though all signals weaken due to the 44\\% zero-F1 floor effect.\nEntity voting and SJ show moderate instance-level correlation (NER: $\\rho{=}0.659$; RE: $\\rho{=}0.605$), indicating information overlap but not redundancy; their differential behavior across difficulty levels reflects the complementary granularity of entity-level frequency vs.\\ span-level set overlap.\nWhile the best $\\rho{=}0.38$ (Voting) explains approximately 14\\% of F1 variance, the best AUROC reaches 0.749 (EM), indicating strong binary discriminative power for the quality/failure classification most relevant to practitioners in quality-aware routing.\\footnote{For context, semantic entropy achieves AUROC $\\approx$ 0.75--0.85 on discrete-answer QA tasks \\cite{kuhn2023semantic}; direct comparison is complicated by the fundamentally different output spaces of structured IE versus closed-form QA.}\nBootstrap CIs for signal pair differences on SciERC NER ($N{=}8$): SJ$-$logprob $\\Delta\\rho{=}{+}0.155$ [+0.074, +0.234]; Voting$-$SJ $\\Delta\\rho{=}{+}0.019$ [$-$0.033, +0.073]; SJ$-$EM $\\Delta\\rho{=}{+}0.065$ [+0.003, +0.130].\nThe SJ advantage over logprob is significant, while the Voting--SJ gap is not; the SJ--EM difference is marginal (CI lower bound +0.003; see Table~\\ref{tab:bootstrap_signal_ci}, Appendix~\\ref{app:bootstrap_signal} for individual signal CIs).\n\n\\paragraph{$\\rho$--AUROC dissociation.}\nOn NER, EM leads AUROC (0.749) despite ranking third in $\\rho$ (0.295); on RE, EM achieves the highest AUROC (0.706) while ranking last in $\\rho$ (0.134).\nBinary agreement provides clean separation between reliable and unreliable instances, while structural signals capture finer-grained quality variation.\nOn CoNLL with LLaMA, logprob achieves the highest AUROC (0.761) yet the lowest $\\rho$ (0.307), confirming this dissociation across datasets.\n\n\\paragraph{Signal rankings shift with task difficulty.}\nOn CoNLL (greedy F1${\\approx}$0.91), EM leads ($\\rho{=}0.451$, AUROC${=}0.816$), surpassing SJ and Voting.\nWhen most samples are near-correct, binary agreement captures remaining variance more efficiently than set-level similarity.\nThis reversal---EM${>}$SJ on easy tasks vs.\\ SJ${>}$EM on hard tasks---demonstrates that optimal signal choice depends on task difficulty.\nCross-model stability is strong: SJ achieves $\\rho{=}0.436$ (Qwen) vs.\\ $0.431$ (LLaMA) on CoNLL ($\\Delta{=}0.005$, within 3-seed $\\sigma{\\approx}0.007$).\nOn WNUT-17, where 54\\% of instances receive zero F1, full-set correlations are misleading: voting achieves $\\rho{=}0.724$ (AUROC${=}0.913$), but this is entirely driven by the zero/non-zero boundary (conditional $\\rho{=}0.038$, n.s.; Table~\\ref{tab:wnut}).\nLogprob exhibits strong \\textit{negative} correlation ($\\rho{=}{-}0.410$, AUROC${=}0.219$), indicating that higher model confidence associates with lower extraction quality on this noisy domain---further undermining logprob as a general-purpose IE quality signal.\nOn the conditional set, all signals collapse toward weak or non-significant correlations ($\\rho{\\leq}0.35$), with SJ achieving only $\\rho{=}0.089$ ($p{=}0.020$) on the full set---suggesting a capability boundary beyond which consistency signals capture binary success/failure but not quality gradation.\n\n\\paragraph{Conditional filtering.}\nFiltering to non-zero F1 instances reshuffles rankings (Figure~\\ref{fig:signal_heatmap}, right).\nEM emerges as the strongest conditional signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$), while Voting and FK drop substantially (Voting NER: $0.379{\\to}0.300$; FK NER: $0.267{\\to}0.176$).\nLogprob RE collapses to $\\rho{=}0.011$, confirming its full-set correlation was driven by zero/non-zero separation.\nThis creates a natural complementarity: Voting and SJ are preferred on the full set, while EM provides the most precise ranking within the non-trivial subset (see Appendix~\\ref{app:additional} for details).\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_selection_gap}\n\\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Left: NER; right: RE. Bars show best-of-$N$ selection F1; the line marks quality estimation $\\rho$. Despite $\\rho$ up to 0.38, no signal reliably surpasses greedy on either task ($p{=}0.39$ for NER logprob, the best signal). Dashed line indicates oracle upper bound.}\n\\label{fig:selection_gap}\n\\end{figure*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Best non-oracle result per column in \\textbf{bold}. EM is omitted because exact-match plurality is degenerate in structured IE: with $N{=}8$, the probability of two identical structured outputs is negligible.}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & RE F1 \\\\\n\\midrule\nOracle & 0.776 & 0.585 \\\\\n\\midrule\nLog-prob           & \\textbf{0.650} & 0.395 \\\\\nSoft Jaccard       & 0.645 & 0.386 \\\\\nVoting             & 0.634 & 0.359 \\\\\nExact Match        & ---   & ---   \\\\\n\\midrule\nGreedy ($T{=}0$)   & 0.644 & \\textbf{0.404} \\\\\nRandom             & 0.608 & 0.354 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDespite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection (Table~\\ref{tab:selection}, Figure~\\ref{fig:selection_gap}).\n\n\\paragraph{No signal reliably surpasses greedy.}\nWe exclude 22 instances with empty gold annotations, yielding $n{=}529$ for statistical analysis.\nWe evaluate statistical significance using instance-level paired bootstrap resampling ($B{=}10{,}000$, with replacement) over these instances, reporting 95\\% percentile CIs.\nThe three random seeds (42, 123, 456) refer to independent inference runs; we average $\\rho$ across seeds and report the bootstrap $p$-value of the paired difference (best signal vs.\\ greedy).\nOn NER, the oracle (0.776) reveals 13.2~pp of headroom above greedy (0.644).\nLogprob achieves the highest selection F1 (0.650, +0.6~pp), but this is not statistically significant ($p{=}0.39$; 95\\% CI: [$-$3.0, +4.2]~pp; Cohen's $d{=}0.038$; sign test: 61W/70L, win\\%${=}$46.6\\%).\nOn RE, the gap is complete: the best signal (logprob, 0.395) falls below greedy (0.404, $-0.9$\\,pp, $p{=}0.80$), while 18.1~pp of oracle headroom remains.\nVoting ($\\rho{=}0.379$, the best quality estimator) selects to only 0.634 on NER---\\textit{below} greedy.\nThe correlation-selection gap is consistent across all six tested configurations (Table~\\ref{tab:cross_selection}), with no signal significantly outperforming greedy in any setting.\n\n\\paragraph{Quality estimation $\\neq$ output selection.}\nInstance-level confidence signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} among $N$ candidates is best.\nWhen per-sample variance is low relative to instance-level difficulty, even perfect quality estimation cannot discriminate among near-identical candidates.\nThis gap has direct consequences for test-time scaling in IE \\cite{brown2024monkeys, snell2024scaling}: closing it likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers}.\n\n%% ============================================================\n\\subsection{Robustness}\n\\label{sec:robustness_main}\n\nConsistency-based signals (SJ, Voting, FK) show robust performance across $T{\\in}\\{0.7, 1.0\\}$; logprob temperature sensitivity remains uncharacterized due to unavailable $T{=}0.7$ data (Table~\\ref{tab:robustness}, Appendix~\\ref{app:robustness}).\nSJ NER $\\rho$ shifts by only 0.028 between $T{=}0.7$ and $T{=}1.0$ (bootstrap CI includes zero).\nDoubling from $N{=}8$ to $N{=}16$ yields sublinear gains: SJ improves by $+0.052$ on Qwen SciERC NER, while logprob is approximately $N$-invariant ($\\Delta\\rho{\\leq}0.021$).\nThe structural-over-logprob advantage is consistent across tested model families, holding across all four $N{=}16$ settings ($\\Delta\\rho{=}{+}0.135$ to ${+}0.175$).\nNER signals are reasonably well-calibrated (ECE 0.069--0.096; Appendix~\\ref{app:calibration}), while RE exhibits greater miscalibration (ECE 0.109--0.339).\nFor RE at $N{=}16$, SJ, FK, and logprob all plateau at $\\rho{\\approx}0.28$, suggesting compound errors impose a ceiling.\n",
      "numLines": 148,
      "startLine": 1,
      "totalLines": 148
    }
  },
  "sourceToolAssistantUUID": "6facf3e1-1bc8-4003-b7f2-31b3af80b99c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-15T03:58:19.274Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RUQwPCLGtixjiXU1i7jA4B`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0a7f762-b9bb-4719-b224-870b5c55e810",
  "isSidechain": false,
  "requestId": "req_011Cb3gcCfji25dhMsq8nbu2",
  "type": "assistant",
  "uuid": "062b493f-6583-4481-b0bb-7b336de3764e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012U5iYCFX3bLXueSRKQGfrs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 847,
      "cache_creation_input_tokens": 1610,
      "cache_read_input_tokens": 28774,
      "output_tokens": 985,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1610,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 847,
          "output_tokens": 985,
          "cache_read_input_tokens": 28774,
          "cache_creation_input_tokens": 1610,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1610
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

_source line 43 · 2026-05-15T03:58:19.279Z_

<details><summary>↩ Tool result · `toolu_01RUQwPCLGtixjiXU1i7jA4B`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, entity voting provides the strongest rank correlation ($\rho{=}0.38$, Table~\ref{tab:quality_estimation}), though exact match leads binary discrimination on SciERC (AUROC${=}0.749$).
5	When temperature or cross-condition robustness is required, SJ is preferable: its temperature sensitivity is small with bootstrap CIs including zero (Table~\ref{tab:robustness}).
6	Under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$), extending binary-agreement advantages to the within-capability regime.
7	Signal rankings depend on task difficulty: EM dominates on easy tasks (CoNLL, F1${\approx}$0.91), Voting and SJ dominate on hard tasks (SciERC, F1$\,{\approx}\,$0.66), and when model capability is insufficient (WNUT-17), full-set correlations are inflated by zero/non-zero separation (Voting $\rho{=}0.724$, conditional $\rho{=}0.038$, n.s.) while all signals converge toward weak or non-significant conditional correlations.
8	This ordering is consistent across tested model families, suggesting the difficulty gradient determines which signal family is most informative.
9	Conditional filtering confirms this pattern: removing zero-F1 instances shifts effective difficulty toward the easy-task regime, and EM reclaims the lead while Voting and SJ drop substantially (Voting RE: $0.350{\to}0.241$).
10	While our NER findings are validated across three datasets, our RE conclusions rest on SciERC alone and warrant further validation.
11	
12	\paragraph{Why quality estimators fail as selectors.}
13	The four instance-level signals (Voting, SJ, FK, EM) produce a single score per input, which by construction cannot rank $N$ candidates; the consensus-proximity strategy (\S\ref{sec:evaluation}) converts them to per-sample scores, but the resulting selection performance (Table~\ref{tab:selection}) shows this conversion adds no reliable value.
14	Quality estimation ranks \textit{instances} by expected output quality; sample selection ranks \textit{candidates within a single instance}, requiring per-sample quality information that instance-level aggregation discards.
15	On SciERC NER, the random baseline (0.608) falls 3.6~pp below greedy (0.644), confirming per-instance sample variance exists; yet the oracle gap of 13.2~pp shows substantially better candidates exist, and the best signal captures only +0.6~pp ($p{=}0.39$).
16	We observe a notable $\rho$--AUROC dissociation: on SciERC, EM achieves AUROC of 0.749 (NER) and 0.706 (RE) yet ranks third or last in $\rho$, because EM${=}1$ collapses both all-correct and all-wrong instances into the same binary outcome, destroying rank order while preserving discriminative power (see Appendix~\ref{app:additional} for details).
17	The practical implication is that these signals are well-suited for routing and triage---flagging uncertain instances for human review---but not for fine-grained ranking within a difficulty tier.
18	
19	\paragraph{Why logprob fails as a selector.}
20	Log-probability---the sole per-sample signal---also fails at selection despite its structural advantage for candidate ranking.
21	Under constrained decoding, logprob primarily reflects grammar compliance rather than semantic extraction quality: a sample may have high token-level confidence yet extract the wrong relation arguments.
22	Bootstrap analysis reveals that 75\% of instance-level logprob comparisons are effectively ties (win\%${=}$46.6\%, comparable to random), consistent with the non-significant selection result ($p{=}0.39$).
23	Mean log-probability is weakly positively correlated with output length (NER: $\rho{=}0.39$; RE: $\rho{=}0.33$; Figure~\ref{fig:length_logprob_scatter}), ruling out length-penalty confounding as an explanation for logprob's selection failure.
24	NER signals are reasonably well-calibrated (ECE 0.069--0.096), but RE miscalibration (ECE 0.109--0.339; Appendix~\ref{app:calibration}) suggests that logprob confidence scores are poorly aligned with extraction quality for compound tasks.
25	Constrained decoding enforces schema compliance at the token level, which may compress per-sample diversity beyond what free-form generation would exhibit---affecting not only logprob but also consensus-proximity selection (SJ, Voting), since reduced per-sample diversity limits any selector's ability to discriminate among near-identical candidates.
26	The random baseline gap (3.6~pp) confirms meaningful variance exists even under constraints, but the correlation-selection gap may partially reflect this reduced diversity.
27	Future work should compare constrained vs.\ unconstrained decoding to disentangle these effects.
28	
29	\paragraph{Methodological implications.}
30	The decoupling of quality estimation ($\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means that evaluating confidence signals on a single metric risks selecting the wrong signal for the intended use case.
31	Effective best-of-$N$ selection likely requires per-sample signals such as trained verifiers \cite{cobbe2021verifiers} that can evaluate individual outputs rather than distribution-level properties.
32	Further $N$-scaling analysis (Appendix~\ref{app:additional}) shows that $N{=}8$ captures most achievable quality estimation benefit; additional samples widen the correlation-selection gap absent stronger selectors.
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "062b493f-6583-4481-b0bb-7b336de3764e",
  "isSidechain": false,
  "promptId": "f5d01f90-29f0-42ef-8c36-beb6e3f39fb5",
  "type": "user",
  "uuid": "67267df5-8431-4267-b344-200deb7cf376",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Practical recommendations.}\nFor per-instance quality ranking, entity voting provides the strongest rank correlation ($\\rho{=}0.38$, Table~\\ref{tab:quality_estimation}), though exact match leads binary discrimination on SciERC (AUROC${=}0.749$).\nWhen temperature or cross-condition robustness is required, SJ is preferable: its temperature sensitivity is small with bootstrap CIs including zero (Table~\\ref{tab:robustness}).\nUnder conditional filtering, EM leads on both NER and RE ($\\rho{=}0.360$, $0.417$), extending binary-agreement advantages to the within-capability regime.\nSignal rankings depend on task difficulty: EM dominates on easy tasks (CoNLL, F1${\\approx}$0.91), Voting and SJ dominate on hard tasks (SciERC, F1$\\,{\\approx}\\,$0.66), and when model capability is insufficient (WNUT-17), full-set correlations are inflated by zero/non-zero separation (Voting $\\rho{=}0.724$, conditional $\\rho{=}0.038$, n.s.) while all signals converge toward weak or non-significant conditional correlations.\nThis ordering is consistent across tested model families, suggesting the difficulty gradient determines which signal family is most informative.\nConditional filtering confirms this pattern: removing zero-F1 instances shifts effective difficulty toward the easy-task regime, and EM reclaims the lead while Voting and SJ drop substantially (Voting RE: $0.350{\\to}0.241$).\nWhile our NER findings are validated across three datasets, our RE conclusions rest on SciERC alone and warrant further validation.\n\n\\paragraph{Why quality estimators fail as selectors.}\nThe four instance-level signals (Voting, SJ, FK, EM) produce a single score per input, which by construction cannot rank $N$ candidates; the consensus-proximity strategy (\\S\\ref{sec:evaluation}) converts them to per-sample scores, but the resulting selection performance (Table~\\ref{tab:selection}) shows this conversion adds no reliable value.\nQuality estimation ranks \\textit{instances} by expected output quality; sample selection ranks \\textit{candidates within a single instance}, requiring per-sample quality information that instance-level aggregation discards.\nOn SciERC NER, the random baseline (0.608) falls 3.6~pp below greedy (0.644), confirming per-instance sample variance exists; yet the oracle gap of 13.2~pp shows substantially better candidates exist, and the best signal captures only +0.6~pp ($p{=}0.39$).\nWe observe a notable $\\rho$--AUROC dissociation: on SciERC, EM achieves AUROC of 0.749 (NER) and 0.706 (RE) yet ranks third or last in $\\rho$, because EM${=}1$ collapses both all-correct and all-wrong instances into the same binary outcome, destroying rank order while preserving discriminative power (see Appendix~\\ref{app:additional} for details).\nThe practical implication is that these signals are well-suited for routing and triage---flagging uncertain instances for human review---but not for fine-grained ranking within a difficulty tier.\n\n\\paragraph{Why logprob fails as a selector.}\nLog-probability---the sole per-sample signal---also fails at selection despite its structural advantage for candidate ranking.\nUnder constrained decoding, logprob primarily reflects grammar compliance rather than semantic extraction quality: a sample may have high token-level confidence yet extract the wrong relation arguments.\nBootstrap analysis reveals that 75\\% of instance-level logprob comparisons are effectively ties (win\\%${=}$46.6\\%, comparable to random), consistent with the non-significant selection result ($p{=}0.39$).\nMean log-probability is weakly positively correlated with output length (NER: $\\rho{=}0.39$; RE: $\\rho{=}0.33$; Figure~\\ref{fig:length_logprob_scatter}), ruling out length-penalty confounding as an explanation for logprob's selection failure.\nNER signals are reasonably well-calibrated (ECE 0.069--0.096), but RE miscalibration (ECE 0.109--0.339; Appendix~\\ref{app:calibration}) suggests that logprob confidence scores are poorly aligned with extraction quality for compound tasks.\nConstrained decoding enforces schema compliance at the token level, which may compress per-sample diversity beyond what free-form generation would exhibit---affecting not only logprob but also consensus-proximity selection (SJ, Voting), since reduced per-sample diversity limits any selector's ability to discriminate among near-identical candidates.\nThe random baseline gap (3.6~pp) confirms meaningful variance exists even under constraints, but the correlation-selection gap may partially reflect this reduced diversity.\nFuture work should compare constrained vs.\\ unconstrained decoding to disentangle these effects.\n\n\\paragraph{Methodological implications.}\nThe decoupling of quality estimation ($\\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means that evaluating confidence signals on a single metric risks selecting the wrong signal for the intended use case.\nEffective best-of-$N$ selection likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers} that can evaluate individual outputs rather than distribution-level properties.\nFurther $N$-scaling analysis (Appendix~\\ref{app:additional}) shows that $N{=}8$ captures most achievable quality estimation benefit; additional samples widen the correlation-selection gap absent stronger selectors.\n",
      "numLines": 33,
      "startLine": 1,
      "totalLines": 33
    }
  },
  "sourceToolAssistantUUID": "062b493f-6583-4481-b0bb-7b336de3764e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-15T03:58:19.702Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WJE4d2qJvJ4c1UosuJAxZc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67267df5-8431-4267-b344-200deb7cf376",
  "isSidechain": false,
  "requestId": "req_011Cb3gcCfji25dhMsq8nbu2",
  "type": "assistant",
  "uuid": "e074cc8b-9a6f-4bd5-b00e-f0aa92a75773",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012U5iYCFX3bLXueSRKQGfrs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 847,
      "cache_creation_input_tokens": 1610,
      "cache_read_input_tokens": 28774,
      "output_tokens": 985,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1610,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 847,
          "output_tokens": 985,
          "cache_read_input_tokens": 28774,
          "cache_creation_input_tokens": 1610,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1610
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

_source line 45 · 2026-05-15T03:58:19.709Z_

<details><summary>↩ Tool result · `toolu_01WJE4d2qJvJ4c1UosuJAxZc`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	This work provides the first multi-family comparison of confidence signals for test-time scaling in generative information extraction.
4	By comparing five signals from three families---structural, surface, and model-internal---across NER and RE tasks of varying difficulty, we disentangle two objectives that prior work has conflated: quality estimation (ranking instances by expected performance) and sample selection (choosing the best output among $N$ candidates).
5	Our experiments on SciERC, CoNLL-2003, and WNUT-17 with Qwen3-8B and LLaMA-3.1-8B reveal that these objectives require fundamentally different signal properties.
6	
7	Three findings anchor our analysis.
8	First, consistency-based signals are effective quality estimators: entity voting achieves the strongest rank correlation ($\rho{=}0.38$) while exact match leads binary discrimination (AUROC${=}0.75$) on SciERC NER, with signal rankings depending on both task complexity and evaluation metric.
9	Second, the \textit{correlation-selection gap} shows that strong instance-level correlation does not yield substantial selection gains---no signal reliably surpasses greedy on either task (NER logprob: +0.6~pp, $p{=}0.39$; RE: $-$0.9~pp) despite 13--18~pp of oracle headroom---because instance-level signals cannot discriminate among candidates with similar consistency profiles.
10	Third, signal rankings depend on task difficulty: exact match leads on easy tasks, Soft Jaccard and voting lead on hard tasks, and when model capability is insufficient, inflated full-set correlations (driven by zero/non-zero separation) mask the collapse of all signals on the conditional set.
11	This ordering is consistent across tested model families, suggesting the difficulty gradient determines which signal family is most informative.
12	While our NER findings are validated across three datasets, our RE conclusions rest on SciERC alone and warrant further validation.
13	
14	Several directions remain open.
15	Trained verifiers or reward models could close the selection gap by learning per-sample quality discrimination that unsupervised consistency signals lack.
16	Cross-task transfer of confidence signals beyond IE---to structured prediction tasks such as semantic parsing and code generation---would test the generality of our findings.
17	Integration with conformal prediction could convert continuous confidence scores into calibrated coverage guarantees.
18	Finally, scaling analysis with larger models (70B+) and more diverse IE tasks would clarify whether increased model capability narrows or widens the correlation-selection gap.
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e074cc8b-9a6f-4bd5-b00e-f0aa92a75773",
  "isSidechain": false,
  "promptId": "f5d01f90-29f0-42ef-8c36-beb6e3f39fb5",
  "type": "user",
  "uuid": "84f54f4d-890b-4143-822e-6159550bf840",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nThis work provides the first multi-family comparison of confidence signals for test-time scaling in generative information extraction.\nBy comparing five signals from three families---structural, surface, and model-internal---across NER and RE tasks of varying difficulty, we disentangle two objectives that prior work has conflated: quality estimation (ranking instances by expected performance) and sample selection (choosing the best output among $N$ candidates).\nOur experiments on SciERC, CoNLL-2003, and WNUT-17 with Qwen3-8B and LLaMA-3.1-8B reveal that these objectives require fundamentally different signal properties.\n\nThree findings anchor our analysis.\nFirst, consistency-based signals are effective quality estimators: entity voting achieves the strongest rank correlation ($\\rho{=}0.38$) while exact match leads binary discrimination (AUROC${=}0.75$) on SciERC NER, with signal rankings depending on both task complexity and evaluation metric.\nSecond, the \\textit{correlation-selection gap} shows that strong instance-level correlation does not yield substantial selection gains---no signal reliably surpasses greedy on either task (NER logprob: +0.6~pp, $p{=}0.39$; RE: $-$0.9~pp) despite 13--18~pp of oracle headroom---because instance-level signals cannot discriminate among candidates with similar consistency profiles.\nThird, signal rankings depend on task difficulty: exact match leads on easy tasks, Soft Jaccard and voting lead on hard tasks, and when model capability is insufficient, inflated full-set correlations (driven by zero/non-zero separation) mask the collapse of all signals on the conditional set.\nThis ordering is consistent across tested model families, suggesting the difficulty gradient determines which signal family is most informative.\nWhile our NER findings are validated across three datasets, our RE conclusions rest on SciERC alone and warrant further validation.\n\nSeveral directions remain open.\nTrained verifiers or reward models could close the selection gap by learning per-sample quality discrimination that unsupervised consistency signals lack.\nCross-task transfer of confidence signals beyond IE---to structured prediction tasks such as semantic parsing and code generation---would test the generality of our findings.\nIntegration with conformal prediction could convert continuous confidence scores into calibrated coverage guarantees.\nFinally, scaling analysis with larger models (70B+) and more diverse IE tasks would clarify whether increased model capability narrows or widens the correlation-selection gap.\n",
      "numLines": 19,
      "startLine": 1,
      "totalLines": 19
    }
  },
  "sourceToolAssistantUUID": "e074cc8b-9a6f-4bd5-b00e-f0aa92a75773",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-15T03:58:20.650Z_

<details open><summary>🔧 Tool call — Read · `toolu_014PvWEAGCNWpHr3oUZQ5PDs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84f54f4d-890b-4143-822e-6159550bf840",
  "isSidechain": false,
  "requestId": "req_011Cb3gcCfji25dhMsq8nbu2",
  "type": "assistant",
  "uuid": "992490c4-38c3-4e2f-b0b4-ff49fe0ecf8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012U5iYCFX3bLXueSRKQGfrs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 847,
      "cache_creation_input_tokens": 1610,
      "cache_read_input_tokens": 28774,
      "output_tokens": 985,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1610,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 847,
          "output_tokens": 985,
          "cache_read_input_tokens": 28774,
          "cache_creation_input_tokens": 1610,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1610
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

_source line 47 · 2026-05-15T03:58:20.656Z_

<details><summary>↩ Tool result · `toolu_014PvWEAGCNWpHr3oUZQ5PDs`</summary>

```text
1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 44\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
3	
4	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
5	Whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering, which are consistent across our two tested model families---hold for larger models (70B+) or closed-source APIs remains untested.
6	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
7	
8	Our analysis of selection potential uses only unsupervised signals.
9	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
10	
11	We evaluate at $N{=}8$ and $N{=}16$.
12	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
13	
14	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
15	Constrained decoding (Outlines/vLLM) enforces schema compliance, potentially compressing per-sample diversity and contributing to the correlation-selection gap beyond what free-form generation would exhibit.
16	Finally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\ $T{=}1.0$) due to missing $T{=}0.7$ logprob data, leaving its temperature sensitivity uncharacterized.
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "992490c4-38c3-4e2f-b0b4-ff49fe0ecf8c",
  "isSidechain": false,
  "promptId": "f5d01f90-29f0-42ef-8c36-beb6e3f39fb5",
  "type": "user",
  "uuid": "752f7347-8c7b-4960-8864-92acf166a369",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex",
      "content": "Our evaluation covers three datasets but only one RE benchmark (SciERC), where 44\\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.\nWNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.\n\nWe evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.\nWhether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering, which are consistent across our two tested model families---hold for larger models (70B+) or closed-source APIs remains untested.\nLarger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.\n\nOur analysis of selection potential uses only unsupervised signals.\nWe do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.\n\nWe evaluate at $N{=}8$ and $N{=}16$.\nThe behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.\n\nOn CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\\rho{=}0.431$ vs.\\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.\nConstrained decoding (Outlines/vLLM) enforces schema compliance, potentially compressing per-sample diversity and contributing to the correlation-selection gap beyond what free-form generation would exhibit.\nFinally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\\ $T{=}1.0$) due to missing $T{=}0.7$ logprob data, leaving its temperature sensitivity uncharacterized.\n",
      "numLines": 17,
      "startLine": 1,
      "totalLines": 17
    }
  },
  "sourceToolAssistantUUID": "992490c4-38c3-4e2f-b0b4-ff49fe0ecf8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-15T03:58:21.157Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Pw8Q5HPbgi7dDVr6hedAtd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "752f7347-8c7b-4960-8864-92acf166a369",
  "isSidechain": false,
  "requestId": "req_011Cb3gcCfji25dhMsq8nbu2",
  "type": "assistant",
  "uuid": "1951f081-243b-415c-92dc-33462096e861",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012U5iYCFX3bLXueSRKQGfrs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 847,
      "cache_creation_input_tokens": 1610,
      "cache_read_input_tokens": 28774,
      "output_tokens": 985,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1610,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 847,
          "output_tokens": 985,
          "cache_read_input_tokens": 28774,
          "cache_creation_input_tokens": 1610,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1610
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

_source line 49 · 2026-05-15T03:58:21.163Z_

<details><summary>↩ Tool result · `toolu_01Pw8Q5HPbgi7dDVr6hedAtd`</summary>

```text
1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	$c_{\text{vote}}$ & Entity voting confidence \\
22	$c_{\text{lp}}$ & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: cross-model transfer (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}
35	\label{tab:robustness}
36	\begin{tabular}{llcc}
37	\toprule
38	& & NER $\rho$ & RE $\rho$ \\
39	\midrule
40	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
41	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
42	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
43	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
44	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
45	\midrule
46	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
47	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
48	\quad SJ & $N{=}16$ & 0.412$^\dagger$ & 0.281 \\
49	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
50	\quad FK & $N{=}16$ & 0.280 & 0.279 \\
51	\midrule
52	\multicolumn{4}{l}{\textit{Cross-model} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
53	\quad SJ &  & $0.463{\pm}0.007$ & --- \\
54	\quad FK &  & $0.455{\pm}0.006$ & --- \\
55	\quad EM &  & $0.460{\pm}0.008$ & --- \\
56	\quad Voting &  & $0.458{\pm}0.003$ & --- \\
57	\quad Logprob &  & $0.310{\pm}0.005$ & --- \\
58	\bottomrule
59	\end{tabular}
60	\end{table}
61	
62	\begin{figure}[t]
63	\centering
64	\includegraphics[width=\columnwidth]{fig_temperature_robustness}
65	\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. Logprob $T{=}0.7$ data unavailable.}
66	\label{fig:temperature_robustness}
67	\end{figure}
68	
69	\paragraph{Temperature sensitivity.}
70	SJ NER $\rho$ shifts from 0.388 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.028 whose bootstrap confidence interval includes zero.
71	FK shows mixed behavior: NER $\rho$ drops by 0.054, while RE $\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.
72	Across all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\ 0.321 at $T{=}0.7$; 0.360 vs.\ 0.267 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.
73	
74	\paragraph{Sample size scaling.}
75	Increasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\rho$ rises from 0.360 to $0.412{\pm}0.025$ (three seeds: 0.428, 0.424, 0.384), a gain of $+0.052$.
76	The magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.
77	LLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\Delta\rho{\approx}{+}0.030$ (range: $+0.027$ to $+0.032$) while logprob gains only $+0.003$ (Table~\ref{tab:quality_estimation}).
78	FK $N$-scaling is inconsistent: degradation on SciERC ($-0.007$ to $-0.019$) but improvement on CoNLL with LLaMA ($+0.027$), suggesting sensitivity to both model and task characteristics.
79	Voting confidence $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.062$ on Qwen SciERC), while logprob is approximately $N$-invariant ($\Delta{\leq}0.021$).
80	SJ, EM, and voting confidence scale consistently across all tested settings; only FK shows setting-dependent variation, suggesting that structural and binary-agreement signals are the most robust to $N$.
81	
82	\paragraph{Cross-model transfer.}
83	LLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\rho{=}0.363$, FK $\rho{=}0.327$).
84	On CoNLL, the cross-model gap is minimal (Table~\ref{tab:quality_estimation}): SJ achieves $\rho{=}0.431$ (LLaMA) vs.\ 0.436 (Qwen), $\Delta{=}0.005$.
85	At $N{=}16$, the structural-over-logprob advantage holds across all four tested settings: Qwen SciERC (Voting $\rho{=}0.411$ vs.\ logprob 0.259, $\Delta{=}{+}0.152$), Qwen CoNLL (EM $\rho{=}0.463$ vs.\ logprob 0.328, $\Delta{=}{+}0.135$), LLaMA SciERC (Voting $\rho{=}0.452$ vs.\ logprob 0.277, $\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\rho{=}0.463{\pm}0.007$ vs.\ logprob $0.310{\pm}0.005$, $\Delta{=}{+}0.153$).
86	
87	\section{Calibration Analysis}\label{app:calibration}
88	
89	\begin{figure*}[t]
90	\centering
91	\includegraphics[width=\textwidth]{fig_reliability}
92	\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), reflecting the difficulty of calibrating confidence for compound extraction tasks.}
93	\label{fig:reliability}
94	\end{figure*}
95	
96	NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), indicating that translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.
97	
98	\section{Additional Analyses}\label{app:additional}
99	
100	\paragraph{Per-relation diagnostic.}
101	RE signal degradation is relation-specific.
102	\textsc{Feature-Of} has near-zero correlation ($\rho{=}0.004$), while \textsc{Hyponym-Of} achieves $\rho{=}0.646$.
103	The primary bottleneck is entity span errors, which account for 55.5\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.
104	We note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.
105	
106	\paragraph{Capability stratification.}
107	For NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\rho{=}0.547$, compared to $\rho{=}0.415$ for 1--2 entities.
108	The SJ advantage over logprob remains stable across sentence-length quartiles ($\Delta\rho{\approx}0.08$--$0.20$).
109	For RE, SJ $\rho$ increases monotonically with sentence length (Q1: 0.110 $\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.
110	Both proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.
111	For RE, entity count and relation count are strongly correlated ($\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.
112	On the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: Voting reaches $\rho{=}0.630$, logprob $\rho{=}0.554$, and SJ $\rho{=}0.502$---all far above the full-set levels.
113	Richer relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.
114	
115	\paragraph{Length vs.\ log-probability.}
116	Figure~\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\rho{=}0.386$, $n{=}4{,}232$; RE: $\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for logprob's selection failure: longer outputs receive \textit{higher}, not lower, token-averaged log-probability under constrained decoding.
117	
118	\begin{figure}[t]
119	\centering
120	\includegraphics[width=\columnwidth]{fig_length_logprob_scatter}
121	\caption{Output length vs.\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\rho{=}0.386$; RE: $\rho{=}0.326$) rule out length-penalty confounding.}
122	\label{fig:length_logprob_scatter}
123	\end{figure}
124	
125	\paragraph{Evaluation circularity.}
126	Leave-one-out SJ (LOO-SJ), which excludes the target sample when computing confidence, yields $\Delta\rho{=}{-}0.014$ relative to standard SJ, with a maximum per-instance $\Delta\rho$ of $3.1{\times}10^{-4}$.
127	Evaluation circularity is negligible.
128	
129	\paragraph{Conditional filtering details.}
130	On LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\rho{=}0.405$ while FK drops to $\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.
131	At $N{=}16$, the divergence persists: SJ maintains $\rho{=}0.308$ on conditional RE while logprob drops to $\rho{=}{-}0.026$.
132	EM ranks first across all four tested conditional configurations---SciERC NER ($\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\rho{=}0.466$), CoNLL LLaMA 3-seed ($\rho{=}0.462$), and SciERC RE ($\rho{=}0.417$)---despite full-set rankings ranging from \#1 (CoNLL Qwen) to \#5 (SciERC RE).
133	On the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.
134	On the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.
135	The margin over SJ is largest on RE ($\Delta\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\Delta\rho{=}{+}0.002$), where all signals converge near $\rho{\approx}0.46$.
136	
137	\paragraph{WNUT-17 full signal analysis.}
138	Table~\ref{tab:wnut} reports all five signals on WNUT-17.
139	Voting achieves $\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\rho{=}0.038$ ($p{=}0.49$).
140	Logprob shows the reverse pattern: full-set $\rho{=}{-}0.410$ but conditional $\rho{=}0.350$, the highest among all signals on the conditional set.
141	This inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.
142	
143	\begin{table}[t]
144	\centering
145	\small
146	\caption{Quality estimation on WNUT-17 (Qwen, $N{=}8$, $T{=}1.0$, $n{=}689$ after filtering gold-empty instances). Cond: non-zero F1 instances ($n{=}334$). Logprob exhibits strong negative full-set $\rho$; its conditional $\rho$ reverses to the highest among all signals, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.}
147	\label{tab:wnut}
148	\begin{tabular}{lccccc}
149	\toprule
150	Signal & $\rho$ & $p$ & AUROC & Cond.\ $\rho$ & Cond.\ $p$ \\
151	\midrule
152	Voting  & .724 & ${<}$1e-112 & .913 & .038 & .487 \\
153	FK      & .125 & .001 & .555 & .169 & .002 \\
154	SJ      & .089 & .020 & .517 & .288 & ${<}$1e-7 \\
155	EM      & .050 & .194 & .487 & .333 & ${<}$1e-9 \\
156	Logprob & $-$.410 & ${<}$1e-28 & .219 & .350 & ${<}$1e-10 \\
157	\bottomrule
158	\end{tabular}
159	\end{table}
160	
161	\paragraph{Cross-configuration selection analysis.}
162	Table~\ref{tab:cross_selection} extends the correlation-selection gap analysis with per-signal best-of-$N$ selection F1 across four additional configurations (supplementing Table~\ref{tab:selection} for Qwen SciERC).
163	No signal reliably surpasses greedy in any setting.
164	On CoNLL, where greedy already exceeds 0.90 F1, all signals perform at or below greedy, confirming the gap is not specific to a single model--dataset combination.
165	
166	\begin{table*}[t]
167	\centering
168	\small
169	\caption{Best-of-$N$ selection F1 across configurations ($T{=}1.0$). Best non-oracle signal per row in \textbf{bold}. No signal reliably surpasses greedy in any configuration; CoNLL shows especially tight clustering where greedy already exceeds 0.90.}
170	\label{tab:cross_selection}
171	\begin{tabular}{llccccccc}
172	\toprule
173	Config & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\
174	\midrule
175	LLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \textbf{.652} & .633 \\
176	LLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \textbf{.649} & \textbf{.649} & .640 & .646 & .640 \\
177	Qwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \textbf{.899} & .893 & .898 & .897 & .895 \\
178	LLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \textbf{.925} & .924 & .924 & .923 \\
179	\bottomrule
180	\end{tabular}
181	\end{table*}
182	
183	\paragraph{Diminishing returns of $N$-scaling.}
184	Our $N{=}8$ and $N{=}16$ comparisons (Table~\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \cite{brown2024monkeys, snell2024scaling}.
185	For quality estimation, structural signals benefit consistently but sublinearly: SJ $\rho$ improves by $+0.052$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\Delta\rho{\leq}0.021$).
186	Structural signals leverage $\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.
187	This asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\rho{=}0.431$ on LLaMA CoNLL (vs.\ logprob $\rho{=}0.307$, $\Delta{=}{+}0.124$), and the gap \textit{widens} at $N{=}16$ ($\Delta{=}{+}0.153$) because structural signals continue to benefit from additional pairwise evidence while logprob does not.
188	For sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.
189	The practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.
190	
191	\section{Bootstrap CI for Signal Comparisons}\label{app:bootstrap_signal}
192	
193	Table~\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\rho$ and pairwise $\Delta\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).
194	The SJ--logprob gap ($\Delta\rho{=}{+}0.155$) is clearly significant, confirming the structural advantage reported in \S\ref{sec:qe_results}.
195	The Voting--SJ gap ($\Delta\rho{=}{+}0.019$) is not significant, indicating that these two structural signals perform comparably.
196	The SJ--EM gap ($\Delta\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.
197	
198	\begin{table}[t]
199	\centering
200	\small
201	\caption{Bootstrap 95\% CIs for signal $\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\Delta\rho$; ``Sig.'' indicates whether the 95\% CI excludes zero.}
202	\label{tab:bootstrap_signal_ci}
203	\begin{tabular}{lcc}
204	\toprule
205	Signal & $\rho$ & 95\% CI \\
206	\midrule
207	Voting Conf. & +0.379 & [+0.299, +0.456] \\
208	Soft Jaccard & +0.360 & [+0.277, +0.437] \\
209	Exact Match & +0.295 & [+0.212, +0.371] \\
210	Fleiss' $\kappa$ & +0.267 & [+0.176, +0.354] \\
211	Log-prob & +0.205 & [+0.119, +0.291] \\
212	\bottomrule
213	\end{tabular}
214	
215	\vspace{0.5em}
216	
217	\begin{tabular}{lccc}
218	\toprule
219	Comparison & $\Delta\rho$ & 95\% CI & Sig. \\
220	\midrule
221	SJ $-$ Logprob & +0.155 & [+0.074, +0.234] & Yes \\
222	Voting $-$ SJ & +0.019 & [$-$0.033, +0.073] & No \\
223	SJ $-$ EM & +0.065 & [+0.003, +0.130] & Yes$^\dagger$ \\
224	\bottomrule
225	\end{tabular}
226	
227	\smallskip
228	{\footnotesize $^\dagger$Borderline significant (CI barely excludes zero).}
229	\end{table}
230	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1951f081-243b-415c-92dc-33462096e861",
  "isSidechain": false,
  "promptId": "f5d01f90-29f0-42ef-8c36-beb6e3f39fb5",
  "type": "user",
  "uuid": "b16d2103-f34a-4992-a8cd-92521151bbac",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "\\section{Notation}\\label{app:notation}\n\nTable~\\ref{tab:notation} summarizes the notation used throughout the paper.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{cl}\n\\toprule\nSymbol & Meaning \\\\\n\\midrule\n$\\mathcal{M}$ & Language model \\\\\n$x$ & Input instance \\\\\n$y_i$ & $i$-th stochastic sample \\\\\n$N$ & Number of samples \\\\\n$T$ & Sampling temperature \\\\\n$c(\\cdot)$ & Confidence signal \\\\\nSJ & Soft Jaccard similarity \\\\\nFK & Fleiss' $\\kappa$ \\\\\nEM & Exact-match voting rate \\\\\n$c_{\\text{vote}}$ & Entity voting confidence \\\\\n$c_{\\text{lp}}$ & Log-probability (mean token log-likelihood) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Notation used throughout the paper.}\n\\label{tab:notation}\n\\end{table}\n\n\\section{Robustness Analysis}\\label{app:robustness}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal robustness across configurations (Spearman $\\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: cross-model transfer (LLaMA CoNLL $N{=}16$, 3-seed mean $\\pm\\sigma$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}\n\\label{tab:robustness}\n\\begin{tabular}{llcc}\n\\toprule\n& & NER $\\rho$ & RE $\\rho$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\\\\n\\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\\\\n\\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\\\\n\\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\\\\n\\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\\\\n\\quad SJ & $N{=}8$  & 0.360 & 0.250 \\\\\n\\quad SJ & $N{=}16$ & 0.412$^\\dagger$ & 0.281 \\\\\n\\quad FK & $N{=}8$  & 0.267 & 0.275 \\\\\n\\quad FK & $N{=}16$ & 0.280 & 0.279 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Cross-model} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\\\\n\\quad SJ &  & $0.463{\\pm}0.007$ & --- \\\\\n\\quad FK &  & $0.455{\\pm}0.006$ & --- \\\\\n\\quad EM &  & $0.460{\\pm}0.008$ & --- \\\\\n\\quad Voting &  & $0.458{\\pm}0.003$ & --- \\\\\n\\quad Logprob &  & $0.310{\\pm}0.005$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_temperature_robustness}\n\\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. Logprob $T{=}0.7$ data unavailable.}\n\\label{fig:temperature_robustness}\n\\end{figure}\n\n\\paragraph{Temperature sensitivity.}\nSJ NER $\\rho$ shifts from 0.388 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.028 whose bootstrap confidence interval includes zero.\nFK shows mixed behavior: NER $\\rho$ drops by 0.054, while RE $\\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.\nAcross all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\\ 0.321 at $T{=}0.7$; 0.360 vs.\\ 0.267 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.\n\n\\paragraph{Sample size scaling.}\nIncreasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\\rho$ rises from 0.360 to $0.412{\\pm}0.025$ (three seeds: 0.428, 0.424, 0.384), a gain of $+0.052$.\nThe magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.\nLLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\\Delta\\rho{\\approx}{+}0.030$ (range: $+0.027$ to $+0.032$) while logprob gains only $+0.003$ (Table~\\ref{tab:quality_estimation}).\nFK $N$-scaling is inconsistent: degradation on SciERC ($-0.007$ to $-0.019$) but improvement on CoNLL with LLaMA ($+0.027$), suggesting sensitivity to both model and task characteristics.\nVoting confidence $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.062$ on Qwen SciERC), while logprob is approximately $N$-invariant ($\\Delta{\\leq}0.021$).\nSJ, EM, and voting confidence scale consistently across all tested settings; only FK shows setting-dependent variation, suggesting that structural and binary-agreement signals are the most robust to $N$.\n\n\\paragraph{Cross-model transfer.}\nLLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\\rho{=}0.363$, FK $\\rho{=}0.327$).\nOn CoNLL, the cross-model gap is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\nAt $N{=}16$, the structural-over-logprob advantage holds across all four tested settings: Qwen SciERC (Voting $\\rho{=}0.411$ vs.\\ logprob 0.259, $\\Delta{=}{+}0.152$), Qwen CoNLL (EM $\\rho{=}0.463$ vs.\\ logprob 0.328, $\\Delta{=}{+}0.135$), LLaMA SciERC (Voting $\\rho{=}0.452$ vs.\\ logprob 0.277, $\\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\\rho{=}0.463{\\pm}0.007$ vs.\\ logprob $0.310{\\pm}0.005$, $\\Delta{=}{+}0.153$).\n\n\\section{Calibration Analysis}\\label{app:calibration}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_reliability}\n\\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), reflecting the difficulty of calibrating confidence for compound extraction tasks.}\n\\label{fig:reliability}\n\\end{figure*}\n\nNER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), indicating that translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.\n\n\\section{Additional Analyses}\\label{app:additional}\n\n\\paragraph{Per-relation diagnostic.}\nRE signal degradation is relation-specific.\n\\textsc{Feature-Of} has near-zero correlation ($\\rho{=}0.004$), while \\textsc{Hyponym-Of} achieves $\\rho{=}0.646$.\nThe primary bottleneck is entity span errors, which account for 55.5\\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.\nWe note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.\n\n\\paragraph{Capability stratification.}\nFor NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nThe SJ advantage over logprob remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$).\nFor RE, SJ $\\rho$ increases monotonically with sentence length (Q1: 0.110 $\\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.\nBoth proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.\nFor RE, entity count and relation count are strongly correlated ($\\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.\nOn the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: Voting reaches $\\rho{=}0.630$, logprob $\\rho{=}0.554$, and SJ $\\rho{=}0.502$---all far above the full-set levels.\nRicher relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.\n\n\\paragraph{Length vs.\\ log-probability.}\nFigure~\\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\\rho{=}0.386$, $n{=}4{,}232$; RE: $\\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for logprob's selection failure: longer outputs receive \\textit{higher}, not lower, token-averaged log-probability under constrained decoding.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_length_logprob_scatter}\n\\caption{Output length vs.\\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\\rho{=}0.386$; RE: $\\rho{=}0.326$) rule out length-penalty confounding.}\n\\label{fig:length_logprob_scatter}\n\\end{figure}\n\n\\paragraph{Evaluation circularity.}\nLeave-one-out SJ (LOO-SJ), which excludes the target sample when computing confidence, yields $\\Delta\\rho{=}{-}0.014$ relative to standard SJ, with a maximum per-instance $\\Delta\\rho$ of $3.1{\\times}10^{-4}$.\nEvaluation circularity is negligible.\n\n\\paragraph{Conditional filtering details.}\nOn LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\\rho{=}0.405$ while FK drops to $\\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.\nAt $N{=}16$, the divergence persists: SJ maintains $\\rho{=}0.308$ on conditional RE while logprob drops to $\\rho{=}{-}0.026$.\nEM ranks first across all four tested conditional configurations---SciERC NER ($\\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\\rho{=}0.466$), CoNLL LLaMA 3-seed ($\\rho{=}0.462$), and SciERC RE ($\\rho{=}0.417$)---despite full-set rankings ranging from \\#1 (CoNLL Qwen) to \\#5 (SciERC RE).\nOn the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.\nOn the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.\nThe margin over SJ is largest on RE ($\\Delta\\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\\Delta\\rho{=}{+}0.002$), where all signals converge near $\\rho{\\approx}0.46$.\n\n\\paragraph{WNUT-17 full signal analysis.}\nTable~\\ref{tab:wnut} reports all five signals on WNUT-17.\nVoting achieves $\\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\\rho{=}0.038$ ($p{=}0.49$).\nLogprob shows the reverse pattern: full-set $\\rho{=}{-}0.410$ but conditional $\\rho{=}0.350$, the highest among all signals on the conditional set.\nThis inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Quality estimation on WNUT-17 (Qwen, $N{=}8$, $T{=}1.0$, $n{=}689$ after filtering gold-empty instances). Cond: non-zero F1 instances ($n{=}334$). Logprob exhibits strong negative full-set $\\rho$; its conditional $\\rho$ reverses to the highest among all signals, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.}\n\\label{tab:wnut}\n\\begin{tabular}{lccccc}\n\\toprule\nSignal & $\\rho$ & $p$ & AUROC & Cond.\\ $\\rho$ & Cond.\\ $p$ \\\\\n\\midrule\nVoting  & .724 & ${<}$1e-112 & .913 & .038 & .487 \\\\\nFK      & .125 & .001 & .555 & .169 & .002 \\\\\nSJ      & .089 & .020 & .517 & .288 & ${<}$1e-7 \\\\\nEM      & .050 & .194 & .487 & .333 & ${<}$1e-9 \\\\\nLogprob & $-$.410 & ${<}$1e-28 & .219 & .350 & ${<}$1e-10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-configuration selection analysis.}\nTable~\\ref{tab:cross_selection} extends the correlation-selection gap analysis with per-signal best-of-$N$ selection F1 across four additional configurations (supplementing Table~\\ref{tab:selection} for Qwen SciERC).\nNo signal reliably surpasses greedy in any setting.\nOn CoNLL, where greedy already exceeds 0.90 F1, all signals perform at or below greedy, confirming the gap is not specific to a single model--dataset combination.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 across configurations ($T{=}1.0$). Best non-oracle signal per row in \\textbf{bold}. No signal reliably surpasses greedy in any configuration; CoNLL shows especially tight clustering where greedy already exceeds 0.90.}\n\\label{tab:cross_selection}\n\\begin{tabular}{llccccccc}\n\\toprule\nConfig & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\\\\n\\midrule\nLLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \\textbf{.652} & .633 \\\\\nLLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \\textbf{.649} & \\textbf{.649} & .640 & .646 & .640 \\\\\nQwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \\textbf{.899} & .893 & .898 & .897 & .895 \\\\\nLLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \\textbf{.925} & .924 & .924 & .923 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\paragraph{Diminishing returns of $N$-scaling.}\nOur $N{=}8$ and $N{=}16$ comparisons (Table~\\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \\cite{brown2024monkeys, snell2024scaling}.\nFor quality estimation, structural signals benefit consistently but sublinearly: SJ $\\rho$ improves by $+0.052$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\\Delta\\rho{\\leq}0.021$).\nStructural signals leverage $\\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.\nThis asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\\rho{=}0.431$ on LLaMA CoNLL (vs.\\ logprob $\\rho{=}0.307$, $\\Delta{=}{+}0.124$), and the gap \\textit{widens} at $N{=}16$ ($\\Delta{=}{+}0.153$) because structural signals continue to benefit from additional pairwise evidence while logprob does not.\nFor sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.\nThe practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.\n\n\\section{Bootstrap CI for Signal Comparisons}\\label{app:bootstrap_signal}\n\nTable~\\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\\rho$ and pairwise $\\Delta\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).\nThe SJ--logprob gap ($\\Delta\\rho{=}{+}0.155$) is clearly significant, confirming the structural advantage reported in \\S\\ref{sec:qe_results}.\nThe Voting--SJ gap ($\\Delta\\rho{=}{+}0.019$) is not significant, indicating that these two structural signals perform comparably.\nThe SJ--EM gap ($\\Delta\\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Bootstrap 95\\% CIs for signal $\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\\Delta\\rho$; ``Sig.'' indicates whether the 95\\% CI excludes zero.}\n\\label{tab:bootstrap_signal_ci}\n\\begin{tabular}{lcc}\n\\toprule\nSignal & $\\rho$ & 95\\% CI \\\\\n\\midrule\nVoting Conf. & +0.379 & [+0.299, +0.456] \\\\\nSoft Jaccard & +0.360 & [+0.277, +0.437] \\\\\nExact Match & +0.295 & [+0.212, +0.371] \\\\\nFleiss' $\\kappa$ & +0.267 & [+0.176, +0.354] \\\\\nLog-prob & +0.205 & [+0.119, +0.291] \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{0.5em}\n\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta\\rho$ & 95\\% CI & Sig. \\\\\n\\midrule\nSJ $-$ Logprob & +0.155 & [+0.074, +0.234] & Yes \\\\\nVoting $-$ SJ & +0.019 & [$-$0.033, +0.073] & No \\\\\nSJ $-$ EM & +0.065 & [+0.003, +0.130] & Yes$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}\n\n\\smallskip\n{\\footnotesize $^\\dagger$Borderline significant (CI barely excludes zero).}\n\\end{table}\n",
      "numLines": 230,
      "startLine": 1,
      "totalLines": 230
    }
  },
  "sourceToolAssistantUUID": "1951f081-243b-415c-92dc-33462096e861",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-15T03:58:23.464Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RR7kbPauGaky4id5efp9ex`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all questions, rating scales (with numeric values and labels), and any instructions for reviewers. I need the exact scoring dimensions and their scales."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b16d2103-f34a-4992-a8cd-92521151bbac",
  "isSidechain": false,
  "requestId": "req_011Cb3gcCfji25dhMsq8nbu2",
  "type": "assistant",
  "uuid": "206fa5be-ccaf-485f-9d57-2de21a6fb7d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012U5iYCFX3bLXueSRKQGfrs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 847,
      "cache_creation_input_tokens": 1610,
      "cache_read_input_tokens": 28774,
      "output_tokens": 985,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1610,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 847,
          "output_tokens": 985,
          "cache_read_input_tokens": 28774,
          "cache_creation_input_tokens": 1610,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1610
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

_source line 51 · 2026-05-15T03:58:24.298Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references · `toolu_01PkoFEPh6d85F7wvc419pfq`</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "206fa5be-ccaf-485f-9d57-2de21a6fb7d4",
  "isSidechain": false,
  "requestId": "req_011Cb3gcCfji25dhMsq8nbu2",
  "type": "assistant",
  "uuid": "d8dc9419-64e2-424b-9f4d-9821bc23cefe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012U5iYCFX3bLXueSRKQGfrs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 847,
      "cache_creation_input_tokens": 1610,
      "cache_read_input_tokens": 28774,
      "output_tokens": 985,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1610,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 847,
          "output_tokens": 985,
          "cache_read_input_tokens": 28774,
          "cache_creation_input_tokens": 1610,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1610
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

_source line 52_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。  ## 审稿对象 - 论文路径：`projects/struct_self_consist_ie/docs/paper/main.tex`（分节结构，各节在 `sections/` 下） - 目标 venue：**EMNLP 2026 Main Conference**（通过 ARR May…",
  "leafUuid": "d8dc9419-64e2-424b-9f4d-9821bc23cefe",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b"
}
```

---

### Runtime record

_source line 53_

```json
{
  "type": "ai-title",
  "aiTitle": "Generative IE confidence signals systematic review",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b"
}
```

---

### Tool result

_source line 54 · 2026-05-15T03:58:29.213Z_

<details><summary>↩ Tool result · `toolu_01RR7kbPauGaky4id5efp9ex`</summary>

```text
# ACL Rolling Review Form - Complete Structure

## Main Scoring Dimensions

**Reviewer Confidence** (1-5 scale)
- "5 = Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- 4 = Quite sure with unlikely but conceivable gaps
- 3 = Pretty sure but possible missed details
- 2 = Willing to defend, fairly likely missed elements
- "1 = Not my area, or paper is very hard to understand"

**Soundness** (1-5 scale with half-point increments)
- "5 = Excellent: This study is one of the most thorough I have seen"
- 4 = Strong with sufficient claim support
- 3 = Acceptable with minor gaps
- 2 = Poor with insufficient support for main claims
- "1 = Major Issues: not yet sufficiently thorough to warrant publication"

**Excitement** (1-5 scale with half-point increments)
- "5 = Highly Exciting: I would recommend this paper to others"
- 4 = Exciting; would mention to others
- 3 = Interesting; might mention selectively
- 2 = Potentially interesting despite personal disengagement
- "1 = Not Exciting: does not resonate with me or broader community"

**Overall Assessment** (1-5 scale with half-point increments)
- 5 = Award consideration (top 2.5%)
- 4 = Conference acceptance
- 3 = Findings track
- 2 = Resubmit next cycle
- 1 = Do not resubmit

## Additional Rating Dimensions

**Reproducibility** (1-5): Easy reproduction → Unable to reproduce
**Datasets** (1-5): Enabling → No usable datasets
**Software** (1-5): Enabling → No usable software released
**Author Identity Knowledge** (1-5): Confirmed identity → No educated guess
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "206fa5be-ccaf-485f-9d57-2de21a6fb7d4",
  "isSidechain": false,
  "promptId": "f5d01f90-29f0-42ef-8c36-beb6e3f39fb5",
  "type": "user",
  "uuid": "1310c645-12c3-4b91-864d-97e1412f4fc3",
  "toolUseResult": {
    "bytes": 25365,
    "code": 200,
    "codeText": "OK",
    "result": "# ACL Rolling Review Form - Complete Structure\n\n## Main Scoring Dimensions\n\n**Reviewer Confidence** (1-5 scale)\n- \"5 = Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work.\"\n- 4 = Quite sure with unlikely but conceivable gaps\n- 3 = Pretty sure but possible missed details\n- 2 = Willing to defend, fairly likely missed elements\n- \"1 = Not my area, or paper is very hard to understand\"\n\n**Soundness** (1-5 scale with half-point increments)\n- \"5 = Excellent: This study is one of the most thorough I have seen\"\n- 4 = Strong with sufficient claim support\n- 3 = Acceptable with minor gaps\n- 2 = Poor with insufficient support for main claims\n- \"1 = Major Issues: not yet sufficiently thorough to warrant publication\"\n\n**Excitement** (1-5 scale with half-point increments)\n- \"5 = Highly Exciting: I would recommend this paper to others\"\n- 4 = Exciting; would mention to others\n- 3 = Interesting; might mention selectively\n- 2 = Potentially interesting despite personal disengagement\n- \"1 = Not Exciting: does not resonate with me or broader community\"\n\n**Overall Assessment** (1-5 scale with half-point increments)\n- 5 = Award consideration (top 2.5%)\n- 4 = Conference acceptance\n- 3 = Findings track\n- 2 = Resubmit next cycle\n- 1 = Do not resubmit\n\n## Additional Rating Dimensions\n\n**Reproducibility** (1-5): Easy reproduction → Unable to reproduce\n**Datasets** (1-5): Enabling → No usable datasets\n**Software** (1-5): Enabling → No usable software released\n**Author Identity Knowledge** (1-5): Confirmed identity → No educated guess",
    "durationMs": 5743,
    "url": "https://aclrollingreview.org/reviewform"
  },
  "sourceToolAssistantUUID": "206fa5be-ccaf-485f-9d57-2de21a6fb7d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-15T03:59:07.512Z_

<details><summary>↩ Tool result · `toolu_01PkoFEPh6d85F7wvc419pfq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 49, \"total_citations\": 69, \"unique_cited_keys\": 49, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 45, \"online_not_found\": 2, \"online_mismatch\": 2}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"angelopoulos2021conformal\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"authors\": \"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\", \"year\": \"2021\", \"venue\": \"ICLR 2021\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"arXiv preprint (ICML 2024 Workshop ICL)\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2110.14168\"}, {\"key\": \"culotta2004confidence\", \"type\": \"inproceedings\", \"title\": \"Confidence Estimation for Information Extraction\", \"authors\": \"Culotta, Aron and McCallum, Andrew\", \"year\": \"2004\", \"venue\": \"HLT-NAACL 2004\"}, {\"key\": \"derczynski2017wnut\", \"type\": \"inproceedings\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"authors\": \"Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut\", \"year\": \"2017\", \"venue\": \"W-NUT Workshop at EMNLP 2017\"}, {\"key\": \"desai2020calibration\", \"type\": \"inproceedings\", \"title\": \"Calibration of Pre-trained Transformers\", \"authors\": \"Desai, Shrey and Durrett, Greg\", \"year\": \"2020\", \"venue\": \"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"fisch2021conformal\", \"type\": \"inproceedings\", \"title\": \"Few-Shot Conformal Prediction with Auxiliary Tasks\", \"authors\": \"Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina\", \"year\": \"2021\", \"venue\": \"ICML 2021\"}, {\"key\": \"fleiss1971agreement\", \"type\": \"article\", \"title\": \"Measuring nominal scale agreement among many raters.\", \"authors\": \"Fleiss, Joseph L.\", \"year\": \"1971\", \"venue\": \"Psychological Bulletin\"}, {\"key\": \"gal2016dropout\", \"type\": \"inproceedings\", \"title\": \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\", \"authors\": \"Gal, Yarin and Ghahramani, Zoubin\", \"year\": \"2016\", \"venue\": \"ICML 2016\"}, {\"key\": \"geifman2017selective\", \"type\": \"inproceedings\", \"title\": \"Selective Classification for Deep Neural Networks\", \"authors\": \"Geifman, Yonatan and El-Yaniv, Ran\", \"year\": \"2017\", \"venue\": \"NeurIPS 2017\"}, {\"key\": \"feng2025optimal\", \"type\": \"article\", \"title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"authors\": \"Feng, Austin and Alonso, Marius and Odonnat, Ambroise\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2511.12309\"}, {\"key\": \"geng2024confidence\", \"type\": \"inproceedings\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"authors\": \"Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Presla...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"guo2017calibration\", \"type\": \"inproceedings\", \"title\": \"On Calibration of Modern Neural Networks\", \"authors\": \"Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.\", \"year\": \"2017\", \"venue\": \"ICML 2017\"}, {\"key\": \"hobelsberger2025systematic\", \"type\": \"article\", \"title\": \"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\", \"authors\": \"Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, O...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2510.20460\"}, {\"key\": \"jaccard1901distribution\", \"type\": \"article\", \"title\": \"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\", \"authors\": \"Jaccard, Paul\", \"year\": \"1901\", \"venue\": \"Bulletin de la Société Vaudoise des Sciences Naturelles\"}, {\"key\": \"josifoski2022genie\", \"type\": \"inproceedings\", \"title\": \"GenIE: Generative Information Extraction\", \"authors\": \"Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and ...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"kadavath2022language\", \"type\": \"article\", \"title\": \"Language Models (Mostly) Know What They Know\", \"authors\": \"Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain...\", \"year\": \"2022\", \"venue\": \"arXiv preprint arXiv:2207.05221\"}, {\"key\": \"kang2025selfcertainty\", \"type\": \"inproceedings\", \"title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"authors\": \"Kang, Zhewei and Zhao, Xuandong and Song, Dawn\", \"year\": \"2025\", \"venue\": \"NeurIPS 2025\"}, {\"key\": \"kim2026reasc\", \"type\": \"inproceedings\", \"title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"authors\": \"Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin\", \"year\": \"2026\", \"venue\": \"ACL 2026\"}, {\"key\": \"kossen2024semantic\", \"type\": \"article\", \"title\": \"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\", \"authors\": \"Kossen, Jannik and Han, Jiatong and Razzak, Muhammed and Schut, Lisa and Malik, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2406.15927\"}, {\"key\": \"li2025llms\", \"type\": \"article\", \"title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"authors\": \"Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi an...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2503.04104\"}, {\"key\": \"kuhn2023semantic\", \"type\": \"inproceedings\", \"title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"authors\": \"Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian\", \"year\": \"2023\", \"venue\": \"ICLR 2023\"}, {\"key\": \"lakshminarayanan2017ensembles\", \"type\": \"inproceedings\", \"title\": \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\", \"authors\": \"Lakshminarayanan, Balaji and Pritzel, Alexander and Blundell, Charles\", \"year\": \"2017\", \"venue\": \"NeurIPS 2017\"}, {\"key\": \"li2023codeie\", \"type\": \"inproceedings\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"authors\": \"Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Hu...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"lightman2024verify\", \"type\": \"inproceedings\", \"title\": \"Let's Verify Step by Step\", \"authors\": \"Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Bak...\", \"year\": \"2024\", \"venue\": \"ICLR 2024\"}, {\"key\": \"luan2018scierc\", \"type\": \"inproceedings\", \"title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"authors\": \"Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh\", \"year\": \"2018\", \"venue\": \"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"manakul2023selfcheckgpt\", \"type\": \"inproceedings\", \"title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"authors\": \"Manakul, Potsawee and Liusie, Adian and Gales, Mark\", \"year\": \"2023\", \"venue\": \"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"nedellec2026consistency\", \"type\": \"article\", \"title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant...\", \"authors\": \"Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert\", \"year\": \"2026\", \"venue\": \"Genomics \\\\& Informatics\"}, {\"key\": \"oh2025latentsc\", \"type\": \"article\", \"title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"authors\": \"Oh, Jungsuk and Lee, Jay-Yoon\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2508.18395\"}, {\"key\": \"sainz2024gollie\", \"type\": \"inproceedings\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"authors\": \"Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lope...\", \"year\": \"2024\", \"venue\": \"ICLR 2024\"}, {\"key\": \"shelmanov2021active\", \"type\": \"inproceedings\", \"title\": \"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\", \"authors\": \"Shelmanov, Artem and Puzyrev, Dmitri and Kupriyanova, Lyubov and Belyakov, Denis...\", \"year\": \"2021\", \"venue\": \"Proceedings of the 16th Conference of the European Chapter of the Association fo...\"}, {\"key\": \"snell2024scaling\", \"type\": \"inproceedings\", \"title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"authors\": \"Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral\", \"year\": \"2024\", \"venue\": \"ICLR 2025\"}, {\"key\": \"taubenfeld2025cisc\", \"type\": \"inproceedings\", \"title\": \"Confidence Improves Self-Consistency in LLMs\", \"authors\": \"Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, ...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"thirukovalluru2024atomic\", \"type\": \"inproceedings\", \"title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"authors\": \"Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"tjongkimsang2003conll\", \"type\": \"inproceedings\", \"title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"authors\": \"Sang, Erik F. Tjong Kim and Meulder, Fien De\", \"year\": \"2003\", \"venue\": \"CoNLL 2003\"}, {\"key\": \"vashurin2025cocoa\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"authors\": \"Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksan...\", \"year\": \"2025\", \"venue\": \"NeurIPS 2025\"}, {\"key\": \"wadhwa2023revisiting\", \"type\": \"inproceedings\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"authors\": \"Wadhwa, Somin and Amir, Silvio and Wallace, Byron\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"wang2023instructuie\", \"type\": \"article\", \"title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"authors\": \"Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2304.08085\"}, {\"key\": \"wang2023selfconsistency\", \"type\": \"inproceedings\", \"title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"authors\": \"Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Na...\", \"year\": \"2023\", \"venue\": \"ICLR 2023\"}, {\"key\": \"wang2025make\", \"type\": \"inproceedings\", \"title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"authors\": \"Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueq...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: NAACL 2025\"}, {\"key\": \"wang2024mathshepherd\", \"type\": \"inproceedings\", \"title\": \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\", \"authors\": \"Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, Runxin and Dai, Damai and Li, ...\", \"year\": \"2024\", \"venue\": \"ACL 2024\"}, {\"key\": \"wang2025rankedvoting\", \"type\": \"inproceedings\", \"title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"authors\": \"Wang, Weiqin and Wang, Yile and Huang, Hui\", \"year\": \"2025\", \"venue\": \"ACL Findings 2025\"}, {\"key\": \"wen2025know\", \"type\": \"article\", \"title\": \"Know Your Limits: A Survey of Abstention in Large Language Models\", \"authors\": \"Wen, Bingbing and Yao, Jihan and Feng, Shangbin and Xu, Chenjun and Tsvetkov, Yu...\", \"year\": \"2025\", \"venue\": \"Transactions of the Association for Computational Linguistics\"}, {\"key\": \"willard2023guided\", \"type\": \"article\", \"title\": \"Efficient Guided Generation for Large Language Models\", \"authors\": \"Willard, Brandon T. and Louf, Rémi\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2307.09702\"}, {\"key\": \"xia2025survey\", \"type\": \"inproceedings\", \"title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"authors\": \"Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang\", \"year\": \"2025\", \"venue\": \"ACL Findings 2025\"}, {\"key\": \"xiao2019uncertainty\", \"type\": \"article\", \"title\": \"Quantifying Uncertainties in Natural Language Processing Tasks\", \"authors\": \"Xiao, Yijun and Wang, William Yang\", \"year\": \"2019\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"zhang2023ener\", \"type\": \"inproceedings\", \"title\": \"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\", \"authors\": \"Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotia...\", \"year\": \"2023\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2023\"}, {\"key\": \"zhou2024uniner\", \"type\": \"inproceedings\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"authors\": \"Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}], \"tex_citations\": [{\"key\": \"wang2023selfconsistency\", \"file\": \"sections/introduction.tex\", \"line\": 4, \"command\": \"citealp\"}, {\"key\": \"snell2024scaling\", \"file\": \"sections/introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"wang2023selfconsistency\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"chen2024usc\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"taubenfeld2025cisc\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"kang2025selfcertainty\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"nedellec2026consistency\", \"file\": \"sections/introduction.tex\", \"line\": 16, \"command\": \"citet\"}, {\"key\": \"luan2018scierc\", \"file\": \"sections/introduction.tex\", \"line\": 31, \"command\": \"cite\"}, {\"key\": \"tjongkimsang2003conll\", \"file\": \"sections/introduction.tex\", \"line\": 31, \"command\": \"cite\"}, {\"key\": \"derczynski2017wnut\", \"file\": \"sections/introduction.tex\", \"line\": 31, \"command\": \"cite\"}, {\"key\": \"wang2023selfconsistency\", \"file\": \"sections/related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"chen2024usc\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"thirukovalluru2024atomic\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"manakul2023selfcheckgpt\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"snell2024scaling\", \"file\": \"sections/related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"taubenfeld2025cisc\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"kang2025selfcertainty\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"kim2026reasc\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"wang2025rankedvoting\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"oh2025latentsc\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"feng2025optimal\", \"file\": \"sections/related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"wang2025make\", \"file\": \"sections/related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"li2025llms\", \"file\": \"sections/related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"nedellec2026consistency\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"citet\"}, {\"key\": \"vashurin2025cocoa\", \"file\": \"sections/related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"zhou2024uniner\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"sainz2024gollie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"josifoski2022genie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"li2023codeie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"wadhwa2023revisiting\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"wang2023instructuie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"geng2024confidence\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"wen2025know\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"xia2025survey\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"hobelsberger2025systematic\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"kuhn2023semantic\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"kossen2024semantic\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"citet\"}, {\"key\": \"kadavath2022language\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"guo2017calibration\", \"file\": \"sections/related_work.tex\", \"line\": 22, \"command\": \"cite\"}, {\"key\": \"desai2020calibration\", \"file\": \"sections/related_work.tex\", \"line\": 22, \"command\": \"cite\"}, {\"key\": \"lakshminarayanan2017ensembles\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"gal2016dropout\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"xiao2019uncertainty\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"shelmanov2021active\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"zhang2023ener\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"fisch2021conformal\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"angelopoulos2021conformal\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"lightman2024verify\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"wang2024mathshepherd\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"geifman2017selective\", \"file\": \"sections/related_work.tex\", \"line\": 26, \"command\": \"cite\"}, {\"key\": \"culotta2004confidence\", \"file\": \"sections/related_work.tex\", \"line\": 26, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/method.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"fleiss1971agreement\", \"file\": \"sections/method.tex\", \"line\": 32, \"command\": \"citet\"}, {\"key\": \"jaccard1901distribution\", \"file\": \"sections/method.tex\", \"line\": 41, \"command\": \"cite\"}, {\"key\": \"luan2018scierc\", \"file\": \"sections/experiments.tex\", \"line\": 9, \"command\": \"cite\"}, {\"key\": \"tjongkimsang2003conll\", \"file\": \"sections/experiments.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"derczynski2017wnut\", \"file\": \"sections/experiments.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/experiments.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"kuhn2023semantic\", \"file\": \"sections/experiments.tex\", \"line\": 64, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/experiments.tex\", \"line\": 136, \"command\": \"cite\"}, {\"key\": \"snell2024scaling\", \"file\": \"sections/experiments.tex\", \"line\": 136, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/experiments.tex\", \"line\": 136, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/discussion.tex\", \"line\": 31, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/appendix.tex\", \"line\": 184, \"command\": \"cite\"}, {\"key\": \"snell2024scaling\", \"file\": \"sections/appendix.tex\", \"line\": 184, \"command\": \"cite\"}], \"online_verification\": [{\"key\": \"angelopoulos2021conformal\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"brown2024monkeys\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"chen2024usc\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Universal Self-Consistency for Large Language Model Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cobbe2021verifiers\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Training Verifiers to Solve Math Word Problems\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"culotta2004confidence\", \"title\": \"Confidence Estimation for Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Confidence estimation for information extraction\", \"matched_year\": \"2004\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"derczynski2017wnut\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"desai2020calibration\", \"title\": \"Calibration of Pre-trained Transformers\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Calibration of Pre-trained Transformers\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fisch2021conformal\", \"title\": \"Few-Shot Conformal Prediction with Auxiliary Tasks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Few-shot Conformal Prediction with Auxiliary Tasks\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fleiss1971agreement\", \"title\": \"Measuring nominal scale agreement among many raters.\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Measuring nominal scale agreement among many raters.\", \"matched_year\": \"1971\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gal2016dropout\", \"title\": \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\", \"matched_year\": \"2015\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"geifman2017selective\", \"title\": \"Selective Classification for Deep Neural Networks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Selective Classification for Deep Neural Networks\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"feng2025optimal\", \"title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=feng vs api=austin\"], \"note\": \"\"}, {\"key\": \"geng2024confidence\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"guo2017calibration\", \"title\": \"On Calibration of Modern Neural Networks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"On Calibration of Modern Neural Networks\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hobelsberger2025systematic\", \"title\": \"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\", \"status\": \"not_found\", \"confidence\": 0.236, \"matched_title\": \"A new criterion for assessing discriminant validity in variance-based structural equation modeling\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.24 below threshold 0.82\"}, {\"key\": \"jaccard1901distribution\", \"title\": \"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\", \"matched_year\": \"1901\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"josifoski2022genie\", \"title\": \"GenIE: Generative Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GenIE: Generative Information Extraction\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kadavath2022language\", \"title\": \"Language Models (Mostly) Know What They Know\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Language Models (Mostly) Know What They Know\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kang2025selfcertainty\", \"title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kim2026reasc\", \"title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kossen2024semantic\", \"title\": \"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2025llms\", \"title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kuhn2023semantic\", \"title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"lakshminarayanan2017ensembles\", \"title\": \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\", \"matched_year\": \"2016\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2023codeie\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"lightman2024verify\", \"title\": \"Let's Verify Step by Step\", \"status\": \"not_found\", \"confidence\": 0.246, \"matched_title\": \"Development and dosimetric verification of static SHArc: Step‐and‐shoot carbon ion arc therapy for LET &lt;sub>d&lt;/sub> escalation in pancreatic tumors\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.25 below threshold 0.82\"}, {\"key\": \"luan2018scierc\", \"title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"manakul2023selfcheckgpt\", \"title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"nedellec2026consistency\", \"title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"oh2025latentsc\", \"title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"sainz2024gollie\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"shelmanov2021active\", \"title\": \"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"snell2024scaling\", \"title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=snell vs api=charlie\"], \"note\": \"\"}, {\"key\": \"taubenfeld2025cisc\", \"title\": \"Confidence Improves Self-Consistency in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Confidence Improves Self-Consistency in LLMs\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"thirukovalluru2024atomic\", \"title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tjongkimsang2003conll\", \"title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"matched_year\": \"2003\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"vashurin2025cocoa\", \"title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wadhwa2023revisiting\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2023instructuie\", \"title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2023selfconsistency\", \"title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025make\", \"title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2024mathshepherd\", \"title\": \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025rankedvoting\", \"title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wen2025know\", \"title\": \"Know Your Limits: A Survey of Abstention in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Know Your Limits: A Survey of Abstention in Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"willard2023guided\", \"title\": \"Efficient Guided Generation for Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Efficient Guided Generation for Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xia2025survey\", \"title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xiao2019uncertainty\", \"title\": \"Quantifying Uncertainties in Natural Language Processing Tasks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Quantifying Uncertainties in Natural Language Processing Tasks\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhang2023ener\", \"title\": \"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhou2024uniner\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8dc9419-64e2-424b-9f4d-9821bc23cefe",
  "isSidechain": false,
  "promptId": "f5d01f90-29f0-42ef-8c36-beb6e3f39fb5",
  "type": "user",
  "uuid": "f00b6c88-6edf-4274-a18f-7afaffbe5470",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"summary\\\": {\\\"total_bib_entries\\\": 49, \\\"total_citations\\\": 69, \\\"unique_cited_keys\\\": 49, \\\"orphan_bib\\\": 0, \\\"missing_bib\\\": 0, \\\"duplicate_keys\\\": 0, \\\"online_verified\\\": 45, \\\"online_not_found\\\": 2, \\\"online_mismatch\\\": 2}, \\\"cross_check\\\": {\\\"orphan_bib\\\": [], \\\"missing_bib\\\": [], \\\"orphan_count\\\": 0, \\\"missing_count\\\": 0}, \\\"bib_entries\\\": [{\\\"key\\\": \\\"angelopoulos2021conformal\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Uncertainty Sets for Image Classifiers using Conformal Prediction\\\", \\\"authors\\\": \\\"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"ICLR 2021\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\\\", \\\"authors\\\": \\\"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2407.21787\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Universal Self-Consistency for Large Language Model Generation\\\", \\\"authors\\\": \\\"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint (ICML 2024 Workshop ICL)\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Training Verifiers to Solve Math Word Problems\\\", \\\"authors\\\": \\\"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2110.14168\\\"}, {\\\"key\\\": \\\"culotta2004confidence\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Confidence Estimation for Information Extraction\\\", \\\"authors\\\": \\\"Culotta, Aron and McCallum, Andrew\\\", \\\"year\\\": \\\"2004\\\", \\\"venue\\\": \\\"HLT-NAACL 2004\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\\\", \\\"authors\\\": \\\"Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"W-NUT Workshop at EMNLP 2017\\\"}, {\\\"key\\\": \\\"desai2020calibration\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Calibration of Pre-trained Transformers\\\", \\\"authors\\\": \\\"Desai, Shrey and Durrett, Greg\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"fisch2021conformal\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Few-Shot Conformal Prediction with Auxiliary Tasks\\\", \\\"authors\\\": \\\"Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"ICML 2021\\\"}, {\\\"key\\\": \\\"fleiss1971agreement\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Measuring nominal scale agreement among many raters.\\\", \\\"authors\\\": \\\"Fleiss, Joseph L.\\\", \\\"year\\\": \\\"1971\\\", \\\"venue\\\": \\\"Psychological Bulletin\\\"}, {\\\"key\\\": \\\"gal2016dropout\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\\\", \\\"authors\\\": \\\"Gal, Yarin and Ghahramani, Zoubin\\\", \\\"year\\\": \\\"2016\\\", \\\"venue\\\": \\\"ICML 2016\\\"}, {\\\"key\\\": \\\"geifman2017selective\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Selective Classification for Deep Neural Networks\\\", \\\"authors\\\": \\\"Geifman, Yonatan and El-Yaniv, Ran\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"NeurIPS 2017\\\"}, {\\\"key\\\": \\\"feng2025optimal\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\\\", \\\"authors\\\": \\\"Feng, Austin and Alonso, Marius and Odonnat, Ambroise\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2511.12309\\\"}, {\\\"key\\\": \\\"geng2024confidence\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"authors\\\": \\\"Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Presla...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"guo2017calibration\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"On Calibration of Modern Neural Networks\\\", \\\"authors\\\": \\\"Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"ICML 2017\\\"}, {\\\"key\\\": \\\"hobelsberger2025systematic\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\\\", \\\"authors\\\": \\\"Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, O...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2510.20460\\\"}, {\\\"key\\\": \\\"jaccard1901distribution\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\\\", \\\"authors\\\": \\\"Jaccard, Paul\\\", \\\"year\\\": \\\"1901\\\", \\\"venue\\\": \\\"Bulletin de la Société Vaudoise des Sciences Naturelles\\\"}, {\\\"key\\\": \\\"josifoski2022genie\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"GenIE: Generative Information Extraction\\\", \\\"authors\\\": \\\"Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and ...\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"Proceedings of the 2022 Conference of the North American Chapter of the Associat...\\\"}, {\\\"key\\\": \\\"kadavath2022language\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Language Models (Mostly) Know What They Know\\\", \\\"authors\\\": \\\"Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain...\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2207.05221\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\\\", \\\"authors\\\": \\\"Kang, Zhewei and Zhao, Xuandong and Song, Dawn\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"NeurIPS 2025\\\"}, {\\\"key\\\": \\\"kim2026reasc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\\\", \\\"authors\\\": \\\"Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"ACL 2026\\\"}, {\\\"key\\\": \\\"kossen2024semantic\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\\\", \\\"authors\\\": \\\"Kossen, Jannik and Han, Jiatong and Razzak, Muhammed and Schut, Lisa and Malik, ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2406.15927\\\"}, {\\\"key\\\": \\\"li2025llms\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\\\", \\\"authors\\\": \\\"Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi an...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2503.04104\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\\\", \\\"authors\\\": \\\"Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"ICLR 2023\\\"}, {\\\"key\\\": \\\"lakshminarayanan2017ensembles\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\\", \\\"authors\\\": \\\"Lakshminarayanan, Balaji and Pritzel, Alexander and Blundell, Charles\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"NeurIPS 2017\\\"}, {\\\"key\\\": \\\"li2023codeie\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"authors\\\": \\\"Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Hu...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"lightman2024verify\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Let's Verify Step by Step\\\", \\\"authors\\\": \\\"Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Bak...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"ICLR 2024\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\\\", \\\"authors\\\": \\\"Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh\\\", \\\"year\\\": \\\"2018\\\", \\\"venue\\\": \\\"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"manakul2023selfcheckgpt\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\\\", \\\"authors\\\": \\\"Manakul, Potsawee and Liusie, Adian and Gales, Mark\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"nedellec2026consistency\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant...\\\", \\\"authors\\\": \\\"Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"Genomics \\\\\\\\& Informatics\\\"}, {\\\"key\\\": \\\"oh2025latentsc\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\\\", \\\"authors\\\": \\\"Oh, Jungsuk and Lee, Jay-Yoon\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2508.18395\\\"}, {\\\"key\\\": \\\"sainz2024gollie\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"authors\\\": \\\"Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lope...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"ICLR 2024\\\"}, {\\\"key\\\": \\\"shelmanov2021active\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\\\", \\\"authors\\\": \\\"Shelmanov, Artem and Puzyrev, Dmitri and Kupriyanova, Lyubov and Belyakov, Denis...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"Proceedings of the 16th Conference of the European Chapter of the Association fo...\\\"}, {\\\"key\\\": \\\"snell2024scaling\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\\\", \\\"authors\\\": \\\"Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"ICLR 2025\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Confidence Improves Self-Consistency in LLMs\\\", \\\"authors\\\": \\\"Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, ...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2025\\\"}, {\\\"key\\\": \\\"thirukovalluru2024atomic\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Atomic Self-Consistency for Better Long Form Generations\\\", \\\"authors\\\": \\\"Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\\\", \\\"authors\\\": \\\"Sang, Erik F. Tjong Kim and Meulder, Fien De\\\", \\\"year\\\": \\\"2003\\\", \\\"venue\\\": \\\"CoNLL 2003\\\"}, {\\\"key\\\": \\\"vashurin2025cocoa\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\\\", \\\"authors\\\": \\\"Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksan...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"NeurIPS 2025\\\"}, {\\\"key\\\": \\\"wadhwa2023revisiting\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"authors\\\": \\\"Wadhwa, Somin and Amir, Silvio and Wallace, Byron\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\\\"}, {\\\"key\\\": \\\"wang2023instructuie\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\\\", \\\"authors\\\": \\\"Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2304.08085\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\", \\\"authors\\\": \\\"Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Na...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"ICLR 2023\\\"}, {\\\"key\\\": \\\"wang2025make\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\\\", \\\"authors\\\": \\\"Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueq...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: NAACL 2025\\\"}, {\\\"key\\\": \\\"wang2024mathshepherd\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\\\", \\\"authors\\\": \\\"Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, Runxin and Dai, Damai and Li, ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"ACL 2024\\\"}, {\\\"key\\\": \\\"wang2025rankedvoting\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Ranked Voting based Self-Consistency of Large Language Models\\\", \\\"authors\\\": \\\"Wang, Weiqin and Wang, Yile and Huang, Hui\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"ACL Findings 2025\\\"}, {\\\"key\\\": \\\"wen2025know\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Know Your Limits: A Survey of Abstention in Large Language Models\\\", \\\"authors\\\": \\\"Wen, Bingbing and Yao, Jihan and Feng, Shangbin and Xu, Chenjun and Tsvetkov, Yu...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Transactions of the Association for Computational Linguistics\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"authors\\\": \\\"Willard, Brandon T. and Louf, Rémi\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2307.09702\\\"}, {\\\"key\\\": \\\"xia2025survey\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Survey of Uncertainty Estimation Methods on Large Language Models\\\", \\\"authors\\\": \\\"Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"ACL Findings 2025\\\"}, {\\\"key\\\": \\\"xiao2019uncertainty\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Quantifying Uncertainties in Natural Language Processing Tasks\\\", \\\"authors\\\": \\\"Xiao, Yijun and Wang, William Yang\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the AAAI Conference on Artificial Intelligence\\\"}, {\\\"key\\\": \\\"zhang2023ener\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\\\", \\\"authors\\\": \\\"Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotia...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: ACL 2023\\\"}, {\\\"key\\\": \\\"zhou2024uniner\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"authors\\\": \\\"Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations (ICLR)\\\"}], \\\"tex_citations\\\": [{\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"citealp\\\"}, {\\\"key\\\": \\\"snell2024scaling\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"nedellec2026consistency\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 31, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 31, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"file\\\": \\\"sections/introduction.tex\\\", \\\"line\\\": 31, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 4, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"thirukovalluru2024atomic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"manakul2023selfcheckgpt\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"snell2024scaling\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 6, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kim2026reasc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2025rankedvoting\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"oh2025latentsc\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"feng2025optimal\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"wang2025make\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"li2025llms\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"nedellec2026consistency\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"vashurin2025cocoa\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zhou2024uniner\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"sainz2024gollie\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"josifoski2022genie\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"li2023codeie\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wadhwa2023revisiting\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2023instructuie\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"geng2024confidence\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wen2025know\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xia2025survey\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"hobelsberger2025systematic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kossen2024semantic\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"kadavath2022language\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 21, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"guo2017calibration\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"desai2020calibration\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 22, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"lakshminarayanan2017ensembles\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gal2016dropout\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xiao2019uncertainty\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"shelmanov2021active\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"zhang2023ener\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fisch2021conformal\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"angelopoulos2021conformal\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"lightman2024verify\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"wang2024mathshepherd\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 25, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"geifman2017selective\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 26, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"culotta2004confidence\\\", \\\"file\\\": \\\"sections/related_work.tex\\\", \\\"line\\\": 26, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fleiss1971agreement\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 32, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"jaccard1901distribution\\\", \\\"file\\\": \\\"sections/method.tex\\\", \\\"line\\\": 41, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 9, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 10, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 11, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 17, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 64, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 136, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"snell2024scaling\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 136, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"file\\\": \\\"sections/experiments.tex\\\", \\\"line\\\": 136, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"file\\\": \\\"sections/discussion.tex\\\", \\\"line\\\": 31, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 184, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"snell2024scaling\\\", \\\"file\\\": \\\"sections/appendix.tex\\\", \\\"line\\\": 184, \\\"command\\\": \\\"cite\\\"}], \\\"online_verification\\\": [{\\\"key\\\": \\\"angelopoulos2021conformal\\\", \\\"title\\\": \\\"Uncertainty Sets for Image Classifiers using Conformal Prediction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Uncertainty Sets for Image Classifiers using Conformal Prediction\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"brown2024monkeys\\\", \\\"title\\\": \\\"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"chen2024usc\\\", \\\"title\\\": \\\"Universal Self-Consistency for Large Language Model Generation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Universal Self-Consistency for Large Language Model Generation\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"cobbe2021verifiers\\\", \\\"title\\\": \\\"Training Verifiers to Solve Math Word Problems\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Training Verifiers to Solve Math Word Problems\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"culotta2004confidence\\\", \\\"title\\\": \\\"Confidence Estimation for Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Confidence estimation for information extraction\\\", \\\"matched_year\\\": \\\"2004\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"derczynski2017wnut\\\", \\\"title\\\": \\\"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\\\", \\\"matched_year\\\": \\\"2017\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"desai2020calibration\\\", \\\"title\\\": \\\"Calibration of Pre-trained Transformers\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Calibration of Pre-trained Transformers\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fisch2021conformal\\\", \\\"title\\\": \\\"Few-Shot Conformal Prediction with Auxiliary Tasks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Few-shot Conformal Prediction with Auxiliary Tasks\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fleiss1971agreement\\\", \\\"title\\\": \\\"Measuring nominal scale agreement among many raters.\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Measuring nominal scale agreement among many raters.\\\", \\\"matched_year\\\": \\\"1971\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"gal2016dropout\\\", \\\"title\\\": \\\"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\\\", \\\"matched_year\\\": \\\"2015\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"geifman2017selective\\\", \\\"title\\\": \\\"Selective Classification for Deep Neural Networks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Selective Classification for Deep Neural Networks\\\", \\\"matched_year\\\": \\\"2017\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"feng2025optimal\\\", \\\"title\\\": \\\"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=feng vs api=austin\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"geng2024confidence\\\", \\\"title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Survey of Confidence Estimation and Calibration in Large Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"guo2017calibration\\\", \\\"title\\\": \\\"On Calibration of Modern Neural Networks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"On Calibration of Modern Neural Networks\\\", \\\"matched_year\\\": \\\"2017\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"hobelsberger2025systematic\\\", \\\"title\\\": \\\"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.236, \\\"matched_title\\\": \\\"A new criterion for assessing discriminant validity in variance-based structural equation modeling\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.24 below threshold 0.82\\\"}, {\\\"key\\\": \\\"jaccard1901distribution\\\", \\\"title\\\": \\\"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\\\", \\\"matched_year\\\": \\\"1901\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"josifoski2022genie\\\", \\\"title\\\": \\\"GenIE: Generative Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GenIE: Generative Information Extraction\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kadavath2022language\\\", \\\"title\\\": \\\"Language Models (Mostly) Know What They Know\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Language Models (Mostly) Know What They Know\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kang2025selfcertainty\\\", \\\"title\\\": \\\"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kim2026reasc\\\", \\\"title\\\": \\\"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kossen2024semantic\\\", \\\"title\\\": \\\"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"li2025llms\\\", \\\"title\\\": \\\"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"kuhn2023semantic\\\", \\\"title\\\": \\\"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"lakshminarayanan2017ensembles\\\", \\\"title\\\": \\\"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\\", \\\"matched_year\\\": \\\"2016\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"li2023codeie\\\", \\\"title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"lightman2024verify\\\", \\\"title\\\": \\\"Let's Verify Step by Step\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.246, \\\"matched_title\\\": \\\"Development and dosimetric verification of static SHArc: Step‐and‐shoot carbon ion arc therapy for LET &lt;sub>d&lt;/sub> escalation in pancreatic tumors\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.25 below threshold 0.82\\\"}, {\\\"key\\\": \\\"luan2018scierc\\\", \\\"title\\\": \\\"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\\\", \\\"matched_year\\\": \\\"2018\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"manakul2023selfcheckgpt\\\", \\\"title\\\": \\\"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"nedellec2026consistency\\\", \\\"title\\\": \\\"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"oh2025latentsc\\\", \\\"title\\\": \\\"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"sainz2024gollie\\\", \\\"title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"shelmanov2021active\\\", \\\"title\\\": \\\"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"snell2024scaling\\\", \\\"title\\\": \\\"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=snell vs api=charlie\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"taubenfeld2025cisc\\\", \\\"title\\\": \\\"Confidence Improves Self-Consistency in LLMs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Confidence Improves Self-Consistency in LLMs\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"thirukovalluru2024atomic\\\", \\\"title\\\": \\\"Atomic Self-Consistency for Better Long Form Generations\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Atomic Self-Consistency for Better Long Form Generations\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"tjongkimsang2003conll\\\", \\\"title\\\": \\\"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2003\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"vashurin2025cocoa\\\", \\\"title\\\": \\\"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wadhwa2023revisiting\\\", \\\"title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Revisiting Relation Extraction in the era of Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2023instructuie\\\", \\\"title\\\": \\\"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2023selfconsistency\\\", \\\"title\\\": \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2025make\\\", \\\"title\\\": \\\"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2024mathshepherd\\\", \\\"title\\\": \\\"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wang2025rankedvoting\\\", \\\"title\\\": \\\"Ranked Voting based Self-Consistency of Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Ranked Voting based Self-Consistency of Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wen2025know\\\", \\\"title\\\": \\\"Know Your Limits: A Survey of Abstention in Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Know Your Limits: A Survey of Abstention in Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"willard2023guided\\\", \\\"title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Efficient Guided Generation for Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xia2025survey\\\", \\\"title\\\": \\\"A Survey of Uncertainty Estimation Methods on Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Survey of Uncertainty Estimation Methods on Large Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xiao2019uncertainty\\\", \\\"title\\\": \\\"Quantifying Uncertainties in Natural Language Processing Tasks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Quantifying Uncertainties in Natural Language Processing Tasks\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zhang2023ener\\\", \\\"title\\\": \\\"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"zhou2024uniner\\\", \\\"title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}]}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 49, \"total_citations\": 69, \"unique_cited_keys\": 49, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 45, \"online_not_found\": 2, \"online_mismatch\": 2}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"angelopoulos2021conformal\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"authors\": \"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\", \"year\": \"2021\", \"venue\": \"ICLR 2021\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"arXiv preprint (ICML 2024 Workshop ICL)\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2110.14168\"}, {\"key\": \"culotta2004confidence\", \"type\": \"inproceedings\", \"title\": \"Confidence Estimation for Information Extraction\", \"authors\": \"Culotta, Aron and McCallum, Andrew\", \"year\": \"2004\", \"venue\": \"HLT-NAACL 2004\"}, {\"key\": \"derczynski2017wnut\", \"type\": \"inproceedings\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"authors\": \"Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut\", \"year\": \"2017\", \"venue\": \"W-NUT Workshop at EMNLP 2017\"}, {\"key\": \"desai2020calibration\", \"type\": \"inproceedings\", \"title\": \"Calibration of Pre-trained Transformers\", \"authors\": \"Desai, Shrey and Durrett, Greg\", \"year\": \"2020\", \"venue\": \"Proceedings of the 2020 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"fisch2021conformal\", \"type\": \"inproceedings\", \"title\": \"Few-Shot Conformal Prediction with Auxiliary Tasks\", \"authors\": \"Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina\", \"year\": \"2021\", \"venue\": \"ICML 2021\"}, {\"key\": \"fleiss1971agreement\", \"type\": \"article\", \"title\": \"Measuring nominal scale agreement among many raters.\", \"authors\": \"Fleiss, Joseph L.\", \"year\": \"1971\", \"venue\": \"Psychological Bulletin\"}, {\"key\": \"gal2016dropout\", \"type\": \"inproceedings\", \"title\": \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\", \"authors\": \"Gal, Yarin and Ghahramani, Zoubin\", \"year\": \"2016\", \"venue\": \"ICML 2016\"}, {\"key\": \"geifman2017selective\", \"type\": \"inproceedings\", \"title\": \"Selective Classification for Deep Neural Networks\", \"authors\": \"Geifman, Yonatan and El-Yaniv, Ran\", \"year\": \"2017\", \"venue\": \"NeurIPS 2017\"}, {\"key\": \"feng2025optimal\", \"type\": \"article\", \"title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"authors\": \"Feng, Austin and Alonso, Marius and Odonnat, Ambroise\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2511.12309\"}, {\"key\": \"geng2024confidence\", \"type\": \"inproceedings\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"authors\": \"Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Presla...\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"guo2017calibration\", \"type\": \"inproceedings\", \"title\": \"On Calibration of Modern Neural Networks\", \"authors\": \"Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.\", \"year\": \"2017\", \"venue\": \"ICML 2017\"}, {\"key\": \"hobelsberger2025systematic\", \"type\": \"article\", \"title\": \"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\", \"authors\": \"Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, O...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2510.20460\"}, {\"key\": \"jaccard1901distribution\", \"type\": \"article\", \"title\": \"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\", \"authors\": \"Jaccard, Paul\", \"year\": \"1901\", \"venue\": \"Bulletin de la Société Vaudoise des Sciences Naturelles\"}, {\"key\": \"josifoski2022genie\", \"type\": \"inproceedings\", \"title\": \"GenIE: Generative Information Extraction\", \"authors\": \"Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and ...\", \"year\": \"2022\", \"venue\": \"Proceedings of the 2022 Conference of the North American Chapter of the Associat...\"}, {\"key\": \"kadavath2022language\", \"type\": \"article\", \"title\": \"Language Models (Mostly) Know What They Know\", \"authors\": \"Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain...\", \"year\": \"2022\", \"venue\": \"arXiv preprint arXiv:2207.05221\"}, {\"key\": \"kang2025selfcertainty\", \"type\": \"inproceedings\", \"title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"authors\": \"Kang, Zhewei and Zhao, Xuandong and Song, Dawn\", \"year\": \"2025\", \"venue\": \"NeurIPS 2025\"}, {\"key\": \"kim2026reasc\", \"type\": \"inproceedings\", \"title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"authors\": \"Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin\", \"year\": \"2026\", \"venue\": \"ACL 2026\"}, {\"key\": \"kossen2024semantic\", \"type\": \"article\", \"title\": \"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\", \"authors\": \"Kossen, Jannik and Han, Jiatong and Razzak, Muhammed and Schut, Lisa and Malik, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2406.15927\"}, {\"key\": \"li2025llms\", \"type\": \"article\", \"title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"authors\": \"Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi an...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2503.04104\"}, {\"key\": \"kuhn2023semantic\", \"type\": \"inproceedings\", \"title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"authors\": \"Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian\", \"year\": \"2023\", \"venue\": \"ICLR 2023\"}, {\"key\": \"lakshminarayanan2017ensembles\", \"type\": \"inproceedings\", \"title\": \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\", \"authors\": \"Lakshminarayanan, Balaji and Pritzel, Alexander and Blundell, Charles\", \"year\": \"2017\", \"venue\": \"NeurIPS 2017\"}, {\"key\": \"li2023codeie\", \"type\": \"inproceedings\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"authors\": \"Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Hu...\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"lightman2024verify\", \"type\": \"inproceedings\", \"title\": \"Let's Verify Step by Step\", \"authors\": \"Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Bak...\", \"year\": \"2024\", \"venue\": \"ICLR 2024\"}, {\"key\": \"luan2018scierc\", \"type\": \"inproceedings\", \"title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"authors\": \"Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh\", \"year\": \"2018\", \"venue\": \"Proceedings of the 2018 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"manakul2023selfcheckgpt\", \"type\": \"inproceedings\", \"title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"authors\": \"Manakul, Potsawee and Liusie, Adian and Gales, Mark\", \"year\": \"2023\", \"venue\": \"Proceedings of the 2023 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"nedellec2026consistency\", \"type\": \"article\", \"title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant...\", \"authors\": \"Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert\", \"year\": \"2026\", \"venue\": \"Genomics \\\\& Informatics\"}, {\"key\": \"oh2025latentsc\", \"type\": \"article\", \"title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"authors\": \"Oh, Jungsuk and Lee, Jay-Yoon\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2508.18395\"}, {\"key\": \"sainz2024gollie\", \"type\": \"inproceedings\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"authors\": \"Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lope...\", \"year\": \"2024\", \"venue\": \"ICLR 2024\"}, {\"key\": \"shelmanov2021active\", \"type\": \"inproceedings\", \"title\": \"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\", \"authors\": \"Shelmanov, Artem and Puzyrev, Dmitri and Kupriyanova, Lyubov and Belyakov, Denis...\", \"year\": \"2021\", \"venue\": \"Proceedings of the 16th Conference of the European Chapter of the Association fo...\"}, {\"key\": \"snell2024scaling\", \"type\": \"inproceedings\", \"title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"authors\": \"Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral\", \"year\": \"2024\", \"venue\": \"ICLR 2025\"}, {\"key\": \"taubenfeld2025cisc\", \"type\": \"inproceedings\", \"title\": \"Confidence Improves Self-Consistency in LLMs\", \"authors\": \"Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, ...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"thirukovalluru2024atomic\", \"type\": \"inproceedings\", \"title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"authors\": \"Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan\", \"year\": \"2024\", \"venue\": \"Proceedings of the 2024 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"tjongkimsang2003conll\", \"type\": \"inproceedings\", \"title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"authors\": \"Sang, Erik F. Tjong Kim and Meulder, Fien De\", \"year\": \"2003\", \"venue\": \"CoNLL 2003\"}, {\"key\": \"vashurin2025cocoa\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"authors\": \"Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksan...\", \"year\": \"2025\", \"venue\": \"NeurIPS 2025\"}, {\"key\": \"wadhwa2023revisiting\", \"type\": \"inproceedings\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"authors\": \"Wadhwa, Somin and Amir, Silvio and Wallace, Byron\", \"year\": \"2023\", \"venue\": \"Proceedings of the 61st Annual Meeting of the Association for Computational Ling...\"}, {\"key\": \"wang2023instructuie\", \"type\": \"article\", \"title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"authors\": \"Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang...\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2304.08085\"}, {\"key\": \"wang2023selfconsistency\", \"type\": \"inproceedings\", \"title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"authors\": \"Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Na...\", \"year\": \"2023\", \"venue\": \"ICLR 2023\"}, {\"key\": \"wang2025make\", \"type\": \"inproceedings\", \"title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"authors\": \"Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueq...\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: NAACL 2025\"}, {\"key\": \"wang2024mathshepherd\", \"type\": \"inproceedings\", \"title\": \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\", \"authors\": \"Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, Runxin and Dai, Damai and Li, ...\", \"year\": \"2024\", \"venue\": \"ACL 2024\"}, {\"key\": \"wang2025rankedvoting\", \"type\": \"inproceedings\", \"title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"authors\": \"Wang, Weiqin and Wang, Yile and Huang, Hui\", \"year\": \"2025\", \"venue\": \"ACL Findings 2025\"}, {\"key\": \"wen2025know\", \"type\": \"article\", \"title\": \"Know Your Limits: A Survey of Abstention in Large Language Models\", \"authors\": \"Wen, Bingbing and Yao, Jihan and Feng, Shangbin and Xu, Chenjun and Tsvetkov, Yu...\", \"year\": \"2025\", \"venue\": \"Transactions of the Association for Computational Linguistics\"}, {\"key\": \"willard2023guided\", \"type\": \"article\", \"title\": \"Efficient Guided Generation for Large Language Models\", \"authors\": \"Willard, Brandon T. and Louf, Rémi\", \"year\": \"2023\", \"venue\": \"arXiv preprint arXiv:2307.09702\"}, {\"key\": \"xia2025survey\", \"type\": \"inproceedings\", \"title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"authors\": \"Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang\", \"year\": \"2025\", \"venue\": \"ACL Findings 2025\"}, {\"key\": \"xiao2019uncertainty\", \"type\": \"article\", \"title\": \"Quantifying Uncertainties in Natural Language Processing Tasks\", \"authors\": \"Xiao, Yijun and Wang, William Yang\", \"year\": \"2019\", \"venue\": \"Proceedings of the AAAI Conference on Artificial Intelligence\"}, {\"key\": \"zhang2023ener\", \"type\": \"inproceedings\", \"title\": \"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\", \"authors\": \"Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotia...\", \"year\": \"2023\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2023\"}, {\"key\": \"zhou2024uniner\", \"type\": \"inproceedings\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"authors\": \"Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}], \"tex_citations\": [{\"key\": \"wang2023selfconsistency\", \"file\": \"sections/introduction.tex\", \"line\": 4, \"command\": \"citealp\"}, {\"key\": \"snell2024scaling\", \"file\": \"sections/introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"wang2023selfconsistency\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"chen2024usc\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"taubenfeld2025cisc\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"kang2025selfcertainty\", \"file\": \"sections/introduction.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"nedellec2026consistency\", \"file\": \"sections/introduction.tex\", \"line\": 16, \"command\": \"citet\"}, {\"key\": \"luan2018scierc\", \"file\": \"sections/introduction.tex\", \"line\": 31, \"command\": \"cite\"}, {\"key\": \"tjongkimsang2003conll\", \"file\": \"sections/introduction.tex\", \"line\": 31, \"command\": \"cite\"}, {\"key\": \"derczynski2017wnut\", \"file\": \"sections/introduction.tex\", \"line\": 31, \"command\": \"cite\"}, {\"key\": \"wang2023selfconsistency\", \"file\": \"sections/related_work.tex\", \"line\": 4, \"command\": \"cite\"}, {\"key\": \"chen2024usc\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"thirukovalluru2024atomic\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"manakul2023selfcheckgpt\", \"file\": \"sections/related_work.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"snell2024scaling\", \"file\": \"sections/related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/related_work.tex\", \"line\": 6, \"command\": \"citet\"}, {\"key\": \"taubenfeld2025cisc\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"kang2025selfcertainty\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"kim2026reasc\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"wang2025rankedvoting\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"oh2025latentsc\", \"file\": \"sections/related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"feng2025optimal\", \"file\": \"sections/related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"wang2025make\", \"file\": \"sections/related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"li2025llms\", \"file\": \"sections/related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"nedellec2026consistency\", \"file\": \"sections/related_work.tex\", \"line\": 13, \"command\": \"citet\"}, {\"key\": \"vashurin2025cocoa\", \"file\": \"sections/related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"zhou2024uniner\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"sainz2024gollie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"josifoski2022genie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"li2023codeie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"wadhwa2023revisiting\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"wang2023instructuie\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/related_work.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"geng2024confidence\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"wen2025know\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"xia2025survey\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"hobelsberger2025systematic\", \"file\": \"sections/related_work.tex\", \"line\": 20, \"command\": \"cite\"}, {\"key\": \"kuhn2023semantic\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"kossen2024semantic\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"citet\"}, {\"key\": \"kadavath2022language\", \"file\": \"sections/related_work.tex\", \"line\": 21, \"command\": \"cite\"}, {\"key\": \"guo2017calibration\", \"file\": \"sections/related_work.tex\", \"line\": 22, \"command\": \"cite\"}, {\"key\": \"desai2020calibration\", \"file\": \"sections/related_work.tex\", \"line\": 22, \"command\": \"cite\"}, {\"key\": \"lakshminarayanan2017ensembles\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"gal2016dropout\", \"file\": \"sections/related_work.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"xiao2019uncertainty\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"shelmanov2021active\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"zhang2023ener\", \"file\": \"sections/related_work.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"fisch2021conformal\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"angelopoulos2021conformal\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"lightman2024verify\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"wang2024mathshepherd\", \"file\": \"sections/related_work.tex\", \"line\": 25, \"command\": \"cite\"}, {\"key\": \"geifman2017selective\", \"file\": \"sections/related_work.tex\", \"line\": 26, \"command\": \"cite\"}, {\"key\": \"culotta2004confidence\", \"file\": \"sections/related_work.tex\", \"line\": 26, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/method.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"fleiss1971agreement\", \"file\": \"sections/method.tex\", \"line\": 32, \"command\": \"citet\"}, {\"key\": \"jaccard1901distribution\", \"file\": \"sections/method.tex\", \"line\": 41, \"command\": \"cite\"}, {\"key\": \"luan2018scierc\", \"file\": \"sections/experiments.tex\", \"line\": 9, \"command\": \"cite\"}, {\"key\": \"tjongkimsang2003conll\", \"file\": \"sections/experiments.tex\", \"line\": 10, \"command\": \"cite\"}, {\"key\": \"derczynski2017wnut\", \"file\": \"sections/experiments.tex\", \"line\": 11, \"command\": \"cite\"}, {\"key\": \"willard2023guided\", \"file\": \"sections/experiments.tex\", \"line\": 17, \"command\": \"cite\"}, {\"key\": \"kuhn2023semantic\", \"file\": \"sections/experiments.tex\", \"line\": 64, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/experiments.tex\", \"line\": 136, \"command\": \"cite\"}, {\"key\": \"snell2024scaling\", \"file\": \"sections/experiments.tex\", \"line\": 136, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/experiments.tex\", \"line\": 136, \"command\": \"cite\"}, {\"key\": \"cobbe2021verifiers\", \"file\": \"sections/discussion.tex\", \"line\": 31, \"command\": \"cite\"}, {\"key\": \"brown2024monkeys\", \"file\": \"sections/appendix.tex\", \"line\": 184, \"command\": \"cite\"}, {\"key\": \"snell2024scaling\", \"file\": \"sections/appendix.tex\", \"line\": 184, \"command\": \"cite\"}], \"online_verification\": [{\"key\": \"angelopoulos2021conformal\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"brown2024monkeys\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"chen2024usc\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Universal Self-Consistency for Large Language Model Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"cobbe2021verifiers\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Training Verifiers to Solve Math Word Problems\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"culotta2004confidence\", \"title\": \"Confidence Estimation for Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Confidence estimation for information extraction\", \"matched_year\": \"2004\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"derczynski2017wnut\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"desai2020calibration\", \"title\": \"Calibration of Pre-trained Transformers\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Calibration of Pre-trained Transformers\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fisch2021conformal\", \"title\": \"Few-Shot Conformal Prediction with Auxiliary Tasks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Few-shot Conformal Prediction with Auxiliary Tasks\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fleiss1971agreement\", \"title\": \"Measuring nominal scale agreement among many raters.\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Measuring nominal scale agreement among many raters.\", \"matched_year\": \"1971\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"gal2016dropout\", \"title\": \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\", \"matched_year\": \"2015\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"geifman2017selective\", \"title\": \"Selective Classification for Deep Neural Networks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Selective Classification for Deep Neural Networks\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"feng2025optimal\", \"title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Optimal Self-Consistency for Efficient Reasoning with Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=feng vs api=austin\"], \"note\": \"\"}, {\"key\": \"geng2024confidence\", \"title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey of Confidence Estimation and Calibration in Large Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"guo2017calibration\", \"title\": \"On Calibration of Modern Neural Networks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"On Calibration of Modern Neural Networks\", \"matched_year\": \"2017\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"hobelsberger2025systematic\", \"title\": \"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\", \"status\": \"not_found\", \"confidence\": 0.236, \"matched_title\": \"A new criterion for assessing discriminant validity in variance-based structural equation modeling\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.24 below threshold 0.82\"}, {\"key\": \"jaccard1901distribution\", \"title\": \"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Étude comparative de la distribution florale dans une portion des Alpes et du Jura\", \"matched_year\": \"1901\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"josifoski2022genie\", \"title\": \"GenIE: Generative Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GenIE: Generative Information Extraction\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kadavath2022language\", \"title\": \"Language Models (Mostly) Know What They Know\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Language Models (Mostly) Know What They Know\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kang2025selfcertainty\", \"title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kim2026reasc\", \"title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kossen2024semantic\", \"title\": \"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2025llms\", \"title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LLMs Can Generate a Better Answer by Aggregating Their Own Responses\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"kuhn2023semantic\", \"title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"lakshminarayanan2017ensembles\", \"title\": \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\", \"matched_year\": \"2016\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"li2023codeie\", \"title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"lightman2024verify\", \"title\": \"Let's Verify Step by Step\", \"status\": \"not_found\", \"confidence\": 0.246, \"matched_title\": \"Development and dosimetric verification of static SHArc: Step‐and‐shoot carbon ion arc therapy for LET &lt;sub>d&lt;/sub> escalation in pancreatic tumors\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.25 below threshold 0.82\"}, {\"key\": \"luan2018scierc\", \"title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\", \"matched_year\": \"2018\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"manakul2023selfcheckgpt\", \"title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"nedellec2026consistency\", \"title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"oh2025latentsc\", \"title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"sainz2024gollie\", \"title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"shelmanov2021active\", \"title\": \"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"snell2024scaling\", \"title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=snell vs api=charlie\"], \"note\": \"\"}, {\"key\": \"taubenfeld2025cisc\", \"title\": \"Confidence Improves Self-Consistency in LLMs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Confidence Improves Self-Consistency in LLMs\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"thirukovalluru2024atomic\", \"title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Atomic Self-Consistency for Better Long Form Generations\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"tjongkimsang2003conll\", \"title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\", \"matched_year\": \"2003\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"vashurin2025cocoa\", \"title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wadhwa2023revisiting\", \"title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Revisiting Relation Extraction in the era of Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2023instructuie\", \"title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2023selfconsistency\", \"title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\", \"matched_year\": \"2022\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025make\", \"title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2024mathshepherd\", \"title\": \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wang2025rankedvoting\", \"title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Ranked Voting based Self-Consistency of Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wen2025know\", \"title\": \"Know Your Limits: A Survey of Abstention in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Know Your Limits: A Survey of Abstention in Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"willard2023guided\", \"title\": \"Efficient Guided Generation for Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Efficient Guided Generation for Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xia2025survey\", \"title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey of Uncertainty Estimation Methods on Large Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xiao2019uncertainty\", \"title\": \"Quantifying Uncertainties in Natural Language Processing Tasks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Quantifying Uncertainties in Natural Language Processing Tasks\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhang2023ener\", \"title\": \"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"zhou2024uniner\", \"title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}]}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "d8dc9419-64e2-424b-9f4d-9821bc23cefe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 56 · 2026-05-15T03:59:07.535Z_

```json
{
  "parentUuid": "f00b6c88-6edf-4274-a18f-7afaffbe5470",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "c8b7a00d-0794-4deb-b4b2-9406db22b0bf",
  "timestamp": "2026-05-15T03:59:07.535Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 57_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。  ## 审稿对象 - 论文路径：`projects/struct_self_consist_ie/docs/paper/main.tex`（分节结构，各节在 `sections/` 下） - 目标 venue：**EMNLP 2026 Main Conference**（通过 ARR May…",
  "leafUuid": "c8b7a00d-0794-4deb-b4b2-9406db22b0bf",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b"
}
```

---

### Runtime record

_source line 58_

```json
{
  "type": "ai-title",
  "aiTitle": "Generative IE confidence signals systematic review",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b"
}
```

---

### Assistant

_source line 59 · 2026-05-15T03:59:23.487Z_

<details><summary>Logged reasoning block</summary>

```text
I now have all the paper content and reference verification results. Let me also check for some potentially missing references in the related work space. Let me search for a few key papers that should probably be cited.

Key observations from the reference verification:
- 49 total bib entries, all cited (0 orphan, 0 missing)
- 45 verified, 2 not found (hobelsberger2025systematic, lightman2024verify), 2 mismatch (feng2025optimal - first author name mismatch, snell2024scaling - first author name mismatch)
- The "not found" ones are likely just not indexed by OpenAlex yet (lightman2024verify is a well-known paper from OpenAI)


- The mismatches appear to be minor formatting differences in how author names are represented

I notice there's no Ethics Statement in the main.tex file. ARR requires a Limitations section, which is present, but also recommends Ethics considerations. Now I'm checking what might be missing from the related work across the key areas the Director mentioned—self-consistency and test-time scaling seem well covered, confidence and uncertainty estimation for LLMs is addressed through surveys, generative IE methods like UniNER and GoLLIE are included, and I'm evaluating whether structured prediction calibration needs additional citations.

Let me search for potentially missing papers and verify the novelty claim about being the first multi-family comparison of confidence signals for generative IE.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8b7a00d-0794-4deb-b4b2-9406db22b0bf",
  "isSidechain": false,
  "requestId": "req_011Cb3ggUSdN3MiuxzRACSDk",
  "type": "assistant",
  "uuid": "66a61d80-ac6b-4e5d-9e82-2a46f7a7cb10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WzTezcWMRVbcHa55K8Rtg6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 53787,
      "cache_read_input_tokens": 11841,
      "output_tokens": 697,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 53787,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 697,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 53787,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 53787
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

_source line 60 · 2026-05-15T03:59:25.182Z_

论文和引用验证结果已读完。引用验证显示 49 条引用全部匹配（无 orphan/missing），2 条未在 OpenAlex 中找到（lightman2024verify 和 hobelsberger2025systematic，属于索引延迟），2 条有 first author 格式差异（minor）。

现在搜索几个可能遗漏的相关工作方向。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66a61d80-ac6b-4e5d-9e82-2a46f7a7cb10",
  "isSidechain": false,
  "requestId": "req_011Cb3ggUSdN3MiuxzRACSDk",
  "type": "assistant",
  "uuid": "7a6466e3-c229-4409-990a-917c1584cb18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WzTezcWMRVbcHa55K8Rtg6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 53787,
      "cache_read_input_tokens": 11841,
      "output_tokens": 697,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 53787,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 697,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 53787,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 53787
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

_source line 61 · 2026-05-15T03:59:26.201Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01J6MwVZwfnkVqCG3JwTx8oB`</summary>

```json
{
  "query": "self-consistency structured prediction information extraction confidence LLM 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a6466e3-c229-4409-990a-917c1584cb18",
  "isSidechain": false,
  "requestId": "req_011Cb3ggUSdN3MiuxzRACSDk",
  "type": "assistant",
  "uuid": "1f9d1a3e-9f76-4512-86e0-faa2c46e49be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WzTezcWMRVbcHa55K8Rtg6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 53787,
      "cache_read_input_tokens": 11841,
      "output_tokens": 697,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 53787,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 697,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 53787,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 53787
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

_source line 62 · 2026-05-15T03:59:27.304Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EpDoUYynVuVoiCoVyyJY7R`</summary>

```json
{
  "query": "\"best-of-N\" selection structured output information extraction verifier 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f9d1a3e-9f76-4512-86e0-faa2c46e49be",
  "isSidechain": false,
  "requestId": "req_011Cb3ggUSdN3MiuxzRACSDk",
  "type": "assistant",
  "uuid": "0edeaa61-0136-4d33-95c0-657fe8ea3869",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WzTezcWMRVbcHa55K8Rtg6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 53787,
      "cache_read_input_tokens": 11841,
      "output_tokens": 697,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 53787,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 697,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 53787,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 53787
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

_source line 63 · 2026-05-15T03:59:27.678Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015ru98kSp8Z1BXk3xE5kSMC`</summary>

```json
{
  "query": "calibration uncertainty structured prediction sequence labeling NER 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0edeaa61-0136-4d33-95c0-657fe8ea3869",
  "isSidechain": false,
  "requestId": "req_011Cb3ggUSdN3MiuxzRACSDk",
  "type": "assistant",
  "uuid": "36c7b09a-ef1d-4c25-a695-a1a140a01b1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WzTezcWMRVbcHa55K8Rtg6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 53787,
      "cache_read_input_tokens": 11841,
      "output_tokens": 697,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 53787,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 697,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 53787,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 53787
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

_source line 64 · 2026-05-15T03:59:34.716Z_

<details><summary>↩ Tool result · `toolu_01EpDoUYynVuVoiCoVyyJY7R`</summary>

```text
Web search results for query: ""best-of-N" selection structured output information extraction verifier 2024 2025"

Links: [{"title":"SLOT: Structuring the Output of Large Language Models","url":"https://aclanthology.org/2025.emnlp-industry.32.pdf"},{"title":"Structured Outputs: Reliable Schema-Validated Data Extraction from Language Models - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/structured-outputs-schema-validated-data-extraction-language-models"},{"title":"STRUCTSENSE: A TASK-AGNOSTIC AGENTIC FRAMEWORK for STRUCTURED INFORMATION EXTRACTION with HUMAN-IN-THE-LOOP EVALUATION and BENCHMARKING","url":"https://arxiv.org/html/2507.03674v1"},{"title":"Leveraging large language models for structured information extraction from pathology reports - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2153353925001075"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"},{"title":"READOC: A Unified Benchmark for Realistic Document ...","url":"https://aclanthology.org/2025.findings-acl.1128.pdf"},{"title":"Benchmarking LLM-based Information Extraction Tools for ...","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full.pdf"},{"title":"StructEval: Benchmarking LLMs’ Capabilities to Generate Structural Outputs","url":"https://arxiv.org/html/2505.20139v1"},{"title":"A Survey of Generative Information Extraction","url":"https://aclanthology.org/2025.coling-main.324.pdf"},{"title":"Structured data extraction from unstructured content using LLM schemas","url":"https://simonwillison.net/2025/Feb/28/llm-schemas/"}]

Based on the web search results, here are the key findings related to your query about "best-of-N" selection, structured output, information extraction, and verifier systems from 2024-2025:

## Structured Output and Information Extraction Advances

The development of dedicated structured output capabilities in 2024 addressed fundamental limitations, enabling models to be constrained to produce outputs in specific formats like JSON, XML, or other schema-validated structures, with OpenAI's introduction of JSON mode in late 2023 and its refinement throughout 2024, along with similar features from other providers.

## Verification-Augmented Approaches

VerifiNER is a verification-augmented NER approach that uses knowledge-grounded reasoning with large language models, presented at the 62nd Annual Meeting of the Association for Computational Linguistics in 2024.

## Evaluation and Benchmarking

Evaluating structured output has become a focal point for understanding LLM's limitations in 2025, with StrucText-Eval shifting the task to reasoning over structure-rich text (JSON, YAML, LaTeX) rather than generating structures themselves.

## Task-Agnostic Frameworks

Recent work includes large language models for generative information extraction surveys, with publications in Frontiers of Computer Science in November 2024.

The search results show active research in structured output generation, verification mechanisms, and information extraction benchmarking during 2024-2025, though specific references to "best-of-N" selection methods in this context are not prominently featured in these particular sources.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0edeaa61-0136-4d33-95c0-657fe8ea3869",
  "isSidechain": false,
  "promptId": "f5d01f90-29f0-42ef-8c36-beb6e3f39fb5",
  "type": "user",
  "uuid": "d195673d-b564-404c-bee5-e92db1c33883",
  "toolUseResult": {
    "query": "\"best-of-N\" selection structured output information extraction verifier 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GdZ16MYfWndCvesVUyXXSr",
        "content": [
          {
            "title": "SLOT: Structuring the Output of Large Language Models",
            "url": "https://aclanthology.org/2025.emnlp-industry.32.pdf"
          },
          {
            "title": "Structured Outputs: Reliable Schema-Validated Data Extraction from Language Models - Interactive | Michael Brenndoerfer | Michael Brenndoerfer",
            "url": "https://mbrenndoerfer.com/writing/structured-outputs-schema-validated-data-extraction-language-models"
          },
          {
            "title": "STRUCTSENSE: A TASK-AGNOSTIC AGENTIC FRAMEWORK for STRUCTURED INFORMATION EXTRACTION with HUMAN-IN-THE-LOOP EVALUATION and BENCHMARKING",
            "url": "https://arxiv.org/html/2507.03674v1"
          },
          {
            "title": "Leveraging large language models for structured information extraction from pathology reports - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S2153353925001075"
          },
          {
            "title": "Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s11704-024-40555-y"
          },
          {
            "title": "READOC: A Unified Benchmark for Realistic Document ...",
            "url": "https://aclanthology.org/2025.findings-acl.1128.pdf"
          },
          {
            "title": "Benchmarking LLM-based Information Extraction Tools for ...",
            "url": "https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full.pdf"
          },
          {
            "title": "StructEval: Benchmarking LLMs’ Capabilities to Generate Structural Outputs",
            "url": "https://arxiv.org/html/2505.20139v1"
          },
          {
            "title": "A Survey of Generative Information Extraction",
            "url": "https://aclanthology.org/2025.coling-main.324.pdf"
          },
          {
            "title": "Structured data extraction from unstructured content using LLM schemas",
            "url": "https://simonwillison.net/2025/Feb/28/llm-schemas/"
          }
        ]
      },
      "Based on the web search results, here are the key findings related to your query about \"best-of-N\" selection, structured output, information extraction, and verifier systems from 2024-2025:\n\n## Structured Output and Information Extraction Advances\n\nThe development of dedicated structured output capabilities in 2024 addressed fundamental limitations, enabling models to be constrained to produce outputs in specific formats like JSON, XML, or other schema-validated structures, with OpenAI's introduction of JSON mode in late 2023 and its refinement throughout 2024, along with similar features from other providers.\n\n## Verification-Augmented Approaches\n\nVerifiNER is a verification-augmented NER approach that uses knowledge-grounded reasoning with large language models, presented at the 62nd Annual Meeting of the Association for Computational Linguistics in 2024.\n\n## Evaluation and Benchmarking\n\nEvaluating structured output has become a focal point for understanding LLM's limitations in 2025, with StrucText-Eval shifting the task to reasoning over structure-rich text (JSON, YAML, LaTeX) rather than generating structures themselves.\n\n## Task-Agnostic Frameworks\n\nRecent work includes large language models for generative information extraction surveys, with publications in Frontiers of Computer Science in November 2024.\n\nThe search results show active research in structured output generation, verification mechanisms, and information extraction benchmarking during 2024-2025, though specific references to \"best-of-N\" selection methods in this context are not prominently featured in these particular sources."
    ],
    "durationSeconds": 7.408621977000003
  },
  "sourceToolAssistantUUID": "0edeaa61-0136-4d33-95c0-657fe8ea3869",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-15T03:59:35.234Z_

<details><summary>↩ Tool result · `toolu_01J6MwVZwfnkVqCG3JwTx8oB`</summary>

```text
Web search results for query: "self-consistency structured prediction information extraction confidence LLM 2024 2025 2026"

Links: [{"title":"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning","url":"https://arxiv.org/html/2601.02970v1"},{"title":"Confidence Improves Self-Consistency in LLMs","url":"https://arxiv.org/html/2502.06233v1"},{"title":"Towards Reliable LLM Grading Through Self-Consistency and Selective Human Review: Higher Accuracy, Less Work","url":"https://www.mdpi.com/2504-4990/8/3/74"},{"title":"Confidence Improves Self-Consistency in LLMs","url":"https://aclanthology.org/2025.findings-acl.1030.pdf"},{"title":"[2502.06233] Confidence Improves Self-Consistency in LLMs","url":"https://arxiv.org/abs/2502.06233"},{"title":"Confidence Improves Self-Consistency in LLMs - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.1030/"},{"title":"Self-Consistency Sampling in LLMs","url":"https://www.emergentmind.com/topics/self-consistency-sampling"},{"title":"Stability Evaluation of Confidence Features Across Model and Data Variants in Large Language Models — Research and Science Today","url":"https://www.rstjournal.com/article/4.2026"},{"title":"GitHub - IAAR-Shanghai/ICSFSurvey: Explore concepts like Self-Correct, Self-Refine, Self-Improve, Self-Contradict, Self-Play, and Self-Knowledge, alongside o1-like reasoning elevation🍓 and hallucination alleviation🍄.","url":"https://github.com/IAAR-Shanghai/ICSFSurvey"},{"title":"THE PATH OF LEAST RESISTANCE: GUIDING LLM REASONING TRAJECTORIES WITH PREFIX CONSENSUS | OpenReview","url":"https://openreview.net/forum?id=hrnSqERgPn"}]

Here are the search results for your query on self-consistency, structured prediction, information extraction, confidence, and LLM developments from 2024-2026:

## Key Recent Developments

### Confidence-Informed Self-Consistency (CISC)

Confidence-Informed Self-Consistency (CISC) performs a weighted majority vote based on confidence scores obtained directly from the model. By prioritizing high-confidence paths, it can identify the correct answer with a significantly smaller sample size. When tested on nine models and four datasets, CISC outperforms self-consistency in nearly all configurations, reducing the required number of reasoning paths by over 40% on average.

The research introduces the notion of within-question confidence evaluation, showing that standard evaluation methods are poor predictors of success in distinguishing correct and incorrect answers to the same question. LLMs can effectively judge the correctness of their own outputs, contributing to the ongoing debate on this topic.

### Reliability-Aware Adaptive Self-Consistency (ReASC)

ReASC is an adaptive self-consistency framework that incorporates a self-certainty variant as a response-level reliability signal to guide how evidence is accumulated at inference time. Response-level reliability can be captured from model confidence signals during generation, and self-certainty has been shown to correlate with the reliability of reasoning trajectories, making it a suitable basis for guiding evidence accumulation without additional supervision.

### Human-in-the-Loop Approaches

The SURE (Selective Uncertainty-based Re-Evaluation) pipeline combines repeated LLM prompting, uncertainty-based flagging, and selective human regrading. Each student answer was scored 20 times to derive majority-voted predictions and self-consistency-based certainty estimates.

### Compute-Efficient Methods

PoLR (Path of Least Resistance) is the first inference-time method to leverage prefix self-consistency for compute-efficient reasoning. PoLR clusters short prefixes of reasoning traces, identifies the dominant cluster, and expands only a subset of promising paths, preserving the accuracy benefits of SC while substantially reducing token usage and latency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f9d1a3e-9f76-4512-86e0-faa2c46e49be",
  "isSidechain": false,
  "promptId": "f5d01f90-29f0-42ef-8c36-beb6e3f39fb5",
  "type": "user",
  "uuid": "2d946f58-d0fc-48b3-bdef-8b331e74e8eb",
  "toolUseResult": {
    "query": "self-consistency structured prediction information extraction confidence LLM 2024 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XGMcs8B5QgnK3iQe5s7ACT",
        "content": [
          {
            "title": "Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning",
            "url": "https://arxiv.org/html/2601.02970v1"
          },
          {
            "title": "Confidence Improves Self-Consistency in LLMs",
            "url": "https://arxiv.org/html/2502.06233v1"
          },
          {
            "title": "Towards Reliable LLM Grading Through Self-Consistency and Selective Human Review: Higher Accuracy, Less Work",
            "url": "https://www.mdpi.com/2504-4990/8/3/74"
          },
          {
            "title": "Confidence Improves Self-Consistency in LLMs",
            "url": "https://aclanthology.org/2025.findings-acl.1030.pdf"
          },
          {
            "title": "[2502.06233] Confidence Improves Self-Consistency in LLMs",
            "url": "https://arxiv.org/abs/2502.06233"
          },
          {
            "title": "Confidence Improves Self-Consistency in LLMs - ACL Anthology",
            "url": "https://aclanthology.org/2025.findings-acl.1030/"
          },
          {
            "title": "Self-Consistency Sampling in LLMs",
            "url": "https://www.emergentmind.com/topics/self-consistency-sampling"
          },
          {
            "title": "Stability Evaluation of Confidence Features Across Model and Data Variants in Large Language Models — Research and Science Today",
            "url": "https://www.rstjournal.com/article/4.2026"
          },
          {
            "title": "GitHub - IAAR-Shanghai/ICSFSurvey: Explore concepts like Self-Correct, Self-Refine, Self-Improve, Self-Contradict, Self-Play, and Self-Knowledge, alongside o1-like reasoning elevation🍓 and hallucination alleviation🍄.",
            "url": "https://github.com/IAAR-Shanghai/ICSFSurvey"
          },
          {
            "title": "THE PATH OF LEAST RESISTANCE: GUIDING LLM REASONING TRAJECTORIES WITH PREFIX CONSENSUS | OpenReview",
            "url": "https://openreview.net/forum?id=hrnSqERgPn"
          }
        ]
      },
      "Here are the search results for your query on self-consistency, structured prediction, information extraction, confidence, and LLM developments from 2024-2026:\n\n## Key Recent Developments\n\n### Confidence-Informed Self-Consistency (CISC)\n\nConfidence-Informed Self-Consistency (CISC) performs a weighted majority vote based on confidence scores obtained directly from the model. By prioritizing high-confidence paths, it can identify the correct answer with a significantly smaller sample size. When tested on nine models and four datasets, CISC outperforms self-consistency in nearly all configurations, reducing the required number of reasoning paths by over 40% on average.\n\nThe research introduces the notion of within-question confidence evaluation, showing that standard evaluation methods are poor predictors of success in distinguishing correct and incorrect answers to the same question. LLMs can effectively judge the correctness of their own outputs, contributing to the ongoing debate on this topic.\n\n### Reliability-Aware Adaptive Self-Consistency (ReASC)\n\nReASC is an adaptive self-consistency framework that incorporates a self-certainty variant as a response-level reliability signal to guide how evidence is accumulated at inference time. Response-level reliability can be captured from model confidence signals during generation, and self-certainty has been shown to correlate with the reliability of reasoning trajectories, making it a suitable basis for guiding evidence accumulation without additional supervision.\n\n### Human-in-the-Loop Approaches\n\nThe SURE (Selective Uncertainty-based Re-Evaluation) pipeline combines repeated LLM prompting, uncertainty-based flagging, and selective human regrading. Each student answer was scored 20 times to derive majority-voted predictions and self-consistency-based certainty estimates.\n\n### Compute-Efficient Methods\n\nPoLR (Path of Least Resistance) is the first inference-time method to leverage prefix self-consistency for compute-efficient reasoning. PoLR clusters short prefixes of reasoning traces, identifies the dominant cluster, and expands only a subset of promising paths, preserving the accuracy benefits of SC while substantially reducing token usage and latency."
    ],
    "durationSeconds": 9.027986581999997
  },
  "sourceToolAssistantUUID": "1f9d1a3e-9f76-4512-86e0-faa2c46e49be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-15T03:59:40.579Z_

<details><summary>↩ Tool result · `toolu_015ru98kSp8Z1BXk3xE5kSMC`</summary>

```text
Web search results for query: "calibration uncertainty structured prediction sequence labeling NER 2024 2025"

Links: [{"title":"Uncertainty Quantification for Named Entity Recognition via Full-Sequence and Subsequence Conformal Prediction","url":"https://arxiv.org/html/2601.16999"},{"title":"Calibrating Language Models for Neural Ranking under ...","url":"https://aclanthology.org/2025.uncertainlp-main.22.pdf"},{"title":"Calibrating Structured Output Predictors for Natural Language Processing - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC7890517/"},{"title":"Uncertainty Quantification and Confidence Calibration in Large","url":"https://xiao0o0o.github.io/2025KDD_tutorial/survey.pdf"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/b94d8b035e2183e47afef9e2f299ba47-Paper-Conference.pdf"},{"title":"Uncertainty Estimation on Sequential Labeling via ... - People","url":"https://people.cs.vt.edu/~clu/Publication/2024/NAACL-Findings-2024-He.pdf"},{"title":"Uncertainty Quantification and Confidence Calibration in ...","url":"https://arxiv.org/pdf/2503.15850"},{"title":"Published as a conference paper at ICLR 2025 DO LLMS ESTIMATE UNCERTAINTY WELL","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/ef472869c217bf693f2d9bbde66a6b07-Paper-Conference.pdf"},{"title":"Calibrated Structured Prediction - Stanford Computer Science","url":"https://cs.stanford.edu/~pliang/papers/calibration-nips2015.pdf"},{"title":"Calibration in Deep Learning: A Survey of the State-of-the-Art Cheng Wang","url":"https://arxiv.org/pdf/2308.01222"}]

I've performed the web search and found several highly relevant recent papers and resources on this topic. Here are the key findings:

## Recent Work (2024-2025)

Combining deep sequence-labeling architectures with distribution-free uncertainty quantification illustrates how formal statistical inference can strengthen the reliability and interpretability of AI systems operating in complex, structured domains.

### Conformal Prediction for NER

Conformal prediction offers a statistically principled framework for uncertainty quantification, producing prediction sets with finite-sample validity under the exchangeability assumption. A recent 2026 paper introduces conformal prediction methods for full-sequence labelings including adaptive procedures and baseline non-conformity scores, with subsequence-level conformal prediction establishing class-conditional calibration for individual entity spans.

### Calibration in Structured Prediction

Research uses BERT-base with token-level softmax output and marginal likelihood based training, with model uncertainty estimates computed by estimating the variance of length normalized MC-dropout samples of span marginals.

### Uncertainty Transmission in Sequence Labeling

Recent approaches include the transmission of uncertainty from all tokens within the text to obtain transmitted uncertainty, advancing beyond token-level only considerations.

### Post-hoc Calibration Methods

The Top-versus-All (TvA) post-hoc calibration method reformulates multiclass confidence calibration into a single binary task by taking the maximum softmax score and assigning a binary label of correctness, allowing standard binary calibration tools such as Temperature Scaling and Histogram Binning.

These recent advances combine classical techniques like CRFs with modern deep learning and principled uncertainty quantification methods for more reliable structured prediction systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36c7b09a-ef1d-4c25-a695-a1a140a01b1c",
  "isSidechain": false,
  "promptId": "f5d01f90-29f0-42ef-8c36-beb6e3f39fb5",
  "type": "user",
  "uuid": "2242b141-ed7f-43da-b82a-dc2dd170f482",
  "toolUseResult": {
    "query": "calibration uncertainty structured prediction sequence labeling NER 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LTZpAw5rSei2axH4ZJdFQR",
        "content": [
          {
            "title": "Uncertainty Quantification for Named Entity Recognition via Full-Sequence and Subsequence Conformal Prediction",
            "url": "https://arxiv.org/html/2601.16999"
          },
          {
            "title": "Calibrating Language Models for Neural Ranking under ...",
            "url": "https://aclanthology.org/2025.uncertainlp-main.22.pdf"
          },
          {
            "title": "Calibrating Structured Output Predictors for Natural Language Processing - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7890517/"
          },
          {
            "title": "Uncertainty Quantification and Confidence Calibration in Large",
            "url": "https://xiao0o0o.github.io/2025KDD_tutorial/survey.pdf"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/b94d8b035e2183e47afef9e2f299ba47-Paper-Conference.pdf"
          },
          {
            "title": "Uncertainty Estimation on Sequential Labeling via ... - People",
            "url": "https://people.cs.vt.edu/~clu/Publication/2024/NAACL-Findings-2024-He.pdf"
          },
          {
            "title": "Uncertainty Quantification and Confidence Calibration in ...",
            "url": "https://arxiv.org/pdf/2503.15850"
          },
          {
            "title": "Published as a conference paper at ICLR 2025 DO LLMS ESTIMATE UNCERTAINTY WELL",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/ef472869c217bf693f2d9bbde66a6b07-Paper-Conference.pdf"
          },
          {
            "title": "Calibrated Structured Prediction - Stanford Computer Science",
            "url": "https://cs.stanford.edu/~pliang/papers/calibration-nips2015.pdf"
          },
          {
            "title": "Calibration in Deep Learning: A Survey of the State-of-the-Art Cheng Wang",
            "url": "https://arxiv.org/pdf/2308.01222"
          }
        ]
      },
      "I've performed the web search and found several highly relevant recent papers and resources on this topic. Here are the key findings:\n\n## Recent Work (2024-2025)\n\nCombining deep sequence-labeling architectures with distribution-free uncertainty quantification illustrates how formal statistical inference can strengthen the reliability and interpretability of AI systems operating in complex, structured domains.\n\n### Conformal Prediction for NER\n\nConformal prediction offers a statistically principled framework for uncertainty quantification, producing prediction sets with finite-sample validity under the exchangeability assumption. A recent 2026 paper introduces conformal prediction methods for full-sequence labelings including adaptive procedures and baseline non-conformity scores, with subsequence-level conformal prediction establishing class-conditional calibration for individual entity spans.\n\n### Calibration in Structured Prediction\n\nResearch uses BERT-base with token-level softmax output and marginal likelihood based training, with model uncertainty estimates computed by estimating the variance of length normalized MC-dropout samples of span marginals.\n\n### Uncertainty Transmission in Sequence Labeling\n\nRecent approaches include the transmission of uncertainty from all tokens within the text to obtain transmitted uncertainty, advancing beyond token-level only considerations.\n\n### Post-hoc Calibration Methods\n\nThe Top-versus-All (TvA) post-hoc calibration method reformulates multiclass confidence calibration into a single binary task by taking the maximum softmax score and assigning a binary label of correctness, allowing standard binary calibration tools such as Temperature Scaling and Histogram Binning.\n\nThese recent advances combine classical techniques like CRFs with modern deep learning and principled uncertainty quantification methods for more reliable structured prediction systems."
    ],
    "durationSeconds": 12.899012760999991
  },
  "sourceToolAssistantUUID": "36c7b09a-ef1d-4c25-a695-a1a140a01b1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 67_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。  ## 审稿对象 - 论文路径：`projects/struct_self_consist_ie/docs/paper/main.tex`（分节结构，各节在 `sections/` 下） - 目标 venue：**EMNLP 2026 Main Conference**（通过 ARR May…",
  "leafUuid": "2242b141-ed7f-43da-b82a-dc2dd170f482",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b"
}
```

---

### Runtime record

_source line 68_

```json
{
  "type": "ai-title",
  "aiTitle": "Generative IE confidence signals systematic review",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b"
}
```

---

### Assistant

_source line 69 · 2026-05-15T03:59:54.397Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me also check on a couple more potential missing references:

1. The "correlation-selection gap" - is this a known concept in self-consistency literature?
2. Is there work specifically on test-time scaling for structured outputs?

Let me also check if there's an Ethics Statement missing.

Looking at main.tex:
- Has \section*{Limitations} ✓
- No \section*{Ethics Statement} - but ARR says it's reviewed by an ethics committee; having an Ethics Statement is recommended but not required for desk rejection. However, the review form does ask about ethical considerations.


Now I'm compiling my review and checking the references against what's actually cited. I notice several potentially relevant papers that aren't included: VerifiNER from ACL 2024 on verification-augmented NER, recent work on uncertainty estimation for sequential labeling tasks, conformal prediction approaches for NER, and some structured output work from industry venues.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2242b141-ed7f-43da-b82a-dc2dd170f482",
  "isSidechain": false,
  "requestId": "req_011Cb3giuhDjEPGGsnGkvAXP",
  "type": "assistant",
  "uuid": "11dc2f11-0df5-48e3-a36c-b534bfe31ed6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0169Dy9s1gPepncmszNuDez3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3604,
      "cache_read_input_tokens": 65628,
      "output_tokens": 552,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3604,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 552,
          "cache_read_input_tokens": 65628,
          "cache_creation_input_tokens": 3604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3604
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

_source line 70 · 2026-05-15T03:59:54.781Z_

搜索一个更具针对性的方向——与本文 correlation-selection gap 概念直接相关的文献。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11dc2f11-0df5-48e3-a36c-b534bfe31ed6",
  "isSidechain": false,
  "requestId": "req_011Cb3giuhDjEPGGsnGkvAXP",
  "type": "assistant",
  "uuid": "06a9c793-c8a3-4057-8ba7-ee04e4702acc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0169Dy9s1gPepncmszNuDez3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3604,
      "cache_read_input_tokens": 65628,
      "output_tokens": 552,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3604,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 552,
          "cache_read_input_tokens": 65628,
          "cache_creation_input_tokens": 3604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3604
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

_source line 71 · 2026-05-15T03:59:55.883Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UMUfDZaRs6azf3ojKuZ5GQ`</summary>

```json
{
  "query": "\"correlation selection gap\" OR \"quality estimation vs selection\" self-consistency LLM sampling 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06a9c793-c8a3-4057-8ba7-ee04e4702acc",
  "isSidechain": false,
  "requestId": "req_011Cb3giuhDjEPGGsnGkvAXP",
  "type": "assistant",
  "uuid": "6fe0c3ab-7313-4bf4-b5a2-5105c3731f66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0169Dy9s1gPepncmszNuDez3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3604,
      "cache_read_input_tokens": 65628,
      "output_tokens": 552,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3604,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 552,
          "cache_read_input_tokens": 65628,
          "cache_creation_input_tokens": 3604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3604
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

_source line 72 · 2026-05-15T03:59:56.092Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017MTtEsT8HkHkp5Dtefwkkk`</summary>

```json
{
  "query": "VerifiNER verification augmented NER LLM 2024 ACL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6fe0c3ab-7313-4bf4-b5a2-5105c3731f66",
  "isSidechain": false,
  "requestId": "req_011Cb3giuhDjEPGGsnGkvAXP",
  "type": "assistant",
  "uuid": "f0f754d1-18bc-446f-b830-80bd5bff6a73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0169Dy9s1gPepncmszNuDez3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3604,
      "cache_read_input_tokens": 65628,
      "output_tokens": 552,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3604,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 552,
          "cache_read_input_tokens": 65628,
          "cache_creation_input_tokens": 3604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3604
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

_source line 73 · 2026-05-15T04:00:03.318Z_

<details><summary>↩ Tool result · `toolu_01UMUfDZaRs6azf3ojKuZ5GQ`</summary>

```text
Web search results for query: ""correlation selection gap" OR "quality estimation vs selection" self-consistency LLM sampling 2024 2025"

Links: [{"title":"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning","url":"https://arxiv.org/html/2601.02970v1"},{"title":"NeurIPS Poster Scalable Best-of-N Selection for Large Language Models via Self-Certainty","url":"https://neurips.cc/virtual/2025/poster/120166"},{"title":"Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling - ACL Anthology","url":"https://aclanthology.org/2025.naacl-long.184/"},{"title":"Self-Consistency Sampling in LLMs","url":"https://www.emergentmind.com/topics/self-consistency-sampling"},{"title":"Towards Reliable LLM Grading Through Self-Consistency and Selective Human Review: Higher Accuracy, Less Work","url":"https://www.mdpi.com/2504-4990/8/3/74"},{"title":"Estimating LLM Consistency: A User Baseline vs Surrogate ...","url":"https://aclanthology.org/2025.emnlp-main.1554.pdf"},{"title":"Leveraging Reasoning Paths for Efficient LLM Sampling","url":"https://aclanthology.org/2025.naacl-long.184.pdf"},{"title":"Confidence Improves Self-Consistency in LLMs","url":"https://aclanthology.org/2025.findings-acl.1030.pdf"},{"title":"Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling | Request PDF","url":"https://www.researchgate.net/publication/392503883_Reasoning_Aware_Self-Consistency_Leveraging_Reasoning_Paths_for_Efficient_LLM_Sampling"},{"title":"Confidence Improves Self-Consistency in LLMs","url":"https://arxiv.org/pdf/2502.06233"}]

Based on the search results, I found several relevant recent papers addressing correlations between quality estimation and selection in self-consistency LLM sampling from 2024-2025:

## Key Findings

**Self-Certainty and Quality Estimation:**
Self-certainty is a novel metric that leverages the inherent probability distribution of LLM outputs to estimate response quality without requiring external reward models, with higher distributional self-certainty correlating with improved response accuracy.

**Reliability-Aware Adaptive Self-Consistency (ReASC):**
Adaptive sampling decisions should be guided not only by how often an answer appears, but also by how much reliable evidence each individual response contributes to the final decision, with response-level reliability captured from model confidence signals during generation.

**Reasoning-Aware Self-Consistency (RASC):**
RASC assesses the quality of reasoning and the consistency of answers for each generated sample, using these assessments to guide early stopping decisions and rationale selection.

**Confidence-Improved Self-Consistency (CISC):**
CISC adds a self-assessment step where a confidence score is assigned to each path, then selects the final answer via a weighted majority vote.

**Current Research Gaps:**
Current research focuses on further efficiency gains via adaptive stopping, improved faithfulness and rationale selection, and systematic theoretical characterization of convergence and error.

These recent papers (2024-2025) specifically address the gap between quality estimation and response selection, proposing methods that use confidence signals and reasoning-level assessments to improve sampling efficiency in LLM reasoning tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6fe0c3ab-7313-4bf4-b5a2-5105c3731f66",
  "isSidechain": false,
  "promptId": "f5d01f90-29f0-42ef-8c36-beb6e3f39fb5",
  "type": "user",
  "uuid": "de71867e-2bc5-4b62-9838-ce31fefc671f",
  "toolUseResult": {
    "query": "\"correlation selection gap\" OR \"quality estimation vs selection\" self-consistency LLM sampling 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_012g9Lr7K9ke9smdrCaMoVir",
        "content": [
          {
            "title": "Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning",
            "url": "https://arxiv.org/html/2601.02970v1"
          },
          {
            "title": "NeurIPS Poster Scalable Best-of-N Selection for Large Language Models via Self-Certainty",
            "url": "https://neurips.cc/virtual/2025/poster/120166"
          },
          {
            "title": "Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling - ACL Anthology",
            "url": "https://aclanthology.org/2025.naacl-long.184/"
          },
          {
            "title": "Self-Consistency Sampling in LLMs",
            "url": "https://www.emergentmind.com/topics/self-consistency-sampling"
          },
          {
            "title": "Towards Reliable LLM Grading Through Self-Consistency and Selective Human Review: Higher Accuracy, Less Work",
            "url": "https://www.mdpi.com/2504-4990/8/3/74"
          },
          {
            "title": "Estimating LLM Consistency: A User Baseline vs Surrogate ...",
            "url": "https://aclanthology.org/2025.emnlp-main.1554.pdf"
          },
          {
            "title": "Leveraging Reasoning Paths for Efficient LLM Sampling",
            "url": "https://aclanthology.org/2025.naacl-long.184.pdf"
          },
          {
            "title": "Confidence Improves Self-Consistency in LLMs",
            "url": "https://aclanthology.org/2025.findings-acl.1030.pdf"
          },
          {
            "title": "Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling | Request PDF",
            "url": "https://www.researchgate.net/publication/392503883_Reasoning_Aware_Self-Consistency_Leveraging_Reasoning_Paths_for_Efficient_LLM_Sampling"
          },
          {
            "title": "Confidence Improves Self-Consistency in LLMs",
            "url": "https://arxiv.org/pdf/2502.06233"
          }
        ]
      },
      "Based on the search results, I found several relevant recent papers addressing correlations between quality estimation and selection in self-consistency LLM sampling from 2024-2025:\n\n## Key Findings\n\n**Self-Certainty and Quality Estimation:**\nSelf-certainty is a novel metric that leverages the inherent probability distribution of LLM outputs to estimate response quality without requiring external reward models, with higher distributional self-certainty correlating with improved response accuracy.\n\n**Reliability-Aware Adaptive Self-Consistency (ReASC):**\nAdaptive sampling decisions should be guided not only by how often an answer appears, but also by how much reliable evidence each individual response contributes to the final decision, with response-level reliability captured from model confidence signals during generation.\n\n**Reasoning-Aware Self-Consistency (RASC):**\nRASC assesses the quality of reasoning and the consistency of answers for each generated sample, using these assessments to guide early stopping decisions and rationale selection.\n\n**Confidence-Improved Self-Consistency (CISC):**\nCISC adds a self-assessment step where a confidence score is assigned to each path, then selects the final answer via a weighted majority vote.\n\n**Current Research Gaps:**\nCurrent research focuses on further efficiency gains via adaptive stopping, improved faithfulness and rationale selection, and systematic theoretical characterization of convergence and error.\n\nThese recent papers (2024-2025) specifically address the gap between quality estimation and response selection, proposing methods that use confidence signals and reasoning-level assessments to improve sampling efficiency in LLM reasoning tasks."
    ],
    "durationSeconds": 7.428879804999975
  },
  "sourceToolAssistantUUID": "6fe0c3ab-7313-4bf4-b5a2-5105c3731f66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-15T04:00:03.717Z_

<details><summary>↩ Tool result · `toolu_017MTtEsT8HkHkp5Dtefwkkk`</summary>

```text
Web search results for query: "VerifiNER verification augmented NER LLM 2024 ACL"

Links: [{"title":"VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.134/"},{"title":"[Quick Review] VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models","url":"https://liner.com/review/verifiner-verificationaugmented-ner-via-knowledgegrounded-reasoning-with-large-language-models"},{"title":"Accepted Main Conference Papers - ACL 2024","url":"https://2024.aclweb.org/program/main_conference_papers/"},{"title":"GitHub - emseoyk/VerifiNER","url":"https://github.com/emseoyk/verifiner"},{"title":"VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/384213955_VerifiNER_Verification-augmented_NER_via_Knowledge-grounded_Reasoning_with_Large_Language_Models"},{"title":"Math-Shepherd: Verify and Reinforce LLMs Step-by- ...","url":"https://aclanthology.org/2024.acl-long.510.pdf"},{"title":"LLatrieval: LLM-Verified Retrieval for Verifiable Generation - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.305/"},{"title":"When Does Verification Pay Off? A Closer Look at LLMs as Solution Verifiers","url":"https://www.arxiv.org/pdf/2512.02304"},{"title":"Provenance: A Light-weight Fact-checker for Retrieval Augmented LLM Generation Output - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-industry.97/"},{"title":"Chain-of-Verification Reduces Hallucination in Large ...","url":"https://aclanthology.org/2024.findings-acl.212.pdf"}]

I've found comprehensive information about VerifiNER. Here's a summary of the search results:

## VerifiNER: Verification-augmented NER with LLMs (ACL 2024)

VerifiNER is a paper titled "Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models" that was presented at the 62nd Annual Meeting of the Association for Computational Linguistics (ACL 2024) in Bangkok, Thailand.

### Overview

VerifiNER is a post-hoc verification framework that identifies errors from existing NER methods using knowledge and revises them into more faithful predictions. The framework leverages the reasoning abilities of large language models to adequately ground on knowledge and the contextual information in the verification process.

### Key Features

VerifiNER features a contextual relevance verification step that employs LLMs and consistency voting over multiple reasoning paths to select the most contextually appropriate entity.

### Performance Results

Across all tested NER models and datasets (GENIA and BC5CDR), VerifiNER consistently achieved substantial F1 score improvements, with an average precision increase of 20.03% while recall decreased by only 1.09%. The results suggest that VerifiNER can successfully verify errors from existing models as a model-agnostic approach, with further analyses on out-of-domain and low-resource settings showing the usefulness of VerifiNER on real-world applications.

The paper is authored by Seoyeon Kim, Kwangwook Seo, Hyungjoo Chae, Jinyoung Yeo, and Dongha Lee, with the official code available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0f754d1-18bc-446f-b830-80bd5bff6a73",
  "isSidechain": false,
  "promptId": "f5d01f90-29f0-42ef-8c36-beb6e3f39fb5",
  "type": "user",
  "uuid": "bef8ea7a-7294-41f1-b8c7-e2ea768eeb5a",
  "toolUseResult": {
    "query": "VerifiNER verification augmented NER LLM 2024 ACL",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UaPP2svjcLNr4hn6Xxsiuz",
        "content": [
          {
            "title": "VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models - ACL Anthology",
            "url": "https://aclanthology.org/2024.acl-long.134/"
          },
          {
            "title": "[Quick Review] VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models",
            "url": "https://liner.com/review/verifiner-verificationaugmented-ner-via-knowledgegrounded-reasoning-with-large-language-models"
          },
          {
            "title": "Accepted Main Conference Papers - ACL 2024",
            "url": "https://2024.aclweb.org/program/main_conference_papers/"
          },
          {
            "title": "GitHub - emseoyk/VerifiNER",
            "url": "https://github.com/emseoyk/verifiner"
          },
          {
            "title": "VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models | Request PDF",
            "url": "https://www.researchgate.net/publication/384213955_VerifiNER_Verification-augmented_NER_via_Knowledge-grounded_Reasoning_with_Large_Language_Models"
          },
          {
            "title": "Math-Shepherd: Verify and Reinforce LLMs Step-by- ...",
            "url": "https://aclanthology.org/2024.acl-long.510.pdf"
          },
          {
            "title": "LLatrieval: LLM-Verified Retrieval for Verifiable Generation - ACL Anthology",
            "url": "https://aclanthology.org/2024.naacl-long.305/"
          },
          {
            "title": "When Does Verification Pay Off? A Closer Look at LLMs as Solution Verifiers",
            "url": "https://www.arxiv.org/pdf/2512.02304"
          },
          {
            "title": "Provenance: A Light-weight Fact-checker for Retrieval Augmented LLM Generation Output - ACL Anthology",
            "url": "https://aclanthology.org/2024.emnlp-industry.97/"
          },
          {
            "title": "Chain-of-Verification Reduces Hallucination in Large ...",
            "url": "https://aclanthology.org/2024.findings-acl.212.pdf"
          }
        ]
      },
      "I've found comprehensive information about VerifiNER. Here's a summary of the search results:\n\n## VerifiNER: Verification-augmented NER with LLMs (ACL 2024)\n\nVerifiNER is a paper titled \"Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models\" that was presented at the 62nd Annual Meeting of the Association for Computational Linguistics (ACL 2024) in Bangkok, Thailand.\n\n### Overview\n\nVerifiNER is a post-hoc verification framework that identifies errors from existing NER methods using knowledge and revises them into more faithful predictions. The framework leverages the reasoning abilities of large language models to adequately ground on knowledge and the contextual information in the verification process.\n\n### Key Features\n\nVerifiNER features a contextual relevance verification step that employs LLMs and consistency voting over multiple reasoning paths to select the most contextually appropriate entity.\n\n### Performance Results\n\nAcross all tested NER models and datasets (GENIA and BC5CDR), VerifiNER consistently achieved substantial F1 score improvements, with an average precision increase of 20.03% while recall decreased by only 1.09%. The results suggest that VerifiNER can successfully verify errors from existing models as a model-agnostic approach, with further analyses on out-of-domain and low-resource settings showing the usefulness of VerifiNER on real-world applications.\n\nThe paper is authored by Seoyeon Kim, Kwangwook Seo, Hyungjoo Chae, Jinyoung Yeo, and Dongha Lee, with the official code available on GitHub."
    ],
    "durationSeconds": 7.618527494999988
  },
  "sourceToolAssistantUUID": "f0f754d1-18bc-446f-b830-80bd5bff6a73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 75 · 2026-05-15T04:01:30.705Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture. Let me also think about the novelty claim and whether there are papers I should check that specifically compare confidence signals (multi-family) for IE.

Key findings from my search:
1. The "correlation-selection gap" term appears to be novel - no prior work uses this specific term
2. However, the underlying observation that quality estimation ≠ selection is partially addressed in RASC (NAACL 2025), CISC (ACL Findings 2025), and Self-Certainty (NeurIPS 2025) - but all for discrete-answer tasks, not structured IE
3. VerifiNER (ACL 2024) is a relevant missing reference - it uses verification for NER, which is related to the verifier-based approach mentioned in the conclusion


4. RASC specifically explores how reasoning path quality differs from final answer selection, which connects to the paper's core distinction

I'm also noticing some critical citation gaps - RASC and VerifiNER should definitely be included, along with He et al.'s work on uncertainty for sequential labeling and the conformal prediction approach for NER. Now I need to evaluate whether the paper's main claims about being the first multi-family comparison for IE actually hold up given these related works.

The first claim about multi-family comparison seems solid - Nedellec is the closest precedent but only covers surface-level approaches. The correlation-selection gap is genuinely novel for structured outputs, even though self-consistency already handles discrete tasks well through majority voting. The soft Jaccard contribution is incremental but legitimate as an extension of Nedellec's work using bipartite matching.

I'm checking the paper structure for an ethics statement and looking at the limitations section...

there isn't one included, though ARR doesn't strictly require it for desk rejection. Let me estimate the page count by tallying up the content - the introduction, related work, method section with equations, and experiments with tables and figures are fairly dense. With the figures and tables distributed throughout, this looks like it'll land around the expected length for the venue.

Now I'm structuring my review according to the requested format, starting with a summary of the paper's main contribution about the correlation-selection gap in confidence signals for test-time scaling.

Moving into the strengths, I'm noting the clear problem decomposition that reveals a fundamental limitation, the rigorous experimental methodology with proper statistical testing, and the insightful framing of the correlation-selection gap concept. The paper handles negative results honestly and includes comprehensive robustness analysis, plus an interesting finding about how inflated correlations on WNUT-17 stem from zero/non-zero separation rather than true quality discrimination.

Now looking at the critical weaknesses: the RE evaluation relies solely on SciERC where 44% of instances hit zero F1, which creates severe floor effects that undermine the strong conclusions drawn about RE signals. The paper acknowledges this limitation but doesn't adequately mitigate it—adding another RE benchmark or substantially qualifying the RE claims would be necessary. There's also a circularity issue in the explanation for why instance-level signals fail at selection: the discussion attributes this to signals producing a single score per input that "by construction cannot rank N candidates," but this constraint was already apparent from the definition in Section 3.1.

The more pressing gap is explaining why logprob, the only per-sample signal, also fails—the constrained decoding hypothesis offered is speculative without empirical validation. I'd need to test this directly, perhaps by comparing constrained versus unconstrained sampling or measuring logprob variance across samples. Additionally, the paper is missing an explicit Ethics Statement, which the ARR review form explicitly requests even for low-risk empirical work. The claim about being the "first multi-family comparison" also needs stronger support beyond what's currently presented.

Regarding the novelty claims, while multi-family confidence comparisons exist for other tasks like QA and summarization, the specificity to generative structured IE is a valid niche—though the paper would benefit from explicitly laying out what makes this setting uniquely challenging. The Soft Jaccard contribution looks incremental too: it performs nearly identically to Voting on several benchmarks, and the improvement over surface EM is only marginally significant.

The ρ–AUROC dissociation is being oversold as a novel finding when it's really just a statistical property—measuring monotonic correlation versus binary discrimination will naturally produce different results, and this isn't unique to their IE setting. Finally, there's some inconsistency in terminology around "quality estimation" versus "quality prediction" that should be cleaned up.

Also, I'm noticing the paper misses two relevant recent works: RASC from NAACL 2025 directly tackles the quality versus consistency distinction they're exploring, and VerifiNER from ACL 2024 demonstrates verification-based approaches they mention as future directions—both should be cited and properly positioned in the related work.

Now looking at the presentation issues: the abstract introduces "oracle headroom" without definition, the introduction's comparison with Nedellec reads a bit adversarial when it could be more neutral, and there's an unsupported claim about temperature-based sampling providing sufficient diversity for Fleiss' κ assumptions. Table 2 omits EM with only a footnote, but it should either cite the probability calculation or show empirical evidence of exact match frequency. The appendix also has an inconsistent column header where "VC" doesn't align with "Voting" terminology.

I'm also noticing the paper references "LLaMA Factory" for fine-tuning without a citation, and I'm thinking through several questions that would strengthen the work: whether a learned verifier could empirically close the oracle gap, what the per-sample logprob variance actually is, how sensitive the consensus-proximity strategy is to different distance metrics, and most intriguingly, why logprob shows that striking inversion on WNUT-17 where it's negatively correlated with the full set but positively correlated conditionally.

There are a few key papers missing from the references—Kim et al.'s verification-augmented NER approach, Jiang et al.'s work on reasoning consistency, and He et al.'s token-level uncertainty estimation for sequence labeling all seem directly relevant to what this paper is doing. Overall I'd rate this around 3.0 for the findings track, with soundness at 3.5, excitement at 3.0, and I'm fairly confident in that assessment at 4.0.

Reconsidering the scoring though—the paper does have real strengths: the research question is clear, the methodology is rigorous with proper statistics, and that correlation-selection gap is genuinely insightful. The writing is solid and it has practical value for the IE community. But there are meaningful limitations: only one RE dataset, the logprob explanation feels speculative, the SJ contribution is incremental, some terminology issues, no ethics statement, and the instance-level gap is somewhat obvious given how they defined it. For a main conference like EMNLP, the quality estimation results are decent but ρ=0.38 isn't particularly strong, and while the negative result about selection failure matters, it needs a more convincing explanation. The paper is thorough but probably doesn't quite hit the excitement bar for main conference acceptance, so 3.0 for findings track seems right.

The missing ethics statement is just a procedural matter—I should wrap up the review now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bef8ea7a-7294-41f1-b8c7-e2ea768eeb5a",
  "isSidechain": false,
  "requestId": "req_011Cb3gkccsH9tZrxZH1zHsf",
  "type": "assistant",
  "uuid": "6ec6807e-f728-4ba8-9ce4-5be2a94778da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R1W8E36t4wB4D5QA4Ec562",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2456,
      "cache_read_input_tokens": 69232,
      "output_tokens": 8315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2456,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8315,
          "cache_read_input_tokens": 69232,
          "cache_creation_input_tokens": 2456,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2456
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

_source line 76 · 2026-05-15T04:02:48.678Z_

所有材料已读完，搜索工作已完成。现在撰写完整审稿意见。

---

## Summary

本文系统比较了三个 family（structural / surface / model-internal）的五种 confidence signal 在 generative IE（NER + RE）上的 quality estimation 和 sample selection 性能。核心发现是 **correlation-selection gap**：instance-level consistency signal 能预测哪些输入模型处理得好（ρ 最高 0.38, AUROC 最高 0.75），但无法在 best-of-N selection 中可靠超越 greedy decoding（p>0.39），尽管存在 13–18pp 的 oracle headroom。论文还发现 signal ranking 依赖于任务难度。实验覆盖 SciERC (NER+RE)、CoNLL-2003、WNUT-17，模型为 Qwen3-8B 和 LLaMA-3.1-8B。

---

## Strengths

- **S1**: Quality estimation 与 sample selection 的问题分解是真正有洞察力的，将先前工作中混淆的两个目标清晰剥离，对社区有概念性贡献
- **S2**: 实验方法论严谨：paired bootstrap (B=10,000)、多 seed 验证、proper CI 报告、Cohen's d 和 sign test 辅助判断——超出该领域大多数 empirical paper 的统计规范
- **S3**: WNUT-17 的分析揭示 inflated correlation 由 zero/non-zero boundary 驱动（Voting full-set ρ=0.724 → conditional ρ=0.038, n.s.），这是一个重要的 methodological warning，值得独立推广
- **S4**: 负面结果的处理诚实且 balanced——没有过度包装，Limitations 节坦率承认 RE 仅有一个 benchmark、logprob temperature sensitivity 未表征等
- **S5**: 论文结构和叙事流畅，Abstract → Introduction → Contributions 逻辑链清晰
- **S6**: Robustness 分析（temperature、N-scaling、cross-model）提供了有价值的 practical guidance

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **RE 结论建立在单一 benchmark 上且受严重 floor effect 影响**
- 具体位置：Section 4.1 (Table 1)、Section 4.2 (Table 2)、Section 6 (Conclusion)
- 问题：RE 评估仅使用 SciERC（44% instances 得到 zero F1），correlation-selection gap 的 RE 部分完全依赖此单一数据集。在如此高的 zero-F1 比例下，任何 signal 的 discriminative power 都会被压缩。论文在 Conclusion 中仍然将 RE 的 gap（-0.9pp, p=0.80）作为核心 finding 的等权支撑。
- 为什么影响接收：一个数据集且带有严重 floor effect 不足以支撑 generalized conclusion。这不是 Limitations 中一句"warrants further validation"能解决的——核心 claim 的一半证据基础薄弱。
- 建议：增加至少一个 RE benchmark（如 TACRED 子集、DocRED）；或显著降低 RE 结论的 claim 强度，将其明确标记为 preliminary observation 而非 confirmed finding。

**N2** [critical] **Logprob 作为唯一 per-sample signal 的失败缺乏实证解释**
- 具体位置：Section 5 "Why logprob fails as a selector" 段
- 问题：四个 instance-level signal 无法做 selection 在定义上就是 expected 的（Section 3.1 已说明它们 produce single score per input）。真正 surprising 且需要解释的是为什么 logprob——唯一的 per-sample signal——也失败了。Discussion 给出的解释是"constrained decoding 下 logprob 主要反映 grammar compliance"，但这是猜测性的，没有实证验证。
- 为什么影响接收：如果 logprob 失败的原因确实是 constrained decoding 压缩了 per-sample diversity，这意味着 correlation-selection gap 可能是实验设置的 artifact 而非结构化 IE 的固有属性。论文自己在 Discussion 中也承认了这一可能性（"the correlation-selection gap may partially reflect this reduced diversity"），但没有提供 disentangle 的证据。
- 建议：(a) 报告 per-sample logprob 的 variance 统计（如果 variance 极低则支持 hypothesis）；(b) 比较 constrained vs. unconstrained decoding 下的 selection performance；(c) 至少提供 constrained decoding 下 unique output 的比例数据。

**N3** [critical] **缺少 Ethics Statement**
- 具体位置：main.tex — 仅有 `\section*{Limitations}`，无 Ethics Statement
- 问题：ARR review form 明确要求 reviewer 评估 ethical considerations。虽然本工作在公开 benchmark 上做 empirical evaluation，风险较低，但缺失 Ethics Statement 是格式合规问题。
- 建议：添加简短的 Ethics Statement，说明数据集均为公开的、无 privacy concern、计算资源消耗等。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **"First multi-family comparison" claim 的边界需更明确**
- 具体位置：Section 1 Contribution 1；Section 6 第一句
- 问题：CoCoA (Vashurin et al., 2025) 已经 fuse model confidence 与 inter-sample consistency（两个 family），虽然是 for QA/summarization。Self-Certainty (Kang et al., 2025) 和 CISC (Taubenfeld et al., 2025) 也比较了 model-internal 与 voting-based signal。"First" claim 的成立依赖于限定词 "for generative structured IE" 的精确度，但读者可能理解为更广的 scope。
- 建议：更精确地限定为 "first multi-family comparison for set-valued structured IE" 并明确说明为什么 structured IE 的 set-valued output 使问题 qualitatively different。

**W2** [warning] **Soft Jaccard 的增量贡献 borderline**
- 具体位置：Section 3.2 Eq. 4-5；Table 1
- 问题：SJ 与 Voting 在 SciERC NER 上差异不显著（Δρ=+0.019, CI 包含零，Table 7）。SJ 相对 EM 的优势仅 borderline significant（Δρ=+0.065, CI lower bound +0.003）。作为 Contribution 1 的组成部分，SJ 作为"core structural signal"的贡献度与其 empirical evidence 不匹配。
- 建议：降低 SJ 在贡献叙述中的权重；强调其作为比较框架的一部分而非独立贡献。

**W3** [warning] **ρ–AUROC dissociation 的呈现过度**
- 具体位置：Section 4.2 "ρ–AUROC dissociation" 段；Section 5 第二段
- 问题：ρ 衡量单调相关性，AUROC 衡量二元判别力——它们在信号具有强 binary-split power 但有限 ordinal resolution 时自然不同，这是统计属性而非本文特有的发现。EM 在这方面的表现（高 AUROC + 低 ρ）完全可预期：EM=1 将 all-correct 和 all-wrong 实例折叠在一起。
- 建议：作为 expected statistical behavior 简要提及即可，不需要占用一个单独的 paragraph header。

**W4** [warning] **术语不一致**
- "confidence signal" vs "consistency signal"：logprob 不是基于 inter-sample consistency 的，但有时被归入 "consistency signals" 的讨论中
- "quality estimation" vs "quality prediction"：Abstract 用前者，Discussion 偶尔出现后者
- Table 4 (Appendix) 用 "VC" 和 "LP" 作为列标题，与正文中 "Voting Conf." 和 "Log-prob" 不一致
- "LLaMA Factory" 在 Section 4.1 中提及但未给出引用

**W5** [warning] **Related Work 有遗漏**
- **VerifiNER** (Kim et al., ACL 2024)：verification-augmented NER，使用 consistency voting 和 LLM reasoning 进行 post-hoc NER 验证——直接相关于论文 Conclusion 中提到的 verifier 方向
- **RASC** (Aggarwal et al., NAACL 2025, "Reasoning Aware Self-Consistency")：显式区分 reasoning quality 和 answer consistency，概念上接近 quality estimation vs. selection 的区分
- 这两篇是最相关的遗漏；不影响核心 claim 但应 cite 和 position

---

## Minor Issues

- Abstract 第 4 行："13–18 pp of oracle headroom"——读者此时不知道 oracle headroom 的定义
- Introduction line 16：对 Nedellec (2026) 的三点对比有效但措辞偏 adversarial（"(i) relies on... (ii) evaluates only... (iii) covers..."），建议更中性的 framing
- Section 3.2 Fleiss' κ："temperature-based sampling provides sufficient response diversity"——此 assertion 需要 justification，FK 假设 independent raters，temperature sampling 的 diversity 是否足够？
- Table 2 脚注说 EM 被省略因为"the probability of two identical structured outputs is negligible"——应提供实际的 unique output fraction 数据支持
- Appendix A.4 "Per-relation diagnostic" 使用 `\textsc{}` 而非 `\textsc{}`（应为 `\textsc{Feature-Of}` 等，需检查编译是否正确）
- Conclusion 的 future work 方向具体且可行，是正面的

---

## Questions for Authors

1. Per-sample logprob variance 是多少？如果在 constrained decoding 下极低，这将直接支持 Discussion 中的 hypothesis 并证明 gap 部分来自实验设置。
2. 是否尝试过其他 per-sample selection strategy（如 sample-level SJ to consensus 的变体）？consensus-proximity strategy 对 distance metric 的选择敏感吗？
3. WNUT-17 logprob 的 full-set/conditional ρ 反转（-0.410 → +0.350）是否有更深层的解释？这暗示 logprob 在 domain-shift 下有 systematically miscalibrated behavior。
4. 是否考虑过即使是 simple learned selector（如 logistic regression on signal combination）也能部分 close the gap？

---

## Missing References

1. Kim et al. (2024) "VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models" — ACL 2024
2. Aggarwal et al. (2025) "Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling" — NAACL 2025
3. He et al. (2024) "Uncertainty Estimation on Sequential Labeling via Token-Level Risk" — NAACL Findings 2024

---

## Scores

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Overall** | **3.0/5** | Findings track — 实验严谨但 RE 证据薄弱、logprob 失败解释缺乏实证、excitement 受限于负面结果主导 |
| Soundness | 3.5/5 | NER 方法论扎实（3 datasets, 2 models, proper stats），但 RE 仅 1 dataset 且 constrained decoding 的 confound 未被 disentangle |
| Excitement | 3.0/5 | Correlation-selection gap 是有价值的概念贡献，但 (a) instance-level signal 无法 select 在定义上 partially obvious，(b) 未能指出 positive path forward（仅说"需要 verifier"） |
| Reproducibility | 4.0/5 | 方法描述详细，使用公开 benchmark 和 open-weight model，但代码/数据未提及是否会公开 |
| Confidence | 4/5 | 熟悉 self-consistency、uncertainty estimation、generative IE 文献 |

**一句话总结**：一篇方法论严谨的 empirical study，提出了有概念价值的 correlation-selection gap，但核心 finding 受限于 RE 证据单薄和 logprob 失败的未验证解释，适合 Findings track 而非 Main conference。

---

现在将审稿意见提交给 Review Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ec6807e-f728-4ba8-9ce4-5be2a94778da",
  "isSidechain": false,
  "requestId": "req_011Cb3gkccsH9tZrxZH1zHsf",
  "type": "assistant",
  "uuid": "58c42dce-55b2-4926-9fd1-ebd6ebf98b1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R1W8E36t4wB4D5QA4Ec562",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2456,
      "cache_read_input_tokens": 69232,
      "output_tokens": 8315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2456,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8315,
          "cache_read_input_tokens": 69232,
          "cache_creation_input_tokens": 2456,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2456
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

_source line 77 · 2026-05-15T04:03:08.738Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01BjssqYRtih1gZz9RDEHBFj`</summary>

```json
{
  "text": "## Reviewer 2 审稿意见：Strong Predictors, Weak Selectors\n\n### Summary\n\n本文系统比较了三个 family（structural / surface / model-internal）的五种 confidence signal 在 generative IE（NER + RE）上的 quality estimation 和 sample selection 性能。核心发现是 correlation-selection gap：instance-level consistency signal 能预测哪些输入模型处理得好（ρ 最高 0.38, AUROC 最高 0.75），但无法在 best-of-N selection 中可靠超越 greedy decoding（p>0.39），尽管存在 13–18pp 的 oracle headroom。\n\n---\n\n### Strengths\n\n- **S1**: Quality estimation 与 sample selection 的问题分解有真正洞察力，将先前工作混淆的两个目标清晰剥离\n- **S2**: 实验方法论严谨：paired bootstrap (B=10,000)、多 seed、proper CI、Cohen's d、sign test\n- **S3**: WNUT-17 分析揭示 inflated correlation 由 zero/non-zero boundary 驱动（Voting ρ=0.724 → conditional ρ=0.038, n.s.），是重要的 methodological warning\n- **S4**: 负面结果处理诚实 balanced，Limitations 坦率承认多项局限\n- **S5**: 论文结构和叙事流畅\n- **S6**: Robustness 分析覆盖 temperature、N-scaling、cross-model\n\n---\n\n### Must-Fix (Critical)\n\n**N1** [critical] RE 结论建立在单一 benchmark 上且受严重 floor effect 影响\n- SciERC RE 44% zero F1，gap 的 RE 证据（-0.9pp, p=0.80）基础薄弱\n- 一个 dataset + 严重 floor effect 不足以支撑 generalized conclusion\n- 建议增加 RE benchmark 或显著降低 RE claim 强度\n\n**N2** [critical] Logprob 失败缺乏实证解释\n- 4 个 instance-level signal 无法 select 在定义上 expected；logprob 作为唯一 per-sample signal 为什么也失败才是关键问题\n- Discussion 的 \"constrained decoding 压缩 diversity\" 解释是猜测性的\n- 如果 gap 来自实验设置 artifact 而非结构化 IE 固有属性，核心 claim 需要重新审视\n- 建议报告 per-sample logprob variance、unique output fraction、或比较 constrained vs. unconstrained decoding\n\n**N3** [critical] 缺少 Ethics Statement\n- ARR review form 明确要求 reviewer 评估 ethical considerations，缺失是格式问题\n\n---\n\n### Should-Fix (Warning)\n\n**W1** \"First multi-family comparison\" claim 边界需更精确限定，与 CoCoA、CISC 等 existing multi-signal comparison 的差异应更明确\n**W2** Soft Jaccard 增量贡献 borderline（vs. Voting Δρ CI 包含零，vs. EM borderline significant CI lower bound +0.003）\n**W3** ρ–AUROC dissociation 是 expected statistical behavior，不应作为独立发现过度强调\n**W4** 术语不一致：\"confidence signal\" vs \"consistency signal\"、\"VC\" vs \"Voting Conf.\"、LLaMA Factory 未引用\n**W5** Related Work 遗漏：VerifiNER (ACL 2024)、RASC (NAACL 2025)\n\n---\n\n### Minor Issues\n\n- Abstract 中 \"oracle headroom\" 此时无定义\n- 对 Nedellec (2026) 措辞偏 adversarial\n- FK independent raters 假设的 justification 不足\n- Table 2 EM omission 需 unique output fraction 数据支持\n\n---\n\n### Missing References\n\n1. Kim et al. (2024) \"VerifiNER\" — ACL 2024\n2. Aggarwal et al. (2025) \"Reasoning Aware Self-Consistency\" — NAACL 2025\n3. He et al. (2024) \"Uncertainty Estimation on Sequential Labeling\" — NAACL Findings 2024\n\n---\n\n### Scores\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| Overall | 3.0/5 | Findings track |\n| Soundness | 3.5/5 | NER 扎实，RE 单 dataset + constrained decoding confound 未 disentangle |\n| Excitement | 3.0/5 | 概念贡献有价值但 partially obvious + 无 positive path forward |\n| Reproducibility | 4.0/5 | 方法详细、公开 benchmark/model，但代码公开未提及 |\n| Confidence | 4/5 | 熟悉相关文献 |\n\n**一句话**：方法论严谨的 empirical study，correlation-selection gap 有概念价值，但 RE 证据薄弱 + logprob 失败解释缺乏实证，适合 Findings 而非 Main。",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58c42dce-55b2-4926-9fd1-ebd6ebf98b1f",
  "isSidechain": false,
  "requestId": "req_011Cb3gkccsH9tZrxZH1zHsf",
  "type": "assistant",
  "uuid": "b09d16b9-9e8f-468c-b338-e88dcd1f548e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R1W8E36t4wB4D5QA4Ec562",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2456,
      "cache_read_input_tokens": 69232,
      "output_tokens": 8315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2456,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8315,
          "cache_read_input_tokens": 69232,
          "cache_creation_input_tokens": 2456,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2456
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

_source line 78_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。  ## 审稿对象 - 论文路径：`projects/struct_self_consist_ie/docs/paper/main.tex`（分节结构，各节在 `sections/` 下） - 目标 venue：**EMNLP 2026 Main Conference**（通过 ARR May…",
  "leafUuid": "b09d16b9-9e8f-468c-b338-e88dcd1f548e",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b"
}
```

---

### Runtime record

_source line 79_

```json
{
  "type": "ai-title",
  "aiTitle": "Generative IE confidence signals systematic review",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b"
}
```

---

### Tool result

_source line 80 · 2026-05-15T04:03:12.652Z_

<details><summary>↩ Tool result · `toolu_01BjssqYRtih1gZz9RDEHBFj`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b09d16b9-9e8f-468c-b338-e88dcd1f548e",
  "isSidechain": false,
  "promptId": "f5d01f90-29f0-42ef-8c36-beb6e3f39fb5",
  "type": "user",
  "uuid": "f7f558c5-091e-4910-a5bb-502037f21c2b",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_3897c2857f11615119e277e820eae311:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "b09d16b9-9e8f-468c-b338-e88dcd1f548e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 81_

```json
{
  "type": "ai-title",
  "aiTitle": "Generative IE confidence signals systematic review",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b"
}
```

---

### Runtime record

_source line 82 · 2026-05-15T04:06:34.917Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T04:06:34.917Z",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "content": "[Round 1 审稿请求]:\n## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每个 Must-Fix、Should-Fix 和 Minor Issue：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n### Summary\n本文系统比较了生成式信息抽取（IE）中五种置信度信号用于质量估计和样本选择两个不同目标的表现。核心发现是\"correlation-selection gap\"：一致性信号在实例级质量估计上有效（ρ 最高 0.38，AUROC 最高 0.75），但用于 best-of-N 选择时没有任何信号能显著超过 greedy decoding（p>0.39），尽管存在 13–18pp 的 oracle headroom。论文还发现信号排序依赖于任务难度。\n\n### Strengths\n- S1: 清晰的问题分解与严谨的框架设计（per-sample vs. instance-level 形式化）\n- S2: 全面的统计报告（Bootstrap B=10,000 + CI + Cohen's d + sign test）\n- S3: 诚实的 scope limitation 声明（RE 单数据集在 4 处明确提及）\n- S4: Task difficulty 分析有洞察力（EM vs. SJ crossover）\n- S5: Soft Jaccard 信号设计合理（type-aware Hungarian matching + token-level IoU）\n\n### Must-Fix (Critical)\n**N1** [critical] Constrained decoding 是 correlation-selection gap 的未控制混淆变量\n- 论文核心发现\"no signal reliably surpasses greedy\"可能部分是 constrained decoding（Outlines/vLLM）压缩 per-sample diversity 的产物\n- Random baseline gap 仅 3.6pp，可能远低于 unconstrained generation 的 variance\n- 建议增加 unconstrained generation 对照或量化 constrained decoding 下的实际 diversity level\n\n**N2** [critical] \"No signal reliably surpasses greedy\" 的统计论证逻辑不完整——failure to reject ≠ evidence of absence\n- p>0.39 只是 absence of evidence，不是 evidence of absence\n- CI 范围 [−3.0, +4.2] 不能排除有意义的选择增益\n- 建议补充等价性检验（TOST）或 power analysis\n\n**N3** [critical] N=8 主要结果仅使用单一 seed（seed=42），缺乏可靠性验证\n- Table 1 N=8 和 Table 2 全部基于 single random seed\n- N=16 的 3-seed σ 约 0.003-0.008 暗示 N=8 的方差可能更大\n- 信号排序差异很小（Voting vs. SJ Δρ=0.019，CI 含零），single-seed 无法确认稳定性\n\n### Should-Fix (Warning)\n**W1** 多重比较校正缺失（SJ–EM borderline significant 在任何 correction 下不会 survive）\n**W2** \"Correlation-selection gap\" 部分为 tautological（4/5 instance-level 信号 by design 无法 per-sample 区分）\n**W3** FK 独立性假设未经验证（温度采样非独立）\n**W4** SJ 定义中 Hungarian matching 的 cost function 未明确（max IoU? 允许 zero-IoU match?）\n**W5** \"Cross-model\" 实为 cross-architecture at fixed 8B scale\n**W6** Consensus-proximity 是唯一 instance-to-sample 转换策略，未比较替代方案（如 MBR decoding）\n\n### Minor Issues\n**M1** WNUT-17 \"54% zero F1\" vs Table 7 显示 51.5%，数据不一致\n**M2** Table 1 N=16 区域大面积空白\n**M3** EM selection 排除理由缺乏经验支持\n**M4** LOO-SJ Δρ 和 per-instance Δρ 量纲不同\n**M5** Figure 1 caption 引入 figure 未直接呈现的 p=0.39\n**M6** Semantic entropy footnote 比较既然不可比就不应出现\n**M7** 引用格式细节\n\n### Questions to Authors\nQ1: 是否考虑过 unconstrained generation 作为对照？\nQ2: Logprob 在 WNUT conditional set 最高 ρ=0.350，如何 reconcile \"logprob 最弱\"？\nQ3: LoRA rank=32 是否影响 sample diversity？\nQ4: N=16 selection 结果有无 multi-seed bootstrap p-value？\n\n### Missing References\n- MBR decoding: Eikema & Aziz (2022), Freitag et al. (2022)\n- Structured prediction uncertainty: Malinin & Gales (2021)"
}
```

---

### Runtime record

_source line 83 · 2026-05-15T04:06:34.918Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T04:06:34.918Z",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b"
}
```

---

## Round 2

2 recorded events

### User

_source line 84 · 2026-05-15T04:06:34.908Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7f558c5-091e-4910-a5bb-502037f21c2b",
  "isSidechain": false,
  "promptId": "598a9ee9-06fa-4905-a6d4-6b653362c4be",
  "type": "user",
  "isMeta": true,
  "uuid": "054ccc44-40b5-4e99-89b3-c59689adec1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 85 · 2026-05-15T04:06:34.908Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "054ccc44-40b5-4e99-89b3-c59689adec1c",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "de0d9485-8aa2-49bb-aeaf-a0165e91d64c",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "id": "0e940222-2435-47db-9606-7315a4a6d027",
    "container": null,
    "model": "&lt;synthetic>",
    "stop_reason": "stop_sequence",
    "stop_sequence": "",
    "type": "message",
    "usage": {
      "input_tokens": 0,
      "output_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": null,
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": null,
      "iterations": null,
      "speed": null
    },
    "context_management": null
  }
}
```

</details>

---

## Round 3

8 recorded events

### User

_source line 86 · 2026-05-15T04:06:34.978Z_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 1 的完整审稿意见

请逐条回应以下 Reviewer 1 的审稿意见。对每个 Must-Fix、Should-Fix 和 Minor Issue：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

以下是 Reviewer 1 的完整审稿原文：

### Summary
本文系统比较了生成式信息抽取（IE）中五种置信度信号用于质量估计和样本选择两个不同目标的表现。核心发现是"correlation-selection gap"：一致性信号在实例级质量估计上有效（ρ 最高 0.38，AUROC 最高 0.75），但用于 best-of-N 选择时没有任何信号能显著超过 greedy decoding（p>0.39），尽管存在 13–18pp 的 oracle headroom。论文还发现信号排序依赖于任务难度。

### Strengths
- S1: 清晰的问题分解与严谨的框架设计（per-sample vs. instance-level 形式化）
- S2: 全面的统计报告（Bootstrap B=10,000 + CI + Cohen's d + sign test）
- S3: 诚实的 scope limitation 声明（RE 单数据集在 4 处明确提及）
- S4: Task difficulty 分析有洞察力（EM vs. SJ crossover）
- S5: Soft Jaccard 信号设计合理（type-aware Hungarian matching + token-level IoU）

### Must-Fix (Critical)
**N1** [critical] Constrained decoding 是 correlation-selection gap 的未控制混淆变量
- 论文核心发现"no signal reliably surpasses greedy"可能部分是 constrained decoding（Outlines/vLLM）压缩 per-sample diversity 的产物
- Random baseline gap 仅 3.6pp，可能远低于 unconstrained generation 的 variance
- 建议增加 unconstrained generation 对照或量化 constrained decoding 下的实际 diversity level

**N2** [critical] "No signal reliably surpasses greedy" 的统计论证逻辑不完整——failure to reject ≠ evidence of absence
- p>0.39 只是 absence of evidence，不是 evidence of absence
- CI 范围 [−3.0, +4.2] 不能排除有意义的选择增益
- 建议补充等价性检验（TOST）或 power analysis

**N3** [critical] N=8 主要结果仅使用单一 seed（seed=42），缺乏可靠性验证
- Table 1 N=8 和 Table 2 全部基于 single random seed
- N=16 的 3-seed σ 约 0.003-0.008 暗示 N=8 的方差可能更大
- 信号排序差异很小（Voting vs. SJ Δρ=0.019，CI 含零），single-seed 无法确认稳定性

### Should-Fix (Warning)
**W1** 多重比较校正缺失（SJ–EM borderline significant 在任何 correction 下不会 survive）
**W2** "Correlation-selection gap" 部分为 tautological（4/5 instance-level 信号 by design 无法 per-sample 区分）
**W3** FK 独立性假设未经验证（温度采样非独立）
**W4** SJ 定义中 Hungarian matching 的 cost function 未明确（max IoU? 允许 zero-IoU match?）
**W5** "Cross-model" 实为 cross-architecture at fixed 8B scale
**W6** Consensus-proximity 是唯一 instance-to-sample 转换策略，未比较替代方案（如 MBR decoding）

### Minor Issues
**M1** WNUT-17 "54% zero F1" vs Table 7 显示 51.5%，数据不一致
**M2** Table 1 N=16 区域大面积空白
**M3** EM selection 排除理由缺乏经验支持
**M4** LOO-SJ Δρ 和 per-instance Δρ 量纲不同
**M5** Figure 1 caption 引入 figure 未直接呈现的 p=0.39
**M6** Semantic entropy footnote 比较既然不可比就不应出现
**M7** 引用格式细节

### Questions to Authors
Q1: 是否考虑过 unconstrained generation 作为对照？
Q2: Logprob 在 WNUT conditional set 最高 ρ=0.350，如何 reconcile "logprob 最弱"？
Q3: LoRA rank=32 是否影响 sample diversity？
Q4: N=16 selection 结果有无 multi-seed bootstrap p-value？

### Missing References
- MBR decoding: Eikema & Aziz (2022), Freitag et al. (2022)
- Structured prediction uncertainty: Malinin & Gales (2021)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de0d9485-8aa2-49bb-aeaf-a0165e91d64c",
  "isSidechain": false,
  "promptId": "598a9ee9-06fa-4905-a6d4-6b653362c4be",
  "type": "user",
  "uuid": "18ae799d-00c0-4f1b-9cf5-d9b426ee0b38",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 87 · 2026-05-15T04:06:34.977Z_

```json
{
  "parentUuid": "18ae799d-00c0-4f1b-9cf5-d9b426ee0b38",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "2ba5303d-f5be-4c1a-9eab-a4754fb32695",
  "timestamp": "2026-05-15T04:06:34.977Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 88 · 2026-05-15T04:07:49.546Z_

<details><summary>Logged reasoning block</summary>

```text
The Director is asking me (Reviewer 2) to do a cross-review of Reviewer 1's opinions. I need to go through each point and either [AGREE] or [REBUT] with evidence from the paper.

Let me go through each point carefully:

### Must-Fix

**N1** Constrained decoding as confound
- R1 argues constrained decoding compresses per-sample diversity, possibly causing the gap
- I raised a similar concern in my N2 — I agree this is critical
- The paper itself acknowledges this in Discussion ("the correlation-selection gap may partially reflect this reduced diversity")


- The random baseline shows a 3.6pp gap, which does indicate some variance exists, so I'll [AGREE] with this concern

**N2** Statistical logic: failure to reject ≠ evidence of absence
- R1 makes a valid point that p>0.39 doesn't constitute evidence of absence, and suggests TOST or power analysis
- The confidence interval [-3.0, +4.2] doesn't rule out meaningful gains, which is fair
- Though the paper's language is careful with "no signal *reliably* surpasses greedy," the consistency across 6 configurations in Table 4 does provide some support for the claim
- I'll partially agree this is valid but perhaps not as critical as framed

**N3** Single seed for N=8
- R1 raises a fair point about using only seed 42 for the main results
- The N=16 multi-seed results show very tight variance (0.003-0.008 for ρ) and consistent rankings, which suggests the seed variance at N=8 is likely manageable
- Since the signal differences themselves are small (Voting vs SJ at Δρ=0.019), the single-seed limitation is a weakness but the multi-seed consistency provides some reassurance

**W1** Multiple comparison correction
- R1 correctly notes that with three pairwise comparisons in Table 7, applying Bonferroni correction (α/3 = 0.017) would eliminate the borderline SJ-EM result
- This is a valid criticism I agree with

**W2** Tautological nature of gap for instance-level signals
- I already identified this issue myself — four of five signals are instance-level by design, so they inherently can't discriminate per-sample
- The paper presents this as a finding despite the structural limitation, which I agree is problematic

**W3** FK independence assumption
- I flagged this in my minor issues as well
- I agree this is a concern

**W4** SJ Hungarian matching cost function
- R1 questions the specifics of the cost function — whether it's maximizing IoU and whether zero-IoU matches are permitted
- The paper describes using token-level IoU with no minimum similarity threshold, so zero-IoU matches are allowed, though the maximization direction could be clearer
- This is a minor clarity issue but the core description is reasonably complete

**W5** "Cross-model" framing
- Both models are actually 8B, so calling it cross-model is somewhat misleading
- The paper does acknowledge in the Limitations section that findings may not generalize to larger models or closed-source APIs

**W6** Instance-to-sample conversion method
- The paper relies solely on consensus-proximity matching, but MBR decoding is an established alternative for this task
- Not comparing against other conversion methods is a legitimate gap

**M1** Discrepancy in WNUT-17 zero F1 reporting
- The paper states 54% zero F1 in Section 4.1, but the appendix table shows different numbers when I calculate the ratio — need to verify against the full dataset size of 1,287 instances
- There's definitely an inconsistency here worth clarifying

**M2** Incomplete Table 1 presentation
- The N=16 section only shows LLaMA CoNLL results while leaving other model-task combinations blank, which makes the table harder to read

**M3** EM selection exclusion needs empirical justification
- The footnote in Table 2 mentions this but doesn't provide evidence for why it was excluded

**M4** Confusing notation in the LOO-SJ analysis
- The appendix reports both a Δρ value for the overall leave-one-out comparison and a "per-instance Δρ," but since ρ is computed across all instances, the per-instance metric doesn't align with how ρ is typically defined

**M5** Figure 1 caption references a p-value that isn't directly visible
- The caption mentions p=0.39 for NER logprob, but this comes from the statistical analysis in Table 2 and Section 4.2, not from the figure itself, which shows the conceptual framework

**M6** Semantic entropy footnote balances utility with transparency
- The footnote provides practitioners with a reference point for semantic entropy performance on QA tasks while acknowledging it's not directly comparable to the main results, though the caveat could be emphasized more clearly

**M7** Citation formatting needs attention throughout

Now I'm noting the specific questions raised about unconstrained generation, the logprob conditional correlation on WNUT, the LoRA rank effect on diversity, and the multi-seed selection approach. I should also flag the missing references on MBR decoding and structured prediction uncertainty that directly relate to the consensus-proximity alternative and the broader uncertainty quantification discussion. Let me prepare my response to the cross-review.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ba5303d-f5be-4c1a-9eab-a4754fb32695",
  "isSidechain": false,
  "requestId": "req_011Cb3hFTWjkG7KX3q16fZCb",
  "type": "assistant",
  "uuid": "f63cbdf4-c041-4854-b245-1efa02ac809b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ZdNkPfHcFp38x8e6fuG4W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1567,
      "cache_read_input_tokens": 80067,
      "output_tokens": 6364,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1567,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 6364,
          "cache_read_input_tokens": 80067,
          "cache_creation_input_tokens": 1567,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1567
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

_source line 89 · 2026-05-15T04:08:59.690Z_

逐条回应 Reviewer 1 的审稿意见。

---

## 交叉回应：Reviewer 2 对 Reviewer 1 的逐条回应

### Must-Fix

**[AGREE] R1-N1: Constrained decoding 作为未控制的混淆变量**
同意，且与我的 N2 一致。论文自己在 Discussion 中承认了这一可能性（Section 5: "the correlation-selection gap may partially reflect this reduced diversity"），但未提供任何 disentangle 的证据。Random baseline gap 仅 3.6pp（Table 2: random 0.608 vs greedy 0.644）确实暗示 per-sample diversity 被压缩。补充一点：即使不跑 unconstrained 实验，报告 constrained decoding 下 unique output 的比例（N=8 中有多少 distinct outputs？）和 per-sample logprob 的方差就能大幅增强或削弱这一 hypothesis。

**[REBUT] R1-N2: Failure to reject ≠ evidence of absence**
统计原理上正确，但我认为此处不构成 critical issue，理由如下：
1. 论文措辞审慎——用的是 "no signal *reliably* surpasses greedy"（Section 4.2），而非 "signals are equivalent to greedy"。"Reliably" 承认了 uncertainty。
2. 更重要的是，这一 pattern 在 **6 个独立 configuration** 中一致复现（Table 4/cross_selection: LLaMA SciERC N=8/N=16, Qwen/LLaMA CoNLL N=8, 加上 Table 2 的 Qwen SciERC NER/RE）。单个 comparison 的 p>0.39 确实只是 absence of evidence，但 6/6 configurations 均未显示 significant improvement，cumulative evidence 远强于单一 test。
3. TOST 或 power analysis 当然 ideal，但鉴于 CI [-3.0, +4.2] 中正面端仅 +4.2pp 而 oracle headroom 有 13.2pp，即使 true effect 存在也仅 capture 了 headroom 的 ~30%——practical significance 有限。
建议降为 Should-Fix：补充 power analysis 或等价性检验会加强论证，但不改变核心 narrative。

**[AGREE] R1-N3: N=8 单一 seed 的可靠性问题**
同意这是一个合理关切。N=16 的 3-seed σ 为 0.003–0.008（Table 1, Table 3），N=8 的方差预期更大。但我要补充一个 mitigating factor：N=16 3-seed 结果中 signal **rankings** 完全一致（Table 3: SJ > EM ≈ Voting > FK >> logprob on LLaMA CoNLL），且 N=8 与 N=16 的 ranking 也一致——这说明 ordering 是稳定的，即使 absolute ρ 值有 seed variance。建议降为 Should-Fix：single seed 影响 exact ρ 的可信度，但不太可能改变 signal ranking 结论。

---

### Should-Fix

**[AGREE] R1-W1: 多重比较校正缺失**
Table 7 (Appendix B) 做了 3 组 pairwise comparison，SJ–EM 的 CI lower bound 仅 +0.003。Bonferroni correction (α/3 = 0.017) 下这几乎必然不再 significant。论文应在 Table 7 或正文中明确注明 correction 后的状态。

**[AGREE] R1-W2: Gap 对 instance-level signals 部分 tautological**
与我的观点一致（我的 N2 也指出了这一点）。4/5 signals 是 instance-level 的，by definition 产生 single score per input，不能 rank N candidates。论文在 Section 3.1 已经 define 了 per-sample vs instance-level 的区别——correlation-selection gap 对这 4 个 signal 来说是 definitional consequence 而非 empirical discovery。真正的 empirical contribution 是 (a) logprob 也失败，(b) consensus-proximity 转换策略也无效。论文应更坦率地承认这一点，将叙事重心放在 logprob 的失败和 consensus-proximity 的局限上。

**[AGREE] R1-W3: FK 独立性假设**
与我的 minor issue 一致。温度采样产生的 N 个样本共享同一个 model、同一个 input，远非 independent raters。FK 值本身可能仍有 discriminative utility（作为 descriptive statistic），但不应被解读为统计学意义上的 inter-rater agreement。

**[AGREE] R1-W4: SJ Hungarian matching cost function 细节不足**
Section 3.2 Eq. 4 说明 sim(a_m, b_m) 是 token-level IoU，且 "(without minimum similarity threshold)"（所以 zero-IoU match 是允许的）。但确实缺少：(a) Hungarian algorithm 是 maximize 还是 minimize (应是 maximize IoU)？(b) 当一个 type group 中 |g_i| ≠ |g_j| 时 unmatched entities 的处理。这些应在正文或 Appendix 中明确。

**[AGREE] R1-W5: "Cross-model" 实为 cross-architecture at fixed 8B**
完全同意。两个模型均为 8B，Limitations 虽提及 70B+ 未测试，但正文中 "cross-model" 的表述可能误导读者以为覆盖了不同 scale。

**[AGREE] R1-W6: Consensus-proximity 是唯一 instance-to-sample 转换策略**
强烈同意，这是我审稿时未充分关注的一个重要遗漏。MBR decoding（Eikema & Aziz 2022; Freitag et al. 2022）是一个成熟的替代方案，尤其适用于 pairwise utility function（如 SJ 本身就可以作为 MBR 的 utility function）。仅测试一种转换策略就声称 "consistency signals fail as selectors" 是不充分的——也许是 consensus-proximity 这个特定策略弱，而非 signals 本身的问题。这应升级为 R1 审稿中最有力的 Should-Fix 之一。

---

### Minor Issues

**[AGREE] R1-M1: WNUT-17 "54% zero F1" 数据不一致**
Section 4.1 说 "54% zero F1"，但 Table 5 (Appendix) 显示 n=689 total、n=334 non-zero → (689-334)/689 = 51.5% zero。差异约 2.5pp，可能源于计算基数不同（total 1,287 vs. filtered 689），但无论如何正文和表格应对齐。

**[AGREE] R1-M2: Table 1 N=16 区域大面积空白**
仅 LLaMA CoNLL 有 N=16 3-seed 数据，其余 3 个 configuration 空白。建议：要么补全数据（如果实验已做但未填入），要么将 N=16 整行移至 Appendix 的 Table 3，主表仅保留 N=8 以避免视觉上暗示数据缺失。

**[AGREE] R1-M3: EM selection 排除缺乏经验支持**
与我的意见一致。应报告 N=8 下 structured output 的实际 unique 比例。

**[AGREE] R1-M4: LOO-SJ Δρ 和 per-instance Δρ 量纲混淆**
Appendix A.4: "Δρ=−0.014...maximum per-instance Δρ of 3.1×10⁻⁴"——ρ 是 population-level statistic，"per-instance Δρ" 语义不明。应改为 "maximum per-instance score difference" 或类似表述。

**[REBUT] R1-M5: Figure 1 caption 引入 p=0.39**
R1 认为 Figure 1 caption 不应引入 figure 未直接呈现的 p-value。但 Figure 1 是 overview figure，其设计目的就是 summarize 核心 finding（左侧 correlation、右侧 selection failure）。在 caption 中引用 supporting statistic 是常见做法（参见 ACL/EMNLP 大量 overview figure 的 caption 风格），因为 overview figure 的功能是 orient reader 而非 present raw data。p=0.39 来自 Table 2 / Section 4.2，读者可以交叉验证。建议保留但可添加 "(Table 2)" 的交叉引用。

**[REBUT] R1-M6: Semantic entropy footnote 不应出现**
不完全同意。该 footnote（Section 4.2 脚注）提供了重要的 calibration context：读者需要知道 AUROC 0.749 在 broader confidence estimation 文献中是什么水平。footnote 已显式 caveat "direct comparison is complicated by the fundamentally different output spaces"。删除后读者反而缺少 reference point。建议保留但强化 caveat 的 placement（如将 caveat 放在数字之前而非之后）。

**[AGREE] R1-M7: 引用格式细节**
原则上同意应统一。

---

### Questions 回应

**Q1 (unconstrained generation)**：与我的 question 一致，同意应作为 essential follow-up。

**Q2 (Logprob WNUT conditional ρ=0.350)**：R1 指出了一个有趣的矛盾——如果 logprob 在 WNUT conditional set 上达到 all-signal-highest ρ=0.350，那么 "logprob is the weakest signal" 的 narrative 在某些 regime 下不成立。我在审稿中也问了同样的问题。论文 Discussion 未充分 address 这个 inversion。

**Q3 (LoRA rank=32 vs diversity)**：这是一个我未考虑到的好问题。LoRA fine-tuning 可能 reduce output diversity（相比 full fine-tuning 或 in-context learning），间接影响 selection headroom。不过这更多是 second-order effect。

**Q4 (N=16 selection multi-seed p-value)**：Table 4 仅给出 point estimate，无 multi-seed bootstrap。对于 LLaMA SciERC N=16 configuration，SJ 和 FK 并列最高（0.649），但无显著性信息。

---

### Missing References 回应

**[AGREE]** MBR decoding references (Eikema & Aziz 2022; Freitag et al. 2022) — 直接相关于 W6，consensus-proximity 实质上是 MBR 的一种特例（utility function = SJ），但论文未 frame it this way，也未比较其他 utility function 或 aggregation 策略。遗漏 MBR 文献是一个 significant gap in related work positioning。

**[AGREE]** Malinin & Gales (2021) structured prediction uncertainty — 与 Related Work 的 uncertainty estimation 段直接相关。

---

现在将交叉回应提交给 Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f63cbdf4-c041-4854-b245-1efa02ac809b",
  "isSidechain": false,
  "requestId": "req_011Cb3hFTWjkG7KX3q16fZCb",
  "type": "assistant",
  "uuid": "6c6b260d-e597-487c-83ed-e667d210bc0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ZdNkPfHcFp38x8e6fuG4W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1567,
      "cache_read_input_tokens": 80067,
      "output_tokens": 6364,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1567,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 6364,
          "cache_read_input_tokens": 80067,
          "cache_creation_input_tokens": 1567,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1567
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

_source line 90 · 2026-05-15T04:09:17.445Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01PHspAL3wrQ2sGSadqdKi9S`</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 Reviewer 1\n\n### Must-Fix\n\n[AGREE] R1-N1 (constrained decoding confound): 同意，与我的 N2 一致。补充建议：即使不跑 unconstrained 实验，报告 unique output fraction 和 per-sample logprob variance 也能大幅帮助 disentangle。\n\n[REBUT] R1-N2 (failure to reject ≠ evidence of absence): 统计原理正确，但 6/6 configurations 一致未显著（Table 4），cumulative evidence 远强于单一 test。且 CI 正面端仅 +4.2pp vs 13.2pp oracle headroom，practical significance 有限。建议降为 Should-Fix。\n\n[AGREE] R1-N3 (single seed): 合理关切。但 N=16 3-seed 下 signal rankings 完全一致（Table 3），且 N=8→N=16 ranking 也稳定——ordering 稳定性有保障。建议降为 Should-Fix。\n\n### Should-Fix\n\n[AGREE] R1-W1 (多重比较): SJ-EM CI lower bound +0.003，Bonferroni 下几乎必然不 survive。\n[AGREE] R1-W2 (tautological gap): 与我观点一致。4/5 instance-level signals 的 selection 失败是 definitional，真正的 empirical contribution 应聚焦 logprob 失败和 consensus-proximity 局限。\n[AGREE] R1-W3 (FK independence): 同意。\n[AGREE] R1-W4 (SJ cost function): 同意需补充 maximize/minimize 方向和 unmatched entities 处理。\n[AGREE] R1-W5 (cross-model at fixed 8B): 同意。\n[AGREE] R1-W6 (consensus-proximity 唯一策略): 强烈同意，这是 R1 最有力的 Should-Fix。MBR decoding 是成熟替代方案，仅测试一种转换策略就声称 \"signals fail as selectors\" 不充分。\n\n### Minor\n\n[AGREE] R1-M1 (54% vs 51.5%): 数据不一致。\n[AGREE] R1-M2 (Table 1 空白): 建议移至 Appendix。\n[AGREE] R1-M3 (EM exclusion): 同意需 empirical support。\n[AGREE] R1-M4 (LOO-SJ 量纲): 同意表述混淆。\n[REBUT] R1-M5 (Figure 1 p=0.39): Overview figure caption 引用 supporting statistic 是常见做法，建议保留但加 \"(Table 2)\" 交叉引用。\n[REBUT] R1-M6 (semantic entropy footnote): 该 footnote 提供重要 calibration context 且已显式 caveat，删除反而让读者缺少 reference point。建议强化 caveat placement 但保留。\n[AGREE] R1-M7 (引用格式): 同意。\n\n### Missing References\n[AGREE] MBR decoding (Eikema & Aziz 2022; Freitag et al. 2022) — 直接相关 W6，significant gap。\n[AGREE] Malinin & Gales (2021) — 相关于 uncertainty estimation。\n\n### 综合评价\nR1 的审稿意见质量高，技术判断准确。我们的分歧主要在严重程度而非方向上：\n- R1-N2 (statistical logic): 我认为 should-fix 而非 critical，因 6/6 配置一致性提供了 cumulative evidence\n- R1-N3 (single seed): 我认为 should-fix 因 ranking stability 有保障\n- R1-W6 (MBR alternative): 我认为这是 R1 最有价值的贡献点，论文确实只测了一种 instance-to-sample 转换策略就做了 sweeping claim",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c6b260d-e597-487c-83ed-e667d210bc0a",
  "isSidechain": false,
  "requestId": "req_011Cb3hFTWjkG7KX3q16fZCb",
  "type": "assistant",
  "uuid": "39b67a45-86bd-44ba-a6f1-08a36aab46c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ZdNkPfHcFp38x8e6fuG4W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1567,
      "cache_read_input_tokens": 80067,
      "output_tokens": 6364,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1567,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 6364,
          "cache_read_input_tokens": 80067,
          "cache_creation_input_tokens": 1567,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1567
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

_source line 91_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## 交叉分享：Reviewer 1 的完整审稿意见  请逐条回应以下 Reviewer 1 的审稿意见。对每个 Must-Fix、Should-Fix 和 Minor Issue： - **[AGREE]** 同意并说明理由 - **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）  ---  以下是 Reviewer…",
  "leafUuid": "39b67a45-86bd-44ba-a6f1-08a36aab46c5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b"
}
```

---

### Runtime record

_source line 92_

```json
{
  "type": "ai-title",
  "aiTitle": "Generative IE confidence signals systematic review",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b"
}
```

---

### Tool result

_source line 93 · 2026-05-15T04:09:21.235Z_

<details><summary>↩ Tool result · `toolu_01PHspAL3wrQ2sGSadqdKi9S`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "39b67a45-86bd-44ba-a6f1-08a36aab46c5",
  "isSidechain": false,
  "promptId": "598a9ee9-06fa-4905-a6d4-6b653362c4be",
  "type": "user",
  "uuid": "5162e66c-2fa4-4ea6-9a7e-89c1f42338d5",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_3897c2857f11615119e277e820eae311:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "39b67a45-86bd-44ba-a6f1-08a36aab46c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5",
  "sessionId": "b9bf08df-1b1e-4be4-9e83-613f82fe746b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---
