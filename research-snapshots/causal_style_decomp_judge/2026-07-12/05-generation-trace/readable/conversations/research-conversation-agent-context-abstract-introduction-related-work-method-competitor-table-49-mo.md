# Research conversation: <agent_context> 论文已有 Abstract, Introduction, Related Work, Method, Competitor Table 五个组件。引用了约 49 篇论文，主要来自 model collapse

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 101
- **Recorded user turns:** 1
- **Tool calls:** 27
- **Original source:** `logs/chats/exported-trajectories/account-2/2878417b-8f77-4e7b-b95b-31a32289cc2b.jsonl`
- **Structured JSON:** [`74b50ea59ae5d12f425b.json`](../../sessions/74/74b50ea59ae5d12f425b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T02:10:30.466Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T02:10:30.466Z",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "content": "&lt;agent_context>\n论文已有 Abstract, Introduction, Related Work, Method, Competitor Table 五个组件。引用了约 49 篇论文，主要来自 model collapse, spectral analysis, data contamination 领域。需要编译完整 .bib 文件确保所有引用可编译。\n&lt;/agent_context>\n\n&lt;project_context>\n# 项目: collapse_severity_monitor\n\n## 运行环境\n- 服务器名: autodl-5090\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh autodl-5090  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/autodl-tmp/collapse_severity_monitor\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：编译论文 .bib 引用文件\n\n### 前置阅读（必须）\n1. 读所有已有论文章节，提取 `\\cite{...}` 和 `\\citep{...}` 中的 citation keys：\n   - `paper/sections/abstract.tex`\n   - `paper/sections/introduction.tex`\n   - `paper/sections/related_work.tex`\n   - `paper/sections/method.tex`\n   - `paper/tables/competitor_comparison.tex`\n2. 读文献资料：\n   - 本地 `/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/_project/report/related_work_notes_45da09.md`\n   - 本地 `/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/_project/report/literature_gap_search.md`\n   - `read_project_file(file=\"literature_map.yaml\")`（如果存在）\n\n### 要求\n1. 从论文章节中提取所有 citation keys\n2. 为每个 key 编写正确的 BibTeX entry：\n   - 优先从 arXiv / conference proceedings 获取准确信息\n   - 用 WebSearch 验证每篇论文的标题、作者、年份、venue\n   - 对于 arXiv preprints 用 `@article`，已发表的用 `@inproceedings` 或 `@article`\n3. 格式要求：\n   - 每个 entry 必须有 title, author, year\n   - 会议论文：booktitle 字段\n   - arXiv：eprint, archivePrefix, primaryClass 字段\n   - 按 citation key 字母排序\n4. 输出到 `/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/references.bib`\n5. 如果 paper/ 目录不存在，创建\n\n### 验证\n- 统计 citation keys 总数\n- 确认每个 key 都有对应 entry\n- 标注任何找不到对应论文的 key（可能是论文章节中的 typo）\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T02:10:30.470Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T02:10:30.470Z",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b"
}
```

---

## Round 1

99 recorded events

### User

_source line 3 · 2026-05-15T02:10:30.506Z_

&lt;agent_context>
论文已有 Abstract, Introduction, Related Work, Method, Competitor Table 五个组件。引用了约 49 篇论文，主要来自 model collapse, spectral analysis, data contamination 领域。需要编译完整 .bib 文件确保所有引用可编译。
&lt;/agent_context>

&lt;project_context>
# 项目: collapse_severity_monitor

## 运行环境
- 服务器名: autodl-5090
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh autodl-5090  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/autodl-tmp/collapse_severity_monitor


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：编译论文 .bib 引用文件

### 前置阅读（必须）
1. 读所有已有论文章节，提取 `\cite{...}` 和 `\citep{...}` 中的 citation keys：
   - `paper/sections/abstract.tex`
   - `paper/sections/introduction.tex`
   - `paper/sections/related_work.tex`
   - `paper/sections/method.tex`
   - `paper/tables/competitor_comparison.tex`
2. 读文献资料：
   - 本地 `/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/_project/report/related_work_notes_45da09.md`
   - 本地 `/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/_project/report/literature_gap_search.md`
   - `read_project_file(file="literature_map.yaml")`（如果存在）

### 要求
1. 从论文章节中提取所有 citation keys
2. 为每个 key 编写正确的 BibTeX entry：
   - 优先从 arXiv / conference proceedings 获取准确信息
   - 用 WebSearch 验证每篇论文的标题、作者、年份、venue
   - 对于 arXiv preprints 用 `@article`，已发表的用 `@inproceedings` 或 `@article`
3. 格式要求：
   - 每个 entry 必须有 title, author, year
   - 会议论文：booktitle 字段
   - arXiv：eprint, archivePrefix, primaryClass 字段
   - 按 citation key 字母排序
4. 输出到 `/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/references.bib`
5. 如果 paper/ 目录不存在，创建

### 验证
- 统计 citation keys 总数
- 确认每个 key 都有对应 entry
- 标注任何找不到对应论文的 key（可能是论文章节中的 typo）


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "a7003b6e-3a25-4888-837a-59f1925bbd90",
  "type": "user",
  "uuid": "a650c8a3-edeb-4a2e-9250-d26a817e5c52",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T02:10:30.505Z_

```json
{
  "parentUuid": "a650c8a3-edeb-4a2e-9250-d26a817e5c52",
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
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
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
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "bc4e92ca-d9c8-41c7-abd5-3eae8dfeebd0",
  "timestamp": "2026-05-15T02:10:30.505Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T02:10:30.505Z_

```json
{
  "parentUuid": "bc4e92ca-d9c8-41c7-abd5-3eae8dfeebd0",
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
  "uuid": "8844211a-fc6a-4f98-9dcf-f636ff16a5bd",
  "timestamp": "2026-05-15T02:10:30.505Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-15T02:10:30.505Z_

```json
{
  "parentUuid": "8844211a-fc6a-4f98-9dcf-f636ff16a5bd",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5c43a947-d6ea-4dc6-99dc-64e7a7b2b888",
  "timestamp": "2026-05-15T02:10:30.505Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
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
  "aiTitle": "Compile bibliography file for paper citations",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b"
}
```

---

### Assistant

_source line 8 · 2026-05-15T02:10:33.396Z_

I'll start by reading all the paper sections to extract citation keys, and the literature reference files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c43a947-d6ea-4dc6-99dc-64e7a7b2b888",
  "isSidechain": false,
  "requestId": "req_011Cb3YQ5PB5pmaXZH39uip6",
  "type": "assistant",
  "uuid": "986ca2a2-017d-49b2-8f2c-4b524cf3ffb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J4FBbgT8Qg63L9A96icQ8m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11431,
      "cache_read_input_tokens": 11841,
      "output_tokens": 285,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 285,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11431
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

_source line 9 · 2026-05-15T02:10:34.371Z_

<details open><summary>🔧 Tool call — Glob · `toolu_017ZgjYdmTBXgrzXB3ca3sAA`</summary>

```json
{
  "pattern": "paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "986ca2a2-017d-49b2-8f2c-4b524cf3ffb6",
  "isSidechain": false,
  "requestId": "req_011Cb3YQ5PB5pmaXZH39uip6",
  "type": "assistant",
  "uuid": "99fceb6a-79da-47a7-88ec-f524bf9ae64b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J4FBbgT8Qg63L9A96icQ8m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11431,
      "cache_read_input_tokens": 11841,
      "output_tokens": 285,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 285,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11431
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

_source line 10 · 2026-05-15T02:10:34.415Z_

<details><summary>↩ Tool result · `toolu_017ZgjYdmTBXgrzXB3ca3sAA`</summary>

```text
paper/sections/related_work.tex
paper/sections/method.tex
paper/sections/introduction.tex
paper/sections/abstract.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99fceb6a-79da-47a7-88ec-f524bf9ae64b",
  "isSidechain": false,
  "promptId": "a7003b6e-3a25-4888-837a-59f1925bbd90",
  "type": "user",
  "uuid": "23dcb23d-ed11-432c-9e67-eb31cbcea2e7",
  "toolUseResult": {
    "filenames": [
      "paper/sections/related_work.tex",
      "paper/sections/method.tex",
      "paper/sections/introduction.tex",
      "paper/sections/abstract.tex"
    ],
    "durationMs": 20,
    "numFiles": 4,
    "truncated": false
  },
  "sourceToolAssistantUUID": "99fceb6a-79da-47a7-88ec-f524bf9ae64b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T02:10:34.899Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01518AMp2fcuwhbfobBnNav6`</summary>

```json
{
  "pattern": "paper/tables/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23dcb23d-ed11-432c-9e67-eb31cbcea2e7",
  "isSidechain": false,
  "requestId": "req_011Cb3YQ5PB5pmaXZH39uip6",
  "type": "assistant",
  "uuid": "7a3b6092-1af8-454c-9837-71be20a5a9ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J4FBbgT8Qg63L9A96icQ8m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11431,
      "cache_read_input_tokens": 11841,
      "output_tokens": 285,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 285,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11431
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

_source line 12 · 2026-05-15T02:10:34.925Z_

<details><summary>↩ Tool result · `toolu_01518AMp2fcuwhbfobBnNav6`</summary>

```text
paper/tables/competitor_comparison.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a3b6092-1af8-454c-9837-71be20a5a9ce",
  "isSidechain": false,
  "promptId": "a7003b6e-3a25-4888-837a-59f1925bbd90",
  "type": "user",
  "uuid": "9452ac2c-b7d6-4184-bb95-3338df9792ee",
  "toolUseResult": {
    "filenames": [
      "paper/tables/competitor_comparison.tex"
    ],
    "durationMs": 20,
    "numFiles": 1,
    "truncated": false
  },
  "sourceToolAssistantUUID": "7a3b6092-1af8-454c-9837-71be20a5a9ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T02:10:35.221Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01LVMiBbsQgY6b6w1DzuaF63`</summary>

```json
{
  "pattern": "paper/**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9452ac2c-b7d6-4184-bb95-3338df9792ee",
  "isSidechain": false,
  "requestId": "req_011Cb3YQ5PB5pmaXZH39uip6",
  "type": "assistant",
  "uuid": "bb0b9e4f-b289-4546-834f-636abf7cb6b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J4FBbgT8Qg63L9A96icQ8m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11431,
      "cache_read_input_tokens": 11841,
      "output_tokens": 285,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 285,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11431
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

_source line 14 · 2026-05-15T02:10:35.301Z_

<details><summary>↩ Tool result · `toolu_01LVMiBbsQgY6b6w1DzuaF63`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb0b9e4f-b289-4546-834f-636abf7cb6b9",
  "isSidechain": false,
  "promptId": "a7003b6e-3a25-4888-837a-59f1925bbd90",
  "type": "user",
  "uuid": "e5021419-9a87-409d-8b47-8157bb2e31f6",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 67,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "bb0b9e4f-b289-4546-834f-636abf7cb6b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T02:10:38.068Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Lsh5gMwj7R7D9KxeKUfxmL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5021419-9a87-409d-8b47-8157bb2e31f6",
  "isSidechain": false,
  "requestId": "req_011Cb3YQRuhpkkZTmW9t91hz",
  "type": "assistant",
  "uuid": "b105e4cb-0c54-4695-97fe-c8740c8347d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q97HJeMTuKyisgq8AC2ect",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 415,
      "cache_read_input_tokens": 23272,
      "output_tokens": 371,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 415,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 371,
          "cache_read_input_tokens": 23272,
          "cache_creation_input_tokens": 415,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 415
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

_source line 16 · 2026-05-15T02:10:38.077Z_

<details><summary>↩ Tool result · `toolu_01Lsh5gMwj7R7D9KxeKUfxmL`</summary>

```text
1	% Abstract — collapse_severity_monitor
2	% MVP evidence: mvp_frac50_100, within_gen_analysis, per_layer_analysis_v5
3	% Qwen2.5-0.5B, WikiText-2, QLoRA, 3 fractions (0/50/100%), seed 42, 5 generations
4	
5	\begin{abstract}
6	Iterative training on synthetic data causes model collapse---progressive degradation in output quality and diversity---yet practitioners lack real-time tools to quantify its severity during training.
7	We systematically evaluate four families of training-time signals---spectral (stable rank, spectral entropy), output (token entropy, perplexity), gradient, and downstream---as collapse severity monitors across contamination levels and generational depth.
8	In controlled experiments (Qwen2.5-0.5B, WikiText-2, 5~iterative generations), spectral and output signals maintain monotonic severity ordering, with perplexity increasing $53\times$ and stable rank $6.6\times$ at full synthetic contamination.
9	Stable rank deviation reaches 34.4\% by 3\% of training progress, enabling early warning before catastrophic degradation materializes.
10	We document a signal taxonomy: spectral signals provide the earliest warning, output signals track severity most reliably, while gradient norms are non-monotonic under QLoRA and downstream benchmarks show minimal sensitivity at small scale.
11	Per-layer analysis reveals non-uniform collapse propagation, with specific sublayers exhibiting anomalous rank collapse that precedes aggregate-level indicators.
12	These findings provide practitioners with actionable guidance for monitoring-based collapse detection during training.
13	\end{abstract}
14	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b105e4cb-0c54-4695-97fe-c8740c8347d5",
  "isSidechain": false,
  "promptId": "a7003b6e-3a25-4888-837a-59f1925bbd90",
  "type": "user",
  "uuid": "25b9ad10-0450-4eca-b63e-a22c0174d453",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/abstract.tex",
      "content": "% Abstract — collapse_severity_monitor\n% MVP evidence: mvp_frac50_100, within_gen_analysis, per_layer_analysis_v5\n% Qwen2.5-0.5B, WikiText-2, QLoRA, 3 fractions (0/50/100%), seed 42, 5 generations\n\n\\begin{abstract}\nIterative training on synthetic data causes model collapse---progressive degradation in output quality and diversity---yet practitioners lack real-time tools to quantify its severity during training.\nWe systematically evaluate four families of training-time signals---spectral (stable rank, spectral entropy), output (token entropy, perplexity), gradient, and downstream---as collapse severity monitors across contamination levels and generational depth.\nIn controlled experiments (Qwen2.5-0.5B, WikiText-2, 5~iterative generations), spectral and output signals maintain monotonic severity ordering, with perplexity increasing $53\\times$ and stable rank $6.6\\times$ at full synthetic contamination.\nStable rank deviation reaches 34.4\\% by 3\\% of training progress, enabling early warning before catastrophic degradation materializes.\nWe document a signal taxonomy: spectral signals provide the earliest warning, output signals track severity most reliably, while gradient norms are non-monotonic under QLoRA and downstream benchmarks show minimal sensitivity at small scale.\nPer-layer analysis reveals non-uniform collapse propagation, with specific sublayers exhibiting anomalous rank collapse that precedes aggregate-level indicators.\nThese findings provide practitioners with actionable guidance for monitoring-based collapse detection during training.\n\\end{abstract}\n",
      "numLines": 14,
      "startLine": 1,
      "totalLines": 14
    }
  },
  "sourceToolAssistantUUID": "b105e4cb-0c54-4695-97fe-c8740c8347d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T02:10:38.447Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QkJr6DDonn4jmWM9tbGrBm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25b9ad10-0450-4eca-b63e-a22c0174d453",
  "isSidechain": false,
  "requestId": "req_011Cb3YQRuhpkkZTmW9t91hz",
  "type": "assistant",
  "uuid": "3c43298f-7aee-40ea-bc72-9236d09c8ff4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q97HJeMTuKyisgq8AC2ect",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 415,
      "cache_read_input_tokens": 23272,
      "output_tokens": 371,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 415,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 371,
          "cache_read_input_tokens": 23272,
          "cache_creation_input_tokens": 415,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 415
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

_source line 18 · 2026-05-15T02:10:39.742Z_

<details><summary>↩ Tool result · `toolu_01HjECHPr9daztmtw6YiQfHn`</summary>

```text
1	% Requires: \usepackage{booktabs, xcolor, amssymb, adjustbox}
2	% Define symbols if not already defined:
3	% \newcommand{\cmark}{\ding{51}}  % or use \checkmark
4	% \newcommand{\xmark}{\ding{55}}  % or use $\times$
5	\providecommand{\cmark}{\checkmark}
6	\providecommand{\xmark}{$\times$}
7	\providecommand{\pmark}{\textcolor{gray}{partial}}
8	
9	\begin{table*}[t]
10	\centering
11	\caption{
12	Comparison of collapse monitoring approaches.
13	\cmark\ = fully supported, \xmark\ = not supported, \pmark\ = partially addressed.
14	SIGMA operates on output embeddings post-hoc; Kalinowski monitors topology online but in a different setting;
15	ForTIFAI modifies the loss to mitigate collapse rather than detect it.
16	Our work is the first to combine online spectral/entropic monitoring with per-layer granularity
17	and early warning in the iterative synthetic data setting.
18	}
19	\label{tab:competitor_comparison}
20	\begin{adjustbox}{max width=\textwidth}
21	\begin{tabular}{@{}lcccc@{}}
22	\toprule
23	\textbf{Capability} & \textbf{SIGMA} & \textbf{Kalinowski} & \textbf{ForTIFAI} & \textbf{Ours} \\
24	 & \citep{Gu2026} & \citep{Kalinowski2026} & \citep{Zibakhsh2025} & \\
25	\midrule
26	Signal type
27	  & Gram matrix spectrum
28	  & Persistent homology
29	  & Output loss (TCE)
30	  & \makecell{Weight spectrum + output\\entropy/PPL + gradient norm} \\[4pt]
31	Online monitoring
32	  & \xmark\ (post-hoc)
33	  & \cmark
34	  & \pmark\ (training-time loss mod.)
35	  & \cmark \\[2pt]
36	Clean reference needed
37	  & \cmark\ (required)
38	  & \xmark
39	  & \xmark
40	  & \xmark \\[2pt]
41	Multi-signal comparison
42	  & \xmark\ (spectrum only)
43	  & \xmark\ (topology only)
44	  & \xmark\ (loss only)
45	  & \cmark\ (4 signal families) \\[2pt]
46	Cross-scale validation
47	  & \xmark
48	  & \xmark
49	  & \xmark
50	  & \cmark\ (0.5B, 1.5B) \\[2pt]
51	Cross-domain validation
52	  & \xmark
53	  & \xmark
54	  & \pmark\ (2 datasets)
55	  & \cmark\ (WikiText, PubMed) \\[2pt]
56	Per-layer analysis
57	  & \xmark
58	  & \xmark
59	  & \xmark
60	  & \cmark \\[2pt]
61	Early warning
62	  & \xmark
63	  & \pmark\ (different setting)
64	  & \xmark
65	  & \cmark\ (3\% training progress) \\[2pt]
66	Iterative collapse focus
67	  & \xmark
68	  & \xmark
69	  & \cmark
70	  & \cmark\ (5 generations) \\[2pt]
71	Statistical rigor
72	  & N/A
73	  & N/A
74	  & 1 seed
75	  & 5 seeds, bootstrap CIs \\
76	\bottomrule
77	\end{tabular}
78	\end{adjustbox}
79	\end{table*}
80	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "514460af-7073-4603-8b7a-765915b961c8",
  "isSidechain": false,
  "promptId": "a7003b6e-3a25-4888-837a-59f1925bbd90",
  "type": "user",
  "uuid": "7483eb10-6401-4f0b-9830-6902a523aea2",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/tables/competitor_comparison.tex",
      "content": "% Requires: \\usepackage{booktabs, xcolor, amssymb, adjustbox}\n% Define symbols if not already defined:\n% \\newcommand{\\cmark}{\\ding{51}}  % or use \\checkmark\n% \\newcommand{\\xmark}{\\ding{55}}  % or use $\\times$\n\\providecommand{\\cmark}{\\checkmark}\n\\providecommand{\\xmark}{$\\times$}\n\\providecommand{\\pmark}{\\textcolor{gray}{partial}}\n\n\\begin{table*}[t]\n\\centering\n\\caption{\nComparison of collapse monitoring approaches.\n\\cmark\\ = fully supported, \\xmark\\ = not supported, \\pmark\\ = partially addressed.\nSIGMA operates on output embeddings post-hoc; Kalinowski monitors topology online but in a different setting;\nForTIFAI modifies the loss to mitigate collapse rather than detect it.\nOur work is the first to combine online spectral/entropic monitoring with per-layer granularity\nand early warning in the iterative synthetic data setting.\n}\n\\label{tab:competitor_comparison}\n\\begin{adjustbox}{max width=\\textwidth}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Capability} & \\textbf{SIGMA} & \\textbf{Kalinowski} & \\textbf{ForTIFAI} & \\textbf{Ours} \\\\\n & \\citep{Gu2026} & \\citep{Kalinowski2026} & \\citep{Zibakhsh2025} & \\\\\n\\midrule\nSignal type\n  & Gram matrix spectrum\n  & Persistent homology\n  & Output loss (TCE)\n  & \\makecell{Weight spectrum + output\\\\entropy/PPL + gradient norm} \\\\[4pt]\nOnline monitoring\n  & \\xmark\\ (post-hoc)\n  & \\cmark\n  & \\pmark\\ (training-time loss mod.)\n  & \\cmark \\\\[2pt]\nClean reference needed\n  & \\cmark\\ (required)\n  & \\xmark\n  & \\xmark\n  & \\xmark \\\\[2pt]\nMulti-signal comparison\n  & \\xmark\\ (spectrum only)\n  & \\xmark\\ (topology only)\n  & \\xmark\\ (loss only)\n  & \\cmark\\ (4 signal families) \\\\[2pt]\nCross-scale validation\n  & \\xmark\n  & \\xmark\n  & \\xmark\n  & \\cmark\\ (0.5B, 1.5B) \\\\[2pt]\nCross-domain validation\n  & \\xmark\n  & \\xmark\n  & \\pmark\\ (2 datasets)\n  & \\cmark\\ (WikiText, PubMed) \\\\[2pt]\nPer-layer analysis\n  & \\xmark\n  & \\xmark\n  & \\xmark\n  & \\cmark \\\\[2pt]\nEarly warning\n  & \\xmark\n  & \\pmark\\ (different setting)\n  & \\xmark\n  & \\cmark\\ (3\\% training progress) \\\\[2pt]\nIterative collapse focus\n  & \\xmark\n  & \\xmark\n  & \\cmark\n  & \\cmark\\ (5 generations) \\\\[2pt]\nStatistical rigor\n  & N/A\n  & N/A\n  & 1 seed\n  & 5 seeds, bootstrap CIs \\\\\n\\bottomrule\n\\end{tabular}\n\\end{adjustbox}\n\\end{table*}\n",
      "numLines": 80,
      "startLine": 1,
      "totalLines": 80
    }
  },
  "sourceToolAssistantUUID": "514460af-7073-4603-8b7a-765915b961c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T02:10:38.453Z_

<details><summary>↩ Tool result · `toolu_01QkJr6DDonn4jmWM9tbGrBm`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Large language models (LLMs) increasingly consume their own outputs: web-scraped training corpora now contain substantial fractions of machine-generated text, and practitioners routinely fine-tune on synthetic data produced by prior model generations.
5	This recursive dynamic creates a self-consuming loop in which each successive model trains on data shaped by its predecessors.
6	\citet{Shumailov2024} demonstrated that such iterative retraining causes \emph{model collapse}---an irreversible degradation in which distribution tails vanish, output diversity contracts, and previously acquired knowledge is lost.
7	\citet{Alemohammad2024} formalized three self-consuming loop variants and proved that without fresh real data, either precision or recall must degrade.
8	Subsequent theoretical work has strengthened these findings: even trace synthetic contamination ($1/1000$ fraction) induces collapse at sufficient scale~\citep{Dohmatob2025}, and the effect compounds across iterations with accelerating severity~\citep{Dohmatob2024_tails,Fu2024_icml}.
9	As synthetic data generation becomes ubiquitous---for alignment, augmentation, and distillation---the need to detect and quantify collapse during training, before it reaches catastrophic levels, is increasingly urgent.
10	
11	Despite extensive theoretical characterization of model collapse, the literature offers practitioners surprisingly little guidance for \emph{monitoring} it in real time.
12	Existing work concentrates on two poles: post-hoc analysis of finished models via test loss or distributional divergence~\citep{Shumailov2024,Alemohammad2024}, and prevention strategies such as data accumulation~\citep{Gerstgrasser2024}, loss modification~\citep{Zibakhsh2025}, or synthetic data filtering~\citep{Feng2025}.
13	Neither pole tells a practitioner, mid-training, how severely their model is collapsing or whether to intervene.
14	The two closest concurrent works---SIGMA~\citep{Gu2026}, which analyzes output embedding spectra, and the topological monitor of \citet{Kalinowski2026}---each address part of this gap but carry significant limitations: SIGMA requires a clean reference distribution and lacks per-layer granularity; the topological approach incurs high computational overhead.
15	Neither provides a systematic comparison of which training-time signals best track collapse across severity levels, nor do they establish quantitative early warning thresholds.
16	
17	We conduct a systematic empirical analysis of training dynamic signals as model collapse severity monitors.
18	Rather than proposing a new detection method, we take an analysis paper approach: we evaluate four families of training-time signals---spectral (stable rank, spectral entropy), output (token entropy, perplexity), gradient (L2 norm), and downstream (HellaSwag accuracy)---across contamination levels ($\alpha \in \{0, 0.1, 0.25, 0.5, 0.75, 1.0\}$), generational depth ($G=5$), model scales (0.5B; 1.5B in progress), and text domains (WikiText-2; PubMed planned).
19	Our goal is to determine which signals track collapse severity, when they first diverge from healthy baselines, and where they saturate or actively mislead---producing a practitioner-oriented monitoring guide grounded in controlled experiments.
20	
21	Our main findings are:
22	
23	\begin{enumerate}
24	    \item \textbf{Signal--severity correlation.}
25	    Spectral and output signals reliably track collapse severity across contamination levels and generational depth.
26	    %% Source: mvp_frac50_100 — 3 fractions (0/50/100%), seed 42, Qwen2.5-0.5B, WikiText-2
27	    In our initial experiments (0.5B scale, WikiText-2), stable rank, spectral entropy, token entropy, and perplexity each maintain monotonic ordering across tested contamination fractions ($|\rho| = 1.0$ per generation with $n=3$ fractions; 6-fraction $\times$ 5-seed validation in progress).
28	    %% Pending: plan_001 — 6 fractions × 5 seeds × 5 generations = 150 runs
29	    Perplexity exhibits super-linear growth across generations at full contamination ($15.7 \to 839.2$ over 5 generations), consistent with accelerating degradation predicted by theory.
30	
31	    \item \textbf{Early warning at 3\% training progress.}
32	    %% Source: within_gen_analysis — within-generation temporal analysis, step-level signals
33	    Stable rank deviation between the fully contaminated ($\alpha=1.0$) and clean ($\alpha=0$) conditions reaches 34.4\% by step 50 of 1{,}540 (${\sim}3\%$ of training), with token entropy and perplexity following at 24.5\% and 17.7\% deviation respectively.
34	    All three signals achieve AUROC~$= 1.0$ for collapse detection at this early checkpoint, indicating that collapse leaves detectable spectral and entropic fingerprints well before downstream metrics respond.
35	
36	    \item \textbf{Signal taxonomy: operating ranges and failure modes.}
37	    %% Source: mvp_frac50_100, within_gen_analysis, per_layer_analysis_v5
38	    Different signal families are informative at different severity levels and scales.
39	    Gradient norm is non-monotonic with contamination under QLoRA, limiting its standalone utility.
40	    Downstream task accuracy (HellaSwag) shows minimal sensitivity at the 0.5B scale (1.2\% drop despite catastrophic perplexity explosion), suggesting that benchmark performance is a poor proxy for generative collapse at small scale.
41	    Per-layer spectral analysis reveals non-uniform collapse propagation, with specific layers (e.g., layer 12 \texttt{down\_proj}) exhibiting anomalous spectral signatures that precede aggregate-level signals.
42	    This taxonomy provides actionable guidance: practitioners should monitor spectral signals for early warning and output signals for severity tracking, while treating gradient norms and small-scale benchmark accuracy with caution.
43	\end{enumerate}
44	
45	The remainder of this paper is organized as follows.
46	Section~\ref{sec:related_work} surveys collapse theory, spectral analysis, and training dynamics, positioning our contribution relative to SIGMA and other concurrent work.
47	Section~\ref{sec:method} details our iterative contamination protocol, signal definitions, and evaluation methodology.
48	Section~\ref{sec:results} presents cross-fraction correlation, within-generation early warning, and per-layer analyses.
49	Section~\ref{sec:discussion} discusses implications for practitioners, limitations, and failure modes.
50	Section~\ref{sec:conclusion} concludes.
51	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c43298f-7aee-40ea-bc72-9236d09c8ff4",
  "isSidechain": false,
  "promptId": "a7003b6e-3a25-4888-837a-59f1925bbd90",
  "type": "user",
  "uuid": "a354d378-f1e4-4a0a-b2d2-faeef379d583",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nLarge language models (LLMs) increasingly consume their own outputs: web-scraped training corpora now contain substantial fractions of machine-generated text, and practitioners routinely fine-tune on synthetic data produced by prior model generations.\nThis recursive dynamic creates a self-consuming loop in which each successive model trains on data shaped by its predecessors.\n\\citet{Shumailov2024} demonstrated that such iterative retraining causes \\emph{model collapse}---an irreversible degradation in which distribution tails vanish, output diversity contracts, and previously acquired knowledge is lost.\n\\citet{Alemohammad2024} formalized three self-consuming loop variants and proved that without fresh real data, either precision or recall must degrade.\nSubsequent theoretical work has strengthened these findings: even trace synthetic contamination ($1/1000$ fraction) induces collapse at sufficient scale~\\citep{Dohmatob2025}, and the effect compounds across iterations with accelerating severity~\\citep{Dohmatob2024_tails,Fu2024_icml}.\nAs synthetic data generation becomes ubiquitous---for alignment, augmentation, and distillation---the need to detect and quantify collapse during training, before it reaches catastrophic levels, is increasingly urgent.\n\nDespite extensive theoretical characterization of model collapse, the literature offers practitioners surprisingly little guidance for \\emph{monitoring} it in real time.\nExisting work concentrates on two poles: post-hoc analysis of finished models via test loss or distributional divergence~\\citep{Shumailov2024,Alemohammad2024}, and prevention strategies such as data accumulation~\\citep{Gerstgrasser2024}, loss modification~\\citep{Zibakhsh2025}, or synthetic data filtering~\\citep{Feng2025}.\nNeither pole tells a practitioner, mid-training, how severely their model is collapsing or whether to intervene.\nThe two closest concurrent works---SIGMA~\\citep{Gu2026}, which analyzes output embedding spectra, and the topological monitor of \\citet{Kalinowski2026}---each address part of this gap but carry significant limitations: SIGMA requires a clean reference distribution and lacks per-layer granularity; the topological approach incurs high computational overhead.\nNeither provides a systematic comparison of which training-time signals best track collapse across severity levels, nor do they establish quantitative early warning thresholds.\n\nWe conduct a systematic empirical analysis of training dynamic signals as model collapse severity monitors.\nRather than proposing a new detection method, we take an analysis paper approach: we evaluate four families of training-time signals---spectral (stable rank, spectral entropy), output (token entropy, perplexity), gradient (L2 norm), and downstream (HellaSwag accuracy)---across contamination levels ($\\alpha \\in \\{0, 0.1, 0.25, 0.5, 0.75, 1.0\\}$), generational depth ($G=5$), model scales (0.5B; 1.5B in progress), and text domains (WikiText-2; PubMed planned).\nOur goal is to determine which signals track collapse severity, when they first diverge from healthy baselines, and where they saturate or actively mislead---producing a practitioner-oriented monitoring guide grounded in controlled experiments.\n\nOur main findings are:\n\n\\begin{enumerate}\n    \\item \\textbf{Signal--severity correlation.}\n    Spectral and output signals reliably track collapse severity across contamination levels and generational depth.\n    %% Source: mvp_frac50_100 — 3 fractions (0/50/100%), seed 42, Qwen2.5-0.5B, WikiText-2\n    In our initial experiments (0.5B scale, WikiText-2), stable rank, spectral entropy, token entropy, and perplexity each maintain monotonic ordering across tested contamination fractions ($|\\rho| = 1.0$ per generation with $n=3$ fractions; 6-fraction $\\times$ 5-seed validation in progress).\n    %% Pending: plan_001 — 6 fractions × 5 seeds × 5 generations = 150 runs\n    Perplexity exhibits super-linear growth across generations at full contamination ($15.7 \\to 839.2$ over 5 generations), consistent with accelerating degradation predicted by theory.\n\n    \\item \\textbf{Early warning at 3\\% training progress.}\n    %% Source: within_gen_analysis — within-generation temporal analysis, step-level signals\n    Stable rank deviation between the fully contaminated ($\\alpha=1.0$) and clean ($\\alpha=0$) conditions reaches 34.4\\% by step 50 of 1{,}540 (${\\sim}3\\%$ of training), with token entropy and perplexity following at 24.5\\% and 17.7\\% deviation respectively.\n    All three signals achieve AUROC~$= 1.0$ for collapse detection at this early checkpoint, indicating that collapse leaves detectable spectral and entropic fingerprints well before downstream metrics respond.\n\n    \\item \\textbf{Signal taxonomy: operating ranges and failure modes.}\n    %% Source: mvp_frac50_100, within_gen_analysis, per_layer_analysis_v5\n    Different signal families are informative at different severity levels and scales.\n    Gradient norm is non-monotonic with contamination under QLoRA, limiting its standalone utility.\n    Downstream task accuracy (HellaSwag) shows minimal sensitivity at the 0.5B scale (1.2\\% drop despite catastrophic perplexity explosion), suggesting that benchmark performance is a poor proxy for generative collapse at small scale.\n    Per-layer spectral analysis reveals non-uniform collapse propagation, with specific layers (e.g., layer 12 \\texttt{down\\_proj}) exhibiting anomalous spectral signatures that precede aggregate-level signals.\n    This taxonomy provides actionable guidance: practitioners should monitor spectral signals for early warning and output signals for severity tracking, while treating gradient norms and small-scale benchmark accuracy with caution.\n\\end{enumerate}\n\nThe remainder of this paper is organized as follows.\nSection~\\ref{sec:related_work} surveys collapse theory, spectral analysis, and training dynamics, positioning our contribution relative to SIGMA and other concurrent work.\nSection~\\ref{sec:method} details our iterative contamination protocol, signal definitions, and evaluation methodology.\nSection~\\ref{sec:results} presents cross-fraction correlation, within-generation early warning, and per-layer analyses.\nSection~\\ref{sec:discussion} discusses implications for practitioners, limitations, and failure modes.\nSection~\\ref{sec:conclusion} concludes.\n",
      "numLines": 51,
      "startLine": 1,
      "totalLines": 51
    }
  },
  "sourceToolAssistantUUID": "3c43298f-7aee-40ea-bc72-9236d09c8ff4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T02:10:38.865Z_

<details open><summary>🔧 Tool call — Read · `toolu_014uJyNEztPThXWiHXLhXFYZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a354d378-f1e4-4a0a-b2d2-faeef379d583",
  "isSidechain": false,
  "requestId": "req_011Cb3YQRuhpkkZTmW9t91hz",
  "type": "assistant",
  "uuid": "7842b6cf-92a1-41f5-a811-857eea741845",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q97HJeMTuKyisgq8AC2ect",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 415,
      "cache_read_input_tokens": 23272,
      "output_tokens": 371,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 415,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 371,
          "cache_read_input_tokens": 23272,
          "cache_creation_input_tokens": 415,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 415
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

_source line 21 · 2026-05-15T02:10:38.869Z_

<details><summary>↩ Tool result · `toolu_014uJyNEztPThXWiHXLhXFYZ`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\subsection{Model Collapse in Iterative Training}
5	
6	The phenomenon of model collapse---progressive degradation when models are iteratively trained on their own outputs---has been established across multiple generative families.
7	\citet{Shumailov2024} provided the first systematic demonstration that iterative training on synthetic data causes distribution tails to vanish, leading to irreversible quality loss in LLMs, VAEs, and GMMs.
8	\citet{Alemohammad2024} formalized three self-consuming loop variants (fully synthetic, synthetic augmentation, and fresh data mixing), proving that without fresh real data, either precision or recall must degrade.
9	Theoretical analyses have since strengthened these findings: \citet{Dohmatob2025} proved via operator-valued free probability theory that even a $1/1000$ synthetic data fraction induces collapse and that larger models amplify the effect, while \citet{Dohmatob2024_tails} showed collapse alters scaling laws and induces systematic skill un-learning.
10	Further theoretical work has characterized error compounding across iterations~\citep{Fu2024_icml}, established safety thresholds for synthetic data fractions under statistical models~\citep{Seddik2024}, and revealed a generalization-to-memorization transition driven by data entropy~\citep{Shi2025_neurips}.
11	\citet{Schaeffer2025} catalogued eight distinct collapse definitions across three families, highlighting the need for precise operationalization.
12	
13	Several lines of work study \emph{prevention} rather than detection.
14	\citet{Gerstgrasser2024} showed that data accumulation (rather than replacement) avoids collapse; \citet{Kazdan2024} systematically compared replacement, accumulation, and fixed-compute regimes; and verification-based approaches filter synthetic data to maintain quality~\citep{Feng2025,Yi2025}.
15	\citet{Gillman2024} demonstrated that correction functions can exponentially stabilize self-consuming loops, while \citet{Zibakhsh2025} proposed a truncated cross-entropy loss that increases tolerance to synthetic contamination by $2.3\times$.
16	\citet{Bakshi2026} proved that even diminishing real data weights can prevent collapse in the long run.
17	
18	These works collectively establish \emph{that} collapse occurs and \emph{how} to mitigate it, but they rely on post-hoc evaluation (test loss, distribution divergence) or require prior knowledge of contamination levels.
19	No prior work provides a real-time, training-time monitoring framework that tracks collapse severity as it develops.
20	
21	
22	\subsection{Training Dynamics as Diagnostic Signals}
23	
24	\paragraph{Spectral analysis of neural networks.}
25	Spectral properties of weight matrices have emerged as powerful diagnostics for model quality and training health.
26	\citet{Martin2021} demonstrated that stable rank, spectral norm, and power-law exponents of weight spectra predict model quality without test data, establishing a random matrix theory (RMT) framework for neural network analysis.
27	\citet{Sanyal2020} proved a direct link between stable rank and generalization gap, showing that stable rank normalization improves generalization by up to 11.3\%.
28	More recently, \citet{Xu2026} found stable rank to be the dominant predictor of LLM compression degradation (Pearson $r=0.890$) with informative per-layer variation between attention and MLP modules.
29	On the theoretical side, \citet{Pennington2017} extended RMT to nonlinear settings, deriving asymptotic spectral distributions through network layers.
30	\citet{Yunis2024} used spectral dynamics of weights to distinguish memorizing from generalizing networks, while \citet{AlphaPruning2024} validated per-layer spectral analysis for LLM quality assessment via alpha-exponent-guided pruning.
31	
32	Spectral scaling across model sizes has received increasing attention.
33	\citet{Liehr2025} discovered that FFN soft rank scales near-linearly with width while hard rank grows sub-linearly, implying that stable rank baselines are scale-dependent.
34	\citet{Staats2024} showed via RMT analysis across BERT, Pythia-410M, and Llama-8B that small singular values carry significant information, cautioning against truncated spectral analyses.
35	\citet{Liu2026_lifecycle} documented the full spectral lifecycle of transformer training across three scales (30M--285M), revealing that stable rank compression propagates as a traveling wave from shallow to deep layers with Q/K and V/O asymmetries.
36	
37	\paragraph{Training dynamics for data and training quality.}
38	Beyond weight spectra, training-time signals have been used to diagnose data quality and training health.
39	\citet{Li2025_gradient} showed that layer-wise gradient SVD effective rank and nuclear norm unify multiple data quality metrics, with higher effective rank indicating higher data quality.
40	\citet{Elgaar2026} used gradient noise scale and singular entropy of the output head as LLM training diagnostics in curriculum learning.
41	\citet{Chen2024_dse} proposed diffusion spectral entropy (DSE) to track training dynamics, observing that information-theoretic measures stagnate at overfitting onset.
42	\citet{Qiu2025} introduced spectral alignment between layer inputs and weight principal singular vectors as an early predictor of loss explosion, detecting pathologies before gradient norms diverge.
43	\citet{Kalra2026} proposed critical sharpness as a lightweight loss landscape curvature measure validated at 7B scale.
44	
45	\paragraph{Closest competitors.}
46	Two concurrent works most directly relate to ours.
47	\textbf{SIGMA}~\citep{Gu2026} analyzes the Gram matrix spectrum of output embeddings to quantify collapse, deriving spectral contraction bounds.
48	However, SIGMA operates as a post-hoc, black-box diagnostic: it requires a clean reference distribution, does not perform per-layer analysis, does not track within-generation training dynamics, and has not been validated in the iterative synthetic data setting.
49	\textbf{Kalinowski}~\citep{Kalinowski2026} proposes an online topological monitor based on persistent homology with sparse incremental updates.
50	While this shares our goal of real-time monitoring, it uses a fundamentally different signal family (topological rather than spectral/entropic), incurs higher computational cost, and has not been evaluated on iterative synthetic data collapse.
51	Table~\ref{tab:competitor_comparison} summarizes the key differences.
52	
53	Neither approach provides a systematic comparison of multiple signal families, documents where signals saturate or mislead, or establishes quantitative early warning thresholds for iterative collapse.
54	
55	
56	\subsection{Data Quality and Contamination Detection}
57	
58	A parallel line of work addresses detection of synthetic data in training corpora.
59	Watermarking approaches embed identifiable patterns in generated text: \citet{Kirchenbauer2023} introduced green/red token list watermarking with statistical detection, while \citet{Dathathri2024} scaled watermarking to production (SynthID-Text, validated on ${\sim}$20M Gemini responses) and \citet{Sander2024} showed that watermark residuals can detect whether a model was trained on watermarked synthetic data.
60	Statistical detection methods identify machine-generated text without explicit watermarks: \citet{Mitchell2023} exploited log-probability curvature for zero-shot detection (DetectGPT), and \citet{Shi2024_mink} proposed Min-K\% Prob for membership inference in pretraining data.
61	At the dataset level, \citet{Penedo2024} documented quality filtering strategies for 15T-token web corpora, and \citet{Zhang2026} proposed a unified quality-trustworthiness evaluation taxonomy for synthetic data.
62	\citet{Wyss2024} introduced surplexity to quantify diversity loss from synthetic contamination at various mixture fractions, providing an output-level post-hoc analysis.
63	\citet{Wang2025_scaling} discovered three-phase scaling behavior and tail truncation effects in real-synthetic data mixtures for LLM training.
64	
65	These methods answer whether synthetic data is \emph{present}; our work addresses how severely it has \emph{degraded} the model.
66	Detection is inherently post-hoc---applied to static datasets or finished models---while our monitoring operates in real time during training.
67	Moreover, detection methods do not quantify collapse severity or provide actionable stopping criteria.
68	
69	
70	\subsection{Positioning of This Work}
71	
72	Across 49 surveyed papers spanning collapse theory, spectral analysis, training dynamics, and data quality, no prior work simultaneously achieves: (a) online monitoring during training, (b) spectral and entropic training-dynamic signals, (c) per-layer granularity, and (d) validation in the iterative synthetic data setting.
73	We bridge the gap between collapse theory---which establishes \emph{that} degradation occurs---and practitioner needs for \emph{when} and \emph{how severely} it manifests.
74	Our signal taxonomy characterizes the operating ranges where each signal family succeeds, saturates, or misleads, providing actionable guidance absent from prior work.
75	The early warning capability (detecting collapse at 3\% training progress) addresses the absence of training-time stopping criteria identified in our literature survey.
76	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7842b6cf-92a1-41f5-a811-857eea741845",
  "isSidechain": false,
  "promptId": "a7003b6e-3a25-4888-837a-59f1925bbd90",
  "type": "user",
  "uuid": "9703c432-2850-4c4c-8b72-e116a70a5262",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\subsection{Model Collapse in Iterative Training}\n\nThe phenomenon of model collapse---progressive degradation when models are iteratively trained on their own outputs---has been established across multiple generative families.\n\\citet{Shumailov2024} provided the first systematic demonstration that iterative training on synthetic data causes distribution tails to vanish, leading to irreversible quality loss in LLMs, VAEs, and GMMs.\n\\citet{Alemohammad2024} formalized three self-consuming loop variants (fully synthetic, synthetic augmentation, and fresh data mixing), proving that without fresh real data, either precision or recall must degrade.\nTheoretical analyses have since strengthened these findings: \\citet{Dohmatob2025} proved via operator-valued free probability theory that even a $1/1000$ synthetic data fraction induces collapse and that larger models amplify the effect, while \\citet{Dohmatob2024_tails} showed collapse alters scaling laws and induces systematic skill un-learning.\nFurther theoretical work has characterized error compounding across iterations~\\citep{Fu2024_icml}, established safety thresholds for synthetic data fractions under statistical models~\\citep{Seddik2024}, and revealed a generalization-to-memorization transition driven by data entropy~\\citep{Shi2025_neurips}.\n\\citet{Schaeffer2025} catalogued eight distinct collapse definitions across three families, highlighting the need for precise operationalization.\n\nSeveral lines of work study \\emph{prevention} rather than detection.\n\\citet{Gerstgrasser2024} showed that data accumulation (rather than replacement) avoids collapse; \\citet{Kazdan2024} systematically compared replacement, accumulation, and fixed-compute regimes; and verification-based approaches filter synthetic data to maintain quality~\\citep{Feng2025,Yi2025}.\n\\citet{Gillman2024} demonstrated that correction functions can exponentially stabilize self-consuming loops, while \\citet{Zibakhsh2025} proposed a truncated cross-entropy loss that increases tolerance to synthetic contamination by $2.3\\times$.\n\\citet{Bakshi2026} proved that even diminishing real data weights can prevent collapse in the long run.\n\nThese works collectively establish \\emph{that} collapse occurs and \\emph{how} to mitigate it, but they rely on post-hoc evaluation (test loss, distribution divergence) or require prior knowledge of contamination levels.\nNo prior work provides a real-time, training-time monitoring framework that tracks collapse severity as it develops.\n\n\n\\subsection{Training Dynamics as Diagnostic Signals}\n\n\\paragraph{Spectral analysis of neural networks.}\nSpectral properties of weight matrices have emerged as powerful diagnostics for model quality and training health.\n\\citet{Martin2021} demonstrated that stable rank, spectral norm, and power-law exponents of weight spectra predict model quality without test data, establishing a random matrix theory (RMT) framework for neural network analysis.\n\\citet{Sanyal2020} proved a direct link between stable rank and generalization gap, showing that stable rank normalization improves generalization by up to 11.3\\%.\nMore recently, \\citet{Xu2026} found stable rank to be the dominant predictor of LLM compression degradation (Pearson $r=0.890$) with informative per-layer variation between attention and MLP modules.\nOn the theoretical side, \\citet{Pennington2017} extended RMT to nonlinear settings, deriving asymptotic spectral distributions through network layers.\n\\citet{Yunis2024} used spectral dynamics of weights to distinguish memorizing from generalizing networks, while \\citet{AlphaPruning2024} validated per-layer spectral analysis for LLM quality assessment via alpha-exponent-guided pruning.\n\nSpectral scaling across model sizes has received increasing attention.\n\\citet{Liehr2025} discovered that FFN soft rank scales near-linearly with width while hard rank grows sub-linearly, implying that stable rank baselines are scale-dependent.\n\\citet{Staats2024} showed via RMT analysis across BERT, Pythia-410M, and Llama-8B that small singular values carry significant information, cautioning against truncated spectral analyses.\n\\citet{Liu2026_lifecycle} documented the full spectral lifecycle of transformer training across three scales (30M--285M), revealing that stable rank compression propagates as a traveling wave from shallow to deep layers with Q/K and V/O asymmetries.\n\n\\paragraph{Training dynamics for data and training quality.}\nBeyond weight spectra, training-time signals have been used to diagnose data quality and training health.\n\\citet{Li2025_gradient} showed that layer-wise gradient SVD effective rank and nuclear norm unify multiple data quality metrics, with higher effective rank indicating higher data quality.\n\\citet{Elgaar2026} used gradient noise scale and singular entropy of the output head as LLM training diagnostics in curriculum learning.\n\\citet{Chen2024_dse} proposed diffusion spectral entropy (DSE) to track training dynamics, observing that information-theoretic measures stagnate at overfitting onset.\n\\citet{Qiu2025} introduced spectral alignment between layer inputs and weight principal singular vectors as an early predictor of loss explosion, detecting pathologies before gradient norms diverge.\n\\citet{Kalra2026} proposed critical sharpness as a lightweight loss landscape curvature measure validated at 7B scale.\n\n\\paragraph{Closest competitors.}\nTwo concurrent works most directly relate to ours.\n\\textbf{SIGMA}~\\citep{Gu2026} analyzes the Gram matrix spectrum of output embeddings to quantify collapse, deriving spectral contraction bounds.\nHowever, SIGMA operates as a post-hoc, black-box diagnostic: it requires a clean reference distribution, does not perform per-layer analysis, does not track within-generation training dynamics, and has not been validated in the iterative synthetic data setting.\n\\textbf{Kalinowski}~\\citep{Kalinowski2026} proposes an online topological monitor based on persistent homology with sparse incremental updates.\nWhile this shares our goal of real-time monitoring, it uses a fundamentally different signal family (topological rather than spectral/entropic), incurs higher computational cost, and has not been evaluated on iterative synthetic data collapse.\nTable~\\ref{tab:competitor_comparison} summarizes the key differences.\n\nNeither approach provides a systematic comparison of multiple signal families, documents where signals saturate or mislead, or establishes quantitative early warning thresholds for iterative collapse.\n\n\n\\subsection{Data Quality and Contamination Detection}\n\nA parallel line of work addresses detection of synthetic data in training corpora.\nWatermarking approaches embed identifiable patterns in generated text: \\citet{Kirchenbauer2023} introduced green/red token list watermarking with statistical detection, while \\citet{Dathathri2024} scaled watermarking to production (SynthID-Text, validated on ${\\sim}$20M Gemini responses) and \\citet{Sander2024} showed that watermark residuals can detect whether a model was trained on watermarked synthetic data.\nStatistical detection methods identify machine-generated text without explicit watermarks: \\citet{Mitchell2023} exploited log-probability curvature for zero-shot detection (DetectGPT), and \\citet{Shi2024_mink} proposed Min-K\\% Prob for membership inference in pretraining data.\nAt the dataset level, \\citet{Penedo2024} documented quality filtering strategies for 15T-token web corpora, and \\citet{Zhang2026} proposed a unified quality-trustworthiness evaluation taxonomy for synthetic data.\n\\citet{Wyss2024} introduced surplexity to quantify diversity loss from synthetic contamination at various mixture fractions, providing an output-level post-hoc analysis.\n\\citet{Wang2025_scaling} discovered three-phase scaling behavior and tail truncation effects in real-synthetic data mixtures for LLM training.\n\nThese methods answer whether synthetic data is \\emph{present}; our work addresses how severely it has \\emph{degraded} the model.\nDetection is inherently post-hoc---applied to static datasets or finished models---while our monitoring operates in real time during training.\nMoreover, detection methods do not quantify collapse severity or provide actionable stopping criteria.\n\n\n\\subsection{Positioning of This Work}\n\nAcross 49 surveyed papers spanning collapse theory, spectral analysis, training dynamics, and data quality, no prior work simultaneously achieves: (a) online monitoring during training, (b) spectral and entropic training-dynamic signals, (c) per-layer granularity, and (d) validation in the iterative synthetic data setting.\nWe bridge the gap between collapse theory---which establishes \\emph{that} degradation occurs---and practitioner needs for \\emph{when} and \\emph{how severely} it manifests.\nOur signal taxonomy characterizes the operating ranges where each signal family succeeds, saturates, or misleads, providing actionable guidance absent from prior work.\nThe early warning capability (detecting collapse at 3\\% training progress) addresses the absence of training-time stopping criteria identified in our literature survey.\n",
      "numLines": 76,
      "startLine": 1,
      "totalLines": 76
    }
  },
  "sourceToolAssistantUUID": "7842b6cf-92a1-41f5-a811-857eea741845",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-15T02:10:39.348Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Qy4v4oU3fHnHJYvLXMn5Ae`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9703c432-2850-4c4c-8b72-e116a70a5262",
  "isSidechain": false,
  "requestId": "req_011Cb3YQRuhpkkZTmW9t91hz",
  "type": "assistant",
  "uuid": "120beef4-0d53-4621-bf74-db5cb6eeaae1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q97HJeMTuKyisgq8AC2ect",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 415,
      "cache_read_input_tokens": 23272,
      "output_tokens": 371,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 415,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 371,
          "cache_read_input_tokens": 23272,
          "cache_creation_input_tokens": 415,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 415
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

_source line 23 · 2026-05-15T02:10:39.355Z_

<details><summary>↩ Tool result · `toolu_01Qy4v4oU3fHnHJYvLXMn5Ae`</summary>

```text
1	% Method section — collapse_severity_monitor
2	% Sources: MVP (mvp_frac50_100, within_gen_analysis, per_layer_analysis_v5)
3	% Pending: plan_001 (1.5B scale, 6 fractions, 5 seeds)
4	
5	\section{Methodology}
6	\label{sec:method}
7	
8	We design a controlled experimental framework to evaluate how training dynamic signals track model collapse severity under iterative synthetic data contamination.
9	Our protocol varies contamination level and generational depth while monitoring four families of training-time signals.
10	
11	\subsection{Iterative Synthetic Data Protocol}
12	\label{sec:protocol}
13	
14	We simulate iterative model collapse through a multi-generation fine-tuning loop.
15	Let $M_0$ denote a pretrained base model and $\mathcal{D}_\text{real}$ a real-text corpus.
16	At each generation $g \in \{0, 1, \ldots, G{-}1\}$ (with $G=5$), we execute the following steps:
17	
18	\begin{enumerate}
19	    \item \textbf{Fine-tune.} Initialize from $M_0$ with a QLoRA adapter and fine-tune on the current training corpus $\mathcal{D}_g$, yielding adapted model $\tilde{M}_g$.
20	    During training, we collect monitoring signals every 50 optimizer steps via a callback (Section~\ref{sec:signals}).
21	    \item \textbf{Generate.} Sample synthetic text $\mathcal{S}_g$ from $\tilde{M}_g$ by prompting with the first 32 tokens of randomly subsampled chunks from $\mathcal{D}_\text{real}$ and generating up to 480 new tokens with nucleus sampling ($p=0.95$, temperature $\tau=1.0$).
22	    We subsample 1{,}500 of $|\mathcal{D}_\text{real}|$ chunks for generation to keep wall-clock time tractable.
23	    \item \textbf{Mix.} Construct the next-generation corpus $\mathcal{D}_{g+1}$ by replacing a fraction $\alpha \in \{0, 0.1, 0.25, 0.5, 0.75, 1.0\}$ of real chunks with synthetic chunks from $\mathcal{S}_g$:
24	    \begin{equation}
25	        \mathcal{D}_{g+1} = (1 - \alpha)\,\mathcal{D}_\text{real} \cup \alpha\,\mathcal{S}_g.
26	        \label{eq:mixing}
27	    \end{equation}
28	    The $\alpha=0$ condition serves as a no-contamination baseline.
29	\end{enumerate}
30	
31	\noindent
32	Each generation thus starts from the \emph{same} pretrained weights $M_0$, isolating the effect of data contamination from cumulative weight drift.
33	The collapse pressure enters solely through the training corpus: at generation $g$, the synthetic component was produced by a model trained on data that itself contained synthetic text from generation $g{-}1$.
34	
35	\paragraph{Models.}
36	We use Qwen2.5-0.5B as our primary model (24 transformer layers, 494M parameters).%
37	\footnote{Scale validation on Qwen2.5-1.5B (28 layers, 1.5B parameters) is in progress; preliminary results will be included in the final version.}
38	All experiments use QLoRA~\citep{dettmers2023qlora} with rank $r=16$, scaling factor $\alpha_\text{LoRA}=32$, and dropout $0.05$.
39	Adapters are applied to all linear projections in each transformer layer: \texttt{q\_proj}, \texttt{k\_proj}, \texttt{v\_proj}, \texttt{o\_proj}, \texttt{up\_proj}, \texttt{down\_proj}, and \texttt{gate\_proj}.
40	The base model is quantized to 4-bit NormalFloat (NF4) with double quantization.
41	
42	\paragraph{Data.}
43	We use WikiText-2 (\texttt{wikitext-2-raw-v1})~\citep{merity2017pointer}, tokenized and chunked into fixed-length sequences of 512 tokens, yielding 4{,}916 training chunks and a held-out validation set.%
44	\footnote{Cross-domain validation on PubMed abstracts is planned as a secondary axis.}
45	
46	\paragraph{Training configuration.}
47	All fine-tuning runs use the AdamW optimizer with learning rate $2 \times 10^{-4}$, weight decay $0.01$, linear warmup over $5\%$ of steps, and gradient clipping at $\|\cdot\|_2 \leq 1.0$.
48	We train for 5 epochs with per-device batch size 4 and gradient accumulation over 4 steps (effective batch size 16), using \texttt{bf16} mixed precision.
49	Each generation comprises approximately 1{,}540 optimizer steps.
50	
51	\paragraph{Contamination fractions.}
52	Our MVP experiments use three fractions ($\alpha \in \{0, 0.5, 1.0\}$) with a single seed.
53	The full experimental design extends to six fractions ($\alpha \in \{0, 0.1, 0.25, 0.5, 0.75, 1.0\}$) with 5 independent seeds per configuration, yielding 150 fine-tuning runs (6~fractions $\times$ 5~generations $\times$ 5~seeds).%
54	\footnote{MVP results (3 fractions, seed 42) are reported here; full 6-fraction $\times$ 5-seed results pending \texttt{plan\_001}.}
55	
56	\subsection{Signal Families}
57	\label{sec:signals}
58	
59	We monitor four families of training-time signals, collected every 50 optimizer steps via a training callback.
60	All signals are computed on a held-out validation set in evaluation mode.
61	
62	\subsubsection{Spectral Signals}
63	\label{sec:spectral}
64	
65	Spectral signals characterize the geometry of the model's internal representations.
66	Given a set of $n$ validation sequences, we collect the last-layer hidden states into a matrix $\mathbf{H} \in \mathbb{R}^{T \times d}$, where $T$ is the total number of tokens across $n$ sequences and $d$ is the hidden dimension.
67	We center $\mathbf{H}$ by subtracting its column mean, then compute the sample covariance:
68	\begin{equation}
69	    \mathbf{C} = \frac{1}{T-1}\,\mathbf{H}^\top \mathbf{H} \in \mathbb{R}^{d \times d}.
70	\end{equation}
71	Let $\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_d \geq 0$ denote the eigenvalues of $\mathbf{C}$ (equivalently, its singular values, since $\mathbf{C}$ is positive semidefinite).
72	
73	\paragraph{Stable rank.}
74	The participation ratio of the eigenspectrum measures the effective dimensionality of the representation:
75	\begin{equation}
76	    \mathrm{SR}(\mathbf{C}) = \frac{\left(\sum_{i=1}^{d} \lambda_i\right)^2}{\sum_{i=1}^{d} \lambda_i^2}.
77	    \label{eq:stable_rank}
78	\end{equation}
79	$\mathrm{SR} = 1$ when all variance concentrates on a single component; $\mathrm{SR} = d$ when variance is uniformly distributed.
80	Under model collapse, we observe that $\mathrm{SR}$ \emph{increases}: the Frobenius norm of the representation grows faster than its leading eigenvalue, dispersing energy across more dimensions rather than concentrating it.%
81	\footnote{This is the participation ratio of the covariance eigenspectrum, closely related to but distinct from the matrix stable rank $\|\mathbf{H}\|_F^2 / \|\mathbf{H}\|_2^2$; the two are monotonically related for centered data.}
82	
83	\paragraph{Spectral entropy.}
84	The normalized entropy of the eigenspectrum provides a complementary measure of spectral concentration:
85	\begin{equation}
86	    \mathrm{SE}(\mathbf{C}) = \frac{-\sum_{i=1}^{d} p_i \log p_i}{\log d}, \quad \text{where } p_i = \frac{\lambda_i}{\sum_{j=1}^{d} \lambda_j}.
87	    \label{eq:spectral_entropy}
88	\end{equation}
89	$\mathrm{SE} \in [0, 1]$, with $\mathrm{SE} = 1$ indicating a uniform spectrum and $\mathrm{SE} \to 0$ indicating concentration on few components.
90	We use $n=64$ validation chunks for SVD computation, retaining the top-5 singular values for trajectory logging.
91	
92	\subsubsection{Output Signals}
93	\label{sec:output}
94	
95	Output signals measure the model's predictive behavior on held-out real text.
96	
97	\paragraph{Token entropy.}
98	For each validation sequence $\mathbf{x} = (x_1, \ldots, x_L)$, we compute the mean per-position entropy of the next-token distribution:
99	\begin{equation}
100	    \mathrm{TE}(\mathbf{x}) = \frac{1}{L-1} \sum_{t=1}^{L-1} H\!\left(P_\theta(\cdot \mid x_{\leq t})\right), \quad H(P) = -\sum_{v} P(v) \log P(v),
101	    \label{eq:token_entropy}
102	\end{equation}
103	and report the average over 100 validation chunks.
104	Decreasing token entropy indicates the model is becoming more ``peaked'' in its predictions---a hallmark of mode collapse in generation.
105	
106	\paragraph{Perplexity.}
107	We compute perplexity as the exponentiated mean per-token negative log-likelihood over the full validation set:
108	\begin{equation}
109	    \mathrm{PPL} = \exp\!\left(\frac{1}{N}\sum_{i=1}^{|\mathcal{V}|} \ell(\mathbf{x}_i)\right),
110	    \label{eq:perplexity}
111	\end{equation}
112	where $\ell(\mathbf{x}_i)$ is the cross-entropy loss on validation sequence $\mathbf{x}_i$ and $N$ is the total token count.
113	Perplexity captures degradation in language modeling quality; under severe collapse, it increases by orders of magnitude (e.g., $15.7 \to 839.2$ over 5 generations at $\alpha=1.0$ in our MVP; source: \texttt{mvp\_frac50\_100}).
114	
115	\subsubsection{Gradient Signal}
116	\label{sec:gradient}
117	
118	We log the L2 gradient norm $\|\nabla_\theta \mathcal{L}\|_2$ computed by the trainer before each optimizer step.
119	Gradient norm is a zero-cost byproduct of standard training and reflects optimization landscape curvature.
120	In our MVP experiments, gradient norm exhibits non-monotonic behavior with respect to contamination fraction under QLoRA, limiting its utility as a standalone severity monitor (Section~\ref{sec:results}).
121	
122	\subsubsection{Downstream Signal}
123	\label{sec:downstream}
124	
125	We evaluate HellaSwag~\citep{zellers2019hellaswag} accuracy (4-choice commonsense reasoning, 1{,}000 samples) as a downstream task probe.
126	HellaSwag is computed at the end of each generation (not at every signal checkpoint, due to evaluation cost).
127	At the 0.5B scale, HellaSwag shows minimal sensitivity to collapse: accuracy drops only 1.2\% (0.435 $\to$ 0.430) despite catastrophic perplexity explosion, suggesting that small-model benchmark performance is a poor proxy for generative collapse severity (source: \texttt{mvp\_frac50\_100}).
128	
129	\subsection{Evaluation Methodology}
130	\label{sec:evaluation}
131	
132	\subsubsection{Cross-Fraction Severity Correlation}
133	\label{sec:cross_fraction}
134	
135	For each signal $s$ and generation $g$, we compute the Spearman rank correlation $\rho_g^{(s)}$ between contamination fraction $\alpha$ and the end-of-generation signal value across all tested fractions.
136	We report the mean absolute correlation $\bar{|\rho|}^{(s)} = \frac{1}{G}\sum_{g=0}^{G-1} |\rho_g^{(s)}|$ as a summary statistic.
137	A signal is considered a reliable severity monitor if $\bar{|\rho|}^{(s)} > 0.7$.
138	
139	In the MVP (3 fractions, $n=1$ seed), all spectral and output signals achieve $|\rho| = 1.0$ per generation, reflecting perfect monotonic ordering over the three tested severity levels (source: \texttt{mvp\_frac50\_100}).
140	We note that $|\rho| = 1.0$ with $n=3$ fractions is a necessary but weak condition; the 6-fraction design (pending \texttt{plan\_001}) provides a more stringent test of monotonicity.
141	
142	\subsubsection{Cross-Generation Tracking}
143	\label{sec:cross_gen}
144	
145	For each signal $s$ and contamination fraction $\alpha$, we compute the Spearman correlation between generation index $g$ and end-of-generation signal value.
146	This measures whether signals track the \emph{accumulation} of collapse across iterative retraining.
147	At $\alpha=1.0$, perplexity exhibits super-linear growth across generations ($15.7 \to 136.9 \to 394.3 \to 691.4 \to 839.2$), consistent with the accelerating degradation predicted by model collapse theory~\citep{shumailov2024ai} (source: \texttt{mvp\_frac50\_100}).
148	
149	\subsubsection{Within-Generation Early Warning}
150	\label{sec:early_warning}
151	
152	We assess how early within a single training run each signal can distinguish a contaminated condition from the clean baseline.
153	Specifically, we compute the relative deviation at each signal checkpoint:
154	\begin{equation}
155	    \Delta_s(t, \alpha) = \frac{|s_\alpha(t) - s_0(t)|}{|s_0(t)|} \times 100\%,
156	    \label{eq:deviation}
157	\end{equation}
158	where $s_\alpha(t)$ and $s_0(t)$ are the signal values at step $t$ for fraction $\alpha$ and the clean baseline ($\alpha=0$), respectively.
159	A signal provides \emph{early warning} if $\Delta_s(t, \alpha) > 5\%$ within the first 10\% of training steps.
160	
161	In the MVP, stable rank achieves the largest early deviation: $\Delta_\mathrm{SR}(50, 1.0) = 34.4\%$ at step 50 (${\sim}3\%$ training progress), followed by token entropy at 24.5\% and perplexity at 17.7\%.
162	Spectral entropy (5.0\%) and gradient norm (2.1\%) respond more slowly, first exceeding 5\% at step 100 (${\sim}6\%$ progress) (source: \texttt{within\_gen\_analysis}).
163	
164	\subsubsection{Statistical Validity}
165	\label{sec:stats}
166	
167	\paragraph{Bootstrap confidence intervals.}
168	For the full experimental design (6 fractions $\times$ 5 seeds), we compute 95\% bootstrap confidence intervals for all reported correlations and effect sizes.
169	Crucially, we use \emph{clustered bootstrap} with the cluster unit being fraction $\times$ seed, rather than pooling individual generation observations.
170	Pooling would inflate sample size and produce artificially narrow intervals, because successive generations within a run are causally dependent---generation $g+1$ trains on data produced by the model from generation $g$.
171	
172	\paragraph{AUROC for collapse detection.}
173	We compute the area under the receiver operating characteristic curve (AUROC) for binary collapse detection at various severity thresholds (e.g., $\alpha \geq 0.5$ vs.\ $\alpha < 0.5$).
174	In the MVP (3 fractions, single seed), stable rank, spectral entropy, and token entropy each achieve AUROC $= 1.0$ for distinguishing the $\alpha = 1.0$ condition at step 50.
175	We treat AUROC as a secondary metric supporting the primary evidence from effect sizes and rank correlations, given the small sample size in the MVP (source: \texttt{within\_gen\_analysis}).
176	
177	\paragraph{Effect sizes.}
178	We prioritize absolute and relative effect sizes (e.g., 6.6$\times$ stable rank separation between $\alpha=0$ and $\alpha=1.0$ at generation 4) as primary evidence, with rank correlations as supporting statistics.
179	This hierarchy follows from the observation that $|\rho| = 1.0$ is easily achieved with few fractions and does not convey the \emph{magnitude} of signal separation (source: \texttt{mvp\_frac50\_100}).
180	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "120beef4-0d53-4621-bf74-db5cb6eeaae1",
  "isSidechain": false,
  "promptId": "a7003b6e-3a25-4888-837a-59f1925bbd90",
  "type": "user",
  "uuid": "144f7820-b8d9-4240-9be0-0e0725e1b69d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/method.tex",
      "content": "% Method section — collapse_severity_monitor\n% Sources: MVP (mvp_frac50_100, within_gen_analysis, per_layer_analysis_v5)\n% Pending: plan_001 (1.5B scale, 6 fractions, 5 seeds)\n\n\\section{Methodology}\n\\label{sec:method}\n\nWe design a controlled experimental framework to evaluate how training dynamic signals track model collapse severity under iterative synthetic data contamination.\nOur protocol varies contamination level and generational depth while monitoring four families of training-time signals.\n\n\\subsection{Iterative Synthetic Data Protocol}\n\\label{sec:protocol}\n\nWe simulate iterative model collapse through a multi-generation fine-tuning loop.\nLet $M_0$ denote a pretrained base model and $\\mathcal{D}_\\text{real}$ a real-text corpus.\nAt each generation $g \\in \\{0, 1, \\ldots, G{-}1\\}$ (with $G=5$), we execute the following steps:\n\n\\begin{enumerate}\n    \\item \\textbf{Fine-tune.} Initialize from $M_0$ with a QLoRA adapter and fine-tune on the current training corpus $\\mathcal{D}_g$, yielding adapted model $\\tilde{M}_g$.\n    During training, we collect monitoring signals every 50 optimizer steps via a callback (Section~\\ref{sec:signals}).\n    \\item \\textbf{Generate.} Sample synthetic text $\\mathcal{S}_g$ from $\\tilde{M}_g$ by prompting with the first 32 tokens of randomly subsampled chunks from $\\mathcal{D}_\\text{real}$ and generating up to 480 new tokens with nucleus sampling ($p=0.95$, temperature $\\tau=1.0$).\n    We subsample 1{,}500 of $|\\mathcal{D}_\\text{real}|$ chunks for generation to keep wall-clock time tractable.\n    \\item \\textbf{Mix.} Construct the next-generation corpus $\\mathcal{D}_{g+1}$ by replacing a fraction $\\alpha \\in \\{0, 0.1, 0.25, 0.5, 0.75, 1.0\\}$ of real chunks with synthetic chunks from $\\mathcal{S}_g$:\n    \\begin{equation}\n        \\mathcal{D}_{g+1} = (1 - \\alpha)\\,\\mathcal{D}_\\text{real} \\cup \\alpha\\,\\mathcal{S}_g.\n        \\label{eq:mixing}\n    \\end{equation}\n    The $\\alpha=0$ condition serves as a no-contamination baseline.\n\\end{enumerate}\n\n\\noindent\nEach generation thus starts from the \\emph{same} pretrained weights $M_0$, isolating the effect of data contamination from cumulative weight drift.\nThe collapse pressure enters solely through the training corpus: at generation $g$, the synthetic component was produced by a model trained on data that itself contained synthetic text from generation $g{-}1$.\n\n\\paragraph{Models.}\nWe use Qwen2.5-0.5B as our primary model (24 transformer layers, 494M parameters).%\n\\footnote{Scale validation on Qwen2.5-1.5B (28 layers, 1.5B parameters) is in progress; preliminary results will be included in the final version.}\nAll experiments use QLoRA~\\citep{dettmers2023qlora} with rank $r=16$, scaling factor $\\alpha_\\text{LoRA}=32$, and dropout $0.05$.\nAdapters are applied to all linear projections in each transformer layer: \\texttt{q\\_proj}, \\texttt{k\\_proj}, \\texttt{v\\_proj}, \\texttt{o\\_proj}, \\texttt{up\\_proj}, \\texttt{down\\_proj}, and \\texttt{gate\\_proj}.\nThe base model is quantized to 4-bit NormalFloat (NF4) with double quantization.\n\n\\paragraph{Data.}\nWe use WikiText-2 (\\texttt{wikitext-2-raw-v1})~\\citep{merity2017pointer}, tokenized and chunked into fixed-length sequences of 512 tokens, yielding 4{,}916 training chunks and a held-out validation set.%\n\\footnote{Cross-domain validation on PubMed abstracts is planned as a secondary axis.}\n\n\\paragraph{Training configuration.}\nAll fine-tuning runs use the AdamW optimizer with learning rate $2 \\times 10^{-4}$, weight decay $0.01$, linear warmup over $5\\%$ of steps, and gradient clipping at $\\|\\cdot\\|_2 \\leq 1.0$.\nWe train for 5 epochs with per-device batch size 4 and gradient accumulation over 4 steps (effective batch size 16), using \\texttt{bf16} mixed precision.\nEach generation comprises approximately 1{,}540 optimizer steps.\n\n\\paragraph{Contamination fractions.}\nOur MVP experiments use three fractions ($\\alpha \\in \\{0, 0.5, 1.0\\}$) with a single seed.\nThe full experimental design extends to six fractions ($\\alpha \\in \\{0, 0.1, 0.25, 0.5, 0.75, 1.0\\}$) with 5 independent seeds per configuration, yielding 150 fine-tuning runs (6~fractions $\\times$ 5~generations $\\times$ 5~seeds).%\n\\footnote{MVP results (3 fractions, seed 42) are reported here; full 6-fraction $\\times$ 5-seed results pending \\texttt{plan\\_001}.}\n\n\\subsection{Signal Families}\n\\label{sec:signals}\n\nWe monitor four families of training-time signals, collected every 50 optimizer steps via a training callback.\nAll signals are computed on a held-out validation set in evaluation mode.\n\n\\subsubsection{Spectral Signals}\n\\label{sec:spectral}\n\nSpectral signals characterize the geometry of the model's internal representations.\nGiven a set of $n$ validation sequences, we collect the last-layer hidden states into a matrix $\\mathbf{H} \\in \\mathbb{R}^{T \\times d}$, where $T$ is the total number of tokens across $n$ sequences and $d$ is the hidden dimension.\nWe center $\\mathbf{H}$ by subtracting its column mean, then compute the sample covariance:\n\\begin{equation}\n    \\mathbf{C} = \\frac{1}{T-1}\\,\\mathbf{H}^\\top \\mathbf{H} \\in \\mathbb{R}^{d \\times d}.\n\\end{equation}\nLet $\\lambda_1 \\geq \\lambda_2 \\geq \\cdots \\geq \\lambda_d \\geq 0$ denote the eigenvalues of $\\mathbf{C}$ (equivalently, its singular values, since $\\mathbf{C}$ is positive semidefinite).\n\n\\paragraph{Stable rank.}\nThe participation ratio of the eigenspectrum measures the effective dimensionality of the representation:\n\\begin{equation}\n    \\mathrm{SR}(\\mathbf{C}) = \\frac{\\left(\\sum_{i=1}^{d} \\lambda_i\\right)^2}{\\sum_{i=1}^{d} \\lambda_i^2}.\n    \\label{eq:stable_rank}\n\\end{equation}\n$\\mathrm{SR} = 1$ when all variance concentrates on a single component; $\\mathrm{SR} = d$ when variance is uniformly distributed.\nUnder model collapse, we observe that $\\mathrm{SR}$ \\emph{increases}: the Frobenius norm of the representation grows faster than its leading eigenvalue, dispersing energy across more dimensions rather than concentrating it.%\n\\footnote{This is the participation ratio of the covariance eigenspectrum, closely related to but distinct from the matrix stable rank $\\|\\mathbf{H}\\|_F^2 / \\|\\mathbf{H}\\|_2^2$; the two are monotonically related for centered data.}\n\n\\paragraph{Spectral entropy.}\nThe normalized entropy of the eigenspectrum provides a complementary measure of spectral concentration:\n\\begin{equation}\n    \\mathrm{SE}(\\mathbf{C}) = \\frac{-\\sum_{i=1}^{d} p_i \\log p_i}{\\log d}, \\quad \\text{where } p_i = \\frac{\\lambda_i}{\\sum_{j=1}^{d} \\lambda_j}.\n    \\label{eq:spectral_entropy}\n\\end{equation}\n$\\mathrm{SE} \\in [0, 1]$, with $\\mathrm{SE} = 1$ indicating a uniform spectrum and $\\mathrm{SE} \\to 0$ indicating concentration on few components.\nWe use $n=64$ validation chunks for SVD computation, retaining the top-5 singular values for trajectory logging.\n\n\\subsubsection{Output Signals}\n\\label{sec:output}\n\nOutput signals measure the model's predictive behavior on held-out real text.\n\n\\paragraph{Token entropy.}\nFor each validation sequence $\\mathbf{x} = (x_1, \\ldots, x_L)$, we compute the mean per-position entropy of the next-token distribution:\n\\begin{equation}\n    \\mathrm{TE}(\\mathbf{x}) = \\frac{1}{L-1} \\sum_{t=1}^{L-1} H\\!\\left(P_\\theta(\\cdot \\mid x_{\\leq t})\\right), \\quad H(P) = -\\sum_{v} P(v) \\log P(v),\n    \\label{eq:token_entropy}\n\\end{equation}\nand report the average over 100 validation chunks.\nDecreasing token entropy indicates the model is becoming more ``peaked'' in its predictions---a hallmark of mode collapse in generation.\n\n\\paragraph{Perplexity.}\nWe compute perplexity as the exponentiated mean per-token negative log-likelihood over the full validation set:\n\\begin{equation}\n    \\mathrm{PPL} = \\exp\\!\\left(\\frac{1}{N}\\sum_{i=1}^{|\\mathcal{V}|} \\ell(\\mathbf{x}_i)\\right),\n    \\label{eq:perplexity}\n\\end{equation}\nwhere $\\ell(\\mathbf{x}_i)$ is the cross-entropy loss on validation sequence $\\mathbf{x}_i$ and $N$ is the total token count.\nPerplexity captures degradation in language modeling quality; under severe collapse, it increases by orders of magnitude (e.g., $15.7 \\to 839.2$ over 5 generations at $\\alpha=1.0$ in our MVP; source: \\texttt{mvp\\_frac50\\_100}).\n\n\\subsubsection{Gradient Signal}\n\\label{sec:gradient}\n\nWe log the L2 gradient norm $\\|\\nabla_\\theta \\mathcal{L}\\|_2$ computed by the trainer before each optimizer step.\nGradient norm is a zero-cost byproduct of standard training and reflects optimization landscape curvature.\nIn our MVP experiments, gradient norm exhibits non-monotonic behavior with respect to contamination fraction under QLoRA, limiting its utility as a standalone severity monitor (Section~\\ref{sec:results}).\n\n\\subsubsection{Downstream Signal}\n\\label{sec:downstream}\n\nWe evaluate HellaSwag~\\citep{zellers2019hellaswag} accuracy (4-choice commonsense reasoning, 1{,}000 samples) as a downstream task probe.\nHellaSwag is computed at the end of each generation (not at every signal checkpoint, due to evaluation cost).\nAt the 0.5B scale, HellaSwag shows minimal sensitivity to collapse: accuracy drops only 1.2\\% (0.435 $\\to$ 0.430) despite catastrophic perplexity explosion, suggesting that small-model benchmark performance is a poor proxy for generative collapse severity (source: \\texttt{mvp\\_frac50\\_100}).\n\n\\subsection{Evaluation Methodology}\n\\label{sec:evaluation}\n\n\\subsubsection{Cross-Fraction Severity Correlation}\n\\label{sec:cross_fraction}\n\nFor each signal $s$ and generation $g$, we compute the Spearman rank correlation $\\rho_g^{(s)}$ between contamination fraction $\\alpha$ and the end-of-generation signal value across all tested fractions.\nWe report the mean absolute correlation $\\bar{|\\rho|}^{(s)} = \\frac{1}{G}\\sum_{g=0}^{G-1} |\\rho_g^{(s)}|$ as a summary statistic.\nA signal is considered a reliable severity monitor if $\\bar{|\\rho|}^{(s)} > 0.7$.\n\nIn the MVP (3 fractions, $n=1$ seed), all spectral and output signals achieve $|\\rho| = 1.0$ per generation, reflecting perfect monotonic ordering over the three tested severity levels (source: \\texttt{mvp\\_frac50\\_100}).\nWe note that $|\\rho| = 1.0$ with $n=3$ fractions is a necessary but weak condition; the 6-fraction design (pending \\texttt{plan\\_001}) provides a more stringent test of monotonicity.\n\n\\subsubsection{Cross-Generation Tracking}\n\\label{sec:cross_gen}\n\nFor each signal $s$ and contamination fraction $\\alpha$, we compute the Spearman correlation between generation index $g$ and end-of-generation signal value.\nThis measures whether signals track the \\emph{accumulation} of collapse across iterative retraining.\nAt $\\alpha=1.0$, perplexity exhibits super-linear growth across generations ($15.7 \\to 136.9 \\to 394.3 \\to 691.4 \\to 839.2$), consistent with the accelerating degradation predicted by model collapse theory~\\citep{shumailov2024ai} (source: \\texttt{mvp\\_frac50\\_100}).\n\n\\subsubsection{Within-Generation Early Warning}\n\\label{sec:early_warning}\n\nWe assess how early within a single training run each signal can distinguish a contaminated condition from the clean baseline.\nSpecifically, we compute the relative deviation at each signal checkpoint:\n\\begin{equation}\n    \\Delta_s(t, \\alpha) = \\frac{|s_\\alpha(t) - s_0(t)|}{|s_0(t)|} \\times 100\\%,\n    \\label{eq:deviation}\n\\end{equation}\nwhere $s_\\alpha(t)$ and $s_0(t)$ are the signal values at step $t$ for fraction $\\alpha$ and the clean baseline ($\\alpha=0$), respectively.\nA signal provides \\emph{early warning} if $\\Delta_s(t, \\alpha) > 5\\%$ within the first 10\\% of training steps.\n\nIn the MVP, stable rank achieves the largest early deviation: $\\Delta_\\mathrm{SR}(50, 1.0) = 34.4\\%$ at step 50 (${\\sim}3\\%$ training progress), followed by token entropy at 24.5\\% and perplexity at 17.7\\%.\nSpectral entropy (5.0\\%) and gradient norm (2.1\\%) respond more slowly, first exceeding 5\\% at step 100 (${\\sim}6\\%$ progress) (source: \\texttt{within\\_gen\\_analysis}).\n\n\\subsubsection{Statistical Validity}\n\\label{sec:stats}\n\n\\paragraph{Bootstrap confidence intervals.}\nFor the full experimental design (6 fractions $\\times$ 5 seeds), we compute 95\\% bootstrap confidence intervals for all reported correlations and effect sizes.\nCrucially, we use \\emph{clustered bootstrap} with the cluster unit being fraction $\\times$ seed, rather than pooling individual generation observations.\nPooling would inflate sample size and produce artificially narrow intervals, because successive generations within a run are causally dependent---generation $g+1$ trains on data produced by the model from generation $g$.\n\n\\paragraph{AUROC for collapse detection.}\nWe compute the area under the receiver operating characteristic curve (AUROC) for binary collapse detection at various severity thresholds (e.g., $\\alpha \\geq 0.5$ vs.\\ $\\alpha < 0.5$).\nIn the MVP (3 fractions, single seed), stable rank, spectral entropy, and token entropy each achieve AUROC $= 1.0$ for distinguishing the $\\alpha = 1.0$ condition at step 50.\nWe treat AUROC as a secondary metric supporting the primary evidence from effect sizes and rank correlations, given the small sample size in the MVP (source: \\texttt{within\\_gen\\_analysis}).\n\n\\paragraph{Effect sizes.}\nWe prioritize absolute and relative effect sizes (e.g., 6.6$\\times$ stable rank separation between $\\alpha=0$ and $\\alpha=1.0$ at generation 4) as primary evidence, with rank correlations as supporting statistics.\nThis hierarchy follows from the observation that $|\\rho| = 1.0$ is easily achieved with few fractions and does not convey the \\emph{magnitude} of signal separation (source: \\texttt{mvp\\_frac50\\_100}).\n",
      "numLines": 180,
      "startLine": 1,
      "totalLines": 180
    }
  },
  "sourceToolAssistantUUID": "120beef4-0d53-4621-bf74-db5cb6eeaae1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-15T02:10:39.737Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HjECHPr9daztmtw6YiQfHn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/tables/competitor_comparison.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "144f7820-b8d9-4240-9be0-0e0725e1b69d",
  "isSidechain": false,
  "requestId": "req_011Cb3YQRuhpkkZTmW9t91hz",
  "type": "assistant",
  "uuid": "514460af-7073-4603-8b7a-765915b961c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q97HJeMTuKyisgq8AC2ect",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 415,
      "cache_read_input_tokens": 23272,
      "output_tokens": 371,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 415,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 371,
          "cache_read_input_tokens": 23272,
          "cache_creation_input_tokens": 415,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 415
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
  "leafUuid": "7483eb10-6401-4f0b-9830-6902a523aea2",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Compile bibliography file for paper citations",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b"
}
```

---

### Assistant

_source line 27 · 2026-05-15T02:10:42.396Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me extract all citation keys from these files. Let me also read the literature reference files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7483eb10-6401-4f0b-9830-6902a523aea2",
  "isSidechain": false,
  "requestId": "req_011Cb3YQm6cVssHK4wzC8S3x",
  "type": "assistant",
  "uuid": "4c40db8c-50b8-4c0d-ba5f-ac7b556bacc3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YEas68yHeLep7hMGzfWWuS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10671,
      "cache_read_input_tokens": 23687,
      "output_tokens": 293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10671,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 293,
          "cache_read_input_tokens": 23687,
          "cache_creation_input_tokens": 10671,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10671
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

_source line 28 · 2026-05-15T02:10:42.942Z_

Now let me read the literature reference files and extract all citation keys.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c40db8c-50b8-4c0d-ba5f-ac7b556bacc3",
  "isSidechain": false,
  "requestId": "req_011Cb3YQm6cVssHK4wzC8S3x",
  "type": "assistant",
  "uuid": "90041bf8-436d-41c8-9f94-1af211d336af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YEas68yHeLep7hMGzfWWuS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10671,
      "cache_read_input_tokens": 23687,
      "output_tokens": 293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10671,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 293,
          "cache_read_input_tokens": 23687,
          "cache_creation_input_tokens": 10671,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10671
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

_source line 29 · 2026-05-15T02:10:45.461Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FKLkFhE1fPU2TtiaGzRb7Q`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/_project/report/related_work_notes_45da09.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90041bf8-436d-41c8-9f94-1af211d336af",
  "isSidechain": false,
  "requestId": "req_011Cb3YQm6cVssHK4wzC8S3x",
  "type": "assistant",
  "uuid": "8ff44be2-3e48-4a31-bc5d-31a480762059",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YEas68yHeLep7hMGzfWWuS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10671,
      "cache_read_input_tokens": 23687,
      "output_tokens": 293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10671,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 293,
          "cache_read_input_tokens": 23687,
          "cache_creation_input_tokens": 10671,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10671
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

_source line 30 · 2026-05-15T02:10:47.256Z_

<details><summary>↩ Tool result · `toolu_01WxeeXXwWDivsYZmxTuSs2z`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d97e96bd-66ea-4c75-a1d7-1437bf5d2006",
  "isSidechain": false,
  "promptId": "a7003b6e-3a25-4888-837a-59f1925bbd90",
  "type": "user",
  "uuid": "60b18341-85e3-45ca-a36e-0d58075f9808",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 22
  },
  "sourceToolAssistantUUID": "d97e96bd-66ea-4c75-a1d7-1437bf5d2006",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-15T02:10:45.466Z_

<details><summary>↩ Tool result · `toolu_01FKLkFhE1fPU2TtiaGzRb7Q`</summary>

```text
1	# Related Work Notes — Collapse Severity Monitor
2	
3	**Project**: collapse_severity_monitor | **Target**: NeurIPS 2026
4	**Based on**: literature_map.yaml (37 papers), worker_research_related-work_20260515T005137
5	**Date**: 2026-05-15
6	
7	---
8	
9	## 1. Model Collapse 理论基础
10	
11	核心问题：在合成数据上迭代训练导致模型质量不可逆退化。
12	
13	### 基石论文
14	
15	| 论文 | 作者 | 年份 | Venue | 核心方法/发现 | 与我们的关系 |
16	|------|------|------|-------|--------------|-------------|
17	| AI Models Collapse When Trained on Recursively Generated Data | Shumailov et al. | 2024 | Nature | 首次系统证明迭代合成数据训练→分布尾部消失→model collapse（LLM/VAE/GMM） | **支持**：定义了我们要解决的问题；他们用事后评估（test loss），我们提供在线监控 |
18	| Self-Consuming Generative Models Go MAD | Alemohammad et al. | 2024 | ICLR | 定义三种自噬循环（fully synthetic / augmentation / fresh data），证明无 fresh data 时 precision 或 recall 必降 | **支持**：MAD 框架直接对应我们的实验设计中的迭代合成数据设定 |
19	| Strong Model Collapse | Dohmatob, Feng et al. | 2025 | ICLR (Spotlight) | 算子值自由概率论证明即使 1/1000 合成数据也导致 collapse，更大模型放大 collapse | **支持**：解释了监控的必要性——即使少量合成数据也危险；fraction 实验与我们的 6 级污染实验直接相关 |
20	| A Tale of Tails: Model Collapse as a Change of Scaling Laws | Dohmatob et al. | 2024 | ICML | Collapse 导致 scaling law 改变，skill un-learning 现象 | **支持**：从 scaling law 角度量化 collapse 严重度，提供事后分析视角的对比 |
21	
22	### 理论扩展与实证
23	
24	| 论文 | 作者 | 年份 | Venue | 核心方法/发现 | 与我们的关系 |
25	|------|------|------|-------|--------------|-------------|
26	| How Bad is Training on Synthetic Data? | Seddik et al. | 2024 | arXiv | 统计模型给出混合训练下合成数据比例安全上限 | **互补**：安全阈值估计可与我们的监控信号阈值对照验证 |
27	| Towards Theoretical Understandings of Self-Consuming Generative Models | Fu et al. | 2024 | ICML | 统计/表达/近似三种误差源在迭代中复合 | **互补**：误差增长理论界为理解信号变化趋势提供预期 |
28	| A Closer Look at Model Collapse | Shi et al. | 2025 | NeurIPS (Spotlight) | 揭示 generalization→memorization 转变；数据熵与泛化强线性相关 | **互补**：他们用数据级熵，我们用模型内部训练动态信号；数据熵可作为外部验证指标 |
29	| Position: Model Collapse Does Not Mean What You Think | Schaeffer, Kazdan et al. | 2025 | arXiv | 梳理 8 种 collapse 定义，分三个家族（test loss / 分布形变 / 缩放行为） | **互补**：论文中需明确采用的 collapse 定义，建议采用其分类框架 |
30	| From Collapse to Improvement | Bakshi et al. | 2026 | arXiv | 非零真实数据权重（即使递减）可避免 collapse | **互补**：刻画迭代训练的长期演化规律 |
31	| Will Large-scale Generative Models Corrupt Future Datasets? | Hataya, Bao & Arai | 2023 | ICCV | ImageNet/COCO 规模验证生成数据的负面影响 | **支持**：视觉领域的早期大规模 collapse 实证 |
32	| LLMs Suffer From Their Own Output | Briesch, Sobania & Rothlauf | 2023 | arXiv | 首次 LLM self-consuming loop 实证，多样性随合成比例下降 | **支持**：早期 LLM 实证；他们用输出级多样性指标，我们用训练动态内部信号 |
33	
34	---
35	
36	## 2. Data Contamination Detection
37	
38	现有方法回答"是否有合成数据"，我们回答"合成数据造成了多严重的 collapse"。两者互补但不重叠。
39	
40	| 论文 | 作者 | 年份 | Venue | 核心方法/发现 | 与我们的关系 |
41	|------|------|------|-------|--------------|-------------|
42	| A Watermark for Large Language Models | Kirchenbauer et al. | 2023 | ICML | Green/red token list 水印框架 + 统计检测 | **互补**：合成数据溯源基础方法，标记合成数据以追踪传播 |
43	| Scalable Watermarking (SynthID-Text) | Dathathri et al. | 2024 | Nature | 产品级文本水印，Gemini ~20M 响应验证 | **互补**：工业级合成数据标记实践 |
44	| Watermarking Makes Language Models Radioactive | Sander et al. | 2024 | NeurIPS | 水印残留可检测模型是否在合成数据上训练 | **互补**：检测"是否用了合成数据"vs 我们监控"多严重" |
45	| DetectGPT: Zero-Shot Machine-Generated Text Detection | Mitchell et al. | 2023 | ICML | LLM 生成文本占据 log-probability 负曲率区域，零样本检测 | **互补**：合成文本检测方法，可识别训练数据中的合成成分 |
46	| Detecting Pretraining Data (Min-K% Prob) | Shi et al. | 2024 | ICLR | 未见样本含低概率 outlier word，检测预训练数据成员 | **互补**：数据污染检测工具，可检测合成数据是否混入训练集 |
47	| Learning by Surprise: Surplexity | Wyss et al. | 2024 | arXiv | Next-token probability 量化多样性损失；25%/50%/75% 合成比例分析 | **互补**：输出级指标，事后分析；fraction 实验设计可对照 |
48	| The FineWeb Datasets | Penedo et al. | 2024 | arXiv | 15T token 数据集策略文档——去重、过滤、数据质量 ablation | **互补**：高质量训练数据标准参考 |
49	| The LLM Data Auditor | Zhang et al. | 2026 | arXiv | 合成数据评估指标分类体系（quality + trustworthiness） | **互补**：数据质量评估框架参考 |
50	
51	---
52	
53	## 3. Training Dynamics Monitoring
54	
55	用训练过程中的信号做实时监控/诊断的先例。
56	
57	### 直接竞品
58	
59	| 论文 | 作者 | 年份 | Venue | 核心方法/发现 | 与我们的关系 |
60	|------|------|------|-------|--------------|-------------|
61	| **SIGMA**: Scalable Spectral Insights for LLM Model Collapse | Gu et al. | 2026 | arXiv | 输出嵌入 Gram 矩阵的谱分析量化 collapse；推导谱收缩界 | **竞争**：事后/黑盒方法，不做 per-layer，不跟踪训练动态。我们是在线实时监控，更早期更细粒度 |
62	| Monitoring Neural Training with Topology | Kalinowski | 2026 | arXiv | 在线拓扑监控器（persistent homology + Collapse Index），稀疏增量更新 | **竞争**：同为在线监控但信号族完全不同（拓扑 vs 频谱/熵）。我们更轻量、更可解释，且验证迭代合成数据场景 |
63	
64	### 竞品对比矩阵
65	
66	| 维度 | SIGMA (Gu 2026) | Kalinowski 2026 | **Ours** |
67	|------|-----------------|-----------------|----------|
68	| 信号类型 | Gram 矩阵谱 | Persistent homology | 权重频谱熵 + stable rank + token entropy + PPL |
69	| 在线/事后 | 事后 | 在线 | **在线** |
70	| Per-layer | ✗ | ✗ | **✓** |
71	| 迭代合成数据 | ✗ | ✗ | **✓** |
72	| 计算开销 | 中等 | 高（拓扑计算） | **低（SVD + 标量统计）** |
73	| 早期预警 | ✗ | 有（不同场景） | **✓ (3% 训练进度)** |
74	| 信号分类学 | ✗ | ✗ | **✓** |
75	
76	### 训练动态诊断方法
77	
78	| 论文 | 作者 | 年份 | Venue | 核心方法/发现 | 与我们的关系 |
79	|------|------|------|-------|--------------|-------------|
80	| Spectral Lens | Liu et al. | 2026 | arXiv | Activation covariance + gradient SVD 谱诊断 LLM 优化 | **互补**：方法论高度相关（频谱分析训练动态），但关注优化诊断而非 collapse |
81	| Critical Sharpness | Kalra et al. | 2026 | arXiv | <10 forward passes 度量 loss landscape 曲率；7B 规模验证 progressive sharpening | **互补**：可作为信号集的潜在补充 |
82	| Diffusion Spectral Entropy (DSE) | Chen & Liu | 2024 | IEEE CISS | DSE 跟踪训练动态，过拟合时 DSMI 停滞 | **互补**：spectral entropy 的替代实现参考 |
83	| Layer Collapse in Diffusion LMs | Conzelmann et al. | 2026 | arXiv | Diffusion LM per-layer activation collapse，少数早期层出现 channel-axis collapse | **互补**：per-layer collapse 分析方法论参考，但场景不同（diffusion LM） |
84	| Neural Collapse | Papyan, Han & Donoho | 2020 | PNAS | 分类网络训练末期 Neural Collapse——类内表征收缩到 Simplex ETF | **互补**：概念区分参考（neural collapse ≠ model collapse），谱分析方法论可借鉴 |
85	
86	### Collapse 缓解策略（与监控正交互补）
87	
88	| 论文 | 作者 | 年份 | Venue | 核心方法/发现 | 与我们的关系 |
89	|------|------|------|-------|--------------|-------------|
90	| Is Model Collapse Inevitable? | Gerstgrasser, Schaeffer et al. | 2024 | arXiv | 数据累积（非替换）可避免 collapse | **互补**：他们研究"何时"，我们研究"如何检测" |
91	| Collapse or Thrive? | Kazdan et al. | 2024 | arXiv | Replace→collapse, Accumulate→stable, Fixed compute→plateau | **互补**：不同工作流验证场景 |
92	| Beyond Model Collapse: Verification | Feng et al. | 2025 | ICLR | 不完美验证器也可有效筛选合成数据 | **互补**：我们的信号可作为验证器触发条件 |
93	| Escaping Model Collapse via Verification | Yi et al. | 2025 | arXiv | 外部验证器阻止 collapse；长期收敛到验证器知识中心 | **互补**：缓解方向 |
94	| Self-Correcting Self-Consuming Loops | Gillman et al. | 2024 | ICML | Correction function 使 loop 指数级稳定 | **互补**：信号可指导何时激活 correction |
95	
96	---
97	
98	## 4. Spectral Analysis in NLP
99	
100	SVD/谱方法在神经网络分析中的应用，构成我们信号设计的方法论基础。
101	
102	| 论文 | 作者 | 年份 | Venue | 核心方法/发现 | 与我们的关系 |
103	|------|------|------|-------|--------------|-------------|
104	| Predicting Trends in Quality (WeightWatcher) | Martin & Mahoney | 2021 | Nature Comms | RMT 分析权重矩阵谱性质（stable rank、power law α、spectral norm），无需训练/测试数据预测模型质量 | **支持**：方法论基础。WeightWatcher 的 stable rank 和谱分析直接启发我们的信号设计 |
105	| Approaching Deep Learning through Spectral Dynamics of Weights | Yunis, Patel et al. | 2024 | arXiv | 谱动态区分记忆 vs 泛化网络；权重衰减增强低秩偏置 | **支持**：谱动态视角可用于理解 collapse 中的权重变化 |
106	| AlphaPruning | Lu et al. | 2024 | NeurIPS | Alpha exponent per-layer 指导 LLM 剪枝（80% sparsity） | **支持**：验证 per-layer 谱分析对 LLM 质量评估有效 |
107	| Stable Rank Normalization | Sanyal, Torr & Dokania | 2020 | ICLR | Stable rank 与泛化直接关联（gap 改善 11.3%） | **支持**：理论证明 stable rank ↔ 泛化，支持我们选用 stable rank 监控 collapse（泛化退化） |
108	| Predicting LLM Compression Degradation from Spectral Statistics | Xu | 2026 | arXiv | Stable rank 是压缩退化主要预测因子（Pearson r=0.890）；per-layer attention vs MLP 分析 | **支持**：直接验证 stable rank 作为退化预测信号的有效性 |
109	| Nonlinear Random Matrix Theory for Deep Learning | Pennington & Worah | 2017 | NeurIPS | 将非线性纳入 RMT 矩方法框架，推导协方差矩阵在网络层间传播的渐近谱分布 | **支持**：RMT 理论基础 |
110	
111	### Stable rank 作为 collapse 信号的文献支撑链
112	
113	1. **Sanyal 2020** (ICLR): stable rank ↔ 泛化 gap 直接关联
114	2. **Martin & Mahoney 2021** (Nature Comms): stable rank 追踪自正则化程度
115	3. **Xu 2026** (arXiv): stable rank 预测 LLM 退化 (r=0.890)
116	4. **本文**: 首次将 stable rank 用于迭代合成数据 collapse 在线监控
117	
118	### Spectral entropy 作为 collapse 信号的文献支撑链
119	
120	1. **Pennington & Worah 2017** (NeurIPS): RMT 理论基础
121	2. **Chen & Liu 2024** (IEEE CISS): DSE 跟踪训练动态
122	3. **SIGMA 2026** (arXiv): 谱分析用于 collapse（但在 Gram 矩阵上）
123	4. **本文**: 首次将 weight spectral entropy 用于 collapse 在线监控
124	
125	---
126	
127	## 5. Gap Analysis
128	
129	### 现有工作未覆盖的空间 = 我们的 contribution space
130	
131	**核心空白**：在 37 篇文献中，**无论文同时做到**：
132	1. 训练中在线监控（非事后评估）
133	2. 用频谱/熵训练动态信号（非拓扑/非输出级）
134	3. Per-layer 粒度分析
135	4. 在迭代合成数据训练场景下验证
136	
137	### 按维度拆解
138	
139	| 维度 | 现有工作覆盖 | 空白 |
140	|------|-------------|------|
141	| **在线 collapse 监控** | Kalinowski (拓扑信号) | 无频谱/熵信号的在线 collapse 监控 |
142	| **Stable rank 用于退化检测** | Xu 2026 (压缩), Martin & Mahoney (通用质量) | 无论文用 stable rank 监控 iterative synthetic data collapse |
143	| **Spectral entropy 用于训练监控** | Chen & Liu 2024 (DSE, 一般训练) | 无论文用 weight spectral entropy 监控 collapse |
144	| **Per-layer collapse 分析** | Conzelmann (diffusion LM), Xu (压缩), Spectral Lens (优化) | 无论文在迭代合成数据训练中做 per-layer collapse 分析 |
145	| **早期预警定量基线** | 无 | 无论文给出 collapse 早期预警的定量进度阈值 |
146	| **信号分类学** | 无 | 无论文系统比较不同信号族在不同 severity 区间的灵敏度 |
147	
148	### 与 paper_framing 三个 Claims 的对应
149	
150	| Claim | 文献支撑 | 残余空白 |
151	|-------|---------|---------|
152	| **Claim 1**: Signal-Severity Correlation（信号与 severity 单调相关） | Stable rank 有效性: Sanyal 2020, Xu 2026, Martin & Mahoney 2021 | 无论文在 collapse 场景下验证单调相关性 |
153	| **Claim 2**: Early Warning（3% 进度检测） | 无直接对比基线 | 缺少 early warning / early stopping 文献作为对比 |
154	| **Claim 3**: Non-Uniform Signal Behavior（信号分类学） | 无 | 完全新颖；建议搜索 Fisher information training dynamics 补充方法论对比 |
155	
156	### 需补充搜索的文献方向（按优先级）
157	
158	1. **Early warning / early stopping** — 与 Claim 2 直接相关，需要对比基线
159	2. **Fisher information 训练监控** — 方法论对比，加强 Claim 3 分类学的完整性
160	3. **LLM per-layer degradation** — 加强 Claim 3 per-layer 分析的文献支撑
161	
162	### 论文 positioning 一句话
163	
164	> To the best of our knowledge, no prior work simultaneously achieves (a) online monitoring during training, (b) spectral/entropy training dynamics signals, (c) per-layer granularity, and (d) validation in the iterative synthetic data training setting.
165	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ff44be2-3e48-4a31-bc5d-31a480762059",
  "isSidechain": false,
  "promptId": "a7003b6e-3a25-4888-837a-59f1925bbd90",
  "type": "user",
  "uuid": "f4173916-4eea-4a15-b628-738ef7467a64",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/_project/report/related_work_notes_45da09.md",
      "content": "# Related Work Notes — Collapse Severity Monitor\n\n**Project**: collapse_severity_monitor | **Target**: NeurIPS 2026\n**Based on**: literature_map.yaml (37 papers), worker_research_related-work_20260515T005137\n**Date**: 2026-05-15\n\n---\n\n## 1. Model Collapse 理论基础\n\n核心问题：在合成数据上迭代训练导致模型质量不可逆退化。\n\n### 基石论文\n\n| 论文 | 作者 | 年份 | Venue | 核心方法/发现 | 与我们的关系 |\n|------|------|------|-------|--------------|-------------|\n| AI Models Collapse When Trained on Recursively Generated Data | Shumailov et al. | 2024 | Nature | 首次系统证明迭代合成数据训练→分布尾部消失→model collapse（LLM/VAE/GMM） | **支持**：定义了我们要解决的问题；他们用事后评估（test loss），我们提供在线监控 |\n| Self-Consuming Generative Models Go MAD | Alemohammad et al. | 2024 | ICLR | 定义三种自噬循环（fully synthetic / augmentation / fresh data），证明无 fresh data 时 precision 或 recall 必降 | **支持**：MAD 框架直接对应我们的实验设计中的迭代合成数据设定 |\n| Strong Model Collapse | Dohmatob, Feng et al. | 2025 | ICLR (Spotlight) | 算子值自由概率论证明即使 1/1000 合成数据也导致 collapse，更大模型放大 collapse | **支持**：解释了监控的必要性——即使少量合成数据也危险；fraction 实验与我们的 6 级污染实验直接相关 |\n| A Tale of Tails: Model Collapse as a Change of Scaling Laws | Dohmatob et al. | 2024 | ICML | Collapse 导致 scaling law 改变，skill un-learning 现象 | **支持**：从 scaling law 角度量化 collapse 严重度，提供事后分析视角的对比 |\n\n### 理论扩展与实证\n\n| 论文 | 作者 | 年份 | Venue | 核心方法/发现 | 与我们的关系 |\n|------|------|------|-------|--------------|-------------|\n| How Bad is Training on Synthetic Data? | Seddik et al. | 2024 | arXiv | 统计模型给出混合训练下合成数据比例安全上限 | **互补**：安全阈值估计可与我们的监控信号阈值对照验证 |\n| Towards Theoretical Understandings of Self-Consuming Generative Models | Fu et al. | 2024 | ICML | 统计/表达/近似三种误差源在迭代中复合 | **互补**：误差增长理论界为理解信号变化趋势提供预期 |\n| A Closer Look at Model Collapse | Shi et al. | 2025 | NeurIPS (Spotlight) | 揭示 generalization→memorization 转变；数据熵与泛化强线性相关 | **互补**：他们用数据级熵，我们用模型内部训练动态信号；数据熵可作为外部验证指标 |\n| Position: Model Collapse Does Not Mean What You Think | Schaeffer, Kazdan et al. | 2025 | arXiv | 梳理 8 种 collapse 定义，分三个家族（test loss / 分布形变 / 缩放行为） | **互补**：论文中需明确采用的 collapse 定义，建议采用其分类框架 |\n| From Collapse to Improvement | Bakshi et al. | 2026 | arXiv | 非零真实数据权重（即使递减）可避免 collapse | **互补**：刻画迭代训练的长期演化规律 |\n| Will Large-scale Generative Models Corrupt Future Datasets? | Hataya, Bao & Arai | 2023 | ICCV | ImageNet/COCO 规模验证生成数据的负面影响 | **支持**：视觉领域的早期大规模 collapse 实证 |\n| LLMs Suffer From Their Own Output | Briesch, Sobania & Rothlauf | 2023 | arXiv | 首次 LLM self-consuming loop 实证，多样性随合成比例下降 | **支持**：早期 LLM 实证；他们用输出级多样性指标，我们用训练动态内部信号 |\n\n---\n\n## 2. Data Contamination Detection\n\n现有方法回答\"是否有合成数据\"，我们回答\"合成数据造成了多严重的 collapse\"。两者互补但不重叠。\n\n| 论文 | 作者 | 年份 | Venue | 核心方法/发现 | 与我们的关系 |\n|------|------|------|-------|--------------|-------------|\n| A Watermark for Large Language Models | Kirchenbauer et al. | 2023 | ICML | Green/red token list 水印框架 + 统计检测 | **互补**：合成数据溯源基础方法，标记合成数据以追踪传播 |\n| Scalable Watermarking (SynthID-Text) | Dathathri et al. | 2024 | Nature | 产品级文本水印，Gemini ~20M 响应验证 | **互补**：工业级合成数据标记实践 |\n| Watermarking Makes Language Models Radioactive | Sander et al. | 2024 | NeurIPS | 水印残留可检测模型是否在合成数据上训练 | **互补**：检测\"是否用了合成数据\"vs 我们监控\"多严重\" |\n| DetectGPT: Zero-Shot Machine-Generated Text Detection | Mitchell et al. | 2023 | ICML | LLM 生成文本占据 log-probability 负曲率区域，零样本检测 | **互补**：合成文本检测方法，可识别训练数据中的合成成分 |\n| Detecting Pretraining Data (Min-K% Prob) | Shi et al. | 2024 | ICLR | 未见样本含低概率 outlier word，检测预训练数据成员 | **互补**：数据污染检测工具，可检测合成数据是否混入训练集 |\n| Learning by Surprise: Surplexity | Wyss et al. | 2024 | arXiv | Next-token probability 量化多样性损失；25%/50%/75% 合成比例分析 | **互补**：输出级指标，事后分析；fraction 实验设计可对照 |\n| The FineWeb Datasets | Penedo et al. | 2024 | arXiv | 15T token 数据集策略文档——去重、过滤、数据质量 ablation | **互补**：高质量训练数据标准参考 |\n| The LLM Data Auditor | Zhang et al. | 2026 | arXiv | 合成数据评估指标分类体系（quality + trustworthiness） | **互补**：数据质量评估框架参考 |\n\n---\n\n## 3. Training Dynamics Monitoring\n\n用训练过程中的信号做实时监控/诊断的先例。\n\n### 直接竞品\n\n| 论文 | 作者 | 年份 | Venue | 核心方法/发现 | 与我们的关系 |\n|------|------|------|-------|--------------|-------------|\n| **SIGMA**: Scalable Spectral Insights for LLM Model Collapse | Gu et al. | 2026 | arXiv | 输出嵌入 Gram 矩阵的谱分析量化 collapse；推导谱收缩界 | **竞争**：事后/黑盒方法，不做 per-layer，不跟踪训练动态。我们是在线实时监控，更早期更细粒度 |\n| Monitoring Neural Training with Topology | Kalinowski | 2026 | arXiv | 在线拓扑监控器（persistent homology + Collapse Index），稀疏增量更新 | **竞争**：同为在线监控但信号族完全不同（拓扑 vs 频谱/熵）。我们更轻量、更可解释，且验证迭代合成数据场景 |\n\n### 竞品对比矩阵\n\n| 维度 | SIGMA (Gu 2026) | Kalinowski 2026 | **Ours** |\n|------|-----------------|-----------------|----------|\n| 信号类型 | Gram 矩阵谱 | Persistent homology | 权重频谱熵 + stable rank + token entropy + PPL |\n| 在线/事后 | 事后 | 在线 | **在线** |\n| Per-layer | ✗ | ✗ | **✓** |\n| 迭代合成数据 | ✗ | ✗ | **✓** |\n| 计算开销 | 中等 | 高（拓扑计算） | **低（SVD + 标量统计）** |\n| 早期预警 | ✗ | 有（不同场景） | **✓ (3% 训练进度)** |\n| 信号分类学 | ✗ | ✗ | **✓** |\n\n### 训练动态诊断方法\n\n| 论文 | 作者 | 年份 | Venue | 核心方法/发现 | 与我们的关系 |\n|------|------|------|-------|--------------|-------------|\n| Spectral Lens | Liu et al. | 2026 | arXiv | Activation covariance + gradient SVD 谱诊断 LLM 优化 | **互补**：方法论高度相关（频谱分析训练动态），但关注优化诊断而非 collapse |\n| Critical Sharpness | Kalra et al. | 2026 | arXiv | <10 forward passes 度量 loss landscape 曲率；7B 规模验证 progressive sharpening | **互补**：可作为信号集的潜在补充 |\n| Diffusion Spectral Entropy (DSE) | Chen & Liu | 2024 | IEEE CISS | DSE 跟踪训练动态，过拟合时 DSMI 停滞 | **互补**：spectral entropy 的替代实现参考 |\n| Layer Collapse in Diffusion LMs | Conzelmann et al. | 2026 | arXiv | Diffusion LM per-layer activation collapse，少数早期层出现 channel-axis collapse | **互补**：per-layer collapse 分析方法论参考，但场景不同（diffusion LM） |\n| Neural Collapse | Papyan, Han & Donoho | 2020 | PNAS | 分类网络训练末期 Neural Collapse——类内表征收缩到 Simplex ETF | **互补**：概念区分参考（neural collapse ≠ model collapse），谱分析方法论可借鉴 |\n\n### Collapse 缓解策略（与监控正交互补）\n\n| 论文 | 作者 | 年份 | Venue | 核心方法/发现 | 与我们的关系 |\n|------|------|------|-------|--------------|-------------|\n| Is Model Collapse Inevitable? | Gerstgrasser, Schaeffer et al. | 2024 | arXiv | 数据累积（非替换）可避免 collapse | **互补**：他们研究\"何时\"，我们研究\"如何检测\" |\n| Collapse or Thrive? | Kazdan et al. | 2024 | arXiv | Replace→collapse, Accumulate→stable, Fixed compute→plateau | **互补**：不同工作流验证场景 |\n| Beyond Model Collapse: Verification | Feng et al. | 2025 | ICLR | 不完美验证器也可有效筛选合成数据 | **互补**：我们的信号可作为验证器触发条件 |\n| Escaping Model Collapse via Verification | Yi et al. | 2025 | arXiv | 外部验证器阻止 collapse；长期收敛到验证器知识中心 | **互补**：缓解方向 |\n| Self-Correcting Self-Consuming Loops | Gillman et al. | 2024 | ICML | Correction function 使 loop 指数级稳定 | **互补**：信号可指导何时激活 correction |\n\n---\n\n## 4. Spectral Analysis in NLP\n\nSVD/谱方法在神经网络分析中的应用，构成我们信号设计的方法论基础。\n\n| 论文 | 作者 | 年份 | Venue | 核心方法/发现 | 与我们的关系 |\n|------|------|------|-------|--------------|-------------|\n| Predicting Trends in Quality (WeightWatcher) | Martin & Mahoney | 2021 | Nature Comms | RMT 分析权重矩阵谱性质（stable rank、power law α、spectral norm），无需训练/测试数据预测模型质量 | **支持**：方法论基础。WeightWatcher 的 stable rank 和谱分析直接启发我们的信号设计 |\n| Approaching Deep Learning through Spectral Dynamics of Weights | Yunis, Patel et al. | 2024 | arXiv | 谱动态区分记忆 vs 泛化网络；权重衰减增强低秩偏置 | **支持**：谱动态视角可用于理解 collapse 中的权重变化 |\n| AlphaPruning | Lu et al. | 2024 | NeurIPS | Alpha exponent per-layer 指导 LLM 剪枝（80% sparsity） | **支持**：验证 per-layer 谱分析对 LLM 质量评估有效 |\n| Stable Rank Normalization | Sanyal, Torr & Dokania | 2020 | ICLR | Stable rank 与泛化直接关联（gap 改善 11.3%） | **支持**：理论证明 stable rank ↔ 泛化，支持我们选用 stable rank 监控 collapse（泛化退化） |\n| Predicting LLM Compression Degradation from Spectral Statistics | Xu | 2026 | arXiv | Stable rank 是压缩退化主要预测因子（Pearson r=0.890）；per-layer attention vs MLP 分析 | **支持**：直接验证 stable rank 作为退化预测信号的有效性 |\n| Nonlinear Random Matrix Theory for Deep Learning | Pennington & Worah | 2017 | NeurIPS | 将非线性纳入 RMT 矩方法框架，推导协方差矩阵在网络层间传播的渐近谱分布 | **支持**：RMT 理论基础 |\n\n### Stable rank 作为 collapse 信号的文献支撑链\n\n1. **Sanyal 2020** (ICLR): stable rank ↔ 泛化 gap 直接关联\n2. **Martin & Mahoney 2021** (Nature Comms): stable rank 追踪自正则化程度\n3. **Xu 2026** (arXiv): stable rank 预测 LLM 退化 (r=0.890)\n4. **本文**: 首次将 stable rank 用于迭代合成数据 collapse 在线监控\n\n### Spectral entropy 作为 collapse 信号的文献支撑链\n\n1. **Pennington & Worah 2017** (NeurIPS): RMT 理论基础\n2. **Chen & Liu 2024** (IEEE CISS): DSE 跟踪训练动态\n3. **SIGMA 2026** (arXiv): 谱分析用于 collapse（但在 Gram 矩阵上）\n4. **本文**: 首次将 weight spectral entropy 用于 collapse 在线监控\n\n---\n\n## 5. Gap Analysis\n\n### 现有工作未覆盖的空间 = 我们的 contribution space\n\n**核心空白**：在 37 篇文献中，**无论文同时做到**：\n1. 训练中在线监控（非事后评估）\n2. 用频谱/熵训练动态信号（非拓扑/非输出级）\n3. Per-layer 粒度分析\n4. 在迭代合成数据训练场景下验证\n\n### 按维度拆解\n\n| 维度 | 现有工作覆盖 | 空白 |\n|------|-------------|------|\n| **在线 collapse 监控** | Kalinowski (拓扑信号) | 无频谱/熵信号的在线 collapse 监控 |\n| **Stable rank 用于退化检测** | Xu 2026 (压缩), Martin & Mahoney (通用质量) | 无论文用 stable rank 监控 iterative synthetic data collapse |\n| **Spectral entropy 用于训练监控** | Chen & Liu 2024 (DSE, 一般训练) | 无论文用 weight spectral entropy 监控 collapse |\n| **Per-layer collapse 分析** | Conzelmann (diffusion LM), Xu (压缩), Spectral Lens (优化) | 无论文在迭代合成数据训练中做 per-layer collapse 分析 |\n| **早期预警定量基线** | 无 | 无论文给出 collapse 早期预警的定量进度阈值 |\n| **信号分类学** | 无 | 无论文系统比较不同信号族在不同 severity 区间的灵敏度 |\n\n### 与 paper_framing 三个 Claims 的对应\n\n| Claim | 文献支撑 | 残余空白 |\n|-------|---------|---------|\n| **Claim 1**: Signal-Severity Correlation（信号与 severity 单调相关） | Stable rank 有效性: Sanyal 2020, Xu 2026, Martin & Mahoney 2021 | 无论文在 collapse 场景下验证单调相关性 |\n| **Claim 2**: Early Warning（3% 进度检测） | 无直接对比基线 | 缺少 early warning / early stopping 文献作为对比 |\n| **Claim 3**: Non-Uniform Signal Behavior（信号分类学） | 无 | 完全新颖；建议搜索 Fisher information training dynamics 补充方法论对比 |\n\n### 需补充搜索的文献方向（按优先级）\n\n1. **Early warning / early stopping** — 与 Claim 2 直接相关，需要对比基线\n2. **Fisher information 训练监控** — 方法论对比，加强 Claim 3 分类学的完整性\n3. **LLM per-layer degradation** — 加强 Claim 3 per-layer 分析的文献支撑\n\n### 论文 positioning 一句话\n\n> To the best of our knowledge, no prior work simultaneously achieves (a) online monitoring during training, (b) spectral/entropy training dynamics signals, (c) per-layer granularity, and (d) validation in the iterative synthetic data training setting.\n",
      "numLines": 165,
      "startLine": 1,
      "totalLines": 165
    }
  },
  "sourceToolAssistantUUID": "8ff44be2-3e48-4a31-bc5d-31a480762059",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-15T02:10:46.334Z_

<details open><summary>🔧 Tool call — Read · `toolu_0162gkkcYJmWc2kVjTGuf8Bb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/_project/report/literature_gap_search.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4173916-4eea-4a15-b628-738ef7467a64",
  "isSidechain": false,
  "requestId": "req_011Cb3YQm6cVssHK4wzC8S3x",
  "type": "assistant",
  "uuid": "b47dd486-bd5f-4a62-97b6-460bde9e4e1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YEas68yHeLep7hMGzfWWuS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10671,
      "cache_read_input_tokens": 23687,
      "output_tokens": 293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10671,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 293,
          "cache_read_input_tokens": 23687,
          "cache_creation_input_tokens": 10671,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10671
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

_source line 33 · 2026-05-15T02:10:46.339Z_

<details><summary>↩ Tool result · `toolu_0162gkkcYJmWc2kVjTGuf8Bb`</summary>

````text
1	# Literature Gap Search — collapse_severity_monitor
2	# 日期: 2026-05-15
3	# 目的: 补充 related_work_notes 识别的 3 个文献空白
4	
5	---
6	
7	## Gap 1: Training Dynamics as Data Quality Proxy
8	
9	**搜索关键词**: training dynamics data quality, gradient-based data valuation, loss curve analysis data contamination, spectral properties gradient SVD
10	
11	**发现**: 该方向近两年研究活跃，梯度谱分析（SVD of gradients）已被用于评估数据质量，但**无论文将其应用于迭代合成数据场景下的 collapse 监控**。
12	
13	### 新增论文
14	
15	```yaml
16	- key: Li2025_gradient_quality
17	  title: "How Instruction and Reasoning Data shape Post-Training: Data Quality through the Lens of Layer-wise Gradients"
18	  authors: "Ming Li, Yanhong Li, Ziyue Li, Tianyi Zhou"
19	  year: 2025
20	  venue: arXiv (2504.10766)
21	  category: method-component
22	  role: supporting
23	  relevance: "用 layer-wise gradient SVD 的 effective rank 和 nuclear norm 统一多种数据质量指标，高质量数据对应更高 effective rank"
24	  gap_addressed: "训练动态（梯度谱）作为数据质量代理"
25	  vs_ours: >
26	    他们用梯度的 SVD 谱评估静态数据集质量（post-training 场景），
27	    我们用权重的 SVD 谱在训练过程中实时追踪质量退化。
28	    方法论高度相关——可作为我们信号选择的理论支撑。
29	
30	- key: Evans2024_dvgs
31	  title: "Data Valuation with Gradient Similarity"
32	  authors: "Nathaniel J. Evans, Gordon B. Mills, Guanming Wu, Xubo Song, Shannon McWeeney"
33	  year: 2024
34	  venue: arXiv (2405.08217)
35	  category: method-component
36	  role: supporting
37	  relevance: "用梯度相似度量化每个训练样本的价值，可识别错误标注和低质量数据"
38	  gap_addressed: "梯度信号作为数据质量代理"
39	  vs_ours: >
40	    他们做样本级数据估值，我们做训练过程级 collapse 监控。
41	    互补方向——他们的梯度相似度可作为我们检测合成数据退化的补充信号。
42	
43	- key: Elgaar2026_curriculum_dynamics
44	  title: "Curriculum Learning for LLM Pretraining: An Analysis of Learning Dynamics"
45	  authors: "Mohamed Elgaar, Hadi Amiri"
46	  year: 2026
47	  venue: arXiv (2601.21698)
48	  category: method-component
49	  role: supporting
50	  relevance: "用 gradient noise scale 和 singular entropy（output head 谱饱和度）作为 LLM 训练动态诊断指标"
51	  gap_addressed: "训练动态信号（singular entropy）作为数据/训练质量指标"
52	  vs_ours: >
53	    他们的 singular entropy 与我们的 spectral entropy 概念相近，用于诊断训练质量。
54	    他们在 curriculum learning 场景，我们在 iterative synthetic data 场景。
55	    验证了 spectral entropy 类信号的诊断有效性。
56	
57	- key: Qiu2025_spectral_alignment
58	  title: "Spectral Alignment as Predictor of Loss Explosion in Neural Network Training"
59	  authors: "Haiquan Qiu, You Wu, Yingjie Tan, Yaqing Wang, Quanming Yao"
60	  year: 2025
61	  venue: arXiv (2510.04202)
62	  category: method-component
63	  role: supporting
64	  relevance: "SA 监控层输入与权重主奇异向量的对齐分布，sign diversity 崩塌是 loss 爆炸的早期预测器"
65	  gap_addressed: "训练动态信号（谱对齐）作为训练健康度/数据质量代理；也与 gap 2（early warning）相关"
66	  vs_ours: >
67	    他们监控 input-weight 对齐，我们监控权重谱本身。
68	    SA 比传统 gradient/weight norm 更早预警——与我们的目标（早期检测）一致。
69	    可作为我们信号集的潜在补充。
70	
71	- key: Wang2025_data_value_scaling
72	  title: "Data Value in the Age of Scaling: Understanding LLM Scaling Dynamics Under Real-Synthetic Data Mixtures"
73	  authors: "Haohui Wang, Jingyuan Qi, Jianpeng Chen, Jun Wu, Lifu Huang, Lecheng Zheng, Kevin Choi, Balaji Veeramani, Edward Bowen, Alison Hu, Tyler Cody, Dawei Zhou"
74	  year: 2025
75	  venue: arXiv (2511.13640)
76	  category: evaluation
77	  role: supporting
78	  relevance: "发现 real-synthetic 混合数据训练 LLM 存在三阶段 scaling 行为，合成数据的 tail truncation 效应"
79	  gap_addressed: "训练动态在 real-synthetic 混合场景下的行为"
80	  vs_ours: >
81	    他们研究 scaling dynamics，我们研究 collapse dynamics。
82	    他们的 three-phase scaling + tail truncation 发现与我们的 collapse 信号机制互补。
83	    为我们的实验设计（不同 synthetic fraction）提供理论参考。
84	```
85	
86	---
87	
88	## Gap 2: Early Stopping Criteria for Model Collapse
89	
90	**搜索关键词**: early stopping model collapse, training signal monitoring, automated training termination, detect model collapse during training
91	
92	**发现**: **该方向文献极为稀少**——这恰恰验证了我们项目的新颖性。现有工作要么做事后检测（SIGMA），要么做缓解（ForTIFAI/verifier），**无论文提出基于训练动态信号的 model collapse early stopping criterion**。
93	
94	### 新增论文
95	
96	```yaml
97	- key: Zibakhsh2025_fortifai
98	  title: "ForTIFAI: Fending Off Recursive Training Induced Failure for AI Model Collapse"
99	  authors: "Soheil Zibakhsh Shabgahi et al."
100	  year: 2025
101	  venue: arXiv (2509.08972)
102	  category: method-component
103	  role: related
104	  relevance: "提出 Truncated Cross-Entropy (TCE) loss，通过忽略高置信度 token 缓解 collapse，模型可容忍 2.3x 更多合成数据"
105	  gap_addressed: "model collapse 的训练时干预/缓解"
106	  vs_ours: >
107	    他们修改 loss function 缓解 collapse（prevention），
108	    我们监控训练信号检测 collapse（detection）。
109	    互补方向：我们的监控信号可指导何时启用 TCE 等缓解策略。
110	    他们不做 per-layer 分析，不提供 early stopping criterion。
111	
112	- key: Fu2025_recursive_stability
113	  title: "A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops"
114	  authors: "Shi Fu, Yingjie Wang, Yuzhu Chen, Xinmei Tian, Dacheng Tao"
115	  year: 2025
116	  venue: ICLR 2025 (arXiv 2502.18865)
117	  category: background
118	  role: supporting
119	  relevance: "提出 recursive stability 概念，理论分析模型架构和 real/synthetic 比例如何影响 STL 成败"
120	  gap_addressed: "何时 collapse 会发生的理论条件"
121	  vs_ours: >
122	    他们给出 collapse 发生的理论条件（offline/事先），
123	    我们给出 collapse 正在发生的实时信号（online/训练中）。
124	    理论互补：他们的 recursive stability 条件可指导我们的阈值设定。
125	```
126	
127	**Gap 2 关键发现**: 搜索确认，截至 2026-05，**没有论文提出基于训练动态信号的 model collapse early stopping criterion**。现有最接近的工作：
128	- SIGMA (已在 lit map) — 事后/黑盒谱检测
129	- Kalinowski (已在 lit map) — 拓扑信号在线监控（但不研究 iterative synthetic data）
130	- ForTIFAI — 修改 loss function 缓解（不是 early stopping）
131	- Qiu2025 (Gap 1) — spectral alignment 预测 loss explosion（不是 collapse-specific）
132	
133	**这验证了我们的核心 novelty：用 spectral/entropy 训练动态信号做 iterative synthetic data collapse 的 early stopping。**
134	
135	---
136	
137	## Gap 3: Spectral Analysis Comparison Across Model Scales
138	
139	**搜索关键词**: spectral properties model scale, stable rank scaling laws, singular value distribution model size, weight matrix spectral analysis transformer scales
140	
141	**发现**: 该方向 2024-2026 年研究活跃，多篇论文研究 transformer 权重谱如何随模型规模变化。但**无论文在迭代合成数据场景下跨规模比较谱变化**。
142	
143	### 新增论文
144	
145	```yaml
146	- key: Liehr2025_spectral_scaling
147	  title: "Spectral Scaling Laws in Language Models: How Effectively Do Feed-Forward Networks Use Their Latent Space?"
148	  authors: "Liehr et al."
149	  year: 2025
150	  venue: EMNLP 2025 (arXiv 2510.00537)
151	  category: method-component
152	  role: supporting
153	  relevance: "发现 FFN 的 soft rank 与宽度近线性 scaling，hard rank 亚线性增长——宽度增加主要添加低能量尾部方向"
154	  gap_addressed: "谱指标（soft/hard rank）如何随模型规模 scale"
155	  vs_ours: >
156	    直接支持我们选用 stable rank（与 soft rank 相关）的合理性。
157	    他们的 asymmetric scaling law 意味着不同规模模型的 stable rank baseline 不同——
158	    我们的监控需要 scale-aware normalization。方法论参考价值高。
159	
160	- key: Staats2024_small_sv
161	  title: "Small Singular Values Matter: A Random Matrix Analysis of Transformer Models"
162	  authors: "Max Staats, Matthias Thamm, Bernd Rosenow"
163	  year: 2024
164	  venue: NeurIPS 2025 (arXiv 2410.17770)
165	  category: method-component
166	  role: supporting
167	  relevance: "跨 BERT/Pythia-410M/Llama-8B 分析权重 SVD 谱，发现小奇异值同样承载重要信息"
168	  gap_addressed: "不同模型规模下 SVD 谱的 RMT 分析对比"
169	  vs_ours: >
170	    他们用 RMT 作为零信息假设，偏离 RMT 的奇异值（大的和小的）都重要。
171	    对我们的 spectral entropy 计算有启发：不应只关注 top singular values，
172	    尾部奇异值的变化可能是 collapse 的早期信号。
173	
174	- key: Liu2026_spectral_lifecycle
175	  title: "The Spectral Lifecycle of Transformer Training: Transient Compression Waves, Persistent Spectral Gradients, and the Q/K-V Asymmetry"
176	  authors: "Yi Liu"
177	  year: 2026
178	  venue: arXiv (2604.22778)
179	  category: method-component
180	  role: supporting
181	  relevance: "首次系统研究 transformer 训练中权重 SVD 谱的全生命周期演化，跨 30M-285M 三个规模"
182	  gap_addressed: "训练过程中谱如何随深度和规模演化"
183	  vs_ours: >
184	    高度相关——他们发现 stable rank compression 以 traveling wave 形式从浅层传播到深层，
185	    Q/K 和 V/O 投影的谱行为不同。这为我们的 per-layer 分析提供关键参考：
186	    collapse 信号可能在不同层类型/深度表现不同。
187	    但他们不研究合成数据/collapse 场景。
188	
189	- key: Liu2026_homogeneity_trap
190	  title: "The Homogeneity Trap: Spectral Collapse in Doubly-Stochastic Deep Networks"
191	  authors: "Yizhi Liu"
192	  year: 2026
193	  venue: arXiv (2601.02080)
194	  category: background
195	  role: supporting
196	  relevance: "doubly-stochastic 约束导致 subdominant singular value σ₂ 被抑制，有效深度受限"
197	  gap_addressed: "特定架构约束下的谱退化现象"
198	  vs_ours: >
199	    虽然场景不同（DSM 约束 vs 合成数据训练），但谱退化机制可类比。
200	    他们的 σ₂ 抑制与我们的 stable rank 下降可能有相似的底层动力学。
201	
202	- key: Guo2026_variance_importance
203	  title: "Variance Is Not Importance: Structural Analysis of Transformer Compressibility Across Model Scales"
204	  authors: "Guo et al."
205	  year: 2026
206	  venue: arXiv (2604.20682)
207	  category: evaluation
208	  role: supporting
209	  relevance: "跨 GPT-2 (124M) 和 Mistral 7B (7.24B) 系统分析谱压缩性，发现高方差方向与预测方向 96% 不相关"
210	  gap_addressed: "不同模型规模下的谱结构差异"
211	  vs_ours: >
212	    关键发现：linearity increases with depth（Mistral 7B R²=0.17→0.93）。
213	    暗示 collapse 信号可能在深层更容易检测（线性层的谱变化更可解释）。
214	    跨规模比较方法论可参考。
215	```
216	
217	---
218	
219	## 综合分析
220	
221	### 新增论文总计: 12 篇
222	
223	| Gap | 新增 | 已有相关 | 空白程度 |
224	|-----|------|---------|---------|
225	| Gap 1: Training dynamics as data quality proxy | 5 | 3 (spectral_lens, chen_liu, kalra) | 中等——有相关工作但无人在 collapse 场景应用 |
226	| Gap 2: Early stopping for model collapse | 2 | 3 (sigma, kalinowski, shi_neurips) | **极高——核心 novelty 空间** |
227	| Gap 3: Spectral analysis across scales | 5 | 4 (xu, martin_mahoney, yunis, lu) | 中等——有跨规模谱分析但无人在 collapse 场景验证 |
228	
229	### Novelty 确认
230	
231	在 49 篇文献（37 已有 + 12 新增）中，**仍然没有工作同时满足**：
232	1. 训练中在线监控（非事后）
233	2. 用 spectral/entropy 训练动态信号
234	3. Per-layer 粒度
235	4. 在迭代合成数据训练场景下验证
236	5. 提供 early stopping criterion
237	
238	**我们的核心定位依然独特且空间更加明确。**
239	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "b47dd486-bd5f-4a62-97b6-460bde9e4e1f",
  "isSidechain": false,
  "promptId": "a7003b6e-3a25-4888-837a-59f1925bbd90",
  "type": "user",
  "uuid": "d7fffb61-d330-4159-890b-02b3e3b2ea88",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/_project/report/literature_gap_search.md",
      "content": "# Literature Gap Search — collapse_severity_monitor\n# 日期: 2026-05-15\n# 目的: 补充 related_work_notes 识别的 3 个文献空白\n\n---\n\n## Gap 1: Training Dynamics as Data Quality Proxy\n\n**搜索关键词**: training dynamics data quality, gradient-based data valuation, loss curve analysis data contamination, spectral properties gradient SVD\n\n**发现**: 该方向近两年研究活跃，梯度谱分析（SVD of gradients）已被用于评估数据质量，但**无论文将其应用于迭代合成数据场景下的 collapse 监控**。\n\n### 新增论文\n\n```yaml\n- key: Li2025_gradient_quality\n  title: \"How Instruction and Reasoning Data shape Post-Training: Data Quality through the Lens of Layer-wise Gradients\"\n  authors: \"Ming Li, Yanhong Li, Ziyue Li, Tianyi Zhou\"\n  year: 2025\n  venue: arXiv (2504.10766)\n  category: method-component\n  role: supporting\n  relevance: \"用 layer-wise gradient SVD 的 effective rank 和 nuclear norm 统一多种数据质量指标，高质量数据对应更高 effective rank\"\n  gap_addressed: \"训练动态（梯度谱）作为数据质量代理\"\n  vs_ours: >\n    他们用梯度的 SVD 谱评估静态数据集质量（post-training 场景），\n    我们用权重的 SVD 谱在训练过程中实时追踪质量退化。\n    方法论高度相关——可作为我们信号选择的理论支撑。\n\n- key: Evans2024_dvgs\n  title: \"Data Valuation with Gradient Similarity\"\n  authors: \"Nathaniel J. Evans, Gordon B. Mills, Guanming Wu, Xubo Song, Shannon McWeeney\"\n  year: 2024\n  venue: arXiv (2405.08217)\n  category: method-component\n  role: supporting\n  relevance: \"用梯度相似度量化每个训练样本的价值，可识别错误标注和低质量数据\"\n  gap_addressed: \"梯度信号作为数据质量代理\"\n  vs_ours: >\n    他们做样本级数据估值，我们做训练过程级 collapse 监控。\n    互补方向——他们的梯度相似度可作为我们检测合成数据退化的补充信号。\n\n- key: Elgaar2026_curriculum_dynamics\n  title: \"Curriculum Learning for LLM Pretraining: An Analysis of Learning Dynamics\"\n  authors: \"Mohamed Elgaar, Hadi Amiri\"\n  year: 2026\n  venue: arXiv (2601.21698)\n  category: method-component\n  role: supporting\n  relevance: \"用 gradient noise scale 和 singular entropy（output head 谱饱和度）作为 LLM 训练动态诊断指标\"\n  gap_addressed: \"训练动态信号（singular entropy）作为数据/训练质量指标\"\n  vs_ours: >\n    他们的 singular entropy 与我们的 spectral entropy 概念相近，用于诊断训练质量。\n    他们在 curriculum learning 场景，我们在 iterative synthetic data 场景。\n    验证了 spectral entropy 类信号的诊断有效性。\n\n- key: Qiu2025_spectral_alignment\n  title: \"Spectral Alignment as Predictor of Loss Explosion in Neural Network Training\"\n  authors: \"Haiquan Qiu, You Wu, Yingjie Tan, Yaqing Wang, Quanming Yao\"\n  year: 2025\n  venue: arXiv (2510.04202)\n  category: method-component\n  role: supporting\n  relevance: \"SA 监控层输入与权重主奇异向量的对齐分布，sign diversity 崩塌是 loss 爆炸的早期预测器\"\n  gap_addressed: \"训练动态信号（谱对齐）作为训练健康度/数据质量代理；也与 gap 2（early warning）相关\"\n  vs_ours: >\n    他们监控 input-weight 对齐，我们监控权重谱本身。\n    SA 比传统 gradient/weight norm 更早预警——与我们的目标（早期检测）一致。\n    可作为我们信号集的潜在补充。\n\n- key: Wang2025_data_value_scaling\n  title: \"Data Value in the Age of Scaling: Understanding LLM Scaling Dynamics Under Real-Synthetic Data Mixtures\"\n  authors: \"Haohui Wang, Jingyuan Qi, Jianpeng Chen, Jun Wu, Lifu Huang, Lecheng Zheng, Kevin Choi, Balaji Veeramani, Edward Bowen, Alison Hu, Tyler Cody, Dawei Zhou\"\n  year: 2025\n  venue: arXiv (2511.13640)\n  category: evaluation\n  role: supporting\n  relevance: \"发现 real-synthetic 混合数据训练 LLM 存在三阶段 scaling 行为，合成数据的 tail truncation 效应\"\n  gap_addressed: \"训练动态在 real-synthetic 混合场景下的行为\"\n  vs_ours: >\n    他们研究 scaling dynamics，我们研究 collapse dynamics。\n    他们的 three-phase scaling + tail truncation 发现与我们的 collapse 信号机制互补。\n    为我们的实验设计（不同 synthetic fraction）提供理论参考。\n```\n\n---\n\n## Gap 2: Early Stopping Criteria for Model Collapse\n\n**搜索关键词**: early stopping model collapse, training signal monitoring, automated training termination, detect model collapse during training\n\n**发现**: **该方向文献极为稀少**——这恰恰验证了我们项目的新颖性。现有工作要么做事后检测（SIGMA），要么做缓解（ForTIFAI/verifier），**无论文提出基于训练动态信号的 model collapse early stopping criterion**。\n\n### 新增论文\n\n```yaml\n- key: Zibakhsh2025_fortifai\n  title: \"ForTIFAI: Fending Off Recursive Training Induced Failure for AI Model Collapse\"\n  authors: \"Soheil Zibakhsh Shabgahi et al.\"\n  year: 2025\n  venue: arXiv (2509.08972)\n  category: method-component\n  role: related\n  relevance: \"提出 Truncated Cross-Entropy (TCE) loss，通过忽略高置信度 token 缓解 collapse，模型可容忍 2.3x 更多合成数据\"\n  gap_addressed: \"model collapse 的训练时干预/缓解\"\n  vs_ours: >\n    他们修改 loss function 缓解 collapse（prevention），\n    我们监控训练信号检测 collapse（detection）。\n    互补方向：我们的监控信号可指导何时启用 TCE 等缓解策略。\n    他们不做 per-layer 分析，不提供 early stopping criterion。\n\n- key: Fu2025_recursive_stability\n  title: \"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops\"\n  authors: \"Shi Fu, Yingjie Wang, Yuzhu Chen, Xinmei Tian, Dacheng Tao\"\n  year: 2025\n  venue: ICLR 2025 (arXiv 2502.18865)\n  category: background\n  role: supporting\n  relevance: \"提出 recursive stability 概念，理论分析模型架构和 real/synthetic 比例如何影响 STL 成败\"\n  gap_addressed: \"何时 collapse 会发生的理论条件\"\n  vs_ours: >\n    他们给出 collapse 发生的理论条件（offline/事先），\n    我们给出 collapse 正在发生的实时信号（online/训练中）。\n    理论互补：他们的 recursive stability 条件可指导我们的阈值设定。\n```\n\n**Gap 2 关键发现**: 搜索确认，截至 2026-05，**没有论文提出基于训练动态信号的 model collapse early stopping criterion**。现有最接近的工作：\n- SIGMA (已在 lit map) — 事后/黑盒谱检测\n- Kalinowski (已在 lit map) — 拓扑信号在线监控（但不研究 iterative synthetic data）\n- ForTIFAI — 修改 loss function 缓解（不是 early stopping）\n- Qiu2025 (Gap 1) — spectral alignment 预测 loss explosion（不是 collapse-specific）\n\n**这验证了我们的核心 novelty：用 spectral/entropy 训练动态信号做 iterative synthetic data collapse 的 early stopping。**\n\n---\n\n## Gap 3: Spectral Analysis Comparison Across Model Scales\n\n**搜索关键词**: spectral properties model scale, stable rank scaling laws, singular value distribution model size, weight matrix spectral analysis transformer scales\n\n**发现**: 该方向 2024-2026 年研究活跃，多篇论文研究 transformer 权重谱如何随模型规模变化。但**无论文在迭代合成数据场景下跨规模比较谱变化**。\n\n### 新增论文\n\n```yaml\n- key: Liehr2025_spectral_scaling\n  title: \"Spectral Scaling Laws in Language Models: How Effectively Do Feed-Forward Networks Use Their Latent Space?\"\n  authors: \"Liehr et al.\"\n  year: 2025\n  venue: EMNLP 2025 (arXiv 2510.00537)\n  category: method-component\n  role: supporting\n  relevance: \"发现 FFN 的 soft rank 与宽度近线性 scaling，hard rank 亚线性增长——宽度增加主要添加低能量尾部方向\"\n  gap_addressed: \"谱指标（soft/hard rank）如何随模型规模 scale\"\n  vs_ours: >\n    直接支持我们选用 stable rank（与 soft rank 相关）的合理性。\n    他们的 asymmetric scaling law 意味着不同规模模型的 stable rank baseline 不同——\n    我们的监控需要 scale-aware normalization。方法论参考价值高。\n\n- key: Staats2024_small_sv\n  title: \"Small Singular Values Matter: A Random Matrix Analysis of Transformer Models\"\n  authors: \"Max Staats, Matthias Thamm, Bernd Rosenow\"\n  year: 2024\n  venue: NeurIPS 2025 (arXiv 2410.17770)\n  category: method-component\n  role: supporting\n  relevance: \"跨 BERT/Pythia-410M/Llama-8B 分析权重 SVD 谱，发现小奇异值同样承载重要信息\"\n  gap_addressed: \"不同模型规模下 SVD 谱的 RMT 分析对比\"\n  vs_ours: >\n    他们用 RMT 作为零信息假设，偏离 RMT 的奇异值（大的和小的）都重要。\n    对我们的 spectral entropy 计算有启发：不应只关注 top singular values，\n    尾部奇异值的变化可能是 collapse 的早期信号。\n\n- key: Liu2026_spectral_lifecycle\n  title: \"The Spectral Lifecycle of Transformer Training: Transient Compression Waves, Persistent Spectral Gradients, and the Q/K-V Asymmetry\"\n  authors: \"Yi Liu\"\n  year: 2026\n  venue: arXiv (2604.22778)\n  category: method-component\n  role: supporting\n  relevance: \"首次系统研究 transformer 训练中权重 SVD 谱的全生命周期演化，跨 30M-285M 三个规模\"\n  gap_addressed: \"训练过程中谱如何随深度和规模演化\"\n  vs_ours: >\n    高度相关——他们发现 stable rank compression 以 traveling wave 形式从浅层传播到深层，\n    Q/K 和 V/O 投影的谱行为不同。这为我们的 per-layer 分析提供关键参考：\n    collapse 信号可能在不同层类型/深度表现不同。\n    但他们不研究合成数据/collapse 场景。\n\n- key: Liu2026_homogeneity_trap\n  title: \"The Homogeneity Trap: Spectral Collapse in Doubly-Stochastic Deep Networks\"\n  authors: \"Yizhi Liu\"\n  year: 2026\n  venue: arXiv (2601.02080)\n  category: background\n  role: supporting\n  relevance: \"doubly-stochastic 约束导致 subdominant singular value σ₂ 被抑制，有效深度受限\"\n  gap_addressed: \"特定架构约束下的谱退化现象\"\n  vs_ours: >\n    虽然场景不同（DSM 约束 vs 合成数据训练），但谱退化机制可类比。\n    他们的 σ₂ 抑制与我们的 stable rank 下降可能有相似的底层动力学。\n\n- key: Guo2026_variance_importance\n  title: \"Variance Is Not Importance: Structural Analysis of Transformer Compressibility Across Model Scales\"\n  authors: \"Guo et al.\"\n  year: 2026\n  venue: arXiv (2604.20682)\n  category: evaluation\n  role: supporting\n  relevance: \"跨 GPT-2 (124M) 和 Mistral 7B (7.24B) 系统分析谱压缩性，发现高方差方向与预测方向 96% 不相关\"\n  gap_addressed: \"不同模型规模下的谱结构差异\"\n  vs_ours: >\n    关键发现：linearity increases with depth（Mistral 7B R²=0.17→0.93）。\n    暗示 collapse 信号可能在深层更容易检测（线性层的谱变化更可解释）。\n    跨规模比较方法论可参考。\n```\n\n---\n\n## 综合分析\n\n### 新增论文总计: 12 篇\n\n| Gap | 新增 | 已有相关 | 空白程度 |\n|-----|------|---------|---------|\n| Gap 1: Training dynamics as data quality proxy | 5 | 3 (spectral_lens, chen_liu, kalra) | 中等——有相关工作但无人在 collapse 场景应用 |\n| Gap 2: Early stopping for model collapse | 2 | 3 (sigma, kalinowski, shi_neurips) | **极高——核心 novelty 空间** |\n| Gap 3: Spectral analysis across scales | 5 | 4 (xu, martin_mahoney, yunis, lu) | 中等——有跨规模谱分析但无人在 collapse 场景验证 |\n\n### Novelty 确认\n\n在 49 篇文献（37 已有 + 12 新增）中，**仍然没有工作同时满足**：\n1. 训练中在线监控（非事后）\n2. 用 spectral/entropy 训练动态信号\n3. Per-layer 粒度\n4. 在迭代合成数据训练场景下验证\n5. 提供 early stopping criterion\n\n**我们的核心定位依然独特且空间更加明确。**\n",
      "numLines": 239,
      "startLine": 1,
      "totalLines": 239
    }
  },
  "sourceToolAssistantUUID": "b47dd486-bd5f-4a62-97b6-460bde9e4e1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool call

_source line 34 · 2026-05-15T02:10:47.252Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WxeeXXwWDivsYZmxTuSs2z`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7fffb61-d330-4159-890b-02b3e3b2ea88",
  "isSidechain": false,
  "requestId": "req_011Cb3YQm6cVssHK4wzC8S3x",
  "type": "assistant",
  "uuid": "d97e96bd-66ea-4c75-a1d7-1437bf5d2006",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YEas68yHeLep7hMGzfWWuS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10671,
      "cache_read_input_tokens": 23687,
      "output_tokens": 293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10671,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 293,
          "cache_read_input_tokens": 23687,
          "cache_creation_input_tokens": 10671,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10671
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

_source line 35 · 2026-05-15T02:10:47.331Z_

```json
{
  "parentUuid": "60b18341-85e3-45ca-a36e-0d58075f9808",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "8df7a19a-b94c-4b47-87d0-1a1b7ef26814",
  "timestamp": "2026-05-15T02:10:47.331Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "last-prompt",
  "leafUuid": "8df7a19a-b94c-4b47-87d0-1a1b7ef26814",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Compile bibliography file for paper citations",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b"
}
```

---

### Assistant

_source line 38 · 2026-05-15T02:12:03.884Z_

<details><summary>Logged reasoning block</summary>

```text
Let me extract all citation keys from the paper sections. Let me go through each file:

**abstract.tex**: No \cite or \citep commands.

**introduction.tex**:
1. `\citet{Shumailov2024}`
2. `\citet{Alemohammad2024}`
3. `\citep{Dohmatob2025}`
4. `\citep{Dohmatob2024_tails,Fu2024_icml}`
5. `\citep{Shumailov2024,Alemohammad2024}`


6. `\citep{Gerstgrasser2024}`
7. `\citep{Zibakhsh2025}`
8. `\citep{Feng2025}`
9. `\citep{Gu2026}`
10. `\citet{Kalinowski2026}`

**related_work.tex**: Now I'm continuing through the related work section, finding more citations starting with Shumailov, Alemohammad, and Dohmatob again. Continuing through the citation list... I'm now compiling a comprehensive list of all the unique citation keys I've found across these files to ensure there are no duplicates and to track everything that needs to be referenced. I'm noticing a citation key mismatch—`shumailov2024ai` appears in method.tex while other files use `Shumailov2024`, and they likely refer to the same Nature paper on model collapse from recursive training data. I need to decide whether to create both entries in the bib file or consolidate them, since BibTeX doesn't support aliases easily.

Now I'm going through the files systematically to count all unique citation keys. From introduction.tex I've identified about ten keys, and related_work.tex adds another ten or so, but I need to finish the full count across all sections to get an accurate total. I'm tallying up the unique references across all the sections—introduction gives me 10 entries, and the related work section has significantly more. Let me recount to make sure I'm getting the total right, since I want to capture all the distinct citations without duplicates. I'm compiling the BibTeX entries by going through my literature notes and knowledge base. Starting with the model collapse papers—Shumailov's work on recursive data training in Nature, Alemohammad's self-consuming models paper from ICLR, and Dohmatob's research on model collapse spanning both ICLR and ICML publications. Continuing through the bibliography, I'm seeing more recent work on model collapse from 2025 and 2026, including papers on verification approaches to escape collapse, self-correcting mechanisms, and studies examining whether collapse actually leads to improvement or degradation in model performance. Continuing through more recent work on spectral properties in language models, including studies on scaling laws, singular value dynamics, transformer training lifecycles, and how different types of training data influence model behavior. Continuing through the bibliography, I'm covering papers on watermarking techniques for language models—from foundational work on watermarks themselves through detection methods like DetectGPT and Min-K% probability approaches, plus datasets like FineWeb. I'm finishing up the bibliography with the HellaSwag paper, then I need to verify these citations. I'll focus my searches on the ones where I'm less certain about details like venues and arXiv IDs, while relying on my knowledge for the well-established papers like QLoRA, Pointer Networks, and HellaSwag. I've got a long list of papers still to verify. Rather than searching for each one individually, I should leverage what I already know from my notes—most have titles, authors, years, and venues. The main gaps are exact arXiv IDs and complete author lists for the uncertain ones. Let me parallelize the verification by splitting these into batches and running multiple search agents simultaneously to handle them more efficiently.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8df7a19a-b94c-4b47-87d0-1a1b7ef26814",
  "isSidechain": false,
  "requestId": "req_011Cb3YRKFdWrUzhaWBxKo6Z",
  "type": "assistant",
  "uuid": "38a09786-f86c-458c-83c9-e3096ac980ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018UaffBe2SeqXd2jbgmUmee",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11343,
      "cache_read_input_tokens": 34358,
      "output_tokens": 5004,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11343,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5004,
          "cache_read_input_tokens": 34358,
          "cache_creation_input_tokens": 11343,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11343
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

_source line 39 · 2026-05-15T02:12:04.384Z_

Let me also read the literature map for additional details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38a09786-f86c-458c-83c9-e3096ac980ff",
  "isSidechain": false,
  "requestId": "req_011Cb3YRKFdWrUzhaWBxKo6Z",
  "type": "assistant",
  "uuid": "63ace836-27fa-445d-ae58-419fdb1434af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018UaffBe2SeqXd2jbgmUmee",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11343,
      "cache_read_input_tokens": 34358,
      "output_tokens": 5004,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11343,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5004,
          "cache_read_input_tokens": 34358,
          "cache_creation_input_tokens": 11343,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11343
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

_source line 40 · 2026-05-15T02:12:04.892Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019YkM4XtpEm7LnZ7yzrKhNK`</summary>

```json
{
  "project": "collapse_severity_monitor",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63ace836-27fa-445d-ae58-419fdb1434af",
  "isSidechain": false,
  "requestId": "req_011Cb3YRKFdWrUzhaWBxKo6Z",
  "type": "assistant",
  "uuid": "b0fa4026-70b3-4120-bb47-a2d38fa80c66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018UaffBe2SeqXd2jbgmUmee",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11343,
      "cache_read_input_tokens": 34358,
      "output_tokens": 5004,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11343,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5004,
          "cache_read_input_tokens": 34358,
          "cache_creation_input_tokens": 11343,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11343
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

_source line 41 · 2026-05-15T02:12:04.955Z_

<details><summary>↩ Tool result · `toolu_019YkM4XtpEm7LnZ7yzrKhNK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/literature_map.yaml\", \"content\": \"# Literature Map — collapse_severity_monitor\\n# 最后更新: 2026-05-14 (expanded to 37 papers)\\n# 研究方向: 在线监控模型 collapse 严重度——用训练动态信号实时跟踪迭代合成数据训练中的质量退化\\n\\n# ============================================================\\n# 竞争关系分类说明:\\n#   direct_competitor  — 解决同一问题（在线监控 collapse）\\n#   related            — 解决相近问题或使用相关方法\\n#   complementary      — 互补（提供理论基础/工具/缓解策略）\\n#   foundation         — 领域基础工作\\n# ============================================================\\n\\npapers:\\n\\n  # ===================== DIRECT COMPETITORS =====================\\n\\n  - id: sigma_2026\\n    title: \\\"SIGMA: Scalable Spectral Insights for LLM Model Collapse\\\"\\n    authors: [Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, Alexander Aue]\\n    year: 2026\\n    venue: arXiv (2601.03385)\\n    relation: direct_competitor\\n    core_method: >\\n      通过 embedding Gram 矩阵的谱分析来量化 model collapse 程度。\\n      推导 Gram 矩阵谱的确定性和随机性界，用谱收缩作为 collapse 指标。\\n    signals: [Gram matrix spectrum, rank deficiency, spectral bounds]\\n    scale: model-level (output embeddings)\\n    key_findings:\\n      - Gram 矩阵满秩是 LLM 正常运作的必要条件\\n      - 秩亏缺意味着语义级信息丢失，标志 collapse 开始\\n      - 随机公式使框架可扩展至大规模模型\\n    vs_ours: >\\n      SIGMA 用输出嵌入的 Gram 矩阵谱，是事后/黑盒方法，不需要模型权重。\\n      我们用训练动态信号（权重频谱熵、stable rank、token entropy），\\n      是训练中实时监控，更早期更细粒度（per-layer）。\\n      SIGMA 不做 per-layer 分析，不跟踪训练过程的动态变化。\\n    threat_level: medium\\n\\n  - id: kalinowski_2026\\n    title: \\\"Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index\\\"\\n    authors: [Alexander Kalinowski]\\n    year: 2026\\n    venue: arXiv (2604.26984)\\n    relation: direct_competitor\\n    core_method: >\\n      提出在线拓扑感知监控器，结合 Modular Morse Homology Maintenance (MMHM)\\n      和复合 Collapse Index (CI)，通过稀疏增量更新实现快速在线监控。\\n    signals: [persistent homology, Collapse Index (CI), topological features]\\n    scale: model-level (representation space topology)\\n    key_findings:\\n      - CI 在 LLM fine-tuning 和时序 KGE 训练中提供低延迟早期预警\\n      - 表征各向异性和多尺度结构丧失在性能指标反应之前就可检测\\n      - 增量更新避免每个 epoch 重建复形\\n    vs_ours: >\\n      Kalinowski 用拓扑信号（persistent homology），我们用频谱/熵信号。\\n      两者都是在线监控，但信号族完全不同。我们的信号更轻量、\\n      更可解释（stable rank/spectral entropy 有直接的线性代数含义）。\\n      Kalinowski 不研究迭代合成数据训练场景。\\n    threat_level: medium\\n\\n  # ===================== CLOSELY RELATED =====================\\n\\n  - id: spectral_lens_2026\\n    title: \\\"Spectral Lens: Activation and Gradient Spectra as Diagnostics of LLM Optimization\\\"\\n    authors: [Andy Zeyi Liu et al.]\\n    year: 2026\\n    venue: arXiv (2605.05683)\\n    relation: related\\n    core_method: >\\n      用 activation covariance 和 per-sample gradient 的 SVD 谱\\n      作为 LLM 训练优化的诊断工具。\\n    signals: [activation covariance spectrum, gradient SVD spectrum]\\n    scale: layer-level\\n    key_findings:\\n      - batch size 是表示几何的隐藏决定因素\\n      - 早期训练的 activation covariance 尾部可预测下游 token 效率\\n      - activation 谱头部运动 + gradient 谱可区分学习侧和执行侧改进\\n    vs_ours: >\\n      方法论高度相关——同样用频谱分析训练动态。\\n      但他们关注优化诊断，不研究 collapse/合成数据退化。\\n      可作为方法论参考。\\n    threat_level: low\\n\\n  - id: shi_neurips2025\\n    title: \\\"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\\\"\\n    authors: [Lianghe Shi, Meng Wu, Huijie Zhang, Zekai Zhang, Molei Tao, Qing Qu]\\n    year: 2025\\n    venue: NeurIPS 2025 (Spotlight)\\n    relation: related\\n    core_method: >\\n      揭示 model collapse 中从泛化到记忆的转变。\\n      发现训练数据熵与模型泛化能力的强线性相关。\\n      提出基于熵的子集选择方法来减缓 collapse。\\n    signals: [dataset entropy, generalization metrics]\\n    scale: model-level (data distribution)\\n    key_findings:\\n      - 迭代训练中数据分布熵急剧下降导致泛化能力下降\\n      - 强线性相关：训练数据集熵与模型泛化能力\\n      - 熵选择方法有效减缓泛化到记忆转变\\n    vs_ours: >\\n      他们用数据级别的熵，我们用模型内部的训练动态信号。\\n      互补：他们的数据熵可作为我们的外部验证指标。\\n      他们不做 per-layer 分析，不做在线监控。\\n    threat_level: low\\n\\n  - id: wyss_2024\\n    title: \\\"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI\\\"\\n    authors: [C. M. Wyss et al.]\\n    year: 2024\\n    venue: arXiv (2410.12341)\\n    relation: related\\n    core_method: >\\n      用语义网络和 next-token 概率来表征 LLM 中的 model collapse。\\n      引入 collapsed prediction 概念量化多样性损失。\\n      分析不同合成 token 比例 (25%/50%/75%) 对 collapse 的影响。\\n    signals: [next-token probability distribution, semantic network metrics, collapsed prediction ratio]\\n    scale: token-level (output)\\n    key_findings:\\n      - Next-token 概率分布可精确量化多样性损失\\n      - 合成 token 比例越高，collapse 越严重\\n      - 跨数据集迁移：在非微调数据集上 collapse 程度不同\\n    vs_ours: >\\n      他们用输出级指标（next-token prob），我们用训练动态内部信号。\\n      他们的 synthetic fraction 实验与我们的实验设计有重叠。\\n      不同之处：他们是事后分析，我们是训练中在线监控。\\n    threat_level: low\\n\\n  - id: xu_2026\\n    title: \\\"Predicting LLM Compression Degradation from Spectral Statistics\\\"\\n    authors: [Mingxue Xu]\\n    year: 2026\\n    venue: arXiv (2604.18085)\\n    relation: related\\n    core_method: >\\n      用 stable rank 和信息密度 (bits/param) 预测 LLM 压缩导致的退化。\\n      交互项 compression_ratio * stable_rank 是退化的强预测器。\\n    signals: [stable rank, information density, compression ratio]\\n    scale: layer-level (attention vs MLP 分开分析)\\n    key_findings:\\n      - stable rank 是压缩退化的主要预测因子（Pearson r=0.890 attention, 0.839 MLP）\\n      - 层类型比压缩方法更重要\\n      - layer-specific calibration 优于 method-specific tuning\\n    vs_ours: >\\n      直接验证 stable rank 作为退化预测信号的有效性。\\n      虽然场景不同（压缩 vs collapse），但支持我们选用 stable rank 的合理性。\\n      他们的 per-layer 分析方法可参考。\\n    threat_level: low\\n\\n  - id: layer_collapse_diffusion_2026\\n    title: \\\"Layer Collapse in Diffusion Language Models\\\"\\n    authors: [Alexander Conzelmann, Albert Catalan-Tatjer, Shiwei Liu]\\n    year: 2026\\n    venue: arXiv (2605.06366)\\n    relation: related\\n    core_method: >\\n      分析 diffusion language model (LLaDA-8B) 中的 per-layer activation 动态，\\n      发现少数早期层展现 collapsed activation patterns。\\n    signals: [activation patterns, super-outlier magnitude]\\n    scale: layer-level\\n    key_findings:\\n      - 几个早期层出现 channel-axis collapse（单一维度主导所有位置）\\n      - 尽管看似冗余，pruning outlier 导致退化为重复随机 token 循环\\n      - Diffusion LM 与 autoregressive LM 的 collapse 行为不同\\n    vs_ours: >\\n      做了 per-layer collapse 分析，但在 diffusion LM 上。\\n      方法论参考：per-layer activation 分析方法。\\n    threat_level: low\\n\\n  # ===================== FOUNDATION =====================\\n\\n  - id: alemohammad_iclr2024\\n    title: \\\"Self-Consuming Generative Models Go MAD\\\"\\n    authors: [Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard G. Baraniuk]\\n    year: 2024\\n    venue: ICLR 2024\\n    relation: foundation\\n    core_method: >\\n      定义三种 autophagous loop（fully synthetic / synthetic augmentation / fresh data），\\n      证明无足够真实数据时 precision 或 recall 必然下降（MAD 现象）。\\n    signals: [FID, precision, recall]\\n    scale: model-level (image generative models)\\n    key_findings:\\n      - 三种 loop 类型的 collapse 行为不同\\n      - 无 fresh data 时 quality 或 diversity 必然退化\\n      - 在 StyleGAN、DDPM、denoising diffusion 上验证\\n    vs_ours: >\\n      领域基础论文之一。他们的 loop 分类框架直接对应我们的实验设计。\\n      他们用 FID/precision/recall（事后指标），我们提供训练中在线信号。\\n\\n  - id: papyan_pnas2020\\n    title: \\\"Prevalence of Neural Collapse during the Terminal Phase of Deep Learning Training\\\"\\n    authors: [Vardan Papyan, X. Y. Han, David L. Donoho]\\n    year: 2020\\n    venue: PNAS 117(40), 24652-24663\\n    relation: foundation\\n    core_method: >\\n      发现分类网络训练末期的 Neural Collapse——类内表征收缩到 Simplex ETF。\\n    signals: [within-class variability, classifier-mean alignment]\\n    scale: model-level (last-layer representations)\\n    key_findings:\\n      - 训练末期出现四种 collapse 现象\\n      - 类均值收敛到 Simplex ETF 顶点\\n      - Collapse 与泛化能力相关\\n    vs_ours: >\\n      虽然 neural collapse 与 model collapse 是不同概念，\\n      但谱分析方法论可借鉴，且提供 \\\"collapse\\\" 概念的对比参考。\\n\\n  - id: hataya_iccv2023\\n    title: \\\"Will Large-scale Generative Models Corrupt Future Datasets?\\\"\\n    authors: [Ryuichiro Hataya, Han Bao, Hiromi Arai]\\n    year: 2023\\n    venue: ICCV 2023 (pp. 20555-20565)\\n    relation: foundation\\n    core_method: >\\n      用 SOTA 生成模型生成 ImageNet/COCO 规模数据集，\\n      评估\\\"被污染\\\"数据集在分类和生成任务上的下游性能退化。\\n    signals: [classification accuracy, FID, generation quality]\\n    scale: dataset-level (ImageNet/COCO scale)\\n    key_findings:\\n      - 生成图像对下游性能有负面影响\\n      - 影响程度取决于任务类型和生成图像比例\\n      - 首次在 ImageNet 规模验证数据集污染效应\\n    vs_ours: >\\n      早期数据集污染实证研究，在视觉领域验证了 collapse 前兆。\\n      他们关注下游任务性能，我们关注训练中的实时信号。\\n\\n  # ===================== COMPLEMENTARY (Theory/Mitigation) =====================\\n\\n  - id: shumailov_nature2024\\n    title: \\\"AI Models Collapse When Trained on Recursively Generated Data\\\"\\n    authors: [Ilia Shumailov et al.]\\n    year: 2024\\n    venue: Nature 631, 755-759\\n    relation: foundation\\n    core_method: >\\n      首次系统性证明迭代合成数据训练导致 model collapse。\\n      在 LLM、VAE、GMM 上验证。分布尾部消失是核心机制。\\n    signals: [test loss, distribution tail metrics]\\n    scale: model-level\\n    key_findings:\\n      - 迭代训练导致不可逆缺陷：分布尾部消失\\n      - 罕见事件最先遗忘\\n      - LLM、VAE、GMM 都有此现象\\n    vs_ours: >\\n      领域基石论文，建立了我们要解决的问题。\\n      他们用事后评估（test loss），我们提供在线监控手段。\\n\\n  - id: dohmatob_iclr2025\\n    title: \\\"Strong Model Collapse\\\"\\n    authors: [Elvis Dohmatob, Yunzhen Feng et al.]\\n    year: 2025\\n    venue: ICLR 2025 (Spotlight)\\n    relation: complementary\\n    core_method: >\\n      用算子值自由概率论证明即使极小比例的合成数据 (1/1000)\\n      也会导致 model collapse，且更大模型放大 collapse。\\n    signals: [test error on real data, bias-variance decomposition]\\n    scale: model-level\\n    key_findings:\\n      - 任何非零常数比例的合成数据都导致 collapse\\n      - 更大模型可放大 collapse\\n      - 神经缩放定律在合成数据下失效\\n    vs_ours: >\\n      理论基础——解释了为什么需要监控（即使少量合成数据也危险）。\\n      他们的 fraction 实验与我们的实验设计直接相关。\\n\\n  - id: gerstgrasser_2024\\n    title: \\\"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\\\"\\n    authors: [Matthias Gerstgrasser, Rylan Schaeffer et al.]\\n    year: 2024\\n    venue: arXiv (2404.01413)\\n    relation: complementary\\n    core_method: >\\n      证明数据累积（而非替换）可避免 model collapse。\\n      替换导致 test error 增长，累积则有有限上界。\\n    signals: [test error over iterations]\\n    scale: model-level\\n    key_findings:\\n      - 累积真实+合成数据则无 collapse（所有模型/模态）\\n      - 替换数据则 collapse\\n      - 关键因素是数据管理策略\\n    vs_ours: >\\n      互补——他们研究何时 collapse（数据管理策略），\\n      我们研究如何实时检测 collapse（训练动态信号）。\\n\\n  - id: kazdan_2024\\n    title: \\\"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\\\"\\n    authors: [Joshua Kazdan et al.]\\n    year: 2024\\n    venue: arXiv (2410.16713)\\n    relation: complementary\\n    core_method: >\\n      系统比较三种训练工作流：replace（collapse）、\\n      accumulate（稳定）、fixed compute（介于两者之间）。\\n    signals: [test loss on real data]\\n    scale: model-level\\n    key_findings:\\n      - Replace 工作流一定 collapse\\n      - Accumulate 工作流保持稳定\\n      - Fixed compute 工作流 loss 升高但 plateau\\n    vs_ours: 互补——提供实验设计参考（不同工作流下 collapse 行为差异）。\\n\\n  - id: seddik_2024\\n    title: \\\"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\\\"\\n    authors: [Mohamed El Amine Seddik et al.]\\n    year: 2024\\n    venue: arXiv (2404.05090)\\n    relation: complementary\\n    core_method: >\\n      统计模型严格刻画不同递归训练场景下的 collapse 程度。\\n      给出混合真实/合成数据时避免 collapse 的最大合成数据比例估计。\\n    signals: [distribution tail, statistical divergence]\\n    scale: model-level\\n    key_findings:\\n      - 纯合成数据训练无法避免 collapse\\n      - 混合训练下存在可计算的合成数据上限\\n      - 分布尾部消失是 collapse 的统计特征\\n    vs_ours: 理论互补——给出合成数据比例的安全阈值。\\n\\n  - id: schaeffer_2025\\n    title: \\\"Position: Model Collapse Does Not Mean What You Think\\\"\\n    authors: [Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, Sanmi Koyejo]\\n    year: 2025\\n    venue: arXiv (2503.03150)\\n    relation: complementary\\n    core_method: >\\n      梳理 model collapse 文献中 8 种不同定义，\\n      分为三个家族：test loss 行为、分布形变、缩放行为。\\n    signals: N/A (position paper)\\n    scale: N/A\\n    key_findings:\\n      - Model collapse 有 8 种不完全一致的定义\\n      - 三个家族：test loss 行为、分布形变、缩放定律\\n      - 术语混乱阻碍了系统性理解\\n    vs_ours: >\\n      重要定位参考——论文中需明确使用哪种 collapse 定义。\\n      建议采用他们的分类框架。\\n\\n  - id: feng_iclr2025\\n    title: \\\"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification\\\"\\n    authors: [Feng et al.]\\n    year: 2025\\n    venue: ICLR 2025\\n    relation: complementary\\n    core_method: >\\n      用高斯混合+线性分类器+线性验证器推导验证器有效的条件。\\n      证明不完美验证器也可有效筛选合成数据。\\n    signals: [verifier-based quality score]\\n    scale: model-level\\n    key_findings:\\n      - 验证器筛选合成数据可达到最优性能\\n      - 即使不完美验证器也有效\\n      - 给出可衡量的代理条件\\n    vs_ours: 互补——缓解策略。我们的监控信号可作为验证器的补充。\\n\\n  - id: yi_2025\\n    title: \\\"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence\\\"\\n    authors: [Bingji Yi, Qiyuan Liu, Yuwei Cheng, Haifeng Xu]\\n    year: 2025\\n    venue: arXiv (2510.16657)\\n    relation: complementary\\n    core_method: >\\n      证明外部验证器（人类或更强模型）可阻止 collapse。\\n      分析验证器引导下的短期改进和长期收敛行为。\\n    signals: [verifier quality score]\\n    scale: model-level\\n    key_findings:\\n      - 外部验证器注入信息则不会 collapse\\n      - 短期有改进，长期收敛到验证器的知识中心\\n    vs_ours: 互补——缓解策略方向，与监控方向正交。\\n\\n  - id: bakshi_2026\\n    title: \\\"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\\\"\\n    authors: [Soham Bakshi et al.]\\n    year: 2026\\n    venue: arXiv (2602.10531)\\n    relation: complementary\\n    core_method: >\\n      分析在真实+合成混合数据上的迭代训练动态。\\n      next-token prediction 模型下的长期演化分析。\\n    signals: [mixture weight, sample size, test performance]\\n    scale: model-level\\n    key_findings:\\n      - 非零真实数据混合权重（即使递减）可避免 collapse\\n      - 混合权重和样本量共同控制长期性能\\n    vs_ours: 理论互补——刻画迭代训练的长期演化。\\n\\n  - id: briesch_2023\\n    title: \\\"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\\\"\\n    authors: [Martin Briesch, Dominik Sobania, Franz Rothlauf]\\n    year: 2023\\n    venue: arXiv (2311.16822)\\n    relation: complementary\\n    core_method: >\\n      首次针对 LLM 研究 self-consuming training loop，\\n      用逻辑表达式构造可验证的生成内容，分析不同合成数据比例下输出多样性下降。\\n    signals: [output diversity, correctness rate]\\n    scale: model-level\\n    key_findings:\\n      - Self-consuming loop 产生正确输出，但多样性随合成数据比例下降\\n      - 首批 LLM self-consuming loop 实证研究之一\\n      - 提出基于逻辑表达式的内容验证方法\\n    vs_ours: >\\n      早期 LLM self-consuming loop 实证研究。\\n      他们用输出级多样性指标，我们用训练动态内部信号；互为补充。\\n\\n  - id: dohmatob_icml2024\\n    title: \\\"A Tale of Tails: Model Collapse as a Change of Scaling Laws\\\"\\n    authors: [Elvis Dohmatob, Yunzhen Feng, Pu Yang, Francois Charton, Julia Kempe]\\n    year: 2024\\n    venue: ICML 2024 (pp. 11165-11197)\\n    relation: complementary\\n    core_method: >\\n      从 scaling law 视角分析 collapse——理论框架揭示 collapse 导致 scaling law 改变。\\n    signals: [test loss scaling, skill metrics]\\n    scale: model-level\\n    key_findings:\\n      - Loss of scaling、shifted scaling with number of generations\\n      - Skill un-learning 现象\\n      - 混合人类/合成数据时的 grokking 效应\\n    vs_ours: >\\n      理论背景——从 scaling law 角度量化 collapse 严重度。\\n      我们用训练动态信号在训练中追踪，他们用事后 scaling 分析。\\n\\n  - id: fu_icml2024\\n    title: \\\"Towards Theoretical Understandings of Self-Consuming Generative Models\\\"\\n    authors: [Shi Fu, Sen Zhang, Yingjie Wang, Xinmei Tian, Dacheng Tao]\\n    year: 2024\\n    venue: ICML 2024\\n    relation: complementary\\n    core_method: >\\n      构建严格理论框架分析 self-consuming loop 中数据分布演化。\\n      分析参数和非参数模型中三种误差源的复合效应。\\n    signals: [distribution divergence, error accumulation]\\n    scale: model-level\\n    key_findings:\\n      - 统计/表达/近似三种误差在迭代中复合\\n      - 给出误差增长的理论界\\n    vs_ours: 理论互补——严格刻画 collapse 的误差复合机制。\\n\\n  - id: gillman_icml2024\\n    title: \\\"Self-Correcting Self-Consuming Loops for Generative Model Training\\\"\\n    authors: [Nate Gillman, Michael Freeman, Daksh Aggarwal, Chia-Hong Hsu, Calvin Luo, Yonglong Tian, Chen Sun]\\n    year: 2024\\n    venue: ICML 2024\\n    relation: complementary\\n    core_method: >\\n      引入 correction function 使 self-consuming loop 指数级更稳定。\\n      在人体运动合成任务上验证。\\n    signals: [corrector quality, loop stability]\\n    scale: model-level\\n    key_findings:\\n      - Correction function 使 loop 指数级稳定\\n      - 即使 synthetic:real = 100:1 也可避免 collapse\\n    vs_ours: 互补——缓解策略，correction function 概念与在线监控互补。\\n\\n  - id: pennington_nips2017\\n    title: \\\"Nonlinear Random Matrix Theory for Deep Learning\\\"\\n    authors: [Jeffrey Pennington, Pratik Worah]\\n    year: 2017\\n    venue: NeurIPS 2017\\n    relation: foundation\\n    core_method: >\\n      将神经网络中的逐点非线性纳入随机矩阵理论的矩方法框架，\\n      推导数据协方差矩阵在网络层间传播的渐近谱分布。\\n    signals: [eigenvalue distribution, spectral density]\\n    scale: layer-level (weight/covariance matrices)\\n    key_findings:\\n      - 非线性激活函数可纳入 RMT 矩方法\\n      - 推导单层随机特征方法在记忆任务上的渐近性能\\n      - 分析数据协方差矩阵在网络中传播时的特征值演化\\n    vs_ours: >\\n      RMT 在深度学习中的理论基础。我们的谱分析方法论（spectral entropy、\\n      stable rank）建立在此类随机矩阵理论之上。\\n\\n  # ===================== DATA CONTAMINATION DETECTION =====================\\n\\n  - id: kirchenbauer_icml2023\\n    title: \\\"A Watermark for Large Language Models\\\"\\n    authors: [John Kirchenbauer, Jonas Geiping, Yuxin Wen, Jonathan Katz, Ian Miers, Tom Goldstein]\\n    year: 2023\\n    venue: ICML 2023 (pp. 17061-17084)\\n    relation: complementary\\n    core_method: >\\n      LLM 文本水印框架——green/red token list + soft promotion + 统计检测。\\n    signals: [green token ratio, z-score]\\n    scale: token-level (output)\\n    key_findings:\\n      - 可嵌入统计可检测水印且不影响文本质量\\n      - 开源检测算法不需模型访问\\n    vs_ours: 合成数据溯源的基础方法，与 collapse 检测互补。\\n\\n  - id: dathathri_nature2024\\n    title: \\\"Scalable Watermarking for Identifying Large Language Model Outputs\\\"\\n    authors: [Sumanth Dathathri, Abigail See, Sumedh Ghaisas et al.]\\n    year: 2024\\n    venue: Nature 634, 818-823\\n    relation: complementary\\n    core_method: >\\n      SynthID-Text：产品级文本水印，与 speculative sampling 集成。\\n      在 Gemini ~20M 响应上验证。\\n    signals: [watermark detection score]\\n    scale: token-level (output)\\n    key_findings:\\n      - 产品级规模的水印部署\\n      - 不影响文本质量，最小延迟开销\\n    vs_ours: 大规模合成数据标记的工业实践，与监控方向互补。\\n\\n  - id: sander_neurips2024\\n    title: \\\"Watermarking Makes Language Models Radioactive\\\"\\n    authors: [Tom Sander, Pierre Fernandez, Alain Durmus, Matthijs Douze, Teddy Furon]\\n    year: 2024\\n    venue: NeurIPS 2024\\n    relation: related\\n    core_method: >\\n      证明在水印 LLM 输出上微调的模型保留水印残留（\\\"放射性\\\"）。\\n    signals: [watermark residual in fine-tuned model]\\n    scale: model-level\\n    key_findings:\\n      - 水印信号通过训练传播到下游模型\\n      - 可检测模型是否在合成数据上训练\\n    vs_ours: >\\n      直接相关——检测合成数据训练的替代方法。\\n      他们检测\\\"是否用了合成数据\\\"，我们监控\\\"合成数据造成多严重的 collapse\\\"。\\n\\n  - id: mitchell_icml2023\\n    title: \\\"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\\\"\\n    authors: [Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn]\\n    year: 2023\\n    venue: ICML 2023 (pp. 24950-24962)\\n    relation: complementary\\n    core_method: >\\n      LLM 生成文本占据 log-probability 负曲率区域，据此零样本检测。\\n    signals: [log probability curvature]\\n    scale: text-level\\n    key_findings:\\n      - 生成文本的概率曲率特征可区分人类/机器文本\\n      - 0.95 AUROC 检测 GPT-NeoX 20B 生成的假新闻\\n    vs_ours: 合成文本检测方法，可识别训练数据中的合成成分。\\n\\n  - id: shi_iclr2024\\n    title: \\\"Detecting Pretraining Data from Large Language Models\\\"\\n    authors: [Weijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, Luke Zettlemoyer]\\n    year: 2024\\n    venue: ICLR 2024\\n    relation: related\\n    core_method: >\\n      Min-K% Prob：未见样本含低概率 outlier word，据此检测预训练数据成员。\\n    signals: [Min-K% probability score]\\n    scale: text-level\\n    key_findings:\\n      - 比 reference model 方法提升 7.4%\\n      - 适用于版权检测、污染检测、隐私审计\\n    vs_ours: 数据污染检测工具——可检测合成数据是否混入训练集，与 collapse 监控互补。\\n\\n  # ===================== METHODOLOGICAL FOUNDATIONS =====================\\n\\n  - id: martin_mahoney_2021\\n    title: \\\"Predicting Trends in the Quality of State-of-the-Art Neural Networks without Access to Training or Testing Data\\\"\\n    authors: [Charles H. Martin, Michael W. Mahoney]\\n    year: 2021\\n    venue: Nature Communications 12\\n    relation: complementary\\n    core_method: >\\n      WeightWatcher 工具——用 RMT 分析权重矩阵的谱性质，\\n      无需训练/测试数据即可预测模型质量。\\n    signals: [stable rank, power law exponent (alpha), spectral norm]\\n    scale: layer-level (per weight matrix)\\n    key_findings:\\n      - stable rank 追踪自正则化程度\\n      - 5+1 训练阶段对应不同的谱形态\\n      - heavy-tailed 分布特征区分好/差模型\\n    vs_ours: >\\n      方法论基础——WeightWatcher 的 stable rank 和谱分析方法\\n      直接启发我们的信号设计。\\n\\n  - id: yunis_2024\\n    title: \\\"Approaching Deep Learning through the Spectral Dynamics of Weights\\\"\\n    authors: [David Yunis, Kumar Kshitij Patel et al.]\\n    year: 2024\\n    venue: arXiv (2408.11804)\\n    relation: complementary\\n    core_method: >\\n      以权重奇异值/向量的动态演化为核心视角理解深度学习。\\n      证明谱动态可区分记忆网络和泛化网络。\\n    signals: [singular value dynamics, singular vector alignment]\\n    scale: layer-level (per weight matrix)\\n    key_findings:\\n      - 权重衰减增强低秩偏置\\n      - 谱动态区分记忆 vs 泛化\\n      - 与 lottery ticket 和 loss surface 结构相关\\n    vs_ours: 方法论基础——谱动态视角可用于理解 collapse 过程中的权重变化。\\n\\n  - id: chen_liu_2024\\n    title: \\\"Assessing Neural Network Representations During Training Using Noise-Resilient Diffusion Spectral Entropy\\\"\\n    authors: [Chen Liu et al.]\\n    year: 2024\\n    venue: IEEE CISS 2024\\n    relation: complementary\\n    core_method: >\\n      提出 Diffusion Spectral Entropy (DSE) 和 Diffusion Spectral Mutual Information (DSMI)，\\n      利用数据几何在高维中可靠计算信息论指标。\\n    signals: [DSE, DSMI]\\n    scale: layer-level (representations)\\n    key_findings:\\n      - DSE 在训练中增加\\n      - DSMI(class label) 在泛化学习中增加，过拟合时停滞\\n      - 可用于指导网络初始化和预测下游准确率\\n    vs_ours: >\\n      方法论工具——DSE 是我们 spectral entropy 信号的潜在替代实现。\\n\\n  - id: lu_neurips2024\\n    title: \\\"AlphaPruning: Using Heavy-Tailed Self Regularization Theory for Improved Layer-wise Pruning of Large Language Models\\\"\\n    authors: [Haiquan Lu, Yefan Zhou, Shiwei Liu, Zhangyang Wang, Michael W. Mahoney, Yaoqing Yang]\\n    year: 2024\\n    venue: NeurIPS 2024\\n    relation: complementary\\n    core_method: >\\n      用 HT-SR 理论的谱密度形态（alpha exponent）指导 LLM 层级剪枝。\\n    signals: [alpha exponent, ESD shape metrics]\\n    scale: layer-level\\n    key_findings:\\n      - Alpha exponent 有效指导 per-layer 剪枝比例\\n      - LLaMA-7B 可剪至 80% sparsity 保持合理 perplexity\\n    vs_ours: >\\n      验证 per-layer 谱分析对 LLM 质量评估的有效性。\\n      支持我们用类似方法监控 collapse。\\n\\n  - id: sanyal_iclr2020\\n    title: \\\"Stable Rank Normalization for Improved Generalization in Neural Networks and GANs\\\"\\n    authors: [Amartya Sanyal, Philip H. S. Torr, Puneet K. Dokania]\\n    year: 2020\\n    venue: ICLR 2020\\n    relation: complementary\\n    core_method: >\\n      提出 stable rank normalization——最小化线性算子的 stable rank。\\n      理论证明唯一最优解，实验验证改善泛化。\\n    signals: [stable rank, Lipschitz constant]\\n    scale: layer-level\\n    key_findings:\\n      - 控制 stable rank 改善泛化 gap 11.3%\\n      - Stable rank 与泛化能力直接关联\\n    vs_ours: >\\n      理论支持——建立 stable rank 与泛化的直接联系。\\n      支持我们选用 stable rank 作为 collapse（泛化退化）的监控信号。\\n\\n  - id: kalra_2026\\n    title: \\\"A Scalable Measure of Loss Landscape Curvature for Analyzing the Training Dynamics of LLMs\\\"\\n    authors: [Dayal Singh Kalra, Jean-Christophe Gagnon-Audet, Andrey Gromov, Ishita Mediratta, Kelvin Niu, Alexander H. Miller, Michael Shvartsman]\\n    year: 2026\\n    venue: arXiv (2601.16979)\\n    relation: related\\n    core_method: >\\n      Critical sharpness：<10 forward passes 高效度量 loss landscape 曲率。\\n      首次在 7B 规模验证 progressive sharpening 和 Edge of Stability。\\n    signals: [critical sharpness, relative critical sharpness]\\n    scale: model-level\\n    key_findings:\\n      - Progressive sharpening 在 7B 规模仍然存在\\n      - Critical sharpness 可指导 pre-train 到 fine-tune 的数据混合\\n    vs_ours: >\\n      训练动态监控方法论参考——高效的大规模 LLM 训练动态度量。\\n      Critical sharpness 可作为我们信号集的潜在补充。\\n\\n  # ===================== DATA QUALITY =====================\\n\\n  - id: penedo_2024\\n    title: \\\"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale\\\"\\n    authors: [Guilherme Penedo, Hynek Kydlicek, Loubna Ben allal, Anton Lozhkov, Margaret Mitchell, Colin Raffel, Leandro Von Werra, Thomas Wolf]\\n    year: 2024\\n    venue: arXiv (2406.17557)\\n    relation: complementary\\n    core_method: >\\n      15T token 数据集的完整策略文档——去重、过滤、教育文本提取。\\n    signals: [data quality classifiers, deduplication metrics]\\n    scale: dataset-level\\n    key_findings:\\n      - 详细 ablation 各种去重和过滤策略\\n      - FineWeb-Edu 在知识密集任务上大幅提升性能\\n    vs_ours: 数据质量策略参考——理解高质量训练数据标准，为分析 collapse 的数据原因提供基线。\\n\\n  - id: zhang_2026\\n    title: \\\"The LLM Data Auditor: A Metric-oriented Survey on Quality and Trustworthiness in Evaluating Synthetic Data\\\"\\n    authors: [Kaituo Zhang, Mingzhi Hu, Hoang Anh Duy Le et al.]\\n    year: 2026\\n    venue: arXiv (2601.17717)\\n    relation: complementary\\n    core_method: >\\n      系统分类合成数据评估指标——quality (validity/fidelity/utility) +\\n      trustworthiness (safety/faithfulness)。\\n    signals: [quality metrics taxonomy, trustworthiness metrics]\\n    scale: dataset-level\\n    key_findings:\\n      - 从内在属性评估合成数据，而非仅看下游性能\\n      - 质量和可信度两个维度的完整分类体系\\n    vs_ours: 合成数据质量评估框架——为理解 collapse 的数据级原因提供指标体系。\\n\\n# ============================================================\\n# 关键发现总结\\n# ============================================================\\n\\nsummary:\\n  total_papers: 37\\n  direct_competitors: 2  # SIGMA, Kalinowski\\n  novelty_confirmation: >\\n    在 34 篇文献中，没有工作同时做到：(a) 训练中在线监控 (b) 用频谱/熵训练动态信号\\n    (c) per-layer 粒度 (d) 在迭代合成数据训练场景下验证。\\n    我们的核心新颖性空间依然存在。\\n\\n  coverage:\\n    model_collapse_theory: 16  # shumailov, dohmatob x2, alemohammad, fu, gerstgrasser, seddik, kazdan, schaeffer, bakshi, shi_neurips2025, feng, yi, gillman, briesch, hataya\\n    data_contamination: 5  # kirchenbauer, dathathri, sander, mitchell, shi_iclr2024\\n    spectral_methods: 9  # sigma, martin_mahoney, yunis, lu, sanyal, spectral_lens, xu, conzelmann, pennington\\n    training_dynamics: 4  # kalinowski, chen_liu, kalra, papyan\\n    data_quality: 3  # wyss, penedo, zhang\\n\\n  gap_analysis:\\n    sigma: >\\n      用输出嵌入 Gram 矩阵谱——事后/黑盒，不做 per-layer，不跟踪训练过程。\\n    kalinowski: >\\n      用拓扑信号——在线但信号族不同，不研究迭代合成数据场景。\\n    our_unique_position: >\\n      训练动态频谱/熵信号 + per-layer 粒度 + 迭代合成数据场景 = 独特定位。\\n\\n  per_layer_collapse_analysis:\\n    papers_with_per_layer:\\n      - layer_collapse_diffusion_2026  # diffusion LM per-layer activation collapse\\n      - xu_2026  # stable rank per-layer（compression 场景）\\n      - spectral_lens_2026  # per-layer activation/gradient 谱\\n      - lu_neurips2024  # alpha exponent per-layer for pruning\\n    gap: \\\"无论文在迭代合成数据训练中做 per-layer collapse 分析\\\"\\n\\n  stable_rank_as_collapse_signal:\\n    papers_using_stable_rank:\\n      - martin_mahoney_2021  # WeightWatcher 中作为模型质量指标\\n      - xu_2026  # 压缩退化预测器 (r=0.89)\\n      - yunis_2024  # 谱动态中的低秩偏置\\n      - sanyal_iclr2020  # stable rank 与泛化的直接联系\\n    gap: \\\"无论文直接用 stable rank 监控 iterative synthetic data collapse\\\"\\n\\n  spectral_entropy_as_collapse_signal:\\n    papers_using_spectral_entropy:\\n      - chen_liu_2024  # DSE 跟踪训练动态\\n      - sigma_2026  # 谱分析但在 Gram 矩阵上\\n    gap: \\\"无论文直接用 weight spectral entropy 监控 collapse\\\"\\n\\n  synthetic_fraction_effects:\\n    papers_studying_fraction:\\n      - dohmatob_iclr2025  # 理论：任何非零 fraction 都危险\\n      - dohmatob_icml2024  # scaling law 角度的 fraction 分析\\n      - alemohammad_iclr2024  # 三种 loop 类型的不同效果\\n      - wyss_2024  # 实证：25%/50%/75% 不同 collapse 程度\\n      - seddik_2024  # 统计：给出安全上限估计\\n    gap: \\\"大量理论/实证工作，但都用事后指标衡量 fraction 效果\\\"\\n\\n  data_contamination_detection:\\n    papers:\\n      - kirchenbauer_icml2023  # 基础水印方法\\n      - dathathri_nature2024  # 产品级水印 (SynthID)\\n      - sander_neurips2024  # 水印放射性传播\\n      - mitchell_icml2023  # DetectGPT 概率曲率检测\\n      - shi_iclr2024  # Min-K% 预训练数据检测\\n    relevance: >\\n      合成数据检测与 collapse 监控互补：他们回答\\\"是否有合成数据\\\"，\\n      我们回答\\\"合成数据造成了多严重的 collapse\\\"。\\n\", \"total_chars\": 26925, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0fa4026-70b3-4120-bb47-a2d38fa80c66",
  "isSidechain": false,
  "promptId": "a7003b6e-3a25-4888-837a-59f1925bbd90",
  "type": "user",
  "uuid": "57e3fa9f-8624-4659-b88a-7ff1df474464",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/literature_map.yaml\\\", \\\"content\\\": \\\"# Literature Map — collapse_severity_monitor\\\\n# 最后更新: 2026-05-14 (expanded to 37 papers)\\\\n# 研究方向: 在线监控模型 collapse 严重度——用训练动态信号实时跟踪迭代合成数据训练中的质量退化\\\\n\\\\n# ============================================================\\\\n# 竞争关系分类说明:\\\\n#   direct_competitor  — 解决同一问题（在线监控 collapse）\\\\n#   related            — 解决相近问题或使用相关方法\\\\n#   complementary      — 互补（提供理论基础/工具/缓解策略）\\\\n#   foundation         — 领域基础工作\\\\n# ============================================================\\\\n\\\\npapers:\\\\n\\\\n  # ===================== DIRECT COMPETITORS =====================\\\\n\\\\n  - id: sigma_2026\\\\n    title: \\\\\\\"SIGMA: Scalable Spectral Insights for LLM Model Collapse\\\\\\\"\\\\n    authors: [Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, Alexander Aue]\\\\n    year: 2026\\\\n    venue: arXiv (2601.03385)\\\\n    relation: direct_competitor\\\\n    core_method: >\\\\n      通过 embedding Gram 矩阵的谱分析来量化 model collapse 程度。\\\\n      推导 Gram 矩阵谱的确定性和随机性界，用谱收缩作为 collapse 指标。\\\\n    signals: [Gram matrix spectrum, rank deficiency, spectral bounds]\\\\n    scale: model-level (output embeddings)\\\\n    key_findings:\\\\n      - Gram 矩阵满秩是 LLM 正常运作的必要条件\\\\n      - 秩亏缺意味着语义级信息丢失，标志 collapse 开始\\\\n      - 随机公式使框架可扩展至大规模模型\\\\n    vs_ours: >\\\\n      SIGMA 用输出嵌入的 Gram 矩阵谱，是事后/黑盒方法，不需要模型权重。\\\\n      我们用训练动态信号（权重频谱熵、stable rank、token entropy），\\\\n      是训练中实时监控，更早期更细粒度（per-layer）。\\\\n      SIGMA 不做 per-layer 分析，不跟踪训练过程的动态变化。\\\\n    threat_level: medium\\\\n\\\\n  - id: kalinowski_2026\\\\n    title: \\\\\\\"Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index\\\\\\\"\\\\n    authors: [Alexander Kalinowski]\\\\n    year: 2026\\\\n    venue: arXiv (2604.26984)\\\\n    relation: direct_competitor\\\\n    core_method: >\\\\n      提出在线拓扑感知监控器，结合 Modular Morse Homology Maintenance (MMHM)\\\\n      和复合 Collapse Index (CI)，通过稀疏增量更新实现快速在线监控。\\\\n    signals: [persistent homology, Collapse Index (CI), topological features]\\\\n    scale: model-level (representation space topology)\\\\n    key_findings:\\\\n      - CI 在 LLM fine-tuning 和时序 KGE 训练中提供低延迟早期预警\\\\n      - 表征各向异性和多尺度结构丧失在性能指标反应之前就可检测\\\\n      - 增量更新避免每个 epoch 重建复形\\\\n    vs_ours: >\\\\n      Kalinowski 用拓扑信号（persistent homology），我们用频谱/熵信号。\\\\n      两者都是在线监控，但信号族完全不同。我们的信号更轻量、\\\\n      更可解释（stable rank/spectral entropy 有直接的线性代数含义）。\\\\n      Kalinowski 不研究迭代合成数据训练场景。\\\\n    threat_level: medium\\\\n\\\\n  # ===================== CLOSELY RELATED =====================\\\\n\\\\n  - id: spectral_lens_2026\\\\n    title: \\\\\\\"Spectral Lens: Activation and Gradient Spectra as Diagnostics of LLM Optimization\\\\\\\"\\\\n    authors: [Andy Zeyi Liu et al.]\\\\n    year: 2026\\\\n    venue: arXiv (2605.05683)\\\\n    relation: related\\\\n    core_method: >\\\\n      用 activation covariance 和 per-sample gradient 的 SVD 谱\\\\n      作为 LLM 训练优化的诊断工具。\\\\n    signals: [activation covariance spectrum, gradient SVD spectrum]\\\\n    scale: layer-level\\\\n    key_findings:\\\\n      - batch size 是表示几何的隐藏决定因素\\\\n      - 早期训练的 activation covariance 尾部可预测下游 token 效率\\\\n      - activation 谱头部运动 + gradient 谱可区分学习侧和执行侧改进\\\\n    vs_ours: >\\\\n      方法论高度相关——同样用频谱分析训练动态。\\\\n      但他们关注优化诊断，不研究 collapse/合成数据退化。\\\\n      可作为方法论参考。\\\\n    threat_level: low\\\\n\\\\n  - id: shi_neurips2025\\\\n    title: \\\\\\\"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\\\\\\\"\\\\n    authors: [Lianghe Shi, Meng Wu, Huijie Zhang, Zekai Zhang, Molei Tao, Qing Qu]\\\\n    year: 2025\\\\n    venue: NeurIPS 2025 (Spotlight)\\\\n    relation: related\\\\n    core_method: >\\\\n      揭示 model collapse 中从泛化到记忆的转变。\\\\n      发现训练数据熵与模型泛化能力的强线性相关。\\\\n      提出基于熵的子集选择方法来减缓 collapse。\\\\n    signals: [dataset entropy, generalization metrics]\\\\n    scale: model-level (data distribution)\\\\n    key_findings:\\\\n      - 迭代训练中数据分布熵急剧下降导致泛化能力下降\\\\n      - 强线性相关：训练数据集熵与模型泛化能力\\\\n      - 熵选择方法有效减缓泛化到记忆转变\\\\n    vs_ours: >\\\\n      他们用数据级别的熵，我们用模型内部的训练动态信号。\\\\n      互补：他们的数据熵可作为我们的外部验证指标。\\\\n      他们不做 per-layer 分析，不做在线监控。\\\\n    threat_level: low\\\\n\\\\n  - id: wyss_2024\\\\n    title: \\\\\\\"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI\\\\\\\"\\\\n    authors: [C. M. Wyss et al.]\\\\n    year: 2024\\\\n    venue: arXiv (2410.12341)\\\\n    relation: related\\\\n    core_method: >\\\\n      用语义网络和 next-token 概率来表征 LLM 中的 model collapse。\\\\n      引入 collapsed prediction 概念量化多样性损失。\\\\n      分析不同合成 token 比例 (25%/50%/75%) 对 collapse 的影响。\\\\n    signals: [next-token probability distribution, semantic network metrics, collapsed prediction ratio]\\\\n    scale: token-level (output)\\\\n    key_findings:\\\\n      - Next-token 概率分布可精确量化多样性损失\\\\n      - 合成 token 比例越高，collapse 越严重\\\\n      - 跨数据集迁移：在非微调数据集上 collapse 程度不同\\\\n    vs_ours: >\\\\n      他们用输出级指标（next-token prob），我们用训练动态内部信号。\\\\n      他们的 synthetic fraction 实验与我们的实验设计有重叠。\\\\n      不同之处：他们是事后分析，我们是训练中在线监控。\\\\n    threat_level: low\\\\n\\\\n  - id: xu_2026\\\\n    title: \\\\\\\"Predicting LLM Compression Degradation from Spectral Statistics\\\\\\\"\\\\n    authors: [Mingxue Xu]\\\\n    year: 2026\\\\n    venue: arXiv (2604.18085)\\\\n    relation: related\\\\n    core_method: >\\\\n      用 stable rank 和信息密度 (bits/param) 预测 LLM 压缩导致的退化。\\\\n      交互项 compression_ratio * stable_rank 是退化的强预测器。\\\\n    signals: [stable rank, information density, compression ratio]\\\\n    scale: layer-level (attention vs MLP 分开分析)\\\\n    key_findings:\\\\n      - stable rank 是压缩退化的主要预测因子（Pearson r=0.890 attention, 0.839 MLP）\\\\n      - 层类型比压缩方法更重要\\\\n      - layer-specific calibration 优于 method-specific tuning\\\\n    vs_ours: >\\\\n      直接验证 stable rank 作为退化预测信号的有效性。\\\\n      虽然场景不同（压缩 vs collapse），但支持我们选用 stable rank 的合理性。\\\\n      他们的 per-layer 分析方法可参考。\\\\n    threat_level: low\\\\n\\\\n  - id: layer_collapse_diffusion_2026\\\\n    title: \\\\\\\"Layer Collapse in Diffusion Language Models\\\\\\\"\\\\n    authors: [Alexander Conzelmann, Albert Catalan-Tatjer, Shiwei Liu]\\\\n    year: 2026\\\\n    venue: arXiv (2605.06366)\\\\n    relation: related\\\\n    core_method: >\\\\n      分析 diffusion language model (LLaDA-8B) 中的 per-layer activation 动态，\\\\n      发现少数早期层展现 collapsed activation patterns。\\\\n    signals: [activation patterns, super-outlier magnitude]\\\\n    scale: layer-level\\\\n    key_findings:\\\\n      - 几个早期层出现 channel-axis collapse（单一维度主导所有位置）\\\\n      - 尽管看似冗余，pruning outlier 导致退化为重复随机 token 循环\\\\n      - Diffusion LM 与 autoregressive LM 的 collapse 行为不同\\\\n    vs_ours: >\\\\n      做了 per-layer collapse 分析，但在 diffusion LM 上。\\\\n      方法论参考：per-layer activation 分析方法。\\\\n    threat_level: low\\\\n\\\\n  # ===================== FOUNDATION =====================\\\\n\\\\n  - id: alemohammad_iclr2024\\\\n    title: \\\\\\\"Self-Consuming Generative Models Go MAD\\\\\\\"\\\\n    authors: [Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard G. Baraniuk]\\\\n    year: 2024\\\\n    venue: ICLR 2024\\\\n    relation: foundation\\\\n    core_method: >\\\\n      定义三种 autophagous loop（fully synthetic / synthetic augmentation / fresh data），\\\\n      证明无足够真实数据时 precision 或 recall 必然下降（MAD 现象）。\\\\n    signals: [FID, precision, recall]\\\\n    scale: model-level (image generative models)\\\\n    key_findings:\\\\n      - 三种 loop 类型的 collapse 行为不同\\\\n      - 无 fresh data 时 quality 或 diversity 必然退化\\\\n      - 在 StyleGAN、DDPM、denoising diffusion 上验证\\\\n    vs_ours: >\\\\n      领域基础论文之一。他们的 loop 分类框架直接对应我们的实验设计。\\\\n      他们用 FID/precision/recall（事后指标），我们提供训练中在线信号。\\\\n\\\\n  - id: papyan_pnas2020\\\\n    title: \\\\\\\"Prevalence of Neural Collapse during the Terminal Phase of Deep Learning Training\\\\\\\"\\\\n    authors: [Vardan Papyan, X. Y. Han, David L. Donoho]\\\\n    year: 2020\\\\n    venue: PNAS 117(40), 24652-24663\\\\n    relation: foundation\\\\n    core_method: >\\\\n      发现分类网络训练末期的 Neural Collapse——类内表征收缩到 Simplex ETF。\\\\n    signals: [within-class variability, classifier-mean alignment]\\\\n    scale: model-level (last-layer representations)\\\\n    key_findings:\\\\n      - 训练末期出现四种 collapse 现象\\\\n      - 类均值收敛到 Simplex ETF 顶点\\\\n      - Collapse 与泛化能力相关\\\\n    vs_ours: >\\\\n      虽然 neural collapse 与 model collapse 是不同概念，\\\\n      但谱分析方法论可借鉴，且提供 \\\\\\\"collapse\\\\\\\" 概念的对比参考。\\\\n\\\\n  - id: hataya_iccv2023\\\\n    title: \\\\\\\"Will Large-scale Generative Models Corrupt Future Datasets?\\\\\\\"\\\\n    authors: [Ryuichiro Hataya, Han Bao, Hiromi Arai]\\\\n    year: 2023\\\\n    venue: ICCV 2023 (pp. 20555-20565)\\\\n    relation: foundation\\\\n    core_method: >\\\\n      用 SOTA 生成模型生成 ImageNet/COCO 规模数据集，\\\\n      评估\\\\\\\"被污染\\\\\\\"数据集在分类和生成任务上的下游性能退化。\\\\n    signals: [classification accuracy, FID, generation quality]\\\\n    scale: dataset-level (ImageNet/COCO scale)\\\\n    key_findings:\\\\n      - 生成图像对下游性能有负面影响\\\\n      - 影响程度取决于任务类型和生成图像比例\\\\n      - 首次在 ImageNet 规模验证数据集污染效应\\\\n    vs_ours: >\\\\n      早期数据集污染实证研究，在视觉领域验证了 collapse 前兆。\\\\n      他们关注下游任务性能，我们关注训练中的实时信号。\\\\n\\\\n  # ===================== COMPLEMENTARY (Theory/Mitigation) =====================\\\\n\\\\n  - id: shumailov_nature2024\\\\n    title: \\\\\\\"AI Models Collapse When Trained on Recursively Generated Data\\\\\\\"\\\\n    authors: [Ilia Shumailov et al.]\\\\n    year: 2024\\\\n    venue: Nature 631, 755-759\\\\n    relation: foundation\\\\n    core_method: >\\\\n      首次系统性证明迭代合成数据训练导致 model collapse。\\\\n      在 LLM、VAE、GMM 上验证。分布尾部消失是核心机制。\\\\n    signals: [test loss, distribution tail metrics]\\\\n    scale: model-level\\\\n    key_findings:\\\\n      - 迭代训练导致不可逆缺陷：分布尾部消失\\\\n      - 罕见事件最先遗忘\\\\n      - LLM、VAE、GMM 都有此现象\\\\n    vs_ours: >\\\\n      领域基石论文，建立了我们要解决的问题。\\\\n      他们用事后评估（test loss），我们提供在线监控手段。\\\\n\\\\n  - id: dohmatob_iclr2025\\\\n    title: \\\\\\\"Strong Model Collapse\\\\\\\"\\\\n    authors: [Elvis Dohmatob, Yunzhen Feng et al.]\\\\n    year: 2025\\\\n    venue: ICLR 2025 (Spotlight)\\\\n    relation: complementary\\\\n    core_method: >\\\\n      用算子值自由概率论证明即使极小比例的合成数据 (1/1000)\\\\n      也会导致 model collapse，且更大模型放大 collapse。\\\\n    signals: [test error on real data, bias-variance decomposition]\\\\n    scale: model-level\\\\n    key_findings:\\\\n      - 任何非零常数比例的合成数据都导致 collapse\\\\n      - 更大模型可放大 collapse\\\\n      - 神经缩放定律在合成数据下失效\\\\n    vs_ours: >\\\\n      理论基础——解释了为什么需要监控（即使少量合成数据也危险）。\\\\n      他们的 fraction 实验与我们的实验设计直接相关。\\\\n\\\\n  - id: gerstgrasser_2024\\\\n    title: \\\\\\\"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\\\\\\\"\\\\n    authors: [Matthias Gerstgrasser, Rylan Schaeffer et al.]\\\\n    year: 2024\\\\n    venue: arXiv (2404.01413)\\\\n    relation: complementary\\\\n    core_method: >\\\\n      证明数据累积（而非替换）可避免 model collapse。\\\\n      替换导致 test error 增长，累积则有有限上界。\\\\n    signals: [test error over iterations]\\\\n    scale: model-level\\\\n    key_findings:\\\\n      - 累积真实+合成数据则无 collapse（所有模型/模态）\\\\n      - 替换数据则 collapse\\\\n      - 关键因素是数据管理策略\\\\n    vs_ours: >\\\\n      互补——他们研究何时 collapse（数据管理策略），\\\\n      我们研究如何实时检测 collapse（训练动态信号）。\\\\n\\\\n  - id: kazdan_2024\\\\n    title: \\\\\\\"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\\\\\\\"\\\\n    authors: [Joshua Kazdan et al.]\\\\n    year: 2024\\\\n    venue: arXiv (2410.16713)\\\\n    relation: complementary\\\\n    core_method: >\\\\n      系统比较三种训练工作流：replace（collapse）、\\\\n      accumulate（稳定）、fixed compute（介于两者之间）。\\\\n    signals: [test loss on real data]\\\\n    scale: model-level\\\\n    key_findings:\\\\n      - Replace 工作流一定 collapse\\\\n      - Accumulate 工作流保持稳定\\\\n      - Fixed compute 工作流 loss 升高但 plateau\\\\n    vs_ours: 互补——提供实验设计参考（不同工作流下 collapse 行为差异）。\\\\n\\\\n  - id: seddik_2024\\\\n    title: \\\\\\\"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\\\\\\\"\\\\n    authors: [Mohamed El Amine Seddik et al.]\\\\n    year: 2024\\\\n    venue: arXiv (2404.05090)\\\\n    relation: complementary\\\\n    core_method: >\\\\n      统计模型严格刻画不同递归训练场景下的 collapse 程度。\\\\n      给出混合真实/合成数据时避免 collapse 的最大合成数据比例估计。\\\\n    signals: [distribution tail, statistical divergence]\\\\n    scale: model-level\\\\n    key_findings:\\\\n      - 纯合成数据训练无法避免 collapse\\\\n      - 混合训练下存在可计算的合成数据上限\\\\n      - 分布尾部消失是 collapse 的统计特征\\\\n    vs_ours: 理论互补——给出合成数据比例的安全阈值。\\\\n\\\\n  - id: schaeffer_2025\\\\n    title: \\\\\\\"Position: Model Collapse Does Not Mean What You Think\\\\\\\"\\\\n    authors: [Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, Sanmi Koyejo]\\\\n    year: 2025\\\\n    venue: arXiv (2503.03150)\\\\n    relation: complementary\\\\n    core_method: >\\\\n      梳理 model collapse 文献中 8 种不同定义，\\\\n      分为三个家族：test loss 行为、分布形变、缩放行为。\\\\n    signals: N/A (position paper)\\\\n    scale: N/A\\\\n    key_findings:\\\\n      - Model collapse 有 8 种不完全一致的定义\\\\n      - 三个家族：test loss 行为、分布形变、缩放定律\\\\n      - 术语混乱阻碍了系统性理解\\\\n    vs_ours: >\\\\n      重要定位参考——论文中需明确使用哪种 collapse 定义。\\\\n      建议采用他们的分类框架。\\\\n\\\\n  - id: feng_iclr2025\\\\n    title: \\\\\\\"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification\\\\\\\"\\\\n    authors: [Feng et al.]\\\\n    year: 2025\\\\n    venue: ICLR 2025\\\\n    relation: complementary\\\\n    core_method: >\\\\n      用高斯混合+线性分类器+线性验证器推导验证器有效的条件。\\\\n      证明不完美验证器也可有效筛选合成数据。\\\\n    signals: [verifier-based quality score]\\\\n    scale: model-level\\\\n    key_findings:\\\\n      - 验证器筛选合成数据可达到最优性能\\\\n      - 即使不完美验证器也有效\\\\n      - 给出可衡量的代理条件\\\\n    vs_ours: 互补——缓解策略。我们的监控信号可作为验证器的补充。\\\\n\\\\n  - id: yi_2025\\\\n    title: \\\\\\\"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence\\\\\\\"\\\\n    authors: [Bingji Yi, Qiyuan Liu, Yuwei Cheng, Haifeng Xu]\\\\n    year: 2025\\\\n    venue: arXiv (2510.16657)\\\\n    relation: complementary\\\\n    core_method: >\\\\n      证明外部验证器（人类或更强模型）可阻止 collapse。\\\\n      分析验证器引导下的短期改进和长期收敛行为。\\\\n    signals: [verifier quality score]\\\\n    scale: model-level\\\\n    key_findings:\\\\n      - 外部验证器注入信息则不会 collapse\\\\n      - 短期有改进，长期收敛到验证器的知识中心\\\\n    vs_ours: 互补——缓解策略方向，与监控方向正交。\\\\n\\\\n  - id: bakshi_2026\\\\n    title: \\\\\\\"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\\\\\\\"\\\\n    authors: [Soham Bakshi et al.]\\\\n    year: 2026\\\\n    venue: arXiv (2602.10531)\\\\n    relation: complementary\\\\n    core_method: >\\\\n      分析在真实+合成混合数据上的迭代训练动态。\\\\n      next-token prediction 模型下的长期演化分析。\\\\n    signals: [mixture weight, sample size, test performance]\\\\n    scale: model-level\\\\n    key_findings:\\\\n      - 非零真实数据混合权重（即使递减）可避免 collapse\\\\n      - 混合权重和样本量共同控制长期性能\\\\n    vs_ours: 理论互补——刻画迭代训练的长期演化。\\\\n\\\\n  - id: briesch_2023\\\\n    title: \\\\\\\"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\\\\\\\"\\\\n    authors: [Martin Briesch, Dominik Sobania, Franz Rothlauf]\\\\n    year: 2023\\\\n    venue: arXiv (2311.16822)\\\\n    relation: complementary\\\\n    core_method: >\\\\n      首次针对 LLM 研究 self-consuming training loop，\\\\n      用逻辑表达式构造可验证的生成内容，分析不同合成数据比例下输出多样性下降。\\\\n    signals: [output diversity, correctness rate]\\\\n    scale: model-level\\\\n    key_findings:\\\\n      - Self-consuming loop 产生正确输出，但多样性随合成数据比例下降\\\\n      - 首批 LLM self-consuming loop 实证研究之一\\\\n      - 提出基于逻辑表达式的内容验证方法\\\\n    vs_ours: >\\\\n      早期 LLM self-consuming loop 实证研究。\\\\n      他们用输出级多样性指标，我们用训练动态内部信号；互为补充。\\\\n\\\\n  - id: dohmatob_icml2024\\\\n    title: \\\\\\\"A Tale of Tails: Model Collapse as a Change of Scaling Laws\\\\\\\"\\\\n    authors: [Elvis Dohmatob, Yunzhen Feng, Pu Yang, Francois Charton, Julia Kempe]\\\\n    year: 2024\\\\n    venue: ICML 2024 (pp. 11165-11197)\\\\n    relation: complementary\\\\n    core_method: >\\\\n      从 scaling law 视角分析 collapse——理论框架揭示 collapse 导致 scaling law 改变。\\\\n    signals: [test loss scaling, skill metrics]\\\\n    scale: model-level\\\\n    key_findings:\\\\n      - Loss of scaling、shifted scaling with number of generations\\\\n      - Skill un-learning 现象\\\\n      - 混合人类/合成数据时的 grokking 效应\\\\n    vs_ours: >\\\\n      理论背景——从 scaling law 角度量化 collapse 严重度。\\\\n      我们用训练动态信号在训练中追踪，他们用事后 scaling 分析。\\\\n\\\\n  - id: fu_icml2024\\\\n    title: \\\\\\\"Towards Theoretical Understandings of Self-Consuming Generative Models\\\\\\\"\\\\n    authors: [Shi Fu, Sen Zhang, Yingjie Wang, Xinmei Tian, Dacheng Tao]\\\\n    year: 2024\\\\n    venue: ICML 2024\\\\n    relation: complementary\\\\n    core_method: >\\\\n      构建严格理论框架分析 self-consuming loop 中数据分布演化。\\\\n      分析参数和非参数模型中三种误差源的复合效应。\\\\n    signals: [distribution divergence, error accumulation]\\\\n    scale: model-level\\\\n    key_findings:\\\\n      - 统计/表达/近似三种误差在迭代中复合\\\\n      - 给出误差增长的理论界\\\\n    vs_ours: 理论互补——严格刻画 collapse 的误差复合机制。\\\\n\\\\n  - id: gillman_icml2024\\\\n    title: \\\\\\\"Self-Correcting Self-Consuming Loops for Generative Model Training\\\\\\\"\\\\n    authors: [Nate Gillman, Michael Freeman, Daksh Aggarwal, Chia-Hong Hsu, Calvin Luo, Yonglong Tian, Chen Sun]\\\\n    year: 2024\\\\n    venue: ICML 2024\\\\n    relation: complementary\\\\n    core_method: >\\\\n      引入 correction function 使 self-consuming loop 指数级更稳定。\\\\n      在人体运动合成任务上验证。\\\\n    signals: [corrector quality, loop stability]\\\\n    scale: model-level\\\\n    key_findings:\\\\n      - Correction function 使 loop 指数级稳定\\\\n      - 即使 synthetic:real = 100:1 也可避免 collapse\\\\n    vs_ours: 互补——缓解策略，correction function 概念与在线监控互补。\\\\n\\\\n  - id: pennington_nips2017\\\\n    title: \\\\\\\"Nonlinear Random Matrix Theory for Deep Learning\\\\\\\"\\\\n    authors: [Jeffrey Pennington, Pratik Worah]\\\\n    year: 2017\\\\n    venue: NeurIPS 2017\\\\n    relation: foundation\\\\n    core_method: >\\\\n      将神经网络中的逐点非线性纳入随机矩阵理论的矩方法框架，\\\\n      推导数据协方差矩阵在网络层间传播的渐近谱分布。\\\\n    signals: [eigenvalue distribution, spectral density]\\\\n    scale: layer-level (weight/covariance matrices)\\\\n    key_findings:\\\\n      - 非线性激活函数可纳入 RMT 矩方法\\\\n      - 推导单层随机特征方法在记忆任务上的渐近性能\\\\n      - 分析数据协方差矩阵在网络中传播时的特征值演化\\\\n    vs_ours: >\\\\n      RMT 在深度学习中的理论基础。我们的谱分析方法论（spectral entropy、\\\\n      stable rank）建立在此类随机矩阵理论之上。\\\\n\\\\n  # ===================== DATA CONTAMINATION DETECTION =====================\\\\n\\\\n  - id: kirchenbauer_icml2023\\\\n    title: \\\\\\\"A Watermark for Large Language Models\\\\\\\"\\\\n    authors: [John Kirchenbauer, Jonas Geiping, Yuxin Wen, Jonathan Katz, Ian Miers, Tom Goldstein]\\\\n    year: 2023\\\\n    venue: ICML 2023 (pp. 17061-17084)\\\\n    relation: complementary\\\\n    core_method: >\\\\n      LLM 文本水印框架——green/red token list + soft promotion + 统计检测。\\\\n    signals: [green token ratio, z-score]\\\\n    scale: token-level (output)\\\\n    key_findings:\\\\n      - 可嵌入统计可检测水印且不影响文本质量\\\\n      - 开源检测算法不需模型访问\\\\n    vs_ours: 合成数据溯源的基础方法，与 collapse 检测互补。\\\\n\\\\n  - id: dathathri_nature2024\\\\n    title: \\\\\\\"Scalable Watermarking for Identifying Large Language Model Outputs\\\\\\\"\\\\n    authors: [Sumanth Dathathri, Abigail See, Sumedh Ghaisas et al.]\\\\n    year: 2024\\\\n    venue: Nature 634, 818-823\\\\n    relation: complementary\\\\n    core_method: >\\\\n      SynthID-Text：产品级文本水印，与 speculative sampling 集成。\\\\n      在 Gemini ~20M 响应上验证。\\\\n    signals: [watermark detection score]\\\\n    scale: token-level (output)\\\\n    key_findings:\\\\n      - 产品级规模的水印部署\\\\n      - 不影响文本质量，最小延迟开销\\\\n    vs_ours: 大规模合成数据标记的工业实践，与监控方向互补。\\\\n\\\\n  - id: sander_neurips2024\\\\n    title: \\\\\\\"Watermarking Makes Language Models Radioactive\\\\\\\"\\\\n    authors: [Tom Sander, Pierre Fernandez, Alain Durmus, Matthijs Douze, Teddy Furon]\\\\n    year: 2024\\\\n    venue: NeurIPS 2024\\\\n    relation: related\\\\n    core_method: >\\\\n      证明在水印 LLM 输出上微调的模型保留水印残留（\\\\\\\"放射性\\\\\\\"）。\\\\n    signals: [watermark residual in fine-tuned model]\\\\n    scale: model-level\\\\n    key_findings:\\\\n      - 水印信号通过训练传播到下游模型\\\\n      - 可检测模型是否在合成数据上训练\\\\n    vs_ours: >\\\\n      直接相关——检测合成数据训练的替代方法。\\\\n      他们检测\\\\\\\"是否用了合成数据\\\\\\\"，我们监控\\\\\\\"合成数据造成多严重的 collapse\\\\\\\"。\\\\n\\\\n  - id: mitchell_icml2023\\\\n    title: \\\\\\\"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\\\\\\\"\\\\n    authors: [Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn]\\\\n    year: 2023\\\\n    venue: ICML 2023 (pp. 24950-24962)\\\\n    relation: complementary\\\\n    core_method: >\\\\n      LLM 生成文本占据 log-probability 负曲率区域，据此零样本检测。\\\\n    signals: [log probability curvature]\\\\n    scale: text-level\\\\n    key_findings:\\\\n      - 生成文本的概率曲率特征可区分人类/机器文本\\\\n      - 0.95 AUROC 检测 GPT-NeoX 20B 生成的假新闻\\\\n    vs_ours: 合成文本检测方法，可识别训练数据中的合成成分。\\\\n\\\\n  - id: shi_iclr2024\\\\n    title: \\\\\\\"Detecting Pretraining Data from Large Language Models\\\\\\\"\\\\n    authors: [Weijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, Luke Zettlemoyer]\\\\n    year: 2024\\\\n    venue: ICLR 2024\\\\n    relation: related\\\\n    core_method: >\\\\n      Min-K% Prob：未见样本含低概率 outlier word，据此检测预训练数据成员。\\\\n    signals: [Min-K% probability score]\\\\n    scale: text-level\\\\n    key_findings:\\\\n      - 比 reference model 方法提升 7.4%\\\\n      - 适用于版权检测、污染检测、隐私审计\\\\n    vs_ours: 数据污染检测工具——可检测合成数据是否混入训练集，与 collapse 监控互补。\\\\n\\\\n  # ===================== METHODOLOGICAL FOUNDATIONS =====================\\\\n\\\\n  - id: martin_mahoney_2021\\\\n    title: \\\\\\\"Predicting Trends in the Quality of State-of-the-Art Neural Networks without Access to Training or Testing Data\\\\\\\"\\\\n    authors: [Charles H. Martin, Michael W. Mahoney]\\\\n    year: 2021\\\\n    venue: Nature Communications 12\\\\n    relation: complementary\\\\n    core_method: >\\\\n      WeightWatcher 工具——用 RMT 分析权重矩阵的谱性质，\\\\n      无需训练/测试数据即可预测模型质量。\\\\n    signals: [stable rank, power law exponent (alpha), spectral norm]\\\\n    scale: layer-level (per weight matrix)\\\\n    key_findings:\\\\n      - stable rank 追踪自正则化程度\\\\n      - 5+1 训练阶段对应不同的谱形态\\\\n      - heavy-tailed 分布特征区分好/差模型\\\\n    vs_ours: >\\\\n      方法论基础——WeightWatcher 的 stable rank 和谱分析方法\\\\n      直接启发我们的信号设计。\\\\n\\\\n  - id: yunis_2024\\\\n    title: \\\\\\\"Approaching Deep Learning through the Spectral Dynamics of Weights\\\\\\\"\\\\n    authors: [David Yunis, Kumar Kshitij Patel et al.]\\\\n    year: 2024\\\\n    venue: arXiv (2408.11804)\\\\n    relation: complementary\\\\n    core_method: >\\\\n      以权重奇异值/向量的动态演化为核心视角理解深度学习。\\\\n      证明谱动态可区分记忆网络和泛化网络。\\\\n    signals: [singular value dynamics, singular vector alignment]\\\\n    scale: layer-level (per weight matrix)\\\\n    key_findings:\\\\n      - 权重衰减增强低秩偏置\\\\n      - 谱动态区分记忆 vs 泛化\\\\n      - 与 lottery ticket 和 loss surface 结构相关\\\\n    vs_ours: 方法论基础——谱动态视角可用于理解 collapse 过程中的权重变化。\\\\n\\\\n  - id: chen_liu_2024\\\\n    title: \\\\\\\"Assessing Neural Network Representations During Training Using Noise-Resilient Diffusion Spectral Entropy\\\\\\\"\\\\n    authors: [Chen Liu et al.]\\\\n    year: 2024\\\\n    venue: IEEE CISS 2024\\\\n    relation: complementary\\\\n    core_method: >\\\\n      提出 Diffusion Spectral Entropy (DSE) 和 Diffusion Spectral Mutual Information (DSMI)，\\\\n      利用数据几何在高维中可靠计算信息论指标。\\\\n    signals: [DSE, DSMI]\\\\n    scale: layer-level (representations)\\\\n    key_findings:\\\\n      - DSE 在训练中增加\\\\n      - DSMI(class label) 在泛化学习中增加，过拟合时停滞\\\\n      - 可用于指导网络初始化和预测下游准确率\\\\n    vs_ours: >\\\\n      方法论工具——DSE 是我们 spectral entropy 信号的潜在替代实现。\\\\n\\\\n  - id: lu_neurips2024\\\\n    title: \\\\\\\"AlphaPruning: Using Heavy-Tailed Self Regularization Theory for Improved Layer-wise Pruning of Large Language Models\\\\\\\"\\\\n    authors: [Haiquan Lu, Yefan Zhou, Shiwei Liu, Zhangyang Wang, Michael W. Mahoney, Yaoqing Yang]\\\\n    year: 2024\\\\n    venue: NeurIPS 2024\\\\n    relation: complementary\\\\n    core_method: >\\\\n      用 HT-SR 理论的谱密度形态（alpha exponent）指导 LLM 层级剪枝。\\\\n    signals: [alpha exponent, ESD shape metrics]\\\\n    scale: layer-level\\\\n    key_findings:\\\\n      - Alpha exponent 有效指导 per-layer 剪枝比例\\\\n      - LLaMA-7B 可剪至 80% sparsity 保持合理 perplexity\\\\n    vs_ours: >\\\\n      验证 per-layer 谱分析对 LLM 质量评估的有效性。\\\\n      支持我们用类似方法监控 collapse。\\\\n\\\\n  - id: sanyal_iclr2020\\\\n    title: \\\\\\\"Stable Rank Normalization for Improved Generalization in Neural Networks and GANs\\\\\\\"\\\\n    authors: [Amartya Sanyal, Philip H. S. Torr, Puneet K. Dokania]\\\\n    year: 2020\\\\n    venue: ICLR 2020\\\\n    relation: complementary\\\\n    core_method: >\\\\n      提出 stable rank normalization——最小化线性算子的 stable rank。\\\\n      理论证明唯一最优解，实验验证改善泛化。\\\\n    signals: [stable rank, Lipschitz constant]\\\\n    scale: layer-level\\\\n    key_findings:\\\\n      - 控制 stable rank 改善泛化 gap 11.3%\\\\n      - Stable rank 与泛化能力直接关联\\\\n    vs_ours: >\\\\n      理论支持——建立 stable rank 与泛化的直接联系。\\\\n      支持我们选用 stable rank 作为 collapse（泛化退化）的监控信号。\\\\n\\\\n  - id: kalra_2026\\\\n    title: \\\\\\\"A Scalable Measure of Loss Landscape Curvature for Analyzing the Training Dynamics of LLMs\\\\\\\"\\\\n    authors: [Dayal Singh Kalra, Jean-Christophe Gagnon-Audet, Andrey Gromov, Ishita Mediratta, Kelvin Niu, Alexander H. Miller, Michael Shvartsman]\\\\n    year: 2026\\\\n    venue: arXiv (2601.16979)\\\\n    relation: related\\\\n    core_method: >\\\\n      Critical sharpness：<10 forward passes 高效度量 loss landscape 曲率。\\\\n      首次在 7B 规模验证 progressive sharpening 和 Edge of Stability。\\\\n    signals: [critical sharpness, relative critical sharpness]\\\\n    scale: model-level\\\\n    key_findings:\\\\n      - Progressive sharpening 在 7B 规模仍然存在\\\\n      - Critical sharpness 可指导 pre-train 到 fine-tune 的数据混合\\\\n    vs_ours: >\\\\n      训练动态监控方法论参考——高效的大规模 LLM 训练动态度量。\\\\n      Critical sharpness 可作为我们信号集的潜在补充。\\\\n\\\\n  # ===================== DATA QUALITY =====================\\\\n\\\\n  - id: penedo_2024\\\\n    title: \\\\\\\"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale\\\\\\\"\\\\n    authors: [Guilherme Penedo, Hynek Kydlicek, Loubna Ben allal, Anton Lozhkov, Margaret Mitchell, Colin Raffel, Leandro Von Werra, Thomas Wolf]\\\\n    year: 2024\\\\n    venue: arXiv (2406.17557)\\\\n    relation: complementary\\\\n    core_method: >\\\\n      15T token 数据集的完整策略文档——去重、过滤、教育文本提取。\\\\n    signals: [data quality classifiers, deduplication metrics]\\\\n    scale: dataset-level\\\\n    key_findings:\\\\n      - 详细 ablation 各种去重和过滤策略\\\\n      - FineWeb-Edu 在知识密集任务上大幅提升性能\\\\n    vs_ours: 数据质量策略参考——理解高质量训练数据标准，为分析 collapse 的数据原因提供基线。\\\\n\\\\n  - id: zhang_2026\\\\n    title: \\\\\\\"The LLM Data Auditor: A Metric-oriented Survey on Quality and Trustworthiness in Evaluating Synthetic Data\\\\\\\"\\\\n    authors: [Kaituo Zhang, Mingzhi Hu, Hoang Anh Duy Le et al.]\\\\n    year: 2026\\\\n    venue: arXiv (2601.17717)\\\\n    relation: complementary\\\\n    core_method: >\\\\n      系统分类合成数据评估指标——quality (validity/fidelity/utility) +\\\\n      trustworthiness (safety/faithfulness)。\\\\n    signals: [quality metrics taxonomy, trustworthiness metrics]\\\\n    scale: dataset-level\\\\n    key_findings:\\\\n      - 从内在属性评估合成数据，而非仅看下游性能\\\\n      - 质量和可信度两个维度的完整分类体系\\\\n    vs_ours: 合成数据质量评估框架——为理解 collapse 的数据级原因提供指标体系。\\\\n\\\\n# ============================================================\\\\n# 关键发现总结\\\\n# ============================================================\\\\n\\\\nsummary:\\\\n  total_papers: 37\\\\n  direct_competitors: 2  # SIGMA, Kalinowski\\\\n  novelty_confirmation: >\\\\n    在 34 篇文献中，没有工作同时做到：(a) 训练中在线监控 (b) 用频谱/熵训练动态信号\\\\n    (c) per-layer 粒度 (d) 在迭代合成数据训练场景下验证。\\\\n    我们的核心新颖性空间依然存在。\\\\n\\\\n  coverage:\\\\n    model_collapse_theory: 16  # shumailov, dohmatob x2, alemohammad, fu, gerstgrasser, seddik, kazdan, schaeffer, bakshi, shi_neurips2025, feng, yi, gillman, briesch, hataya\\\\n    data_contamination: 5  # kirchenbauer, dathathri, sander, mitchell, shi_iclr2024\\\\n    spectral_methods: 9  # sigma, martin_mahoney, yunis, lu, sanyal, spectral_lens, xu, conzelmann, pennington\\\\n    training_dynamics: 4  # kalinowski, chen_liu, kalra, papyan\\\\n    data_quality: 3  # wyss, penedo, zhang\\\\n\\\\n  gap_analysis:\\\\n    sigma: >\\\\n      用输出嵌入 Gram 矩阵谱——事后/黑盒，不做 per-layer，不跟踪训练过程。\\\\n    kalinowski: >\\\\n      用拓扑信号——在线但信号族不同，不研究迭代合成数据场景。\\\\n    our_unique_position: >\\\\n      训练动态频谱/熵信号 + per-layer 粒度 + 迭代合成数据场景 = 独特定位。\\\\n\\\\n  per_layer_collapse_analysis:\\\\n    papers_with_per_layer:\\\\n      - layer_collapse_diffusion_2026  # diffusion LM per-layer activation collapse\\\\n      - xu_2026  # stable rank per-layer（compression 场景）\\\\n      - spectral_lens_2026  # per-layer activation/gradient 谱\\\\n      - lu_neurips2024  # alpha exponent per-layer for pruning\\\\n    gap: \\\\\\\"无论文在迭代合成数据训练中做 per-layer collapse 分析\\\\\\\"\\\\n\\\\n  stable_rank_as_collapse_signal:\\\\n    papers_using_stable_rank:\\\\n      - martin_mahoney_2021  # WeightWatcher 中作为模型质量指标\\\\n      - xu_2026  # 压缩退化预测器 (r=0.89)\\\\n      - yunis_2024  # 谱动态中的低秩偏置\\\\n      - sanyal_iclr2020  # stable rank 与泛化的直接联系\\\\n    gap: \\\\\\\"无论文直接用 stable rank 监控 iterative synthetic data collapse\\\\\\\"\\\\n\\\\n  spectral_entropy_as_collapse_signal:\\\\n    papers_using_spectral_entropy:\\\\n      - chen_liu_2024  # DSE 跟踪训练动态\\\\n      - sigma_2026  # 谱分析但在 Gram 矩阵上\\\\n    gap: \\\\\\\"无论文直接用 weight spectral entropy 监控 collapse\\\\\\\"\\\\n\\\\n  synthetic_fraction_effects:\\\\n    papers_studying_fraction:\\\\n      - dohmatob_iclr2025  # 理论：任何非零 fraction 都危险\\\\n      - dohmatob_icml2024  # scaling law 角度的 fraction 分析\\\\n      - alemohammad_iclr2024  # 三种 loop 类型的不同效果\\\\n      - wyss_2024  # 实证：25%/50%/75% 不同 collapse 程度\\\\n      - seddik_2024  # 统计：给出安全上限估计\\\\n    gap: \\\\\\\"大量理论/实证工作，但都用事后指标衡量 fraction 效果\\\\\\\"\\\\n\\\\n  data_contamination_detection:\\\\n    papers:\\\\n      - kirchenbauer_icml2023  # 基础水印方法\\\\n      - dathathri_nature2024  # 产品级水印 (SynthID)\\\\n      - sander_neurips2024  # 水印放射性传播\\\\n      - mitchell_icml2023  # DetectGPT 概率曲率检测\\\\n      - shi_iclr2024  # Min-K% 预训练数据检测\\\\n    relevance: >\\\\n      合成数据检测与 collapse 监控互补：他们回答\\\\\\\"是否有合成数据\\\\\\\"，\\\\n      我们回答\\\\\\\"合成数据造成了多严重的 collapse\\\\\\\"。\\\\n\\\", \\\"total_chars\\\": 26925, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/literature_map.yaml\", \"content\": \"# Literature Map — collapse_severity_monitor\\n# 最后更新: 2026-05-14 (expanded to 37 papers)\\n# 研究方向: 在线监控模型 collapse 严重度——用训练动态信号实时跟踪迭代合成数据训练中的质量退化\\n\\n# ============================================================\\n# 竞争关系分类说明:\\n#   direct_competitor  — 解决同一问题（在线监控 collapse）\\n#   related            — 解决相近问题或使用相关方法\\n#   complementary      — 互补（提供理论基础/工具/缓解策略）\\n#   foundation         — 领域基础工作\\n# ============================================================\\n\\npapers:\\n\\n  # ===================== DIRECT COMPETITORS =====================\\n\\n  - id: sigma_2026\\n    title: \\\"SIGMA: Scalable Spectral Insights for LLM Model Collapse\\\"\\n    authors: [Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, Alexander Aue]\\n    year: 2026\\n    venue: arXiv (2601.03385)\\n    relation: direct_competitor\\n    core_method: >\\n      通过 embedding Gram 矩阵的谱分析来量化 model collapse 程度。\\n      推导 Gram 矩阵谱的确定性和随机性界，用谱收缩作为 collapse 指标。\\n    signals: [Gram matrix spectrum, rank deficiency, spectral bounds]\\n    scale: model-level (output embeddings)\\n    key_findings:\\n      - Gram 矩阵满秩是 LLM 正常运作的必要条件\\n      - 秩亏缺意味着语义级信息丢失，标志 collapse 开始\\n      - 随机公式使框架可扩展至大规模模型\\n    vs_ours: >\\n      SIGMA 用输出嵌入的 Gram 矩阵谱，是事后/黑盒方法，不需要模型权重。\\n      我们用训练动态信号（权重频谱熵、stable rank、token entropy），\\n      是训练中实时监控，更早期更细粒度（per-layer）。\\n      SIGMA 不做 per-layer 分析，不跟踪训练过程的动态变化。\\n    threat_level: medium\\n\\n  - id: kalinowski_2026\\n    title: \\\"Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index\\\"\\n    authors: [Alexander Kalinowski]\\n    year: 2026\\n    venue: arXiv (2604.26984)\\n    relation: direct_competitor\\n    core_method: >\\n      提出在线拓扑感知监控器，结合 Modular Morse Homology Maintenance (MMHM)\\n      和复合 Collapse Index (CI)，通过稀疏增量更新实现快速在线监控。\\n    signals: [persistent homology, Collapse Index (CI), topological features]\\n    scale: model-level (representation space topology)\\n    key_findings:\\n      - CI 在 LLM fine-tuning 和时序 KGE 训练中提供低延迟早期预警\\n      - 表征各向异性和多尺度结构丧失在性能指标反应之前就可检测\\n      - 增量更新避免每个 epoch 重建复形\\n    vs_ours: >\\n      Kalinowski 用拓扑信号（persistent homology），我们用频谱/熵信号。\\n      两者都是在线监控，但信号族完全不同。我们的信号更轻量、\\n      更可解释（stable rank/spectral entropy 有直接的线性代数含义）。\\n      Kalinowski 不研究迭代合成数据训练场景。\\n    threat_level: medium\\n\\n  # ===================== CLOSELY RELATED =====================\\n\\n  - id: spectral_lens_2026\\n    title: \\\"Spectral Lens: Activation and Gradient Spectra as Diagnostics of LLM Optimization\\\"\\n    authors: [Andy Zeyi Liu et al.]\\n    year: 2026\\n    venue: arXiv (2605.05683)\\n    relation: related\\n    core_method: >\\n      用 activation covariance 和 per-sample gradient 的 SVD 谱\\n      作为 LLM 训练优化的诊断工具。\\n    signals: [activation covariance spectrum, gradient SVD spectrum]\\n    scale: layer-level\\n    key_findings:\\n      - batch size 是表示几何的隐藏决定因素\\n      - 早期训练的 activation covariance 尾部可预测下游 token 效率\\n      - activation 谱头部运动 + gradient 谱可区分学习侧和执行侧改进\\n    vs_ours: >\\n      方法论高度相关——同样用频谱分析训练动态。\\n      但他们关注优化诊断，不研究 collapse/合成数据退化。\\n      可作为方法论参考。\\n    threat_level: low\\n\\n  - id: shi_neurips2025\\n    title: \\\"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\\\"\\n    authors: [Lianghe Shi, Meng Wu, Huijie Zhang, Zekai Zhang, Molei Tao, Qing Qu]\\n    year: 2025\\n    venue: NeurIPS 2025 (Spotlight)\\n    relation: related\\n    core_method: >\\n      揭示 model collapse 中从泛化到记忆的转变。\\n      发现训练数据熵与模型泛化能力的强线性相关。\\n      提出基于熵的子集选择方法来减缓 collapse。\\n    signals: [dataset entropy, generalization metrics]\\n    scale: model-level (data distribution)\\n    key_findings:\\n      - 迭代训练中数据分布熵急剧下降导致泛化能力下降\\n      - 强线性相关：训练数据集熵与模型泛化能力\\n      - 熵选择方法有效减缓泛化到记忆转变\\n    vs_ours: >\\n      他们用数据级别的熵，我们用模型内部的训练动态信号。\\n      互补：他们的数据熵可作为我们的外部验证指标。\\n      他们不做 per-layer 分析，不做在线监控。\\n    threat_level: low\\n\\n  - id: wyss_2024\\n    title: \\\"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI\\\"\\n    authors: [C. M. Wyss et al.]\\n    year: 2024\\n    venue: arXiv (2410.12341)\\n    relation: related\\n    core_method: >\\n      用语义网络和 next-token 概率来表征 LLM 中的 model collapse。\\n      引入 collapsed prediction 概念量化多样性损失。\\n      分析不同合成 token 比例 (25%/50%/75%) 对 collapse 的影响。\\n    signals: [next-token probability distribution, semantic network metrics, collapsed prediction ratio]\\n    scale: token-level (output)\\n    key_findings:\\n      - Next-token 概率分布可精确量化多样性损失\\n      - 合成 token 比例越高，collapse 越严重\\n      - 跨数据集迁移：在非微调数据集上 collapse 程度不同\\n    vs_ours: >\\n      他们用输出级指标（next-token prob），我们用训练动态内部信号。\\n      他们的 synthetic fraction 实验与我们的实验设计有重叠。\\n      不同之处：他们是事后分析，我们是训练中在线监控。\\n    threat_level: low\\n\\n  - id: xu_2026\\n    title: \\\"Predicting LLM Compression Degradation from Spectral Statistics\\\"\\n    authors: [Mingxue Xu]\\n    year: 2026\\n    venue: arXiv (2604.18085)\\n    relation: related\\n    core_method: >\\n      用 stable rank 和信息密度 (bits/param) 预测 LLM 压缩导致的退化。\\n      交互项 compression_ratio * stable_rank 是退化的强预测器。\\n    signals: [stable rank, information density, compression ratio]\\n    scale: layer-level (attention vs MLP 分开分析)\\n    key_findings:\\n      - stable rank 是压缩退化的主要预测因子（Pearson r=0.890 attention, 0.839 MLP）\\n      - 层类型比压缩方法更重要\\n      - layer-specific calibration 优于 method-specific tuning\\n    vs_ours: >\\n      直接验证 stable rank 作为退化预测信号的有效性。\\n      虽然场景不同（压缩 vs collapse），但支持我们选用 stable rank 的合理性。\\n      他们的 per-layer 分析方法可参考。\\n    threat_level: low\\n\\n  - id: layer_collapse_diffusion_2026\\n    title: \\\"Layer Collapse in Diffusion Language Models\\\"\\n    authors: [Alexander Conzelmann, Albert Catalan-Tatjer, Shiwei Liu]\\n    year: 2026\\n    venue: arXiv (2605.06366)\\n    relation: related\\n    core_method: >\\n      分析 diffusion language model (LLaDA-8B) 中的 per-layer activation 动态，\\n      发现少数早期层展现 collapsed activation patterns。\\n    signals: [activation patterns, super-outlier magnitude]\\n    scale: layer-level\\n    key_findings:\\n      - 几个早期层出现 channel-axis collapse（单一维度主导所有位置）\\n      - 尽管看似冗余，pruning outlier 导致退化为重复随机 token 循环\\n      - Diffusion LM 与 autoregressive LM 的 collapse 行为不同\\n    vs_ours: >\\n      做了 per-layer collapse 分析，但在 diffusion LM 上。\\n      方法论参考：per-layer activation 分析方法。\\n    threat_level: low\\n\\n  # ===================== FOUNDATION =====================\\n\\n  - id: alemohammad_iclr2024\\n    title: \\\"Self-Consuming Generative Models Go MAD\\\"\\n    authors: [Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard G. Baraniuk]\\n    year: 2024\\n    venue: ICLR 2024\\n    relation: foundation\\n    core_method: >\\n      定义三种 autophagous loop（fully synthetic / synthetic augmentation / fresh data），\\n      证明无足够真实数据时 precision 或 recall 必然下降（MAD 现象）。\\n    signals: [FID, precision, recall]\\n    scale: model-level (image generative models)\\n    key_findings:\\n      - 三种 loop 类型的 collapse 行为不同\\n      - 无 fresh data 时 quality 或 diversity 必然退化\\n      - 在 StyleGAN、DDPM、denoising diffusion 上验证\\n    vs_ours: >\\n      领域基础论文之一。他们的 loop 分类框架直接对应我们的实验设计。\\n      他们用 FID/precision/recall（事后指标），我们提供训练中在线信号。\\n\\n  - id: papyan_pnas2020\\n    title: \\\"Prevalence of Neural Collapse during the Terminal Phase of Deep Learning Training\\\"\\n    authors: [Vardan Papyan, X. Y. Han, David L. Donoho]\\n    year: 2020\\n    venue: PNAS 117(40), 24652-24663\\n    relation: foundation\\n    core_method: >\\n      发现分类网络训练末期的 Neural Collapse——类内表征收缩到 Simplex ETF。\\n    signals: [within-class variability, classifier-mean alignment]\\n    scale: model-level (last-layer representations)\\n    key_findings:\\n      - 训练末期出现四种 collapse 现象\\n      - 类均值收敛到 Simplex ETF 顶点\\n      - Collapse 与泛化能力相关\\n    vs_ours: >\\n      虽然 neural collapse 与 model collapse 是不同概念，\\n      但谱分析方法论可借鉴，且提供 \\\"collapse\\\" 概念的对比参考。\\n\\n  - id: hataya_iccv2023\\n    title: \\\"Will Large-scale Generative Models Corrupt Future Datasets?\\\"\\n    authors: [Ryuichiro Hataya, Han Bao, Hiromi Arai]\\n    year: 2023\\n    venue: ICCV 2023 (pp. 20555-20565)\\n    relation: foundation\\n    core_method: >\\n      用 SOTA 生成模型生成 ImageNet/COCO 规模数据集，\\n      评估\\\"被污染\\\"数据集在分类和生成任务上的下游性能退化。\\n    signals: [classification accuracy, FID, generation quality]\\n    scale: dataset-level (ImageNet/COCO scale)\\n    key_findings:\\n      - 生成图像对下游性能有负面影响\\n      - 影响程度取决于任务类型和生成图像比例\\n      - 首次在 ImageNet 规模验证数据集污染效应\\n    vs_ours: >\\n      早期数据集污染实证研究，在视觉领域验证了 collapse 前兆。\\n      他们关注下游任务性能，我们关注训练中的实时信号。\\n\\n  # ===================== COMPLEMENTARY (Theory/Mitigation) =====================\\n\\n  - id: shumailov_nature2024\\n    title: \\\"AI Models Collapse When Trained on Recursively Generated Data\\\"\\n    authors: [Ilia Shumailov et al.]\\n    year: 2024\\n    venue: Nature 631, 755-759\\n    relation: foundation\\n    core_method: >\\n      首次系统性证明迭代合成数据训练导致 model collapse。\\n      在 LLM、VAE、GMM 上验证。分布尾部消失是核心机制。\\n    signals: [test loss, distribution tail metrics]\\n    scale: model-level\\n    key_findings:\\n      - 迭代训练导致不可逆缺陷：分布尾部消失\\n      - 罕见事件最先遗忘\\n      - LLM、VAE、GMM 都有此现象\\n    vs_ours: >\\n      领域基石论文，建立了我们要解决的问题。\\n      他们用事后评估（test loss），我们提供在线监控手段。\\n\\n  - id: dohmatob_iclr2025\\n    title: \\\"Strong Model Collapse\\\"\\n    authors: [Elvis Dohmatob, Yunzhen Feng et al.]\\n    year: 2025\\n    venue: ICLR 2025 (Spotlight)\\n    relation: complementary\\n    core_method: >\\n      用算子值自由概率论证明即使极小比例的合成数据 (1/1000)\\n      也会导致 model collapse，且更大模型放大 collapse。\\n    signals: [test error on real data, bias-variance decomposition]\\n    scale: model-level\\n    key_findings:\\n      - 任何非零常数比例的合成数据都导致 collapse\\n      - 更大模型可放大 collapse\\n      - 神经缩放定律在合成数据下失效\\n    vs_ours: >\\n      理论基础——解释了为什么需要监控（即使少量合成数据也危险）。\\n      他们的 fraction 实验与我们的实验设计直接相关。\\n\\n  - id: gerstgrasser_2024\\n    title: \\\"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\\\"\\n    authors: [Matthias Gerstgrasser, Rylan Schaeffer et al.]\\n    year: 2024\\n    venue: arXiv (2404.01413)\\n    relation: complementary\\n    core_method: >\\n      证明数据累积（而非替换）可避免 model collapse。\\n      替换导致 test error 增长，累积则有有限上界。\\n    signals: [test error over iterations]\\n    scale: model-level\\n    key_findings:\\n      - 累积真实+合成数据则无 collapse（所有模型/模态）\\n      - 替换数据则 collapse\\n      - 关键因素是数据管理策略\\n    vs_ours: >\\n      互补——他们研究何时 collapse（数据管理策略），\\n      我们研究如何实时检测 collapse（训练动态信号）。\\n\\n  - id: kazdan_2024\\n    title: \\\"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\\\"\\n    authors: [Joshua Kazdan et al.]\\n    year: 2024\\n    venue: arXiv (2410.16713)\\n    relation: complementary\\n    core_method: >\\n      系统比较三种训练工作流：replace（collapse）、\\n      accumulate（稳定）、fixed compute（介于两者之间）。\\n    signals: [test loss on real data]\\n    scale: model-level\\n    key_findings:\\n      - Replace 工作流一定 collapse\\n      - Accumulate 工作流保持稳定\\n      - Fixed compute 工作流 loss 升高但 plateau\\n    vs_ours: 互补——提供实验设计参考（不同工作流下 collapse 行为差异）。\\n\\n  - id: seddik_2024\\n    title: \\\"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\\\"\\n    authors: [Mohamed El Amine Seddik et al.]\\n    year: 2024\\n    venue: arXiv (2404.05090)\\n    relation: complementary\\n    core_method: >\\n      统计模型严格刻画不同递归训练场景下的 collapse 程度。\\n      给出混合真实/合成数据时避免 collapse 的最大合成数据比例估计。\\n    signals: [distribution tail, statistical divergence]\\n    scale: model-level\\n    key_findings:\\n      - 纯合成数据训练无法避免 collapse\\n      - 混合训练下存在可计算的合成数据上限\\n      - 分布尾部消失是 collapse 的统计特征\\n    vs_ours: 理论互补——给出合成数据比例的安全阈值。\\n\\n  - id: schaeffer_2025\\n    title: \\\"Position: Model Collapse Does Not Mean What You Think\\\"\\n    authors: [Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, Sanmi Koyejo]\\n    year: 2025\\n    venue: arXiv (2503.03150)\\n    relation: complementary\\n    core_method: >\\n      梳理 model collapse 文献中 8 种不同定义，\\n      分为三个家族：test loss 行为、分布形变、缩放行为。\\n    signals: N/A (position paper)\\n    scale: N/A\\n    key_findings:\\n      - Model collapse 有 8 种不完全一致的定义\\n      - 三个家族：test loss 行为、分布形变、缩放定律\\n      - 术语混乱阻碍了系统性理解\\n    vs_ours: >\\n      重要定位参考——论文中需明确使用哪种 collapse 定义。\\n      建议采用他们的分类框架。\\n\\n  - id: feng_iclr2025\\n    title: \\\"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification\\\"\\n    authors: [Feng et al.]\\n    year: 2025\\n    venue: ICLR 2025\\n    relation: complementary\\n    core_method: >\\n      用高斯混合+线性分类器+线性验证器推导验证器有效的条件。\\n      证明不完美验证器也可有效筛选合成数据。\\n    signals: [verifier-based quality score]\\n    scale: model-level\\n    key_findings:\\n      - 验证器筛选合成数据可达到最优性能\\n      - 即使不完美验证器也有效\\n      - 给出可衡量的代理条件\\n    vs_ours: 互补——缓解策略。我们的监控信号可作为验证器的补充。\\n\\n  - id: yi_2025\\n    title: \\\"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence\\\"\\n    authors: [Bingji Yi, Qiyuan Liu, Yuwei Cheng, Haifeng Xu]\\n    year: 2025\\n    venue: arXiv (2510.16657)\\n    relation: complementary\\n    core_method: >\\n      证明外部验证器（人类或更强模型）可阻止 collapse。\\n      分析验证器引导下的短期改进和长期收敛行为。\\n    signals: [verifier quality score]\\n    scale: model-level\\n    key_findings:\\n      - 外部验证器注入信息则不会 collapse\\n      - 短期有改进，长期收敛到验证器的知识中心\\n    vs_ours: 互补——缓解策略方向，与监控方向正交。\\n\\n  - id: bakshi_2026\\n    title: \\\"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\\\"\\n    authors: [Soham Bakshi et al.]\\n    year: 2026\\n    venue: arXiv (2602.10531)\\n    relation: complementary\\n    core_method: >\\n      分析在真实+合成混合数据上的迭代训练动态。\\n      next-token prediction 模型下的长期演化分析。\\n    signals: [mixture weight, sample size, test performance]\\n    scale: model-level\\n    key_findings:\\n      - 非零真实数据混合权重（即使递减）可避免 collapse\\n      - 混合权重和样本量共同控制长期性能\\n    vs_ours: 理论互补——刻画迭代训练的长期演化。\\n\\n  - id: briesch_2023\\n    title: \\\"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\\\"\\n    authors: [Martin Briesch, Dominik Sobania, Franz Rothlauf]\\n    year: 2023\\n    venue: arXiv (2311.16822)\\n    relation: complementary\\n    core_method: >\\n      首次针对 LLM 研究 self-consuming training loop，\\n      用逻辑表达式构造可验证的生成内容，分析不同合成数据比例下输出多样性下降。\\n    signals: [output diversity, correctness rate]\\n    scale: model-level\\n    key_findings:\\n      - Self-consuming loop 产生正确输出，但多样性随合成数据比例下降\\n      - 首批 LLM self-consuming loop 实证研究之一\\n      - 提出基于逻辑表达式的内容验证方法\\n    vs_ours: >\\n      早期 LLM self-consuming loop 实证研究。\\n      他们用输出级多样性指标，我们用训练动态内部信号；互为补充。\\n\\n  - id: dohmatob_icml2024\\n    title: \\\"A Tale of Tails: Model Collapse as a Change of Scaling Laws\\\"\\n    authors: [Elvis Dohmatob, Yunzhen Feng, Pu Yang, Francois Charton, Julia Kempe]\\n    year: 2024\\n    venue: ICML 2024 (pp. 11165-11197)\\n    relation: complementary\\n    core_method: >\\n      从 scaling law 视角分析 collapse——理论框架揭示 collapse 导致 scaling law 改变。\\n    signals: [test loss scaling, skill metrics]\\n    scale: model-level\\n    key_findings:\\n      - Loss of scaling、shifted scaling with number of generations\\n      - Skill un-learning 现象\\n      - 混合人类/合成数据时的 grokking 效应\\n    vs_ours: >\\n      理论背景——从 scaling law 角度量化 collapse 严重度。\\n      我们用训练动态信号在训练中追踪，他们用事后 scaling 分析。\\n\\n  - id: fu_icml2024\\n    title: \\\"Towards Theoretical Understandings of Self-Consuming Generative Models\\\"\\n    authors: [Shi Fu, Sen Zhang, Yingjie Wang, Xinmei Tian, Dacheng Tao]\\n    year: 2024\\n    venue: ICML 2024\\n    relation: complementary\\n    core_method: >\\n      构建严格理论框架分析 self-consuming loop 中数据分布演化。\\n      分析参数和非参数模型中三种误差源的复合效应。\\n    signals: [distribution divergence, error accumulation]\\n    scale: model-level\\n    key_findings:\\n      - 统计/表达/近似三种误差在迭代中复合\\n      - 给出误差增长的理论界\\n    vs_ours: 理论互补——严格刻画 collapse 的误差复合机制。\\n\\n  - id: gillman_icml2024\\n    title: \\\"Self-Correcting Self-Consuming Loops for Generative Model Training\\\"\\n    authors: [Nate Gillman, Michael Freeman, Daksh Aggarwal, Chia-Hong Hsu, Calvin Luo, Yonglong Tian, Chen Sun]\\n    year: 2024\\n    venue: ICML 2024\\n    relation: complementary\\n    core_method: >\\n      引入 correction function 使 self-consuming loop 指数级更稳定。\\n      在人体运动合成任务上验证。\\n    signals: [corrector quality, loop stability]\\n    scale: model-level\\n    key_findings:\\n      - Correction function 使 loop 指数级稳定\\n      - 即使 synthetic:real = 100:1 也可避免 collapse\\n    vs_ours: 互补——缓解策略，correction function 概念与在线监控互补。\\n\\n  - id: pennington_nips2017\\n    title: \\\"Nonlinear Random Matrix Theory for Deep Learning\\\"\\n    authors: [Jeffrey Pennington, Pratik Worah]\\n    year: 2017\\n    venue: NeurIPS 2017\\n    relation: foundation\\n    core_method: >\\n      将神经网络中的逐点非线性纳入随机矩阵理论的矩方法框架，\\n      推导数据协方差矩阵在网络层间传播的渐近谱分布。\\n    signals: [eigenvalue distribution, spectral density]\\n    scale: layer-level (weight/covariance matrices)\\n    key_findings:\\n      - 非线性激活函数可纳入 RMT 矩方法\\n      - 推导单层随机特征方法在记忆任务上的渐近性能\\n      - 分析数据协方差矩阵在网络中传播时的特征值演化\\n    vs_ours: >\\n      RMT 在深度学习中的理论基础。我们的谱分析方法论（spectral entropy、\\n      stable rank）建立在此类随机矩阵理论之上。\\n\\n  # ===================== DATA CONTAMINATION DETECTION =====================\\n\\n  - id: kirchenbauer_icml2023\\n    title: \\\"A Watermark for Large Language Models\\\"\\n    authors: [John Kirchenbauer, Jonas Geiping, Yuxin Wen, Jonathan Katz, Ian Miers, Tom Goldstein]\\n    year: 2023\\n    venue: ICML 2023 (pp. 17061-17084)\\n    relation: complementary\\n    core_method: >\\n      LLM 文本水印框架——green/red token list + soft promotion + 统计检测。\\n    signals: [green token ratio, z-score]\\n    scale: token-level (output)\\n    key_findings:\\n      - 可嵌入统计可检测水印且不影响文本质量\\n      - 开源检测算法不需模型访问\\n    vs_ours: 合成数据溯源的基础方法，与 collapse 检测互补。\\n\\n  - id: dathathri_nature2024\\n    title: \\\"Scalable Watermarking for Identifying Large Language Model Outputs\\\"\\n    authors: [Sumanth Dathathri, Abigail See, Sumedh Ghaisas et al.]\\n    year: 2024\\n    venue: Nature 634, 818-823\\n    relation: complementary\\n    core_method: >\\n      SynthID-Text：产品级文本水印，与 speculative sampling 集成。\\n      在 Gemini ~20M 响应上验证。\\n    signals: [watermark detection score]\\n    scale: token-level (output)\\n    key_findings:\\n      - 产品级规模的水印部署\\n      - 不影响文本质量，最小延迟开销\\n    vs_ours: 大规模合成数据标记的工业实践，与监控方向互补。\\n\\n  - id: sander_neurips2024\\n    title: \\\"Watermarking Makes Language Models Radioactive\\\"\\n    authors: [Tom Sander, Pierre Fernandez, Alain Durmus, Matthijs Douze, Teddy Furon]\\n    year: 2024\\n    venue: NeurIPS 2024\\n    relation: related\\n    core_method: >\\n      证明在水印 LLM 输出上微调的模型保留水印残留（\\\"放射性\\\"）。\\n    signals: [watermark residual in fine-tuned model]\\n    scale: model-level\\n    key_findings:\\n      - 水印信号通过训练传播到下游模型\\n      - 可检测模型是否在合成数据上训练\\n    vs_ours: >\\n      直接相关——检测合成数据训练的替代方法。\\n      他们检测\\\"是否用了合成数据\\\"，我们监控\\\"合成数据造成多严重的 collapse\\\"。\\n\\n  - id: mitchell_icml2023\\n    title: \\\"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\\\"\\n    authors: [Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn]\\n    year: 2023\\n    venue: ICML 2023 (pp. 24950-24962)\\n    relation: complementary\\n    core_method: >\\n      LLM 生成文本占据 log-probability 负曲率区域，据此零样本检测。\\n    signals: [log probability curvature]\\n    scale: text-level\\n    key_findings:\\n      - 生成文本的概率曲率特征可区分人类/机器文本\\n      - 0.95 AUROC 检测 GPT-NeoX 20B 生成的假新闻\\n    vs_ours: 合成文本检测方法，可识别训练数据中的合成成分。\\n\\n  - id: shi_iclr2024\\n    title: \\\"Detecting Pretraining Data from Large Language Models\\\"\\n    authors: [Weijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, Luke Zettlemoyer]\\n    year: 2024\\n    venue: ICLR 2024\\n    relation: related\\n    core_method: >\\n      Min-K% Prob：未见样本含低概率 outlier word，据此检测预训练数据成员。\\n    signals: [Min-K% probability score]\\n    scale: text-level\\n    key_findings:\\n      - 比 reference model 方法提升 7.4%\\n      - 适用于版权检测、污染检测、隐私审计\\n    vs_ours: 数据污染检测工具——可检测合成数据是否混入训练集，与 collapse 监控互补。\\n\\n  # ===================== METHODOLOGICAL FOUNDATIONS =====================\\n\\n  - id: martin_mahoney_2021\\n    title: \\\"Predicting Trends in the Quality of State-of-the-Art Neural Networks without Access to Training or Testing Data\\\"\\n    authors: [Charles H. Martin, Michael W. Mahoney]\\n    year: 2021\\n    venue: Nature Communications 12\\n    relation: complementary\\n    core_method: >\\n      WeightWatcher 工具——用 RMT 分析权重矩阵的谱性质，\\n      无需训练/测试数据即可预测模型质量。\\n    signals: [stable rank, power law exponent (alpha), spectral norm]\\n    scale: layer-level (per weight matrix)\\n    key_findings:\\n      - stable rank 追踪自正则化程度\\n      - 5+1 训练阶段对应不同的谱形态\\n      - heavy-tailed 分布特征区分好/差模型\\n    vs_ours: >\\n      方法论基础——WeightWatcher 的 stable rank 和谱分析方法\\n      直接启发我们的信号设计。\\n\\n  - id: yunis_2024\\n    title: \\\"Approaching Deep Learning through the Spectral Dynamics of Weights\\\"\\n    authors: [David Yunis, Kumar Kshitij Patel et al.]\\n    year: 2024\\n    venue: arXiv (2408.11804)\\n    relation: complementary\\n    core_method: >\\n      以权重奇异值/向量的动态演化为核心视角理解深度学习。\\n      证明谱动态可区分记忆网络和泛化网络。\\n    signals: [singular value dynamics, singular vector alignment]\\n    scale: layer-level (per weight matrix)\\n    key_findings:\\n      - 权重衰减增强低秩偏置\\n      - 谱动态区分记忆 vs 泛化\\n      - 与 lottery ticket 和 loss surface 结构相关\\n    vs_ours: 方法论基础——谱动态视角可用于理解 collapse 过程中的权重变化。\\n\\n  - id: chen_liu_2024\\n    title: \\\"Assessing Neural Network Representations During Training Using Noise-Resilient Diffusion Spectral Entropy\\\"\\n    authors: [Chen Liu et al.]\\n    year: 2024\\n    venue: IEEE CISS 2024\\n    relation: complementary\\n    core_method: >\\n      提出 Diffusion Spectral Entropy (DSE) 和 Diffusion Spectral Mutual Information (DSMI)，\\n      利用数据几何在高维中可靠计算信息论指标。\\n    signals: [DSE, DSMI]\\n    scale: layer-level (representations)\\n    key_findings:\\n      - DSE 在训练中增加\\n      - DSMI(class label) 在泛化学习中增加，过拟合时停滞\\n      - 可用于指导网络初始化和预测下游准确率\\n    vs_ours: >\\n      方法论工具——DSE 是我们 spectral entropy 信号的潜在替代实现。\\n\\n  - id: lu_neurips2024\\n    title: \\\"AlphaPruning: Using Heavy-Tailed Self Regularization Theory for Improved Layer-wise Pruning of Large Language Models\\\"\\n    authors: [Haiquan Lu, Yefan Zhou, Shiwei Liu, Zhangyang Wang, Michael W. Mahoney, Yaoqing Yang]\\n    year: 2024\\n    venue: NeurIPS 2024\\n    relation: complementary\\n    core_method: >\\n      用 HT-SR 理论的谱密度形态（alpha exponent）指导 LLM 层级剪枝。\\n    signals: [alpha exponent, ESD shape metrics]\\n    scale: layer-level\\n    key_findings:\\n      - Alpha exponent 有效指导 per-layer 剪枝比例\\n      - LLaMA-7B 可剪至 80% sparsity 保持合理 perplexity\\n    vs_ours: >\\n      验证 per-layer 谱分析对 LLM 质量评估的有效性。\\n      支持我们用类似方法监控 collapse。\\n\\n  - id: sanyal_iclr2020\\n    title: \\\"Stable Rank Normalization for Improved Generalization in Neural Networks and GANs\\\"\\n    authors: [Amartya Sanyal, Philip H. S. Torr, Puneet K. Dokania]\\n    year: 2020\\n    venue: ICLR 2020\\n    relation: complementary\\n    core_method: >\\n      提出 stable rank normalization——最小化线性算子的 stable rank。\\n      理论证明唯一最优解，实验验证改善泛化。\\n    signals: [stable rank, Lipschitz constant]\\n    scale: layer-level\\n    key_findings:\\n      - 控制 stable rank 改善泛化 gap 11.3%\\n      - Stable rank 与泛化能力直接关联\\n    vs_ours: >\\n      理论支持——建立 stable rank 与泛化的直接联系。\\n      支持我们选用 stable rank 作为 collapse（泛化退化）的监控信号。\\n\\n  - id: kalra_2026\\n    title: \\\"A Scalable Measure of Loss Landscape Curvature for Analyzing the Training Dynamics of LLMs\\\"\\n    authors: [Dayal Singh Kalra, Jean-Christophe Gagnon-Audet, Andrey Gromov, Ishita Mediratta, Kelvin Niu, Alexander H. Miller, Michael Shvartsman]\\n    year: 2026\\n    venue: arXiv (2601.16979)\\n    relation: related\\n    core_method: >\\n      Critical sharpness：<10 forward passes 高效度量 loss landscape 曲率。\\n      首次在 7B 规模验证 progressive sharpening 和 Edge of Stability。\\n    signals: [critical sharpness, relative critical sharpness]\\n    scale: model-level\\n    key_findings:\\n      - Progressive sharpening 在 7B 规模仍然存在\\n      - Critical sharpness 可指导 pre-train 到 fine-tune 的数据混合\\n    vs_ours: >\\n      训练动态监控方法论参考——高效的大规模 LLM 训练动态度量。\\n      Critical sharpness 可作为我们信号集的潜在补充。\\n\\n  # ===================== DATA QUALITY =====================\\n\\n  - id: penedo_2024\\n    title: \\\"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale\\\"\\n    authors: [Guilherme Penedo, Hynek Kydlicek, Loubna Ben allal, Anton Lozhkov, Margaret Mitchell, Colin Raffel, Leandro Von Werra, Thomas Wolf]\\n    year: 2024\\n    venue: arXiv (2406.17557)\\n    relation: complementary\\n    core_method: >\\n      15T token 数据集的完整策略文档——去重、过滤、教育文本提取。\\n    signals: [data quality classifiers, deduplication metrics]\\n    scale: dataset-level\\n    key_findings:\\n      - 详细 ablation 各种去重和过滤策略\\n      - FineWeb-Edu 在知识密集任务上大幅提升性能\\n    vs_ours: 数据质量策略参考——理解高质量训练数据标准，为分析 collapse 的数据原因提供基线。\\n\\n  - id: zhang_2026\\n    title: \\\"The LLM Data Auditor: A Metric-oriented Survey on Quality and Trustworthiness in Evaluating Synthetic Data\\\"\\n    authors: [Kaituo Zhang, Mingzhi Hu, Hoang Anh Duy Le et al.]\\n    year: 2026\\n    venue: arXiv (2601.17717)\\n    relation: complementary\\n    core_method: >\\n      系统分类合成数据评估指标——quality (validity/fidelity/utility) +\\n      trustworthiness (safety/faithfulness)。\\n    signals: [quality metrics taxonomy, trustworthiness metrics]\\n    scale: dataset-level\\n    key_findings:\\n      - 从内在属性评估合成数据，而非仅看下游性能\\n      - 质量和可信度两个维度的完整分类体系\\n    vs_ours: 合成数据质量评估框架——为理解 collapse 的数据级原因提供指标体系。\\n\\n# ============================================================\\n# 关键发现总结\\n# ============================================================\\n\\nsummary:\\n  total_papers: 37\\n  direct_competitors: 2  # SIGMA, Kalinowski\\n  novelty_confirmation: >\\n    在 34 篇文献中，没有工作同时做到：(a) 训练中在线监控 (b) 用频谱/熵训练动态信号\\n    (c) per-layer 粒度 (d) 在迭代合成数据训练场景下验证。\\n    我们的核心新颖性空间依然存在。\\n\\n  coverage:\\n    model_collapse_theory: 16  # shumailov, dohmatob x2, alemohammad, fu, gerstgrasser, seddik, kazdan, schaeffer, bakshi, shi_neurips2025, feng, yi, gillman, briesch, hataya\\n    data_contamination: 5  # kirchenbauer, dathathri, sander, mitchell, shi_iclr2024\\n    spectral_methods: 9  # sigma, martin_mahoney, yunis, lu, sanyal, spectral_lens, xu, conzelmann, pennington\\n    training_dynamics: 4  # kalinowski, chen_liu, kalra, papyan\\n    data_quality: 3  # wyss, penedo, zhang\\n\\n  gap_analysis:\\n    sigma: >\\n      用输出嵌入 Gram 矩阵谱——事后/黑盒，不做 per-layer，不跟踪训练过程。\\n    kalinowski: >\\n      用拓扑信号——在线但信号族不同，不研究迭代合成数据场景。\\n    our_unique_position: >\\n      训练动态频谱/熵信号 + per-layer 粒度 + 迭代合成数据场景 = 独特定位。\\n\\n  per_layer_collapse_analysis:\\n    papers_with_per_layer:\\n      - layer_collapse_diffusion_2026  # diffusion LM per-layer activation collapse\\n      - xu_2026  # stable rank per-layer（compression 场景）\\n      - spectral_lens_2026  # per-layer activation/gradient 谱\\n      - lu_neurips2024  # alpha exponent per-layer for pruning\\n    gap: \\\"无论文在迭代合成数据训练中做 per-layer collapse 分析\\\"\\n\\n  stable_rank_as_collapse_signal:\\n    papers_using_stable_rank:\\n      - martin_mahoney_2021  # WeightWatcher 中作为模型质量指标\\n      - xu_2026  # 压缩退化预测器 (r=0.89)\\n      - yunis_2024  # 谱动态中的低秩偏置\\n      - sanyal_iclr2020  # stable rank 与泛化的直接联系\\n    gap: \\\"无论文直接用 stable rank 监控 iterative synthetic data collapse\\\"\\n\\n  spectral_entropy_as_collapse_signal:\\n    papers_using_spectral_entropy:\\n      - chen_liu_2024  # DSE 跟踪训练动态\\n      - sigma_2026  # 谱分析但在 Gram 矩阵上\\n    gap: \\\"无论文直接用 weight spectral entropy 监控 collapse\\\"\\n\\n  synthetic_fraction_effects:\\n    papers_studying_fraction:\\n      - dohmatob_iclr2025  # 理论：任何非零 fraction 都危险\\n      - dohmatob_icml2024  # scaling law 角度的 fraction 分析\\n      - alemohammad_iclr2024  # 三种 loop 类型的不同效果\\n      - wyss_2024  # 实证：25%/50%/75% 不同 collapse 程度\\n      - seddik_2024  # 统计：给出安全上限估计\\n    gap: \\\"大量理论/实证工作，但都用事后指标衡量 fraction 效果\\\"\\n\\n  data_contamination_detection:\\n    papers:\\n      - kirchenbauer_icml2023  # 基础水印方法\\n      - dathathri_nature2024  # 产品级水印 (SynthID)\\n      - sander_neurips2024  # 水印放射性传播\\n      - mitchell_icml2023  # DetectGPT 概率曲率检测\\n      - shi_iclr2024  # Min-K% 预训练数据检测\\n    relevance: >\\n      合成数据检测与 collapse 监控互补：他们回答\\\"是否有合成数据\\\"，\\n      我们回答\\\"合成数据造成了多严重的 collapse\\\"。\\n\", \"total_chars\": 26925, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "b0fa4026-70b3-4120-bb47-a2d38fa80c66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 42_

```json
{
  "type": "last-prompt",
  "leafUuid": "57e3fa9f-8624-4659-b88a-7ff1df474464",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Compile bibliography file for paper citations",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b"
}
```

---

### Assistant

_source line 44 · 2026-05-15T02:12:58.202Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent! Now I have very detailed information from the literature_map.yaml. Let me compile all the citation keys and their corresponding information.

Let me go through the 44 unique citation keys and map them to the entries in the literature map:

1. **Shumailov2024** → shumailov_nature2024 in lit map: "AI Models Collapse When Trained on Recursively Generated Data", Ilia Shumailov et al., Nature 2024, 631, 755-759
2. **shumailov2024ai** → Same paper, different key


3. **Alemohammad2024** → alemohammad_iclr2024: "Self-Consuming Generative Models Go MAD", ICLR 2024
4. **Dohmatob2025** → dohmatob_iclr2025: "Strong Model Collapse", ICLR 2025 (Spotlight)
5. **Dohmatob2024_tails** → dohmatob_icml2024: "A Tale of Tails: Model Collapse as a Change of Scaling Laws", ICML 2024
6. **Fu2024_icml** → fu_icml2024: "Towards..." (entry appears to be cut off in the source)

Continuing to map the remaining citation keys to their full bibliographic details... Continuing through the bibliography with more recent work on model collapse and synthetic data verification, including papers on self-correcting training loops and methods to escape collapse through data validation. Continuing through the reference list with more recent papers on spectral properties and training dynamics, including work on scaling laws, singular value importance, transformer lifecycle analysis, and curriculum learning approaches. Continuing through the watermarking and detection literature—I'm cataloging papers on identifying LLM outputs through watermarking techniques and detecting pretraining data, including work on radioactive models and detection methods like DetectGPT, along with major dataset papers. I've got solid information from the literature map for most of these papers, so I'm focusing on tracking down the full author lists for the ones I'm less certain about—Shumailov, Dohmatob, Seddik, Feng, Zibakhsh, Bakshi, Liehr, and Chen's data scaling paper.

For the remaining papers, I need to verify arXiv identifiers where they're missing, confirm conference booktitles, and fill in exact publication details for a few older papers like the QLora and HellaSwag work. I'll batch-search these in parallel to get everything I need for accurate BibTeX entries. I need to clarify whether "Chen Liu" is a single author or two separate authors for that paper, then I'll organize these verification tasks into parallel search groups to efficiently confirm all the missing details at once.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57e3fa9f-8624-4659-b88a-7ff1df474464",
  "isSidechain": false,
  "requestId": "req_011Cb3YX3Jc9ikrXhVWsX4iK",
  "type": "assistant",
  "uuid": "b0ce8622-af17-4418-a4cd-94a0196b2d05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L19KA2SXUrFcSwucZhxQkJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18143,
      "cache_read_input_tokens": 45701,
      "output_tokens": 2786,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18143,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2786,
          "cache_read_input_tokens": 45701,
          "cache_creation_input_tokens": 18143,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18143
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

_source line 45 · 2026-05-15T02:12:58.210Z_

I've extracted all 44 unique citation keys. Now I need to verify details for several papers via web search. Let me load the WebSearch tool and launch parallel verification agents.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0ce8622-af17-4418-a4cd-94a0196b2d05",
  "isSidechain": false,
  "requestId": "req_011Cb3YX3Jc9ikrXhVWsX4iK",
  "type": "assistant",
  "uuid": "a753793d-19e8-4396-b532-5c8aeed622e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L19KA2SXUrFcSwucZhxQkJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18143,
      "cache_read_input_tokens": 45701,
      "output_tokens": 2786,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18143,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2786,
          "cache_read_input_tokens": 45701,
          "cache_creation_input_tokens": 18143,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18143
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

_source line 46 · 2026-05-15T02:12:58.314Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WnoJfLLBqSH9TrrpmZrA9t`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a753793d-19e8-4396-b532-5c8aeed622e7",
  "isSidechain": false,
  "requestId": "req_011Cb3YX3Jc9ikrXhVWsX4iK",
  "type": "assistant",
  "uuid": "b5e21056-7d79-44c1-8fcd-5abf8be05eee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L19KA2SXUrFcSwucZhxQkJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18143,
      "cache_read_input_tokens": 45701,
      "output_tokens": 2786,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18143,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2786,
          "cache_read_input_tokens": 45701,
          "cache_creation_input_tokens": 18143,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18143
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

_source line 47 · 2026-05-15T02:12:58.341Z_

<details><summary>↩ Tool result · `toolu_01WnoJfLLBqSH9TrrpmZrA9t`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b5e21056-7d79-44c1-8fcd-5abf8be05eee",
  "isSidechain": false,
  "promptId": "a7003b6e-3a25-4888-837a-59f1925bbd90",
  "type": "user",
  "uuid": "0968d50d-ed6e-4d56-afb7-4b36bb173e35",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 22
  },
  "sourceToolAssistantUUID": "b5e21056-7d79-44c1-8fcd-5abf8be05eee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-15T02:13:01.319Z_

Now let me launch parallel agents to verify paper details in batches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0968d50d-ed6e-4d56-afb7-4b36bb173e35",
  "isSidechain": false,
  "requestId": "req_011Cb3Yaywogmwy3wMJ57RhW",
  "type": "assistant",
  "uuid": "8961f6be-8f48-4e8c-9615-e5a4b45a788c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AwvPK5c1LxKqDiwxd5GVZm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3311,
      "cache_read_input_tokens": 63844,
      "output_tokens": 2345,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3311,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2345,
          "cache_read_input_tokens": 63844,
          "cache_creation_input_tokens": 3311,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3311
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

_source line 49 · 2026-05-15T02:13:09.563Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01GGB984cWMBCKtFBrgiX5NL`</summary>

```json
{
  "description": "Verify papers batch 1",
  "prompt": "I'm building a BibTeX file for an ML research paper. I need you to verify the exact details for these papers using WebSearch. For each paper, find: full author list, exact title, year, venue (conference/journal), and arXiv ID if applicable. Return the information in a structured format.\n\nPapers to verify:\n\n1. \"AI Models Collapse When Trained on Recursively Generated Data\" - Shumailov et al., Nature 2024\n2. \"Strong Model Collapse\" - Dohmatob, Feng et al., ICLR 2025 \n3. \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\" - Dohmatob et al., ICML 2024\n4. \"Towards Theoretical Understandings of Self-Consuming Generative Models\" - Fu et al., ICML 2024\n5. \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\" - Seddik et al., arXiv 2404.05090\n6. \"QLoRA: Efficient Finetuning of Quantized LLMs\" - Dettmers et al., NeurIPS 2023\n7. \"Pointer Sentinel Mixture Models\" - Merity et al., ICLR 2017\n8. \"HellaSwag: Can a Machine Really Finish Your Sentence?\" - Zellers et al., ACL 2019\n\nBe concise - just the facts for each paper.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8961f6be-8f48-4e8c-9615-e5a4b45a788c",
  "isSidechain": false,
  "requestId": "req_011Cb3Yaywogmwy3wMJ57RhW",
  "type": "assistant",
  "uuid": "777a0648-14af-47d8-8ca9-5c5c13acbd4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AwvPK5c1LxKqDiwxd5GVZm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3311,
      "cache_read_input_tokens": 63844,
      "output_tokens": 2345,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3311,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2345,
          "cache_read_input_tokens": 63844,
          "cache_creation_input_tokens": 3311,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3311
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

_source line 50 · 2026-05-15T02:13:16.803Z_

<details open><summary>🔧 Tool call — Agent · `toolu_014xDtXNR4AGVFd6FJBDiXAu`</summary>

```json
{
  "description": "Verify papers batch 2",
  "prompt": "I'm building a BibTeX file for an ML research paper. I need you to verify the exact details for these papers using WebSearch. For each paper, find: full author list, exact title, year, venue, and arXiv ID if applicable. Return the information in a structured format.\n\nPapers to verify:\n\n1. \"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification\" - Feng et al., ICLR 2025\n2. \"ForTIFAI: Fending Off Recursive Training Induced Failure for AI Model Collapse\" - Zibakhsh Shabgahi et al., arXiv 2509.08972\n3. \"From Collapse to Improvement\" - Bakshi et al., arXiv 2602.10531\n4. \"Spectral Scaling Laws in Language Models\" - Liehr et al., EMNLP 2025, arXiv 2510.00537\n5. \"A Closer Look at Model Collapse\" - Shi et al., NeurIPS 2025 Spotlight\n6. \"Position: Model Collapse Does Not Mean What You Think\" - Schaeffer, Kazdan et al., arXiv 2503.03150\n7. \"Is Model Collapse Inevitable?\" - Gerstgrasser, Schaeffer et al., arXiv 2404.01413\n8. \"Collapse or Thrive?\" - Kazdan et al., arXiv 2410.16713\n\nBe concise - just the facts for each paper.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "777a0648-14af-47d8-8ca9-5c5c13acbd4b",
  "isSidechain": false,
  "requestId": "req_011Cb3Yaywogmwy3wMJ57RhW",
  "type": "assistant",
  "uuid": "274c7e1c-b7d9-4d3f-998e-6409b7ac89e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AwvPK5c1LxKqDiwxd5GVZm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3311,
      "cache_read_input_tokens": 63844,
      "output_tokens": 2345,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3311,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2345,
          "cache_read_input_tokens": 63844,
          "cache_creation_input_tokens": 3311,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3311
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

_source line 51 · 2026-05-15T02:13:24.726Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01LrhE4rBLqMtsHGt8EnQa6F`</summary>

```json
{
  "description": "Verify papers batch 3",
  "prompt": "I'm building a BibTeX file for an ML research paper. I need you to verify the exact details for these papers using WebSearch. For each paper, find: full author list, exact title, year, venue, and arXiv ID if applicable. Return the information in a structured format.\n\nPapers to verify:\n\n1. \"Self-Consuming Generative Models Go MAD\" - Alemohammad et al., ICLR 2024\n2. \"Escaping Model Collapse via Synthetic Data Verification\" - Yi et al., arXiv 2510.16657\n3. \"Self-Correcting Self-Consuming Loops for Generative Model Training\" - Gillman et al., ICML 2024\n4. \"Predicting Trends in the Quality of State-of-the-Art Neural Networks without Access to Training or Testing Data\" - Martin & Mahoney, Nature Communications 2021\n5. \"Stable Rank Normalization for Improved Generalization in Neural Networks and GANs\" - Sanyal, Torr & Dokania, ICLR 2020\n6. \"Assessing Neural Network Representations During Training Using Noise-Resilient Diffusion Spectral Entropy\" - Chen & Liu, IEEE CISS 2024\n7. \"SIGMA: Scalable Spectral Insights for LLM Model Collapse\" - Gu et al., arXiv 2601.03385\n8. \"Monitoring Neural Training with Topology\" - Kalinowski, arXiv 2604.26984\n\nBe concise - just the facts for each paper.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "274c7e1c-b7d9-4d3f-998e-6409b7ac89e3",
  "isSidechain": false,
  "requestId": "req_011Cb3Yaywogmwy3wMJ57RhW",
  "type": "assistant",
  "uuid": "10abb7ac-19d4-4629-ad0a-a83940c129fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AwvPK5c1LxKqDiwxd5GVZm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3311,
      "cache_read_input_tokens": 63844,
      "output_tokens": 2345,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3311,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2345,
          "cache_read_input_tokens": 63844,
          "cache_creation_input_tokens": 3311,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3311
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

_source line 52 · 2026-05-15T02:13:34.899Z_

<details open><summary>🔧 Tool call — Agent · `toolu_016n39MJpt5zzJGQvQ24gak6`</summary>

```json
{
  "description": "Verify papers batch 4",
  "prompt": "I'm building a BibTeX file for an ML research paper. I need you to verify the exact details for these papers using WebSearch. For each paper, find: full author list, exact title, year, venue, and arXiv ID if applicable. Return the information in a structured format.\n\nPapers to verify:\n\n1. \"Predicting LLM Compression Degradation from Spectral Statistics\" - Xu, arXiv 2604.18085\n2. \"Nonlinear Random Matrix Theory for Deep Learning\" - Pennington & Worah, NeurIPS 2017\n3. \"Approaching Deep Learning through the Spectral Dynamics of Weights\" - Yunis, Patel et al., arXiv 2408.11804\n4. \"AlphaPruning: Using Heavy-Tailed Self Regularization Theory for Improved Layer-wise Pruning of Large Language Models\" - Lu et al., NeurIPS 2024\n5. \"How Instruction and Reasoning Data shape Post-Training: Data Quality through the Lens of Layer-wise Gradients\" - Ming Li et al., arXiv 2504.10766\n6. \"Curriculum Learning for LLM Pretraining: An Analysis of Learning Dynamics\" - Elgaar & Amiri, arXiv 2601.21698\n7. \"Spectral Alignment as Predictor of Loss Explosion in Neural Network Training\" - Qiu et al., arXiv 2510.04202\n8. \"A Scalable Measure of Loss Landscape Curvature for Analyzing the Training Dynamics of LLMs\" - Kalra et al., arXiv 2601.16979\n9. \"The Spectral Lifecycle of Transformer Training\" - Liu, arXiv 2604.22778\n10. \"Small Singular Values Matter: A Random Matrix Analysis of Transformer Models\" - Staats et al., arXiv 2410.17770\n\nBe concise - just the facts for each paper.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10abb7ac-19d4-4629-ad0a-a83940c129fd",
  "isSidechain": false,
  "requestId": "req_011Cb3Yaywogmwy3wMJ57RhW",
  "type": "assistant",
  "uuid": "8f693cf4-8023-4298-bfa2-83d675fbbc9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AwvPK5c1LxKqDiwxd5GVZm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3311,
      "cache_read_input_tokens": 63844,
      "output_tokens": 2345,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3311,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2345,
          "cache_read_input_tokens": 63844,
          "cache_creation_input_tokens": 3311,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3311
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

_source line 53 · 2026-05-15T02:13:42.861Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01XSU7nhHCC1vCBrTismAMn6`</summary>

```json
{
  "description": "Verify papers batch 5",
  "prompt": "I'm building a BibTeX file for an ML research paper. I need you to verify the exact details for these papers using WebSearch. For each paper, find: full author list, exact title, year, venue, and arXiv ID if applicable. Return the information in a structured format.\n\nPapers to verify:\n\n1. \"A Watermark for Large Language Models\" - Kirchenbauer et al., ICML 2023\n2. \"Scalable Watermarking for Identifying Large Language Model Outputs\" (SynthID-Text) - Dathathri et al., Nature 2024\n3. \"Watermarking Makes Language Models Radioactive\" - Sander et al., NeurIPS 2024\n4. \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\" - Mitchell et al., ICML 2023\n5. \"Detecting Pretraining Data from Large Language Models\" (Min-K% Prob) - Shi et al., ICLR 2024\n6. \"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale\" - Penedo et al., arXiv 2406.17557\n7. \"The LLM Data Auditor\" - Zhang et al., arXiv 2601.17717\n8. \"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI\" - Wyss et al., arXiv 2410.12341\n9. \"Data Value in the Age of Scaling\" - Wang et al., arXiv 2511.13640\n\nBe concise - just the facts for each paper.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f693cf4-8023-4298-bfa2-83d675fbbc9a",
  "isSidechain": false,
  "requestId": "req_011Cb3Yaywogmwy3wMJ57RhW",
  "type": "assistant",
  "uuid": "c2d19e74-646e-4ce6-aa2d-1575ec1536fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AwvPK5c1LxKqDiwxd5GVZm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3311,
      "cache_read_input_tokens": 63844,
      "output_tokens": 2345,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3311,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2345,
          "cache_read_input_tokens": 63844,
          "cache_creation_input_tokens": 3311,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3311
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

_source line 54 · 2026-05-15T02:13:57.539Z_

<details><summary>↩ Tool result · `toolu_01GGB984cWMBCKtFBrgiX5NL`</summary>

```text
Here are the verified details for all 8 papers:

---

**1. AI Models Collapse When Trained on Recursively Generated Data**
- **Authors:** Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, Yarin Gal
- **Year:** 2024
- **Venue:** Nature, vol. 631, pp. 755--759
- **arXiv:** 2305.17493

---

**2. Strong Model Collapse**
- **Authors:** Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe
- **Year:** 2025
- **Venue:** ICLR 2025 (Spotlight)
- **arXiv:** 2410.04840

---

**3. A Tale of Tails: Model Collapse as a Change of Scaling Laws**
- **Authors:** Elvis Dohmatob, Yunzhen Feng, Pu Yang, Francois Charton, Julia Kempe
- **Year:** 2024
- **Venue:** ICML 2024 (Proceedings of Machine Learning Research, vol. 235, pp. 11165--11197)
- **arXiv:** 2402.07043

---

**4. Towards Theoretical Understandings of Self-Consuming Generative Models**
- **Authors:** Shi Fu, Sen Zhang, Yingjie Wang, Xinmei Tian, Dacheng Tao
- **Year:** 2024
- **Venue:** ICML 2024
- **arXiv:** 2402.11778

---

**5. How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse**
- **Authors:** Mohamed El Amine Seddik, Suei-Wen Chen, Soufiane Hayou, Pierre Youssef, Merouane Debbah
- **Year:** 2024
- **Venue:** arXiv preprint
- **arXiv:** 2404.05090

---

**6. QLoRA: Efficient Finetuning of Quantized LLMs**
- **Authors:** Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, Luke Zettlemoyer
- **Year:** 2023
- **Venue:** NeurIPS 2023
- **arXiv:** 2305.14314

---

**7. Pointer Sentinel Mixture Models**
- **Authors:** Stephen Merity, Caiming Xiong, James Bradbury, Richard Socher
- **Year:** 2017
- **Venue:** ICLR 2017
- **arXiv:** 1609.07843

---

**8. HellaSwag: Can a Machine Really Finish Your Sentence?**
- **Authors:** Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali Farhadi, Yejin Choi
- **Year:** 2019
- **Venue:** ACL 2019 (Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics)
- **arXiv:** 1905.07830

---

All details you provided were correct. The only note: paper #5 (Seddik et al.) appears to remain an arXiv preprint -- I did not find evidence of formal conference/journal publication.

Sources:
- [Nature - Shumailov et al. 2024](https://www.nature.com/articles/s41586-024-07566-y)
- [OpenReview - Strong Model Collapse](https://openreview.net/forum?id=et5l9qPUhm)
- [PMLR - A Tale of Tails](https://proceedings.mlr.press/v235/dohmatob24b.html)
- [arXiv - Self-Consuming Generative Models](https://arxiv.org/abs/2402.11778)
- [arXiv - How Bad is Training on Synthetic Data](https://arxiv.org/abs/2404.05090)
- [NeurIPS - QLoRA](https://proceedings.neurips.cc/paper_files/paper/2023/hash/1feb87871436031bdc0f2beaa62a049b-Abstract-Conference.html)
- [OpenReview - Pointer Sentinel Mixture Models](https://openreview.net/forum?id=Byj72udxe)
- [ACL Anthology - HellaSwag](https://aclanthology.org/P19-1472/)

agentId: aebaa3c7c8ef0c330 (use SendMessage with to: 'aebaa3c7c8ef0c330' to continue this agent)
&lt;usage>total_tokens: 23751
tool_uses: 9
duration_ms: 47971&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "777a0648-14af-47d8-8ca9-5c5c13acbd4b",
  "isSidechain": false,
  "promptId": "a7003b6e-3a25-4888-837a-59f1925bbd90",
  "type": "user",
  "uuid": "fe77223a-3f67-4150-8dbb-c5547e46ab02",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm building a BibTeX file for an ML research paper. I need you to verify the exact details for these papers using WebSearch. For each paper, find: full author list, exact title, year, venue (conference/journal), and arXiv ID if applicable. Return the information in a structured format.\n\nPapers to verify:\n\n1. \"AI Models Collapse When Trained on Recursively Generated Data\" - Shumailov et al., Nature 2024\n2. \"Strong Model Collapse\" - Dohmatob, Feng et al., ICLR 2025 \n3. \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\" - Dohmatob et al., ICML 2024\n4. \"Towards Theoretical Understandings of Self-Consuming Generative Models\" - Fu et al., ICML 2024\n5. \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\" - Seddik et al., arXiv 2404.05090\n6. \"QLoRA: Efficient Finetuning of Quantized LLMs\" - Dettmers et al., NeurIPS 2023\n7. \"Pointer Sentinel Mixture Models\" - Merity et al., ICLR 2017\n8. \"HellaSwag: Can a Machine Really Finish Your Sentence?\" - Zellers et al., ACL 2019\n\nBe concise - just the facts for each paper.",
    "agentId": "aebaa3c7c8ef0c330",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the verified details for all 8 papers:\n\n---\n\n**1. AI Models Collapse When Trained on Recursively Generated Data**\n- **Authors:** Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, Yarin Gal\n- **Year:** 2024\n- **Venue:** Nature, vol. 631, pp. 755--759\n- **arXiv:** 2305.17493\n\n---\n\n**2. Strong Model Collapse**\n- **Authors:** Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe\n- **Year:** 2025\n- **Venue:** ICLR 2025 (Spotlight)\n- **arXiv:** 2410.04840\n\n---\n\n**3. A Tale of Tails: Model Collapse as a Change of Scaling Laws**\n- **Authors:** Elvis Dohmatob, Yunzhen Feng, Pu Yang, Francois Charton, Julia Kempe\n- **Year:** 2024\n- **Venue:** ICML 2024 (Proceedings of Machine Learning Research, vol. 235, pp. 11165--11197)\n- **arXiv:** 2402.07043\n\n---\n\n**4. Towards Theoretical Understandings of Self-Consuming Generative Models**\n- **Authors:** Shi Fu, Sen Zhang, Yingjie Wang, Xinmei Tian, Dacheng Tao\n- **Year:** 2024\n- **Venue:** ICML 2024\n- **arXiv:** 2402.11778\n\n---\n\n**5. How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse**\n- **Authors:** Mohamed El Amine Seddik, Suei-Wen Chen, Soufiane Hayou, Pierre Youssef, Merouane Debbah\n- **Year:** 2024\n- **Venue:** arXiv preprint\n- **arXiv:** 2404.05090\n\n---\n\n**6. QLoRA: Efficient Finetuning of Quantized LLMs**\n- **Authors:** Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, Luke Zettlemoyer\n- **Year:** 2023\n- **Venue:** NeurIPS 2023\n- **arXiv:** 2305.14314\n\n---\n\n**7. Pointer Sentinel Mixture Models**\n- **Authors:** Stephen Merity, Caiming Xiong, James Bradbury, Richard Socher\n- **Year:** 2017\n- **Venue:** ICLR 2017\n- **arXiv:** 1609.07843\n\n---\n\n**8. HellaSwag: Can a Machine Really Finish Your Sentence?**\n- **Authors:** Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali Farhadi, Yejin Choi\n- **Year:** 2019\n- **Venue:** ACL 2019 (Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics)\n- **arXiv:** 1905.07830\n\n---\n\nAll details you provided were correct. The only note: paper #5 (Seddik et al.) appears to remain an arXiv preprint -- I did not find evidence of formal conference/journal publication.\n\nSources:\n- [Nature - Shumailov et al. 2024](https://www.nature.com/articles/s41586-024-07566-y)\n- [OpenReview - Strong Model Collapse](https://openreview.net/forum?id=et5l9qPUhm)\n- [PMLR - A Tale of Tails](https://proceedings.mlr.press/v235/dohmatob24b.html)\n- [arXiv - Self-Consuming Generative Models](https://arxiv.org/abs/2402.11778)\n- [arXiv - How Bad is Training on Synthetic Data](https://arxiv.org/abs/2404.05090)\n- [NeurIPS - QLoRA](https://proceedings.neurips.cc/paper_files/paper/2023/hash/1feb87871436031bdc0f2beaa62a049b-Abstract-Conference.html)\n- [OpenReview - Pointer Sentinel Mixture Models](https://openreview.net/forum?id=Byj72udxe)\n- [ACL Anthology - HellaSwag](https://aclanthology.org/P19-1472/)"
      }
    ],
    "totalDurationMs": 47971,
    "totalTokens": 23751,
    "totalToolUseCount": 9,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6767,
      "cache_read_input_tokens": 15848,
      "output_tokens": 1135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6767
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1135,
          "cache_read_input_tokens": 15848,
          "cache_creation_input_tokens": 6767,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6767,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 9
    }
  },
  "sourceToolAssistantUUID": "777a0648-14af-47d8-8ca9-5c5c13acbd4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 55_

```json
{
  "type": "last-prompt",
  "leafUuid": "fe77223a-3f67-4150-8dbb-c5547e46ab02",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b"
}
```

---

### Runtime record

_source line 56_

```json
{
  "type": "ai-title",
  "aiTitle": "Compile bibliography file for paper citations",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b"
}
```

---

### Tool result

_source line 57 · 2026-05-15T02:14:20.814Z_

<details><summary>↩ Tool result · `toolu_01LrhE4rBLqMtsHGt8EnQa6F`</summary>

```text
Here are the verified details for all 8 papers:

---

**1. Self-Consuming Generative Models Go MAD**
- **Authors:** Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard G. Baraniuk
- **Title:** Self-Consuming Generative Models Go MAD
- **Year:** 2024
- **Venue:** ICLR 2024
- **arXiv:** 2307.01850

**2. Escaping Model Collapse via Synthetic Data Verification**
- **Authors:** Bingji Yi, Qiyuan Liu, Yuwei Cheng, Haifeng Xu
- **Title:** Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence
- **Year:** 2025
- **Venue:** arXiv preprint (also on OpenReview)
- **arXiv:** 2510.16657

**3. Self-Correcting Self-Consuming Loops for Generative Model Training**
- **Authors:** Nate Gillman, Michael Freeman, Daksh Aggarwal, Chia-Hong Hsu, Calvin Luo, Yonglong Tian, Chen Sun
- **Title:** Self-Correcting Self-Consuming Loops for Generative Model Training
- **Year:** 2024
- **Venue:** ICML 2024 (Proceedings of the 41st International Conference on Machine Learning, pp. 15646-15677)
- **arXiv:** 2402.07087

**4. Predicting Trends in the Quality of State-of-the-Art Neural Networks...**
- **Authors:** Charles H. Martin, Tongsu (Serena) Peng, Michael W. Mahoney
- **Title:** Predicting trends in the quality of state-of-the-art neural networks without access to training or testing data
- **Year:** 2021
- **Venue:** Nature Communications, vol. 12, article 4122
- **arXiv:** 2002.06716
- **Note:** Your citation said "Martin & Mahoney" but there is a third author, Tongsu (Serena) Peng.

**5. Stable Rank Normalization for Improved Generalization in Neural Networks and GANs**
- **Authors:** Amartya Sanyal, Philip H.S. Torr, Puneet K. Dokania
- **Title:** Stable Rank Normalization for Improved Generalization in Neural Networks and GANs
- **Year:** 2020
- **Venue:** ICLR 2020
- **arXiv:** 1906.04659

**6. Assessing Neural Network Representations During Training Using Noise-Resilient Diffusion Spectral Entropy**
- **Authors:** Danqi Liao, Chen Liu, Benjamin W. Christensen, Alexander Tong, Guillaume Huguet, Guy Wolf, Maximilian Nickel, Ian Adelstein, Smita Krishnaswamy
- **Title:** Assessing Neural Network Representations During Training Using Noise-Resilient Diffusion Spectral Entropy
- **Year:** 2024
- **Venue:** IEEE CISS 2024 (58th Annual Conference on Information Sciences and Systems); also appeared at ICML Workshop 2023
- **arXiv:** 2312.04823
- **Note:** Your citation said "Chen & Liu" but Chen Liu is a single author (not two). The first author is Danqi Liao; the paper has 9 authors total.

**7. SIGMA: Scalable Spectral Insights for LLM Model Collapse**
- **Authors:** Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, Alexander Aue
- **Title:** SIGMA: Scalable Spectral Insights for LLM Model Collapse
- **Year:** 2026
- **Venue:** arXiv preprint
- **arXiv:** 2601.03385

**8. Monitoring Neural Training with Topology**
- **Authors:** Alexander Kalinowski
- **Title:** Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index
- **Year:** 2026
- **Venue:** arXiv preprint
- **arXiv:** 2604.26984
- **Note:** The full title includes the subtitle "A Footprint-Predictable Collapse Index."

---

Key corrections to flag:
- Paper 4 has a third author (Tongsu Peng) you may have omitted.
- Paper 6: "Chen Liu" is one person (first+last name), not two authors. The first author is Danqi Liao, and there are 9 authors total.
- Paper 8's full title is longer than what you listed.

Sources:
- [Paper 1 - OpenReview](https://openreview.net/forum?id=ShjMHfmPs0)
- [Paper 2 - arXiv](https://arxiv.org/abs/2510.16657)
- [Paper 3 - PMLR](https://proceedings.mlr.press/v235/gillman24a.html)
- [Paper 4 - Nature Communications](https://www.nature.com/articles/s41467-021-24025-8)
- [Paper 5 - arXiv](https://arxiv.org/abs/1906.04659)
- [Paper 6 - arXiv](https://arxiv.org/abs/2312.04823)
- [Paper 7 - arXiv](https://arxiv.org/abs/2601.03385)
- [Paper 8 - arXiv](https://arxiv.org/abs/2604.26984)

agentId: afe3b726861e7ce81 (use SendMessage with to: 'afe3b726861e7ce81' to continue this agent)
&lt;usage>total_tokens: 26571
tool_uses: 11
duration_ms: 56085&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10abb7ac-19d4-4629-ad0a-a83940c129fd",
  "isSidechain": false,
  "promptId": "a7003b6e-3a25-4888-837a-59f1925bbd90",
  "type": "user",
  "uuid": "8c5fa67e-cba0-4959-87a6-eb2aa1b1e681",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm building a BibTeX file for an ML research paper. I need you to verify the exact details for these papers using WebSearch. For each paper, find: full author list, exact title, year, venue, and arXiv ID if applicable. Return the information in a structured format.\n\nPapers to verify:\n\n1. \"Self-Consuming Generative Models Go MAD\" - Alemohammad et al., ICLR 2024\n2. \"Escaping Model Collapse via Synthetic Data Verification\" - Yi et al., arXiv 2510.16657\n3. \"Self-Correcting Self-Consuming Loops for Generative Model Training\" - Gillman et al., ICML 2024\n4. \"Predicting Trends in the Quality of State-of-the-Art Neural Networks without Access to Training or Testing Data\" - Martin & Mahoney, Nature Communications 2021\n5. \"Stable Rank Normalization for Improved Generalization in Neural Networks and GANs\" - Sanyal, Torr & Dokania, ICLR 2020\n6. \"Assessing Neural Network Representations During Training Using Noise-Resilient Diffusion Spectral Entropy\" - Chen & Liu, IEEE CISS 2024\n7. \"SIGMA: Scalable Spectral Insights for LLM Model Collapse\" - Gu et al., arXiv 2601.03385\n8. \"Monitoring Neural Training with Topology\" - Kalinowski, arXiv 2604.26984\n\nBe concise - just the facts for each paper.",
    "agentId": "afe3b726861e7ce81",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the verified details for all 8 papers:\n\n---\n\n**1. Self-Consuming Generative Models Go MAD**\n- **Authors:** Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard G. Baraniuk\n- **Title:** Self-Consuming Generative Models Go MAD\n- **Year:** 2024\n- **Venue:** ICLR 2024\n- **arXiv:** 2307.01850\n\n**2. Escaping Model Collapse via Synthetic Data Verification**\n- **Authors:** Bingji Yi, Qiyuan Liu, Yuwei Cheng, Haifeng Xu\n- **Title:** Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence\n- **Year:** 2025\n- **Venue:** arXiv preprint (also on OpenReview)\n- **arXiv:** 2510.16657\n\n**3. Self-Correcting Self-Consuming Loops for Generative Model Training**\n- **Authors:** Nate Gillman, Michael Freeman, Daksh Aggarwal, Chia-Hong Hsu, Calvin Luo, Yonglong Tian, Chen Sun\n- **Title:** Self-Correcting Self-Consuming Loops for Generative Model Training\n- **Year:** 2024\n- **Venue:** ICML 2024 (Proceedings of the 41st International Conference on Machine Learning, pp. 15646-15677)\n- **arXiv:** 2402.07087\n\n**4. Predicting Trends in the Quality of State-of-the-Art Neural Networks...**\n- **Authors:** Charles H. Martin, Tongsu (Serena) Peng, Michael W. Mahoney\n- **Title:** Predicting trends in the quality of state-of-the-art neural networks without access to training or testing data\n- **Year:** 2021\n- **Venue:** Nature Communications, vol. 12, article 4122\n- **arXiv:** 2002.06716\n- **Note:** Your citation said \"Martin & Mahoney\" but there is a third author, Tongsu (Serena) Peng.\n\n**5. Stable Rank Normalization for Improved Generalization in Neural Networks and GANs**\n- **Authors:** Amartya Sanyal, Philip H.S. Torr, Puneet K. Dokania\n- **Title:** Stable Rank Normalization for Improved Generalization in Neural Networks and GANs\n- **Year:** 2020\n- **Venue:** ICLR 2020\n- **arXiv:** 1906.04659\n\n**6. Assessing Neural Network Representations During Training Using Noise-Resilient Diffusion Spectral Entropy**\n- **Authors:** Danqi Liao, Chen Liu, Benjamin W. Christensen, Alexander Tong, Guillaume Huguet, Guy Wolf, Maximilian Nickel, Ian Adelstein, Smita Krishnaswamy\n- **Title:** Assessing Neural Network Representations During Training Using Noise-Resilient Diffusion Spectral Entropy\n- **Year:** 2024\n- **Venue:** IEEE CISS 2024 (58th Annual Conference on Information Sciences and Systems); also appeared at ICML Workshop 2023\n- **arXiv:** 2312.04823\n- **Note:** Your citation said \"Chen & Liu\" but Chen Liu is a single author (not two). The first author is Danqi Liao; the paper has 9 authors total.\n\n**7. SIGMA: Scalable Spectral Insights for LLM Model Collapse**\n- **Authors:** Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, Alexander Aue\n- **Title:** SIGMA: Scalable Spectral Insights for LLM Model Collapse\n- **Year:** 2026\n- **Venue:** arXiv preprint\n- **arXiv:** 2601.03385\n\n**8. Monitoring Neural Training with Topology**\n- **Authors:** Alexander Kalinowski\n- **Title:** Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index\n- **Year:** 2026\n- **Venue:** arXiv preprint\n- **arXiv:** 2604.26984\n- **Note:** The full title includes the subtitle \"A Footprint-Predictable Collapse Index.\"\n\n---\n\nKey corrections to flag:\n- Paper 4 has a third author (Tongsu Peng) you may have omitted.\n- Paper 6: \"Chen Liu\" is one person (first+last name), not two authors. The first author is Danqi Liao, and there are 9 authors total.\n- Paper 8's full title is longer than what you listed.\n\nSources:\n- [Paper 1 - OpenReview](https://openreview.net/forum?id=ShjMHfmPs0)\n- [Paper 2 - arXiv](https://arxiv.org/abs/2510.16657)\n- [Paper 3 - PMLR](https://proceedings.mlr.press/v235/gillman24a.html)\n- [Paper 4 - Nature Communications](https://www.nature.com/articles/s41467-021-24025-8)\n- [Paper 5 - arXiv](https://arxiv.org/abs/1906.04659)\n- [Paper 6 - arXiv](https://arxiv.org/abs/2312.04823)\n- [Paper 7 - arXiv](https://arxiv.org/abs/2601.03385)\n- [Paper 8 - arXiv](https://arxiv.org/abs/2604.26984)"
      }
    ],
    "totalDurationMs": 56085,
    "totalTokens": 26571,
    "totalToolUseCount": 11,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2392,
      "cache_read_input_tokens": 22729,
      "output_tokens": 1449,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2392
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1449,
          "cache_read_input_tokens": 22729,
          "cache_creation_input_tokens": 2392,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2392,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 11
    }
  },
  "sourceToolAssistantUUID": "10abb7ac-19d4-4629-ad0a-a83940c129fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-15T02:15:14.064Z_

<details><summary>↩ Tool result · `toolu_014xDtXNR4AGVFd6FJBDiXAu`</summary>

```text
Here are the verified details for all 8 papers:

---

**1. Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification**
- **Authors:** Yunzhen Feng, Elvis Dohmatob, Pu Yang, Francois Charton, Julia Kempe
- **Year:** 2024 (arXiv), 2025 (conference)
- **Venue:** ICLR 2025 (confirmed)
- **arXiv:** 2406.07515
- **Note:** Your provided details are correct.

**2. ForTIFAI: Fending Off Recursive Training Induced Failure for AI Model Collapse**
- **Authors:** Soheil Zibakhsh Shabgahi, Pedram Aghazadeh, Azalia Mirhoseini, Farinaz Koushanfar
- **Year:** 2025
- **Venue:** arXiv preprint (no confirmed venue acceptance found)
- **arXiv:** 2509.08972 (confirmed)
- **Note:** The title changed between versions. v1 used "...for AI Models"; the current version uses "...for AI Model Collapse". No venue beyond arXiv confirmed.

**3. From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources**
- **Authors:** Soham Bakshi, Sunrit Chakraborty
- **Year:** 2026
- **Venue:** arXiv preprint
- **arXiv:** 2602.10531 (confirmed)
- **Note:** Your details are correct. Only 2 authors.

**4. Spectral Scaling Laws in Language Models: How Effectively Do Feed-Forward Networks Use Their Latent Space?**
- **Authors:** Nandan Kumar Jha, Brandon Reagen
- **Year:** 2025
- **Venue:** EMNLP 2025 (confirmed, ACL Anthology: 2025.emnlp-main.1776)
- **arXiv:** 2510.00537 (confirmed)
- **DISCREPANCY:** The authors are Jha and Reagen, **not** "Liehr et al." No author named Liehr is associated with this paper. Please verify this is the correct paper you intended.

**5. A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective**
- **Authors:** Lianghe Shi\*, Meng Wu\*, Huijie Zhang, Zekai Zhang, Molei Tao, Qing Qu (\*equal contribution)
- **Year:** 2025
- **Venue:** NeurIPS 2025 Spotlight (confirmed, top 3.2%)
- **arXiv:** 2509.16499
- **Note:** First author is Shi (Lianghe Shi), consistent with "Shi et al." Your details are correct.

**6. Position: Model Collapse Does Not Mean What You Think**
- **Authors:** Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, Sanmi Koyejo
- **Year:** 2025
- **Venue:** arXiv preprint; submitted to NeurIPS 2025 per OpenReview. An invited talk on this topic was given at ICLR 2025.
- **arXiv:** 2503.03150 (confirmed)
- **Note:** Lead author is Schaeffer, not "Schaeffer, Kazdan" -- Kazdan is second author.

**7. Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data**
- **Authors:** Matthias Gerstgrasser, Rylan Schaeffer, Apratim Dey, Rafael Rafailov, Henry Sleight, John Hughes, Tomasz Korbak, Rajashree Agrawal, Dhruv Bhandarkar Pai, Andrey Gromov, Daniel A. Roberts, Diyi Yang, David L. Donoho, Sanmi Koyejo
- **Year:** 2024
- **Venue:** COLM 2024 (First Conference on Language Modeling), **not** just arXiv
- **arXiv:** 2404.01413 (confirmed)

**8. Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World**
- **Authors:** Joshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, David L. Donoho, Sanmi Koyejo
- **Year:** 2025
- **Venue:** ICML 2025 (PMLR 267:29469-29494), **not** just arXiv
- **arXiv:** 2410.16713 (confirmed)

---

**Summary of discrepancies from your input:**
- Paper 4: Authors are Jha & Reagen, not "Liehr et al." -- verify this is the right paper.
- Paper 7: Published at COLM 2024, not just arXiv.
- Paper 8: Published at ICML 2025, not just arXiv.

Sources:
- [Paper 1 - arXiv](https://arxiv.org/abs/2406.07515)
- [Paper 2 - arXiv](https://arxiv.org/abs/2509.08972)
- [Paper 3 - arXiv](https://arxiv.org/abs/2602.10531)
- [Paper 4 - arXiv](https://arxiv.org/abs/2510.00537)
- [Paper 4 - ACL Anthology](https://aclanthology.org/2025.emnlp-main.1776/)
- [Paper 5 - arXiv](https://arxiv.org/abs/2509.16499)
- [Paper 6 - arXiv](https://arxiv.org/abs/2503.03150)
- [Paper 7 - arXiv](https://arxiv.org/abs/2404.01413)
- [Paper 7 - OpenReview (COLM 2024)](https://openreview.net/forum?id=5B2K4LRgmz)
- [Paper 8 - arXiv](https://arxiv.org/abs/2410.16713)
- [Paper 8 - PMLR (ICML 2025)](https://proceedings.mlr.press/v267/kazdan25a.html)

agentId: a996017165d69dd1b (use SendMessage with to: 'a996017165d69dd1b' to continue this agent)
&lt;usage>total_tokens: 35641
tool_uses: 21
duration_ms: 117258&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "274c7e1c-b7d9-4d3f-998e-6409b7ac89e3",
  "isSidechain": false,
  "promptId": "a7003b6e-3a25-4888-837a-59f1925bbd90",
  "type": "user",
  "uuid": "08842d6c-6051-43d1-b6bd-65ae1e38ab04",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm building a BibTeX file for an ML research paper. I need you to verify the exact details for these papers using WebSearch. For each paper, find: full author list, exact title, year, venue, and arXiv ID if applicable. Return the information in a structured format.\n\nPapers to verify:\n\n1. \"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification\" - Feng et al., ICLR 2025\n2. \"ForTIFAI: Fending Off Recursive Training Induced Failure for AI Model Collapse\" - Zibakhsh Shabgahi et al., arXiv 2509.08972\n3. \"From Collapse to Improvement\" - Bakshi et al., arXiv 2602.10531\n4. \"Spectral Scaling Laws in Language Models\" - Liehr et al., EMNLP 2025, arXiv 2510.00537\n5. \"A Closer Look at Model Collapse\" - Shi et al., NeurIPS 2025 Spotlight\n6. \"Position: Model Collapse Does Not Mean What You Think\" - Schaeffer, Kazdan et al., arXiv 2503.03150\n7. \"Is Model Collapse Inevitable?\" - Gerstgrasser, Schaeffer et al., arXiv 2404.01413\n8. \"Collapse or Thrive?\" - Kazdan et al., arXiv 2410.16713\n\nBe concise - just the facts for each paper.",
    "agentId": "a996017165d69dd1b",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the verified details for all 8 papers:\n\n---\n\n**1. Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification**\n- **Authors:** Yunzhen Feng, Elvis Dohmatob, Pu Yang, Francois Charton, Julia Kempe\n- **Year:** 2024 (arXiv), 2025 (conference)\n- **Venue:** ICLR 2025 (confirmed)\n- **arXiv:** 2406.07515\n- **Note:** Your provided details are correct.\n\n**2. ForTIFAI: Fending Off Recursive Training Induced Failure for AI Model Collapse**\n- **Authors:** Soheil Zibakhsh Shabgahi, Pedram Aghazadeh, Azalia Mirhoseini, Farinaz Koushanfar\n- **Year:** 2025\n- **Venue:** arXiv preprint (no confirmed venue acceptance found)\n- **arXiv:** 2509.08972 (confirmed)\n- **Note:** The title changed between versions. v1 used \"...for AI Models\"; the current version uses \"...for AI Model Collapse\". No venue beyond arXiv confirmed.\n\n**3. From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources**\n- **Authors:** Soham Bakshi, Sunrit Chakraborty\n- **Year:** 2026\n- **Venue:** arXiv preprint\n- **arXiv:** 2602.10531 (confirmed)\n- **Note:** Your details are correct. Only 2 authors.\n\n**4. Spectral Scaling Laws in Language Models: How Effectively Do Feed-Forward Networks Use Their Latent Space?**\n- **Authors:** Nandan Kumar Jha, Brandon Reagen\n- **Year:** 2025\n- **Venue:** EMNLP 2025 (confirmed, ACL Anthology: 2025.emnlp-main.1776)\n- **arXiv:** 2510.00537 (confirmed)\n- **DISCREPANCY:** The authors are Jha and Reagen, **not** \"Liehr et al.\" No author named Liehr is associated with this paper. Please verify this is the correct paper you intended.\n\n**5. A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective**\n- **Authors:** Lianghe Shi\\*, Meng Wu\\*, Huijie Zhang, Zekai Zhang, Molei Tao, Qing Qu (\\*equal contribution)\n- **Year:** 2025\n- **Venue:** NeurIPS 2025 Spotlight (confirmed, top 3.2%)\n- **arXiv:** 2509.16499\n- **Note:** First author is Shi (Lianghe Shi), consistent with \"Shi et al.\" Your details are correct.\n\n**6. Position: Model Collapse Does Not Mean What You Think**\n- **Authors:** Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, Sanmi Koyejo\n- **Year:** 2025\n- **Venue:** arXiv preprint; submitted to NeurIPS 2025 per OpenReview. An invited talk on this topic was given at ICLR 2025.\n- **arXiv:** 2503.03150 (confirmed)\n- **Note:** Lead author is Schaeffer, not \"Schaeffer, Kazdan\" -- Kazdan is second author.\n\n**7. Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data**\n- **Authors:** Matthias Gerstgrasser, Rylan Schaeffer, Apratim Dey, Rafael Rafailov, Henry Sleight, John Hughes, Tomasz Korbak, Rajashree Agrawal, Dhruv Bhandarkar Pai, Andrey Gromov, Daniel A. Roberts, Diyi Yang, David L. Donoho, Sanmi Koyejo\n- **Year:** 2024\n- **Venue:** COLM 2024 (First Conference on Language Modeling), **not** just arXiv\n- **arXiv:** 2404.01413 (confirmed)\n\n**8. Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World**\n- **Authors:** Joshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, David L. Donoho, Sanmi Koyejo\n- **Year:** 2025\n- **Venue:** ICML 2025 (PMLR 267:29469-29494), **not** just arXiv\n- **arXiv:** 2410.16713 (confirmed)\n\n---\n\n**Summary of discrepancies from your input:**\n- Paper 4: Authors are Jha & Reagen, not \"Liehr et al.\" -- verify this is the right paper.\n- Paper 7: Published at COLM 2024, not just arXiv.\n- Paper 8: Published at ICML 2025, not just arXiv.\n\nSources:\n- [Paper 1 - arXiv](https://arxiv.org/abs/2406.07515)\n- [Paper 2 - arXiv](https://arxiv.org/abs/2509.08972)\n- [Paper 3 - arXiv](https://arxiv.org/abs/2602.10531)\n- [Paper 4 - arXiv](https://arxiv.org/abs/2510.00537)\n- [Paper 4 - ACL Anthology](https://aclanthology.org/2025.emnlp-main.1776/)\n- [Paper 5 - arXiv](https://arxiv.org/abs/2509.16499)\n- [Paper 6 - arXiv](https://arxiv.org/abs/2503.03150)\n- [Paper 7 - arXiv](https://arxiv.org/abs/2404.01413)\n- [Paper 7 - OpenReview (COLM 2024)](https://openreview.net/forum?id=5B2K4LRgmz)\n- [Paper 8 - arXiv](https://arxiv.org/abs/2410.16713)\n- [Paper 8 - PMLR (ICML 2025)](https://proceedings.mlr.press/v267/kazdan25a.html)"
      }
    ],
    "totalDurationMs": 117258,
    "totalTokens": 35641,
    "totalToolUseCount": 21,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1111,
      "cache_read_input_tokens": 32911,
      "output_tokens": 1618,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1111
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1618,
          "cache_read_input_tokens": 32911,
          "cache_creation_input_tokens": 1111,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1111,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 21
    }
  },
  "sourceToolAssistantUUID": "274c7e1c-b7d9-4d3f-998e-6409b7ac89e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-15T02:15:16.368Z_

<details><summary>↩ Tool result · `toolu_016n39MJpt5zzJGQvQ24gak6`</summary>

```text
Here are the verified details for all 10 papers:

---

**1. Predicting LLM Compression Degradation from Spectral Statistics**
- **Authors:** Mingxue Xu (sole author)
- **Title:** Predicting LLM Compression Degradation from Spectral Statistics
- **Year:** 2026
- **Venue:** arXiv preprint
- **arXiv ID:** 2604.18085

**2. Nonlinear Random Matrix Theory for Deep Learning**
- **Authors:** Jeffrey Pennington, Pratik Worah
- **Title:** Nonlinear random matrix theory for deep learning
- **Year:** 2017
- **Venue:** Advances in Neural Information Processing Systems 30 (NeurIPS 2017), pp. 2637-2646
- **arXiv ID:** No standard arXiv preprint found; the paper appears to have been published directly through NIPS proceedings. A later journal version appeared in J. Stat. Mech. (2019) 124005.

**3. Approaching Deep Learning through the Spectral Dynamics of Weights**
- **Authors:** David Yunis, Kumar Kshitij Patel, Samuel Wheeler, Pedro Savarese, Gal Vardi, Karen Livescu, Michael Maire, Matthew R. Walter
- **Title:** Approaching Deep Learning through the Spectral Dynamics of Weights
- **Year:** 2024
- **Venue:** arXiv preprint
- **arXiv ID:** 2408.11804

**4. AlphaPruning**
- **Authors:** Haiquan Lu, Yefan Zhou, Shiwei Liu, Zhangyang Wang, Michael W. Mahoney, Yaoqing Yang
- **Title:** AlphaPruning: Using Heavy-Tailed Self Regularization Theory for Improved Layer-wise Pruning of Large Language Models
- **Year:** 2024
- **Venue:** NeurIPS 2024
- **arXiv ID:** 2410.10912

**5. How Instruction and Reasoning Data shape Post-Training**
- **Authors:** Ming Li, Yanhong Li, Ziyue Li, Tianyi Zhou
- **Title:** How Instruction and Reasoning Data shape Post-Training: Data Quality through the Lens of Layer-wise Gradients
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv ID:** 2504.10766

**6. Curriculum Learning for LLM Pretraining**
- **Authors:** Mohamed Elgaar, Hadi Amiri
- **Title:** Curriculum Learning for LLM Pretraining: An Analysis of Learning Dynamics
- **Year:** 2026
- **Venue:** arXiv preprint
- **arXiv ID:** 2601.21698

**7. Spectral Alignment as Predictor of Loss Explosion**
- **Authors:** Haiquan Qiu, You Wu, Yingjie Tan, Yaqing Wang, Quanming Yao
- **Title:** Spectral Alignment as Predictor of Loss Explosion in Neural Network Training
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv ID:** 2510.04202

**8. A Scalable Measure of Loss Landscape Curvature**
- **Authors:** Dayal Singh Kalra, Jean-Christophe Gagnon-Audet, Andrey Gromov, Ishita Mediratta, Kelvin Niu, Alexander H. Miller, Michael Shvartsman
- **Title:** A Scalable Measure of Loss Landscape Curvature for Analyzing the Training Dynamics of LLMs
- **Year:** 2026
- **Venue:** arXiv preprint
- **arXiv ID:** 2601.16979

**9. The Spectral Lifecycle of Transformer Training**
- **Authors:** Yi Liu (sole author)
- **Title:** The Spectral Lifecycle of Transformer Training: Transient Compression Waves, Persistent Spectral Gradients, and the Q/K--V Asymmetry
- **Year:** 2026
- **Venue:** arXiv preprint
- **arXiv ID:** 2604.22778

**10. Small Singular Values Matter**
- **Authors:** Max Staats, Matthias Thamm, Bernd Rosenow
- **Title:** Small Singular Values Matter: A Random Matrix Analysis of Transformer Models
- **Year:** 2024 (arXiv), presented at NeurIPS 2025
- **Venue:** NeurIPS 2025
- **arXiv ID:** 2410.17770

---

**Corrections to your original list:**
- Paper 4 (AlphaPruning): arXiv ID is **2410.10912**, not mentioned in your query but now confirmed.
- Paper 2 (Pennington & Worah): No standard arXiv ID found; cite via NeurIPS 2017 proceedings.
- Paper 9: Full title is longer than cited -- includes the subtitle "Transient Compression Waves, Persistent Spectral Gradients, and the Q/K--V Asymmetry".
- Paper 10: Originally on arXiv Oct 2024, but the venue is **NeurIPS 2025** (not 2024).

Sources:
- [Paper 1 - arXiv 2604.18085](https://arxiv.org/abs/2604.18085)
- [Paper 2 - NeurIPS 2017 proceedings](https://proceedings.neurips.cc/paper/2017/hash/0f3d014eead934bbdbacb62a01dc4831-Abstract.html)
- [Paper 3 - arXiv 2408.11804](https://arxiv.org/abs/2408.11804)
- [Paper 4 - arXiv 2410.10912](https://arxiv.org/abs/2410.10912)
- [Paper 5 - arXiv 2504.10766](https://arxiv.org/abs/2504.10766)
- [Paper 6 - arXiv 2601.21698](https://arxiv.org/abs/2601.21698)
- [Paper 7 - arXiv 2510.04202](https://arxiv.org/abs/2510.04202)
- [Paper 8 - arXiv 2601.16979](https://arxiv.org/abs/2601.16979)
- [Paper 9 - arXiv 2604.22778](https://arxiv.org/abs/2604.22778)
- [Paper 10 - arXiv 2410.17770](https://arxiv.org/abs/2410.17770)
- [Paper 10 - NeurIPS 2025 poster](https://neurips.cc/virtual/2025/loc/san-diego/poster/117389)

agentId: abf2430077a2896fc (use SendMessage with to: 'abf2430077a2896fc' to continue this agent)
&lt;usage>total_tokens: 35191
tool_uses: 20
duration_ms: 101466&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f693cf4-8023-4298-bfa2-83d675fbbc9a",
  "isSidechain": false,
  "promptId": "a7003b6e-3a25-4888-837a-59f1925bbd90",
  "type": "user",
  "uuid": "d7306386-032b-4f6b-b73d-2a01f0b6f158",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm building a BibTeX file for an ML research paper. I need you to verify the exact details for these papers using WebSearch. For each paper, find: full author list, exact title, year, venue, and arXiv ID if applicable. Return the information in a structured format.\n\nPapers to verify:\n\n1. \"Predicting LLM Compression Degradation from Spectral Statistics\" - Xu, arXiv 2604.18085\n2. \"Nonlinear Random Matrix Theory for Deep Learning\" - Pennington & Worah, NeurIPS 2017\n3. \"Approaching Deep Learning through the Spectral Dynamics of Weights\" - Yunis, Patel et al., arXiv 2408.11804\n4. \"AlphaPruning: Using Heavy-Tailed Self Regularization Theory for Improved Layer-wise Pruning of Large Language Models\" - Lu et al., NeurIPS 2024\n5. \"How Instruction and Reasoning Data shape Post-Training: Data Quality through the Lens of Layer-wise Gradients\" - Ming Li et al., arXiv 2504.10766\n6. \"Curriculum Learning for LLM Pretraining: An Analysis of Learning Dynamics\" - Elgaar & Amiri, arXiv 2601.21698\n7. \"Spectral Alignment as Predictor of Loss Explosion in Neural Network Training\" - Qiu et al., arXiv 2510.04202\n8. \"A Scalable Measure of Loss Landscape Curvature for Analyzing the Training Dynamics of LLMs\" - Kalra et al., arXiv 2601.16979\n9. \"The Spectral Lifecycle of Transformer Training\" - Liu, arXiv 2604.22778\n10. \"Small Singular Values Matter: A Random Matrix Analysis of Transformer Models\" - Staats et al., arXiv 2410.17770\n\nBe concise - just the facts for each paper.",
    "agentId": "abf2430077a2896fc",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the verified details for all 10 papers:\n\n---\n\n**1. Predicting LLM Compression Degradation from Spectral Statistics**\n- **Authors:** Mingxue Xu (sole author)\n- **Title:** Predicting LLM Compression Degradation from Spectral Statistics\n- **Year:** 2026\n- **Venue:** arXiv preprint\n- **arXiv ID:** 2604.18085\n\n**2. Nonlinear Random Matrix Theory for Deep Learning**\n- **Authors:** Jeffrey Pennington, Pratik Worah\n- **Title:** Nonlinear random matrix theory for deep learning\n- **Year:** 2017\n- **Venue:** Advances in Neural Information Processing Systems 30 (NeurIPS 2017), pp. 2637-2646\n- **arXiv ID:** No standard arXiv preprint found; the paper appears to have been published directly through NIPS proceedings. A later journal version appeared in J. Stat. Mech. (2019) 124005.\n\n**3. Approaching Deep Learning through the Spectral Dynamics of Weights**\n- **Authors:** David Yunis, Kumar Kshitij Patel, Samuel Wheeler, Pedro Savarese, Gal Vardi, Karen Livescu, Michael Maire, Matthew R. Walter\n- **Title:** Approaching Deep Learning through the Spectral Dynamics of Weights\n- **Year:** 2024\n- **Venue:** arXiv preprint\n- **arXiv ID:** 2408.11804\n\n**4. AlphaPruning**\n- **Authors:** Haiquan Lu, Yefan Zhou, Shiwei Liu, Zhangyang Wang, Michael W. Mahoney, Yaoqing Yang\n- **Title:** AlphaPruning: Using Heavy-Tailed Self Regularization Theory for Improved Layer-wise Pruning of Large Language Models\n- **Year:** 2024\n- **Venue:** NeurIPS 2024\n- **arXiv ID:** 2410.10912\n\n**5. How Instruction and Reasoning Data shape Post-Training**\n- **Authors:** Ming Li, Yanhong Li, Ziyue Li, Tianyi Zhou\n- **Title:** How Instruction and Reasoning Data shape Post-Training: Data Quality through the Lens of Layer-wise Gradients\n- **Year:** 2025\n- **Venue:** arXiv preprint\n- **arXiv ID:** 2504.10766\n\n**6. Curriculum Learning for LLM Pretraining**\n- **Authors:** Mohamed Elgaar, Hadi Amiri\n- **Title:** Curriculum Learning for LLM Pretraining: An Analysis of Learning Dynamics\n- **Year:** 2026\n- **Venue:** arXiv preprint\n- **arXiv ID:** 2601.21698\n\n**7. Spectral Alignment as Predictor of Loss Explosion**\n- **Authors:** Haiquan Qiu, You Wu, Yingjie Tan, Yaqing Wang, Quanming Yao\n- **Title:** Spectral Alignment as Predictor of Loss Explosion in Neural Network Training\n- **Year:** 2025\n- **Venue:** arXiv preprint\n- **arXiv ID:** 2510.04202\n\n**8. A Scalable Measure of Loss Landscape Curvature**\n- **Authors:** Dayal Singh Kalra, Jean-Christophe Gagnon-Audet, Andrey Gromov, Ishita Mediratta, Kelvin Niu, Alexander H. Miller, Michael Shvartsman\n- **Title:** A Scalable Measure of Loss Landscape Curvature for Analyzing the Training Dynamics of LLMs\n- **Year:** 2026\n- **Venue:** arXiv preprint\n- **arXiv ID:** 2601.16979\n\n**9. The Spectral Lifecycle of Transformer Training**\n- **Authors:** Yi Liu (sole author)\n- **Title:** The Spectral Lifecycle of Transformer Training: Transient Compression Waves, Persistent Spectral Gradients, and the Q/K--V Asymmetry\n- **Year:** 2026\n- **Venue:** arXiv preprint\n- **arXiv ID:** 2604.22778\n\n**10. Small Singular Values Matter**\n- **Authors:** Max Staats, Matthias Thamm, Bernd Rosenow\n- **Title:** Small Singular Values Matter: A Random Matrix Analysis of Transformer Models\n- **Year:** 2024 (arXiv), presented at NeurIPS 2025\n- **Venue:** NeurIPS 2025\n- **arXiv ID:** 2410.17770\n\n---\n\n**Corrections to your original list:**\n- Paper 4 (AlphaPruning): arXiv ID is **2410.10912**, not mentioned in your query but now confirmed.\n- Paper 2 (Pennington & Worah): No standard arXiv ID found; cite via NeurIPS 2017 proceedings.\n- Paper 9: Full title is longer than cited -- includes the subtitle \"Transient Compression Waves, Persistent Spectral Gradients, and the Q/K--V Asymmetry\".\n- Paper 10: Originally on arXiv Oct 2024, but the venue is **NeurIPS 2025** (not 2024).\n\nSources:\n- [Paper 1 - arXiv 2604.18085](https://arxiv.org/abs/2604.18085)\n- [Paper 2 - NeurIPS 2017 proceedings](https://proceedings.neurips.cc/paper/2017/hash/0f3d014eead934bbdbacb62a01dc4831-Abstract.html)\n- [Paper 3 - arXiv 2408.11804](https://arxiv.org/abs/2408.11804)\n- [Paper 4 - arXiv 2410.10912](https://arxiv.org/abs/2410.10912)\n- [Paper 5 - arXiv 2504.10766](https://arxiv.org/abs/2504.10766)\n- [Paper 6 - arXiv 2601.21698](https://arxiv.org/abs/2601.21698)\n- [Paper 7 - arXiv 2510.04202](https://arxiv.org/abs/2510.04202)\n- [Paper 8 - arXiv 2601.16979](https://arxiv.org/abs/2601.16979)\n- [Paper 9 - arXiv 2604.22778](https://arxiv.org/abs/2604.22778)\n- [Paper 10 - arXiv 2410.17770](https://arxiv.org/abs/2410.17770)\n- [Paper 10 - NeurIPS 2025 poster](https://neurips.cc/virtual/2025/loc/san-diego/poster/117389)"
      }
    ],
    "totalDurationMs": 101466,
    "totalTokens": 35191,
    "totalToolUseCount": 20,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 651,
      "cache_read_input_tokens": 32838,
      "output_tokens": 1701,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 651
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1701,
          "cache_read_input_tokens": 32838,
          "cache_creation_input_tokens": 651,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 651,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 20
    }
  },
  "sourceToolAssistantUUID": "8f693cf4-8023-4298-bfa2-83d675fbbc9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 60_

```json
{
  "type": "last-prompt",
  "leafUuid": "d7306386-032b-4f6b-b73d-2a01f0b6f158",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b"
}
```

---

### Runtime record

_source line 61_

```json
{
  "type": "ai-title",
  "aiTitle": "Compile bibliography file for paper citations",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b"
}
```

---

### Tool result

_source line 62 · 2026-05-15T02:15:28.647Z_

<details><summary>↩ Tool result · `toolu_01XSU7nhHCC1vCBrTismAMn6`</summary>

```text
No "Wyss" author found anywhere for this paper. The arXiv ID 2410.12341 is consistently attributed to Gambetta et al. The user likely has incorrect attribution. Here are the verified results:

---

**1. A Watermark for Large Language Models**
- **Authors:** John Kirchenbauer, Jonas Geiping, Yuxin Wen, Jonathan Katz, Ian Miers, Tom Goldstein
- **Year:** 2023
- **Venue:** ICML 2023
- **arXiv:** 2301.10226

**2. Scalable Watermarking for Identifying Large Language Model Outputs (SynthID-Text)**
- **Authors:** Sumanth Dathathri\*, Abigail See\*, Sumedh Ghaisas\*, Po-Sen Huang\*, Rob McAdam\*, Johannes Welbl, Vandana Bachani, Alex Kaskasoli, Robert Stanforth, Tatiana Matejovicova, Jamie Hayes, Nidhi Vyas, Majd Al Merey, Jonah Brown-Cohen, Rudy Bunel, Borja Balle, Taylan Cemgil, Zahra Ahmed, Kitty Stacpoole, Ilia Shumailov, Ciprian Baetu, Sven Gowal, Demis Hassabis, Pushmeet Kohli (\* = equal contribution)
- **Year:** 2024
- **Venue:** Nature, vol. 634, pp. 818--823
- **No arXiv ID** (published directly in Nature)

**3. Watermarking Makes Language Models Radioactive**
- **Authors:** Tom Sander, Pierre Fernandez, Alain Durmus, Matthijs Douze, Teddy Furon
- **Year:** 2024
- **Venue:** NeurIPS 2024
- **arXiv:** 2402.14904

**4. DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature**
- **Authors:** Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn
- **Year:** 2023
- **Venue:** ICML 2023 (pp. 24950--24962)
- **arXiv:** 2301.11305

**5. Detecting Pretraining Data from Large Language Models (Min-K% Prob)**
- **Authors:** Weijia Shi\*, Anirudh Ajith\*, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, Luke Zettlemoyer (\* = equal contribution)
- **Year:** 2024
- **Venue:** ICLR 2024
- **arXiv:** 2310.16789

**6. The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale**
- **Authors:** Guilherme Penedo, Hynek Kydlicek, Loubna Ben Allal, Anton Lozhkov, Margaret Mitchell, Colin Raffel, Leandro von Werra, Thomas Wolf
- **Year:** 2024
- **Venue:** NeurIPS 2024 (Datasets and Benchmarks Track)
- **arXiv:** 2406.17557

**7. The LLM Data Auditor: A Metric-oriented Survey on Quality and Trustworthiness in Evaluating Synthetic Data**
- **Authors:** Kaituo Zhang, Mingzhi Hu, Hoang Anh Duy Le, Fariha Kabir Torsha, Zhimeng Jiang, Minh Khai Bui, Chia-Yuan Chang, Yu-Neng Chuang, Zhen Xiong, Ying Lin, Guanchu Wang, Na Zou
- **Year:** 2025 (submitted January 2025)
- **Venue:** arXiv preprint
- **arXiv:** 2601.17717

**8. Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI**
- **WARNING: No author named "Wyss" found.** The actual authors are:
- **Authors:** Daniele Gambetta, Gizem Gezici, Fosca Giannotti, Dino Pedreschi, Alistair Knott, Luca Pappalardo
- **Year:** 2024 (submitted October 2024)
- **Venue:** arXiv preprint
- **arXiv:** 2410.12341
- Note: The paper went through title revisions (v1 was titled "A linguistic analysis of undesirable outcomes in the era of generative AI"). The attribution to "Wyss et al." appears to be incorrect -- please double-check your source.

**9. Data Value in the Age of Scaling: Understanding LLM Scaling Dynamics Under Real-Synthetic Data Mixtures**
- **Authors:** Haohui Wang, Jingyuan Qi, Jianpeng Chen, Jun Wu, Lifu Huang, Lecheng Zheng, Kevin Choi, Balaji Veeramani, Edward Bowen, Alison Hu, Tyler Cody, Dawei Zhou
- **Year:** 2025 (submitted November 2025)
- **Venue:** arXiv preprint
- **arXiv:** 2511.13640

Sources:
- [Kirchenbauer et al. - arXiv](https://arxiv.org/abs/2301.10226)
- [Kirchenbauer et al. - ICML proceedings](https://proceedings.mlr.press/v202/kirchenbauer23a.html)
- [Dathathri et al. - Nature](https://www.nature.com/articles/s41586-024-08025-4)
- [Sander et al. - arXiv](https://arxiv.org/abs/2402.14904)
- [Sander et al. - NeurIPS proceedings](https://proceedings.neurips.cc//paper_files/paper/2024/hash/2567c95fd41459a98a73ba893775d22a-Abstract-Conference.html)
- [Mitchell et al. - arXiv](https://arxiv.org/abs/2301.11305)
- [Mitchell et al. - ICML proceedings](https://proceedings.mlr.press/v202/mitchell23a.html)
- [Shi et al. - arXiv](https://arxiv.org/abs/2310.16789)
- [Shi et al. - OpenReview](https://openreview.net/forum?id=zWqr3MQuNs)
- [Penedo et al. - arXiv](https://arxiv.org/abs/2406.17557)
- [Penedo et al. - NeurIPS proceedings](https://neurips.cc/virtual/2024/poster/97513)
- [Zhang et al. - arXiv](https://arxiv.org/abs/2601.17717)
- [Gambetta et al. - arXiv](https://arxiv.org/abs/2410.12341)
- [Wang et al. - arXiv](https://arxiv.org/abs/2511.13640)

agentId: ac442dd236de4295a (use SendMessage with to: 'ac442dd236de4295a' to continue this agent)
&lt;usage>total_tokens: 32202
tool_uses: 17
duration_ms: 105784&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2d19e74-646e-4ce6-aa2d-1575ec1536fe",
  "isSidechain": false,
  "promptId": "a7003b6e-3a25-4888-837a-59f1925bbd90",
  "type": "user",
  "uuid": "333cb807-c562-4fec-8902-ef957a6c045c",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm building a BibTeX file for an ML research paper. I need you to verify the exact details for these papers using WebSearch. For each paper, find: full author list, exact title, year, venue, and arXiv ID if applicable. Return the information in a structured format.\n\nPapers to verify:\n\n1. \"A Watermark for Large Language Models\" - Kirchenbauer et al., ICML 2023\n2. \"Scalable Watermarking for Identifying Large Language Model Outputs\" (SynthID-Text) - Dathathri et al., Nature 2024\n3. \"Watermarking Makes Language Models Radioactive\" - Sander et al., NeurIPS 2024\n4. \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\" - Mitchell et al., ICML 2023\n5. \"Detecting Pretraining Data from Large Language Models\" (Min-K% Prob) - Shi et al., ICLR 2024\n6. \"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale\" - Penedo et al., arXiv 2406.17557\n7. \"The LLM Data Auditor\" - Zhang et al., arXiv 2601.17717\n8. \"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI\" - Wyss et al., arXiv 2410.12341\n9. \"Data Value in the Age of Scaling\" - Wang et al., arXiv 2511.13640\n\nBe concise - just the facts for each paper.",
    "agentId": "ac442dd236de4295a",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "No \"Wyss\" author found anywhere for this paper. The arXiv ID 2410.12341 is consistently attributed to Gambetta et al. The user likely has incorrect attribution. Here are the verified results:\n\n---\n\n**1. A Watermark for Large Language Models**\n- **Authors:** John Kirchenbauer, Jonas Geiping, Yuxin Wen, Jonathan Katz, Ian Miers, Tom Goldstein\n- **Year:** 2023\n- **Venue:** ICML 2023\n- **arXiv:** 2301.10226\n\n**2. Scalable Watermarking for Identifying Large Language Model Outputs (SynthID-Text)**\n- **Authors:** Sumanth Dathathri\\*, Abigail See\\*, Sumedh Ghaisas\\*, Po-Sen Huang\\*, Rob McAdam\\*, Johannes Welbl, Vandana Bachani, Alex Kaskasoli, Robert Stanforth, Tatiana Matejovicova, Jamie Hayes, Nidhi Vyas, Majd Al Merey, Jonah Brown-Cohen, Rudy Bunel, Borja Balle, Taylan Cemgil, Zahra Ahmed, Kitty Stacpoole, Ilia Shumailov, Ciprian Baetu, Sven Gowal, Demis Hassabis, Pushmeet Kohli (\\* = equal contribution)\n- **Year:** 2024\n- **Venue:** Nature, vol. 634, pp. 818--823\n- **No arXiv ID** (published directly in Nature)\n\n**3. Watermarking Makes Language Models Radioactive**\n- **Authors:** Tom Sander, Pierre Fernandez, Alain Durmus, Matthijs Douze, Teddy Furon\n- **Year:** 2024\n- **Venue:** NeurIPS 2024\n- **arXiv:** 2402.14904\n\n**4. DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature**\n- **Authors:** Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn\n- **Year:** 2023\n- **Venue:** ICML 2023 (pp. 24950--24962)\n- **arXiv:** 2301.11305\n\n**5. Detecting Pretraining Data from Large Language Models (Min-K% Prob)**\n- **Authors:** Weijia Shi\\*, Anirudh Ajith\\*, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, Luke Zettlemoyer (\\* = equal contribution)\n- **Year:** 2024\n- **Venue:** ICLR 2024\n- **arXiv:** 2310.16789\n\n**6. The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale**\n- **Authors:** Guilherme Penedo, Hynek Kydlicek, Loubna Ben Allal, Anton Lozhkov, Margaret Mitchell, Colin Raffel, Leandro von Werra, Thomas Wolf\n- **Year:** 2024\n- **Venue:** NeurIPS 2024 (Datasets and Benchmarks Track)\n- **arXiv:** 2406.17557\n\n**7. The LLM Data Auditor: A Metric-oriented Survey on Quality and Trustworthiness in Evaluating Synthetic Data**\n- **Authors:** Kaituo Zhang, Mingzhi Hu, Hoang Anh Duy Le, Fariha Kabir Torsha, Zhimeng Jiang, Minh Khai Bui, Chia-Yuan Chang, Yu-Neng Chuang, Zhen Xiong, Ying Lin, Guanchu Wang, Na Zou\n- **Year:** 2025 (submitted January 2025)\n- **Venue:** arXiv preprint\n- **arXiv:** 2601.17717\n\n**8. Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI**\n- **WARNING: No author named \"Wyss\" found.** The actual authors are:\n- **Authors:** Daniele Gambetta, Gizem Gezici, Fosca Giannotti, Dino Pedreschi, Alistair Knott, Luca Pappalardo\n- **Year:** 2024 (submitted October 2024)\n- **Venue:** arXiv preprint\n- **arXiv:** 2410.12341\n- Note: The paper went through title revisions (v1 was titled \"A linguistic analysis of undesirable outcomes in the era of generative AI\"). The attribution to \"Wyss et al.\" appears to be incorrect -- please double-check your source.\n\n**9. Data Value in the Age of Scaling: Understanding LLM Scaling Dynamics Under Real-Synthetic Data Mixtures**\n- **Authors:** Haohui Wang, Jingyuan Qi, Jianpeng Chen, Jun Wu, Lifu Huang, Lecheng Zheng, Kevin Choi, Balaji Veeramani, Edward Bowen, Alison Hu, Tyler Cody, Dawei Zhou\n- **Year:** 2025 (submitted November 2025)\n- **Venue:** arXiv preprint\n- **arXiv:** 2511.13640\n\nSources:\n- [Kirchenbauer et al. - arXiv](https://arxiv.org/abs/2301.10226)\n- [Kirchenbauer et al. - ICML proceedings](https://proceedings.mlr.press/v202/kirchenbauer23a.html)\n- [Dathathri et al. - Nature](https://www.nature.com/articles/s41586-024-08025-4)\n- [Sander et al. - arXiv](https://arxiv.org/abs/2402.14904)\n- [Sander et al. - NeurIPS proceedings](https://proceedings.neurips.cc//paper_files/paper/2024/hash/2567c95fd41459a98a73ba893775d22a-Abstract-Conference.html)\n- [Mitchell et al. - arXiv](https://arxiv.org/abs/2301.11305)\n- [Mitchell et al. - ICML proceedings](https://proceedings.mlr.press/v202/mitchell23a.html)\n- [Shi et al. - arXiv](https://arxiv.org/abs/2310.16789)\n- [Shi et al. - OpenReview](https://openreview.net/forum?id=zWqr3MQuNs)\n- [Penedo et al. - arXiv](https://arxiv.org/abs/2406.17557)\n- [Penedo et al. - NeurIPS proceedings](https://neurips.cc/virtual/2024/poster/97513)\n- [Zhang et al. - arXiv](https://arxiv.org/abs/2601.17717)\n- [Gambetta et al. - arXiv](https://arxiv.org/abs/2410.12341)\n- [Wang et al. - arXiv](https://arxiv.org/abs/2511.13640)"
      }
    ],
    "totalDurationMs": 105784,
    "totalTokens": 32202,
    "totalToolUseCount": 17,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1071,
      "cache_read_input_tokens": 29331,
      "output_tokens": 1799,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1071
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1799,
          "cache_read_input_tokens": 29331,
          "cache_creation_input_tokens": 1071,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1071,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 17
    }
  },
  "sourceToolAssistantUUID": "c2d19e74-646e-4ce6-aa2d-1575ec1536fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 63 · 2026-05-15T02:15:28.653Z_

```json
{
  "parentUuid": "333cb807-c562-4fec-8902-ef957a6c045c",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "b3f76237-1cd3-44ff-92ba-0c31bfb85f9f",
  "timestamp": "2026-05-15T02:15:28.653Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 64 · 2026-05-15T02:15:56.288Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the verified information. Let me compile the BibTeX file. Let me also note some discrepancies:

1. **Liehr2025** - The paper at arXiv 2510.00537 is actually by Jha and Reagen, not "Liehr et al." The citation key in the paper uses `Liehr2025` but this seems to be a mistake in the literature notes. I need to search for the actual "Liehr" paper or use the correct authors for arXiv 2510.00537. Let me check what the paper text says about this:
   
The related_work.tex file references `Liehr2025` with a description about FFN soft rank scaling near-linearly with width, which matches arXiv 2510.00537, but the agents attribute that paper to Jha and Reagen instead. There's a mismatch here—either the literature notes misidentified the authors, or there's a separate Liehr paper I'm missing. Since the tex file uses the `Liehr2025` key, I'll need to create a BibTeX entry with that citation key regardless, but I should verify which authors and which paper actually belong to it. There's a clear mismatch here—the citation key references Liehr but the arXiv ID points to a paper by Jha and Reagen. I need to figure out if there's actually a separate Liehr paper on spectral scaling laws, or if the literature notes have the wrong attribution. Let me search for papers by Liehr on this topic to resolve the discrepancy.

I'm also noticing the same kind of problem with Wyss2024—the literature map lists it as a Wyss paper on surplexity, but the agent found that arXiv 2410.12341 is by Gambetta et al. instead. I should track down the actual Wyss paper to see if there's a different arXiv ID or if this is another attribution error.

From the agent's searches, I've already got some corrections—Penedo2024 was presented at NeurIPS 2024 in the Datasets and Benchmarks Track, which is useful context.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3f76237-1cd3-44ff-92ba-0c31bfb85f9f",
  "isSidechain": false,
  "requestId": "req_011Cb3Yn42gAfWJbRCBxau7t",
  "type": "assistant",
  "uuid": "db809318-8fac-4c3e-af32-ba403079633a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LXMUf6z9roZWMNHqiCsanN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10631,
      "cache_read_input_tokens": 67155,
      "output_tokens": 1232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10631,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1232,
          "cache_read_input_tokens": 67155,
          "cache_creation_input_tokens": 10631,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10631
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

_source line 65 · 2026-05-15T02:15:56.313Z_

Two discrepancies found - let me verify the Liehr and Wyss papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db809318-8fac-4c3e-af32-ba403079633a",
  "isSidechain": false,
  "requestId": "req_011Cb3Yn42gAfWJbRCBxau7t",
  "type": "assistant",
  "uuid": "c3f14456-5171-473e-8a24-ceb29aed45af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LXMUf6z9roZWMNHqiCsanN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10631,
      "cache_read_input_tokens": 67155,
      "output_tokens": 1232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10631,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1232,
          "cache_read_input_tokens": 67155,
          "cache_creation_input_tokens": 10631,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10631
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

_source line 66 · 2026-05-15T02:15:56.830Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GUsdCQNbinRZhNyYV6FhY9`</summary>

```json
{
  "query": "Liehr \"spectral scaling laws\" language models FFN soft rank 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3f14456-5171-473e-8a24-ceb29aed45af",
  "isSidechain": false,
  "requestId": "req_011Cb3Yn42gAfWJbRCBxau7t",
  "type": "assistant",
  "uuid": "3fce9a01-020a-42b7-870c-d522217d4799",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LXMUf6z9roZWMNHqiCsanN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10631,
      "cache_read_input_tokens": 67155,
      "output_tokens": 1232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10631,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1232,
          "cache_read_input_tokens": 67155,
          "cache_creation_input_tokens": 10631,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10631
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

_source line 67 · 2026-05-15T02:15:56.969Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VLSCbW5C8Pqxb8Jq1YHasd`</summary>

```json
{
  "query": "Wyss \"surplexity\" model collapse generative AI 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fce9a01-020a-42b7-870c-d522217d4799",
  "isSidechain": false,
  "requestId": "req_011Cb3Yn42gAfWJbRCBxau7t",
  "type": "assistant",
  "uuid": "aa899e38-85a4-417c-b7f2-c4f707ad5d83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LXMUf6z9roZWMNHqiCsanN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10631,
      "cache_read_input_tokens": 67155,
      "output_tokens": 1232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10631,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1232,
          "cache_read_input_tokens": 67155,
          "cache_creation_input_tokens": 10631,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10631
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

_source line 68 · 2026-05-15T02:16:03.940Z_

<details><summary>↩ Tool result · `toolu_01GUsdCQNbinRZhNyYV6FhY9`</summary>

```text
Web search results for query: "Liehr "spectral scaling laws" language models FFN soft rank 2025"

Links: [{"title":"Spectral Scaling Laws in Language Models","url":"https://aclanthology.org/2025.emnlp-main.1776.pdf"},{"title":"Spectral Scaling Laws in Language Models:","url":"https://arxiv.org/pdf/2510.00537"},{"title":"[2510.00537] Spectral Scaling Laws in Language Models: How Effectively Do Feed-Forward Networks Use Their Latent Space?","url":"https://arxiv.org/abs/2510.00537"},{"title":"Spectral Scaling Laws in Language Models: How Effectively Do Feed-Forward Networks Use Their Latent Space?","url":"https://arxiv.org/html/2510.00537v1"},{"title":"Spectral Scaling Laws in Language Models: emphHow Effectively Do Feed-Forward Networks Use Their Latent Space? - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1776/"},{"title":"Spectral Scaling Laws in Language Models: \\\\ {\\em How Effectively Do Feed-Forward Networks Use Their Latent Space?} | OpenReview","url":"https://openreview.net/forum?id=VSJ5eupW6j"},{"title":"[2001.08361] Scaling Laws for Neural Language Models","url":"https://arxiv.org/abs/2001.08361"},{"title":"Scaling Laws for Neural Language Models Jared Kaplan ∗","url":"https://arxiv.org/pdf/2001.08361"},{"title":"Revisiting Scaling Laws for Language Models","url":"https://aclanthology.org/2025.acl-long.1163.pdf"},{"title":"VersatileFFN: Achieving Parameter Efficiency in LLMs via Adaptive","url":"https://arxiv.org/pdf/2512.14531"}]

I found research on spectral scaling laws in language models. Here are the key findings:

## Spectral Scaling Laws in Language Models

The key finding is an asymmetric spectral scaling law: soft rank follows an almost perfect power law with FFN width, while hard rank grows only sublinearly and with high variance.

### Research Methodology

The study uses a lightweight diagnostic suite: Hard Rank (participation ratio), Soft Rank (Shannon Rank), Spectral Concentration, and the composite Spectral Utilization Index (SUI), to quantify how many latent directions are meaningfully activated across LLaMA, GPT-2, and nGPT families.

### Key Implications

This asymmetry suggests that widening FFNs mostly adds low-energy tail directions, while dominant-mode subspaces saturate early. Moreover, at larger widths, variance further collapses into a narrow subspace, leaving much of the latent space under-utilized.

### Practical Significance

These results recast FFN width selection as a principled trade-off between tail capacity and dominant-mode capacity, offering concrete guidance for inference-efficient LLM design.

The research was published in November 2025 at the Conference on Empirical Methods in Natural Language Processing (EMNLP 2025) and appears to be authored by Nandan Kumar Jha and Brandon Reagen.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3fce9a01-020a-42b7-870c-d522217d4799",
  "isSidechain": false,
  "promptId": "a7003b6e-3a25-4888-837a-59f1925bbd90",
  "type": "user",
  "uuid": "d4d1eb28-fcc4-45d8-9e39-bfa4a1f88afd",
  "toolUseResult": {
    "query": "Liehr \"spectral scaling laws\" language models FFN soft rank 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MZ245ybsu5NPiWSzWt5kgU",
        "content": [
          {
            "title": "Spectral Scaling Laws in Language Models",
            "url": "https://aclanthology.org/2025.emnlp-main.1776.pdf"
          },
          {
            "title": "Spectral Scaling Laws in Language Models:",
            "url": "https://arxiv.org/pdf/2510.00537"
          },
          {
            "title": "[2510.00537] Spectral Scaling Laws in Language Models: How Effectively Do Feed-Forward Networks Use Their Latent Space?",
            "url": "https://arxiv.org/abs/2510.00537"
          },
          {
            "title": "Spectral Scaling Laws in Language Models: How Effectively Do Feed-Forward Networks Use Their Latent Space?",
            "url": "https://arxiv.org/html/2510.00537v1"
          },
          {
            "title": "Spectral Scaling Laws in Language Models: emphHow Effectively Do Feed-Forward Networks Use Their Latent Space? - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.1776/"
          },
          {
            "title": "Spectral Scaling Laws in Language Models: \\\\ {\\em How Effectively Do Feed-Forward Networks Use Their Latent Space?} | OpenReview",
            "url": "https://openreview.net/forum?id=VSJ5eupW6j"
          },
          {
            "title": "[2001.08361] Scaling Laws for Neural Language Models",
            "url": "https://arxiv.org/abs/2001.08361"
          },
          {
            "title": "Scaling Laws for Neural Language Models Jared Kaplan ∗",
            "url": "https://arxiv.org/pdf/2001.08361"
          },
          {
            "title": "Revisiting Scaling Laws for Language Models",
            "url": "https://aclanthology.org/2025.acl-long.1163.pdf"
          },
          {
            "title": "VersatileFFN: Achieving Parameter Efficiency in LLMs via Adaptive",
            "url": "https://arxiv.org/pdf/2512.14531"
          }
        ]
      },
      "I found research on spectral scaling laws in language models. Here are the key findings:\n\n## Spectral Scaling Laws in Language Models\n\nThe key finding is an asymmetric spectral scaling law: soft rank follows an almost perfect power law with FFN width, while hard rank grows only sublinearly and with high variance.\n\n### Research Methodology\n\nThe study uses a lightweight diagnostic suite: Hard Rank (participation ratio), Soft Rank (Shannon Rank), Spectral Concentration, and the composite Spectral Utilization Index (SUI), to quantify how many latent directions are meaningfully activated across LLaMA, GPT-2, and nGPT families.\n\n### Key Implications\n\nThis asymmetry suggests that widening FFNs mostly adds low-energy tail directions, while dominant-mode subspaces saturate early. Moreover, at larger widths, variance further collapses into a narrow subspace, leaving much of the latent space under-utilized.\n\n### Practical Significance\n\nThese results recast FFN width selection as a principled trade-off between tail capacity and dominant-mode capacity, offering concrete guidance for inference-efficient LLM design.\n\nThe research was published in November 2025 at the Conference on Empirical Methods in Natural Language Processing (EMNLP 2025) and appears to be authored by Nandan Kumar Jha and Brandon Reagen."
    ],
    "durationSeconds": 7.1049741089999445
  },
  "sourceToolAssistantUUID": "3fce9a01-020a-42b7-870c-d522217d4799",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-15T02:16:04.077Z_

<details><summary>↩ Tool result · `toolu_01VLSCbW5C8Pqxb8Jq1YHasd`</summary>

```text
Web search results for query: "Wyss "surplexity" model collapse generative AI 2024"

Links: [{"title":"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI","url":"https://arxiv.org/html/2410.12341"},{"title":"[2410.12341] Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI","url":"https://arxiv.org/abs/2410.12341"},{"title":"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI","url":"https://www.arxiv.org/pdf/2410.12341v3"},{"title":"Surplexity for Mitigating Model Collapse in Generative AI","url":"https://openreview.net/pdf?id=zzk6DUQggQ"},{"title":"A Note on Shumailov et al. (2024): 'AI Models Collapse ...","url":"https://arxiv.org/html/2410.12954v2"},{"title":"AI models collapse when trained on recursively generated data | Nature","url":"https://www.nature.com/articles/s41586-024-07566-y"},{"title":"AI models collapse when trained on recursively generated data - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/39048682/"},{"title":"[2410.12954] A Note on Shumailov et al. (2024): `AI Models Collapse When Trained on Recursively Generated Data'","url":"https://arxiv.org/abs/2410.12954"},{"title":"Model collapse - Wikipedia","url":"https://en.wikipedia.org/wiki/Model_collapse"},{"title":"Could we see the collapse of generative AI? | Inria","url":"https://www.inria.fr/en/collapse-ia-generatives"}]

Based on the search results, here's what I found about the Wyss "surplexity" model collapse research:

## Overview

The concept of surplexity is a measure of model surprise, which is used both to detect collapse and to filter training data. As synthetic content increasingly infiltrates the web, generative AI models may be retrained on their own outputs: a process termed "autophagy", which leads to model collapse: a progressive loss of performance and diversity across generations.

## The Surplexity Solution

The research addresses a key limitation of existing mitigation strategies: current characterizations of model collapse remain limited, and existing mitigation methods assume reliable knowledge of whether training data is human-authored or AI-generated.

The proposed practical mitigation strategy involves filtering training items by high surplexity, maximizing the surprise of the model. Unlike existing methods, this approach does not require distinguishing between human- and AI-generated data.

## Key Findings

Over simulation steps, the surplexity-based strategy achieves the highest accuracy, slightly outperforming the human-text baseline. Experiments across datasets and models demonstrate that the strategy is at least as effective as human-data baselines, and even more effective in reducing distributional skewedness.

The research paper was authored by Daniele Gambetta and colleagues, with results published in 2024 on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa899e38-85a4-417c-b7f2-c4f707ad5d83",
  "isSidechain": false,
  "promptId": "a7003b6e-3a25-4888-837a-59f1925bbd90",
  "type": "user",
  "uuid": "2c78eb16-dd5d-45bd-9205-7f764b3ffbb6",
  "toolUseResult": {
    "query": "Wyss \"surplexity\" model collapse generative AI 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BmtDbvSyqPm9VdSeZRZ2EN",
        "content": [
          {
            "title": "Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI",
            "url": "https://arxiv.org/html/2410.12341"
          },
          {
            "title": "[2410.12341] Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI",
            "url": "https://arxiv.org/abs/2410.12341"
          },
          {
            "title": "Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI",
            "url": "https://www.arxiv.org/pdf/2410.12341v3"
          },
          {
            "title": "Surplexity for Mitigating Model Collapse in Generative AI",
            "url": "https://openreview.net/pdf?id=zzk6DUQggQ"
          },
          {
            "title": "A Note on Shumailov et al. (2024): 'AI Models Collapse ...",
            "url": "https://arxiv.org/html/2410.12954v2"
          },
          {
            "title": "AI models collapse when trained on recursively generated data | Nature",
            "url": "https://www.nature.com/articles/s41586-024-07566-y"
          },
          {
            "title": "AI models collapse when trained on recursively generated data - PubMed",
            "url": "https://pubmed.ncbi.nlm.nih.gov/39048682/"
          },
          {
            "title": "[2410.12954] A Note on Shumailov et al. (2024): `AI Models Collapse When Trained on Recursively Generated Data'",
            "url": "https://arxiv.org/abs/2410.12954"
          },
          {
            "title": "Model collapse - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Model_collapse"
          },
          {
            "title": "Could we see the collapse of generative AI? | Inria",
            "url": "https://www.inria.fr/en/collapse-ia-generatives"
          }
        ]
      },
      "Based on the search results, here's what I found about the Wyss \"surplexity\" model collapse research:\n\n## Overview\n\nThe concept of surplexity is a measure of model surprise, which is used both to detect collapse and to filter training data. As synthetic content increasingly infiltrates the web, generative AI models may be retrained on their own outputs: a process termed \"autophagy\", which leads to model collapse: a progressive loss of performance and diversity across generations.\n\n## The Surplexity Solution\n\nThe research addresses a key limitation of existing mitigation strategies: current characterizations of model collapse remain limited, and existing mitigation methods assume reliable knowledge of whether training data is human-authored or AI-generated.\n\nThe proposed practical mitigation strategy involves filtering training items by high surplexity, maximizing the surprise of the model. Unlike existing methods, this approach does not require distinguishing between human- and AI-generated data.\n\n## Key Findings\n\nOver simulation steps, the surplexity-based strategy achieves the highest accuracy, slightly outperforming the human-text baseline. Experiments across datasets and models demonstrate that the strategy is at least as effective as human-data baselines, and even more effective in reducing distributional skewedness.\n\nThe research paper was authored by Daniele Gambetta and colleagues, with results published in 2024 on arXiv."
    ],
    "durationSeconds": 7.082409695999988
  },
  "sourceToolAssistantUUID": "aa899e38-85a4-417c-b7f2-c4f707ad5d83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 70_

```json
{
  "type": "last-prompt",
  "leafUuid": "2c78eb16-dd5d-45bd-9205-7f764b3ffbb6",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b"
}
```

---

### Runtime record

_source line 71_

```json
{
  "type": "ai-title",
  "aiTitle": "Compile bibliography file for paper citations",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b"
}
```

---

### Assistant

_source line 72 · 2026-05-15T02:18:03.466Z_

<details><summary>Logged reasoning block</summary>

```text
OK so:

1. **Liehr2025**: The paper "Spectral Scaling Laws in Language Models" (arXiv 2510.00537) is by Nandan Kumar Jha and Brandon Reagen, NOT "Liehr et al." There's no author named Liehr associated with this paper. The literature notes have incorrect attribution. Since the tex file uses `\citet{Liehr2025}`, which would render as "Liehr (2025)" in the text, this is a problem. But my task is to create the BibTeX entries. I should:
   - Create the entry with key `Liehr2025` using the correct authors (Jha and Reagen)
   - The citation key doesn't need to match the author name, so `\citet{Liehr2025}` will correctly render as "Jha and Reagen (2025)" once I use the proper authors in the bib entry. I'll note this key mismatch.

2. **Wyss2024**: The paper "Learning by Surprise: Surplexity" (arXiv 2410.12341) is by Daniele Gambetta et al., NOT "Wyss et al." I need to create the entry with the correct authors and flag this discrepancy as well.

Let me verify if there's a separate paper by C. M. Wyss about surplexity, or if this is simply a misattribution in the literature notes...

Actually, looking at the arXiv versions, it seems the surplexity paper is consistently authored by Gambetta and colleagues, not Wyss. I'll use the correct author attribution in the BibTeX entry and note this discrepancy.

Now I'm compiling the complete BibTeX file with all 44 entries, starting with the pruning and model collapse papers... I'm continuing through the bibliography, noting Dathathri's work on watermarking large language models published in Nature, and moving into additional references on related topics. Continuing through the references, I see Feng and colleagues' work on synthesized data verification at ICLR 2025, followed by Fu's ICML paper on self-consuming generative models, and then Gerstgrasser's collaborative study that appears to be cut off.

The next piece completes that title about whether model collapse is inevitable and discusses mixing real with synthetic data, published at COLM 2024. Then there's Gillman's work on self-correcting training loops from ICML 2024, Gu's recent paper on spectral analysis for model collapse detection, and the beginning of Kalra's entry.

Now I'm seeing the rest of Kalra's citation with co-authors examining loss landscape curvature during LLM training, followed by Kalinowski's topological approach to predicting collapse, and Kazdan's ICML 2025 paper on the risks and benefits of synthetic data in self-generating systems—though I notice the key says 2024 but the venue is listed as 2025, with the arXiv version from October 2024. submitted in 2024, published at ICML 2025. The citation key uses 2024 (probably based on arXiv date). I'll keep the key as-is but use the ICML 2025 venue.

Kirchenbauer and colleagues published their watermarking work at ICML 2023, with the arXiv preprint from early 2023. Li's recent paper on instruction and reasoning data uses layer-wise gradients to analyze post-training dynamics, still in preprint form. Jha and Reagen's work on spectral scaling laws in feed-forward networks appeared at EMNLP 2025, though my notes mistakenly attributed it to Liehr. Liu's paper examining the spectral lifecycle of transformers during training is forthcoming, and Martin's foundational work on predicting neural network quality without access to training data was published in Nature Communications.

Now I'm continuing through the bibliography with Mitchell's DetectGPT paper from ICML 2023, Penedo's FineWeb dataset paper from NeurIPS 2024, and Pennington's work on nonlinear random matrix theory from NeurIPS 2017.

I'm adding Qiu's recent paper on spectral alignment as a predictor of loss explosion, Sander's work on watermarking language models from NeurIPS 2024, and Sanyal's ICLR 2020 paper on stable rank normalization for improved generalization. The list appears to be cut off at the beginning of another entry.

Continuing with Schaeffer's position paper challenging assumptions about model collapse, Seddik's statistical analysis of language model collapse from synthetic data training, and Shi's ICLR 2024 work on detecting pretraining data in large language models.

Now I'm adding more recent papers on model collapse: Shi's 2025 NeurIPS spotlight examining the generalization-to-memorization perspective, Shumailov's Nature paper on how recursive data generation causes model collapse, and starting to catalog Staats' 2024 work. Continuing through the bibliography, I'm seeing entry 37 complete with Xu's work on predicting LLM compression degradation from spectral statistics, followed by Yi and colleagues' paper on escaping model collapse through synthetic data verification, Yunis's work on spectral dynamics of neural network weights, and the start of Zhang's 2026 entry. Finishing up the bibliography entries for Merity's work on pointer networks and the HellaSwag benchmark, then I'll organize everything by citation key for the BibTeX file.

I'm realizing there's a mismatch with some of the citation keys used in the tex file—like `\citet{Liehr2025}` and `\citet{Wyss2024}`—where the actual author names don't match what the keys suggest, so the rendered citations might look off.

I'll use the correct author information in the BibTeX entries and note these discrepancies as potential issues to fix in the tex files.

For papers like Kazdan2024 and Staats2024 that appeared on arXiv in 2024 but were published at conferences in 2025, I'm going with the conference publication details since that's the authoritative venue, even though the citation key reflects the earlier year.

For Pennington2017, I'll use @inproceedings with NeurIPS 2017 since no standard arXiv preprint exists.

Now I'm constructing the complete BibTeX file, being careful with author formatting using "and" between names, proper field syntax, and the right structure for arXiv papers versus conference proceedings. I'll sort everything alphabetically by key.

For the primaryClass field, I'm assigning appropriate categories—cs.LG for machine learning papers, cs.CL for NLP work, cs.CR for cryptography, and stat.ML for statistics papers. Since the agent already confirmed there's no standard arXiv version for Pennington2017, I'll stick with the @inproceedings format.

Now I need to handle the author lists carefully, especially for Dathathri2024 which has 24 authors that all need to be included. For Zhang2026, the arXiv ID 2601.17717 indicates January 2026, so I'll use 2026 as the year despite the January 2025 submission date. I'll assign primaryClass based on the paper's focus—cs.CL for language model and NLP work, cs.LG for general machine learning papers, and stat.ML where appropriate. Now let me write out the complete BibTeX entries.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c78eb16-dd5d-45bd-9205-7f764b3ffbb6",
  "isSidechain": false,
  "requestId": "req_011Cb3YpfVw3sCeKCiNptSs8",
  "type": "assistant",
  "uuid": "5f1d118a-b7c7-4b47-8ac1-554f66cebf76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ChyNEAigcaDMjnXthP5p9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2880,
      "cache_read_input_tokens": 77786,
      "output_tokens": 5826,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2880,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5826,
          "cache_read_input_tokens": 77786,
          "cache_creation_input_tokens": 2880,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2880
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

_source line 73 · 2026-05-15T02:18:04.699Z_

All verification complete. Two discrepancies found:
- **Liehr2025**: Actually by Jha & Reagen (not "Liehr")
- **Wyss2024**: Actually by Gambetta et al. (not "Wyss")

Key corrections: Gerstgrasser2024→COLM 2024, Kazdan2024→ICML 2025, Penedo2024→NeurIPS 2024, Martin2021 has 3 authors. Now writing the complete BibTeX file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f1d118a-b7c7-4b47-8ac1-554f66cebf76",
  "isSidechain": false,
  "requestId": "req_011Cb3YpfVw3sCeKCiNptSs8",
  "type": "assistant",
  "uuid": "60082d74-ce37-4ecf-9c19-bbfde3764a91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ChyNEAigcaDMjnXthP5p9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2880,
      "cache_read_input_tokens": 77786,
      "output_tokens": 5826,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2880,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5826,
          "cache_read_input_tokens": 77786,
          "cache_creation_input_tokens": 2880,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2880
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

_source line 74 · 2026-05-15T02:18:06.424Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01QiKc36w5cLnznghorwa9KF`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/",
  "description": "Check paper directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60082d74-ce37-4ecf-9c19-bbfde3764a91",
  "isSidechain": false,
  "requestId": "req_011Cb3YpfVw3sCeKCiNptSs8",
  "type": "assistant",
  "uuid": "583c3831-9513-477a-bda9-ca4061ce7e4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ChyNEAigcaDMjnXthP5p9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2880,
      "cache_read_input_tokens": 77786,
      "output_tokens": 5826,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2880,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5826,
          "cache_read_input_tokens": 77786,
          "cache_creation_input_tokens": 2880,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2880
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

_source line 75 · 2026-05-15T02:18:06.589Z_

<details><summary>↩ Tool result · `toolu_01QiKc36w5cLnznghorwa9KF`</summary>

```text
sections
tables
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "583c3831-9513-477a-bda9-ca4061ce7e4b",
  "isSidechain": false,
  "promptId": "a7003b6e-3a25-4888-837a-59f1925bbd90",
  "type": "user",
  "uuid": "cc7ded1c-763c-4033-aaf7-b1a42880cedd",
  "toolUseResult": {
    "stdout": "sections\ntables",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "583c3831-9513-477a-bda9-ca4061ce7e4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 76_

```json
{
  "type": "last-prompt",
  "leafUuid": "cc7ded1c-763c-4033-aaf7-b1a42880cedd",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b"
}
```

---

### Runtime record

_source line 77_

```json
{
  "type": "ai-title",
  "aiTitle": "Compile bibliography file for paper citations",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b"
}
```

---

### Tool call

_source line 78 · 2026-05-15T02:20:02.257Z_

<details open><summary>🔧 Tool call — Write · `toolu_01WaGu9qdJ7sd1uDHHeJqX97`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/references.bib",
  "content": "% references.bib — collapse_severity_monitor\n% Auto-compiled from paper sections: abstract, introduction, related_work, method, competitor_comparison\n% 44 citation keys, sorted alphabetically\n% Generated: 2026-05-15\n\n@inproceedings{AlphaPruning2024,\n  title     = {{AlphaPruning}: Using Heavy-Tailed Self Regularization Theory for Improved Layer-wise Pruning of Large Language Models},\n  author    = {Haiquan Lu and Yefan Zhou and Shiwei Liu and Zhangyang Wang and Michael W. Mahoney and Yaoqing Yang},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2024},\n  eprint    = {2410.10912},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@inproceedings{Alemohammad2024,\n  title     = {Self-Consuming Generative Models Go {MAD}},\n  author    = {Sina Alemohammad and Josue Casco-Rodriguez and Lorenzo Luzi and Ahmed Imtiaz Humayun and Hossein Babaei and Daniel LeJeune and Ali Siahkoohi and Richard G. Baraniuk},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year      = {2024},\n  eprint    = {2307.01850},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@article{Bakshi2026,\n  title   = {From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources},\n  author  = {Soham Bakshi and Sunrit Chakraborty},\n  year    = {2026},\n  eprint  = {2602.10531},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@inproceedings{Chen2024_dse,\n  title     = {Assessing Neural Network Representations During Training Using Noise-Resilient Diffusion Spectral Entropy},\n  author    = {Danqi Liao and Chen Liu and Benjamin W. Christensen and Alexander Tong and Guillaume Huguet and Guy Wolf and Maximilian Nickel and Ian Adelstein and Smita Krishnaswamy},\n  booktitle = {Proceedings of the 58th Annual Conference on Information Sciences and Systems (CISS)},\n  year      = {2024},\n  publisher = {IEEE},\n  eprint    = {2312.04823},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@article{Dathathri2024,\n  title   = {Scalable Watermarking for Identifying Large Language Model Outputs},\n  author  = {Sumanth Dathathri and Abigail See and Sumedh Ghaisas and Po-Sen Huang and Rob McAdam and Johannes Welbl and Vandana Bachani and Alex Kaskasoli and Robert Stanforth and Tatiana Matejovicova and Jamie Hayes and Nidhi Vyas and Majd Al Merey and Jonah Brown-Cohen and Rudy Bunel and Borja Balle and Taylan Cemgil and Zahra Ahmed and Kitty Stacpoole and Ilia Shumailov and Ciprian Baetu and Sven Gowal and Demis Hassabis and Pushmeet Kohli},\n  journal = {Nature},\n  volume  = {634},\n  pages   = {818--823},\n  year    = {2024}\n}\n\n@inproceedings{dettmers2023qlora,\n  title     = {{QLoRA}: Efficient Finetuning of Quantized Large Language Models},\n  author    = {Tim Dettmers and Artidoro Pagnoni and Ari Holtzman and Luke Zettlemoyer},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2023},\n  eprint    = {2305.14314},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@inproceedings{Dohmatob2024_tails,\n  title     = {A Tale of Tails: Model Collapse as a Change of Scaling Laws},\n  author    = {Elvis Dohmatob and Yunzhen Feng and Pu Yang and Francois Charton and Julia Kempe},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  pages     = {11165--11197},\n  year      = {2024},\n  eprint    = {2402.07043},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@inproceedings{Dohmatob2025,\n  title     = {Strong Model Collapse},\n  author    = {Elvis Dohmatob and Yunzhen Feng and Arjun Subramonian and Julia Kempe},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year      = {2025},\n  note      = {Spotlight},\n  eprint    = {2410.04840},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@article{Elgaar2026,\n  title   = {Curriculum Learning for {LLM} Pretraining: An Analysis of Learning Dynamics},\n  author  = {Mohamed Elgaar and Hadi Amiri},\n  year    = {2026},\n  eprint  = {2601.21698},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.CL}\n}\n\n@inproceedings{Feng2025,\n  title     = {Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification},\n  author    = {Yunzhen Feng and Elvis Dohmatob and Pu Yang and Francois Charton and Julia Kempe},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year      = {2025},\n  eprint    = {2406.07515},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@inproceedings{Fu2024_icml,\n  title     = {Towards Theoretical Understandings of Self-Consuming Generative Models},\n  author    = {Shi Fu and Sen Zhang and Yingjie Wang and Xinmei Tian and Dacheng Tao},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  year      = {2024},\n  eprint    = {2402.11778},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@inproceedings{Gerstgrasser2024,\n  title     = {Is Model Collapse Inevitable? {Breaking} the Curse of Recursion by Accumulating Real and Synthetic Data},\n  author    = {Matthias Gerstgrasser and Rylan Schaeffer and Apratim Dey and Rafael Rafailov and Henry Sleight and John Hughes and Tomasz Korbak and Rajashree Agrawal and Dhruv Bhandarkar Pai and Andrey Gromov and Daniel A. Roberts and Diyi Yang and David L. Donoho and Sanmi Koyejo},\n  booktitle = {Proceedings of the First Conference on Language Modeling (COLM)},\n  year      = {2024},\n  eprint    = {2404.01413},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@inproceedings{Gillman2024,\n  title     = {Self-Correcting Self-Consuming Loops for Generative Model Training},\n  author    = {Nate Gillman and Michael Freeman and Daksh Aggarwal and Chia-Hong Hsu and Calvin Luo and Yonglong Tian and Chen Sun},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  pages     = {15646--15677},\n  year      = {2024},\n  eprint    = {2402.07087},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@article{Gu2026,\n  title   = {{SIGMA}: Scalable Spectral Insights for {LLM} Model Collapse},\n  author  = {Yi Gu and Lingyou Pang and Xiangkun Ye and Tianyu Wang and Jianyu Lin and Carey E. Priebe and Alexander Aue},\n  year    = {2026},\n  eprint  = {2601.03385},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@article{Kalra2026,\n  title   = {A Scalable Measure of Loss Landscape Curvature for Analyzing the Training Dynamics of {LLMs}},\n  author  = {Dayal Singh Kalra and Jean-Christophe Gagnon-Audet and Andrey Gromov and Ishita Mediratta and Kelvin Niu and Alexander H. Miller and Michael Shvartsman},\n  year    = {2026},\n  eprint  = {2601.16979},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@article{Kalinowski2026,\n  title   = {Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index},\n  author  = {Alexander Kalinowski},\n  year    = {2026},\n  eprint  = {2604.26984},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@inproceedings{Kazdan2024,\n  title     = {Collapse or Thrive? {Perils} and Promises of Synthetic Data in a Self-Generating World},\n  author    = {Joshua Kazdan and Rylan Schaeffer and Apratim Dey and Matthias Gerstgrasser and Rafael Rafailov and David L. Donoho and Sanmi Koyejo},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  pages     = {29469--29494},\n  year      = {2025},\n  eprint    = {2410.16713},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@inproceedings{Kirchenbauer2023,\n  title     = {A Watermark for Large Language Models},\n  author    = {John Kirchenbauer and Jonas Geiping and Yuxin Wen and Jonathan Katz and Ian Miers and Tom Goldstein},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  pages     = {17061--17084},\n  year      = {2023},\n  eprint    = {2301.10226},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.CL}\n}\n\n@article{Li2025_gradient,\n  title   = {How Instruction and Reasoning Data shape Post-Training: Data Quality through the Lens of Layer-wise Gradients},\n  author  = {Ming Li and Yanhong Li and Ziyue Li and Tianyi Zhou},\n  year    = {2025},\n  eprint  = {2504.10766},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.CL}\n}\n\n% NOTE: Citation key says \"Liehr2025\" but verified authors are Jha and Reagen.\n% The \\citet{Liehr2025} calls in the paper will render the correct author names from this entry.\n% Consider renaming the key to Jha2025 and updating the .tex files.\n@inproceedings{Liehr2025,\n  title     = {Spectral Scaling Laws in Language Models: How Effectively Do Feed-Forward Networks Use Their Latent Space?},\n  author    = {Nandan Kumar Jha and Brandon Reagen},\n  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year      = {2025},\n  eprint    = {2510.00537},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.CL}\n}\n\n@article{Liu2026_lifecycle,\n  title   = {The Spectral Lifecycle of Transformer Training: Transient Compression Waves, Persistent Spectral Gradients, and the {Q/K--V} Asymmetry},\n  author  = {Yi Liu},\n  year    = {2026},\n  eprint  = {2604.22778},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@article{Martin2021,\n  title   = {Predicting Trends in the Quality of State-of-the-Art Neural Networks without Access to Training or Testing Data},\n  author  = {Charles H. Martin and Tongsu Serena Peng and Michael W. Mahoney},\n  journal = {Nature Communications},\n  volume  = {12},\n  pages   = {4122},\n  year    = {2021},\n  eprint  = {2002.06716},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@inproceedings{merity2017pointer,\n  title     = {Pointer Sentinel Mixture Models},\n  author    = {Stephen Merity and Caiming Xiong and James Bradbury and Richard Socher},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year      = {2017},\n  eprint    = {1609.07843},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.CL}\n}\n\n@inproceedings{Mitchell2023,\n  title     = {{DetectGPT}: Zero-Shot Machine-Generated Text Detection using Probability Curvature},\n  author    = {Eric Mitchell and Yoonho Lee and Alexander Khazatsky and Christopher D. Manning and Chelsea Finn},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  pages     = {24950--24962},\n  year      = {2023},\n  eprint    = {2301.11305},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.CL}\n}\n\n@inproceedings{Penedo2024,\n  title     = {The {FineWeb} Datasets: Decanting the Web for the Finest Text Data at Scale},\n  author    = {Guilherme Penedo and Hynek Kydlicek and Loubna Ben Allal and Anton Lozhkov and Margaret Mitchell and Colin Raffel and Leandro von Werra and Thomas Wolf},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS), Datasets and Benchmarks Track},\n  year      = {2024},\n  eprint    = {2406.17557},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.CL}\n}\n\n@inproceedings{Pennington2017,\n  title     = {Nonlinear Random Matrix Theory for Deep Learning},\n  author    = {Jeffrey Pennington and Pratik Worah},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  pages     = {2637--2646},\n  year      = {2017}\n}\n\n@article{Qiu2025,\n  title   = {Spectral Alignment as Predictor of Loss Explosion in Neural Network Training},\n  author  = {Haiquan Qiu and You Wu and Yingjie Tan and Yaqing Wang and Quanming Yao},\n  year    = {2025},\n  eprint  = {2510.04202},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@inproceedings{Sander2024,\n  title     = {Watermarking Makes Language Models Radioactive},\n  author    = {Tom Sander and Pierre Fernandez and Alain Durmus and Matthijs Douze and Teddy Furon},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2024},\n  eprint    = {2402.14904},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.CL}\n}\n\n@inproceedings{Sanyal2020,\n  title     = {Stable Rank Normalization for Improved Generalization in Neural Networks and {GANs}},\n  author    = {Amartya Sanyal and Philip H. S. Torr and Puneet K. Dokania},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year      = {2020},\n  eprint    = {1906.04659},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@article{Schaeffer2025,\n  title   = {Position: Model Collapse Does Not Mean What You Think},\n  author  = {Rylan Schaeffer and Joshua Kazdan and Alvan Caleb Arulandu and Sanmi Koyejo},\n  year    = {2025},\n  eprint  = {2503.03150},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@article{Seddik2024,\n  title   = {How Bad is Training on Synthetic Data? {A} Statistical Analysis of Language Model Collapse},\n  author  = {Mohamed El Amine Seddik and Suei-Wen Chen and Soufiane Hayou and Pierre Youssef and Merouane Debbah},\n  year    = {2024},\n  eprint  = {2404.05090},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.CL}\n}\n\n@inproceedings{Shi2024_mink,\n  title     = {Detecting Pretraining Data from Large Language Models},\n  author    = {Weijia Shi and Anirudh Ajith and Mengzhou Xia and Yangsibo Huang and Daogao Liu and Terra Blevins and Danqi Chen and Luke Zettlemoyer},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year      = {2024},\n  eprint    = {2310.16789},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.CL}\n}\n\n@inproceedings{Shi2025_neurips,\n  title     = {A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective},\n  author    = {Lianghe Shi and Meng Wu and Huijie Zhang and Zekai Zhang and Molei Tao and Qing Qu},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2025},\n  note      = {Spotlight},\n  eprint    = {2509.16499},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@article{Shumailov2024,\n  title   = {{AI} Models Collapse When Trained on Recursively Generated Data},\n  author  = {Ilia Shumailov and Zakhar Shumaylov and Yiren Zhao and Nicolas Papernot and Ross Anderson and Yarin Gal},\n  journal = {Nature},\n  volume  = {631},\n  pages   = {755--759},\n  year    = {2024},\n  eprint  = {2305.17493},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n% Alias for Shumailov2024 — same paper, different citation key used in method.tex\n@article{shumailov2024ai,\n  title   = {{AI} Models Collapse When Trained on Recursively Generated Data},\n  author  = {Ilia Shumailov and Zakhar Shumaylov and Yiren Zhao and Nicolas Papernot and Ross Anderson and Yarin Gal},\n  journal = {Nature},\n  volume  = {631},\n  pages   = {755--759},\n  year    = {2024},\n  eprint  = {2305.17493},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@inproceedings{Staats2024,\n  title     = {Small Singular Values Matter: A Random Matrix Analysis of Transformer Models},\n  author    = {Max Staats and Matthias Thamm and Bernd Rosenow},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2025},\n  eprint    = {2410.17770},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@article{Wang2025_scaling,\n  title   = {Data Value in the Age of Scaling: Understanding {LLM} Scaling Dynamics Under Real-Synthetic Data Mixtures},\n  author  = {Haohui Wang and Jingyuan Qi and Jianpeng Chen and Jun Wu and Lifu Huang and Lecheng Zheng and Kevin Choi and Balaji Veeramani and Edward Bowen and Alison Hu and Tyler Cody and Dawei Zhou},\n  year    = {2025},\n  eprint  = {2511.13640},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.CL}\n}\n\n% NOTE: Citation key says \"Wyss2024\" but verified authors are Gambetta et al.\n% The \\citet{Wyss2024} calls in the paper will render the correct author names from this entry.\n% Consider renaming the key to Gambetta2024 and updating the .tex files.\n@article{Wyss2024,\n  title   = {Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative {AI}},\n  author  = {Daniele Gambetta and Gizem Gezici and Fosca Giannotti and Dino Pedreschi and Alistair Knott and Luca Pappalardo},\n  year    = {2024},\n  eprint  = {2410.12341},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.CL}\n}\n\n@article{Xu2026,\n  title   = {Predicting {LLM} Compression Degradation from Spectral Statistics},\n  author  = {Mingxue Xu},\n  year    = {2026},\n  eprint  = {2604.18085},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@article{Yi2025,\n  title   = {Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence},\n  author  = {Bingji Yi and Qiyuan Liu and Yuwei Cheng and Haifeng Xu},\n  year    = {2025},\n  eprint  = {2510.16657},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@article{Yunis2024,\n  title   = {Approaching Deep Learning through the Spectral Dynamics of Weights},\n  author  = {David Yunis and Kumar Kshitij Patel and Samuel Wheeler and Pedro Savarese and Gal Vardi and Karen Livescu and Michael Maire and Matthew R. Walter},\n  year    = {2024},\n  eprint  = {2408.11804},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@inproceedings{zellers2019hellaswag,\n  title     = {{HellaSwag}: Can a Machine Really Finish Your Sentence?},\n  author    = {Rowan Zellers and Ari Holtzman and Yonatan Bisk and Ali Farhadi and Yejin Choi},\n  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year      = {2019},\n  eprint    = {1905.07830},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.CL}\n}\n\n@article{Zhang2026,\n  title   = {The {LLM} Data Auditor: A Metric-oriented Survey on Quality and Trustworthiness in Evaluating Synthetic Data},\n  author  = {Kaituo Zhang and Mingzhi Hu and Hoang Anh Duy Le and Fariha Kabir Torsha and Zhimeng Jiang and Minh Khai Bui and Chia-Yuan Chang and Yu-Neng Chuang and Zhen Xiong and Ying Lin and Guanchu Wang and Na Zou},\n  year    = {2026},\n  eprint  = {2601.17717},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.CL}\n}\n\n@article{Zibakhsh2025,\n  title   = {{ForTIFAI}: Fending Off Recursive Training Induced Failure for {AI} Model Collapse},\n  author  = {Soheil Zibakhsh Shabgahi and Pedram Aghazadeh and Azalia Mirhoseini and Farinaz Koushanfar},\n  year    = {2025},\n  eprint  = {2509.08972},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc7ded1c-763c-4033-aaf7-b1a42880cedd",
  "isSidechain": false,
  "requestId": "req_011Cb3YyhQnGw8wkFz4AP2Ao",
  "type": "assistant",
  "uuid": "0b96f507-fc66-452d-b1a7-281b083eb89d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013yEMQVhyovX1yKGBjGjdYG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5827,
      "cache_read_input_tokens": 80666,
      "output_tokens": 6765,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5827,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6765,
          "cache_read_input_tokens": 80666,
          "cache_creation_input_tokens": 5827,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5827
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

_source line 79 · 2026-05-15T02:20:02.295Z_

<details><summary>↩ Tool result · `toolu_01WaGu9qdJ7sd1uDHHeJqX97`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b96f507-fc66-452d-b1a7-281b083eb89d",
  "isSidechain": false,
  "promptId": "a7003b6e-3a25-4888-837a-59f1925bbd90",
  "type": "user",
  "uuid": "0cc80816-bf64-4c32-a714-18dbc9dd5c20",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/references.bib",
    "content": "% references.bib — collapse_severity_monitor\n% Auto-compiled from paper sections: abstract, introduction, related_work, method, competitor_comparison\n% 44 citation keys, sorted alphabetically\n% Generated: 2026-05-15\n\n@inproceedings{AlphaPruning2024,\n  title     = {{AlphaPruning}: Using Heavy-Tailed Self Regularization Theory for Improved Layer-wise Pruning of Large Language Models},\n  author    = {Haiquan Lu and Yefan Zhou and Shiwei Liu and Zhangyang Wang and Michael W. Mahoney and Yaoqing Yang},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2024},\n  eprint    = {2410.10912},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@inproceedings{Alemohammad2024,\n  title     = {Self-Consuming Generative Models Go {MAD}},\n  author    = {Sina Alemohammad and Josue Casco-Rodriguez and Lorenzo Luzi and Ahmed Imtiaz Humayun and Hossein Babaei and Daniel LeJeune and Ali Siahkoohi and Richard G. Baraniuk},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year      = {2024},\n  eprint    = {2307.01850},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@article{Bakshi2026,\n  title   = {From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources},\n  author  = {Soham Bakshi and Sunrit Chakraborty},\n  year    = {2026},\n  eprint  = {2602.10531},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@inproceedings{Chen2024_dse,\n  title     = {Assessing Neural Network Representations During Training Using Noise-Resilient Diffusion Spectral Entropy},\n  author    = {Danqi Liao and Chen Liu and Benjamin W. Christensen and Alexander Tong and Guillaume Huguet and Guy Wolf and Maximilian Nickel and Ian Adelstein and Smita Krishnaswamy},\n  booktitle = {Proceedings of the 58th Annual Conference on Information Sciences and Systems (CISS)},\n  year      = {2024},\n  publisher = {IEEE},\n  eprint    = {2312.04823},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@article{Dathathri2024,\n  title   = {Scalable Watermarking for Identifying Large Language Model Outputs},\n  author  = {Sumanth Dathathri and Abigail See and Sumedh Ghaisas and Po-Sen Huang and Rob McAdam and Johannes Welbl and Vandana Bachani and Alex Kaskasoli and Robert Stanforth and Tatiana Matejovicova and Jamie Hayes and Nidhi Vyas and Majd Al Merey and Jonah Brown-Cohen and Rudy Bunel and Borja Balle and Taylan Cemgil and Zahra Ahmed and Kitty Stacpoole and Ilia Shumailov and Ciprian Baetu and Sven Gowal and Demis Hassabis and Pushmeet Kohli},\n  journal = {Nature},\n  volume  = {634},\n  pages   = {818--823},\n  year    = {2024}\n}\n\n@inproceedings{dettmers2023qlora,\n  title     = {{QLoRA}: Efficient Finetuning of Quantized Large Language Models},\n  author    = {Tim Dettmers and Artidoro Pagnoni and Ari Holtzman and Luke Zettlemoyer},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2023},\n  eprint    = {2305.14314},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@inproceedings{Dohmatob2024_tails,\n  title     = {A Tale of Tails: Model Collapse as a Change of Scaling Laws},\n  author    = {Elvis Dohmatob and Yunzhen Feng and Pu Yang and Francois Charton and Julia Kempe},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  pages     = {11165--11197},\n  year      = {2024},\n  eprint    = {2402.07043},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@inproceedings{Dohmatob2025,\n  title     = {Strong Model Collapse},\n  author    = {Elvis Dohmatob and Yunzhen Feng and Arjun Subramonian and Julia Kempe},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year      = {2025},\n  note      = {Spotlight},\n  eprint    = {2410.04840},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@article{Elgaar2026,\n  title   = {Curriculum Learning for {LLM} Pretraining: An Analysis of Learning Dynamics},\n  author  = {Mohamed Elgaar and Hadi Amiri},\n  year    = {2026},\n  eprint  = {2601.21698},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.CL}\n}\n\n@inproceedings{Feng2025,\n  title     = {Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification},\n  author    = {Yunzhen Feng and Elvis Dohmatob and Pu Yang and Francois Charton and Julia Kempe},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year      = {2025},\n  eprint    = {2406.07515},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@inproceedings{Fu2024_icml,\n  title     = {Towards Theoretical Understandings of Self-Consuming Generative Models},\n  author    = {Shi Fu and Sen Zhang and Yingjie Wang and Xinmei Tian and Dacheng Tao},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  year      = {2024},\n  eprint    = {2402.11778},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@inproceedings{Gerstgrasser2024,\n  title     = {Is Model Collapse Inevitable? {Breaking} the Curse of Recursion by Accumulating Real and Synthetic Data},\n  author    = {Matthias Gerstgrasser and Rylan Schaeffer and Apratim Dey and Rafael Rafailov and Henry Sleight and John Hughes and Tomasz Korbak and Rajashree Agrawal and Dhruv Bhandarkar Pai and Andrey Gromov and Daniel A. Roberts and Diyi Yang and David L. Donoho and Sanmi Koyejo},\n  booktitle = {Proceedings of the First Conference on Language Modeling (COLM)},\n  year      = {2024},\n  eprint    = {2404.01413},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@inproceedings{Gillman2024,\n  title     = {Self-Correcting Self-Consuming Loops for Generative Model Training},\n  author    = {Nate Gillman and Michael Freeman and Daksh Aggarwal and Chia-Hong Hsu and Calvin Luo and Yonglong Tian and Chen Sun},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  pages     = {15646--15677},\n  year      = {2024},\n  eprint    = {2402.07087},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@article{Gu2026,\n  title   = {{SIGMA}: Scalable Spectral Insights for {LLM} Model Collapse},\n  author  = {Yi Gu and Lingyou Pang and Xiangkun Ye and Tianyu Wang and Jianyu Lin and Carey E. Priebe and Alexander Aue},\n  year    = {2026},\n  eprint  = {2601.03385},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@article{Kalra2026,\n  title   = {A Scalable Measure of Loss Landscape Curvature for Analyzing the Training Dynamics of {LLMs}},\n  author  = {Dayal Singh Kalra and Jean-Christophe Gagnon-Audet and Andrey Gromov and Ishita Mediratta and Kelvin Niu and Alexander H. Miller and Michael Shvartsman},\n  year    = {2026},\n  eprint  = {2601.16979},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@article{Kalinowski2026,\n  title   = {Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index},\n  author  = {Alexander Kalinowski},\n  year    = {2026},\n  eprint  = {2604.26984},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@inproceedings{Kazdan2024,\n  title     = {Collapse or Thrive? {Perils} and Promises of Synthetic Data in a Self-Generating World},\n  author    = {Joshua Kazdan and Rylan Schaeffer and Apratim Dey and Matthias Gerstgrasser and Rafael Rafailov and David L. Donoho and Sanmi Koyejo},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  pages     = {29469--29494},\n  year      = {2025},\n  eprint    = {2410.16713},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@inproceedings{Kirchenbauer2023,\n  title     = {A Watermark for Large Language Models},\n  author    = {John Kirchenbauer and Jonas Geiping and Yuxin Wen and Jonathan Katz and Ian Miers and Tom Goldstein},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  pages     = {17061--17084},\n  year      = {2023},\n  eprint    = {2301.10226},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.CL}\n}\n\n@article{Li2025_gradient,\n  title   = {How Instruction and Reasoning Data shape Post-Training: Data Quality through the Lens of Layer-wise Gradients},\n  author  = {Ming Li and Yanhong Li and Ziyue Li and Tianyi Zhou},\n  year    = {2025},\n  eprint  = {2504.10766},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.CL}\n}\n\n% NOTE: Citation key says \"Liehr2025\" but verified authors are Jha and Reagen.\n% The \\citet{Liehr2025} calls in the paper will render the correct author names from this entry.\n% Consider renaming the key to Jha2025 and updating the .tex files.\n@inproceedings{Liehr2025,\n  title     = {Spectral Scaling Laws in Language Models: How Effectively Do Feed-Forward Networks Use Their Latent Space?},\n  author    = {Nandan Kumar Jha and Brandon Reagen},\n  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year      = {2025},\n  eprint    = {2510.00537},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.CL}\n}\n\n@article{Liu2026_lifecycle,\n  title   = {The Spectral Lifecycle of Transformer Training: Transient Compression Waves, Persistent Spectral Gradients, and the {Q/K--V} Asymmetry},\n  author  = {Yi Liu},\n  year    = {2026},\n  eprint  = {2604.22778},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@article{Martin2021,\n  title   = {Predicting Trends in the Quality of State-of-the-Art Neural Networks without Access to Training or Testing Data},\n  author  = {Charles H. Martin and Tongsu Serena Peng and Michael W. Mahoney},\n  journal = {Nature Communications},\n  volume  = {12},\n  pages   = {4122},\n  year    = {2021},\n  eprint  = {2002.06716},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@inproceedings{merity2017pointer,\n  title     = {Pointer Sentinel Mixture Models},\n  author    = {Stephen Merity and Caiming Xiong and James Bradbury and Richard Socher},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year      = {2017},\n  eprint    = {1609.07843},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.CL}\n}\n\n@inproceedings{Mitchell2023,\n  title     = {{DetectGPT}: Zero-Shot Machine-Generated Text Detection using Probability Curvature},\n  author    = {Eric Mitchell and Yoonho Lee and Alexander Khazatsky and Christopher D. Manning and Chelsea Finn},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  pages     = {24950--24962},\n  year      = {2023},\n  eprint    = {2301.11305},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.CL}\n}\n\n@inproceedings{Penedo2024,\n  title     = {The {FineWeb} Datasets: Decanting the Web for the Finest Text Data at Scale},\n  author    = {Guilherme Penedo and Hynek Kydlicek and Loubna Ben Allal and Anton Lozhkov and Margaret Mitchell and Colin Raffel and Leandro von Werra and Thomas Wolf},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS), Datasets and Benchmarks Track},\n  year      = {2024},\n  eprint    = {2406.17557},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.CL}\n}\n\n@inproceedings{Pennington2017,\n  title     = {Nonlinear Random Matrix Theory for Deep Learning},\n  author    = {Jeffrey Pennington and Pratik Worah},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  pages     = {2637--2646},\n  year      = {2017}\n}\n\n@article{Qiu2025,\n  title   = {Spectral Alignment as Predictor of Loss Explosion in Neural Network Training},\n  author  = {Haiquan Qiu and You Wu and Yingjie Tan and Yaqing Wang and Quanming Yao},\n  year    = {2025},\n  eprint  = {2510.04202},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@inproceedings{Sander2024,\n  title     = {Watermarking Makes Language Models Radioactive},\n  author    = {Tom Sander and Pierre Fernandez and Alain Durmus and Matthijs Douze and Teddy Furon},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2024},\n  eprint    = {2402.14904},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.CL}\n}\n\n@inproceedings{Sanyal2020,\n  title     = {Stable Rank Normalization for Improved Generalization in Neural Networks and {GANs}},\n  author    = {Amartya Sanyal and Philip H. S. Torr and Puneet K. Dokania},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year      = {2020},\n  eprint    = {1906.04659},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@article{Schaeffer2025,\n  title   = {Position: Model Collapse Does Not Mean What You Think},\n  author  = {Rylan Schaeffer and Joshua Kazdan and Alvan Caleb Arulandu and Sanmi Koyejo},\n  year    = {2025},\n  eprint  = {2503.03150},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@article{Seddik2024,\n  title   = {How Bad is Training on Synthetic Data? {A} Statistical Analysis of Language Model Collapse},\n  author  = {Mohamed El Amine Seddik and Suei-Wen Chen and Soufiane Hayou and Pierre Youssef and Merouane Debbah},\n  year    = {2024},\n  eprint  = {2404.05090},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.CL}\n}\n\n@inproceedings{Shi2024_mink,\n  title     = {Detecting Pretraining Data from Large Language Models},\n  author    = {Weijia Shi and Anirudh Ajith and Mengzhou Xia and Yangsibo Huang and Daogao Liu and Terra Blevins and Danqi Chen and Luke Zettlemoyer},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year      = {2024},\n  eprint    = {2310.16789},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.CL}\n}\n\n@inproceedings{Shi2025_neurips,\n  title     = {A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective},\n  author    = {Lianghe Shi and Meng Wu and Huijie Zhang and Zekai Zhang and Molei Tao and Qing Qu},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2025},\n  note      = {Spotlight},\n  eprint    = {2509.16499},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@article{Shumailov2024,\n  title   = {{AI} Models Collapse When Trained on Recursively Generated Data},\n  author  = {Ilia Shumailov and Zakhar Shumaylov and Yiren Zhao and Nicolas Papernot and Ross Anderson and Yarin Gal},\n  journal = {Nature},\n  volume  = {631},\n  pages   = {755--759},\n  year    = {2024},\n  eprint  = {2305.17493},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n% Alias for Shumailov2024 — same paper, different citation key used in method.tex\n@article{shumailov2024ai,\n  title   = {{AI} Models Collapse When Trained on Recursively Generated Data},\n  author  = {Ilia Shumailov and Zakhar Shumaylov and Yiren Zhao and Nicolas Papernot and Ross Anderson and Yarin Gal},\n  journal = {Nature},\n  volume  = {631},\n  pages   = {755--759},\n  year    = {2024},\n  eprint  = {2305.17493},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@inproceedings{Staats2024,\n  title     = {Small Singular Values Matter: A Random Matrix Analysis of Transformer Models},\n  author    = {Max Staats and Matthias Thamm and Bernd Rosenow},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2025},\n  eprint    = {2410.17770},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@article{Wang2025_scaling,\n  title   = {Data Value in the Age of Scaling: Understanding {LLM} Scaling Dynamics Under Real-Synthetic Data Mixtures},\n  author  = {Haohui Wang and Jingyuan Qi and Jianpeng Chen and Jun Wu and Lifu Huang and Lecheng Zheng and Kevin Choi and Balaji Veeramani and Edward Bowen and Alison Hu and Tyler Cody and Dawei Zhou},\n  year    = {2025},\n  eprint  = {2511.13640},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.CL}\n}\n\n% NOTE: Citation key says \"Wyss2024\" but verified authors are Gambetta et al.\n% The \\citet{Wyss2024} calls in the paper will render the correct author names from this entry.\n% Consider renaming the key to Gambetta2024 and updating the .tex files.\n@article{Wyss2024,\n  title   = {Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative {AI}},\n  author  = {Daniele Gambetta and Gizem Gezici and Fosca Giannotti and Dino Pedreschi and Alistair Knott and Luca Pappalardo},\n  year    = {2024},\n  eprint  = {2410.12341},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.CL}\n}\n\n@article{Xu2026,\n  title   = {Predicting {LLM} Compression Degradation from Spectral Statistics},\n  author  = {Mingxue Xu},\n  year    = {2026},\n  eprint  = {2604.18085},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@article{Yi2025,\n  title   = {Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence},\n  author  = {Bingji Yi and Qiyuan Liu and Yuwei Cheng and Haifeng Xu},\n  year    = {2025},\n  eprint  = {2510.16657},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@article{Yunis2024,\n  title   = {Approaching Deep Learning through the Spectral Dynamics of Weights},\n  author  = {David Yunis and Kumar Kshitij Patel and Samuel Wheeler and Pedro Savarese and Gal Vardi and Karen Livescu and Michael Maire and Matthew R. Walter},\n  year    = {2024},\n  eprint  = {2408.11804},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n\n@inproceedings{zellers2019hellaswag,\n  title     = {{HellaSwag}: Can a Machine Really Finish Your Sentence?},\n  author    = {Rowan Zellers and Ari Holtzman and Yonatan Bisk and Ali Farhadi and Yejin Choi},\n  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year      = {2019},\n  eprint    = {1905.07830},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.CL}\n}\n\n@article{Zhang2026,\n  title   = {The {LLM} Data Auditor: A Metric-oriented Survey on Quality and Trustworthiness in Evaluating Synthetic Data},\n  author  = {Kaituo Zhang and Mingzhi Hu and Hoang Anh Duy Le and Fariha Kabir Torsha and Zhimeng Jiang and Minh Khai Bui and Chia-Yuan Chang and Yu-Neng Chuang and Zhen Xiong and Ying Lin and Guanchu Wang and Na Zou},\n  year    = {2026},\n  eprint  = {2601.17717},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.CL}\n}\n\n@article{Zibakhsh2025,\n  title   = {{ForTIFAI}: Fending Off Recursive Training Induced Failure for {AI} Model Collapse},\n  author  = {Soheil Zibakhsh Shabgahi and Pedram Aghazadeh and Azalia Mirhoseini and Farinaz Koushanfar},\n  year    = {2025},\n  eprint  = {2509.08972},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.LG}\n}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "0b96f507-fc66-452d-b1a7-281b083eb89d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 80_

```json
{
  "type": "last-prompt",
  "leafUuid": "0cc80816-bf64-4c32-a714-18dbc9dd5c20",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b"
}
```

---

### Runtime record

_source line 81_

```json
{
  "type": "ai-title",
  "aiTitle": "Compile bibliography file for paper citations",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b"
}
```

---

### Assistant

_source line 82 · 2026-05-15T02:20:05.367Z_

Now let me verify completeness — extract all citation keys from the tex files and cross-check against the bib.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cc80816-bf64-4c32-a714-18dbc9dd5c20",
  "isSidechain": false,
  "requestId": "req_011Cb3Z8E4yxDZuwzzqXMWwC",
  "type": "assistant",
  "uuid": "e20a30e6-1774-42be-bc79-a61626cec753",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DxykKs9gqnyTsoYUtvSG8o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6816,
      "cache_read_input_tokens": 86493,
      "output_tokens": 199,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6816,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 199,
          "cache_read_input_tokens": 86493,
          "cache_creation_input_tokens": 6816,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6816
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

_source line 83 · 2026-05-15T02:20:07.736Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01MrUx2SAkc6KKuHvxANWQuh`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper && grep -ohP '\\\\cite[tp]?\\{[^}]+\\}' sections/*.tex tables/*.tex | sed 's/\\\\cite[tp]\\?{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u",
  "description": "Extract all unique citation keys from tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e20a30e6-1774-42be-bc79-a61626cec753",
  "isSidechain": false,
  "requestId": "req_011Cb3Z8E4yxDZuwzzqXMWwC",
  "type": "assistant",
  "uuid": "eeba5234-e9df-4357-bf39-c46aa7f3c66c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DxykKs9gqnyTsoYUtvSG8o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6816,
      "cache_read_input_tokens": 86493,
      "output_tokens": 199,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6816,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 199,
          "cache_read_input_tokens": 86493,
          "cache_creation_input_tokens": 6816,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6816
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

_source line 84 · 2026-05-15T02:20:07.827Z_

<details><summary>↩ Tool result · `toolu_01MrUx2SAkc6KKuHvxANWQuh`</summary>

```text
Alemohammad2024
AlphaPruning2024
Bakshi2026
Chen2024_dse
Dathathri2024
Dohmatob2024_tails
Dohmatob2025
Elgaar2026
Feng2025
Fu2024_icml
Gerstgrasser2024
Gillman2024
Gu2026
Kalinowski2026
Kalra2026
Kazdan2024
Kirchenbauer2023
Li2025_gradient
Liehr2025
Liu2026_lifecycle
Martin2021
Mitchell2023
Penedo2024
Pennington2017
Qiu2025
Sander2024
Sanyal2020
Schaeffer2025
Seddik2024
Shi2024_mink
Shi2025_neurips
Shumailov2024
Staats2024
Wang2025_scaling
Wyss2024
Xu2026
Yi2025
Yunis2024
Zhang2026
Zibakhsh2025
dettmers2023qlora
hu2022lora
merity2017pointer
shumailov2024ai
zellers2019hellaswag
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eeba5234-e9df-4357-bf39-c46aa7f3c66c",
  "isSidechain": false,
  "promptId": "a7003b6e-3a25-4888-837a-59f1925bbd90",
  "type": "user",
  "uuid": "e814d0e6-9f58-49f9-bf86-8625c3ad4c1c",
  "toolUseResult": {
    "stdout": "Alemohammad2024\nAlphaPruning2024\nBakshi2026\nChen2024_dse\nDathathri2024\nDohmatob2024_tails\nDohmatob2025\nElgaar2026\nFeng2025\nFu2024_icml\nGerstgrasser2024\nGillman2024\nGu2026\nKalinowski2026\nKalra2026\nKazdan2024\nKirchenbauer2023\nLi2025_gradient\nLiehr2025\nLiu2026_lifecycle\nMartin2021\nMitchell2023\nPenedo2024\nPennington2017\nQiu2025\nSander2024\nSanyal2020\nSchaeffer2025\nSeddik2024\nShi2024_mink\nShi2025_neurips\nShumailov2024\nStaats2024\nWang2025_scaling\nWyss2024\nXu2026\nYi2025\nYunis2024\nZhang2026\nZibakhsh2025\ndettmers2023qlora\nhu2022lora\nmerity2017pointer\nshumailov2024ai\nzellers2019hellaswag",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "eeba5234-e9df-4357-bf39-c46aa7f3c66c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 85 · 2026-05-15T02:20:13.802Z_

<details><summary>Logged reasoning block</summary>

```text
I see there's one key I missed: `hu2022lora`. Let me check where it's used - it wasn't in my extraction earlier. Let me grep for it.

Actually wait, I went through all the files carefully. Let me check again... Let me grep for `hu2022lora` specifically.

I need to add a BibTeX entry for `hu2022lora`. This is likely the LoRA paper: "LoRA: Low-Rank Adaptation of Large Language Models" by Edward J. Hu et al., ICLR 2022.


Let me add the entry now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e814d0e6-9f58-49f9-bf86-8625c3ad4c1c",
  "isSidechain": false,
  "requestId": "req_011Cb3Z8deK4tXnr8Pa9fedP",
  "type": "assistant",
  "uuid": "ff5f0a38-3102-4d61-810a-bc775b919ea5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L14QEPKAvVi1u1gbu2kRVA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 508,
      "cache_read_input_tokens": 93309,
      "output_tokens": 294,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 508,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 294,
          "cache_read_input_tokens": 93309,
          "cache_creation_input_tokens": 508,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 508
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

_source line 86 · 2026-05-15T02:20:14.255Z_

Missing one key: `hu2022lora`. Let me find where it's used and add it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff5f0a38-3102-4d61-810a-bc775b919ea5",
  "isSidechain": false,
  "requestId": "req_011Cb3Z8deK4tXnr8Pa9fedP",
  "type": "assistant",
  "uuid": "f50c4a8c-9e16-42ac-a2d6-15b8843321a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L14QEPKAvVi1u1gbu2kRVA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 508,
      "cache_read_input_tokens": 93309,
      "output_tokens": 294,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 508,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 294,
          "cache_read_input_tokens": 93309,
          "cache_creation_input_tokens": 508,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 508
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

_source line 87 · 2026-05-15T02:20:14.893Z_

<details open><summary>🔧 Tool call — Grep · `toolu_011BsesyDA2qXqmpjKX9djEF`</summary>

```json
{
  "pattern": "hu2022lora",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f50c4a8c-9e16-42ac-a2d6-15b8843321a8",
  "isSidechain": false,
  "requestId": "req_011Cb3Z8deK4tXnr8Pa9fedP",
  "type": "assistant",
  "uuid": "6e2eded1-bf3b-4c5c-8790-8686ff364145",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L14QEPKAvVi1u1gbu2kRVA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 508,
      "cache_read_input_tokens": 93309,
      "output_tokens": 294,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 508,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 294,
          "cache_read_input_tokens": 93309,
          "cache_creation_input_tokens": 508,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 508
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

_source line 88 · 2026-05-15T02:20:14.931Z_

<details><summary>↩ Tool result · `toolu_011BsesyDA2qXqmpjKX9djEF`</summary>

```text
sections/method.tex:122:First, gradients flow only through the low-rank adapter matrices $A \in \mathbb{R}^{d \times r}$ and $B \in \mathbb{R}^{r \times d}$ rather than the full weight matrix~\citep{hu2022lora}, so the gradient landscape is confined to a rank-$r$ subspace that can amplify or attenuate contamination-induced shifts in ways that do not mirror full-rank fine-tuning.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e2eded1-bf3b-4c5c-8790-8686ff364145",
  "isSidechain": false,
  "promptId": "a7003b6e-3a25-4888-837a-59f1925bbd90",
  "type": "user",
  "uuid": "65719ae1-ee31-400d-a083-330e24f2f34d",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "sections/method.tex:122:First, gradients flow only through the low-rank adapter matrices $A \\in \\mathbb{R}^{d \\times r}$ and $B \\in \\mathbb{R}^{r \\times d}$ rather than the full weight matrix~\\citep{hu2022lora}, so the gradient landscape is confined to a rank-$r$ subspace that can amplify or attenuate contamination-induced shifts in ways that do not mirror full-rank fine-tuning.",
    "numLines": 1
  },
  "sourceToolAssistantUUID": "6e2eded1-bf3b-4c5c-8790-8686ff364145",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 89 · 2026-05-15T02:20:14.933Z_

```json
{
  "parentUuid": "65719ae1-ee31-400d-a083-330e24f2f34d",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "fc2e4fc2-233f-4688-8b58-d7b3c0aad723",
  "timestamp": "2026-05-15T02:20:14.933Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 90 · 2026-05-15T02:20:18.587Z_

<details><summary>Logged reasoning block</summary>

```text
Found it - `hu2022lora` is used in method.tex line 122, which I must have missed earlier because I didn't read that far. This is the LoRA paper: "LoRA: Low-Rank Adaptation of Large Language Models" by Edward J. Hu et al., ICLR 2022.

Let me add this entry to the bib file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc2e4fc2-233f-4688-8b58-d7b3c0aad723",
  "isSidechain": false,
  "requestId": "req_011Cb3Z9APFZVqUthr9vC9QE",
  "type": "assistant",
  "uuid": "62d8a678-44a0-4500-af71-3ca49906b228",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011BMWgRTqQRWX9RSSFJEzK9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 525,
      "cache_read_input_tokens": 93817,
      "output_tokens": 249,
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
          "output_tokens": 249,
          "cache_read_input_tokens": 93817,
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

_source line 91 · 2026-05-15T02:20:19.038Z_

Found it in method.tex. That's the LoRA paper. Let me add it to the bib file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62d8a678-44a0-4500-af71-3ca49906b228",
  "isSidechain": false,
  "requestId": "req_011Cb3Z9APFZVqUthr9vC9QE",
  "type": "assistant",
  "uuid": "ced1ed3a-b165-4a25-bd70-0c3576339e1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011BMWgRTqQRWX9RSSFJEzK9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 525,
      "cache_read_input_tokens": 93817,
      "output_tokens": 249,
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
          "output_tokens": 249,
          "cache_read_input_tokens": 93817,
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

_source line 92 · 2026-05-15T02:20:19.854Z_

<details open><summary>🔧 Tool call — Read · `toolu_018K6nciEmfjaornHeft6bsA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/method.tex",
  "offset": 115,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ced1ed3a-b165-4a25-bd70-0c3576339e1d",
  "isSidechain": false,
  "requestId": "req_011Cb3Z9APFZVqUthr9vC9QE",
  "type": "assistant",
  "uuid": "db641971-4014-4a8c-8128-3fd48cc3d8e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011BMWgRTqQRWX9RSSFJEzK9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 525,
      "cache_read_input_tokens": 93817,
      "output_tokens": 249,
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
          "output_tokens": 249,
          "cache_read_input_tokens": 93817,
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

_source line 93 · 2026-05-15T02:20:19.859Z_

<details><summary>↩ Tool result · `toolu_018K6nciEmfjaornHeft6bsA`</summary>

```text
115	\subsubsection{Gradient Signal}
116	\label{sec:gradient}
117	
118	We log the L2 gradient norm $\|\nabla_\theta \mathcal{L}\|_2$ computed by the trainer before each optimizer step.
119	Gradient norm is a zero-cost byproduct of standard training and reflects optimization landscape curvature.
120	In our MVP experiments, gradient norm exhibits non-monotonic behavior with respect to contamination fraction under QLoRA, limiting its utility as a standalone severity monitor (Section~\ref{sec:results}).
121	We attribute this non-monotonicity to two interacting factors specific to QLoRA training.
122	First, gradients flow only through the low-rank adapter matrices $A \in \mathbb{R}^{d \times r}$ and $B \in \mathbb{R}^{r \times d}$ rather than the full weight matrix~\citep{hu2022lora}, so the gradient landscape is confined to a rank-$r$ subspace that can amplify or attenuate contamination-induced shifts in ways that do not mirror full-rank fine-tuning.
123	Second, the NF4 quantization of frozen base weights introduces discretization noise that propagates through the backward pass~\citep{dettmers2023qlora}, adding a stochastic component to the gradient norm that obscures the monotonic contamination signal visible in spectral and output metrics.
124	
125	\subsubsection{Downstream Signal}
126	\label{sec:downstream}
127	
128	We evaluate HellaSwag~\citep{zellers2019hellaswag} accuracy (4-choice commonsense reasoning, 1{,}000 samples) as a downstream task probe.
129	HellaSwag is computed at the end of each generation (not at every signal checkpoint, due to evaluation cost).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db641971-4014-4a8c-8128-3fd48cc3d8e7",
  "isSidechain": false,
  "promptId": "a7003b6e-3a25-4888-837a-59f1925bbd90",
  "type": "user",
  "uuid": "97778249-295c-4cec-8336-212bd10947fd",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/method.tex",
      "content": "\\subsubsection{Gradient Signal}\n\\label{sec:gradient}\n\nWe log the L2 gradient norm $\\|\\nabla_\\theta \\mathcal{L}\\|_2$ computed by the trainer before each optimizer step.\nGradient norm is a zero-cost byproduct of standard training and reflects optimization landscape curvature.\nIn our MVP experiments, gradient norm exhibits non-monotonic behavior with respect to contamination fraction under QLoRA, limiting its utility as a standalone severity monitor (Section~\\ref{sec:results}).\nWe attribute this non-monotonicity to two interacting factors specific to QLoRA training.\nFirst, gradients flow only through the low-rank adapter matrices $A \\in \\mathbb{R}^{d \\times r}$ and $B \\in \\mathbb{R}^{r \\times d}$ rather than the full weight matrix~\\citep{hu2022lora}, so the gradient landscape is confined to a rank-$r$ subspace that can amplify or attenuate contamination-induced shifts in ways that do not mirror full-rank fine-tuning.\nSecond, the NF4 quantization of frozen base weights introduces discretization noise that propagates through the backward pass~\\citep{dettmers2023qlora}, adding a stochastic component to the gradient norm that obscures the monotonic contamination signal visible in spectral and output metrics.\n\n\\subsubsection{Downstream Signal}\n\\label{sec:downstream}\n\nWe evaluate HellaSwag~\\citep{zellers2019hellaswag} accuracy (4-choice commonsense reasoning, 1{,}000 samples) as a downstream task probe.\nHellaSwag is computed at the end of each generation (not at every signal checkpoint, due to evaluation cost).",
      "numLines": 15,
      "startLine": 115,
      "totalLines": 183
    }
  },
  "sourceToolAssistantUUID": "db641971-4014-4a8c-8128-3fd48cc3d8e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-15T02:20:25.379Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01BwVRKvffNVTaG4gJzRqR8E`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/references.bib",
  "old_string": "@article{Kalra2026,",
  "new_string": "@inproceedings{hu2022lora,\n  title     = {{LoRA}: Low-Rank Adaptation of Large Language Models},\n  author    = {Edward J. Hu and Yelong Shen and Phillip Wallis and Zeyuan Allen-Zhu and Yuanzhi Li and Shean Wang and Lu Wang and Weizhu Chen},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year      = {2022},\n  eprint    = {2106.09685},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.CL}\n}\n\n@article{Kalra2026,"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97778249-295c-4cec-8336-212bd10947fd",
  "isSidechain": false,
  "requestId": "req_011Cb3Z9XLKs1ER1XsFhGGKZ",
  "type": "assistant",
  "uuid": "ad363568-6c0d-447f-a184-0f2c32964c06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019m37EDkJm2JPuqPqKZxumX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 705,
      "cache_read_input_tokens": 94342,
      "output_tokens": 300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 705,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 300,
          "cache_read_input_tokens": 94342,
          "cache_creation_input_tokens": 705,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 705
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

_source line 95 · 2026-05-15T02:20:25.398Z_

<details><summary>↩ Tool result · `toolu_01BwVRKvffNVTaG4gJzRqR8E`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad363568-6c0d-447f-a184-0f2c32964c06",
  "isSidechain": false,
  "promptId": "a7003b6e-3a25-4888-837a-59f1925bbd90",
  "type": "user",
  "uuid": "10d4002e-0fe2-4757-899c-1457fa94cc61",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/references.bib",
    "oldString": "@article{Kalra2026,",
    "newString": "@inproceedings{hu2022lora,\n  title     = {{LoRA}: Low-Rank Adaptation of Large Language Models},\n  author    = {Edward J. Hu and Yelong Shen and Phillip Wallis and Zeyuan Allen-Zhu and Yuanzhi Li and Shean Wang and Lu Wang and Weizhu Chen},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year      = {2022},\n  eprint    = {2106.09685},\n  archivePrefix = {arXiv},\n  primaryClass  = {cs.CL}\n}\n\n@article{Kalra2026,",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 143,
        "oldLines": 6,
        "newStart": 143,
        "newLines": 16,
        "lines": [
          "   primaryClass  = {cs.LG}",
          " }",
          " ",
          "+@inproceedings{hu2022lora,",
          "+  title     = {{LoRA}: Low-Rank Adaptation of Large Language Models},",
          "+  author    = {Edward J. Hu and Yelong Shen and Phillip Wallis and Zeyuan Allen-Zhu and Yuanzhi Li and Shean Wang and Lu Wang and Weizhu Chen},",
          "+  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},",
          "+  year      = {2022},",
          "+  eprint    = {2106.09685},",
          "+  archivePrefix = {arXiv},",
          "+  primaryClass  = {cs.CL}",
          "+}",
          "+",
          " @article{Kalra2026,",
          "   title   = {A Scalable Measure of Loss Landscape Curvature for Analyzing the Training Dynamics of {LLMs}},",
          "   author  = {Dayal Singh Kalra and Jean-Christophe Gagnon-Audet and Andrey Gromov and Ishita Mediratta and Kelvin Niu and Alexander H. Miller and Michael Shvartsman},"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "ad363568-6c0d-447f-a184-0f2c32964c06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 96 · 2026-05-15T02:20:28.665Z_

Now verify all keys are covered.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10d4002e-0fe2-4757-899c-1457fa94cc61",
  "isSidechain": false,
  "requestId": "req_011Cb3Z9vpx6migTV3scEYft",
  "type": "assistant",
  "uuid": "138c8dba-2dd5-48a3-b1c3-6ddde73fbfdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BxizN7FtT6xca5AJGjPDxv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 371,
      "cache_read_input_tokens": 95047,
      "output_tokens": 383,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 371,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 383,
          "cache_read_input_tokens": 95047,
          "cache_creation_input_tokens": 371,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 371
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

_source line 97 · 2026-05-15T02:20:33.524Z_

<details open><summary>🔧 Tool call — Bash · `toolu_018pZLkRybKdkxKRFaGVmEPi`</summary>

```json
{
  "command": "TEX_KEYS=$(grep -ohP '\\\\cite[tp]?\\{[^}]+\\}' sections/*.tex tables/*.tex | sed 's/\\\\cite[tp]\\?{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u) && BIB_KEYS=$(grep -oP '^@\\w+\\{(\\S+),' references.bib | sed 's/^@\\w\\+{//;s/,$//' | sort -u) && echo \"=== TEX keys: $(echo \"$TEX_KEYS\" | wc -l) ===\" && echo \"=== BIB keys: $(echo \"$BIB_KEYS\" | wc -l) ===\" && echo \"\" && echo \"=== Missing from BIB ===\" && comm -23 <(echo \"$TEX_KEYS\") <(echo \"$BIB_KEYS\") && echo \"\" && echo \"=== Extra in BIB (unused) ===\" && comm -13 <(echo \"$TEX_KEYS\") <(echo \"$BIB_KEYS\")",
  "description": "Cross-check tex citation keys against bib entries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "138c8dba-2dd5-48a3-b1c3-6ddde73fbfdc",
  "isSidechain": false,
  "requestId": "req_011Cb3Z9vpx6migTV3scEYft",
  "type": "assistant",
  "uuid": "748d2832-ee69-4e00-aa81-ebe58e2e401a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BxizN7FtT6xca5AJGjPDxv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 371,
      "cache_read_input_tokens": 95047,
      "output_tokens": 383,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 371,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 383,
          "cache_read_input_tokens": 95047,
          "cache_creation_input_tokens": 371,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 371
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

_source line 98 · 2026-05-15T02:20:33.635Z_

<details><summary>↩ Tool result · `toolu_018pZLkRybKdkxKRFaGVmEPi`</summary>

```text
=== TEX keys: 45 ===
=== BIB keys: 45 ===

=== Missing from BIB ===

=== Extra in BIB (unused) ===
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "748d2832-ee69-4e00-aa81-ebe58e2e401a",
  "isSidechain": false,
  "promptId": "a7003b6e-3a25-4888-837a-59f1925bbd90",
  "type": "user",
  "uuid": "5dc94793-7d27-4033-b4c0-7d85fe589f1c",
  "toolUseResult": {
    "stdout": "=== TEX keys: 45 ===\n=== BIB keys: 45 ===\n\n=== Missing from BIB ===\n\n=== Extra in BIB (unused) ===",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "748d2832-ee69-4e00-aa81-ebe58e2e401a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 99 · 2026-05-15T02:20:44.829Z_

All 45 citation keys matched. Summary:

**45 citation keys** extracted from 5 tex files, all with corresponding BibTeX entries in `paper/references.bib`.

**Entry breakdown:**
- 20 `@inproceedings` (ICML, ICLR, NeurIPS, ACL, EMNLP, COLM, CISS)
- 22 `@article` (Nature, Nature Comms, arXiv preprints)
- 3 entries are arXiv-only without venue (Gu2026, Kalinowski2026, etc.)

**Discrepancies flagged (require tex updates):**
- **`Liehr2025`** — actual authors are Jha & Reagen, not Liehr. `\citet{Liehr2025}` will render as "Jha and Reagen (2025)". Consider renaming key to `Jha2025`.
- **`Wyss2024`** — actual authors are Gambetta et al., not Wyss. `\citet{Wyss2024}` will render as "Gambetta et al. (2024)". Consider renaming key to `Gambetta2024`.
- **`shumailov2024ai`** — duplicate of `Shumailov2024` (same Nature paper). Consider unifying to one key.
- **`Kazdan2024`** — key says 2024 but published at ICML 2025. Minor cosmetic issue.
- **`Staats2024`** — key says 2024 but published at NeurIPS 2025. Minor cosmetic issue.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5dc94793-7d27-4033-b4c0-7d85fe589f1c",
  "isSidechain": false,
  "requestId": "req_011Cb3ZAXxZkot2Es9CVgnoP",
  "type": "assistant",
  "uuid": "71f50833-ce27-4dca-9cb0-b96ef53cd880",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LdhyErHWgQ2CHNX5q36uF1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 410,
      "cache_read_input_tokens": 95418,
      "output_tokens": 398,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 410,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 398,
          "cache_read_input_tokens": 95418,
          "cache_creation_input_tokens": 410,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 410
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

_source line 100_

```json
{
  "type": "last-prompt",
  "leafUuid": "71f50833-ce27-4dca-9cb0-b96ef53cd880",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b"
}
```

---

### Runtime record

_source line 101_

```json
{
  "type": "ai-title",
  "aiTitle": "Compile bibliography file for paper citations",
  "sessionId": "2878417b-8f77-4e7b-b95b-31a32289cc2b"
}
```

---
